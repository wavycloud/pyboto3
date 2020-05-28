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

def create_lifecycle_policy(ExecutionRoleArn=None, Description=None, State=None, PolicyDetails=None, Tags=None):
    """
    Creates a policy to manage the lifecycle of the specified AWS resources. You can create up to 100 lifecycle policies.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_lifecycle_policy(
        ExecutionRoleArn='string',
        Description='string',
        State='ENABLED'|'DISABLED',
        PolicyDetails={
            'PolicyType': 'EBS_SNAPSHOT_MANAGEMENT',
            'ResourceTypes': [
                'VOLUME'|'INSTANCE',
            ],
            'TargetTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'Schedules': [
                {
                    'Name': 'string',
                    'CopyTags': True|False,
                    'TagsToAdd': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'VariableTags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'CreateRule': {
                        'Interval': 123,
                        'IntervalUnit': 'HOURS',
                        'Times': [
                            'string',
                        ],
                        'CronExpression': 'string'
                    },
                    'RetainRule': {
                        'Count': 123,
                        'Interval': 123,
                        'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS'
                    },
                    'FastRestoreRule': {
                        'Count': 123,
                        'Interval': 123,
                        'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS',
                        'AvailabilityZones': [
                            'string',
                        ]
                    },
                    'CrossRegionCopyRules': [
                        {
                            'TargetRegion': 'string',
                            'Encrypted': True|False,
                            'CmkArn': 'string',
                            'CopyTags': True|False,
                            'RetainRule': {
                                'Interval': 123,
                                'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS'
                            }
                        },
                    ]
                },
            ],
            'Parameters': {
                'ExcludeBootVolume': True|False
            }
        },
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ExecutionRoleArn: string
    :param ExecutionRoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.\n

    :type Description: string
    :param Description: [REQUIRED]\nA description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are supported.\n

    :type State: string
    :param State: [REQUIRED]\nThe desired activation state of the lifecycle policy after creation.\n

    :type PolicyDetails: dict
    :param PolicyDetails: [REQUIRED]\nThe configuration details of the lifecycle policy.\n\nPolicyType (string) --The valid target resource types and actions a policy can manage. The default is EBS_SNAPSHOT_MANAGEMENT.\n\nResourceTypes (list) --The resource type. Use VOLUME to create snapshots of individual volumes or use INSTANCE to create multi-volume snapshots from the volumes for an instance.\n\n(string) --\n\n\nTargetTags (list) --The single tag that identifies targeted resources for this policy.\n\n(dict) --Specifies a tag for a resource.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The tag value.\n\n\n\n\n\nSchedules (list) --The schedule of policy-defined actions.\n\n(dict) --Specifies a backup schedule.\n\nName (string) --The name of the schedule.\n\nCopyTags (boolean) --Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.\n\nTagsToAdd (list) --The tags to apply to policy-created resources. These user-defined tags are in addition to the AWS-added lifecycle tags.\n\n(dict) --Specifies a tag for a resource.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The tag value.\n\n\n\n\n\nVariableTags (list) --A collection of key/value pairs with values determined dynamically when the policy is executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two following formats: $(instance-id) or $(timestamp) . Variable tags are only valid for EBS Snapshot Management \xe2\x80\x93 Instance policies.\n\n(dict) --Specifies a tag for a resource.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The tag value.\n\n\n\n\n\nCreateRule (dict) --The creation rule.\n\nInterval (integer) --The interval between snapshots. The supported values are 1, 2, 3, 4, 6, 8, 12, and 24.\n\nIntervalUnit (string) --The interval unit.\n\nTimes (list) --The time, in UTC, to start the operation. The supported format is hh:mm.\nThe operation occurs within a one-hour window following the specified time. If you do not specify a time, Amazon DLM selects a time within the next 24 hours.\n\n(string) --\n\n\nCronExpression (string) --The schedule, as a Cron expression. The schedule interval must be between 1 hour and 1 year. For more information, see Cron expressions in the Amazon CloudWatch User Guide .\n\n\n\nRetainRule (dict) --The retention rule.\n\nCount (integer) --The number of snapshots to retain for each volume, up to a maximum of 1000.\n\nInterval (integer) --The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.\n\nIntervalUnit (string) --The unit of time for time-based retention.\n\n\n\nFastRestoreRule (dict) --The rule for enabling fast snapshot restore.\n\nCount (integer) --The number of snapshots to be enabled with fast snapshot restore.\n\nInterval (integer) --The amount of time to enable fast snapshot restore. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.\n\nIntervalUnit (string) --The unit of time for enabling fast snapshot restore.\n\nAvailabilityZones (list) -- [REQUIRED]The Availability Zones in which to enable fast snapshot restore.\n\n(string) --\n\n\n\n\nCrossRegionCopyRules (list) --The rule for cross-Region snapshot copies.\n\n(dict) --Specifies a rule for cross-Region snapshot copies.\n\nTargetRegion (string) -- [REQUIRED]The target Region.\n\nEncrypted (boolean) -- [REQUIRED]To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or if encryption by default is not enabled.\n\nCmkArn (string) --The Amazon Resource Name (ARN) of the AWS KMS customer master key (CMK) to use for EBS encryption. If this parameter is not specified, your AWS managed CMK for EBS is used.\n\nCopyTags (boolean) --Copy all user-defined tags from the source snapshot to the copied snapshot.\n\nRetainRule (dict) --The retention rule.\n\nInterval (integer) --The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.\n\nIntervalUnit (string) --The unit of time for time-based retention.\n\n\n\n\n\n\n\n\n\n\n\nParameters (dict) --A set of optional parameters for the policy.\n\nExcludeBootVolume (boolean) --[EBS Snapshot Management \xe2\x80\x93 Instance policies only] Indicates whether to exclude the root volume from snapshots created using CreateSnapshots . The default is false.\n\n\n\n\n

    :type Tags: dict
    :param Tags: The tags to apply to the lifecycle policy during creation.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PolicyId': 'string'
}


Response Structure

(dict) --

PolicyId (string) --
The identifier of the lifecycle policy.







Exceptions

DLM.Client.exceptions.InvalidRequestException
DLM.Client.exceptions.LimitExceededException
DLM.Client.exceptions.InternalServerException


    :return: {
        'PolicyId': 'string'
    }
    
    
    :returns: 
    DLM.Client.exceptions.InvalidRequestException
    DLM.Client.exceptions.LimitExceededException
    DLM.Client.exceptions.InternalServerException
    
    """
    pass

