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

def accept_invitation(GraphArn=None):
    """
    Accepts an invitation for the member account to contribute data to a behavior graph. This operation can only be called by an invited member account.
    The request provides the ARN of behavior graph.
    The member account status in the graph must be INVITED .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_invitation(
        GraphArn='string'
    )
    
    
    :type GraphArn: string
    :param GraphArn: [REQUIRED]\nThe ARN of the behavior graph that the member account is accepting the invitation for.\nThe member account status in the behavior graph must be INVITED .\n

    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_graph():
    """
    Creates a new behavior graph for the calling account, and sets that account as the master account. This operation is called by the account that is enabling Detective.
    Before you try to enable Detective, make sure that your account has been enrolled in Amazon GuardDuty for at least 48 hours. If you do not meet this requirement, you cannot enable Detective. If you do meet the GuardDuty prerequisite, then when you make the request to enable Detective, it checks whether your data volume is within the Detective quota. If it exceeds the quota, then you cannot enable Detective.
    The operation also enables Detective for the calling account in the currently selected Region. It returns the ARN of the new behavior graph.
    An account can only be the master account for one behavior graph within a Region. If the same account calls CreateGraph with the same master account, it always returns the same behavior graph ARN. It does not create a new behavior graph.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_graph()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'GraphArn': 'string'
}


Response Structure

(dict) --
GraphArn (string) --The ARN of the new behavior graph.






Exceptions

Detective.Client.exceptions.ConflictException
Detective.Client.exceptions.InternalServerException
Detective.Client.exceptions.ServiceQuotaExceededException


    :return: {
        'GraphArn': 'string'
    }
    
    
    """
    pass

def create_members(GraphArn=None, Message=None, Accounts=None):
    """
    Sends a request to invite the specified AWS accounts to be member accounts in the behavior graph. This operation can only be called by the master account for a behavior graph.
    The request provides the behavior graph ARN and the list of accounts to invite.
    The response separates the requested accounts into two lists:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_members(
        GraphArn='string',
        Message='string',
        Accounts=[
            {
                'AccountId': 'string',
                'EmailAddress': 'string'
            },
        ]
    )
    
    
    :type GraphArn: string
    :param GraphArn: [REQUIRED]\nThe ARN of the behavior graph to invite the member accounts to contribute their data to.\n

    :type Message: string
    :param Message: Customized message text to include in the invitation email message to the invited member accounts.

    :type Accounts: list
    :param Accounts: [REQUIRED]\nThe list of AWS accounts to invite to become member accounts in the behavior graph. For each invited account, the account list contains the account identifier and the AWS account root user email address.\n\n(dict) --An AWS account that is the master of or a member of a behavior graph.\n\nAccountId (string) -- [REQUIRED]The account identifier of the AWS account.\n\nEmailAddress (string) -- [REQUIRED]The AWS account root user email address for the AWS account.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Members': [
        {
            'AccountId': 'string',
            'EmailAddress': 'string',
            'GraphArn': 'string',
            'MasterId': 'string',
            'Status': 'INVITED'|'VERIFICATION_IN_PROGRESS'|'VERIFICATION_FAILED'|'ENABLED'|'ACCEPTED_BUT_DISABLED',
            'DisabledReason': 'VOLUME_TOO_HIGH'|'VOLUME_UNKNOWN',
            'InvitedTime': datetime(2015, 1, 1),
            'UpdatedTime': datetime(2015, 1, 1),
            'PercentOfGraphUtilization': 123.0,
            'PercentOfGraphUtilizationUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Reason': 'string'
        },
    ]
}


Response Structure

(dict) --

Members (list) --
The set of member account invitation requests that Detective was able to process. This includes accounts that are being verified, that failed verification, and that passed verification and are being sent an invitation.

(dict) --
Details about a member account that was invited to contribute to a behavior graph.

AccountId (string) --
The AWS account identifier for the member account.

EmailAddress (string) --
The AWS account root user email address for the member account.

GraphArn (string) --
The ARN of the behavior graph that the member account was invited to.

MasterId (string) --
The AWS account identifier of the master account for the behavior graph.

Status (string) --
The current membership status of the member account. The status can have one of the following values:

