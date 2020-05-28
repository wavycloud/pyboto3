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

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_analyzer(analyzerName=None, archiveRules=None, clientToken=None, tags=None, type=None):
    """
    Creates an analyzer for your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_analyzer(
        analyzerName='string',
        archiveRules=[
            {
                'filter': {
                    'string': {
                        'contains': [
                            'string',
                        ],
                        'eq': [
                            'string',
                        ],
                        'exists': True|False,
                        'neq': [
                            'string',
                        ]
                    }
                },
                'ruleName': 'string'
            },
        ],
        clientToken='string',
        tags={
            'string': 'string'
        },
        type='ACCOUNT'|'ORGANIZATION'
    )
    
    
    :type analyzerName: string
    :param analyzerName: [REQUIRED]\nThe name of the analyzer to create.\n

    :type archiveRules: list
    :param archiveRules: Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.\n\n(dict) --An criterion statement in an archive rule. Each archive rule may have multiple criteria.\n\nfilter (dict) -- [REQUIRED]The condition and values for a criterion.\n\n(string) --\n(dict) --The criteria to use in the filter that defines the archive rule.\n\ncontains (list) --A 'contains' operator to match for the filter used to create the rule.\n\n(string) --\n\n\neq (list) --An 'equals' operator to match for the filter used to create the rule.\n\n(string) --\n\n\nexists (boolean) --An 'exists' operator to match for the filter used to create the rule.\n\nneq (list) --A 'not equals' operator to match for the filter used to create the rule.\n\n(string) --\n\n\n\n\n\n\n\n\nruleName (string) -- [REQUIRED]The name of the rule.\n\n\n\n\n

    :type clientToken: string
    :param clientToken: A client token.\nThis field is autopopulated if not provided.\n

    :type tags: dict
    :param tags: The tags to apply to the analyzer.\n\n(string) --\n(string) --\n\n\n\n

    :type type: string
    :param type: [REQUIRED]\nThe type of analyzer to create. Only ACCOUNT analyzers are supported. You can create only one analyzer per account per Region.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string'
}


Response Structure

(dict) --
The response to the request to create an analyzer.

arn (string) --
The ARN of the analyzer that was created by the request.







Exceptions

AccessAnalyzer.Client.exceptions.ConflictException
AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ServiceQuotaExceededException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {
        'arn': 'string'
    }
    
    
    :returns: 
    AccessAnalyzer.Client.exceptions.ConflictException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ServiceQuotaExceededException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

def create_archive_rule(analyzerName=None, clientToken=None, filter=None, ruleName=None):
    """
    Creates an archive rule for the specified analyzer. Archive rules automatically archive findings that meet the criteria you define when you create the rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_archive_rule(
        analyzerName='string',
        clientToken='string',
        filter={
            'string': {
                'contains': [
                    'string',
                ],
                'eq': [
                    'string',
                ],
                'exists': True|False,
                'neq': [
                    'string',
                ]
            }
        },
        ruleName='string'
    )
    
    
    :type analyzerName: string
    :param analyzerName: [REQUIRED]\nThe name of the created analyzer.\n

    :type clientToken: string
    :param clientToken: A client token.\nThis field is autopopulated if not provided.\n

    :type filter: dict
    :param filter: [REQUIRED]\nThe criteria for the rule.\n\n(string) --\n(dict) --The criteria to use in the filter that defines the archive rule.\n\ncontains (list) --A 'contains' operator to match for the filter used to create the rule.\n\n(string) --\n\n\neq (list) --An 'equals' operator to match for the filter used to create the rule.\n\n(string) --\n\n\nexists (boolean) --An 'exists' operator to match for the filter used to create the rule.\n\nneq (list) --A 'not equals' operator to match for the filter used to create the rule.\n\n(string) --\n\n\n\n\n\n\n\n

    :type ruleName: string
    :param ruleName: [REQUIRED]\nThe name of the rule to create.\n

    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ConflictException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ServiceQuotaExceededException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

