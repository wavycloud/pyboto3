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
    Adds one or more attachments to an attachment set.
    An attachment set is a temporary container for attachments that you add to a case or case communication. The set is available for 1 hour after it\'s created. The expiryTime returned in the response is when the set expires.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param attachments: [REQUIRED]\nOne or more attachments to add to the set. You can add up to three attachments per set. The size limit is 5 MB per attachment.\nIn the Attachment object, use the data parameter to specify the contents of the attachment file. In the previous request syntax, the value for data appear as blob , which is represented as a base64-encoded string. The value for fileName is the name of the attachment, such as troubleshoot-screenshot.png .\n\n(dict) --An attachment to a case communication. The attachment consists of the file name and the content of the file.\n\nfileName (string) --The name of the attachment file.\n\ndata (bytes) --The content of the attachment file.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'attachmentSetId': 'string',
    'expiryTime': 'string'
}


Response Structure

(dict) --
The ID and expiry time of the attachment set returned by the  AddAttachmentsToSet operation.

attachmentSetId (string) --
The ID of the attachment set. If an attachmentSetId was not specified, a new attachment set is created, and the ID of the set is returned in the response. If an attachmentSetId was specified, the attachments are added to the specified set, if it exists.

expiryTime (string) --
The time and date when the attachment set expires.







Exceptions

Support.Client.exceptions.InternalServerError
Support.Client.exceptions.AttachmentSetIdNotFound
Support.Client.exceptions.AttachmentSetExpired
Support.Client.exceptions.AttachmentSetSizeLimitExceeded
Support.Client.exceptions.AttachmentLimitExceeded


    :return: {
        'attachmentSetId': 'string',
        'expiryTime': 'string'
    }
    
    
    :returns: 
    Support.Client.exceptions.InternalServerError
    Support.Client.exceptions.AttachmentSetIdNotFound
    Support.Client.exceptions.AttachmentSetExpired
    Support.Client.exceptions.AttachmentSetSizeLimitExceeded
    Support.Client.exceptions.AttachmentLimitExceeded
    
    """
    pass

def add_communication_to_case(caseId=None, communicationBody=None, ccEmailAddresses=None, attachmentSetId=None):
    """
    Adds additional customer communication to an AWS Support case. You use the caseId value to identify the case to add communication to. You can list a set of email addresses to copy on the communication using the ccEmailAddresses value. The communicationBody value contains the text of the communication.
    The response indicates the success or failure of the request.
    This operation implements a subset of the features of the AWS Support Center.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param communicationBody: [REQUIRED]\nThe body of an email communication to add to the support case.\n

    :type ccEmailAddresses: list
    :param ccEmailAddresses: The email addresses in the CC line of an email to be added to the support case.\n\n(string) --\n\n

    :type attachmentSetId: string
    :param attachmentSetId: The ID of a set of one or more attachments for the communication to add to the case. Create the set by calling AddAttachmentsToSet

    :rtype: dict

ReturnsResponse Syntax
{
    'result': True|False
}


Response Structure

(dict) --
The result of the  AddCommunicationToCase operation.

result (boolean) --
True if  AddCommunicationToCase succeeds. Otherwise, returns an error.







Exceptions

