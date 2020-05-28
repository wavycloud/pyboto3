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

def get_snapshot_block(SnapshotId=None, BlockIndex=None, BlockToken=None):
    """
    Returns the data in a block in an Amazon Elastic Block Store snapshot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_snapshot_block(
        SnapshotId='string',
        BlockIndex=123,
        BlockToken='string'
    )
    
    
    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]\nThe ID of the snapshot containing the block from which to get data.\n

    :type BlockIndex: integer
    :param BlockIndex: [REQUIRED]\nThe block index of the block from which to get data.\nObtain the BlockIndex by running the ListChangedBlocks or ListSnapshotBlocks operations.\n

    :type BlockToken: string
    :param BlockToken: [REQUIRED]\nThe block token of the block from which to get data.\nObtain the BlockToken by running the ListChangedBlocks or ListSnapshotBlocks operations.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DataLength': 123,
    'BlockData': StreamingBody(),
    'Checksum': 'string',
    'ChecksumAlgorithm': 'SHA256'
}


Response Structure

(dict) --

DataLength (integer) --
The size of the data in the block.

BlockData (StreamingBody) --
The data content of the block.

Checksum (string) --
The checksum generated for the block, which is Base64 encoded.

ChecksumAlgorithm (string) --
The algorithm used to generate the checksum for the block, such as SHA256.







Exceptions

EBS.Client.exceptions.ValidationException
EBS.Client.exceptions.ResourceNotFoundException


    :return: {
        'DataLength': 123,
        'BlockData': StreamingBody(),
        'Checksum': 'string',
        'ChecksumAlgorithm': 'SHA256'
    }
    
    
    :returns: 
    EBS.Client.exceptions.ValidationException
    EBS.Client.exceptions.ResourceNotFoundException
    
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

def list_changed_blocks(FirstSnapshotId=None, SecondSnapshotId=None, NextToken=None, MaxResults=None, StartingBlockIndex=None):
    """
    Returns the block indexes and block tokens for blocks that are different between two Amazon Elastic Block Store snapshots of the same volume/snapshot lineage.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_changed_blocks(
        FirstSnapshotId='string',
        SecondSnapshotId='string',
        NextToken='string',
        MaxResults=123,
        StartingBlockIndex=123
    )
    
    
    :type FirstSnapshotId: string
    :param FirstSnapshotId: The ID of the first snapshot to use for the comparison.\n\nWarning\nThe FirstSnapshotID parameter must be specified with a SecondSnapshotId parameter; otherwise, an error occurs.\n\n

    :type SecondSnapshotId: string
    :param SecondSnapshotId: [REQUIRED]\nThe ID of the second snapshot to use for the comparison.\n\nWarning\nThe SecondSnapshotId parameter must be specified with a FirstSnapshotID parameter; otherwise, an error occurs.\n\n

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :type MaxResults: integer
    :param MaxResults: The number of results to return.

    :type StartingBlockIndex: integer
    :param StartingBlockIndex: The block index from which the comparison should start.\nThe list in the response will start from this block index or the next valid block index in the snapshots.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ChangedBlocks': [
        {
            'BlockIndex': 123,
            'FirstBlockToken': 'string',
            'SecondBlockToken': 'string'
        },
    ],
    'ExpiryTime': datetime(2015, 1, 1),
    'VolumeSize': 123,
    'BlockSize': 123,
    'NextToken': 'string'
}


Response Structure

(dict) --

ChangedBlocks (list) --
An array of objects containing information about the changed blocks.

(dict) --
A block of data in an Amazon Elastic Block Store snapshot that is different from another snapshot of the same volume/snapshot lineage.

BlockIndex (integer) --
The block index.

FirstBlockToken (string) --
The block token for the block index of the FirstSnapshotId specified in the ListChangedBlocks operation. This value is absent if the first snapshot does not have the changed block that is on the second snapshot.

SecondBlockToken (string) --
The block token for the block index of the SecondSnapshotId specified in the ListChangedBlocks operation.





ExpiryTime (datetime) --
The time when the BlockToken expires.

VolumeSize (integer) --
The size of the volume in GB.

BlockSize (integer) --
The size of the block.

NextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

EBS.Client.exceptions.ValidationException
EBS.Client.exceptions.ResourceNotFoundException


    :return: {
        'ChangedBlocks': [
            {
                'BlockIndex': 123,
                'FirstBlockToken': 'string',
                'SecondBlockToken': 'string'
            },
        ],
        'ExpiryTime': datetime(2015, 1, 1),
        'VolumeSize': 123,
        'BlockSize': 123,
        'NextToken': 'string'
    }
    
    
    :returns: 
    EBS.Client.exceptions.ValidationException
    EBS.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_snapshot_blocks(SnapshotId=None, NextToken=None, MaxResults=None, StartingBlockIndex=None):
    """
    Returns the block indexes and block tokens for blocks in an Amazon Elastic Block Store snapshot.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_snapshot_blocks(
        SnapshotId='string',
        NextToken='string',
        MaxResults=123,
        StartingBlockIndex=123
    )
    
    
    :type SnapshotId: string
    :param SnapshotId: [REQUIRED]\nThe ID of the snapshot from which to get block indexes and block tokens.\n

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :type MaxResults: integer
    :param MaxResults: The number of results to return.

    :type StartingBlockIndex: integer
    :param StartingBlockIndex: The block index from which the list should start. The list in the response will start from this block index or the next valid block index in the snapshot.

    :rtype: dict

ReturnsResponse Syntax
{
    'Blocks': [
        {
            'BlockIndex': 123,
            'BlockToken': 'string'
        },
    ],
    'ExpiryTime': datetime(2015, 1, 1),
    'VolumeSize': 123,
    'BlockSize': 123,
    'NextToken': 'string'
}


Response Structure

(dict) --

Blocks (list) --
An array of objects containing information about the blocks.

(dict) --
A block of data in an Amazon Elastic Block Store snapshot.

BlockIndex (integer) --
The block index.

BlockToken (string) --
The block token for the block index.





ExpiryTime (datetime) --
The time when the BlockToken expires.

VolumeSize (integer) --
The size of the volume in GB.

BlockSize (integer) --
The size of the block.

NextToken (string) --
The token to use to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

EBS.Client.exceptions.ValidationException
EBS.Client.exceptions.ResourceNotFoundException


    :return: {
        'Blocks': [
            {
                'BlockIndex': 123,
                'BlockToken': 'string'
            },
        ],
        'ExpiryTime': datetime(2015, 1, 1),
        'VolumeSize': 123,
        'BlockSize': 123,
        'NextToken': 'string'
    }
    
    
    :returns: 
    EBS.Client.exceptions.ValidationException
    EBS.Client.exceptions.ResourceNotFoundException
    
    """
    pass

