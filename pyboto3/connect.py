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

def create_user(Username=None, Password=None, IdentityInfo=None, PhoneConfig=None, DirectoryUserId=None, SecurityProfileIds=None, RoutingProfileId=None, HierarchyGroupId=None, InstanceId=None, Tags=None):
    """
    Creates a user account for the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user(
        Username='string',
        Password='string',
        IdentityInfo={
            'FirstName': 'string',
            'LastName': 'string',
            'Email': 'string'
        },
        PhoneConfig={
            'PhoneType': 'SOFT_PHONE'|'DESK_PHONE',
            'AutoAccept': True|False,
            'AfterContactWorkTimeLimit': 123,
            'DeskPhoneNumber': 'string'
        },
        DirectoryUserId='string',
        SecurityProfileIds=[
            'string',
        ],
        RoutingProfileId='string',
        HierarchyGroupId='string',
        InstanceId='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type Username: string
    :param Username: [REQUIRED]\nThe user name for the account. For instances not using SAML for identity management, the user name can include up to 20 characters. If you are using SAML for identity management, the user name can include up to 64 characters from [a-zA-Z0-9_-.@]+.\n

    :type Password: string
    :param Password: The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password.

    :type IdentityInfo: dict
    :param IdentityInfo: The information about the identity of the user.\n\nFirstName (string) --The first name. This is required if you are using Amazon Connect or SAML for identity management.\n\nLastName (string) --The last name. This is required if you are using Amazon Connect or SAML for identity management.\n\nEmail (string) --The email address. If you are using SAML for identity management and include this parameter, an error is returned.\n\n\n

    :type PhoneConfig: dict
    :param PhoneConfig: [REQUIRED]\nThe phone settings for the user.\n\nPhoneType (string) -- [REQUIRED]The phone type.\n\nAutoAccept (boolean) --The Auto accept setting.\n\nAfterContactWorkTimeLimit (integer) --The After Call Work (ACW) timeout setting, in seconds.\n\nDeskPhoneNumber (string) --The phone number for the user\'s desk phone.\n\n\n

    :type DirectoryUserId: string
    :param DirectoryUserId: The identifier of the user account in the directory used for identity management. If Amazon Connect cannot access the directory, you can specify this identifier to authenticate users. If you include the identifier, we assume that Amazon Connect cannot access the directory. Otherwise, the identity information is used to authenticate users from your directory.\nThis parameter is required if you are using an existing directory for identity management in Amazon Connect when Amazon Connect cannot access your directory to authenticate users. If you are using SAML for identity management and include this parameter, an error is returned.\n

    :type SecurityProfileIds: list
    :param SecurityProfileIds: [REQUIRED]\nThe identifier of the security profile for the user.\n\n(string) --\n\n

    :type RoutingProfileId: string
    :param RoutingProfileId: [REQUIRED]\nThe identifier of the routing profile for the user.\n

    :type HierarchyGroupId: string
    :param HierarchyGroupId: The identifier of the hierarchy group for the user.

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type Tags: dict
    :param Tags: One or more tags.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'UserId': 'string',
    'UserArn': 'string'
}


Response Structure

(dict) --

UserId (string) --
The identifier of the user account.

UserArn (string) --
The Amazon Resource Name (ARN) of the user account.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.LimitExceededException
Connect.Client.exceptions.DuplicateResourceException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'UserId': 'string',
        'UserArn': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.LimitExceededException
    Connect.Client.exceptions.DuplicateResourceException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def delete_user(InstanceId=None, UserId=None):
    """
    Deletes a user account from the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user(
        InstanceId='string',
        UserId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe identifier of the user.\n

    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def describe_user(UserId=None, InstanceId=None):
    """
    Describes the specified user account. You can find the instance ID in the console (it\xe2\x80\x99s the final part of the ARN). The console does not display the user IDs. Instead, list the users and note the IDs provided in the output.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_user(
        UserId='string',
        InstanceId='string'
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]\nThe identifier of the user account.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'Id': 'string',
        'Arn': 'string',
        'Username': 'string',
        'IdentityInfo': {
            'FirstName': 'string',
            'LastName': 'string',
            'Email': 'string'
        },
        'PhoneConfig': {
            'PhoneType': 'SOFT_PHONE'|'DESK_PHONE',
            'AutoAccept': True|False,
            'AfterContactWorkTimeLimit': 123,
            'DeskPhoneNumber': 'string'
        },
        'DirectoryUserId': 'string',
        'SecurityProfileIds': [
            'string',
        ],
        'RoutingProfileId': 'string',
        'HierarchyGroupId': 'string',
        'Tags': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

User (dict) --
Information about the user account and configuration settings.

Id (string) --
The identifier of the user account.

Arn (string) --
The Amazon Resource Name (ARN) of the user account.

Username (string) --
The user name assigned to the user account.

IdentityInfo (dict) --
Information about the user identity.

FirstName (string) --
The first name. This is required if you are using Amazon Connect or SAML for identity management.

LastName (string) --
The last name. This is required if you are using Amazon Connect or SAML for identity management.

Email (string) --
The email address. If you are using SAML for identity management and include this parameter, an error is returned.



PhoneConfig (dict) --
Information about the phone configuration for the user.

PhoneType (string) --
The phone type.

AutoAccept (boolean) --
The Auto accept setting.

AfterContactWorkTimeLimit (integer) --
The After Call Work (ACW) timeout setting, in seconds.

DeskPhoneNumber (string) --
The phone number for the user\'s desk phone.



DirectoryUserId (string) --
The identifier of the user account in the directory used for identity management.

SecurityProfileIds (list) --
The identifiers of the security profiles for the user.

(string) --


RoutingProfileId (string) --
The identifier of the routing profile for the user.

HierarchyGroupId (string) --
The identifier of the hierarchy group for the user.

Tags (dict) --
The tags.

(string) --
(string) --












Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'User': {
            'Id': 'string',
            'Arn': 'string',
            'Username': 'string',
            'IdentityInfo': {
                'FirstName': 'string',
                'LastName': 'string',
                'Email': 'string'
            },
            'PhoneConfig': {
                'PhoneType': 'SOFT_PHONE'|'DESK_PHONE',
                'AutoAccept': True|False,
                'AfterContactWorkTimeLimit': 123,
                'DeskPhoneNumber': 'string'
            },
            'DirectoryUserId': 'string',
            'SecurityProfileIds': [
                'string',
            ],
            'RoutingProfileId': 'string',
            'HierarchyGroupId': 'string',
            'Tags': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_user_hierarchy_group(HierarchyGroupId=None, InstanceId=None):
    """
    Describes the specified hierarchy group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_user_hierarchy_group(
        HierarchyGroupId='string',
        InstanceId='string'
    )
    
    
    :type HierarchyGroupId: string
    :param HierarchyGroupId: [REQUIRED]\nThe identifier of the hierarchy group.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HierarchyGroup': {
        'Id': 'string',
        'Arn': 'string',
        'Name': 'string',
        'LevelId': 'string',
        'HierarchyPath': {
            'LevelOne': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
            'LevelTwo': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
            'LevelThree': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
            'LevelFour': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
            'LevelFive': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            }
        }
    }
}