Support.Client.exceptions.InternalServerError
Support.Client.exceptions.CaseIdNotFound
Support.Client.exceptions.AttachmentSetIdNotFound
Support.Client.exceptions.AttachmentSetExpired


    :return: {
        'result': True|False
    }
    
    
    :returns: 
    Support.Client.exceptions.InternalServerError
    Support.Client.exceptions.CaseIdNotFound
    Support.Client.exceptions.AttachmentSetIdNotFound
    Support.Client.exceptions.AttachmentSetExpired
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_case(subject=None, serviceCode=None, severityCode=None, categoryCode=None, communicationBody=None, ccEmailAddresses=None, language=None, issueType=None, attachmentSetId=None):
    """
    Creates a case in the AWS Support Center. This operation is similar to how you create a case in the AWS Support Center Create Case page.
    The AWS Support API doesn\'t support requesting service limit increases. You can submit a service limit increase in the following ways:
    A successful  CreateCase request returns an AWS Support case number. You can use the  DescribeCases operation and specify the case number to get existing AWS Support cases. After you create a case, you can use the  AddCommunicationToCase operation to add additional communication or attachments to an existing case.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param subject: [REQUIRED]\nThe title of the AWS Support case. The title appears in the Subject field on the AWS Support Center Create Case page.\n

    :type serviceCode: string
    :param serviceCode: The code for the AWS service. You can use the DescribeServices operation to get the possible serviceCode values.

    :type severityCode: string
    :param severityCode: A value that indicates the urgency of the case. This value determines the response time according to your service level agreement with AWS Support. You can use the DescribeSeverityLevels operation to get the possible values for severityCode .\nFor more information, see SeverityLevel and Choosing a Severity in the AWS Support User Guide .\n\nNote\nThe availability of severity levels depends on the support plan for the AWS account.\n\n

    :type categoryCode: string
    :param categoryCode: The category of problem for the AWS Support case. You also use the DescribeServices operation to get the category code for a service. Each AWS service defines its own set of category codes.

    :type communicationBody: string
    :param communicationBody: [REQUIRED]\nThe communication body text that describes the issue. This text appears in the Description field on the AWS Support Center Create Case page.\n

    :type ccEmailAddresses: list
    :param ccEmailAddresses: A list of email addresses that AWS Support copies on case correspondence. AWS Support identifies the account that creates the case when you specify your AWS credentials in an HTTP POST method or use the AWS SDKs .\n\n(string) --\n\n

    :type language: string
    :param language: The language in which AWS Support handles the case. You must specify the ISO 639-1 code for the language parameter if you want support in that language. Currently, English ('en') and Japanese ('ja') are supported.

    :type issueType: string
    :param issueType: The type of issue for the case. You can specify customer-service or technical . If you don\'t specify a value, the default is technical .

    :type attachmentSetId: string
    :param attachmentSetId: The ID of a set of one or more attachments for the case. Create the set by using the AddAttachmentsToSet operation.

    :rtype: dict

ReturnsResponse Syntax
{
    'caseId': 'string'
}


Response Structure

(dict) --
The AWS Support case ID returned by a successful completion of the  CreateCase operation.

caseId (string) --
The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string in the following format: case-12345678910-2013-c4c1d2bf33c5cf47







Exceptions

Support.Client.exceptions.InternalServerError
Support.Client.exceptions.CaseCreationLimitExceeded
Support.Client.exceptions.AttachmentSetIdNotFound
Support.Client.exceptions.AttachmentSetExpired


    :return: {
        'caseId': 'string'
    }
    
    
    :returns: 
    The caseId is separate from the displayId that appears in the Support Center . You can use the  DescribeCases operation to get the displayId .
    
    """
    pass

