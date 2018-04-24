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

def associate_delegate_to_resource(OrganizationId=None, ResourceId=None, EntityId=None):
    """
    Adds a member to the resource's set of delegates.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_delegate_to_resource(
        OrganizationId='string',
        ResourceId='string',
        EntityId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The organization under which the resource exists.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The resource for which members are associated.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The member (user or group) to associate to the resource.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_member_to_group(OrganizationId=None, GroupId=None, MemberId=None):
    """
    Adds a member to the group's set.
    See also: AWS API Documentation
    
    
    :example: response = client.associate_member_to_group(
        OrganizationId='string',
        GroupId='string',
        MemberId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The organization under which the group exists.
            

    :type GroupId: string
    :param GroupId: [REQUIRED]
            The group for which the member is associated.
            

    :type MemberId: string
    :param MemberId: [REQUIRED]
            The member to associate to the group.
            

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

def create_alias(OrganizationId=None, EntityId=None, Alias=None):
    """
    Adds an alias to the set of a given member of Amazon WorkMail.
    See also: AWS API Documentation
    
    
    :example: response = client.create_alias(
        OrganizationId='string',
        EntityId='string',
        Alias='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The organization under which the member exists.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The alias is added to this Amazon WorkMail entity.
            

    :type Alias: string
    :param Alias: [REQUIRED]
            The alias to add to the user.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_group(OrganizationId=None, Name=None):
    """
    Creates a group that can be used in Amazon WorkMail by calling the RegisterToWorkMail operation.
    See also: AWS API Documentation
    
    
    :example: response = client.create_group(
        OrganizationId='string',
        Name='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The organization under which the group is to be created.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the group.
            

    :rtype: dict
    :return: {
        'GroupId': 'string'
    }
    
    
    """
    pass

def create_resource(OrganizationId=None, Name=None, Type=None):
    """
    Creates a new Amazon WorkMail resource. The available types are equipment and room.
    See also: AWS API Documentation
    
    
    :example: response = client.create_resource(
        OrganizationId='string',
        Name='string',
        Type='ROOM'|'EQUIPMENT'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier associated with the organization for which the resource is created.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name of the created resource.
            

    :type Type: string
    :param Type: [REQUIRED]
            The type of the created resource.
            

    :rtype: dict
    :return: {
        'ResourceId': 'string'
    }
    
    
    """
    pass

def create_user(OrganizationId=None, Name=None, DisplayName=None, Password=None):
    """
    Creates a user who can be used in Amazon WorkMail by calling the RegisterToWorkMail operation.
    See also: AWS API Documentation
    
    
    :example: response = client.create_user(
        OrganizationId='string',
        Name='string',
        DisplayName='string',
        Password='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier of the organization for which the user is created.
            

    :type Name: string
    :param Name: [REQUIRED]
            The name for the user to be created.
            

    :type DisplayName: string
    :param DisplayName: [REQUIRED]
            The display name for the user to be created.
            

    :type Password: string
    :param Password: [REQUIRED]
            The password for the user to be created.
            

    :rtype: dict
    :return: {
        'UserId': 'string'
    }
    
    
    """
    pass

def delete_alias(OrganizationId=None, EntityId=None, Alias=None):
    """
    Remove the alias from a set of aliases for a given user.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_alias(
        OrganizationId='string',
        EntityId='string',
        Alias='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the user exists.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The identifier for the Amazon WorkMail entity to have the aliases removed.
            

    :type Alias: string
    :param Alias: [REQUIRED]
            The aliases to be removed from the user's set of aliases. Duplicate entries in the list are collapsed into single entries (the list is transformed into a set).
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_group(OrganizationId=None, GroupId=None):
    """
    Deletes a group from Amazon WorkMail.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_group(
        OrganizationId='string',
        GroupId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The organization that contains the group.
            

    :type GroupId: string
    :param GroupId: [REQUIRED]
            The identifier of the group to be deleted.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_mailbox_permissions(OrganizationId=None, EntityId=None, GranteeId=None):
    """
    Deletes permissions granted to a user or group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_mailbox_permissions(
        OrganizationId='string',
        EntityId='string',
        GranteeId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier of the organization under which the entity (user or group) exists.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The identifier of the entity (user or group) for which to delete mailbox permissions.
            

    :type GranteeId: string
    :param GranteeId: [REQUIRED]
            The identifier of the entity (user or group) for which to delete granted permissions.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_resource(OrganizationId=None, ResourceId=None):
    """
    Deletes the specified resource.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_resource(
        OrganizationId='string',
        ResourceId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier associated with the organization for which the resource is deleted.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the resource to be deleted.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_user(OrganizationId=None, UserId=None):
    """
    Deletes a user from Amazon WorkMail and all subsequent systems. The action can't be undone. The mailbox is kept as-is for a minimum of 30 days, without any means to restore it.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_user(
        OrganizationId='string',
        UserId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The organization that contains the user.
            

    :type UserId: string
    :param UserId: [REQUIRED]
            The identifier of the user to be deleted.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def deregister_from_work_mail(OrganizationId=None, EntityId=None):
    """
    Mark a user, group, or resource as no longer used in Amazon WorkMail. This action disassociates the mailbox and schedules it for clean-up. Amazon WorkMail keeps mailboxes for 30 days before they are permanently removed. The functionality in the console is Disable .
    See also: AWS API Documentation
    
    
    :example: response = client.deregister_from_work_mail(
        OrganizationId='string',
        EntityId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the Amazon WorkMail entity exists.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The identifier for the entity to be updated.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_group(OrganizationId=None, GroupId=None):
    """
    Returns the data available for the group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_group(
        OrganizationId='string',
        GroupId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the group exists.
            

    :type GroupId: string
    :param GroupId: [REQUIRED]
            The identifier for the group to be described.
            

    :rtype: dict
    :return: {
        'GroupId': 'string',
        'Name': 'string',
        'Email': 'string',
        'State': 'ENABLED'|'DISABLED'|'DELETED',
        'EnabledDate': datetime(2015, 1, 1),
        'DisabledDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_organization(OrganizationId=None):
    """
    Provides more information regarding a given organization based on its identifier.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_organization(
        OrganizationId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization to be described.
            

    :rtype: dict
    :return: {
        'OrganizationId': 'string',
        'Alias': 'string',
        'State': 'string',
        'DirectoryId': 'string',
        'DirectoryType': 'string',
        'DefaultMailDomain': 'string',
        'CompletedDate': datetime(2015, 1, 1),
        'ErrorMessage': 'string'
    }
    
    
    """
    pass

def describe_resource(OrganizationId=None, ResourceId=None):
    """
    Returns the data available for the resource.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_resource(
        OrganizationId='string',
        ResourceId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier associated with the organization for which the resource is described.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the resource to be described.
            

    :rtype: dict
    :return: {
        'ResourceId': 'string',
        'Email': 'string',
        'Name': 'string',
        'Type': 'ROOM'|'EQUIPMENT',
        'BookingOptions': {
            'AutoAcceptRequests': True|False,
            'AutoDeclineRecurringRequests': True|False,
            'AutoDeclineConflictingRequests': True|False
        },
        'State': 'ENABLED'|'DISABLED'|'DELETED',
        'EnabledDate': datetime(2015, 1, 1),
        'DisabledDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_user(OrganizationId=None, UserId=None):
    """
    Provides information regarding the user.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_user(
        OrganizationId='string',
        UserId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the user exists.
            

    :type UserId: string
    :param UserId: [REQUIRED]
            The identifier for the user to be described.
            

    :rtype: dict
    :return: {
        'UserId': 'string',
        'Name': 'string',
        'Email': 'string',
        'DisplayName': 'string',
        'State': 'ENABLED'|'DISABLED'|'DELETED',
        'UserRole': 'USER'|'RESOURCE'|'SYSTEM_USER',
        'EnabledDate': datetime(2015, 1, 1),
        'DisabledDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def disassociate_delegate_from_resource(OrganizationId=None, ResourceId=None, EntityId=None):
    """
    Removes a member from the resource's set of delegates.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_delegate_from_resource(
        OrganizationId='string',
        ResourceId='string',
        EntityId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the resource exists.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the resource from which delegates' set members are removed.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The identifier for the member (user, group) to be removed from the resource's delegates.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def disassociate_member_from_group(OrganizationId=None, GroupId=None, MemberId=None):
    """
    Removes a member from a group.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_member_from_group(
        OrganizationId='string',
        GroupId='string',
        MemberId='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the group exists.
            

    :type GroupId: string
    :param GroupId: [REQUIRED]
            The identifier for the group from which members are removed.
            

    :type MemberId: string
    :param MemberId: [REQUIRED]
            The identifier for the member to be removed to the group.
            

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

def list_aliases(OrganizationId=None, EntityId=None, NextToken=None, MaxResults=None):
    """
    Creates a paginated call to list the aliases associated with a given entity.
    See also: AWS API Documentation
    
    
    :example: response = client.list_aliases(
        OrganizationId='string',
        EntityId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the entity exists.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The identifier for the entity for which to list the aliases.
            

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results. The first call does not contain any tokens.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict
    :return: {
        'Aliases': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_group_members(OrganizationId=None, GroupId=None, NextToken=None, MaxResults=None):
    """
    Returns an overview of the members of a group.
    See also: AWS API Documentation
    
    
    :example: response = client.list_group_members(
        OrganizationId='string',
        GroupId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the group exists.
            

    :type GroupId: string
    :param GroupId: [REQUIRED]
            The identifier for the group to which the members are associated.
            

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results. The first call does not contain any tokens.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict
    :return: {
        'Members': [
            {
                'Id': 'string',
                'Name': 'string',
                'Type': 'GROUP'|'USER',
                'State': 'ENABLED'|'DISABLED'|'DELETED',
                'EnabledDate': datetime(2015, 1, 1),
                'DisabledDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_groups(OrganizationId=None, NextToken=None, MaxResults=None):
    """
    Returns summaries of the organization's groups.
    See also: AWS API Documentation
    
    
    :example: response = client.list_groups(
        OrganizationId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the groups exist.
            

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results. The first call does not contain any tokens.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict
    :return: {
        'Groups': [
            {
                'Id': 'string',
                'Email': 'string',
                'Name': 'string',
                'State': 'ENABLED'|'DISABLED'|'DELETED',
                'EnabledDate': datetime(2015, 1, 1),
                'DisabledDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_mailbox_permissions(OrganizationId=None, EntityId=None, NextToken=None, MaxResults=None):
    """
    Lists the mailbox permissions associated with a mailbox.
    See also: AWS API Documentation
    
    
    :example: response = client.list_mailbox_permissions(
        OrganizationId='string',
        EntityId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier of the organization under which the entity (user or group) exists.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The identifier of the entity (user or group) for which to list mailbox permissions.
            

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results. The first call does not contain any tokens.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict
    :return: {
        'Permissions': [
            {
                'GranteeId': 'string',
                'GranteeType': 'GROUP'|'USER',
                'PermissionValues': [
                    'FULL_ACCESS'|'SEND_AS'|'SEND_ON_BEHALF',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_organizations(NextToken=None, MaxResults=None):
    """
    Returns summaries of the customer's non-deleted organizations.
    See also: AWS API Documentation
    
    
    :example: response = client.list_organizations(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results. The first call does not contain any tokens.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict
    :return: {
        'OrganizationSummaries': [
            {
                'OrganizationId': 'string',
                'Alias': 'string',
                'ErrorMessage': 'string',
                'State': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_resource_delegates(OrganizationId=None, ResourceId=None, NextToken=None, MaxResults=None):
    """
    Lists the delegates associated with a resource. Users and groups can be resource delegates and answer requests on behalf of the resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resource_delegates(
        OrganizationId='string',
        ResourceId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization that contains the resource for which delegates are listed.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier for the resource whose delegates are listed.
            

    :type NextToken: string
    :param NextToken: The token used to paginate through the delegates associated with a resource.

    :type MaxResults: integer
    :param MaxResults: The number of maximum results in a page.

    :rtype: dict
    :return: {
        'Delegates': [
            {
                'Id': 'string',
                'Type': 'GROUP'|'USER'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_resources(OrganizationId=None, NextToken=None, MaxResults=None):
    """
    Returns summaries of the organization's resources.
    See also: AWS API Documentation
    
    
    :example: response = client.list_resources(
        OrganizationId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the resources exist.
            

    :type NextToken: string
    :param NextToken: The token to use to retrieve the next page of results. The first call does not contain any tokens.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict
    :return: {
        'Resources': [
            {
                'Id': 'string',
                'Email': 'string',
                'Name': 'string',
                'Type': 'ROOM'|'EQUIPMENT',
                'State': 'ENABLED'|'DISABLED'|'DELETED',
                'EnabledDate': datetime(2015, 1, 1),
                'DisabledDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_users(OrganizationId=None, NextToken=None, MaxResults=None):
    """
    Returns summaries of the organization's users.
    See also: AWS API Documentation
    
    
    :example: response = client.list_users(
        OrganizationId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the users exist.
            

    :type NextToken: string
    :param NextToken: TBD

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call.

    :rtype: dict
    :return: {
        'Users': [
            {
                'Id': 'string',
                'Email': 'string',
                'Name': 'string',
                'DisplayName': 'string',
                'State': 'ENABLED'|'DISABLED'|'DELETED',
                'UserRole': 'USER'|'RESOURCE'|'SYSTEM_USER',
                'EnabledDate': datetime(2015, 1, 1),
                'DisabledDate': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def put_mailbox_permissions(OrganizationId=None, EntityId=None, GranteeId=None, PermissionValues=None):
    """
    Sets permissions for a user or group. This replaces any pre-existing permissions set for the entity.
    See also: AWS API Documentation
    
    
    :example: response = client.put_mailbox_permissions(
        OrganizationId='string',
        EntityId='string',
        GranteeId='string',
        PermissionValues=[
            'FULL_ACCESS'|'SEND_AS'|'SEND_ON_BEHALF',
        ]
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier of the organization under which the entity (user or group) exists.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The identifier of the entity (user or group) for which to update mailbox permissions.
            

    :type GranteeId: string
    :param GranteeId: [REQUIRED]
            The identifier of the entity (user or group) to which to grant the permissions.
            

    :type PermissionValues: list
    :param PermissionValues: [REQUIRED]
            The permissions granted to the grantee. SEND_AS allows the grantee to send email as the owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF allows the grantee to send email on behalf of the owner of the mailbox (the grantee is not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee full access to the mailbox, irrespective of other folder-level permissions set on the mailbox.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def register_to_work_mail(OrganizationId=None, EntityId=None, Email=None):
    """
    Registers an existing and disabled user, group, or resource/entity for Amazon WorkMail use by associating a mailbox and calendaring capabilities. It performs no change if the entity is enabled and fails if the entity is deleted. This operation results in the accumulation of costs. For more information, see Pricing . The equivalent console functionality for this operation is Enable . Users can either be created by calling the CreateUser API or they can be synchronized from your directory. For more information, see DeregisterFromWorkMail.
    See also: AWS API Documentation
    
    
    :example: response = client.register_to_work_mail(
        OrganizationId='string',
        EntityId='string',
        Email='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier for the organization under which the Amazon WorkMail entity exists.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The identifier for the entity to be updated.
            

    :type Email: string
    :param Email: [REQUIRED]
            The email for the entity to be updated.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def reset_password(OrganizationId=None, UserId=None, Password=None):
    """
    Allows the administrator to reset the password for a user.
    See also: AWS API Documentation
    
    
    :example: response = client.reset_password(
        OrganizationId='string',
        UserId='string',
        Password='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier of the organization that contains the user for which the password is reset.
            

    :type UserId: string
    :param UserId: [REQUIRED]
            The identifier of the user for whom the password is reset.
            

    :type Password: string
    :param Password: [REQUIRED]
            The new password for the user.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_primary_email_address(OrganizationId=None, EntityId=None, Email=None):
    """
    Updates the primary email for an entity. The current email is moved into the list of aliases (or swapped between an existing alias and the current primary email) and the email provided in the input is promoted as the primary.
    See also: AWS API Documentation
    
    
    :example: response = client.update_primary_email_address(
        OrganizationId='string',
        EntityId='string',
        Email='string'
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The organization that contains the entity to update.
            

    :type EntityId: string
    :param EntityId: [REQUIRED]
            The entity to update (user, group, or resource).
            

    :type Email: string
    :param Email: [REQUIRED]
            The value of the email to be updated as primary.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_resource(OrganizationId=None, ResourceId=None, Name=None, BookingOptions=None):
    """
    Updates data for the resource. It must be preceded by a describe call in order to have the latest information. The dataset in the request should be the one expected when performing another describe call.
    See also: AWS API Documentation
    
    
    :example: response = client.update_resource(
        OrganizationId='string',
        ResourceId='string',
        Name='string',
        BookingOptions={
            'AutoAcceptRequests': True|False,
            'AutoDeclineRecurringRequests': True|False,
            'AutoDeclineConflictingRequests': True|False
        }
    )
    
    
    :type OrganizationId: string
    :param OrganizationId: [REQUIRED]
            The identifier associated with the organization for which the resource is updated.
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The identifier of the resource to be updated.
            

    :type Name: string
    :param Name: The name of the resource to be updated.

    :type BookingOptions: dict
    :param BookingOptions: The resource's booking options to be updated.
            AutoAcceptRequests (boolean) --The resource's ability to automatically reply to requests. If disabled, delegates must be associated to the resource.
            AutoDeclineRecurringRequests (boolean) --The resource's ability to automatically decline any recurring requests.
            AutoDeclineConflictingRequests (boolean) --The resource's ability to automatically decline any conflicting requests.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

