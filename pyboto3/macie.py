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

def associate_member_account(memberAccountId=None):
    """
    Associates a specified AWS account with Amazon Macie Classic as a member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_member_account(
        memberAccountId='string'
    )
    
    
    :type memberAccountId: string
    :param memberAccountId: [REQUIRED]\nThe ID of the AWS account that you want to associate with Amazon Macie Classic as a member account.\n

    """
    pass

def associate_s3_resources(memberAccountId=None, s3Resources=None):
    """
    Associates specified S3 resources with Amazon Macie Classic for monitoring and data classification. If memberAccountId isn\'t specified, the action associates specified S3 resources with Macie Classic for the current master account. If memberAccountId is specified, the action associates specified S3 resources with Macie Classic for the specified member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_s3_resources(
        memberAccountId='string',
        s3Resources=[
            {
                'bucketName': 'string',
                'prefix': 'string',
                'classificationType': {
                    'oneTime': 'FULL'|'NONE',
                    'continuous': 'FULL'
                }
            },
        ]
    )
    
    
    :type memberAccountId: string
    :param memberAccountId: The ID of the Amazon Macie Classic member account whose resources you want to associate with Macie Classic.

    :type s3Resources: list
    :param s3Resources: [REQUIRED]\nThe S3 resources that you want to associate with Amazon Macie Classic for monitoring and data classification.\n\n(dict) --The S3 resources that you want to associate with Amazon Macie Classic for monitoring and data classification. This data type is used as a request parameter in the AssociateS3Resources action and a response parameter in the ListS3Resources action.\n\nbucketName (string) -- [REQUIRED]The name of the S3 bucket that you want to associate with Amazon Macie Classic.\n\nprefix (string) --The prefix of the S3 bucket that you want to associate with Amazon Macie Classic.\n\nclassificationType (dict) -- [REQUIRED]The classification type that you want to specify for the resource associated with Amazon Macie Classic.\n\noneTime (string) -- [REQUIRED]A one-time classification of all of the existing objects in a specified S3 bucket.\n\ncontinuous (string) -- [REQUIRED]A continuous classification of the objects that are added to a specified S3 bucket. Amazon Macie Classic begins performing continuous classification after a bucket is successfully associated with Amazon Macie Classic.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'failedS3Resources': [
        {
            'failedItem': {
                'bucketName': 'string',
                'prefix': 'string'
            },
            'errorCode': 'string',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

failedS3Resources (list) --
S3 resources that couldn\'t be associated with Amazon Macie Classic. An error code and an error message are provided for each failed item.

(dict) --
Includes details about the failed S3 resources.

failedItem (dict) --
The failed S3 resources.

bucketName (string) --
The name of the S3 bucket.

prefix (string) --
The prefix of the S3 bucket.



errorCode (string) --
The status code of a failed item.

errorMessage (string) --
The error message of a failed item.











Exceptions

Macie.Client.exceptions.InvalidInputException
Macie.Client.exceptions.AccessDeniedException
Macie.Client.exceptions.LimitExceededException
Macie.Client.exceptions.InternalException


    :return: {
        'failedS3Resources': [
            {
                'failedItem': {
                    'bucketName': 'string',
                    'prefix': 'string'
                },
                'errorCode': 'string',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Macie.Client.exceptions.InvalidInputException
    Macie.Client.exceptions.AccessDeniedException
    Macie.Client.exceptions.LimitExceededException
    Macie.Client.exceptions.InternalException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def disassociate_member_account(memberAccountId=None):
    """
    Removes the specified member account from Amazon Macie Classic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_member_account(
        memberAccountId='string'
    )
    
    
    :type memberAccountId: string
    :param memberAccountId: [REQUIRED]\nThe ID of the member account that you want to remove from Amazon Macie Classic.\n

    """
    pass

def disassociate_s3_resources(memberAccountId=None, associatedS3Resources=None):
    """
    Removes specified S3 resources from being monitored by Amazon Macie Classic. If memberAccountId isn\'t specified, the action removes specified S3 resources from Macie Classic for the current master account. If memberAccountId is specified, the action removes specified S3 resources from Macie Classic for the specified member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_s3_resources(
        memberAccountId='string',
        associatedS3Resources=[
            {
                'bucketName': 'string',
                'prefix': 'string'
            },
        ]
    )
    
    
    :type memberAccountId: string
    :param memberAccountId: The ID of the Amazon Macie Classic member account whose resources you want to remove from being monitored by Amazon Macie Classic.

    :type associatedS3Resources: list
    :param associatedS3Resources: [REQUIRED]\nThe S3 resources (buckets or prefixes) that you want to remove from being monitored and classified by Amazon Macie Classic.\n\n(dict) --Contains information about the S3 resource. This data type is used as a request parameter in the DisassociateS3Resources action and can be used as a response parameter in the AssociateS3Resources and UpdateS3Resources actions.\n\nbucketName (string) -- [REQUIRED]The name of the S3 bucket.\n\nprefix (string) --The prefix of the S3 bucket.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'failedS3Resources': [
        {
            'failedItem': {
                'bucketName': 'string',
                'prefix': 'string'
            },
            'errorCode': 'string',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

failedS3Resources (list) --
S3 resources that couldn\'t be removed from being monitored and classified by Amazon Macie Classic. An error code and an error message are provided for each failed item.

(dict) --
Includes details about the failed S3 resources.

failedItem (dict) --
The failed S3 resources.

bucketName (string) --
The name of the S3 bucket.

prefix (string) --
The prefix of the S3 bucket.



errorCode (string) --
The status code of a failed item.

errorMessage (string) --
The error message of a failed item.











Exceptions

Macie.Client.exceptions.InvalidInputException
Macie.Client.exceptions.AccessDeniedException
Macie.Client.exceptions.InternalException


    :return: {
        'failedS3Resources': [
            {
                'failedItem': {
                    'bucketName': 'string',
                    'prefix': 'string'
                },
                'errorCode': 'string',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Macie.Client.exceptions.InvalidInputException
    Macie.Client.exceptions.AccessDeniedException
    Macie.Client.exceptions.InternalException
    
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

def list_member_accounts(nextToken=None, maxResults=None):
    """
    Lists all Amazon Macie Classic member accounts for the current Amazon Macie Classic master account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_member_accounts(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: Use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListMemberAccounts action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: Use this parameter to indicate the maximum number of items that you want in the response. The default value is 250.

    :rtype: dict

ReturnsResponse Syntax
{
    'memberAccounts': [
        {
            'accountId': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

memberAccounts (list) --
A list of the Amazon Macie Classic member accounts returned by the action. The current master account is also included in this list.

(dict) --
Contains information about the Amazon Macie Classic member account.

accountId (string) --
The AWS account ID of the Amazon Macie Classic member account.





nextToken (string) --
When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Macie.Client.exceptions.InternalException
Macie.Client.exceptions.InvalidInputException


    :return: {
        'memberAccounts': [
            {
                'accountId': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Macie.Client.exceptions.InternalException
    Macie.Client.exceptions.InvalidInputException
    
    """
    pass

def list_s3_resources(memberAccountId=None, nextToken=None, maxResults=None):
    """
    Lists all the S3 resources associated with Amazon Macie Classic. If memberAccountId isn\'t specified, the action lists the S3 resources associated with Amazon Macie Classic for the current master account. If memberAccountId is specified, the action lists the S3 resources associated with Amazon Macie Classic for the specified member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_s3_resources(
        memberAccountId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type memberAccountId: string
    :param memberAccountId: The Amazon Macie Classic member account ID whose associated S3 resources you want to list.

    :type nextToken: string
    :param nextToken: Use this parameter when paginating results. Set its value to null on your first call to the ListS3Resources action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.

    :type maxResults: integer
    :param maxResults: Use this parameter to indicate the maximum number of items that you want in the response. The default value is 250.

    :rtype: dict

ReturnsResponse Syntax
{
    's3Resources': [
        {
            'bucketName': 'string',
            'prefix': 'string',
            'classificationType': {
                'oneTime': 'FULL'|'NONE',
                'continuous': 'FULL'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

s3Resources (list) --
A list of the associated S3 resources returned by the action.

(dict) --
The S3 resources that you want to associate with Amazon Macie Classic for monitoring and data classification. This data type is used as a request parameter in the AssociateS3Resources action and a response parameter in the ListS3Resources action.

bucketName (string) --
The name of the S3 bucket that you want to associate with Amazon Macie Classic.

prefix (string) --
The prefix of the S3 bucket that you want to associate with Amazon Macie Classic.

classificationType (dict) --
The classification type that you want to specify for the resource associated with Amazon Macie Classic.

oneTime (string) --
A one-time classification of all of the existing objects in a specified S3 bucket.

continuous (string) --
A continuous classification of the objects that are added to a specified S3 bucket. Amazon Macie Classic begins performing continuous classification after a bucket is successfully associated with Amazon Macie Classic.







nextToken (string) --
When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.







Exceptions

Macie.Client.exceptions.InvalidInputException
Macie.Client.exceptions.AccessDeniedException
Macie.Client.exceptions.InternalException


    :return: {
        's3Resources': [
            {
                'bucketName': 'string',
                'prefix': 'string',
                'classificationType': {
                    'oneTime': 'FULL'|'NONE',
                    'continuous': 'FULL'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Macie.Client.exceptions.InvalidInputException
    Macie.Client.exceptions.AccessDeniedException
    Macie.Client.exceptions.InternalException
    
    """
    pass

def update_s3_resources(memberAccountId=None, s3ResourcesUpdate=None):
    """
    Updates the classification types for the specified S3 resources. If memberAccountId isn\'t specified, the action updates the classification types of the S3 resources associated with Amazon Macie Classic for the current master account. If memberAccountId is specified, the action updates the classification types of the S3 resources associated with Amazon Macie Classic for the specified member account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_s3_resources(
        memberAccountId='string',
        s3ResourcesUpdate=[
            {
                'bucketName': 'string',
                'prefix': 'string',
                'classificationTypeUpdate': {
                    'oneTime': 'FULL'|'NONE',
                    'continuous': 'FULL'
                }
            },
        ]
    )
    
    
    :type memberAccountId: string
    :param memberAccountId: The AWS ID of the Amazon Macie Classic member account whose S3 resources\' classification types you want to update.

    :type s3ResourcesUpdate: list
    :param s3ResourcesUpdate: [REQUIRED]\nThe S3 resources whose classification types you want to update.\n\n(dict) --The S3 resources whose classification types you want to update. This data type is used as a request parameter in the UpdateS3Resources action.\n\nbucketName (string) -- [REQUIRED]The name of the S3 bucket whose classification types you want to update.\n\nprefix (string) --The prefix of the S3 bucket whose classification types you want to update.\n\nclassificationTypeUpdate (dict) -- [REQUIRED]The classification type that you want to update for the resource associated with Amazon Macie Classic.\n\noneTime (string) --A one-time classification of all of the existing objects in a specified S3 bucket.\n\ncontinuous (string) --A continuous classification of the objects that are added to a specified S3 bucket. Amazon Macie Classic begins performing continuous classification after a bucket is successfully associated with Amazon Macie Classic.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'failedS3Resources': [
        {
            'failedItem': {
                'bucketName': 'string',
                'prefix': 'string'
            },
            'errorCode': 'string',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

failedS3Resources (list) --
The S3 resources whose classification types can\'t be updated. An error code and an error message are provided for each failed item.

(dict) --
Includes details about the failed S3 resources.

failedItem (dict) --
The failed S3 resources.

bucketName (string) --
The name of the S3 bucket.

prefix (string) --
The prefix of the S3 bucket.



errorCode (string) --
The status code of a failed item.

errorMessage (string) --
The error message of a failed item.











Exceptions

Macie.Client.exceptions.InvalidInputException
Macie.Client.exceptions.AccessDeniedException
Macie.Client.exceptions.InternalException


    :return: {
        'failedS3Resources': [
            {
                'failedItem': {
                    'bucketName': 'string',
                    'prefix': 'string'
                },
                'errorCode': 'string',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    Macie.Client.exceptions.InvalidInputException
    Macie.Client.exceptions.AccessDeniedException
    Macie.Client.exceptions.InternalException
    
    """
    pass