def describe_attachment(attachmentId=None):
    """
    Returns the attachment that has the specified ID. Attachments can include screenshots, error logs, or other files that describe your issue. Attachment IDs are generated by the case management system when you add an attachment to a case or case communication. Attachment IDs are returned in the  AttachmentDetails objects that are returned by the  DescribeCommunications operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_attachment(
        attachmentId='string'
    )
    
    
    :type attachmentId: string
    :param attachmentId: [REQUIRED]\nThe ID of the attachment to return. Attachment IDs are returned by the DescribeCommunications operation.\n

    :rtype: dict
ReturnsResponse Syntax{
    'attachment': {
        'fileName': 'string',
        'data': b'bytes'
    }
}


Response Structure

(dict) --The content and file name of the attachment returned by the  DescribeAttachment operation.

attachment (dict) --This object includes the attachment content and file name.
In the previous response syntax, the value for the data parameter appears as blob , which is represented as a base64-encoded string. The value for fileName is the name of the attachment, such as troubleshoot-screenshot.png .

fileName (string) --The name of the attachment file.

data (bytes) --The content of the attachment file.








Exceptions

Support.Client.exceptions.InternalServerError
Support.Client.exceptions.DescribeAttachmentLimitExceeded
Support.Client.exceptions.AttachmentIdNotFound


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
    
    Exceptions
    
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
    :param caseIdList: A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.\n\n(string) --\n\n

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

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Returns an array of  CaseDetails objects and a nextToken that defines a point for pagination in the result set.

cases (list) --
The details for the cases that match the request.

(dict) --
A JSON-formatted object that contains the metadata for a support case. It is contained the response from a  DescribeCases request. CaseDetails contains the following fields:

caseId. The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47 .
categoryCode. The category of problem for the AWS Support case. Corresponds to the CategoryCode values returned by a call to  DescribeServices .
displayId. The identifier for the case on pages in the AWS Support Center.
language. The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations that take them.
recentCommunications. One or more  Communication objects. Fields of these objects are attachments , body , caseId , submittedBy , and timeCreated .
nextToken. A resumption point for pagination.
serviceCode. The identifier for the AWS service that corresponds to the service code defined in the call to  DescribeServices .
severityCode. The severity code assigned to the case. Contains one of the values returned by the call to  DescribeSeverityLevels . The possible values are: low , normal , high , urgent , and critical .
status. The status of the case in the AWS Support Center. Valid values:
opened
pending-customer-action
reopened
resolved
unassigned
work-in-progress


subject. The subject line of the case.
submittedBy. The email address of the account that submitted the case.
timeCreated. The time the case was created, in ISO-8601 format.


caseId (string) --
The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47

displayId (string) --
The ID displayed for the case in the AWS Support Center. This is a numeric string.

subject (string) --
The subject line for the case in the AWS Support Center.

status (string) --
The status of the case.
Valid values:

opened
pending-customer-action
reopened
resolved
unassigned
work-in-progress


serviceCode (string) --
The code for the AWS service. You can get a list of codes and the corresponding service names by calling  DescribeServices .

categoryCode (string) --
The category of problem for the AWS Support case.

severityCode (string) --
The code for the severity level returned by the call to  DescribeSeverityLevels .

submittedBy (string) --
The email address of the account that submitted the case.

timeCreated (string) --
The time that the case was case created in the AWS Support Center.

recentCommunications (dict) --
The five most recent communications between you and AWS Support Center, including the IDs of any attachments to the communications. Also includes a nextToken that you can use to retrieve earlier communications.

communications (list) --
The five most recent communications associated with the case.

(dict) --
A communication associated with an AWS Support case. The communication consists of the case ID, the message body, attachment information, the submitter of the communication, and the date and time of the communication.

caseId (string) --
The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47

body (string) --
The text of the communication between the customer and AWS Support.

submittedBy (string) --
The identity of the account that submitted, or responded to, the support case. Customer entries include the role or IAM user as well as the email address. For example, "AdminRole (Role) <someone@example.com>. Entries from the AWS Support team display "Amazon Web Services," and do not show an email address.

timeCreated (string) --
The time the communication was created.

attachmentSet (list) --
Information about the attachments to the case communication.

(dict) --
The file name and ID of an attachment to a case communication. You can use the ID to retrieve the attachment with the  DescribeAttachment operation.

attachmentId (string) --
The ID of the attachment.

fileName (string) --
The file name of the attachment.









nextToken (string) --
A resumption point for pagination.



ccEmailAddresses (list) --
The email addresses that receive copies of communication about the case.

(string) --


language (string) --
The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ("en") and Japanese ("ja"). Language parameters must be passed explicitly for operations that take them.





nextToken (string) --
A resumption point for pagination.







Exceptions

Support.Client.exceptions.InternalServerError
Support.Client.exceptions.CaseIdNotFound


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
    
    Exceptions
    
    :example: response = client.describe_communications(
        caseId='string',
        beforeTime='string',
        afterTime='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type caseId: string
    :param caseId: [REQUIRED]\nThe AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47\n

    :type beforeTime: string
    :param beforeTime: The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.

    :type afterTime: string
    :param afterTime: The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.

    :type nextToken: string
    :param nextToken: A resumption point for pagination.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return before paginating.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
The communications returned by the  DescribeCommunications operation.

communications (list) --
The communications for the case.

(dict) --
A communication associated with an AWS Support case. The communication consists of the case ID, the message body, attachment information, the submitter of the communication, and the date and time of the communication.

caseId (string) --
The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47

body (string) --
The text of the communication between the customer and AWS Support.

submittedBy (string) --
The identity of the account that submitted, or responded to, the support case. Customer entries include the role or IAM user as well as the email address. For example, "AdminRole (Role) <someone@example.com>. Entries from the AWS Support team display "Amazon Web Services," and do not show an email address.

timeCreated (string) --
The time the communication was created.

attachmentSet (list) --
Information about the attachments to the case communication.

(dict) --
The file name and ID of an attachment to a case communication. You can use the ID to retrieve the attachment with the  DescribeAttachment operation.

attachmentId (string) --
The ID of the attachment.

fileName (string) --
The file name of the attachment.









nextToken (string) --
A resumption point for pagination.







Exceptions

Support.Client.exceptions.InternalServerError
Support.Client.exceptions.CaseIdNotFound


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
    
    
    :returns: 
    Support.Client.exceptions.InternalServerError
    Support.Client.exceptions.CaseIdNotFound
    
    """
    pass

