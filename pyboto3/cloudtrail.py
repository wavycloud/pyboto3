'''

The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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

def add_tags(ResourceId=None, TagsList=None):
    """
    Adds one or more tags to a trail, up to a limit of 10. Tags must be unique per trail. Overwrites an existing tag's value when a new value is specified for an existing tag key. If you specify a key without a value, the tag will be created with the specified key and a value of null. You can tag a trail that applies to all regions only from the region in which the trail was created (that is, from its home region).
    
    
    :example: response = client.add_tags(
        ResourceId='string',
        TagsList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            Specifies the ARN of the trail to which one or more tags will be added. The format of a trail ARN is:
            arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail
            

    :type TagsList: list
    :param TagsList: Contains a list of CloudTrail tags, up to a limit of 10.
            (dict) --A custom key-value pair associated with a resource such as a CloudTrail trail.
            Key (string) -- [REQUIRED]The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.
            Value (string) --The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.
            
            

    :rtype: dict
    :return: {}
    
    
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

def create_trail(Name=None, S3BucketName=None, S3KeyPrefix=None, SnsTopicName=None, IncludeGlobalServiceEvents=None, IsMultiRegionTrail=None, EnableLogFileValidation=None, CloudWatchLogsLogGroupArn=None, CloudWatchLogsRoleArn=None, KmsKeyId=None):
    """
    Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective of the region in which they were created.
    
    
    :example: response = client.create_trail(
        Name='string',
        S3BucketName='string',
        S3KeyPrefix='string',
        SnsTopicName='string',
        IncludeGlobalServiceEvents=True|False,
        IsMultiRegionTrail=True|False,
        EnableLogFileValidation=True|False,
        CloudWatchLogsLogGroupArn='string',
        CloudWatchLogsRoleArn='string',
        KmsKeyId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Specifies the name of the trail. The name must meet the following requirements:
            Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
            Start with a letter or number, and end with a letter or number
            Be between 3 and 128 characters
            Have no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are invalid.
            Not be in IP address format (for example, 192.168.5.4)
            

    :type S3BucketName: string
    :param S3BucketName: [REQUIRED]
            Specifies the name of the Amazon S3 bucket designated for publishing log files. See Amazon S3 Bucket Naming Requirements .
            

    :type S3KeyPrefix: string
    :param S3KeyPrefix: Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files . The maximum length is 200 characters.

    :type SnsTopicName: string
    :param SnsTopicName: Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.

    :type IncludeGlobalServiceEvents: boolean
    :param IncludeGlobalServiceEvents: Specifies whether the trail is publishing events from global services such as IAM to the log files.

    :type IsMultiRegionTrail: boolean
    :param IsMultiRegionTrail: Specifies whether the trail is created in the current region or in all regions. The default is false.

    :type EnableLogFileValidation: boolean
    :param EnableLogFileValidation: Specifies whether log file integrity validation is enabled. The default is false.
            Note
            When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail will not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.
            

    :type CloudWatchLogsLogGroupArn: string
    :param CloudWatchLogsLogGroupArn: Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.

    :type CloudWatchLogsRoleArn: string
    :param CloudWatchLogsRoleArn: Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.

    :type KmsKeyId: string
    :param KmsKeyId: Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be a an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
            Examples:
            alias/MyAliasName
            arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            12345678-1234-1234-1234-123456789012
            

    :rtype: dict
    :return: {
        'Name': 'string',
        'S3BucketName': 'string',
        'S3KeyPrefix': 'string',
        'SnsTopicName': 'string',
        'SnsTopicARN': 'string',
        'IncludeGlobalServiceEvents': True|False,
        'IsMultiRegionTrail': True|False,
        'TrailARN': 'string',
        'LogFileValidationEnabled': True|False,
        'CloudWatchLogsLogGroupArn': 'string',
        'CloudWatchLogsRoleArn': 'string',
        'KmsKeyId': 'string'
    }
    
    
    """
    pass

def delete_trail(Name=None):
    """
    Deletes a trail. This operation must be called from the region in which the trail was created. DeleteTrail cannot be called on the shadow trails (replicated trails in other regions) of a trail that is enabled in all regions.
    
    
    :example: response = client.delete_trail(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Specifies the name or the CloudTrail ARN of the trail to be deleted. The format of a trail ARN is:
            arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_trails(trailNameList=None, includeShadowTrails=None):
    """
    Retrieves settings for the trail associated with the current region for your account.
    
    
    :example: response = client.describe_trails(
        trailNameList=[
            'string',
        ],
        includeShadowTrails=True|False
    )
    
    
    :type trailNameList: list
    :param trailNameList: Specifies a list of trail names, trail ARNs, or both, of the trails to describe. The format of a trail ARN is:
            arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail
            If an empty list is specified, information for the trail in the current region is returned.
            If an empty list is specified and IncludeShadowTrails is false, then information for all trails in the current region is returned.
            If an empty list is specified and IncludeShadowTrails is null or true, then information for all trails in the current region and any associated shadow trails in other regions is returned.
            Note
            If one or more trail names are specified, information is returned only if the names match the names of trails belonging only to the current region. To return information about a trail in another region, you must specify its trail ARN.
            (string) --
            

    :type includeShadowTrails: boolean
    :param includeShadowTrails: Specifies whether to include shadow trails in the response. A shadow trail is the replication in a region of a trail that was created in a different region. The default is true.

    :rtype: dict
    :return: {
        'trailList': [
            {
                'Name': 'string',
                'S3BucketName': 'string',
                'S3KeyPrefix': 'string',
                'SnsTopicName': 'string',
                'SnsTopicARN': 'string',
                'IncludeGlobalServiceEvents': True|False,
                'IsMultiRegionTrail': True|False,
                'HomeRegion': 'string',
                'TrailARN': 'string',
                'LogFileValidationEnabled': True|False,
                'CloudWatchLogsLogGroupArn': 'string',
                'CloudWatchLogsRoleArn': 'string',
                'KmsKeyId': 'string'
            },
        ]
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

def get_trail_status(Name=None):
    """
    Returns a JSON-formatted list of information about the specified trail. Fields include information on delivery errors, Amazon SNS and Amazon S3 errors, and start and stop logging times for each trail. This operation returns trail status from a single region. To return trail status from all regions, you must call the operation on each region.
    
    
    :example: response = client.get_trail_status(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Specifies the name or the CloudTrail ARN of the trail for which you are requesting status. To get the status of a shadow trail (a replication of the trail in another region), you must specify its ARN. The format of a trail ARN is:
            arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail
            

    :rtype: dict
    :return: {
        'IsLogging': True|False,
        'LatestDeliveryError': 'string',
        'LatestNotificationError': 'string',
        'LatestDeliveryTime': datetime(2015, 1, 1),
        'LatestNotificationTime': datetime(2015, 1, 1),
        'StartLoggingTime': datetime(2015, 1, 1),
        'StopLoggingTime': datetime(2015, 1, 1),
        'LatestCloudWatchLogsDeliveryError': 'string',
        'LatestCloudWatchLogsDeliveryTime': datetime(2015, 1, 1),
        'LatestDigestDeliveryTime': datetime(2015, 1, 1),
        'LatestDigestDeliveryError': 'string',
        'LatestDeliveryAttemptTime': 'string',
        'LatestNotificationAttemptTime': 'string',
        'LatestNotificationAttemptSucceeded': 'string',
        'LatestDeliveryAttemptSucceeded': 'string',
        'TimeLoggingStarted': 'string',
        'TimeLoggingStopped': 'string'
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_public_keys(StartTime=None, EndTime=None, NextToken=None):
    """
    Returns all public keys whose private keys were used to sign the digest files within the specified time range. The public key is needed to validate digest files that were signed with its corresponding private key.
    
    
    :example: response = client.list_public_keys(
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        NextToken='string'
    )
    
    
    :type StartTime: datetime
    :param StartTime: Optionally specifies, in UTC, the start of the time range to look up public keys for CloudTrail digest files. If not specified, the current time is used, and the current public key is returned.

    :type EndTime: datetime
    :param EndTime: Optionally specifies, in UTC, the end of the time range to look up public keys for CloudTrail digest files. If not specified, the current time is used.

    :type NextToken: string
    :param NextToken: Reserved for future use.

    :rtype: dict
    :return: {
        'PublicKeyList': [
            {
                'Value': b'bytes',
                'ValidityStartTime': datetime(2015, 1, 1),
                'ValidityEndTime': datetime(2015, 1, 1),
                'Fingerprint': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_tags(ResourceIdList=None, NextToken=None):
    """
    Lists the tags for the trail in the current region.
    
    
    :example: response = client.list_tags(
        ResourceIdList=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type ResourceIdList: list
    :param ResourceIdList: [REQUIRED]
            Specifies a list of trail ARNs whose tags will be listed. The list has a limit of 20 ARNs. The format of a trail ARN is:
            arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail
            (string) --
            

    :type NextToken: string
    :param NextToken: Reserved for future use.

    :rtype: dict
    :return: {
        'ResourceTagList': [
            {
                'ResourceId': 'string',
                'TagsList': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def lookup_events(LookupAttributes=None, StartTime=None, EndTime=None, MaxResults=None, NextToken=None):
    """
    Looks up API activity events captured by CloudTrail that create, update, or delete resources in your account. Events for a region can be looked up for the times in which you had CloudTrail turned on in that region during the last seven days. Lookup supports five different attributes: time range (defined by a start time and end time), user name, event name, resource type, and resource name. All attributes are optional. The maximum number of attributes that can be specified in any one lookup request are time range and one other attribute. The default number of results returned is 10, with a maximum of 50 possible. The response includes a token that you can use to get the next page of results.
    
    
    :example: response = client.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'EventId'|'EventName'|'Username'|'ResourceType'|'ResourceName',
                'AttributeValue': 'string'
            },
        ],
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type LookupAttributes: list
    :param LookupAttributes: Contains a list of lookup attributes. Currently the list can contain only one item.
            (dict) --Specifies an attribute and value that filter the events returned.
            AttributeKey (string) -- [REQUIRED]Specifies an attribute on which to filter the events returned.
            AttributeValue (string) -- [REQUIRED]Specifies a value for the specified AttributeKey.
            
            

    :type StartTime: datetime
    :param StartTime: Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.

    :type EndTime: datetime
    :param EndTime: Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.

    :type MaxResults: integer
    :param MaxResults: The number of events to return. Possible values are 1 through 50. The default is 10.

    :type NextToken: string
    :param NextToken: The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the the original call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.

    :rtype: dict
    :return: {
        'Events': [
            {
                'EventId': 'string',
                'EventName': 'string',
                'EventTime': datetime(2015, 1, 1),
                'Username': 'string',
                'Resources': [
                    {
                        'ResourceType': 'string',
                        'ResourceName': 'string'
                    },
                ],
                'CloudTrailEvent': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def remove_tags(ResourceId=None, TagsList=None):
    """
    Removes the specified tags from a trail.
    
    
    :example: response = client.remove_tags(
        ResourceId='string',
        TagsList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            Specifies the ARN of the trail from which tags should be removed. The format of a trail ARN is:
            arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail
            

    :type TagsList: list
    :param TagsList: Specifies a list of tags to be removed.
            (dict) --A custom key-value pair associated with a resource such as a CloudTrail trail.
            Key (string) -- [REQUIRED]The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.
            Value (string) --The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.
            
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def start_logging(Name=None):
    """
    Starts the recording of AWS API calls and log file delivery for a trail. For a trail that is enabled in all regions, this operation must be called from the region in which the trail was created. This operation cannot be called on the shadow trails (replicated trails in other regions) of a trail that is enabled in all regions.
    
    
    :example: response = client.start_logging(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Specifies the name or the CloudTrail ARN of the trail for which CloudTrail logs AWS API calls. The format of a trail ARN is:
            arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def stop_logging(Name=None):
    """
    Suspends the recording of AWS API calls and log file delivery for the specified trail. Under most circumstances, there is no need to use this action. You can update a trail without stopping it first. This action is the only way to stop recording. For a trail enabled in all regions, this operation must be called from the region in which the trail was created, or an InvalidHomeRegionException will occur. This operation cannot be called on the shadow trails (replicated trails in other regions) of a trail enabled in all regions.
    
    
    :example: response = client.stop_logging(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Specifies the name or the CloudTrail ARN of the trail for which CloudTrail will stop logging AWS API calls. The format of a trail ARN is:
            arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def update_trail(Name=None, S3BucketName=None, S3KeyPrefix=None, SnsTopicName=None, IncludeGlobalServiceEvents=None, IsMultiRegionTrail=None, EnableLogFileValidation=None, CloudWatchLogsLogGroupArn=None, CloudWatchLogsRoleArn=None, KmsKeyId=None):
    """
    Updates the settings that specify delivery of log files. Changes to a trail do not require stopping the CloudTrail service. Use this action to designate an existing bucket for log delivery. If the existing bucket has previously been a target for CloudTrail log files, an IAM policy exists for the bucket. UpdateTrail must be called from the region in which the trail was created; otherwise, an InvalidHomeRegionException is thrown.
    
    
    :example: response = client.update_trail(
        Name='string',
        S3BucketName='string',
        S3KeyPrefix='string',
        SnsTopicName='string',
        IncludeGlobalServiceEvents=True|False,
        IsMultiRegionTrail=True|False,
        EnableLogFileValidation=True|False,
        CloudWatchLogsLogGroupArn='string',
        CloudWatchLogsRoleArn='string',
        KmsKeyId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Specifies the name of the trail or trail ARN. If Name is a trail name, the string must meet the following requirements:
            Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
            Start with a letter or number, and end with a letter or number
            Be between 3 and 128 characters
            Have no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are invalid.
            Not be in IP address format (for example, 192.168.5.4)
            If Name is a trail ARN, it must be in the format:
            arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail
            

    :type S3BucketName: string
    :param S3BucketName: Specifies the name of the Amazon S3 bucket designated for publishing log files. See Amazon S3 Bucket Naming Requirements .

    :type S3KeyPrefix: string
    :param S3KeyPrefix: Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files . The maximum length is 200 characters.

    :type SnsTopicName: string
    :param SnsTopicName: Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.

    :type IncludeGlobalServiceEvents: boolean
    :param IncludeGlobalServiceEvents: Specifies whether the trail is publishing events from global services such as IAM to the log files.

    :type IsMultiRegionTrail: boolean
    :param IsMultiRegionTrail: Specifies whether the trail applies only to the current region or to all regions. The default is false. If the trail exists only in the current region and this value is set to true, shadow trails (replications of the trail) will be created in the other regions. If the trail exists in all regions and this value is set to false, the trail will remain in the region where it was created, and its shadow trails in other regions will be deleted.

    :type EnableLogFileValidation: boolean
    :param EnableLogFileValidation: Specifies whether log file validation is enabled. The default is false.
            Note
            When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail will not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.
            

    :type CloudWatchLogsLogGroupArn: string
    :param CloudWatchLogsLogGroupArn: Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.

    :type CloudWatchLogsRoleArn: string
    :param CloudWatchLogsRoleArn: Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.

    :type KmsKeyId: string
    :param KmsKeyId: Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be a an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
            Examples:
            alias/MyAliasName
            arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
            arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
            12345678-1234-1234-1234-123456789012
            

    :rtype: dict
    :return: {
        'Name': 'string',
        'S3BucketName': 'string',
        'S3KeyPrefix': 'string',
        'SnsTopicName': 'string',
        'SnsTopicARN': 'string',
        'IncludeGlobalServiceEvents': True|False,
        'IsMultiRegionTrail': True|False,
        'TrailARN': 'string',
        'LogFileValidationEnabled': True|False,
        'CloudWatchLogsLogGroupArn': 'string',
        'CloudWatchLogsRoleArn': 'string',
        'KmsKeyId': 'string'
    }
    
    
    """
    pass

