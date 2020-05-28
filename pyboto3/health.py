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

def describe_affected_accounts_for_organization(eventArn=None, nextToken=None, maxResults=None):
    """
    Returns a list of accounts in the organization from AWS Organizations that are affected by the provided event.
    Before you can call this operation, you must first enable AWS Health to work with AWS Organizations. To do this, call the  EnableHealthServiceAccessForOrganization operation from your organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_affected_accounts_for_organization(
        eventArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type eventArn: string
    :param eventArn: [REQUIRED]\nThe unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456\n

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :rtype: dict

ReturnsResponse Syntax
{
    'affectedAccounts': [
        'string',
    ],
    'eventScopeCode': 'PUBLIC'|'ACCOUNT_SPECIFIC'|'NONE',
    'nextToken': 'string'
}


Response Structure

(dict) --

affectedAccounts (list) --
A JSON set of elements of the affected accounts.

(string) --


eventScopeCode (string) --

nextToken (string) --
If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.







Exceptions

Health.Client.exceptions.InvalidPaginationToken


    :return: {
        'affectedAccounts': [
            'string',
        ],
        'eventScopeCode': 'PUBLIC'|'ACCOUNT_SPECIFIC'|'NONE',
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_affected_entities(filter=None, locale=None, nextToken=None, maxResults=None):
    """
    Returns a list of entities that have been affected by the specified events, based on the specified filter criteria. Entities can refer to individual customer resources, groups of customer resources, or any other construct, depending on the AWS service. Events that have impact beyond that of the affected entities, or where the extent of impact is unknown, include at least one entity indicating this.
    At least one event ARN is required. Results are sorted by the lastUpdatedTime of the entity, starting with the most recent.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_affected_entities(
        filter={
            'eventArns': [
                'string',
            ],
            'entityArns': [
                'string',
            ],
            'entityValues': [
                'string',
            ],
            'lastUpdatedTimes': [
                {
                    'from': datetime(2015, 1, 1),
                    'to': datetime(2015, 1, 1)
                },
            ],
            'tags': [
                {
                    'string': 'string'
                },
            ],
            'statusCodes': [
                'IMPAIRED'|'UNIMPAIRED'|'UNKNOWN',
            ]
        },
        locale='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type filter: dict
    :param filter: [REQUIRED]\nValues to narrow the results returned. At least one event ARN is required.\n\neventArns (list) -- [REQUIRED]A list of event ARNs (unique identifiers). For example: 'arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456', 'arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101'\n\n(string) --\n\n\nentityArns (list) --A list of entity ARNs (unique identifiers).\n\n(string) --\n\n\nentityValues (list) --A list of IDs for affected entities.\n\n(string) --\n\n\nlastUpdatedTimes (list) --A list of the most recent dates and times that the entity was updated.\n\n(dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .\n\nfrom (datetime) --The starting date and time of a time range.\n\nto (datetime) --The ending date and time of a time range.\n\n\n\n\n\ntags (list) --A map of entity tags attached to the affected entity.\n\n(dict) --\n(string) --\n(string) --\n\n\n\n\n\n\nstatusCodes (list) --A list of entity status codes (IMPAIRED , UNIMPAIRED , or UNKNOWN ).\n\n(string) --\n\n\n\n

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :rtype: dict

ReturnsResponse Syntax
{
    'entities': [
        {
            'entityArn': 'string',
            'eventArn': 'string',
            'entityValue': 'string',
            'entityUrl': 'string',
            'awsAccountId': 'string',
            'lastUpdatedTime': datetime(2015, 1, 1),
            'statusCode': 'IMPAIRED'|'UNIMPAIRED'|'UNKNOWN',
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

entities (list) --
The entities that match the filter criteria.

(dict) --
Information about an entity that is affected by a Health event.

entityArn (string) --
The unique identifier for the entity. Format: arn:aws:health:*entity-region* :*aws-account* :entity/*entity-id* `` . Example: ``arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K

eventArn (string) --
The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

entityValue (string) --
The ID of the affected entity.

entityUrl (string) --
The URL of the affected entity.

awsAccountId (string) --
The 12-digit AWS account number that contains the affected entity.

lastUpdatedTime (datetime) --
The most recent time that the entity was updated.

statusCode (string) --
The most recent status of the entity affected by the event. The possible values are IMPAIRED , UNIMPAIRED , and UNKNOWN .

tags (dict) --
A map of entity tags attached to the affected entity.

(string) --
(string) --








nextToken (string) --
If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.







Exceptions

Health.Client.exceptions.InvalidPaginationToken
Health.Client.exceptions.UnsupportedLocale


    :return: {
        'entities': [
            {
                'entityArn': 'string',
                'eventArn': 'string',
                'entityValue': 'string',
                'entityUrl': 'string',
                'awsAccountId': 'string',
                'lastUpdatedTime': datetime(2015, 1, 1),
                'statusCode': 'IMPAIRED'|'UNIMPAIRED'|'UNKNOWN',
                'tags': {
                    'string': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_affected_entities_for_organization(organizationEntityFilters=None, locale=None, nextToken=None, maxResults=None):
    """
    Returns a list of entities that have been affected by one or more events for one or more accounts in your organization in AWS Organizations, based on the filter criteria. Entities can refer to individual customer resources, groups of customer resources, or any other construct, depending on the AWS service.
    At least one event ARN and account ID are required. Results are sorted by the lastUpdatedTime of the entity, starting with the most recent.
    Before you can call this operation, you must first enable AWS Health to work with AWS Organizations. To do this, call the  EnableHealthServiceAccessForOrganization operation from your organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_affected_entities_for_organization(
        organizationEntityFilters=[
            {
                'eventArn': 'string',
                'awsAccountId': 'string'
            },
        ],
        locale='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type organizationEntityFilters: list
    :param organizationEntityFilters: [REQUIRED]\nA JSON set of elements including the awsAccountId and the eventArn .\n\n(dict) --The values used to filter results from the DescribeEventDetailsForOrganization and DescribeAffectedEntitiesForOrganization operations.\n\neventArn (string) -- [REQUIRED]The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456\n\nawsAccountId (string) --The 12-digit AWS account numbers that contains the affected entities.\n\n\n\n\n

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :rtype: dict

ReturnsResponse Syntax
{
    'entities': [
        {
            'entityArn': 'string',
            'eventArn': 'string',
            'entityValue': 'string',
            'entityUrl': 'string',
            'awsAccountId': 'string',
            'lastUpdatedTime': datetime(2015, 1, 1),
            'statusCode': 'IMPAIRED'|'UNIMPAIRED'|'UNKNOWN',
            'tags': {
                'string': 'string'
            }
        },
    ],
    'failedSet': [
        {
            'awsAccountId': 'string',
            'eventArn': 'string',
            'errorName': 'string',
            'errorMessage': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

entities (list) --
A JSON set of elements including the awsAccountId and its entityArn , entityValue and its entityArn , lastUpdatedTime , statusCode , and tags .

(dict) --
Information about an entity that is affected by a Health event.

entityArn (string) --
The unique identifier for the entity. Format: arn:aws:health:*entity-region* :*aws-account* :entity/*entity-id* `` . Example: ``arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K

eventArn (string) --
The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

entityValue (string) --
The ID of the affected entity.

entityUrl (string) --
The URL of the affected entity.

awsAccountId (string) --
The 12-digit AWS account number that contains the affected entity.

lastUpdatedTime (datetime) --
The most recent time that the entity was updated.

statusCode (string) --
The most recent status of the entity affected by the event. The possible values are IMPAIRED , UNIMPAIRED , and UNKNOWN .

tags (dict) --
A map of entity tags attached to the affected entity.

(string) --
(string) --








failedSet (list) --
A JSON set of elements of the failed response, including the awsAccountId , errorMessage , errorName , and eventArn .

(dict) --
Error information returned when a  DescribeAffectedEntitiesForOrganization operation cannot find or process a specific entity.

awsAccountId (string) --
The 12-digit AWS account numbers that contains the affected entities.

eventArn (string) --
The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

errorName (string) --
The name of the error.

errorMessage (string) --
The unique identifier for the event type. The format is AWS_SERVICE_DESCRIPTION . For example, AWS_EC2_SYSTEM_MAINTENANCE_EVENT .





nextToken (string) --
If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.







Exceptions

Health.Client.exceptions.InvalidPaginationToken
Health.Client.exceptions.UnsupportedLocale


    :return: {
        'entities': [
            {
                'entityArn': 'string',
                'eventArn': 'string',
                'entityValue': 'string',
                'entityUrl': 'string',
                'awsAccountId': 'string',
                'lastUpdatedTime': datetime(2015, 1, 1),
                'statusCode': 'IMPAIRED'|'UNIMPAIRED'|'UNKNOWN',
                'tags': {
                    'string': 'string'
                }
            },
        ],
        'failedSet': [
            {
                'awsAccountId': 'string',
                'eventArn': 'string',
                'errorName': 'string',
                'errorMessage': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_entity_aggregates(eventArns=None):
    """
    Returns the number of entities that are affected by each of the specified events. If no events are specified, the counts of all affected entities are returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_entity_aggregates(
        eventArns=[
            'string',
        ]
    )
    
    
    :type eventArns: list
    :param eventArns: A list of event ARNs (unique identifiers). For example: 'arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456', 'arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101'\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'entityAggregates': [
        {
            'eventArn': 'string',
            'count': 123
        },
    ]
}


Response Structure

(dict) --
entityAggregates (list) --The number of entities that are affected by each of the specified events.

(dict) --The number of entities that are affected by one or more events. Returned by the  DescribeEntityAggregates operation.

eventArn (string) --The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

count (integer) --The number entities that match the criteria for the specified events.











    :return: {
        'entityAggregates': [
            {
                'eventArn': 'string',
                'count': 123
            },
        ]
    }
    
    
    """
    pass

def describe_event_aggregates(filter=None, aggregateField=None, maxResults=None, nextToken=None):
    """
    Returns the number of events of each event type (issue, scheduled change, and account notification). If no filter is specified, the counts of all events in each category are returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_aggregates(
        filter={
            'eventArns': [
                'string',
            ],
            'eventTypeCodes': [
                'string',
            ],
            'services': [
                'string',
            ],
            'regions': [
                'string',
            ],
            'availabilityZones': [
                'string',
            ],
            'startTimes': [
                {
                    'from': datetime(2015, 1, 1),
                    'to': datetime(2015, 1, 1)
                },
            ],
            'endTimes': [
                {
                    'from': datetime(2015, 1, 1),
                    'to': datetime(2015, 1, 1)
                },
            ],
            'lastUpdatedTimes': [
                {
                    'from': datetime(2015, 1, 1),
                    'to': datetime(2015, 1, 1)
                },
            ],
            'entityArns': [
                'string',
            ],
            'entityValues': [
                'string',
            ],
            'eventTypeCategories': [
                'issue'|'accountNotification'|'scheduledChange'|'investigation',
            ],
            'tags': [
                {
                    'string': 'string'
                },
            ],
            'eventStatusCodes': [
                'open'|'closed'|'upcoming',
            ]
        },
        aggregateField='eventTypeCategory',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type filter: dict
    :param filter: Values to narrow the results returned.\n\neventArns (list) --A list of event ARNs (unique identifiers). For example: 'arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456', 'arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101'\n\n(string) --\n\n\neventTypeCodes (list) --A list of unique identifiers for event types. For example, 'AWS_EC2_SYSTEM_MAINTENANCE_EVENT','AWS_RDS_MAINTENANCE_SCHEDULED'.\n\n(string) --\n\n\nservices (list) --The AWS services associated with the event. For example, EC2 , RDS .\n\n(string) --\n\n\nregions (list) --A list of AWS regions.\n\n(string) --\n\n\navailabilityZones (list) --A list of AWS availability zones.\n\n(string) --\n\n\nstartTimes (list) --A list of dates and times that the event began.\n\n(dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .\n\nfrom (datetime) --The starting date and time of a time range.\n\nto (datetime) --The ending date and time of a time range.\n\n\n\n\n\nendTimes (list) --A list of dates and times that the event ended.\n\n(dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .\n\nfrom (datetime) --The starting date and time of a time range.\n\nto (datetime) --The ending date and time of a time range.\n\n\n\n\n\nlastUpdatedTimes (list) --A list of dates and times that the event was last updated.\n\n(dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .\n\nfrom (datetime) --The starting date and time of a time range.\n\nto (datetime) --The ending date and time of a time range.\n\n\n\n\n\nentityArns (list) --A list of entity ARNs (unique identifiers).\n\n(string) --\n\n\nentityValues (list) --A list of entity identifiers, such as EC2 instance IDs (i-34ab692e ) or EBS volumes (vol-426ab23e ).\n\n(string) --\n\n\neventTypeCategories (list) --A list of event type category codes (issue , scheduledChange , or accountNotification ).\n\n(string) --\n\n\ntags (list) --A map of entity tags attached to the affected entity.\n\n(dict) --\n(string) --\n(string) --\n\n\n\n\n\n\neventStatusCodes (list) --A list of event status codes.\n\n(string) --\n\n\n\n

    :type aggregateField: string
    :param aggregateField: [REQUIRED]\nThe only currently supported value is eventTypeCategory .\n

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :rtype: dict

ReturnsResponse Syntax
{
    'eventAggregates': [
        {
            'aggregateValue': 'string',
            'count': 123
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

eventAggregates (list) --
The number of events in each category that meet the optional filter criteria.

(dict) --
The number of events of each issue type. Returned by the  DescribeEventAggregates operation.

aggregateValue (string) --
The issue type for the associated count.

count (integer) --
The number of events of the associated issue type.





nextToken (string) --
If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.







Exceptions

Health.Client.exceptions.InvalidPaginationToken


    :return: {
        'eventAggregates': [
            {
                'aggregateValue': 'string',
                'count': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Health.Client.exceptions.InvalidPaginationToken
    
    """
    pass

def describe_event_details(eventArns=None, locale=None):
    """
    Returns detailed information about one or more specified events. Information includes standard event data (region, service, and so on, as returned by  DescribeEvents ), a detailed event description, and possible additional metadata that depends upon the nature of the event. Affected entities are not included; to retrieve those, use the  DescribeAffectedEntities operation.
    If a specified event cannot be retrieved, an error message is returned for that event.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_details(
        eventArns=[
            'string',
        ],
        locale='string'
    )
    
    
    :type eventArns: list
    :param eventArns: [REQUIRED]\nA list of event ARNs (unique identifiers). For example: 'arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456', 'arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101'\n\n(string) --\n\n

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :rtype: dict

ReturnsResponse Syntax
{
    'successfulSet': [
        {
            'event': {
                'arn': 'string',
                'service': 'string',
                'eventTypeCode': 'string',
                'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange'|'investigation',
                'region': 'string',
                'availabilityZone': 'string',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'statusCode': 'open'|'closed'|'upcoming',
                'eventScopeCode': 'PUBLIC'|'ACCOUNT_SPECIFIC'|'NONE'
            },
            'eventDescription': {
                'latestDescription': 'string'
            },
            'eventMetadata': {
                'string': 'string'
            }
        },
    ],
    'failedSet': [
        {
            'eventArn': 'string',
            'errorName': 'string',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

successfulSet (list) --
Information about the events that could be retrieved.

(dict) --
Detailed information about an event. A combination of an  Event object, an  EventDescription object, and additional metadata about the event. Returned by the  DescribeEventDetails operation.

event (dict) --
Summary information about the event.

arn (string) --
The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

service (string) --
The AWS service that is affected by the event. For example, EC2 , RDS .

eventTypeCode (string) --
The unique identifier for the event type. The format is AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT .

eventTypeCategory (string) --
The category of the event. Possible values are issue , scheduledChange , and accountNotification .

region (string) --
The AWS region name of the event.

availabilityZone (string) --
The AWS Availability Zone of the event. For example, us-east-1a.

startTime (datetime) --
The date and time that the event began.

endTime (datetime) --
The date and time that the event ended.

lastUpdatedTime (datetime) --
The most recent date and time that the event was updated.

statusCode (string) --
The most recent status of the event. Possible values are open , closed , and upcoming .

eventScopeCode (string) --



eventDescription (dict) --
The most recent description of the event.

latestDescription (string) --
The most recent description of the event.



eventMetadata (dict) --
Additional metadata about the event.

(string) --
(string) --








failedSet (list) --
Error messages for any events that could not be retrieved.

(dict) --
Error information returned when a  DescribeEventDetails operation cannot find a specified event.

eventArn (string) --
The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

errorName (string) --
The name of the error.

errorMessage (string) --
A message that describes the error.











Exceptions

Health.Client.exceptions.UnsupportedLocale


    :return: {
        'successfulSet': [
            {
                'event': {
                    'arn': 'string',
                    'service': 'string',
                    'eventTypeCode': 'string',
                    'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange'|'investigation',
                    'region': 'string',
                    'availabilityZone': 'string',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'statusCode': 'open'|'closed'|'upcoming',
                    'eventScopeCode': 'PUBLIC'|'ACCOUNT_SPECIFIC'|'NONE'
                },
                'eventDescription': {
                    'latestDescription': 'string'
                },
                'eventMetadata': {
                    'string': 'string'
                }
            },
        ],
        'failedSet': [
            {
                'eventArn': 'string',
                'errorName': 'string',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_event_details_for_organization(organizationEventDetailFilters=None, locale=None):
    """
    Returns detailed information about one or more specified events for one or more accounts in your organization. Information includes standard event data (Region, service, and so on, as returned by  DescribeEventsForOrganization , a detailed event description, and possible additional metadata that depends upon the nature of the event. Affected entities are not included; to retrieve those, use the  DescribeAffectedEntitiesForOrganization operation.
    Before you can call this operation, you must first enable AWS Health to work with AWS Organizations. To do this, call the  EnableHealthServiceAccessForOrganization operation from your organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_details_for_organization(
        organizationEventDetailFilters=[
            {
                'eventArn': 'string',
                'awsAccountId': 'string'
            },
        ],
        locale='string'
    )
    
    
    :type organizationEventDetailFilters: list
    :param organizationEventDetailFilters: [REQUIRED]\nA set of JSON elements that includes the awsAccountId and the eventArn .\n\n(dict) --The values used to filter results from the DescribeEventDetailsForOrganization and DescribeAffectedEntitiesForOrganization operations.\n\neventArn (string) -- [REQUIRED]The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456\n\nawsAccountId (string) --The 12-digit AWS account numbers that contains the affected entities.\n\n\n\n\n

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :rtype: dict

ReturnsResponse Syntax
{
    'successfulSet': [
        {
            'awsAccountId': 'string',
            'event': {
                'arn': 'string',
                'service': 'string',
                'eventTypeCode': 'string',
                'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange'|'investigation',
                'region': 'string',
                'availabilityZone': 'string',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'statusCode': 'open'|'closed'|'upcoming',
                'eventScopeCode': 'PUBLIC'|'ACCOUNT_SPECIFIC'|'NONE'
            },
            'eventDescription': {
                'latestDescription': 'string'
            },
            'eventMetadata': {
                'string': 'string'
            }
        },
    ],
    'failedSet': [
        {
            'awsAccountId': 'string',
            'eventArn': 'string',
            'errorName': 'string',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

successfulSet (list) --
Information about the events that could be retrieved.

(dict) --
Detailed information about an event. A combination of an  Event object, an  EventDescription object, and additional metadata about the event. Returned by the  DescribeEventDetailsForOrganization operation.

awsAccountId (string) --
The 12-digit AWS account numbers that contains the affected entities.

event (dict) --
Summary information about an AWS Health event.

arn (string) --
The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

service (string) --
The AWS service that is affected by the event. For example, EC2 , RDS .

eventTypeCode (string) --
The unique identifier for the event type. The format is AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT .

eventTypeCategory (string) --
The category of the event. Possible values are issue , scheduledChange , and accountNotification .

region (string) --
The AWS region name of the event.

availabilityZone (string) --
The AWS Availability Zone of the event. For example, us-east-1a.

startTime (datetime) --
The date and time that the event began.

endTime (datetime) --
The date and time that the event ended.

lastUpdatedTime (datetime) --
The most recent date and time that the event was updated.

statusCode (string) --
The most recent status of the event. Possible values are open , closed , and upcoming .

eventScopeCode (string) --



eventDescription (dict) --
The detailed description of the event. Included in the information returned by the  DescribeEventDetails operation.

latestDescription (string) --
The most recent description of the event.



eventMetadata (dict) --
Additional metadata about the event.

(string) --
(string) --








failedSet (list) --
Error messages for any events that could not be retrieved.

(dict) --
Error information returned when a  DescribeEventDetailsForOrganization operation cannot find a specified event.

awsAccountId (string) --
Error information returned when a  DescribeEventDetailsForOrganization operation cannot find a specified event.

eventArn (string) --
The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

errorName (string) --
The name of the error.

errorMessage (string) --
A message that describes the error.











Exceptions

Health.Client.exceptions.UnsupportedLocale


    :return: {
        'successfulSet': [
            {
                'awsAccountId': 'string',
                'event': {
                    'arn': 'string',
                    'service': 'string',
                    'eventTypeCode': 'string',
                    'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange'|'investigation',
                    'region': 'string',
                    'availabilityZone': 'string',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'statusCode': 'open'|'closed'|'upcoming',
                    'eventScopeCode': 'PUBLIC'|'ACCOUNT_SPECIFIC'|'NONE'
                },
                'eventDescription': {
                    'latestDescription': 'string'
                },
                'eventMetadata': {
                    'string': 'string'
                }
            },
        ],
        'failedSet': [
            {
                'awsAccountId': 'string',
                'eventArn': 'string',
                'errorName': 'string',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_event_types(filter=None, locale=None, nextToken=None, maxResults=None):
    """
    Returns the event types that meet the specified filter criteria. If no filter criteria are specified, all event types are returned, in no particular order.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_types(
        filter={
            'eventTypeCodes': [
                'string',
            ],
            'services': [
                'string',
            ],
            'eventTypeCategories': [
                'issue'|'accountNotification'|'scheduledChange'|'investigation',
            ]
        },
        locale='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type filter: dict
    :param filter: Values to narrow the results returned.\n\neventTypeCodes (list) --A list of event type codes.\n\n(string) --\n\n\nservices (list) --The AWS services associated with the event. For example, EC2 , RDS .\n\n(string) --\n\n\neventTypeCategories (list) --A list of event type category codes (issue , scheduledChange , or accountNotification ).\n\n(string) --\n\n\n\n

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :rtype: dict

ReturnsResponse Syntax
{
    'eventTypes': [
        {
            'service': 'string',
            'code': 'string',
            'category': 'issue'|'accountNotification'|'scheduledChange'|'investigation'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

eventTypes (list) --
A list of event types that match the filter criteria. Event types have a category (issue , accountNotification , or scheduledChange ), a service (for example, EC2 , RDS , DATAPIPELINE , BILLING ), and a code (in the format AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT ).

(dict) --
Metadata about a type of event that is reported by AWS Health. Data consists of the category (for example, issue ), the service (for example, EC2 ), and the event type code (for example, AWS_EC2_SYSTEM_MAINTENANCE_EVENT ).

service (string) --
The AWS service that is affected by the event. For example, EC2 , RDS .

code (string) --
The unique identifier for the event type. The format is AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT .

category (string) --
A list of event type category codes (issue , scheduledChange , or accountNotification ).





nextToken (string) --
If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.







Exceptions

Health.Client.exceptions.InvalidPaginationToken
Health.Client.exceptions.UnsupportedLocale


    :return: {
        'eventTypes': [
            {
                'service': 'string',
                'code': 'string',
                'category': 'issue'|'accountNotification'|'scheduledChange'|'investigation'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Health.Client.exceptions.InvalidPaginationToken
    Health.Client.exceptions.UnsupportedLocale
    
    """
    pass

def describe_events(filter=None, nextToken=None, maxResults=None, locale=None):
    """
    Returns information about events that meet the specified filter criteria. Events are returned in a summary form and do not include the detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the  DescribeEventDetails and  DescribeAffectedEntities operations.
    If no filter criteria are specified, all events are returned. Results are sorted by lastModifiedTime , starting with the most recent.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_events(
        filter={
            'eventArns': [
                'string',
            ],
            'eventTypeCodes': [
                'string',
            ],
            'services': [
                'string',
            ],
            'regions': [
                'string',
            ],
            'availabilityZones': [
                'string',
            ],
            'startTimes': [
                {
                    'from': datetime(2015, 1, 1),
                    'to': datetime(2015, 1, 1)
                },
            ],
            'endTimes': [
                {
                    'from': datetime(2015, 1, 1),
                    'to': datetime(2015, 1, 1)
                },
            ],
            'lastUpdatedTimes': [
                {
                    'from': datetime(2015, 1, 1),
                    'to': datetime(2015, 1, 1)
                },
            ],
            'entityArns': [
                'string',
            ],
            'entityValues': [
                'string',
            ],
            'eventTypeCategories': [
                'issue'|'accountNotification'|'scheduledChange'|'investigation',
            ],
            'tags': [
                {
                    'string': 'string'
                },
            ],
            'eventStatusCodes': [
                'open'|'closed'|'upcoming',
            ]
        },
        nextToken='string',
        maxResults=123,
        locale='string'
    )
    
    
    :type filter: dict
    :param filter: Values to narrow the results returned.\n\neventArns (list) --A list of event ARNs (unique identifiers). For example: 'arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456', 'arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101'\n\n(string) --\n\n\neventTypeCodes (list) --A list of unique identifiers for event types. For example, 'AWS_EC2_SYSTEM_MAINTENANCE_EVENT','AWS_RDS_MAINTENANCE_SCHEDULED'.\n\n(string) --\n\n\nservices (list) --The AWS services associated with the event. For example, EC2 , RDS .\n\n(string) --\n\n\nregions (list) --A list of AWS regions.\n\n(string) --\n\n\navailabilityZones (list) --A list of AWS availability zones.\n\n(string) --\n\n\nstartTimes (list) --A list of dates and times that the event began.\n\n(dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .\n\nfrom (datetime) --The starting date and time of a time range.\n\nto (datetime) --The ending date and time of a time range.\n\n\n\n\n\nendTimes (list) --A list of dates and times that the event ended.\n\n(dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .\n\nfrom (datetime) --The starting date and time of a time range.\n\nto (datetime) --The ending date and time of a time range.\n\n\n\n\n\nlastUpdatedTimes (list) --A list of dates and times that the event was last updated.\n\n(dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .\n\nfrom (datetime) --The starting date and time of a time range.\n\nto (datetime) --The ending date and time of a time range.\n\n\n\n\n\nentityArns (list) --A list of entity ARNs (unique identifiers).\n\n(string) --\n\n\nentityValues (list) --A list of entity identifiers, such as EC2 instance IDs (i-34ab692e ) or EBS volumes (vol-426ab23e ).\n\n(string) --\n\n\neventTypeCategories (list) --A list of event type category codes (issue , scheduledChange , or accountNotification ).\n\n(string) --\n\n\ntags (list) --A map of entity tags attached to the affected entity.\n\n(dict) --\n(string) --\n(string) --\n\n\n\n\n\n\neventStatusCodes (list) --A list of event status codes.\n\n(string) --\n\n\n\n

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :rtype: dict

ReturnsResponse Syntax
{
    'events': [
        {
            'arn': 'string',
            'service': 'string',
            'eventTypeCode': 'string',
            'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange'|'investigation',
            'region': 'string',
            'availabilityZone': 'string',
            'startTime': datetime(2015, 1, 1),
            'endTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1),
            'statusCode': 'open'|'closed'|'upcoming',
            'eventScopeCode': 'PUBLIC'|'ACCOUNT_SPECIFIC'|'NONE'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

events (list) --
The events that match the specified filter criteria.

(dict) --
Summary information about an AWS Health event.

arn (string) --
The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

service (string) --
The AWS service that is affected by the event. For example, EC2 , RDS .

eventTypeCode (string) --
The unique identifier for the event type. The format is AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT .

eventTypeCategory (string) --
The category of the event. Possible values are issue , scheduledChange , and accountNotification .

region (string) --
The AWS region name of the event.

availabilityZone (string) --
The AWS Availability Zone of the event. For example, us-east-1a.

startTime (datetime) --
The date and time that the event began.

endTime (datetime) --
The date and time that the event ended.

lastUpdatedTime (datetime) --
The most recent date and time that the event was updated.

statusCode (string) --
The most recent status of the event. Possible values are open , closed , and upcoming .

eventScopeCode (string) --





nextToken (string) --
If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.







Exceptions

Health.Client.exceptions.InvalidPaginationToken
Health.Client.exceptions.UnsupportedLocale


    :return: {
        'events': [
            {
                'arn': 'string',
                'service': 'string',
                'eventTypeCode': 'string',
                'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange'|'investigation',
                'region': 'string',
                'availabilityZone': 'string',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'statusCode': 'open'|'closed'|'upcoming',
                'eventScopeCode': 'PUBLIC'|'ACCOUNT_SPECIFIC'|'NONE'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Health.Client.exceptions.InvalidPaginationToken
    Health.Client.exceptions.UnsupportedLocale
    
    """
    pass

def describe_events_for_organization(filter=None, nextToken=None, maxResults=None, locale=None):
    """
    Returns information about events across your organization in AWS Organizations, meeting the specified filter criteria. Events are returned in a summary form and do not include the accounts impacted, detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the  DescribeAffectedAccountsForOrganization ,  DescribeEventDetailsForOrganization , and  DescribeAffectedEntitiesForOrganization operations.
    If no filter criteria are specified, all events across your organization are returned. Results are sorted by lastModifiedTime , starting with the most recent.
    Before you can call this operation, you must first enable Health to work with AWS Organizations. To do this, call the  EnableHealthServiceAccessForOrganization operation from your organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_events_for_organization(
        filter={
            'eventTypeCodes': [
                'string',
            ],
            'awsAccountIds': [
                'string',
            ],
            'services': [
                'string',
            ],
            'regions': [
                'string',
            ],
            'startTime': {
                'from': datetime(2015, 1, 1),
                'to': datetime(2015, 1, 1)
            },
            'endTime': {
                'from': datetime(2015, 1, 1),
                'to': datetime(2015, 1, 1)
            },
            'lastUpdatedTime': {
                'from': datetime(2015, 1, 1),
                'to': datetime(2015, 1, 1)
            },
            'entityArns': [
                'string',
            ],
            'entityValues': [
                'string',
            ],
            'eventTypeCategories': [
                'issue'|'accountNotification'|'scheduledChange'|'investigation',
            ],
            'eventStatusCodes': [
                'open'|'closed'|'upcoming',
            ]
        },
        nextToken='string',
        maxResults=123,
        locale='string'
    )
    
    
    :type filter: dict
    :param filter: Values to narrow the results returned.\n\neventTypeCodes (list) --A list of unique identifiers for event types. For example, 'AWS_EC2_SYSTEM_MAINTENANCE_EVENT','AWS_RDS_MAINTENANCE_SCHEDULED'.\n\n(string) --\n\n\nawsAccountIds (list) --A list of 12-digit AWS account numbers that contains the affected entities.\n\n(string) --\n\n\nservices (list) --The AWS services associated with the event. For example, EC2 , RDS .\n\n(string) --\n\n\nregions (list) --A list of AWS Regions.\n\n(string) --\n\n\nstartTime (dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .\n\nfrom (datetime) --The starting date and time of a time range.\n\nto (datetime) --The ending date and time of a time range.\n\n\n\nendTime (dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .\n\nfrom (datetime) --The starting date and time of a time range.\n\nto (datetime) --The ending date and time of a time range.\n\n\n\nlastUpdatedTime (dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .\n\nfrom (datetime) --The starting date and time of a time range.\n\nto (datetime) --The ending date and time of a time range.\n\n\n\nentityArns (list) --REPLACEME\n\n(string) --\n\n\nentityValues (list) --A list of entity identifiers, such as EC2 instance IDs (i-34ab692e) or EBS volumes (vol-426ab23e).\n\n(string) --\n\n\neventTypeCategories (list) --REPLACEME\n\n(string) --\n\n\neventStatusCodes (list) --A list of event status codes.\n\n(string) --\n\n\n\n

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :rtype: dict

ReturnsResponse Syntax
{
    'events': [
        {
            'arn': 'string',
            'service': 'string',
            'eventTypeCode': 'string',
            'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange'|'investigation',
            'eventScopeCode': 'PUBLIC'|'ACCOUNT_SPECIFIC'|'NONE',
            'region': 'string',
            'startTime': datetime(2015, 1, 1),
            'endTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1),
            'statusCode': 'open'|'closed'|'upcoming'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

events (list) --
The events that match the specified filter criteria.

(dict) --
Summary information about an event, returned by the  DescribeEventsForOrganization operation.

arn (string) --
The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

service (string) --
The AWS service that is affected by the event. For example, EC2, RDS.

eventTypeCode (string) --
The unique identifier for the event type. The format is AWS_SERVICE_DESCRIPTION . For example, AWS_EC2_SYSTEM_MAINTENANCE_EVENT .

eventTypeCategory (string) --
The category of the event type.

eventScopeCode (string) --

region (string) --
The AWS Region name of the event.

startTime (datetime) --
The date and time that the event began.

endTime (datetime) --
The date and time that the event ended.

lastUpdatedTime (datetime) --
The most recent date and time that the event was updated.

statusCode (string) --
The most recent status of the event. Possible values are open , closed , and upcoming .





nextToken (string) --
If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.







Exceptions

Health.Client.exceptions.InvalidPaginationToken
Health.Client.exceptions.UnsupportedLocale


    :return: {
        'events': [
            {
                'arn': 'string',
                'service': 'string',
                'eventTypeCode': 'string',
                'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange'|'investigation',
                'eventScopeCode': 'PUBLIC'|'ACCOUNT_SPECIFIC'|'NONE',
                'region': 'string',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'statusCode': 'open'|'closed'|'upcoming'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Health.Client.exceptions.InvalidPaginationToken
    Health.Client.exceptions.UnsupportedLocale
    
    """
    pass

def describe_health_service_status_for_organization():
    """
    This operation provides status information on enabling or disabling AWS Health to work with your organization. To call this operation, you must sign in as an IAM user, assume an IAM role, or sign in as the root user (not recommended) in the organization\'s master account.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_health_service_status_for_organization()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'healthServiceAccessStatusForOrganization': 'string'
}


Response Structure

(dict) --
healthServiceAccessStatusForOrganization (string) --Information about the status of enabling or disabling AWS Health Organizational View in your organization.
Valid values are ENABLED | DISABLED | PENDING .







    :return: {
        'healthServiceAccessStatusForOrganization': 'string'
    }
    
    
    """
    pass

def disable_health_service_access_for_organization():
    """
    Calling this operation disables Health from working with AWS Organizations. This does not remove the Service Linked Role (SLR) from the the master account in your organization. Use the IAM console, API, or AWS CLI to remove the SLR if desired. To call this operation, you must sign in as an IAM user, assume an IAM role, or sign in as the root user (not recommended) in the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_health_service_access_for_organization()
    
    
    """
    pass

def enable_health_service_access_for_organization():
    """
    Calling this operation enables AWS Health to work with AWS Organizations. This applies a Service Linked Role (SLR) to the master account in the organization. To learn more about the steps in this process, visit enabling service access for AWS Health in AWS Organizations. To call this operation, you must sign in as an IAM user, assume an IAM role, or sign in as the root user (not recommended) in the organization\'s master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_health_service_access_for_organization()
    
    
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

