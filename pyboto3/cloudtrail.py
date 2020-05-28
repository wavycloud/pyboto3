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

def add_tags(ResourceId=None, TagsList=None):
    """
    Adds one or more tags to a trail, up to a limit of 50. Overwrites an existing tag\'s value when a new value is specified for an existing tag key. Tag key names must be unique for a trail; you cannot have two keys with the same name but different values. If you specify a key without a value, the tag will be created with the specified key and a value of null. You can tag a trail that applies to all AWS Regions only from the Region in which the trail was created (also known as its home region).
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ResourceId: [REQUIRED]\nSpecifies the ARN of the trail to which one or more tags will be added. The format of a trail ARN is:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n

    :type TagsList: list
    :param TagsList: Contains a list of CloudTrail tags, up to a limit of 50\n\n(dict) --A custom key-value pair associated with a resource such as a CloudTrail trail.\n\nKey (string) -- [REQUIRED]The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.\n\nValue (string) --The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Returns the objects or data listed below if successful. Otherwise, returns an error.





Exceptions

CloudTrail.Client.exceptions.ResourceNotFoundException
CloudTrail.Client.exceptions.CloudTrailARNInvalidException
CloudTrail.Client.exceptions.ResourceTypeNotSupportedException
CloudTrail.Client.exceptions.TagsLimitExceededException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.InvalidTagParameterException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.NotOrganizationMasterAccountException


    :return: {}
    
    
    :returns: 
    CloudTrail.Client.exceptions.ResourceNotFoundException
    CloudTrail.Client.exceptions.CloudTrailARNInvalidException
    CloudTrail.Client.exceptions.ResourceTypeNotSupportedException
    CloudTrail.Client.exceptions.TagsLimitExceededException
    CloudTrail.Client.exceptions.InvalidTrailNameException
    CloudTrail.Client.exceptions.InvalidTagParameterException
    CloudTrail.Client.exceptions.UnsupportedOperationException
    CloudTrail.Client.exceptions.OperationNotPermittedException
    CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_trail(Name=None, S3BucketName=None, S3KeyPrefix=None, SnsTopicName=None, IncludeGlobalServiceEvents=None, IsMultiRegionTrail=None, EnableLogFileValidation=None, CloudWatchLogsLogGroupArn=None, CloudWatchLogsRoleArn=None, KmsKeyId=None, IsOrganizationTrail=None, TagsList=None):
    """
    Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket.
    See also: AWS API Documentation
    
    Exceptions
    
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
        KmsKeyId='string',
        IsOrganizationTrail=True|False,
        TagsList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nSpecifies the name of the trail. The name must meet the following requirements:\n\nContain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)\nStart with a letter or number, and end with a letter or number\nBe between 3 and 128 characters\nHave no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are invalid.\nNot be in IP address format (for example, 192.168.5.4)\n\n

    :type S3BucketName: string
    :param S3BucketName: [REQUIRED]\nSpecifies the name of the Amazon S3 bucket designated for publishing log files. See Amazon S3 Bucket Naming Requirements .\n

    :type S3KeyPrefix: string
    :param S3KeyPrefix: Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files . The maximum length is 200 characters.

    :type SnsTopicName: string
    :param SnsTopicName: Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.

    :type IncludeGlobalServiceEvents: boolean
    :param IncludeGlobalServiceEvents: Specifies whether the trail is publishing events from global services such as IAM to the log files.

    :type IsMultiRegionTrail: boolean
    :param IsMultiRegionTrail: Specifies whether the trail is created in the current region or in all regions. The default is false, which creates a trail only in the region where you are signed in. As a best practice, consider creating trails that log events in all regions.

    :type EnableLogFileValidation: boolean
    :param EnableLogFileValidation: Specifies whether log file integrity validation is enabled. The default is false.\n\nNote\nWhen you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail will not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.\n\n

    :type CloudWatchLogsLogGroupArn: string
    :param CloudWatchLogsLogGroupArn: Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.

    :type CloudWatchLogsRoleArn: string
    :param CloudWatchLogsRoleArn: Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.

    :type KmsKeyId: string
    :param KmsKeyId: Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.\nExamples:\n\nalias/MyAliasName\narn:aws:kms:us-east-2:123456789012:alias/MyAliasName\narn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012\n12345678-1234-1234-1234-123456789012\n\n

    :type IsOrganizationTrail: boolean
    :param IsOrganizationTrail: Specifies whether the trail is created for all accounts in an organization in AWS Organizations, or only for the current AWS account. The default is false, and cannot be true unless the call is made on behalf of an AWS account that is the master account for an organization in AWS Organizations.

    :type TagsList: list
    :param TagsList: A list of tags.\n\n(dict) --A custom key-value pair associated with a resource such as a CloudTrail trail.\n\nKey (string) -- [REQUIRED]The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.\n\nValue (string) --The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
    'KmsKeyId': 'string',
    'IsOrganizationTrail': True|False
}


Response Structure

(dict) --
Returns the objects or data listed below if successful. Otherwise, returns an error.

Name (string) --
Specifies the name of the trail.

S3BucketName (string) --
Specifies the name of the Amazon S3 bucket designated for publishing log files.

S3KeyPrefix (string) --
Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files .

SnsTopicName (string) --
This field is no longer in use. Use SnsTopicARN.

SnsTopicARN (string) --
Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:

arn:aws:sns:us-east-2:123456789012:MyTopic


IncludeGlobalServiceEvents (boolean) --
Specifies whether the trail is publishing events from global services such as IAM to the log files.

IsMultiRegionTrail (boolean) --
Specifies whether the trail exists in one region or in all regions.

TrailARN (string) --
Specifies the ARN of the trail that was created. The format of a trail ARN is:

arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail


LogFileValidationEnabled (boolean) --
Specifies whether log file integrity validation is enabled.

CloudWatchLogsLogGroupArn (string) --
Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs will be delivered.

CloudWatchLogsRoleArn (string) --
Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.

KmsKeyId (string) --
Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the format:

arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012


IsOrganizationTrail (boolean) --
Specifies whether the trail is an organization trail.







Exceptions

