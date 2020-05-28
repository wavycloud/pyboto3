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

def add_attributes_to_findings(findingArns=None, attributes=None):
    """
    Assigns attributes (key and value pairs) to the findings that are specified by the ARNs of the findings.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Assigns attributes (key and value pairs) to the findings that are specified by the ARNs of the findings.
    Expected Output:
    
    :example: response = client.add_attributes_to_findings(
        findingArns=[
            'string',
        ],
        attributes=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type findingArns: list
    :param findingArns: [REQUIRED]\nThe ARNs that specify the findings that you want to assign attributes to.\n\n(string) --\n\n

    :type attributes: list
    :param attributes: [REQUIRED]\nThe array of attributes that you want to assign to specified findings.\n\n(dict) --This data type is used as a request parameter in the AddAttributesToFindings and CreateAssessmentTemplate actions.\n\nkey (string) -- [REQUIRED]The attribute key.\n\nvalue (string) --The value assigned to the attribute key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'failedItems': {
        'string': {
            'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
            'retryable': True|False
        }
    }
}


Response Structure

(dict) --

failedItems (dict) --
Attribute details that cannot be described. An error code is provided for each failed item.

(string) --

(dict) --
Includes details about the failed items.

failureCode (string) --
The status code of a failed item.

retryable (boolean) --
Indicates whether you can immediately retry a request for this item for a specified resource.













Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException
Inspector.Client.exceptions.ServiceTemporarilyUnavailableException

Examples
Assigns attributes (key and value pairs) to the findings that are specified by the ARNs of the findings.
response = client.add_attributes_to_findings(
    attributes=[
        {
            'key': 'Example',
            'value': 'example',
        },
    ],
    findingArns=[
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU',
    ],
)

print(response)


Expected Output:
{
    'failedItems': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'failedItems': {
            'string': {
                'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                'retryable': True|False
            }
        }
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_assessment_target(assessmentTargetName=None, resourceGroupArn=None):
    """
    Creates a new assessment target using the ARN of the resource group that is generated by  CreateResourceGroup . If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target. If the service-linked role isn\xe2\x80\x99t already registered, this action also creates and registers a service-linked role to grant Amazon Inspector access to AWS Services needed to perform security assessments. You can create up to 50 assessment targets per AWS account. You can run up to 500 concurrent agents per AWS account. For more information, see Amazon Inspector Assessment Targets .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a new assessment target using the ARN of the resource group that is generated by CreateResourceGroup. You can create up to 50 assessment targets per AWS account. You can run up to 500 concurrent agents per AWS account.
    Expected Output:
    
    :example: response = client.create_assessment_target(
        assessmentTargetName='string',
        resourceGroupArn='string'
    )
    
    
    :type assessmentTargetName: string
    :param assessmentTargetName: [REQUIRED]\nThe user-defined name that identifies the assessment target that you want to create. The name must be unique within the AWS account.\n

    :type resourceGroupArn: string
    :param resourceGroupArn: The ARN that specifies the resource group that is used to create the assessment target. If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target.

    :rtype: dict

ReturnsResponse Syntax
{
    'assessmentTargetArn': 'string'
}


Response Structure

(dict) --

assessmentTargetArn (string) --
The ARN that specifies the assessment target that is created.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.LimitExceededException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException
Inspector.Client.exceptions.InvalidCrossAccountRoleException
Inspector.Client.exceptions.ServiceTemporarilyUnavailableException

Examples
Creates a new assessment target using the ARN of the resource group that is generated by CreateResourceGroup. You can create up to 50 assessment targets per AWS account. You can run up to 500 concurrent agents per AWS account.
response = client.create_assessment_target(
    assessmentTargetName='ExampleAssessmentTarget',
    resourceGroupArn='arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-AB6DMKnv',
)

print(response)


Expected Output:
{
    'assessmentTargetArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'assessmentTargetArn': 'string'
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.LimitExceededException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.InvalidCrossAccountRoleException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

def create_assessment_template(assessmentTargetArn=None, assessmentTemplateName=None, durationInSeconds=None, rulesPackageArns=None, userAttributesForFindings=None):
    """
    Creates an assessment template for the assessment target that is specified by the ARN of the assessment target. If the service-linked role isn\xe2\x80\x99t already registered, this action also creates and registers a service-linked role to grant Amazon Inspector access to AWS Services needed to perform security assessments.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates an assessment template for the assessment target that is specified by the ARN of the assessment target.
    Expected Output:
    
    :example: response = client.create_assessment_template(
        assessmentTargetArn='string',
        assessmentTemplateName='string',
        durationInSeconds=123,
        rulesPackageArns=[
            'string',
        ],
        userAttributesForFindings=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type assessmentTargetArn: string
    :param assessmentTargetArn: [REQUIRED]\nThe ARN that specifies the assessment target for which you want to create the assessment template.\n

    :type assessmentTemplateName: string
    :param assessmentTemplateName: [REQUIRED]\nThe user-defined name that identifies the assessment template that you want to create. You can create several assessment templates for an assessment target. The names of the assessment templates that correspond to a particular assessment target must be unique.\n

    :type durationInSeconds: integer
    :param durationInSeconds: [REQUIRED]\nThe duration of the assessment run in seconds.\n

    :type rulesPackageArns: list
    :param rulesPackageArns: [REQUIRED]\nThe ARNs that specify the rules packages that you want to attach to the assessment template.\n\n(string) --\n\n

    :type userAttributesForFindings: list
    :param userAttributesForFindings: The user-defined attributes that are assigned to every finding that is generated by the assessment run that uses this assessment template. An attribute is a key and value pair (an Attribute object). Within an assessment template, each key must be unique.\n\n(dict) --This data type is used as a request parameter in the AddAttributesToFindings and CreateAssessmentTemplate actions.\n\nkey (string) -- [REQUIRED]The attribute key.\n\nvalue (string) --The value assigned to the attribute key.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'assessmentTemplateArn': 'string'
}


Response Structure

(dict) --

assessmentTemplateArn (string) --
The ARN that specifies the assessment template that is created.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.LimitExceededException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException
Inspector.Client.exceptions.ServiceTemporarilyUnavailableException

Examples
Creates an assessment template for the assessment target that is specified by the ARN of the assessment target.
response = client.create_assessment_template(
    assessmentTargetArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX',
    assessmentTemplateName='ExampleAssessmentTemplate',
    durationInSeconds=180,
    rulesPackageArns=[
        'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-11B9DBXp',
    ],
    userAttributesForFindings=[
        {
            'key': 'Example',
            'value': 'example',
        },
    ],
)

print(response)


Expected Output:
{
    'assessmentTemplateArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'assessmentTemplateArn': 'string'
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.LimitExceededException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

def create_exclusions_preview(assessmentTemplateArn=None):
    """
    Starts the generation of an exclusions preview for the specified assessment template. The exclusions preview lists the potential exclusions (ExclusionPreview) that Inspector can detect before it runs the assessment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_exclusions_preview(
        assessmentTemplateArn='string'
    )
    
    
    :type assessmentTemplateArn: string
    :param assessmentTemplateArn: [REQUIRED]\nThe ARN that specifies the assessment template for which you want to create an exclusions preview.\n

    :rtype: dict
ReturnsResponse Syntax{
    'previewToken': 'string'
}


Response Structure

(dict) --
previewToken (string) --Specifies the unique identifier of the requested exclusions preview. You can use the unique identifier to retrieve the exclusions preview when running the GetExclusionsPreview API.






Exceptions

Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.PreviewGenerationInProgressException
Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException
Inspector.Client.exceptions.ServiceTemporarilyUnavailableException


    :return: {
        'previewToken': 'string'
    }
    
    
    """
    pass

def create_resource_group(resourceGroupTags=None):
    """
    Creates a resource group using the specified set of tags (key and value pairs) that are used to select the EC2 instances to be included in an Amazon Inspector assessment target. The created resource group is then used to create an Amazon Inspector assessment target. For more information, see  CreateAssessmentTarget .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a resource group using the specified set of tags (key and value pairs) that are used to select the EC2 instances to be included in an Amazon Inspector assessment target. The created resource group is then used to create an Amazon Inspector assessment target.
    Expected Output:
    
    :example: response = client.create_resource_group(
        resourceGroupTags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceGroupTags: list
    :param resourceGroupTags: [REQUIRED]\nA collection of keys and an array of possible values, \'[{'key':'key1','values':['Value1','Value2']},{'key':'Key2','values':['Value3']}]\'.\nFor example,\'[{'key':'Name','values':['TestEC2Instance']}]\'.\n\n(dict) --This data type is used as one of the elements of the ResourceGroup data type.\n\nkey (string) -- [REQUIRED]A tag key.\n\nvalue (string) --The value assigned to a tag key.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'resourceGroupArn': 'string'
}


Response Structure

(dict) --
resourceGroupArn (string) --The ARN that specifies the resource group that is created.






Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.LimitExceededException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.ServiceTemporarilyUnavailableException

Examples
Creates a resource group using the specified set of tags (key and value pairs) that are used to select the EC2 instances to be included in an Amazon Inspector assessment target. The created resource group is then used to create an Amazon Inspector assessment target.
response = client.create_resource_group(
    resourceGroupTags=[
        {
            'key': 'Name',
            'value': 'example',
        },
    ],
)

print(response)


Expected Output:
{
    'resourceGroupArn': 'arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-AB6DMKnv',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'resourceGroupArn': 'string'
    }
    
    
    """
    pass

def delete_assessment_run(assessmentRunArn=None):
    """
    Deletes the assessment run that is specified by the ARN of the assessment run.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the assessment run that is specified by the ARN of the assessment run.
    Expected Output:
    
    :example: response = client.delete_assessment_run(
        assessmentRunArn='string'
    )
    
    
    :type assessmentRunArn: string
    :param assessmentRunArn: [REQUIRED]\nThe ARN that specifies the assessment run that you want to delete.\n

    :return: response = client.delete_assessment_run(
        assessmentRunArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-11LMTAVe',
    )
    
    print(response)
    
    
    """
    pass

def delete_assessment_target(assessmentTargetArn=None):
    """
    Deletes the assessment target that is specified by the ARN of the assessment target.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the assessment target that is specified by the ARN of the assessment target.
    Expected Output:
    
    :example: response = client.delete_assessment_target(
        assessmentTargetArn='string'
    )
    
    
    :type assessmentTargetArn: string
    :param assessmentTargetArn: [REQUIRED]\nThe ARN that specifies the assessment target that you want to delete.\n

    :return: response = client.delete_assessment_target(
        assessmentTargetArn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
    )
    
    print(response)
    
    
    """
    pass

def delete_assessment_template(assessmentTemplateArn=None):
    """
    Deletes the assessment template that is specified by the ARN of the assessment template.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes the assessment template that is specified by the ARN of the assessment template.
    Expected Output:
    
    :example: response = client.delete_assessment_template(
        assessmentTemplateArn='string'
    )
    
    
    :type assessmentTemplateArn: string
    :param assessmentTemplateArn: [REQUIRED]\nThe ARN that specifies the assessment template that you want to delete.\n

    :return: response = client.delete_assessment_template(
        assessmentTemplateArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T',
    )
    
    print(response)
    
    
    """
    pass

def describe_assessment_runs(assessmentRunArns=None):
    """
    Describes the assessment runs that are specified by the ARNs of the assessment runs.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes the assessment runs that are specified by the ARNs of the assessment runs.
    Expected Output:
    
    :example: response = client.describe_assessment_runs(
        assessmentRunArns=[
            'string',
        ]
    )
    
    
    :type assessmentRunArns: list
    :param assessmentRunArns: [REQUIRED]\nThe ARN that specifies the assessment run that you want to describe.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'assessmentRuns': [
        {
            'arn': 'string',
            'name': 'string',
            'assessmentTemplateArn': 'string',
            'state': 'CREATED'|'START_DATA_COLLECTION_PENDING'|'START_DATA_COLLECTION_IN_PROGRESS'|'COLLECTING_DATA'|'STOP_DATA_COLLECTION_PENDING'|'DATA_COLLECTED'|'START_EVALUATING_RULES_PENDING'|'EVALUATING_RULES'|'FAILED'|'ERROR'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'CANCELED',
            'durationInSeconds': 123,
            'rulesPackageArns': [
                'string',
            ],
            'userAttributesForFindings': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'startedAt': datetime(2015, 1, 1),
            'completedAt': datetime(2015, 1, 1),
            'stateChangedAt': datetime(2015, 1, 1),
            'dataCollected': True|False,
            'stateChanges': [
                {
                    'stateChangedAt': datetime(2015, 1, 1),
                    'state': 'CREATED'|'START_DATA_COLLECTION_PENDING'|'START_DATA_COLLECTION_IN_PROGRESS'|'COLLECTING_DATA'|'STOP_DATA_COLLECTION_PENDING'|'DATA_COLLECTED'|'START_EVALUATING_RULES_PENDING'|'EVALUATING_RULES'|'FAILED'|'ERROR'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'CANCELED'
                },
            ],
            'notifications': [
                {
                    'date': datetime(2015, 1, 1),
                    'event': 'ASSESSMENT_RUN_STARTED'|'ASSESSMENT_RUN_COMPLETED'|'ASSESSMENT_RUN_STATE_CHANGED'|'FINDING_REPORTED'|'OTHER',
                    'message': 'string',
                    'error': True|False,
                    'snsTopicArn': 'string',
                    'snsPublishStatusCode': 'SUCCESS'|'TOPIC_DOES_NOT_EXIST'|'ACCESS_DENIED'|'INTERNAL_ERROR'
                },
            ],
            'findingCounts': {
                'string': 123
            }
        },
    ],
    'failedItems': {
        'string': {
            'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
            'retryable': True|False
        }
    }
}


