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

def accept_qualification_request(QualificationRequestId=None, IntegerValue=None):
    """
    The AcceptQualificationRequest operation approves a Worker\'s request for a Qualification.
    Only the owner of the Qualification type can grant a Qualification request for that type.
    A successful request for the AcceptQualificationRequest operation returns with no errors and an empty body.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_qualification_request(
        QualificationRequestId='string',
        IntegerValue=123
    )
    
    
    :type QualificationRequestId: string
    :param QualificationRequestId: [REQUIRED]\nThe ID of the Qualification request, as returned by the GetQualificationRequests operation.\n

    :type IntegerValue: integer
    :param IntegerValue: The value of the Qualification. You can omit this value if you are using the presence or absence of the Qualification as the basis for a HIT requirement.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def approve_assignment(AssignmentId=None, RequesterFeedback=None, OverrideRejection=None):
    """
    The ApproveAssignment operation approves the results of a completed assignment.
    Approving an assignment initiates two payments from the Requester\'s Amazon.com account
    If the Requester\'s account does not have adequate funds for these payments, the call to ApproveAssignment returns an exception, and the approval is not processed. You can include an optional feedback message with the approval, which the Worker can see in the Status section of the web site.
    You can also call this operation for assignments that were previous rejected and approve them by explicitly overriding the previous rejection. This only works on rejected assignments that were submitted within the previous 30 days and only if the assignment\'s related HIT has not been deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.approve_assignment(
        AssignmentId='string',
        RequesterFeedback='string',
        OverrideRejection=True|False
    )
    
    
    :type AssignmentId: string
    :param AssignmentId: [REQUIRED]\nThe ID of the assignment. The assignment must correspond to a HIT created by the Requester.\n

    :type RequesterFeedback: string
    :param RequesterFeedback: A message for the Worker, which the Worker can see in the Status section of the web site.

    :type OverrideRejection: boolean
    :param OverrideRejection: A flag indicating that an assignment should be approved even if it was previously rejected. Defaults to False .

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    AssignmentId (string) -- [REQUIRED]
    The ID of the assignment. The assignment must correspond to a HIT created by the Requester.
    
    RequesterFeedback (string) -- A message for the Worker, which the Worker can see in the Status section of the web site.
    OverrideRejection (boolean) -- A flag indicating that an assignment should be approved even if it was previously rejected. Defaults to False .
    
    """
    pass

def associate_qualification_with_worker(QualificationTypeId=None, WorkerId=None, IntegerValue=None, SendNotification=None):
    """
    The AssociateQualificationWithWorker operation gives a Worker a Qualification. AssociateQualificationWithWorker does not require that the Worker submit a Qualification request. It gives the Qualification directly to the Worker.
    You can only assign a Qualification of a Qualification type that you created (using the CreateQualificationType operation).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_qualification_with_worker(
        QualificationTypeId='string',
        WorkerId='string',
        IntegerValue=123,
        SendNotification=True|False
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]\nThe ID of the Qualification type to use for the assigned Qualification.\n

    :type WorkerId: string
    :param WorkerId: [REQUIRED]\nThe ID of the Worker to whom the Qualification is being assigned. Worker IDs are included with submitted HIT assignments and Qualification requests.\n

    :type IntegerValue: integer
    :param IntegerValue: The value of the Qualification to assign.

    :type SendNotification: boolean
    :param SendNotification: Specifies whether to send a notification email message to the Worker saying that the qualification was assigned to the Worker. Note: this is true by default.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_additional_assignments_for_hit(HITId=None, NumberOfAdditionalAssignments=None, UniqueRequestToken=None):
    """
    The CreateAdditionalAssignmentsForHIT operation increases the maximum number of assignments of an existing HIT.
    To extend the maximum number of assignments, specify the number of additional assignments.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_additional_assignments_for_hit(
        HITId='string',
        NumberOfAdditionalAssignments=123,
        UniqueRequestToken='string'
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]\nThe ID of the HIT to extend.\n

    :type NumberOfAdditionalAssignments: integer
    :param NumberOfAdditionalAssignments: [REQUIRED]\nThe number of additional assignments to request for this HIT.\n

    :type UniqueRequestToken: string
    :param UniqueRequestToken: A unique identifier for this request, which allows you to retry the call on error without extending the HIT multiple times. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the extend HIT already exists in the system from a previous call using the same UniqueRequestToken , subsequent calls will return an error with a message containing the request ID.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    HITId (string) -- [REQUIRED]
    The ID of the HIT to extend.
    
    NumberOfAdditionalAssignments (integer) -- [REQUIRED]
    The number of additional assignments to request for this HIT.
    
    UniqueRequestToken (string) -- A unique identifier for this request, which allows you to retry the call on error without extending the HIT multiple times. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the extend HIT already exists in the system from a previous call using the same UniqueRequestToken , subsequent calls will return an error with a message containing the request ID.
    
    """
    pass