CloudTrail.Client.exceptions.MaximumNumberOfTrailsExceededException
CloudTrail.Client.exceptions.TrailAlreadyExistsException
CloudTrail.Client.exceptions.S3BucketDoesNotExistException
CloudTrail.Client.exceptions.InsufficientS3BucketPolicyException
CloudTrail.Client.exceptions.InsufficientSnsTopicPolicyException
CloudTrail.Client.exceptions.InsufficientEncryptionPolicyException
CloudTrail.Client.exceptions.InvalidS3BucketNameException
CloudTrail.Client.exceptions.InvalidS3PrefixException
CloudTrail.Client.exceptions.InvalidSnsTopicNameException
CloudTrail.Client.exceptions.InvalidKmsKeyIdException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.TrailNotProvidedException
CloudTrail.Client.exceptions.InvalidParameterCombinationException
CloudTrail.Client.exceptions.KmsKeyNotFoundException
CloudTrail.Client.exceptions.KmsKeyDisabledException
CloudTrail.Client.exceptions.KmsException
CloudTrail.Client.exceptions.InvalidCloudWatchLogsLogGroupArnException
CloudTrail.Client.exceptions.InvalidCloudWatchLogsRoleArnException
CloudTrail.Client.exceptions.CloudWatchLogsDeliveryUnavailableException
CloudTrail.Client.exceptions.InvalidTagParameterException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.CloudTrailAccessNotEnabledException
CloudTrail.Client.exceptions.InsufficientDependencyServiceAccessPermissionException
CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
CloudTrail.Client.exceptions.OrganizationsNotInUseException
CloudTrail.Client.exceptions.OrganizationNotInAllFeaturesModeException


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
        'KmsKeyId': 'string',
        'IsOrganizationTrail': True|False
    }
    
    
    :returns: 
    CloudTrail.Client.exceptions.MaximumNumberOfTrailsExceededException
    CloudTrail.Client.exceptions.TrailAlreadyExistsException
    CloudTrail.Client.exceptions.S3BucketDoesNotExistException
    CloudTrail.Client.exceptions.InsufficientS3BucketPolicyException
    CloudTrail.Client.exceptions.InsufficientSnsTopicPolicyException
    CloudTrail.Client.exceptions.InsufficientEncryptionPolicyException
    CloudTrail.Client.exceptions.InvalidS3BucketNameException
    CloudTrail.Client.exceptions.InvalidS3PrefixException
    CloudTrail.Client.exceptions.InvalidSnsTopicNameException
    CloudTrail.Client.exceptions.InvalidKmsKeyIdException
    CloudTrail.Client.exceptions.InvalidTrailNameException
    CloudTrail.Client.exceptions.TrailNotProvidedException
    CloudTrail.Client.exceptions.InvalidParameterCombinationException
    CloudTrail.Client.exceptions.KmsKeyNotFoundException
    CloudTrail.Client.exceptions.KmsKeyDisabledException
    CloudTrail.Client.exceptions.KmsException
    CloudTrail.Client.exceptions.InvalidCloudWatchLogsLogGroupArnException
    CloudTrail.Client.exceptions.InvalidCloudWatchLogsRoleArnException
    CloudTrail.Client.exceptions.CloudWatchLogsDeliveryUnavailableException
    CloudTrail.Client.exceptions.InvalidTagParameterException
    CloudTrail.Client.exceptions.UnsupportedOperationException
    CloudTrail.Client.exceptions.OperationNotPermittedException
    CloudTrail.Client.exceptions.CloudTrailAccessNotEnabledException
    CloudTrail.Client.exceptions.InsufficientDependencyServiceAccessPermissionException
    CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
    CloudTrail.Client.exceptions.OrganizationsNotInUseException
    CloudTrail.Client.exceptions.OrganizationNotInAllFeaturesModeException
    
    """
    pass

def delete_trail(Name=None):
    """
    Deletes a trail. This operation must be called from the region in which the trail was created. DeleteTrail cannot be called on the shadow trails (replicated trails in other regions) of a trail that is enabled in all regions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_trail(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nSpecifies the name or the CloudTrail ARN of the trail to be deleted. The format of a trail ARN is: arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Returns the objects or data listed below if successful. Otherwise, returns an error.




Exceptions

CloudTrail.Client.exceptions.TrailNotFoundException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.InvalidHomeRegionException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
CloudTrail.Client.exceptions.InsufficientDependencyServiceAccessPermissionException


    :return: {}
    
    
    """
    pass

def describe_trails(trailNameList=None, includeShadowTrails=None):
    """
    Retrieves settings for one or more trails associated with the current region for your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_trails(
        trailNameList=[
            'string',
        ],
        includeShadowTrails=True|False
    )
    
    
    :type trailNameList: list
    :param trailNameList: Specifies a list of trail names, trail ARNs, or both, of the trails to describe. The format of a trail ARN is:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\nIf an empty list is specified, information for the trail in the current region is returned.\n\nIf an empty list is specified and IncludeShadowTrails is false, then information for all trails in the current region is returned.\nIf an empty list is specified and IncludeShadowTrails is null or true, then information for all trails in the current region and any associated shadow trails in other regions is returned.\n\n\nNote\nIf one or more trail names are specified, information is returned only if the names match the names of trails belonging only to the current region. To return information about a trail in another region, you must specify its trail ARN.\n\n\n(string) --\n\n

    :type includeShadowTrails: boolean
    :param includeShadowTrails: Specifies whether to include shadow trails in the response. A shadow trail is the replication in a region of a trail that was created in a different region, or in the case of an organization trail, the replication of an organization trail in member accounts. If you do not include shadow trails, organization trails in a member account and region replication trails will not be returned. The default is true.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'KmsKeyId': 'string',
            'HasCustomEventSelectors': True|False,
            'HasInsightSelectors': True|False,
            'IsOrganizationTrail': True|False
        },
    ]
}


Response Structure

(dict) --
Returns the objects or data listed below if successful. Otherwise, returns an error.

trailList (list) --
The list of trail objects. Trail objects with string values are only returned if values for the objects exist in a trail\'s configuration. For example, SNSTopicName and SNSTopicARN are only returned in results if a trail is configured to send SNS notifications. Similarly, KMSKeyId only appears in results if a trail\'s log files are encrypted with AWS KMS-managed keys.

(dict) --
The settings for a trail.

Name (string) --
Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.

S3BucketName (string) --
Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See Amazon S3 Bucket Naming Requirements .

S3KeyPrefix (string) --
Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files .The maximum length is 200 characters.

SnsTopicName (string) --
This field is no longer in use. Use SnsTopicARN.

SnsTopicARN (string) --
Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:

arn:aws:sns:us-east-2:123456789012:MyTopic


IncludeGlobalServiceEvents (boolean) --
Set to True to include AWS API calls from AWS global services such as IAM. Otherwise, False .

IsMultiRegionTrail (boolean) --
Specifies whether the trail exists only in one region or exists in all regions.

HomeRegion (string) --
The region in which the trail was created.

TrailARN (string) --
Specifies the ARN of the trail. The format of a trail ARN is:

arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail


LogFileValidationEnabled (boolean) --
Specifies whether log file validation is enabled.

CloudWatchLogsLogGroupArn (string) --
Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered.

CloudWatchLogsRoleArn (string) --
Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.

KmsKeyId (string) --
Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the format:

arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012


HasCustomEventSelectors (boolean) --
Specifies if the trail has custom event selectors.

HasInsightSelectors (boolean) --
Specifies whether a trail has insight types specified in an InsightSelector list.

IsOrganizationTrail (boolean) --
Specifies whether the trail is an organization trail.











Exceptions

CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.InvalidTrailNameException


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
                'KmsKeyId': 'string',
                'HasCustomEventSelectors': True|False,
                'HasInsightSelectors': True|False,
                'IsOrganizationTrail': True|False
            },
        ]
    }
    
    
    :returns: 
    CloudTrail.Client.exceptions.UnsupportedOperationException
    CloudTrail.Client.exceptions.OperationNotPermittedException
    CloudTrail.Client.exceptions.InvalidTrailNameException
    
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

