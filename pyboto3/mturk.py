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
    The AcceptQualificationRequest operation approves a Worker's request for a Qualification.
    Only the owner of the Qualification type can grant a Qualification request for that type.
    A successful request for the AcceptQualificationRequest operation returns with no errors and an empty body.
    See also: AWS API Documentation
    
    
    :example: response = client.accept_qualification_request(
        QualificationRequestId='string',
        IntegerValue=123
    )
    
    
    :type QualificationRequestId: string
    :param QualificationRequestId: [REQUIRED]
            The ID of the Qualification request, as returned by the GetQualificationRequests operation.
            

    :type IntegerValue: integer
    :param IntegerValue: The value of the Qualification. You can omit this value if you are using the presence or absence of the Qualification as the basis for a HIT requirement.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def approve_assignment(AssignmentId=None, RequesterFeedback=None, OverrideRejection=None):
    """
    The ApproveAssignment operation approves the results of a completed assignment.
    Approving an assignment initiates two payments from the Requester's Amazon.com account
    If the Requester's account does not have adequate funds for these payments, the call to ApproveAssignment returns an exception, and the approval is not processed. You can include an optional feedback message with the approval, which the Worker can see in the Status section of the web site.
    You can also call this operation for assignments that were previous rejected and approve them by explicitly overriding the previous rejection. This only works on rejected assignments that were submitted within the previous 30 days and only if the assignment's related HIT has not been deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.approve_assignment(
        AssignmentId='string',
        RequesterFeedback='string',
        OverrideRejection=True|False
    )
    
    
    :type AssignmentId: string
    :param AssignmentId: [REQUIRED]
            The ID of the assignment. The assignment must correspond to a HIT created by the Requester.
            

    :type RequesterFeedback: string
    :param RequesterFeedback: A message for the Worker, which the Worker can see in the Status section of the web site.

    :type OverrideRejection: boolean
    :param OverrideRejection: A flag indicating that an assignment should be approved even if it was previously rejected. Defaults to False .

    :rtype: dict
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
    
    
    :example: response = client.associate_qualification_with_worker(
        QualificationTypeId='string',
        WorkerId='string',
        IntegerValue=123,
        SendNotification=True|False
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]
            The ID of the Qualification type to use for the assigned Qualification.
            

    :type WorkerId: string
    :param WorkerId: [REQUIRED]
            The ID of the Worker to whom the Qualification is being assigned. Worker IDs are included with submitted HIT assignments and Qualification requests.
            

    :type IntegerValue: integer
    :param IntegerValue: The value of the Qualification to assign.

    :type SendNotification: boolean
    :param SendNotification: Specifies whether to send a notification email message to the Worker saying that the qualification was assigned to the Worker. Note: this is true by default.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def create_additional_assignments_for_hit(HITId=None, NumberOfAdditionalAssignments=None, UniqueRequestToken=None):
    """
    The CreateAdditionalAssignmentsForHIT operation increases the maximum number of assignments of an existing HIT.
    To extend the maximum number of assignments, specify the number of additional assignments.
    See also: AWS API Documentation
    
    
    :example: response = client.create_additional_assignments_for_hit(
        HITId='string',
        NumberOfAdditionalAssignments=123,
        UniqueRequestToken='string'
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]
            The ID of the HIT to extend.
            

    :type NumberOfAdditionalAssignments: integer
    :param NumberOfAdditionalAssignments: The number of additional assignments to request for this HIT.

    :type UniqueRequestToken: string
    :param UniqueRequestToken: A unique identifier for this request, which allows you to retry the call on error without extending the HIT multiple times. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the extend HIT already exists in the system from a previous call using the same UniqueRequestToken , subsequent calls will return an error with a message containing the request ID.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    HITId (string) -- [REQUIRED]
    The ID of the HIT to extend.
    
    NumberOfAdditionalAssignments (integer) -- The number of additional assignments to request for this HIT.
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
                'RequiredToPreview': True|False
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
    :param LifetimeInSeconds: [REQUIRED]
            An amount of time, in seconds, after which the HIT is no longer available for users to accept. After the lifetime of the HIT elapses, the HIT no longer appears in HIT searches, even if not all of the assignments for the HIT have been accepted.
            

    :type AssignmentDurationInSeconds: integer
    :param AssignmentDurationInSeconds: [REQUIRED]
            The amount of time, in seconds, that a Worker has to complete the HIT after accepting it. If a Worker does not complete the assignment within the specified duration, the assignment is considered abandoned. If the HIT is still active (that is, its lifetime has not elapsed), the assignment becomes available for other users to find and accept.
            

    :type Reward: string
    :param Reward: [REQUIRED]
            The amount of money the Requester will pay a Worker for successfully completing the HIT.
            

    :type Title: string
    :param Title: [REQUIRED]
            The title of the HIT. A title should be short and descriptive about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT title appears in search results, and everywhere the HIT is mentioned.
            

    :type Keywords: string
    :param Keywords: One or more words or phrases that describe the HIT, separated by commas. These words are used in searches to find HITs.

    :type Description: string
    :param Description: [REQUIRED]
            A general description of the HIT. A description includes detailed information about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT description appears in the expanded view of search results, and in the HIT and assignment screens. A good description gives the user enough information to evaluate the HIT before accepting it.
            

    :type Question: string
    :param Question: The data the person completing the HIT uses to produce the results.
            Constraints: Must be a QuestionForm data structure, an ExternalQuestion data structure, or an HTMLQuestion data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace.
            Either a Question parameter or a HITLayoutId parameter must be provided.
            

    :type RequesterAnnotation: string
    :param RequesterAnnotation: An arbitrary data field. The RequesterAnnotation parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, this parameter could be an identifier internal to the Requester's application that corresponds with the HIT.
            The RequesterAnnotation parameter for a HIT is only visible to the Requester who created the HIT. It is not shown to the Worker, or any other Requester.
            The RequesterAnnotation parameter may be different for each HIT you submit. It does not affect how your HITs are grouped.
            

    :type QualificationRequirements: list
    :param QualificationRequirements: A condition that a Worker's Qualifications must meet before the Worker is allowed to accept and complete the HIT.
            (dict) --The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT.
            QualificationTypeId (string) -- [REQUIRED]The ID of the Qualification type for the requirement.
            Comparator (string) -- [REQUIRED]The kind of comparison to make against a Qualification's value. You can compare a Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user's profile, regardless of its value.
            IntegerValues (list) --The integer value to compare against the Qualification's value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.
            (integer) --
            LocaleValues (list) --The locale value to compare against the Qualification's value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.
            (dict) --The Locale data structure represents a geographical region or location.
            Country (string) -- [REQUIRED]The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.
            Subdivision (string) --The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.
            
            RequiredToPreview (boolean) --If true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT's question data, but will not be allowed to accept and complete the HIT. The default is false.
            
            

    :type UniqueRequestToken: string
    :param UniqueRequestToken: A unique identifier for this request which allows you to retry the call on error without creating duplicate HITs. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the HIT already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return a AWS.MechanicalTurk.HitAlreadyExists error with a message containing the HITId.
            Note
            Note: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same UniqueRequestToken made after the 24 hour limit could create duplicate HITs.
            

    :type AssignmentReviewPolicy: dict
    :param AssignmentReviewPolicy: The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for Mechanical Turk to take various actions based on the policy.
            PolicyName (string) --Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01
            Parameters (list) --Name of the parameter from the Review policy.
            (dict) --Name of the parameter from the Review policy.
            Key (string) --Name of the parameter from the list of Review Polices.
            Values (list) --The list of values of the Parameter
            (string) --
            MapEntries (list) --List of ParameterMapEntry objects.
            (dict) --This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.
            Key (string) --The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.
            Values (list) --The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.
            (string) --
            
            
            

    :type HITReviewPolicy: dict
    :param HITReviewPolicy: The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take various actions based on the policy.
            PolicyName (string) --Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01
            Parameters (list) --Name of the parameter from the Review policy.
            (dict) --Name of the parameter from the Review policy.
            Key (string) --Name of the parameter from the list of Review Polices.
            Values (list) --The list of values of the Parameter
            (string) --
            MapEntries (list) --List of ParameterMapEntry objects.
            (dict) --This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.
            Key (string) --The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.
            Values (list) --The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.
            (string) --
            
            
            

    :type HITLayoutId: string
    :param HITLayoutId: The HITLayoutId allows you to use a pre-existing HIT design with placeholder values and create an additional HIT by providing those values as HITLayoutParameters.
            Constraints: Either a Question parameter or a HITLayoutId parameter must be provided.
            

    :type HITLayoutParameters: list
    :param HITLayoutParameters: If the HITLayoutId is provided, any placeholder values must be filled in with values using the HITLayoutParameter structure. For more information, see HITLayout.
            (dict) --The HITLayoutParameter data structure defines parameter values used with a HITLayout. A HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human Intelligence Task (HIT) question data for CreateHIT.
            Name (string) --The name of the parameter in the HITLayout.
            Value (string) --The value substituted for the parameter referenced in the HITLayout.
            
            

    :rtype: dict
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
                    'RequiredToPreview': True|False
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
                'RequiredToPreview': True|False
            },
        ]
    )
    
    
    :type AutoApprovalDelayInSeconds: integer
    :param AutoApprovalDelayInSeconds: The number of seconds after an assignment for the HIT has been submitted, after which the assignment is considered Approved automatically unless the Requester explicitly rejects it.

    :type AssignmentDurationInSeconds: integer
    :param AssignmentDurationInSeconds: [REQUIRED]
            The amount of time, in seconds, that a Worker has to complete the HIT after accepting it. If a Worker does not complete the assignment within the specified duration, the assignment is considered abandoned. If the HIT is still active (that is, its lifetime has not elapsed), the assignment becomes available for other users to find and accept.
            

    :type Reward: string
    :param Reward: [REQUIRED]
            The amount of money the Requester will pay a Worker for successfully completing the HIT.
            

    :type Title: string
    :param Title: [REQUIRED]
            The title of the HIT. A title should be short and descriptive about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT title appears in search results, and everywhere the HIT is mentioned.
            

    :type Keywords: string
    :param Keywords: One or more words or phrases that describe the HIT, separated by commas. These words are used in searches to find HITs.

    :type Description: string
    :param Description: [REQUIRED]
            A general description of the HIT. A description includes detailed information about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT description appears in the expanded view of search results, and in the HIT and assignment screens. A good description gives the user enough information to evaluate the HIT before accepting it.
            

    :type QualificationRequirements: list
    :param QualificationRequirements: A condition that a Worker's Qualifications must meet before the Worker is allowed to accept and complete the HIT.
            (dict) --The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT.
            QualificationTypeId (string) -- [REQUIRED]The ID of the Qualification type for the requirement.
            Comparator (string) -- [REQUIRED]The kind of comparison to make against a Qualification's value. You can compare a Qualification's value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user's profile, regardless of its value.
            IntegerValues (list) --The integer value to compare against the Qualification's value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.
            (integer) --
            LocaleValues (list) --The locale value to compare against the Qualification's value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.
            (dict) --The Locale data structure represents a geographical region or location.
            Country (string) -- [REQUIRED]The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.
            Subdivision (string) --The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.
            
            RequiredToPreview (boolean) --If true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT's question data, but will not be allowed to accept and complete the HIT. The default is false.
            
            

    :rtype: dict
    :return: {
        'HITTypeId': 'string'
    }
    
    
    """
    pass

def create_hit_with_hit_type(HITTypeId=None, MaxAssignments=None, LifetimeInSeconds=None, Question=None, RequesterAnnotation=None, UniqueRequestToken=None, AssignmentReviewPolicy=None, HITReviewPolicy=None, HITLayoutId=None, HITLayoutParameters=None):
    """
    The CreateHITWithHITType operation creates a new Human Intelligence Task (HIT) using an existing HITTypeID generated by the CreateHITType operation.
    This is an alternative way to create HITs from the CreateHIT operation. This is the recommended best practice for Requesters who are creating large numbers of HITs.
    CreateHITWithHITType also supports several ways to provide question data: by providing a value for the Question parameter that fully specifies the contents of the HIT, or by providing a HitLayoutId and associated HitLayoutParameters .
    See also: AWS API Documentation
    
    
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
    :param HITTypeId: [REQUIRED]
            The HIT type ID you want to create this HIT with.
            

    :type MaxAssignments: integer
    :param MaxAssignments: The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

    :type LifetimeInSeconds: integer
    :param LifetimeInSeconds: [REQUIRED]
            An amount of time, in seconds, after which the HIT is no longer available for users to accept. After the lifetime of the HIT elapses, the HIT no longer appears in HIT searches, even if not all of the assignments for the HIT have been accepted.
            

    :type Question: string
    :param Question: The data the person completing the HIT uses to produce the results.
            Constraints: Must be a QuestionForm data structure, an ExternalQuestion data structure, or an HTMLQuestion data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace.
            Either a Question parameter or a HITLayoutId parameter must be provided.
            

    :type RequesterAnnotation: string
    :param RequesterAnnotation: An arbitrary data field. The RequesterAnnotation parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, this parameter could be an identifier internal to the Requester's application that corresponds with the HIT.
            The RequesterAnnotation parameter for a HIT is only visible to the Requester who created the HIT. It is not shown to the Worker, or any other Requester.
            The RequesterAnnotation parameter may be different for each HIT you submit. It does not affect how your HITs are grouped.
            

    :type UniqueRequestToken: string
    :param UniqueRequestToken: A unique identifier for this request which allows you to retry the call on error without creating duplicate HITs. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the HIT already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return a AWS.MechanicalTurk.HitAlreadyExists error with a message containing the HITId.
            Note
            Note: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same UniqueRequestToken made after the 24 hour limit could create duplicate HITs.
            

    :type AssignmentReviewPolicy: dict
    :param AssignmentReviewPolicy: The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for Mechanical Turk to take various actions based on the policy.
            PolicyName (string) --Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01
            Parameters (list) --Name of the parameter from the Review policy.
            (dict) --Name of the parameter from the Review policy.
            Key (string) --Name of the parameter from the list of Review Polices.
            Values (list) --The list of values of the Parameter
            (string) --
            MapEntries (list) --List of ParameterMapEntry objects.
            (dict) --This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.
            Key (string) --The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.
            Values (list) --The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.
            (string) --
            
            
            

    :type HITReviewPolicy: dict
    :param HITReviewPolicy: The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take various actions based on the policy.
            PolicyName (string) --Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01
            Parameters (list) --Name of the parameter from the Review policy.
            (dict) --Name of the parameter from the Review policy.
            Key (string) --Name of the parameter from the list of Review Polices.
            Values (list) --The list of values of the Parameter
            (string) --
            MapEntries (list) --List of ParameterMapEntry objects.
            (dict) --This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.
            Key (string) --The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.
            Values (list) --The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.
            (string) --
            
            
            

    :type HITLayoutId: string
    :param HITLayoutId: The HITLayoutId allows you to use a pre-existing HIT design with placeholder values and create an additional HIT by providing those values as HITLayoutParameters.
            Constraints: Either a Question parameter or a HITLayoutId parameter must be provided.
            

    :type HITLayoutParameters: list
    :param HITLayoutParameters: If the HITLayoutId is provided, any placeholder values must be filled in with values using the HITLayoutParameter structure. For more information, see HITLayout.
            (dict) --The HITLayoutParameter data structure defines parameter values used with a HITLayout. A HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human Intelligence Task (HIT) question data for CreateHIT.
            Name (string) --The name of the parameter in the HITLayout.
            Value (string) --The value substituted for the parameter referenced in the HITLayout.
            
            

    :rtype: dict
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
                    'RequiredToPreview': True|False
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
    :param Name: [REQUIRED]
            The name you give to the Qualification type. The type name is used to represent the Qualification to Workers, and to find the type using a Qualification type search. It must be unique across all of your Qualification types.
            

    :type Keywords: string
    :param Keywords: One or more words or phrases that describe the Qualification type, separated by commas. The keywords of a type make the type easier to find during a search.

    :type Description: string
    :param Description: [REQUIRED]
            A long description for the Qualification type. On the Amazon Mechanical Turk website, the long description is displayed when a Worker examines a Qualification type.
            

    :type QualificationTypeStatus: string
    :param QualificationTypeStatus: [REQUIRED]
            The initial status of the Qualification type.
            Constraints: Valid values are: Active | Inactive
            

    :type RetryDelayInSeconds: integer
    :param RetryDelayInSeconds: The number of seconds that a Worker must wait after requesting a Qualification of the Qualification type before the worker can retry the Qualification request.
            Constraints: None. If not specified, retries are disabled and Workers can request a Qualification of this type only once, even if the Worker has not been granted the Qualification. It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must delete existing retry-enabled Qualification type and then create a new Qualification type with retries disabled.
            

    :type Test: string
    :param Test: The questions for the Qualification test a Worker must answer correctly to obtain a Qualification of this type. If this parameter is specified, TestDurationInSeconds must also be specified.
            Constraints: Must not be longer than 65535 bytes. Must be a QuestionForm data structure. This parameter cannot be specified if AutoGranted is true.
            Constraints: None. If not specified, the Worker may request the Qualification without answering any questions.
            

    :type AnswerKey: string
    :param AnswerKey: The answers to the Qualification test specified in the Test parameter, in the form of an AnswerKey data structure.
            Constraints: Must not be longer than 65535 bytes.
            Constraints: None. If not specified, you must process Qualification requests manually.
            

    :type TestDurationInSeconds: integer
    :param TestDurationInSeconds: The number of seconds the Worker has to complete the Qualification test, starting from the time the Worker requests the Qualification.

    :type AutoGranted: boolean
    :param AutoGranted: Specifies whether requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test.
            Constraints: If the Test parameter is specified, this parameter cannot be true.
            

    :type AutoGrantedValue: integer
    :param AutoGrantedValue: The Qualification value to use for automatically granted Qualifications. This parameter is used only if the AutoGranted parameter is true.

    :rtype: dict
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

