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

def add_attachments_to_set(attachmentSetId=None, attachments=None):
    """
    Adds one or more attachments to an attachment set. If an attachmentSetId is not specified, a new attachment set is created, and the ID of the set is returned in the response. If an attachmentSetId is specified, the attachments are added to the specified set, if it exists.
    An attachment set is a temporary container for attachments that are to be added to a case or case communication. The set is available for one hour after it is created; the expiryTime returned in the response indicates when the set expires. The maximum number of attachments in a set is 3, and the maximum size of any attachment in the set is 5 MB.
    See also: AWS API Documentation
    
    
    :example: response = client.add_attachments_to_set(
        attachmentSetId='string',
        attachments=[
            {
                'fileName': 'string',
                'data': b'bytes'
            },
        ]
    )
    
    
    :type attachmentSetId: string
    :param attachmentSetId: The ID of the attachment set. If an attachmentSetId is not specified, a new attachment set is created, and the ID of the set is returned in the response. If an attachmentSetId is specified, the attachments are added to the specified set, if it exists.

    :type attachments: list
    :param attachments: [REQUIRED]
            One or more attachments to add to the set. The limit is 3 attachments per set, and the size limit is 5 MB per attachment.
            (dict) --An attachment to a case communication. The attachment consists of the file name and the content of the file.
            fileName (string) --The name of the attachment file.
            data (bytes) --The content of the attachment file.
            
            

    :rtype: dict
    :return: {
        'attachmentSetId': 'string',
        'expiryTime': 'string'
    }
    
    
    """
    pass