def get_event_selectors(TrailName=None):
    """
    Describes the settings for the event selectors that you configured for your trail. The information returned for your event selectors includes the following:
    For more information, see Logging Data and Management Events for Trails in the AWS CloudTrail User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_event_selectors(
        TrailName='string'
    )
    
    
    :type TrailName: string
    :param TrailName: [REQUIRED]\nSpecifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:\n\nContain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)\nStart with a letter or number, and end with a letter or number\nBe between 3 and 128 characters\nHave no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are not valid.\nNot be in IP address format (for example, 192.168.5.4)\n\nIf you specify a trail ARN, it must be in the format:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n

    :rtype: dict
ReturnsResponse Syntax{
    'TrailARN': 'string',
    'EventSelectors': [
        {
            'ReadWriteType': 'ReadOnly'|'WriteOnly'|'All',
            'IncludeManagementEvents': True|False,
            'DataResources': [
                {
                    'Type': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'ExcludeManagementEventSources': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --
TrailARN (string) --The specified trail ARN that has the event selectors.

EventSelectors (list) --The event selectors that are configured for the trail.

(dict) --Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn\'t match any event selector, the trail doesn\'t log the event.
You can configure up to five event selectors for a trail.

ReadWriteType (string) --Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 GetConsoleOutput is a read-only API operation and RunInstances is a write-only API operation.
By default, the value is All .

IncludeManagementEvents (boolean) --Specify if you want your event selector to include management events for your trail.
For more information, see Management Events in the AWS CloudTrail User Guide .
By default, the value is true .

DataResources (list) --CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.
For more information, see Data Events and Limits in AWS CloudTrail in the AWS CloudTrail User Guide .

(dict) --The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors for your trail to log data events. Data events provide information about the resource operations performed on or within a resource itself. These are also known as data plane operations. You can specify up to 250 data resources for a trail.

Note
The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

The following example demonstrates how logging works when you configure logging of all data events for an S3 bucket named bucket-1 . In this example, the CloudTrail user specified an empty prefix, and the option to log both Read and Write data events.

A user uploads an image file to bucket-1 .
The PutObject API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event.
A user uploads an object to an Amazon S3 bucket named arn:aws:s3:::bucket-2 .
The PutObject API operation occurred for an object in an S3 bucket that the CloudTrail user didn\'t specify for the trail. The trail doesn\xe2\x80\x99t log the event.

The following example demonstrates how logging works when you configure logging of AWS Lambda data events for a Lambda function named MyLambdaFunction , but not for all AWS Lambda functions.

A user runs a script that includes a call to the MyLambdaFunction function and the MyOtherLambdaFunction function.
The Invoke API operation on MyLambdaFunction is an AWS Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for MyLambdaFunction , any invocations of that function are logged. The trail processes and logs the event.
The Invoke API operation on MyOtherLambdaFunction is an AWS Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the Invoke operation for MyOtherLambdaFunction does not match the function specified for the trail. The trail doesn\xe2\x80\x99t log the event.


Type (string) --The resource type in which you want to log data events. You can specify AWS::S3::Object or AWS::Lambda::Function resources.

Values (list) --An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.

To log data events for all objects in all S3 buckets in your AWS account, specify the prefix as arn:aws:s3::: .


Note
This will also enable logging of data event activity performed by any user or role in your AWS account, even if that activity is performed on a bucket that belongs to another AWS account.


To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as arn:aws:s3:::bucket-1/ . The trail logs data events for all objects in this S3 bucket.
To log data events for specific objects, specify the S3 bucket and object prefix such as arn:aws:s3:::bucket-1/example-images . The trail logs data events for objects in this S3 bucket that match the prefix.
To log data events for all functions in your AWS account, specify the prefix as arn:aws:lambda .


Note
This will also enable logging of Invoke activity performed by any user or role in your AWS account, even if that activity is performed on a function that belongs to another AWS account.


To log data events for a specific Lambda function, specify the function ARN.


Note
Lambda function ARNs are exact. For example, if you specify a function ARN arn:aws:lambda:us-west-2:111111111111:function:helloworld , data events will only be logged for arn:aws:lambda:us-west-2:111111111111:function:helloworld . They will not be logged for arn:aws:lambda:us-west-2:111111111111:function:helloworld2 .


(string) --






ExcludeManagementEventSources (list) --An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out AWS Key Management Service events by containing "kms.amazonaws.com" . By default, ExcludeManagementEventSources is empty, and AWS KMS events are included in events that are logged to your trail.

(string) --











Exceptions

CloudTrail.Client.exceptions.TrailNotFoundException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException


    :return: {
        'TrailARN': 'string',
        'EventSelectors': [
            {
                'ReadWriteType': 'ReadOnly'|'WriteOnly'|'All',
                'IncludeManagementEvents': True|False,
                'DataResources': [
                    {
                        'Type': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ExcludeManagementEventSources': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
    Start with a letter or number, and end with a letter or number
    Be between 3 and 128 characters
    Have no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are not valid.
    Not be in IP address format (for example, 192.168.5.4)
    
    """
    pass

def get_insight_selectors(TrailName=None):
    """
    Describes the settings for the Insights event selectors that you configured for your trail. GetInsightSelectors shows if CloudTrail Insights event logging is enabled on the trail, and if it is, which insight types are enabled. If you run GetInsightSelectors on a trail that does not have Insights events enabled, the operation throws the exception InsightNotEnabledException
    For more information, see Logging CloudTrail Insights Events for Trails in the AWS CloudTrail User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_insight_selectors(
        TrailName='string'
    )
    
    
    :type TrailName: string
    :param TrailName: [REQUIRED]\nSpecifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:\n\nContain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)\nStart with a letter or number, and end with a letter or number\nBe between 3 and 128 characters\nHave no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are not valid.\nNot be in IP address format (for example, 192.168.5.4)\n\nIf you specify a trail ARN, it must be in the format:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n

    :rtype: dict
ReturnsResponse Syntax{
    'TrailARN': 'string',
    'InsightSelectors': [
        {
            'InsightType': 'ApiCallRateInsight'
        },
    ]
}


Response Structure

(dict) --
TrailARN (string) --The Amazon Resource Name (ARN) of a trail for which you want to get Insights selectors.

InsightSelectors (list) --A JSON string that contains the insight types you want to log on a trail. In this release, only ApiCallRateInsight is supported as an insight type.

(dict) --A JSON string that contains a list of insight types that are logged on a trail.

InsightType (string) --The type of insights to log on a trail. In this release, only ApiCallRateInsight is supported as an insight type.










Exceptions

CloudTrail.Client.exceptions.TrailNotFoundException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.InsightNotEnabledException


    :return: {
        'TrailARN': 'string',
        'InsightSelectors': [
            {
                'InsightType': 'ApiCallRateInsight'
            },
        ]
    }
    
    
    :returns: 
    CloudTrail.Client.exceptions.TrailNotFoundException
    CloudTrail.Client.exceptions.InvalidTrailNameException
    CloudTrail.Client.exceptions.UnsupportedOperationException
    CloudTrail.Client.exceptions.OperationNotPermittedException
    CloudTrail.Client.exceptions.InsightNotEnabledException
    
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

def get_trail(Name=None):
    """
    Returns settings information for a specified trail.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_trail(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name or the Amazon Resource Name (ARN) of the trail for which you want to retrieve settings information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Trail': {
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
        'KmsKeyId': 'string',
        'HasCustomEventSelectors': True|False,
        'HasInsightSelectors': True|False,
        'IsOrganizationTrail': True|False
    }
}


Response Structure

(dict) --
Trail (dict) --The settings for a trail.

Name (string) --Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.

S3BucketName (string) --Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See Amazon S3 Bucket Naming Requirements .

S3KeyPrefix (string) --Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files .The maximum length is 200 characters.

SnsTopicName (string) --This field is no longer in use. Use SnsTopicARN.

SnsTopicARN (string) --Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:

arn:aws:sns:us-east-2:123456789012:MyTopic

IncludeGlobalServiceEvents (boolean) --Set to True to include AWS API calls from AWS global services such as IAM. Otherwise, False .

IsMultiRegionTrail (boolean) --Specifies whether the trail exists only in one region or exists in all regions.

HomeRegion (string) --The region in which the trail was created.

TrailARN (string) --Specifies the ARN of the trail. The format of a trail ARN is:

arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail

LogFileValidationEnabled (boolean) --Specifies whether log file validation is enabled.

CloudWatchLogsLogGroupArn (string) --Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered.

CloudWatchLogsRoleArn (string) --Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.

KmsKeyId (string) --Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the format:

arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012

HasCustomEventSelectors (boolean) --Specifies if the trail has custom event selectors.

HasInsightSelectors (boolean) --Specifies whether a trail has insight types specified in an InsightSelector list.

IsOrganizationTrail (boolean) --Specifies whether the trail is an organization trail.








Exceptions