Response Structure

(dict) --
assessmentRuns (list) --Information about the assessment run.

(dict) --A snapshot of an Amazon Inspector assessment run that contains the findings of the assessment run .
Used as the response element in the  DescribeAssessmentRuns action.

arn (string) --The ARN of the assessment run.

name (string) --The auto-generated name for the assessment run.

assessmentTemplateArn (string) --The ARN of the assessment template that is associated with the assessment run.

state (string) --The state of the assessment run.

durationInSeconds (integer) --The duration of the assessment run.

rulesPackageArns (list) --The rules packages selected for the assessment run.

(string) --


userAttributesForFindings (list) --The user-defined attributes that are assigned to every generated finding.

(dict) --This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

key (string) --The attribute key.

value (string) --The value assigned to the attribute key.





createdAt (datetime) --The time when  StartAssessmentRun was called.

startedAt (datetime) --The time when  StartAssessmentRun was called.

completedAt (datetime) --The assessment run completion time that corresponds to the rules packages evaluation completion time or failure.

stateChangedAt (datetime) --The last time when the assessment run\'s state changed.

dataCollected (boolean) --A Boolean value (true or false) that specifies whether the process of collecting data from the agents is completed.

stateChanges (list) --A list of the assessment run state changes.

(dict) --Used as one of the elements of the  AssessmentRun data type.

stateChangedAt (datetime) --The last time the assessment run state changed.

state (string) --The assessment run state.





notifications (list) --A list of notifications for the event subscriptions. A notification about a particular generated finding is added to this list only once.

(dict) --Used as one of the elements of the  AssessmentRun data type.

date (datetime) --The date of the notification.

event (string) --The event for which a notification is sent.

message (string) --The message included in the notification.

error (boolean) --The Boolean value that specifies whether the notification represents an error.

snsTopicArn (string) --The SNS topic to which the SNS notification is sent.

snsPublishStatusCode (string) --The status code of the SNS notification.





findingCounts (dict) --Provides a total count of generated findings per severity.

(string) --
(integer) --








failedItems (dict) --Assessment run details that cannot be described. An error code is provided for each failed item.

(string) --
(dict) --Includes details about the failed items.

failureCode (string) --The status code of a failed item.

retryable (boolean) --Indicates whether you can immediately retry a request for this item for a specified resource.












Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException

Examples
Describes the assessment runs that are specified by the ARNs of the assessment runs.
response = client.describe_assessment_runs(
    assessmentRunArns=[
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
    ],
)

print(response)