def delete_lifecycle_policy(PolicyId=None):
    """
    Deletes the specified lifecycle policy and halts the automated operations that the policy specified.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_lifecycle_policy(
        PolicyId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]\nThe identifier of the lifecycle policy.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

DLM.Client.exceptions.ResourceNotFoundException
DLM.Client.exceptions.InternalServerException
DLM.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    DLM.Client.exceptions.ResourceNotFoundException
    DLM.Client.exceptions.InternalServerException
    DLM.Client.exceptions.LimitExceededException
    
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

def get_lifecycle_policies(PolicyIds=None, State=None, ResourceTypes=None, TargetTags=None, TagsToAdd=None):
    """
    Gets summary information about all or the specified data lifecycle policies.
    To get complete information about a policy, use  GetLifecyclePolicy .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_lifecycle_policies(
        PolicyIds=[
            'string',
        ],
        State='ENABLED'|'DISABLED'|'ERROR',
        ResourceTypes=[
            'VOLUME'|'INSTANCE',
        ],
        TargetTags=[
            'string',
        ],
        TagsToAdd=[
            'string',
        ]
    )
    
    
    :type PolicyIds: list
    :param PolicyIds: The identifiers of the data lifecycle policies.\n\n(string) --\n\n

    :type State: string
    :param State: The activation state.

    :type ResourceTypes: list
    :param ResourceTypes: The resource type.\n\n(string) --\n\n

    :type TargetTags: list
    :param TargetTags: The target tag for a policy.\nTags are strings in the format key=value .\n\n(string) --\n\n

    :type TagsToAdd: list
    :param TagsToAdd: The tags to add to objects created by the policy.\nTags are strings in the format key=value .\nThese user-defined tags are added in addition to the AWS-added lifecycle tags.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Policies': [
        {
            'PolicyId': 'string',
            'Description': 'string',
            'State': 'ENABLED'|'DISABLED'|'ERROR',
            'Tags': {
                'string': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

Policies (list) --
Summary information about the lifecycle policies.

(dict) --
Summary information about a lifecycle policy.

PolicyId (string) --
The identifier of the lifecycle policy.

Description (string) --
The description of the lifecycle policy.

State (string) --
The activation state of the lifecycle policy.

Tags (dict) --
The tags.

(string) --
(string) --














Exceptions

DLM.Client.exceptions.ResourceNotFoundException
DLM.Client.exceptions.InvalidRequestException
DLM.Client.exceptions.InternalServerException
DLM.Client.exceptions.LimitExceededException


    :return: {
        'Policies': [
            {
                'PolicyId': 'string',
                'Description': 'string',
                'State': 'ENABLED'|'DISABLED'|'ERROR',
                'Tags': {
                    'string': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_lifecycle_policy(PolicyId=None):
    """
    Gets detailed information about the specified lifecycle policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_lifecycle_policy(
        PolicyId='string'
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]\nThe identifier of the lifecycle policy.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Policy': {
        'PolicyId': 'string',
        'Description': 'string',
        'State': 'ENABLED'|'DISABLED'|'ERROR',
        'StatusMessage': 'string',
        'ExecutionRoleArn': 'string',
        'DateCreated': datetime(2015, 1, 1),
        'DateModified': datetime(2015, 1, 1),
        'PolicyDetails': {
            'PolicyType': 'EBS_SNAPSHOT_MANAGEMENT',
            'ResourceTypes': [
                'VOLUME'|'INSTANCE',
            ],
            'TargetTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'Schedules': [
                {
                    'Name': 'string',
                    'CopyTags': True|False,
                    'TagsToAdd': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'VariableTags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'CreateRule': {
                        'Interval': 123,
                        'IntervalUnit': 'HOURS',
                        'Times': [
                            'string',
                        ],
                        'CronExpression': 'string'
                    },
                    'RetainRule': {
                        'Count': 123,
                        'Interval': 123,
                        'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS'
                    },
                    'FastRestoreRule': {
                        'Count': 123,
                        'Interval': 123,
                        'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS',
                        'AvailabilityZones': [
                            'string',
                        ]
                    },
                    'CrossRegionCopyRules': [
                        {
                            'TargetRegion': 'string',
                            'Encrypted': True|False,
                            'CmkArn': 'string',
                            'CopyTags': True|False,
                            'RetainRule': {
                                'Interval': 123,
                                'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS'
                            }
                        },
                    ]
                },
            ],
            'Parameters': {
                'ExcludeBootVolume': True|False
            }
        },
        'Tags': {
            'string': 'string'
        },
        'PolicyArn': 'string'
    }
}


Response Structure

(dict) --
Policy (dict) --Detailed information about the lifecycle policy.

PolicyId (string) --The identifier of the lifecycle policy.

Description (string) --The description of the lifecycle policy.

State (string) --The activation state of the lifecycle policy.

StatusMessage (string) --The description of the status.

ExecutionRoleArn (string) --The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.

DateCreated (datetime) --The local date and time when the lifecycle policy was created.

DateModified (datetime) --The local date and time when the lifecycle policy was last modified.

PolicyDetails (dict) --The configuration of the lifecycle policy

PolicyType (string) --The valid target resource types and actions a policy can manage. The default is EBS_SNAPSHOT_MANAGEMENT.

ResourceTypes (list) --The resource type. Use VOLUME to create snapshots of individual volumes or use INSTANCE to create multi-volume snapshots from the volumes for an instance.

(string) --


TargetTags (list) --The single tag that identifies targeted resources for this policy.

(dict) --Specifies a tag for a resource.

Key (string) --The tag key.

Value (string) --The tag value.





Schedules (list) --The schedule of policy-defined actions.

(dict) --Specifies a backup schedule.

Name (string) --The name of the schedule.

CopyTags (boolean) --Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.

TagsToAdd (list) --The tags to apply to policy-created resources. These user-defined tags are in addition to the AWS-added lifecycle tags.

(dict) --Specifies a tag for a resource.

Key (string) --The tag key.

Value (string) --The tag value.





VariableTags (list) --A collection of key/value pairs with values determined dynamically when the policy is executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two following formats: $(instance-id) or $(timestamp) . Variable tags are only valid for EBS Snapshot Management \xe2\x80\x93 Instance policies.

(dict) --Specifies a tag for a resource.

Key (string) --The tag key.

Value (string) --The tag value.





CreateRule (dict) --The creation rule.

Interval (integer) --The interval between snapshots. The supported values are 1, 2, 3, 4, 6, 8, 12, and 24.

IntervalUnit (string) --The interval unit.

Times (list) --The time, in UTC, to start the operation. The supported format is hh:mm.
The operation occurs within a one-hour window following the specified time. If you do not specify a time, Amazon DLM selects a time within the next 24 hours.

(string) --


CronExpression (string) --The schedule, as a Cron expression. The schedule interval must be between 1 hour and 1 year. For more information, see Cron expressions in the Amazon CloudWatch User Guide .



RetainRule (dict) --The retention rule.

Count (integer) --The number of snapshots to retain for each volume, up to a maximum of 1000.

Interval (integer) --The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.

IntervalUnit (string) --The unit of time for time-based retention.



FastRestoreRule (dict) --The rule for enabling fast snapshot restore.

Count (integer) --The number of snapshots to be enabled with fast snapshot restore.

Interval (integer) --The amount of time to enable fast snapshot restore. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.

IntervalUnit (string) --The unit of time for enabling fast snapshot restore.

AvailabilityZones (list) --The Availability Zones in which to enable fast snapshot restore.

(string) --




CrossRegionCopyRules (list) --The rule for cross-Region snapshot copies.

(dict) --Specifies a rule for cross-Region snapshot copies.

TargetRegion (string) --The target Region.

Encrypted (boolean) --To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or if encryption by default is not enabled.

CmkArn (string) --The Amazon Resource Name (ARN) of the AWS KMS customer master key (CMK) to use for EBS encryption. If this parameter is not specified, your AWS managed CMK for EBS is used.

CopyTags (boolean) --Copy all user-defined tags from the source snapshot to the copied snapshot.

RetainRule (dict) --The retention rule.

Interval (integer) --The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.

IntervalUnit (string) --The unit of time for time-based retention.











Parameters (dict) --A set of optional parameters for the policy.

ExcludeBootVolume (boolean) --[EBS Snapshot Management \xe2\x80\x93 Instance policies only] Indicates whether to exclude the root volume from snapshots created using CreateSnapshots . The default is false.





Tags (dict) --The tags.

(string) --
(string) --




PolicyArn (string) --The Amazon Resource Name (ARN) of the policy.








Exceptions

DLM.Client.exceptions.ResourceNotFoundException
DLM.Client.exceptions.InternalServerException
DLM.Client.exceptions.LimitExceededException


    :return: {
        'Policy': {
            'PolicyId': 'string',
            'Description': 'string',
            'State': 'ENABLED'|'DISABLED'|'ERROR',
            'StatusMessage': 'string',
            'ExecutionRoleArn': 'string',
            'DateCreated': datetime(2015, 1, 1),
            'DateModified': datetime(2015, 1, 1),
            'PolicyDetails': {
                'PolicyType': 'EBS_SNAPSHOT_MANAGEMENT',
                'ResourceTypes': [
                    'VOLUME'|'INSTANCE',
                ],
                'TargetTags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Schedules': [
                    {
                        'Name': 'string',
                        'CopyTags': True|False,
                        'TagsToAdd': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'VariableTags': [
                            {
                                'Key': 'string',
                                'Value': 'string'
                            },
                        ],
                        'CreateRule': {
                            'Interval': 123,
                            'IntervalUnit': 'HOURS',
                            'Times': [
                                'string',
                            ],
                            'CronExpression': 'string'
                        },
                        'RetainRule': {
                            'Count': 123,
                            'Interval': 123,
                            'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS'
                        },
                        'FastRestoreRule': {
                            'Count': 123,
                            'Interval': 123,
                            'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS',
                            'AvailabilityZones': [
                                'string',
                            ]
                        },
                        'CrossRegionCopyRules': [
                            {
                                'TargetRegion': 'string',
                                'Encrypted': True|False,
                                'CmkArn': 'string',
                                'CopyTags': True|False,
                                'RetainRule': {
                                    'Interval': 123,
                                    'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS'
                                }
                            },
                        ]
                    },
                ],
                'Parameters': {
                    'ExcludeBootVolume': True|False
                }
            },
            'Tags': {
                'string': 'string'
            },
            'PolicyArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
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

def list_tags_for_resource(ResourceArn=None):
    """
    Lists the tags for the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --Information about the tags.

(string) --
(string) --









Exceptions

DLM.Client.exceptions.InternalServerException
DLM.Client.exceptions.InvalidRequestException
DLM.Client.exceptions.ResourceNotFoundException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    DLM.Client.exceptions.InternalServerException
    DLM.Client.exceptions.InvalidRequestException
    DLM.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds the specified tags to the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nOne or more tags.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DLM.Client.exceptions.InternalServerException
DLM.Client.exceptions.InvalidRequestException
DLM.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes the specified tags from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tag keys.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DLM.Client.exceptions.InternalServerException
DLM.Client.exceptions.InvalidRequestException
DLM.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_lifecycle_policy(PolicyId=None, ExecutionRoleArn=None, State=None, Description=None, PolicyDetails=None):
    """
    Updates the specified lifecycle policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_lifecycle_policy(
        PolicyId='string',
        ExecutionRoleArn='string',
        State='ENABLED'|'DISABLED',
        Description='string',
        PolicyDetails={
            'PolicyType': 'EBS_SNAPSHOT_MANAGEMENT',
            'ResourceTypes': [
                'VOLUME'|'INSTANCE',
            ],
            'TargetTags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'Schedules': [
                {
                    'Name': 'string',
                    'CopyTags': True|False,
                    'TagsToAdd': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'VariableTags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'CreateRule': {
                        'Interval': 123,
                        'IntervalUnit': 'HOURS',
                        'Times': [
                            'string',
                        ],
                        'CronExpression': 'string'
                    },
                    'RetainRule': {
                        'Count': 123,
                        'Interval': 123,
                        'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS'
                    },
                    'FastRestoreRule': {
                        'Count': 123,
                        'Interval': 123,
                        'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS',
                        'AvailabilityZones': [
                            'string',
                        ]
                    },
                    'CrossRegionCopyRules': [
                        {
                            'TargetRegion': 'string',
                            'Encrypted': True|False,
                            'CmkArn': 'string',
                            'CopyTags': True|False,
                            'RetainRule': {
                                'Interval': 123,
                                'IntervalUnit': 'DAYS'|'WEEKS'|'MONTHS'|'YEARS'
                            }
                        },
                    ]
                },
            ],
            'Parameters': {
                'ExcludeBootVolume': True|False
            }
        }
    )
    
    
    :type PolicyId: string
    :param PolicyId: [REQUIRED]\nThe identifier of the lifecycle policy.\n

    :type ExecutionRoleArn: string
    :param ExecutionRoleArn: The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.

    :type State: string
    :param State: The desired activation state of the lifecycle policy after creation.

    :type Description: string
    :param Description: A description of the lifecycle policy.

    :type PolicyDetails: dict
    :param PolicyDetails: The configuration of the lifecycle policy. You cannot update the policy type or the resource type.\n\nPolicyType (string) --The valid target resource types and actions a policy can manage. The default is EBS_SNAPSHOT_MANAGEMENT.\n\nResourceTypes (list) --The resource type. Use VOLUME to create snapshots of individual volumes or use INSTANCE to create multi-volume snapshots from the volumes for an instance.\n\n(string) --\n\n\nTargetTags (list) --The single tag that identifies targeted resources for this policy.\n\n(dict) --Specifies a tag for a resource.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The tag value.\n\n\n\n\n\nSchedules (list) --The schedule of policy-defined actions.\n\n(dict) --Specifies a backup schedule.\n\nName (string) --The name of the schedule.\n\nCopyTags (boolean) --Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.\n\nTagsToAdd (list) --The tags to apply to policy-created resources. These user-defined tags are in addition to the AWS-added lifecycle tags.\n\n(dict) --Specifies a tag for a resource.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The tag value.\n\n\n\n\n\nVariableTags (list) --A collection of key/value pairs with values determined dynamically when the policy is executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two following formats: $(instance-id) or $(timestamp) . Variable tags are only valid for EBS Snapshot Management \xe2\x80\x93 Instance policies.\n\n(dict) --Specifies a tag for a resource.\n\nKey (string) -- [REQUIRED]The tag key.\n\nValue (string) -- [REQUIRED]The tag value.\n\n\n\n\n\nCreateRule (dict) --The creation rule.\n\nInterval (integer) --The interval between snapshots. The supported values are 1, 2, 3, 4, 6, 8, 12, and 24.\n\nIntervalUnit (string) --The interval unit.\n\nTimes (list) --The time, in UTC, to start the operation. The supported format is hh:mm.\nThe operation occurs within a one-hour window following the specified time. If you do not specify a time, Amazon DLM selects a time within the next 24 hours.\n\n(string) --\n\n\nCronExpression (string) --The schedule, as a Cron expression. The schedule interval must be between 1 hour and 1 year. For more information, see Cron expressions in the Amazon CloudWatch User Guide .\n\n\n\nRetainRule (dict) --The retention rule.\n\nCount (integer) --The number of snapshots to retain for each volume, up to a maximum of 1000.\n\nInterval (integer) --The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.\n\nIntervalUnit (string) --The unit of time for time-based retention.\n\n\n\nFastRestoreRule (dict) --The rule for enabling fast snapshot restore.\n\nCount (integer) --The number of snapshots to be enabled with fast snapshot restore.\n\nInterval (integer) --The amount of time to enable fast snapshot restore. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.\n\nIntervalUnit (string) --The unit of time for enabling fast snapshot restore.\n\nAvailabilityZones (list) -- [REQUIRED]The Availability Zones in which to enable fast snapshot restore.\n\n(string) --\n\n\n\n\nCrossRegionCopyRules (list) --The rule for cross-Region snapshot copies.\n\n(dict) --Specifies a rule for cross-Region snapshot copies.\n\nTargetRegion (string) -- [REQUIRED]The target Region.\n\nEncrypted (boolean) -- [REQUIRED]To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or if encryption by default is not enabled.\n\nCmkArn (string) --The Amazon Resource Name (ARN) of the AWS KMS customer master key (CMK) to use for EBS encryption. If this parameter is not specified, your AWS managed CMK for EBS is used.\n\nCopyTags (boolean) --Copy all user-defined tags from the source snapshot to the copied snapshot.\n\nRetainRule (dict) --The retention rule.\n\nInterval (integer) --The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.\n\nIntervalUnit (string) --The unit of time for time-based retention.\n\n\n\n\n\n\n\n\n\n\n\nParameters (dict) --A set of optional parameters for the policy.\n\nExcludeBootVolume (boolean) --[EBS Snapshot Management \xe2\x80\x93 Instance policies only] Indicates whether to exclude the root volume from snapshots created using CreateSnapshots . The default is false.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

DLM.Client.exceptions.ResourceNotFoundException
DLM.Client.exceptions.InvalidRequestException
DLM.Client.exceptions.InternalServerException
DLM.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