def create_worker_block(WorkerId=None, Reason=None):
    """
    The CreateWorkerBlock operation allows you to prevent a Worker from working on your HITs. For example, you can block a Worker who is producing poor quality work. You can block up to 100,000 Workers.
    See also: AWS API Documentation
    
    
    :example: response = client.create_worker_block(
        WorkerId='string',
        Reason='string'
    )
    
    
    :type WorkerId: string
    :param WorkerId: [REQUIRED]
            The ID of the Worker to block.
            

    :type Reason: string
    :param Reason: [REQUIRED]
            A message explaining the reason for blocking the Worker. This parameter enables you to keep track of your Workers. The Worker does not see this message.
            

    :rtype: dict
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
    
    
    :example: response = client.delete_hit(
        HITId='string'
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]
            The ID of the HIT to be deleted.
            

    :rtype: dict
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
    
    
    :example: response = client.delete_qualification_type(
        QualificationTypeId='string'
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]
            The ID of the QualificationType to dispose.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_worker_block(WorkerId=None, Reason=None):
    """
    The DeleteWorkerBlock operation allows you to reinstate a blocked Worker to work on your HITs. This operation reverses the effects of the CreateWorkerBlock operation. You need the Worker ID to use this operation. If the Worker ID is missing or invalid, this operation fails and returns the message WorkerId is invalid. If the specified Worker is not blocked, this operation returns successfully.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_worker_block(
        WorkerId='string',
        Reason='string'
    )
    
    
    :type WorkerId: string
    :param WorkerId: [REQUIRED]
            The ID of the Worker to unblock.
            

    :type Reason: string
    :param Reason: A message that explains the reason for unblocking the Worker. The Worker does not see this message.

    :rtype: dict
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
    
    
    :example: response = client.disassociate_qualification_from_worker(
        WorkerId='string',
        QualificationTypeId='string',
        Reason='string'
    )
    
    
    :type WorkerId: string
    :param WorkerId: [REQUIRED]
            The ID of the Worker who possesses the Qualification to be revoked.
            

    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]
            The ID of the Qualification type of the Qualification to be revoked.
            

    :type Reason: string
    :param Reason: A text message that explains why the Qualification was revoked. The user who had the Qualification sees this message.

    :rtype: dict
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

