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

def delete_object(Path=None):
    """
    Deletes an object at the specified path.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_object(
        Path='string'
    )
    
    
    :type Path: string
    :param Path: [REQUIRED]\nThe path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

MediaStoreData.Client.exceptions.ContainerNotFoundException
MediaStoreData.Client.exceptions.ObjectNotFoundException
MediaStoreData.Client.exceptions.InternalServerError


    :return: {}
    
    
    :returns: 
    MediaStoreData.Client.exceptions.ContainerNotFoundException
    MediaStoreData.Client.exceptions.ObjectNotFoundException
    MediaStoreData.Client.exceptions.InternalServerError
    
    """
    pass

def describe_object(Path=None):
    """
    Gets the headers for an object at the specified path.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_object(
        Path='string'
    )
    
    
    :type Path: string
    :param Path: [REQUIRED]\nThe path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>\n

    :rtype: dict
ReturnsResponse Syntax{
    'ETag': 'string',
    'ContentType': 'string',
    'ContentLength': 123,
    'CacheControl': 'string',
    'LastModified': datetime(2015, 1, 1)
}


Response Structure

(dict) --
ETag (string) --The ETag that represents a unique instance of the object.

ContentType (string) --The content type of the object.

ContentLength (integer) --The length of the object in bytes.

CacheControl (string) --An optional CacheControl header that allows the caller to control the object\'s cache behavior. Headers can be passed in as specified in the HTTP at https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 .
Headers with a custom user-defined value are also accepted.

LastModified (datetime) --The date and time that the object was last modified.






Exceptions

MediaStoreData.Client.exceptions.ContainerNotFoundException
MediaStoreData.Client.exceptions.ObjectNotFoundException
MediaStoreData.Client.exceptions.InternalServerError


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
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_object(Path=None, Range=None):
    """
    Downloads the object at the specified path. If the object\xe2\x80\x99s upload availability is set to streaming , AWS Elemental MediaStore downloads the object even if it\xe2\x80\x99s still uploading the object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_object(
        Path='string',
        Range='string'
    )
    
    
    :type Path: string
    :param Path: [REQUIRED]\nThe path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>\nFor example, to upload the file mlaw.avi to the folder path premium\\canada in the container movies , enter the path premium/canada/mlaw.avi .\nDo not include the container name in this path.\nIf the path includes any folders that don\'t exist yet, the service creates them. For example, suppose you have an existing premium/usa subfolder. If you specify premium/canada , the service creates a canada subfolder in the premium folder. You then have two subfolders, usa and canada , in the premium folder.\nThere is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.\nFor more information about folders and how they exist in a container, see the AWS Elemental MediaStore User Guide .\nThe file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension.\n

    :type Range: string
    :param Range: The range bytes of an object to retrieve. For more information about the Range header, see http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35 . AWS Elemental MediaStore ignores this header for partially uploaded objects that have streaming upload availability.

    :rtype: dict

ReturnsResponse Syntax
{
    'Body': StreamingBody(),
    'CacheControl': 'string',
    'ContentRange': 'string',
    'ContentLength': 123,
    'ContentType': 'string',
    'ETag': 'string',
    'LastModified': datetime(2015, 1, 1),
    'StatusCode': 123
}


Response Structure

(dict) --

Body (StreamingBody) --
The bytes of the object.

CacheControl (string) --
An optional CacheControl header that allows the caller to control the object\'s cache behavior. Headers can be passed in as specified in the HTTP spec at https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 .
Headers with a custom user-defined value are also accepted.

ContentRange (string) --
The range of bytes to retrieve.

ContentLength (integer) --
The length of the object in bytes.

ContentType (string) --
The content type of the object.

ETag (string) --
The ETag that represents a unique instance of the object.

LastModified (datetime) --
The date and time that the object was last modified.

StatusCode (integer) --
The HTML status code of the request. Status codes ranging from 200 to 299 indicate success. All other status codes indicate the type of error that occurred.







Exceptions

MediaStoreData.Client.exceptions.ContainerNotFoundException
MediaStoreData.Client.exceptions.ObjectNotFoundException
MediaStoreData.Client.exceptions.RequestedRangeNotSatisfiableException
MediaStoreData.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    MediaStoreData.Client.exceptions.ContainerNotFoundException
    MediaStoreData.Client.exceptions.ObjectNotFoundException
    MediaStoreData.Client.exceptions.RequestedRangeNotSatisfiableException
    MediaStoreData.Client.exceptions.InternalServerError
    
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

