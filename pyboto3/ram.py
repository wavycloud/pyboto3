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

def accept_resource_share_invitation(resourceShareInvitationArn=None, clientToken=None):
    """
    Accepts an invitation to a resource share from another AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_resource_share_invitation(
        resourceShareInvitationArn='string',
        clientToken='string'
    )
    
    
    :type resourceShareInvitationArn: string
    :param resourceShareInvitationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the invitation.\n

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceShareInvitation': {
        'resourceShareInvitationArn': 'string',
        'resourceShareName': 'string',
        'resourceShareArn': 'string',
        'senderAccountId': 'string',
        'receiverAccountId': 'string',
        'invitationTimestamp': datetime(2015, 1, 1),
        'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
        'resourceShareAssociations': [
            {
                'resourceShareArn': 'string',
                'resourceShareName': 'string',
                'associatedEntity': 'string',
                'associationType': 'PRINCIPAL'|'RESOURCE',
                'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'external': True|False
            },
        ]
    },
    'clientToken': 'string'
}


Response Structure

(dict) --

resourceShareInvitation (dict) --
Information about the invitation.

resourceShareInvitationArn (string) --
The Amazon Resource Name (ARN) of the invitation.

resourceShareName (string) --
The name of the resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

senderAccountId (string) --
The ID of the AWS account that sent the invitation.

receiverAccountId (string) --
The ID of the AWS account that received the invitation.

invitationTimestamp (datetime) --
The date and time when the invitation was sent.

status (string) --
The status of the invitation.

resourceShareAssociations (list) --
To view the resources associated with a pending resource share invitation, use ListPendingInvitationResources .

(dict) --
Describes an association with a resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

resourceShareName (string) --
The name of the resource share.

associatedEntity (string) --
The associated entity. For resource associations, this is the ARN of the resource. For principal associations, this is the ID of an AWS account or the ARN of an OU or organization from AWS Organizations.

associationType (string) --
The association type.

status (string) --
The status of the association.

statusMessage (string) --
A message about the status of the association.

creationTime (datetime) --
The time when the association was created.

lastUpdatedTime (datetime) --
The time when the association was last updated.

external (boolean) --
Indicates whether the principal belongs to the same AWS organization as the AWS account that owns the resource share.







clientToken (string) --
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.







Exceptions

RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.OperationNotPermittedException
RAM.Client.exceptions.ResourceShareInvitationArnNotFoundException
RAM.Client.exceptions.ResourceShareInvitationAlreadyAcceptedException
RAM.Client.exceptions.ResourceShareInvitationAlreadyRejectedException
RAM.Client.exceptions.ResourceShareInvitationExpiredException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.InvalidClientTokenException
RAM.Client.exceptions.IdempotentParameterMismatchException


    :return: {
        'resourceShareInvitation': {
            'resourceShareInvitationArn': 'string',
            'resourceShareName': 'string',
            'resourceShareArn': 'string',
            'senderAccountId': 'string',
            'receiverAccountId': 'string',
            'invitationTimestamp': datetime(2015, 1, 1),
            'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
            'resourceShareAssociations': [
                {
                    'resourceShareArn': 'string',
                    'resourceShareName': 'string',
                    'associatedEntity': 'string',
                    'associationType': 'PRINCIPAL'|'RESOURCE',
                    'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                    'statusMessage': 'string',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'external': True|False
                },
            ]
        },
        'clientToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.OperationNotPermittedException
    RAM.Client.exceptions.ResourceShareInvitationArnNotFoundException
    RAM.Client.exceptions.ResourceShareInvitationAlreadyAcceptedException
    RAM.Client.exceptions.ResourceShareInvitationAlreadyRejectedException
    RAM.Client.exceptions.ResourceShareInvitationExpiredException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.InvalidClientTokenException
    RAM.Client.exceptions.IdempotentParameterMismatchException
    
    """
    pass

def associate_resource_share(resourceShareArn=None, resourceArns=None, principals=None, clientToken=None):
    """
    Associates the specified resource share with the specified principals and resources.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_resource_share(
        resourceShareArn='string',
        resourceArns=[
            'string',
        ],
        principals=[
            'string',
        ],
        clientToken='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource share.\n

    :type resourceArns: list
    :param resourceArns: The Amazon Resource Names (ARN) of the resources.\n\n(string) --\n\n

    :type principals: list
    :param principals: The principals.\n\n(string) --\n\n

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceShareAssociations': [
        {
            'resourceShareArn': 'string',
            'resourceShareName': 'string',
            'associatedEntity': 'string',
            'associationType': 'PRINCIPAL'|'RESOURCE',
            'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
            'statusMessage': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1),
            'external': True|False
        },
    ],
    'clientToken': 'string'
}


Response Structure

(dict) --

resourceShareAssociations (list) --
Information about the associations.

(dict) --
Describes an association with a resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

resourceShareName (string) --
The name of the resource share.

associatedEntity (string) --
The associated entity. For resource associations, this is the ARN of the resource. For principal associations, this is the ID of an AWS account or the ARN of an OU or organization from AWS Organizations.

associationType (string) --
The association type.

status (string) --
The status of the association.

statusMessage (string) --
A message about the status of the association.

creationTime (datetime) --
The time when the association was created.

lastUpdatedTime (datetime) --
The time when the association was last updated.

external (boolean) --
Indicates whether the principal belongs to the same AWS organization as the AWS account that owns the resource share.





clientToken (string) --
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.







Exceptions

RAM.Client.exceptions.IdempotentParameterMismatchException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.InvalidStateTransitionException
RAM.Client.exceptions.ResourceShareLimitExceededException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.InvalidStateTransitionException
RAM.Client.exceptions.InvalidClientTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.OperationNotPermittedException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.UnknownResourceException


    :return: {
        'resourceShareAssociations': [
            {
                'resourceShareArn': 'string',
                'resourceShareName': 'string',
                'associatedEntity': 'string',
                'associationType': 'PRINCIPAL'|'RESOURCE',
                'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'external': True|False
            },
        ],
        'clientToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.IdempotentParameterMismatchException
    RAM.Client.exceptions.UnknownResourceException
    RAM.Client.exceptions.InvalidStateTransitionException
    RAM.Client.exceptions.ResourceShareLimitExceededException
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.InvalidStateTransitionException
    RAM.Client.exceptions.InvalidClientTokenException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.OperationNotPermittedException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.UnknownResourceException
    
    """
    pass