def get_account_balance():
    """
    The GetAccountBalance operation retrieves the amount of money in your Amazon Mechanical Turk account.
    See also: AWS API Documentation
    
    
    :example: response = client.get_account_balance()
    
    
    :rtype: dict
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
    
    
    :example: response = client.get_assignment(
        AssignmentId='string'
    )
    
    
    :type AssignmentId: string
    :param AssignmentId: [REQUIRED]
            The ID of the Assignment to be retrieved.
            

    :rtype: dict
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
                    'RequiredToPreview': True|False
                },
            ],
            'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
            'NumberOfAssignmentsPending': 123,
            'NumberOfAssignmentsAvailable': 123,
            'NumberOfAssignmentsCompleted': 123
        }
    }
    
    
    """
    pass

def get_file_upload_url(AssignmentId=None, QuestionIdentifier=None):
    """
    The GetFileUploadURL operation generates and returns a temporary URL. You use the temporary URL to retrieve a file uploaded by a Worker as an answer to a FileUploadAnswer question for a HIT. The temporary URL is generated the instant the GetFileUploadURL operation is called, and is valid for 60 seconds. You can get a temporary file upload URL any time until the HIT is disposed. After the HIT is disposed, any uploaded files are deleted, and cannot be retrieved.
    See also: AWS API Documentation
    
    
    :example: response = client.get_file_upload_url(
        AssignmentId='string',
        QuestionIdentifier='string'
    )
    
    
    :type AssignmentId: string
    :param AssignmentId: [REQUIRED]
            The ID of the assignment that contains the question with a FileUploadAnswer.
            

    :type QuestionIdentifier: string
    :param QuestionIdentifier: [REQUIRED]
            The identifier of the question with a FileUploadAnswer, as specified in the QuestionForm of the HIT.
            

    :rtype: dict
    :return: {
        'FileUploadURL': 'string'
    }
    
    
    """
    pass