CloudTrail.Client.exceptions.TrailNotFoundException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException


    :return: {
        'Trail': {
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
            'KmsKeyId': 'string',
            'HasCustomEventSelectors': True|False,
            'HasInsightSelectors': True|False,
            'IsOrganizationTrail': True|False
        }
    }
    
    
    """
    pass

def get_trail_status(Name=None):
    """
    Returns a JSON-formatted list of information about the specified trail. Fields include information on delivery errors, Amazon SNS and Amazon S3 errors, and start and stop logging times for each trail. This operation returns trail status from a single region. To return trail status from all regions, you must call the operation on each region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_trail_status(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nSpecifies the name or the CloudTrail ARN of the trail for which you are requesting status. To get the status of a shadow trail (a replication of the trail in another region), you must specify its ARN. The format of a trail ARN is:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --Returns the objects or data listed below if successful. Otherwise, returns an error.

IsLogging (boolean) --Whether the CloudTrail is currently logging AWS API calls.

LatestDeliveryError (string) --Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver log files to the designated bucket. For more information see the topic Error Responses in the Amazon S3 API Reference.

Note
This error occurs only when there is a problem with the destination S3 bucket and will not occur for timeouts. To resolve the issue, create a new bucket and call UpdateTrail to specify the new bucket, or fix the existing objects so that CloudTrail can again write to the bucket.


LatestNotificationError (string) --Displays any Amazon SNS error that CloudTrail encountered when attempting to send a notification. For more information about Amazon SNS errors, see the Amazon SNS Developer Guide .

LatestDeliveryTime (datetime) --Specifies the date and time that CloudTrail last delivered log files to an account\'s Amazon S3 bucket.

LatestNotificationTime (datetime) --Specifies the date and time of the most recent Amazon SNS notification that CloudTrail has written a new log file to an account\'s Amazon S3 bucket.

StartLoggingTime (datetime) --Specifies the most recent date and time when CloudTrail started recording API calls for an AWS account.

StopLoggingTime (datetime) --Specifies the most recent date and time when CloudTrail stopped recording API calls for an AWS account.

LatestCloudWatchLogsDeliveryError (string) --Displays any CloudWatch Logs error that CloudTrail encountered when attempting to deliver logs to CloudWatch Logs.

LatestCloudWatchLogsDeliveryTime (datetime) --Displays the most recent date and time when CloudTrail delivered logs to CloudWatch Logs.

LatestDigestDeliveryTime (datetime) --Specifies the date and time that CloudTrail last delivered a digest file to an account\'s Amazon S3 bucket.

LatestDigestDeliveryError (string) --Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver a digest file to the designated bucket. For more information see the topic Error Responses in the Amazon S3 API Reference.

Note
This error occurs only when there is a problem with the destination S3 bucket and will not occur for timeouts. To resolve the issue, create a new bucket and call UpdateTrail to specify the new bucket, or fix the existing objects so that CloudTrail can again write to the bucket.


LatestDeliveryAttemptTime (string) --This field is no longer in use.

LatestNotificationAttemptTime (string) --This field is no longer in use.

LatestNotificationAttemptSucceeded (string) --This field is no longer in use.

LatestDeliveryAttemptSucceeded (string) --This field is no longer in use.

TimeLoggingStarted (string) --This field is no longer in use.

TimeLoggingStopped (string) --This field is no longer in use.






Exceptions

CloudTrail.Client.exceptions.TrailNotFoundException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException


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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def list_public_keys(StartTime=None, EndTime=None, NextToken=None):
    """
    Returns all public keys whose private keys were used to sign the digest files within the specified time range. The public key is needed to validate digest files that were signed with its corresponding private key.
    See also: AWS API Documentation
    
    Exceptions
    
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

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Returns the objects or data listed below if successful. Otherwise, returns an error.

PublicKeyList (list) --
Contains an array of PublicKey objects.

Note
The returned public keys may have validity time ranges that overlap.


(dict) --
Contains information about a returned public key.

Value (bytes) --
The DER encoded public key value in PKCS#1 format.

ValidityStartTime (datetime) --
The starting time of validity of the public key.

ValidityEndTime (datetime) --
The ending time of validity of the public key.

Fingerprint (string) --
The fingerprint of the public key.





NextToken (string) --
Reserved for future use.







Exceptions

CloudTrail.Client.exceptions.InvalidTimeRangeException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.InvalidTokenException


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
    
    
    :returns: 
    CloudTrail.Client.exceptions.InvalidTimeRangeException
    CloudTrail.Client.exceptions.UnsupportedOperationException
    CloudTrail.Client.exceptions.OperationNotPermittedException
    CloudTrail.Client.exceptions.InvalidTokenException
    
    """
    pass

def list_tags(ResourceIdList=None, NextToken=None):
    """
    Lists the tags for the trail in the current region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags(
        ResourceIdList=[
            'string',
        ],
        NextToken='string'
    )
    
    
    :type ResourceIdList: list
    :param ResourceIdList: [REQUIRED]\nSpecifies a list of trail ARNs whose tags will be listed. The list has a limit of 20 ARNs. The format of a trail ARN is:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: Reserved for future use.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Returns the objects or data listed below if successful. Otherwise, returns an error.

ResourceTagList (list) --
A list of resource tags.

(dict) --
A resource tag.

ResourceId (string) --
Specifies the ARN of the resource.

TagsList (list) --
A list of tags.

(dict) --
A custom key-value pair associated with a resource such as a CloudTrail trail.

Key (string) --
The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.

Value (string) --
The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.









NextToken (string) --
Reserved for future use.







Exceptions

CloudTrail.Client.exceptions.ResourceNotFoundException
CloudTrail.Client.exceptions.CloudTrailARNInvalidException
CloudTrail.Client.exceptions.ResourceTypeNotSupportedException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.InvalidTokenException


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
    
    
    :returns: 
    CloudTrail.Client.exceptions.ResourceNotFoundException
    CloudTrail.Client.exceptions.CloudTrailARNInvalidException
    CloudTrail.Client.exceptions.ResourceTypeNotSupportedException
    CloudTrail.Client.exceptions.InvalidTrailNameException
    CloudTrail.Client.exceptions.UnsupportedOperationException
    CloudTrail.Client.exceptions.OperationNotPermittedException
    CloudTrail.Client.exceptions.InvalidTokenException
    
    """
    pass

def list_trails(NextToken=None):
    """
    Lists trails that are in the current account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_trails(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the the original call. For example, if the original call specified an AttributeKey of \'Username\' with a value of \'root\', the call with NextToken should include those same parameters.

    :rtype: dict
ReturnsResponse Syntax{
    'Trails': [
        {
            'TrailARN': 'string',
            'Name': 'string',
            'HomeRegion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Trails (list) --Returns the name, ARN, and home region of trails in the current account.

(dict) --Information about a CloudTrail trail, including the trail\'s name, home region, and Amazon Resource Name (ARN).

TrailARN (string) --The ARN of a trail.

Name (string) --The name of a trail.

HomeRegion (string) --The AWS region in which a trail was created.





NextToken (string) --The token to use to get the next page of results after a previous API call. If the token does not appear, there are no more results to return. The token must be passed in with the same parameters as the previous call. For example, if the original call specified an AttributeKey of \'Username\' with a value of \'root\', the call with NextToken should include those same parameters.






Exceptions

CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException


    :return: {
        'Trails': [
            {
                'TrailARN': 'string',
                'Name': 'string',
                'HomeRegion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def lookup_events(LookupAttributes=None, StartTime=None, EndTime=None, EventCategory=None, MaxResults=None, NextToken=None):
    """
    Looks up management events or CloudTrail Insights events that are captured by CloudTrail. You can look up events that occurred in a region within the last 90 days. Lookup supports the following attributes for management events:
    Lookup supports the following attributes for Insights events:
    All attributes are optional. The default number of results returned is 50, with a maximum of 50 possible. The response includes a token that you can use to get the next page of results.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'EventId'|'EventName'|'ReadOnly'|'Username'|'ResourceType'|'ResourceName'|'EventSource'|'AccessKeyId',
                'AttributeValue': 'string'
            },
        ],
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        EventCategory='insight',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type LookupAttributes: list
    :param LookupAttributes: Contains a list of lookup attributes. Currently the list can contain only one item.\n\n(dict) --Specifies an attribute and value that filter the events returned.\n\nAttributeKey (string) -- [REQUIRED]Specifies an attribute on which to filter the events returned.\n\nAttributeValue (string) -- [REQUIRED]Specifies a value for the specified AttributeKey.\n\n\n\n\n

    :type StartTime: datetime
    :param StartTime: Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.

    :type EndTime: datetime
    :param EndTime: Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.

    :type EventCategory: string
    :param EventCategory: Specifies the event category. If you do not specify an event category, events of the category are not returned in the response. For example, if you do not specify insight as the value of EventCategory , no Insights events are returned.

    :type MaxResults: integer
    :param MaxResults: The number of events to return. Possible values are 1 through 50. The default is 50.

    :type NextToken: string
    :param NextToken: The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the the original call. For example, if the original call specified an AttributeKey of \'Username\' with a value of \'root\', the call with NextToken should include those same parameters.

    :rtype: dict

