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

def abort_document_version_upload(AuthenticationToken=None, DocumentId=None, VersionId=None):
    """
    Aborts the upload of the specified document version that was previously initiated by  InitiateDocumentVersionUpload . The client should make this call only when it no longer intends to upload the document version, or fails to do so.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.abort_document_version_upload(
        AuthenticationToken='string',
        DocumentId='string',
        VersionId='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :type VersionId: string
    :param VersionId: [REQUIRED]\nThe ID of the version.\n

    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.ProhibitedStateException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def activate_user(UserId=None, AuthenticationToken=None):
    """
    Activates the specified user. Only active users can access Amazon WorkDocs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.activate_user(
        UserId='string',
        AuthenticationToken='string'
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]\nThe ID of the user.\n

    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'Id': 'string',
        'Username': 'string',
        'EmailAddress': 'string',
        'GivenName': 'string',
        'Surname': 'string',
        'OrganizationId': 'string',
        'RootFolderId': 'string',
        'RecycleBinFolderId': 'string',
        'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
        'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'ModifiedTimestamp': datetime(2015, 1, 1),
        'TimeZoneId': 'string',
        'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
        'Storage': {
            'StorageUtilizedInBytes': 123,
            'StorageRule': {
                'StorageAllocatedInBytes': 123,
                'StorageType': 'UNLIMITED'|'QUOTA'
            }
        }
    }
}


Response Structure

(dict) --

User (dict) --
The user information.

Id (string) --
The ID of the user.

Username (string) --
The login name of the user.

EmailAddress (string) --
The email address of the user.

GivenName (string) --
The given name of the user.

Surname (string) --
The surname of the user.

OrganizationId (string) --
The ID of the organization.

RootFolderId (string) --
The ID of the root folder.

RecycleBinFolderId (string) --
The ID of the recycle bin folder.

Status (string) --
The status of the user.

Type (string) --
The type of user.

CreatedTimestamp (datetime) --
The time when the user was created.

ModifiedTimestamp (datetime) --
The time when the user was modified.

TimeZoneId (string) --
The time zone ID of the user.

Locale (string) --
The locale of the user.

Storage (dict) --
The storage for the user.

StorageUtilizedInBytes (integer) --
The amount of storage used, in bytes.

StorageRule (dict) --
The storage for a user.

StorageAllocatedInBytes (integer) --
The amount of storage allocated, in bytes.