def get_hit(HITId=None):
    """
    The GetHIT operation retrieves the details of the specified HIT.
    See also: AWS API Documentation
    
    
    :example: response = client.get_hit(
        HITId='string'
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]
            The ID of the HIT to be retrieved.
            

    :rtype: dict
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
                    'RequiredToPreview': True|False
                },
            ],
            'HITReviewStatus': 'NotReviewed'|'MarkedForReview'|'ReviewedAppropriate'|'ReviewedInappropriate',
            'NumberOfAssignmentsPending': 123,
            'NumberOfAssignmentsAvailable': 123,
            'NumberOfAssignmentsCompleted': 123
        }
    }
    
    
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

def get_qualification_score(QualificationTypeId=None, WorkerId=None):
    """
    The GetQualificationScore operation returns the value of a Worker's Qualification for a given Qualification type.
    To get a Worker's Qualification, you must know the Worker's ID. The Worker's ID is included in the assignment data returned by the ListAssignmentsForHIT operation.
    Only the owner of a Qualification type can query the value of a Worker's Qualification of that type.
    See also: AWS API Documentation
    
    
    :example: response = client.get_qualification_score(
        QualificationTypeId='string',
        WorkerId='string'
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]
            The ID of the QualificationType.
            

    :type WorkerId: string
    :param WorkerId: [REQUIRED]
            The ID of the Worker whose Qualification is being updated.
            

    :rtype: dict
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
    
    
    """
    pass

def get_qualification_type(QualificationTypeId=None):
    """
    The GetQualificationType operation retrieves information about a Qualification type using its ID.
    See also: AWS API Documentation
    
    
    :example: response = client.get_qualification_type(
        QualificationTypeId='string'
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]
            The ID of the QualificationType.
            

    :rtype: dict
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