Expected Output:
{
    'assessmentRuns': [
        {
            'name': 'Run 1 for ExampleAssessmentTemplate',
            'arn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
            'assessmentTemplateArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw',
            'completedAt': datetime(2016, 3, 22, 20, 58, 21, 1, 82, 0),
            'createdAt': datetime(2016, 3, 22, 20, 56, 10, 1, 82, 0),
            'dataCollected': True,
            'durationInSeconds': 3600,
            'findingCounts': {
                'High': 14,
                'Informational': 0,
                'Low': 0,
                'Medium': 2,
                'Undefined': 0,
            },
            'notifications': [
            ],
            'rulesPackageArns': [
                'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP',
            ],
            'startedAt': datetime(2016, 3, 22, 20, 56, 10, 1, 82, 0),
            'state': 'COMPLETED',
            'stateChangedAt': datetime(2016, 3, 22, 20, 58, 21, 1, 82, 0),
            'stateChanges': [
                {
                    'state': 'CREATED',
                    'stateChangedAt': datetime(2016, 3, 22, 20, 56, 10, 1, 82, 0),
                },
                {
                    'state': 'START_DATA_COLLECTION_PENDING',
                    'stateChangedAt': datetime(2016, 3, 22, 20, 56, 10, 1, 82, 0),
                },
                {
                    'state': 'START_DATA_COLLECTION_IN_PROGRESS',
                    'stateChangedAt': datetime(2016, 3, 22, 20, 56, 10, 1, 82, 0),
                },
                {
                    'state': 'COLLECTING_DATA',
                    'stateChangedAt': datetime(2016, 3, 22, 20, 56, 10, 1, 82, 0),
                },
                {
                    'state': 'STOP_DATA_COLLECTION_PENDING',
                    'stateChangedAt': datetime(2016, 3, 22, 20, 57, 19, 1, 82, 0),
                },
                {
                    'state': 'DATA_COLLECTED',
                    'stateChangedAt': datetime(2016, 3, 22, 20, 58, 19, 1, 82, 0),
                },
                {
                    'state': 'EVALUATING_RULES',
                    'stateChangedAt': datetime(2016, 3, 22, 20, 58, 20, 1, 82, 0),
                },
                {
                    'state': 'COMPLETED',
                    'stateChangedAt': datetime(2016, 3, 22, 20, 58, 21, 1, 82, 0),
                },
            ],
            'userAttributesForFindings': [
            ],
        },
    ],
    'failedItems': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'assessmentRuns': [
            {
                'arn': 'string',
                'name': 'string',
                'assessmentTemplateArn': 'string',
                'state': 'CREATED'|'START_DATA_COLLECTION_PENDING'|'START_DATA_COLLECTION_IN_PROGRESS'|'COLLECTING_DATA'|'STOP_DATA_COLLECTION_PENDING'|'DATA_COLLECTED'|'START_EVALUATING_RULES_PENDING'|'EVALUATING_RULES'|'FAILED'|'ERROR'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'CANCELED',
                'durationInSeconds': 123,
                'rulesPackageArns': [
                    'string',
                ],
                'userAttributesForFindings': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'createdAt': datetime(2015, 1, 1),
                'startedAt': datetime(2015, 1, 1),
                'completedAt': datetime(2015, 1, 1),
                'stateChangedAt': datetime(2015, 1, 1),
                'dataCollected': True|False,
                'stateChanges': [
                    {
                        'stateChangedAt': datetime(2015, 1, 1),
                        'state': 'CREATED'|'START_DATA_COLLECTION_PENDING'|'START_DATA_COLLECTION_IN_PROGRESS'|'COLLECTING_DATA'|'STOP_DATA_COLLECTION_PENDING'|'DATA_COLLECTED'|'START_EVALUATING_RULES_PENDING'|'EVALUATING_RULES'|'FAILED'|'ERROR'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'CANCELED'
                    },
                ],
                'notifications': [
                    {
                        'date': datetime(2015, 1, 1),
                        'event': 'ASSESSMENT_RUN_STARTED'|'ASSESSMENT_RUN_COMPLETED'|'ASSESSMENT_RUN_STATE_CHANGED'|'FINDING_REPORTED'|'OTHER',
                        'message': 'string',
                        'error': True|False,
                        'snsTopicArn': 'string',
                        'snsPublishStatusCode': 'SUCCESS'|'TOPIC_DOES_NOT_EXIST'|'ACCESS_DENIED'|'INTERNAL_ERROR'
                    },
                ],
                'findingCounts': {
                    'string': 123
                }
            },
        ],
        'failedItems': {
            'string': {
                'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                'retryable': True|False
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_assessment_targets(assessmentTargetArns=None):
    """
    Describes the assessment targets that are specified by the ARNs of the assessment targets.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes the assessment targets that are specified by the ARNs of the assessment targets.
    Expected Output:
    
    :example: response = client.describe_assessment_targets(
        assessmentTargetArns=[
            'string',
        ]
    )
    
    
    :type assessmentTargetArns: list
    :param assessmentTargetArns: [REQUIRED]\nThe ARNs that specifies the assessment targets that you want to describe.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'assessmentTargets': [
        {
            'arn': 'string',
            'name': 'string',
            'resourceGroupArn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'updatedAt': datetime(2015, 1, 1)
        },
    ],
    'failedItems': {
        'string': {
            'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
            'retryable': True|False
        }
    }
}


Response Structure

(dict) --
assessmentTargets (list) --Information about the assessment targets.

(dict) --Contains information about an Amazon Inspector application. This data type is used as the response element in the  DescribeAssessmentTargets action.

arn (string) --The ARN that specifies the Amazon Inspector assessment target.

name (string) --The name of the Amazon Inspector assessment target.

resourceGroupArn (string) --The ARN that specifies the resource group that is associated with the assessment target.

createdAt (datetime) --The time at which the assessment target is created.

updatedAt (datetime) --The time at which  UpdateAssessmentTarget is called.





failedItems (dict) --Assessment target details that cannot be described. An error code is provided for each failed item.

(string) --
(dict) --Includes details about the failed items.

failureCode (string) --The status code of a failed item.

retryable (boolean) --Indicates whether you can immediately retry a request for this item for a specified resource.












Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException

Examples
Describes the assessment targets that are specified by the ARNs of the assessment targets.
response = client.describe_assessment_targets(
    assessmentTargetArns=[
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
    ],
)

print(response)


Expected Output:
{
    'assessmentTargets': [
        {
            'name': 'ExampleAssessmentTarget',
            'arn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
            'createdAt': datetime(2016, 3, 15, 20, 36, 31, 1, 75, 0),
            'resourceGroupArn': 'arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI',
            'updatedAt': datetime(2016, 3, 15, 20, 36, 31, 1, 75, 0),
        },
    ],
    'failedItems': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'assessmentTargets': [
            {
                'arn': 'string',
                'name': 'string',
                'resourceGroupArn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'updatedAt': datetime(2015, 1, 1)
            },
        ],
        'failedItems': {
            'string': {
                'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                'retryable': True|False
            }
        }
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    
    """
    pass

def describe_assessment_templates(assessmentTemplateArns=None):
    """
    Describes the assessment templates that are specified by the ARNs of the assessment templates.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes the assessment templates that are specified by the ARNs of the assessment templates.
    Expected Output:
    
    :example: response = client.describe_assessment_templates(
        assessmentTemplateArns=[
            'string',
        ]
    )
    
    
    :type assessmentTemplateArns: list
    :param assessmentTemplateArns: [REQUIRED]\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'assessmentTemplates': [
        {
            'arn': 'string',
            'name': 'string',
            'assessmentTargetArn': 'string',
            'durationInSeconds': 123,
            'rulesPackageArns': [
                'string',
            ],
            'userAttributesForFindings': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'lastAssessmentRunArn': 'string',
            'assessmentRunCount': 123,
            'createdAt': datetime(2015, 1, 1)
        },
    ],
    'failedItems': {
        'string': {
            'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
            'retryable': True|False
        }
    }
}


Response Structure

(dict) --
assessmentTemplates (list) --Information about the assessment templates.

(dict) --Contains information about an Amazon Inspector assessment template. This data type is used as the response element in the  DescribeAssessmentTemplates action.

arn (string) --The ARN of the assessment template.

name (string) --The name of the assessment template.

assessmentTargetArn (string) --The ARN of the assessment target that corresponds to this assessment template.

durationInSeconds (integer) --The duration in seconds specified for this assessment template. The default value is 3600 seconds (one hour). The maximum value is 86400 seconds (one day).

rulesPackageArns (list) --The rules packages that are specified for this assessment template.

(string) --


userAttributesForFindings (list) --The user-defined attributes that are assigned to every generated finding from the assessment run that uses this assessment template.

(dict) --This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

key (string) --The attribute key.

value (string) --The value assigned to the attribute key.





lastAssessmentRunArn (string) --The Amazon Resource Name (ARN) of the most recent assessment run associated with this assessment template. This value exists only when the value of assessmentRunCount is greaterpa than zero.

assessmentRunCount (integer) --The number of existing assessment runs associated with this assessment template. This value can be zero or a positive integer.

createdAt (datetime) --The time at which the assessment template is created.





failedItems (dict) --Assessment template details that cannot be described. An error code is provided for each failed item.

(string) --
(dict) --Includes details about the failed items.

failureCode (string) --The status code of a failed item.

retryable (boolean) --Indicates whether you can immediately retry a request for this item for a specified resource.












Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException

Examples
Describes the assessment templates that are specified by the ARNs of the assessment templates.
response = client.describe_assessment_templates(
    assessmentTemplateArns=[
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw',
    ],
)

print(response)


Expected Output:
{
    'assessmentTemplates': [
        {
            'name': 'ExampleAssessmentTemplate',
            'arn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw',
            'assessmentRunCount': 0,
            'assessmentTargetArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
            'createdAt': datetime(2016, 3, 15, 20, 36, 31, 1, 75, 0),
            'durationInSeconds': 3600,
            'rulesPackageArns': [
                'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP',
            ],
            'userAttributesForFindings': [
            ],
        },
    ],
    'failedItems': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'assessmentTemplates': [
            {
                'arn': 'string',
                'name': 'string',
                'assessmentTargetArn': 'string',
                'durationInSeconds': 123,
                'rulesPackageArns': [
                    'string',
                ],
                'userAttributesForFindings': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'lastAssessmentRunArn': 'string',
                'assessmentRunCount': 123,
                'createdAt': datetime(2015, 1, 1)
            },
        ],
        'failedItems': {
            'string': {
                'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                'retryable': True|False
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_cross_account_access_role():
    """
    Describes the IAM role that enables Amazon Inspector to access your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes the IAM role that enables Amazon Inspector to access your AWS account.
    Expected Output:
    
    :example: response = client.describe_cross_account_access_role()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'roleArn': 'string',
    'valid': True|False,
    'registeredAt': datetime(2015, 1, 1)
}


Response Structure

(dict) --
roleArn (string) --The ARN that specifies the IAM role that Amazon Inspector uses to access your AWS account.

valid (boolean) --A Boolean value that specifies whether the IAM role has the necessary policies attached to enable Amazon Inspector to access your AWS account.

registeredAt (datetime) --The date when the cross-account access role was registered.






Exceptions

Inspector.Client.exceptions.InternalException

Examples
Describes the IAM role that enables Amazon Inspector to access your AWS account.
response = client.describe_cross_account_access_role(
)

print(response)


Expected Output:
{
    'registeredAt': datetime(2016, 3, 15, 19, 13, 2, 1, 75, 0),
    'roleArn': 'arn:aws:iam::123456789012:role/inspector',
    'valid': True,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'roleArn': 'string',
        'valid': True|False,
        'registeredAt': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_exclusions(exclusionArns=None, locale=None):
    """
    Describes the exclusions that are specified by the exclusions\' ARNs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_exclusions(
        exclusionArns=[
            'string',
        ],
        locale='EN_US'
    )
    
    
    :type exclusionArns: list
    :param exclusionArns: [REQUIRED]\nThe list of ARNs that specify the exclusions that you want to describe.\n\n(string) --\n\n

    :type locale: string
    :param locale: The locale into which you want to translate the exclusion\'s title, description, and recommendation.

    :rtype: dict

ReturnsResponse Syntax
{
    'exclusions': {
        'string': {
            'arn': 'string',
            'title': 'string',
            'description': 'string',
            'recommendation': 'string',
            'scopes': [
                {
                    'key': 'INSTANCE_ID'|'RULES_PACKAGE_ARN',
                    'value': 'string'
                },
            ],
            'attributes': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    },
    'failedItems': {
        'string': {
            'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
            'retryable': True|False
        }
    }
}


Response Structure

(dict) --

exclusions (dict) --
Information about the exclusions.

(string) --

(dict) --
Contains information about what was excluded from an assessment run.

arn (string) --
The ARN that specifies the exclusion.

title (string) --
The name of the exclusion.

description (string) --
The description of the exclusion.

recommendation (string) --
The recommendation for the exclusion.

scopes (list) --
The AWS resources for which the exclusion pertains.

(dict) --
This data type contains key-value pairs that identify various Amazon resources.

key (string) --
The type of the scope.

value (string) --
The resource identifier for the specified scope type.





attributes (list) --
The system-defined attributes for the exclusion.

(dict) --
This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

key (string) --
The attribute key.

value (string) --
The value assigned to the attribute key.











failedItems (dict) --
Exclusion details that cannot be described. An error code is provided for each failed item.

(string) --

(dict) --
Includes details about the failed items.

failureCode (string) --
The status code of a failed item.

retryable (boolean) --
Indicates whether you can immediately retry a request for this item for a specified resource.













Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException


    :return: {
        'exclusions': {
            'string': {
                'arn': 'string',
                'title': 'string',
                'description': 'string',
                'recommendation': 'string',
                'scopes': [
                    {
                        'key': 'INSTANCE_ID'|'RULES_PACKAGE_ARN',
                        'value': 'string'
                    },
                ],
                'attributes': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            }
        },
        'failedItems': {
            'string': {
                'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                'retryable': True|False
            }
        }
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    
    """
    pass

def describe_findings(findingArns=None, locale=None):
    """
    Describes the findings that are specified by the ARNs of the findings.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes the findings that are specified by the ARNs of the findings.
    Expected Output:
    
    :example: response = client.describe_findings(
        findingArns=[
            'string',
        ],
        locale='EN_US'
    )
    
    
    :type findingArns: list
    :param findingArns: [REQUIRED]\nThe ARN that specifies the finding that you want to describe.\n\n(string) --\n\n

    :type locale: string
    :param locale: The locale into which you want to translate a finding description, recommendation, and the short description that identifies the finding.

    :rtype: dict

ReturnsResponse Syntax
{
    'findings': [
        {
            'arn': 'string',
            'schemaVersion': 123,
            'service': 'string',
            'serviceAttributes': {
                'schemaVersion': 123,
                'assessmentRunArn': 'string',
                'rulesPackageArn': 'string'
            },
            'assetType': 'ec2-instance',
            'assetAttributes': {
                'schemaVersion': 123,
                'agentId': 'string',
                'autoScalingGroup': 'string',
                'amiId': 'string',
                'hostname': 'string',
                'ipv4Addresses': [
                    'string',
                ],
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'networkInterfaces': [
                    {
                        'networkInterfaceId': 'string',
                        'subnetId': 'string',
                        'vpcId': 'string',
                        'privateDnsName': 'string',
                        'privateIpAddress': 'string',
                        'privateIpAddresses': [
                            {
                                'privateDnsName': 'string',
                                'privateIpAddress': 'string'
                            },
                        ],
                        'publicDnsName': 'string',
                        'publicIp': 'string',
                        'ipv6Addresses': [
                            'string',
                        ],
                        'securityGroups': [
                            {
                                'groupName': 'string',
                                'groupId': 'string'
                            },
                        ]
                    },
                ]
            },
            'id': 'string',
            'title': 'string',
            'description': 'string',
            'recommendation': 'string',
            'severity': 'Low'|'Medium'|'High'|'Informational'|'Undefined',
            'numericSeverity': 123.0,
            'confidence': 123,
            'indicatorOfCompromise': True|False,
            'attributes': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'userAttributes': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'updatedAt': datetime(2015, 1, 1)
        },
    ],
    'failedItems': {
        'string': {
            'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
            'retryable': True|False
        }
    }
}


Response Structure

(dict) --

findings (list) --
Information about the finding.

(dict) --
Contains information about an Amazon Inspector finding. This data type is used as the response element in the  DescribeFindings action.

arn (string) --
The ARN that specifies the finding.

schemaVersion (integer) --
The schema version of this data type.

service (string) --
The data element is set to "Inspector".

serviceAttributes (dict) --
This data type is used in the  Finding data type.

schemaVersion (integer) --
The schema version of this data type.

assessmentRunArn (string) --
The ARN of the assessment run during which the finding is generated.

rulesPackageArn (string) --
The ARN of the rules package that is used to generate the finding.



assetType (string) --
The type of the host from which the finding is generated.

assetAttributes (dict) --
A collection of attributes of the host from which the finding is generated.

schemaVersion (integer) --
The schema version of this data type.

agentId (string) --
The ID of the agent that is installed on the EC2 instance where the finding is generated.

autoScalingGroup (string) --
The Auto Scaling group of the EC2 instance where the finding is generated.

amiId (string) --
The ID of the Amazon Machine Image (AMI) that is installed on the EC2 instance where the finding is generated.

hostname (string) --
The hostname of the EC2 instance where the finding is generated.

ipv4Addresses (list) --
The list of IP v4 addresses of the EC2 instance where the finding is generated.

(string) --


tags (list) --
The tags related to the EC2 instance where the finding is generated.

(dict) --
A key and value pair. This data type is used as a request parameter in the  SetTagsForResource action and a response element in the  ListTagsForResource action.

key (string) --
A tag key.

value (string) --
A value assigned to a tag key.





networkInterfaces (list) --
An array of the network interfaces interacting with the EC2 instance where the finding is generated.

(dict) --
Contains information about the network interfaces interacting with an EC2 instance. This data type is used as one of the elements of the  AssetAttributes data type.

networkInterfaceId (string) --
The ID of the network interface.

subnetId (string) --
The ID of a subnet associated with the network interface.

vpcId (string) --
The ID of a VPC associated with the network interface.

privateDnsName (string) --
The name of a private DNS associated with the network interface.

privateIpAddress (string) --
The private IP address associated with the network interface.

privateIpAddresses (list) --
A list of the private IP addresses associated with the network interface. Includes the privateDnsName and privateIpAddress.

(dict) --
Contains information about a private IP address associated with a network interface. This data type is used as a response element in the  DescribeFindings action.

privateDnsName (string) --
The DNS name of the private IP address.

privateIpAddress (string) --
The full IP address of the network inteface.





publicDnsName (string) --
The name of a public DNS associated with the network interface.

publicIp (string) --
The public IP address from which the network interface is reachable.

ipv6Addresses (list) --
The IP addresses associated with the network interface.

(string) --


securityGroups (list) --
A list of the security groups associated with the network interface. Includes the groupId and groupName.

(dict) --
Contains information about a security group associated with a network interface. This data type is used as one of the elements of the  NetworkInterface data type.

groupName (string) --
The name of the security group.

groupId (string) --
The ID of the security group.











id (string) --
The ID of the finding.

title (string) --
The name of the finding.

description (string) --
The description of the finding.

recommendation (string) --
The recommendation for the finding.

severity (string) --
The finding severity. Values can be set to High, Medium, Low, and Informational.

numericSeverity (float) --
The numeric value of the finding severity.

confidence (integer) --
This data element is currently not used.

indicatorOfCompromise (boolean) --
This data element is currently not used.

attributes (list) --
The system-defined attributes for the finding.

(dict) --
This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

key (string) --
The attribute key.

value (string) --
The value assigned to the attribute key.





userAttributes (list) --
The user-defined attributes that are assigned to the finding.

(dict) --
This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

key (string) --
The attribute key.

value (string) --
The value assigned to the attribute key.





createdAt (datetime) --
The time when the finding was generated.

updatedAt (datetime) --
The time when  AddAttributesToFindings is called.





failedItems (dict) --
Finding details that cannot be described. An error code is provided for each failed item.

(string) --

(dict) --
Includes details about the failed items.

failureCode (string) --
The status code of a failed item.

retryable (boolean) --
Indicates whether you can immediately retry a request for this item for a specified resource.













Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException

Examples
Describes the findings that are specified by the ARNs of the findings.
response = client.describe_findings(
    findingArns=[
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4',
    ],
)

print(response)


Expected Output:
{
    'failedItems': {
    },
    'findings': [
        {
            'arn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4',
            'assetAttributes': {
                'ipv4Addresses': [
                ],
                'schemaVersion': 1,
            },
            'assetType': 'ec2-instance',
            'attributes': [
            ],
            'confidence': 10,
            'createdAt': datetime(2016, 3, 22, 20, 58, 21, 1, 82, 0),
            'description': 'Amazon Inspector did not find any potential security issues during this assessment.',
            'indicatorOfCompromise': False,
            'numericSeverity': 0,
            'recommendation': 'No remediation needed.',
            'schemaVersion': 1,
            'service': 'Inspector',
            'serviceAttributes': {
                'assessmentRunArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
                'rulesPackageArn': 'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP',
                'schemaVersion': 1,
            },
            'severity': 'Informational',
            'title': 'No potential security issues found',
            'updatedAt': datetime(2016, 3, 22, 20, 58, 21, 1, 82, 0),
            'userAttributes': [
            ],
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'findings': [
            {
                'arn': 'string',
                'schemaVersion': 123,
                'service': 'string',
                'serviceAttributes': {
                    'schemaVersion': 123,
                    'assessmentRunArn': 'string',
                    'rulesPackageArn': 'string'
                },
                'assetType': 'ec2-instance',
                'assetAttributes': {
                    'schemaVersion': 123,
                    'agentId': 'string',
                    'autoScalingGroup': 'string',
                    'amiId': 'string',
                    'hostname': 'string',
                    'ipv4Addresses': [
                        'string',
                    ],
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'networkInterfaces': [
                        {
                            'networkInterfaceId': 'string',
                            'subnetId': 'string',
                            'vpcId': 'string',
                            'privateDnsName': 'string',
                            'privateIpAddress': 'string',
                            'privateIpAddresses': [
                                {
                                    'privateDnsName': 'string',
                                    'privateIpAddress': 'string'
                                },
                            ],
                            'publicDnsName': 'string',
                            'publicIp': 'string',
                            'ipv6Addresses': [
                                'string',
                            ],
                            'securityGroups': [
                                {
                                    'groupName': 'string',
                                    'groupId': 'string'
                                },
                            ]
                        },
                    ]
                },
                'id': 'string',
                'title': 'string',
                'description': 'string',
                'recommendation': 'string',
                'severity': 'Low'|'Medium'|'High'|'Informational'|'Undefined',
                'numericSeverity': 123.0,
                'confidence': 123,
                'indicatorOfCompromise': True|False,
                'attributes': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'userAttributes': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'createdAt': datetime(2015, 1, 1),
                'updatedAt': datetime(2015, 1, 1)
            },
        ],
        'failedItems': {
            'string': {
                'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                'retryable': True|False
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_resource_groups(resourceGroupArns=None):
    """
    Describes the resource groups that are specified by the ARNs of the resource groups.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes the resource groups that are specified by the ARNs of the resource groups.
    Expected Output:
    
    :example: response = client.describe_resource_groups(
        resourceGroupArns=[
            'string',
        ]
    )
    
    
    :type resourceGroupArns: list
    :param resourceGroupArns: [REQUIRED]\nThe ARN that specifies the resource group that you want to describe.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'resourceGroups': [
        {
            'arn': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'createdAt': datetime(2015, 1, 1)
        },
    ],
    'failedItems': {
        'string': {
            'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
            'retryable': True|False
        }
    }
}


Response Structure

(dict) --
resourceGroups (list) --Information about a resource group.

(dict) --Contains information about a resource group. The resource group defines a set of tags that, when queried, identify the AWS resources that make up the assessment target. This data type is used as the response element in the  DescribeResourceGroups action.

arn (string) --The ARN of the resource group.

tags (list) --The tags (key and value pairs) of the resource group. This data type property is used in the  CreateResourceGroup action.

(dict) --This data type is used as one of the elements of the  ResourceGroup data type.

key (string) --A tag key.

value (string) --The value assigned to a tag key.





createdAt (datetime) --The time at which resource group is created.





failedItems (dict) --Resource group details that cannot be described. An error code is provided for each failed item.

(string) --
(dict) --Includes details about the failed items.

failureCode (string) --The status code of a failed item.

retryable (boolean) --Indicates whether you can immediately retry a request for this item for a specified resource.












Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException

Examples
Describes the resource groups that are specified by the ARNs of the resource groups.
response = client.describe_resource_groups(
    resourceGroupArns=[
        'arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI',
    ],
)

print(response)


Expected Output:
{
    'failedItems': {
    },
    'resourceGroups': [
        {
            'arn': 'arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI',
            'createdAt': datetime(2016, 3, 15, 20, 36, 31, 1, 75, 0),
            'tags': [
                {
                    'key': 'Name',
                    'value': 'example',
                },
            ],
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'resourceGroups': [
            {
                'arn': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'createdAt': datetime(2015, 1, 1)
            },
        ],
        'failedItems': {
            'string': {
                'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                'retryable': True|False
            }
        }
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    
    """
    pass

def describe_rules_packages(rulesPackageArns=None, locale=None):
    """
    Describes the rules packages that are specified by the ARNs of the rules packages.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Describes the rules packages that are specified by the ARNs of the rules packages.
    Expected Output:
    
    :example: response = client.describe_rules_packages(
        rulesPackageArns=[
            'string',
        ],
        locale='EN_US'
    )
    
    
    :type rulesPackageArns: list
    :param rulesPackageArns: [REQUIRED]\nThe ARN that specifies the rules package that you want to describe.\n\n(string) --\n\n

    :type locale: string
    :param locale: The locale that you want to translate a rules package description into.

    :rtype: dict

ReturnsResponse Syntax
{
    'rulesPackages': [
        {
            'arn': 'string',
            'name': 'string',
            'version': 'string',
            'provider': 'string',
            'description': 'string'
        },
    ],
    'failedItems': {
        'string': {
            'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
            'retryable': True|False
        }
    }
}


Response Structure

(dict) --

rulesPackages (list) --
Information about the rules package.

(dict) --
Contains information about an Amazon Inspector rules package. This data type is used as the response element in the  DescribeRulesPackages action.

arn (string) --
The ARN of the rules package.

name (string) --
The name of the rules package.

version (string) --
The version ID of the rules package.

provider (string) --
The provider of the rules package.

description (string) --
The description of the rules package.





failedItems (dict) --
Rules package details that cannot be described. An error code is provided for each failed item.

(string) --

(dict) --
Includes details about the failed items.

failureCode (string) --
The status code of a failed item.

retryable (boolean) --
Indicates whether you can immediately retry a request for this item for a specified resource.













Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException

Examples
Describes the rules packages that are specified by the ARNs of the rules packages.
response = client.describe_rules_packages(
    rulesPackageArns=[
        'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ',
    ],
)

print(response)


Expected Output:
{
    'failedItems': {
    },
    'rulesPackages': [
        {
            'version': '1.1',
            'name': 'Security Best Practices',
            'arn': 'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ',
            'description': 'The rules in this package help determine whether your systems are configured securely.',
            'provider': 'Amazon Web Services, Inc.',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'rulesPackages': [
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'provider': 'string',
                'description': 'string'
            },
        ],
        'failedItems': {
            'string': {
                'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                'retryable': True|False
            }
        }
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    
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

def get_assessment_report(assessmentRunArn=None, reportFileFormat=None, reportType=None):
    """
    Produces an assessment report that includes detailed and comprehensive results of a specified assessment run.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_assessment_report(
        assessmentRunArn='string',
        reportFileFormat='HTML'|'PDF',
        reportType='FINDING'|'FULL'
    )
    
    
    :type assessmentRunArn: string
    :param assessmentRunArn: [REQUIRED]\nThe ARN that specifies the assessment run for which you want to generate a report.\n

    :type reportFileFormat: string
    :param reportFileFormat: [REQUIRED]\nSpecifies the file format (html or pdf) of the assessment report that you want to generate.\n

    :type reportType: string
    :param reportType: [REQUIRED]\nSpecifies the type of the assessment report that you want to generate. There are two types of assessment reports: a finding report and a full report. For more information, see Assessment Reports .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'status': 'WORK_IN_PROGRESS'|'FAILED'|'COMPLETED',
    'url': 'string'
}


Response Structure

(dict) --

status (string) --
Specifies the status of the request to generate an assessment report.

url (string) --
Specifies the URL where you can find the generated assessment report. This parameter is only returned if the report is successfully generated.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException
Inspector.Client.exceptions.AssessmentRunInProgressException
Inspector.Client.exceptions.UnsupportedFeatureException
Inspector.Client.exceptions.ServiceTemporarilyUnavailableException


    :return: {
        'status': 'WORK_IN_PROGRESS'|'FAILED'|'COMPLETED',
        'url': 'string'
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.AssessmentRunInProgressException
    Inspector.Client.exceptions.UnsupportedFeatureException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

def get_exclusions_preview(assessmentTemplateArn=None, previewToken=None, nextToken=None, maxResults=None, locale=None):
    """
    Retrieves the exclusions preview (a list of ExclusionPreview objects) specified by the preview token. You can obtain the preview token by running the CreateExclusionsPreview API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_exclusions_preview(
        assessmentTemplateArn='string',
        previewToken='string',
        nextToken='string',
        maxResults=123,
        locale='EN_US'
    )
    
    
    :type assessmentTemplateArn: string
    :param assessmentTemplateArn: [REQUIRED]\nThe ARN that specifies the assessment template for which the exclusions preview was requested.\n

    :type previewToken: string
    :param previewToken: [REQUIRED]\nThe unique identifier associated of the exclusions preview.\n

    :type nextToken: string
    :param nextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the GetExclusionsPreviewRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.

    :type locale: string
    :param locale: The locale into which you want to translate the exclusion\'s title, description, and recommendation.

    :rtype: dict

ReturnsResponse Syntax
{
    'previewStatus': 'WORK_IN_PROGRESS'|'COMPLETED',
    'exclusionPreviews': [
        {
            'title': 'string',
            'description': 'string',
            'recommendation': 'string',
            'scopes': [
                {
                    'key': 'INSTANCE_ID'|'RULES_PACKAGE_ARN',
                    'value': 'string'
                },
            ],
            'attributes': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

previewStatus (string) --
Specifies the status of the request to generate an exclusions preview.

exclusionPreviews (list) --
Information about the exclusions included in the preview.

(dict) --
Contains information about what is excluded from an assessment run given the current state of the assessment template.

title (string) --
The name of the exclusion preview.

description (string) --
The description of the exclusion preview.

recommendation (string) --
The recommendation for the exclusion preview.

scopes (list) --
The AWS resources for which the exclusion preview pertains.

(dict) --
This data type contains key-value pairs that identify various Amazon resources.

key (string) --
The type of the scope.

value (string) --
The resource identifier for the specified scope type.





attributes (list) --
The system-defined attributes for the exclusion preview.

(dict) --
This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

key (string) --
The attribute key.

value (string) --
The value assigned to the attribute key.









nextToken (string) --
When a response is generated, if there is more data to be listed, this parameters is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException


    :return: {
        'previewStatus': 'WORK_IN_PROGRESS'|'COMPLETED',
        'exclusionPreviews': [
            {
                'title': 'string',
                'description': 'string',
                'recommendation': 'string',
                'scopes': [
                    {
                        'key': 'INSTANCE_ID'|'RULES_PACKAGE_ARN',
                        'value': 'string'
                    },
                ],
                'attributes': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    
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

def get_telemetry_metadata(assessmentRunArn=None):
    """
    Information about the data that is collected for the specified assessment run.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Information about the data that is collected for the specified assessment run.
    Expected Output:
    
    :example: response = client.get_telemetry_metadata(
        assessmentRunArn='string'
    )
    
    
    :type assessmentRunArn: string
    :param assessmentRunArn: [REQUIRED]\nThe ARN that specifies the assessment run that has the telemetry data that you want to obtain.\n

    :rtype: dict
ReturnsResponse Syntax{
    'telemetryMetadata': [
        {
            'messageType': 'string',
            'count': 123,
            'dataSize': 123
        },
    ]
}


Response Structure

(dict) --
telemetryMetadata (list) --Telemetry details.

(dict) --The metadata about the Amazon Inspector application data metrics collected by the agent. This data type is used as the response element in the  GetTelemetryMetadata action.

messageType (string) --A specific type of behavioral data that is collected by the agent.

count (integer) --The count of messages that the agent sends to the Amazon Inspector service.

dataSize (integer) --The data size of messages that the agent sends to the Amazon Inspector service.










Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException

Examples
Information about the data that is collected for the specified assessment run.
response = client.get_telemetry_metadata(
    assessmentRunArn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
)

print(response)


Expected Output:
{
    'telemetryMetadata': [
        {
            'count': 2,
            'dataSize': 345,
            'messageType': 'InspectorDuplicateProcess',
        },
        {
            'count': 3,
            'dataSize': 255,
            'messageType': 'InspectorTimeEventMsg',
        },
        {
            'count': 4,
            'dataSize': 1082,
            'messageType': 'InspectorNetworkInterface',
        },
        {
            'count': 2,
            'dataSize': 349,
            'messageType': 'InspectorDnsEntry',
        },
        {
            'count': 11,
            'dataSize': 2514,
            'messageType': 'InspectorDirectoryInfoMsg',
        },
        {
            'count': 1,
            'dataSize': 179,
            'messageType': 'InspectorTcpV6ListeningPort',
        },
        {
            'count': 101,
            'dataSize': 10949,
            'messageType': 'InspectorTerminal',
        },
        {
            'count': 26,
            'dataSize': 5916,
            'messageType': 'InspectorUser',
        },
        {
            'count': 282,
            'dataSize': 32148,
            'messageType': 'InspectorDynamicallyLoadedCodeModule',
        },
        {
            'count': 18,
            'dataSize': 10172,
            'messageType': 'InspectorCreateProcess',
        },
        {
            'count': 3,
            'dataSize': 8001,
            'messageType': 'InspectorProcessPerformance',
        },
        {
            'count': 1,
            'dataSize': 360,
            'messageType': 'InspectorOperatingSystem',
        },
        {
            'count': 6,
            'dataSize': 546,
            'messageType': 'InspectorStopProcess',
        },
        {
            'count': 1,
            'dataSize': 1553,
            'messageType': 'InspectorInstanceMetaData',
        },
        {
            'count': 2,
            'dataSize': 434,
            'messageType': 'InspectorTcpV4Connection',
        },
        {
            'count': 474,
            'dataSize': 2960322,
            'messageType': 'InspectorPackageInfo',
        },
        {
            'count': 3,
            'dataSize': 2235,
            'messageType': 'InspectorSystemPerformance',
        },
        {
            'count': 105,
            'dataSize': 46048,
            'messageType': 'InspectorCodeModule',
        },
        {
            'count': 1,
            'dataSize': 182,
            'messageType': 'InspectorUdpV6ListeningPort',
        },
        {
            'count': 2,
            'dataSize': 371,
            'messageType': 'InspectorUdpV4ListeningPort',
        },
        {
            'count': 18,
            'dataSize': 8362,
            'messageType': 'InspectorKernelModule',
        },
        {
            'count': 29,
            'dataSize': 48788,
            'messageType': 'InspectorConfigurationInfo',
        },
        {
            'count': 1,
            'dataSize': 79,
            'messageType': 'InspectorMonitoringStart',
        },
        {
            'count': 5,
            'dataSize': 0,
            'messageType': 'InspectorSplitMsgBegin',
        },
        {
            'count': 51,
            'dataSize': 4593,
            'messageType': 'InspectorGroup',
        },
        {
            'count': 1,
            'dataSize': 184,
            'messageType': 'InspectorTcpV4ListeningPort',
        },
        {
            'count': 1159,
            'dataSize': 3146579,
            'messageType': 'Total',
        },
        {
            'count': 5,
            'dataSize': 0,
            'messageType': 'InspectorSplitMsgEnd',
        },
        {
            'count': 1,
            'dataSize': 612,
            'messageType': 'InspectorLoadImageInProcess',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'telemetryMetadata': [
            {
                'messageType': 'string',
                'count': 123,
                'dataSize': 123
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

def list_assessment_run_agents(assessmentRunArn=None, filter=None, nextToken=None, maxResults=None):
    """
    Lists the agents of the assessment runs that are specified by the ARNs of the assessment runs.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists the agents of the assessment runs that are specified by the ARNs of the assessment runs.
    Expected Output:
    
    :example: response = client.list_assessment_run_agents(
        assessmentRunArn='string',
        filter={
            'agentHealths': [
                'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
            ],
            'agentHealthCodes': [
                'IDLE'|'RUNNING'|'SHUTDOWN'|'UNHEALTHY'|'THROTTLED'|'UNKNOWN',
            ]
        },
        nextToken='string',
        maxResults=123
    )
    
    
    :type assessmentRunArn: string
    :param assessmentRunArn: [REQUIRED]\nThe ARN that specifies the assessment run whose agents you want to list.\n

    :type filter: dict
    :param filter: You can use this parameter to specify a subset of data to be included in the action\'s response.\nFor a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.\n\nagentHealths (list) -- [REQUIRED]The current health state of the agent. Values can be set to HEALTHY or UNHEALTHY .\n\n(string) --\n\n\nagentHealthCodes (list) -- [REQUIRED]The detailed health state of the agent. Values can be set to IDLE , RUNNING , SHUTDOWN , UNHEALTHY , THROTTLED , and UNKNOWN .\n\n(string) --\n\n\n\n

    :type nextToken: string
    :param nextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListAssessmentRunAgents action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.

    :rtype: dict

ReturnsResponse Syntax
{
    'assessmentRunAgents': [
        {
            'agentId': 'string',
            'assessmentRunArn': 'string',
            'agentHealth': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
            'agentHealthCode': 'IDLE'|'RUNNING'|'SHUTDOWN'|'UNHEALTHY'|'THROTTLED'|'UNKNOWN',
            'agentHealthDetails': 'string',
            'autoScalingGroup': 'string',
            'telemetryMetadata': [
                {
                    'messageType': 'string',
                    'count': 123,
                    'dataSize': 123
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

assessmentRunAgents (list) --
A list of ARNs that specifies the agents returned by the action.

(dict) --
Contains information about an Amazon Inspector agent. This data type is used as a response element in the  ListAssessmentRunAgents action.

agentId (string) --
The AWS account of the EC2 instance where the agent is installed.

assessmentRunArn (string) --
The ARN of the assessment run that is associated with the agent.

agentHealth (string) --
The current health state of the agent.

agentHealthCode (string) --
The detailed health state of the agent.

agentHealthDetails (string) --
The description for the agent health code.

autoScalingGroup (string) --
The Auto Scaling group of the EC2 instance that is specified by the agent ID.

telemetryMetadata (list) --
The Amazon Inspector application data metrics that are collected by the agent.

(dict) --
The metadata about the Amazon Inspector application data metrics collected by the agent. This data type is used as the response element in the  GetTelemetryMetadata action.

messageType (string) --
A specific type of behavioral data that is collected by the agent.

count (integer) --
The count of messages that the agent sends to the Amazon Inspector service.

dataSize (integer) --
The data size of messages that the agent sends to the Amazon Inspector service.









nextToken (string) --
When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException

Examples
Lists the agents of the assessment runs that are specified by the ARNs of the assessment runs.
response = client.list_assessment_run_agents(
    assessmentRunArn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
    maxResults=123,
)

print(response)


Expected Output:
{
    'assessmentRunAgents': [
        {
            'agentHealth': 'HEALTHY',
            'agentHealthCode': 'RUNNING',
            'agentId': 'i-49113b93',
            'assessmentRunArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
            'telemetryMetadata': [
                {
                    'count': 2,
                    'dataSize': 345,
                    'messageType': 'InspectorDuplicateProcess',
                },
                {
                    'count': 3,
                    'dataSize': 255,
                    'messageType': 'InspectorTimeEventMsg',
                },
                {
                    'count': 4,
                    'dataSize': 1082,
                    'messageType': 'InspectorNetworkInterface',
                },
                {
                    'count': 2,
                    'dataSize': 349,
                    'messageType': 'InspectorDnsEntry',
                },
                {
                    'count': 11,
                    'dataSize': 2514,
                    'messageType': 'InspectorDirectoryInfoMsg',
                },
                {
                    'count': 1,
                    'dataSize': 179,
                    'messageType': 'InspectorTcpV6ListeningPort',
                },
                {
                    'count': 101,
                    'dataSize': 10949,
                    'messageType': 'InspectorTerminal',
                },
                {
                    'count': 26,
                    'dataSize': 5916,
                    'messageType': 'InspectorUser',
                },
                {
                    'count': 282,
                    'dataSize': 32148,
                    'messageType': 'InspectorDynamicallyLoadedCodeModule',
                },
                {
                    'count': 18,
                    'dataSize': 10172,
                    'messageType': 'InspectorCreateProcess',
                },
                {
                    'count': 3,
                    'dataSize': 8001,
                    'messageType': 'InspectorProcessPerformance',
                },
                {
                    'count': 1,
                    'dataSize': 360,
                    'messageType': 'InspectorOperatingSystem',
                },
                {
                    'count': 6,
                    'dataSize': 546,
                    'messageType': 'InspectorStopProcess',
                },
                {
                    'count': 1,
                    'dataSize': 1553,
                    'messageType': 'InspectorInstanceMetaData',
                },
                {
                    'count': 2,
                    'dataSize': 434,
                    'messageType': 'InspectorTcpV4Connection',
                },
                {
                    'count': 474,
                    'dataSize': 2960322,
                    'messageType': 'InspectorPackageInfo',
                },
                {
                    'count': 3,
                    'dataSize': 2235,
                    'messageType': 'InspectorSystemPerformance',
                },
                {
                    'count': 105,
                    'dataSize': 46048,
                    'messageType': 'InspectorCodeModule',
                },
                {
                    'count': 1,
                    'dataSize': 182,
                    'messageType': 'InspectorUdpV6ListeningPort',
                },
                {
                    'count': 2,
                    'dataSize': 371,
                    'messageType': 'InspectorUdpV4ListeningPort',
                },
                {
                    'count': 18,
                    'dataSize': 8362,
                    'messageType': 'InspectorKernelModule',
                },
                {
                    'count': 29,
                    'dataSize': 48788,
                    'messageType': 'InspectorConfigurationInfo',
                },
                {
                    'count': 1,
                    'dataSize': 79,
                    'messageType': 'InspectorMonitoringStart',
                },
                {
                    'count': 5,
                    'dataSize': 0,
                    'messageType': 'InspectorSplitMsgBegin',
                },
                {
                    'count': 51,
                    'dataSize': 4593,
                    'messageType': 'InspectorGroup',
                },
                {
                    'count': 1,
                    'dataSize': 184,
                    'messageType': 'InspectorTcpV4ListeningPort',
                },
                {
                    'count': 1159,
                    'dataSize': 3146579,
                    'messageType': 'Total',
                },
                {
                    'count': 5,
                    'dataSize': 0,
                    'messageType': 'InspectorSplitMsgEnd',
                },
                {
                    'count': 1,
                    'dataSize': 612,
                    'messageType': 'InspectorLoadImageInProcess',
                },
            ],
        },
    ],
    'nextToken': '1',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'assessmentRunAgents': [
            {
                'agentId': 'string',
                'assessmentRunArn': 'string',
                'agentHealth': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                'agentHealthCode': 'IDLE'|'RUNNING'|'SHUTDOWN'|'UNHEALTHY'|'THROTTLED'|'UNKNOWN',
                'agentHealthDetails': 'string',
                'autoScalingGroup': 'string',
                'telemetryMetadata': [
                    {
                        'messageType': 'string',
                        'count': 123,
                        'dataSize': 123
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    
    """
    pass

def list_assessment_runs(assessmentTemplateArns=None, filter=None, nextToken=None, maxResults=None):
    """
    Lists the assessment runs that correspond to the assessment templates that are specified by the ARNs of the assessment templates.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists the assessment runs that correspond to the assessment templates that are specified by the ARNs of the assessment templates.
    Expected Output:
    
    :example: response = client.list_assessment_runs(
        assessmentTemplateArns=[
            'string',
        ],
        filter={
            'namePattern': 'string',
            'states': [
                'CREATED'|'START_DATA_COLLECTION_PENDING'|'START_DATA_COLLECTION_IN_PROGRESS'|'COLLECTING_DATA'|'STOP_DATA_COLLECTION_PENDING'|'DATA_COLLECTED'|'START_EVALUATING_RULES_PENDING'|'EVALUATING_RULES'|'FAILED'|'ERROR'|'COMPLETED'|'COMPLETED_WITH_ERRORS'|'CANCELED',
            ],
            'durationRange': {
                'minSeconds': 123,
                'maxSeconds': 123
            },
            'rulesPackageArns': [
                'string',
            ],
            'startTimeRange': {
                'beginDate': datetime(2015, 1, 1),
                'endDate': datetime(2015, 1, 1)
            },
            'completionTimeRange': {
                'beginDate': datetime(2015, 1, 1),
                'endDate': datetime(2015, 1, 1)
            },
            'stateChangeTimeRange': {
                'beginDate': datetime(2015, 1, 1),
                'endDate': datetime(2015, 1, 1)
            }
        },
        nextToken='string',
        maxResults=123
    )
    
    
    :type assessmentTemplateArns: list
    :param assessmentTemplateArns: The ARNs that specify the assessment templates whose assessment runs you want to list.\n\n(string) --\n\n

    :type filter: dict
    :param filter: You can use this parameter to specify a subset of data to be included in the action\'s response.\nFor a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.\n\nnamePattern (string) --For a record to match a filter, an explicit value or a string containing a wildcard that is specified for this data type property must match the value of the assessmentRunName property of the AssessmentRun data type.\n\nstates (list) --For a record to match a filter, one of the values specified for this data type property must be the exact match of the value of the assessmentRunState property of the AssessmentRun data type.\n\n(string) --\n\n\ndurationRange (dict) --For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the durationInSeconds property of the AssessmentRun data type.\n\nminSeconds (integer) --The minimum value of the duration range. Must be greater than zero.\n\nmaxSeconds (integer) --The maximum value of the duration range. Must be less than or equal to 604800 seconds (1 week).\n\n\n\nrulesPackageArns (list) --For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the rulesPackages property of the AssessmentRun data type.\n\n(string) --\n\n\nstartTimeRange (dict) --For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the startTime property of the AssessmentRun data type.\n\nbeginDate (datetime) --The minimum value of the timestamp range.\n\nendDate (datetime) --The maximum value of the timestamp range.\n\n\n\ncompletionTimeRange (dict) --For a record to match a filter, the value that is specified for this data type property must inclusively match any value between the specified minimum and maximum values of the completedAt property of the AssessmentRun data type.\n\nbeginDate (datetime) --The minimum value of the timestamp range.\n\nendDate (datetime) --The maximum value of the timestamp range.\n\n\n\nstateChangeTimeRange (dict) --For a record to match a filter, the value that is specified for this data type property must match the stateChangedAt property of the AssessmentRun data type.\n\nbeginDate (datetime) --The minimum value of the timestamp range.\n\nendDate (datetime) --The maximum value of the timestamp range.\n\n\n\n\n

    :type nextToken: string
    :param nextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListAssessmentRuns action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.

    :rtype: dict

ReturnsResponse Syntax
{
    'assessmentRunArns': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

assessmentRunArns (list) --
A list of ARNs that specifies the assessment runs that are returned by the action.

(string) --


nextToken (string) --
When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException

Examples
Lists the assessment runs that correspond to the assessment templates that are specified by the ARNs of the assessment templates.
response = client.list_assessment_runs(
    assessmentTemplateArns=[
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw',
    ],
    maxResults=123,
)

print(response)


Expected Output:
{
    'assessmentRunArns': [
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-v5D6fI3v',
    ],
    'nextToken': '1',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'assessmentRunArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_assessment_targets(filter=None, nextToken=None, maxResults=None):
    """
    Lists the ARNs of the assessment targets within this AWS account. For more information about assessment targets, see Amazon Inspector Assessment Targets .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists the ARNs of the assessment targets within this AWS account.
    Expected Output:
    
    :example: response = client.list_assessment_targets(
        filter={
            'assessmentTargetNamePattern': 'string'
        },
        nextToken='string',
        maxResults=123
    )
    
    
    :type filter: dict
    :param filter: You can use this parameter to specify a subset of data to be included in the action\'s response.\nFor a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.\n\nassessmentTargetNamePattern (string) --For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the assessmentTargetName property of the AssessmentTarget data type.\n\n\n

    :type nextToken: string
    :param nextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListAssessmentTargets action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

    :rtype: dict

ReturnsResponse Syntax
{
    'assessmentTargetArns': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

assessmentTargetArns (list) --
A list of ARNs that specifies the assessment targets that are returned by the action.

(string) --


nextToken (string) --
When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException

Examples
Lists the ARNs of the assessment targets within this AWS account.
response = client.list_assessment_targets(
    maxResults=123,
)

print(response)


Expected Output:
{
    'assessmentTargetArns': [
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
    ],
    'nextToken': '1',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'assessmentTargetArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_assessment_templates(assessmentTargetArns=None, filter=None, nextToken=None, maxResults=None):
    """
    Lists the assessment templates that correspond to the assessment targets that are specified by the ARNs of the assessment targets.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists the assessment templates that correspond to the assessment targets that are specified by the ARNs of the assessment targets.
    Expected Output:
    
    :example: response = client.list_assessment_templates(
        assessmentTargetArns=[
            'string',
        ],
        filter={
            'namePattern': 'string',
            'durationRange': {
                'minSeconds': 123,
                'maxSeconds': 123
            },
            'rulesPackageArns': [
                'string',
            ]
        },
        nextToken='string',
        maxResults=123
    )
    
    
    :type assessmentTargetArns: list
    :param assessmentTargetArns: A list of ARNs that specifies the assessment targets whose assessment templates you want to list.\n\n(string) --\n\n

    :type filter: dict
    :param filter: You can use this parameter to specify a subset of data to be included in the action\'s response.\nFor a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.\n\nnamePattern (string) --For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the assessmentTemplateName property of the AssessmentTemplate data type.\n\ndurationRange (dict) --For a record to match a filter, the value specified for this data type property must inclusively match any value between the specified minimum and maximum values of the durationInSeconds property of the AssessmentTemplate data type.\n\nminSeconds (integer) --The minimum value of the duration range. Must be greater than zero.\n\nmaxSeconds (integer) --The maximum value of the duration range. Must be less than or equal to 604800 seconds (1 week).\n\n\n\nrulesPackageArns (list) --For a record to match a filter, the values that are specified for this data type property must be contained in the list of values of the rulesPackageArns property of the AssessmentTemplate data type.\n\n(string) --\n\n\n\n

    :type nextToken: string
    :param nextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListAssessmentTemplates action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

    :rtype: dict

ReturnsResponse Syntax
{
    'assessmentTemplateArns': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

assessmentTemplateArns (list) --
A list of ARNs that specifies the assessment templates returned by the action.

(string) --


nextToken (string) --
When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException

Examples
Lists the assessment templates that correspond to the assessment targets that are specified by the ARNs of the assessment targets.
response = client.list_assessment_templates(
    assessmentTargetArns=[
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
    ],
    maxResults=123,
)

print(response)


Expected Output:
{
    'assessmentTemplateArns': [
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw',
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-Uza6ihLh',
    ],
    'nextToken': '1',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'assessmentTemplateArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_event_subscriptions(resourceArn=None, nextToken=None, maxResults=None):
    """
    Lists all the event subscriptions for the assessment template that is specified by the ARN of the assessment template. For more information, see  SubscribeToEvent and  UnsubscribeFromEvent .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists all the event subscriptions for the assessment template that is specified by the ARN of the assessment template.
    Expected Output:
    
    :example: response = client.list_event_subscriptions(
        resourceArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceArn: string
    :param resourceArn: The ARN of the assessment template for which you want to list the existing event subscriptions.

    :type nextToken: string
    :param nextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListEventSubscriptions action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

    :rtype: dict

ReturnsResponse Syntax
{
    'subscriptions': [
        {
            'resourceArn': 'string',
            'topicArn': 'string',
            'eventSubscriptions': [
                {
                    'event': 'ASSESSMENT_RUN_STARTED'|'ASSESSMENT_RUN_COMPLETED'|'ASSESSMENT_RUN_STATE_CHANGED'|'FINDING_REPORTED'|'OTHER',
                    'subscribedAt': datetime(2015, 1, 1)
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

subscriptions (list) --
Details of the returned event subscriptions.

(dict) --
This data type is used as a response element in the  ListEventSubscriptions action.

resourceArn (string) --
The ARN of the assessment template that is used during the event for which the SNS notification is sent.

topicArn (string) --
The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS notifications are sent.

eventSubscriptions (list) --
The list of existing event subscriptions.

(dict) --
This data type is used in the  Subscription data type.

event (string) --
The event for which Amazon Simple Notification Service (SNS) notifications are sent.

subscribedAt (datetime) --
The time at which  SubscribeToEvent is called.









nextToken (string) --
When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException

Examples
Lists all the event subscriptions for the assessment template that is specified by the ARN of the assessment template.
response = client.list_event_subscriptions(
    maxResults=123,
    resourceArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0',
)

print(response)


Expected Output:
{
    'nextToken': '1',
    'subscriptions': [
        {
            'eventSubscriptions': [
                {
                    'event': 'ASSESSMENT_RUN_COMPLETED',
                    'subscribedAt': datetime(2016, 3, 31, 20, 17, 20, 3, 91, 0),
                },
            ],
            'resourceArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0',
            'topicArn': 'arn:aws:sns:us-west-2:123456789012:exampletopic',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'subscriptions': [
            {
                'resourceArn': 'string',
                'topicArn': 'string',
                'eventSubscriptions': [
                    {
                        'event': 'ASSESSMENT_RUN_STARTED'|'ASSESSMENT_RUN_COMPLETED'|'ASSESSMENT_RUN_STATE_CHANGED'|'FINDING_REPORTED'|'OTHER',
                        'subscribedAt': datetime(2015, 1, 1)
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    
    """
    pass

def list_exclusions(assessmentRunArn=None, nextToken=None, maxResults=None):
    """
    List exclusions that are generated by the assessment run.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_exclusions(
        assessmentRunArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type assessmentRunArn: string
    :param assessmentRunArn: [REQUIRED]\nThe ARN of the assessment run that generated the exclusions that you want to list.\n

    :type nextToken: string
    :param nextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListExclusionsRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.

    :rtype: dict

ReturnsResponse Syntax
{
    'exclusionArns': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

exclusionArns (list) --
A list of exclusions\' ARNs returned by the action.

(string) --


nextToken (string) --
When a response is generated, if there is more data to be listed, this parameters is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException


    :return: {
        'exclusionArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_findings(assessmentRunArns=None, filter=None, nextToken=None, maxResults=None):
    """
    Lists findings that are generated by the assessment runs that are specified by the ARNs of the assessment runs.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists findings that are generated by the assessment runs that are specified by the ARNs of the assessment runs.
    Expected Output:
    
    :example: response = client.list_findings(
        assessmentRunArns=[
            'string',
        ],
        filter={
            'agentIds': [
                'string',
            ],
            'autoScalingGroups': [
                'string',
            ],
            'ruleNames': [
                'string',
            ],
            'severities': [
                'Low'|'Medium'|'High'|'Informational'|'Undefined',
            ],
            'rulesPackageArns': [
                'string',
            ],
            'attributes': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'userAttributes': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'creationTimeRange': {
                'beginDate': datetime(2015, 1, 1),
                'endDate': datetime(2015, 1, 1)
            }
        },
        nextToken='string',
        maxResults=123
    )
    
    
    :type assessmentRunArns: list
    :param assessmentRunArns: The ARNs of the assessment runs that generate the findings that you want to list.\n\n(string) --\n\n

    :type filter: dict
    :param filter: You can use this parameter to specify a subset of data to be included in the action\'s response.\nFor a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.\n\nagentIds (list) --For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the agentId property of the Finding data type.\n\n(string) --\n\n\nautoScalingGroups (list) --For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the autoScalingGroup property of the Finding data type.\n\n(string) --\n\n\nruleNames (list) --For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the ruleName property of the Finding data type.\n\n(string) --\n\n\nseverities (list) --For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the severity property of the Finding data type.\n\n(string) --\n\n\nrulesPackageArns (list) --For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the rulesPackageArn property of the Finding data type.\n\n(string) --\n\n\nattributes (list) --For a record to match a filter, the list of values that are specified for this data type property must be contained in the list of values of the attributes property of the Finding data type.\n\n(dict) --This data type is used as a request parameter in the AddAttributesToFindings and CreateAssessmentTemplate actions.\n\nkey (string) -- [REQUIRED]The attribute key.\n\nvalue (string) --The value assigned to the attribute key.\n\n\n\n\n\nuserAttributes (list) --For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the userAttributes property of the Finding data type.\n\n(dict) --This data type is used as a request parameter in the AddAttributesToFindings and CreateAssessmentTemplate actions.\n\nkey (string) -- [REQUIRED]The attribute key.\n\nvalue (string) --The value assigned to the attribute key.\n\n\n\n\n\ncreationTimeRange (dict) --The time range during which the finding is generated.\n\nbeginDate (datetime) --The minimum value of the timestamp range.\n\nendDate (datetime) --The maximum value of the timestamp range.\n\n\n\n\n

    :type nextToken: string
    :param nextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListFindings action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

    :rtype: dict

ReturnsResponse Syntax
{
    'findingArns': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

findingArns (list) --
A list of ARNs that specifies the findings returned by the action.

(string) --


nextToken (string) --
When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException

Examples
Lists findings that are generated by the assessment runs that are specified by the ARNs of the assessment runs.
response = client.list_findings(
    assessmentRunArns=[
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE',
    ],
    maxResults=123,
)

print(response)


Expected Output:
{
    'findingArns': [
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4',
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-v5D6fI3v/finding/0-tyvmqBLy',
    ],
    'nextToken': '1',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'findingArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_rules_packages(nextToken=None, maxResults=None):
    """
    Lists all available Amazon Inspector rules packages.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists all available Amazon Inspector rules packages.
    Expected Output:
    
    :example: response = client.list_rules_packages(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListRulesPackages action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

    :rtype: dict

ReturnsResponse Syntax
{
    'rulesPackageArns': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

rulesPackageArns (list) --
The list of ARNs that specifies the rules packages returned by the action.

(string) --


nextToken (string) --
When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException

Examples
Lists all available Amazon Inspector rules packages.
response = client.list_rules_packages(
    maxResults=123,
)

print(response)


Expected Output:
{
    'nextToken': '1',
    'rulesPackageArns': [
        'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p',
        'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-H5hpSawc',
        'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ',
        'arn:aws:inspector:us-west-2:758058086616:rulespackage/0-vg5GGHSD',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'rulesPackageArns': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Lists all tags associated with an assessment template.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Lists all tags associated with an assessment template.
    Expected Output:
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN that specifies the assessment template whose tags you want to list.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ]
}


Response Structure

(dict) --
tags (list) --A collection of key and value pairs.

(dict) --A key and value pair. This data type is used as a request parameter in the  SetTagsForResource action and a response element in the  ListTagsForResource action.

key (string) --A tag key.

value (string) --A value assigned to a tag key.










Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException

Examples
Lists all tags associated with an assessment template.
response = client.list_tags_for_resource(
    resourceArn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-gcwFliYu',
)

print(response)


Expected Output:
{
    'tags': [
        {
            'key': 'Name',
            'value': 'Example',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
    
    
    """
    pass

def preview_agents(previewAgentsArn=None, nextToken=None, maxResults=None):
    """
    Previews the agents installed on the EC2 instances that are part of the specified assessment target.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Previews the agents installed on the EC2 instances that are part of the specified assessment target.
    Expected Output:
    
    :example: response = client.preview_agents(
        previewAgentsArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type previewAgentsArn: string
    :param previewAgentsArn: [REQUIRED]\nThe ARN of the assessment target whose agents you want to preview.\n

    :type nextToken: string
    :param nextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the PreviewAgents action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.

    :rtype: dict

ReturnsResponse Syntax
{
    'agentPreviews': [
        {
            'hostname': 'string',
            'agentId': 'string',
            'autoScalingGroup': 'string',
            'agentHealth': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
            'agentVersion': 'string',
            'operatingSystem': 'string',
            'kernelVersion': 'string',
            'ipv4Address': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

agentPreviews (list) --
The resulting list of agents.

(dict) --
Used as a response element in the  PreviewAgents action.

hostname (string) --
The hostname of the EC2 instance on which the Amazon Inspector Agent is installed.

agentId (string) --
The ID of the EC2 instance where the agent is installed.

autoScalingGroup (string) --
The Auto Scaling group for the EC2 instance where the agent is installed.

agentHealth (string) --
The health status of the Amazon Inspector Agent.

agentVersion (string) --
The version of the Amazon Inspector Agent.

operatingSystem (string) --
The operating system running on the EC2 instance on which the Amazon Inspector Agent is installed.

kernelVersion (string) --
The kernel version of the operating system running on the EC2 instance on which the Amazon Inspector Agent is installed.

ipv4Address (string) --
The IP address of the EC2 instance on which the Amazon Inspector Agent is installed.





nextToken (string) --
When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException
Inspector.Client.exceptions.InvalidCrossAccountRoleException

Examples
Previews the agents installed on the EC2 instances that are part of the specified assessment target.
response = client.preview_agents(
    maxResults=123,
    previewAgentsArn='arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq',
)

print(response)


Expected Output:
{
    'agentPreviews': [
        {
            'agentId': 'i-49113b93',
        },
    ],
    'nextToken': '1',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'agentPreviews': [
            {
                'hostname': 'string',
                'agentId': 'string',
                'autoScalingGroup': 'string',
                'agentHealth': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                'agentVersion': 'string',
                'operatingSystem': 'string',
                'kernelVersion': 'string',
                'ipv4Address': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.InvalidCrossAccountRoleException
    
    """
    pass

def register_cross_account_access_role(roleArn=None):
    """
    Registers the IAM role that grants Amazon Inspector access to AWS Services needed to perform security assessments.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Registers the IAM role that Amazon Inspector uses to list your EC2 instances at the start of the assessment run or when you call the PreviewAgents action.
    Expected Output:
    
    :example: response = client.register_cross_account_access_role(
        roleArn='string'
    )
    
    
    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe ARN of the IAM role that grants Amazon Inspector access to AWS Services needed to perform security assessments.\n

    :return: response = client.register_cross_account_access_role(
        roleArn='arn:aws:iam::123456789012:role/inspector',
    )
    
    print(response)
    
    
    """
    pass

def remove_attributes_from_findings(findingArns=None, attributeKeys=None):
    """
    Removes entire attributes (key and value pairs) from the findings that are specified by the ARNs of the findings where an attribute with the specified key exists.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Removes entire attributes (key and value pairs) from the findings that are specified by the ARNs of the findings where an attribute with the specified key exists.
    Expected Output:
    
    :example: response = client.remove_attributes_from_findings(
        findingArns=[
            'string',
        ],
        attributeKeys=[
            'string',
        ]
    )
    
    
    :type findingArns: list
    :param findingArns: [REQUIRED]\nThe ARNs that specify the findings that you want to remove attributes from.\n\n(string) --\n\n

    :type attributeKeys: list
    :param attributeKeys: [REQUIRED]\nThe array of attribute keys that you want to remove from specified findings.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'failedItems': {
        'string': {
            'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
            'retryable': True|False
        }
    }
}


Response Structure

(dict) --

failedItems (dict) --
Attributes details that cannot be described. An error code is provided for each failed item.

(string) --

(dict) --
Includes details about the failed items.

failureCode (string) --
The status code of a failed item.

retryable (boolean) --
Indicates whether you can immediately retry a request for this item for a specified resource.













Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException
Inspector.Client.exceptions.ServiceTemporarilyUnavailableException

Examples
Removes entire attributes (key and value pairs) from the findings that are specified by the ARNs of the findings where an attribute with the specified key exists.
response = client.remove_attributes_from_findings(
    attributeKeys=[
        'key=Example,value=example',
    ],
    findingArns=[
        'arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU',
    ],
)

print(response)


Expected Output:
{
    'failedItems': {
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'failedItems': {
            'string': {
                'failureCode': 'INVALID_ARN'|'DUPLICATE_ARN'|'ITEM_DOES_NOT_EXIST'|'ACCESS_DENIED'|'LIMIT_EXCEEDED'|'INTERNAL_ERROR',
                'retryable': True|False
            }
        }
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

def set_tags_for_resource(resourceArn=None, tags=None):
    """
    Sets tags (key and value pairs) to the assessment template that is specified by the ARN of the assessment template.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Sets tags (key and value pairs) to the assessment template that is specified by the ARN of the assessment template.
    Expected Output:
    
    :example: response = client.set_tags_for_resource(
        resourceArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the assessment template that you want to set tags to.\n

    :type tags: list
    :param tags: A collection of key and value pairs that you want to set to the assessment template.\n\n(dict) --A key and value pair. This data type is used as a request parameter in the SetTagsForResource action and a response element in the ListTagsForResource action.\n\nkey (string) -- [REQUIRED]A tag key.\n\nvalue (string) --A value assigned to a tag key.\n\n\n\n\n

    :return: response = client.set_tags_for_resource(
        resourceArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0',
        tags=[
            {
                'key': 'Example',
                'value': 'example',
            },
        ],
    )
    
    print(response)
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

def start_assessment_run(assessmentTemplateArn=None, assessmentRunName=None):
    """
    Starts the assessment run specified by the ARN of the assessment template. For this API to function properly, you must not exceed the limit of running up to 500 concurrent agents per AWS account.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Starts the assessment run specified by the ARN of the assessment template. For this API to function properly, you must not exceed the limit of running up to 500 concurrent agents per AWS account.
    Expected Output:
    
    :example: response = client.start_assessment_run(
        assessmentTemplateArn='string',
        assessmentRunName='string'
    )
    
    
    :type assessmentTemplateArn: string
    :param assessmentTemplateArn: [REQUIRED]\nThe ARN of the assessment template of the assessment run that you want to start.\n

    :type assessmentRunName: string
    :param assessmentRunName: You can specify the name for the assessment run. The name must be unique for the assessment template whose ARN is used to start the assessment run.

    :rtype: dict

ReturnsResponse Syntax
{
    'assessmentRunArn': 'string'
}


Response Structure

(dict) --

assessmentRunArn (string) --
The ARN of the assessment run that has been started.







Exceptions

Inspector.Client.exceptions.InternalException
Inspector.Client.exceptions.InvalidInputException
Inspector.Client.exceptions.LimitExceededException
Inspector.Client.exceptions.AccessDeniedException
Inspector.Client.exceptions.NoSuchEntityException
Inspector.Client.exceptions.InvalidCrossAccountRoleException
Inspector.Client.exceptions.AgentsAlreadyRunningAssessmentException
Inspector.Client.exceptions.ServiceTemporarilyUnavailableException

Examples
Starts the assessment run specified by the ARN of the assessment template. For this API to function properly, you must not exceed the limit of running up to 500 concurrent agents per AWS account.
response = client.start_assessment_run(
    assessmentRunName='examplerun',
    assessmentTemplateArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T',
)

print(response)


Expected Output:
{
    'assessmentRunArn': 'arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-jOoroxyY',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'assessmentRunArn': 'string'
    }
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.LimitExceededException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.InvalidCrossAccountRoleException
    Inspector.Client.exceptions.AgentsAlreadyRunningAssessmentException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

def stop_assessment_run(assessmentRunArn=None, stopAction=None):
    """
    Stops the assessment run that is specified by the ARN of the assessment run.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Stops the assessment run that is specified by the ARN of the assessment run.
    Expected Output:
    
    :example: response = client.stop_assessment_run(
        assessmentRunArn='string',
        stopAction='START_EVALUATION'|'SKIP_EVALUATION'
    )
    
    
    :type assessmentRunArn: string
    :param assessmentRunArn: [REQUIRED]\nThe ARN of the assessment run that you want to stop.\n

    :type stopAction: string
    :param stopAction: An input option that can be set to either START_EVALUATION or SKIP_EVALUATION. START_EVALUATION (the default value), stops the AWS agent from collecting data and begins the results evaluation and the findings generation process. SKIP_EVALUATION cancels the assessment run immediately, after which no findings are generated.

    :return: response = client.stop_assessment_run(
        assessmentRunArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-11LMTAVe',
    )
    
    print(response)
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

def subscribe_to_event(resourceArn=None, event=None, topicArn=None):
    """
    Enables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Enables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.
    Expected Output:
    
    :example: response = client.subscribe_to_event(
        resourceArn='string',
        event='ASSESSMENT_RUN_STARTED'|'ASSESSMENT_RUN_COMPLETED'|'ASSESSMENT_RUN_STATE_CHANGED'|'FINDING_REPORTED'|'OTHER',
        topicArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the assessment template that is used during the event for which you want to receive SNS notifications.\n

    :type event: string
    :param event: [REQUIRED]\nThe event for which you want to receive SNS notifications.\n

    :type topicArn: string
    :param topicArn: [REQUIRED]\nThe ARN of the SNS topic to which the SNS notifications are sent.\n

    :return: response = client.subscribe_to_event(
        event='ASSESSMENT_RUN_COMPLETED',
        resourceArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0',
        topicArn='arn:aws:sns:us-west-2:123456789012:exampletopic',
    )
    
    print(response)
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.LimitExceededException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

def unsubscribe_from_event(resourceArn=None, event=None, topicArn=None):
    """
    Disables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Disables the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic.
    Expected Output:
    
    :example: response = client.unsubscribe_from_event(
        resourceArn='string',
        event='ASSESSMENT_RUN_STARTED'|'ASSESSMENT_RUN_COMPLETED'|'ASSESSMENT_RUN_STATE_CHANGED'|'FINDING_REPORTED'|'OTHER',
        topicArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the assessment template that is used during the event for which you want to stop receiving SNS notifications.\n

    :type event: string
    :param event: [REQUIRED]\nThe event for which you want to stop receiving SNS notifications.\n

    :type topicArn: string
    :param topicArn: [REQUIRED]\nThe ARN of the SNS topic to which SNS notifications are sent.\n

    :return: response = client.unsubscribe_from_event(
        event='ASSESSMENT_RUN_COMPLETED',
        resourceArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0',
        topicArn='arn:aws:sns:us-west-2:123456789012:exampletopic',
    )
    
    print(response)
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

def update_assessment_target(assessmentTargetArn=None, assessmentTargetName=None, resourceGroupArn=None):
    """
    Updates the assessment target that is specified by the ARN of the assessment target.
    If resourceGroupArn is not specified, all EC2 instances in the current AWS account and region are included in the assessment target.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Updates the assessment target that is specified by the ARN of the assessment target.
    Expected Output:
    
    :example: response = client.update_assessment_target(
        assessmentTargetArn='string',
        assessmentTargetName='string',
        resourceGroupArn='string'
    )
    
    
    :type assessmentTargetArn: string
    :param assessmentTargetArn: [REQUIRED]\nThe ARN of the assessment target that you want to update.\n

    :type assessmentTargetName: string
    :param assessmentTargetName: [REQUIRED]\nThe name of the assessment target that you want to update.\n

    :type resourceGroupArn: string
    :param resourceGroupArn: The ARN of the resource group that is used to specify the new resource group to associate with the assessment target.

    :return: response = client.update_assessment_target(
        assessmentTargetArn='arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX',
        assessmentTargetName='Example',
        resourceGroupArn='arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-yNbgL5Pt',
    )
    
    print(response)
    
    
    :returns: 
    Inspector.Client.exceptions.InternalException
    Inspector.Client.exceptions.InvalidInputException
    Inspector.Client.exceptions.AccessDeniedException
    Inspector.Client.exceptions.NoSuchEntityException
    Inspector.Client.exceptions.ServiceTemporarilyUnavailableException
    
    """
    pass