INVITED - Indicates that the member was sent an invitation but has not yet responded.
VERIFICATION_IN_PROGRESS - Indicates that Detective is verifying that the account identifier and email address provided for the member account match. If they do match, then Detective sends the invitation. If the email address and account identifier don\'t match, then the member cannot be added to the behavior graph.
VERIFICATION_FAILED - Indicates that the account and email address provided for the member account do not match, and Detective did not send an invitation to the account.
ENABLED - Indicates that the member account accepted the invitation to contribute to the behavior graph.
ACCEPTED_BUT_DISABLED - Indicates that the member account accepted the invitation but is prevented from contributing data to the behavior graph. DisabledReason provides the reason why the member account is not enabled.

Member accounts that declined an invitation or that were removed from the behavior graph are not included.

DisabledReason (string) --
For member accounts with a status of ACCEPTED_BUT_DISABLED , the reason that the member account is not enabled.
The reason can have one of the following values:

VOLUME_TOO_HIGH - Indicates that adding the member account would cause the data volume for the behavior graph to be too high.
VOLUME_UNKNOWN - Indicates that Detective is unable to verify the data volume for the member account. This is usually because the member account is not enrolled in Amazon GuardDuty.


InvitedTime (datetime) --
The date and time that Detective sent the invitation to the member account. The value is in milliseconds since the epoch.

UpdatedTime (datetime) --
The date and time that the member account was last updated. The value is in milliseconds since the epoch.

PercentOfGraphUtilization (float) --
The member account data volume as a percentage of the maximum allowed data volume. 0 indicates 0 percent, and 100 indicates 100 percent.
Note that this is not the percentage of the behavior graph data volume.
For example, the data volume for the behavior graph is 80 GB per day. The maximum data volume is 160 GB per day. If the data volume for the member account is 40 GB per day, then PercentOfGraphUtilization is 25. It represents 25% of the maximum allowed data volume.

PercentOfGraphUtilizationUpdatedTime (datetime) --
The date and time when the graph utilization percentage was last updated.





UnprocessedAccounts (list) --
The list of accounts for which Detective was unable to process the invitation request. For each account, the list provides the reason why the request could not be processed. The list includes accounts that are already member accounts in the behavior graph.

(dict) --
A member account that was included in a request but for which the request could not be processed.

AccountId (string) --
The AWS account identifier of the member account that was not processed.

Reason (string) --
The reason that the member account request could not be processed.











Exceptions

Detective.Client.exceptions.InternalServerException
Detective.Client.exceptions.ResourceNotFoundException
Detective.Client.exceptions.ValidationException
Detective.Client.exceptions.ServiceQuotaExceededException


    :return: {
        'Members': [
            {
                'AccountId': 'string',
                'EmailAddress': 'string',
                'GraphArn': 'string',
                'MasterId': 'string',
                'Status': 'INVITED'|'VERIFICATION_IN_PROGRESS'|'VERIFICATION_FAILED'|'ENABLED'|'ACCEPTED_BUT_DISABLED',
                'DisabledReason': 'VOLUME_TOO_HIGH'|'VOLUME_UNKNOWN',
                'InvitedTime': datetime(2015, 1, 1),
                'UpdatedTime': datetime(2015, 1, 1),
                'PercentOfGraphUtilization': 123.0,
                'PercentOfGraphUtilizationUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    GraphArn (string) -- [REQUIRED]
    The ARN of the behavior graph to invite the member accounts to contribute their data to.
    
    Message (string) -- Customized message text to include in the invitation email message to the invited member accounts.
    Accounts (list) -- [REQUIRED]
    The list of AWS accounts to invite to become member accounts in the behavior graph. For each invited account, the account list contains the account identifier and the AWS account root user email address.
    
    (dict) --An AWS account that is the master of or a member of a behavior graph.
    
    AccountId (string) -- [REQUIRED]The account identifier of the AWS account.
    
    EmailAddress (string) -- [REQUIRED]The AWS account root user email address for the AWS account.
    
    
    
    
    
    
    """
    pass

def delete_graph(GraphArn=None):
    """
    Disables the specified behavior graph and queues it to be deleted. This operation removes the graph from each member account\'s list of behavior graphs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_graph(
        GraphArn='string'
    )
    
    
    :type GraphArn: string
    :param GraphArn: [REQUIRED]\nThe ARN of the behavior graph to disable.\n

    """
    pass

def delete_members(GraphArn=None, AccountIds=None):
    """
    Deletes one or more member accounts from the master account behavior graph. This operation can only be called by a Detective master account. That account cannot use DeleteMembers to delete their own account from the behavior graph. To disable a behavior graph, the master account uses the DeleteGraph API method.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_members(
        GraphArn='string',
        AccountIds=[
            'string',
        ]
    )
    
    
    :type GraphArn: string
    :param GraphArn: [REQUIRED]\nThe ARN of the behavior graph to delete members from.\n

    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nThe list of AWS account identifiers for the member accounts to delete from the behavior graph.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AccountIds': [
        'string',
    ],
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Reason': 'string'
        },
    ]
}