Response Structure

(dict) --

HierarchyGroup (dict) --
Information about the hierarchy group.

Id (string) --
The identifier of the hierarchy group.

Arn (string) --
The Amazon Resource Name (ARN) of the hierarchy group.

Name (string) --
The name of the hierarchy group.

LevelId (string) --
The identifier of the level in the hierarchy group.

HierarchyPath (dict) --
Information about the levels in the hierarchy group.

LevelOne (dict) --
Information about level one.

Id (string) --
The identifier of the hierarchy group.

Arn (string) --
The Amazon Resource Name (ARN) of the hierarchy group.

Name (string) --
The name of the hierarchy group.



LevelTwo (dict) --
Information about level two.

Id (string) --
The identifier of the hierarchy group.

Arn (string) --
The Amazon Resource Name (ARN) of the hierarchy group.

Name (string) --
The name of the hierarchy group.



LevelThree (dict) --
Information about level three.

Id (string) --
The identifier of the hierarchy group.

Arn (string) --
The Amazon Resource Name (ARN) of the hierarchy group.

Name (string) --
The name of the hierarchy group.



LevelFour (dict) --
Information about level four.

Id (string) --
The identifier of the hierarchy group.

Arn (string) --
The Amazon Resource Name (ARN) of the hierarchy group.

Name (string) --
The name of the hierarchy group.



LevelFive (dict) --
Information about level five.

Id (string) --
The identifier of the hierarchy group.

Arn (string) --
The Amazon Resource Name (ARN) of the hierarchy group.