def delete_analyzer(analyzerName=None, clientToken=None):
    """
    Deletes the specified analyzer. When you delete an analyzer, Access Analyzer is disabled for the account in the current or specific Region. All findings that were generated by the analyzer are deleted. You cannot undo this action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_analyzer(
        analyzerName='string',
        clientToken='string'
    )
    
    
    :type analyzerName: string
    :param analyzerName: [REQUIRED]\nThe name of the analyzer to delete.\n

    :type clientToken: string
    :param clientToken: A client token.\nThis field is autopopulated if not provided.\n

    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

def delete_archive_rule(analyzerName=None, clientToken=None, ruleName=None):
    """
    Deletes the specified archive rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_archive_rule(
        analyzerName='string',
        clientToken='string',
        ruleName='string'
    )
    
    
    :type analyzerName: string
    :param analyzerName: [REQUIRED]\nThe name of the analyzer that associated with the archive rule to delete.\n

    :type clientToken: string
    :param clientToken: A client token.\nThis field is autopopulated if not provided.\n

    :type ruleName: string
    :param ruleName: [REQUIRED]\nThe name of the rule to delete.\n

    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
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

def get_analyzed_resource(analyzerArn=None, resourceArn=None):
    """
    Retrieves information about a resource that was analyzed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_analyzed_resource(
        analyzerArn='string',
        resourceArn='string'
    )
    
    
    :type analyzerArn: string
    :param analyzerArn: [REQUIRED]\nThe ARN of the analyzer to retrieve information from.\n

    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource to retrieve information about.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'resource': {
        'actions': [
            'string',
        ],
        'analyzedAt': datetime(2015, 1, 1),
        'createdAt': datetime(2015, 1, 1),
        'error': 'string',
        'isPublic': True|False,
        'resourceArn': 'string',
        'resourceOwnerAccount': 'string',
        'resourceType': 'AWS::IAM::Role'|'AWS::KMS::Key'|'AWS::Lambda::Function'|'AWS::Lambda::LayerVersion'|'AWS::S3::Bucket'|'AWS::SQS::Queue',
        'sharedVia': [
            'string',
        ],
        'status': 'ACTIVE'|'ARCHIVED'|'RESOLVED',
        'updatedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
The response to the request.

resource (dict) --
An AnalyedResource object that contains information that Access Analyzer found when it analyzed the resource.

actions (list) --
The actions that an external principal is granted permission to use by the policy that generated the finding.

(string) --


analyzedAt (datetime) --
The time at which the resource was analyzed.

createdAt (datetime) --
The time at which the finding was created.

error (string) --
An error message.

isPublic (boolean) --
Indicates whether the policy that generated the finding grants public access to the resource.

resourceArn (string) --
The ARN of the resource that was analyzed.

resourceOwnerAccount (string) --
The AWS account ID that owns the resource.

resourceType (string) --
The type of the resource that was analyzed.

sharedVia (list) --
Indicates how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.

(string) --


status (string) --
The current status of the finding generated from the analyzed resource.

updatedAt (datetime) --
The time at which the finding was updated.









Exceptions

AccessAnalyzer.Client.exceptions.ResourceNotFoundException
AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {
        'resource': {
            'actions': [
                'string',
            ],
            'analyzedAt': datetime(2015, 1, 1),
            'createdAt': datetime(2015, 1, 1),
            'error': 'string',
            'isPublic': True|False,
            'resourceArn': 'string',
            'resourceOwnerAccount': 'string',
            'resourceType': 'AWS::IAM::Role'|'AWS::KMS::Key'|'AWS::Lambda::Function'|'AWS::Lambda::LayerVersion'|'AWS::S3::Bucket'|'AWS::SQS::Queue',
            'sharedVia': [
                'string',
            ],
            'status': 'ACTIVE'|'ARCHIVED'|'RESOLVED',
            'updatedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_analyzer(analyzerName=None):
    """
    Retrieves information about the specified analyzer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_analyzer(
        analyzerName='string'
    )
    
    
    :type analyzerName: string
    :param analyzerName: [REQUIRED]\nThe name of the analyzer retrieved.\n

    :rtype: dict