Response Structure

(dict) --

AccountIds (list) --
The list of AWS account identifiers for the member accounts that Detective successfully deleted from the behavior graph.

(string) --


UnprocessedAccounts (list) --
The list of member accounts that Detective was not able to delete from the behavior graph. For each member account, provides the reason that the deletion could not be processed.

(dict) --
A member account that was included in a request but for which the request could not be processed.

AccountId (string) --
The AWS account identifier of the member account that was not processed.

Reason (string) --
The reason that the member account request could not be processed.











Exceptions

Detective.Client.exceptions.ConflictException
Detective.Client.exceptions.InternalServerException
Detective.Client.exceptions.ResourceNotFoundException
Detective.Client.exceptions.ValidationException


    :return: {
        'AccountIds': [
            'string',
        ],
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def disassociate_membership(GraphArn=None):
    """
    Removes the member account from the specified behavior graph. This operation can only be called by a member account that has the ENABLED status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_membership(
        GraphArn='string'
    )
    
    
    :type GraphArn: string
    :param GraphArn: [REQUIRED]\nThe ARN of the behavior graph to remove the member account from.\nThe member account\'s member status in the behavior graph must be ENABLED .\n

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

def get_members(GraphArn=None, AccountIds=None):
    """
    Returns the membership details for specified member accounts for a behavior graph.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_members(
        GraphArn='string',
        AccountIds=[
            'string',
        ]
    )
    
    
    :type GraphArn: string
    :param GraphArn: [REQUIRED]\nThe ARN of the behavior graph for which to request the member details.\n

    :type AccountIds: list
    :param AccountIds: [REQUIRED]\nThe list of AWS account identifiers for the member account for which to return member details.\nYou cannot use GetMembers to retrieve information about member accounts that were removed from the behavior graph.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'MemberDetails': [
        {
            'AccountId': 'string',
            'EmailAddress': 'string',
            'GraphArn': 'string',
            'MasterId': 'string',
            'Status': 'INVITED'|'VERIFICATION_IN_PROGRESS'|'VERIFICATION_FAILED'|'ENABLED'|'ACCEPTED_BUT_DISABLED',
            'DisabledReason': 'VOLUME_TOO_HIGH'|'VOLUME_UNKNOWN',
            'InvitedTime': datetime(2015, 1, 1),
            'UpdatedTime': datetime(2015, 1, 1),
            'PercentOfGraphUtilization': 123.0,
            'PercentOfGraphUtilizationUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'UnprocessedAccounts': [
        {
            'AccountId': 'string',
            'Reason': 'string'
        },
    ]
}


Response Structure

(dict) --

MemberDetails (list) --
The member account details that Detective is returning in response to the request.

(dict) --
Details about a member account that was invited to contribute to a behavior graph.

AccountId (string) --
The AWS account identifier for the member account.

EmailAddress (string) --
The AWS account root user email address for the member account.

GraphArn (string) --
The ARN of the behavior graph that the member account was invited to.

MasterId (string) --
The AWS account identifier of the master account for the behavior graph.

Status (string) --
The current membership status of the member account. The status can have one of the following values:

INVITED - Indicates that the member was sent an invitation but has not yet responded.
VERIFICATION_IN_PROGRESS - Indicates that Detective is verifying that the account identifier and email address provided for the member account match. If they do match, then Detective sends the invitation. If the email address and account identifier don\'t match, then the member cannot be added to the behavior graph.
VERIFICATION_FAILED - Indicates that the account and email address provided for the member account do not match, and Detective did not send an invitation to the account.
ENABLED - Indicates that the member account accepted the invitation to contribute to the behavior graph.
ACCEPTED_BUT_DISABLED - Indicates that the member account accepted the invitation but is prevented from contributing data to the behavior graph. DisabledReason provides the reason why the member account is not enabled.

Member accounts that declined an invitation or that were removed from the behavior graph are not included.

DisabledReason (string) --
For member accounts with a status of ACCEPTED_BUT_DISABLED , the reason that the member account is not enabled.
The reason can have one of the following values:

VOLUME_TOO_HIGH - Indicates that adding the member account would cause the data volume for the behavior graph to be too high.
VOLUME_UNKNOWN - Indicates that Detective is unable to verify the data volume for the member account. This is usually because the member account is not enrolled in Amazon GuardDuty.


InvitedTime (datetime) --
The date and time that Detective sent the invitation to the member account. The value is in milliseconds since the epoch.

UpdatedTime (datetime) --
The date and time that the member account was last updated. The value is in milliseconds since the epoch.

PercentOfGraphUtilization (float) --
The member account data volume as a percentage of the maximum allowed data volume. 0 indicates 0 percent, and 100 indicates 100 percent.
Note that this is not the percentage of the behavior graph data volume.
For example, the data volume for the behavior graph is 80 GB per day. The maximum data volume is 160 GB per day. If the data volume for the member account is 40 GB per day, then PercentOfGraphUtilization is 25. It represents 25% of the maximum allowed data volume.

PercentOfGraphUtilizationUpdatedTime (datetime) --
The date and time when the graph utilization percentage was last updated.





UnprocessedAccounts (list) --
The requested member accounts for which Detective was unable to return member details.
For each account, provides the reason why the request could not be processed.

(dict) --
A member account that was included in a request but for which the request could not be processed.

AccountId (string) --
The AWS account identifier of the member account that was not processed.

Reason (string) --
The reason that the member account request could not be processed.











Exceptions

Detective.Client.exceptions.InternalServerException
Detective.Client.exceptions.ResourceNotFoundException
Detective.Client.exceptions.ValidationException


    :return: {
        'MemberDetails': [
            {
                'AccountId': 'string',
                'EmailAddress': 'string',
                'GraphArn': 'string',
                'MasterId': 'string',
                'Status': 'INVITED'|'VERIFICATION_IN_PROGRESS'|'VERIFICATION_FAILED'|'ENABLED'|'ACCEPTED_BUT_DISABLED',
                'DisabledReason': 'VOLUME_TOO_HIGH'|'VOLUME_UNKNOWN',
                'InvitedTime': datetime(2015, 1, 1),
                'UpdatedTime': datetime(2015, 1, 1),
                'PercentOfGraphUtilization': 123.0,
                'PercentOfGraphUtilizationUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'UnprocessedAccounts': [
            {
                'AccountId': 'string',
                'Reason': 'string'
            },
        ]
    }
    
    
    :returns: 
    INVITED - Indicates that the member was sent an invitation but has not yet responded.
    VERIFICATION_IN_PROGRESS - Indicates that Detective is verifying that the account identifier and email address provided for the member account match. If they do match, then Detective sends the invitation. If the email address and account identifier don\'t match, then the member cannot be added to the behavior graph.
    VERIFICATION_FAILED - Indicates that the account and email address provided for the member account do not match, and Detective did not send an invitation to the account.
    ENABLED - Indicates that the member account accepted the invitation to contribute to the behavior graph.
    ACCEPTED_BUT_DISABLED - Indicates that the member account accepted the invitation but is prevented from contributing data to the behavior graph. DisabledReason provides the reason why the member account is not enabled.
    
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

def list_graphs(NextToken=None, MaxResults=None):
    """
    Returns the list of behavior graphs that the calling account is a master of. This operation can only be called by a master account.
    Because an account can currently only be the master of one behavior graph within a Region, the results always contain a single graph.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_graphs(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of graphs to return at a time. The total must be less than the overall limit on the number of results to return, which is currently 200.

    :rtype: dict

ReturnsResponse Syntax
{
    'GraphList': [
        {
            'Arn': 'string',
            'CreatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

GraphList (list) --
A list of behavior graphs that the account is a master for.

(dict) --
A behavior graph in Detective.

Arn (string) --
The ARN of the behavior graph.

CreatedTime (datetime) --
The date and time that the behavior graph was created. The value is in milliseconds since the epoch.





NextToken (string) --
If there are more behavior graphs remaining in the results, then this is the pagination token to use to request the next page of behavior graphs.







Exceptions

Detective.Client.exceptions.InternalServerException
Detective.Client.exceptions.ValidationException


    :return: {
        'GraphList': [
            {
                'Arn': 'string',
                'CreatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Detective.Client.exceptions.InternalServerException
    Detective.Client.exceptions.ValidationException
    
    """
    pass

def list_invitations(NextToken=None, MaxResults=None):
    """
    Retrieves the list of open and accepted behavior graph invitations for the member account. This operation can only be called by a member account.
    Open invitations are invitations that the member account has not responded to.
    The results do not include behavior graphs for which the member account declined the invitation. The results also do not include behavior graphs that the member account resigned from or was removed from.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_invitations(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: For requests to retrieve the next page of results, the pagination token that was returned with the previous page of results. The initial request does not include a pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of behavior graph invitations to return in the response. The total must be less than the overall limit on the number of results to return, which is currently 200.

    :rtype: dict

ReturnsResponse Syntax
{
    'Invitations': [
        {
            'AccountId': 'string',
            'EmailAddress': 'string',
            'GraphArn': 'string',
            'MasterId': 'string',
            'Status': 'INVITED'|'VERIFICATION_IN_PROGRESS'|'VERIFICATION_FAILED'|'ENABLED'|'ACCEPTED_BUT_DISABLED',
            'DisabledReason': 'VOLUME_TOO_HIGH'|'VOLUME_UNKNOWN',
            'InvitedTime': datetime(2015, 1, 1),
            'UpdatedTime': datetime(2015, 1, 1),
            'PercentOfGraphUtilization': 123.0,
            'PercentOfGraphUtilizationUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Invitations (list) --
The list of behavior graphs for which the member account has open or accepted invitations.

(dict) --
Details about a member account that was invited to contribute to a behavior graph.

AccountId (string) --
The AWS account identifier for the member account.

EmailAddress (string) --
The AWS account root user email address for the member account.

GraphArn (string) --
The ARN of the behavior graph that the member account was invited to.

MasterId (string) --
The AWS account identifier of the master account for the behavior graph.

Status (string) --
The current membership status of the member account. The status can have one of the following values:

INVITED - Indicates that the member was sent an invitation but has not yet responded.
VERIFICATION_IN_PROGRESS - Indicates that Detective is verifying that the account identifier and email address provided for the member account match. If they do match, then Detective sends the invitation. If the email address and account identifier don\'t match, then the member cannot be added to the behavior graph.
VERIFICATION_FAILED - Indicates that the account and email address provided for the member account do not match, and Detective did not send an invitation to the account.
ENABLED - Indicates that the member account accepted the invitation to contribute to the behavior graph.
ACCEPTED_BUT_DISABLED - Indicates that the member account accepted the invitation but is prevented from contributing data to the behavior graph. DisabledReason provides the reason why the member account is not enabled.

Member accounts that declined an invitation or that were removed from the behavior graph are not included.

DisabledReason (string) --
For member accounts with a status of ACCEPTED_BUT_DISABLED , the reason that the member account is not enabled.
The reason can have one of the following values:

VOLUME_TOO_HIGH - Indicates that adding the member account would cause the data volume for the behavior graph to be too high.
VOLUME_UNKNOWN - Indicates that Detective is unable to verify the data volume for the member account. This is usually because the member account is not enrolled in Amazon GuardDuty.


InvitedTime (datetime) --
The date and time that Detective sent the invitation to the member account. The value is in milliseconds since the epoch.

UpdatedTime (datetime) --
The date and time that the member account was last updated. The value is in milliseconds since the epoch.

PercentOfGraphUtilization (float) --
The member account data volume as a percentage of the maximum allowed data volume. 0 indicates 0 percent, and 100 indicates 100 percent.
Note that this is not the percentage of the behavior graph data volume.
For example, the data volume for the behavior graph is 80 GB per day. The maximum data volume is 160 GB per day. If the data volume for the member account is 40 GB per day, then PercentOfGraphUtilization is 25. It represents 25% of the maximum allowed data volume.

PercentOfGraphUtilizationUpdatedTime (datetime) --
The date and time when the graph utilization percentage was last updated.





NextToken (string) --
If there are more behavior graphs remaining in the results, then this is the pagination token to use to request the next page of behavior graphs.







Exceptions

Detective.Client.exceptions.InternalServerException
Detective.Client.exceptions.ValidationException


    :return: {
        'Invitations': [
            {
                'AccountId': 'string',
                'EmailAddress': 'string',
                'GraphArn': 'string',
                'MasterId': 'string',
                'Status': 'INVITED'|'VERIFICATION_IN_PROGRESS'|'VERIFICATION_FAILED'|'ENABLED'|'ACCEPTED_BUT_DISABLED',
                'DisabledReason': 'VOLUME_TOO_HIGH'|'VOLUME_UNKNOWN',
                'InvitedTime': datetime(2015, 1, 1),
                'UpdatedTime': datetime(2015, 1, 1),
                'PercentOfGraphUtilization': 123.0,
                'PercentOfGraphUtilizationUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    INVITED - Indicates that the member was sent an invitation but has not yet responded.
    VERIFICATION_IN_PROGRESS - Indicates that Detective is verifying that the account identifier and email address provided for the member account match. If they do match, then Detective sends the invitation. If the email address and account identifier don\'t match, then the member cannot be added to the behavior graph.
    VERIFICATION_FAILED - Indicates that the account and email address provided for the member account do not match, and Detective did not send an invitation to the account.
    ENABLED - Indicates that the member account accepted the invitation to contribute to the behavior graph.
    ACCEPTED_BUT_DISABLED - Indicates that the member account accepted the invitation but is prevented from contributing data to the behavior graph. DisabledReason provides the reason why the member account is not enabled.
    
    """
    pass

def list_members(GraphArn=None, NextToken=None, MaxResults=None):
    """
    Retrieves the list of member accounts for a behavior graph. Does not return member accounts that were removed from the behavior graph.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_members(
        GraphArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type GraphArn: string
    :param GraphArn: [REQUIRED]\nThe ARN of the behavior graph for which to retrieve the list of member accounts.\n

    :type NextToken: string
    :param NextToken: For requests to retrieve the next page of member account results, the pagination token that was returned with the previous page of results. The initial request does not include a pagination token.

    :type MaxResults: integer
    :param MaxResults: The maximum number of member accounts to include in the response. The total must be less than the overall limit on the number of results to return, which is currently 200.

    :rtype: dict

ReturnsResponse Syntax
{
    'MemberDetails': [
        {
            'AccountId': 'string',
            'EmailAddress': 'string',
            'GraphArn': 'string',
            'MasterId': 'string',
            'Status': 'INVITED'|'VERIFICATION_IN_PROGRESS'|'VERIFICATION_FAILED'|'ENABLED'|'ACCEPTED_BUT_DISABLED',
            'DisabledReason': 'VOLUME_TOO_HIGH'|'VOLUME_UNKNOWN',
            'InvitedTime': datetime(2015, 1, 1),
            'UpdatedTime': datetime(2015, 1, 1),
            'PercentOfGraphUtilization': 123.0,
            'PercentOfGraphUtilizationUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

MemberDetails (list) --
The list of member accounts in the behavior graph.
The results include member accounts that did not pass verification and member accounts that have not yet accepted the invitation to the behavior graph. The results do not include member accounts that were removed from the behavior graph.

(dict) --
Details about a member account that was invited to contribute to a behavior graph.

AccountId (string) --
The AWS account identifier for the member account.

EmailAddress (string) --
The AWS account root user email address for the member account.

GraphArn (string) --
The ARN of the behavior graph that the member account was invited to.

MasterId (string) --
The AWS account identifier of the master account for the behavior graph.

Status (string) --
The current membership status of the member account. The status can have one of the following values:

INVITED - Indicates that the member was sent an invitation but has not yet responded.
VERIFICATION_IN_PROGRESS - Indicates that Detective is verifying that the account identifier and email address provided for the member account match. If they do match, then Detective sends the invitation. If the email address and account identifier don\'t match, then the member cannot be added to the behavior graph.
VERIFICATION_FAILED - Indicates that the account and email address provided for the member account do not match, and Detective did not send an invitation to the account.
ENABLED - Indicates that the member account accepted the invitation to contribute to the behavior graph.
ACCEPTED_BUT_DISABLED - Indicates that the member account accepted the invitation but is prevented from contributing data to the behavior graph. DisabledReason provides the reason why the member account is not enabled.

Member accounts that declined an invitation or that were removed from the behavior graph are not included.

DisabledReason (string) --
For member accounts with a status of ACCEPTED_BUT_DISABLED , the reason that the member account is not enabled.
The reason can have one of the following values:

VOLUME_TOO_HIGH - Indicates that adding the member account would cause the data volume for the behavior graph to be too high.
VOLUME_UNKNOWN - Indicates that Detective is unable to verify the data volume for the member account. This is usually because the member account is not enrolled in Amazon GuardDuty.


InvitedTime (datetime) --
The date and time that Detective sent the invitation to the member account. The value is in milliseconds since the epoch.

UpdatedTime (datetime) --
The date and time that the member account was last updated. The value is in milliseconds since the epoch.

PercentOfGraphUtilization (float) --
The member account data volume as a percentage of the maximum allowed data volume. 0 indicates 0 percent, and 100 indicates 100 percent.
Note that this is not the percentage of the behavior graph data volume.
For example, the data volume for the behavior graph is 80 GB per day. The maximum data volume is 160 GB per day. If the data volume for the member account is 40 GB per day, then PercentOfGraphUtilization is 25. It represents 25% of the maximum allowed data volume.

PercentOfGraphUtilizationUpdatedTime (datetime) --
The date and time when the graph utilization percentage was last updated.





NextToken (string) --
If there are more member accounts remaining in the results, then this is the pagination token to use to request the next page of member accounts.







Exceptions

Detective.Client.exceptions.InternalServerException
Detective.Client.exceptions.ResourceNotFoundException
Detective.Client.exceptions.ValidationException


    :return: {
        'MemberDetails': [
            {
                'AccountId': 'string',
                'EmailAddress': 'string',
                'GraphArn': 'string',
                'MasterId': 'string',
                'Status': 'INVITED'|'VERIFICATION_IN_PROGRESS'|'VERIFICATION_FAILED'|'ENABLED'|'ACCEPTED_BUT_DISABLED',
                'DisabledReason': 'VOLUME_TOO_HIGH'|'VOLUME_UNKNOWN',
                'InvitedTime': datetime(2015, 1, 1),
                'UpdatedTime': datetime(2015, 1, 1),
                'PercentOfGraphUtilization': 123.0,
                'PercentOfGraphUtilizationUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    INVITED - Indicates that the member was sent an invitation but has not yet responded.
    VERIFICATION_IN_PROGRESS - Indicates that Detective is verifying that the account identifier and email address provided for the member account match. If they do match, then Detective sends the invitation. If the email address and account identifier don\'t match, then the member cannot be added to the behavior graph.
    VERIFICATION_FAILED - Indicates that the account and email address provided for the member account do not match, and Detective did not send an invitation to the account.
    ENABLED - Indicates that the member account accepted the invitation to contribute to the behavior graph.
    ACCEPTED_BUT_DISABLED - Indicates that the member account accepted the invitation but is prevented from contributing data to the behavior graph. DisabledReason provides the reason why the member account is not enabled.
    
    """
    pass

def reject_invitation(GraphArn=None):
    """
    Rejects an invitation to contribute the account data to a behavior graph. This operation must be called by a member account that has the INVITED status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reject_invitation(
        GraphArn='string'
    )
    
    
    :type GraphArn: string
    :param GraphArn: [REQUIRED]\nThe ARN of the behavior graph to reject the invitation to.\nThe member account\'s current member status in the behavior graph must be INVITED .\n

    """
    pass

def start_monitoring_member(GraphArn=None, AccountId=None):
    """
    Sends a request to enable data ingest for a member account that has a status of ACCEPTED_BUT_DISABLED .
    For valid member accounts, the status is updated as follows.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_monitoring_member(
        GraphArn='string',
        AccountId='string'
    )
    
    
    :type GraphArn: string
    :param GraphArn: [REQUIRED]\nThe ARN of the behavior graph.\n

    :type AccountId: string
    :param AccountId: [REQUIRED]\nThe account ID of the member account to try to enable.\nThe account must be an invited member account with a status of ACCEPTED_BUT_DISABLED .\n

    :returns: 
    GraphArn (string) -- [REQUIRED]
    The ARN of the behavior graph.
    
    AccountId (string) -- [REQUIRED]
    The account ID of the member account to try to enable.
    The account must be an invited member account with a status of ACCEPTED_BUT_DISABLED .
    
    
    """
    pass