def describe_services(serviceCodeList=None, language=None):
    """
    Returns the current list of AWS services and a list of service categories that applies to each one. You then use service names and categories in your  CreateCase requests. Each AWS service has its own set of categories.
    The service codes and category codes correspond to the values that are displayed in the Service and Category drop-down lists on the AWS Support Center Create Case page. The values in those fields, however, do not necessarily match the service codes and categories returned by the DescribeServices request. Always use the service codes and categories obtained programmatically. This practice ensures that you always have the most recent set of service and category codes.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_services(
        serviceCodeList=[
            'string',
        ],
        language='string'
    )
    
    
    :type serviceCodeList: list
    :param serviceCodeList: A JSON-formatted list of service codes available for AWS services.\n\n(string) --\n\n

    :type language: string
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
The list of AWS services returned by the  DescribeServices operation.

services (list) --
A JSON-formatted list of AWS services.

(dict) --
Information about an AWS service returned by the  DescribeServices operation.

code (string) --
The code for an AWS service returned by the  DescribeServices response. The name element contains the corresponding friendly name.

name (string) --
The friendly name for an AWS service. The code element contains the corresponding code.

categories (list) --
A list of categories that describe the type of support issue a case describes. Categories consist of a category name and a category code. Category names and codes are passed to AWS Support when you call  CreateCase .

(dict) --
A JSON-formatted name/value pair that represents the category name and category code of the problem, selected from the  DescribeServices response for each AWS service.

code (string) --
The category code for the support case.

name (string) --
The category name for the support case.















Exceptions

Support.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    Support.Client.exceptions.InternalServerError
    
    """
    pass