def add_communication_to_case(caseId=None, communicationBody=None, ccEmailAddresses=None, attachmentSetId=None):
    """
    Adds additional customer communication to an AWS Support case. You use the caseId value to identify the case to add communication to. You can list a set of email addresses to copy on the communication using the ccEmailAddresses value. The communicationBody value contains the text of the communication.
    The response indicates the success or failure of the request.
    This operation implements a subset of the features of the AWS Support Center.
    See also: AWS API Documentation
    
    
    :example: response = client.add_communication_to_case(
        caseId='string',
        communicationBody='string',
        ccEmailAddresses=[
            'string',
        ],
        attachmentSetId='string'
    )
    
    
    :type caseId: string
    :param caseId: The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47

    :type communicationBody: string
    :param communicationBody: [REQUIRED]
            The body of an email communication to add to the support case.
            

    :type ccEmailAddresses: list
    :param ccEmailAddresses: The email addresses in the CC line of an email to be added to the support case.
            (string) --
            

    :type attachmentSetId: string
    :param attachmentSetId: The ID of a set of one or more attachments for the communication to add to the case. Create the set by calling AddAttachmentsToSet

    :rtype: dict
    :return: {
        'result': True|False
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

def create_case(subject=None, serviceCode=None, severityCode=None, categoryCode=None, communicationBody=None, ccEmailAddresses=None, language=None, issueType=None, attachmentSetId=None):
    """
    Creates a new case in the AWS Support Center. This operation is modeled on the behavior of the AWS Support Center Create Case page. Its parameters require you to specify the following information:
    A successful  CreateCase request returns an AWS Support case number. Case numbers are used by the  DescribeCases operation to retrieve existing AWS Support cases.
    See also: AWS API Documentation
    
    
    :example: response = client.create_case(
        subject='string',
        serviceCode='string',
        severityCode='string',
        categoryCode='string',
        communicationBody='string',
        ccEmailAddresses=[
            'string',
        ],
        language='string',
        issueType='string',
        attachmentSetId='string'
    )
    
    
    :type subject: string
    :param subject: [REQUIRED]
            The title of the AWS Support case.
            

    :type serviceCode: string
    :param serviceCode: The code for the AWS service returned by the call to DescribeServices .

    :type severityCode: string
    :param severityCode: The code for the severity level returned by the call to DescribeSeverityLevels .
            Note
            The availability of severity levels depends on each customer's support subscription. In other words, your subscription may not necessarily require the urgent level of response time.
            

    :type categoryCode: string
    :param categoryCode: The category of problem for the AWS Support case.

    :type communicationBody: string
    :param communicationBody: [REQUIRED]
            The communication body text when you create an AWS Support case by calling CreateCase .
            

    :type ccEmailAddresses: list
    :param ccEmailAddresses: A list of email addresses that AWS Support copies on case correspondence.
            (string) --
            

    :type language: string
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.

    :type issueType: string
    :param issueType: The type of issue for the case. You can specify either 'customer-service' or 'technical.' If you do not indicate a value, the default is 'technical.'

    :type attachmentSetId: string
    :param attachmentSetId: The ID of a set of one or more attachments for the case. Create the set by using AddAttachmentsToSet .

    :rtype: dict
    :return: {
        'caseId': 'string'
    }
    
    
    :returns: 
    subject (string) -- [REQUIRED]
    The title of the AWS Support case.
    
    serviceCode (string) -- The code for the AWS service returned by the call to  DescribeServices .
    severityCode (string) -- The code for the severity level returned by the call to  DescribeSeverityLevels .
    
    Note
    The availability of severity levels depends on each customer's support subscription. In other words, your subscription may not necessarily require the urgent level of response time.
    
    
    categoryCode (string) -- The category of problem for the AWS Support case.
    communicationBody (string) -- [REQUIRED]
    The communication body text when you create an AWS Support case by calling  CreateCase .
    
    ccEmailAddresses (list) -- A list of email addresses that AWS Support copies on case correspondence.
    
    (string) --
    
    
    language (string) -- The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations that take them.
    issueType (string) -- The type of issue for the case. You can specify either "customer-service" or "technical." If you do not indicate a value, the default is "technical."
    attachmentSetId (string) -- The ID of a set of one or more attachments for the case. Create the set by using  AddAttachmentsToSet .
    
    """
    pass

def describe_attachment(attachmentId=None):
    """
    Returns the attachment that has the specified ID. Attachment IDs are generated by the case management system when you add an attachment to a case or case communication. Attachment IDs are returned in the  AttachmentDetails objects that are returned by the  DescribeCommunications operation.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_attachment(
        attachmentId='string'
    )
    
    
    :type attachmentId: string
    :param attachmentId: [REQUIRED]
            The ID of the attachment to return. Attachment IDs are returned by the DescribeCommunications operation.
            

    :rtype: dict
    :return: {
        'attachment': {
            'fileName': 'string',
            'data': b'bytes'
        }
    }
    
    
    """
    pass

def describe_cases(caseIdList=None, displayId=None, afterTime=None, beforeTime=None, includeResolvedCases=None, nextToken=None, maxResults=None, language=None, includeCommunications=None):
    """
    Returns a list of cases that you specify by passing one or more case IDs. In addition, you can filter the cases by date by setting values for the afterTime and beforeTime request parameters. You can set values for the includeResolvedCases and includeCommunications request parameters to control how much information is returned.
    Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request for data might cause an error.
    The response returns the following in JSON format:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_cases(
        caseIdList=[
            'string',
        ],
        displayId='string',
        afterTime='string',
        beforeTime='string',
        includeResolvedCases=True|False,
        nextToken='string',
        maxResults=123,
        language='string',
        includeCommunications=True|False
    )
    
    
    :type caseIdList: list
    :param caseIdList: A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.
            (string) --
            

    :type displayId: string
    :param displayId: The ID displayed for a case in the AWS Support Center user interface.

    :type afterTime: string
    :param afterTime: The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.

    :type beforeTime: string
    :param beforeTime: The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.

    :type includeResolvedCases: boolean
    :param includeResolvedCases: Specifies whether resolved support cases should be included in the DescribeCases results. The default is false .

    :type nextToken: string
    :param nextToken: A resumption point for pagination.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return before paginating.

    :type language: string
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.

    :type includeCommunications: boolean
    :param includeCommunications: Specifies whether communications should be included in the DescribeCases results. The default is true .

    :rtype: dict
    :return: {
        'cases': [
            {
                'caseId': 'string',
                'displayId': 'string',
                'subject': 'string',
                'status': 'string',
                'serviceCode': 'string',
                'categoryCode': 'string',
                'severityCode': 'string',
                'submittedBy': 'string',
                'timeCreated': 'string',
                'recentCommunications': {
                    'communications': [
                        {
                            'caseId': 'string',
                            'body': 'string',
                            'submittedBy': 'string',
                            'timeCreated': 'string',
                            'attachmentSet': [
                                {
                                    'attachmentId': 'string',
                                    'fileName': 'string'
                                },
                            ]
                        },
                    ],
                    'nextToken': 'string'
                },
                'ccEmailAddresses': [
                    'string',
                ],
                'language': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    caseIdList (list) -- A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.
    
    (string) --
    
    
    displayId (string) -- The ID displayed for a case in the AWS Support Center user interface.
    afterTime (string) -- The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.
    beforeTime (string) -- The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.
    includeResolvedCases (boolean) -- Specifies whether resolved support cases should be included in the  DescribeCases results. The default is false .
    nextToken (string) -- A resumption point for pagination.
    maxResults (integer) -- The maximum number of results to return before paginating.
    language (string) -- The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations that take them.
    includeCommunications (boolean) -- Specifies whether communications should be included in the  DescribeCases results. The default is true .
    
    """
    pass

def describe_communications(caseId=None, beforeTime=None, afterTime=None, nextToken=None, maxResults=None):
    """
    Returns communications (and attachments) for one or more support cases. You can use the afterTime and beforeTime parameters to filter by date. You can use the caseId parameter to restrict the results to a particular case.
    Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request for data might cause an error.
    You can use the maxResults and nextToken parameters to control the pagination of the result set. Set maxResults to the number of cases you want displayed on each page, and use nextToken to specify the resumption of pagination.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_communications(
        caseId='string',
        beforeTime='string',
        afterTime='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type caseId: string
    :param caseId: [REQUIRED]
            The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47
            

    :type beforeTime: string
    :param beforeTime: The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.

    :type afterTime: string
    :param afterTime: The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.

    :type nextToken: string
    :param nextToken: A resumption point for pagination.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return before paginating.

    :rtype: dict
    :return: {
        'communications': [
            {
                'caseId': 'string',
                'body': 'string',
                'submittedBy': 'string',
                'timeCreated': 'string',
                'attachmentSet': [
                    {
                        'attachmentId': 'string',
                        'fileName': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def describe_services(serviceCodeList=None, language=None):
    """
    Returns the current list of AWS services and a list of service categories that applies to each one. You then use service names and categories in your  CreateCase requests. Each AWS service has its own set of categories.
    The service codes and category codes correspond to the values that are displayed in the Service and Category drop-down lists on the AWS Support Center Create Case page. The values in those fields, however, do not necessarily match the service codes and categories returned by the DescribeServices request. Always use the service codes and categories obtained programmatically. This practice ensures that you always have the most recent set of service and category codes.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_services(
        serviceCodeList=[
            'string',
        ],
        language='string'
    )
    
    
    :type serviceCodeList: list
    :param serviceCodeList: A JSON-formatted list of service codes available for AWS services.
            (string) --
            

    :type language: string
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.

    :rtype: dict
    :return: {
        'services': [
            {
                'code': 'string',
                'name': 'string',
                'categories': [
                    {
                        'code': 'string',
                        'name': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def describe_severity_levels(language=None):
    """
    Returns the list of severity levels that you can assign to an AWS Support case. The severity level for a case is also a field in the  CaseDetails data type included in any  CreateCase request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_severity_levels(
        language='string'
    )
    
    
    :type language: string
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.

    :rtype: dict
    :return: {
        'severityLevels': [
            {
                'code': 'string',
                'name': 'string'
            },
        ]
    }
    
    
    """
    pass

def describe_trusted_advisor_check_refresh_statuses(checkIds=None):
    """
    Returns the refresh status of the Trusted Advisor checks that have the specified check IDs. Check IDs can be obtained by calling  DescribeTrustedAdvisorChecks .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_trusted_advisor_check_refresh_statuses(
        checkIds=[
            'string',
        ]
    )
    
    
    :type checkIds: list
    :param checkIds: [REQUIRED]
            The IDs of the Trusted Advisor checks to get the status of. Note: Specifying the check ID of a check that is automatically refreshed causes an InvalidParameterValue error.
            (string) --
            

    :rtype: dict
    :return: {
        'statuses': [
            {
                'checkId': 'string',
                'status': 'string',
                'millisUntilNextRefreshable': 123
            },
        ]
    }
    
    
    """
    pass

def describe_trusted_advisor_check_result(checkId=None, language=None):
    """
    Returns the results of the Trusted Advisor check that has the specified check ID. Check IDs can be obtained by calling  DescribeTrustedAdvisorChecks .
    The response contains a  TrustedAdvisorCheckResult object, which contains these three objects:
    In addition, the response contains these fields:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_trusted_advisor_check_result(
        checkId='string',
        language='string'
    )
    
    
    :type checkId: string
    :param checkId: [REQUIRED]
            The unique identifier for the Trusted Advisor check.
            

    :type language: string
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.

    :rtype: dict
    :return: {
        'result': {
            'checkId': 'string',
            'timestamp': 'string',
            'status': 'string',
            'resourcesSummary': {
                'resourcesProcessed': 123,
                'resourcesFlagged': 123,
                'resourcesIgnored': 123,
                'resourcesSuppressed': 123
            },
            'categorySpecificSummary': {
                'costOptimizing': {
                    'estimatedMonthlySavings': 123.0,
                    'estimatedPercentMonthlySavings': 123.0
                }
            },
            'flaggedResources': [
                {
                    'status': 'string',
                    'region': 'string',
                    'resourceId': 'string',
                    'isSuppressed': True|False,
                    'metadata': [
                        'string',
                    ]
                },
            ]
        }
    }
    
    
    :returns: 
    status. The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or "not_available".
    timestamp. The time of the last refresh of the check.
    checkId. The unique identifier for the check.
    
    """
    pass

def describe_trusted_advisor_check_summaries(checkIds=None):
    """
    Returns the summaries of the results of the Trusted Advisor checks that have the specified check IDs. Check IDs can be obtained by calling  DescribeTrustedAdvisorChecks .
    The response contains an array of  TrustedAdvisorCheckSummary objects.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_trusted_advisor_check_summaries(
        checkIds=[
            'string',
        ]
    )
    
    
    :type checkIds: list
    :param checkIds: [REQUIRED]
            The IDs of the Trusted Advisor checks.
            (string) --
            

    :rtype: dict
    :return: {
        'summaries': [
            {
                'checkId': 'string',
                'timestamp': 'string',
                'status': 'string',
                'hasFlaggedResources': True|False,
                'resourcesSummary': {
                    'resourcesProcessed': 123,
                    'resourcesFlagged': 123,
                    'resourcesIgnored': 123,
                    'resourcesSuppressed': 123
                },
                'categorySpecificSummary': {
                    'costOptimizing': {
                        'estimatedMonthlySavings': 123.0,
                        'estimatedPercentMonthlySavings': 123.0
                    }
                }
            },
        ]
    }
    
    
    """
    pass

def describe_trusted_advisor_checks(language=None):
    """
    Returns information about all available Trusted Advisor checks, including name, ID, category, description, and metadata. You must specify a language code; English ("en") and Japanese ("ja") are currently supported. The response contains a  TrustedAdvisorCheckDescription for each check.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_trusted_advisor_checks(
        language='string'
    )
    
    
    :type language: string
    :param language: [REQUIRED]
            The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.
            

    :rtype: dict
    :return: {
        'checks': [
            {
                'id': 'string',
                'name': 'string',
                'description': 'string',
                'category': 'string',
                'metadata': [
                    'string',
                ]
            },
        ]
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

def refresh_trusted_advisor_check(checkId=None):
    """
    Requests a refresh of the Trusted Advisor check that has the specified check ID. Check IDs can be obtained by calling  DescribeTrustedAdvisorChecks .
    The response contains a  TrustedAdvisorCheckRefreshStatus object, which contains these fields:
    See also: AWS API Documentation
    
    
    :example: response = client.refresh_trusted_advisor_check(
        checkId='string'
    )
    
    
    :type checkId: string
    :param checkId: [REQUIRED]
            The unique identifier for the Trusted Advisor check to refresh. Note: Specifying the check ID of a check that is automatically refreshed causes an InvalidParameterValue error.
            

    :rtype: dict
    :return: {
        'status': {
            'checkId': 'string',
            'status': 'string',
            'millisUntilNextRefreshable': 123
        }
    }
    
    
    """
    pass

def resolve_case(caseId=None):
    """
    Takes a caseId and returns the initial state of the case along with the state of the case after the call to  ResolveCase completed.
    See also: AWS API Documentation
    
    
    :example: response = client.resolve_case(
        caseId='string'
    )
    
    
    :type caseId: string
    :param caseId: The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47

    :rtype: dict
    :return: {
        'initialCaseStatus': 'string',
        'finalCaseStatus': 'string'
    }
    
    
    """
    pass

