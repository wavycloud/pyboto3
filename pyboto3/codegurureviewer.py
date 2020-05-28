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

def associate_repository(Repository=None, ClientRequestToken=None):
    """
    Associates an AWS CodeCommit repository with Amazon CodeGuru Reviewer. When you associate an AWS CodeCommit repository with Amazon CodeGuru Reviewer, Amazon CodeGuru Reviewer will provide recommendations for each pull request raised within the repository. You can view recommendations in the AWS CodeCommit repository.
    You can associate a GitHub repository using the Amazon CodeGuru Reviewer console.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_repository(
        Repository={
            'CodeCommit': {
                'Name': 'string'
            },
            'Bitbucket': {
                'Name': 'string',
                'ConnectionArn': 'string',
                'Owner': 'string'
            }
        },
        ClientRequestToken='string'
    )
    
    
    :type Repository: dict
    :param Repository: [REQUIRED]\nThe repository to associate.\n\nCodeCommit (dict) --Information about an AWS CodeCommit repository.\n\nName (string) -- [REQUIRED]The name of the AWS CodeCommit repository.\n\n\n\nBitbucket (dict) --Information about a Bitbucket Cloud repository.\n\nName (string) -- [REQUIRED]The name of the third party source repository.\n\nConnectionArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) identifying the repository connection.\n\nOwner (string) -- [REQUIRED]The username of the owner of the repository.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.\nTo add a new repository association, this parameter specifies a unique identifier for the new repository association that helps ensure idempotency.\nIf you use the AWS CLI or one of the AWS SDKs to call this operation, you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes that in the request. If you don\'t use the SDK and instead generate a raw HTTP request to the Secrets Manager service endpoint, you must generate a ClientRequestToken yourself for new versions and include that value in the request.\nYou typically interact with this value if you implement your own retry logic and want to ensure that a given repository association is not created twice. We recommend that you generate a UUID-type value to ensure uniqueness within the specified repository association.\nAmazon CodeGuru Reviewer uses this value to prevent the accidental creation of duplicate repository associations if there are failures and retries.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RepositoryAssociation': {
        'AssociationId': 'string',
        'AssociationArn': 'string',
        'ConnectionArn': 'string',
        'Name': 'string',
        'Owner': 'string',
        'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
        'State': 'Associated'|'Associating'|'Failed'|'Disassociating',
        'StateReason': 'string',
        'LastUpdatedTimeStamp': datetime(2015, 1, 1),
        'CreatedTimeStamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

RepositoryAssociation (dict) --
Information about the repository association.

AssociationId (string) --
The ID of the repository association.

AssociationArn (string) --
The Amazon Resource Name (ARN) identifying the repository association.

ConnectionArn (string) --
The Amazon Resource Name (ARN) identifying the repository connection.

Name (string) --
The name of the repository.

Owner (string) --
The owner of the repository.

ProviderType (string) --
The provider type of the repository association.

State (string) --
The state of the repository association.

StateReason (string) --
A description of why the repository association is in the current state.

LastUpdatedTimeStamp (datetime) --
The time, in milliseconds since the epoch, when the repository association was last updated.

CreatedTimeStamp (datetime) --
The time, in milliseconds since the epoch, when the repository association was created.









Exceptions

CodeGuruReviewer.Client.exceptions.InternalServerException
CodeGuruReviewer.Client.exceptions.ValidationException
CodeGuruReviewer.Client.exceptions.AccessDeniedException
CodeGuruReviewer.Client.exceptions.ConflictException
CodeGuruReviewer.Client.exceptions.ThrottlingException


    :return: {
        'RepositoryAssociation': {
            'AssociationId': 'string',
            'AssociationArn': 'string',
            'ConnectionArn': 'string',
            'Name': 'string',
            'Owner': 'string',
            'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
            'State': 'Associated'|'Associating'|'Failed'|'Disassociating',
            'StateReason': 'string',
            'LastUpdatedTimeStamp': datetime(2015, 1, 1),
            'CreatedTimeStamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CodeGuruReviewer.Client.exceptions.InternalServerException
    CodeGuruReviewer.Client.exceptions.ValidationException
    CodeGuruReviewer.Client.exceptions.AccessDeniedException
    CodeGuruReviewer.Client.exceptions.ConflictException
    CodeGuruReviewer.Client.exceptions.ThrottlingException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def describe_code_review(CodeReviewArn=None):
    """
    Returns the metadaata associated with the code review along with its status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_code_review(
        CodeReviewArn='string'
    )
    
    
    :type CodeReviewArn: string
    :param CodeReviewArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the code review to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'CodeReview': {
        'Name': 'string',
        'CodeReviewArn': 'string',
        'RepositoryName': 'string',
        'Owner': 'string',
        'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
        'State': 'Completed'|'Pending'|'Failed'|'Deleting',
        'StateReason': 'string',
        'CreatedTimeStamp': datetime(2015, 1, 1),
        'LastUpdatedTimeStamp': datetime(2015, 1, 1),
        'Type': 'PullRequest',
        'PullRequestId': 'string',
        'SourceCodeType': {
            'CommitDiff': {
                'SourceCommit': 'string',
                'DestinationCommit': 'string'
            }
        },
        'Metrics': {
            'MeteredLinesOfCodeCount': 123,
            'FindingsCount': 123
        }
    }
}