def describe_severity_levels(language=None):
    """
    Returns the list of severity levels that you can assign to an AWS Support case. The severity level for a case is also a field in the  CaseDetails data type included in any  CreateCase request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_severity_levels(
        language='string'
    )
    
    
    :type language: string
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.

    :rtype: dict
ReturnsResponse Syntax{
    'severityLevels': [
        {
            'code': 'string',
            'name': 'string'
        },
    ]
}


Response Structure

(dict) --The list of severity levels returned by the  DescribeSeverityLevels operation.

severityLevels (list) --The available severity levels for the support case. Available severity levels are defined by your service level agreement with AWS.

(dict) --A code and name pair that represents the severity level of a support case. The available values depend on the support plan for the account. For more information, see Choosing a Severity .

code (string) --The code for case severity level.
Valid values: low | normal | high | urgent | critical

name (string) --The name of the severity level that corresponds to the severity level code.

Note
The values returned by the API differ from the values that are displayed in the AWS Support Center. For example, for the code "low", the API name is "Low", but the name in the Support Center is "General guidance". These are the Support Center code/name mappings:

low : General guidance
normal : System impaired
high : Production system impaired
urgent : Production system down
critical : Business-critical system down


For more information, see Choosing a Severity










Exceptions

Support.Client.exceptions.InternalServerError


    :return: {
        'severityLevels': [
            {
                'code': 'string',
                'name': 'string'
            },
        ]
    }
    
    
    :returns: 
    Support.Client.exceptions.InternalServerError
    
    """
    pass

def describe_trusted_advisor_check_refresh_statuses(checkIds=None):
    """
    Returns the refresh status of the Trusted Advisor checks that have the specified check IDs. Check IDs can be obtained by calling  DescribeTrustedAdvisorChecks .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_trusted_advisor_check_refresh_statuses(
        checkIds=[
            'string',
        ]
    )
    
    
    :type checkIds: list
    :param checkIds: [REQUIRED]\nThe IDs of the Trusted Advisor checks to get the status of. Note: Specifying the check ID of a check that is automatically refreshed causes an InvalidParameterValue error.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'statuses': [
        {
            'checkId': 'string',
            'status': 'string',
            'millisUntilNextRefreshable': 123
        },
    ]
}


Response Structure

(dict) --The statuses of the Trusted Advisor checks returned by the  DescribeTrustedAdvisorCheckRefreshStatuses operation.

statuses (list) --The refresh status of the specified Trusted Advisor checks.

(dict) --The refresh status of a Trusted Advisor check.

checkId (string) --The unique identifier for the Trusted Advisor check.

status (string) --The status of the Trusted Advisor check for which a refresh has been requested:

none: The check is not refreshed or the non-success status exceeds the timeout
enqueued: The check refresh requests has entered the refresh queue
processing: The check refresh request is picked up by the rule processing engine
success: The check is successfully refreshed
abandoned: The check refresh has failed


millisUntilNextRefreshable (integer) --The amount of time, in milliseconds, until the Trusted Advisor check is eligible for refresh.










Exceptions

Support.Client.exceptions.InternalServerError


    :return: {
        'statuses': [
            {
                'checkId': 'string',
                'status': 'string',
                'millisUntilNextRefreshable': 123
            },
        ]
    }
    
    
    :returns: 
    none: The check is not refreshed or the non-success status exceeds the timeout
    enqueued: The check refresh requests has entered the refresh queue
    processing: The check refresh request is picked up by the rule processing engine
    success: The check is successfully refreshed
    abandoned: The check refresh has failed
    
    """
    pass