def associate_resource_share_permission(resourceShareArn=None, permissionArn=None, replace=None, clientToken=None):
    """
    Associates a permission with a resource share.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_resource_share_permission(
        resourceShareArn='string',
        permissionArn='string',
        replace=True|False,
        clientToken='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource share.\n

    :type permissionArn: string
    :param permissionArn: [REQUIRED]\nThe ARN of the AWS RAM permission to associate with the resource share.\n

    :type replace: boolean
    :param replace: Indicates whether the permission should replace the permissions that are currently associated with the resource share. Use true to replace the current permissions. Use false to add the permission to the current permission.

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'returnValue': True|False,
    'clientToken': 'string'
}


Response Structure

(dict) --

returnValue (boolean) --
Indicates whether the request succeeded.

clientToken (string) --
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.







Exceptions

RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.InvalidClientTokenException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.OperationNotPermittedException


    :return: {
        'returnValue': True|False,
        'clientToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.UnknownResourceException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.InvalidClientTokenException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.OperationNotPermittedException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_resource_share(name=None, resourceArns=None, principals=None, tags=None, allowExternalPrincipals=None, clientToken=None, permissionArns=None):
    """
    Creates a resource share.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_resource_share(
        name='string',
        resourceArns=[
            'string',
        ],
        principals=[
            'string',
        ],
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        allowExternalPrincipals=True|False,
        clientToken='string',
        permissionArns=[
            'string',
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the resource share.\n

    :type resourceArns: list
    :param resourceArns: The Amazon Resource Names (ARN) of the resources to associate with the resource share.\n\n(string) --\n\n

    :type principals: list
    :param principals: The principals to associate with the resource share. The possible values are IDs of AWS accounts, the ARN of an OU or organization from AWS Organizations.\n\n(string) --\n\n

    :type tags: list
    :param tags: One or more tags.\n\n(dict) --Information about a tag.\n\nkey (string) --The key of the tag.\n\nvalue (string) --The value of the tag.\n\n\n\n\n

    :type allowExternalPrincipals: boolean
    :param allowExternalPrincipals: Indicates whether principals outside your AWS organization can be associated with a resource share.

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :type permissionArns: list
    :param permissionArns: The ARNs of the permissions to associate with the resource share. If you do not specify an ARN for the permission, AWS RAM automatically attaches the default version of the permission for each resource type.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceShare': {
        'resourceShareArn': 'string',
        'name': 'string',
        'owningAccountId': 'string',
        'allowExternalPrincipals': True|False,
        'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
        'statusMessage': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'creationTime': datetime(2015, 1, 1),
        'lastUpdatedTime': datetime(2015, 1, 1),
        'featureSet': 'CREATED_FROM_POLICY'|'PROMOTING_TO_STANDARD'|'STANDARD'
    },
    'clientToken': 'string'
}


Response Structure

(dict) --

resourceShare (dict) --
Information about the resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

name (string) --
The name of the resource share.

owningAccountId (string) --
The ID of the AWS account that owns the resource share.

allowExternalPrincipals (boolean) --
Indicates whether principals outside your AWS organization can be associated with a resource share.

status (string) --
The status of the resource share.

statusMessage (string) --
A message about the status of the resource share.

tags (list) --
The tags for the resource share.

(dict) --
Information about a tag.

key (string) --
The key of the tag.

value (string) --
The value of the tag.





creationTime (datetime) --
The time when the resource share was created.

lastUpdatedTime (datetime) --
The time when the resource share was last updated.

featureSet (string) --
Indicates how the resource share was created. Possible values include:

CREATED_FROM_POLICY - Indicates that the resource share was created from an AWS Identity and Access Management (AWS IAM) policy attached to a resource. These resource shares are visible only to the AWS account that created it. They cannot be modified in AWS RAM.
PROMOTING_TO_STANDARD - The resource share is in the process of being promoted. For more information, see  PromoteResourceShareCreatedFromPolicy .
STANDARD - Indicates that the resource share was created in AWS RAM using the console or APIs. These resource shares are visible to all principals. They can be modified in AWS RAM.




clientToken (string) --
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.







Exceptions

RAM.Client.exceptions.IdempotentParameterMismatchException
RAM.Client.exceptions.InvalidStateTransitionException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.InvalidClientTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.OperationNotPermittedException
RAM.Client.exceptions.ResourceShareLimitExceededException
RAM.Client.exceptions.TagPolicyViolationException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'resourceShare': {
            'resourceShareArn': 'string',
            'name': 'string',
            'owningAccountId': 'string',
            'allowExternalPrincipals': True|False,
            'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
            'statusMessage': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1),
            'featureSet': 'CREATED_FROM_POLICY'|'PROMOTING_TO_STANDARD'|'STANDARD'
        },
        'clientToken': 'string'
    }
    
    
    :returns: 
    CREATED_FROM_POLICY - Indicates that the resource share was created from an AWS Identity and Access Management (AWS IAM) policy attached to a resource. These resource shares are visible only to the AWS account that created it. They cannot be modified in AWS RAM.
    PROMOTING_TO_STANDARD - The resource share is in the process of being promoted. For more information, see  PromoteResourceShareCreatedFromPolicy .
    STANDARD - Indicates that the resource share was created in AWS RAM using the console or APIs. These resource shares are visible to all principals. They can be modified in AWS RAM.
    
    """
    pass

def delete_resource_share(resourceShareArn=None, clientToken=None):
    """
    Deletes the specified resource share.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_resource_share(
        resourceShareArn='string',
        clientToken='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource share.\n

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'returnValue': True|False,
    'clientToken': 'string'
}


Response Structure

(dict) --