def create_hit(MaxAssignments=None, AutoApprovalDelayInSeconds=None, LifetimeInSeconds=None, AssignmentDurationInSeconds=None, Reward=None, Title=None, Keywords=None, Description=None, Question=None, RequesterAnnotation=None, QualificationRequirements=None, UniqueRequestToken=None, AssignmentReviewPolicy=None, HITReviewPolicy=None, HITLayoutId=None, HITLayoutParameters=None):
    """
    The CreateHIT operation creates a new Human Intelligence Task (HIT). The new HIT is made available for Workers to find and accept on the Amazon Mechanical Turk website.
    This operation allows you to specify a new HIT by passing in values for the properties of the HIT, such as its title, reward amount and number of assignments. When you pass these values to CreateHIT , a new HIT is created for you, with a new HITTypeID . The HITTypeID can be used to create additional HITs in the future without needing to specify common parameters such as the title, description and reward amount each time.
    An alternative way to create HITs is to first generate a HITTypeID using the CreateHITType operation and then call the CreateHITWithHITType operation. This is the recommended best practice for Requesters who are creating large numbers of HITs.
    CreateHIT also supports several ways to provide question data: by providing a value for the Question parameter that fully specifies the contents of the HIT, or by providing a HitLayoutId and associated HitLayoutParameters .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_hit(
        MaxAssignments=123,
        AutoApprovalDelayInSeconds=123,
        LifetimeInSeconds=123,
        AssignmentDurationInSeconds=123,
        Reward='string',
        Title='string',
        Keywords='string',
        Description='string',
        Question='string',
        RequesterAnnotation='string',
        QualificationRequirements=[
            {
                'QualificationTypeId': 'string',
                'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                'IntegerValues': [
                    123,
                ],
                'LocaleValues': [
                    {
                        'Country': 'string',
                        'Subdivision': 'string'
                    },
                ],
                'RequiredToPreview': True|False,
                'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
            },
        ],
        UniqueRequestToken='string',
        AssignmentReviewPolicy={
            'PolicyName': 'string',
            'Parameters': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ],
                    'MapEntries': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
            ]
        },
        HITReviewPolicy={
            'PolicyName': 'string',
            'Parameters': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ],
                    'MapEntries': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
            ]
        },
        HITLayoutId='string',
        HITLayoutParameters=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type MaxAssignments: integer
    :param MaxAssignments: The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

    :type AutoApprovalDelayInSeconds: integer
    :param AutoApprovalDelayInSeconds: The number of seconds after an assignment for the HIT has been submitted, after which the assignment is considered Approved automatically unless the Requester explicitly rejects it.

    :type LifetimeInSeconds: integer
    :param LifetimeInSeconds: [REQUIRED]\nAn amount of time, in seconds, after which the HIT is no longer available for users to accept. After the lifetime of the HIT elapses, the HIT no longer appears in HIT searches, even if not all of the assignments for the HIT have been accepted.\n

    :type AssignmentDurationInSeconds: integer
    :param AssignmentDurationInSeconds: [REQUIRED]\nThe amount of time, in seconds, that a Worker has to complete the HIT after accepting it. If a Worker does not complete the assignment within the specified duration, the assignment is considered abandoned. If the HIT is still active (that is, its lifetime has not elapsed), the assignment becomes available for other users to find and accept.\n

    :type Reward: string
    :param Reward: [REQUIRED]\nThe amount of money the Requester will pay a Worker for successfully completing the HIT.\n

    :type Title: string
    :param Title: [REQUIRED]\nThe title of the HIT. A title should be short and descriptive about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT title appears in search results, and everywhere the HIT is mentioned.\n

    :type Keywords: string
    :param Keywords: One or more words or phrases that describe the HIT, separated by commas. These words are used in searches to find HITs.

    :type Description: string
    :param Description: [REQUIRED]\nA general description of the HIT. A description includes detailed information about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT description appears in the expanded view of search results, and in the HIT and assignment screens. A good description gives the user enough information to evaluate the HIT before accepting it.\n

    :type Question: string
    :param Question: The data the person completing the HIT uses to produce the results.\nConstraints: Must be a QuestionForm data structure, an ExternalQuestion data structure, or an HTMLQuestion data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace.\nEither a Question parameter or a HITLayoutId parameter must be provided.\n

    :type RequesterAnnotation: string
    :param RequesterAnnotation: An arbitrary data field. The RequesterAnnotation parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, this parameter could be an identifier internal to the Requester\'s application that corresponds with the HIT.\nThe RequesterAnnotation parameter for a HIT is only visible to the Requester who created the HIT. It is not shown to the Worker, or any other Requester.\nThe RequesterAnnotation parameter may be different for each HIT you submit. It does not affect how your HITs are grouped.\n

    :type QualificationRequirements: list
    :param QualificationRequirements: Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ActionsGuarded field on each QualificationRequirement structure.\n\n(dict) --The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results.\n\nQualificationTypeId (string) -- [REQUIRED]The ID of the Qualification type for the requirement.\n\nComparator (string) -- [REQUIRED]The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value.\n\nIntegerValues (list) --The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.\n\n(integer) --\n\n\nLocaleValues (list) --The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.\n\n(dict) --The Locale data structure represents a geographical region or location.\n\nCountry (string) -- [REQUIRED]The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.\n\nSubdivision (string) --The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.\n\n\n\n\n\nRequiredToPreview (boolean) --DEPRECATED: Use the ActionsGuarded field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ActionsGuarded field.\n\nActionsGuarded (string) --Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include 'Accept' (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), 'PreviewAndAccept' (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and 'DiscoverPreviewAndAccept' (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the RequiredToPreview field.\n\n\n\n\n

    :type UniqueRequestToken: string
    :param UniqueRequestToken: A unique identifier for this request which allows you to retry the call on error without creating duplicate HITs. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the HIT already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return a AWS.MechanicalTurk.HitAlreadyExists error with a message containing the HITId.\n\nNote\nNote: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same UniqueRequestToken made after the 24 hour limit could create duplicate HITs.\n\n

    :type AssignmentReviewPolicy: dict
    :param AssignmentReviewPolicy: The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for Mechanical Turk to take various actions based on the policy.\n\nPolicyName (string) -- [REQUIRED]Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01\n\nParameters (list) --Name of the parameter from the Review policy.\n\n(dict) --Name of the parameter from the Review policy.\n\nKey (string) --Name of the parameter from the list of Review Polices.\n\nValues (list) --The list of values of the Parameter\n\n(string) --\n\n\nMapEntries (list) --List of ParameterMapEntry objects.\n\n(dict) --This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.\n\nKey (string) --The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.\n\nValues (list) --The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.\n\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n

    :type HITReviewPolicy: dict
    :param HITReviewPolicy: The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take various actions based on the policy.\n\nPolicyName (string) -- [REQUIRED]Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01\n\nParameters (list) --Name of the parameter from the Review policy.\n\n(dict) --Name of the parameter from the Review policy.\n\nKey (string) --Name of the parameter from the list of Review Polices.\n\nValues (list) --The list of values of the Parameter\n\n(string) --\n\n\nMapEntries (list) --List of ParameterMapEntry objects.\n\n(dict) --This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.\n\nKey (string) --The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.\n\nValues (list) --The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.\n\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n

    :type HITLayoutId: string
    :param HITLayoutId: The HITLayoutId allows you to use a pre-existing HIT design with placeholder values and create an additional HIT by providing those values as HITLayoutParameters.\nConstraints: Either a Question parameter or a HITLayoutId parameter must be provided.\n

    :type HITLayoutParameters: list
    :param HITLayoutParameters: If the HITLayoutId is provided, any placeholder values must be filled in with values using the HITLayoutParameter structure. For more information, see HITLayout.\n\n(dict) --The HITLayoutParameter data structure defines parameter values used with a HITLayout. A HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human Intelligence Task (HIT) question data for CreateHIT.\n\nName (string) -- [REQUIRED]The name of the parameter in the HITLayout.\n\nValue (string) -- [REQUIRED]The value substituted for the parameter referenced in the HITLayout.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HIT': {
        'HITId': 'string',
        'HITTypeId': 'string',
        'HITGroupId': 'string',
        'HITLayoutId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'Title': 'string',
        'Description': 'string',
        'Question': 'string',
        'Keywords': 'string',
        'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
        'MaxAssignments': 123,
        'Reward': 'string',
        'AutoApprovalDelayInSeconds': 123,
        'Expiration': datetime(2015, 1, 1),
        'AssignmentDurationInSeconds': 123,
        'RequesterAnnotation': 'string',
        'QualificationRequirements': [
            {
                'QualificationTypeId': 'string',
                'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                'IntegerValues': [
                    123,
                ],
                'LocaleValues': [
                    {
                        'Country': 'string',
                        'Subdivision': 'string'
                    },
                ],
                'RequiredToPreview': True|False,
                'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
            },
        ],
        'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
        'NumberOfAssignmentsPending': 123,
        'NumberOfAssignmentsAvailable': 123,
        'NumberOfAssignmentsCompleted': 123
    }
}


Response Structure

(dict) --

HIT (dict) --
Contains the newly created HIT data. For a description of the HIT data structure as it appears in responses, see the HIT Data Structure documentation.

HITId (string) --
A unique identifier for the HIT.

HITTypeId (string) --
The ID of the HIT type of this HIT

HITGroupId (string) --
The ID of the HIT Group of this HIT.

HITLayoutId (string) --
The ID of the HIT Layout of this HIT.

CreationTime (datetime) --
The date and time the HIT was created.

Title (string) --
The title of the HIT.

Description (string) --
A general description of the HIT.

Question (string) --
The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

Keywords (string) --
One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.

HITStatus (string) --
The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed.

MaxAssignments (integer) --
The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

Reward (string) --
A string representing a currency amount.

AutoApprovalDelayInSeconds (integer) --
The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid.

Expiration (datetime) --
The date and time the HIT expires.

AssignmentDurationInSeconds (integer) --
The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

RequesterAnnotation (string) --
An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.

QualificationRequirements (list) --
Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ActionsGuarded field on each QualificationRequirement structure.

(dict) --
The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results.

QualificationTypeId (string) --
The ID of the Qualification type for the requirement.

Comparator (string) --
The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value.

IntegerValues (list) --
The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.

(integer) --


LocaleValues (list) --
The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.

(dict) --
The Locale data structure represents a geographical region or location.

Country (string) --
The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision (string) --
The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.





RequiredToPreview (boolean) --
DEPRECATED: Use the ActionsGuarded field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ActionsGuarded field.

ActionsGuarded (string) --
Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the RequiredToPreview field.





HITReviewStatus (string) --
Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.

NumberOfAssignmentsPending (integer) --
The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.

NumberOfAssignmentsAvailable (integer) --
The number of assignments for this HIT that are available for Workers to accept.

NumberOfAssignmentsCompleted (integer) --
The number of assignments for this HIT that have been approved or rejected.









Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'HIT': {
            'HITId': 'string',
            'HITTypeId': 'string',
            'HITGroupId': 'string',
            'HITLayoutId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Title': 'string',
            'Description': 'string',
            'Question': 'string',
            'Keywords': 'string',
            'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
            'MaxAssignments': 123,
            'Reward': 'string',
            'AutoApprovalDelayInSeconds': 123,
            'Expiration': datetime(2015, 1, 1),
            'AssignmentDurationInSeconds': 123,
            'RequesterAnnotation': 'string',
            'QualificationRequirements': [
                {
                    'QualificationTypeId': 'string',
                    'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                    'IntegerValues': [
                        123,
                    ],
                    'LocaleValues': [
                        {
                            'Country': 'string',
                            'Subdivision': 'string'
                        },
                    ],
                    'RequiredToPreview': True|False,
                    'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
                },
            ],
            'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
            'NumberOfAssignmentsPending': 123,
            'NumberOfAssignmentsAvailable': 123,
            'NumberOfAssignmentsCompleted': 123
        }
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def create_hit_type(AutoApprovalDelayInSeconds=None, AssignmentDurationInSeconds=None, Reward=None, Title=None, Keywords=None, Description=None, QualificationRequirements=None):
    """
    The CreateHITType operation creates a new HIT type. This operation allows you to define a standard set of HIT properties to use when creating HITs. If you register a HIT type with values that match an existing HIT type, the HIT type ID of the existing type will be returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_hit_type(
        AutoApprovalDelayInSeconds=123,
        AssignmentDurationInSeconds=123,
        Reward='string',
        Title='string',
        Keywords='string',
        Description='string',
        QualificationRequirements=[
            {
                'QualificationTypeId': 'string',
                'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                'IntegerValues': [
                    123,
                ],
                'LocaleValues': [
                    {
                        'Country': 'string',
                        'Subdivision': 'string'
                    },
                ],
                'RequiredToPreview': True|False,
                'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
            },
        ]
    )
    
    
    :type AutoApprovalDelayInSeconds: integer
    :param AutoApprovalDelayInSeconds: The number of seconds after an assignment for the HIT has been submitted, after which the assignment is considered Approved automatically unless the Requester explicitly rejects it.

    :type AssignmentDurationInSeconds: integer
    :param AssignmentDurationInSeconds: [REQUIRED]\nThe amount of time, in seconds, that a Worker has to complete the HIT after accepting it. If a Worker does not complete the assignment within the specified duration, the assignment is considered abandoned. If the HIT is still active (that is, its lifetime has not elapsed), the assignment becomes available for other users to find and accept.\n

    :type Reward: string
    :param Reward: [REQUIRED]\nThe amount of money the Requester will pay a Worker for successfully completing the HIT.\n

    :type Title: string
    :param Title: [REQUIRED]\nThe title of the HIT. A title should be short and descriptive about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT title appears in search results, and everywhere the HIT is mentioned.\n

    :type Keywords: string
    :param Keywords: One or more words or phrases that describe the HIT, separated by commas. These words are used in searches to find HITs.

    :type Description: string
    :param Description: [REQUIRED]\nA general description of the HIT. A description includes detailed information about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT description appears in the expanded view of search results, and in the HIT and assignment screens. A good description gives the user enough information to evaluate the HIT before accepting it.\n

    :type QualificationRequirements: list
    :param QualificationRequirements: Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ActionsGuarded field on each QualificationRequirement structure.\n\n(dict) --The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results.\n\nQualificationTypeId (string) -- [REQUIRED]The ID of the Qualification type for the requirement.\n\nComparator (string) -- [REQUIRED]The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value.\n\nIntegerValues (list) --The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.\n\n(integer) --\n\n\nLocaleValues (list) --The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.\n\n(dict) --The Locale data structure represents a geographical region or location.\n\nCountry (string) -- [REQUIRED]The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.\n\nSubdivision (string) --The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.\n\n\n\n\n\nRequiredToPreview (boolean) --DEPRECATED: Use the ActionsGuarded field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ActionsGuarded field.\n\nActionsGuarded (string) --Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include 'Accept' (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), 'PreviewAndAccept' (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and 'DiscoverPreviewAndAccept' (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the RequiredToPreview field.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HITTypeId': 'string'
}


Response Structure

(dict) --

HITTypeId (string) --
The ID of the newly registered HIT type.







Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'HITTypeId': 'string'
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def create_hit_with_hit_type(HITTypeId=None, MaxAssignments=None, LifetimeInSeconds=None, Question=None, RequesterAnnotation=None, UniqueRequestToken=None, AssignmentReviewPolicy=None, HITReviewPolicy=None, HITLayoutId=None, HITLayoutParameters=None):
    """
    The CreateHITWithHITType operation creates a new Human Intelligence Task (HIT) using an existing HITTypeID generated by the CreateHITType operation.
    This is an alternative way to create HITs from the CreateHIT operation. This is the recommended best practice for Requesters who are creating large numbers of HITs.
    CreateHITWithHITType also supports several ways to provide question data: by providing a value for the Question parameter that fully specifies the contents of the HIT, or by providing a HitLayoutId and associated HitLayoutParameters .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_hit_with_hit_type(
        HITTypeId='string',
        MaxAssignments=123,
        LifetimeInSeconds=123,
        Question='string',
        RequesterAnnotation='string',
        UniqueRequestToken='string',
        AssignmentReviewPolicy={
            'PolicyName': 'string',
            'Parameters': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ],
                    'MapEntries': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
            ]
        },
        HITReviewPolicy={
            'PolicyName': 'string',
            'Parameters': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ],
                    'MapEntries': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
            ]
        },
        HITLayoutId='string',
        HITLayoutParameters=[
            {
                'Name': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type HITTypeId: string
    :param HITTypeId: [REQUIRED]\nThe HIT type ID you want to create this HIT with.\n

    :type MaxAssignments: integer
    :param MaxAssignments: The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

    :type LifetimeInSeconds: integer
    :param LifetimeInSeconds: [REQUIRED]\nAn amount of time, in seconds, after which the HIT is no longer available for users to accept. After the lifetime of the HIT elapses, the HIT no longer appears in HIT searches, even if not all of the assignments for the HIT have been accepted.\n

    :type Question: string
    :param Question: The data the person completing the HIT uses to produce the results.\nConstraints: Must be a QuestionForm data structure, an ExternalQuestion data structure, or an HTMLQuestion data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace.\nEither a Question parameter or a HITLayoutId parameter must be provided.\n

    :type RequesterAnnotation: string
    :param RequesterAnnotation: An arbitrary data field. The RequesterAnnotation parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, this parameter could be an identifier internal to the Requester\'s application that corresponds with the HIT.\nThe RequesterAnnotation parameter for a HIT is only visible to the Requester who created the HIT. It is not shown to the Worker, or any other Requester.\nThe RequesterAnnotation parameter may be different for each HIT you submit. It does not affect how your HITs are grouped.\n

    :type UniqueRequestToken: string
    :param UniqueRequestToken: A unique identifier for this request which allows you to retry the call on error without creating duplicate HITs. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the HIT already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return a AWS.MechanicalTurk.HitAlreadyExists error with a message containing the HITId.\n\nNote\nNote: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same UniqueRequestToken made after the 24 hour limit could create duplicate HITs.\n\n

    :type AssignmentReviewPolicy: dict
    :param AssignmentReviewPolicy: The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for Mechanical Turk to take various actions based on the policy.\n\nPolicyName (string) -- [REQUIRED]Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01\n\nParameters (list) --Name of the parameter from the Review policy.\n\n(dict) --Name of the parameter from the Review policy.\n\nKey (string) --Name of the parameter from the list of Review Polices.\n\nValues (list) --The list of values of the Parameter\n\n(string) --\n\n\nMapEntries (list) --List of ParameterMapEntry objects.\n\n(dict) --This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.\n\nKey (string) --The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.\n\nValues (list) --The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.\n\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n

    :type HITReviewPolicy: dict
    :param HITReviewPolicy: The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take various actions based on the policy.\n\nPolicyName (string) -- [REQUIRED]Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01\n\nParameters (list) --Name of the parameter from the Review policy.\n\n(dict) --Name of the parameter from the Review policy.\n\nKey (string) --Name of the parameter from the list of Review Polices.\n\nValues (list) --The list of values of the Parameter\n\n(string) --\n\n\nMapEntries (list) --List of ParameterMapEntry objects.\n\n(dict) --This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.\n\nKey (string) --The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.\n\nValues (list) --The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.\n\n(string) --\n\n\n\n\n\n\n\n\n\n\n\n

    :type HITLayoutId: string
    :param HITLayoutId: The HITLayoutId allows you to use a pre-existing HIT design with placeholder values and create an additional HIT by providing those values as HITLayoutParameters.\nConstraints: Either a Question parameter or a HITLayoutId parameter must be provided.\n

    :type HITLayoutParameters: list
    :param HITLayoutParameters: If the HITLayoutId is provided, any placeholder values must be filled in with values using the HITLayoutParameter structure. For more information, see HITLayout.\n\n(dict) --The HITLayoutParameter data structure defines parameter values used with a HITLayout. A HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human Intelligence Task (HIT) question data for CreateHIT.\n\nName (string) -- [REQUIRED]The name of the parameter in the HITLayout.\n\nValue (string) -- [REQUIRED]The value substituted for the parameter referenced in the HITLayout.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'HIT': {
        'HITId': 'string',
        'HITTypeId': 'string',
        'HITGroupId': 'string',
        'HITLayoutId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'Title': 'string',
        'Description': 'string',
        'Question': 'string',
        'Keywords': 'string',
        'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
        'MaxAssignments': 123,
        'Reward': 'string',
        'AutoApprovalDelayInSeconds': 123,
        'Expiration': datetime(2015, 1, 1),
        'AssignmentDurationInSeconds': 123,
        'RequesterAnnotation': 'string',
        'QualificationRequirements': [
            {
                'QualificationTypeId': 'string',
                'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                'IntegerValues': [
                    123,
                ],
                'LocaleValues': [
                    {
                        'Country': 'string',
                        'Subdivision': 'string'
                    },
                ],
                'RequiredToPreview': True|False,
                'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
            },
        ],
        'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
        'NumberOfAssignmentsPending': 123,
        'NumberOfAssignmentsAvailable': 123,
        'NumberOfAssignmentsCompleted': 123
    }
}


Response Structure

(dict) --

HIT (dict) --
Contains the newly created HIT data. For a description of the HIT data structure as it appears in responses, see the HIT Data Structure documentation.

HITId (string) --
A unique identifier for the HIT.

HITTypeId (string) --
The ID of the HIT type of this HIT

HITGroupId (string) --
The ID of the HIT Group of this HIT.

HITLayoutId (string) --
The ID of the HIT Layout of this HIT.

CreationTime (datetime) --
The date and time the HIT was created.

Title (string) --
The title of the HIT.

Description (string) --
A general description of the HIT.

Question (string) --
The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

Keywords (string) --
One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.

HITStatus (string) --
The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed.

MaxAssignments (integer) --
The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

Reward (string) --
A string representing a currency amount.

AutoApprovalDelayInSeconds (integer) --
The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid.

Expiration (datetime) --
The date and time the HIT expires.

AssignmentDurationInSeconds (integer) --
The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

RequesterAnnotation (string) --
An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.

QualificationRequirements (list) --
Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ActionsGuarded field on each QualificationRequirement structure.

(dict) --
The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results.

QualificationTypeId (string) --
The ID of the Qualification type for the requirement.

Comparator (string) --
The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value.

IntegerValues (list) --
The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.

(integer) --


LocaleValues (list) --
The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.

(dict) --
The Locale data structure represents a geographical region or location.

Country (string) --
The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision (string) --
The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.





RequiredToPreview (boolean) --
DEPRECATED: Use the ActionsGuarded field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ActionsGuarded field.

ActionsGuarded (string) --
Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the RequiredToPreview field.





HITReviewStatus (string) --
Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.

NumberOfAssignmentsPending (integer) --
The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.

NumberOfAssignmentsAvailable (integer) --
The number of assignments for this HIT that are available for Workers to accept.

NumberOfAssignmentsCompleted (integer) --
The number of assignments for this HIT that have been approved or rejected.









Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'HIT': {
            'HITId': 'string',
            'HITTypeId': 'string',
            'HITGroupId': 'string',
            'HITLayoutId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Title': 'string',
            'Description': 'string',
            'Question': 'string',
            'Keywords': 'string',
            'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
            'MaxAssignments': 123,
            'Reward': 'string',
            'AutoApprovalDelayInSeconds': 123,
            'Expiration': datetime(2015, 1, 1),
            'AssignmentDurationInSeconds': 123,
            'RequesterAnnotation': 'string',
            'QualificationRequirements': [
                {
                    'QualificationTypeId': 'string',
                    'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                    'IntegerValues': [
                        123,
                    ],
                    'LocaleValues': [
                        {
                            'Country': 'string',
                            'Subdivision': 'string'
                        },
                    ],
                    'RequiredToPreview': True|False,
                    'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
                },
            ],
            'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
            'NumberOfAssignmentsPending': 123,
            'NumberOfAssignmentsAvailable': 123,
            'NumberOfAssignmentsCompleted': 123
        }
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def create_qualification_type(Name=None, Keywords=None, Description=None, QualificationTypeStatus=None, RetryDelayInSeconds=None, Test=None, AnswerKey=None, TestDurationInSeconds=None, AutoGranted=None, AutoGrantedValue=None):
    """
    The CreateQualificationType operation creates a new Qualification type, which is represented by a QualificationType data structure.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_qualification_type(
        Name='string',
        Keywords='string',
        Description='string',
        QualificationTypeStatus='Active'|'Inactive',
        RetryDelayInSeconds=123,
        Test='string',
        AnswerKey='string',
        TestDurationInSeconds=123,
        AutoGranted=True|False,
        AutoGrantedValue=123
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name you give to the Qualification type. The type name is used to represent the Qualification to Workers, and to find the type using a Qualification type search. It must be unique across all of your Qualification types.\n

    :type Keywords: string
    :param Keywords: One or more words or phrases that describe the Qualification type, separated by commas. The keywords of a type make the type easier to find during a search.

    :type Description: string
    :param Description: [REQUIRED]\nA long description for the Qualification type. On the Amazon Mechanical Turk website, the long description is displayed when a Worker examines a Qualification type.\n

    :type QualificationTypeStatus: string
    :param QualificationTypeStatus: [REQUIRED]\nThe initial status of the Qualification type.\nConstraints: Valid values are: Active | Inactive\n

    :type RetryDelayInSeconds: integer
    :param RetryDelayInSeconds: The number of seconds that a Worker must wait after requesting a Qualification of the Qualification type before the worker can retry the Qualification request.\nConstraints: None. If not specified, retries are disabled and Workers can request a Qualification of this type only once, even if the Worker has not been granted the Qualification. It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must delete existing retry-enabled Qualification type and then create a new Qualification type with retries disabled.\n

    :type Test: string
    :param Test: The questions for the Qualification test a Worker must answer correctly to obtain a Qualification of this type. If this parameter is specified, TestDurationInSeconds must also be specified.\nConstraints: Must not be longer than 65535 bytes. Must be a QuestionForm data structure. This parameter cannot be specified if AutoGranted is true.\nConstraints: None. If not specified, the Worker may request the Qualification without answering any questions.\n

    :type AnswerKey: string
    :param AnswerKey: The answers to the Qualification test specified in the Test parameter, in the form of an AnswerKey data structure.\nConstraints: Must not be longer than 65535 bytes.\nConstraints: None. If not specified, you must process Qualification requests manually.\n

    :type TestDurationInSeconds: integer
    :param TestDurationInSeconds: The number of seconds the Worker has to complete the Qualification test, starting from the time the Worker requests the Qualification.

    :type AutoGranted: boolean
    :param AutoGranted: Specifies whether requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test.\nConstraints: If the Test parameter is specified, this parameter cannot be true.\n

    :type AutoGrantedValue: integer
    :param AutoGrantedValue: The Qualification value to use for automatically granted Qualifications. This parameter is used only if the AutoGranted parameter is true.

    :rtype: dict

ReturnsResponse Syntax
{
    'QualificationType': {
        'QualificationTypeId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'Name': 'string',
        'Description': 'string',
        'Keywords': 'string',
        'QualificationTypeStatus': 'Active'|'Inactive',
        'Test': 'string',
        'TestDurationInSeconds': 123,
        'AnswerKey': 'string',
        'RetryDelayInSeconds': 123,
        'IsRequestable': True|False,
        'AutoGranted': True|False,
        'AutoGrantedValue': 123
    }
}


Response Structure

(dict) --

QualificationType (dict) --
The created Qualification type, returned as a QualificationType data structure.

QualificationTypeId (string) --
A unique identifier for the Qualification type. A Qualification type is given a Qualification type ID when you call the CreateQualificationType operation.

CreationTime (datetime) --
The date and time the Qualification type was created.

Name (string) --
The name of the Qualification type. The type name is used to identify the type, and to find the type using a Qualification type search.

Description (string) --
A long description for the Qualification type.

Keywords (string) --
One or more words or phrases that describe theQualification type, separated by commas. The Keywords make the type easier to find using a search.

QualificationTypeStatus (string) --
The status of the Qualification type. A Qualification type\'s status determines if users can apply to receive a Qualification of this type, and if HITs can be created with requirements based on this type. Valid values are Active | Inactive.

Test (string) --
The questions for a Qualification test associated with this Qualification type that a user can take to obtain a Qualification of this type. This parameter must be specified if AnswerKey is present. A Qualification type cannot have both a specified Test parameter and an AutoGranted value of true.

TestDurationInSeconds (integer) --
The amount of time, in seconds, given to a Worker to complete the Qualification test, beginning from the time the Worker requests the Qualification.

AnswerKey (string) --
The answers to the Qualification test specified in the Test parameter.

RetryDelayInSeconds (integer) --
The amount of time, in seconds, Workers must wait after taking the Qualification test before they can take it again. Workers can take a Qualification test multiple times if they were not granted the Qualification from a previous attempt, or if the test offers a gradient score and they want a better score. If not specified, retries are disabled and Workers can request a Qualification only once.

IsRequestable (boolean) --
Specifies whether the Qualification type is one that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is False for Qualifications assigned automatically by the system. Valid values are True | False.

AutoGranted (boolean) --
Specifies that requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test. Valid values are True | False.

AutoGrantedValue (integer) --
The Qualification integer value to use for automatically granted Qualifications, if AutoGranted is true. This is 1 by default.









Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'QualificationType': {
            'QualificationTypeId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Name': 'string',
            'Description': 'string',
            'Keywords': 'string',
            'QualificationTypeStatus': 'Active'|'Inactive',
            'Test': 'string',
            'TestDurationInSeconds': 123,
            'AnswerKey': 'string',
            'RetryDelayInSeconds': 123,
            'IsRequestable': True|False,
            'AutoGranted': True|False,
            'AutoGrantedValue': 123
        }
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def create_worker_block(WorkerId=None, Reason=None):
    """
    The CreateWorkerBlock operation allows you to prevent a Worker from working on your HITs. For example, you can block a Worker who is producing poor quality work. You can block up to 100,000 Workers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_worker_block(
        WorkerId='string',
        Reason='string'
    )
    
    
    :type WorkerId: string
    :param WorkerId: [REQUIRED]\nThe ID of the Worker to block.\n

    :type Reason: string
    :param Reason: [REQUIRED]\nA message explaining the reason for blocking the Worker. This parameter enables you to keep track of your Workers. The Worker does not see this message.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_hit(HITId=None):
    """
    The DeleteHIT operation is used to delete HIT that is no longer needed. Only the Requester who created the HIT can delete it.
    You can only dispose of HITs that are in the Reviewable state, with all of their submitted assignments already either approved or rejected. If you call the DeleteHIT operation on a HIT that is not in the Reviewable state (for example, that has not expired, or still has active assignments), or on a HIT that is Reviewable but without all of its submitted assignments already approved or rejected, the service will return an error.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_hit(
        HITId='string'
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]\nThe ID of the HIT to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_qualification_type(QualificationTypeId=None):
    """
    The DeleteQualificationType deletes a Qualification type and deletes any HIT types that are associated with the Qualification type.
    This operation does not revoke Qualifications already assigned to Workers because the Qualifications might be needed for active HITs. If there are any pending requests for the Qualification type, Amazon Mechanical Turk rejects those requests. After you delete a Qualification type, you can no longer use it to create HITs or HIT types.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_qualification_type(
        QualificationTypeId='string'
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]\nThe ID of the QualificationType to dispose.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def delete_worker_block(WorkerId=None, Reason=None):
    """
    The DeleteWorkerBlock operation allows you to reinstate a blocked Worker to work on your HITs. This operation reverses the effects of the CreateWorkerBlock operation. You need the Worker ID to use this operation. If the Worker ID is missing or invalid, this operation fails and returns the message \xe2\x80\x9cWorkerId is invalid.\xe2\x80\x9d If the specified Worker is not blocked, this operation returns successfully.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_worker_block(
        WorkerId='string',
        Reason='string'
    )
    
    
    :type WorkerId: string
    :param WorkerId: [REQUIRED]\nThe ID of the Worker to unblock.\n

    :type Reason: string
    :param Reason: A message that explains the reason for unblocking the Worker. The Worker does not see this message.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_qualification_from_worker(WorkerId=None, QualificationTypeId=None, Reason=None):
    """
    The DisassociateQualificationFromWorker revokes a previously granted Qualification from a user.
    You can provide a text message explaining why the Qualification was revoked. The user who had the Qualification can see this message.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_qualification_from_worker(
        WorkerId='string',
        QualificationTypeId='string',
        Reason='string'
    )
    
    
    :type WorkerId: string
    :param WorkerId: [REQUIRED]\nThe ID of the Worker who possesses the Qualification to be revoked.\n

    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]\nThe ID of the Qualification type of the Qualification to be revoked.\n

    :type Reason: string
    :param Reason: A text message that explains why the Qualification was revoked. The user who had the Qualification sees this message.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def get_account_balance():
    """
    The GetAccountBalance operation retrieves the amount of money in your Amazon Mechanical Turk account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_account_balance()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'AvailableBalance': 'string',
    'OnHoldBalance': 'string'
}


Response Structure

(dict) --
AvailableBalance (string) --A string representing a currency amount.

OnHoldBalance (string) --A string representing a currency amount.






Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'AvailableBalance': 'string',
        'OnHoldBalance': 'string'
    }
    
    
    """
    pass

def get_assignment(AssignmentId=None):
    """
    The GetAssignment operation retrieves the details of the specified Assignment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_assignment(
        AssignmentId='string'
    )
    
    
    :type AssignmentId: string
    :param AssignmentId: [REQUIRED]\nThe ID of the Assignment to be retrieved.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Assignment': {
        'AssignmentId': 'string',
        'WorkerId': 'string',
        'HITId': 'string',
        'AssignmentStatus': 'Submitted'|'Approved'|'Rejected',
        'AutoApprovalTime': datetime(2015, 1, 1),
        'AcceptTime': datetime(2015, 1, 1),
        'SubmitTime': datetime(2015, 1, 1),
        'ApprovalTime': datetime(2015, 1, 1),
        'RejectionTime': datetime(2015, 1, 1),
        'Deadline': datetime(2015, 1, 1),
        'Answer': 'string',
        'RequesterFeedback': 'string'
    },
    'HIT': {
        'HITId': 'string',
        'HITTypeId': 'string',
        'HITGroupId': 'string',
        'HITLayoutId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'Title': 'string',
        'Description': 'string',
        'Question': 'string',
        'Keywords': 'string',
        'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
        'MaxAssignments': 123,
        'Reward': 'string',
        'AutoApprovalDelayInSeconds': 123,
        'Expiration': datetime(2015, 1, 1),
        'AssignmentDurationInSeconds': 123,
        'RequesterAnnotation': 'string',
        'QualificationRequirements': [
            {
                'QualificationTypeId': 'string',
                'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                'IntegerValues': [
                    123,
                ],
                'LocaleValues': [
                    {
                        'Country': 'string',
                        'Subdivision': 'string'
                    },
                ],
                'RequiredToPreview': True|False,
                'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
            },
        ],
        'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
        'NumberOfAssignmentsPending': 123,
        'NumberOfAssignmentsAvailable': 123,
        'NumberOfAssignmentsCompleted': 123
    }
}