def get_waiter():
    """
    
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
    
    
    :example: response = client.list_assignments_for_hit(
        HITId='string',
        NextToken='string',
        MaxResults=123,
        AssignmentStatuses=[
            'Submitted'|'Approved'|'Rejected',
        ]
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]
            The ID of the HIT.
            

    :type NextToken: string
    :param NextToken: Pagination token

    :type MaxResults: integer
    :param MaxResults: 

    :type AssignmentStatuses: list
    :param AssignmentStatuses: The status of the assignments to return: Submitted | Approved | Rejected
            (string) --
            

    :rtype: dict
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
    
    
    """
    pass

def list_bonus_payments(HITId=None, AssignmentId=None, NextToken=None, MaxResults=None):
    """
    The ListBonusPayments operation retrieves the amounts of bonuses you have paid to Workers for a given HIT or assignment.
    See also: AWS API Documentation
    
    
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
    
    
    """
    pass

def list_hits(NextToken=None, MaxResults=None):
    """
    The ListHITs operation returns all of a Requester's HITs. The operation returns HITs of any status, except for HITs that have been deleted of with the DeleteHIT operation or that have been auto-deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_hits(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token

    :type MaxResults: integer
    :param MaxResults: 

    :rtype: dict
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
                        'RequiredToPreview': True|False
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
    
    
    :example: response = client.list_hits_for_qualification_type(
        QualificationTypeId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]
            The ID of the Qualification type to use when querying HITs.
            

    :type NextToken: string
    :param NextToken: Pagination Token

    :type MaxResults: integer
    :param MaxResults: Limit the number of results returned.

    :rtype: dict
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
                        'RequiredToPreview': True|False
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
    
    
    """
    pass

def list_qualification_types(Query=None, MustBeRequestable=None, MustBeOwnedByCaller=None, NextToken=None, MaxResults=None):
    """
    The ListQualificationRequests operation retrieves requests for Qualifications of a particular Qualification type. The owner of the Qualification type calls this operation to poll for pending requests, and accepts them using the AcceptQualification operation.
    See also: AWS API Documentation
    
    
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
    :param MustBeRequestable: [REQUIRED]
            Specifies that only Qualification types that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test, are returned as results of the search. Some Qualification types, such as those assigned automatically by the system, cannot be requested directly by users. If false, all Qualification types, including those managed by the system, are considered. Valid values are True | False.
            

    :type MustBeOwnedByCaller: boolean
    :param MustBeOwnedByCaller: Specifies that only Qualification types that the Requester created are returned. If false, the operation returns all Qualification types.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict
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
    
    
    """
    pass

