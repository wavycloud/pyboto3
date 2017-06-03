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

def describe_affected_entities(filter=None, locale=None, nextToken=None, maxResults=None):
    """
    Returns a list of entities that have been affected by the specified events, based on the specified filter criteria. Entities can refer to individual customer resources, groups of customer resources, or any other construct, depending on the AWS service. Events that have impact beyond that of the affected entities, or where the extent of impact is unknown, include at least one entity indicating this.
    At least one event ARN is required. Results are sorted by the lastUpdatedTime of the entity, starting with the most recent.
    See also: AWS API Documentation
    
    
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
    :param filter: [REQUIRED]
            Values to narrow the results returned. At least one event ARN is required.
            eventArns (list) -- [REQUIRED]A list of event ARNs (unique identifiers). For example: 'arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331', 'arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz'
            (string) --
            entityArns (list) --A list of entity ARNs (unique identifiers).
            (string) --
            entityValues (list) --A list of IDs for affected entities.
            (string) --
            lastUpdatedTimes (list) --A list of the most recent dates and times that the entity was updated.
            (dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .
            from (datetime) --The starting date and time of a time range.
            to (datetime) --The ending date and time of a time range.
            
            tags (list) --A map of entity tags attached to the affected entity.
            (dict) --
            (string) --
            (string) --
            
            statusCodes (list) --A list of entity status codes (IMPAIRED , UNIMPAIRED , or UNKNOWN ).
            (string) --
            

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :rtype: dict
    :return: {
        'entities': [
            {
                'entityArn': 'string',
                'eventArn': 'string',
                'entityValue': 'string',
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
    :param eventArns: A list of event ARNs (unique identifiers). For example: 'arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331', 'arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz'
            (string) --
            

    :rtype: dict
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
                'issue'|'accountNotification'|'scheduledChange',
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
    :param filter: Values to narrow the results returned.
            eventArns (list) --A list of event ARNs (unique identifiers). For example: 'arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331', 'arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz'
            (string) --
            eventTypeCodes (list) --A list of unique identifiers for event types. For example, 'AWS_EC2_SYSTEM_MAINTENANCE_EVENT','AWS_RDS_MAINTENANCE_SCHEDULED'
            (string) --
            services (list) --The AWS services associated with the event. For example, EC2 , RDS .
            (string) --
            regions (list) --A list of AWS regions.
            (string) --
            availabilityZones (list) --A list of AWS availability zones.
            (string) --
            startTimes (list) --A list of dates and times that the event began.
            (dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .
            from (datetime) --The starting date and time of a time range.
            to (datetime) --The ending date and time of a time range.
            
            endTimes (list) --A list of dates and times that the event ended.
            (dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .
            from (datetime) --The starting date and time of a time range.
            to (datetime) --The ending date and time of a time range.
            
            lastUpdatedTimes (list) --A list of dates and times that the event was last updated.
            (dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .
            from (datetime) --The starting date and time of a time range.
            to (datetime) --The ending date and time of a time range.
            
            entityArns (list) --A list of entity ARNs (unique identifiers).
            (string) --
            entityValues (list) --A list of entity identifiers, such as EC2 instance IDs (i-34ab692e ) or EBS volumes (vol-426ab23e ).
            (string) --
            eventTypeCategories (list) --A list of event type category codes (issue , scheduledChange , or accountNotification ).
            (string) --
            tags (list) --A map of entity tags attached to the affected entity.
            (dict) --
            (string) --
            (string) --
            
            eventStatusCodes (list) --A list of event status codes.
            (string) --
            

    :type aggregateField: string
    :param aggregateField: [REQUIRED]
            The only currently supported value is eventTypeCategory .
            

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :rtype: dict
    :return: {
        'eventAggregates': [
            {
                'aggregateValue': 'string',
                'count': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_event_details(eventArns=None, locale=None):
    """
    Returns detailed information about one or more specified events. Information includes standard event data (region, service, etc., as returned by  DescribeEvents ), a detailed event description, and possible additional metadata that depends upon the nature of the event. Affected entities are not included; to retrieve those, use the  DescribeAffectedEntities operation.
    If a specified event cannot be retrieved, an error message is returned for that event.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_details(
        eventArns=[
            'string',
        ],
        locale='string'
    )
    
    
    :type eventArns: list
    :param eventArns: [REQUIRED]
            A list of event ARNs (unique identifiers). For example: 'arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331', 'arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz'
            (string) --
            

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :rtype: dict
    :return: {
        'successfulSet': [
            {
                'event': {
                    'arn': 'string',
                    'service': 'string',
                    'eventTypeCode': 'string',
                    'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange',
                    'region': 'string',
                    'availabilityZone': 'string',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'statusCode': 'open'|'closed'|'upcoming'
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

def describe_event_types(filter=None, locale=None, nextToken=None, maxResults=None):
    """
    Returns the event types that meet the specified filter criteria. If no filter criteria are specified, all event types are returned, in no particular order.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_event_types(
        filter={
            'eventTypeCodes': [
                'string',
            ],
            'services': [
                'string',
            ],
            'eventTypeCategories': [
                'issue'|'accountNotification'|'scheduledChange',
            ]
        },
        locale='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type filter: dict
    :param filter: Values to narrow the results returned.
            eventTypeCodes (list) --A list of event type codes.
            (string) --
            services (list) --The AWS services associated with the event. For example, EC2 , RDS .
            (string) --
            eventTypeCategories (list) --A list of event type category codes (issue , scheduledChange , or accountNotification ).
            (string) --
            

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :rtype: dict
    :return: {
        'eventTypes': [
            {
                'service': 'string',
                'code': 'string',
                'category': 'issue'|'accountNotification'|'scheduledChange'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_events(filter=None, nextToken=None, maxResults=None, locale=None):
    """
    Returns information about events that meet the specified filter criteria. Events are returned in a summary form and do not include the detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the  DescribeEventDetails and  DescribeAffectedEntities operations.
    If no filter criteria are specified, all events are returned. Results are sorted by lastModifiedTime , starting with the most recent.
    See also: AWS API Documentation
    
    
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
                'issue'|'accountNotification'|'scheduledChange',
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
    :param filter: Values to narrow the results returned.
            eventArns (list) --A list of event ARNs (unique identifiers). For example: 'arn:aws:health:us-east-1::event/AWS_EC2_MAINTENANCE_5331', 'arn:aws:health:us-west-1::event/AWS_EBS_LOST_VOLUME_xyz'
            (string) --
            eventTypeCodes (list) --A list of unique identifiers for event types. For example, 'AWS_EC2_SYSTEM_MAINTENANCE_EVENT','AWS_RDS_MAINTENANCE_SCHEDULED'
            (string) --
            services (list) --The AWS services associated with the event. For example, EC2 , RDS .
            (string) --
            regions (list) --A list of AWS regions.
            (string) --
            availabilityZones (list) --A list of AWS availability zones.
            (string) --
            startTimes (list) --A list of dates and times that the event began.
            (dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .
            from (datetime) --The starting date and time of a time range.
            to (datetime) --The ending date and time of a time range.
            
            endTimes (list) --A list of dates and times that the event ended.
            (dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .
            from (datetime) --The starting date and time of a time range.
            to (datetime) --The ending date and time of a time range.
            
            lastUpdatedTimes (list) --A list of dates and times that the event was last updated.
            (dict) --A range of dates and times that is used by the EventFilter and EntityFilter objects. If from is set and to is set: match items where the timestamp (startTime , endTime , or lastUpdatedTime ) is between from and to inclusive. If from is set and to is not set: match items where the timestamp value is equal to or after from . If from is not set and to is set: match items where the timestamp value is equal to or before to .
            from (datetime) --The starting date and time of a time range.
            to (datetime) --The ending date and time of a time range.
            
            entityArns (list) --A list of entity ARNs (unique identifiers).
            (string) --
            entityValues (list) --A list of entity identifiers, such as EC2 instance IDs (i-34ab692e ) or EBS volumes (vol-426ab23e ).
            (string) --
            eventTypeCategories (list) --A list of event type category codes (issue , scheduledChange , or accountNotification ).
            (string) --
            tags (list) --A map of entity tags attached to the affected entity.
            (dict) --
            (string) --
            (string) --
            
            eventStatusCodes (list) --A list of event status codes.
            (string) --
            

    :type nextToken: string
    :param nextToken: If the results of a search are large, only a portion of the results are returned, and a nextToken pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.

    :type maxResults: integer
    :param maxResults: The maximum number of items to return in one batch, between 10 and 100, inclusive.

    :type locale: string
    :param locale: The locale (language) to return information in. English (en) is the default and the only supported value at this time.

    :rtype: dict
    :return: {
        'events': [
            {
                'arn': 'string',
                'service': 'string',
                'eventTypeCode': 'string',
                'eventTypeCategory': 'issue'|'accountNotification'|'scheduledChange',
                'region': 'string',
                'availabilityZone': 'string',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'statusCode': 'open'|'closed'|'upcoming'
            },
        ],
        'nextToken': 'string'
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

def get_waiter():
    """
    
    """
    pass

