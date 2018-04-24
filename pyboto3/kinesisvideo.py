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

def create_stream(DeviceName=None, StreamName=None, MediaType=None, KmsKeyId=None, DataRetentionInHours=None):
    """
    Creates a new Kinesis video stream.
    When you create a new stream, Kinesis Video Streams assigns it a version number. When you change the stream's metadata, Kinesis Video Streams updates the version.
    For information about how the service works, see How it Works .
    You must have permissions for the KinesisVideo:CreateStream action.
    See also: AWS API Documentation
    
    
    :example: response = client.create_stream(
        DeviceName='string',
        StreamName='string',
        MediaType='string',
        KmsKeyId='string',
        DataRetentionInHours=123
    )
    
    
    :type DeviceName: string
    :param DeviceName: The name of the device that is writing to the stream.
            Note
            In the current implementation, Kinesis Video Streams does not use this name.
            

    :type StreamName: string
    :param StreamName: [REQUIRED]
            A name for the stream that you are creating.
            The stream name is an identifier for the stream, and must be unique for each account and region.
            

    :type MediaType: string
    :param MediaType: The media type of the stream. Consumers of the stream can use this information when processing the stream. For more information about media types, see Media Types . If you choose to specify the MediaType , see Naming Requirements for guidelines.
            To play video on the console, the media must be H.264 encoded, and you need to specify this video type in this parameter as video/h264 .
            This parameter is optional; the default value is null (or empty in JSON).
            

    :type KmsKeyId: string
    :param KmsKeyId: The ID of the AWS Key Management Service (AWS KMS) key that you want Kinesis Video Streams to use to encrypt stream data.
            If no key ID is specified, the default, Kinesis Video-managed key (aws/kinesisvideo ) is used.
            For more information, see DescribeKey .
            

    :type DataRetentionInHours: integer
    :param DataRetentionInHours: The number of hours that you want to retain the data in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.
            The default value is 0, indicating that the stream does not persist data.
            

    :rtype: dict
    :return: {
        'StreamARN': 'string'
    }
    
    
    """
    pass

