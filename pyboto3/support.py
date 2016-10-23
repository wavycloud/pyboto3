"""
The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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
"""


def add_attachments_to_set(attachmentSetId=None, attachments=None):
    """
    :param attachmentSetId: The ID of the attachment set. If an attachmentSetId is not specified, a new attachment set is created, and the ID of the set is returned in the response. If an attachmentSetId is specified, the attachments are added to the specified set, if it exists.
    :type attachmentSetId: string
    :param attachments: [REQUIRED]
            One or more attachments to add to the set. The limit is 3 attachments per set, and the size limit is 5 MB per attachment.
            (dict) --An attachment to a case communication. The attachment consists of the file name and the content of the file.
            fileName (string) --The name of the attachment file.
            data (bytes) --The content of the attachment file.
            
            
    :type attachments: list
    """
    pass


def add_communication_to_case(caseId=None, communicationBody=None, ccEmailAddresses=None, attachmentSetId=None):
    """
    :param caseId: The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47
    :type caseId: string
    :param communicationBody: [REQUIRED]
            The body of an email communication to add to the support case.
            
    :type communicationBody: string
    :param ccEmailAddresses: The email addresses in the CC line of an email to be added to the support case.
            (string) --
            
    :type ccEmailAddresses: list
    :param attachmentSetId: The ID of a set of one or more attachments for the communication to add to the case. Create the set by calling AddAttachmentsToSet
    :type attachmentSetId: string
    """
    pass