ReturnsResponse Syntax
{
    'Events': [
        {
            'EventId': 'string',
            'EventName': 'string',
            'ReadOnly': 'string',
            'AccessKeyId': 'string',
            'EventTime': datetime(2015, 1, 1),
            'EventSource': 'string',
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


Response Structure

(dict) --
Contains a response to a LookupEvents action.

Events (list) --
A list of events returned based on the lookup attributes specified and the CloudTrail event. The events list is sorted by time. The most recent event is listed first.

(dict) --
Contains information about an event that was returned by a lookup request. The result includes a representation of a CloudTrail event.

EventId (string) --
The CloudTrail ID of the event returned.

EventName (string) --
The name of the event returned.

ReadOnly (string) --
Information about whether the event is a write event or a read event.

AccessKeyId (string) --
The AWS access key ID that was used to sign the request. If the request was made with temporary security credentials, this is the access key ID of the temporary credentials.

EventTime (datetime) --
The date and time of the event returned.

EventSource (string) --
The AWS service that the request was made to.

Username (string) --
A user name or role name of the requester that called the API in the event returned.

Resources (list) --
A list of resources referenced by the event returned.

(dict) --
Specifies the type and name of a resource referenced by an event.

ResourceType (string) --
The type of a resource referenced by the event returned. When the resource type cannot be determined, null is returned. Some examples of resource types are: Instance for EC2, Trail for CloudTrail, DBInstance for RDS, and AccessKey for IAM. To learn more about how to look up and filter events by the resource types supported for a service, see Filtering CloudTrail Events .

ResourceName (string) --
The name of the resource referenced by the event returned. These are user-created names whose values will depend on the environment. For example, the resource name might be "auto-scaling-test-group" for an Auto Scaling Group or "i-1234567" for an EC2 Instance.





CloudTrailEvent (string) --
A JSON string that contains a representation of the event returned.





NextToken (string) --
The token to use to get the next page of results after a previous API call. If the token does not appear, there are no more results to return. The token must be passed in with the same parameters as the previous call. For example, if the original call specified an AttributeKey of \'Username\' with a value of \'root\', the call with NextToken should include those same parameters.







Exceptions

CloudTrail.Client.exceptions.InvalidLookupAttributesException
CloudTrail.Client.exceptions.InvalidTimeRangeException
CloudTrail.Client.exceptions.InvalidMaxResultsException
CloudTrail.Client.exceptions.InvalidNextTokenException
CloudTrail.Client.exceptions.InvalidEventCategoryException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException


    :return: {
        'Events': [
            {
                'EventId': 'string',
                'EventName': 'string',
                'ReadOnly': 'string',
                'AccessKeyId': 'string',
                'EventTime': datetime(2015, 1, 1),
                'EventSource': 'string',
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
    
    
    :returns: 
    Event ID
    Event name
    Event source
    
    """
    pass

def put_event_selectors(TrailName=None, EventSelectors=None):
    """
    Configures an event selector for your trail. Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events.
    When an event occurs in your account, CloudTrail evaluates the event selectors in all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn\'t match any event selector, the trail doesn\'t log the event.
    Example
    The PutEventSelectors operation must be called from the region in which the trail was created; otherwise, an InvalidHomeRegionException is thrown.
    You can configure up to five event selectors for each trail. For more information, see Logging Data and Management Events for Trails and Limits in AWS CloudTrail in the AWS CloudTrail User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_event_selectors(
        TrailName='string',
        EventSelectors=[
            {
                'ReadWriteType': 'ReadOnly'|'WriteOnly'|'All',
                'IncludeManagementEvents': True|False,
                'DataResources': [
                    {
                        'Type': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ExcludeManagementEventSources': [
                    'string',
                ]
            },
        ]
    )
    
    
    :type TrailName: string
    :param TrailName: [REQUIRED]\nSpecifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:\n\nContain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)\nStart with a letter or number, and end with a letter or number\nBe between 3 and 128 characters\nHave no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are invalid.\nNot be in IP address format (for example, 192.168.5.4)\n\nIf you specify a trail ARN, it must be in the format:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n

    :type EventSelectors: list
    :param EventSelectors: [REQUIRED]\nSpecifies the settings for your event selectors. You can configure up to five event selectors for a trail.\n\n(dict) --Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn\'t match any event selector, the trail doesn\'t log the event.\nYou can configure up to five event selectors for a trail.\n\nReadWriteType (string) --Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 GetConsoleOutput is a read-only API operation and RunInstances is a write-only API operation.\nBy default, the value is All .\n\nIncludeManagementEvents (boolean) --Specify if you want your event selector to include management events for your trail.\nFor more information, see Management Events in the AWS CloudTrail User Guide .\nBy default, the value is true .\n\nDataResources (list) --CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.\nFor more information, see Data Events and Limits in AWS CloudTrail in the AWS CloudTrail User Guide .\n\n(dict) --The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors for your trail to log data events. Data events provide information about the resource operations performed on or within a resource itself. These are also known as data plane operations. You can specify up to 250 data resources for a trail.\n\nNote\nThe total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.\n\nThe following example demonstrates how logging works when you configure logging of all data events for an S3 bucket named bucket-1 . In this example, the CloudTrail user specified an empty prefix, and the option to log both Read and Write data events.\n\nA user uploads an image file to bucket-1 .\nThe PutObject API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event.\nA user uploads an object to an Amazon S3 bucket named arn:aws:s3:::bucket-2 .\nThe PutObject API operation occurred for an object in an S3 bucket that the CloudTrail user didn\'t specify for the trail. The trail doesn\xe2\x80\x99t log the event.\n\nThe following example demonstrates how logging works when you configure logging of AWS Lambda data events for a Lambda function named MyLambdaFunction , but not for all AWS Lambda functions.\n\nA user runs a script that includes a call to the MyLambdaFunction function and the MyOtherLambdaFunction function.\nThe Invoke API operation on MyLambdaFunction is an AWS Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for MyLambdaFunction , any invocations of that function are logged. The trail processes and logs the event.\nThe Invoke API operation on MyOtherLambdaFunction is an AWS Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the Invoke operation for MyOtherLambdaFunction does not match the function specified for the trail. The trail doesn\xe2\x80\x99t log the event.\n\n\nType (string) --The resource type in which you want to log data events. You can specify AWS::S3::Object or AWS::Lambda::Function resources.\n\nValues (list) --An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.\n\nTo log data events for all objects in all S3 buckets in your AWS account, specify the prefix as arn:aws:s3::: .\n\n\nNote\nThis will also enable logging of data event activity performed by any user or role in your AWS account, even if that activity is performed on a bucket that belongs to another AWS account.\n\n\nTo log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as arn:aws:s3:::bucket-1/ . The trail logs data events for all objects in this S3 bucket.\nTo log data events for specific objects, specify the S3 bucket and object prefix such as arn:aws:s3:::bucket-1/example-images . The trail logs data events for objects in this S3 bucket that match the prefix.\nTo log data events for all functions in your AWS account, specify the prefix as arn:aws:lambda .\n\n\nNote\nThis will also enable logging of Invoke activity performed by any user or role in your AWS account, even if that activity is performed on a function that belongs to another AWS account.\n\n\nTo log data events for a specific Lambda function, specify the function ARN.\n\n\nNote\nLambda function ARNs are exact. For example, if you specify a function ARN arn:aws:lambda:us-west-2:111111111111:function:helloworld , data events will only be logged for arn:aws:lambda:us-west-2:111111111111:function:helloworld . They will not be logged for arn:aws:lambda:us-west-2:111111111111:function:helloworld2 .\n\n\n(string) --\n\n\n\n\n\n\nExcludeManagementEventSources (list) --An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out AWS Key Management Service events by containing 'kms.amazonaws.com' . By default, ExcludeManagementEventSources is empty, and AWS KMS events are included in events that are logged to your trail.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TrailARN': 'string',
    'EventSelectors': [
        {
            'ReadWriteType': 'ReadOnly'|'WriteOnly'|'All',
            'IncludeManagementEvents': True|False,
            'DataResources': [
                {
                    'Type': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            'ExcludeManagementEventSources': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --

TrailARN (string) --
Specifies the ARN of the trail that was updated with event selectors. The format of a trail ARN is:

arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail


EventSelectors (list) --
Specifies the event selectors configured for your trail.

(dict) --
Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn\'t match any event selector, the trail doesn\'t log the event.
You can configure up to five event selectors for a trail.

ReadWriteType (string) --
Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 GetConsoleOutput is a read-only API operation and RunInstances is a write-only API operation.
By default, the value is All .

IncludeManagementEvents (boolean) --
Specify if you want your event selector to include management events for your trail.
For more information, see Management Events in the AWS CloudTrail User Guide .
By default, the value is true .

DataResources (list) --
CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.
For more information, see Data Events and Limits in AWS CloudTrail in the AWS CloudTrail User Guide .

(dict) --
The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors for your trail to log data events. Data events provide information about the resource operations performed on or within a resource itself. These are also known as data plane operations. You can specify up to 250 data resources for a trail.

Note
The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

The following example demonstrates how logging works when you configure logging of all data events for an S3 bucket named bucket-1 . In this example, the CloudTrail user specified an empty prefix, and the option to log both Read and Write data events.

A user uploads an image file to bucket-1 .
The PutObject API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event.
A user uploads an object to an Amazon S3 bucket named arn:aws:s3:::bucket-2 .
The PutObject API operation occurred for an object in an S3 bucket that the CloudTrail user didn\'t specify for the trail. The trail doesn\xe2\x80\x99t log the event.

The following example demonstrates how logging works when you configure logging of AWS Lambda data events for a Lambda function named MyLambdaFunction , but not for all AWS Lambda functions.

A user runs a script that includes a call to the MyLambdaFunction function and the MyOtherLambdaFunction function.
The Invoke API operation on MyLambdaFunction is an AWS Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for MyLambdaFunction , any invocations of that function are logged. The trail processes and logs the event.
The Invoke API operation on MyOtherLambdaFunction is an AWS Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the Invoke operation for MyOtherLambdaFunction does not match the function specified for the trail. The trail doesn\xe2\x80\x99t log the event.


Type (string) --
The resource type in which you want to log data events. You can specify AWS::S3::Object or AWS::Lambda::Function resources.

Values (list) --
An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.

To log data events for all objects in all S3 buckets in your AWS account, specify the prefix as arn:aws:s3::: .


Note
This will also enable logging of data event activity performed by any user or role in your AWS account, even if that activity is performed on a bucket that belongs to another AWS account.


To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as arn:aws:s3:::bucket-1/ . The trail logs data events for all objects in this S3 bucket.
To log data events for specific objects, specify the S3 bucket and object prefix such as arn:aws:s3:::bucket-1/example-images . The trail logs data events for objects in this S3 bucket that match the prefix.
To log data events for all functions in your AWS account, specify the prefix as arn:aws:lambda .


Note
This will also enable logging of Invoke activity performed by any user or role in your AWS account, even if that activity is performed on a function that belongs to another AWS account.


To log data events for a specific Lambda function, specify the function ARN.


Note
Lambda function ARNs are exact. For example, if you specify a function ARN arn:aws:lambda:us-west-2:111111111111:function:helloworld , data events will only be logged for arn:aws:lambda:us-west-2:111111111111:function:helloworld . They will not be logged for arn:aws:lambda:us-west-2:111111111111:function:helloworld2 .


(string) --






ExcludeManagementEventSources (list) --
An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out AWS Key Management Service events by containing "kms.amazonaws.com" . By default, ExcludeManagementEventSources is empty, and AWS KMS events are included in events that are logged to your trail.

(string) --












Exceptions

CloudTrail.Client.exceptions.TrailNotFoundException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.InvalidHomeRegionException
CloudTrail.Client.exceptions.InvalidEventSelectorsException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
CloudTrail.Client.exceptions.InsufficientDependencyServiceAccessPermissionException


    :return: {
        'TrailARN': 'string',
        'EventSelectors': [
            {
                'ReadWriteType': 'ReadOnly'|'WriteOnly'|'All',
                'IncludeManagementEvents': True|False,
                'DataResources': [
                    {
                        'Type': 'string',
                        'Values': [
                            'string',
                        ]
                    },
                ],
                'ExcludeManagementEventSources': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    TrailName (string) -- [REQUIRED]
    Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:
    
    Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
    Start with a letter or number, and end with a letter or number
    Be between 3 and 128 characters
    Have no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are invalid.
    Not be in IP address format (for example, 192.168.5.4)
    
    If you specify a trail ARN, it must be in the format:
    
    arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail
    
    EventSelectors (list) -- [REQUIRED]
    Specifies the settings for your event selectors. You can configure up to five event selectors for a trail.
    
    (dict) --Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn\'t match any event selector, the trail doesn\'t log the event.
    You can configure up to five event selectors for a trail.
    
    ReadWriteType (string) --Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 GetConsoleOutput is a read-only API operation and RunInstances is a write-only API operation.
    By default, the value is All .
    
    IncludeManagementEvents (boolean) --Specify if you want your event selector to include management events for your trail.
    For more information, see Management Events in the AWS CloudTrail User Guide .
    By default, the value is true .
    
    DataResources (list) --CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.
    For more information, see Data Events and Limits in AWS CloudTrail in the AWS CloudTrail User Guide .
    
    (dict) --The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors for your trail to log data events. Data events provide information about the resource operations performed on or within a resource itself. These are also known as data plane operations. You can specify up to 250 data resources for a trail.
    
    Note
    The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.
    
    The following example demonstrates how logging works when you configure logging of all data events for an S3 bucket named bucket-1 . In this example, the CloudTrail user specified an empty prefix, and the option to log both Read and Write data events.
    
    A user uploads an image file to bucket-1 .
    The PutObject API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event.
    A user uploads an object to an Amazon S3 bucket named arn:aws:s3:::bucket-2 .
    The PutObject API operation occurred for an object in an S3 bucket that the CloudTrail user didn\'t specify for the trail. The trail doesn\xe2\x80\x99t log the event.
    
    The following example demonstrates how logging works when you configure logging of AWS Lambda data events for a Lambda function named MyLambdaFunction , but not for all AWS Lambda functions.
    
    A user runs a script that includes a call to the MyLambdaFunction function and the MyOtherLambdaFunction function.
    The Invoke API operation on MyLambdaFunction is an AWS Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for MyLambdaFunction , any invocations of that function are logged. The trail processes and logs the event.
    The Invoke API operation on MyOtherLambdaFunction is an AWS Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the Invoke operation for MyOtherLambdaFunction does not match the function specified for the trail. The trail doesn\xe2\x80\x99t log the event.
    
    
    Type (string) --The resource type in which you want to log data events. You can specify AWS::S3::Object or AWS::Lambda::Function resources.
    
    Values (list) --An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.
    
    To log data events for all objects in all S3 buckets in your AWS account, specify the prefix as arn:aws:s3::: .
    
    
    Note
    This will also enable logging of data event activity performed by any user or role in your AWS account, even if that activity is performed on a bucket that belongs to another AWS account.
    
    
    To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as arn:aws:s3:::bucket-1/ . The trail logs data events for all objects in this S3 bucket.
    To log data events for specific objects, specify the S3 bucket and object prefix such as arn:aws:s3:::bucket-1/example-images . The trail logs data events for objects in this S3 bucket that match the prefix.
    To log data events for all functions in your AWS account, specify the prefix as arn:aws:lambda .
    
    
    Note
    This will also enable logging of Invoke activity performed by any user or role in your AWS account, even if that activity is performed on a function that belongs to another AWS account.
    
    
    To log data events for a specific Lambda function, specify the function ARN.
    
    
    Note
    Lambda function ARNs are exact. For example, if you specify a function ARN arn:aws:lambda:us-west-2:111111111111:function:helloworld , data events will only be logged for arn:aws:lambda:us-west-2:111111111111:function:helloworld . They will not be logged for arn:aws:lambda:us-west-2:111111111111:function:helloworld2 .
    
    
    (string) --
    
    
    
    
    
    
    ExcludeManagementEventSources (list) --An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out AWS Key Management Service events by containing "kms.amazonaws.com" . By default, ExcludeManagementEventSources is empty, and AWS KMS events are included in events that are logged to your trail.
    
    (string) --
    
    
    
    
    
    
    
    """
    pass

def put_insight_selectors(TrailName=None, InsightSelectors=None):
    """
    Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing trail. You also use PutInsightSelectors to turn off Insights event logging, by passing an empty list of insight types. In this release, only ApiCallRateInsight is supported as an Insights selector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_insight_selectors(
        TrailName='string',
        InsightSelectors=[
            {
                'InsightType': 'ApiCallRateInsight'
            },
        ]
    )
    
    
    :type TrailName: string
    :param TrailName: [REQUIRED]\nThe name of the CloudTrail trail for which you want to change or add Insights selectors.\n

    :type InsightSelectors: list
    :param InsightSelectors: [REQUIRED]\nA JSON string that contains the insight types you want to log on a trail. In this release, only ApiCallRateInsight is supported as an insight type.\n\n(dict) --A JSON string that contains a list of insight types that are logged on a trail.\n\nInsightType (string) --The type of insights to log on a trail. In this release, only ApiCallRateInsight is supported as an insight type.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TrailARN': 'string',
    'InsightSelectors': [
        {
            'InsightType': 'ApiCallRateInsight'
        },
    ]
}


Response Structure

(dict) --

TrailARN (string) --
The Amazon Resource Name (ARN) of a trail for which you want to change or add Insights selectors.

InsightSelectors (list) --
A JSON string that contains the insight types you want to log on a trail. In this release, only ApiCallRateInsight is supported as an insight type.

(dict) --
A JSON string that contains a list of insight types that are logged on a trail.

InsightType (string) --
The type of insights to log on a trail. In this release, only ApiCallRateInsight is supported as an insight type.











Exceptions

CloudTrail.Client.exceptions.TrailNotFoundException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.InvalidHomeRegionException
CloudTrail.Client.exceptions.InvalidInsightSelectorsException
CloudTrail.Client.exceptions.InsufficientS3BucketPolicyException
CloudTrail.Client.exceptions.InsufficientEncryptionPolicyException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.NotOrganizationMasterAccountException


    :return: {
        'TrailARN': 'string',
        'InsightSelectors': [
            {
                'InsightType': 'ApiCallRateInsight'
            },
        ]
    }
    
    
    :returns: 
    CloudTrail.Client.exceptions.TrailNotFoundException
    CloudTrail.Client.exceptions.InvalidTrailNameException
    CloudTrail.Client.exceptions.InvalidHomeRegionException
    CloudTrail.Client.exceptions.InvalidInsightSelectorsException
    CloudTrail.Client.exceptions.InsufficientS3BucketPolicyException
    CloudTrail.Client.exceptions.InsufficientEncryptionPolicyException
    CloudTrail.Client.exceptions.UnsupportedOperationException
    CloudTrail.Client.exceptions.OperationNotPermittedException
    CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
    
    """
    pass

def remove_tags(ResourceId=None, TagsList=None):
    """
    Removes the specified tags from a trail.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param ResourceId: [REQUIRED]\nSpecifies the ARN of the trail from which tags should be removed. The format of a trail ARN is:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n

    :type TagsList: list
    :param TagsList: Specifies a list of tags to be removed.\n\n(dict) --A custom key-value pair associated with a resource such as a CloudTrail trail.\n\nKey (string) -- [REQUIRED]The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.\n\nValue (string) --The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Returns the objects or data listed below if successful. Otherwise, returns an error.





Exceptions

CloudTrail.Client.exceptions.ResourceNotFoundException
CloudTrail.Client.exceptions.CloudTrailARNInvalidException
CloudTrail.Client.exceptions.ResourceTypeNotSupportedException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.InvalidTagParameterException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.NotOrganizationMasterAccountException


    :return: {}
    
    
    :returns: 
    CloudTrail.Client.exceptions.ResourceNotFoundException
    CloudTrail.Client.exceptions.CloudTrailARNInvalidException
    CloudTrail.Client.exceptions.ResourceTypeNotSupportedException
    CloudTrail.Client.exceptions.InvalidTrailNameException
    CloudTrail.Client.exceptions.InvalidTagParameterException
    CloudTrail.Client.exceptions.UnsupportedOperationException
    CloudTrail.Client.exceptions.OperationNotPermittedException
    CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
    
    """
    pass

def start_logging(Name=None):
    """
    Starts the recording of AWS API calls and log file delivery for a trail. For a trail that is enabled in all regions, this operation must be called from the region in which the trail was created. This operation cannot be called on the shadow trails (replicated trails in other regions) of a trail that is enabled in all regions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_logging(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nSpecifies the name or the CloudTrail ARN of the trail for which CloudTrail logs AWS API calls. The format of a trail ARN is:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Returns the objects or data listed below if successful. Otherwise, returns an error.




Exceptions

CloudTrail.Client.exceptions.TrailNotFoundException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.InvalidHomeRegionException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
CloudTrail.Client.exceptions.InsufficientDependencyServiceAccessPermissionException


    :return: {}
    
    
    """
    pass

def stop_logging(Name=None):
    """
    Suspends the recording of AWS API calls and log file delivery for the specified trail. Under most circumstances, there is no need to use this action. You can update a trail without stopping it first. This action is the only way to stop recording. For a trail enabled in all regions, this operation must be called from the region in which the trail was created, or an InvalidHomeRegionException will occur. This operation cannot be called on the shadow trails (replicated trails in other regions) of a trail enabled in all regions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_logging(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nSpecifies the name or the CloudTrail ARN of the trail for which CloudTrail will stop logging AWS API calls. The format of a trail ARN is:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Returns the objects or data listed below if successful. Otherwise, returns an error.




Exceptions

CloudTrail.Client.exceptions.TrailNotFoundException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.InvalidHomeRegionException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
CloudTrail.Client.exceptions.InsufficientDependencyServiceAccessPermissionException


    :return: {}
    
    
    """
    pass

def update_trail(Name=None, S3BucketName=None, S3KeyPrefix=None, SnsTopicName=None, IncludeGlobalServiceEvents=None, IsMultiRegionTrail=None, EnableLogFileValidation=None, CloudWatchLogsLogGroupArn=None, CloudWatchLogsRoleArn=None, KmsKeyId=None, IsOrganizationTrail=None):
    """
    Updates the settings that specify delivery of log files. Changes to a trail do not require stopping the CloudTrail service. Use this action to designate an existing bucket for log delivery. If the existing bucket has previously been a target for CloudTrail log files, an IAM policy exists for the bucket. UpdateTrail must be called from the region in which the trail was created; otherwise, an InvalidHomeRegionException is thrown.
    See also: AWS API Documentation
    
    Exceptions
    
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
        KmsKeyId='string',
        IsOrganizationTrail=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nSpecifies the name of the trail or trail ARN. If Name is a trail name, the string must meet the following requirements:\n\nContain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)\nStart with a letter or number, and end with a letter or number\nBe between 3 and 128 characters\nHave no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are invalid.\nNot be in IP address format (for example, 192.168.5.4)\n\nIf Name is a trail ARN, it must be in the format:\n\narn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail\n

    :type S3BucketName: string
    :param S3BucketName: Specifies the name of the Amazon S3 bucket designated for publishing log files. See Amazon S3 Bucket Naming Requirements .

    :type S3KeyPrefix: string
    :param S3KeyPrefix: Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files . The maximum length is 200 characters.

    :type SnsTopicName: string
    :param SnsTopicName: Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.

    :type IncludeGlobalServiceEvents: boolean
    :param IncludeGlobalServiceEvents: Specifies whether the trail is publishing events from global services such as IAM to the log files.

    :type IsMultiRegionTrail: boolean
    :param IsMultiRegionTrail: Specifies whether the trail applies only to the current region or to all regions. The default is false. If the trail exists only in the current region and this value is set to true, shadow trails (replications of the trail) will be created in the other regions. If the trail exists in all regions and this value is set to false, the trail will remain in the region where it was created, and its shadow trails in other regions will be deleted. As a best practice, consider using trails that log events in all regions.

    :type EnableLogFileValidation: boolean
    :param EnableLogFileValidation: Specifies whether log file validation is enabled. The default is false.\n\nNote\nWhen you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail will not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.\n\n

    :type CloudWatchLogsLogGroupArn: string
    :param CloudWatchLogsLogGroupArn: Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.

    :type CloudWatchLogsRoleArn: string
    :param CloudWatchLogsRoleArn: Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.

    :type KmsKeyId: string
    :param KmsKeyId: Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.\nExamples:\n\nalias/MyAliasName\narn:aws:kms:us-east-2:123456789012:alias/MyAliasName\narn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012\n12345678-1234-1234-1234-123456789012\n\n

    :type IsOrganizationTrail: boolean
    :param IsOrganizationTrail: Specifies whether the trail is applied to all accounts in an organization in AWS Organizations, or only for the current AWS account. The default is false, and cannot be true unless the call is made on behalf of an AWS account that is the master account for an organization in AWS Organizations. If the trail is not an organization trail and this is set to true, the trail will be created in all AWS accounts that belong to the organization. If the trail is an organization trail and this is set to false, the trail will remain in the current AWS account but be deleted from all member accounts in the organization.

    :rtype: dict

ReturnsResponse Syntax
{
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
    'KmsKeyId': 'string',
    'IsOrganizationTrail': True|False
}


Response Structure

(dict) --
Returns the objects or data listed below if successful. Otherwise, returns an error.

Name (string) --
Specifies the name of the trail.

S3BucketName (string) --
Specifies the name of the Amazon S3 bucket designated for publishing log files.

S3KeyPrefix (string) --
Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files .

SnsTopicName (string) --
This field is no longer in use. Use SnsTopicARN.

SnsTopicARN (string) --
Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:

arn:aws:sns:us-east-2:123456789012:MyTopic


IncludeGlobalServiceEvents (boolean) --
Specifies whether the trail is publishing events from global services such as IAM to the log files.

IsMultiRegionTrail (boolean) --
Specifies whether the trail exists in one region or in all regions.

TrailARN (string) --
Specifies the ARN of the trail that was updated. The format of a trail ARN is:

arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail


LogFileValidationEnabled (boolean) --
Specifies whether log file integrity validation is enabled.

CloudWatchLogsLogGroupArn (string) --
Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs will be delivered.

CloudWatchLogsRoleArn (string) --
Specifies the role for the CloudWatch Logs endpoint to assume to write to a user\'s log group.

KmsKeyId (string) --
Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the format:

arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012


IsOrganizationTrail (boolean) --
Specifies whether the trail is an organization trail.







Exceptions

CloudTrail.Client.exceptions.S3BucketDoesNotExistException
CloudTrail.Client.exceptions.InsufficientS3BucketPolicyException
CloudTrail.Client.exceptions.InsufficientSnsTopicPolicyException
CloudTrail.Client.exceptions.InsufficientEncryptionPolicyException
CloudTrail.Client.exceptions.TrailNotFoundException
CloudTrail.Client.exceptions.InvalidS3BucketNameException
CloudTrail.Client.exceptions.InvalidS3PrefixException
CloudTrail.Client.exceptions.InvalidSnsTopicNameException
CloudTrail.Client.exceptions.InvalidKmsKeyIdException
CloudTrail.Client.exceptions.InvalidTrailNameException
CloudTrail.Client.exceptions.TrailNotProvidedException
CloudTrail.Client.exceptions.InvalidEventSelectorsException
CloudTrail.Client.exceptions.InvalidParameterCombinationException
CloudTrail.Client.exceptions.InvalidHomeRegionException
CloudTrail.Client.exceptions.KmsKeyNotFoundException
CloudTrail.Client.exceptions.KmsKeyDisabledException
CloudTrail.Client.exceptions.KmsException
CloudTrail.Client.exceptions.InvalidCloudWatchLogsLogGroupArnException
CloudTrail.Client.exceptions.InvalidCloudWatchLogsRoleArnException
CloudTrail.Client.exceptions.CloudWatchLogsDeliveryUnavailableException
CloudTrail.Client.exceptions.UnsupportedOperationException
CloudTrail.Client.exceptions.OperationNotPermittedException
CloudTrail.Client.exceptions.CloudTrailAccessNotEnabledException
CloudTrail.Client.exceptions.InsufficientDependencyServiceAccessPermissionException
CloudTrail.Client.exceptions.OrganizationsNotInUseException
CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
CloudTrail.Client.exceptions.OrganizationNotInAllFeaturesModeException


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
        'KmsKeyId': 'string',
        'IsOrganizationTrail': True|False
    }
    
    
    :returns: 
    CloudTrail.Client.exceptions.S3BucketDoesNotExistException
    CloudTrail.Client.exceptions.InsufficientS3BucketPolicyException
    CloudTrail.Client.exceptions.InsufficientSnsTopicPolicyException
    CloudTrail.Client.exceptions.InsufficientEncryptionPolicyException
    CloudTrail.Client.exceptions.TrailNotFoundException
    CloudTrail.Client.exceptions.InvalidS3BucketNameException
    CloudTrail.Client.exceptions.InvalidS3PrefixException
    CloudTrail.Client.exceptions.InvalidSnsTopicNameException
    CloudTrail.Client.exceptions.InvalidKmsKeyIdException
    CloudTrail.Client.exceptions.InvalidTrailNameException
    CloudTrail.Client.exceptions.TrailNotProvidedException
    CloudTrail.Client.exceptions.InvalidEventSelectorsException
    CloudTrail.Client.exceptions.InvalidParameterCombinationException
    CloudTrail.Client.exceptions.InvalidHomeRegionException
    CloudTrail.Client.exceptions.KmsKeyNotFoundException
    CloudTrail.Client.exceptions.KmsKeyDisabledException
    CloudTrail.Client.exceptions.KmsException
    CloudTrail.Client.exceptions.InvalidCloudWatchLogsLogGroupArnException
    CloudTrail.Client.exceptions.InvalidCloudWatchLogsRoleArnException
    CloudTrail.Client.exceptions.CloudWatchLogsDeliveryUnavailableException
    CloudTrail.Client.exceptions.UnsupportedOperationException
    CloudTrail.Client.exceptions.OperationNotPermittedException
    CloudTrail.Client.exceptions.CloudTrailAccessNotEnabledException
    CloudTrail.Client.exceptions.InsufficientDependencyServiceAccessPermissionException
    CloudTrail.Client.exceptions.OrganizationsNotInUseException
    CloudTrail.Client.exceptions.NotOrganizationMasterAccountException
    CloudTrail.Client.exceptions.OrganizationNotInAllFeaturesModeException
    
    """
    pass