def delete_stream(StreamARN=None, CurrentVersion=None):
    """
    Deletes a Kinesis video stream and the data contained in the stream.
    This method marks the stream for deletion, and makes the data in the stream inaccessible immediately.
    To ensure that you have the latest version of the stream before deleting it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the DescribeStream API.
    This operation requires permission for the KinesisVideo:DeleteStream action.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_stream(
        StreamARN='string',
        CurrentVersion='string'
    )
    
    
    :type StreamARN: string
    :param StreamARN: [REQUIRED]
            The Amazon Resource Name (ARN) of the stream that you want to delete.
            

    :type CurrentVersion: string
    :param CurrentVersion: Optional: The version of the stream that you want to delete.
            Specify the version as a safeguard to ensure that your are deleting the correct stream. To get the stream version, use the DescribeStream API.
            If not specified, only the CreationTime is checked before deleting the stream.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_stream(StreamName=None, StreamARN=None):
    """
    Returns the most current information about the specified stream. You must specify either the StreamName or the StreamARN .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stream(
        StreamName='string',
        StreamARN='string'
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream.

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream.

    :rtype: dict
    :return: {
        'StreamInfo': {
            'DeviceName': 'string',
            'StreamName': 'string',
            'StreamARN': 'string',
            'MediaType': 'string',
            'KmsKeyId': 'string',
            'Version': 'string',
            'Status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
            'CreationTime': datetime(2015, 1, 1),
            'DataRetentionInHours': 123
        }
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

def get_data_endpoint(StreamName=None, StreamARN=None, APIName=None):
    """
    Gets an endpoint for a specified stream for either reading or writing. Use this endpoint in your application to read from the specified stream (using the GetMedia or GetMediaForFragmentList operations) or write to it (using the PutMedia operation).
    In the request, specify the stream either by StreamName or StreamARN .
    See also: AWS API Documentation
    
    
    :example: response = client.get_data_endpoint(
        StreamName='string',
        StreamARN='string',
        APIName='PUT_MEDIA'|'GET_MEDIA'|'LIST_FRAGMENTS'|'GET_MEDIA_FOR_FRAGMENT_LIST'
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream that you want to get the endpoint for. You must specify either this parameter or a StreamARN in the request.

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream that you want to get the endpoint for. You must specify either this parameter or a StreamName in the request.

    :type APIName: string
    :param APIName: [REQUIRED]
            The name of the API action for which to get an endpoint.
            

    :rtype: dict
    :return: {
        'DataEndpoint': 'string'
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

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_streams(MaxResults=None, NextToken=None, StreamNameCondition=None):
    """
    Returns an array of StreamInfo objects. Each object describes a stream. To retrieve only streams that satisfy a specific condition, you can specify a StreamNameCondition .
    See also: AWS API Documentation
    
    
    :example: response = client.list_streams(
        MaxResults=123,
        NextToken='string',
        StreamNameCondition={
            'ComparisonOperator': 'BEGINS_WITH',
            'ComparisonValue': 'string'
        }
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of streams to return in the response. The default is 10,000.

    :type NextToken: string
    :param NextToken: If you specify this parameter, when the result of a ListStreams operation is truncated, the call returns the NextToken in the response. To get another batch of streams, provide this token in your next request.

    :type StreamNameCondition: dict
    :param StreamNameCondition: Optional: Returns only streams that satisfy a specific condition. Currently, you can specify only the prefix of a stream name as a condition.
            ComparisonOperator (string) --A comparison operator. Currently, you can specify only the BEGINS_WITH operator, which finds streams whose names start with a given prefix.
            ComparisonValue (string) --A value to compare.
            

    :rtype: dict
    :return: {
        'StreamInfoList': [
            {
                'DeviceName': 'string',
                'StreamName': 'string',
                'StreamARN': 'string',
                'MediaType': 'string',
                'KmsKeyId': 'string',
                'Version': 'string',
                'Status': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING',
                'CreationTime': datetime(2015, 1, 1),
                'DataRetentionInHours': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_tags_for_stream(NextToken=None, StreamARN=None, StreamName=None):
    """
    Returns a list of tags associated with the specified stream.
    In the request, you must specify either the StreamName or the StreamARN .
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_stream(
        NextToken='string',
        StreamARN='string',
        StreamName='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If you specify this parameter and the result of a ListTagsForStream call is truncated, the response includes a token that you can use in the next request to fetch the next batch of tags.

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream that you want to list tags for.

    :type StreamName: string
    :param StreamName: The name of the stream that you want to list tags for.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def tag_stream(StreamARN=None, StreamName=None, Tags=None):
    """
    Adds one or more tags to a stream. A tag is a key-value pair (the value is optional) that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    You must provide either the StreamName or the StreamARN .
    This operation requires permission for the KinesisVideo:TagStream action.
    Kinesis video streams support up to 50 tags.
    See also: AWS API Documentation
    
    
    :example: response = client.tag_stream(
        StreamARN='string',
        StreamName='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the resource that you want to add the tag or tags to.

    :type StreamName: string
    :param StreamName: The name of the stream that you want to add the tag or tags to.

    :type Tags: dict
    :param Tags: [REQUIRED]
            A list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional).
            (string) --
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_stream(StreamARN=None, StreamName=None, TagKeyList=None):
    """
    Removes one or more tags from a stream. In the request, specify only a tag key or keys; don't specify the value. If you specify a tag key that does not exist, it's ignored.
    In the request, you must provide the StreamName or StreamARN .
    See also: AWS API Documentation
    
    
    :example: response = client.untag_stream(
        StreamARN='string',
        StreamName='string',
        TagKeyList=[
            'string',
        ]
    )
    
    
    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream that you want to remove tags from.

    :type StreamName: string
    :param StreamName: The name of the stream that you want to remove tags from.

    :type TagKeyList: list
    :param TagKeyList: [REQUIRED]
            A list of the keys of the tags that you want to remove.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_data_retention(StreamName=None, StreamARN=None, CurrentVersion=None, Operation=None, DataRetentionChangeInHours=None):
    """
    Increases or decreases the stream's data retention period by the value that you specify. To indicate whether you want to increase or decrease the data retention period, specify the Operation parameter in the request body. In the request, you must specify either the StreamName or the StreamARN .
    This operation requires permission for the KinesisVideo:UpdateDataRetention action.
    Changing the data retention period affects the data in the stream as follows:
    See also: AWS API Documentation
    
    
    :example: response = client.update_data_retention(
        StreamName='string',
        StreamARN='string',
        CurrentVersion='string',
        Operation='INCREASE_DATA_RETENTION'|'DECREASE_DATA_RETENTION',
        DataRetentionChangeInHours=123
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream whose retention period you want to change.

    :type StreamARN: string
    :param StreamARN: The Amazon Resource Name (ARN) of the stream whose retention period you want to change.

    :type CurrentVersion: string
    :param CurrentVersion: [REQUIRED]
            The version of the stream whose retention period you want to change. To get the version, call either the DescribeStream or the ListStreams API.
            

    :type Operation: string
    :param Operation: [REQUIRED]
            Indicates whether you want to increase or decrease the retention period.
            

    :type DataRetentionChangeInHours: integer
    :param DataRetentionChangeInHours: [REQUIRED]
            The retention period, in hours. The value you specify replaces the current value.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    StreamName (string) -- The name of the stream whose retention period you want to change.
    StreamARN (string) -- The Amazon Resource Name (ARN) of the stream whose retention period you want to change.
    CurrentVersion (string) -- [REQUIRED]
    The version of the stream whose retention period you want to change. To get the version, call either the DescribeStream or the ListStreams API.
    
    Operation (string) -- [REQUIRED]
    Indicates whether you want to increase or decrease the retention period.
    
    DataRetentionChangeInHours (integer) -- [REQUIRED]
    The retention period, in hours. The value you specify replaces the current value.
    
    
    """
    pass

def update_stream(StreamName=None, StreamARN=None, CurrentVersion=None, DeviceName=None, MediaType=None):
    """
    Updates stream metadata, such as the device name and media type.
    You must provide the stream name or the Amazon Resource Name (ARN) of the stream.
    To make sure that you have the latest version of the stream before updating it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the DescribeStream API.
    See also: AWS API Documentation
    
    
    :example: response = client.update_stream(
        StreamName='string',
        StreamARN='string',
        CurrentVersion='string',
        DeviceName='string',
        MediaType='string'
    )
    
    
    :type StreamName: string
    :param StreamName: The name of the stream whose metadata you want to update.
            The stream name is an identifier for the stream, and must be unique for each account and region.
            

    :type StreamARN: string
    :param StreamARN: The ARN of the stream whose metadata you want to update.

    :type CurrentVersion: string
    :param CurrentVersion: [REQUIRED]
            The version of the stream whose metadata you want to update.
            

    :type DeviceName: string
    :param DeviceName: The name of the device that is writing to the stream.
            Note
            In the current implementation, Kinesis Video Streams does not use this name.
            

    :type MediaType: string
    :param MediaType: The stream's media type. Use MediaType to specify the type of content that the stream contains to the consumers of the stream. For more information about media types, see Media Types . If you choose to specify the MediaType , see Naming Requirements .
            To play video on the console, you must specify the correct video type. For example, if the video in the stream is H.264, specify video/h264 as the MediaType .
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