def can_paginate(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
    :type operation_name: string
    """
    pass


def create_case(subject=None, serviceCode=None, severityCode=None, categoryCode=None, communicationBody=None,
                ccEmailAddresses=None, language=None, issueType=None, attachmentSetId=None):
    """
    :param subject: [REQUIRED]
            The title of the AWS Support case.
            
    :type subject: string
    :param serviceCode: The code for the AWS service returned by the call to DescribeServices .
    :type serviceCode: string
    :param severityCode: The code for the severity level returned by the call to DescribeSeverityLevels .
            Note
            The availability of severity levels depends on each customer's support subscription. In other words, your subscription may not necessarily require the urgent level of response time.
            
    :type severityCode: string
    :param categoryCode: The category of problem for the AWS Support case.
    :type categoryCode: string
    :param communicationBody: [REQUIRED]
            The communication body text when you create an AWS Support case by calling CreateCase .
            
    :type communicationBody: string
    :param ccEmailAddresses: A list of email addresses that AWS Support copies on case correspondence.
            (string) --
            
    :type ccEmailAddresses: list
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.
    :type language: string
    :param issueType: The type of issue for the case. You can specify either 'customer-service' or 'technical.' If you do not indicate a value, the default is 'technical.'
    :type issueType: string
    :param attachmentSetId: The ID of a set of one or more attachments for the case. Create the set by using AddAttachmentsToSet .
    :type attachmentSetId: string
    """
    pass


def describe_attachment(attachmentId=None):
    """
    :param attachmentId: [REQUIRED]
            The ID of the attachment to return. Attachment IDs are returned by the DescribeCommunications operation.
            Return typedict
            ReturnsResponse Syntax{
              'attachment': {
                'fileName': 'string',
                'data': b'bytes'
              }
            }
            Response Structure
            (dict) --The content and file name of the attachment returned by the DescribeAttachment operation.
            attachment (dict) --The attachment content and file name.
            fileName (string) --The name of the attachment file.
            data (bytes) --The content of the attachment file.
            
            
            
    :type attachmentId: string
    """
    pass


def describe_cases(caseIdList=None, displayId=None, afterTime=None, beforeTime=None, includeResolvedCases=None,
                   nextToken=None, maxResults=None, language=None, includeCommunications=None):
    """
    :param caseIdList: A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.
            (string) --
            
    :type caseIdList: list
    :param displayId: The ID displayed for a case in the AWS Support Center user interface.
    :type displayId: string
    :param afterTime: The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.
    :type afterTime: string
    :param beforeTime: The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.
    :type beforeTime: string
    :param includeResolvedCases: Specifies whether resolved support cases should be included in the DescribeCases results. The default is false .
    :type includeResolvedCases: boolean
    :param nextToken: A resumption point for pagination.
    :type nextToken: string
    :param maxResults: The maximum number of results to return before paginating.
    :type maxResults: integer
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.
    :type language: string
    :param includeCommunications: Specifies whether communications should be included in the DescribeCases results. The default is true .
    :type includeCommunications: boolean
    """
    pass


def describe_communications(caseId=None, beforeTime=None, afterTime=None, nextToken=None, maxResults=None):
    """
    :param caseId: [REQUIRED]
            The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47
            
    :type caseId: string
    :param beforeTime: The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.
    :type beforeTime: string
    :param afterTime: The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.
    :type afterTime: string
    :param nextToken: A resumption point for pagination.
    :type nextToken: string
    :param maxResults: The maximum number of results to return before paginating.
    :type maxResults: integer
    """
    pass


def describe_services(serviceCodeList=None, language=None):
    """
    :param serviceCodeList: A JSON-formatted list of service codes available for AWS services.
            (string) --
            
    :type serviceCodeList: list
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.
    :type language: string
    """
    pass


def describe_severity_levels(language=None):
    """
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.
            Return typedict
            ReturnsResponse Syntax{
              'severityLevels': [
                {
                  'code': 'string',
                  'name': 'string'
                },
              ]
            }
            Response Structure
            (dict) --The list of severity levels returned by the DescribeSeverityLevels operation.
            severityLevels (list) --The available severity levels for the support case. Available severity levels are defined by your service level agreement with AWS.
            (dict) --A code and name pair that represent a severity level that can be applied to a support case.
            code (string) --One of four values: 'low,' 'medium,' 'high,' and 'urgent'. These values correspond to response times returned to the caller in severityLevel.name .
            name (string) --The name of the severity level that corresponds to the severity level code.
            
            
            
    :type language: string
    """
    pass


def describe_trusted_advisor_check_refresh_statuses(checkIds=None):
    """
    :param checkIds: [REQUIRED]
            The IDs of the Trusted Advisor checks to get the status of. Note: Specifying the check ID of a check that is automatically refreshed causes an InvalidParameterValue error.
            (string) --
            Return typedict
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
            (dict) --The statuses of the Trusted Advisor checks returned by the DescribeTrustedAdvisorCheckRefreshStatuses operation.
            statuses (list) --The refresh status of the specified Trusted Advisor checks.
            (dict) --The refresh status of a Trusted Advisor check.
            checkId (string) --The unique identifier for the Trusted Advisor check.
            status (string) --The status of the Trusted Advisor check for which a refresh has been requested: 'none', 'enqueued', 'processing', 'success', or 'abandoned'.
            millisUntilNextRefreshable (integer) --The amount of time, in milliseconds, until the Trusted Advisor check is eligible for refresh.
            
            
            
    :type checkIds: list
    """
    pass


def describe_trusted_advisor_check_result(checkId=None, language=None):
    """
    :param checkId: [REQUIRED]
            The unique identifier for the Trusted Advisor check.
            
    :type checkId: string
    :param language: The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.
    :type language: string
    """
    pass


def describe_trusted_advisor_check_summaries(checkIds=None):
    """
    :param checkIds: [REQUIRED]
            The IDs of the Trusted Advisor checks.
            (string) --
            Return typedict
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
            (dict) --The summaries of the Trusted Advisor checks returned by the DescribeTrustedAdvisorCheckSummaries operation.
            summaries (list) --The summary information for the requested Trusted Advisor checks.
            (dict) --A summary of a Trusted Advisor check result, including the alert status, last refresh, and number of resources examined.
            checkId (string) --The unique identifier for the Trusted Advisor check.
            timestamp (string) --The time of the last refresh of the check.
            status (string) --The alert status of the check: 'ok' (green), 'warning' (yellow), 'error' (red), or 'not_available'.
            hasFlaggedResources (boolean) --Specifies whether the Trusted Advisor check has flagged resources.
            resourcesSummary (dict) --Details about AWS resources that were analyzed in a call to Trusted Advisor DescribeTrustedAdvisorCheckSummaries .
            resourcesProcessed (integer) --The number of AWS resources that were analyzed by the Trusted Advisor check.
            resourcesFlagged (integer) --The number of AWS resources that were flagged (listed) by the Trusted Advisor check.
            resourcesIgnored (integer) --The number of AWS resources ignored by Trusted Advisor because information was unavailable.
            resourcesSuppressed (integer) --The number of AWS resources ignored by Trusted Advisor because they were marked as suppressed by the user.
            categorySpecificSummary (dict) --Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.
            costOptimizing (dict) --The summary information about cost savings for a Trusted Advisor check that is in the Cost Optimizing category.
            estimatedMonthlySavings (float) --The estimated monthly savings that might be realized if the recommended actions are taken.
            estimatedPercentMonthlySavings (float) --The estimated percentage of savings that might be realized if the recommended actions are taken.
            
            
            
            
    :type checkIds: list
    """
    pass


def describe_trusted_advisor_checks(language=None):
    """
    :param language: [REQUIRED]
            The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English ('en') and Japanese ('ja'). Language parameters must be passed explicitly for operations that take them.
            Return typedict
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
            (dict) --Information about the Trusted Advisor checks returned by the DescribeTrustedAdvisorChecks operation.
            checks (list) --Information about all available Trusted Advisor checks.
            (dict) --The description and metadata for a Trusted Advisor check.
            id (string) --The unique identifier for the Trusted Advisor check.
            name (string) --The display name for the Trusted Advisor check.
            description (string) --The description of the Trusted Advisor check, which includes the alert criteria and recommended actions (contains HTML markup).
            category (string) --The category of the Trusted Advisor check.
            metadata (list) --The column headings for the data returned by the Trusted Advisor check. The order of the headings corresponds to the order of the data in the Metadata element of the TrustedAdvisorResourceDetail for the check. Metadata contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data.
            (string) --
            
            
            
    :type language: string
    """
    pass


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    :param ClientMethod: The client method to presign for
    :type ClientMethod: string
    :param Params: The parameters normally passed to
            ClientMethod.
    :type Params: dict
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
    :type ExpiresIn: int
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
    :type HttpMethod: string
    """
    pass


def get_paginator(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
    :type operation_name: string
    """
    pass


def get_waiter():
    """
    """
    pass


def refresh_trusted_advisor_check(checkId=None):
    """
    :param checkId: [REQUIRED]
            The unique identifier for the Trusted Advisor check to refresh. Note: Specifying the check ID of a check that is automatically refreshed causes an InvalidParameterValue error.
            Return typedict
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
            status (string) --The status of the Trusted Advisor check for which a refresh has been requested: 'none', 'enqueued', 'processing', 'success', or 'abandoned'.
            millisUntilNextRefreshable (integer) --The amount of time, in milliseconds, until the Trusted Advisor check is eligible for refresh.
            
            
            
    :type checkId: string
    """
    pass


def resolve_case(caseId=None):
    """
    :param caseId: The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-12345678910-2013-c4c1d2bf33c5cf47
            Return typedict
            ReturnsResponse Syntax{
              'initialCaseStatus': 'string',
              'finalCaseStatus': 'string'
            }
            Response Structure
            (dict) --The status of the case returned by the ResolveCase operation.
            initialCaseStatus (string) --The status of the case when the ResolveCase request was sent.
            finalCaseStatus (string) --The status of the case after the ResolveCase request was processed.
            
            
    :type caseId: string
    """
    pass