returnValue (boolean) --
Indicates whether the request succeeded.

clientToken (string) --
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.







Exceptions

RAM.Client.exceptions.OperationNotPermittedException
RAM.Client.exceptions.IdempotentParameterMismatchException
RAM.Client.exceptions.InvalidStateTransitionException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.InvalidClientTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'returnValue': True|False,
        'clientToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.OperationNotPermittedException
    RAM.Client.exceptions.IdempotentParameterMismatchException
    RAM.Client.exceptions.InvalidStateTransitionException
    RAM.Client.exceptions.UnknownResourceException
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.InvalidClientTokenException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def disassociate_resource_share(resourceShareArn=None, resourceArns=None, principals=None, clientToken=None):
    """
    Disassociates the specified principals or resources from the specified resource share.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_resource_share(
        resourceShareArn='string',
        resourceArns=[
            'string',
        ],
        principals=[
            'string',
        ],
        clientToken='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource share.\n

    :type resourceArns: list
    :param resourceArns: The Amazon Resource Names (ARNs) of the resources.\n\n(string) --\n\n

    :type principals: list
    :param principals: The principals.\n\n(string) --\n\n

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceShareAssociations': [
        {
            'resourceShareArn': 'string',
            'resourceShareName': 'string',
            'associatedEntity': 'string',
            'associationType': 'PRINCIPAL'|'RESOURCE',
            'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
            'statusMessage': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1),
            'external': True|False
        },
    ],
    'clientToken': 'string'
}


Response Structure

(dict) --

resourceShareAssociations (list) --
Information about the associations.

(dict) --
Describes an association with a resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

resourceShareName (string) --
The name of the resource share.

associatedEntity (string) --
The associated entity. For resource associations, this is the ARN of the resource. For principal associations, this is the ID of an AWS account or the ARN of an OU or organization from AWS Organizations.

associationType (string) --
The association type.

status (string) --
The status of the association.

statusMessage (string) --
A message about the status of the association.

creationTime (datetime) --
The time when the association was created.

lastUpdatedTime (datetime) --
The time when the association was last updated.

external (boolean) --
Indicates whether the principal belongs to the same AWS organization as the AWS account that owns the resource share.





clientToken (string) --
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.







Exceptions

RAM.Client.exceptions.IdempotentParameterMismatchException
RAM.Client.exceptions.ResourceShareLimitExceededException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.InvalidStateTransitionException
RAM.Client.exceptions.InvalidClientTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.OperationNotPermittedException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.UnknownResourceException


    :return: {
        'resourceShareAssociations': [
            {
                'resourceShareArn': 'string',
                'resourceShareName': 'string',
                'associatedEntity': 'string',
                'associationType': 'PRINCIPAL'|'RESOURCE',
                'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'external': True|False
            },
        ],
        'clientToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.IdempotentParameterMismatchException
    RAM.Client.exceptions.ResourceShareLimitExceededException
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.InvalidStateTransitionException
    RAM.Client.exceptions.InvalidClientTokenException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.OperationNotPermittedException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.UnknownResourceException
    
    """
    pass

def disassociate_resource_share_permission(resourceShareArn=None, permissionArn=None, clientToken=None):
    """
    Disassociates an AWS RAM permission from a resource share.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_resource_share_permission(
        resourceShareArn='string',
        permissionArn='string',
        clientToken='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource share.\n

    :type permissionArn: string
    :param permissionArn: [REQUIRED]\nThe ARN of the permission to disassociate from the resource share.\n

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'returnValue': True|False,
    'clientToken': 'string'
}


Response Structure

(dict) --

returnValue (boolean) --
Indicates whether the request succeeded.

clientToken (string) --
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.







Exceptions

RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.InvalidClientTokenException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.OperationNotPermittedException


    :return: {
        'returnValue': True|False,
        'clientToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.UnknownResourceException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.InvalidClientTokenException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.OperationNotPermittedException
    
    """
    pass

def enable_sharing_with_aws_organization():
    """
    Enables resource sharing within your AWS Organization.
    The caller must be the master account for the AWS Organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_sharing_with_aws_organization()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'returnValue': True|False
}


Response Structure

(dict) --
returnValue (boolean) --Indicates whether the request succeeded.






Exceptions

RAM.Client.exceptions.OperationNotPermittedException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'returnValue': True|False
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

def get_permission(permissionArn=None, permissionVersion=None):
    """
    Gets the contents of an AWS RAM permission in JSON format.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_permission(
        permissionArn='string',
        permissionVersion=123
    )
    
    
    :type permissionArn: string
    :param permissionArn: [REQUIRED]\nThe ARN of the permission.\n

    :type permissionVersion: integer
    :param permissionVersion: The identifier for the version of the permission.

    :rtype: dict