def list_items(Path=None, MaxResults=None, NextToken=None):
    """
    Provides a list of metadata entries about folders and objects in the specified folder.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_items(
        Path='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Path: string
    :param Path: The path in the container from which to retrieve items. Format: <folder name>/<folder name>/<file name>

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per API request. For example, you submit a ListItems request with MaxResults set at 500. Although 2,000 items match your request, the service returns no more than the first 500 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) The service might return fewer results than the MaxResults value.\nIf MaxResults is not included in the request, the service defaults to pagination with a maximum of 1,000 results per page.\n

    :type NextToken: string
    :param NextToken: The token that identifies which batch of results that you want to see. For example, you submit a ListItems request with MaxResults set at 500. The service returns the first batch of results (up to 500) and a NextToken value. To see the next batch of results, you can submit the ListItems request a second time and specify the NextToken value.\nTokens expire after 15 minutes.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Items (list) --
The metadata entries for the folders and objects at the requested path.

(dict) --
A metadata entry for a folder or object.

Name (string) --
The name of the item.

Type (string) --
The item type (folder or object).

ETag (string) --
The ETag that represents a unique instance of the item.

LastModified (datetime) --
The date and time that the item was last modified.

ContentType (string) --
The content type of the item.

ContentLength (integer) --
The length of the item in bytes.





NextToken (string) --
The token that can be used in a request to view the next set of results. For example, you submit a ListItems request that matches 2,000 items with MaxResults set at 500. The service returns the first batch of results (up to 500) and a NextToken value that can be used to fetch the next batch of results.







Exceptions

MediaStoreData.Client.exceptions.ContainerNotFoundException
MediaStoreData.Client.exceptions.InternalServerError


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
    
    
    :returns: 
    MediaStoreData.Client.exceptions.ContainerNotFoundException
    MediaStoreData.Client.exceptions.InternalServerError
    
    """
    pass

def put_object(Body=None, Path=None, ContentType=None, CacheControl=None, StorageClass=None, UploadAvailability=None):
    """
    Uploads an object to the specified path. Object sizes are limited to 25 MB for standard upload availability and 10 MB for streaming upload availability.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_object(
        Body=b'bytes'|file,
        Path='string',
        ContentType='string',
        CacheControl='string',
        StorageClass='TEMPORAL',
        UploadAvailability='STANDARD'|'STREAMING'
    )
    
    
    :type Body: bytes or seekable file-like object
    :param Body: [REQUIRED]\nThe bytes to be stored.\n

    :type Path: string
    :param Path: [REQUIRED]\nThe path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>\nFor example, to upload the file mlaw.avi to the folder path premium\\canada in the container movies , enter the path premium/canada/mlaw.avi .\nDo not include the container name in this path.\nIf the path includes any folders that don\'t exist yet, the service creates them. For example, suppose you have an existing premium/usa subfolder. If you specify premium/canada , the service creates a canada subfolder in the premium folder. You then have two subfolders, usa and canada , in the premium folder.\nThere is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.\nFor more information about folders and how they exist in a container, see the AWS Elemental MediaStore User Guide .\nThe file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension.\n

    :type ContentType: string
    :param ContentType: The content type of the object.

    :type CacheControl: string
    :param CacheControl: An optional CacheControl header that allows the caller to control the object\'s cache behavior. Headers can be passed in as specified in the HTTP at https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 .\nHeaders with a custom user-defined value are also accepted.\n

    :type StorageClass: string
    :param StorageClass: Indicates the storage class of a Put request. Defaults to high-performance temporal storage class, and objects are persisted into durable storage shortly after being received.

    :type UploadAvailability: string
    :param UploadAvailability: Indicates the availability of an object while it is still uploading. If the value is set to streaming , the object is available for downloading after some initial buffering but before the object is uploaded completely. If the value is set to standard , the object is available for downloading only when it is uploaded completely. The default value for this header is standard .\nTo use this header, you must also set the HTTP Transfer-Encoding header to chunked .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ContentSHA256': 'string',
    'ETag': 'string',
    'StorageClass': 'TEMPORAL'
}


Response Structure

(dict) --

ContentSHA256 (string) --
The SHA256 digest of the object that is persisted.

ETag (string) --
Unique identifier of the object in the container.

StorageClass (string) --
The storage class where the object was persisted. The class should be \xe2\x80\x9cTemporal\xe2\x80\x9d.







Exceptions

MediaStoreData.Client.exceptions.ContainerNotFoundException
MediaStoreData.Client.exceptions.InternalServerError


    :return: {
        'ContentSHA256': 'string',
        'ETag': 'string',
        'StorageClass': 'TEMPORAL'
    }
    
    
    :returns: 
    MediaStoreData.Client.exceptions.ContainerNotFoundException
    MediaStoreData.Client.exceptions.InternalServerError
    
    """
    pass