def describe_trusted_advisor_check_result(checkId=None, language=None):
    """
    Returns the results of the Trusted Advisor check that has the specified check ID. Check IDs can be obtained by calling  DescribeTrustedAdvisorChecks .
    The response contains a  TrustedAdvisorCheckResult object, which contains these three objects:
    In addition, the response contains these fields:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_trusted_advisor_check_result(
        checkId='string',
        language='string'
    )
    
    
    :type checkId: string
    :param checkId: [REQUIRED]\nThe unique identifier for the Trusted Advisor check.\n

    :type language: string
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
The result of the Trusted Advisor check returned by the  DescribeTrustedAdvisorCheckResult operation.

result (dict) --
The detailed results of the Trusted Advisor check.

checkId (string) --
The unique identifier for the Trusted Advisor check.

timestamp (string) --
The time of the last refresh of the check.

status (string) --
The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or "not_available".

resourcesSummary (dict) --
Details about AWS resources that were analyzed in a call to Trusted Advisor  DescribeTrustedAdvisorCheckSummaries .

resourcesProcessed (integer) --
The number of AWS resources that were analyzed by the Trusted Advisor check.

resourcesFlagged (integer) --
The number of AWS resources that were flagged (listed) by the Trusted Advisor check.

resourcesIgnored (integer) --
The number of AWS resources ignored by Trusted Advisor because information was unavailable.

resourcesSuppressed (integer) --
The number of AWS resources ignored by Trusted Advisor because they were marked as suppressed by the user.



categorySpecificSummary (dict) --
Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.

costOptimizing (dict) --
The summary information about cost savings for a Trusted Advisor check that is in the Cost Optimizing category.

estimatedMonthlySavings (float) --
The estimated monthly savings that might be realized if the recommended operations are taken.

estimatedPercentMonthlySavings (float) --
The estimated percentage of savings that might be realized if the recommended operations are taken.





flaggedResources (list) --
The details about each resource listed in the check result.

(dict) --
Contains information about a resource identified by a Trusted Advisor check.

status (string) --
The status code for the resource identified in the Trusted Advisor check.

region (string) --
The AWS region in which the identified resource is located.

resourceId (string) --
The unique identifier for the identified resource.

isSuppressed (boolean) --
Specifies whether the AWS resource was ignored by Trusted Advisor because it was marked as suppressed by the user.

metadata (list) --
Additional information about the identified resource. The exact metadata and its order can be obtained by inspecting the  TrustedAdvisorCheckDescription object returned by the call to  DescribeTrustedAdvisorChecks . Metadata contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data.

(string) --














Exceptions

Support.Client.exceptions.InternalServerError


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
    
    Exceptions
    
    :example: response = client.describe_trusted_advisor_check_summaries(
        checkIds=[
            'string',
        ]
    )
    
    
    :type checkIds: list
    :param checkIds: [REQUIRED]\nThe IDs of the Trusted Advisor checks.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --The summaries of the Trusted Advisor checks returned by the  DescribeTrustedAdvisorCheckSummaries operation.

summaries (list) --The summary information for the requested Trusted Advisor checks.

(dict) --A summary of a Trusted Advisor check result, including the alert status, last refresh, and number of resources examined.

checkId (string) --The unique identifier for the Trusted Advisor check.

timestamp (string) --The time of the last refresh of the check.

status (string) --The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or "not_available".

hasFlaggedResources (boolean) --Specifies whether the Trusted Advisor check has flagged resources.

resourcesSummary (dict) --Details about AWS resources that were analyzed in a call to Trusted Advisor  DescribeTrustedAdvisorCheckSummaries .

resourcesProcessed (integer) --The number of AWS resources that were analyzed by the Trusted Advisor check.

resourcesFlagged (integer) --The number of AWS resources that were flagged (listed) by the Trusted Advisor check.

resourcesIgnored (integer) --The number of AWS resources ignored by Trusted Advisor because information was unavailable.

resourcesSuppressed (integer) --The number of AWS resources ignored by Trusted Advisor because they were marked as suppressed by the user.



categorySpecificSummary (dict) --Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.

costOptimizing (dict) --The summary information about cost savings for a Trusted Advisor check that is in the Cost Optimizing category.

estimatedMonthlySavings (float) --The estimated monthly savings that might be realized if the recommended operations are taken.

estimatedPercentMonthlySavings (float) --The estimated percentage of savings that might be realized if the recommended operations are taken.














Exceptions

Support.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    Support.Client.exceptions.InternalServerError
    
    """
    pass

