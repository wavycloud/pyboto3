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

def abort_document_version_upload(DocumentId=None, VersionId=None):
    """
    Aborts the upload of the specified document version that was previously initiated by  InitiateDocumentVersionUpload . The client should make this call only when it no longer intends or fails to upload the document version.
    See also: AWS API Documentation
    
    
    :example: response = client.abort_document_version_upload(
        DocumentId='string',
        VersionId='string'
    )
    
    
    :type DocumentId: string
    :param DocumentId: [REQUIRED]
            The ID of the document.
            

    :type VersionId: string
    :param VersionId: [REQUIRED]
            The ID of the version.
            

    """
    pass

def activate_user(UserId=None):
    """
    Activates the specified user. Only active users can access Amazon WorkDocs.
    See also: AWS API Documentation
    
    
    :example: response = client.activate_user(
        UserId='string'
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]
            The ID of the user.
            

    :rtype: dict
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
            'Type': 'USER'|'ADMIN',
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

def add_resource_permissions(ResourceId=None, Principals=None):
    """
    Creates a set of permissions for the specified folder or document. The resource permissions are overwritten if the principals already have different permissions.
    See also: AWS API Documentation
    
    
    :example: response = client.add_resource_permissions(
        ResourceId='string',
        Principals=[
            {
                'Id': 'string',
                'Type': 'USER'|'GROUP'|'INVITE'|'ANONYMOUS'|'ORGANIZATION',
                'Role': 'VIEWER'|'CONTRIBUTOR'|'OWNER'|'COOWNER'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the resource.
            

    :type Principals: list
    :param Principals: [REQUIRED]
            The users, groups, or organization being granted permission.
            (dict) --Describes the recipient type and ID, if available.
            Id (string) -- [REQUIRED]The ID of the recipient.
            Type (string) -- [REQUIRED]The type of the recipient.
            Role (string) -- [REQUIRED]The role of the recipient.
            
            

    :rtype: dict
    :return: {
        'ShareResults': [
            {
                'PrincipalId': 'string',
                'Role': 'VIEWER'|'CONTRIBUTOR'|'OWNER'|'COOWNER',
                'Status': 'SUCCESS'|'FAILURE',
                'ShareId': 'string',
                'StatusMessage': 'string'
            },
        ]
    }
    
    
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

def create_folder(Name=None, ParentFolderId=None):
    """
    Creates a folder with the specified name and parent folder.
    See also: AWS API Documentation
    
    
    :example: response = client.create_folder(
        Name='string',
        ParentFolderId='string'
    )
    
    
    :type Name: string
    :param Name: The name of the new folder.

    :type ParentFolderId: string
    :param ParentFolderId: [REQUIRED]
            The ID of the parent folder.
            

    :rtype: dict
    :return: {
        'Metadata': {
            'Id': 'string',
            'Name': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Signature': 'string'
        }
    }
    
    
    """
    pass

def create_notification_subscription(OrganizationId=None, Endpoint=None, Protocol=None, SubscriptionType=None):
    """
    Configure WorkDocs to use Amazon SNS notifications.
    The endpoint receives a confirmation message, and must confirm the subscription. For more information, see Confirm the Subscription in the Amazon Simple Notification Service Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.create_notification_subscription(
        OrganizationId='string',
        Endpoint='string',
        Protocol='HTTPS',
        SubscriptionType='ALL'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The ID of the organization.
            

    :type Endpoint: string
    :param Endpoint: [REQUIRED]
            The endpoint to receive the notifications. If the protocol is HTTPS, the endpoint is a URL that begins with 'https://'.
            

    :type Protocol: string
    :param Protocol: [REQUIRED]
            The protocol to use. The supported value is https, which delivers JSON-encoded messasges using HTTPS POST.
            

    :type SubscriptionType: string
    :param SubscriptionType: [REQUIRED]
            The notification type.
            

    :rtype: dict
    :return: {
        'Subscription': {
            'SubscriptionId': 'string',
            'EndPoint': 'string',
            'Protocol': 'HTTPS'
        }
    }
    
    
    """
    pass

def create_user(OrganizationId=None, Username=None, GivenName=None, Surname=None, Password=None, TimeZoneId=None, StorageRule=None):
    """
    Creates a user in a Simple AD or Microsoft AD directory. The status of a newly created user is "ACTIVE". New users can access Amazon WorkDocs.
    See also: AWS API Documentation
    
    
    :example: response = client.create_user(
        OrganizationId='string',
        Username='string',
        GivenName='string',
        Surname='string',
        Password='string',
        TimeZoneId='string',
        StorageRule={
            'StorageAllocatedInBytes': 123,
            'StorageType': 'UNLIMITED'|'QUOTA'
        }
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: The ID of the organization.

    :type Username: string
    :param Username: [REQUIRED]
            The login name of the user.
            

    :type GivenName: string
    :param GivenName: [REQUIRED]
            The given name of the user.
            

    :type Surname: string
    :param Surname: [REQUIRED]
            The surname of the user.
            

    :type Password: string
    :param Password: [REQUIRED]
            The password of the user.
            

    :type TimeZoneId: string
    :param TimeZoneId: The time zone ID of the user.

    :type StorageRule: dict
    :param StorageRule: The amount of storage for the user.
            StorageAllocatedInBytes (integer) --The amount of storage allocated, in bytes.
            StorageType (string) --The type of storage.
            

    :rtype: dict
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
            'Type': 'USER'|'ADMIN',
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

def deactivate_user(UserId=None):
    """
    Deactivates the specified user, which revokes the user's access to Amazon WorkDocs.
    See also: AWS API Documentation
    
    
    :example: response = client.deactivate_user(
        UserId='string'
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]
            The ID of the user.
            

    """
    pass

def delete_document(DocumentId=None):
    """
    Permanently deletes the specified document and its associated metadata.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_document(
        DocumentId='string'
    )
    
    
    :type DocumentId: string
    :param DocumentId: [REQUIRED]
            The ID of the document.
            

    """
    pass

def delete_folder(FolderId=None):
    """
    Permanently deletes the specified folder and its contents.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_folder(
        FolderId='string'
    )
    
    
    :type FolderId: string
    :param FolderId: [REQUIRED]
            The ID of the folder.
            

    """
    pass

def delete_folder_contents(FolderId=None):
    """
    Deletes the contents of the specified folder.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_folder_contents(
        FolderId='string'
    )
    
    
    :type FolderId: string
    :param FolderId: [REQUIRED]
            The ID of the folder.
            

    """
    pass

def delete_notification_subscription(SubscriptionId=None, OrganizationId=None):
    """
    Deletes the specified subscription from the specified organization.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_notification_subscription(
        SubscriptionId='string',
        OrganizationId='string'
    )
    
    
    :type SubscriptionId: string
    :param SubscriptionId: [REQUIRED]
            The ID of the subscription.
            

    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The ID of the organization.
            

    """
    pass

def delete_user(UserId=None):
    """
    Deletes the specified user from a Simple AD or Microsoft AD directory.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user(
        UserId='string'
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]
            The ID of the user.
            

    """
    pass

def describe_document_versions(DocumentId=None, Marker=None, Limit=None, Include=None, Fields=None):
    """
    Retrieves the document versions for the specified document.
    By default, only active versions are returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_document_versions(
        DocumentId='string',
        Marker='string',
        Limit=123,
        Include='string',
        Fields='string'
    )
    
    
    :type DocumentId: string
    :param DocumentId: [REQUIRED]
            The ID of the document.
            

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type Limit: integer
    :param Limit: The maximum number of versions to return with this call.

    :type Include: string
    :param Include: A comma-separated list of values. Specify 'INITIALIZED' to include incomplete versions.

    :type Fields: string
    :param Fields: Specify 'SOURCE' to include initialized versions and a URL for the source document.

    :rtype: dict
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

def describe_folder_contents(FolderId=None, Sort=None, Order=None, Limit=None, Marker=None, Type=None, Include=None):
    """
    Describes the contents of the specified folder, including its documents and sub-folders.
    By default, Amazon WorkDocs returns the first 100 active document and folder metadata items. If there are more results, the response includes a marker that you can use to request the next set of results. You can also request initialized documents.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_folder_contents(
        FolderId='string',
        Sort='DATE'|'NAME',
        Order='ASCENDING'|'DESCENDING',
        Limit=123,
        Marker='string',
        Type='ALL'|'DOCUMENT'|'FOLDER',
        Include='string'
    )
    
    
    :type FolderId: string
    :param FolderId: [REQUIRED]
            The ID of the folder.
            

    :type Sort: string
    :param Sort: The sorting criteria.

    :type Order: string
    :param Order: The order for the contents of the folder.

    :type Limit: integer
    :param Limit: The maximum number of items to return with this call.

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type Type: string
    :param Type: The type of items.

    :type Include: string
    :param Include: The contents to include. Specify 'INITIALIZED' to include initialized documents.

    :rtype: dict
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
                'Signature': 'string'
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
                'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED'
            },
        ],
        'Marker': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_notification_subscriptions(OrganizationId=None, Marker=None, Limit=None):
    """
    Lists the specified notification subscriptions.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_notification_subscriptions(
        OrganizationId='string',
        Marker='string',
        Limit=123
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The ID of the organization.
            

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call.)

    :type Limit: integer
    :param Limit: The maximum number of items to return with this call.

    :rtype: dict
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
    
    
    """
    pass

def describe_resource_permissions(ResourceId=None, Limit=None, Marker=None):
    """
    Describes the permissions of a specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_resource_permissions(
        ResourceId='string',
        Limit=123,
        Marker='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the resource.
            

    :type Limit: integer
    :param Limit: The maximum number of items to return with this call.

    :type Marker: string
    :param Marker: The marker for the next set of results. (You received this marker from a previous call)

    :rtype: dict
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
    
    
    """
    pass

def describe_users(OrganizationId=None, UserIds=None, Query=None, Include=None, Order=None, Sort=None, Marker=None, Limit=None, Fields=None):
    """
    Describes the specified users. You can describe all users or filter the results (for example, by status or organization).
    By default, Amazon WorkDocs returns the first 24 active or pending users. If there are more results, the response includes a marker that you can use to request the next set of results.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_users(
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
                'Type': 'USER'|'ADMIN',
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

def get_document(DocumentId=None):
    """
    Retrieves the specified document object.
    See also: AWS API Documentation
    
    
    :example: response = client.get_document(
        DocumentId='string'
    )
    
    
    :type DocumentId: string
    :param DocumentId: [REQUIRED]
            The ID of the document object.
            

    :rtype: dict
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
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_document_path(DocumentId=None, Limit=None, Fields=None, Marker=None):
    """
    Retrieves the path information (the hierarchy from the root folder) for the requested document.
    By default, Amazon WorkDocs returns a maximum of 100 levels upwards from the requested document and only includes the IDs of the parent folders in the path. You can limit the maximum number of levels. You can also request the names of the parent folders.
    See also: AWS API Documentation
    
    
    :example: response = client.get_document_path(
        DocumentId='string',
        Limit=123,
        Fields='string',
        Marker='string'
    )
    
    
    :type DocumentId: string
    :param DocumentId: [REQUIRED]
            The ID of the document.
            

    :type Limit: integer
    :param Limit: The maximum number of levels in the hierarchy to return.

    :type Fields: string
    :param Fields: A comma-separated list of values. Specify 'NAME' to include the names of the parent folders.

    :type Marker: string
    :param Marker: This value is not supported.

    :rtype: dict
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
    
    
    """
    pass

def get_document_version(DocumentId=None, VersionId=None, Fields=None):
    """
    Retrieves version metadata for the specified document.
    See also: AWS API Documentation
    
    
    :example: response = client.get_document_version(
        DocumentId='string',
        VersionId='string',
        Fields='string'
    )
    
    
    :type DocumentId: string
    :param DocumentId: [REQUIRED]
            The ID of the document.
            

    :type VersionId: string
    :param VersionId: [REQUIRED]
            The version ID of the document.
            

    :type Fields: string
    :param Fields: A comma-separated list of values. Specify 'SOURCE' to include a URL for the source document.

    :rtype: dict
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
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_folder(FolderId=None):
    """
    Retrieves the metadata of the specified folder.
    See also: AWS API Documentation
    
    
    :example: response = client.get_folder(
        FolderId='string'
    )
    
    
    :type FolderId: string
    :param FolderId: [REQUIRED]
            The ID of the folder.
            

    :rtype: dict
    :return: {
        'Metadata': {
            'Id': 'string',
            'Name': 'string',
            'CreatorId': 'string',
            'ParentFolderId': 'string',
            'CreatedTimestamp': datetime(2015, 1, 1),
            'ModifiedTimestamp': datetime(2015, 1, 1),
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED',
            'Signature': 'string'
        }
    }
    
    
    """
    pass

def get_folder_path(FolderId=None, Limit=None, Fields=None, Marker=None):
    """
    Retrieves the path information (the hierarchy from the root folder) for the specified folder.
    By default, Amazon WorkDocs returns a maximum of 100 levels upwards from the requested folder and only includes the IDs of the parent folders in the path. You can limit the maximum number of levels. You can also request the parent folder names.
    See also: AWS API Documentation
    
    
    :example: response = client.get_folder_path(
        FolderId='string',
        Limit=123,
        Fields='string',
        Marker='string'
    )
    
    
    :type FolderId: string
    :param FolderId: [REQUIRED]
            The ID of the folder.
            

    :type Limit: integer
    :param Limit: The maximum number of levels in the hierarchy to return.

    :type Fields: string
    :param Fields: A comma-separated list of values. Specify 'NAME' to include the names of the parent folders.

    :type Marker: string
    :param Marker: This value is not supported.

    :rtype: dict
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

def get_waiter():
    """
    
    """
    pass

def initiate_document_version_upload(Id=None, Name=None, ContentCreatedTimestamp=None, ContentModifiedTimestamp=None, ContentType=None, DocumentSizeInBytes=None, ParentFolderId=None):
    """
    Creates a new document object and version object.
    The client specifies the parent folder ID and name of the document to upload. The ID is optionally specified when creating a new version of an existing document. This is the first step to upload a document. Next, upload the document to the URL returned from the call, and then call  UpdateDocumentVersion .
    To cancel the document upload, call  AbortDocumentVersionUpload .
    See also: AWS API Documentation
    
    
    :example: response = client.initiate_document_version_upload(
        Id='string',
        Name='string',
        ContentCreatedTimestamp=datetime(2015, 1, 1),
        ContentModifiedTimestamp=datetime(2015, 1, 1),
        ContentType='string',
        DocumentSizeInBytes=123,
        ParentFolderId='string'
    )
    
    
    :type Id: string
    :param Id: The ID of the document.

    :type Name: string
    :param Name: The name of the document.

    :type ContentCreatedTimestamp: datetime
    :param ContentCreatedTimestamp: The time stamp when the content of the document was originally created.

    :type ContentModifiedTimestamp: datetime
    :param ContentModifiedTimestamp: The time stamp when the content of the document was modified.

    :type ContentType: string
    :param ContentType: The content type of the document.

    :type DocumentSizeInBytes: integer
    :param DocumentSizeInBytes: The size of the document, in bytes.

    :type ParentFolderId: string
    :param ParentFolderId: [REQUIRED]
            The ID of the parent folder.
            

    :rtype: dict
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
            'ResourceState': 'ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED'
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

def remove_all_resource_permissions(ResourceId=None):
    """
    Removes all the permissions from the specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_all_resource_permissions(
        ResourceId='string'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the resource.
            

    """
    pass

def remove_resource_permission(ResourceId=None, PrincipalId=None, PrincipalType=None):
    """
    Removes the permission for the specified principal from the specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_resource_permission(
        ResourceId='string',
        PrincipalId='string',
        PrincipalType='USER'|'GROUP'|'INVITE'|'ANONYMOUS'|'ORGANIZATION'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the resource.
            

    :type PrincipalId: string
    :param PrincipalId: [REQUIRED]
            The principal ID of the resource.
            

    :type PrincipalType: string
    :param PrincipalType: The principal type of the resource.

    """
    pass

def update_document(DocumentId=None, Name=None, ParentFolderId=None, ResourceState=None):
    """
    Updates the specified attributes of the specified document. The user must have access to both the document and its parent folder, if applicable.
    See also: AWS API Documentation
    
    
    :example: response = client.update_document(
        DocumentId='string',
        Name='string',
        ParentFolderId='string',
        ResourceState='ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED'
    )
    
    
    :type DocumentId: string
    :param DocumentId: [REQUIRED]
            The ID of the document.
            

    :type Name: string
    :param Name: The name of the document.

    :type ParentFolderId: string
    :param ParentFolderId: The ID of the parent folder.

    :type ResourceState: string
    :param ResourceState: The resource state of the document. Note that only ACTIVE and RECYCLED are supported.

    """
    pass

def update_document_version(DocumentId=None, VersionId=None, VersionStatus=None):
    """
    Changes the status of the document version to ACTIVE.
    Amazon WorkDocs also sets its document container to ACTIVE. This is the last step in a document upload, after the client uploads the document to an S3-presigned URL returned by  InitiateDocumentVersionUpload .
    See also: AWS API Documentation
    
    
    :example: response = client.update_document_version(
        DocumentId='string',
        VersionId='string',
        VersionStatus='ACTIVE'
    )
    
    
    :type DocumentId: string
    :param DocumentId: [REQUIRED]
            The ID of the document.
            

    :type VersionId: string
    :param VersionId: [REQUIRED]
            The version ID of the document.
            

    :type VersionStatus: string
    :param VersionStatus: The status of the version.

    """
    pass

def update_folder(FolderId=None, Name=None, ParentFolderId=None, ResourceState=None):
    """
    Updates the specified attributes of the specified folder. The user must have access to both the folder and its parent folder, if applicable.
    See also: AWS API Documentation
    
    
    :example: response = client.update_folder(
        FolderId='string',
        Name='string',
        ParentFolderId='string',
        ResourceState='ACTIVE'|'RESTORING'|'RECYCLING'|'RECYCLED'
    )
    
    
    :type FolderId: string
    :param FolderId: [REQUIRED]
            The ID of the folder.
            

    :type Name: string
    :param Name: The name of the folder.

    :type ParentFolderId: string
    :param ParentFolderId: The ID of the parent folder.

    :type ResourceState: string
    :param ResourceState: The resource state of the folder. Note that only ACTIVE and RECYCLED are accepted values from the API.

    """
    pass

def update_user(UserId=None, GivenName=None, Surname=None, Type=None, StorageRule=None, TimeZoneId=None, Locale=None):
    """
    Updates the specified attributes of the specified user, and grants or revokes administrative privileges to the Amazon WorkDocs site.
    See also: AWS API Documentation
    
    
    :example: response = client.update_user(
        UserId='string',
        GivenName='string',
        Surname='string',
        Type='USER'|'ADMIN',
        StorageRule={
            'StorageAllocatedInBytes': 123,
            'StorageType': 'UNLIMITED'|'QUOTA'
        },
        TimeZoneId='string',
        Locale='en'|'fr'|'ko'|'de'|'es'|'ja'|'ru'|'zh_CN'|'zh_TW'|'pt_BR'|'default'
    )
    
    
    :type UserId: string
    :param UserId: [REQUIRED]
            The ID of the user.
            

    :type GivenName: string
    :param GivenName: The given name of the user.

    :type Surname: string
    :param Surname: The surname of the user.

    :type Type: string
    :param Type: The type of the user.

    :type StorageRule: dict
    :param StorageRule: The amount of storage for the user.
            StorageAllocatedInBytes (integer) --The amount of storage allocated, in bytes.
            StorageType (string) --The type of storage.
            

    :type TimeZoneId: string
    :param TimeZoneId: The time zone ID of the user.

    :type Locale: string
    :param Locale: The locale of the user.

    :rtype: dict
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
            'Type': 'USER'|'ADMIN',
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