Response Structure

(dict) --
CodeReview (dict) --Information about the code review.

Name (string) --The name of the code review.

CodeReviewArn (string) --The Amazon Resource Name (ARN) of the code review to describe.

RepositoryName (string) --The name of the repository.

Owner (string) --The owner of the repository.

ProviderType (string) --The provider type of the repository association.

State (string) --The state of the code review.

StateReason (string) --The reason for the state of the code review.

CreatedTimeStamp (datetime) --The time, in milliseconds since the epoch, when the code review was created.

LastUpdatedTimeStamp (datetime) --The time, in milliseconds since the epoch, when the code review was last updated.

Type (string) --The type of code review.

PullRequestId (string) --The pull request ID for the code review.

SourceCodeType (dict) --The type of the source code for the code review.

CommitDiff (dict) --The commit diff for the pull request.

SourceCommit (string) --Source Commit SHA.

DestinationCommit (string) --Destination Commit SHA





Metrics (dict) --The statistics from the code review.

MeteredLinesOfCodeCount (integer) --Lines of code metered in the code review.

FindingsCount (integer) --Total number of recommendations found in the code review.










Exceptions

CodeGuruReviewer.Client.exceptions.ResourceNotFoundException
CodeGuruReviewer.Client.exceptions.InternalServerException
CodeGuruReviewer.Client.exceptions.ValidationException
CodeGuruReviewer.Client.exceptions.AccessDeniedException
CodeGuruReviewer.Client.exceptions.ThrottlingException


    :return: {
        'CodeReview': {
            'Name': 'string',
            'CodeReviewArn': 'string',
            'RepositoryName': 'string',
            'Owner': 'string',
            'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
            'State': 'Completed'|'Pending'|'Failed'|'Deleting',
            'StateReason': 'string',
            'CreatedTimeStamp': datetime(2015, 1, 1),
            'LastUpdatedTimeStamp': datetime(2015, 1, 1),
            'Type': 'PullRequest',
            'PullRequestId': 'string',
            'SourceCodeType': {
                'CommitDiff': {
                    'SourceCommit': 'string',
                    'DestinationCommit': 'string'
                }
            },
            'Metrics': {
                'MeteredLinesOfCodeCount': 123,
                'FindingsCount': 123
            }
        }
    }
    
    
    """
    pass

def describe_recommendation_feedback(CodeReviewArn=None, RecommendationId=None, UserId=None):
    """
    Describes the customer feedback for a CodeGuru Reviewer recommendation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_recommendation_feedback(
        CodeReviewArn='string',
        RecommendationId='string',
        UserId='string'
    )
    
    
    :type CodeReviewArn: string
    :param CodeReviewArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that identifies the code review.\n

    :type RecommendationId: string
    :param RecommendationId: [REQUIRED]\nThe recommendation ID that can be used to track the provided recommendations and then to collect the feedback.\n

    :type UserId: string
    :param UserId: Optional parameter to describe the feedback for a given user. If this is not supplied, it defaults to the user making the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'RecommendationFeedback': {
        'CodeReviewArn': 'string',
        'RecommendationId': 'string',
        'Reactions': [
            'ThumbsUp'|'ThumbsDown',
        ],
        'UserId': 'string',
        'CreatedTimeStamp': datetime(2015, 1, 1),
        'LastUpdatedTimeStamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

RecommendationFeedback (dict) --
The recommendation feedback given by the user.

CodeReviewArn (string) --
The Amazon Resource Name (ARN) that identifies the code review.

RecommendationId (string) --
The recommendation ID that can be used to track the provided recommendations. Later on it can be used to collect the feedback.

Reactions (list) --
List for storing reactions. Reactions are utf-8 text code for emojis. You can send an empty list to clear off all your feedback.

(string) --


UserId (string) --
The user principal that made the API call.

CreatedTimeStamp (datetime) --
The time at which the feedback was created.

LastUpdatedTimeStamp (datetime) --
The time at which the feedback was last updated.









Exceptions

CodeGuruReviewer.Client.exceptions.ResourceNotFoundException
CodeGuruReviewer.Client.exceptions.InternalServerException
CodeGuruReviewer.Client.exceptions.ValidationException
CodeGuruReviewer.Client.exceptions.AccessDeniedException
CodeGuruReviewer.Client.exceptions.ThrottlingException


    :return: {
        'RecommendationFeedback': {
            'CodeReviewArn': 'string',
            'RecommendationId': 'string',
            'Reactions': [
                'ThumbsUp'|'ThumbsDown',
            ],
            'UserId': 'string',
            'CreatedTimeStamp': datetime(2015, 1, 1),
            'LastUpdatedTimeStamp': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_repository_association(AssociationArn=None):
    """
    Describes a repository association.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_repository_association(
        AssociationArn='string'
    )
    
    
    :type AssociationArn: string
    :param AssociationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) identifying the association. You can retrieve this ARN by calling ListRepositories .\n

    :rtype: dict
ReturnsResponse Syntax{
    'RepositoryAssociation': {
        'AssociationId': 'string',
        'AssociationArn': 'string',
        'ConnectionArn': 'string',
        'Name': 'string',
        'Owner': 'string',
        'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
        'State': 'Associated'|'Associating'|'Failed'|'Disassociating',
        'StateReason': 'string',
        'LastUpdatedTimeStamp': datetime(2015, 1, 1),
        'CreatedTimeStamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
RepositoryAssociation (dict) --Information about the repository association.

AssociationId (string) --The ID of the repository association.

AssociationArn (string) --The Amazon Resource Name (ARN) identifying the repository association.

ConnectionArn (string) --The Amazon Resource Name (ARN) identifying the repository connection.

Name (string) --The name of the repository.

Owner (string) --The owner of the repository.

ProviderType (string) --The provider type of the repository association.

State (string) --The state of the repository association.

StateReason (string) --A description of why the repository association is in the current state.

LastUpdatedTimeStamp (datetime) --The time, in milliseconds since the epoch, when the repository association was last updated.

CreatedTimeStamp (datetime) --The time, in milliseconds since the epoch, when the repository association was created.








Exceptions

CodeGuruReviewer.Client.exceptions.NotFoundException
CodeGuruReviewer.Client.exceptions.InternalServerException
CodeGuruReviewer.Client.exceptions.ValidationException
CodeGuruReviewer.Client.exceptions.AccessDeniedException
CodeGuruReviewer.Client.exceptions.ThrottlingException


    :return: {
        'RepositoryAssociation': {
            'AssociationId': 'string',
            'AssociationArn': 'string',
            'ConnectionArn': 'string',
            'Name': 'string',
            'Owner': 'string',
            'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
            'State': 'Associated'|'Associating'|'Failed'|'Disassociating',
            'StateReason': 'string',
            'LastUpdatedTimeStamp': datetime(2015, 1, 1),
            'CreatedTimeStamp': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def disassociate_repository(AssociationArn=None):
    """
    Removes the association between Amazon CodeGuru Reviewer and a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_repository(
        AssociationArn='string'
    )
    
    
    :type AssociationArn: string
    :param AssociationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) identifying the association.\n

    :rtype: dict
ReturnsResponse Syntax{
    'RepositoryAssociation': {
        'AssociationId': 'string',
        'AssociationArn': 'string',
        'ConnectionArn': 'string',
        'Name': 'string',
        'Owner': 'string',
        'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
        'State': 'Associated'|'Associating'|'Failed'|'Disassociating',
        'StateReason': 'string',
        'LastUpdatedTimeStamp': datetime(2015, 1, 1),
        'CreatedTimeStamp': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
RepositoryAssociation (dict) --Information about the disassociated repository.

AssociationId (string) --The ID of the repository association.

AssociationArn (string) --The Amazon Resource Name (ARN) identifying the repository association.

ConnectionArn (string) --The Amazon Resource Name (ARN) identifying the repository connection.

Name (string) --The name of the repository.

Owner (string) --The owner of the repository.

ProviderType (string) --The provider type of the repository association.

State (string) --The state of the repository association.

StateReason (string) --A description of why the repository association is in the current state.

LastUpdatedTimeStamp (datetime) --The time, in milliseconds since the epoch, when the repository association was last updated.

CreatedTimeStamp (datetime) --The time, in milliseconds since the epoch, when the repository association was created.








Exceptions

CodeGuruReviewer.Client.exceptions.NotFoundException
CodeGuruReviewer.Client.exceptions.InternalServerException
CodeGuruReviewer.Client.exceptions.ValidationException
CodeGuruReviewer.Client.exceptions.AccessDeniedException
CodeGuruReviewer.Client.exceptions.ConflictException
CodeGuruReviewer.Client.exceptions.ThrottlingException


    :return: {
        'RepositoryAssociation': {
            'AssociationId': 'string',
            'AssociationArn': 'string',
            'ConnectionArn': 'string',
            'Name': 'string',
            'Owner': 'string',
            'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
            'State': 'Associated'|'Associating'|'Failed'|'Disassociating',
            'StateReason': 'string',
            'LastUpdatedTimeStamp': datetime(2015, 1, 1),
            'CreatedTimeStamp': datetime(2015, 1, 1)
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

def list_code_reviews(ProviderTypes=None, States=None, RepositoryNames=None, Type=None, MaxResults=None, NextToken=None):
    """
    Lists all the code reviews that the customer has created in the past 90 days.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_code_reviews(
        ProviderTypes=[
            'CodeCommit'|'GitHub'|'Bitbucket',
        ],
        States=[
            'Completed'|'Pending'|'Failed'|'Deleting',
        ],
        RepositoryNames=[
            'string',
        ],
        Type='PullRequest',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ProviderTypes: list
    :param ProviderTypes: List of provider types for filtering that needs to be applied before displaying the result. For example, 'providerTypes=[GitHub]' will list code reviews from GitHub.\n\n(string) --\n\n

    :type States: list
    :param States: List of states for filtering that needs to be applied before displaying the result. For example, 'states=[Pending]' will list code reviews in the Pending state.\n\n(string) --\n\n

    :type RepositoryNames: list
    :param RepositoryNames: List of repository names for filtering that needs to be applied before displaying the result.\n\n(string) --\n\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of code reviews to list in the response.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results that are returned per call. The default is 100.

    :type NextToken: string
    :param NextToken: If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.

    :rtype: dict

ReturnsResponse Syntax
{
    'CodeReviewSummaries': [
        {
            'Name': 'string',
            'CodeReviewArn': 'string',
            'RepositoryName': 'string',
            'Owner': 'string',
            'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
            'State': 'Completed'|'Pending'|'Failed'|'Deleting',
            'CreatedTimeStamp': datetime(2015, 1, 1),
            'LastUpdatedTimeStamp': datetime(2015, 1, 1),
            'Type': 'PullRequest',
            'PullRequestId': 'string',
            'MetricsSummary': {
                'MeteredLinesOfCodeCount': 123,
                'FindingsCount': 123
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CodeReviewSummaries (list) --
A list of code reviews that meet the criteria of the request.

(dict) --
Information about the summary of the code review.

Name (string) --
The name of the code review.

CodeReviewArn (string) --
The Amazon Resource Name (ARN) of the code review to describe.

RepositoryName (string) --
The name of the repository.

Owner (string) --
The owner of the repository.

ProviderType (string) --
The provider type of the repository association.

State (string) --
The state of the code review.

CreatedTimeStamp (datetime) --
The time, in milliseconds since the epoch, when the code review was created.

LastUpdatedTimeStamp (datetime) --
The time, in milliseconds since the epoch, when the code review was last updated.

Type (string) --
The type of the code review.

PullRequestId (string) --
The pull request ID for the code review.

MetricsSummary (dict) --
The statistics from the code review.

MeteredLinesOfCodeCount (integer) --
Lines of code metered in the code review.

FindingsCount (integer) --
Total number of recommendations found in the code review.







NextToken (string) --
Pagination token.







Exceptions

CodeGuruReviewer.Client.exceptions.InternalServerException
CodeGuruReviewer.Client.exceptions.ValidationException
CodeGuruReviewer.Client.exceptions.ThrottlingException
CodeGuruReviewer.Client.exceptions.AccessDeniedException


    :return: {
        'CodeReviewSummaries': [
            {
                'Name': 'string',
                'CodeReviewArn': 'string',
                'RepositoryName': 'string',
                'Owner': 'string',
                'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
                'State': 'Completed'|'Pending'|'Failed'|'Deleting',
                'CreatedTimeStamp': datetime(2015, 1, 1),
                'LastUpdatedTimeStamp': datetime(2015, 1, 1),
                'Type': 'PullRequest',
                'PullRequestId': 'string',
                'MetricsSummary': {
                    'MeteredLinesOfCodeCount': 123,
                    'FindingsCount': 123
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CodeGuruReviewer.Client.exceptions.InternalServerException
    CodeGuruReviewer.Client.exceptions.ValidationException
    CodeGuruReviewer.Client.exceptions.ThrottlingException
    CodeGuruReviewer.Client.exceptions.AccessDeniedException
    
    """
    pass

def list_recommendation_feedback(NextToken=None, MaxResults=None, CodeReviewArn=None, UserIds=None, RecommendationIds=None):
    """
    Lists the customer feedback for a CodeGuru Reviewer recommendation for all users. This API will be used from the console to extract the previously given feedback by the user to pre-populate the feedback emojis for all recommendations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_recommendation_feedback(
        NextToken='string',
        MaxResults=123,
        CodeReviewArn='string',
        UserIds=[
            'string',
        ],
        RecommendationIds=[
            'string',
        ]
    )
    
    
    :type NextToken: string
    :param NextToken: If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results that are returned per call. The default is 100.

    :type CodeReviewArn: string
    :param CodeReviewArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that identifies the code review.\n

    :type UserIds: list
    :param UserIds: Filter on userIds that need to be applied before displaying the result. This can be used to query all the recommendation feedback for a code review from a given user.\n\n(string) --\n\n

    :type RecommendationIds: list
    :param RecommendationIds: Filter on recommendationIds that need to be applied before displaying the result. This can be used to query all the recommendation feedback for a given recommendation.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RecommendationFeedbackSummaries': [
        {
            'RecommendationId': 'string',
            'Reactions': [
                'ThumbsUp'|'ThumbsDown',
            ],
            'UserId': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RecommendationFeedbackSummaries (list) --
Recommendation feedback summaries corresponding to the code reivew ARN.

(dict) --
Information about recommendation feedback summaries.

RecommendationId (string) --
The recommendation ID that can be used to track the provided recommendations. Later on it can be used to collect the feedback.

Reactions (list) --
List for storing reactions. Reactions are utf-8 text code for emojis.

(string) --


UserId (string) --
The identifier for the user that gave the feedback.





NextToken (string) --
If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.







Exceptions

CodeGuruReviewer.Client.exceptions.ResourceNotFoundException
CodeGuruReviewer.Client.exceptions.InternalServerException
CodeGuruReviewer.Client.exceptions.ValidationException
CodeGuruReviewer.Client.exceptions.AccessDeniedException
CodeGuruReviewer.Client.exceptions.ThrottlingException


    :return: {
        'RecommendationFeedbackSummaries': [
            {
                'RecommendationId': 'string',
                'Reactions': [
                    'ThumbsUp'|'ThumbsDown',
                ],
                'UserId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_recommendations(NextToken=None, MaxResults=None, CodeReviewArn=None):
    """
    Returns the list of all recommendations for a completed code review.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_recommendations(
        NextToken='string',
        MaxResults=123,
        CodeReviewArn='string'
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results that are returned per call. The default is 100.

    :type CodeReviewArn: string
    :param CodeReviewArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the code review to describe.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RecommendationSummaries': [
        {
            'FilePath': 'string',
            'RecommendationId': 'string',
            'StartLine': 123,
            'EndLine': 123,
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RecommendationSummaries (list) --
List of recommendations for the requested code review.

(dict) --
Information about recommendations.

FilePath (string) --
Name of the file on which a recommendation is provided.

RecommendationId (string) --
The recommendation ID that can be used to track the provided recommendations. Later on it can be used to collect the feedback.

StartLine (integer) --
Start line from where the recommendation is applicable in the source commit or source branch.

EndLine (integer) --
Last line where the recommendation is applicable in the source commit or source branch. For a single line comment the start line and end line values will be the same.

Description (string) --
A description of the recommendation generated by CodeGuru Reviewer for the lines of code between the start line and the end line.





NextToken (string) --
Pagination token.







Exceptions

CodeGuruReviewer.Client.exceptions.ResourceNotFoundException
CodeGuruReviewer.Client.exceptions.InternalServerException
CodeGuruReviewer.Client.exceptions.ValidationException
CodeGuruReviewer.Client.exceptions.AccessDeniedException
CodeGuruReviewer.Client.exceptions.ThrottlingException


    :return: {
        'RecommendationSummaries': [
            {
                'FilePath': 'string',
                'RecommendationId': 'string',
                'StartLine': 123,
                'EndLine': 123,
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CodeGuruReviewer.Client.exceptions.ResourceNotFoundException
    CodeGuruReviewer.Client.exceptions.InternalServerException
    CodeGuruReviewer.Client.exceptions.ValidationException
    CodeGuruReviewer.Client.exceptions.AccessDeniedException
    CodeGuruReviewer.Client.exceptions.ThrottlingException
    
    """
    pass

def list_repository_associations(ProviderTypes=None, States=None, Names=None, Owners=None, MaxResults=None, NextToken=None):
    """
    Lists repository associations. You can optionally filter on one or more of the following recommendation properties: provider types, states, names, and owners.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_repository_associations(
        ProviderTypes=[
            'CodeCommit'|'GitHub'|'Bitbucket',
        ],
        States=[
            'Associated'|'Associating'|'Failed'|'Disassociating',
        ],
        Names=[
            'string',
        ],
        Owners=[
            'string',
        ],
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ProviderTypes: list
    :param ProviderTypes: List of provider types to use as a filter.\n\n(string) --\n\n

    :type States: list
    :param States: List of states to use as a filter.\n\n(string) --\n\n

    :type Names: list
    :param Names: List of repository names to use as a filter.\n\n(string) --\n\n

    :type Owners: list
    :param Owners: List of owners to use as a filter. For GitHub, this is name of the GitHub account that was used to associate the repository. For AWS CodeCommit, it is the name of the CodeCommit account that was used to associate the repository.\n\n(string) --\n\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of repository association results returned by ListRepositoryAssociations in paginated output. When this parameter is used, ListRepositoryAssociations only returns maxResults results in a single page with a nextToken response element. The remaining results of the initial request can be seen by sending another ListRepositoryAssociations request with the returned nextToken value. This value can be between 1 and 25. If this parameter is not used, ListRepositoryAssociations returns up to 25 results and a nextToken value if applicable.

    :type NextToken: string
    :param NextToken: The nextToken value returned from a previous paginated ListRepositoryAssociations request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the nextToken value.\n\nNote\nTreat this token as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RepositoryAssociationSummaries': [
        {
            'AssociationArn': 'string',
            'ConnectionArn': 'string',
            'LastUpdatedTimeStamp': datetime(2015, 1, 1),
            'AssociationId': 'string',
            'Name': 'string',
            'Owner': 'string',
            'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
            'State': 'Associated'|'Associating'|'Failed'|'Disassociating'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

RepositoryAssociationSummaries (list) --
A list of repository associations that meet the criteria of the request.

(dict) --
Information about a repository association.

AssociationArn (string) --
The Amazon Resource Name (ARN) identifying the repository association.

ConnectionArn (string) --
The Amazon Resource Name (ARN) identifying the repository connection.

LastUpdatedTimeStamp (datetime) --
The time, in milliseconds since the epoch, since the repository association was last updated.

AssociationId (string) --
The repository association ID.

Name (string) --
The name of the repository association.

Owner (string) --
The owner of the repository association.

ProviderType (string) --
The provider type of the repository association.

State (string) --
The state of the repository association.

Associated

Amazon CodeGuru Reviewer is associated with the repository.

Associating

The association is in progress.

Failed

The association failed.

Disassociating

Amazon CodeGuru Reviewer is in the process of disassociating with the repository.





NextToken (string) --
The nextToken value to include in a future ListRecommendations request. When the results of a ListRecommendations request exceed maxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

CodeGuruReviewer.Client.exceptions.InternalServerException
CodeGuruReviewer.Client.exceptions.ValidationException
CodeGuruReviewer.Client.exceptions.ThrottlingException


    :return: {
        'RepositoryAssociationSummaries': [
            {
                'AssociationArn': 'string',
                'ConnectionArn': 'string',
                'LastUpdatedTimeStamp': datetime(2015, 1, 1),
                'AssociationId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'ProviderType': 'CodeCommit'|'GitHub'|'Bitbucket',
                'State': 'Associated'|'Associating'|'Failed'|'Disassociating'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CodeGuruReviewer.Client.exceptions.InternalServerException
    CodeGuruReviewer.Client.exceptions.ValidationException
    CodeGuruReviewer.Client.exceptions.ThrottlingException
    
    """
    pass

def put_recommendation_feedback(CodeReviewArn=None, RecommendationId=None, Reactions=None):
    """
    Stores customer feedback for a CodeGuru-Reviewer recommendation. When this API is called again with different reactions the previous feedback is overwritten.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_recommendation_feedback(
        CodeReviewArn='string',
        RecommendationId='string',
        Reactions=[
            'ThumbsUp'|'ThumbsDown',
        ]
    )
    
    
    :type CodeReviewArn: string
    :param CodeReviewArn: [REQUIRED]\nThe Amazon Resource Name (ARN) that identifies the code review.\n

    :type RecommendationId: string
    :param RecommendationId: [REQUIRED]\nThe recommendation ID that can be used to track the provided recommendations and then to collect the feedback.\n

    :type Reactions: list
    :param Reactions: [REQUIRED]\nList for storing reactions. Reactions are utf-8 text code for emojis. If you send an empty list it clears all your feedback.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CodeGuruReviewer.Client.exceptions.ResourceNotFoundException
CodeGuruReviewer.Client.exceptions.InternalServerException
CodeGuruReviewer.Client.exceptions.ValidationException
CodeGuruReviewer.Client.exceptions.AccessDeniedException
CodeGuruReviewer.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