Name (string) --
The name of the hierarchy group.













Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'HierarchyGroup': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'LevelId': 'string',
            'HierarchyPath': {
                'LevelOne': {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string'
                },
                'LevelTwo': {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string'
                },
                'LevelThree': {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string'
                },
                'LevelFour': {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string'
                },
                'LevelFive': {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def describe_user_hierarchy_structure(InstanceId=None):
    """
    Describes the hierarchy structure of the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_user_hierarchy_structure(
        InstanceId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :rtype: dict
ReturnsResponse Syntax{
    'HierarchyStructure': {
        'LevelOne': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        },
        'LevelTwo': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        },
        'LevelThree': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        },
        'LevelFour': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        },
        'LevelFive': {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        }
    }
}


Response Structure

(dict) --
HierarchyStructure (dict) --Information about the hierarchy structure.

LevelOne (dict) --Information about level one.

Id (string) --The identifier of the hierarchy level.

Arn (string) --The Amazon Resource Name (ARN) of the hierarchy level.

Name (string) --The name of the hierarchy level.



LevelTwo (dict) --Information about level two.

Id (string) --The identifier of the hierarchy level.

Arn (string) --The Amazon Resource Name (ARN) of the hierarchy level.

Name (string) --The name of the hierarchy level.



LevelThree (dict) --Information about level three.

Id (string) --The identifier of the hierarchy level.

Arn (string) --The Amazon Resource Name (ARN) of the hierarchy level.

Name (string) --The name of the hierarchy level.



LevelFour (dict) --Information about level four.

Id (string) --The identifier of the hierarchy level.

Arn (string) --The Amazon Resource Name (ARN) of the hierarchy level.

Name (string) --The name of the hierarchy level.



LevelFive (dict) --Information about level five.

Id (string) --The identifier of the hierarchy level.

Arn (string) --The Amazon Resource Name (ARN) of the hierarchy level.

Name (string) --The name of the hierarchy level.










Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'HierarchyStructure': {
            'LevelOne': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
            'LevelTwo': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
            'LevelThree': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
            'LevelFour': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
            'LevelFive': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            }
        }
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

def get_contact_attributes(InstanceId=None, InitialContactId=None):
    """
    Retrieves the contact attributes for the specified contact.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_contact_attributes(
        InstanceId='string',
        InitialContactId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type InitialContactId: string
    :param InitialContactId: [REQUIRED]\nThe identifier of the initial contact.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Attributes': {
        'string': 'string'
    }
}


Response Structure

(dict) --

Attributes (dict) --
Information about the attributes.

(string) --
(string) --










Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'Attributes': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_current_metric_data(InstanceId=None, Filters=None, Groupings=None, CurrentMetrics=None, NextToken=None, MaxResults=None):
    """
    Gets the real-time metric data from the specified Amazon Connect instance.
    For more information, see Real-time Metrics Reports in the Amazon Connect Administrator Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_current_metric_data(
        InstanceId='string',
        Filters={
            'Queues': [
                'string',
            ],
            'Channels': [
                'VOICE'|'CHAT',
            ]
        },
        Groupings=[
            'QUEUE'|'CHANNEL',
        ],
        CurrentMetrics=[
            {
                'Name': 'AGENTS_ONLINE'|'AGENTS_AVAILABLE'|'AGENTS_ON_CALL'|'AGENTS_NON_PRODUCTIVE'|'AGENTS_AFTER_CONTACT_WORK'|'AGENTS_ERROR'|'AGENTS_STAFFED'|'CONTACTS_IN_QUEUE'|'OLDEST_CONTACT_AGE'|'CONTACTS_SCHEDULED'|'AGENTS_ON_CONTACT'|'SLOTS_ACTIVE'|'SLOTS_AVAILABLE',
                'Unit': 'SECONDS'|'COUNT'|'PERCENT'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type Filters: dict
    :param Filters: [REQUIRED]\nThe queues, up to 100, or channels, to use to filter the metrics returned. Metric data is retrieved only for the resources associated with the queues or channels included in the filter. You can include both queue IDs and queue ARNs in the same request. The only supported channel is VOICE .\n\nQueues (list) --The queues to use to filter the metrics. You can specify up to 100 queues per request.\n\n(string) --\n\n\nChannels (list) --The channel to use to filter the metrics.\n\n(string) --\n\n\n\n

    :type Groupings: list
    :param Groupings: The grouping applied to the metrics returned. For example, when grouped by QUEUE , the metrics returned apply to each queue rather than aggregated for all queues. If you group by CHANNEL , you should include a Channels filter. The only supported channel is VOICE .\nIf no Grouping is included in the request, a summary of metrics is returned.\n\n(string) --\n\n

    :type CurrentMetrics: list
    :param CurrentMetrics: [REQUIRED]\nThe metrics to retrieve. Specify the name and unit for each metric. The following metrics are available:\n\nAGENTS_AFTER_CONTACT_WORK\nUnit: COUNT\n\nAGENTS_AVAILABLE\nUnit: COUNT\n\nAGENTS_ERROR\nUnit: COUNT\n\nAGENTS_NON_PRODUCTIVE\nUnit: COUNT\n\nAGENTS_ON_CALL\nUnit: COUNT\n\nAGENTS_ON_CONTACT\nUnit: COUNT\n\nAGENTS_ONLINE\nUnit: COUNT\n\nAGENTS_STAFFED\nUnit: COUNT\n\nCONTACTS_IN_QUEUE\nUnit: COUNT\n\nCONTACTS_SCHEDULED\nUnit: COUNT\n\nOLDEST_CONTACT_AGE\nUnit: SECONDS\n\nSLOTS_ACTIVE\nUnit: COUNT\n\nSLOTS_AVAILABLE\nUnit: COUNT\n\n(dict) --Contains information about a real-time metric.\n\nName (string) --The name of the metric.\n\nUnit (string) --The unit for the metric.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.\nThe token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.\n

    :type MaxResults: integer
    :param MaxResults: The maximimum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'MetricResults': [
        {
            'Dimensions': {
                'Queue': {
                    'Id': 'string',
                    'Arn': 'string'
                },
                'Channel': 'VOICE'|'CHAT'
            },
            'Collections': [
                {
                    'Metric': {
                        'Name': 'AGENTS_ONLINE'|'AGENTS_AVAILABLE'|'AGENTS_ON_CALL'|'AGENTS_NON_PRODUCTIVE'|'AGENTS_AFTER_CONTACT_WORK'|'AGENTS_ERROR'|'AGENTS_STAFFED'|'CONTACTS_IN_QUEUE'|'OLDEST_CONTACT_AGE'|'CONTACTS_SCHEDULED'|'AGENTS_ON_CONTACT'|'SLOTS_ACTIVE'|'SLOTS_AVAILABLE',
                        'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                    },
                    'Value': 123.0
                },
            ]
        },
    ],
    'DataSnapshotTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --

NextToken (string) --
If there are additional results, this is the token for the next set of results.
The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.

MetricResults (list) --
Information about the real-time metrics.

(dict) --
Contains information about a set of real-time metrics.

Dimensions (dict) --
The dimensions for the metrics.

Queue (dict) --
Information about the queue for which metrics are returned.

Id (string) --
The identifier of the queue.

Arn (string) --
The Amazon Resource Name (ARN) of the queue.



Channel (string) --
The channel used for grouping and filters.



Collections (list) --
The set of metrics.

(dict) --
Contains the data for a real-time metric.

Metric (dict) --
Information about the metric.

Name (string) --
The name of the metric.

Unit (string) --
The unit for the metric.



Value (float) --
The value of the metric.









DataSnapshotTime (datetime) --
The time at which the metrics were retrieved and cached for pagination.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.InternalServiceException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.ResourceNotFoundException


    :return: {
        'NextToken': 'string',
        'MetricResults': [
            {
                'Dimensions': {
                    'Queue': {
                        'Id': 'string',
                        'Arn': 'string'
                    },
                    'Channel': 'VOICE'|'CHAT'
                },
                'Collections': [
                    {
                        'Metric': {
                            'Name': 'AGENTS_ONLINE'|'AGENTS_AVAILABLE'|'AGENTS_ON_CALL'|'AGENTS_NON_PRODUCTIVE'|'AGENTS_AFTER_CONTACT_WORK'|'AGENTS_ERROR'|'AGENTS_STAFFED'|'CONTACTS_IN_QUEUE'|'OLDEST_CONTACT_AGE'|'CONTACTS_SCHEDULED'|'AGENTS_ON_CONTACT'|'SLOTS_ACTIVE'|'SLOTS_AVAILABLE',
                            'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                        },
                        'Value': 123.0
                    },
                ]
            },
        ],
        'DataSnapshotTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.InternalServiceException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def get_federation_token(InstanceId=None):
    """
    Retrieves a token for federation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_federation_token(
        InstanceId='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Credentials': {
        'AccessToken': 'string',
        'AccessTokenExpiration': datetime(2015, 1, 1),
        'RefreshToken': 'string',
        'RefreshTokenExpiration': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Credentials (dict) --The credentials to use for federation.

AccessToken (string) --An access token generated for a federated user to access Amazon Connect.

AccessTokenExpiration (datetime) --A token generated with an expiration time for the session a user is logged in to Amazon Connect.

RefreshToken (string) --Renews a token generated for a user to access the Amazon Connect instance.

RefreshTokenExpiration (datetime) --Renews the expiration timer for a generated token.








Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.UserNotFoundException
Connect.Client.exceptions.InternalServiceException
Connect.Client.exceptions.DuplicateResourceException


    :return: {
        'Credentials': {
            'AccessToken': 'string',
            'AccessTokenExpiration': datetime(2015, 1, 1),
            'RefreshToken': 'string',
            'RefreshTokenExpiration': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def get_metric_data(InstanceId=None, StartTime=None, EndTime=None, Filters=None, Groupings=None, HistoricalMetrics=None, NextToken=None, MaxResults=None):
    """
    Gets historical metric data from the specified Amazon Connect instance.
    For more information, see Historical Metrics Reports in the Amazon Connect Administrator Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_metric_data(
        InstanceId='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Filters={
            'Queues': [
                'string',
            ],
            'Channels': [
                'VOICE'|'CHAT',
            ]
        },
        Groupings=[
            'QUEUE'|'CHANNEL',
        ],
        HistoricalMetrics=[
            {
                'Name': 'CONTACTS_QUEUED'|'CONTACTS_HANDLED'|'CONTACTS_ABANDONED'|'CONTACTS_CONSULTED'|'CONTACTS_AGENT_HUNG_UP_FIRST'|'CONTACTS_HANDLED_INCOMING'|'CONTACTS_HANDLED_OUTBOUND'|'CONTACTS_HOLD_ABANDONS'|'CONTACTS_TRANSFERRED_IN'|'CONTACTS_TRANSFERRED_OUT'|'CONTACTS_TRANSFERRED_IN_FROM_QUEUE'|'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE'|'CONTACTS_MISSED'|'CALLBACK_CONTACTS_HANDLED'|'API_CONTACTS_HANDLED'|'OCCUPANCY'|'HANDLE_TIME'|'AFTER_CONTACT_WORK_TIME'|'QUEUED_TIME'|'ABANDON_TIME'|'QUEUE_ANSWER_TIME'|'HOLD_TIME'|'INTERACTION_TIME'|'INTERACTION_AND_HOLD_TIME'|'SERVICE_LEVEL',
                'Threshold': {
                    'Comparison': 'LT',
                    'ThresholdValue': 123.0
                },
                'Statistic': 'SUM'|'MAX'|'AVG',
                'Unit': 'SECONDS'|'COUNT'|'PERCENT'
            },
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type StartTime: datetime
    :param StartTime: [REQUIRED]\nThe timestamp, in UNIX Epoch time format, at which to start the reporting interval for the retrieval of historical metrics data. The time must be specified using a multiple of 5 minutes, such as 10:05, 10:10, 10:15.\nThe start time cannot be earlier than 24 hours before the time of the request. Historical metrics are available only for 24 hours.\n

    :type EndTime: datetime
    :param EndTime: [REQUIRED]\nThe timestamp, in UNIX Epoch time format, at which to end the reporting interval for the retrieval of historical metrics data. The time must be specified using an interval of 5 minutes, such as 11:00, 11:05, 11:10, and must be later than the start time timestamp.\nThe time range between the start and end time must be less than 24 hours.\n

    :type Filters: dict
    :param Filters: [REQUIRED]\nThe queues, up to 100, or channels, to use to filter the metrics returned. Metric data is retrieved only for the resources associated with the queues or channels included in the filter. You can include both queue IDs and queue ARNs in the same request. The only supported channel is VOICE .\n\nQueues (list) --The queues to use to filter the metrics. You can specify up to 100 queues per request.\n\n(string) --\n\n\nChannels (list) --The channel to use to filter the metrics.\n\n(string) --\n\n\n\n

    :type Groupings: list
    :param Groupings: The grouping applied to the metrics returned. For example, when results are grouped by queue, the metrics returned are grouped by queue. The values returned apply to the metrics for each queue rather than aggregated for all queues.\nThe only supported grouping is QUEUE .\nIf no grouping is specified, a summary of metrics for all queues is returned.\n\n(string) --\n\n

    :type HistoricalMetrics: list
    :param HistoricalMetrics: [REQUIRED]\nThe metrics to retrieve. Specify the name, unit, and statistic for each metric. The following historical metrics are available:\n\nABANDON_TIME\nUnit: SECONDS\nStatistic: AVG\n\nAFTER_CONTACT_WORK_TIME\nUnit: SECONDS\nStatistic: AVG\n\nAPI_CONTACTS_HANDLED\nUnit: COUNT\nStatistic: SUM\n\nCALLBACK_CONTACTS_HANDLED\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_ABANDONED\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_AGENT_HUNG_UP_FIRST\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_CONSULTED\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_HANDLED\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_HANDLED_INCOMING\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_HANDLED_OUTBOUND\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_HOLD_ABANDONS\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_MISSED\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_QUEUED\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_TRANSFERRED_IN\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_TRANSFERRED_IN_FROM_QUEUE\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_TRANSFERRED_OUT\nUnit: COUNT\nStatistic: SUM\n\nCONTACTS_TRANSFERRED_OUT_FROM_QUEUE\nUnit: COUNT\nStatistic: SUM\n\nHANDLE_TIME\nUnit: SECONDS\nStatistic: AVG\n\nHOLD_TIME\nUnit: SECONDS\nStatistic: AVG\n\nINTERACTION_AND_HOLD_TIME\nUnit: SECONDS\nStatistic: AVG\n\nINTERACTION_TIME\nUnit: SECONDS\nStatistic: AVG\n\nOCCUPANCY\nUnit: PERCENT\nStatistic: AVG\n\nQUEUE_ANSWER_TIME\nUnit: SECONDS\nStatistic: AVG\n\nQUEUED_TIME\nUnit: SECONDS\nStatistic: MAX\n\nSERVICE_LEVEL\nUnit: PERCENT\nStatistic: AVG\nThreshold: Only 'Less than' comparisons are supported, with the following service level thresholds: 15, 20, 25, 30, 45, 60, 90, 120, 180, 240, 300, 600\n\n(dict) --Contains information about a historical metric.\n\nName (string) --The name of the metric.\n\nThreshold (dict) --The threshold for the metric, used with service level metrics.\n\nComparison (string) --The type of comparison. Only 'less than' (LT) comparisons are supported.\n\nThresholdValue (float) --The threshold value to compare.\n\n\n\nStatistic (string) --The statistic for the metric.\n\nUnit (string) --The unit for the metric.\n\n\n\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximimum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'MetricResults': [
        {
            'Dimensions': {
                'Queue': {
                    'Id': 'string',
                    'Arn': 'string'
                },
                'Channel': 'VOICE'|'CHAT'
            },
            'Collections': [
                {
                    'Metric': {
                        'Name': 'CONTACTS_QUEUED'|'CONTACTS_HANDLED'|'CONTACTS_ABANDONED'|'CONTACTS_CONSULTED'|'CONTACTS_AGENT_HUNG_UP_FIRST'|'CONTACTS_HANDLED_INCOMING'|'CONTACTS_HANDLED_OUTBOUND'|'CONTACTS_HOLD_ABANDONS'|'CONTACTS_TRANSFERRED_IN'|'CONTACTS_TRANSFERRED_OUT'|'CONTACTS_TRANSFERRED_IN_FROM_QUEUE'|'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE'|'CONTACTS_MISSED'|'CALLBACK_CONTACTS_HANDLED'|'API_CONTACTS_HANDLED'|'OCCUPANCY'|'HANDLE_TIME'|'AFTER_CONTACT_WORK_TIME'|'QUEUED_TIME'|'ABANDON_TIME'|'QUEUE_ANSWER_TIME'|'HOLD_TIME'|'INTERACTION_TIME'|'INTERACTION_AND_HOLD_TIME'|'SERVICE_LEVEL',
                        'Threshold': {
                            'Comparison': 'LT',
                            'ThresholdValue': 123.0
                        },
                        'Statistic': 'SUM'|'MAX'|'AVG',
                        'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                    },
                    'Value': 123.0
                },
            ]
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If there are additional results, this is the token for the next set of results.
The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.

MetricResults (list) --
Information about the historical metrics.
If no grouping is specified, a summary of metric data is returned.

(dict) --
Contains information about the historical metrics retrieved.

Dimensions (dict) --
The dimension for the metrics.

Queue (dict) --
Information about the queue for which metrics are returned.

Id (string) --
The identifier of the queue.

Arn (string) --
The Amazon Resource Name (ARN) of the queue.



Channel (string) --
The channel used for grouping and filters.



Collections (list) --
The set of metrics.

(dict) --
Contains the data for a historical metric.

Metric (dict) --
Information about the metric.

Name (string) --
The name of the metric.

Threshold (dict) --
The threshold for the metric, used with service level metrics.

Comparison (string) --
The type of comparison. Only "less than" (LT) comparisons are supported.

ThresholdValue (float) --
The threshold value to compare.



Statistic (string) --
The statistic for the metric.

Unit (string) --
The unit for the metric.



Value (float) --
The value of the metric.















Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.InternalServiceException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.ResourceNotFoundException


    :return: {
        'NextToken': 'string',
        'MetricResults': [
            {
                'Dimensions': {
                    'Queue': {
                        'Id': 'string',
                        'Arn': 'string'
                    },
                    'Channel': 'VOICE'|'CHAT'
                },
                'Collections': [
                    {
                        'Metric': {
                            'Name': 'CONTACTS_QUEUED'|'CONTACTS_HANDLED'|'CONTACTS_ABANDONED'|'CONTACTS_CONSULTED'|'CONTACTS_AGENT_HUNG_UP_FIRST'|'CONTACTS_HANDLED_INCOMING'|'CONTACTS_HANDLED_OUTBOUND'|'CONTACTS_HOLD_ABANDONS'|'CONTACTS_TRANSFERRED_IN'|'CONTACTS_TRANSFERRED_OUT'|'CONTACTS_TRANSFERRED_IN_FROM_QUEUE'|'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE'|'CONTACTS_MISSED'|'CALLBACK_CONTACTS_HANDLED'|'API_CONTACTS_HANDLED'|'OCCUPANCY'|'HANDLE_TIME'|'AFTER_CONTACT_WORK_TIME'|'QUEUED_TIME'|'ABANDON_TIME'|'QUEUE_ANSWER_TIME'|'HOLD_TIME'|'INTERACTION_TIME'|'INTERACTION_AND_HOLD_TIME'|'SERVICE_LEVEL',
                            'Threshold': {
                                'Comparison': 'LT',
                                'ThresholdValue': 123.0
                            },
                            'Statistic': 'SUM'|'MAX'|'AVG',
                            'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                        },
                        'Value': 123.0
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.InternalServiceException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.ResourceNotFoundException
    
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

def list_contact_flows(InstanceId=None, ContactFlowTypes=None, NextToken=None, MaxResults=None):
    """
    Provides information about the contact flows for the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_contact_flows(
        InstanceId='string',
        ContactFlowTypes=[
            'CONTACT_FLOW'|'CUSTOMER_QUEUE'|'CUSTOMER_HOLD'|'CUSTOMER_WHISPER'|'AGENT_HOLD'|'AGENT_WHISPER'|'OUTBOUND_WHISPER'|'AGENT_TRANSFER'|'QUEUE_TRANSFER',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type ContactFlowTypes: list
    :param ContactFlowTypes: The type of contact flow.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximimum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'ContactFlowSummaryList': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'ContactFlowType': 'CONTACT_FLOW'|'CUSTOMER_QUEUE'|'CUSTOMER_HOLD'|'CUSTOMER_WHISPER'|'AGENT_HOLD'|'AGENT_WHISPER'|'OUTBOUND_WHISPER'|'AGENT_TRANSFER'|'QUEUE_TRANSFER'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ContactFlowSummaryList (list) --
Information about the contact flows.

(dict) --
Contains summary information about a contact flow.

Id (string) --
The identifier of the contact flow.

Arn (string) --
The Amazon Resource Name (ARN) of the contact flow.

Name (string) --
The name of the contact flow.

ContactFlowType (string) --
The type of contact flow.





NextToken (string) --
If there are additional results, this is the token for the next set of results.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'ContactFlowSummaryList': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'ContactFlowType': 'CONTACT_FLOW'|'CUSTOMER_QUEUE'|'CUSTOMER_HOLD'|'CUSTOMER_WHISPER'|'AGENT_HOLD'|'AGENT_WHISPER'|'OUTBOUND_WHISPER'|'AGENT_TRANSFER'|'QUEUE_TRANSFER'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def list_hours_of_operations(InstanceId=None, NextToken=None, MaxResults=None):
    """
    Provides information about the hours of operation for the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_hours_of_operations(
        InstanceId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximimum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'HoursOfOperationSummaryList': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

HoursOfOperationSummaryList (list) --
Information about the hours of operation.

(dict) --
Contains summary information about hours of operation for a contact center.

Id (string) --
The identifier of the hours of operation.

Arn (string) --
The Amazon Resource Name (ARN) of the hours of operation.

Name (string) --
The name of the hours of operation.





NextToken (string) --
If there are additional results, this is the token for the next set of results.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'HoursOfOperationSummaryList': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def list_phone_numbers(InstanceId=None, PhoneNumberTypes=None, PhoneNumberCountryCodes=None, NextToken=None, MaxResults=None):
    """
    Provides information about the phone numbers for the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_phone_numbers(
        InstanceId='string',
        PhoneNumberTypes=[
            'TOLL_FREE'|'DID',
        ],
        PhoneNumberCountryCodes=[
            'AF'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BA'|'BW'|'BR'|'IO'|'VG'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CK'|'CR'|'HR'|'CU'|'CW'|'CY'|'CZ'|'CD'|'DK'|'DJ'|'DM'|'DO'|'TL'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'PF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'CI'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'AN'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'KP'|'MP'|'NO'|'OM'|'PK'|'PW'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'CG'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'KR'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'VI'|'UG'|'UA'|'AE'|'GB'|'US'|'UY'|'UZ'|'VU'|'VA'|'VE'|'VN'|'WF'|'EH'|'YE'|'ZM'|'ZW',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type PhoneNumberTypes: list
    :param PhoneNumberTypes: The type of phone number.\n\n(string) --\n\n

    :type PhoneNumberCountryCodes: list
    :param PhoneNumberCountryCodes: The ISO country code.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximimum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'PhoneNumberSummaryList': [
        {
            'Id': 'string',
            'Arn': 'string',
            'PhoneNumber': 'string',
            'PhoneNumberType': 'TOLL_FREE'|'DID',
            'PhoneNumberCountryCode': 'AF'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BA'|'BW'|'BR'|'IO'|'VG'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CK'|'CR'|'HR'|'CU'|'CW'|'CY'|'CZ'|'CD'|'DK'|'DJ'|'DM'|'DO'|'TL'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'PF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'CI'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'AN'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'KP'|'MP'|'NO'|'OM'|'PK'|'PW'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'CG'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'KR'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'VI'|'UG'|'UA'|'AE'|'GB'|'US'|'UY'|'UZ'|'VU'|'VA'|'VE'|'VN'|'WF'|'EH'|'YE'|'ZM'|'ZW'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

PhoneNumberSummaryList (list) --
Information about the phone numbers.

(dict) --
Contains summary information about a phone number for a contact center.

Id (string) --
The identifier of the phone number.

Arn (string) --
The Amazon Resource Name (ARN) of the phone number.

PhoneNumber (string) --
The phone number.

PhoneNumberType (string) --
The type of phone number.

PhoneNumberCountryCode (string) --
The ISO country code.





NextToken (string) --
If there are additional results, this is the token for the next set of results.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'PhoneNumberSummaryList': [
            {
                'Id': 'string',
                'Arn': 'string',
                'PhoneNumber': 'string',
                'PhoneNumberType': 'TOLL_FREE'|'DID',
                'PhoneNumberCountryCode': 'AF'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BA'|'BW'|'BR'|'IO'|'VG'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CK'|'CR'|'HR'|'CU'|'CW'|'CY'|'CZ'|'CD'|'DK'|'DJ'|'DM'|'DO'|'TL'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'PF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'CI'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'AN'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'KP'|'MP'|'NO'|'OM'|'PK'|'PW'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'CG'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'KR'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'VI'|'UG'|'UA'|'AE'|'GB'|'US'|'UY'|'UZ'|'VU'|'VA'|'VE'|'VN'|'WF'|'EH'|'YE'|'ZM'|'ZW'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def list_queues(InstanceId=None, QueueTypes=None, NextToken=None, MaxResults=None):
    """
    Provides information about the queues for the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_queues(
        InstanceId='string',
        QueueTypes=[
            'STANDARD'|'AGENT',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type QueueTypes: list
    :param QueueTypes: The type of queue.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximimum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'QueueSummaryList': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string',
            'QueueType': 'STANDARD'|'AGENT'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

QueueSummaryList (list) --
Information about the queues.

(dict) --
Contains summary information about a queue.

Id (string) --
The identifier of the queue.

Arn (string) --
The Amazon Resource Name (ARN) of the queue.

Name (string) --
The name of the queue.

QueueType (string) --
The type of queue.





NextToken (string) --
If there are additional results, this is the token for the next set of results.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'QueueSummaryList': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'QueueType': 'STANDARD'|'AGENT'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def list_routing_profiles(InstanceId=None, NextToken=None, MaxResults=None):
    """
    Provides summary information about the routing profiles for the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_routing_profiles(
        InstanceId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximimum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'RoutingProfileSummaryList': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RoutingProfileSummaryList (list) --
Information about the routing profiles.

(dict) --
Contains summary information about a routing profile.

Id (string) --
The identifier of the routing profile.

Arn (string) --
The Amazon Resource Name (ARN) of the routing profile.

Name (string) --
The name of the routing profile.





NextToken (string) --
If there are additional results, this is the token for the next set of results.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'RoutingProfileSummaryList': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def list_security_profiles(InstanceId=None, NextToken=None, MaxResults=None):
    """
    Provides summary information about the security profiles for the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_security_profiles(
        InstanceId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximimum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'SecurityProfileSummaryList': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

SecurityProfileSummaryList (list) --
Information about the security profiles.

(dict) --
Contains information about a security profile.

Id (string) --
The identifier of the security profile.

Arn (string) --
The Amazon Resource Name (ARN) of the security profile.

Name (string) --
The name of the security profile.





NextToken (string) --
If there are additional results, this is the token for the next set of results.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'SecurityProfileSummaryList': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Lists the tags for the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
tags (dict) --Information about the tags.

(string) --
(string) --









Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.InternalServiceException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.InternalServiceException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    
    """
    pass

def list_user_hierarchy_groups(InstanceId=None, NextToken=None, MaxResults=None):
    """
    Provides summary information about the hierarchy groups for the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_user_hierarchy_groups(
        InstanceId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximimum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'UserHierarchyGroupSummaryList': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

UserHierarchyGroupSummaryList (list) --
Information about the hierarchy groups.

(dict) --
Contains summary information about a hierarchy group.

Id (string) --
The identifier of the hierarchy group.

Arn (string) --
The Amazon Resource Name (ARN) of the hierarchy group.

Name (string) --
The name of the hierarchy group.





NextToken (string) --
If there are additional results, this is the token for the next set of results.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'UserHierarchyGroupSummaryList': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def list_users(InstanceId=None, NextToken=None, MaxResults=None):
    """
    Provides summary information about the users for the specified Amazon Connect instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_users(
        InstanceId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type NextToken: string
    :param NextToken: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximimum number of results to return per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'UserSummaryList': [
        {
            'Id': 'string',
            'Arn': 'string',
            'Username': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

UserSummaryList (list) --
Information about the users.

(dict) --
Contains summary information about a user.

Id (string) --
The identifier of the user account.

Arn (string) --
The Amazon Resource Name (ARN) of the user account.

Username (string) --
The Amazon Connect user name of the user account.





NextToken (string) --
If there are additional results, this is the token for the next set of results.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.ThrottlingException
Connect.Client.exceptions.InternalServiceException


    :return: {
        'UserSummaryList': [
            {
                'Id': 'string',
                'Arn': 'string',
                'Username': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def start_chat_contact(InstanceId=None, ContactFlowId=None, Attributes=None, ParticipantDetails=None, InitialMessage=None, ClientToken=None):
    """
    Initiates a contact flow to start a new chat for the customer. Response of this API provides a token required to obtain credentials from the CreateParticipantConnection API in the Amazon Connect Participant Service.
    When a new chat contact is successfully created, clients need to subscribe to the participant\xe2\x80\x99s connection for the created chat within 5 minutes. This is achieved by invoking CreateParticipantConnection with WEBSOCKET and CONNECTION_CREDENTIALS.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_chat_contact(
        InstanceId='string',
        ContactFlowId='string',
        Attributes={
            'string': 'string'
        },
        ParticipantDetails={
            'DisplayName': 'string'
        },
        InitialMessage={
            'ContentType': 'string',
            'Content': 'string'
        },
        ClientToken='string'
    )
    
    
    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type ContactFlowId: string
    :param ContactFlowId: [REQUIRED]\nThe identifier of the contact flow for the chat.\n

    :type Attributes: dict
    :param Attributes: A custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in contact flows just like any other contact attributes.\nThere can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.\n\n(string) --\n(string) --\n\n\n\n

    :type ParticipantDetails: dict
    :param ParticipantDetails: [REQUIRED]\nInformation identifying the participant.\n\nDisplayName (string) -- [REQUIRED]Display name of the participant.\n\n\n

    :type InitialMessage: dict
    :param InitialMessage: The initial message to be sent to the newly created chat.\n\nContentType (string) -- [REQUIRED]The type of the content. Supported types are text/plain.\n\nContent (string) -- [REQUIRED]The content of the chat message.\n\n\n

    :type ClientToken: string
    :param ClientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContactId': 'string',
    'ParticipantId': 'string',
    'ParticipantToken': 'string'
}


Response Structure

(dict) --

ContactId (string) --
The identifier of this contact within the Amazon Connect instance.

ParticipantId (string) --
The identifier for a chat participant. The participantId for a chat participant is the same throughout the chat lifecycle.

ParticipantToken (string) --
The token used by the chat participant to call CreateParticipantConnection . The participant token is valid for the lifetime of a chat participant.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.InternalServiceException
Connect.Client.exceptions.LimitExceededException


    :return: {
        'ContactId': 'string',
        'ParticipantId': 'string',
        'ParticipantToken': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.InternalServiceException
    Connect.Client.exceptions.LimitExceededException
    
    """
    pass

def start_outbound_voice_contact(DestinationPhoneNumber=None, ContactFlowId=None, InstanceId=None, ClientToken=None, SourcePhoneNumber=None, QueueId=None, Attributes=None):
    """
    Initiates a contact flow to place an outbound call to a customer.
    There is a 60 second dialing timeout for this operation. If the call is not connected after 60 seconds, it fails.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param DestinationPhoneNumber: [REQUIRED]\nThe phone number of the customer, in E.164 format.\n

    :type ContactFlowId: string
    :param ContactFlowId: [REQUIRED]\nThe identifier of the contact flow for the outbound call.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type ClientToken: string
    :param ClientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned. If the contact is disconnected, a new contact is started.\nThis field is autopopulated if not provided.\n

    :type SourcePhoneNumber: string
    :param SourcePhoneNumber: The phone number associated with the Amazon Connect instance, in E.164 format. If you do not specify a source phone number, you must specify a queue.

    :type QueueId: string
    :param QueueId: The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the contact flow is used. If you do not specify a queue, you must specify a source phone number.

    :type Attributes: dict
    :param Attributes: A custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in contact flows just like any other contact attributes.\nThere can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContactId': 'string'
}


Response Structure

(dict) --

ContactId (string) --
The identifier of this contact within the Amazon Connect instance.







Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.InternalServiceException
Connect.Client.exceptions.LimitExceededException
Connect.Client.exceptions.DestinationNotAllowedException
Connect.Client.exceptions.OutboundContactNotPermittedException


    :return: {
        'ContactId': 'string'
    }
    
    
    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.InternalServiceException
    Connect.Client.exceptions.LimitExceededException
    Connect.Client.exceptions.DestinationNotAllowedException
    Connect.Client.exceptions.OutboundContactNotPermittedException
    
    """
    pass

def stop_contact(ContactId=None, InstanceId=None):
    """
    Ends the specified contact.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_contact(
        ContactId='string',
        InstanceId='string'
    )
    
    
    :type ContactId: string
    :param ContactId: [REQUIRED]\nThe ID of the contact.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.ContactNotFoundException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.InternalServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds the specified tags to the specified resource.
    The supported resource type is users.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type tags: dict
    :param tags: [REQUIRED]\nOne or more tags. For example, { 'tags': {'key1':'value1', 'key2':'value2'} }.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.InternalServiceException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes the specified tags from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe tag keys.\n\n(string) --\n\n

    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.InternalServiceException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    
    """
    pass

def update_contact_attributes(InitialContactId=None, InstanceId=None, Attributes=None):
    """
    Creates or updates the contact attributes associated with the specified contact.
    You can add or update attributes for both ongoing and completed contacts. For example, you can update the customer\'s name or the reason the customer called while the call is active, or add notes about steps that the agent took during the call that are displayed to the next agent that takes the call. You can also update attributes for a contact using data from your CRM application and save the data with the contact in Amazon Connect. You could also flag calls for additional analysis, such as legal review or identifying abusive callers.
    Contact attributes are available in Amazon Connect for 24 months, and are then deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_contact_attributes(
        InitialContactId='string',
        InstanceId='string',
        Attributes={
            'string': 'string'
        }
    )
    
    
    :type InitialContactId: string
    :param InitialContactId: [REQUIRED]\nThe identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :type Attributes: dict
    :param Attributes: [REQUIRED]\nThe Amazon Connect attributes. These attributes can be accessed in contact flows just like any other contact attributes.\nYou can have up to 32,768 UTF-8 bytes across all attributes for a contact. Attribute keys can include only alphanumeric, dash, and underscore characters.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Connect.Client.exceptions.InvalidRequestException
Connect.Client.exceptions.InvalidParameterException
Connect.Client.exceptions.ResourceNotFoundException
Connect.Client.exceptions.InternalServiceException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_user_hierarchy(HierarchyGroupId=None, UserId=None, InstanceId=None):
    """
    Assigns the specified hierarchy group to the specified user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_hierarchy(
        HierarchyGroupId='string',
        UserId='string',
        InstanceId='string'
    )
    
    
    :type HierarchyGroupId: string
    :param HierarchyGroupId: The identifier of the hierarchy group.

    :type UserId: string
    :param UserId: [REQUIRED]\nThe identifier of the user account.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def update_user_identity_info(IdentityInfo=None, UserId=None, InstanceId=None):
    """
    Updates the identity information for the specified user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_identity_info(
        IdentityInfo={
            'FirstName': 'string',
            'LastName': 'string',
            'Email': 'string'
        },
        UserId='string',
        InstanceId='string'
    )
    
    
    :type IdentityInfo: dict
    :param IdentityInfo: [REQUIRED]\nThe identity information for the user.\n\nFirstName (string) --The first name. This is required if you are using Amazon Connect or SAML for identity management.\n\nLastName (string) --The last name. This is required if you are using Amazon Connect or SAML for identity management.\n\nEmail (string) --The email address. If you are using SAML for identity management and include this parameter, an error is returned.\n\n\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe identifier of the user account.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def update_user_phone_config(PhoneConfig=None, UserId=None, InstanceId=None):
    """
    Updates the phone configuration settings for the specified user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_phone_config(
        PhoneConfig={
            'PhoneType': 'SOFT_PHONE'|'DESK_PHONE',
            'AutoAccept': True|False,
            'AfterContactWorkTimeLimit': 123,
            'DeskPhoneNumber': 'string'
        },
        UserId='string',
        InstanceId='string'
    )
    
    
    :type PhoneConfig: dict
    :param PhoneConfig: [REQUIRED]\nInformation about phone configuration settings for the user.\n\nPhoneType (string) -- [REQUIRED]The phone type.\n\nAutoAccept (boolean) --The Auto accept setting.\n\nAfterContactWorkTimeLimit (integer) --The After Call Work (ACW) timeout setting, in seconds.\n\nDeskPhoneNumber (string) --The phone number for the user\'s desk phone.\n\n\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe identifier of the user account.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def update_user_routing_profile(RoutingProfileId=None, UserId=None, InstanceId=None):
    """
    Assigns the specified routing profile to the specified user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_routing_profile(
        RoutingProfileId='string',
        UserId='string',
        InstanceId='string'
    )
    
    
    :type RoutingProfileId: string
    :param RoutingProfileId: [REQUIRED]\nThe identifier of the routing profile for the user.\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe identifier of the user account.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

def update_user_security_profiles(SecurityProfileIds=None, UserId=None, InstanceId=None):
    """
    Assigns the specified security profiles to the specified user.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user_security_profiles(
        SecurityProfileIds=[
            'string',
        ],
        UserId='string',
        InstanceId='string'
    )
    
    
    :type SecurityProfileIds: list
    :param SecurityProfileIds: [REQUIRED]\nThe identifiers of the security profiles for the user.\n\n(string) --\n\n

    :type UserId: string
    :param UserId: [REQUIRED]\nThe identifier of the user account.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe identifier of the Amazon Connect instance.\n

    :returns: 
    Connect.Client.exceptions.InvalidRequestException
    Connect.Client.exceptions.InvalidParameterException
    Connect.Client.exceptions.ResourceNotFoundException
    Connect.Client.exceptions.ThrottlingException
    Connect.Client.exceptions.InternalServiceException
    
    """
    pass