Response Structure

(dict) --
Assignment (dict) --The assignment. The response includes one Assignment element.

AssignmentId (string) --A unique identifier for the assignment.

WorkerId (string) --The ID of the Worker who accepted the HIT.

HITId (string) --The ID of the HIT.

AssignmentStatus (string) --The status of the assignment.

AutoApprovalTime (datetime) --If results have been submitted, AutoApprovalTime is the date and time the results of the assignment results are considered Approved automatically if they have not already been explicitly approved or rejected by the Requester. This value is derived from the auto-approval delay specified by the Requester in the HIT. This value is omitted from the assignment if the Worker has not yet submitted results.

AcceptTime (datetime) --The date and time the Worker accepted the assignment.

SubmitTime (datetime) --If the Worker has submitted results, SubmitTime is the date and time the assignment was submitted. This value is omitted from the assignment if the Worker has not yet submitted results.

ApprovalTime (datetime) --If the Worker has submitted results and the Requester has approved the results, ApprovalTime is the date and time the Requester approved the results. This value is omitted from the assignment if the Requester has not yet approved the results.

RejectionTime (datetime) --If the Worker has submitted results and the Requester has rejected the results, RejectionTime is the date and time the Requester rejected the results.

Deadline (datetime) --The date and time of the deadline for the assignment. This value is derived from the deadline specification for the HIT and the date and time the Worker accepted the HIT.

Answer (string) --The Worker\'s answers submitted for the HIT contained in a QuestionFormAnswers document, if the Worker provides an answer. If the Worker does not provide any answers, Answer may contain a QuestionFormAnswers document, or Answer may be empty.

RequesterFeedback (string) --The feedback string included with the call to the ApproveAssignment operation or the RejectAssignment operation, if the Requester approved or rejected the assignment and specified feedback.



HIT (dict) --The HIT associated with this assignment. The response includes one HIT element.

HITId (string) --A unique identifier for the HIT.

HITTypeId (string) --The ID of the HIT type of this HIT

HITGroupId (string) --The ID of the HIT Group of this HIT.

HITLayoutId (string) --The ID of the HIT Layout of this HIT.

CreationTime (datetime) --The date and time the HIT was created.

Title (string) --The title of the HIT.

Description (string) --A general description of the HIT.

Question (string) --The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

Keywords (string) --One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.

HITStatus (string) --The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed.

MaxAssignments (integer) --The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

Reward (string) --A string representing a currency amount.

AutoApprovalDelayInSeconds (integer) --The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid.

Expiration (datetime) --The date and time the HIT expires.

AssignmentDurationInSeconds (integer) --The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

RequesterAnnotation (string) --An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.

QualificationRequirements (list) --Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ActionsGuarded field on each QualificationRequirement structure.

(dict) --The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results.

QualificationTypeId (string) --The ID of the Qualification type for the requirement.

Comparator (string) --The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value.

IntegerValues (list) --The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.

(integer) --


LocaleValues (list) --The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.