ReturnsResponse Syntax{
    'analyzer': {
        'arn': 'string',
        'createdAt': datetime(2015, 1, 1),
        'lastResourceAnalyzed': 'string',
        'lastResourceAnalyzedAt': datetime(2015, 1, 1),
        'name': 'string',
        'status': 'ACTIVE'|'CREATING'|'DISABLED'|'FAILED',
        'statusReason': {
            'code': 'AWS_SERVICE_ACCESS_DISABLED'|'DELEGATED_ADMINISTRATOR_DEREGISTERED'|'ORGANIZATION_DELETED'|'SERVICE_LINKED_ROLE_CREATION_FAILED'
        },
        'tags': {
            'string': 'string'
        },
        'type': 'ACCOUNT'|'ORGANIZATION'
    }
}


Response Structure

(dict) --The response to the request.

analyzer (dict) --An AnalyzerSummary object that contains information about the analyzer.

arn (string) --The ARN of the analyzer.

createdAt (datetime) --A timestamp for the time at which the analyzer was created.

lastResourceAnalyzed (string) --The resource that was most recently analyzed by the analyzer.

lastResourceAnalyzedAt (datetime) --The time at which the most recently analyzed resource was analyzed.

name (string) --The name of the analyzer.

status (string) --The status of the analyzer. An Active analyzer successfully monitors supported resources and generates new findings. The analyzer is Disabled when a user action, such as removing trusted access for IAM Access Analyzer from AWS Organizations, causes the analyzer to stop generating new findings. The status is Creating when the analyzer creation is in progress and Failed when the analyzer creation has failed.

statusReason (dict) --The statusReason provides more details about the current status of the analyzer. For example, if the creation for the analyzer fails, a Failed status is displayed. For an analyzer with organization as the type, this failure can be due to an issue with creating the service-linked roles required in the member accounts of the AWS organization.

code (string) --The reason code for the current status of the analyzer.



tags (dict) --The tags added to the analyzer.

(string) --
(string) --




type (string) --The type of analyzer, which corresponds to the zone of trust chosen for the analyzer.








Exceptions

AccessAnalyzer.Client.exceptions.ResourceNotFoundException
AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {
        'analyzer': {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastResourceAnalyzed': 'string',
            'lastResourceAnalyzedAt': datetime(2015, 1, 1),
            'name': 'string',
            'status': 'ACTIVE'|'CREATING'|'DISABLED'|'FAILED',
            'statusReason': {
                'code': 'AWS_SERVICE_ACCESS_DISABLED'|'DELEGATED_ADMINISTRATOR_DEREGISTERED'|'ORGANIZATION_DELETED'|'SERVICE_LINKED_ROLE_CREATION_FAILED'
            },
            'tags': {
                'string': 'string'
            },
            'type': 'ACCOUNT'|'ORGANIZATION'
        }
    }
    
    
    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

