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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def create_project(name=None, region=None, contents=None, snapshotId=None):
    """
    Creates an AWS Mobile Hub project.
    See also: AWS API Documentation
    
    
    :example: response = client.create_project(
        name='string',
        region='string',
        contents=b'bytes'|file,
        snapshotId='string'
    )
    
    
    :type name: string
    :param name: Name of the project.

    :type region: string
    :param region: Default region where project resources should be created.

    :type contents: bytes or seekable file-like object
    :param contents: ZIP or YAML file which contains configuration settings to be used when creating the project. This may be the contents of the file downloaded from the URL provided in an export project operation.

    :type snapshotId: string
    :param snapshotId: Unique identifier for an exported snapshot of project configuration. This snapshot identifier is included in the share URL when a project is exported.

    :rtype: dict
    :return: {
        'details': {
            'name': 'string',
            'projectId': 'string',
            'region': 'string',
            'state': 'NORMAL'|'SYNCING'|'IMPORTING',
            'createdDate': datetime(2015, 1, 1),
            'lastUpdatedDate': datetime(2015, 1, 1),
            'consoleUrl': 'string',
            'resources': [
                {
                    'type': 'string',
                    'name': 'string',
                    'arn': 'string',
                    'feature': 'string',
                    'attributes': {
                        'string': 'string'
                    }
                },
            ]
        }
    }
    
    
    """
    pass

def delete_project(projectId=None):
    """
    Delets a project in AWS Mobile Hub.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_project(
        projectId='string'
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]
            Unique project identifier.
            

    :rtype: dict
    :return: {
        'deletedResources': [
            {
                'type': 'string',
                'name': 'string',
                'arn': 'string',
                'feature': 'string',
                'attributes': {
                    'string': 'string'
                }
            },
        ],
        'orphanedResources': [
            {
                'type': 'string',
                'name': 'string',
                'arn': 'string',
                'feature': 'string',
                'attributes': {
                    'string': 'string'
                }
            },
        ]
    }
    
    
    """
    pass

def describe_bundle(bundleId=None):
    """
    Get the bundle details for the requested bundle id.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_bundle(
        bundleId='string'
    )
    
    
    :type bundleId: string
    :param bundleId: [REQUIRED]
            Unique bundle identifier.
            

    :rtype: dict
    :return: {
        'details': {
            'bundleId': 'string',
            'title': 'string',
            'version': 'string',
            'description': 'string',
            'iconUrl': 'string',
            'availablePlatforms': [
                'OSX'|'WINDOWS'|'LINUX'|'OBJC'|'SWIFT'|'ANDROID'|'JAVASCRIPT',
            ]
        }
    }
    
    
    """
    pass

def describe_project(projectId=None, syncFromResources=None):
    """
    Gets details about a project in AWS Mobile Hub.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_project(
        projectId='string',
        syncFromResources=True|False
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]
            Unique project identifier.
            

    :type syncFromResources: boolean
    :param syncFromResources: If set to true, causes AWS Mobile Hub to synchronize information from other services, e.g., update state of AWS CloudFormation stacks in the AWS Mobile Hub project.

    :rtype: dict
    :return: {
        'details': {
            'name': 'string',
            'projectId': 'string',
            'region': 'string',
            'state': 'NORMAL'|'SYNCING'|'IMPORTING',
            'createdDate': datetime(2015, 1, 1),
            'lastUpdatedDate': datetime(2015, 1, 1),
            'consoleUrl': 'string',
            'resources': [
                {
                    'type': 'string',
                    'name': 'string',
                    'arn': 'string',
                    'feature': 'string',
                    'attributes': {
                        'string': 'string'
                    }
                },
            ]
        }
    }
    
    
    """
    pass

def export_bundle(bundleId=None, projectId=None, platform=None):
    """
    Generates customized software development kit (SDK) and or tool packages used to integrate mobile web or mobile app clients with backend AWS resources.
    See also: AWS API Documentation
    
    
    :example: response = client.export_bundle(
        bundleId='string',
        projectId='string',
        platform='OSX'|'WINDOWS'|'LINUX'|'OBJC'|'SWIFT'|'ANDROID'|'JAVASCRIPT'
    )
    
    
    :type bundleId: string
    :param bundleId: [REQUIRED]
            Unique bundle identifier.
            

    :type projectId: string
    :param projectId: Unique project identifier.

    :type platform: string
    :param platform: Developer desktop or target application platform.

    :rtype: dict
    :return: {
        'downloadUrl': 'string'
    }
    
    
    """
    pass

def export_project(projectId=None):
    """
    Exports project configuration to a snapshot which can be downloaded and shared. Note that mobile app push credentials are encrypted in exported projects, so they can only be shared successfully within the same AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.export_project(
        projectId='string'
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]
            Unique project identifier.
            

    :rtype: dict
    :return: {
        'downloadUrl': 'string',
        'shareUrl': 'string',
        'snapshotId': 'string'
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

def list_bundles(maxResults=None, nextToken=None):
    """
    List all available bundles.
    See also: AWS API Documentation
    
    
    :example: response = client.list_bundles(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing bundles from start. If non-null pagination token is returned in a result, then pass its value in here in another request to list more bundles.

    :rtype: dict
    :return: {
        'bundleList': [
            {
                'bundleId': 'string',
                'title': 'string',
                'version': 'string',
                'description': 'string',
                'iconUrl': 'string',
                'availablePlatforms': [
                    'OSX'|'WINDOWS'|'LINUX'|'OBJC'|'SWIFT'|'ANDROID'|'JAVASCRIPT',
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def list_projects(maxResults=None, nextToken=None):
    """
    Lists projects in AWS Mobile Hub.
    See also: AWS API Documentation
    
    
    :example: response = client.list_projects(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing projects from start. If non-null pagination token is returned in a result, then pass its value in here in another request to list more projects.

    :rtype: dict
    :return: {
        'projects': [
            {
                'name': 'string',
                'projectId': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    """
    pass

def update_project(contents=None, projectId=None):
    """
    Update an existing project.
    See also: AWS API Documentation
    
    
    :example: response = client.update_project(
        contents=b'bytes'|file,
        projectId='string'
    )
    
    
    :type contents: bytes or seekable file-like object
    :param contents: ZIP or YAML file which contains project configuration to be updated. This should be the contents of the file downloaded from the URL provided in an export project operation.

    :type projectId: string
    :param projectId: [REQUIRED]
            Unique project identifier.
            

    :rtype: dict
    :return: {
        'details': {
            'name': 'string',
            'projectId': 'string',
            'region': 'string',
            'state': 'NORMAL'|'SYNCING'|'IMPORTING',
            'createdDate': datetime(2015, 1, 1),
            'lastUpdatedDate': datetime(2015, 1, 1),
            'consoleUrl': 'string',
            'resources': [
                {
                    'type': 'string',
                    'name': 'string',
                    'arn': 'string',
                    'feature': 'string',
                    'attributes': {
                        'string': 'string'
                    }
                },
            ]
        }
    }
    
    
    """
    pass