(dict) --The Locale data structure represents a geographical region or location.

Country (string) --The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision (string) --The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.





RequiredToPreview (boolean) --DEPRECATED: Use the ActionsGuarded field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ActionsGuarded field.

ActionsGuarded (string) --Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the RequiredToPreview field.





HITReviewStatus (string) --Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.

NumberOfAssignmentsPending (integer) --The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.

NumberOfAssignmentsAvailable (integer) --The number of assignments for this HIT that are available for Workers to accept.

NumberOfAssignmentsCompleted (integer) --The number of assignments for this HIT that have been approved or rejected.








Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'Assignment': {
            'AssignmentId': 'string',
            'WorkerId': 'string',
            'HITId': 'string',
            'AssignmentStatus': 'Submitted'|'Approved'|'Rejected',
            'AutoApprovalTime': datetime(2015, 1, 1),
            'AcceptTime': datetime(2015, 1, 1),
            'SubmitTime': datetime(2015, 1, 1),
            'ApprovalTime': datetime(2015, 1, 1),
            'RejectionTime': datetime(2015, 1, 1),
            'Deadline': datetime(2015, 1, 1),
            'Answer': 'string',
            'RequesterFeedback': 'string'
        },
        'HIT': {
            'HITId': 'string',
            'HITTypeId': 'string',
            'HITGroupId': 'string',
            'HITLayoutId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Title': 'string',
            'Description': 'string',
            'Question': 'string',
            'Keywords': 'string',
            'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
            'MaxAssignments': 123,
            'Reward': 'string',
            'AutoApprovalDelayInSeconds': 123,
            'Expiration': datetime(2015, 1, 1),
            'AssignmentDurationInSeconds': 123,
            'RequesterAnnotation': 'string',
            'QualificationRequirements': [
                {
                    'QualificationTypeId': 'string',
                    'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                    'IntegerValues': [
                        123,
                    ],
                    'LocaleValues': [
                        {
                            'Country': 'string',
                            'Subdivision': 'string'
                        },
                    ],
                    'RequiredToPreview': True|False,
                    'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
                },
            ],
            'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
            'NumberOfAssignmentsPending': 123,
            'NumberOfAssignmentsAvailable': 123,
            'NumberOfAssignmentsCompleted': 123
        }
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def get_file_upload_url(AssignmentId=None, QuestionIdentifier=None):
    """
    The GetFileUploadURL operation generates and returns a temporary URL. You use the temporary URL to retrieve a file uploaded by a Worker as an answer to a FileUploadAnswer question for a HIT. The temporary URL is generated the instant the GetFileUploadURL operation is called, and is valid for 60 seconds. You can get a temporary file upload URL any time until the HIT is disposed. After the HIT is disposed, any uploaded files are deleted, and cannot be retrieved. Pending Deprecation on December 12, 2017. The Answer Specification structure will no longer support the FileUploadAnswer element to be used for the QuestionForm data structure. Instead, we recommend that Requesters who want to create HITs asking Workers to upload files to use Amazon S3.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_file_upload_url(
        AssignmentId='string',
        QuestionIdentifier='string'
    )
    
    
    :type AssignmentId: string
    :param AssignmentId: [REQUIRED]\nThe ID of the assignment that contains the question with a FileUploadAnswer.\n

    :type QuestionIdentifier: string
    :param QuestionIdentifier: [REQUIRED]\nThe identifier of the question with a FileUploadAnswer, as specified in the QuestionForm of the HIT.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FileUploadURL': 'string'
}


Response Structure

(dict) --

FileUploadURL (string) --
A temporary URL for the file that the Worker uploaded for the answer.







Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'FileUploadURL': 'string'
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def get_hit(HITId=None):
    """
    The GetHIT operation retrieves the details of the specified HIT.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_hit(
        HITId='string'
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]\nThe ID of the HIT to be retrieved.\n

    :rtype: dict
ReturnsResponse Syntax{
    'HIT': {
        'HITId': 'string',
        'HITTypeId': 'string',
        'HITGroupId': 'string',
        'HITLayoutId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'Title': 'string',
        'Description': 'string',
        'Question': 'string',
        'Keywords': 'string',
        'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
        'MaxAssignments': 123,
        'Reward': 'string',
        'AutoApprovalDelayInSeconds': 123,
        'Expiration': datetime(2015, 1, 1),
        'AssignmentDurationInSeconds': 123,
        'RequesterAnnotation': 'string',
        'QualificationRequirements': [
            {
                'QualificationTypeId': 'string',
                'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                'IntegerValues': [
                    123,
                ],
                'LocaleValues': [
                    {
                        'Country': 'string',
                        'Subdivision': 'string'
                    },
                ],
                'RequiredToPreview': True|False,
                'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
            },
        ],
        'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
        'NumberOfAssignmentsPending': 123,
        'NumberOfAssignmentsAvailable': 123,
        'NumberOfAssignmentsCompleted': 123
    }
}


Response Structure

(dict) --
HIT (dict) --Contains the requested HIT data.

HITId (string) --A unique identifier for the HIT.

HITTypeId (string) --The ID of the HIT type of this HIT

HITGroupId (string) --The ID of the HIT Group of this HIT.

HITLayoutId (string) --The ID of the HIT Layout of this HIT.

CreationTime (datetime) --The date and time the HIT was created.

Title (string) --The title of the HIT.

Description (string) --A general description of the HIT.

Question (string) --The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

Keywords (string) --One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.

HITStatus (string) --The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed.

MaxAssignments (integer) --The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

Reward (string) --A string representing a currency amount.

AutoApprovalDelayInSeconds (integer) --The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid.

Expiration (datetime) --The date and time the HIT expires.

AssignmentDurationInSeconds (integer) --The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

RequesterAnnotation (string) --An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.

QualificationRequirements (list) --Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ActionsGuarded field on each QualificationRequirement structure.

(dict) --The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results.

QualificationTypeId (string) --The ID of the Qualification type for the requirement.

Comparator (string) --The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value.

IntegerValues (list) --The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.

(integer) --


LocaleValues (list) --The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.

(dict) --The Locale data structure represents a geographical region or location.

Country (string) --The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision (string) --The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.





RequiredToPreview (boolean) --DEPRECATED: Use the ActionsGuarded field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ActionsGuarded field.

ActionsGuarded (string) --Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the RequiredToPreview field.





HITReviewStatus (string) --Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.

NumberOfAssignmentsPending (integer) --The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.

NumberOfAssignmentsAvailable (integer) --The number of assignments for this HIT that are available for Workers to accept.

NumberOfAssignmentsCompleted (integer) --The number of assignments for this HIT that have been approved or rejected.








Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'HIT': {
            'HITId': 'string',
            'HITTypeId': 'string',
            'HITGroupId': 'string',
            'HITLayoutId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Title': 'string',
            'Description': 'string',
            'Question': 'string',
            'Keywords': 'string',
            'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
            'MaxAssignments': 123,
            'Reward': 'string',
            'AutoApprovalDelayInSeconds': 123,
            'Expiration': datetime(2015, 1, 1),
            'AssignmentDurationInSeconds': 123,
            'RequesterAnnotation': 'string',
            'QualificationRequirements': [
                {
                    'QualificationTypeId': 'string',
                    'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                    'IntegerValues': [
                        123,
                    ],
                    'LocaleValues': [
                        {
                            'Country': 'string',
                            'Subdivision': 'string'
                        },
                    ],
                    'RequiredToPreview': True|False,
                    'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
                },
            ],
            'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
            'NumberOfAssignmentsPending': 123,
            'NumberOfAssignmentsAvailable': 123,
            'NumberOfAssignmentsCompleted': 123
        }
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
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

def get_qualification_score(QualificationTypeId=None, WorkerId=None):
    """
    The GetQualificationScore operation returns the value of a Worker\'s Qualification for a given Qualification type.
    To get a Worker\'s Qualification, you must know the Worker\'s ID. The Worker\'s ID is included in the assignment data returned by the ListAssignmentsForHIT operation.
    Only the owner of a Qualification type can query the value of a Worker\'s Qualification of that type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_qualification_score(
        QualificationTypeId='string',
        WorkerId='string'
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]\nThe ID of the QualificationType.\n

    :type WorkerId: string
    :param WorkerId: [REQUIRED]\nThe ID of the Worker whose Qualification is being updated.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Qualification': {
        'QualificationTypeId': 'string',
        'WorkerId': 'string',
        'GrantTime': datetime(2015, 1, 1),
        'IntegerValue': 123,
        'LocaleValue': {
            'Country': 'string',
            'Subdivision': 'string'
        },
        'Status': 'Granted'|'Revoked'
    }
}


Response Structure

(dict) --

Qualification (dict) --
The Qualification data structure of the Qualification assigned to a user, including the Qualification type and the value (score).

QualificationTypeId (string) --
The ID of the Qualification type for the Qualification.

WorkerId (string) --
The ID of the Worker who possesses the Qualification.

GrantTime (datetime) --
The date and time the Qualification was granted to the Worker. If the Worker\'s Qualification was revoked, and then re-granted based on a new Qualification request, GrantTime is the date and time of the last call to the AcceptQualificationRequest operation.

IntegerValue (integer) --
The value (score) of the Qualification, if the Qualification has an integer value.

LocaleValue (dict) --
The Locale data structure represents a geographical region or location.

Country (string) --
The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision (string) --
The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.



Status (string) --
The status of the Qualification. Valid values are Granted | Revoked.









Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'Qualification': {
            'QualificationTypeId': 'string',
            'WorkerId': 'string',
            'GrantTime': datetime(2015, 1, 1),
            'IntegerValue': 123,
            'LocaleValue': {
                'Country': 'string',
                'Subdivision': 'string'
            },
            'Status': 'Granted'|'Revoked'
        }
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def get_qualification_type(QualificationTypeId=None):
    """
    The GetQualificationType operation retrieves information about a Qualification type using its ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_qualification_type(
        QualificationTypeId='string'
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]\nThe ID of the QualificationType.\n

    :rtype: dict
ReturnsResponse Syntax{
    'QualificationType': {
        'QualificationTypeId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'Name': 'string',
        'Description': 'string',
        'Keywords': 'string',
        'QualificationTypeStatus': 'Active'|'Inactive',
        'Test': 'string',
        'TestDurationInSeconds': 123,
        'AnswerKey': 'string',
        'RetryDelayInSeconds': 123,
        'IsRequestable': True|False,
        'AutoGranted': True|False,
        'AutoGrantedValue': 123
    }
}


Response Structure

(dict) --
QualificationType (dict) --The returned Qualification Type

QualificationTypeId (string) --A unique identifier for the Qualification type. A Qualification type is given a Qualification type ID when you call the CreateQualificationType operation.

CreationTime (datetime) --The date and time the Qualification type was created.

Name (string) --The name of the Qualification type. The type name is used to identify the type, and to find the type using a Qualification type search.

Description (string) --A long description for the Qualification type.

Keywords (string) --One or more words or phrases that describe theQualification type, separated by commas. The Keywords make the type easier to find using a search.

QualificationTypeStatus (string) --The status of the Qualification type. A Qualification type\'s status determines if users can apply to receive a Qualification of this type, and if HITs can be created with requirements based on this type. Valid values are Active | Inactive.

Test (string) --The questions for a Qualification test associated with this Qualification type that a user can take to obtain a Qualification of this type. This parameter must be specified if AnswerKey is present. A Qualification type cannot have both a specified Test parameter and an AutoGranted value of true.

TestDurationInSeconds (integer) --The amount of time, in seconds, given to a Worker to complete the Qualification test, beginning from the time the Worker requests the Qualification.

AnswerKey (string) --The answers to the Qualification test specified in the Test parameter.

RetryDelayInSeconds (integer) --The amount of time, in seconds, Workers must wait after taking the Qualification test before they can take it again. Workers can take a Qualification test multiple times if they were not granted the Qualification from a previous attempt, or if the test offers a gradient score and they want a better score. If not specified, retries are disabled and Workers can request a Qualification only once.

IsRequestable (boolean) --Specifies whether the Qualification type is one that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is False for Qualifications assigned automatically by the system. Valid values are True | False.

AutoGranted (boolean) --Specifies that requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test. Valid values are True | False.

AutoGrantedValue (integer) --The Qualification integer value to use for automatically granted Qualifications, if AutoGranted is true. This is 1 by default.








Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'QualificationType': {
            'QualificationTypeId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Name': 'string',
            'Description': 'string',
            'Keywords': 'string',
            'QualificationTypeStatus': 'Active'|'Inactive',
            'Test': 'string',
            'TestDurationInSeconds': 123,
            'AnswerKey': 'string',
            'RetryDelayInSeconds': 123,
            'IsRequestable': True|False,
            'AutoGranted': True|False,
            'AutoGrantedValue': 123
        }
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

