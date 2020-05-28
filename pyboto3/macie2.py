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

def accept_invitation(invitationId=None, masterAccount=None):
    """
    Accepts an Amazon Macie membership invitation that was received from a specific account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_invitation(
        invitationId='string',
        masterAccount='string'
    )
    
    
    :type invitationId: string
    :param invitationId: [REQUIRED]\nThe unique identifier for the invitation to accept.\n

    :type masterAccount: string
    :param masterAccount: [REQUIRED]\nThe AWS account ID for the account that sent the invitation.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The request succeeded and there isn\'t any content to include in the body of the response (No Content).





Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def archive_findings(findingIds=None):
    """
    Archives one or more findings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.archive_findings(
        findingIds=[
            'string',
        ]
    )
    
    
    :type findingIds: list
    :param findingIds: [REQUIRED]\nAn array of strings that lists the unique identifiers for the findings to archive.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded and there isn\'t any content to include in the body of the response (No Content).




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def batch_get_custom_data_identifiers(ids=None):
    """
    Retrieves information about one or more custom data identifiers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_custom_data_identifiers(
        ids=[
            'string',
        ]
    )
    
    
    :type ids: list
    :param ids: An array of strings that lists the unique identifiers for the custom data identifiers to retrieve information about.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'customDataIdentifiers': [
        {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'deleted': True|False,
            'description': 'string',
            'id': 'string',
            'name': 'string'
        },
    ],
    'notFoundIdentifierIds': [
        'string',
    ]
}


Response Structure

(dict) --The request succeeded.

customDataIdentifiers (list) --An array of objects, one for each custom data identifier that meets the criteria specified in the request.

(dict) --Provides information about a custom data identifier.

arn (string) --The Amazon Resource Name (ARN) of the custom data identifier.

createdAt (datetime) --The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created.

deleted (boolean) --Specifies whether the custom data identifier was deleted. If you delete a custom data identifier, Amazon Macie doesn\'t delete it permanently. Instead, it soft deletes the identifier.

description (string) --The custom description of the custom data identifier.

id (string) --The unique identifier for the custom data identifier.

name (string) --The custom name of the custom data identifier.





notFoundIdentifierIds (list) --An array of identifiers, one for each identifier that was specified in the request, but doesn\'t correlate to an existing custom data identifier.

(string) --







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'customDataIdentifiers': [
            {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'deleted': True|False,
                'description': 'string',
                'id': 'string',
                'name': 'string'
            },
        ],
        'notFoundIdentifierIds': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_classification_job(clientToken=None, customDataIdentifierIds=None, description=None, initialRun=None, jobType=None, name=None, s3JobDefinition=None, samplingPercentage=None, scheduleFrequency=None, tags=None):
    """
    Creates and defines the settings for a classification job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_classification_job(
        clientToken='string',
        customDataIdentifierIds=[
            'string',
        ],
        description='string',
        initialRun=True|False,
        jobType='ONE_TIME'|'SCHEDULED',
        name='string',
        s3JobDefinition={
            'bucketDefinitions': [
                {
                    'accountId': 'string',
                    'buckets': [
                        'string',
                    ]
                },
            ],
            'scoping': {
                'excludes': {
                    'and': [
                        {
                            'simpleScopeTerm': {
                                'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                                'key': 'BUCKET_CREATION_DATE'|'OBJECT_EXTENSION'|'OBJECT_LAST_MODIFIED_DATE'|'OBJECT_SIZE'|'TAG',
                                'values': [
                                    'string',
                                ]
                            },
                            'tagScopeTerm': {
                                'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                                'key': 'string',
                                'tagValues': [
                                    {
                                        'key': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'target': 'S3_OBJECT'
                            }
                        },
                    ]
                },
                'includes': {
                    'and': [
                        {
                            'simpleScopeTerm': {
                                'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                                'key': 'BUCKET_CREATION_DATE'|'OBJECT_EXTENSION'|'OBJECT_LAST_MODIFIED_DATE'|'OBJECT_SIZE'|'TAG',
                                'values': [
                                    'string',
                                ]
                            },
                            'tagScopeTerm': {
                                'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                                'key': 'string',
                                'tagValues': [
                                    {
                                        'key': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'target': 'S3_OBJECT'
                            }
                        },
                    ]
                }
            }
        },
        samplingPercentage=123,
        scheduleFrequency={
            'dailySchedule': {}
            ,
            'monthlySchedule': {
                'dayOfMonth': 123
            },
            'weeklySchedule': {
                'dayOfWeek': 'SUNDAY'|'MONDAY'|'TUESDAY'|'WEDNESDAY'|'THURSDAY'|'FRIDAY'|'SATURDAY'
            }
        },
        tags={
            'string': 'string'
        }
    )
    
    
    :type clientToken: string
    :param clientToken: [REQUIRED]\nA unique, case-sensitive token that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type customDataIdentifierIds: list
    :param customDataIdentifierIds: The custom data identifiers to use for data analysis and classification.\n\n(string) --\n\n

    :type description: string
    :param description: A custom description of the job. The description can contain as many as 512 characters.

    :type initialRun: boolean
    :param initialRun: Specifies whether to run the job immediately, after it\'s created.

    :type jobType: string
    :param jobType: [REQUIRED]\nThe schedule for running the job. Valid values are:\n\nONE_TIME - Run the job only once. If you specify this value, don\'t specify a value for the scheduleFrequency property.\nSCHEDULED - Run the job on a daily, weekly, or monthly basis. If you specify this value, use the scheduleFrequency property to define the recurrence pattern for the job.\n\n

    :type name: string
    :param name: [REQUIRED]\nA custom name for the job. The name must contain at least 3 characters and can contain as many as 64 characters.\n

    :type s3JobDefinition: dict
    :param s3JobDefinition: [REQUIRED]\nThe S3 buckets that contain the objects to analyze, and the scope of that analysis.\n\nbucketDefinitions (list) --An array of objects, one for each bucket that contains objects to analyze.\n\n(dict) --Specifies which S3 buckets contain the objects that a classification job analyzes.\n\naccountId (string) --The unique identifier for the AWS account that owns one or more of the buckets. If specified, the job analyzes objects in all the buckets that are owned by the account and meet other conditions specified for the job.\n\nbuckets (list) --An array that lists the names of the buckets.\n\n(string) --\n\n\n\n\n\n\nscoping (dict) --A JobScopeTerm object that specifies conditions for including or excluding objects from the job.\n\nexcludes (dict) --Reserved for future use.\n\nand (list) --Reserved for future use.\n\n(dict) --Specifies one or more conditions that determine which objects a classification job analyzes.\n\nsimpleScopeTerm (dict) --A property-based condition that defines a property, operator, and one or more values for including or excluding an object from a job.\n\ncomparator (string) --The operator to use in the condition.\n\nkey (string) --The property to use in the condition.\n\nvalues (list) --An array that lists one or more values to use in the condition.\n\n(string) --\n\n\n\n\ntagScopeTerm (dict) --A tag-based condition that defines a property, operator, and one or more values for including or excluding an object from a job.\n\ncomparator (string) --The operator to use in the condition.\n\nkey (string) --The tag key to use in the condition.\n\ntagValues (list) --The tag key and value pairs to use in the condition.\n\n(dict) --Specifies a tag key and value, as a pair, to use in a tag-based condition for a classification job.\n\nkey (string) --The value for the tag key to use in the condition.\n\nvalue (string) --The tag value, associated with the specified tag key, to use in the condition.\n\n\n\n\n\ntarget (string) --The type of object to apply the condition to.\n\n\n\n\n\n\n\n\n\nincludes (dict) --Reserved for future use.\n\nand (list) --Reserved for future use.\n\n(dict) --Specifies one or more conditions that determine which objects a classification job analyzes.\n\nsimpleScopeTerm (dict) --A property-based condition that defines a property, operator, and one or more values for including or excluding an object from a job.\n\ncomparator (string) --The operator to use in the condition.\n\nkey (string) --The property to use in the condition.\n\nvalues (list) --An array that lists one or more values to use in the condition.\n\n(string) --\n\n\n\n\ntagScopeTerm (dict) --A tag-based condition that defines a property, operator, and one or more values for including or excluding an object from a job.\n\ncomparator (string) --The operator to use in the condition.\n\nkey (string) --The tag key to use in the condition.\n\ntagValues (list) --The tag key and value pairs to use in the condition.\n\n(dict) --Specifies a tag key and value, as a pair, to use in a tag-based condition for a classification job.\n\nkey (string) --The value for the tag key to use in the condition.\n\nvalue (string) --The tag value, associated with the specified tag key, to use in the condition.\n\n\n\n\n\ntarget (string) --The type of object to apply the condition to.\n\n\n\n\n\n\n\n\n\n\n\n\n

    :type samplingPercentage: integer
    :param samplingPercentage: The sampling depth, as a percentage, to apply when processing objects. This value determines the percentage of eligible objects that the job analyzes. If the value is less than 100, Amazon Macie randomly selects the objects to analyze, up to the specified percentage.

    :type scheduleFrequency: dict
    :param scheduleFrequency: The recurrence pattern for running the job. To run the job only once, don\'t specify a value for this property and set the value of the jobType property to ONE_TIME.\n\ndailySchedule (dict) --Run the job once a day, every day. If specified, this is an empty object.\n\nmonthlySchedule (dict) --Run the job once a month, on a specific day of the month. This value can be an integer from 1 through 30.\n\ndayOfMonth (integer) --Run the job once a month, on a specific day of the month. This value can be an integer from 1 through 30.\n\n\n\nweeklySchedule (dict) --Run the job once a week, on a specific day of the week. Valid values are: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, and SUNDAY.\n\ndayOfWeek (string) --Run the job once a week, on a specific day of the week. Valid values are: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, and SUNDAY.\n\n\n\n\n

    :type tags: dict
    :param tags: A map of key-value pairs that specifies the tags to associate with the job.\nA job can have a maximum of 50 tags. Each tag consists of a required tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobArn': 'string',
    'jobId': 'string'
}


Response Structure

(dict) --
The request succeeded. The specified job was created.

jobArn (string) --
The Amazon Resource Name (ARN) of the job.

jobId (string) --
The unique identifier for the job.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'jobArn': 'string',
        'jobId': 'string'
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def create_custom_data_identifier(clientToken=None, description=None, ignoreWords=None, keywords=None, maximumMatchDistance=None, name=None, regex=None, tags=None):
    """
    Creates and defines the criteria and other settings for a custom data identifier.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_custom_data_identifier(
        clientToken='string',
        description='string',
        ignoreWords=[
            'string',
        ],
        keywords=[
            'string',
        ],
        maximumMatchDistance=123,
        name='string',
        regex='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type clientToken: string
    :param clientToken: A unique, case-sensitive token that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type description: string
    :param description: A custom description of the custom data identifier. The description can contain up to 120 characters.\nWe strongly recommend that you avoid including any sensitive data in the description of a custom data identifier. Other users of your account might be able to see the identifier\'s description, depending on the actions that they\'re allowed to perform in Amazon Macie.\n

    :type ignoreWords: list
    :param ignoreWords: An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4 - 90 characters.\n\n(string) --\n\n

    :type keywords: list
    :param keywords: An array that lists specific character sequences (keywords), one of which must be within proximity (maximumMatchDistance) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 4 - 90 characters.\n\n(string) --\n\n

    :type maximumMatchDistance: integer
    :param maximumMatchDistance: The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the keywords array. Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1 - 300 characters. The default value is 300.

    :type name: string
    :param name: A custom name for the custom data identifier. The name can contain as many as 120 characters.\nWe strongly recommend that you avoid including any sensitive data in the name of a custom data identifier. Other users of your account might be able to see the identifier\'s name, depending on the actions that they\'re allowed to perform in Amazon Macie.\n

    :type regex: string
    :param regex: The regular expression (regex) that defines the pattern to match. The expression can contain as many as 500 characters.

    :type tags: dict
    :param tags: A map of key-value pairs that specifies the tags to associate with the custom data identifier.\nA custom data identifier can have a maximum of 50 tags. Each tag consists of a required tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'customDataIdentifierId': 'string'
}


Response Structure

(dict) --
The request succeeded. The specified custom data identifier was created.

customDataIdentifierId (string) --
The unique identifier for the custom data identifier that was created.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'customDataIdentifierId': 'string'
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def create_findings_filter(action=None, clientToken=None, description=None, findingCriteria=None, name=None, position=None, tags=None):
    """
    Creates and defines the criteria and other settings for a findings filter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_findings_filter(
        action='ARCHIVE'|'NOOP',
        clientToken='string',
        description='string',
        findingCriteria={
            'criterion': {
                'string': {
                    'eq': [
                        'string',
                    ],
                    'gt': 123,
                    'gte': 123,
                    'lt': 123,
                    'lte': 123,
                    'neq': [
                        'string',
                    ]
                }
            }
        },
        name='string',
        position=123,
        tags={
            'string': 'string'
        }
    )
    
    
    :type action: string
    :param action: [REQUIRED]\nThe action to perform on findings that meet the filter criteria (findingCriteria). Valid values are: ARCHIVE, automatically archive the findings; and, NOOP, don\'t perform any action on the findings.\n

    :type clientToken: string
    :param clientToken: A unique, case-sensitive token that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type description: string
    :param description: A custom description of the filter. The description can contain as many as 512 characters.\nWe strongly recommend that you avoid including any sensitive data in the description of a filter. Other users of your account might be able to see the filter\'s description, depending on the actions that they\'re allowed to perform in Amazon Macie.\n

    :type findingCriteria: dict
    :param findingCriteria: [REQUIRED]\nThe criteria to use to filter findings.\n\ncriterion (dict) --A condition that specifies the property, operator, and value to use to filter the results.\n\n(string) --\n(dict) --Specifies the operator to use in a property-based condition that filters the results of a query for findings.\n\neq (list) --An equal to condition to apply to a specified property value for findings.\n\n(string) --\n\n\ngt (integer) --A greater than condition to apply to a specified property value for findings.\n\ngte (integer) --A greater than or equal to condition to apply to a specified property value for findings.\n\nlt (integer) --A less than condition to apply to a specified property value for findings.\n\nlte (integer) --A less than or equal to condition to apply to a specified property value for findings.\n\nneq (list) --A not equal to condition to apply to a specified property value for findings.\n\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type name: string
    :param name: [REQUIRED]\nA custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters.\nWe strongly recommend that you avoid including any sensitive data in the name of a filter. Other users of your account might be able to see the filter\'s name, depending on the actions that they\'re allowed to perform in Amazon Macie.\n

    :type position: integer
    :param position: The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.

    :type tags: dict
    :param tags: A map of key-value pairs that specifies the tags to associate with the filter.\nA findings filter can have a maximum of 50 tags. Each tag consists of a required tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'id': 'string'
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the filter that was created.

id (string) --
The unique identifier for the filter that was created.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'arn': 'string',
        'id': 'string'
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def create_invitations(accountIds=None, disableEmailNotification=None, message=None):
    """
    Sends an Amazon Macie membership invitation to one or more accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_invitations(
        accountIds=[
            'string',
        ],
        disableEmailNotification=True|False,
        message='string'
    )
    
    
    :type accountIds: list
    :param accountIds: [REQUIRED]\nAn array that lists AWS account IDs, one for each account to send the invitation to.\n\n(string) --\n\n

    :type disableEmailNotification: boolean
    :param disableEmailNotification: Specifies whether to send an email notification to the root user of each account that the invitation will be sent to. This notification is in addition to an alert that the root user receives in AWS Personal Health Dashboard. To send an email notification to the root user of each account, set this value to true.

    :type message: string
    :param message: A custom message to include in the invitation. Amazon Macie adds this message to the standard content that it sends for an invitation.

    :rtype: dict

ReturnsResponse Syntax
{
    'unprocessedAccounts': [
        {
            'accountId': 'string',
            'errorCode': 'ClientError'|'InternalError',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
The request succeeded. Processing might not be complete.

unprocessedAccounts (list) --
An array of objects, one for each account whose invitation hasn\'t been processed. Each object identifies the account and explains why the invitation hasn\'t been processed for the account.

(dict) --
Provides information about an account-related request that hasn\'t been processed.

accountId (string) --
The AWS account ID for the account that the request applies to.

errorCode (string) --
The source of the issue or delay in processing the request.

errorMessage (string) --
The reason why the request hasn\'t been processed.











Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'unprocessedAccounts': [
            {
                'accountId': 'string',
                'errorCode': 'ClientError'|'InternalError',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def create_member(account=None, tags=None):
    """
    Associates an account with an Amazon Macie master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_member(
        account={
            'accountId': 'string',
            'email': 'string'
        },
        tags={
            'string': 'string'
        }
    )
    
    
    :type account: dict
    :param account: [REQUIRED]\nThe details for the account to associate with the master account.\n\naccountId (string) -- [REQUIRED]The AWS account ID for the account.\n\nemail (string) -- [REQUIRED]The email address for the account.\n\n\n

    :type tags: dict
    :param tags: A map of key-value pairs that specifies the tags to associate with the account in Amazon Macie.\nAn account can have a maximum of 50 tags. Each tag consists of a required tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string'
}


Response Structure

(dict) --
The request succeeded.

arn (string) --
The Amazon Resource Name (ARN) of the account that was associated with the master account.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'arn': 'string'
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def create_sample_findings(findingTypes=None):
    """
    Creates sample findings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_sample_findings(
        findingTypes=[
            'SensitiveData:S3Object/Multiple'|'SensitiveData:S3Object/Financial'|'SensitiveData:S3Object/Personal'|'SensitiveData:S3Object/Credentials'|'SensitiveData:S3Object/CustomIdentifier'|'Policy:IAMUser/S3BucketPublic'|'Policy:IAMUser/S3BucketSharedExternally'|'Policy:IAMUser/S3BucketReplicatedExternally'|'Policy:IAMUser/S3BucketEncryptionDisabled'|'Policy:IAMUser/S3BlockPublicAccessDisabled',
        ]
    )
    
    
    :type findingTypes: list
    :param findingTypes: An array that lists one or more types of findings to include in the set of sample findings. Currently, the only supported value is Policy:IAMUser/S3BucketEncryptionDisabled.\n\n(string) --The type of finding. Valid values are:\n\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded and there isn\'t any content to include in the body of the response (No Content).




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    """
    pass

def decline_invitations(accountIds=None):
    """
    Declines Amazon Macie membership invitations that were received from specific accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.decline_invitations(
        accountIds=[
            'string',
        ]
    )
    
    
    :type accountIds: list
    :param accountIds: [REQUIRED]\nAn array that lists AWS account IDs, one for each account that sent an invitation to decline.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'unprocessedAccounts': [
        {
            'accountId': 'string',
            'errorCode': 'ClientError'|'InternalError',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --The request succeeded. Processing might not be complete.

unprocessedAccounts (list) --An array of objects, one for each account whose invitation hasn\'t been declined. Each object identifies the account and explains why the request hasn\'t been processed for that account.

(dict) --Provides information about an account-related request that hasn\'t been processed.

accountId (string) --The AWS account ID for the account that the request applies to.

errorCode (string) --The source of the issue or delay in processing the request.

errorMessage (string) --The reason why the request hasn\'t been processed.










Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'unprocessedAccounts': [
            {
                'accountId': 'string',
                'errorCode': 'ClientError'|'InternalError',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def delete_custom_data_identifier(id=None):
    """
    Deletes a custom data identifier.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_custom_data_identifier(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe unique identifier for the Amazon Macie resource or account that the request applies to.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded. The specified custom data identifier was deleted and there isn\'t any content to include in the body of the response (No Content).




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    """
    pass

def delete_findings_filter(id=None):
    """
    Deletes a findings filter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_findings_filter(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe unique identifier for the Amazon Macie resource or account that the request applies to.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded. The specified findings filter was deleted and there isn\'t any content to include in the body of the response (No Content).




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    """
    pass

def delete_invitations(accountIds=None):
    """
    Deletes Amazon Macie membership invitations that were received from specific accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_invitations(
        accountIds=[
            'string',
        ]
    )
    
    
    :type accountIds: list
    :param accountIds: [REQUIRED]\nAn array that lists AWS account IDs, one for each account that sent an invitation to delete.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'unprocessedAccounts': [
        {
            'accountId': 'string',
            'errorCode': 'ClientError'|'InternalError',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --The request succeeded. Processing might not be complete.

unprocessedAccounts (list) --An array of objects, one for each account whose invitation hasn\'t been deleted. Each object identifies the account and explains why the request hasn\'t been processed for that account.

(dict) --Provides information about an account-related request that hasn\'t been processed.

accountId (string) --The AWS account ID for the account that the request applies to.

errorCode (string) --The source of the issue or delay in processing the request.

errorMessage (string) --The reason why the request hasn\'t been processed.










Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'unprocessedAccounts': [
            {
                'accountId': 'string',
                'errorCode': 'ClientError'|'InternalError',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def delete_member(id=None):
    """
    Deletes the association between an Amazon Macie master account and an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_member(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe unique identifier for the Amazon Macie resource or account that the request applies to.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded. The association was deleted and there isn\'t any content to include in the body of the response (No Content).




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    """
    pass

def describe_buckets(criteria=None, maxResults=None, nextToken=None, sortCriteria=None):
    """
    Retrieves (queries) statistical data and other information about one or more S3 buckets that Amazon Macie monitors and analyzes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_buckets(
        criteria={
            'string': {
                'eq': [
                    'string',
                ],
                'gt': 123,
                'gte': 123,
                'lt': 123,
                'lte': 123,
                'neq': [
                    'string',
                ],
                'prefix': 'string'
            }
        },
        maxResults=123,
        nextToken='string',
        sortCriteria={
            'attributeName': 'string',
            'orderBy': 'ASC'|'DESC'
        }
    )
    
    
    :type criteria: dict
    :param criteria: The criteria to use to filter the query results.\n\n(string) --\n(dict) --Specifies the operator to use in an attribute-based condition that filters the results of a query for information about S3 buckets.\n\neq (list) --An equal to condition to apply to a specified attribute value for buckets.\n\n(string) --\n\n\ngt (integer) --A greater than condition to apply to a specified attribute value for buckets.\n\ngte (integer) --A greater than or equal to condition to apply to a specified attribute value for buckets.\n\nlt (integer) --A less than condition to apply to a specified attribute value for buckets.\n\nlte (integer) --A less than or equal to condition to apply to a specified attribute value for buckets.\n\nneq (list) --A not equal to condition to apply to a specified attribute value for buckets.\n\n(string) --\n\n\nprefix (string) --The prefix of the buckets to include in the results.\n\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of items to include in each page of the response. The default value is 50.

    :type nextToken: string
    :param nextToken: The nextToken string that specifies which page of results to return in a paginated response.

    :type sortCriteria: dict
    :param sortCriteria: The criteria to use to sort the query results.\n\nattributeName (string) --The name of the attribute to sort the results by. This value can be the name of any property that Amazon Macie defines as bucket metadata, such as bucketName, accountId, or lastUpdated.\n\norderBy (string) --The sort order to apply to the results, based on the value for the property specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'buckets': [
        {
            'accountId': 'string',
            'bucketArn': 'string',
            'bucketCreatedAt': datetime(2015, 1, 1),
            'bucketName': 'string',
            'classifiableObjectCount': 123,
            'lastUpdated': datetime(2015, 1, 1),
            'objectCount': 123,
            'objectCountByEncryptionType': {
                'customerManaged': 123,
                'kmsManaged': 123,
                's3Managed': 123,
                'unencrypted': 123
            },
            'publicAccess': {
                'effectivePermission': 'PUBLIC'|'NOT_PUBLIC',
                'permissionConfiguration': {
                    'accountLevelPermissions': {
                        'blockPublicAccess': {
                            'blockPublicAcls': True|False,
                            'blockPublicPolicy': True|False,
                            'ignorePublicAcls': True|False,
                            'restrictPublicBuckets': True|False
                        }
                    },
                    'bucketLevelPermissions': {
                        'accessControlList': {
                            'allowsPublicReadAccess': True|False,
                            'allowsPublicWriteAccess': True|False
                        },
                        'blockPublicAccess': {
                            'blockPublicAcls': True|False,
                            'blockPublicPolicy': True|False,
                            'ignorePublicAcls': True|False,
                            'restrictPublicBuckets': True|False
                        },
                        'bucketPolicy': {
                            'allowsPublicReadAccess': True|False,
                            'allowsPublicWriteAccess': True|False
                        }
                    }
                }
            },
            'region': 'string',
            'replicationDetails': {
                'replicated': True|False,
                'replicatedExternally': True|False,
                'replicationAccounts': [
                    'string',
                ]
            },
            'sharedAccess': 'EXTERNAL'|'INTERNAL'|'NOT_SHARED',
            'sizeInBytes': 123,
            'sizeInBytesCompressed': 123,
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'versioning': True|False
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The request succeeded.

buckets (list) --
An array of objects, one for each bucket that meets the filter criteria specified in the request.

(dict) --
Provides information about an S3 bucket that Amazon Macie monitors and analyzes.

accountId (string) --
The unique identifier for the AWS account that\'s associated with the bucket.

bucketArn (string) --
The Amazon Resource Name (ARN) of the bucket.

bucketCreatedAt (datetime) --
The date and time, in UTC and extended ISO 8601 format, when the bucket was created.

bucketName (string) --
The name of the bucket.

classifiableObjectCount (integer) --
The total number of objects that Amazon Macie can monitor and analyze in the bucket. These objects use a file format, file extension, or content type that Amazon Macie supports.

lastUpdated (datetime) --
The date and time, in UTC and extended ISO 8601 format, when Amazon Macie last analyzed the bucket.

objectCount (integer) --
The total number of objects in the bucket.

objectCountByEncryptionType (dict) --
The total number of objects that are in the bucket, grouped by server-side encryption type. This includes a grouping that reports the total number of objects that aren\'t encrypted.

customerManaged (integer) --
Reserved for future use.

kmsManaged (integer) --
Reserved for future use.

s3Managed (integer) --
Reserved for future use.

unencrypted (integer) --
Reserved for future use.



publicAccess (dict) --
Specifies whether the bucket is publicly accessible. If this value is true, an access control list (ACL), bucket policy, or block public access settings allow the bucket to be accessed by the general public.

effectivePermission (string) --
Specifies whether the bucket is publicly accessible due to the combination of permissions settings that apply to the bucket. Possible values are: PUBLIC, the bucket is publicly accessible; and, NOT_PUBLIC, the bucket isn\'t publicly accessible.

permissionConfiguration (dict) --
The account-level and bucket-level permissions for the bucket.

accountLevelPermissions (dict) --
The account-level permissions settings that apply to the bucket.

blockPublicAccess (dict) --
The block public access settings for the bucket.

blockPublicAcls (boolean) --
Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket.

blockPublicPolicy (boolean) --
Specifies whether Amazon S3 blocks public bucket policies for the bucket.

ignorePublicAcls (boolean) --
Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket.

restrictPublicBuckets (boolean) --
Specifies whether Amazon S3 restricts public bucket policies for the bucket.





bucketLevelPermissions (dict) --
The bucket-level permissions settings for the bucket.

accessControlList (dict) --
The permissions settings of the access control list (ACL) for the bucket. This value is null if an ACL hasn\'t been defined for the bucket.

allowsPublicReadAccess (boolean) --
Specifies whether the ACL grants the general public with read access permissions for the bucket.

allowsPublicWriteAccess (boolean) --
Specifies whether the ACL grants the general public with write access permissions for the bucket.



blockPublicAccess (dict) --
The block public access settings for the bucket.

blockPublicAcls (boolean) --
Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket.

blockPublicPolicy (boolean) --
Specifies whether Amazon S3 blocks public bucket policies for the bucket.

ignorePublicAcls (boolean) --
Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket.

restrictPublicBuckets (boolean) --
Specifies whether Amazon S3 restricts public bucket policies for the bucket.



bucketPolicy (dict) --
The permissions settings of the bucket policy for the bucket. This value is null if a bucket policy hasn\'t been defined for the bucket.

allowsPublicReadAccess (boolean) --
Specifies whether the bucket policy allows the general public to have read access to the bucket.

allowsPublicWriteAccess (boolean) --
Specifies whether the bucket policy allows the general public to have write access to the bucket.









region (string) --
The AWS Region that hosts the bucket.

replicationDetails (dict) --
Specifies whether the bucket is configured to replicate one or more objects to buckets for other AWS accounts and, if so, which accounts.

replicated (boolean) --
Specifies whether the bucket is configured to replicate one or more objects to any destination.

replicatedExternally (boolean) --
Specifies whether the bucket is configured to replicate one or more objects to an AWS account that isn\'t part of the Amazon Macie organization.

replicationAccounts (list) --
An array of AWS account IDs, one for each AWS account that the bucket is configured to replicate one or more objects to.

(string) --




sharedAccess (string) --
Specifies whether the bucket is shared with another AWS account or configured to support cross-origin resource sharing (CORS). Valid values are:

EXTERNAL - The bucket is shared with an AWS account that isn\xe2\x80\x99t part of the Amazon Macie organization.
INTERNAL - The bucket is shared with an AWS account that\'s part of the Amazon Macie organization.
NOT_SHARED - The bucket isn\'t shared with other AWS accounts.


sizeInBytes (integer) --
The total storage size, in bytes, of the bucket.

sizeInBytesCompressed (integer) --
The total compressed storage size, in bytes, of the bucket.

tags (list) --
An array that specifies the tags (keys and values) that are associated with the bucket.

(dict) --
Provides information about the tags that are associated with an S3 bucket or object. Each tag consists of a required tag key and an associated tag value.

key (string) --
One part of a key-value pair that comprises a tag. A tag key is a general label that acts as a category for more specific tag values.

value (string) --
One part of a key-value pair that comprises a tag. A tag value acts as a descriptor for a tag key. A tag value can be empty or null.





versioning (boolean) --
Specifies whether versioning is enabled for the bucket.





nextToken (string) --
The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'buckets': [
            {
                'accountId': 'string',
                'bucketArn': 'string',
                'bucketCreatedAt': datetime(2015, 1, 1),
                'bucketName': 'string',
                'classifiableObjectCount': 123,
                'lastUpdated': datetime(2015, 1, 1),
                'objectCount': 123,
                'objectCountByEncryptionType': {
                    'customerManaged': 123,
                    'kmsManaged': 123,
                    's3Managed': 123,
                    'unencrypted': 123
                },
                'publicAccess': {
                    'effectivePermission': 'PUBLIC'|'NOT_PUBLIC',
                    'permissionConfiguration': {
                        'accountLevelPermissions': {
                            'blockPublicAccess': {
                                'blockPublicAcls': True|False,
                                'blockPublicPolicy': True|False,
                                'ignorePublicAcls': True|False,
                                'restrictPublicBuckets': True|False
                            }
                        },
                        'bucketLevelPermissions': {
                            'accessControlList': {
                                'allowsPublicReadAccess': True|False,
                                'allowsPublicWriteAccess': True|False
                            },
                            'blockPublicAccess': {
                                'blockPublicAcls': True|False,
                                'blockPublicPolicy': True|False,
                                'ignorePublicAcls': True|False,
                                'restrictPublicBuckets': True|False
                            },
                            'bucketPolicy': {
                                'allowsPublicReadAccess': True|False,
                                'allowsPublicWriteAccess': True|False
                            }
                        }
                    }
                },
                'region': 'string',
                'replicationDetails': {
                    'replicated': True|False,
                    'replicatedExternally': True|False,
                    'replicationAccounts': [
                        'string',
                    ]
                },
                'sharedAccess': 'EXTERNAL'|'INTERNAL'|'NOT_SHARED',
                'sizeInBytes': 123,
                'sizeInBytesCompressed': 123,
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'versioning': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_classification_job(jobId=None):
    """
    Retrieves information about the status and settings for a classification job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_classification_job(
        jobId='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique identifier for the classification job.\n

    :rtype: dict
ReturnsResponse Syntax{
    'clientToken': 'string',
    'createdAt': datetime(2015, 1, 1),
    'customDataIdentifierIds': [
        'string',
    ],
    'description': 'string',
    'initialRun': True|False,
    'jobArn': 'string',
    'jobId': 'string',
    'jobStatus': 'RUNNING'|'PAUSED'|'CANCELLED'|'COMPLETE'|'IDLE',
    'jobType': 'ONE_TIME'|'SCHEDULED',
    'lastRunTime': datetime(2015, 1, 1),
    'name': 'string',
    's3JobDefinition': {
        'bucketDefinitions': [
            {
                'accountId': 'string',
                'buckets': [
                    'string',
                ]
            },
        ],
        'scoping': {
            'excludes': {
                'and': [
                    {
                        'simpleScopeTerm': {
                            'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                            'key': 'BUCKET_CREATION_DATE'|'OBJECT_EXTENSION'|'OBJECT_LAST_MODIFIED_DATE'|'OBJECT_SIZE'|'TAG',
                            'values': [
                                'string',
                            ]
                        },
                        'tagScopeTerm': {
                            'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                            'key': 'string',
                            'tagValues': [
                                {
                                    'key': 'string',
                                    'value': 'string'
                                },
                            ],
                            'target': 'S3_OBJECT'
                        }
                    },
                ]
            },
            'includes': {
                'and': [
                    {
                        'simpleScopeTerm': {
                            'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                            'key': 'BUCKET_CREATION_DATE'|'OBJECT_EXTENSION'|'OBJECT_LAST_MODIFIED_DATE'|'OBJECT_SIZE'|'TAG',
                            'values': [
                                'string',
                            ]
                        },
                        'tagScopeTerm': {
                            'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                            'key': 'string',
                            'tagValues': [
                                {
                                    'key': 'string',
                                    'value': 'string'
                                },
                            ],
                            'target': 'S3_OBJECT'
                        }
                    },
                ]
            }
        }
    },
    'samplingPercentage': 123,
    'scheduleFrequency': {
        'dailySchedule': {},
        'monthlySchedule': {
            'dayOfMonth': 123
        },
        'weeklySchedule': {
            'dayOfWeek': 'SUNDAY'|'MONDAY'|'TUESDAY'|'WEDNESDAY'|'THURSDAY'|'FRIDAY'|'SATURDAY'
        }
    },
    'statistics': {
        'approximateNumberOfObjectsToProcess': 123.0,
        'numberOfRuns': 123.0
    },
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --The request succeeded.

clientToken (string) --The token that was provided to ensure the idempotency of the request to create the job.

createdAt (datetime) --The date and time, in UTC and extended ISO 8601 format, when the job was created.

customDataIdentifierIds (list) --The custom data identifiers that the job uses to analyze data.

(string) --


description (string) --The custom description of the job.

initialRun (boolean) --Specifies whether the job has run for the first time.

jobArn (string) --The Amazon Resource Name (ARN) of the job.

jobId (string) --The unique identifier for the job.

jobStatus (string) --The current status of the job. Possible value are:

CANCELLED - The job was cancelled by you or a user of the master account for your organization. A job might also be cancelled if ownership of an S3 bucket changed while the job was running, and that change affected the job\'s access to the bucket.
COMPLETE - Amazon Macie finished processing all the data specified for the job.
IDLE - For a recurring job, the previous scheduled run is complete and the next scheduled run is pending. This value doesn\'t apply to jobs that occur only once.
PAUSED - Amazon Macie started the job, but completion of the job would exceed one or more quotas for your account.
RUNNING - The job is in progress.


jobType (string) --The schedule for running the job. Possible value are:

ONE_TIME - The job ran or will run only once.
SCHEDULED - The job runs on a daily, weekly, or monthly basis. The scheduleFrequency property indicates the recurrence pattern for the job.


lastRunTime (datetime) --The date and time, in UTC and extended ISO 8601 format, when the job last ran.

name (string) --The custom name of the job.

s3JobDefinition (dict) --The S3 buckets that the job is configured to analyze, and the scope of that analysis.

bucketDefinitions (list) --An array of objects, one for each bucket that contains objects to analyze.

(dict) --Specifies which S3 buckets contain the objects that a classification job analyzes.

accountId (string) --The unique identifier for the AWS account that owns one or more of the buckets. If specified, the job analyzes objects in all the buckets that are owned by the account and meet other conditions specified for the job.

buckets (list) --An array that lists the names of the buckets.

(string) --






scoping (dict) --A JobScopeTerm object that specifies conditions for including or excluding objects from the job.

excludes (dict) --Reserved for future use.

and (list) --Reserved for future use.

(dict) --Specifies one or more conditions that determine which objects a classification job analyzes.

simpleScopeTerm (dict) --A property-based condition that defines a property, operator, and one or more values for including or excluding an object from a job.

comparator (string) --The operator to use in the condition.

key (string) --The property to use in the condition.

values (list) --An array that lists one or more values to use in the condition.

(string) --




tagScopeTerm (dict) --A tag-based condition that defines a property, operator, and one or more values for including or excluding an object from a job.

comparator (string) --The operator to use in the condition.

key (string) --The tag key to use in the condition.

tagValues (list) --The tag key and value pairs to use in the condition.

(dict) --Specifies a tag key and value, as a pair, to use in a tag-based condition for a classification job.

key (string) --The value for the tag key to use in the condition.

value (string) --The tag value, associated with the specified tag key, to use in the condition.





target (string) --The type of object to apply the condition to.









includes (dict) --Reserved for future use.

and (list) --Reserved for future use.

(dict) --Specifies one or more conditions that determine which objects a classification job analyzes.

simpleScopeTerm (dict) --A property-based condition that defines a property, operator, and one or more values for including or excluding an object from a job.

comparator (string) --The operator to use in the condition.

key (string) --The property to use in the condition.

values (list) --An array that lists one or more values to use in the condition.

(string) --




tagScopeTerm (dict) --A tag-based condition that defines a property, operator, and one or more values for including or excluding an object from a job.

comparator (string) --The operator to use in the condition.

key (string) --The tag key to use in the condition.

tagValues (list) --The tag key and value pairs to use in the condition.

(dict) --Specifies a tag key and value, as a pair, to use in a tag-based condition for a classification job.

key (string) --The value for the tag key to use in the condition.

value (string) --The tag value, associated with the specified tag key, to use in the condition.





target (string) --The type of object to apply the condition to.













samplingPercentage (integer) --The sampling depth, as a percentage, that the job applies when it processes objects.

scheduleFrequency (dict) --The recurrence pattern for running the job. If the job is configured to run every day, this value is an empty dailySchedule object. If the job is configured to run only once, this value is null.

dailySchedule (dict) --Run the job once a day, every day. If specified, this is an empty object.

monthlySchedule (dict) --Run the job once a month, on a specific day of the month. This value can be an integer from 1 through 30.

dayOfMonth (integer) --Run the job once a month, on a specific day of the month. This value can be an integer from 1 through 30.



weeklySchedule (dict) --Run the job once a week, on a specific day of the week. Valid values are: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, and SUNDAY.

dayOfWeek (string) --Run the job once a week, on a specific day of the week. Valid values are: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, and SUNDAY.





statistics (dict) --The number of times that the job has run and processing statistics for the job\'s most recent run.

approximateNumberOfObjectsToProcess (float) --The approximate number of objects that the job has yet to process during its current run.

numberOfRuns (float) --The number of times that the job has run.



tags (dict) --A map of key-value pairs that identifies the tags (keys and values) that are associated with the classification job.

(string) --
(string) --









Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'clientToken': 'string',
        'createdAt': datetime(2015, 1, 1),
        'customDataIdentifierIds': [
            'string',
        ],
        'description': 'string',
        'initialRun': True|False,
        'jobArn': 'string',
        'jobId': 'string',
        'jobStatus': 'RUNNING'|'PAUSED'|'CANCELLED'|'COMPLETE'|'IDLE',
        'jobType': 'ONE_TIME'|'SCHEDULED',
        'lastRunTime': datetime(2015, 1, 1),
        'name': 'string',
        's3JobDefinition': {
            'bucketDefinitions': [
                {
                    'accountId': 'string',
                    'buckets': [
                        'string',
                    ]
                },
            ],
            'scoping': {
                'excludes': {
                    'and': [
                        {
                            'simpleScopeTerm': {
                                'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                                'key': 'BUCKET_CREATION_DATE'|'OBJECT_EXTENSION'|'OBJECT_LAST_MODIFIED_DATE'|'OBJECT_SIZE'|'TAG',
                                'values': [
                                    'string',
                                ]
                            },
                            'tagScopeTerm': {
                                'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                                'key': 'string',
                                'tagValues': [
                                    {
                                        'key': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'target': 'S3_OBJECT'
                            }
                        },
                    ]
                },
                'includes': {
                    'and': [
                        {
                            'simpleScopeTerm': {
                                'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                                'key': 'BUCKET_CREATION_DATE'|'OBJECT_EXTENSION'|'OBJECT_LAST_MODIFIED_DATE'|'OBJECT_SIZE'|'TAG',
                                'values': [
                                    'string',
                                ]
                            },
                            'tagScopeTerm': {
                                'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                                'key': 'string',
                                'tagValues': [
                                    {
                                        'key': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'target': 'S3_OBJECT'
                            }
                        },
                    ]
                }
            }
        },
        'samplingPercentage': 123,
        'scheduleFrequency': {
            'dailySchedule': {},
            'monthlySchedule': {
                'dayOfMonth': 123
            },
            'weeklySchedule': {
                'dayOfWeek': 'SUNDAY'|'MONDAY'|'TUESDAY'|'WEDNESDAY'|'THURSDAY'|'FRIDAY'|'SATURDAY'
            }
        },
        'statistics': {
            'approximateNumberOfObjectsToProcess': 123.0,
            'numberOfRuns': 123.0
        },
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    CANCELLED - The job was cancelled by you or a user of the master account for your organization. A job might also be cancelled if ownership of an S3 bucket changed while the job was running, and that change affected the job\'s access to the bucket.
    COMPLETE - Amazon Macie finished processing all the data specified for the job.
    IDLE - For a recurring job, the previous scheduled run is complete and the next scheduled run is pending. This value doesn\'t apply to jobs that occur only once.
    PAUSED - Amazon Macie started the job, but completion of the job would exceed one or more quotas for your account.
    RUNNING - The job is in progress.
    
    """
    pass

def describe_organization_configuration():
    """
    Retrieves information about the Amazon Macie configuration settings for an AWS organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_organization_configuration()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'autoEnable': True|False,
    'maxAccountLimitReached': True|False
}


Response Structure

(dict) --The request succeeded.

autoEnable (boolean) --Specifies whether Amazon Macie is enabled automatically for accounts that are added to the AWS organization.

maxAccountLimitReached (boolean) --Specifies whether the maximum number of Amazon Macie member accounts are already associated with the AWS organization.






Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'autoEnable': True|False,
        'maxAccountLimitReached': True|False
    }
    
    
    """
    pass

def disable_macie():
    """
    Disables an Amazon Macie account and deletes Macie resources for the account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_macie()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded and there isn\'t any content to include in the body of the response (No Content).




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    """
    pass

def disable_organization_admin_account(adminAccountId=None):
    """
    Disables an account as a delegated administrator of Amazon Macie for an AWS organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_organization_admin_account(
        adminAccountId='string'
    )
    
    
    :type adminAccountId: string
    :param adminAccountId: [REQUIRED]\nThe AWS account ID of the delegated administrator account.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded and there isn\'t any content to include in the body of the response (No Content).




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    """
    pass

def disassociate_from_master_account():
    """
    Disassociates a member account from its Amazon Macie master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_from_master_account()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded and there isn\'t any content to include in the body of the response (No Content).




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    """
    pass

def disassociate_member(id=None):
    """
    Disassociates an Amazon Macie master account from a member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_member(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe unique identifier for the Amazon Macie resource or account that the request applies to.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded.




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    """
    pass

def enable_macie(clientToken=None, findingPublishingFrequency=None, status=None):
    """
    Enables Amazon Macie and specifies the configuration settings for a Macie account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_macie(
        clientToken='string',
        findingPublishingFrequency='FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS',
        status='PAUSED'|'ENABLED'
    )
    
    
    :type clientToken: string
    :param clientToken: A unique, case-sensitive token that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :type findingPublishingFrequency: string
    :param findingPublishingFrequency: Specifies how often to publish findings for the account. This includes adding findings to AWS Security Hub and exporting finding events to Amazon CloudWatch.

    :type status: string
    :param status: Specifies the status for the account. To enable Amazon Macie and start all Amazon Macie activities for the account, set this value to ENABLED.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The request succeeded and there isn\'t any content to include in the body of the response (No Content).





Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def enable_organization_admin_account(adminAccountId=None, clientToken=None):
    """
    Enables an account as a delegated administrator of Amazon Macie for an AWS organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_organization_admin_account(
        adminAccountId='string',
        clientToken='string'
    )
    
    
    :type adminAccountId: string
    :param adminAccountId: [REQUIRED]\nThe AWS account ID for the account.\n

    :type clientToken: string
    :param clientToken: A unique, case-sensitive token that you provide to ensure the idempotency of the request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The request succeeded and there isn\'t any content to include in the body of the response (No Content).





Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
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

def get_bucket_statistics(accountId=None):
    """
    Retrieves (queries) aggregated statistical data for all the S3 buckets that Amazon Macie monitors and analyzes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_bucket_statistics(
        accountId='string'
    )
    
    
    :type accountId: string
    :param accountId: The unique identifier for the AWS account.

    :rtype: dict
ReturnsResponse Syntax{
    'bucketCount': 123,
    'bucketCountByEffectivePermission': {
        'publiclyAccessible': 123,
        'publiclyReadable': 123,
        'publiclyWritable': 123
    },
    'bucketCountByEncryptionType': {
        'kmsManaged': 123,
        's3Managed': 123,
        'unencrypted': 123
    },
    'bucketCountBySharedAccessType': {
        'external': 123,
        'internal': 123,
        'notShared': 123
    },
    'classifiableObjectCount': 123,
    'lastUpdated': datetime(2015, 1, 1),
    'objectCount': 123,
    'sizeInBytes': 123,
    'sizeInBytesCompressed': 123
}


Response Structure

(dict) --The request succeeded.

bucketCount (integer) --The total number of buckets.

bucketCountByEffectivePermission (dict) --The total number of buckets that are publicly accessible, based on a combination of permissions settings for each bucket.

publiclyAccessible (integer) --Reserved for future use.

publiclyReadable (integer) --Reserved for future use.

publiclyWritable (integer) --Reserved for future use.



bucketCountByEncryptionType (dict) --The total number of buckets, grouped by server-side encryption type. This object also reports the total number of buckets that aren\'t encrypted.

kmsManaged (integer) --Reserved for future use.

s3Managed (integer) --Reserved for future use.

unencrypted (integer) --Reserved for future use.



bucketCountBySharedAccessType (dict) --The total number of buckets that are shared with another AWS account or configured to support cross-origin resource sharing (CORS).

external (integer) --Reserved for future use.

internal (integer) --Reserved for future use.

notShared (integer) --Reserved for future use.



classifiableObjectCount (integer) --The total number of objects that Amazon Macie can monitor and analyze in all the buckets. These objects use a file format, file extension, or content type that Amazon Macie supports.

lastUpdated (datetime) --The date and time, in UTC and extended ISO 8601 format, when Amazon Macie last analyzed the buckets.

objectCount (integer) --The total number of objects in all the buckets.

sizeInBytes (integer) --The total storage size, in bytes, of all the buckets.

sizeInBytesCompressed (integer) --The total compressed storage size, in bytes, of all the buckets.






Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'bucketCount': 123,
        'bucketCountByEffectivePermission': {
            'publiclyAccessible': 123,
            'publiclyReadable': 123,
            'publiclyWritable': 123
        },
        'bucketCountByEncryptionType': {
            'kmsManaged': 123,
            's3Managed': 123,
            'unencrypted': 123
        },
        'bucketCountBySharedAccessType': {
            'external': 123,
            'internal': 123,
            'notShared': 123
        },
        'classifiableObjectCount': 123,
        'lastUpdated': datetime(2015, 1, 1),
        'objectCount': 123,
        'sizeInBytes': 123,
        'sizeInBytesCompressed': 123
    }
    
    
    """
    pass

def get_classification_export_configuration():
    """
    Retrieves the configuration settings for exporting data classification results.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_classification_export_configuration()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'configuration': {
        's3Destination': {
            'bucketName': 'string',
            'keyPrefix': 'string',
            'kmsKeyArn': 'string'
        }
    }
}


Response Structure

(dict) --The request succeeded.

configuration (dict) --The location that data classification results are exported to, and the encryption settings that are used when storing results in that location.

s3Destination (dict) --The S3 bucket to export data classification results to, and the encryption settings to use when storing results in that bucket.

bucketName (string) --The Amazon Resource Name (ARN) of the bucket. This must be the ARN of an existing bucket.

keyPrefix (string) --The path prefix to use in the path to the location in the bucket. This prefix specifies where to store classification results in the bucket.

kmsKeyArn (string) --The Amazon Resource Name (ARN) of the AWS Key Management Service master key to use for encryption of the exported results. This must be the ARN of an existing KMS key. In addition, the key must be in the same AWS Region as the bucket.










Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'configuration': {
            's3Destination': {
                'bucketName': 'string',
                'keyPrefix': 'string',
                'kmsKeyArn': 'string'
            }
        }
    }
    
    
    """
    pass

def get_custom_data_identifier(id=None):
    """
    Retrieves information about the criteria and other settings for a custom data identifier.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_custom_data_identifier(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe unique identifier for the Amazon Macie resource or account that the request applies to.\n

    :rtype: dict
ReturnsResponse Syntax{
    'arn': 'string',
    'createdAt': datetime(2015, 1, 1),
    'deleted': True|False,
    'description': 'string',
    'id': 'string',
    'ignoreWords': [
        'string',
    ],
    'keywords': [
        'string',
    ],
    'maximumMatchDistance': 123,
    'name': 'string',
    'regex': 'string',
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --The request succeeded.

arn (string) --The Amazon Resource Name (ARN) of the custom data identifier.

createdAt (datetime) --The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created.

deleted (boolean) --Specifies whether the custom data identifier was deleted. If you delete a custom data identifier, Amazon Macie doesn\'t delete it permanently. Instead, it soft deletes the identifier.

description (string) --The custom description of the custom data identifier.

id (string) --The unique identifier for the custom data identifier.

ignoreWords (list) --An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it.

(string) --


keywords (list) --An array that lists specific character sequences (keywords), one of which must be within proximity (maximumMatchDistance) of the regular expression to match.

(string) --


maximumMatchDistance (integer) --The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the keywords array. Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern.

name (string) --The custom name of the custom data identifier.

regex (string) --The regular expression (regex) that defines the pattern to match.

tags (dict) --A map of key-value pairs that identifies the tags (keys and values) that are associated with the custom data identifier.

(string) --
(string) --









Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'arn': 'string',
        'createdAt': datetime(2015, 1, 1),
        'deleted': True|False,
        'description': 'string',
        'id': 'string',
        'ignoreWords': [
            'string',
        ],
        'keywords': [
            'string',
        ],
        'maximumMatchDistance': 123,
        'name': 'string',
        'regex': 'string',
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_finding_statistics(findingCriteria=None, groupBy=None, size=None, sortCriteria=None):
    """
    Retrieves (queries) aggregated statistical data about findings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_finding_statistics(
        findingCriteria={
            'criterion': {
                'string': {
                    'eq': [
                        'string',
                    ],
                    'gt': 123,
                    'gte': 123,
                    'lt': 123,
                    'lte': 123,
                    'neq': [
                        'string',
                    ]
                }
            }
        },
        groupBy='resourcesAffected.s3Bucket.name'|'type'|'classificationDetails.jobId'|'severity.description',
        size=123,
        sortCriteria={
            'attributeName': 'groupKey'|'count',
            'orderBy': 'ASC'|'DESC'
        }
    )
    
    
    :type findingCriteria: dict
    :param findingCriteria: The criteria to use to filter the query results.\n\ncriterion (dict) --A condition that specifies the property, operator, and value to use to filter the results.\n\n(string) --\n(dict) --Specifies the operator to use in a property-based condition that filters the results of a query for findings.\n\neq (list) --An equal to condition to apply to a specified property value for findings.\n\n(string) --\n\n\ngt (integer) --A greater than condition to apply to a specified property value for findings.\n\ngte (integer) --A greater than or equal to condition to apply to a specified property value for findings.\n\nlt (integer) --A less than condition to apply to a specified property value for findings.\n\nlte (integer) --A less than or equal to condition to apply to a specified property value for findings.\n\nneq (list) --A not equal to condition to apply to a specified property value for findings.\n\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type groupBy: string
    :param groupBy: [REQUIRED]\nThe finding property to use to group the query results. Valid values are:\n\nclassificationDetails.jobId - The unique identifier for the classification job that produced the finding.\nresourcesAffected.s3Bucket.name - The name of the S3 bucket that the finding applies to.\nseverity.description - The severity of the finding, such as High or Medium.\ntype - The type of finding, such as Policy:IAMUser/S3BucketPublic and SensitiveData:S3Object/Personal.\n\n

    :type size: integer
    :param size: The maximum number of items to include in each page of the response.

    :type sortCriteria: dict
    :param sortCriteria: The criteria to use to sort the query results.\n\nattributeName (string) --The grouping to sort the results by. Valid values are: count, sort the results by the number of findings in each group of results; and, groupKey, sort the results by the name of each group of results.\n\norderBy (string) --The sort order to apply to the results, based on the value for the property specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'countsByGroup': [
        {
            'count': 123,
            'groupKey': 'string'
        },
    ]
}


Response Structure

(dict) --
The request succeeded.

countsByGroup (list) --
An array of objects, one for each group of findings that meet the filter criteria specified in the request.

(dict) --
Provides a group of results for a query that retrieved information about findings.

count (integer) --
The total number of findings in the group of query results.

groupKey (string) --
The name of the property that defines the group in the query results, as specified by the groupBy property in the query request.











Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'countsByGroup': [
            {
                'count': 123,
                'groupKey': 'string'
            },
        ]
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def get_findings(findingIds=None, sortCriteria=None):
    """
    Retrieves information about one or more findings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_findings(
        findingIds=[
            'string',
        ],
        sortCriteria={
            'attributeName': 'string',
            'orderBy': 'ASC'|'DESC'
        }
    )
    
    
    :type findingIds: list
    :param findingIds: [REQUIRED]\nAn array of strings that lists the unique identifiers for the findings to retrieve information about.\n\n(string) --\n\n

    :type sortCriteria: dict
    :param sortCriteria: The criteria for sorting the results of the request.\n\nattributeName (string) --The name of the property to sort the results by. This value can be the name of any property that Amazon Macie defines for a finding.\n\norderBy (string) --The sort order to apply to the results, based on the value for the property specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'findings': [
        {
            'accountId': 'string',
            'archived': True|False,
            'category': 'CLASSIFICATION'|'POLICY',
            'classificationDetails': {
                'detailedResultsLocation': 'string',
                'jobArn': 'string',
                'jobId': 'string',
                'result': {
                    'customDataIdentifiers': {
                        'detections': [
                            {
                                'arn': 'string',
                                'count': 123,
                                'name': 'string'
                            },
                        ],
                        'totalCount': 123
                    },
                    'mimeType': 'string',
                    'sensitiveData': [
                        {
                            'category': 'FINANCIAL_INFORMATION'|'PERSONAL_INFORMATION'|'CREDENTIALS'|'CUSTOM_IDENTIFIER',
                            'detections': [
                                {
                                    'count': 123,
                                    'type': 'string'
                                },
                            ],
                            'totalCount': 123
                        },
                    ],
                    'sizeClassified': 123,
                    'status': {
                        'code': 'string',
                        'reason': 'string'
                    }
                }
            },
            'count': 123,
            'createdAt': datetime(2015, 1, 1),
            'description': 'string',
            'id': 'string',
            'partition': 'string',
            'policyDetails': {
                'action': {
                    'actionType': 'AWS_API_CALL',
                    'apiCallDetails': {
                        'api': 'string',
                        'apiServiceName': 'string',
                        'firstSeen': datetime(2015, 1, 1),
                        'lastSeen': datetime(2015, 1, 1)
                    }
                },
                'actor': {
                    'domainDetails': {
                        'domainName': 'string'
                    },
                    'ipAddressDetails': {
                        'ipAddressV4': 'string',
                        'ipCity': {
                            'name': 'string'
                        },
                        'ipCountry': {
                            'code': 'string',
                            'name': 'string'
                        },
                        'ipGeoLocation': {
                            'lat': 123.0,
                            'lon': 123.0
                        },
                        'ipOwner': {
                            'asn': 'string',
                            'asnOrg': 'string',
                            'isp': 'string',
                            'org': 'string'
                        }
                    },
                    'userIdentity': {
                        'assumedRole': {
                            'accessKeyId': 'string',
                            'accountId': 'string',
                            'arn': 'string',
                            'principalId': 'string',
                            'sessionContext': {
                                'attributes': {
                                    'creationDate': datetime(2015, 1, 1),
                                    'mfaAuthenticated': True|False
                                },
                                'sessionIssuer': {
                                    'accountId': 'string',
                                    'arn': 'string',
                                    'principalId': 'string',
                                    'type': 'string',
                                    'userName': 'string'
                                }
                            }
                        },
                        'awsAccount': {
                            'accountId': 'string',
                            'principalId': 'string'
                        },
                        'awsService': {
                            'invokedBy': 'string'
                        },
                        'federatedUser': {
                            'accessKeyId': 'string',
                            'accountId': 'string',
                            'arn': 'string',
                            'principalId': 'string',
                            'sessionContext': {
                                'attributes': {
                                    'creationDate': datetime(2015, 1, 1),
                                    'mfaAuthenticated': True|False
                                },
                                'sessionIssuer': {
                                    'accountId': 'string',
                                    'arn': 'string',
                                    'principalId': 'string',
                                    'type': 'string',
                                    'userName': 'string'
                                }
                            }
                        },
                        'iamUser': {
                            'accountId': 'string',
                            'arn': 'string',
                            'principalId': 'string',
                            'userName': 'string'
                        },
                        'root': {
                            'accountId': 'string',
                            'arn': 'string',
                            'principalId': 'string'
                        },
                        'type': 'AssumedRole'|'IAMUser'|'FederatedUser'|'Root'|'AWSAccount'|'AWSService'
                    }
                }
            },
            'region': 'string',
            'resourcesAffected': {
                's3Bucket': {
                    'arn': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'defaultServerSideEncryption': {
                        'encryptionType': 'NONE'|'AES256'|'aws:kms',
                        'kmsMasterKeyId': 'string'
                    },
                    'name': 'string',
                    'owner': {
                        'displayName': 'string',
                        'id': 'string'
                    },
                    'publicAccess': {
                        'effectivePermission': 'PUBLIC'|'NOT_PUBLIC',
                        'permissionConfiguration': {
                            'accountLevelPermissions': {
                                'blockPublicAccess': {
                                    'blockPublicAcls': True|False,
                                    'blockPublicPolicy': True|False,
                                    'ignorePublicAcls': True|False,
                                    'restrictPublicBuckets': True|False
                                }
                            },
                            'bucketLevelPermissions': {
                                'accessControlList': {
                                    'allowsPublicReadAccess': True|False,
                                    'allowsPublicWriteAccess': True|False
                                },
                                'blockPublicAccess': {
                                    'blockPublicAcls': True|False,
                                    'blockPublicPolicy': True|False,
                                    'ignorePublicAcls': True|False,
                                    'restrictPublicBuckets': True|False
                                },
                                'bucketPolicy': {
                                    'allowsPublicReadAccess': True|False,
                                    'allowsPublicWriteAccess': True|False
                                }
                            }
                        }
                    },
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ]
                },
                's3Object': {
                    'bucketArn': 'string',
                    'eTag': 'string',
                    'extension': 'string',
                    'key': 'string',
                    'lastModified': datetime(2015, 1, 1),
                    'path': 'string',
                    'publicAccess': True|False,
                    'serverSideEncryption': {
                        'encryptionType': 'NONE'|'AES256'|'aws:kms',
                        'kmsMasterKeyId': 'string'
                    },
                    'size': 123,
                    'storageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'|'ONEZONE_IA'|'GLACIER',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'versionId': 'string'
                }
            },
            'sample': True|False,
            'schemaVersion': 'string',
            'severity': {
                'description': 'Low'|'Medium'|'High',
                'score': 123
            },
            'title': 'string',
            'type': 'SensitiveData:S3Object/Multiple'|'SensitiveData:S3Object/Financial'|'SensitiveData:S3Object/Personal'|'SensitiveData:S3Object/Credentials'|'SensitiveData:S3Object/CustomIdentifier'|'Policy:IAMUser/S3BucketPublic'|'Policy:IAMUser/S3BucketSharedExternally'|'Policy:IAMUser/S3BucketReplicatedExternally'|'Policy:IAMUser/S3BucketEncryptionDisabled'|'Policy:IAMUser/S3BlockPublicAccessDisabled',
            'updatedAt': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --
The request succeeded.

findings (list) --
An array of objects, one for each finding that meets the criteria specified in the request.

(dict) --
Provides information about a finding.

accountId (string) --
The identifier for the AWS account that the finding applies to. This is typically the account that owns the affected resource.

archived (boolean) --
Specifies whether the finding is archived.

category (string) --
The category of the finding. Possible values are: CLASSIFICATION, for a sensitive data finding; and, POLICY, for a policy finding.

classificationDetails (dict) --
The details of a sensitive data finding. This value is null for a policy finding.

detailedResultsLocation (string) --
The Amazon Resource Name (ARN) of the file that contains the detailed record, including offsets, for the finding.

jobArn (string) --
The Amazon Resource Name (ARN) of the classification job that produced the finding.

jobId (string) --
The unique identifier for the classification job that produced the finding.

result (dict) --
The status and detailed results of the finding.

customDataIdentifiers (dict) --
The number of occurrences of the data that produced the finding, and the custom data identifiers that detected the data.

detections (list) --
The names of the custom data identifiers that detected the data, and the number of occurrences of the data that each identifier detected.

(dict) --
Provides information about a custom data identifier that produced a sensitive data finding, and the number of occurrences of the data that it detected for the finding.

arn (string) --
The Amazon Resource Name (ARN) of the custom data identifier.

count (integer) --
The total number of occurrences of the data that the custom data identifier detected for the finding.

name (string) --
The name of the custom data identifier.





totalCount (integer) --
The total number of occurrences of the data that was detected by the custom data identifiers and produced the finding.



mimeType (string) --
The type of content, expressed as a MIME type, that the finding applies to. For example, application/gzip, for a GNU Gzip compressed archive file, or application/pdf, for an Adobe PDF file.

sensitiveData (list) --
The category and number of occurrences of the sensitive data that produced the finding.

(dict) --
Provides information about the category, type, and number of occurrences of sensitive data that produced a finding.

category (string) --
The category of sensitive data that was detected. For example, FINANCIAL_INFORMATION, for financial information such as credit card numbers, or PERSONAL_INFORMATION, for personally identifiable information such as names and addresses.

detections (list) --
An array of objects, one for each type of sensitive data that was detected. Each object reports the number of occurrences of a specific type of sensitive data that was detected.

(dict) --
Provides information about sensitive data that was detected by managed data identifiers and produced a finding.

count (integer) --
The total number of occurrences of the type of data that was detected.

type (string) --
The type of data that was detected. For example, AWS_CREDENTIALS, PHONE_NUMBER, or ADDRESS.





totalCount (integer) --
The total number of occurrences of the sensitive data that was detected.





sizeClassified (integer) --
The total size, in bytes, of the data that the finding applies to.

status (dict) --
The status of the finding.

code (string) --
The status of the finding, such as COMPLETE.

reason (string) --
A brief description of the status of the finding. Amazon Macie uses this value to notify you of any errors, warnings, or considerations that might impact your analysis of the finding.







count (integer) --
The total number of occurrences of this finding.

createdAt (datetime) --
The date and time, in UTC and extended ISO 8601 format, when the finding was created.

description (string) --
The description of the finding.

id (string) --
The unique identifier for the finding. This is a random string that Amazon Macie generates and assigns to a finding when it creates the finding.

partition (string) --
The AWS partition that Amazon Macie created the finding in.

policyDetails (dict) --
The details of a policy finding. This value is null for a sensitive data finding.

action (dict) --
The action that occurred and produced the finding.

actionType (string) --
The type of action that occurred for the affected resource. This value is typically AWS_API_CALL, which indicates that an entity invoked an API operation for the resource.

apiCallDetails (dict) --
For the affected resource:

The name of the operation that was invoked most recently and produced the finding (api).
The first date and time when any operation was invoked and produced the finding (firstSeen).
The most recent date and time when the specified operation was invoked and produced the finding (lastSeen).

All date and time values are in UTC and extended ISO 8601 format.

api (string) --
Reserved for future use.

apiServiceName (string) --
Reserved for future use.

firstSeen (datetime) --
Reserved for future use.

lastSeen (datetime) --
Reserved for future use.





actor (dict) --
The entity who performed the action that produced the finding.

domainDetails (dict) --
The DNS name of the entity that performed the action on the affected resource.

domainName (string) --
Reserved for future use.



ipAddressDetails (dict) --
The IP address of the device that the entity used to perform the action on the affected resource. This object also provides information such as the owner and geographical location for the IP address.

ipAddressV4 (string) --
Reserved for future use.

ipCity (dict) --
Reserved for future use.

name (string) --
Reserved for future use.



ipCountry (dict) --
Reserved for future use.

code (string) --
Reserved for future use.

name (string) --
Reserved for future use.



ipGeoLocation (dict) --
Reserved for future use.

lat (float) --
Reserved for future use.

lon (float) --
Reserved for future use.



ipOwner (dict) --
Reserved for future use.

asn (string) --
Reserved for future use.

asnOrg (string) --
Reserved for future use.

isp (string) --
Reserved for future use.

org (string) --
Reserved for future use.





userIdentity (dict) --
The name and type of entity who performed the action on the affected resource.

assumedRole (dict) --
Reserved for future use.

accessKeyId (string) --
Reserved for future use.

accountId (string) --
Reserved for future use.

arn (string) --
Reserved for future use.

principalId (string) --
Reserved for future use.

sessionContext (dict) --
Reserved for future use.

attributes (dict) --
The date and time when the credentials were issued, and whether the credentials were authenticated with a multi-factor authentication (MFA) device.

creationDate (datetime) --
The date and time, in ISO 8601 format, when the credentials were issued.

mfaAuthenticated (boolean) --
Specifies whether the credentials were authenticated with a multi-factor authentication (MFA) device.



sessionIssuer (dict) --
The source and type of credentials that the entity obtained.

accountId (string) --
The account that owns the entity that was used to get the credentials.

arn (string) --
The Amazon Resource Name (ARN) of the source account, IAM user, or role that was used to get the credentials.

principalId (string) --
The internal identifier for the entity that was used to get the credentials.

type (string) --
The source of the temporary security credentials, such as Root, IAMUser, or Role.

userName (string) --
The name or alias of the user or role that issued the session. This value is null if the credentials were obtained from a root account that doesn\'t have an alias.







awsAccount (dict) --
Reserved for future use.

accountId (string) --
Reserved for future use.

principalId (string) --
Reserved for future use.



awsService (dict) --
Reserved for future use.

invokedBy (string) --
Reserved for future use.



federatedUser (dict) --
Reserved for future use.

accessKeyId (string) --
Reserved for future use.

accountId (string) --
Reserved for future use.

arn (string) --
Reserved for future use.

principalId (string) --
Reserved for future use.

sessionContext (dict) --
Reserved for future use.

attributes (dict) --
The date and time when the credentials were issued, and whether the credentials were authenticated with a multi-factor authentication (MFA) device.

creationDate (datetime) --
The date and time, in ISO 8601 format, when the credentials were issued.

mfaAuthenticated (boolean) --
Specifies whether the credentials were authenticated with a multi-factor authentication (MFA) device.



sessionIssuer (dict) --
The source and type of credentials that the entity obtained.

accountId (string) --
The account that owns the entity that was used to get the credentials.

arn (string) --
The Amazon Resource Name (ARN) of the source account, IAM user, or role that was used to get the credentials.

principalId (string) --
The internal identifier for the entity that was used to get the credentials.

type (string) --
The source of the temporary security credentials, such as Root, IAMUser, or Role.

userName (string) --
The name or alias of the user or role that issued the session. This value is null if the credentials were obtained from a root account that doesn\'t have an alias.







iamUser (dict) --
Reserved for future use.

accountId (string) --
Reserved for future use.

arn (string) --
Reserved for future use.

principalId (string) --
Reserved for future use.

userName (string) --
Reserved for future use.



root (dict) --
Reserved for future use.

accountId (string) --
Reserved for future use.

arn (string) --
Reserved for future use.

principalId (string) --
Reserved for future use.



type (string) --
Reserved for future use.







region (string) --
The AWS Region that Amazon Macie created the finding in.

resourcesAffected (dict) --
The resources that the finding applies to.

s3Bucket (dict) --
An array of objects, one for each S3 bucket that the finding applies to. Each object provides a set of metadata about an affected S3 bucket.

arn (string) --
The Amazon Resource Name (ARN) of the bucket.

createdAt (datetime) --
The date and time, in UTC and extended ISO 8601 format, when the bucket was created.

defaultServerSideEncryption (dict) --
The server-side encryption settings for the bucket.

encryptionType (string) --
The server-side encryption algorithm that\'s used when storing data in the bucket or object. If encryption is disabled for the bucket or object, this value is NONE.

kmsMasterKeyId (string) --
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) master key that\'s used to encrypt the bucket or object. This value is null if KMS isn\'t used to encrypt the bucket or object.



name (string) --
The name of the bucket.

owner (dict) --
The display name and account identifier for the user who owns the bucket.

displayName (string) --
The display name of the user who owns the bucket.

id (string) --
The AWS account ID for the user who owns the bucket.



publicAccess (dict) --
The permissions settings that determine whether the bucket is publicly accessible.

effectivePermission (string) --
Specifies whether the bucket is publicly accessible due to the combination of permissions settings that apply to the bucket. Possible values are: PUBLIC, the bucket is publicly accessible; and, NOT_PUBLIC, the bucket isn\'t publicly accessible.

permissionConfiguration (dict) --
The account-level and bucket-level permissions for the bucket.

accountLevelPermissions (dict) --
The account-level permissions settings that apply to the bucket.

blockPublicAccess (dict) --
The block public access settings for the bucket.

blockPublicAcls (boolean) --
Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket.

blockPublicPolicy (boolean) --
Specifies whether Amazon S3 blocks public bucket policies for the bucket.

ignorePublicAcls (boolean) --
Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket.

restrictPublicBuckets (boolean) --
Specifies whether Amazon S3 restricts public bucket policies for the bucket.





bucketLevelPermissions (dict) --
The bucket-level permissions settings for the bucket.

accessControlList (dict) --
The permissions settings of the access control list (ACL) for the bucket. This value is null if an ACL hasn\'t been defined for the bucket.

allowsPublicReadAccess (boolean) --
Specifies whether the ACL grants the general public with read access permissions for the bucket.

allowsPublicWriteAccess (boolean) --
Specifies whether the ACL grants the general public with write access permissions for the bucket.



blockPublicAccess (dict) --
The block public access settings for the bucket.

blockPublicAcls (boolean) --
Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket.

blockPublicPolicy (boolean) --
Specifies whether Amazon S3 blocks public bucket policies for the bucket.

ignorePublicAcls (boolean) --
Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket.

restrictPublicBuckets (boolean) --
Specifies whether Amazon S3 restricts public bucket policies for the bucket.



bucketPolicy (dict) --
The permissions settings of the bucket policy for the bucket. This value is null if a bucket policy hasn\'t been defined for the bucket.

allowsPublicReadAccess (boolean) --
Specifies whether the bucket policy allows the general public to have read access to the bucket.

allowsPublicWriteAccess (boolean) --
Specifies whether the bucket policy allows the general public to have write access to the bucket.









tags (list) --
The tags that are associated with the bucket.

(dict) --
Provides information about the tags that are associated with an S3 bucket or object. Each tag consists of a required tag key and an associated tag value.

key (string) --
One part of a key-value pair that comprises a tag. A tag key is a general label that acts as a category for more specific tag values.

value (string) --
One part of a key-value pair that comprises a tag. A tag value acts as a descriptor for a tag key. A tag value can be empty or null.







s3Object (dict) --
An array of objects, one for each S3 object that the finding applies to. Each object provides a set of metadata about an affected S3 object.

bucketArn (string) --
The Amazon Resource Name (ARN) of the bucket that contains the object.

eTag (string) --
The entity tag (ETag) that identifies the affected version of the object. If the object was overwritten or changed after Amazon Macie produced the finding, this value might be different from the current ETag for the object.

extension (string) --
The file extension of the object. If the object doesn\'t have a file extension, this value is "".

key (string) --
The full key (name) that\'s assigned to the object.

lastModified (datetime) --
The date and time, in UTC and extended ISO 8601 format, when the object was last modified.

path (string) --
The path to the object, including the full key (name).

publicAccess (boolean) --
Specifies whether the object is publicly accessible due to the combination of permissions settings that apply to the object.

serverSideEncryption (dict) --
The server-side encryption settings for the object.

encryptionType (string) --
The server-side encryption algorithm that\'s used when storing data in the bucket or object. If encryption is disabled for the bucket or object, this value is NONE.

kmsMasterKeyId (string) --
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) master key that\'s used to encrypt the bucket or object. This value is null if KMS isn\'t used to encrypt the bucket or object.



size (integer) --
The total storage size, in bytes, of the object.

storageClass (string) --
The storage class of the object.

tags (list) --
The tags that are associated with the object.

(dict) --
Provides information about the tags that are associated with an S3 bucket or object. Each tag consists of a required tag key and an associated tag value.

key (string) --
One part of a key-value pair that comprises a tag. A tag key is a general label that acts as a category for more specific tag values.

value (string) --
One part of a key-value pair that comprises a tag. A tag value acts as a descriptor for a tag key. A tag value can be empty or null.





versionId (string) --
The identifier for the affected version of the object.





sample (boolean) --
Specifies whether the finding is a sample finding. A sample finding is a finding that uses example data to demonstrate what a finding might contain.

schemaVersion (string) --
The version of the schema that was used to define the data structures in the finding.

severity (dict) --
The severity of the finding.

description (string) --
The textual representation of the severity value, such as Low or High.

score (integer) --
The numeric score for the severity value, ranging from 0 (least severe) to 4 (most severe).



title (string) --
The brief description of the finding.

type (string) --
The type of the finding.

updatedAt (datetime) --
The date and time, in UTC and extended ISO 8601 format, when the finding was last updated. For sensitive data findings, this value is the same as the value for the createdAt property. Sensitive data findings aren\'t updated.











Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'findings': [
            {
                'accountId': 'string',
                'archived': True|False,
                'category': 'CLASSIFICATION'|'POLICY',
                'classificationDetails': {
                    'detailedResultsLocation': 'string',
                    'jobArn': 'string',
                    'jobId': 'string',
                    'result': {
                        'customDataIdentifiers': {
                            'detections': [
                                {
                                    'arn': 'string',
                                    'count': 123,
                                    'name': 'string'
                                },
                            ],
                            'totalCount': 123
                        },
                        'mimeType': 'string',
                        'sensitiveData': [
                            {
                                'category': 'FINANCIAL_INFORMATION'|'PERSONAL_INFORMATION'|'CREDENTIALS'|'CUSTOM_IDENTIFIER',
                                'detections': [
                                    {
                                        'count': 123,
                                        'type': 'string'
                                    },
                                ],
                                'totalCount': 123
                            },
                        ],
                        'sizeClassified': 123,
                        'status': {
                            'code': 'string',
                            'reason': 'string'
                        }
                    }
                },
                'count': 123,
                'createdAt': datetime(2015, 1, 1),
                'description': 'string',
                'id': 'string',
                'partition': 'string',
                'policyDetails': {
                    'action': {
                        'actionType': 'AWS_API_CALL',
                        'apiCallDetails': {
                            'api': 'string',
                            'apiServiceName': 'string',
                            'firstSeen': datetime(2015, 1, 1),
                            'lastSeen': datetime(2015, 1, 1)
                        }
                    },
                    'actor': {
                        'domainDetails': {
                            'domainName': 'string'
                        },
                        'ipAddressDetails': {
                            'ipAddressV4': 'string',
                            'ipCity': {
                                'name': 'string'
                            },
                            'ipCountry': {
                                'code': 'string',
                                'name': 'string'
                            },
                            'ipGeoLocation': {
                                'lat': 123.0,
                                'lon': 123.0
                            },
                            'ipOwner': {
                                'asn': 'string',
                                'asnOrg': 'string',
                                'isp': 'string',
                                'org': 'string'
                            }
                        },
                        'userIdentity': {
                            'assumedRole': {
                                'accessKeyId': 'string',
                                'accountId': 'string',
                                'arn': 'string',
                                'principalId': 'string',
                                'sessionContext': {
                                    'attributes': {
                                        'creationDate': datetime(2015, 1, 1),
                                        'mfaAuthenticated': True|False
                                    },
                                    'sessionIssuer': {
                                        'accountId': 'string',
                                        'arn': 'string',
                                        'principalId': 'string',
                                        'type': 'string',
                                        'userName': 'string'
                                    }
                                }
                            },
                            'awsAccount': {
                                'accountId': 'string',
                                'principalId': 'string'
                            },
                            'awsService': {
                                'invokedBy': 'string'
                            },
                            'federatedUser': {
                                'accessKeyId': 'string',
                                'accountId': 'string',
                                'arn': 'string',
                                'principalId': 'string',
                                'sessionContext': {
                                    'attributes': {
                                        'creationDate': datetime(2015, 1, 1),
                                        'mfaAuthenticated': True|False
                                    },
                                    'sessionIssuer': {
                                        'accountId': 'string',
                                        'arn': 'string',
                                        'principalId': 'string',
                                        'type': 'string',
                                        'userName': 'string'
                                    }
                                }
                            },
                            'iamUser': {
                                'accountId': 'string',
                                'arn': 'string',
                                'principalId': 'string',
                                'userName': 'string'
                            },
                            'root': {
                                'accountId': 'string',
                                'arn': 'string',
                                'principalId': 'string'
                            },
                            'type': 'AssumedRole'|'IAMUser'|'FederatedUser'|'Root'|'AWSAccount'|'AWSService'
                        }
                    }
                },
                'region': 'string',
                'resourcesAffected': {
                    's3Bucket': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'defaultServerSideEncryption': {
                            'encryptionType': 'NONE'|'AES256'|'aws:kms',
                            'kmsMasterKeyId': 'string'
                        },
                        'name': 'string',
                        'owner': {
                            'displayName': 'string',
                            'id': 'string'
                        },
                        'publicAccess': {
                            'effectivePermission': 'PUBLIC'|'NOT_PUBLIC',
                            'permissionConfiguration': {
                                'accountLevelPermissions': {
                                    'blockPublicAccess': {
                                        'blockPublicAcls': True|False,
                                        'blockPublicPolicy': True|False,
                                        'ignorePublicAcls': True|False,
                                        'restrictPublicBuckets': True|False
                                    }
                                },
                                'bucketLevelPermissions': {
                                    'accessControlList': {
                                        'allowsPublicReadAccess': True|False,
                                        'allowsPublicWriteAccess': True|False
                                    },
                                    'blockPublicAccess': {
                                        'blockPublicAcls': True|False,
                                        'blockPublicPolicy': True|False,
                                        'ignorePublicAcls': True|False,
                                        'restrictPublicBuckets': True|False
                                    },
                                    'bucketPolicy': {
                                        'allowsPublicReadAccess': True|False,
                                        'allowsPublicWriteAccess': True|False
                                    }
                                }
                            }
                        },
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                    's3Object': {
                        'bucketArn': 'string',
                        'eTag': 'string',
                        'extension': 'string',
                        'key': 'string',
                        'lastModified': datetime(2015, 1, 1),
                        'path': 'string',
                        'publicAccess': True|False,
                        'serverSideEncryption': {
                            'encryptionType': 'NONE'|'AES256'|'aws:kms',
                            'kmsMasterKeyId': 'string'
                        },
                        'size': 123,
                        'storageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'|'ONEZONE_IA'|'GLACIER',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'versionId': 'string'
                    }
                },
                'sample': True|False,
                'schemaVersion': 'string',
                'severity': {
                    'description': 'Low'|'Medium'|'High',
                    'score': 123
                },
                'title': 'string',
                'type': 'SensitiveData:S3Object/Multiple'|'SensitiveData:S3Object/Financial'|'SensitiveData:S3Object/Personal'|'SensitiveData:S3Object/Credentials'|'SensitiveData:S3Object/CustomIdentifier'|'Policy:IAMUser/S3BucketPublic'|'Policy:IAMUser/S3BucketSharedExternally'|'Policy:IAMUser/S3BucketReplicatedExternally'|'Policy:IAMUser/S3BucketEncryptionDisabled'|'Policy:IAMUser/S3BlockPublicAccessDisabled',
                'updatedAt': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    The name of the operation that was invoked most recently and produced the finding (api).
    The first date and time when any operation was invoked and produced the finding (firstSeen).
    The most recent date and time when the specified operation was invoked and produced the finding (lastSeen).
    
    """
    pass

def get_findings_filter(id=None):
    """
    Retrieves information about the criteria and other settings for a findings filter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_findings_filter(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe unique identifier for the Amazon Macie resource or account that the request applies to.\n

    :rtype: dict
ReturnsResponse Syntax{
    'action': 'ARCHIVE'|'NOOP',
    'arn': 'string',
    'description': 'string',
    'findingCriteria': {
        'criterion': {
            'string': {
                'eq': [
                    'string',
                ],
                'gt': 123,
                'gte': 123,
                'lt': 123,
                'lte': 123,
                'neq': [
                    'string',
                ]
            }
        }
    },
    'id': 'string',
    'name': 'string',
    'position': 123,
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --The request succeeded.

action (string) --The action that\'s performed on findings that meet the filter criteria (findingCriteria). Possible values are: ARCHIVE, automatically archive the findings; and, NOOP, don\'t perform any action on the findings.

arn (string) --The Amazon Resource Name (ARN) of the filter.

description (string) --The custom description of the filter.

findingCriteria (dict) --The criteria that\'s used to filter findings.

criterion (dict) --A condition that specifies the property, operator, and value to use to filter the results.

(string) --
(dict) --Specifies the operator to use in a property-based condition that filters the results of a query for findings.

eq (list) --An equal to condition to apply to a specified property value for findings.

(string) --


gt (integer) --A greater than condition to apply to a specified property value for findings.

gte (integer) --A greater than or equal to condition to apply to a specified property value for findings.

lt (integer) --A less than condition to apply to a specified property value for findings.

lte (integer) --A less than or equal to condition to apply to a specified property value for findings.

neq (list) --A not equal to condition to apply to a specified property value for findings.

(string) --










id (string) --The unique identifier for the filter.

name (string) --The custom name of the filter.

position (integer) --The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.

tags (dict) --A map of key-value pairs that identifies the tags (keys and values) that are associated with the filter.

(string) --
(string) --









Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'action': 'ARCHIVE'|'NOOP',
        'arn': 'string',
        'description': 'string',
        'findingCriteria': {
            'criterion': {
                'string': {
                    'eq': [
                        'string',
                    ],
                    'gt': 123,
                    'gte': 123,
                    'lt': 123,
                    'lte': 123,
                    'neq': [
                        'string',
                    ]
                }
            }
        },
        'id': 'string',
        'name': 'string',
        'position': 123,
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_invitations_count():
    """
    Retrieves the count of Amazon Macie membership invitations that were received by an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_invitations_count()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'invitationsCount': 123
}


Response Structure

(dict) --The request succeeded.

invitationsCount (integer) --The total number of invitations that were received by the account, not including the currently accepted invitation.






Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'invitationsCount': 123
    }
    
    
    """
    pass

def get_macie_session():
    """
    Retrieves information about the current status and configuration settings for an Amazon Macie account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_macie_session()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'createdAt': datetime(2015, 1, 1),
    'findingPublishingFrequency': 'FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS',
    'serviceRole': 'string',
    'status': 'PAUSED'|'ENABLED',
    'updatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --The request succeeded.

createdAt (datetime) --The date and time, in UTC and extended ISO 8601 format, when the Amazon Macie account was created.

findingPublishingFrequency (string) --The frequency with which Amazon Macie publishes findings for the account. This includes adding findings to AWS Security Hub and exporting finding events to Amazon CloudWatch.

serviceRole (string) --The Amazon Resource Name (ARN) of the service-level role that allows Amazon Macie to monitor and analyze data in AWS resources for the account.

status (string) --The current status of the Amazon Macie account. Possible values are: PAUSED, the account is enabled but all Amazon Macie activities are suspended (paused) for the account; and, ENABLED, the account is enabled and all Amazon Macie activities are enabled for the account.

updatedAt (datetime) --The date and time, in UTC and extended ISO 8601 format, of the most recent change to the status of the Amazon Macie account.






Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'createdAt': datetime(2015, 1, 1),
        'findingPublishingFrequency': 'FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS',
        'serviceRole': 'string',
        'status': 'PAUSED'|'ENABLED',
        'updatedAt': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def get_master_account():
    """
    Retrieves information about the Amazon Macie master account for an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_master_account()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'master': {
        'accountId': 'string',
        'invitationId': 'string',
        'invitedAt': datetime(2015, 1, 1),
        'relationshipStatus': 'Enabled'|'Paused'|'Invited'|'Created'|'Removed'|'Resigned'|'EmailVerificationInProgress'|'EmailVerificationFailed'
    }
}


Response Structure

(dict) --The request succeeded.

master (dict) --The AWS account ID for the master account. If the accounts are associated by a Macie membership invitation, this object also provides details about the invitation that was sent and accepted to establish the relationship between the accounts.

accountId (string) --The AWS account ID for the account that sent the invitation.

invitationId (string) --The unique identifier for the invitation. Amazon Macie uses this identifier to validate the inviter account with the invitee account.

invitedAt (datetime) --The date and time, in UTC and extended ISO 8601 format, when the invitation was sent.

relationshipStatus (string) --The status of the relationship between the account that sent the invitation (inviter account ) and the account that received the invitation (invitee account ).








Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'master': {
            'accountId': 'string',
            'invitationId': 'string',
            'invitedAt': datetime(2015, 1, 1),
            'relationshipStatus': 'Enabled'|'Paused'|'Invited'|'Created'|'Removed'|'Resigned'|'EmailVerificationInProgress'|'EmailVerificationFailed'
        }
    }
    
    
    """
    pass

def get_member(id=None):
    """
    Retrieves information about a member account that\'s associated with an Amazon Macie master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_member(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe unique identifier for the Amazon Macie resource or account that the request applies to.\n

    :rtype: dict
ReturnsResponse Syntax{
    'accountId': 'string',
    'arn': 'string',
    'email': 'string',
    'invitedAt': datetime(2015, 1, 1),
    'masterAccountId': 'string',
    'relationshipStatus': 'Enabled'|'Paused'|'Invited'|'Created'|'Removed'|'Resigned'|'EmailVerificationInProgress'|'EmailVerificationFailed',
    'tags': {
        'string': 'string'
    },
    'updatedAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --The request succeeded.

accountId (string) --The AWS account ID for the account.

arn (string) --The Amazon Resource Name (ARN) of the account.

email (string) --The email address for the account.

invitedAt (datetime) --The date and time, in UTC and extended ISO 8601 format, when an Amazon Macie membership invitation was last sent to the account. This value is null if a Macie invitation hasn\'t been sent to the account.

masterAccountId (string) --The AWS account ID for the master account.

relationshipStatus (string) --The current status of the relationship between the account and the master account.

tags (dict) --A map of key-value pairs that identifies the tags (keys and values) that are associated with the member account in Amazon Macie.

(string) --
(string) --




updatedAt (datetime) --The date and time, in UTC and extended ISO 8601 format, of the most recent change to the status of the relationship between the account and the master account.






Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'accountId': 'string',
        'arn': 'string',
        'email': 'string',
        'invitedAt': datetime(2015, 1, 1),
        'masterAccountId': 'string',
        'relationshipStatus': 'Enabled'|'Paused'|'Invited'|'Created'|'Removed'|'Resigned'|'EmailVerificationInProgress'|'EmailVerificationFailed',
        'tags': {
            'string': 'string'
        },
        'updatedAt': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
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

def get_usage_statistics(filterBy=None, maxResults=None, nextToken=None, sortBy=None):
    """
    Retrieves (queries) quotas and aggregated usage data for one or more accounts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_usage_statistics(
        filterBy=[
            {
                'key': 'accountId',
                'values': [
                    'string',
                ]
            },
        ],
        maxResults=123,
        nextToken='string',
        sortBy={
            'key': 'accountId'|'total',
            'orderBy': 'ASC'|'DESC'
        }
    )
    
    
    :type filterBy: list
    :param filterBy: The criteria to use to filter the query results.\n\n(dict) --Specifies criteria for filtering the results of a query for account quotas and usage data.\n\nkey (string) --The field to use to filter the results. The only supported value is accountId.\n\nvalues (list) --An array that lists the AWS account ID for each account to include in the results.\n\n(string) --\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of items to include in each page of the response.

    :type nextToken: string
    :param nextToken: The nextToken string that specifies which page of results to return in a paginated response.

    :type sortBy: dict
    :param sortBy: The criteria to use to sort the query results.\n\nkey (string) --The field to sort the results by.\n\norderBy (string) --The sort order to apply to the results, based on the value for the field specified by the key property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'records': [
        {
            'accountId': 'string',
            'freeTrialStartDate': datetime(2015, 1, 1),
            'usage': [
                {
                    'currency': 'USD',
                    'estimatedCost': 'string',
                    'serviceLimit': {
                        'isServiceLimited': True|False,
                        'unit': 'TERABYTES',
                        'value': 123
                    },
                    'type': 'DATA_INVENTORY_EVALUATION'|'SENSITIVE_DATA_DISCOVERY'
                },
            ]
        },
    ]
}


Response Structure

(dict) --
The request succeeded.

nextToken (string) --
The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.

records (list) --
An array of objects that contains the results of the query. Each object contains the data for an account that meets the filter criteria specified in the request.

(dict) --
Provides quota and aggregated usage data for an account.

accountId (string) --
The AWS account ID for the account that the data applies to.

freeTrialStartDate (datetime) --
The date and time, in UTC and extended ISO 8601 format, when the free trial period started for the account. This value is null if the account didn\'t participate in the free trial.

usage (list) --
An array of objects that contains usage data and quotas for the account. Each object contains the data for a specific usage metric and the corresponding quota.

(dict) --
Provides data for a specific usage metric and the corresponding quota for an account. The value for the metric is an aggregated value that reports usage during the past 30 days.

currency (string) --
The type of currency that the value for the metric (estimatedCost) is reported in.

estimatedCost (string) --
The estimated value for the metric.

serviceLimit (dict) --
The current value for the quota that corresponds to the metric specified by the type field.

isServiceLimited (boolean) --
Specifies whether the account has met the quota that corresponds to the metric specified by the UsageByAccount.type field in the response.

unit (string) --
The unit of measurement for the value specified by the value field.

value (integer) --
The value for the metric specified by the UsageByAccount.type field in the response.



type (string) --
The name of the metric. Possible values are: DATA_INVENTORY_EVALUATION, for monitoring S3 buckets; and, SENSITIVE_DATA_DISCOVERY, for analyzing sensitive data.















Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'nextToken': 'string',
        'records': [
            {
                'accountId': 'string',
                'freeTrialStartDate': datetime(2015, 1, 1),
                'usage': [
                    {
                        'currency': 'USD',
                        'estimatedCost': 'string',
                        'serviceLimit': {
                            'isServiceLimited': True|False,
                            'unit': 'TERABYTES',
                            'value': 123
                        },
                        'type': 'DATA_INVENTORY_EVALUATION'|'SENSITIVE_DATA_DISCOVERY'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def get_usage_totals():
    """
    Retrieves (queries) aggregated usage data for an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_usage_totals()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'usageTotals': [
        {
            'currency': 'USD',
            'estimatedCost': 'string',
            'type': 'DATA_INVENTORY_EVALUATION'|'SENSITIVE_DATA_DISCOVERY'
        },
    ]
}


Response Structure

(dict) --The request succeeded.

usageTotals (list) --An array of objects that contains the results of the query. Each object contains the data for a specific usage metric.

(dict) --Provides aggregated data for a usage metric. The value for the metric reports usage data for an account during the past 30 days.

currency (string) --The type of currency that the value for the metric (estimatedCost) is reported in.

estimatedCost (string) --The estimated value for the metric.

type (string) --The name of the metric. Possible values are: DATA_INVENTORY_EVALUATION, for monitoring S3 buckets; and, SENSITIVE_DATA_DISCOVERY, for analyzing sensitive data.










Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'usageTotals': [
            {
                'currency': 'USD',
                'estimatedCost': 'string',
                'type': 'DATA_INVENTORY_EVALUATION'|'SENSITIVE_DATA_DISCOVERY'
            },
        ]
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

def list_classification_jobs(filterCriteria=None, maxResults=None, nextToken=None, sortCriteria=None):
    """
    Retrieves information about the status and settings for one or more classification jobs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_classification_jobs(
        filterCriteria={
            'excludes': [
                {
                    'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                    'key': 'jobType'|'jobStatus'|'createdAt'|'name',
                    'values': [
                        'string',
                    ]
                },
            ],
            'includes': [
                {
                    'comparator': 'EQ'|'GT'|'GTE'|'LT'|'LTE'|'NE'|'CONTAINS',
                    'key': 'jobType'|'jobStatus'|'createdAt'|'name',
                    'values': [
                        'string',
                    ]
                },
            ]
        },
        maxResults=123,
        nextToken='string',
        sortCriteria={
            'attributeName': 'createdAt'|'jobStatus'|'name'|'jobType',
            'orderBy': 'ASC'|'DESC'
        }
    )
    
    
    :type filterCriteria: dict
    :param filterCriteria: The criteria to use to filter the results.\n\nexcludes (list) --An array of objects, one for each condition that determines which jobs to exclude from the results.\n\n(dict) --Specifies a condition that filters the results of a request for information about classification jobs. Each condition consists of a property, an operator, and one or more values.\n\ncomparator (string) --The operator to use to filter the results.\n\nkey (string) --The property to use to filter the results.\n\nvalues (list) --An array that lists one or more values to use to filter the results.\n\n(string) --\n\n\n\n\n\n\nincludes (list) --An array of objects, one for each condition that determines which jobs to include in the results.\n\n(dict) --Specifies a condition that filters the results of a request for information about classification jobs. Each condition consists of a property, an operator, and one or more values.\n\ncomparator (string) --The operator to use to filter the results.\n\nkey (string) --The property to use to filter the results.\n\nvalues (list) --An array that lists one or more values to use to filter the results.\n\n(string) --\n\n\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of items to include in each page of the response.

    :type nextToken: string
    :param nextToken: The nextToken string that specifies which page of results to return in a paginated response.

    :type sortCriteria: dict
    :param sortCriteria: The criteria to use to sort the results.\n\nattributeName (string) --The property to sort the results by.\n\norderBy (string) --The sort order to apply to the results, based on the value for the property specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'items': [
        {
            'bucketDefinitions': [
                {
                    'accountId': 'string',
                    'buckets': [
                        'string',
                    ]
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'jobId': 'string',
            'jobStatus': 'RUNNING'|'PAUSED'|'CANCELLED'|'COMPLETE'|'IDLE',
            'jobType': 'ONE_TIME'|'SCHEDULED',
            'name': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The request succeeded.

items (list) --
An array of objects, one for each job that meets the filter criteria specified in the request.

(dict) --
Provides information about a classification job, including the current status of the job.

bucketDefinitions (list) --
The S3 buckets that the job is configured to analyze.

(dict) --
Specifies which S3 buckets contain the objects that a classification job analyzes.

accountId (string) --
The unique identifier for the AWS account that owns one or more of the buckets. If specified, the job analyzes objects in all the buckets that are owned by the account and meet other conditions specified for the job.

buckets (list) --
An array that lists the names of the buckets.

(string) --






createdAt (datetime) --
The date and time, in UTC and extended ISO 8601 format, when the job was created.

jobId (string) --
The unique identifier for the job.

jobStatus (string) --
The current status of the job. Possible value are:

CANCELLED - The job was cancelled by you or a user of the master account for your organization. A job might also be cancelled if ownership of an S3 bucket changed while the job was running, and that change affected the job\'s access to the bucket.
COMPLETE - Amazon Macie finished processing all the data specified for the job.
IDLE - For a recurring job, the previous scheduled run is complete and the next scheduled run is pending. This value doesn\'t apply to jobs that occur only once.
PAUSED - Amazon Macie started the job, but completion of the job would exceed one or more quotas for your account.
RUNNING - The job is in progress.


jobType (string) --
The schedule for running the job. Possible value are:

ONE_TIME - The job ran or will run only once.
SCHEDULED - The job runs on a daily, weekly, or monthly basis.


name (string) --
The custom name of the job.





nextToken (string) --
The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'items': [
            {
                'bucketDefinitions': [
                    {
                        'accountId': 'string',
                        'buckets': [
                            'string',
                        ]
                    },
                ],
                'createdAt': datetime(2015, 1, 1),
                'jobId': 'string',
                'jobStatus': 'RUNNING'|'PAUSED'|'CANCELLED'|'COMPLETE'|'IDLE',
                'jobType': 'ONE_TIME'|'SCHEDULED',
                'name': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_custom_data_identifiers(maxResults=None, nextToken=None):
    """
    Retrieves a subset of information about all the custom data identifiers for an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_custom_data_identifiers(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of items to include in each page of the response.

    :type nextToken: string
    :param nextToken: The nextToken string that specifies which page of results to return in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'items': [
        {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'description': 'string',
            'id': 'string',
            'name': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The request succeeded.

items (list) --
An array of objects, one for each custom data identifier.

(dict) --
Provides information about a custom data identifier.

arn (string) --
The Amazon Resource Name (ARN) of the custom data identifier.

createdAt (datetime) --
The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created.

description (string) --
The custom description of the custom data identifier.

id (string) --
The unique identifier for the custom data identifier.

name (string) --
The custom name of the custom data identifier.





nextToken (string) --
The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'items': [
            {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'description': 'string',
                'id': 'string',
                'name': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def list_findings(findingCriteria=None, maxResults=None, nextToken=None, sortCriteria=None):
    """
    Retrieves a subset of information about one or more findings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_findings(
        findingCriteria={
            'criterion': {
                'string': {
                    'eq': [
                        'string',
                    ],
                    'gt': 123,
                    'gte': 123,
                    'lt': 123,
                    'lte': 123,
                    'neq': [
                        'string',
                    ]
                }
            }
        },
        maxResults=123,
        nextToken='string',
        sortCriteria={
            'attributeName': 'string',
            'orderBy': 'ASC'|'DESC'
        }
    )
    
    
    :type findingCriteria: dict
    :param findingCriteria: The criteria to use to filter the results.\n\ncriterion (dict) --A condition that specifies the property, operator, and value to use to filter the results.\n\n(string) --\n(dict) --Specifies the operator to use in a property-based condition that filters the results of a query for findings.\n\neq (list) --An equal to condition to apply to a specified property value for findings.\n\n(string) --\n\n\ngt (integer) --A greater than condition to apply to a specified property value for findings.\n\ngte (integer) --A greater than or equal to condition to apply to a specified property value for findings.\n\nlt (integer) --A less than condition to apply to a specified property value for findings.\n\nlte (integer) --A less than or equal to condition to apply to a specified property value for findings.\n\nneq (list) --A not equal to condition to apply to a specified property value for findings.\n\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of items to include in each page of the response.

    :type nextToken: string
    :param nextToken: The nextToken string that specifies which page of results to return in a paginated response.

    :type sortCriteria: dict
    :param sortCriteria: The criteria to use to sort the results.\n\nattributeName (string) --The name of the property to sort the results by. This value can be the name of any property that Amazon Macie defines for a finding.\n\norderBy (string) --The sort order to apply to the results, based on the value for the property specified by the attributeName property. Valid values are: ASC, sort the results in ascending order; and, DESC, sort the results in descending order.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'findingIds': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The request succeeded.

findingIds (list) --
An array of strings, where each string is the unique identifier for a finding that meets the filter criteria specified in the request.

(string) --


nextToken (string) --
The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'findingIds': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_findings_filters(maxResults=None, nextToken=None):
    """
    Retrieves a subset of information about all the findings filters for an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_findings_filters(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of items to include in each page of a paginated response.

    :type nextToken: string
    :param nextToken: The nextToken string that specifies which page of results to return in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'findingsFilterListItems': [
        {
            'arn': 'string',
            'id': 'string',
            'name': 'string',
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The request succeeded.

findingsFilterListItems (list) --
An array of objects, one for each filter that\'s associated with the account.

(dict) --
Provides information about a findings filter.

arn (string) --
The Amazon Resource Name (ARN) of the filter.

id (string) --
The unique identifier for the filter.

name (string) --
The custom name of the filter.

tags (dict) --
A map of key-value pairs that identifies the tags (keys and values) that are associated with the filter.

(string) --
(string) --








nextToken (string) --
The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'findingsFilterListItems': [
            {
                'arn': 'string',
                'id': 'string',
                'name': 'string',
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

def list_invitations(maxResults=None, nextToken=None):
    """
    Retrieves information about all the Amazon Macie membership invitations that were received by an account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_invitations(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of items to include in each page of a paginated response.

    :type nextToken: string
    :param nextToken: The nextToken string that specifies which page of results to return in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'invitations': [
        {
            'accountId': 'string',
            'invitationId': 'string',
            'invitedAt': datetime(2015, 1, 1),
            'relationshipStatus': 'Enabled'|'Paused'|'Invited'|'Created'|'Removed'|'Resigned'|'EmailVerificationInProgress'|'EmailVerificationFailed'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The request succeeded.

invitations (list) --
An array of objects, one for each invitation that was received by the account.

(dict) --
Provides information about an Amazon Macie membership invitation that was received by an account.

accountId (string) --
The AWS account ID for the account that sent the invitation.

invitationId (string) --
The unique identifier for the invitation. Amazon Macie uses this identifier to validate the inviter account with the invitee account.

invitedAt (datetime) --
The date and time, in UTC and extended ISO 8601 format, when the invitation was sent.

relationshipStatus (string) --
The status of the relationship between the account that sent the invitation (inviter account ) and the account that received the invitation (invitee account ).





nextToken (string) --
The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'invitations': [
            {
                'accountId': 'string',
                'invitationId': 'string',
                'invitedAt': datetime(2015, 1, 1),
                'relationshipStatus': 'Enabled'|'Paused'|'Invited'|'Created'|'Removed'|'Resigned'|'EmailVerificationInProgress'|'EmailVerificationFailed'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def list_members(maxResults=None, nextToken=None, onlyAssociated=None):
    """
    Retrieves information about the accounts that are associated with an Amazon Macie master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_members(
        maxResults=123,
        nextToken='string',
        onlyAssociated='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of items to include in each page of a paginated response.

    :type nextToken: string
    :param nextToken: The nextToken string that specifies which page of results to return in a paginated response.

    :type onlyAssociated: string
    :param onlyAssociated: Specifies which accounts to include in the response, based on the status of an account\'s relationship with the master account. By default, the response includes only current member accounts. To include all accounts, set the value for this parameter to false.

    :rtype: dict

ReturnsResponse Syntax
{
    'members': [
        {
            'accountId': 'string',
            'arn': 'string',
            'email': 'string',
            'invitedAt': datetime(2015, 1, 1),
            'masterAccountId': 'string',
            'relationshipStatus': 'Enabled'|'Paused'|'Invited'|'Created'|'Removed'|'Resigned'|'EmailVerificationInProgress'|'EmailVerificationFailed',
            'tags': {
                'string': 'string'
            },
            'updatedAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The request succeeded.

members (list) --
An array of objects, one for each account that\'s associated with the master account and meets the criteria specified by the onlyAssociated request parameter.

(dict) --
Provides information about an account that\'s associated with an Amazon Macie master account.

accountId (string) --
The AWS account ID for the account.

arn (string) --
The Amazon Resource Name (ARN) of the account.

email (string) --
The email address for the account.

invitedAt (datetime) --
The date and time, in UTC and extended ISO 8601 format, when an Amazon Macie membership invitation was last sent to the account. This value is null if a Macie invitation hasn\'t been sent to the account.

masterAccountId (string) --
The AWS account ID for the master account.

relationshipStatus (string) --
The current status of the relationship between the account and the master account.

tags (dict) --
A map of key-value pairs that identifies the tags (keys and values) that are associated with the account in Amazon Macie.

(string) --
(string) --




updatedAt (datetime) --
The date and time, in UTC and extended ISO 8601 format, of the most recent change to the status of the relationship between the account and the master account.





nextToken (string) --
The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'members': [
            {
                'accountId': 'string',
                'arn': 'string',
                'email': 'string',
                'invitedAt': datetime(2015, 1, 1),
                'masterAccountId': 'string',
                'relationshipStatus': 'Enabled'|'Paused'|'Invited'|'Created'|'Removed'|'Resigned'|'EmailVerificationInProgress'|'EmailVerificationFailed',
                'tags': {
                    'string': 'string'
                },
                'updatedAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_organization_admin_accounts(maxResults=None, nextToken=None):
    """
    Retrieves information about the account that\'s designated as the delegated administrator of Amazon Macie for an AWS organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_organization_admin_accounts(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of items to include in each page of a paginated response.

    :type nextToken: string
    :param nextToken: The nextToken string that specifies which page of results to return in a paginated response.

    :rtype: dict

ReturnsResponse Syntax
{
    'adminAccounts': [
        {
            'accountId': 'string',
            'status': 'ENABLED'|'DISABLING_IN_PROGRESS'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The request succeeded.

adminAccounts (list) --
An array of objects, one for each account that\'s designated as a delegated administrator of Amazon Macie for the AWS organization. Of those accounts, only one can have a status of ENABLED.

(dict) --
Provides information about an account that\'s designated as a delegated administrator of Amazon Macie for an AWS organization.

accountId (string) --
The AWS account ID for the account.

status (string) --
The current status of the account as a delegated administrator of Amazon Macie for the organization.





nextToken (string) --
The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'adminAccounts': [
            {
                'accountId': 'string',
                'status': 'ENABLED'|'DISABLING_IN_PROGRESS'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Retrieves the tags (keys and values) that are associated with a classification job, custom data identifier, findings filter, or member account.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the classification job, custom data identifier, findings filter, or member account.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --The request succeeded.

tags (dict) --A map of key-value pairs that identifies the tags (keys and values) that are associated with the resource.

(string) --
(string) --










    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    """
    pass

def put_classification_export_configuration(configuration=None):
    """
    Creates or updates the configuration settings for exporting data classification results.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_classification_export_configuration(
        configuration={
            's3Destination': {
                'bucketName': 'string',
                'keyPrefix': 'string',
                'kmsKeyArn': 'string'
            }
        }
    )
    
    
    :type configuration: dict
    :param configuration: [REQUIRED]\nThe location to export data classification results to, and the encryption settings to use when storing results in that location.\n\ns3Destination (dict) --The S3 bucket to export data classification results to, and the encryption settings to use when storing results in that bucket.\n\nbucketName (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the bucket. This must be the ARN of an existing bucket.\n\nkeyPrefix (string) --The path prefix to use in the path to the location in the bucket. This prefix specifies where to store classification results in the bucket.\n\nkmsKeyArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the AWS Key Management Service master key to use for encryption of the exported results. This must be the ARN of an existing KMS key. In addition, the key must be in the same AWS Region as the bucket.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'configuration': {
        's3Destination': {
            'bucketName': 'string',
            'keyPrefix': 'string',
            'kmsKeyArn': 'string'
        }
    }
}


Response Structure

(dict) --The request succeeded.

configuration (dict) --The location that data classification results are exported to, and the encryption settings that are used when storing results in that location.

s3Destination (dict) --The S3 bucket to export data classification results to, and the encryption settings to use when storing results in that bucket.

bucketName (string) --The Amazon Resource Name (ARN) of the bucket. This must be the ARN of an existing bucket.

keyPrefix (string) --The path prefix to use in the path to the location in the bucket. This prefix specifies where to store classification results in the bucket.

kmsKeyArn (string) --The Amazon Resource Name (ARN) of the AWS Key Management Service master key to use for encryption of the exported results. This must be the ARN of an existing KMS key. In addition, the key must be in the same AWS Region as the bucket.










Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'configuration': {
            's3Destination': {
                'bucketName': 'string',
                'keyPrefix': 'string',
                'kmsKeyArn': 'string'
            }
        }
    }
    
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds or updates one or more tags (keys and values) that are associated with a classification job, custom data identifier, findings filter, or member account.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the classification job, custom data identifier, findings filter, or member account.\n

    :type tags: dict
    :param tags: [REQUIRED]\nA map of key-value pairs that specifies the tags to associate with the resource.\nA resource can have a maximum of 50 tags. Each tag consists of a required tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The request succeeded and there isn\'t any content to include in the body of the response (No Content).






    :return: {}
    
    
    """
    pass

def test_custom_data_identifier(ignoreWords=None, keywords=None, maximumMatchDistance=None, regex=None, sampleText=None):
    """
    Tests a custom data identifier.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.test_custom_data_identifier(
        ignoreWords=[
            'string',
        ],
        keywords=[
            'string',
        ],
        maximumMatchDistance=123,
        regex='string',
        sampleText='string'
    )
    
    
    :type ignoreWords: list
    :param ignoreWords: An array that lists specific character sequences (ignore words) to exclude from the results. If the text matched by the regular expression is the same as any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4 - 90 characters.\n\n(string) --\n\n

    :type keywords: list
    :param keywords: An array that lists specific character sequences (keywords), one of which must be within proximity (maximumMatchDistance) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 4 - 90 characters.\n\n(string) --\n\n

    :type maximumMatchDistance: integer
    :param maximumMatchDistance: The maximum number of characters that can exist between text that matches the regex pattern and the character sequences specified by the keywords array. Macie includes or excludes a result based on the proximity of a keyword to text that matches the regex pattern. The distance can be 1 - 300 characters. The default value is 300.

    :type regex: string
    :param regex: [REQUIRED]\nThe regular expression (regex) that defines the pattern to match. The expression can contain as many as 500 characters.\n

    :type sampleText: string
    :param sampleText: [REQUIRED]\nThe sample text to inspect by using the custom data identifier. The text can contain as many as 1,000 characters.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'matchCount': 123
}


Response Structure

(dict) --
The request succeeded.

matchCount (integer) --
The number of instances of sample text that matched the detection criteria specified in the custom data identifier.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'matchCount': 123
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def unarchive_findings(findingIds=None):
    """
    Reactivates (unarchives) one or more findings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.unarchive_findings(
        findingIds=[
            'string',
        ]
    )
    
    
    :type findingIds: list
    :param findingIds: [REQUIRED]\nAn array of strings that lists the unique identifiers for the findings to reactivate.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded and there isn\'t any content to include in the body of the response (No Content).




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes one or more tags (keys and values) from a classification job, custom data identifier, findings filter, or member account.
    See also: AWS API Documentation
    
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the classification job, custom data identifier, findings filter, or member account.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe key of the tag to remove from the resource. To remove multiple tags, append the tagKeys parameter and argument for each additional tag to remove, separated by an ampersand (&).\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The request succeeded and there isn\'t any content to include in the body of the response (No Content).






    :return: {}
    
    
    """
    pass

def update_classification_job(jobId=None, jobStatus=None):
    """
    Cancels a classification job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_classification_job(
        jobId='string',
        jobStatus='RUNNING'|'PAUSED'|'CANCELLED'|'COMPLETE'|'IDLE'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique identifier for the classification job.\n

    :type jobStatus: string
    :param jobStatus: [REQUIRED]\nThe status to change the job\'s status to. The only supported value is CANCELLED, which cancels the job completely.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The request succeeded. The job\'s status was changed and there isn\'t any content to include in the body of the response (No Content).





Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def update_findings_filter(action=None, description=None, findingCriteria=None, id=None, name=None, position=None):
    """
    Updates the criteria and other settings for a findings filter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_findings_filter(
        action='ARCHIVE'|'NOOP',
        description='string',
        findingCriteria={
            'criterion': {
                'string': {
                    'eq': [
                        'string',
                    ],
                    'gt': 123,
                    'gte': 123,
                    'lt': 123,
                    'lte': 123,
                    'neq': [
                        'string',
                    ]
                }
            }
        },
        id='string',
        name='string',
        position=123
    )
    
    
    :type action: string
    :param action: The action to perform on findings that meet the filter criteria (findingCriteria). Valid values are: ARCHIVE, automatically archive the findings; and, NOOP, don\'t perform any action on the findings.

    :type description: string
    :param description: A custom description of the filter. The description can contain as many as 512 characters.\nWe strongly recommend that you avoid including any sensitive data in the description of a filter. Other users might be able to see the filter\'s description, depending on the actions that they\'re allowed to perform in Amazon Macie.\n

    :type findingCriteria: dict
    :param findingCriteria: The criteria to use to filter findings.\n\ncriterion (dict) --A condition that specifies the property, operator, and value to use to filter the results.\n\n(string) --\n(dict) --Specifies the operator to use in a property-based condition that filters the results of a query for findings.\n\neq (list) --An equal to condition to apply to a specified property value for findings.\n\n(string) --\n\n\ngt (integer) --A greater than condition to apply to a specified property value for findings.\n\ngte (integer) --A greater than or equal to condition to apply to a specified property value for findings.\n\nlt (integer) --A less than condition to apply to a specified property value for findings.\n\nlte (integer) --A less than or equal to condition to apply to a specified property value for findings.\n\nneq (list) --A not equal to condition to apply to a specified property value for findings.\n\n(string) --\n\n\n\n\n\n\n\n\n\n

    :type id: string
    :param id: [REQUIRED]\nThe unique identifier for the Amazon Macie resource or account that the request applies to.\n

    :type name: string
    :param name: A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters.\nWe strongly recommend that you avoid including any sensitive data in the name of a filter. Other users might be able to see the filter\'s name, depending on the actions that they\'re allowed to perform in Amazon Macie.\n

    :type position: integer
    :param position: The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string',
    'id': 'string'
}


Response Structure

(dict) --
The request succeeded. The specified findings filter was updated.

arn (string) --
The Amazon Resource Name (ARN) of the filter that was updated.

id (string) --
The unique identifier for the filter that was updated.







Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {
        'arn': 'string',
        'id': 'string'
    }
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def update_macie_session(findingPublishingFrequency=None, status=None):
    """
    Suspends or re-enables an Amazon Macie account, or updates the configuration settings for a Macie account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_macie_session(
        findingPublishingFrequency='FIFTEEN_MINUTES'|'ONE_HOUR'|'SIX_HOURS',
        status='PAUSED'|'ENABLED'
    )
    
    
    :type findingPublishingFrequency: string
    :param findingPublishingFrequency: Specifies how often to publish findings for the account. This includes adding findings to AWS Security Hub and exporting finding events to Amazon CloudWatch.

    :type status: string
    :param status: Specifies whether to change the status of the account. Valid values are: ENABLED, resume all Amazon Macie activities for the account; and, PAUSED, suspend all Macie activities for the account.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The request succeeded and there isn\'t any content to include in the body of the response (No Content).





Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def update_member_session(id=None, status=None):
    """
    Enables an Amazon Macie master account to suspend or re-enable a member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_member_session(
        id='string',
        status='PAUSED'|'ENABLED'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe unique identifier for the Amazon Macie resource or account that the request applies to.\n

    :type status: string
    :param status: [REQUIRED]\nSpecifies the new status for the account. Valid values are: ENABLED, resume all Amazon Macie activities for the account; and, PAUSED, suspend all Macie activities for the account.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The request succeeded and there isn\'t any content to include in the body of the response (No Content).





Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    Macie2.Client.exceptions.ValidationException
    Macie2.Client.exceptions.InternalServerException
    Macie2.Client.exceptions.ServiceQuotaExceededException
    Macie2.Client.exceptions.AccessDeniedException
    Macie2.Client.exceptions.ResourceNotFoundException
    Macie2.Client.exceptions.ThrottlingException
    Macie2.Client.exceptions.ConflictException
    
    """
    pass

def update_organization_configuration(autoEnable=None):
    """
    Updates Amazon Macie configuration settings for an AWS organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_organization_configuration(
        autoEnable=True|False
    )
    
    
    :type autoEnable: boolean
    :param autoEnable: [REQUIRED]\nSpecifies whether Amazon Macie is enabled automatically for each account, when the account is added to the AWS organization.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The request succeeded and there isn\'t any content to include in the body of the response (No Content).




Exceptions

Macie2.Client.exceptions.ValidationException
Macie2.Client.exceptions.InternalServerException
Macie2.Client.exceptions.ServiceQuotaExceededException
Macie2.Client.exceptions.AccessDeniedException
Macie2.Client.exceptions.ResourceNotFoundException
Macie2.Client.exceptions.ThrottlingException
Macie2.Client.exceptions.ConflictException


    :return: {}
    
    
    """
    pass