def list_review_policy_results_for_hit(HITId=None, PolicyLevels=None, RetrieveActions=None, RetrieveResults=None, NextToken=None, MaxResults=None):
    """
    The ListReviewPolicyResultsForHIT operation retrieves the computed results and the actions taken in the course of executing your Review Policies for a given HIT. For information about how to specify Review Policies when you call CreateHIT, see Review Policies. The ListReviewPolicyResultsForHIT operation can return results for both Assignment-level and HIT-level review results.
    See also: AWS API Documentation
    
    
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
    :param HITId: [REQUIRED]
            The unique identifier of the HIT to retrieve review results for.
            

    :type PolicyLevels: list
    :param PolicyLevels: The Policy Level(s) to retrieve review results for - HIT or Assignment. If omitted, the default behavior is to retrieve all data for both policy levels. For a list of all the described policies, see Review Policies.
            (string) --
            

    :type RetrieveActions: boolean
    :param RetrieveActions: Specify if the operation should retrieve a list of the actions taken executing the Review Policies and their outcomes.

    :type RetrieveResults: boolean
    :param RetrieveResults: Specify if the operation should retrieve a list of the results computed by the Review Policies.

    :type NextToken: string
    :param NextToken: Pagination token

    :type MaxResults: integer
    :param MaxResults: Limit the number of results returned.

    :rtype: dict
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
                        'RequiredToPreview': True|False
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
    
    
    :example: response = client.list_worker_blocks(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token

    :type MaxResults: integer
    :param MaxResults: 

    :rtype: dict
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
    
    
    """
    pass

def list_workers_with_qualification_type(QualificationTypeId=None, Status=None, NextToken=None, MaxResults=None):
    """
    The ListWorkersWithQualificationType operation returns all of the Workers that have been associated with a given Qualification type.
    See also: AWS API Documentation
    
    
    :example: response = client.list_workers_with_qualification_type(
        QualificationTypeId='string',
        Status='Granted'|'Revoked',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type QualificationTypeId: string
    :param QualificationTypeId: [REQUIRED]
            The ID of the Qualification type of the Qualifications to return.
            

    :type Status: string
    :param Status: The status of the Qualifications to return. Can be Granted | Revoked .

    :type NextToken: string
    :param NextToken: Pagination Token

    :type MaxResults: integer
    :param MaxResults: Limit the number of results returned.

    :rtype: dict
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
    
    
    """
    pass

def notify_workers(Subject=None, MessageText=None, WorkerIds=None):
    """
    The NotifyWorkers operation sends an email to one or more Workers that you specify with the Worker ID. You can specify up to 100 Worker IDs to send the same message with a single call to the NotifyWorkers operation. The NotifyWorkers operation will send a notification email to a Worker only if you have previously approved or rejected work from the Worker.
    See also: AWS API Documentation
    
    
    :example: response = client.notify_workers(
        Subject='string',
        MessageText='string',
        WorkerIds=[
            'string',
        ]
    )
    
    
    :type Subject: string
    :param Subject: [REQUIRED]
            The subject line of the email message to send. Can include up to 200 characters.
            

    :type MessageText: string
    :param MessageText: [REQUIRED]
            The text of the email message to send. Can include up to 4,096 characters
            

    :type WorkerIds: list
    :param WorkerIds: [REQUIRED]
            A list of Worker IDs you wish to notify. You can notify upto 100 Workers at a time.
            (string) --
            

    :rtype: dict
    :return: {
        'NotifyWorkersFailureStatuses': [
            {
                'NotifyWorkersFailureCode': 'SoftFailure'|'HardFailure',
                'NotifyWorkersFailureMessage': 'string',
                'WorkerId': 'string'
            },
        ]
    }
    
    
    """
    pass