ReturnsResponse Syntax
{
    'permission': {
        'arn': 'string',
        'version': 'string',
        'defaultVersion': True|False,
        'name': 'string',
        'resourceType': 'string',
        'permission': 'string',
        'creationTime': datetime(2015, 1, 1),
        'lastUpdatedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

permission (dict) --
Information about the permission.

arn (string) --
The ARN of the permission.

version (string) --
The identifier for the version of the permission.

defaultVersion (boolean) --
The identifier for the version of the permission that is set as the default version.

name (string) --
The name of the permission.

resourceType (string) --
The resource type to which the permission applies.

permission (string) --
The permission\'s effect and actions in JSON format. The effect indicates whether the actions are allowed or denied. The actions list the API actions to which the principal is granted or denied access.

creationTime (datetime) --
The date and time when the permission was created.

lastUpdatedTime (datetime) --
The date and time when the permission was last updated.









Exceptions

RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.OperationNotPermittedException


    :return: {
        'permission': {
            'arn': 'string',
            'version': 'string',
            'defaultVersion': True|False,
            'name': 'string',
            'resourceType': 'string',
            'permission': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.UnknownResourceException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.OperationNotPermittedException
    
    """
    pass

def get_resource_policies(resourceArns=None, principal=None, nextToken=None, maxResults=None):
    """
    Gets the policies for the specified resources that you own and have shared.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resource_policies(
        resourceArns=[
            'string',
        ],
        principal='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceArns: list
    :param resourceArns: [REQUIRED]\nThe Amazon Resource Names (ARN) of the resources.\n\n(string) --\n\n

    :type principal: string
    :param principal: The principal.

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'policies': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

policies (list) --
A key policy document, in JSON format.

(string) --


nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.InvalidNextTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.ResourceArnNotFoundException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'policies': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_resource_share_associations(associationType=None, resourceShareArns=None, resourceArn=None, principal=None, associationStatus=None, nextToken=None, maxResults=None):
    """
    Gets the resources or principals for the resource shares that you own.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resource_share_associations(
        associationType='PRINCIPAL'|'RESOURCE',
        resourceShareArns=[
            'string',
        ],
        resourceArn='string',
        principal='string',
        associationStatus='ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
        nextToken='string',
        maxResults=123
    )
    
    
    :type associationType: string
    :param associationType: [REQUIRED]\nThe association type. Specify PRINCIPAL to list the principals that are associated with the specified resource share. Specify RESOURCE to list the resources that are associated with the specified resource share.\n

    :type resourceShareArns: list
    :param resourceShareArns: The Amazon Resource Names (ARN) of the resource shares.\n\n(string) --\n\n

    :type resourceArn: string
    :param resourceArn: The Amazon Resource Name (ARN) of the resource. You cannot specify this parameter if the association type is PRINCIPAL .

    :type principal: string
    :param principal: The principal. You cannot specify this parameter if the association type is RESOURCE .

    :type associationStatus: string
    :param associationStatus: The association status.

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceShareAssociations': [
        {
            'resourceShareArn': 'string',
            'resourceShareName': 'string',
            'associatedEntity': 'string',
            'associationType': 'PRINCIPAL'|'RESOURCE',
            'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
            'statusMessage': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1),
            'external': True|False
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

resourceShareAssociations (list) --
Information about the associations.

(dict) --
Describes an association with a resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

resourceShareName (string) --
The name of the resource share.

associatedEntity (string) --
The associated entity. For resource associations, this is the ARN of the resource. For principal associations, this is the ID of an AWS account or the ARN of an OU or organization from AWS Organizations.

associationType (string) --
The association type.

status (string) --
The status of the association.

statusMessage (string) --
A message about the status of the association.

creationTime (datetime) --
The time when the association was created.

lastUpdatedTime (datetime) --
The time when the association was last updated.

external (boolean) --
Indicates whether the principal belongs to the same AWS organization as the AWS account that owns the resource share.





nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.InvalidNextTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.OperationNotPermittedException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'resourceShareAssociations': [
            {
                'resourceShareArn': 'string',
                'resourceShareName': 'string',
                'associatedEntity': 'string',
                'associationType': 'PRINCIPAL'|'RESOURCE',
                'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'external': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.UnknownResourceException
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.InvalidNextTokenException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.OperationNotPermittedException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def get_resource_share_invitations(resourceShareInvitationArns=None, resourceShareArns=None, nextToken=None, maxResults=None):
    """
    Gets the invitations for resource sharing that you\'ve received.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resource_share_invitations(
        resourceShareInvitationArns=[
            'string',
        ],
        resourceShareArns=[
            'string',
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceShareInvitationArns: list
    :param resourceShareInvitationArns: The Amazon Resource Names (ARN) of the invitations.\n\n(string) --\n\n

    :type resourceShareArns: list
    :param resourceShareArns: The Amazon Resource Names (ARN) of the resource shares.\n\n(string) --\n\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceShareInvitations': [
        {
            'resourceShareInvitationArn': 'string',
            'resourceShareName': 'string',
            'resourceShareArn': 'string',
            'senderAccountId': 'string',
            'receiverAccountId': 'string',
            'invitationTimestamp': datetime(2015, 1, 1),
            'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
            'resourceShareAssociations': [
                {
                    'resourceShareArn': 'string',
                    'resourceShareName': 'string',
                    'associatedEntity': 'string',
                    'associationType': 'PRINCIPAL'|'RESOURCE',
                    'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                    'statusMessage': 'string',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'external': True|False
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

resourceShareInvitations (list) --
Information about the invitations.

(dict) --
Describes an invitation to join a resource share.

resourceShareInvitationArn (string) --
The Amazon Resource Name (ARN) of the invitation.

resourceShareName (string) --
The name of the resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

senderAccountId (string) --
The ID of the AWS account that sent the invitation.

receiverAccountId (string) --
The ID of the AWS account that received the invitation.

invitationTimestamp (datetime) --
The date and time when the invitation was sent.

status (string) --
The status of the invitation.

resourceShareAssociations (list) --
To view the resources associated with a pending resource share invitation, use ListPendingInvitationResources .

(dict) --
Describes an association with a resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

resourceShareName (string) --
The name of the resource share.

associatedEntity (string) --
The associated entity. For resource associations, this is the ARN of the resource. For principal associations, this is the ID of an AWS account or the ARN of an OU or organization from AWS Organizations.

associationType (string) --
The association type.

status (string) --
The status of the association.

statusMessage (string) --
A message about the status of the association.

creationTime (datetime) --
The time when the association was created.

lastUpdatedTime (datetime) --
The time when the association was last updated.

external (boolean) --
Indicates whether the principal belongs to the same AWS organization as the AWS account that owns the resource share.









nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RAM.Client.exceptions.ResourceShareInvitationArnNotFoundException
RAM.Client.exceptions.InvalidMaxResultsException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.InvalidNextTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'resourceShareInvitations': [
            {
                'resourceShareInvitationArn': 'string',
                'resourceShareName': 'string',
                'resourceShareArn': 'string',
                'senderAccountId': 'string',
                'receiverAccountId': 'string',
                'invitationTimestamp': datetime(2015, 1, 1),
                'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
                'resourceShareAssociations': [
                    {
                        'resourceShareArn': 'string',
                        'resourceShareName': 'string',
                        'associatedEntity': 'string',
                        'associationType': 'PRINCIPAL'|'RESOURCE',
                        'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'external': True|False
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.ResourceShareInvitationArnNotFoundException
    RAM.Client.exceptions.InvalidMaxResultsException
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.UnknownResourceException
    RAM.Client.exceptions.InvalidNextTokenException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def get_resource_shares(resourceShareArns=None, resourceShareStatus=None, resourceOwner=None, name=None, tagFilters=None, nextToken=None, maxResults=None):
    """
    Gets the resource shares that you own or the resource shares that are shared with you.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resource_shares(
        resourceShareArns=[
            'string',
        ],
        resourceShareStatus='PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
        resourceOwner='SELF'|'OTHER-ACCOUNTS',
        name='string',
        tagFilters=[
            {
                'tagKey': 'string',
                'tagValues': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceShareArns: list
    :param resourceShareArns: The Amazon Resource Names (ARN) of the resource shares.\n\n(string) --\n\n

    :type resourceShareStatus: string
    :param resourceShareStatus: The status of the resource share.

    :type resourceOwner: string
    :param resourceOwner: [REQUIRED]\nThe type of owner.\n

    :type name: string
    :param name: The name of the resource share.

    :type tagFilters: list
    :param tagFilters: One or more tag filters.\n\n(dict) --Used to filter information based on tags.\n\ntagKey (string) --The tag key.\n\ntagValues (list) --The tag values.\n\n(string) --\n\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceShares': [
        {
            'resourceShareArn': 'string',
            'name': 'string',
            'owningAccountId': 'string',
            'allowExternalPrincipals': True|False,
            'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
            'statusMessage': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1),
            'featureSet': 'CREATED_FROM_POLICY'|'PROMOTING_TO_STANDARD'|'STANDARD'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

resourceShares (list) --
Information about the resource shares.

(dict) --
Describes a resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

name (string) --
The name of the resource share.

owningAccountId (string) --
The ID of the AWS account that owns the resource share.

allowExternalPrincipals (boolean) --
Indicates whether principals outside your AWS organization can be associated with a resource share.

status (string) --
The status of the resource share.

statusMessage (string) --
A message about the status of the resource share.

tags (list) --
The tags for the resource share.

(dict) --
Information about a tag.

key (string) --
The key of the tag.

value (string) --
The value of the tag.





creationTime (datetime) --
The time when the resource share was created.

lastUpdatedTime (datetime) --
The time when the resource share was last updated.

featureSet (string) --
Indicates how the resource share was created. Possible values include:

CREATED_FROM_POLICY - Indicates that the resource share was created from an AWS Identity and Access Management (AWS IAM) policy attached to a resource. These resource shares are visible only to the AWS account that created it. They cannot be modified in AWS RAM.
PROMOTING_TO_STANDARD - The resource share is in the process of being promoted. For more information, see  PromoteResourceShareCreatedFromPolicy .
STANDARD - Indicates that the resource share was created in AWS RAM using the console or APIs. These resource shares are visible to all principals. They can be modified in AWS RAM.






nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.InvalidNextTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'resourceShares': [
            {
                'resourceShareArn': 'string',
                'name': 'string',
                'owningAccountId': 'string',
                'allowExternalPrincipals': True|False,
                'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                'statusMessage': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'featureSet': 'CREATED_FROM_POLICY'|'PROMOTING_TO_STANDARD'|'STANDARD'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CREATED_FROM_POLICY - Indicates that the resource share was created from an AWS Identity and Access Management (AWS IAM) policy attached to a resource. These resource shares are visible only to the AWS account that created it. They cannot be modified in AWS RAM.
    PROMOTING_TO_STANDARD - The resource share is in the process of being promoted. For more information, see  PromoteResourceShareCreatedFromPolicy .
    STANDARD - Indicates that the resource share was created in AWS RAM using the console or APIs. These resource shares are visible to all principals. They can be modified in AWS RAM.
    
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

def list_pending_invitation_resources(resourceShareInvitationArn=None, nextToken=None, maxResults=None):
    """
    Lists the resources in a resource share that is shared with you but that the invitation is still pending for.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_pending_invitation_resources(
        resourceShareInvitationArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceShareInvitationArn: string
    :param resourceShareInvitationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the invitation.\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'resources': [
        {
            'arn': 'string',
            'type': 'string',
            'resourceShareArn': 'string',
            'resourceGroupArn': 'string',
            'status': 'AVAILABLE'|'ZONAL_RESOURCE_INACCESSIBLE'|'LIMIT_EXCEEDED'|'UNAVAILABLE'|'PENDING',
            'statusMessage': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

resources (list) --
Information about the resources included the resource share.

(dict) --
Describes a resource associated with a resource share.

arn (string) --
The Amazon Resource Name (ARN) of the resource.

type (string) --
The resource type.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

resourceGroupArn (string) --
The ARN of the resource group. This value is returned only if the resource is a resource group.

status (string) --
The status of the resource.

statusMessage (string) --
A message about the status of the resource.

creationTime (datetime) --
The time when the resource was associated with the resource share.

lastUpdatedTime (datetime) --
The time when the association was last updated.





nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.InvalidNextTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.ResourceShareInvitationArnNotFoundException
RAM.Client.exceptions.MissingRequiredParameterException
RAM.Client.exceptions.ResourceShareInvitationAlreadyRejectedException
RAM.Client.exceptions.ResourceShareInvitationExpiredException


    :return: {
        'resources': [
            {
                'arn': 'string',
                'type': 'string',
                'resourceShareArn': 'string',
                'resourceGroupArn': 'string',
                'status': 'AVAILABLE'|'ZONAL_RESOURCE_INACCESSIBLE'|'LIMIT_EXCEEDED'|'UNAVAILABLE'|'PENDING',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.InvalidNextTokenException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.ResourceShareInvitationArnNotFoundException
    RAM.Client.exceptions.MissingRequiredParameterException
    RAM.Client.exceptions.ResourceShareInvitationAlreadyRejectedException
    RAM.Client.exceptions.ResourceShareInvitationExpiredException
    
    """
    pass

def list_permissions(resourceType=None, nextToken=None, maxResults=None):
    """
    Lists the AWS RAM permissions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_permissions(
        resourceType='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceType: string
    :param resourceType: Specifies the resource type for which to list permissions. For example, to list only permissions that apply to EC2 subnets, specify ec2:Subnet .

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'permissions': [
        {
            'arn': 'string',
            'version': 'string',
            'defaultVersion': True|False,
            'name': 'string',
            'resourceType': 'string',
            'status': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

permissions (list) --
Information about the permissions.

(dict) --
Information about a permission that is associated with a resource share.

arn (string) --
The ARN of the permission.

version (string) --
The identifier for the version of the permission.

defaultVersion (boolean) --
The identifier for the version of the permission that is set as the default version.

name (string) --
The name of the permission.

resourceType (string) --
The type of resource to which the permission applies.

status (string) --
The current status of the permission.

creationTime (datetime) --
The date and time when the permission was created.

lastUpdatedTime (datetime) --
The date and time when the permission was last updated.





nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.InvalidNextTokenException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.OperationNotPermittedException


    :return: {
        'permissions': [
            {
                'arn': 'string',
                'version': 'string',
                'defaultVersion': True|False,
                'name': 'string',
                'resourceType': 'string',
                'status': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.InvalidNextTokenException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.OperationNotPermittedException
    
    """
    pass

def list_principals(resourceOwner=None, resourceArn=None, principals=None, resourceType=None, resourceShareArns=None, nextToken=None, maxResults=None):
    """
    Lists the principals that you have shared resources with or that have shared resources with you.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_principals(
        resourceOwner='SELF'|'OTHER-ACCOUNTS',
        resourceArn='string',
        principals=[
            'string',
        ],
        resourceType='string',
        resourceShareArns=[
            'string',
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceOwner: string
    :param resourceOwner: [REQUIRED]\nThe type of owner.\n

    :type resourceArn: string
    :param resourceArn: The Amazon Resource Name (ARN) of the resource.

    :type principals: list
    :param principals: The principals.\n\n(string) --\n\n

    :type resourceType: string
    :param resourceType: The resource type.\nValid values: codebuild:Project | codebuild:ReportGroup | ec2:CapacityReservation | ec2:DedicatedHost | ec2:Subnet | ec2:TrafficMirrorTarget | ec2:TransitGateway | imagebuilder:Component | imagebuilder:Image | imagebuilder:ImageRecipe | license-manager:LicenseConfiguration I resource-groups:Group | rds:Cluster | route53resolver:ResolverRule\n

    :type resourceShareArns: list
    :param resourceShareArns: The Amazon Resource Names (ARN) of the resource shares.\n\n(string) --\n\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'principals': [
        {
            'id': 'string',
            'resourceShareArn': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1),
            'external': True|False
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

principals (list) --
The principals.

(dict) --
Describes a principal for use with AWS Resource Access Manager.

id (string) --
The ID of the principal.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

creationTime (datetime) --
The time when the principal was associated with the resource share.

lastUpdatedTime (datetime) --
The time when the association was last updated.

external (boolean) --
Indicates whether the principal belongs to the same AWS organization as the AWS account that owns the resource share.





nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.InvalidNextTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'principals': [
            {
                'id': 'string',
                'resourceShareArn': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'external': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.UnknownResourceException
    RAM.Client.exceptions.InvalidNextTokenException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_resource_share_permissions(resourceShareArn=None, nextToken=None, maxResults=None):
    """
    Lists the AWS RAM permissions that are associated with a resource share.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resource_share_permissions(
        resourceShareArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource share.\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'permissions': [
        {
            'arn': 'string',
            'version': 'string',
            'defaultVersion': True|False,
            'name': 'string',
            'resourceType': 'string',
            'status': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

permissions (list) --
The permissions associated with the resource share.

(dict) --
Information about a permission that is associated with a resource share.

arn (string) --
The ARN of the permission.

version (string) --
The identifier for the version of the permission.

defaultVersion (boolean) --
The identifier for the version of the permission that is set as the default version.

name (string) --
The name of the permission.

resourceType (string) --
The type of resource to which the permission applies.

status (string) --
The current status of the permission.

creationTime (datetime) --
The date and time when the permission was created.

lastUpdatedTime (datetime) --
The date and time when the permission was last updated.





nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.InvalidNextTokenException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.OperationNotPermittedException


    :return: {
        'permissions': [
            {
                'arn': 'string',
                'version': 'string',
                'defaultVersion': True|False,
                'name': 'string',
                'resourceType': 'string',
                'status': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.UnknownResourceException
    RAM.Client.exceptions.InvalidNextTokenException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.OperationNotPermittedException
    
    """
    pass

def list_resource_types(nextToken=None, maxResults=None):
    """
    Lists the shareable resource types supported by AWS RAM.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resource_types(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceTypes': [
        {
            'resourceType': 'string',
            'serviceName': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

resourceTypes (list) --
The shareable resource types supported by AWS RAM.

(dict) --
Information about the shareable resource types and the AWS services to which they belong.

resourceType (string) --
The shareable resource types.

serviceName (string) --
The name of the AWS services to which the resources belong.





nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RAM.Client.exceptions.InvalidNextTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'resourceTypes': [
            {
                'resourceType': 'string',
                'serviceName': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.InvalidNextTokenException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_resources(resourceOwner=None, principal=None, resourceType=None, resourceArns=None, resourceShareArns=None, nextToken=None, maxResults=None):
    """
    Lists the resources that you added to a resource shares or the resources that are shared with you.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_resources(
        resourceOwner='SELF'|'OTHER-ACCOUNTS',
        principal='string',
        resourceType='string',
        resourceArns=[
            'string',
        ],
        resourceShareArns=[
            'string',
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type resourceOwner: string
    :param resourceOwner: [REQUIRED]\nThe type of owner.\n

    :type principal: string
    :param principal: The principal.

    :type resourceType: string
    :param resourceType: The resource type.\nValid values: codebuild:Project | codebuild:ReportGroup | ec2:CapacityReservation | ec2:DedicatedHost | ec2:Subnet | ec2:TrafficMirrorTarget | ec2:TransitGateway | imagebuilder:Component | imagebuilder:Image | imagebuilder:ImageRecipe | license-manager:LicenseConfiguration I resource-groups:Group | rds:Cluster | route53resolver:ResolverRule\n

    :type resourceArns: list
    :param resourceArns: The Amazon Resource Names (ARN) of the resources.\n\n(string) --\n\n

    :type resourceShareArns: list
    :param resourceShareArns: The Amazon Resource Names (ARN) of the resource shares.\n\n(string) --\n\n

    :type nextToken: string
    :param nextToken: The token for the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'resources': [
        {
            'arn': 'string',
            'type': 'string',
            'resourceShareArn': 'string',
            'resourceGroupArn': 'string',
            'status': 'AVAILABLE'|'ZONAL_RESOURCE_INACCESSIBLE'|'LIMIT_EXCEEDED'|'UNAVAILABLE'|'PENDING',
            'statusMessage': 'string',
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

resources (list) --
Information about the resources.

(dict) --
Describes a resource associated with a resource share.

arn (string) --
The Amazon Resource Name (ARN) of the resource.

type (string) --
The resource type.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

resourceGroupArn (string) --
The ARN of the resource group. This value is returned only if the resource is a resource group.

status (string) --
The status of the resource.

statusMessage (string) --
A message about the status of the resource.

creationTime (datetime) --
The time when the resource was associated with the resource share.

lastUpdatedTime (datetime) --
The time when the association was last updated.





nextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

RAM.Client.exceptions.InvalidResourceTypeException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.InvalidNextTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'resources': [
            {
                'arn': 'string',
                'type': 'string',
                'resourceShareArn': 'string',
                'resourceGroupArn': 'string',
                'status': 'AVAILABLE'|'ZONAL_RESOURCE_INACCESSIBLE'|'LIMIT_EXCEEDED'|'UNAVAILABLE'|'PENDING',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.InvalidResourceTypeException
    RAM.Client.exceptions.UnknownResourceException
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.InvalidNextTokenException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def promote_resource_share_created_from_policy(resourceShareArn=None):
    """
    Resource shares that were created by attaching a policy to a resource are visible only to the resource share owner, and the resource share cannot be modified in AWS RAM.
    Use this API action to promote the resource share. When you promote the resource share, it becomes:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.promote_resource_share_created_from_policy(
        resourceShareArn='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]\nThe ARN of the resource share to promote.\n

    :rtype: dict
ReturnsResponse Syntax{
    'returnValue': True|False
}


Response Structure

(dict) --
returnValue (boolean) --Indicates whether the request succeeded.






Exceptions

RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.OperationNotPermittedException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.MissingRequiredParameterException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.UnknownResourceException


    :return: {
        'returnValue': True|False
    }
    
    
    :returns: 
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.OperationNotPermittedException
    RAM.Client.exceptions.InvalidParameterException
    RAM.Client.exceptions.MissingRequiredParameterException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.UnknownResourceException
    
    """
    pass

def reject_resource_share_invitation(resourceShareInvitationArn=None, clientToken=None):
    """
    Rejects an invitation to a resource share from another AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reject_resource_share_invitation(
        resourceShareInvitationArn='string',
        clientToken='string'
    )
    
    
    :type resourceShareInvitationArn: string
    :param resourceShareInvitationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the invitation.\n

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceShareInvitation': {
        'resourceShareInvitationArn': 'string',
        'resourceShareName': 'string',
        'resourceShareArn': 'string',
        'senderAccountId': 'string',
        'receiverAccountId': 'string',
        'invitationTimestamp': datetime(2015, 1, 1),
        'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
        'resourceShareAssociations': [
            {
                'resourceShareArn': 'string',
                'resourceShareName': 'string',
                'associatedEntity': 'string',
                'associationType': 'PRINCIPAL'|'RESOURCE',
                'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                'statusMessage': 'string',
                'creationTime': datetime(2015, 1, 1),
                'lastUpdatedTime': datetime(2015, 1, 1),
                'external': True|False
            },
        ]
    },
    'clientToken': 'string'
}


Response Structure

(dict) --

resourceShareInvitation (dict) --
Information about the invitation.

resourceShareInvitationArn (string) --
The Amazon Resource Name (ARN) of the invitation.

resourceShareName (string) --
The name of the resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

senderAccountId (string) --
The ID of the AWS account that sent the invitation.

receiverAccountId (string) --
The ID of the AWS account that received the invitation.

invitationTimestamp (datetime) --
The date and time when the invitation was sent.

status (string) --
The status of the invitation.

resourceShareAssociations (list) --
To view the resources associated with a pending resource share invitation, use ListPendingInvitationResources .

(dict) --
Describes an association with a resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

resourceShareName (string) --
The name of the resource share.

associatedEntity (string) --
The associated entity. For resource associations, this is the ARN of the resource. For principal associations, this is the ID of an AWS account or the ARN of an OU or organization from AWS Organizations.

associationType (string) --
The association type.

status (string) --
The status of the association.

statusMessage (string) --
A message about the status of the association.

creationTime (datetime) --
The time when the association was created.

lastUpdatedTime (datetime) --
The time when the association was last updated.

external (boolean) --
Indicates whether the principal belongs to the same AWS organization as the AWS account that owns the resource share.







clientToken (string) --
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.







Exceptions

RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.OperationNotPermittedException
RAM.Client.exceptions.ResourceShareInvitationArnNotFoundException
RAM.Client.exceptions.ResourceShareInvitationAlreadyAcceptedException
RAM.Client.exceptions.ResourceShareInvitationAlreadyRejectedException
RAM.Client.exceptions.ResourceShareInvitationExpiredException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException
RAM.Client.exceptions.InvalidClientTokenException
RAM.Client.exceptions.IdempotentParameterMismatchException


    :return: {
        'resourceShareInvitation': {
            'resourceShareInvitationArn': 'string',
            'resourceShareName': 'string',
            'resourceShareArn': 'string',
            'senderAccountId': 'string',
            'receiverAccountId': 'string',
            'invitationTimestamp': datetime(2015, 1, 1),
            'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
            'resourceShareAssociations': [
                {
                    'resourceShareArn': 'string',
                    'resourceShareName': 'string',
                    'associatedEntity': 'string',
                    'associationType': 'PRINCIPAL'|'RESOURCE',
                    'status': 'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
                    'statusMessage': 'string',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'external': True|False
                },
            ]
        },
        'clientToken': 'string'
    }
    
    
    :returns: 
    RAM.Client.exceptions.MalformedArnException
    RAM.Client.exceptions.OperationNotPermittedException
    RAM.Client.exceptions.ResourceShareInvitationArnNotFoundException
    RAM.Client.exceptions.ResourceShareInvitationAlreadyAcceptedException
    RAM.Client.exceptions.ResourceShareInvitationAlreadyRejectedException
    RAM.Client.exceptions.ResourceShareInvitationExpiredException
    RAM.Client.exceptions.ServerInternalException
    RAM.Client.exceptions.ServiceUnavailableException
    RAM.Client.exceptions.InvalidClientTokenException
    RAM.Client.exceptions.IdempotentParameterMismatchException
    
    """
    pass

def tag_resource(resourceShareArn=None, tags=None):
    """
    Adds the specified tags to the specified resource share that you own.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceShareArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource share.\n

    :type tags: list
    :param tags: [REQUIRED]\nOne or more tags.\n\n(dict) --Information about a tag.\n\nkey (string) --The key of the tag.\n\nvalue (string) --The value of the tag.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.TagLimitExceededException
RAM.Client.exceptions.ResourceArnNotFoundException
RAM.Client.exceptions.TagPolicyViolationException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceShareArn=None, tagKeys=None):
    """
    Removes the specified tags from the specified resource share that you own.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceShareArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource share.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe tag keys of the tags to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_resource_share(resourceShareArn=None, name=None, allowExternalPrincipals=None, clientToken=None):
    """
    Updates the specified resource share that you own.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_resource_share(
        resourceShareArn='string',
        name='string',
        allowExternalPrincipals=True|False,
        clientToken='string'
    )
    
    
    :type resourceShareArn: string
    :param resourceShareArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource share.\n

    :type name: string
    :param name: The name of the resource share.

    :type allowExternalPrincipals: boolean
    :param allowExternalPrincipals: Indicates whether principals outside your AWS organization can be associated with a resource share.

    :type clientToken: string
    :param clientToken: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceShare': {
        'resourceShareArn': 'string',
        'name': 'string',
        'owningAccountId': 'string',
        'allowExternalPrincipals': True|False,
        'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
        'statusMessage': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'creationTime': datetime(2015, 1, 1),
        'lastUpdatedTime': datetime(2015, 1, 1),
        'featureSet': 'CREATED_FROM_POLICY'|'PROMOTING_TO_STANDARD'|'STANDARD'
    },
    'clientToken': 'string'
}


Response Structure

(dict) --

resourceShare (dict) --
Information about the resource share.

resourceShareArn (string) --
The Amazon Resource Name (ARN) of the resource share.

name (string) --
The name of the resource share.

owningAccountId (string) --
The ID of the AWS account that owns the resource share.

allowExternalPrincipals (boolean) --
Indicates whether principals outside your AWS organization can be associated with a resource share.

status (string) --
The status of the resource share.

statusMessage (string) --
A message about the status of the resource share.

tags (list) --
The tags for the resource share.

(dict) --
Information about a tag.

key (string) --
The key of the tag.

value (string) --
The value of the tag.





creationTime (datetime) --
The time when the resource share was created.

lastUpdatedTime (datetime) --
The time when the resource share was last updated.

featureSet (string) --
Indicates how the resource share was created. Possible values include:

CREATED_FROM_POLICY - Indicates that the resource share was created from an AWS Identity and Access Management (AWS IAM) policy attached to a resource. These resource shares are visible only to the AWS account that created it. They cannot be modified in AWS RAM.
PROMOTING_TO_STANDARD - The resource share is in the process of being promoted. For more information, see  PromoteResourceShareCreatedFromPolicy .
STANDARD - Indicates that the resource share was created in AWS RAM using the console or APIs. These resource shares are visible to all principals. They can be modified in AWS RAM.




clientToken (string) --
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.







Exceptions

RAM.Client.exceptions.IdempotentParameterMismatchException
RAM.Client.exceptions.MissingRequiredParameterException
RAM.Client.exceptions.UnknownResourceException
RAM.Client.exceptions.MalformedArnException
RAM.Client.exceptions.InvalidClientTokenException
RAM.Client.exceptions.InvalidParameterException
RAM.Client.exceptions.OperationNotPermittedException
RAM.Client.exceptions.ServerInternalException
RAM.Client.exceptions.ServiceUnavailableException


    :return: {
        'resourceShare': {
            'resourceShareArn': 'string',
            'name': 'string',
            'owningAccountId': 'string',
            'allowExternalPrincipals': True|False,
            'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
            'statusMessage': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'creationTime': datetime(2015, 1, 1),
            'lastUpdatedTime': datetime(2015, 1, 1),
            'featureSet': 'CREATED_FROM_POLICY'|'PROMOTING_TO_STANDARD'|'STANDARD'
        },
        'clientToken': 'string'
    }
    
    
    :returns: 
    CREATED_FROM_POLICY - Indicates that the resource share was created from an AWS Identity and Access Management (AWS IAM) policy attached to a resource. These resource shares are visible only to the AWS account that created it. They cannot be modified in AWS RAM.
    PROMOTING_TO_STANDARD - The resource share is in the process of being promoted. For more information, see  PromoteResourceShareCreatedFromPolicy .
    STANDARD - Indicates that the resource share was created in AWS RAM using the console or APIs. These resource shares are visible to all principals. They can be modified in AWS RAM.
    
    """
    pass