def get_archive_rule(analyzerName=None, ruleName=None):
    """
    Retrieves information about an archive rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_archive_rule(
        analyzerName='string',
        ruleName='string'
    )
    
    
    :type analyzerName: string
    :param analyzerName: [REQUIRED]\nThe name of the analyzer to retrieve rules from.\n

    :type ruleName: string
    :param ruleName: [REQUIRED]\nThe name of the rule to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'archiveRule': {
        'createdAt': datetime(2015, 1, 1),
        'filter': {
            'string': {
                'contains': [
                    'string',
                ],
                'eq': [
                    'string',
                ],
                'exists': True|False,
                'neq': [
                    'string',
                ]
            }
        },
        'ruleName': 'string',
        'updatedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
The response to the request.

archiveRule (dict) --
Contains information about an archive rule.

createdAt (datetime) --
The time at which the archive rule was created.

filter (dict) --
A filter used to define the archive rule.

(string) --

(dict) --
The criteria to use in the filter that defines the archive rule.

contains (list) --
A "contains" operator to match for the filter used to create the rule.

(string) --


eq (list) --
An "equals" operator to match for the filter used to create the rule.

(string) --


exists (boolean) --
An "exists" operator to match for the filter used to create the rule.

neq (list) --
A "not equals" operator to match for the filter used to create the rule.

(string) --








ruleName (string) --
The name of the archive rule.

updatedAt (datetime) --
The time at which the archive rule was last updated.









Exceptions

AccessAnalyzer.Client.exceptions.ResourceNotFoundException
AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {
        'archiveRule': {
            'createdAt': datetime(2015, 1, 1),
            'filter': {
                'string': {
                    'contains': [
                        'string',
                    ],
                    'eq': [
                        'string',
                    ],
                    'exists': True|False,
                    'neq': [
                        'string',
                    ]
                }
            },
            'ruleName': 'string',
            'updatedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_finding(analyzerArn=None, id=None):
    """
    Retrieves information about the specified finding.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_finding(
        analyzerArn='string',
        id='string'
    )
    
    
    :type analyzerArn: string
    :param analyzerArn: [REQUIRED]\nThe ARN of the analyzer that generated the finding.\n

    :type id: string
    :param id: [REQUIRED]\nThe ID of the finding to retrieve.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'finding': {
        'action': [
            'string',
        ],
        'analyzedAt': datetime(2015, 1, 1),
        'condition': {
            'string': 'string'
        },
        'createdAt': datetime(2015, 1, 1),
        'error': 'string',
        'id': 'string',
        'isPublic': True|False,
        'principal': {
            'string': 'string'
        },
        'resource': 'string',
        'resourceOwnerAccount': 'string',
        'resourceType': 'AWS::IAM::Role'|'AWS::KMS::Key'|'AWS::Lambda::Function'|'AWS::Lambda::LayerVersion'|'AWS::S3::Bucket'|'AWS::SQS::Queue',
        'sources': [
            {
                'detail': {
                    'accessPointArn': 'string'
                },
                'type': 'BUCKET_ACL'|'POLICY'|'S3_ACCESS_POINT'
            },
        ],
        'status': 'ACTIVE'|'ARCHIVED'|'RESOLVED',
        'updatedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
The response to the request.

finding (dict) --
A finding object that contains finding details.

action (list) --
The action in the analyzed policy statement that an external principal has permission to use.

(string) --


analyzedAt (datetime) --
The time at which the resource was analyzed.

condition (dict) --
The condition in the analyzed policy statement that resulted in a finding.

(string) --
(string) --




createdAt (datetime) --
The time at which the finding was generated.

error (string) --
An error.

id (string) --
The ID of the finding.

isPublic (boolean) --
Indicates whether the policy that generated the finding allows public access to the resource.

principal (dict) --
The external principal that access to a resource within the zone of trust.

(string) --
(string) --




resource (string) --
The resource that an external principal has access to.

resourceOwnerAccount (string) --
The AWS account ID that owns the resource.

resourceType (string) --
The type of the resource reported in the finding.

sources (list) --
The sources of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

(dict) --
The source of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

detail (dict) --
Includes details about how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.

accessPointArn (string) --
The ARN of the access point that generated the finding.



type (string) --
Indicates the type of access that generated the finding.





status (string) --
The current status of the finding.

updatedAt (datetime) --
The time at which the finding was updated.









Exceptions

AccessAnalyzer.Client.exceptions.ResourceNotFoundException
AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {
        'finding': {
            'action': [
                'string',
            ],
            'analyzedAt': datetime(2015, 1, 1),
            'condition': {
                'string': 'string'
            },
            'createdAt': datetime(2015, 1, 1),
            'error': 'string',
            'id': 'string',
            'isPublic': True|False,
            'principal': {
                'string': 'string'
            },
            'resource': 'string',
            'resourceOwnerAccount': 'string',
            'resourceType': 'AWS::IAM::Role'|'AWS::KMS::Key'|'AWS::Lambda::Function'|'AWS::Lambda::LayerVersion'|'AWS::S3::Bucket'|'AWS::SQS::Queue',
            'sources': [
                {
                    'detail': {
                        'accessPointArn': 'string'
                    },
                    'type': 'BUCKET_ACL'|'POLICY'|'S3_ACCESS_POINT'
                },
            ],
            'status': 'ACTIVE'|'ARCHIVED'|'RESOLVED',
            'updatedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
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

def list_analyzed_resources(analyzerArn=None, maxResults=None, nextToken=None, resourceType=None):
    """
    Retrieves a list of resources of the specified type that have been analyzed by the specified analyzer..
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_analyzed_resources(
        analyzerArn='string',
        maxResults=123,
        nextToken='string',
        resourceType='AWS::IAM::Role'|'AWS::KMS::Key'|'AWS::Lambda::Function'|'AWS::Lambda::LayerVersion'|'AWS::S3::Bucket'|'AWS::SQS::Queue'
    )
    
    
    :type analyzerArn: string
    :param analyzerArn: [REQUIRED]\nThe ARN of the analyzer to retrieve a list of analyzed resources from.\n

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :type nextToken: string
    :param nextToken: A token used for pagination of results returned.

    :type resourceType: string
    :param resourceType: The type of resource.

    :rtype: dict

ReturnsResponse Syntax
{
    'analyzedResources': [
        {
            'resourceArn': 'string',
            'resourceOwnerAccount': 'string',
            'resourceType': 'AWS::IAM::Role'|'AWS::KMS::Key'|'AWS::Lambda::Function'|'AWS::Lambda::LayerVersion'|'AWS::S3::Bucket'|'AWS::SQS::Queue'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The response to the request.

analyzedResources (list) --
A list of resources that were analyzed.

(dict) --
Contains the ARN of the analyzed resource.

resourceArn (string) --
The ARN of the analyzed resource.

resourceOwnerAccount (string) --
The AWS account ID that owns the resource.

resourceType (string) --
The type of resource that was analyzed.





nextToken (string) --
A token used for pagination of results returned.







Exceptions

AccessAnalyzer.Client.exceptions.ResourceNotFoundException
AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {
        'analyzedResources': [
            {
                'resourceArn': 'string',
                'resourceOwnerAccount': 'string',
                'resourceType': 'AWS::IAM::Role'|'AWS::KMS::Key'|'AWS::Lambda::Function'|'AWS::Lambda::LayerVersion'|'AWS::S3::Bucket'|'AWS::SQS::Queue'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

def list_analyzers(maxResults=None, nextToken=None, type=None):
    """
    Retrieves a list of analyzers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_analyzers(
        maxResults=123,
        nextToken='string',
        type='ACCOUNT'|'ORGANIZATION'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :type nextToken: string
    :param nextToken: A token used for pagination of results returned.

    :type type: string
    :param type: The type of analyzer.

    :rtype: dict

ReturnsResponse Syntax
{
    'analyzers': [
        {
            'arn': 'string',
            'createdAt': datetime(2015, 1, 1),
            'lastResourceAnalyzed': 'string',
            'lastResourceAnalyzedAt': datetime(2015, 1, 1),
            'name': 'string',
            'status': 'ACTIVE'|'CREATING'|'DISABLED'|'FAILED',
            'statusReason': {
                'code': 'AWS_SERVICE_ACCESS_DISABLED'|'DELEGATED_ADMINISTRATOR_DEREGISTERED'|'ORGANIZATION_DELETED'|'SERVICE_LINKED_ROLE_CREATION_FAILED'
            },
            'tags': {
                'string': 'string'
            },
            'type': 'ACCOUNT'|'ORGANIZATION'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The response to the request.

analyzers (list) --
The analyzers retrieved.

(dict) --
Contains information about the analyzer.

arn (string) --
The ARN of the analyzer.

createdAt (datetime) --
A timestamp for the time at which the analyzer was created.

lastResourceAnalyzed (string) --
The resource that was most recently analyzed by the analyzer.

lastResourceAnalyzedAt (datetime) --
The time at which the most recently analyzed resource was analyzed.

name (string) --
The name of the analyzer.

status (string) --
The status of the analyzer. An Active analyzer successfully monitors supported resources and generates new findings. The analyzer is Disabled when a user action, such as removing trusted access for IAM Access Analyzer from AWS Organizations, causes the analyzer to stop generating new findings. The status is Creating when the analyzer creation is in progress and Failed when the analyzer creation has failed.

statusReason (dict) --
The statusReason provides more details about the current status of the analyzer. For example, if the creation for the analyzer fails, a Failed status is displayed. For an analyzer with organization as the type, this failure can be due to an issue with creating the service-linked roles required in the member accounts of the AWS organization.

code (string) --
The reason code for the current status of the analyzer.



tags (dict) --
The tags added to the analyzer.

(string) --
(string) --




type (string) --
The type of analyzer, which corresponds to the zone of trust chosen for the analyzer.





nextToken (string) --
A token used for pagination of results returned.







Exceptions

AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {
        'analyzers': [
            {
                'arn': 'string',
                'createdAt': datetime(2015, 1, 1),
                'lastResourceAnalyzed': 'string',
                'lastResourceAnalyzedAt': datetime(2015, 1, 1),
                'name': 'string',
                'status': 'ACTIVE'|'CREATING'|'DISABLED'|'FAILED',
                'statusReason': {
                    'code': 'AWS_SERVICE_ACCESS_DISABLED'|'DELEGATED_ADMINISTRATOR_DEREGISTERED'|'ORGANIZATION_DELETED'|'SERVICE_LINKED_ROLE_CREATION_FAILED'
                },
                'tags': {
                    'string': 'string'
                },
                'type': 'ACCOUNT'|'ORGANIZATION'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_archive_rules(analyzerName=None, maxResults=None, nextToken=None):
    """
    Retrieves a list of archive rules created for the specified analyzer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_archive_rules(
        analyzerName='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type analyzerName: string
    :param analyzerName: [REQUIRED]\nThe name of the analyzer to retrieve rules from.\n

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the request.

    :type nextToken: string
    :param nextToken: A token used for pagination of results returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'archiveRules': [
        {
            'createdAt': datetime(2015, 1, 1),
            'filter': {
                'string': {
                    'contains': [
                        'string',
                    ],
                    'eq': [
                        'string',
                    ],
                    'exists': True|False,
                    'neq': [
                        'string',
                    ]
                }
            },
            'ruleName': 'string',
            'updatedAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The response to the request.

archiveRules (list) --
A list of archive rules created for the specified analyzer.

(dict) --
Contains information about an archive rule.

createdAt (datetime) --
The time at which the archive rule was created.

filter (dict) --
A filter used to define the archive rule.

(string) --

(dict) --
The criteria to use in the filter that defines the archive rule.

contains (list) --
A "contains" operator to match for the filter used to create the rule.

(string) --


eq (list) --
An "equals" operator to match for the filter used to create the rule.

(string) --


exists (boolean) --
An "exists" operator to match for the filter used to create the rule.

neq (list) --
A "not equals" operator to match for the filter used to create the rule.

(string) --








ruleName (string) --
The name of the archive rule.

updatedAt (datetime) --
The time at which the archive rule was last updated.





nextToken (string) --
A token used for pagination of results returned.







Exceptions

AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {
        'archiveRules': [
            {
                'createdAt': datetime(2015, 1, 1),
                'filter': {
                    'string': {
                        'contains': [
                            'string',
                        ],
                        'eq': [
                            'string',
                        ],
                        'exists': True|False,
                        'neq': [
                            'string',
                        ]
                    }
                },
                'ruleName': 'string',
                'updatedAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_findings(analyzerArn=None, filter=None, maxResults=None, nextToken=None, sort=None):
    """
    Retrieves a list of findings generated by the specified analyzer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_findings(
        analyzerArn='string',
        filter={
            'string': {
                'contains': [
                    'string',
                ],
                'eq': [
                    'string',
                ],
                'exists': True|False,
                'neq': [
                    'string',
                ]
            }
        },
        maxResults=123,
        nextToken='string',
        sort={
            'attributeName': 'string',
            'orderBy': 'ASC'|'DESC'
        }
    )
    
    
    :type analyzerArn: string
    :param analyzerArn: [REQUIRED]\nThe ARN of the analyzer to retrieve findings from.\n

    :type filter: dict
    :param filter: A filter to match for the findings to return.\n\n(string) --\n(dict) --The criteria to use in the filter that defines the archive rule.\n\ncontains (list) --A 'contains' operator to match for the filter used to create the rule.\n\n(string) --\n\n\neq (list) --An 'equals' operator to match for the filter used to create the rule.\n\n(string) --\n\n\nexists (boolean) --An 'exists' operator to match for the filter used to create the rule.\n\nneq (list) --A 'not equals' operator to match for the filter used to create the rule.\n\n(string) --\n\n\n\n\n\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :type nextToken: string
    :param nextToken: A token used for pagination of results returned.

    :type sort: dict
    :param sort: The sort order for the findings returned.\n\nattributeName (string) --The name of the attribute to sort on.\n\norderBy (string) --The sort order, ascending or descending.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'findings': [
        {
            'action': [
                'string',
            ],
            'analyzedAt': datetime(2015, 1, 1),
            'condition': {
                'string': 'string'
            },
            'createdAt': datetime(2015, 1, 1),
            'error': 'string',
            'id': 'string',
            'isPublic': True|False,
            'principal': {
                'string': 'string'
            },
            'resource': 'string',
            'resourceOwnerAccount': 'string',
            'resourceType': 'AWS::IAM::Role'|'AWS::KMS::Key'|'AWS::Lambda::Function'|'AWS::Lambda::LayerVersion'|'AWS::S3::Bucket'|'AWS::SQS::Queue',
            'sources': [
                {
                    'detail': {
                        'accessPointArn': 'string'
                    },
                    'type': 'BUCKET_ACL'|'POLICY'|'S3_ACCESS_POINT'
                },
            ],
            'status': 'ACTIVE'|'ARCHIVED'|'RESOLVED',
            'updatedAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The response to the request.

findings (list) --
A list of findings retrieved from the analyzer that match the filter criteria specified, if any.

(dict) --
Contains information about a finding.

action (list) --
The action in the analyzed policy statement that an external principal has permission to use.

(string) --


analyzedAt (datetime) --
The time at which the resource-based policy that generated the finding was analyzed.

condition (dict) --
The condition in the analyzed policy statement that resulted in a finding.

(string) --
(string) --




createdAt (datetime) --
The time at which the finding was created.

error (string) --
The error that resulted in an Error finding.

id (string) --
The ID of the finding.

isPublic (boolean) --
Indicates whether the finding reports a resource that has a policy that allows public access.

principal (dict) --
The external principal that has access to a resource within the zone of trust.

(string) --
(string) --




resource (string) --
The resource that the external principal has access to.

resourceOwnerAccount (string) --
The AWS account ID that owns the resource.

resourceType (string) --
The type of the resource that the external principal has access to.

sources (list) --
The sources of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

(dict) --
The source of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

detail (dict) --
Includes details about how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.

accessPointArn (string) --
The ARN of the access point that generated the finding.



type (string) --
Indicates the type of access that generated the finding.





status (string) --
The status of the finding.

updatedAt (datetime) --
The time at which the finding was most recently updated.





nextToken (string) --
A token used for pagination of results returned.







Exceptions

AccessAnalyzer.Client.exceptions.ResourceNotFoundException
AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {
        'findings': [
            {
                'action': [
                    'string',
                ],
                'analyzedAt': datetime(2015, 1, 1),
                'condition': {
                    'string': 'string'
                },
                'createdAt': datetime(2015, 1, 1),
                'error': 'string',
                'id': 'string',
                'isPublic': True|False,
                'principal': {
                    'string': 'string'
                },
                'resource': 'string',
                'resourceOwnerAccount': 'string',
                'resourceType': 'AWS::IAM::Role'|'AWS::KMS::Key'|'AWS::Lambda::Function'|'AWS::Lambda::LayerVersion'|'AWS::S3::Bucket'|'AWS::SQS::Queue',
                'sources': [
                    {
                        'detail': {
                            'accessPointArn': 'string'
                        },
                        'type': 'BUCKET_ACL'|'POLICY'|'S3_ACCESS_POINT'
                    },
                ],
                'status': 'ACTIVE'|'ARCHIVED'|'RESOLVED',
                'updatedAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Retrieves a list of tags applied to the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource to retrieve tags from.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --The response to the request.

tags (dict) --The tags that are applied to the specified resource.

(string) --
(string) --









Exceptions

AccessAnalyzer.Client.exceptions.ResourceNotFoundException
AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

def start_resource_scan(analyzerArn=None, resourceArn=None):
    """
    Immediately starts a scan of the policies applied to the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_resource_scan(
        analyzerArn='string',
        resourceArn='string'
    )
    
    
    :type analyzerArn: string
    :param analyzerArn: [REQUIRED]\nThe ARN of the analyzer to use to scan the policies applied to the specified resource.\n

    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource to scan.\n

    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds a tag to the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource to add the tag to.\n

    :type tags: dict
    :param tags: [REQUIRED]\nThe tags to add to the resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The response to the request.





Exceptions

AccessAnalyzer.Client.exceptions.ResourceNotFoundException
AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes a tag from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource to remove the tag from.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe key for the tag to add.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The response to the request.





Exceptions

AccessAnalyzer.Client.exceptions.ResourceNotFoundException
AccessAnalyzer.Client.exceptions.ValidationException
AccessAnalyzer.Client.exceptions.InternalServerException
AccessAnalyzer.Client.exceptions.ThrottlingException
AccessAnalyzer.Client.exceptions.AccessDeniedException


    :return: {}
    
    
    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

def update_archive_rule(analyzerName=None, clientToken=None, filter=None, ruleName=None):
    """
    Updates the criteria and values for the specified archive rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_archive_rule(
        analyzerName='string',
        clientToken='string',
        filter={
            'string': {
                'contains': [
                    'string',
                ],
                'eq': [
                    'string',
                ],
                'exists': True|False,
                'neq': [
                    'string',
                ]
            }
        },
        ruleName='string'
    )
    
    
    :type analyzerName: string
    :param analyzerName: [REQUIRED]\nThe name of the analyzer to update the archive rules for.\n

    :type clientToken: string
    :param clientToken: A client token.\nThis field is autopopulated if not provided.\n

    :type filter: dict
    :param filter: [REQUIRED]\nA filter to match for the rules to update. Only rules that match the filter are updated.\n\n(string) --\n(dict) --The criteria to use in the filter that defines the archive rule.\n\ncontains (list) --A 'contains' operator to match for the filter used to create the rule.\n\n(string) --\n\n\neq (list) --An 'equals' operator to match for the filter used to create the rule.\n\n(string) --\n\n\nexists (boolean) --An 'exists' operator to match for the filter used to create the rule.\n\nneq (list) --A 'not equals' operator to match for the filter used to create the rule.\n\n(string) --\n\n\n\n\n\n\n\n

    :type ruleName: string
    :param ruleName: [REQUIRED]\nThe name of the rule to update.\n

    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

def update_findings(analyzerArn=None, clientToken=None, ids=None, resourceArn=None, status=None):
    """
    Updates the status for the specified findings.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_findings(
        analyzerArn='string',
        clientToken='string',
        ids=[
            'string',
        ],
        resourceArn='string',
        status='ACTIVE'|'ARCHIVED'
    )
    
    
    :type analyzerArn: string
    :param analyzerArn: [REQUIRED]\nThe ARN of the analyzer that generated the findings to update.\n

    :type clientToken: string
    :param clientToken: A client token.\nThis field is autopopulated if not provided.\n

    :type ids: list
    :param ids: The IDs of the findings to update.\n\n(string) --\n\n

    :type resourceArn: string
    :param resourceArn: The ARN of the resource identified in the finding.

    :type status: string
    :param status: [REQUIRED]\nThe state represents the action to take to update the finding Status. Use ARCHIVE to change an Active finding to an Archived finding. Use ACTIVE to change an Archived finding to an Active finding.\n

    :returns: 
    AccessAnalyzer.Client.exceptions.ResourceNotFoundException
    AccessAnalyzer.Client.exceptions.ValidationException
    AccessAnalyzer.Client.exceptions.InternalServerException
    AccessAnalyzer.Client.exceptions.ThrottlingException
    AccessAnalyzer.Client.exceptions.AccessDeniedException
    
    """
    pass