def reject_assignment(AssignmentId=None, RequesterFeedback=None):
    """
    The RejectAssignment operation rejects the results of a completed assignment.
    You can include an optional feedback message with the rejection, which the Worker can see in the Status section of the web site. When you include a feedback message with the rejection, it helps the Worker understand why the assignment was rejected, and can improve the quality of the results the Worker submits in the future.
    Only the Requester who created the HIT can reject an assignment for the HIT.
    See also: AWS API Documentation
    
    
    :example: response = client.reject_assignment(
        AssignmentId='string',
        RequesterFeedback='string'
    )
    
    
    :type AssignmentId: string
    :param AssignmentId: [REQUIRED]
            The ID of the assignment. The assignment must correspond to a HIT created by the Requester.
            

    :type RequesterFeedback: string
    :param RequesterFeedback: A message for the Worker, which the Worker can see in the Status section of the web site.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reject_qualification_request(QualificationRequestId=None, Reason=None):
    """
    The RejectQualificationRequest operation rejects a user's request for a Qualification.
    You can provide a text message explaining why the request was rejected. The Worker who made the request can see this message.
    See also: AWS API Documentation
    
    
    :example: response = client.reject_qualification_request(
        QualificationRequestId='string',
        Reason='string'
    )
    
    
    :type QualificationRequestId: string
    :param QualificationRequestId: [REQUIRED]
            The ID of the Qualification request, as returned by the ListQualificationRequests operation.
            

    :type Reason: string
    :param Reason: A text message explaining why the request was rejected, to be shown to the Worker who made the request.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def send_bonus(WorkerId=None, BonusAmount=None, AssignmentId=None, Reason=None, UniqueRequestToken=None):
    """
    The SendBonus operation issues a payment of money from your account to a Worker. This payment happens separately from the reward you pay to the Worker when you approve the Worker's assignment. The SendBonus operation requires the Worker's ID and the assignment ID as parameters to initiate payment of the bonus. You must include a message that explains the reason for the bonus payment, as the Worker may not be expecting the payment. Amazon Mechanical Turk collects a fee for bonus payments, similar to the HIT listing fee. This operation fails if your account does not have enough funds to pay for both the bonus and the fees.
    See also: AWS API Documentation
    
    
    :example: response = client.send_bonus(
        WorkerId='string',
        BonusAmount='string',
        AssignmentId='string',
        Reason='string',
        UniqueRequestToken='string'
    )
    
    
    :type WorkerId: string
    :param WorkerId: [REQUIRED]
            The ID of the Worker being paid the bonus.
            

    :type BonusAmount: string
    :param BonusAmount: [REQUIRED]
            The Bonus amount is a US Dollar amount specified using a string (for example, '5' represents $5.00 USD and '101.42' represents $101.42 USD). Do not include currency symbols or currency codes.
            

    :type AssignmentId: string
    :param AssignmentId: [REQUIRED]
            The ID of the assignment for which this bonus is paid.
            

    :type Reason: string
    :param Reason: A message that explains the reason for the bonus payment. The Worker receiving the bonus can see this message.

    :type UniqueRequestToken: string
    :param UniqueRequestToken: A unique identifier for this request, which allows you to retry the call on error without granting multiple bonuses. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the bonus already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return an error with a message containing the request ID.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def send_test_event_notification(Notification=None, TestEventType=None):
    """
    The SendTestEventNotification operation causes Amazon Mechanical Turk to send a notification message as if a HIT event occurred, according to the provided notification specification. This allows you to test notifications without setting up notifications for a real HIT type and trying to trigger them using the website. When you call this operation, the service attempts to send the test notification immediately.
    See also: AWS API Documentation
    
    
    :example: response = client.send_test_event_notification(
        Notification={
            'Destination': 'string',
            'Transport': 'Email'|'SQS',
            'Version': 'string',
            'EventTypes': [
                'AssignmentAccepted'|'AssignmentAbandoned'|'AssignmentReturned'|'AssignmentSubmitted'|'AssignmentRejected'|'AssignmentApproved'|'HITCreated'|'HITExpired'|'HITReviewable'|'HITExtended'|'HITDisposed'|'Ping',
            ]
        },
        TestEventType='AssignmentAccepted'|'AssignmentAbandoned'|'AssignmentReturned'|'AssignmentSubmitted'|'AssignmentRejected'|'AssignmentApproved'|'HITCreated'|'HITExpired'|'HITReviewable'|'HITExtended'|'HITDisposed'|'Ping'
    )
    
    
    :type Notification: dict
    :param Notification: [REQUIRED]
            The notification specification to test. This value is identical to the value you would provide to the UpdateNotificationSettings operation when you establish the notification specification for a HIT type.
            Destination (string) -- [REQUIRED]The destination for notification messages. or email notifications (if Transport is Email), this is an email address. For Amazon Simple Queue Service (Amazon SQS) notifications (if Transport is SQS), this is the URL for your Amazon SQS queue.
            Transport (string) -- [REQUIRED]The method Amazon Mechanical Turk uses to send the notification. Valid Values: Email | SQS.
            Version (string) --The version of the Notification API to use. Valid value is 2006-05-05.
            EventTypes (list) --The list of events that should cause notifications to be sent. Valid Values: AssignmentAccepted | AssignmentAbandoned | AssignmentReturned | AssignmentSubmitted | AssignmentRejected | AssignmentApproved | HITCreated | HITExtended | HITDisposed | HITReviewable | HITExpired | Ping. The Ping event is only valid for the SendTestEventNotification operation.
            (string) --
            

    :type TestEventType: string
    :param TestEventType: [REQUIRED]
            The event to simulate to test the notification specification. This event is included in the test message even if the notification specification does not include the event type. The notification specification does not filter out the test event.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_expiration_for_hit(HITId=None, ExpireAt=None):
    """
    The UpdateExpirationForHIT operation allows you update the expiration time of a HIT. If you update it to a time in the past, the HIT will be immediately expired.
    See also: AWS API Documentation
    
    
    :example: response = client.update_expiration_for_hit(
        HITId='string',
        ExpireAt=datetime(2015, 1, 1)
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]
            The HIT to update.
            

    :type ExpireAt: datetime
    :param ExpireAt: The date and time at which you want the HIT to expire

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_hit_review_status(HITId=None, Revert=None):
    """
    The UpdateHITReviewStatus operation updates the status of a HIT. If the status is Reviewable, this operation can update the status to Reviewing, or it can revert a Reviewing HIT back to the Reviewable status.
    See also: AWS API Documentation
    
    
    :example: response = client.update_hit_review_status(
        HITId='string',
        Revert=True|False
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]
            The ID of the HIT to update.
            

    :type Revert: boolean
    :param Revert: Specifies how to update the HIT status. Default is False .
            Setting this to false will only transition a HIT from Reviewable to Reviewing
            Setting this to true will only transition a HIT from Reviewing to Reviewable
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_hit_type_of_hit(HITId=None, HITTypeId=None):
    """
    The UpdateHITTypeOfHIT operation allows you to change the HITType properties of a HIT. This operation disassociates the HIT from its old HITType properties and associates it with the new HITType properties. The HIT takes on the properties of the new HITType in place of the old ones.
    See also: AWS API Documentation
    
    
    :example: response = client.update_hit_type_of_hit(
        HITId='string',
        HITTypeId='string'
    )
    
    
    :type HITId: string
    :param HITId: [REQUIRED]
            The HIT to update.
            

    :type HITTypeId: string
    :param HITTypeId: [REQUIRED]
            The ID of the new HIT type.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_notification_settings(HITTypeId=None, Notification=None, Active=None):
    """
    The UpdateNotificationSettings operation creates, updates, disables or re-enables notifications for a HIT type. If you call the UpdateNotificationSettings operation for a HIT type that already has a notification specification, the operation replaces the old specification with a new one. You can call the UpdateNotificationSettings operation to enable or disable notifications for the HIT type, without having to modify the notification specification itself by providing updates to the Active status without specifying a new notification specification. To change the Active status of a HIT type's notifications, the HIT type must already have a notification specification, or one must be provided in the same call to UpdateNotificationSettings .
    See also: AWS API Documentation
    
    
    :example: response = client.update_notification_settings(
        HITTypeId='string',
        Notification={
            'Destination': 'string',
            'Transport': 'Email'|'SQS',
            'Version': 'string',
            'EventTypes': [
                'AssignmentAccepted'|'AssignmentAbandoned'|'AssignmentReturned'|'AssignmentSubmitted'|'AssignmentRejected'|'AssignmentApproved'|'HITCreated'|'HITExpired'|'HITReviewable'|'HITExtended'|'HITDisposed'|'Ping',
            ]
        },
        Active=True|False
    )
    
    
    :type HITTypeId: string
    :param HITTypeId: [REQUIRED]
            The ID of the HIT type whose notification specification is being updated.
            

    :type Notification: dict
    :param Notification: The notification specification for the HIT type.
            Destination (string) -- [REQUIRED]The destination for notification messages. or email notifications (if Transport is Email), this is an email address. For Amazon Simple Queue Service (Amazon SQS) notifications (if Transport is SQS), this is the URL for your Amazon SQS queue.
            Transport (string) -- [REQUIRED]The method Amazon Mechanical Turk uses to send the notification. Valid Values: Email | SQS.
            Version (string) --The version of the Notification API to use. Valid value is 2006-05-05.
            EventTypes (list) --The list of events that should cause notifications to be sent. Valid Values: AssignmentAccepted | AssignmentAbandoned | AssignmentReturned | AssignmentSubmitted | AssignmentRejected | AssignmentApproved | HITCreated | HITExtended | HITDisposed | HITReviewable | HITExpired | Ping. The Ping event is only valid for the SendTestEventNotification operation.
            (string) --
            

    :type Active: boolean
    :param Active: Specifies whether notifications are sent for HITs of this HIT type, according to the notification specification. You must specify either the Notification parameter or the Active parameter for the call to UpdateNotificationSettings to succeed.

    :rtype: dict
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
    :param QualificationTypeId: [REQUIRED]
            The ID of the Qualification type to update.
            

    :type Description: string
    :param Description: The new description of the Qualification type.

    :type QualificationTypeStatus: string
    :param QualificationTypeStatus: The new status of the Qualification type - Active | Inactive

    :type Test: string
    :param Test: The questions for the Qualification test a Worker must answer correctly to obtain a Qualification of this type. If this parameter is specified, TestDurationInSeconds must also be specified.
            Constraints: Must not be longer than 65535 bytes. Must be a QuestionForm data structure. This parameter cannot be specified if AutoGranted is true.
            Constraints: None. If not specified, the Worker may request the Qualification without answering any questions.
            

    :type AnswerKey: string
    :param AnswerKey: The answers to the Qualification test specified in the Test parameter, in the form of an AnswerKey data structure.

    :type TestDurationInSeconds: integer
    :param TestDurationInSeconds: The number of seconds the Worker has to complete the Qualification test, starting from the time the Worker requests the Qualification.

    :type RetryDelayInSeconds: integer
    :param RetryDelayInSeconds: The amount of time, in seconds, that Workers must wait after requesting a Qualification of the specified Qualification type before they can retry the Qualification request. It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must dispose of the existing retry-enabled Qualification type using DisposeQualificationType and then create a new Qualification type with retries disabled using CreateQualificationType.

    :type AutoGranted: boolean
    :param AutoGranted: Specifies whether requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test.
            Constraints: If the Test parameter is specified, this parameter cannot be true.
            

    :type AutoGrantedValue: integer
    :param AutoGrantedValue: The Qualification value to use for automatically granted Qualifications. This parameter is used only if the AutoGranted parameter is true.

    :rtype: dict
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