StorageType (string) --
The type of storage.













Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'User': {
            'Id': 'string',
            'Username': 'string',
            'EmailAddress': 'string',
            'GivenName': 'string',
            'Surname': 'string',
            'OrganizationId': 'string',
            'RootFolderId': 'string',
            'RecycleBinFolderId': 'string',
            'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
            'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'TimeZoneId': 'string',
            'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
            'Storage': {
                'StorageUtilizedInBytes': 123,
                'StorageRule': {
                    'StorageAllocatedInBytes': 123,
                    'StorageType': 'UNLIMITED'|'QUOTA'
                }
            }
        }
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def add_resource_permissions(AuthenticationToken=None, ResourceId=None, Principals=None, NotificationOptions=None):
    """
    Creates a set of permissions for the specified folder or document. The resource permissions are overwritten if the principals already have different permissions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_resource_permissions(
        AuthenticationToken='string',
        ResourceId='string',
        Principals=[
            {
                'Id': 'string',
                'Type': 'USER'|'GROUP'|'INVITE'|'ANONYMOUS'|'ORGANIZATION',
                'Role': 'VIEWER'|'CONTRIBUTOR'|'OWNER'|'COOWNER'
            },
        ],
        NotificationOptions={
            'SendEmail': True|False,
            'EmailMessage': 'string'
        }
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource.\n

    :type Principals: list
    :param Principals: [REQUIRED]\nThe users, groups, or organization being granted permission.\n\n(dict) --Describes the recipient type and ID, if available.\n\nId (string) -- [REQUIRED]The ID of the recipient.\n\nType (string) -- [REQUIRED]The type of the recipient.\n\nRole (string) -- [REQUIRED]The role of the recipient.\n\n\n\n\n

    :type NotificationOptions: dict
    :param NotificationOptions: The notification options.\n\nSendEmail (boolean) --Boolean value to indicate an email notification should be sent to the receipients.\n\nEmailMessage (string) --Text value to be included in the email body.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ShareResults': [
        {
            'PrincipalId': 'string',
            'InviteePrincipalId': 'string',
            'Role': 'VIEWER'|'CONTRIBUTOR'|'OWNER'|'COOWNER',
            'Status': 'SUCCESS'|'FAILURE',
            'ShareId': 'string',
            'StatusMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

ShareResults (list) --
The share results.

(dict) --
Describes the share results of a resource.

PrincipalId (string) --
The ID of the principal.

InviteePrincipalId (string) --
The ID of the invited user.

Role (string) --
The role.

Status (string) --
The status.

ShareId (string) --
The ID of the resource that was shared.

StatusMessage (string) --
The status message.











Exceptions

WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'ShareResults': [
            {
                'PrincipalId': 'string',
                'InviteePrincipalId': 'string',
                'Role': 'VIEWER'|'CONTRIBUTOR'|'OWNER'|'COOWNER',
                'Status': 'SUCCESS'|'FAILURE',
                'ShareId': 'string',
                'StatusMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_comment(AuthenticationToken=None, DocumentId=None, VersionId=None, ParentId=None, ThreadId=None, Text=None, Visibility=None, NotifyCollaborators=None):
    """
    Adds a new comment to the specified document version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_comment(
        AuthenticationToken='string',
        DocumentId='string',
        VersionId='string',
        ParentId='string',
        ThreadId='string',
        Text='string',
        Visibility='PUBLIC'|'PRIVATE',
        NotifyCollaborators=True|False
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :type VersionId: string
    :param VersionId: [REQUIRED]\nThe ID of the document version.\n

    :type ParentId: string
    :param ParentId: The ID of the parent comment.

    :type ThreadId: string
    :param ThreadId: The ID of the root comment in the thread.

    :type Text: string
    :param Text: [REQUIRED]\nThe text of the comment.\n

    :type Visibility: string
    :param Visibility: The visibility of the comment. Options are either PRIVATE, where the comment is visible only to the comment author and document owner and co-owners, or PUBLIC, where the comment is visible to document owners, co-owners, and contributors.

    :type NotifyCollaborators: boolean
    :param NotifyCollaborators: Set this parameter to TRUE to send an email out to the document collaborators after the comment is created.

    :rtype: dict

ReturnsResponse Syntax
{
    'Comment': {
        'CommentId': 'string',
        'ParentId': 'string',
        'ThreadId': 'string',
        'Text': 'string',
        'Contributor': {
            'Id': 'string',
            'Username': 'string',
            'EmailAddress': 'string',
            'GivenName': 'string',
            'Surname': 'string',
            'OrganizationId': 'string',
            'RootFolderId': 'string',
            'RecycleBinFolderId': 'string',
            'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
            'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'TimeZoneId': 'string',
            'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
            'Storage': {
                'StorageUtilizedInBytes': 123,
                'StorageRule': {
                    'StorageAllocatedInBytes': 123,
                    'StorageType': 'UNLIMITED'|'QUOTA'
                }
            }
        },
        'CreatedTimestamp': datetime(2015, 1, 1),
        'Status': 'DRAFT'|'PUBLISHED'|'DELETED',
        'Visibility': 'PUBLIC'|'PRIVATE',
        'RecipientId': 'string'
    }
}


Response Structure

(dict) --

Comment (dict) --
The comment that has been created.

CommentId (string) --
The ID of the comment.

ParentId (string) --
The ID of the parent comment.

ThreadId (string) --
The ID of the root comment in the thread.

Text (string) --
The text of the comment.

Contributor (dict) --
The details of the user who made the comment.

Id (string) --
The ID of the user.

Username (string) --
The login name of the user.

EmailAddress (string) --
The email address of the user.

GivenName (string) --
The given name of the user.

Surname (string) --
The surname of the user.

OrganizationId (string) --
The ID of the organization.

RootFolderId (string) --
The ID of the root folder.

RecycleBinFolderId (string) --
The ID of the recycle bin folder.

Status (string) --
The status of the user.

Type (string) --
The type of user.

CreatedTimestamp (datetime) --
The time when the user was created.

ModifiedTimestamp (datetime) --
The time when the user was modified.

TimeZoneId (string) --
The time zone ID of the user.

Locale (string) --
The locale of the user.

Storage (dict) --
The storage for the user.

StorageUtilizedInBytes (integer) --
The amount of storage used, in bytes.

StorageRule (dict) --
The storage for a user.

StorageAllocatedInBytes (integer) --
The amount of storage allocated, in bytes.

StorageType (string) --
The type of storage.







CreatedTimestamp (datetime) --
The time that the comment was created.

Status (string) --
The status of the comment.

Visibility (string) --
The visibility of the comment. Options are either PRIVATE, where the comment is visible only to the comment author and document owner and co-owners, or PUBLIC, where the comment is visible to document owners, co-owners, and contributors.

RecipientId (string) --
If the comment is a reply to another user\'s comment, this field contains the user ID of the user being replied to.









Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.ProhibitedStateException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException
WorkDocs.Client.exceptions.DocumentLockedForCommentsException
WorkDocs.Client.exceptions.InvalidCommentOperationException


    :return: {
        'Comment': {
            'CommentId': 'string',
            'ParentId': 'string',
            'ThreadId': 'string',
            'Text': 'string',
            'Contributor': {
                'Id': 'string',
                'Username': 'string',
                'EmailAddress': 'string',
                'GivenName': 'string',
                'Surname': 'string',
                'OrganizationId': 'string',
                'RootFolderId': 'string',
                'RecycleBinFolderId': 'string',
                'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
                'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'TimeZoneId': 'string',
                'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
                'Storage': {
                    'StorageUtilizedInBytes': 123,
                    'StorageRule': {
                        'StorageAllocatedInBytes': 123,
                        'StorageType': 'UNLIMITED'|'QUOTA'
                    }
                }
            },
            'CreatedTimestamp': datetime(2015, 1, 1),
            'Status': 'DRAFT'|'PUBLISHED'|'DELETED',
            'Visibility': 'PUBLIC'|'PRIVATE',
            'RecipientId': 'string'
        }
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.ProhibitedStateException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    WorkDocs.Client.exceptions.DocumentLockedForCommentsException
    WorkDocs.Client.exceptions.InvalidCommentOperationException
    
    """
    pass

def create_custom_metadata(AuthenticationToken=None, ResourceId=None, VersionId=None, CustomMetadata=None):
    """
    Adds one or more custom properties to the specified resource (a folder, document, or version).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_custom_metadata(
        AuthenticationToken='string',
        ResourceId='string',
        VersionId='string',
        CustomMetadata={
            'string': 'string'
        }
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource.\n

    :type VersionId: string
    :param VersionId: The ID of the version, if the custom metadata is being added to a document version.

    :type CustomMetadata: dict
    :param CustomMetadata: [REQUIRED]\nCustom metadata in the form of name-value pairs.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.ProhibitedStateException
WorkDocs.Client.exceptions.CustomMetadataLimitExceededException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_folder(AuthenticationToken=None, Name=None, ParentFolderId=None):
    """
    Creates a folder with the specified name and parent folder.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_folder(
        AuthenticationToken='string',
        Name='string',
        ParentFolderId='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type Name: string
    :param Name: The name of the new folder.

    :type ParentFolderId: string
    :param ParentFolderId: [REQUIRED]\nThe ID of the parent folder.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Metadata': {
        'Id': 'string',
        'Name': 'string',
        'CreatorId': 'string',
        'ParentFolderId': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'ModifiedTimestamp': datetime(2015, 1, 1),
        'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
        'Signature': 'string',
        'Labels': [
            'string',
        ],
        'Size': 123,
        'LatestVersionSize': 123
    }
}


Response Structure

(dict) --

Metadata (dict) --
The metadata of the folder.

Id (string) --
The ID of the folder.

Name (string) --
The name of the folder.

CreatorId (string) --
The ID of the creator.

ParentFolderId (string) --
The ID of the parent folder.

CreatedTimestamp (datetime) --
The time when the folder was created.

ModifiedTimestamp (datetime) --
The time when the folder was updated.

ResourceState (string) --
The resource state of the folder.

Signature (string) --
The unique identifier created from the subfolders and documents of the folder.

Labels (list) --
List of labels on the folder.

(string) --


Size (integer) --
The size of the folder metadata.

LatestVersionSize (integer) --
The size of the latest version of the folder metadata.









Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.EntityAlreadyExistsException
WorkDocs.Client.exceptions.ProhibitedStateException
WorkDocs.Client.exceptions.ConflictingOperationException
WorkDocs.Client.exceptions.LimitExceededException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'Metadata': {
            'Id': 'string',
            'Name': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Signature': 'string',
            'Labels': [
                'string',
            ],
            'Size': 123,
            'LatestVersionSize': 123
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def create_labels(ResourceId=None, Labels=None, AuthenticationToken=None):
    """
    Adds the specified list of labels to the given resource (a document or folder)
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_labels(
        ResourceId='string',
        Labels=[
            'string',
        ],
        AuthenticationToken='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource.\n

    :type Labels: list
    :param Labels: [REQUIRED]\nList of labels to add to the resource.\n\n(string) --\n\n

    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException
WorkDocs.Client.exceptions.TooManyLabelsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_notification_subscription(OrganizationId=None, Endpoint=None, Protocol=None, SubscriptionType=None):
    """
    Configure Amazon WorkDocs to use Amazon SNS notifications. The endpoint receives a confirmation message, and must confirm the subscription.
    For more information, see Subscribe to Notifications in the Amazon WorkDocs Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_notification_subscription(
        OrganizationId='string',
        Endpoint='string',
        Protocol='HTTPS',
        SubscriptionType='ALL'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]\nThe ID of the organization.\n

    :type Endpoint: string
    :param Endpoint: [REQUIRED]\nThe endpoint to receive the notifications. If the protocol is HTTPS, the endpoint is a URL that begins with https .\n

    :type Protocol: string
    :param Protocol: [REQUIRED]\nThe protocol to use. The supported value is https, which delivers JSON-encoded messages using HTTPS POST.\n

    :type SubscriptionType: string
    :param SubscriptionType: [REQUIRED]\nThe notification type.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Subscription': {
        'SubscriptionId': 'string',
        'EndPoint': 'string',
        'Protocol': 'HTTPS'
    }
}


Response Structure

(dict) --

Subscription (dict) --
The subscription.

SubscriptionId (string) --
The ID of the subscription.

EndPoint (string) --
The endpoint of the subscription.

Protocol (string) --
The protocol of the subscription.









Exceptions

WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.TooManySubscriptionsException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'Subscription': {
            'SubscriptionId': 'string',
            'EndPoint': 'string',
            'Protocol': 'HTTPS'
        }
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.TooManySubscriptionsException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def create_user(OrganizationId=None, Username=None, EmailAddress=None, GivenName=None, Surname=None, Password=None, TimeZoneId=None, StorageRule=None, AuthenticationToken=None):
    """
    Creates a user in a Simple AD or Microsoft AD directory. The status of a newly created user is "ACTIVE". New users can access Amazon WorkDocs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_user(
        OrganizationId='string',
        Username='string',
        EmailAddress='string',
        GivenName='string',
        Surname='string',
        Password='string',
        TimeZoneId='string',
        StorageRule={
            'StorageAllocatedInBytes': 123,
            'StorageType': 'UNLIMITED'|'QUOTA'
        },
        AuthenticationToken='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: The ID of the organization.

    :type Username: string
    :param Username: [REQUIRED]\nThe login name of the user.\n

    :type EmailAddress: string
    :param EmailAddress: The email address of the user.

    :type GivenName: string
    :param GivenName: [REQUIRED]\nThe given name of the user.\n

    :type Surname: string
    :param Surname: [REQUIRED]\nThe surname of the user.\n

    :type Password: string
    :param Password: [REQUIRED]\nThe password of the user.\n

    :type TimeZoneId: string
    :param TimeZoneId: The time zone ID of the user.

    :type StorageRule: dict
    :param StorageRule: The amount of storage for the user.\n\nStorageAllocatedInBytes (integer) --The amount of storage allocated, in bytes.\n\nStorageType (string) --The type of storage.\n\n\n

    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'Id': 'string',
        'Username': 'string',
        'EmailAddress': 'string',
        'GivenName': 'string',
        'Surname': 'string',
        'OrganizationId': 'string',
        'RootFolderId': 'string',
        'RecycleBinFolderId': 'string',
        'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
        'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'ModifiedTimestamp': datetime(2015, 1, 1),
        'TimeZoneId': 'string',
        'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
        'Storage': {
            'StorageUtilizedInBytes': 123,
            'StorageRule': {
                'StorageAllocatedInBytes': 123,
                'StorageType': 'UNLIMITED'|'QUOTA'
            }
        }
    }
}


Response Structure

(dict) --

User (dict) --
The user information.

Id (string) --
The ID of the user.

Username (string) --
The login name of the user.

EmailAddress (string) --
The email address of the user.

GivenName (string) --
The given name of the user.

Surname (string) --
The surname of the user.

OrganizationId (string) --
The ID of the organization.

RootFolderId (string) --
The ID of the root folder.

RecycleBinFolderId (string) --
The ID of the recycle bin folder.

Status (string) --
The status of the user.

Type (string) --
The type of user.

CreatedTimestamp (datetime) --
The time when the user was created.

ModifiedTimestamp (datetime) --
The time when the user was modified.

TimeZoneId (string) --
The time zone ID of the user.

Locale (string) --
The locale of the user.

Storage (dict) --
The storage for the user.

StorageUtilizedInBytes (integer) --
The amount of storage used, in bytes.

StorageRule (dict) --
The storage for a user.

StorageAllocatedInBytes (integer) --
The amount of storage allocated, in bytes.

StorageType (string) --
The type of storage.













Exceptions

WorkDocs.Client.exceptions.EntityAlreadyExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'User': {
            'Id': 'string',
            'Username': 'string',
            'EmailAddress': 'string',
            'GivenName': 'string',
            'Surname': 'string',
            'OrganizationId': 'string',
            'RootFolderId': 'string',
            'RecycleBinFolderId': 'string',
            'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
            'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'TimeZoneId': 'string',
            'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
            'Storage': {
                'StorageUtilizedInBytes': 123,
                'StorageRule': {
                    'StorageAllocatedInBytes': 123,
                    'StorageType': 'UNLIMITED'|'QUOTA'
                }
            }
        }
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.EntityAlreadyExistsException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def deactivate_user(UserId=None, AuthenticationToken=None):
    """
    Deactivates the specified user, which revokes the user\'s access to Amazon WorkDocs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deactivate_user(
        UserId='string',
        AuthenticationToken='string'
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]\nThe ID of the user.\n

    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_comment(AuthenticationToken=None, DocumentId=None, VersionId=None, CommentId=None):
    """
    Deletes the specified comment from the document version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_comment(
        AuthenticationToken='string',
        DocumentId='string',
        VersionId='string',
        CommentId='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :type VersionId: string
    :param VersionId: [REQUIRED]\nThe ID of the document version.\n

    :type CommentId: string
    :param CommentId: [REQUIRED]\nThe ID of the comment.\n

    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.ProhibitedStateException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    WorkDocs.Client.exceptions.DocumentLockedForCommentsException
    
    """
    pass

def delete_custom_metadata(AuthenticationToken=None, ResourceId=None, VersionId=None, Keys=None, DeleteAll=None):
    """
    Deletes custom metadata from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_custom_metadata(
        AuthenticationToken='string',
        ResourceId='string',
        VersionId='string',
        Keys=[
            'string',
        ],
        DeleteAll=True|False
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource, either a document or folder.\n

    :type VersionId: string
    :param VersionId: The ID of the version, if the custom metadata is being deleted from a document version.

    :type Keys: list
    :param Keys: List of properties to remove.\n\n(string) --\n\n

    :type DeleteAll: boolean
    :param DeleteAll: Flag to indicate removal of all custom metadata properties from the specified resource.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.ProhibitedStateException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_document(AuthenticationToken=None, DocumentId=None):
    """
    Permanently deletes the specified document and its associated metadata.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_document(
        AuthenticationToken='string',
        DocumentId='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.ProhibitedStateException
    WorkDocs.Client.exceptions.ConflictingOperationException
    WorkDocs.Client.exceptions.ConcurrentModificationException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_folder(AuthenticationToken=None, FolderId=None):
    """
    Permanently deletes the specified folder and its contents.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_folder(
        AuthenticationToken='string',
        FolderId='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type FolderId: string
    :param FolderId: [REQUIRED]\nThe ID of the folder.\n

    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.ProhibitedStateException
    WorkDocs.Client.exceptions.ConflictingOperationException
    WorkDocs.Client.exceptions.ConcurrentModificationException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_folder_contents(AuthenticationToken=None, FolderId=None):
    """
    Deletes the contents of the specified folder.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_folder_contents(
        AuthenticationToken='string',
        FolderId='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type FolderId: string
    :param FolderId: [REQUIRED]\nThe ID of the folder.\n

    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.ProhibitedStateException
    WorkDocs.Client.exceptions.ConflictingOperationException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_labels(ResourceId=None, AuthenticationToken=None, Labels=None, DeleteAll=None):
    """
    Deletes the specified list of labels from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_labels(
        ResourceId='string',
        AuthenticationToken='string',
        Labels=[
            'string',
        ],
        DeleteAll=True|False
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource.\n

    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type Labels: list
    :param Labels: List of labels to delete from the resource.\n\n(string) --\n\n

    :type DeleteAll: boolean
    :param DeleteAll: Flag to request removal of all labels from the specified resource.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_notification_subscription(SubscriptionId=None, OrganizationId=None):
    """
    Deletes the specified subscription from the specified organization.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_notification_subscription(
        SubscriptionId='string',
        OrganizationId='string'
    )
    
    
    :type SubscriptionId: string
    :param SubscriptionId: [REQUIRED]\nThe ID of the subscription.\n

    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]\nThe ID of the organization.\n

    :returns: 
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    WorkDocs.Client.exceptions.ProhibitedStateException
    
    """
    pass

def delete_user(AuthenticationToken=None, UserId=None):
    """
    Deletes the specified user from a Simple AD or Microsoft AD directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_user(
        AuthenticationToken='string',
        UserId='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using AWS credentials.

    :type UserId: string
    :param UserId: [REQUIRED]\nThe ID of the user.\n

    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_activities(AuthenticationToken=None, StartTime=None, EndTime=None, OrganizationId=None, ActivityTypes=None, ResourceId=None, UserId=None, IncludeIndirectActivities=None, Limit=None, Marker=None):
    """
    Describes the user activities in a specified time period.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_activities(
        AuthenticationToken='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        OrganizationId='string',
        ActivityTypes='string',
        ResourceId='string',
        UserId='string',
        IncludeIndirectActivities=True|False,
        Limit=123,
        Marker='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type StartTime: datetime
    :param StartTime: The timestamp that determines the starting time of the activities. The response includes the activities performed after the specified timestamp.

    :type EndTime: datetime
    :param EndTime: The timestamp that determines the end time of the activities. The response includes the activities performed before the specified timestamp.

    :type OrganizationId: string
    :param OrganizationId: The ID of the organization. This is a mandatory parameter when using administrative API (SigV4) requests.

    :type ActivityTypes: string
    :param ActivityTypes: Specifies which activity types to include in the response. If this field is left empty, all activity types are returned.

    :type ResourceId: string
    :param ResourceId: The document or folder ID for which to describe activity types.

    :type UserId: string
    :param UserId: The ID of the user who performed the action. The response includes activities pertaining to this user. This is an optional parameter and is only applicable for administrative API (SigV4) requests.

    :type IncludeIndirectActivities: boolean
    :param IncludeIndirectActivities: Includes indirect activities. An indirect activity results from a direct activity performed on a parent resource. For example, sharing a parent folder (the direct activity) shares all of the subfolders and documents within the parent folder (the indirect activity).

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :type Marker: string
    :param Marker: The marker for the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'UserActivities': [
        {
            'Type': 'DOCUMENT_CHECKED_IN'|'DOCUMENT_CHECKED_OUT'|'DOCUMENT_RENAMED'|'DOCUMENT_VERSION_UPLOADED'|'DOCUMENT_VERSION_DELETED'|'DOCUMENT_VERSION_VIEWED'|'DOCUMENT_VERSION_DOWNLOADED'|'DOCUMENT_RECYCLED'|'DOCUMENT_RESTORED'|'DOCUMENT_REVERTED'|'DOCUMENT_SHARED'|'DOCUMENT_UNSHARED'|'DOCUMENT_SHARE_PERMISSION_CHANGED'|'DOCUMENT_SHAREABLE_LINK_CREATED'|'DOCUMENT_SHAREABLE_LINK_REMOVED'|'DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED'|'DOCUMENT_MOVED'|'DOCUMENT_COMMENT_ADDED'|'DOCUMENT_COMMENT_DELETED'|'DOCUMENT_ANNOTATION_ADDED'|'DOCUMENT_ANNOTATION_DELETED'|'FOLDER_CREATED'|'FOLDER_DELETED'|'FOLDER_RENAMED'|'FOLDER_RECYCLED'|'FOLDER_RESTORED'|'FOLDER_SHARED'|'FOLDER_UNSHARED'|'FOLDER_SHARE_PERMISSION_CHANGED'|'FOLDER_SHAREABLE_LINK_CREATED'|'FOLDER_SHAREABLE_LINK_REMOVED'|'FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED'|'FOLDER_MOVED',
            'TimeStamp': datetime(2015, 1, 1),
            'IsIndirectActivity': True|False,
            'OrganizationId': 'string',
            'Initiator': {
                'Id': 'string',
                'Username': 'string',
                'GivenName': 'string',
                'Surname': 'string',
                'EmailAddress': 'string'
            },
            'Participants': {
                'Users': [
                    {
                        'Id': 'string',
                        'Username': 'string',
                        'GivenName': 'string',
                        'Surname': 'string',
                        'EmailAddress': 'string'
                    },
                ],
                'Groups': [
                    {
                        'Id': 'string',
                        'Name': 'string'
                    },
                ]
            },
            'ResourceMetadata': {
                'Type': 'FOLDER'|'DOCUMENT',
                'Name': 'string',
                'OriginalName': 'string',
                'Id': 'string',
                'VersionId': 'string',
                'Owner': {
                    'Id': 'string',
                    'Username': 'string',
                    'GivenName': 'string',
                    'Surname': 'string',
                    'EmailAddress': 'string'
                },
                'ParentId': 'string'
            },
            'OriginalParent': {
                'Type': 'FOLDER'|'DOCUMENT',
                'Name': 'string',
                'OriginalName': 'string',
                'Id': 'string',
                'VersionId': 'string',
                'Owner': {
                    'Id': 'string',
                    'Username': 'string',
                    'GivenName': 'string',
                    'Surname': 'string',
                    'EmailAddress': 'string'
                },
                'ParentId': 'string'
            },
            'CommentMetadata': {
                'CommentId': 'string',
                'Contributor': {
                    'Id': 'string',
                    'Username': 'string',
                    'EmailAddress': 'string',
                    'GivenName': 'string',
                    'Surname': 'string',
                    'OrganizationId': 'string',
                    'RootFolderId': 'string',
                    'RecycleBinFolderId': 'string',
                    'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
                    'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'ModifiedTimestamp': datetime(2015, 1, 1),
                    'TimeZoneId': 'string',
                    'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
                    'Storage': {
                        'StorageUtilizedInBytes': 123,
                        'StorageRule': {
                            'StorageAllocatedInBytes': 123,
                            'StorageType': 'UNLIMITED'|'QUOTA'
                        }
                    }
                },
                'CreatedTimestamp': datetime(2015, 1, 1),
                'CommentStatus': 'DRAFT'|'PUBLISHED'|'DELETED',
                'RecipientId': 'string'
            }
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

UserActivities (list) --
The list of activities for the specified user and time period.

(dict) --
Describes the activity information.

Type (string) --
The activity type.

TimeStamp (datetime) --
The timestamp when the action was performed.

IsIndirectActivity (boolean) --
Indicates whether an activity is indirect or direct. An indirect activity results from a direct activity performed on a parent resource. For example, sharing a parent folder (the direct activity) shares all of the subfolders and documents within the parent folder (the indirect activity).

OrganizationId (string) --
The ID of the organization.

Initiator (dict) --
The user who performed the action.

Id (string) --
The ID of the user.

Username (string) --
The name of the user.

GivenName (string) --
The given name of the user before a rename operation.

Surname (string) --
The surname of the user.

EmailAddress (string) --
The email address of the user.



Participants (dict) --
The list of users or groups impacted by this action. This is an optional field and is filled for the following sharing activities: DOCUMENT_SHARED, DOCUMENT_SHARED, DOCUMENT_UNSHARED, FOLDER_SHARED, FOLDER_UNSHARED.

Users (list) --
The list of users.

(dict) --
Describes the metadata of the user.

Id (string) --
The ID of the user.

Username (string) --
The name of the user.

GivenName (string) --
The given name of the user before a rename operation.

Surname (string) --
The surname of the user.

EmailAddress (string) --
The email address of the user.





Groups (list) --
The list of user groups.

(dict) --
Describes the metadata of a user group.

Id (string) --
The ID of the user group.

Name (string) --
The name of the group.







ResourceMetadata (dict) --
The metadata of the resource involved in the user action.

Type (string) --
The type of resource.

Name (string) --
The name of the resource.

OriginalName (string) --
The original name of the resource before a rename operation.

Id (string) --
The ID of the resource.

VersionId (string) --
The version ID of the resource. This is an optional field and is filled for action on document version.

Owner (dict) --
The owner of the resource.

Id (string) --
The ID of the user.

Username (string) --
The name of the user.

GivenName (string) --
The given name of the user before a rename operation.

Surname (string) --
The surname of the user.

EmailAddress (string) --
The email address of the user.



ParentId (string) --
The parent ID of the resource before a rename operation.



OriginalParent (dict) --
The original parent of the resource. This is an optional field and is filled for move activities.

Type (string) --
The type of resource.

Name (string) --
The name of the resource.

OriginalName (string) --
The original name of the resource before a rename operation.

Id (string) --
The ID of the resource.

VersionId (string) --
The version ID of the resource. This is an optional field and is filled for action on document version.

Owner (dict) --
The owner of the resource.

Id (string) --
The ID of the user.

Username (string) --
The name of the user.

GivenName (string) --
The given name of the user before a rename operation.

Surname (string) --
The surname of the user.

EmailAddress (string) --
The email address of the user.



ParentId (string) --
The parent ID of the resource before a rename operation.



CommentMetadata (dict) --
Metadata of the commenting activity. This is an optional field and is filled for commenting activities.

CommentId (string) --
The ID of the comment.

Contributor (dict) --
The user who made the comment.

Id (string) --
The ID of the user.

Username (string) --
The login name of the user.

EmailAddress (string) --
The email address of the user.

GivenName (string) --
The given name of the user.

Surname (string) --
The surname of the user.

OrganizationId (string) --
The ID of the organization.

RootFolderId (string) --
The ID of the root folder.

RecycleBinFolderId (string) --
The ID of the recycle bin folder.

Status (string) --
The status of the user.

Type (string) --
The type of user.

CreatedTimestamp (datetime) --
The time when the user was created.

ModifiedTimestamp (datetime) --
The time when the user was modified.

TimeZoneId (string) --
The time zone ID of the user.

Locale (string) --
The locale of the user.

Storage (dict) --
The storage for the user.

StorageUtilizedInBytes (integer) --
The amount of storage used, in bytes.

StorageRule (dict) --
The storage for a user.

StorageAllocatedInBytes (integer) --
The amount of storage allocated, in bytes.

StorageType (string) --
The type of storage.







CreatedTimestamp (datetime) --
The timestamp that the comment was created.

CommentStatus (string) --
The status of the comment.

RecipientId (string) --
The ID of the user being replied to.







Marker (string) --
The marker for the next set of results.







Exceptions

WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.InvalidArgumentException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'UserActivities': [
            {
                'Type': 'DOCUMENT_CHECKED_IN'|'DOCUMENT_CHECKED_OUT'|'DOCUMENT_RENAMED'|'DOCUMENT_VERSION_UPLOADED'|'DOCUMENT_VERSION_DELETED'|'DOCUMENT_VERSION_VIEWED'|'DOCUMENT_VERSION_DOWNLOADED'|'DOCUMENT_RECYCLED'|'DOCUMENT_RESTORED'|'DOCUMENT_REVERTED'|'DOCUMENT_SHARED'|'DOCUMENT_UNSHARED'|'DOCUMENT_SHARE_PERMISSION_CHANGED'|'DOCUMENT_SHAREABLE_LINK_CREATED'|'DOCUMENT_SHAREABLE_LINK_REMOVED'|'DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED'|'DOCUMENT_MOVED'|'DOCUMENT_COMMENT_ADDED'|'DOCUMENT_COMMENT_DELETED'|'DOCUMENT_ANNOTATION_ADDED'|'DOCUMENT_ANNOTATION_DELETED'|'FOLDER_CREATED'|'FOLDER_DELETED'|'FOLDER_RENAMED'|'FOLDER_RECYCLED'|'FOLDER_RESTORED'|'FOLDER_SHARED'|'FOLDER_UNSHARED'|'FOLDER_SHARE_PERMISSION_CHANGED'|'FOLDER_SHAREABLE_LINK_CREATED'|'FOLDER_SHAREABLE_LINK_REMOVED'|'FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED'|'FOLDER_MOVED',
                'TimeStamp': datetime(2015, 1, 1),
                'IsIndirectActivity': True|False,
                'OrganizationId': 'string',
                'Initiator': {
                    'Id': 'string',
                    'Username': 'string',
                    'GivenName': 'string',
                    'Surname': 'string',
                    'EmailAddress': 'string'
                },
                'Participants': {
                    'Users': [
                        {
                            'Id': 'string',
                            'Username': 'string',
                            'GivenName': 'string',
                            'Surname': 'string',
                            'EmailAddress': 'string'
                        },
                    ],
                    'Groups': [
                        {
                            'Id': 'string',
                            'Name': 'string'
                        },
                    ]
                },
                'ResourceMetadata': {
                    'Type': 'FOLDER'|'DOCUMENT',
                    'Name': 'string',
                    'OriginalName': 'string',
                    'Id': 'string',
                    'VersionId': 'string',
                    'Owner': {
                        'Id': 'string',
                        'Username': 'string',
                        'GivenName': 'string',
                        'Surname': 'string',
                        'EmailAddress': 'string'
                    },
                    'ParentId': 'string'
                },
                'OriginalParent': {
                    'Type': 'FOLDER'|'DOCUMENT',
                    'Name': 'string',
                    'OriginalName': 'string',
                    'Id': 'string',
                    'VersionId': 'string',
                    'Owner': {
                        'Id': 'string',
                        'Username': 'string',
                        'GivenName': 'string',
                        'Surname': 'string',
                        'EmailAddress': 'string'
                    },
                    'ParentId': 'string'
                },
                'CommentMetadata': {
                    'CommentId': 'string',
                    'Contributor': {
                        'Id': 'string',
                        'Username': 'string',
                        'EmailAddress': 'string',
                        'GivenName': 'string',
                        'Surname': 'string',
                        'OrganizationId': 'string',
                        'RootFolderId': 'string',
                        'RecycleBinFolderId': 'string',
                        'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
                        'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'ModifiedTimestamp': datetime(2015, 1, 1),
                        'TimeZoneId': 'string',
                        'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
                        'Storage': {
                            'StorageUtilizedInBytes': 123,
                            'StorageRule': {
                                'StorageAllocatedInBytes': 123,
                                'StorageType': 'UNLIMITED'|'QUOTA'
                            }
                        }
                    },
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'CommentStatus': 'DRAFT'|'PUBLISHED'|'DELETED',
                    'RecipientId': 'string'
                }
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.InvalidArgumentException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_comments(AuthenticationToken=None, DocumentId=None, VersionId=None, Limit=None, Marker=None):
    """
    List all the comments for the specified document version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_comments(
        AuthenticationToken='string',
        DocumentId='string',
        VersionId='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :type VersionId: string
    :param VersionId: [REQUIRED]\nThe ID of the document version.\n

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :type Marker: string
    :param Marker: The marker for the next set of results. This marker was received from a previous call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Comments': [
        {
            'CommentId': 'string',
            'ParentId': 'string',
            'ThreadId': 'string',
            'Text': 'string',
            'Contributor': {
                'Id': 'string',
                'Username': 'string',
                'EmailAddress': 'string',
                'GivenName': 'string',
                'Surname': 'string',
                'OrganizationId': 'string',
                'RootFolderId': 'string',
                'RecycleBinFolderId': 'string',
                'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
                'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'TimeZoneId': 'string',
                'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
                'Storage': {
                    'StorageUtilizedInBytes': 123,
                    'StorageRule': {
                        'StorageAllocatedInBytes': 123,
                        'StorageType': 'UNLIMITED'|'QUOTA'
                    }
                }
            },
            'CreatedTimestamp': datetime(2015, 1, 1),
            'Status': 'DRAFT'|'PUBLISHED'|'DELETED',
            'Visibility': 'PUBLIC'|'PRIVATE',
            'RecipientId': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

Comments (list) --
The list of comments for the specified document version.

(dict) --
Describes a comment.

CommentId (string) --
The ID of the comment.

ParentId (string) --
The ID of the parent comment.

ThreadId (string) --
The ID of the root comment in the thread.

Text (string) --
The text of the comment.

Contributor (dict) --
The details of the user who made the comment.

Id (string) --
The ID of the user.

Username (string) --
The login name of the user.

EmailAddress (string) --
The email address of the user.

GivenName (string) --
The given name of the user.

Surname (string) --
The surname of the user.

OrganizationId (string) --
The ID of the organization.

RootFolderId (string) --
The ID of the root folder.

RecycleBinFolderId (string) --
The ID of the recycle bin folder.

Status (string) --
The status of the user.

Type (string) --
The type of user.

CreatedTimestamp (datetime) --
The time when the user was created.

ModifiedTimestamp (datetime) --
The time when the user was modified.

TimeZoneId (string) --
The time zone ID of the user.

Locale (string) --
The locale of the user.

Storage (dict) --
The storage for the user.

StorageUtilizedInBytes (integer) --
The amount of storage used, in bytes.

StorageRule (dict) --
The storage for a user.

StorageAllocatedInBytes (integer) --
The amount of storage allocated, in bytes.

StorageType (string) --
The type of storage.







CreatedTimestamp (datetime) --
The time that the comment was created.

Status (string) --
The status of the comment.

Visibility (string) --
The visibility of the comment. Options are either PRIVATE, where the comment is visible only to the comment author and document owner and co-owners, or PUBLIC, where the comment is visible to document owners, co-owners, and contributors.

RecipientId (string) --
If the comment is a reply to another user\'s comment, this field contains the user ID of the user being replied to.





Marker (string) --
The marker for the next set of results. This marker was received from a previous call.







Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.ProhibitedStateException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'Comments': [
            {
                'CommentId': 'string',
                'ParentId': 'string',
                'ThreadId': 'string',
                'Text': 'string',
                'Contributor': {
                    'Id': 'string',
                    'Username': 'string',
                    'EmailAddress': 'string',
                    'GivenName': 'string',
                    'Surname': 'string',
                    'OrganizationId': 'string',
                    'RootFolderId': 'string',
                    'RecycleBinFolderId': 'string',
                    'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
                    'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'ModifiedTimestamp': datetime(2015, 1, 1),
                    'TimeZoneId': 'string',
                    'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
                    'Storage': {
                        'StorageUtilizedInBytes': 123,
                        'StorageRule': {
                            'StorageAllocatedInBytes': 123,
                            'StorageType': 'UNLIMITED'|'QUOTA'
                        }
                    }
                },
                'CreatedTimestamp': datetime(2015, 1, 1),
                'Status': 'DRAFT'|'PUBLISHED'|'DELETED',
                'Visibility': 'PUBLIC'|'PRIVATE',
                'RecipientId': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.ProhibitedStateException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_document_versions(AuthenticationToken=None, DocumentId=None, Marker=None, Limit=None, Include=None, Fields=None):
    """
    Retrieves the document versions for the specified document.
    By default, only active versions are returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_document_versions(
        AuthenticationToken='string',
        DocumentId='string',
        Marker='string',
        Limit=123,
        Include='string',
        Fields='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type Limit: integer
    :param Limit: The maximum number of versions to return with this call.

    :type Include: string
    :param Include: A comma-separated list of values. Specify 'INITIALIZED' to include incomplete versions.

    :type Fields: string
    :param Fields: Specify 'SOURCE' to include initialized versions and a URL for the source document.

    :rtype: dict

ReturnsResponse Syntax
{
    'DocumentVersions': [
        {
            'Id': 'string',
            'Name': 'string',
            'ContentType': 'string',
            'Size': 123,
            'Signature': 'string',
            'Status': 'INITIALIZED'|'ACTIVE',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ContentCreatedTimestamp': datetime(2015, 1, 1),
            'ContentModifiedTimestamp': datetime(2015, 1, 1),
            'CreatorId': 'string',
            'Thumbnail': {
                'string': 'string'
            },
            'Source': {
                'string': 'string'
            }
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

DocumentVersions (list) --
The document versions.

(dict) --
Describes a version of a document.

Id (string) --
The ID of the version.

Name (string) --
The name of the version.

ContentType (string) --
The content type of the document.

Size (integer) --
The size of the document, in bytes.

Signature (string) --
The signature of the document.

Status (string) --
The status of the document.

CreatedTimestamp (datetime) --
The timestamp when the document was first uploaded.

ModifiedTimestamp (datetime) --
The timestamp when the document was last uploaded.

ContentCreatedTimestamp (datetime) --
The timestamp when the content of the document was originally created.

ContentModifiedTimestamp (datetime) --
The timestamp when the content of the document was modified.

CreatorId (string) --
The ID of the creator.

Thumbnail (dict) --
The thumbnail of the document.

(string) --
(string) --




Source (dict) --
The source of the document.

(string) --
(string) --








Marker (string) --
The marker to use when requesting the next set of results. If there are no additional results, the string is empty.







Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.InvalidArgumentException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException
WorkDocs.Client.exceptions.ProhibitedStateException


    :return: {
        'DocumentVersions': [
            {
                'Id': 'string',
                'Name': 'string',
                'ContentType': 'string',
                'Size': 123,
                'Signature': 'string',
                'Status': 'INITIALIZED'|'ACTIVE',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'ContentCreatedTimestamp': datetime(2015, 1, 1),
                'ContentModifiedTimestamp': datetime(2015, 1, 1),
                'CreatorId': 'string',
                'Thumbnail': {
                    'string': 'string'
                },
                'Source': {
                    'string': 'string'
                }
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_folder_contents(AuthenticationToken=None, FolderId=None, Sort=None, Order=None, Limit=None, Marker=None, Type=None, Include=None):
    """
    Describes the contents of the specified folder, including its documents and subfolders.
    By default, Amazon WorkDocs returns the first 100 active document and folder metadata items. If there are more results, the response includes a marker that you can use to request the next set of results. You can also request initialized documents.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_folder_contents(
        AuthenticationToken='string',
        FolderId='string',
        Sort='DATE'|'NAME',
        Order='ASCENDING'|'DESCENDING',
        Limit=123,
        Marker='string',
        Type='ALL'|'DOCUMENT'|'FOLDER',
        Include='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type FolderId: string
    :param FolderId: [REQUIRED]\nThe ID of the folder.\n

    :type Sort: string
    :param Sort: The sorting criteria.

    :type Order: string
    :param Order: The order for the contents of the folder.

    :type Limit: integer
    :param Limit: The maximum number of items to return with this call.

    :type Marker: string
    :param Marker: The marker for the next set of results. This marker was received from a previous call.

    :type Type: string
    :param Type: The type of items.

    :type Include: string
    :param Include: The contents to include. Specify 'INITIALIZED' to include initialized documents.

    :rtype: dict

ReturnsResponse Syntax
{
    'Folders': [
        {
            'Id': 'string',
            'Name': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Signature': 'string',
            'Labels': [
                'string',
            ],
            'Size': 123,
            'LatestVersionSize': 123
        },
    ],
    'Documents': [
        {
            'Id': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'LatestVersionMetadata': {
                'Id': 'string',
                'Name': 'string',
                'ContentType': 'string',
                'Size': 123,
                'Signature': 'string',
                'Status': 'INITIALIZED'|'ACTIVE',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'ContentCreatedTimestamp': datetime(2015, 1, 1),
                'ContentModifiedTimestamp': datetime(2015, 1, 1),
                'CreatorId': 'string',
                'Thumbnail': {
                    'string': 'string'
                },
                'Source': {
                    'string': 'string'
                }
            },
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Labels': [
                'string',
            ]
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

Folders (list) --
The subfolders in the specified folder.

(dict) --
Describes a folder.

Id (string) --
The ID of the folder.

Name (string) --
The name of the folder.

CreatorId (string) --
The ID of the creator.

ParentFolderId (string) --
The ID of the parent folder.

CreatedTimestamp (datetime) --
The time when the folder was created.

ModifiedTimestamp (datetime) --
The time when the folder was updated.

ResourceState (string) --
The resource state of the folder.

Signature (string) --
The unique identifier created from the subfolders and documents of the folder.

Labels (list) --
List of labels on the folder.

(string) --


Size (integer) --
The size of the folder metadata.

LatestVersionSize (integer) --
The size of the latest version of the folder metadata.





Documents (list) --
The documents in the specified folder.

(dict) --
Describes the document.

Id (string) --
The ID of the document.

CreatorId (string) --
The ID of the creator.

ParentFolderId (string) --
The ID of the parent folder.

CreatedTimestamp (datetime) --
The time when the document was created.

ModifiedTimestamp (datetime) --
The time when the document was updated.

LatestVersionMetadata (dict) --
The latest version of the document.

Id (string) --
The ID of the version.

Name (string) --
The name of the version.

ContentType (string) --
The content type of the document.

Size (integer) --
The size of the document, in bytes.

Signature (string) --
The signature of the document.

Status (string) --
The status of the document.

CreatedTimestamp (datetime) --
The timestamp when the document was first uploaded.

ModifiedTimestamp (datetime) --
The timestamp when the document was last uploaded.

ContentCreatedTimestamp (datetime) --
The timestamp when the content of the document was originally created.

ContentModifiedTimestamp (datetime) --
The timestamp when the content of the document was modified.

CreatorId (string) --
The ID of the creator.

Thumbnail (dict) --
The thumbnail of the document.

(string) --
(string) --




Source (dict) --
The source of the document.

(string) --
(string) --






ResourceState (string) --
The resource state.

Labels (list) --
List of labels on the document.

(string) --






Marker (string) --
The marker to use when requesting the next set of results. If there are no additional results, the string is empty.







Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.InvalidArgumentException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException
WorkDocs.Client.exceptions.ProhibitedStateException


    :return: {
        'Folders': [
            {
                'Id': 'string',
                'Name': 'string',
                'CreatorId': 'string',
                'ParentFolderId': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
                'Signature': 'string',
                'Labels': [
                    'string',
                ],
                'Size': 123,
                'LatestVersionSize': 123
            },
        ],
        'Documents': [
            {
                'Id': 'string',
                'CreatorId': 'string',
                'ParentFolderId': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'LatestVersionMetadata': {
                    'Id': 'string',
                    'Name': 'string',
                    'ContentType': 'string',
                    'Size': 123,
                    'Signature': 'string',
                    'Status': 'INITIALIZED'|'ACTIVE',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'ModifiedTimestamp': datetime(2015, 1, 1),
                    'ContentCreatedTimestamp': datetime(2015, 1, 1),
                    'ContentModifiedTimestamp': datetime(2015, 1, 1),
                    'CreatorId': 'string',
                    'Thumbnail': {
                        'string': 'string'
                    },
                    'Source': {
                        'string': 'string'
                    }
                },
                'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
                'Labels': [
                    'string',
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_groups(AuthenticationToken=None, SearchQuery=None, OrganizationId=None, Marker=None, Limit=None):
    """
    Describes the groups specified by the query. Groups are defined by the underlying Active Directory.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_groups(
        AuthenticationToken='string',
        SearchQuery='string',
        OrganizationId='string',
        Marker='string',
        Limit=123
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type SearchQuery: string
    :param SearchQuery: [REQUIRED]\nA query to describe groups by group name.\n

    :type OrganizationId: string
    :param OrganizationId: The ID of the organization.

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type Limit: integer
    :param Limit: The maximum number of items to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Groups': [
        {
            'Id': 'string',
            'Name': 'string'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

Groups (list) --
The list of groups.

(dict) --
Describes the metadata of a user group.

Id (string) --
The ID of the user group.

Name (string) --
The name of the group.





Marker (string) --
The marker to use when requesting the next set of results. If there are no additional results, the string is empty.







Exceptions

WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'Groups': [
            {
                'Id': 'string',
                'Name': 'string'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_notification_subscriptions(OrganizationId=None, Marker=None, Limit=None):
    """
    Lists the specified notification subscriptions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_notification_subscriptions(
        OrganizationId='string',
        Marker='string',
        Limit=123
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]\nThe ID of the organization.\n

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type Limit: integer
    :param Limit: The maximum number of items to return with this call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Subscriptions': [
        {
            'SubscriptionId': 'string',
            'EndPoint': 'string',
            'Protocol': 'HTTPS'
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

Subscriptions (list) --
The subscriptions.

(dict) --
Describes a subscription.

SubscriptionId (string) --
The ID of the subscription.

EndPoint (string) --
The endpoint of the subscription.

Protocol (string) --
The protocol of the subscription.





Marker (string) --
The marker to use when requesting the next set of results. If there are no additional results, the string is empty.







Exceptions

WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'Subscriptions': [
            {
                'SubscriptionId': 'string',
                'EndPoint': 'string',
                'Protocol': 'HTTPS'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_resource_permissions(AuthenticationToken=None, ResourceId=None, PrincipalId=None, Limit=None, Marker=None):
    """
    Describes the permissions of a specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_resource_permissions(
        AuthenticationToken='string',
        ResourceId='string',
        PrincipalId='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource.\n

    :type PrincipalId: string
    :param PrincipalId: The ID of the principal to filter permissions by.

    :type Limit: integer
    :param Limit: The maximum number of items to return with this call.

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call)

    :rtype: dict

ReturnsResponse Syntax
{
    'Principals': [
        {
            'Id': 'string',
            'Type': 'USER'|'GROUP'|'INVITE'|'ANONYMOUS'|'ORGANIZATION',
            'Roles': [
                {
                    'Role': 'VIEWER'|'CONTRIBUTOR'|'OWNER'|'COOWNER',
                    'Type': 'DIRECT'|'INHERITED'
                },
            ]
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

Principals (list) --
The principals.

(dict) --
Describes a resource.

Id (string) --
The ID of the resource.

Type (string) --
The type of resource.

Roles (list) --
The permission information for the resource.

(dict) --
Describes the permissions.

Role (string) --
The role of the user.

Type (string) --
The type of permissions.









Marker (string) --
The marker to use when requesting the next set of results. If there are no additional results, the string is empty.







Exceptions

WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'Principals': [
            {
                'Id': 'string',
                'Type': 'USER'|'GROUP'|'INVITE'|'ANONYMOUS'|'ORGANIZATION',
                'Roles': [
                    {
                        'Role': 'VIEWER'|'CONTRIBUTOR'|'OWNER'|'COOWNER',
                        'Type': 'DIRECT'|'INHERITED'
                    },
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def describe_root_folders(AuthenticationToken=None, Limit=None, Marker=None):
    """
    Describes the current user\'s special folders; the RootFolder and the RecycleBin . RootFolder is the root of user\'s files and folders and RecycleBin is the root of recycled items. This is not a valid action for SigV4 (administrative API) clients.
    This action requires an authentication token. To get an authentication token, register an application with Amazon WorkDocs. For more information, see Authentication and Access Control for User Applications in the Amazon WorkDocs Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_root_folders(
        AuthenticationToken='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: [REQUIRED]\nAmazon WorkDocs authentication token.\n

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :rtype: dict

ReturnsResponse Syntax
{
    'Folders': [
        {
            'Id': 'string',
            'Name': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Signature': 'string',
            'Labels': [
                'string',
            ],
            'Size': 123,
            'LatestVersionSize': 123
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

Folders (list) --
The user\'s special folders.

(dict) --
Describes a folder.

Id (string) --
The ID of the folder.

Name (string) --
The name of the folder.

CreatorId (string) --
The ID of the creator.

ParentFolderId (string) --
The ID of the parent folder.

CreatedTimestamp (datetime) --
The time when the folder was created.

ModifiedTimestamp (datetime) --
The time when the folder was updated.

ResourceState (string) --
The resource state of the folder.

Signature (string) --
The unique identifier created from the subfolders and documents of the folder.

Labels (list) --
List of labels on the folder.

(string) --


Size (integer) --
The size of the folder metadata.

LatestVersionSize (integer) --
The size of the latest version of the folder metadata.





Marker (string) --
The marker for the next set of results.







Exceptions

WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.InvalidArgumentException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'Folders': [
            {
                'Id': 'string',
                'Name': 'string',
                'CreatorId': 'string',
                'ParentFolderId': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
                'Signature': 'string',
                'Labels': [
                    'string',
                ],
                'Size': 123,
                'LatestVersionSize': 123
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_users(AuthenticationToken=None, OrganizationId=None, UserIds=None, Query=None, Include=None, Order=None, Sort=None, Marker=None, Limit=None, Fields=None):
    """
    Describes the specified users. You can describe all users or filter the results (for example, by status or organization).
    By default, Amazon WorkDocs returns the first 24 active or pending users. If there are more results, the response includes a marker that you can use to request the next set of results.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_users(
        AuthenticationToken='string',
        OrganizationId='string',
        UserIds='string',
        Query='string',
        Include='ALL'|'ACTIVE_PENDING',
        Order='ASCENDING'|'DESCENDING',
        Sort='USER_NAME'|'FULL_NAME'|'STORAGE_LIMIT'|'USER_STATUS'|'STORAGE_USED',
        Marker='string',
        Limit=123,
        Fields='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type OrganizationId: string
    :param OrganizationId: The ID of the organization.

    :type UserIds: string
    :param UserIds: The IDs of the users.

    :type Query: string
    :param Query: A query to filter users by user name.

    :type Include: string
    :param Include: The state of the users. Specify 'ALL' to include inactive users.

    :type Order: string
    :param Order: The order for the results.

    :type Sort: string
    :param Sort: The sorting criteria.

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type Limit: integer
    :param Limit: The maximum number of items to return.

    :type Fields: string
    :param Fields: A comma-separated list of values. Specify 'STORAGE_METADATA' to include the user storage quota and utilization information.

    :rtype: dict

ReturnsResponse Syntax
{
    'Users': [
        {
            'Id': 'string',
            'Username': 'string',
            'EmailAddress': 'string',
            'GivenName': 'string',
            'Surname': 'string',
            'OrganizationId': 'string',
            'RootFolderId': 'string',
            'RecycleBinFolderId': 'string',
            'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
            'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'TimeZoneId': 'string',
            'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
            'Storage': {
                'StorageUtilizedInBytes': 123,
                'StorageRule': {
                    'StorageAllocatedInBytes': 123,
                    'StorageType': 'UNLIMITED'|'QUOTA'
                }
            }
        },
    ],
    'TotalNumberOfUsers': 123,
    'Marker': 'string'
}


Response Structure

(dict) --

Users (list) --
The users.

(dict) --
Describes a user.

Id (string) --
The ID of the user.

Username (string) --
The login name of the user.

EmailAddress (string) --
The email address of the user.

GivenName (string) --
The given name of the user.

Surname (string) --
The surname of the user.

OrganizationId (string) --
The ID of the organization.

RootFolderId (string) --
The ID of the root folder.

RecycleBinFolderId (string) --
The ID of the recycle bin folder.

Status (string) --
The status of the user.

Type (string) --
The type of user.

CreatedTimestamp (datetime) --
The time when the user was created.

ModifiedTimestamp (datetime) --
The time when the user was modified.

TimeZoneId (string) --
The time zone ID of the user.

Locale (string) --
The locale of the user.

Storage (dict) --
The storage for the user.

StorageUtilizedInBytes (integer) --
The amount of storage used, in bytes.

StorageRule (dict) --
The storage for a user.

StorageAllocatedInBytes (integer) --
The amount of storage allocated, in bytes.

StorageType (string) --
The type of storage.









TotalNumberOfUsers (integer) --
The total number of users included in the results.

Marker (string) --
The marker to use when requesting the next set of results. If there are no additional results, the string is empty.







Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException
WorkDocs.Client.exceptions.InvalidArgumentException
WorkDocs.Client.exceptions.RequestedEntityTooLargeException


    :return: {
        'Users': [
            {
                'Id': 'string',
                'Username': 'string',
                'EmailAddress': 'string',
                'GivenName': 'string',
                'Surname': 'string',
                'OrganizationId': 'string',
                'RootFolderId': 'string',
                'RecycleBinFolderId': 'string',
                'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
                'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'TimeZoneId': 'string',
                'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
                'Storage': {
                    'StorageUtilizedInBytes': 123,
                    'StorageRule': {
                        'StorageAllocatedInBytes': 123,
                        'StorageType': 'UNLIMITED'|'QUOTA'
                    }
                }
            },
        ],
        'TotalNumberOfUsers': 123,
        'Marker': 'string'
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    WorkDocs.Client.exceptions.InvalidArgumentException
    WorkDocs.Client.exceptions.RequestedEntityTooLargeException
    
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

def get_current_user(AuthenticationToken=None):
    """
    Retrieves details of the current user for whom the authentication token was generated. This is not a valid action for SigV4 (administrative API) clients.
    This action requires an authentication token. To get an authentication token, register an application with Amazon WorkDocs. For more information, see Authentication and Access Control for User Applications in the Amazon WorkDocs Developer Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_current_user(
        AuthenticationToken='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: [REQUIRED]\nAmazon WorkDocs authentication token.\n

    :rtype: dict
ReturnsResponse Syntax{
    'User': {
        'Id': 'string',
        'Username': 'string',
        'EmailAddress': 'string',
        'GivenName': 'string',
        'Surname': 'string',
        'OrganizationId': 'string',
        'RootFolderId': 'string',
        'RecycleBinFolderId': 'string',
        'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
        'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'ModifiedTimestamp': datetime(2015, 1, 1),
        'TimeZoneId': 'string',
        'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
        'Storage': {
            'StorageUtilizedInBytes': 123,
            'StorageRule': {
                'StorageAllocatedInBytes': 123,
                'StorageType': 'UNLIMITED'|'QUOTA'
            }
        }
    }
}


Response Structure

(dict) --
User (dict) --Metadata of the user.

Id (string) --The ID of the user.

Username (string) --The login name of the user.

EmailAddress (string) --The email address of the user.

GivenName (string) --The given name of the user.

Surname (string) --The surname of the user.

OrganizationId (string) --The ID of the organization.

RootFolderId (string) --The ID of the root folder.

RecycleBinFolderId (string) --The ID of the recycle bin folder.

Status (string) --The status of the user.

Type (string) --The type of user.

CreatedTimestamp (datetime) --The time when the user was created.

ModifiedTimestamp (datetime) --The time when the user was modified.

TimeZoneId (string) --The time zone ID of the user.

Locale (string) --The locale of the user.

Storage (dict) --The storage for the user.

StorageUtilizedInBytes (integer) --The amount of storage used, in bytes.

StorageRule (dict) --The storage for a user.

StorageAllocatedInBytes (integer) --The amount of storage allocated, in bytes.

StorageType (string) --The type of storage.












Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'User': {
            'Id': 'string',
            'Username': 'string',
            'EmailAddress': 'string',
            'GivenName': 'string',
            'Surname': 'string',
            'OrganizationId': 'string',
            'RootFolderId': 'string',
            'RecycleBinFolderId': 'string',
            'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
            'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'TimeZoneId': 'string',
            'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
            'Storage': {
                'StorageUtilizedInBytes': 123,
                'StorageRule': {
                    'StorageAllocatedInBytes': 123,
                    'StorageType': 'UNLIMITED'|'QUOTA'
                }
            }
        }
    }
    
    
    """
    pass

def get_document(AuthenticationToken=None, DocumentId=None, IncludeCustomMetadata=None):
    """
    Retrieves details of a document.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_document(
        AuthenticationToken='string',
        DocumentId='string',
        IncludeCustomMetadata=True|False
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :type IncludeCustomMetadata: boolean
    :param IncludeCustomMetadata: Set this to TRUE to include custom metadata in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Metadata': {
        'Id': 'string',
        'CreatorId': 'string',
        'ParentFolderId': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'ModifiedTimestamp': datetime(2015, 1, 1),
        'LatestVersionMetadata': {
            'Id': 'string',
            'Name': 'string',
            'ContentType': 'string',
            'Size': 123,
            'Signature': 'string',
            'Status': 'INITIALIZED'|'ACTIVE',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ContentCreatedTimestamp': datetime(2015, 1, 1),
            'ContentModifiedTimestamp': datetime(2015, 1, 1),
            'CreatorId': 'string',
            'Thumbnail': {
                'string': 'string'
            },
            'Source': {
                'string': 'string'
            }
        },
        'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
        'Labels': [
            'string',
        ]
    },
    'CustomMetadata': {
        'string': 'string'
    }
}


Response Structure

(dict) --

Metadata (dict) --
The metadata details of the document.

Id (string) --
The ID of the document.

CreatorId (string) --
The ID of the creator.

ParentFolderId (string) --
The ID of the parent folder.

CreatedTimestamp (datetime) --
The time when the document was created.

ModifiedTimestamp (datetime) --
The time when the document was updated.

LatestVersionMetadata (dict) --
The latest version of the document.

Id (string) --
The ID of the version.

Name (string) --
The name of the version.

ContentType (string) --
The content type of the document.

Size (integer) --
The size of the document, in bytes.

Signature (string) --
The signature of the document.

Status (string) --
The status of the document.

CreatedTimestamp (datetime) --
The timestamp when the document was first uploaded.

ModifiedTimestamp (datetime) --
The timestamp when the document was last uploaded.

ContentCreatedTimestamp (datetime) --
The timestamp when the content of the document was originally created.

ContentModifiedTimestamp (datetime) --
The timestamp when the content of the document was modified.

CreatorId (string) --
The ID of the creator.

Thumbnail (dict) --
The thumbnail of the document.

(string) --
(string) --




Source (dict) --
The source of the document.

(string) --
(string) --






ResourceState (string) --
The resource state.

Labels (list) --
List of labels on the document.

(string) --




CustomMetadata (dict) --
The custom metadata on the document.

(string) --
(string) --










Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.InvalidArgumentException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException
WorkDocs.Client.exceptions.InvalidPasswordException


    :return: {
        'Metadata': {
            'Id': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'LatestVersionMetadata': {
                'Id': 'string',
                'Name': 'string',
                'ContentType': 'string',
                'Size': 123,
                'Signature': 'string',
                'Status': 'INITIALIZED'|'ACTIVE',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'ContentCreatedTimestamp': datetime(2015, 1, 1),
                'ContentModifiedTimestamp': datetime(2015, 1, 1),
                'CreatorId': 'string',
                'Thumbnail': {
                    'string': 'string'
                },
                'Source': {
                    'string': 'string'
                }
            },
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Labels': [
                'string',
            ]
        },
        'CustomMetadata': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_document_path(AuthenticationToken=None, DocumentId=None, Limit=None, Fields=None, Marker=None):
    """
    Retrieves the path information (the hierarchy from the root folder) for the requested document.
    By default, Amazon WorkDocs returns a maximum of 100 levels upwards from the requested document and only includes the IDs of the parent folders in the path. You can limit the maximum number of levels. You can also request the names of the parent folders.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_document_path(
        AuthenticationToken='string',
        DocumentId='string',
        Limit=123,
        Fields='string',
        Marker='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :type Limit: integer
    :param Limit: The maximum number of levels in the hierarchy to return.

    :type Fields: string
    :param Fields: A comma-separated list of values. Specify NAME to include the names of the parent folders.

    :type Marker: string
    :param Marker: This value is not supported.

    :rtype: dict

ReturnsResponse Syntax
{
    'Path': {
        'Components': [
            {
                'Id': 'string',
                'Name': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Path (dict) --
The path information.

Components (list) --
The components of the resource path.

(dict) --
Describes the resource path.

Id (string) --
The ID of the resource path.

Name (string) --
The name of the resource path.













Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'Path': {
            'Components': [
                {
                    'Id': 'string',
                    'Name': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def get_document_version(AuthenticationToken=None, DocumentId=None, VersionId=None, Fields=None, IncludeCustomMetadata=None):
    """
    Retrieves version metadata for the specified document.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_document_version(
        AuthenticationToken='string',
        DocumentId='string',
        VersionId='string',
        Fields='string',
        IncludeCustomMetadata=True|False
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :type VersionId: string
    :param VersionId: [REQUIRED]\nThe version ID of the document.\n

    :type Fields: string
    :param Fields: A comma-separated list of values. Specify 'SOURCE' to include a URL for the source document.

    :type IncludeCustomMetadata: boolean
    :param IncludeCustomMetadata: Set this to TRUE to include custom metadata in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Metadata': {
        'Id': 'string',
        'Name': 'string',
        'ContentType': 'string',
        'Size': 123,
        'Signature': 'string',
        'Status': 'INITIALIZED'|'ACTIVE',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'ModifiedTimestamp': datetime(2015, 1, 1),
        'ContentCreatedTimestamp': datetime(2015, 1, 1),
        'ContentModifiedTimestamp': datetime(2015, 1, 1),
        'CreatorId': 'string',
        'Thumbnail': {
            'string': 'string'
        },
        'Source': {
            'string': 'string'
        }
    },
    'CustomMetadata': {
        'string': 'string'
    }
}


Response Structure

(dict) --

Metadata (dict) --
The version metadata.

Id (string) --
The ID of the version.

Name (string) --
The name of the version.

ContentType (string) --
The content type of the document.

Size (integer) --
The size of the document, in bytes.

Signature (string) --
The signature of the document.

Status (string) --
The status of the document.

CreatedTimestamp (datetime) --
The timestamp when the document was first uploaded.

ModifiedTimestamp (datetime) --
The timestamp when the document was last uploaded.

ContentCreatedTimestamp (datetime) --
The timestamp when the content of the document was originally created.

ContentModifiedTimestamp (datetime) --
The timestamp when the content of the document was modified.

CreatorId (string) --
The ID of the creator.

Thumbnail (dict) --
The thumbnail of the document.

(string) --
(string) --




Source (dict) --
The source of the document.

(string) --
(string) --






CustomMetadata (dict) --
The custom metadata on the document version.

(string) --
(string) --










Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException
WorkDocs.Client.exceptions.ProhibitedStateException
WorkDocs.Client.exceptions.InvalidPasswordException


    :return: {
        'Metadata': {
            'Id': 'string',
            'Name': 'string',
            'ContentType': 'string',
            'Size': 123,
            'Signature': 'string',
            'Status': 'INITIALIZED'|'ACTIVE',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ContentCreatedTimestamp': datetime(2015, 1, 1),
            'ContentModifiedTimestamp': datetime(2015, 1, 1),
            'CreatorId': 'string',
            'Thumbnail': {
                'string': 'string'
            },
            'Source': {
                'string': 'string'
            }
        },
        'CustomMetadata': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_folder(AuthenticationToken=None, FolderId=None, IncludeCustomMetadata=None):
    """
    Retrieves the metadata of the specified folder.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_folder(
        AuthenticationToken='string',
        FolderId='string',
        IncludeCustomMetadata=True|False
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type FolderId: string
    :param FolderId: [REQUIRED]\nThe ID of the folder.\n

    :type IncludeCustomMetadata: boolean
    :param IncludeCustomMetadata: Set to TRUE to include custom metadata in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'Metadata': {
        'Id': 'string',
        'Name': 'string',
        'CreatorId': 'string',
        'ParentFolderId': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'ModifiedTimestamp': datetime(2015, 1, 1),
        'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
        'Signature': 'string',
        'Labels': [
            'string',
        ],
        'Size': 123,
        'LatestVersionSize': 123
    },
    'CustomMetadata': {
        'string': 'string'
    }
}


Response Structure

(dict) --

Metadata (dict) --
The metadata of the folder.

Id (string) --
The ID of the folder.

Name (string) --
The name of the folder.

CreatorId (string) --
The ID of the creator.

ParentFolderId (string) --
The ID of the parent folder.

CreatedTimestamp (datetime) --
The time when the folder was created.

ModifiedTimestamp (datetime) --
The time when the folder was updated.

ResourceState (string) --
The resource state of the folder.

Signature (string) --
The unique identifier created from the subfolders and documents of the folder.

Labels (list) --
List of labels on the folder.

(string) --


Size (integer) --
The size of the folder metadata.

LatestVersionSize (integer) --
The size of the latest version of the folder metadata.



CustomMetadata (dict) --
The custom metadata on the folder.

(string) --
(string) --










Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.InvalidArgumentException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException
WorkDocs.Client.exceptions.ProhibitedStateException


    :return: {
        'Metadata': {
            'Id': 'string',
            'Name': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Signature': 'string',
            'Labels': [
                'string',
            ],
            'Size': 123,
            'LatestVersionSize': 123
        },
        'CustomMetadata': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_folder_path(AuthenticationToken=None, FolderId=None, Limit=None, Fields=None, Marker=None):
    """
    Retrieves the path information (the hierarchy from the root folder) for the specified folder.
    By default, Amazon WorkDocs returns a maximum of 100 levels upwards from the requested folder and only includes the IDs of the parent folders in the path. You can limit the maximum number of levels. You can also request the parent folder names.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_folder_path(
        AuthenticationToken='string',
        FolderId='string',
        Limit=123,
        Fields='string',
        Marker='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type FolderId: string
    :param FolderId: [REQUIRED]\nThe ID of the folder.\n

    :type Limit: integer
    :param Limit: The maximum number of levels in the hierarchy to return.

    :type Fields: string
    :param Fields: A comma-separated list of values. Specify 'NAME' to include the names of the parent folders.

    :type Marker: string
    :param Marker: This value is not supported.

    :rtype: dict

ReturnsResponse Syntax
{
    'Path': {
        'Components': [
            {
                'Id': 'string',
                'Name': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

Path (dict) --
The path information.

Components (list) --
The components of the resource path.

(dict) --
Describes the resource path.

Id (string) --
The ID of the resource path.

Name (string) --
The name of the resource path.













Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'Path': {
            'Components': [
                {
                    'Id': 'string',
                    'Name': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
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

def get_resources(AuthenticationToken=None, UserId=None, CollectionType=None, Limit=None, Marker=None):
    """
    Retrieves a collection of resources, including folders and documents. The only CollectionType supported is SHARED_WITH_ME .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resources(
        AuthenticationToken='string',
        UserId='string',
        CollectionType='SHARED_WITH_ME',
        Limit=123,
        Marker='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: The Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type UserId: string
    :param UserId: The user ID for the resource collection. This is a required field for accessing the API operation using IAM credentials.

    :type CollectionType: string
    :param CollectionType: The collection type.

    :type Limit: integer
    :param Limit: The maximum number of resources to return.

    :type Marker: string
    :param Marker: The marker for the next set of results. This marker was received from a previous call.

    :rtype: dict

ReturnsResponse Syntax
{
    'Folders': [
        {
            'Id': 'string',
            'Name': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Signature': 'string',
            'Labels': [
                'string',
            ],
            'Size': 123,
            'LatestVersionSize': 123
        },
    ],
    'Documents': [
        {
            'Id': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'LatestVersionMetadata': {
                'Id': 'string',
                'Name': 'string',
                'ContentType': 'string',
                'Size': 123,
                'Signature': 'string',
                'Status': 'INITIALIZED'|'ACTIVE',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'ContentCreatedTimestamp': datetime(2015, 1, 1),
                'ContentModifiedTimestamp': datetime(2015, 1, 1),
                'CreatorId': 'string',
                'Thumbnail': {
                    'string': 'string'
                },
                'Source': {
                    'string': 'string'
                }
            },
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Labels': [
                'string',
            ]
        },
    ],
    'Marker': 'string'
}


Response Structure

(dict) --

Folders (list) --
The folders in the specified folder.

(dict) --
Describes a folder.

Id (string) --
The ID of the folder.

Name (string) --
The name of the folder.

CreatorId (string) --
The ID of the creator.

ParentFolderId (string) --
The ID of the parent folder.

CreatedTimestamp (datetime) --
The time when the folder was created.

ModifiedTimestamp (datetime) --
The time when the folder was updated.

ResourceState (string) --
The resource state of the folder.

Signature (string) --
The unique identifier created from the subfolders and documents of the folder.

Labels (list) --
List of labels on the folder.

(string) --


Size (integer) --
The size of the folder metadata.

LatestVersionSize (integer) --
The size of the latest version of the folder metadata.





Documents (list) --
The documents in the specified collection.

(dict) --
Describes the document.

Id (string) --
The ID of the document.

CreatorId (string) --
The ID of the creator.

ParentFolderId (string) --
The ID of the parent folder.

CreatedTimestamp (datetime) --
The time when the document was created.

ModifiedTimestamp (datetime) --
The time when the document was updated.

LatestVersionMetadata (dict) --
The latest version of the document.

Id (string) --
The ID of the version.

Name (string) --
The name of the version.

ContentType (string) --
The content type of the document.

Size (integer) --
The size of the document, in bytes.

Signature (string) --
The signature of the document.

Status (string) --
The status of the document.

CreatedTimestamp (datetime) --
The timestamp when the document was first uploaded.

ModifiedTimestamp (datetime) --
The timestamp when the document was last uploaded.

ContentCreatedTimestamp (datetime) --
The timestamp when the content of the document was originally created.

ContentModifiedTimestamp (datetime) --
The timestamp when the content of the document was modified.

CreatorId (string) --
The ID of the creator.

Thumbnail (dict) --
The thumbnail of the document.

(string) --
(string) --




Source (dict) --
The source of the document.

(string) --
(string) --






ResourceState (string) --
The resource state.

Labels (list) --
List of labels on the document.

(string) --






Marker (string) --
The marker to use when requesting the next set of results. If there are no additional results, the string is empty.







Exceptions

WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.InvalidArgumentException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException


    :return: {
        'Folders': [
            {
                'Id': 'string',
                'Name': 'string',
                'CreatorId': 'string',
                'ParentFolderId': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
                'Signature': 'string',
                'Labels': [
                    'string',
                ],
                'Size': 123,
                'LatestVersionSize': 123
            },
        ],
        'Documents': [
            {
                'Id': 'string',
                'CreatorId': 'string',
                'ParentFolderId': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'LatestVersionMetadata': {
                    'Id': 'string',
                    'Name': 'string',
                    'ContentType': 'string',
                    'Size': 123,
                    'Signature': 'string',
                    'Status': 'INITIALIZED'|'ACTIVE',
                    'CreatedTimestamp': datetime(2015, 1, 1),
                    'ModifiedTimestamp': datetime(2015, 1, 1),
                    'ContentCreatedTimestamp': datetime(2015, 1, 1),
                    'ContentModifiedTimestamp': datetime(2015, 1, 1),
                    'CreatorId': 'string',
                    'Thumbnail': {
                        'string': 'string'
                    },
                    'Source': {
                        'string': 'string'
                    }
                },
                'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
                'Labels': [
                    'string',
                ]
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    
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

def initiate_document_version_upload(AuthenticationToken=None, Id=None, Name=None, ContentCreatedTimestamp=None, ContentModifiedTimestamp=None, ContentType=None, DocumentSizeInBytes=None, ParentFolderId=None):
    """
    Creates a new document object and version object.
    The client specifies the parent folder ID and name of the document to upload. The ID is optionally specified when creating a new version of an existing document. This is the first step to upload a document. Next, upload the document to the URL returned from the call, and then call  UpdateDocumentVersion .
    To cancel the document upload, call  AbortDocumentVersionUpload .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.initiate_document_version_upload(
        AuthenticationToken='string',
        Id='string',
        Name='string',
        ContentCreatedTimestamp=datetime(2015, 1, 1),
        ContentModifiedTimestamp=datetime(2015, 1, 1),
        ContentType='string',
        DocumentSizeInBytes=123,
        ParentFolderId='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type Id: string
    :param Id: The ID of the document.

    :type Name: string
    :param Name: The name of the document.

    :type ContentCreatedTimestamp: datetime
    :param ContentCreatedTimestamp: The timestamp when the content of the document was originally created.

    :type ContentModifiedTimestamp: datetime
    :param ContentModifiedTimestamp: The timestamp when the content of the document was modified.

    :type ContentType: string
    :param ContentType: The content type of the document.

    :type DocumentSizeInBytes: integer
    :param DocumentSizeInBytes: The size of the document, in bytes.

    :type ParentFolderId: string
    :param ParentFolderId: [REQUIRED]\nThe ID of the parent folder.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Metadata': {
        'Id': 'string',
        'CreatorId': 'string',
        'ParentFolderId': 'string',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'ModifiedTimestamp': datetime(2015, 1, 1),
        'LatestVersionMetadata': {
            'Id': 'string',
            'Name': 'string',
            'ContentType': 'string',
            'Size': 123,
            'Signature': 'string',
            'Status': 'INITIALIZED'|'ACTIVE',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ContentCreatedTimestamp': datetime(2015, 1, 1),
            'ContentModifiedTimestamp': datetime(2015, 1, 1),
            'CreatorId': 'string',
            'Thumbnail': {
                'string': 'string'
            },
            'Source': {
                'string': 'string'
            }
        },
        'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
        'Labels': [
            'string',
        ]
    },
    'UploadMetadata': {
        'UploadUrl': 'string',
        'SignedHeaders': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --

Metadata (dict) --
The document metadata.

Id (string) --
The ID of the document.

CreatorId (string) --
The ID of the creator.

ParentFolderId (string) --
The ID of the parent folder.

CreatedTimestamp (datetime) --
The time when the document was created.

ModifiedTimestamp (datetime) --
The time when the document was updated.

LatestVersionMetadata (dict) --
The latest version of the document.

Id (string) --
The ID of the version.

Name (string) --
The name of the version.

ContentType (string) --
The content type of the document.

Size (integer) --
The size of the document, in bytes.

Signature (string) --
The signature of the document.

Status (string) --
The status of the document.

CreatedTimestamp (datetime) --
The timestamp when the document was first uploaded.

ModifiedTimestamp (datetime) --
The timestamp when the document was last uploaded.

ContentCreatedTimestamp (datetime) --
The timestamp when the content of the document was originally created.

ContentModifiedTimestamp (datetime) --
The timestamp when the content of the document was modified.

CreatorId (string) --
The ID of the creator.

Thumbnail (dict) --
The thumbnail of the document.

(string) --
(string) --




Source (dict) --
The source of the document.

(string) --
(string) --






ResourceState (string) --
The resource state.

Labels (list) --
List of labels on the document.

(string) --




UploadMetadata (dict) --
The upload metadata.

UploadUrl (string) --
The URL of the upload.

SignedHeaders (dict) --
The signed headers.

(string) --
(string) --












Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.EntityAlreadyExistsException
WorkDocs.Client.exceptions.StorageLimitExceededException
WorkDocs.Client.exceptions.StorageLimitWillExceedException
WorkDocs.Client.exceptions.ProhibitedStateException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException
WorkDocs.Client.exceptions.DraftUploadOutOfSyncException
WorkDocs.Client.exceptions.ResourceAlreadyCheckedOutException


    :return: {
        'Metadata': {
            'Id': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'LatestVersionMetadata': {
                'Id': 'string',
                'Name': 'string',
                'ContentType': 'string',
                'Size': 123,
                'Signature': 'string',
                'Status': 'INITIALIZED'|'ACTIVE',
                'CreatedTimestamp': datetime(2015, 1, 1),
                'ModifiedTimestamp': datetime(2015, 1, 1),
                'ContentCreatedTimestamp': datetime(2015, 1, 1),
                'ContentModifiedTimestamp': datetime(2015, 1, 1),
                'CreatorId': 'string',
                'Thumbnail': {
                    'string': 'string'
                },
                'Source': {
                    'string': 'string'
                }
            },
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Labels': [
                'string',
            ]
        },
        'UploadMetadata': {
            'UploadUrl': 'string',
            'SignedHeaders': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def remove_all_resource_permissions(AuthenticationToken=None, ResourceId=None):
    """
    Removes all the permissions from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_all_resource_permissions(
        AuthenticationToken='string',
        ResourceId='string'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource.\n

    :returns: 
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def remove_resource_permission(AuthenticationToken=None, ResourceId=None, PrincipalId=None, PrincipalType=None):
    """
    Removes the permission for the specified principal from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_resource_permission(
        AuthenticationToken='string',
        ResourceId='string',
        PrincipalId='string',
        PrincipalType='USER'|'GROUP'|'INVITE'|'ANONYMOUS'|'ORGANIZATION'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type ResourceId: string
    :param ResourceId: [REQUIRED]\nThe ID of the resource.\n

    :type PrincipalId: string
    :param PrincipalId: [REQUIRED]\nThe principal ID of the resource.\n

    :type PrincipalType: string
    :param PrincipalType: The principal type of the resource.

    :returns: 
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def update_document(AuthenticationToken=None, DocumentId=None, Name=None, ParentFolderId=None, ResourceState=None):
    """
    Updates the specified attributes of a document. The user must have access to both the document and its parent folder, if applicable.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_document(
        AuthenticationToken='string',
        DocumentId='string',
        Name='string',
        ParentFolderId='string',
        ResourceState='ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :type Name: string
    :param Name: The name of the document.

    :type ParentFolderId: string
    :param ParentFolderId: The ID of the parent folder.

    :type ResourceState: string
    :param ResourceState: The resource state of the document. Only ACTIVE and RECYCLED are supported.

    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.EntityAlreadyExistsException
    WorkDocs.Client.exceptions.LimitExceededException
    WorkDocs.Client.exceptions.ProhibitedStateException
    WorkDocs.Client.exceptions.ConflictingOperationException
    WorkDocs.Client.exceptions.ConcurrentModificationException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def update_document_version(AuthenticationToken=None, DocumentId=None, VersionId=None, VersionStatus=None):
    """
    Changes the status of the document version to ACTIVE.
    Amazon WorkDocs also sets its document container to ACTIVE. This is the last step in a document upload, after the client uploads the document to an S3-presigned URL returned by  InitiateDocumentVersionUpload .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_document_version(
        AuthenticationToken='string',
        DocumentId='string',
        VersionId='string',
        VersionStatus='ACTIVE'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe ID of the document.\n

    :type VersionId: string
    :param VersionId: [REQUIRED]\nThe version ID of the document.\n

    :type VersionStatus: string
    :param VersionStatus: The status of the version.

    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.ProhibitedStateException
    WorkDocs.Client.exceptions.ConcurrentModificationException
    WorkDocs.Client.exceptions.InvalidOperationException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def update_folder(AuthenticationToken=None, FolderId=None, Name=None, ParentFolderId=None, ResourceState=None):
    """
    Updates the specified attributes of the specified folder. The user must have access to both the folder and its parent folder, if applicable.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_folder(
        AuthenticationToken='string',
        FolderId='string',
        Name='string',
        ParentFolderId='string',
        ResourceState='ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type FolderId: string
    :param FolderId: [REQUIRED]\nThe ID of the folder.\n

    :type Name: string
    :param Name: The name of the folder.

    :type ParentFolderId: string
    :param ParentFolderId: The ID of the parent folder.

    :type ResourceState: string
    :param ResourceState: The resource state of the folder. Only ACTIVE and RECYCLED are accepted values from the API.

    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.EntityAlreadyExistsException
    WorkDocs.Client.exceptions.ProhibitedStateException
    WorkDocs.Client.exceptions.ConflictingOperationException
    WorkDocs.Client.exceptions.ConcurrentModificationException
    WorkDocs.Client.exceptions.LimitExceededException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def update_user(AuthenticationToken=None, UserId=None, GivenName=None, Surname=None, Type=None, StorageRule=None, TimeZoneId=None, Locale=None, GrantPoweruserPrivileges=None):
    """
    Updates the specified attributes of the specified user, and grants or revokes administrative privileges to the Amazon WorkDocs site.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_user(
        AuthenticationToken='string',
        UserId='string',
        GivenName='string',
        Surname='string',
        Type='USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
        StorageRule={
            'StorageAllocatedInBytes': 123,
            'StorageType': 'UNLIMITED'|'QUOTA'
        },
        TimeZoneId='string',
        Locale='en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
        GrantPoweruserPrivileges='TRUE'|'FALSE'
    )
    
    
    :type AuthenticationToken: string
    :param AuthenticationToken: Amazon WorkDocs authentication token. Not required when using AWS administrator credentials to access the API.

    :type UserId: string
    :param UserId: [REQUIRED]\nThe ID of the user.\n

    :type GivenName: string
    :param GivenName: The given name of the user.

    :type Surname: string
    :param Surname: The surname of the user.

    :type Type: string
    :param Type: The type of the user.

    :type StorageRule: dict
    :param StorageRule: The amount of storage for the user.\n\nStorageAllocatedInBytes (integer) --The amount of storage allocated, in bytes.\n\nStorageType (string) --The type of storage.\n\n\n

    :type TimeZoneId: string
    :param TimeZoneId: The time zone ID of the user.

    :type Locale: string
    :param Locale: The locale of the user.

    :type GrantPoweruserPrivileges: string
    :param GrantPoweruserPrivileges: Boolean value to determine whether the user is granted Poweruser privileges.

    :rtype: dict

ReturnsResponse Syntax
{
    'User': {
        'Id': 'string',
        'Username': 'string',
        'EmailAddress': 'string',
        'GivenName': 'string',
        'Surname': 'string',
        'OrganizationId': 'string',
        'RootFolderId': 'string',
        'RecycleBinFolderId': 'string',
        'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
        'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
        'CreatedTimestamp': datetime(2015, 1, 1),
        'ModifiedTimestamp': datetime(2015, 1, 1),
        'TimeZoneId': 'string',
        'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
        'Storage': {
            'StorageUtilizedInBytes': 123,
            'StorageRule': {
                'StorageAllocatedInBytes': 123,
                'StorageType': 'UNLIMITED'|'QUOTA'
            }
        }
    }
}


Response Structure

(dict) --

User (dict) --
The user information.

Id (string) --
The ID of the user.

Username (string) --
The login name of the user.

EmailAddress (string) --
The email address of the user.

GivenName (string) --
The given name of the user.

Surname (string) --
The surname of the user.

OrganizationId (string) --
The ID of the organization.

RootFolderId (string) --
The ID of the root folder.

RecycleBinFolderId (string) --
The ID of the recycle bin folder.

Status (string) --
The status of the user.

Type (string) --
The type of user.

CreatedTimestamp (datetime) --
The time when the user was created.

ModifiedTimestamp (datetime) --
The time when the user was modified.

TimeZoneId (string) --
The time zone ID of the user.

Locale (string) --
The locale of the user.

Storage (dict) --
The storage for the user.

StorageUtilizedInBytes (integer) --
The amount of storage used, in bytes.

StorageRule (dict) --
The storage for a user.

StorageAllocatedInBytes (integer) --
The amount of storage allocated, in bytes.

StorageType (string) --
The type of storage.













Exceptions

WorkDocs.Client.exceptions.EntityNotExistsException
WorkDocs.Client.exceptions.UnauthorizedOperationException
WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
WorkDocs.Client.exceptions.IllegalUserStateException
WorkDocs.Client.exceptions.FailedDependencyException
WorkDocs.Client.exceptions.ServiceUnavailableException
WorkDocs.Client.exceptions.DeactivatingLastSystemUserException
WorkDocs.Client.exceptions.InvalidArgumentException


    :return: {
        'User': {
            'Id': 'string',
            'Username': 'string',
            'EmailAddress': 'string',
            'GivenName': 'string',
            'Surname': 'string',
            'OrganizationId': 'string',
            'RootFolderId': 'string',
            'RecycleBinFolderId': 'string',
            'Status': 'ACTIVE'|'INACTIVE'|'PENDING',
            'Type': 'USER'|'ADMIN'|'POWERUSER'|'MINIMALUSER'|'WORKSPACESUSER',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'TimeZoneId': 'string',
            'Locale': 'en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default',
            'Storage': {
                'StorageUtilizedInBytes': 123,
                'StorageRule': {
                    'StorageAllocatedInBytes': 123,
                    'StorageType': 'UNLIMITED'|'QUOTA'
                }
            }
        }
    }
    
    
    :returns: 
    WorkDocs.Client.exceptions.EntityNotExistsException
    WorkDocs.Client.exceptions.UnauthorizedOperationException
    WorkDocs.Client.exceptions.UnauthorizedResourceAccessException
    WorkDocs.Client.exceptions.IllegalUserStateException
    WorkDocs.Client.exceptions.FailedDependencyException
    WorkDocs.Client.exceptions.ServiceUnavailableException
    WorkDocs.Client.exceptions.DeactivatingLastSystemUserException
    WorkDocs.Client.exceptions.InvalidArgumentException
    
    """
    pass

