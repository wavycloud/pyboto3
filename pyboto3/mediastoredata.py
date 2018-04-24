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

def delete_object(Path=None):
    """
    Deletes an object at the specified path.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_object(
        Path='string'
    )
    
    
    :type Path: string
    :param Path: [REQUIRED]
            The path (including the file name) where the object is stored in the container. Format: folder name/folder name/file name
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_object(Path=None):
    """
    Gets the headers for an object at the specified path.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_object(
        Path='string'
    )
    
    
    :type Path: string
    :param Path: [REQUIRED]
            The path (including the file name) where the object is stored in the container. Format: folder name/folder name/file name
            

    :rtype: dict
    :return: {
        'ETag': 'string',
        'ContentType': 'string',
        'ContentLength': 123,
        'CacheControl': 'string',
        'LastModified': datetime(2015, 1, 1)
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

def get_object(Path=None, Range=None):
    """
    Downloads the object at the specified path.
    See also: AWS API Documentation
    
    
    :example: response = client.get_object(
        Path='string',
        Range='string'
    )
    
    
    :type Path: string
    :param Path: [REQUIRED]
            The path (including the file name) where the object is stored in the container. Format: folder name/folder name/file name
            For example, to upload the file mlaw.avi to the folder path premium\canada in the container movies , enter the path premium/canada/mlaw.avi .
            Do not include the container name in this path.
            If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing premium/usa subfolder. If you specify premium/canada , the service creates a canada subfolder in the premium folder. You then have two subfolders, usa and canada , in the premium folder.
            There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.
            For more information about folders and how they exist in a container, see the AWS Elemental MediaStore User Guide .
            The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension.
            

    :type Range: string
    :param Range: The range bytes of an object to retrieve. For more information about the Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35 .

    :rtype: dict
    :return: {
        'Body': StreamingBody(),
        'CacheControl': 'string',
        'ContentRange': 'string',
        'ContentLength': 123,
        'ContentType': 'string',
        'ETag': 'string',
        'LastModified': datetime(2015, 1, 1),
        'StatusCode': 123
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

def list_items(Path=None, MaxResults=None, NextToken=None):
    """
    Provides a list of metadata entries about folders and objects in the specified folder.
    See also: AWS API Documentation
    
    
    :example: response = client.list_items(
        Path='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Path: string
    :param Path: The path in the container from which to retrieve items. Format: folder name/folder name/file name

    :type MaxResults: integer
    :param MaxResults: The maximum results to return. The service might return fewer results.

    :type NextToken: string
    :param NextToken: The NextToken received in the ListItemsResponse for the same container and path. Tokens expire after 15 minutes.

    :rtype: dict
    :return: {
        'Items': [
            {
                'Name': 'string',
                'Type': 'OBJECT'|'FOLDER',
                'ETag': 'string',
                'LastModified': datetime(2015, 1, 1),
                'ContentType': 'string',
                'ContentLength': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def put_object(Body=None, Path=None, ContentType=None, CacheControl=None, StorageClass=None):
    """
    Uploads an object to the specified path. Object sizes are limited to 10 MB.
    See also: AWS API Documentation
    
    
    :example: response = client.put_object(
        Body=b'bytes'|file,
        Path='string',
        ContentType='string',
        CacheControl='string',
        StorageClass='TEMPORAL'
    )
    
    
    :type Body: bytes or seekable file-like object
    :param Body: [REQUIRED]
            The bytes to be stored.
            

    :type Path: string
    :param Path: [REQUIRED]
            The path (including the file name) where the object is stored in the container. Format: folder name/folder name/file name
            For example, to upload the file mlaw.avi to the folder path premium\canada in the container movies , enter the path premium/canada/mlaw.avi .
            Do not include the container name in this path.
            If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing premium/usa subfolder. If you specify premium/canada , the service creates a canada subfolder in the premium folder. You then have two subfolders, usa and canada , in the premium folder.
            There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.
            For more information about folders and how they exist in a container, see the AWS Elemental MediaStore User Guide .
            The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension.
            

    :type ContentType: string
    :param ContentType: The content type of the object.

    :type CacheControl: string
    :param CacheControl: An optional CacheControl header that allows the caller to control the object's cache behavior. Headers can be passed in as specified in the HTTP at https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 .
            Headers with a custom user-defined value are also accepted.
            

    :type StorageClass: string
    :param StorageClass: Indicates the storage class of a Put request. Defaults to high-performance temporal storage class, and objects are persisted into durable storage shortly after being received.

    :rtype: dict
    :return: {
        'ContentSHA256': 'string',
        'ETag': 'string',
        'StorageClass': 'TEMPORAL'
    }
    
    
    """
    pass