def list_assignments_for_hit(HITId=None, NextToken=None, MaxResults=None, AssignmentStatuses=None):
    """
    The ListAssignmentsForHIT operation retrieves completed assignments for a HIT. You can use this operation to retrieve the results for a HIT.
    You can get assignments for a HIT at any time, even if the HIT is not yet Reviewable. If a HIT requested multiple assignments, and has received some results but has not yet become Reviewable, you can still retrieve the partial results with this operation.
    Use the AssignmentStatus parameter to control which set of assignments for a HIT are returned. The ListAssignmentsForHIT operation can return submitted assignments awaiting approval, or it can return assignments that have already been approved or rejected. You can set AssignmentStatus=Approved,Rejected to get assignments that have already been approved and rejected together in one result set.
    Only the Requester who created the HIT can retrieve the assignments for that HIT.
    Results are sorted and divided into numbered pages and the operation returns a single page of results. You can use the parameters of the operation to control sorting and pagination.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_assignments_for_hit(
        HITId='string',
        NextToken='string',
        MaxResults=123,
        AssignmentStatuses=[
            'Submitted'|'Approved'|'Rejected',
        ]
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]\nThe ID of the HIT.\n

    :type NextToken: string
    :param NextToken: Pagination token

    :type MaxResults: integer
    :param MaxResults: 

    :type AssignmentStatuses: list
    :param AssignmentStatuses: The status of the assignments to return: Submitted | Approved | Rejected\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'NumResults': 123,
    'Assignments': [
        {
            'AssignmentId': 'string',
            'WorkerId': 'string',
            'HITId': 'string',
            'AssignmentStatus': 'Submitted'|'Approved'|'Rejected',
            'AutoApprovalTime': datetime(2015, 1, 1),
            'AcceptTime': datetime(2015, 1, 1),
            'SubmitTime': datetime(2015, 1, 1),
            'ApprovalTime': datetime(2015, 1, 1),
            'RejectionTime': datetime(2015, 1, 1),
            'Deadline': datetime(2015, 1, 1),
            'Answer': 'string',
            'RequesterFeedback': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

NumResults (integer) --
The number of assignments on the page in the filtered results list, equivalent to the number of assignments returned by this call.

Assignments (list) --
The collection of Assignment data structures returned by this call.

(dict) --
The Assignment data structure represents a single assignment of a HIT to a Worker. The assignment tracks the Worker\'s efforts to complete the HIT, and contains the results for later retrieval.

AssignmentId (string) --
A unique identifier for the assignment.

WorkerId (string) --
The ID of the Worker who accepted the HIT.

HITId (string) --
The ID of the HIT.

AssignmentStatus (string) --
The status of the assignment.

AutoApprovalTime (datetime) --
If results have been submitted, AutoApprovalTime is the date and time the results of the assignment results are considered Approved automatically if they have not already been explicitly approved or rejected by the Requester. This value is derived from the auto-approval delay specified by the Requester in the HIT. This value is omitted from the assignment if the Worker has not yet submitted results.

AcceptTime (datetime) --
The date and time the Worker accepted the assignment.

SubmitTime (datetime) --
If the Worker has submitted results, SubmitTime is the date and time the assignment was submitted. This value is omitted from the assignment if the Worker has not yet submitted results.

ApprovalTime (datetime) --
If the Worker has submitted results and the Requester has approved the results, ApprovalTime is the date and time the Requester approved the results. This value is omitted from the assignment if the Requester has not yet approved the results.

RejectionTime (datetime) --
If the Worker has submitted results and the Requester has rejected the results, RejectionTime is the date and time the Requester rejected the results.

Deadline (datetime) --
The date and time of the deadline for the assignment. This value is derived from the deadline specification for the HIT and the date and time the Worker accepted the HIT.

Answer (string) --
The Worker\'s answers submitted for the HIT contained in a QuestionFormAnswers document, if the Worker provides an answer. If the Worker does not provide any answers, Answer may contain a QuestionFormAnswers document, or Answer may be empty.

RequesterFeedback (string) --
The feedback string included with the call to the ApproveAssignment operation or the RejectAssignment operation, if the Requester approved or rejected the assignment and specified feedback.











Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'NextToken': 'string',
        'NumResults': 123,
        'Assignments': [
            {
                'AssignmentId': 'string',
                'WorkerId': 'string',
                'HITId': 'string',
                'AssignmentStatus': 'Submitted'|'Approved'|'Rejected',
                'AutoApprovalTime': datetime(2015, 1, 1),
                'AcceptTime': datetime(2015, 1, 1),
                'SubmitTime': datetime(2015, 1, 1),
                'ApprovalTime': datetime(2015, 1, 1),
                'RejectionTime': datetime(2015, 1, 1),
                'Deadline': datetime(2015, 1, 1),
                'Answer': 'string',
                'RequesterFeedback': 'string'
            },
        ]
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def list_bonus_payments(HITId=None, AssignmentId=None, NextToken=None, MaxResults=None):
    """
    The ListBonusPayments operation retrieves the amounts of bonuses you have paid to Workers for a given HIT or assignment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_bonus_payments(
        HITId='string',
        AssignmentId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type HITId: string
    :param HITId: The ID of the HIT associated with the bonus payments to retrieve. If not specified, all bonus payments for all assignments for the given HIT are returned. Either the HITId parameter or the AssignmentId parameter must be specified

    :type AssignmentId: string
    :param AssignmentId: The ID of the assignment associated with the bonus payments to retrieve. If specified, only bonus payments for the given assignment are returned. Either the HITId parameter or the AssignmentId parameter must be specified

    :type NextToken: string
    :param NextToken: Pagination token

    :type MaxResults: integer
    :param MaxResults: 

    :rtype: dict

ReturnsResponse Syntax
{
    'NumResults': 123,
    'NextToken': 'string',
    'BonusPayments': [
        {
            'WorkerId': 'string',
            'BonusAmount': 'string',
            'AssignmentId': 'string',
            'Reason': 'string',
            'GrantTime': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

NumResults (integer) --
The number of bonus payments on this page in the filtered results list, equivalent to the number of bonus payments being returned by this call.

NextToken (string) --
If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

BonusPayments (list) --
A successful request to the ListBonusPayments operation returns a list of BonusPayment objects.

(dict) --
An object representing a Bonus payment paid to a Worker.

WorkerId (string) --
The ID of the Worker to whom the bonus was paid.

BonusAmount (string) --
A string representing a currency amount.

AssignmentId (string) --
The ID of the assignment associated with this bonus payment.

Reason (string) --
The Reason text given when the bonus was granted, if any.

GrantTime (datetime) --
The date and time of when the bonus was granted.











Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'NumResults': 123,
        'NextToken': 'string',
        'BonusPayments': [
            {
                'WorkerId': 'string',
                'BonusAmount': 'string',
                'AssignmentId': 'string',
                'Reason': 'string',
                'GrantTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def list_hits(NextToken=None, MaxResults=None):
    """
    The ListHITs operation returns all of a Requester\'s HITs. The operation returns HITs of any status, except for HITs that have been deleted of with the DeleteHIT operation or that have been auto-deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_hits(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token

    :type MaxResults: integer
    :param MaxResults: 

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'NumResults': 123,
    'HITs': [
        {
            'HITId': 'string',
            'HITTypeId': 'string',
            'HITGroupId': 'string',
            'HITLayoutId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Title': 'string',
            'Description': 'string',
            'Question': 'string',
            'Keywords': 'string',
            'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
            'MaxAssignments': 123,
            'Reward': 'string',
            'AutoApprovalDelayInSeconds': 123,
            'Expiration': datetime(2015, 1, 1),
            'AssignmentDurationInSeconds': 123,
            'RequesterAnnotation': 'string',
            'QualificationRequirements': [
                {
                    'QualificationTypeId': 'string',
                    'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                    'IntegerValues': [
                        123,
                    ],
                    'LocaleValues': [
                        {
                            'Country': 'string',
                            'Subdivision': 'string'
                        },
                    ],
                    'RequiredToPreview': True|False,
                    'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
                },
            ],
            'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
            'NumberOfAssignmentsPending': 123,
            'NumberOfAssignmentsAvailable': 123,
            'NumberOfAssignmentsCompleted': 123
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

NumResults (integer) --
The number of HITs on this page in the filtered results list, equivalent to the number of HITs being returned by this call.

HITs (list) --
The list of HIT elements returned by the query.

(dict) --
The HIT data structure represents a single HIT, including all the information necessary for a Worker to accept and complete the HIT.

HITId (string) --
A unique identifier for the HIT.

HITTypeId (string) --
The ID of the HIT type of this HIT

HITGroupId (string) --
The ID of the HIT Group of this HIT.

HITLayoutId (string) --
The ID of the HIT Layout of this HIT.

CreationTime (datetime) --
The date and time the HIT was created.

Title (string) --
The title of the HIT.

Description (string) --
A general description of the HIT.

Question (string) --
The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

Keywords (string) --
One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.

HITStatus (string) --
The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed.

MaxAssignments (integer) --
The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

Reward (string) --
A string representing a currency amount.

AutoApprovalDelayInSeconds (integer) --
The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid.

Expiration (datetime) --
The date and time the HIT expires.

AssignmentDurationInSeconds (integer) --
The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

RequesterAnnotation (string) --
An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.

QualificationRequirements (list) --
Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ActionsGuarded field on each QualificationRequirement structure.

(dict) --
The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results.

QualificationTypeId (string) --
The ID of the Qualification type for the requirement.

Comparator (string) --
The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value.

IntegerValues (list) --
The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.

(integer) --


LocaleValues (list) --
The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.

(dict) --
The Locale data structure represents a geographical region or location.

Country (string) --
The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision (string) --
The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.





RequiredToPreview (boolean) --
DEPRECATED: Use the ActionsGuarded field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ActionsGuarded field.

ActionsGuarded (string) --
Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the RequiredToPreview field.





HITReviewStatus (string) --
Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.

NumberOfAssignmentsPending (integer) --
The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.

NumberOfAssignmentsAvailable (integer) --
The number of assignments for this HIT that are available for Workers to accept.

NumberOfAssignmentsCompleted (integer) --
The number of assignments for this HIT that have been approved or rejected.











Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'NextToken': 'string',
        'NumResults': 123,
        'HITs': [
            {
                'HITId': 'string',
                'HITTypeId': 'string',
                'HITGroupId': 'string',
                'HITLayoutId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'Title': 'string',
                'Description': 'string',
                'Question': 'string',
                'Keywords': 'string',
                'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
                'MaxAssignments': 123,
                'Reward': 'string',
                'AutoApprovalDelayInSeconds': 123,
                'Expiration': datetime(2015, 1, 1),
                'AssignmentDurationInSeconds': 123,
                'RequesterAnnotation': 'string',
                'QualificationRequirements': [
                    {
                        'QualificationTypeId': 'string',
                        'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                        'IntegerValues': [
                            123,
                        ],
                        'LocaleValues': [
                            {
                                'Country': 'string',
                                'Subdivision': 'string'
                            },
                        ],
                        'RequiredToPreview': True|False,
                        'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
                    },
                ],
                'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
                'NumberOfAssignmentsPending': 123,
                'NumberOfAssignmentsAvailable': 123,
                'NumberOfAssignmentsCompleted': 123
            },
        ]
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def list_hits_for_qualification_type(QualificationTypeId=None, NextToken=None, MaxResults=None):
    """
    The ListHITsForQualificationType operation returns the HITs that use the given Qualification type for a Qualification requirement. The operation returns HITs of any status, except for HITs that have been deleted with the DeleteHIT operation or that have been auto-deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_hits_for_qualification_type(
        QualificationTypeId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]\nThe ID of the Qualification type to use when querying HITs.\n

    :type NextToken: string
    :param NextToken: Pagination Token

    :type MaxResults: integer
    :param MaxResults: Limit the number of results returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'NumResults': 123,
    'HITs': [
        {
            'HITId': 'string',
            'HITTypeId': 'string',
            'HITGroupId': 'string',
            'HITLayoutId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Title': 'string',
            'Description': 'string',
            'Question': 'string',
            'Keywords': 'string',
            'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
            'MaxAssignments': 123,
            'Reward': 'string',
            'AutoApprovalDelayInSeconds': 123,
            'Expiration': datetime(2015, 1, 1),
            'AssignmentDurationInSeconds': 123,
            'RequesterAnnotation': 'string',
            'QualificationRequirements': [
                {
                    'QualificationTypeId': 'string',
                    'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                    'IntegerValues': [
                        123,
                    ],
                    'LocaleValues': [
                        {
                            'Country': 'string',
                            'Subdivision': 'string'
                        },
                    ],
                    'RequiredToPreview': True|False,
                    'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
                },
            ],
            'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
            'NumberOfAssignmentsPending': 123,
            'NumberOfAssignmentsAvailable': 123,
            'NumberOfAssignmentsCompleted': 123
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

NumResults (integer) --
The number of HITs on this page in the filtered results list, equivalent to the number of HITs being returned by this call.

HITs (list) --
The list of HIT elements returned by the query.

(dict) --
The HIT data structure represents a single HIT, including all the information necessary for a Worker to accept and complete the HIT.

HITId (string) --
A unique identifier for the HIT.

HITTypeId (string) --
The ID of the HIT type of this HIT

HITGroupId (string) --
The ID of the HIT Group of this HIT.

HITLayoutId (string) --
The ID of the HIT Layout of this HIT.

CreationTime (datetime) --
The date and time the HIT was created.

Title (string) --
The title of the HIT.

Description (string) --
A general description of the HIT.

Question (string) --
The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

Keywords (string) --
One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.

HITStatus (string) --
The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed.

MaxAssignments (integer) --
The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

Reward (string) --
A string representing a currency amount.

AutoApprovalDelayInSeconds (integer) --
The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid.

Expiration (datetime) --
The date and time the HIT expires.

AssignmentDurationInSeconds (integer) --
The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

RequesterAnnotation (string) --
An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.

QualificationRequirements (list) --
Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ActionsGuarded field on each QualificationRequirement structure.

(dict) --
The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results.

QualificationTypeId (string) --
The ID of the Qualification type for the requirement.

Comparator (string) --
The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value.

IntegerValues (list) --
The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.

(integer) --


LocaleValues (list) --
The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.

(dict) --
The Locale data structure represents a geographical region or location.

Country (string) --
The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision (string) --
The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.





RequiredToPreview (boolean) --
DEPRECATED: Use the ActionsGuarded field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ActionsGuarded field.

ActionsGuarded (string) --
Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the RequiredToPreview field.





HITReviewStatus (string) --
Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.

NumberOfAssignmentsPending (integer) --
The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.

NumberOfAssignmentsAvailable (integer) --
The number of assignments for this HIT that are available for Workers to accept.

NumberOfAssignmentsCompleted (integer) --
The number of assignments for this HIT that have been approved or rejected.











Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'NextToken': 'string',
        'NumResults': 123,
        'HITs': [
            {
                'HITId': 'string',
                'HITTypeId': 'string',
                'HITGroupId': 'string',
                'HITLayoutId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'Title': 'string',
                'Description': 'string',
                'Question': 'string',
                'Keywords': 'string',
                'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
                'MaxAssignments': 123,
                'Reward': 'string',
                'AutoApprovalDelayInSeconds': 123,
                'Expiration': datetime(2015, 1, 1),
                'AssignmentDurationInSeconds': 123,
                'RequesterAnnotation': 'string',
                'QualificationRequirements': [
                    {
                        'QualificationTypeId': 'string',
                        'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                        'IntegerValues': [
                            123,
                        ],
                        'LocaleValues': [
                            {
                                'Country': 'string',
                                'Subdivision': 'string'
                            },
                        ],
                        'RequiredToPreview': True|False,
                        'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
                    },
                ],
                'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
                'NumberOfAssignmentsPending': 123,
                'NumberOfAssignmentsAvailable': 123,
                'NumberOfAssignmentsCompleted': 123
            },
        ]
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def list_qualification_requests(QualificationTypeId=None, NextToken=None, MaxResults=None):
    """
    The ListQualificationRequests operation retrieves requests for Qualifications of a particular Qualification type. The owner of the Qualification type calls this operation to poll for pending requests, and accepts them using the AcceptQualification operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_qualification_requests(
        QualificationTypeId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: The ID of the QualificationType.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict

ReturnsResponse Syntax
{
    'NumResults': 123,
    'NextToken': 'string',
    'QualificationRequests': [
        {
            'QualificationRequestId': 'string',
            'QualificationTypeId': 'string',
            'WorkerId': 'string',
            'Test': 'string',
            'Answer': 'string',
            'SubmitTime': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

NumResults (integer) --
The number of Qualification requests on this page in the filtered results list, equivalent to the number of Qualification requests being returned by this call.

NextToken (string) --
If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

QualificationRequests (list) --
The Qualification request. The response includes one QualificationRequest element for each Qualification request returned by the query.

(dict) --
The QualificationRequest data structure represents a request a Worker has made for a Qualification.

QualificationRequestId (string) --
The ID of the Qualification request, a unique identifier generated when the request was submitted.

QualificationTypeId (string) --
The ID of the Qualification type the Worker is requesting, as returned by the CreateQualificationType operation.

WorkerId (string) --
The ID of the Worker requesting the Qualification.

Test (string) --
The contents of the Qualification test that was presented to the Worker, if the type has a test and the Worker has submitted answers. This value is identical to the QuestionForm associated with the Qualification type at the time the Worker requests the Qualification.

Answer (string) --
The Worker\'s answers for the Qualification type\'s test contained in a QuestionFormAnswers document, if the type has a test and the Worker has submitted answers. If the Worker does not provide any answers, Answer may be empty.

SubmitTime (datetime) --
The date and time the Qualification request had a status of Submitted. This is either the time the Worker submitted answers for a Qualification test, or the time the Worker requested the Qualification if the Qualification type does not have a test.











Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'NumResults': 123,
        'NextToken': 'string',
        'QualificationRequests': [
            {
                'QualificationRequestId': 'string',
                'QualificationTypeId': 'string',
                'WorkerId': 'string',
                'Test': 'string',
                'Answer': 'string',
                'SubmitTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def list_qualification_types(Query=None, MustBeRequestable=None, MustBeOwnedByCaller=None, NextToken=None, MaxResults=None):
    """
    The ListQualificationTypes operation returns a list of Qualification types, filtered by an optional search term.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_qualification_types(
        Query='string',
        MustBeRequestable=True|False,
        MustBeOwnedByCaller=True|False,
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Query: string
    :param Query: A text query against all of the searchable attributes of Qualification types.

    :type MustBeRequestable: boolean
    :param MustBeRequestable: [REQUIRED]\nSpecifies that only Qualification types that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test, are returned as results of the search. Some Qualification types, such as those assigned automatically by the system, cannot be requested directly by users. If false, all Qualification types, including those managed by the system, are considered. Valid values are True | False.\n

    :type MustBeOwnedByCaller: boolean
    :param MustBeOwnedByCaller: Specifies that only Qualification types that the Requester created are returned. If false, the operation returns all Qualification types.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict

ReturnsResponse Syntax
{
    'NumResults': 123,
    'NextToken': 'string',
    'QualificationTypes': [
        {
            'QualificationTypeId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Name': 'string',
            'Description': 'string',
            'Keywords': 'string',
            'QualificationTypeStatus': 'Active'|'Inactive',
            'Test': 'string',
            'TestDurationInSeconds': 123,
            'AnswerKey': 'string',
            'RetryDelayInSeconds': 123,
            'IsRequestable': True|False,
            'AutoGranted': True|False,
            'AutoGrantedValue': 123
        },
    ]
}


Response Structure

(dict) --

NumResults (integer) --
The number of Qualification types on this page in the filtered results list, equivalent to the number of types this operation returns.

NextToken (string) --
If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

QualificationTypes (list) --
The list of QualificationType elements returned by the query.

(dict) --
The QualificationType data structure represents a Qualification type, a description of a property of a Worker that must match the requirements of a HIT for the Worker to be able to accept the HIT. The type also describes how a Worker can obtain a Qualification of that type, such as through a Qualification test.

QualificationTypeId (string) --
A unique identifier for the Qualification type. A Qualification type is given a Qualification type ID when you call the CreateQualificationType operation.

CreationTime (datetime) --
The date and time the Qualification type was created.

Name (string) --
The name of the Qualification type. The type name is used to identify the type, and to find the type using a Qualification type search.

Description (string) --
A long description for the Qualification type.

Keywords (string) --
One or more words or phrases that describe theQualification type, separated by commas. The Keywords make the type easier to find using a search.

QualificationTypeStatus (string) --
The status of the Qualification type. A Qualification type\'s status determines if users can apply to receive a Qualification of this type, and if HITs can be created with requirements based on this type. Valid values are Active | Inactive.

Test (string) --
The questions for a Qualification test associated with this Qualification type that a user can take to obtain a Qualification of this type. This parameter must be specified if AnswerKey is present. A Qualification type cannot have both a specified Test parameter and an AutoGranted value of true.

TestDurationInSeconds (integer) --
The amount of time, in seconds, given to a Worker to complete the Qualification test, beginning from the time the Worker requests the Qualification.

AnswerKey (string) --
The answers to the Qualification test specified in the Test parameter.

RetryDelayInSeconds (integer) --
The amount of time, in seconds, Workers must wait after taking the Qualification test before they can take it again. Workers can take a Qualification test multiple times if they were not granted the Qualification from a previous attempt, or if the test offers a gradient score and they want a better score. If not specified, retries are disabled and Workers can request a Qualification only once.

IsRequestable (boolean) --
Specifies whether the Qualification type is one that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is False for Qualifications assigned automatically by the system. Valid values are True | False.

AutoGranted (boolean) --
Specifies that requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test. Valid values are True | False.

AutoGrantedValue (integer) --
The Qualification integer value to use for automatically granted Qualifications, if AutoGranted is true. This is 1 by default.











Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'NumResults': 123,
        'NextToken': 'string',
        'QualificationTypes': [
            {
                'QualificationTypeId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'Name': 'string',
                'Description': 'string',
                'Keywords': 'string',
                'QualificationTypeStatus': 'Active'|'Inactive',
                'Test': 'string',
                'TestDurationInSeconds': 123,
                'AnswerKey': 'string',
                'RetryDelayInSeconds': 123,
                'IsRequestable': True|False,
                'AutoGranted': True|False,
                'AutoGrantedValue': 123
            },
        ]
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def list_review_policy_results_for_hit(HITId=None, PolicyLevels=None, RetrieveActions=None, RetrieveResults=None, NextToken=None, MaxResults=None):
    """
    The ListReviewPolicyResultsForHIT operation retrieves the computed results and the actions taken in the course of executing your Review Policies for a given HIT. For information about how to specify Review Policies when you call CreateHIT, see Review Policies. The ListReviewPolicyResultsForHIT operation can return results for both Assignment-level and HIT-level review results.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_review_policy_results_for_hit(
        HITId='string',
        PolicyLevels=[
            'Assignment'|'HIT',
        ],
        RetrieveActions=True|False,
        RetrieveResults=True|False,
        NextToken='string',
        MaxResults=123
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]\nThe unique identifier of the HIT to retrieve review results for.\n

    :type PolicyLevels: list
    :param PolicyLevels: The Policy Level(s) to retrieve review results for - HIT or Assignment. If omitted, the default behavior is to retrieve all data for both policy levels. For a list of all the described policies, see Review Policies.\n\n(string) --\n\n

    :type RetrieveActions: boolean
    :param RetrieveActions: Specify if the operation should retrieve a list of the actions taken executing the Review Policies and their outcomes.

    :type RetrieveResults: boolean
    :param RetrieveResults: Specify if the operation should retrieve a list of the results computed by the Review Policies.

    :type NextToken: string
    :param NextToken: Pagination token

    :type MaxResults: integer
    :param MaxResults: Limit the number of results returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'HITId': 'string',
    'AssignmentReviewPolicy': {
        'PolicyName': 'string',
        'Parameters': [
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MapEntries': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ]
            },
        ]
    },
    'HITReviewPolicy': {
        'PolicyName': 'string',
        'Parameters': [
            {
                'Key': 'string',
                'Values': [
                    'string',
                ],
                'MapEntries': [
                    {
                        'Key': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ]
            },
        ]
    },
    'AssignmentReviewReport': {
        'ReviewResults': [
            {
                'ActionId': 'string',
                'SubjectId': 'string',
                'SubjectType': 'string',
                'QuestionId': 'string',
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'ReviewActions': [
            {
                'ActionId': 'string',
                'ActionName': 'string',
                'TargetId': 'string',
                'TargetType': 'string',
                'Status': 'Intended'|'Succeeded'|'Failed'|'Cancelled',
                'CompleteTime': datetime(2015, 1, 1),
                'Result': 'string',
                'ErrorCode': 'string'
            },
        ]
    },
    'HITReviewReport': {
        'ReviewResults': [
            {
                'ActionId': 'string',
                'SubjectId': 'string',
                'SubjectType': 'string',
                'QuestionId': 'string',
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'ReviewActions': [
            {
                'ActionId': 'string',
                'ActionName': 'string',
                'TargetId': 'string',
                'TargetType': 'string',
                'Status': 'Intended'|'Succeeded'|'Failed'|'Cancelled',
                'CompleteTime': datetime(2015, 1, 1),
                'Result': 'string',
                'ErrorCode': 'string'
            },
        ]
    },
    'NextToken': 'string'
}


Response Structure

(dict) --

HITId (string) --
The HITId of the HIT for which results have been returned.

AssignmentReviewPolicy (dict) --
The name of the Assignment-level Review Policy. This contains only the PolicyName element.

PolicyName (string) --
Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

Parameters (list) --
Name of the parameter from the Review policy.

(dict) --
Name of the parameter from the Review policy.

Key (string) --
Name of the parameter from the list of Review Polices.

Values (list) --
The list of values of the Parameter

(string) --


MapEntries (list) --
List of ParameterMapEntry objects.

(dict) --
This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

Key (string) --
The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

Values (list) --
The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.

(string) --












HITReviewPolicy (dict) --
The name of the HIT-level Review Policy. This contains only the PolicyName element.

PolicyName (string) --
Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

Parameters (list) --
Name of the parameter from the Review policy.

(dict) --
Name of the parameter from the Review policy.

Key (string) --
Name of the parameter from the list of Review Polices.

Values (list) --
The list of values of the Parameter

(string) --


MapEntries (list) --
List of ParameterMapEntry objects.

(dict) --
This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

Key (string) --
The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

Values (list) --
The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.

(string) --












AssignmentReviewReport (dict) --
Contains both ReviewResult and ReviewAction elements for an Assignment.

ReviewResults (list) --
A list of ReviewResults objects for each action specified in the Review Policy.

(dict) --
This data structure is returned multiple times for each result specified in the Review Policy.

ActionId (string) --
A unique identifier of the Review action result.

SubjectId (string) --
The HITID or AssignmentId about which this result was taken. Note that HIT-level Review Policies will often emit results about both the HIT itself and its Assignments, while Assignment-level review policies generally only emit results about the Assignment itself.

SubjectType (string) --
The type of the object from the SubjectId field.

QuestionId (string) --
Specifies the QuestionId the result is describing. Depending on whether the TargetType is a HIT or Assignment this results could specify multiple values. If TargetType is HIT and QuestionId is absent, then the result describes results of the HIT, including the HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the result describes the Worker\'s performance on the HIT.

Key (string) --
Key identifies the particular piece of reviewed information.

Value (string) --
The values of Key provided by the review policies you have selected.





ReviewActions (list) --
A list of ReviewAction objects for each action specified in the Review Policy.

(dict) --
Both the AssignmentReviewReport and the HITReviewReport elements contains the ReviewActionDetail data structure. This structure is returned multiple times for each action specified in the Review Policy.

ActionId (string) --
The unique identifier for the action.

ActionName (string) --
The nature of the action itself. The Review Policy is responsible for examining the HIT and Assignments, emitting results, and deciding which other actions will be necessary.

TargetId (string) --
The specific HITId or AssignmentID targeted by the action.

TargetType (string) --
The type of object in TargetId.

Status (string) --
The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED.

CompleteTime (datetime) --
The date when the action was completed.

Result (string) --
A description of the outcome of the review.

ErrorCode (string) --
Present only when the Results have a FAILED Status.







HITReviewReport (dict) --
Contains both ReviewResult and ReviewAction elements for a particular HIT.

ReviewResults (list) --
A list of ReviewResults objects for each action specified in the Review Policy.

(dict) --
This data structure is returned multiple times for each result specified in the Review Policy.

ActionId (string) --
A unique identifier of the Review action result.

SubjectId (string) --
The HITID or AssignmentId about which this result was taken. Note that HIT-level Review Policies will often emit results about both the HIT itself and its Assignments, while Assignment-level review policies generally only emit results about the Assignment itself.

SubjectType (string) --
The type of the object from the SubjectId field.

QuestionId (string) --
Specifies the QuestionId the result is describing. Depending on whether the TargetType is a HIT or Assignment this results could specify multiple values. If TargetType is HIT and QuestionId is absent, then the result describes results of the HIT, including the HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the result describes the Worker\'s performance on the HIT.

Key (string) --
Key identifies the particular piece of reviewed information.

Value (string) --
The values of Key provided by the review policies you have selected.





ReviewActions (list) --
A list of ReviewAction objects for each action specified in the Review Policy.

(dict) --
Both the AssignmentReviewReport and the HITReviewReport elements contains the ReviewActionDetail data structure. This structure is returned multiple times for each action specified in the Review Policy.

ActionId (string) --
The unique identifier for the action.

ActionName (string) --
The nature of the action itself. The Review Policy is responsible for examining the HIT and Assignments, emitting results, and deciding which other actions will be necessary.

TargetId (string) --
The specific HITId or AssignmentID targeted by the action.

TargetType (string) --
The type of object in TargetId.

Status (string) --
The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED.

CompleteTime (datetime) --
The date when the action was completed.

Result (string) --
A description of the outcome of the review.

ErrorCode (string) --
Present only when the Results have a FAILED Status.







NextToken (string) --
If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.







Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'HITId': 'string',
        'AssignmentReviewPolicy': {
            'PolicyName': 'string',
            'Parameters': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ],
                    'MapEntries': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
            ]
        },
        'HITReviewPolicy': {
            'PolicyName': 'string',
            'Parameters': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ],
                    'MapEntries': [
                        {
                            'Key': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
            ]
        },
        'AssignmentReviewReport': {
            'ReviewResults': [
                {
                    'ActionId': 'string',
                    'SubjectId': 'string',
                    'SubjectType': 'string',
                    'QuestionId': 'string',
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'ReviewActions': [
                {
                    'ActionId': 'string',
                    'ActionName': 'string',
                    'TargetId': 'string',
                    'TargetType': 'string',
                    'Status': 'Intended'|'Succeeded'|'Failed'|'Cancelled',
                    'CompleteTime': datetime(2015, 1, 1),
                    'Result': 'string',
                    'ErrorCode': 'string'
                },
            ]
        },
        'HITReviewReport': {
            'ReviewResults': [
                {
                    'ActionId': 'string',
                    'SubjectId': 'string',
                    'SubjectType': 'string',
                    'QuestionId': 'string',
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'ReviewActions': [
                {
                    'ActionId': 'string',
                    'ActionName': 'string',
                    'TargetId': 'string',
                    'TargetType': 'string',
                    'Status': 'Intended'|'Succeeded'|'Failed'|'Cancelled',
                    'CompleteTime': datetime(2015, 1, 1),
                    'Result': 'string',
                    'ErrorCode': 'string'
                },
            ]
        },
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_reviewable_hits(HITTypeId=None, Status=None, NextToken=None, MaxResults=None):
    """
    The ListReviewableHITs operation retrieves the HITs with Status equal to Reviewable or Status equal to Reviewing that belong to the Requester calling the operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_reviewable_hits(
        HITTypeId='string',
        Status='Reviewable'|'Reviewing',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type HITTypeId: string
    :param HITTypeId: The ID of the HIT type of the HITs to consider for the query. If not specified, all HITs for the Reviewer are considered

    :type Status: string
    :param Status: Can be either Reviewable or Reviewing . Reviewable is the default value.

    :type NextToken: string
    :param NextToken: Pagination Token

    :type MaxResults: integer
    :param MaxResults: Limit the number of results returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'NumResults': 123,
    'HITs': [
        {
            'HITId': 'string',
            'HITTypeId': 'string',
            'HITGroupId': 'string',
            'HITLayoutId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Title': 'string',
            'Description': 'string',
            'Question': 'string',
            'Keywords': 'string',
            'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
            'MaxAssignments': 123,
            'Reward': 'string',
            'AutoApprovalDelayInSeconds': 123,
            'Expiration': datetime(2015, 1, 1),
            'AssignmentDurationInSeconds': 123,
            'RequesterAnnotation': 'string',
            'QualificationRequirements': [
                {
                    'QualificationTypeId': 'string',
                    'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                    'IntegerValues': [
                        123,
                    ],
                    'LocaleValues': [
                        {
                            'Country': 'string',
                            'Subdivision': 'string'
                        },
                    ],
                    'RequiredToPreview': True|False,
                    'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
                },
            ],
            'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
            'NumberOfAssignmentsPending': 123,
            'NumberOfAssignmentsAvailable': 123,
            'NumberOfAssignmentsCompleted': 123
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

NumResults (integer) --
The number of HITs on this page in the filtered results list, equivalent to the number of HITs being returned by this call.

HITs (list) --
The list of HIT elements returned by the query.

(dict) --
The HIT data structure represents a single HIT, including all the information necessary for a Worker to accept and complete the HIT.

HITId (string) --
A unique identifier for the HIT.

HITTypeId (string) --
The ID of the HIT type of this HIT

HITGroupId (string) --
The ID of the HIT Group of this HIT.

HITLayoutId (string) --
The ID of the HIT Layout of this HIT.

CreationTime (datetime) --
The date and time the HIT was created.

Title (string) --
The title of the HIT.

Description (string) --
A general description of the HIT.

Question (string) --
The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

Keywords (string) --
One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.

HITStatus (string) --
The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed.

MaxAssignments (integer) --
The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

Reward (string) --
A string representing a currency amount.

AutoApprovalDelayInSeconds (integer) --
The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid.

Expiration (datetime) --
The date and time the HIT expires.

AssignmentDurationInSeconds (integer) --
The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

RequesterAnnotation (string) --
An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.

QualificationRequirements (list) --
Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ActionsGuarded field on each QualificationRequirement structure.

(dict) --
The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results.

QualificationTypeId (string) --
The ID of the Qualification type for the requirement.

Comparator (string) --
The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value.

IntegerValues (list) --
The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.

(integer) --


LocaleValues (list) --
The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.

(dict) --
The Locale data structure represents a geographical region or location.

Country (string) --
The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision (string) --
The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.





RequiredToPreview (boolean) --
DEPRECATED: Use the ActionsGuarded field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ActionsGuarded field.

ActionsGuarded (string) --
Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include "Accept" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), "PreviewAndAccept" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and "DiscoverPreviewAndAccept" (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the RequiredToPreview field.





HITReviewStatus (string) --
Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.

NumberOfAssignmentsPending (integer) --
The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.

NumberOfAssignmentsAvailable (integer) --
The number of assignments for this HIT that are available for Workers to accept.

NumberOfAssignmentsCompleted (integer) --
The number of assignments for this HIT that have been approved or rejected.











Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'NextToken': 'string',
        'NumResults': 123,
        'HITs': [
            {
                'HITId': 'string',
                'HITTypeId': 'string',
                'HITGroupId': 'string',
                'HITLayoutId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'Title': 'string',
                'Description': 'string',
                'Question': 'string',
                'Keywords': 'string',
                'HITStatus': 'Assignable'|'Unassignable'|'Reviewable'|'Reviewing'|'Disposed',
                'MaxAssignments': 123,
                'Reward': 'string',
                'AutoApprovalDelayInSeconds': 123,
                'Expiration': datetime(2015, 1, 1),
                'AssignmentDurationInSeconds': 123,
                'RequesterAnnotation': 'string',
                'QualificationRequirements': [
                    {
                        'QualificationTypeId': 'string',
                        'Comparator': 'LessThan'|'LessThanOrEqualTo'|'GreaterThan'|'GreaterThanOrEqualTo'|'EqualTo'|'NotEqualTo'|'Exists'|'DoesNotExist'|'In'|'NotIn',
                        'IntegerValues': [
                            123,
                        ],
                        'LocaleValues': [
                            {
                                'Country': 'string',
                                'Subdivision': 'string'
                            },
                        ],
                        'RequiredToPreview': True|False,
                        'ActionsGuarded': 'Accept'|'PreviewAndAccept'|'DiscoverPreviewAndAccept'
                    },
                ],
                'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
                'NumberOfAssignmentsPending': 123,
                'NumberOfAssignmentsAvailable': 123,
                'NumberOfAssignmentsCompleted': 123
            },
        ]
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def list_worker_blocks(NextToken=None, MaxResults=None):
    """
    The ListWorkersBlocks operation retrieves a list of Workers who are blocked from working on your HITs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_worker_blocks(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token

    :type MaxResults: integer
    :param MaxResults: 

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'NumResults': 123,
    'WorkerBlocks': [
        {
            'WorkerId': 'string',
            'Reason': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

NumResults (integer) --
The number of assignments on the page in the filtered results list, equivalent to the number of assignments returned by this call.

WorkerBlocks (list) --
The list of WorkerBlocks, containing the collection of Worker IDs and reasons for blocking.

(dict) --
The WorkerBlock data structure represents a Worker who has been blocked. It has two elements: the WorkerId and the Reason for the block.

WorkerId (string) --
The ID of the Worker who accepted the HIT.

Reason (string) --
A message explaining the reason the Worker was blocked.











Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'NextToken': 'string',
        'NumResults': 123,
        'WorkerBlocks': [
            {
                'WorkerId': 'string',
                'Reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def list_workers_with_qualification_type(QualificationTypeId=None, Status=None, NextToken=None, MaxResults=None):
    """
    The ListWorkersWithQualificationType operation returns all of the Workers that have been associated with a given Qualification type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_workers_with_qualification_type(
        QualificationTypeId='string',
        Status='Granted'|'Revoked',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]\nThe ID of the Qualification type of the Qualifications to return.\n

    :type Status: string
    :param Status: The status of the Qualifications to return. Can be Granted | Revoked .

    :type NextToken: string
    :param NextToken: Pagination Token

    :type MaxResults: integer
    :param MaxResults: Limit the number of results returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'NumResults': 123,
    'Qualifications': [
        {
            'QualificationTypeId': 'string',
            'WorkerId': 'string',
            'GrantTime': datetime(2015, 1, 1),
            'IntegerValue': 123,
            'LocaleValue': {
                'Country': 'string',
                'Subdivision': 'string'
            },
            'Status': 'Granted'|'Revoked'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

NumResults (integer) --
The number of Qualifications on this page in the filtered results list, equivalent to the number of Qualifications being returned by this call.

Qualifications (list) --
The list of Qualification elements returned by this call.

(dict) --
The Qualification data structure represents a Qualification assigned to a user, including the Qualification type and the value (score).

QualificationTypeId (string) --
The ID of the Qualification type for the Qualification.

WorkerId (string) --
The ID of the Worker who possesses the Qualification.

GrantTime (datetime) --
The date and time the Qualification was granted to the Worker. If the Worker\'s Qualification was revoked, and then re-granted based on a new Qualification request, GrantTime is the date and time of the last call to the AcceptQualificationRequest operation.

IntegerValue (integer) --
The value (score) of the Qualification, if the Qualification has an integer value.

LocaleValue (dict) --
The Locale data structure represents a geographical region or location.

Country (string) --
The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision (string) --
The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.



Status (string) --
The status of the Qualification. Valid values are Granted | Revoked.











Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'NextToken': 'string',
        'NumResults': 123,
        'Qualifications': [
            {
                'QualificationTypeId': 'string',
                'WorkerId': 'string',
                'GrantTime': datetime(2015, 1, 1),
                'IntegerValue': 123,
                'LocaleValue': {
                    'Country': 'string',
                    'Subdivision': 'string'
                },
                'Status': 'Granted'|'Revoked'
            },
        ]
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def notify_workers(Subject=None, MessageText=None, WorkerIds=None):
    """
    The NotifyWorkers operation sends an email to one or more Workers that you specify with the Worker ID. You can specify up to 100 Worker IDs to send the same message with a single call to the NotifyWorkers operation. The NotifyWorkers operation will send a notification email to a Worker only if you have previously approved or rejected work from the Worker.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.notify_workers(
        Subject='string',
        MessageText='string',
        WorkerIds=[
            'string',
        ]
    )
    
    
    :type Subject: string
    :param Subject: [REQUIRED]\nThe subject line of the email message to send. Can include up to 200 characters.\n

    :type MessageText: string
    :param MessageText: [REQUIRED]\nThe text of the email message to send. Can include up to 4,096 characters\n

    :type WorkerIds: list
    :param WorkerIds: [REQUIRED]\nA list of Worker IDs you wish to notify. You can notify upto 100 Workers at a time.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'NotifyWorkersFailureStatuses': [
        {
            'NotifyWorkersFailureCode': 'SoftFailure'|'HardFailure',
            'NotifyWorkersFailureMessage': 'string',
            'WorkerId': 'string'
        },
    ]
}


Response Structure

(dict) --

NotifyWorkersFailureStatuses (list) --
When MTurk sends notifications to the list of Workers, it returns back any failures it encounters in this list of NotifyWorkersFailureStatus objects.

(dict) --
When MTurk encounters an issue with notifying the Workers you specified, it returns back this object with failure details.

NotifyWorkersFailureCode (string) --
Encoded value for the failure type.

NotifyWorkersFailureMessage (string) --
A message detailing the reason the Worker could not be notified.

WorkerId (string) --
The ID of the Worker.











Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'NotifyWorkersFailureStatuses': [
            {
                'NotifyWorkersFailureCode': 'SoftFailure'|'HardFailure',
                'NotifyWorkersFailureMessage': 'string',
                'WorkerId': 'string'
            },
        ]
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

def reject_assignment(AssignmentId=None, RequesterFeedback=None):
    """
    The RejectAssignment operation rejects the results of a completed assignment.
    You can include an optional feedback message with the rejection, which the Worker can see in the Status section of the web site. When you include a feedback message with the rejection, it helps the Worker understand why the assignment was rejected, and can improve the quality of the results the Worker submits in the future.
    Only the Requester who created the HIT can reject an assignment for the HIT.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reject_assignment(
        AssignmentId='string',
        RequesterFeedback='string'
    )
    
    
    :type AssignmentId: string
    :param AssignmentId: [REQUIRED]\nThe ID of the assignment. The assignment must correspond to a HIT created by the Requester.\n

    :type RequesterFeedback: string
    :param RequesterFeedback: [REQUIRED]\nA message for the Worker, which the Worker can see in the Status section of the web site.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reject_qualification_request(QualificationRequestId=None, Reason=None):
    """
    The RejectQualificationRequest operation rejects a user\'s request for a Qualification.
    You can provide a text message explaining why the request was rejected. The Worker who made the request can see this message.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reject_qualification_request(
        QualificationRequestId='string',
        Reason='string'
    )
    
    
    :type QualificationRequestId: string
    :param QualificationRequestId: [REQUIRED]\nThe ID of the Qualification request, as returned by the ListQualificationRequests operation.\n

    :type Reason: string
    :param Reason: A text message explaining why the request was rejected, to be shown to the Worker who made the request.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def send_bonus(WorkerId=None, BonusAmount=None, AssignmentId=None, Reason=None, UniqueRequestToken=None):
    """
    The SendBonus operation issues a payment of money from your account to a Worker. This payment happens separately from the reward you pay to the Worker when you approve the Worker\'s assignment. The SendBonus operation requires the Worker\'s ID and the assignment ID as parameters to initiate payment of the bonus. You must include a message that explains the reason for the bonus payment, as the Worker may not be expecting the payment. Amazon Mechanical Turk collects a fee for bonus payments, similar to the HIT listing fee. This operation fails if your account does not have enough funds to pay for both the bonus and the fees.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_bonus(
        WorkerId='string',
        BonusAmount='string',
        AssignmentId='string',
        Reason='string',
        UniqueRequestToken='string'
    )
    
    
    :type WorkerId: string
    :param WorkerId: [REQUIRED]\nThe ID of the Worker being paid the bonus.\n

    :type BonusAmount: string
    :param BonusAmount: [REQUIRED]\nThe Bonus amount is a US Dollar amount specified using a string (for example, '5' represents $5.00 USD and '101.42' represents $101.42 USD). Do not include currency symbols or currency codes.\n

    :type AssignmentId: string
    :param AssignmentId: [REQUIRED]\nThe ID of the assignment for which this bonus is paid.\n

    :type Reason: string
    :param Reason: [REQUIRED]\nA message that explains the reason for the bonus payment. The Worker receiving the bonus can see this message.\n

    :type UniqueRequestToken: string
    :param UniqueRequestToken: A unique identifier for this request, which allows you to retry the call on error without granting multiple bonuses. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the bonus already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return an error with a message containing the request ID.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def send_test_event_notification(Notification=None, TestEventType=None):
    """
    The SendTestEventNotification operation causes Amazon Mechanical Turk to send a notification message as if a HIT event occurred, according to the provided notification specification. This allows you to test notifications without setting up notifications for a real HIT type and trying to trigger them using the website. When you call this operation, the service attempts to send the test notification immediately.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_test_event_notification(
        Notification={
            'Destination': 'string',
            'Transport': 'Email'|'SQS'|'SNS',
            'Version': 'string',
            'EventTypes': [
                'AssignmentAccepted'|'AssignmentAbandoned'|'AssignmentReturned'|'AssignmentSubmitted'|'AssignmentRejected'|'AssignmentApproved'|'HITCreated'|'HITExpired'|'HITReviewable'|'HITExtended'|'HITDisposed'|'Ping',
            ]
        },
        TestEventType='AssignmentAccepted'|'AssignmentAbandoned'|'AssignmentReturned'|'AssignmentSubmitted'|'AssignmentRejected'|'AssignmentApproved'|'HITCreated'|'HITExpired'|'HITReviewable'|'HITExtended'|'HITDisposed'|'Ping'
    )
    
    
    :type Notification: dict
    :param Notification: [REQUIRED]\nThe notification specification to test. This value is identical to the value you would provide to the UpdateNotificationSettings operation when you establish the notification specification for a HIT type.\n\nDestination (string) -- [REQUIRED]The target for notification messages. The Destination\xe2\x80\x99s format is determined by the specified Transport:\n\nWhen Transport is Email, the Destination is your email address.\nWhen Transport is SQS, the Destination is your queue URL.\nWhen Transport is SNS, the Destination is the ARN of your topic.\n\n\nTransport (string) -- [REQUIRED]The method Amazon Mechanical Turk uses to send the notification. Valid Values: Email | SQS | SNS.\n\nVersion (string) -- [REQUIRED]The version of the Notification API to use. Valid value is 2006-05-05.\n\nEventTypes (list) -- [REQUIRED]The list of events that should cause notifications to be sent. Valid Values: AssignmentAccepted | AssignmentAbandoned | AssignmentReturned | AssignmentSubmitted | AssignmentRejected | AssignmentApproved | HITCreated | HITExtended | HITDisposed | HITReviewable | HITExpired | Ping. The Ping event is only valid for the SendTestEventNotification operation.\n\n(string) --\n\n\n\n

    :type TestEventType: string
    :param TestEventType: [REQUIRED]\nThe event to simulate to test the notification specification. This event is included in the test message even if the notification specification does not include the event type. The notification specification does not filter out the test event.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_expiration_for_hit(HITId=None, ExpireAt=None):
    """
    The UpdateExpirationForHIT operation allows you update the expiration time of a HIT. If you update it to a time in the past, the HIT will be immediately expired.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_expiration_for_hit(
        HITId='string',
        ExpireAt=datetime(2015, 1, 1)
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]\nThe HIT to update.\n

    :type ExpireAt: datetime
    :param ExpireAt: [REQUIRED]\nThe date and time at which you want the HIT to expire\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_hit_review_status(HITId=None, Revert=None):
    """
    The UpdateHITReviewStatus operation updates the status of a HIT. If the status is Reviewable, this operation can update the status to Reviewing, or it can revert a Reviewing HIT back to the Reviewable status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_hit_review_status(
        HITId='string',
        Revert=True|False
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]\nThe ID of the HIT to update.\n

    :type Revert: boolean
    :param Revert: Specifies how to update the HIT status. Default is False .\n\nSetting this to false will only transition a HIT from Reviewable to Reviewing\nSetting this to true will only transition a HIT from Reviewing to Reviewable\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_hit_type_of_hit(HITId=None, HITTypeId=None):
    """
    The UpdateHITTypeOfHIT operation allows you to change the HITType properties of a HIT. This operation disassociates the HIT from its old HITType properties and associates it with the new HITType properties. The HIT takes on the properties of the new HITType in place of the old ones.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_hit_type_of_hit(
        HITId='string',
        HITTypeId='string'
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]\nThe HIT to update.\n

    :type HITTypeId: string
    :param HITTypeId: [REQUIRED]\nThe ID of the new HIT type.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_notification_settings(HITTypeId=None, Notification=None, Active=None):
    """
    The UpdateNotificationSettings operation creates, updates, disables or re-enables notifications for a HIT type. If you call the UpdateNotificationSettings operation for a HIT type that already has a notification specification, the operation replaces the old specification with a new one. You can call the UpdateNotificationSettings operation to enable or disable notifications for the HIT type, without having to modify the notification specification itself by providing updates to the Active status without specifying a new notification specification. To change the Active status of a HIT type\'s notifications, the HIT type must already have a notification specification, or one must be provided in the same call to UpdateNotificationSettings .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_notification_settings(
        HITTypeId='string',
        Notification={
            'Destination': 'string',
            'Transport': 'Email'|'SQS'|'SNS',
            'Version': 'string',
            'EventTypes': [
                'AssignmentAccepted'|'AssignmentAbandoned'|'AssignmentReturned'|'AssignmentSubmitted'|'AssignmentRejected'|'AssignmentApproved'|'HITCreated'|'HITExpired'|'HITReviewable'|'HITExtended'|'HITDisposed'|'Ping',
            ]
        },
        Active=True|False
    )
    
    
    :type HITTypeId: string
    :param HITTypeId: [REQUIRED]\nThe ID of the HIT type whose notification specification is being updated.\n

    :type Notification: dict
    :param Notification: The notification specification for the HIT type.\n\nDestination (string) -- [REQUIRED]The target for notification messages. The Destination\xe2\x80\x99s format is determined by the specified Transport:\n\nWhen Transport is Email, the Destination is your email address.\nWhen Transport is SQS, the Destination is your queue URL.\nWhen Transport is SNS, the Destination is the ARN of your topic.\n\n\nTransport (string) -- [REQUIRED]The method Amazon Mechanical Turk uses to send the notification. Valid Values: Email | SQS | SNS.\n\nVersion (string) -- [REQUIRED]The version of the Notification API to use. Valid value is 2006-05-05.\n\nEventTypes (list) -- [REQUIRED]The list of events that should cause notifications to be sent. Valid Values: AssignmentAccepted | AssignmentAbandoned | AssignmentReturned | AssignmentSubmitted | AssignmentRejected | AssignmentApproved | HITCreated | HITExtended | HITDisposed | HITReviewable | HITExpired | Ping. The Ping event is only valid for the SendTestEventNotification operation.\n\n(string) --\n\n\n\n

    :type Active: boolean
    :param Active: Specifies whether notifications are sent for HITs of this HIT type, according to the notification specification. You must specify either the Notification parameter or the Active parameter for the call to UpdateNotificationSettings to succeed.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_qualification_type(QualificationTypeId=None, Description=None, QualificationTypeStatus=None, Test=None, AnswerKey=None, TestDurationInSeconds=None, RetryDelayInSeconds=None, AutoGranted=None, AutoGrantedValue=None):
    """
    The UpdateQualificationType operation modifies the attributes of an existing Qualification type, which is represented by a QualificationType data structure. Only the owner of a Qualification type can modify its attributes.
    Most attributes of a Qualification type can be changed after the type has been created. However, the Name and Keywords fields cannot be modified. The RetryDelayInSeconds parameter can be modified or added to change the delay or to enable retries, but RetryDelayInSeconds cannot be used to disable retries.
    You can use this operation to update the test for a Qualification type. The test is updated based on the values specified for the Test, TestDurationInSeconds and AnswerKey parameters. All three parameters specify the updated test. If you are updating the test for a type, you must specify the Test and TestDurationInSeconds parameters. The AnswerKey parameter is optional; omitting it specifies that the updated test does not have an answer key.
    If you omit the Test parameter, the test for the Qualification type is unchanged. There is no way to remove a test from a Qualification type that has one. If the type already has a test, you cannot update it to be AutoGranted. If the Qualification type does not have a test and one is provided by an update, the type will henceforth have a test.
    If you want to update the test duration or answer key for an existing test without changing the questions, you must specify a Test parameter with the original questions, along with the updated values.
    If you provide an updated Test but no AnswerKey, the new test will not have an answer key. Requests for such Qualifications must be granted manually.
    You can also update the AutoGranted and AutoGrantedValue attributes of the Qualification type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_qualification_type(
        QualificationTypeId='string',
        Description='string',
        QualificationTypeStatus='Active'|'Inactive',
        Test='string',
        AnswerKey='string',
        TestDurationInSeconds=123,
        RetryDelayInSeconds=123,
        AutoGranted=True|False,
        AutoGrantedValue=123
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]\nThe ID of the Qualification type to update.\n

    :type Description: string
    :param Description: The new description of the Qualification type.

    :type QualificationTypeStatus: string
    :param QualificationTypeStatus: The new status of the Qualification type - Active | Inactive

    :type Test: string
    :param Test: The questions for the Qualification test a Worker must answer correctly to obtain a Qualification of this type. If this parameter is specified, TestDurationInSeconds must also be specified.\nConstraints: Must not be longer than 65535 bytes. Must be a QuestionForm data structure. This parameter cannot be specified if AutoGranted is true.\nConstraints: None. If not specified, the Worker may request the Qualification without answering any questions.\n

    :type AnswerKey: string
    :param AnswerKey: The answers to the Qualification test specified in the Test parameter, in the form of an AnswerKey data structure.

    :type TestDurationInSeconds: integer
    :param TestDurationInSeconds: The number of seconds the Worker has to complete the Qualification test, starting from the time the Worker requests the Qualification.

    :type RetryDelayInSeconds: integer
    :param RetryDelayInSeconds: The amount of time, in seconds, that Workers must wait after requesting a Qualification of the specified Qualification type before they can retry the Qualification request. It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must dispose of the existing retry-enabled Qualification type using DisposeQualificationType and then create a new Qualification type with retries disabled using CreateQualificationType.

    :type AutoGranted: boolean
    :param AutoGranted: Specifies whether requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test.\nConstraints: If the Test parameter is specified, this parameter cannot be true.\n

    :type AutoGrantedValue: integer
    :param AutoGrantedValue: The Qualification value to use for automatically granted Qualifications. This parameter is used only if the AutoGranted parameter is true.

    :rtype: dict

ReturnsResponse Syntax
{
    'QualificationType': {
        'QualificationTypeId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'Name': 'string',
        'Description': 'string',
        'Keywords': 'string',
        'QualificationTypeStatus': 'Active'|'Inactive',
        'Test': 'string',
        'TestDurationInSeconds': 123,
        'AnswerKey': 'string',
        'RetryDelayInSeconds': 123,
        'IsRequestable': True|False,
        'AutoGranted': True|False,
        'AutoGrantedValue': 123
    }
}


Response Structure

(dict) --

QualificationType (dict) --
Contains a QualificationType data structure.

QualificationTypeId (string) --
A unique identifier for the Qualification type. A Qualification type is given a Qualification type ID when you call the CreateQualificationType operation.

CreationTime (datetime) --
The date and time the Qualification type was created.

Name (string) --
The name of the Qualification type. The type name is used to identify the type, and to find the type using a Qualification type search.

Description (string) --
A long description for the Qualification type.

Keywords (string) --
One or more words or phrases that describe theQualification type, separated by commas. The Keywords make the type easier to find using a search.

QualificationTypeStatus (string) --
The status of the Qualification type. A Qualification type\'s status determines if users can apply to receive a Qualification of this type, and if HITs can be created with requirements based on this type. Valid values are Active | Inactive.

Test (string) --
The questions for a Qualification test associated with this Qualification type that a user can take to obtain a Qualification of this type. This parameter must be specified if AnswerKey is present. A Qualification type cannot have both a specified Test parameter and an AutoGranted value of true.

TestDurationInSeconds (integer) --
The amount of time, in seconds, given to a Worker to complete the Qualification test, beginning from the time the Worker requests the Qualification.

AnswerKey (string) --
The answers to the Qualification test specified in the Test parameter.

RetryDelayInSeconds (integer) --
The amount of time, in seconds, Workers must wait after taking the Qualification test before they can take it again. Workers can take a Qualification test multiple times if they were not granted the Qualification from a previous attempt, or if the test offers a gradient score and they want a better score. If not specified, retries are disabled and Workers can request a Qualification only once.

IsRequestable (boolean) --
Specifies whether the Qualification type is one that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is False for Qualifications assigned automatically by the system. Valid values are True | False.

AutoGranted (boolean) --
Specifies that requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test. Valid values are True | False.

AutoGrantedValue (integer) --
The Qualification integer value to use for automatically granted Qualifications, if AutoGranted is true. This is 1 by default.









Exceptions

MTurk.Client.exceptions.ServiceFault
MTurk.Client.exceptions.RequestError


    :return: {
        'QualificationType': {
            'QualificationTypeId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'Name': 'string',
            'Description': 'string',
            'Keywords': 'string',
            'QualificationTypeStatus': 'Active'|'Inactive',
            'Test': 'string',
            'TestDurationInSeconds': 123,
            'AnswerKey': 'string',
            'RetryDelayInSeconds': 123,
            'IsRequestable': True|False,
            'AutoGranted': True|False,
            'AutoGrantedValue': 123
        }
    }
    
    
    :returns: 
    MTurk.Client.exceptions.ServiceFault
    MTurk.Client.exceptions.RequestError
    
    """
    pass