def describe_trusted_advisor_checks(language=None):
    """
    Returns information about all available Trusted Advisor checks, including name, ID, category, description, and metadata. You must specify a language code; English ("en") and Japanese ("ja") are currently supported. The response contains a  TrustedAdvisorCheckDescription for each check. The region must be set to us-east-1.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_trusted_advisor_checks(
        language='string'
    )
    
    
    :type language: string
    :param language: [REQUIRED]\nThe ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --Information about the Trusted Advisor checks returned by the  DescribeTrustedAdvisorChecks operation.

checks (list) --Information about all available Trusted Advisor checks.

(dict) --The description and metadata for a Trusted Advisor check.

id (string) --The unique identifier for the Trusted Advisor check.

name (string) --The display name for the Trusted Advisor check.

description (string) --The description of the Trusted Advisor check, which includes the alert criteria and recommended operations (contains HTML markup).

category (string) --The category of the Trusted Advisor check.

metadata (list) --The column headings for the data returned by the Trusted Advisor check. The order of the headings corresponds to the order of the data in the Metadata element of the  TrustedAdvisorResourceDetail for the check. Metadata contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data.

(string) --











Exceptions

Support.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    Support.Client.exceptions.InternalServerError
    
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

def refresh_trusted_advisor_check(checkId=None):
    """
    Requests a refresh of the Trusted Advisor check that has the specified check ID. Check IDs can be obtained by calling  DescribeTrustedAdvisorChecks .
    The response contains a  TrustedAdvisorCheckRefreshStatus object, which contains these fields:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.refresh_trusted_advisor_check(
        checkId='string'
    )
    
    
    :type checkId: string
    :param checkId: [REQUIRED]\nThe unique identifier for the Trusted Advisor check to refresh. Note: Specifying the check ID of a check that is automatically refreshed causes an InvalidParameterValue error.\n

    :rtype: dict
ReturnsResponse Syntax{
    'status': {
        'checkId': 'string',
        'status': 'string',
        'millisUntilNextRefreshable': 123
    }
}


Response Structure

(dict) --The current refresh status of a Trusted Advisor check.

status (dict) --The current refresh status for a check, including the amount of time until the check is eligible for refresh.

checkId (string) --The unique identifier for the Trusted Advisor check.

status (string) --The status of the Trusted Advisor check for which a refresh has been requested:

none: The check is not refreshed or the non-success status exceeds the timeout
enqueued: The check refresh requests has entered the refresh queue
processing: The check refresh request is picked up by the rule processing engine
success: The check is successfully refreshed
abandoned: The check refresh has failed


millisUntilNextRefreshable (integer) --The amount of time, in milliseconds, until the Trusted Advisor check is eligible for refresh.








Exceptions

Support.Client.exceptions.InternalServerError


    :return: {
        'status': {
            'checkId': 'string',
            'status': 'string',
            'millisUntilNextRefreshable': 123
        }
    }
    
    
    :returns: 
    none: The check is not refreshed or the non-success status exceeds the timeout
    enqueued: The check refresh requests has entered the refresh queue
    processing: The check refresh request is picked up by the rule processing engine
    success: The check is successfully refreshed
    abandoned: The check refresh has failed
    
    """
    pass

def resolve_case(caseId=None):
    """
    Takes a caseId and returns the initial state of the case along with the state of the case after the call to  ResolveCase completed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resolve_case(
        caseId='string'
    )
    
    
    :type caseId: string
    :param caseId: The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47

    :rtype: dict
ReturnsResponse Syntax{
    'initialCaseStatus': 'string',
    'finalCaseStatus': 'string'
}


Response Structure

(dict) --The status of the case returned by the  ResolveCase operation.

initialCaseStatus (string) --The status of the case when the  ResolveCase request was sent.

finalCaseStatus (string) --The status of the case after the  ResolveCase request was processed.






Exceptions

Support.Client.exceptions.InternalServerError
Support.Client.exceptions.CaseIdNotFound


    :return: {
        'initialCaseStatus': 'string',
        'finalCaseStatus': 'string'
    }
    
    
    """
    pass

