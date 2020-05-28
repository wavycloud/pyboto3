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

def cancel_cluster(ClusterId=None):
    """
    Cancels a cluster job. You can only cancel a cluster job while it\'s in the AwaitingQuorum status. You\'ll have at least an hour after creating a cluster job to cancel it.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation cancels a cluster job. You can only cancel a cluster job while it\'s in the AwaitingQuorum status.
    Expected Output:
    
    :example: response = client.cancel_cluster(
        ClusterId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe 39-character ID for the cluster that you want to cancel, for example CID123e4567-e89b-12d3-a456-426655440000 .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Snowball.Client.exceptions.KMSRequestFailedException
Snowball.Client.exceptions.InvalidJobStateException
Snowball.Client.exceptions.InvalidResourceException

Examples
This operation cancels a cluster job. You can only cancel a cluster job while it\'s in the AwaitingQuorum status.
response = client.cancel_cluster(
    ClusterId='CID123e4567-e89b-12d3-a456-426655440000',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    Snowball.Client.exceptions.KMSRequestFailedException
    Snowball.Client.exceptions.InvalidJobStateException
    Snowball.Client.exceptions.InvalidResourceException
    
    """
    pass

def cancel_job(JobId=None):
    """
    Cancels the specified job. You can only cancel a job before its JobState value changes to PreparingAppliance . Requesting the ListJobs or DescribeJob action returns a job\'s JobState as part of the response element data returned.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation cancels a job. You can only cancel a job before its JobState value changes to PreparingAppliance.
    Expected Output:
    
    :example: response = client.cancel_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe 39-character job ID for the job that you want to cancel, for example JID123e4567-e89b-12d3-a456-426655440000 .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Snowball.Client.exceptions.InvalidResourceException
Snowball.Client.exceptions.InvalidJobStateException
Snowball.Client.exceptions.KMSRequestFailedException

Examples
This operation cancels a job. You can only cancel a job before its JobState value changes to PreparingAppliance.
response = client.cancel_job(
    JobId='JID123e4567-e89b-12d3-a456-426655440000',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    Snowball.Client.exceptions.InvalidResourceException
    Snowball.Client.exceptions.InvalidJobStateException
    Snowball.Client.exceptions.KMSRequestFailedException
    
    """
    pass

def create_address(Address=None):
    """
    Creates an address for a Snowball to be shipped to. In most regions, addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. If the address is invalid or unsupported, then an exception is thrown.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation creates an address for a job. Addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. If the address is invalid or unsupported, then an exception is thrown.
    Expected Output:
    
    :example: response = client.create_address(
        Address={
            'AddressId': 'string',
            'Name': 'string',
            'Company': 'string',
            'Street1': 'string',
            'Street2': 'string',
            'Street3': 'string',
            'City': 'string',
            'StateOrProvince': 'string',
            'PrefectureOrDistrict': 'string',
            'Landmark': 'string',
            'Country': 'string',
            'PostalCode': 'string',
            'PhoneNumber': 'string',
            'IsRestricted': True|False
        }
    )
    
    
    :type Address: dict
    :param Address: [REQUIRED]\nThe address that you want the Snowball shipped to.\n\nAddressId (string) --The unique ID for an address.\n\nName (string) --The name of a person to receive a Snowball at an address.\n\nCompany (string) --The name of the company to receive a Snowball at an address.\n\nStreet1 (string) --The first line in a street address that a Snowball is to be delivered to.\n\nStreet2 (string) --The second line in a street address that a Snowball is to be delivered to.\n\nStreet3 (string) --The third line in a street address that a Snowball is to be delivered to.\n\nCity (string) --The city in an address that a Snowball is to be delivered to.\n\nStateOrProvince (string) --The state or province in an address that a Snowball is to be delivered to.\n\nPrefectureOrDistrict (string) --This field is no longer used and the value is ignored.\n\nLandmark (string) --This field is no longer used and the value is ignored.\n\nCountry (string) --The country in an address that a Snowball is to be delivered to.\n\nPostalCode (string) --The postal code in an address that a Snowball is to be delivered to.\n\nPhoneNumber (string) --The phone number associated with an address that a Snowball is to be delivered to.\n\nIsRestricted (boolean) --If the address you are creating is a primary address, then set this option to true. This field is not supported in most regions.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'AddressId': 'string'
}


Response Structure

(dict) --
AddressId (string) --The automatically generated ID for a specific address. You\'ll use this ID when you create a job to specify which address you want the Snowball for that job shipped to.






Exceptions

Snowball.Client.exceptions.InvalidAddressException
Snowball.Client.exceptions.UnsupportedAddressException

Examples
This operation creates an address for a job. Addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. If the address is invalid or unsupported, then an exception is thrown.
response = client.create_address(
    Address={
        'City': 'Seattle',
        'Company': 'My Company's Name',
        'Country': 'USA',
        'Name': 'My Name',
        'PhoneNumber': '425-555-5555',
        'PostalCode': '98101',
        'StateOrProvince': 'WA',
        'Street1': '123 Main Street',
    },
)

print(response)


Expected Output:
{
    'AddressId': 'ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AddressId': 'string'
    }
    
    
    """
    pass

def create_cluster(JobType=None, Resources=None, Description=None, AddressId=None, KmsKeyARN=None, RoleARN=None, SnowballType=None, ShippingOption=None, Notification=None, ForwardingAddressId=None, TaxDocuments=None):
    """
    Creates an empty cluster. Each cluster supports five nodes. You use the  CreateJob action separately to create the jobs for each of these nodes. The cluster does not ship until these five node jobs have been created.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates an empty cluster. Each cluster supports five nodes. You use the CreateJob action separately to create the jobs for each of these nodes. The cluster does not ship until these five node jobs have been created.
    Expected Output:
    
    :example: response = client.create_cluster(
        JobType='IMPORT'|'EXPORT'|'LOCAL_USE',
        Resources={
            'S3Resources': [
                {
                    'BucketArn': 'string',
                    'KeyRange': {
                        'BeginMarker': 'string',
                        'EndMarker': 'string'
                    }
                },
            ],
            'LambdaResources': [
                {
                    'LambdaArn': 'string',
                    'EventTriggers': [
                        {
                            'EventResourceARN': 'string'
                        },
                    ]
                },
            ],
            'Ec2AmiResources': [
                {
                    'AmiId': 'string',
                    'SnowballAmiId': 'string'
                },
            ]
        },
        Description='string',
        AddressId='string',
        KmsKeyARN='string',
        RoleARN='string',
        SnowballType='STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
        ShippingOption='SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
        Notification={
            'SnsTopicARN': 'string',
            'JobStatesToNotify': [
                'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            ],
            'NotifyAll': True|False
        },
        ForwardingAddressId='string',
        TaxDocuments={
            'IND': {
                'GSTIN': 'string'
            }
        }
    )
    
    
    :type JobType: string
    :param JobType: [REQUIRED]\nThe type of job for this cluster. Currently, the only job type supported for clusters is LOCAL_USE .\n

    :type Resources: dict
    :param Resources: [REQUIRED]\nThe resources associated with the cluster job. These resources include Amazon S3 buckets and optional AWS Lambda functions written in the Python language.\n\nS3Resources (list) --An array of S3Resource objects.\n\n(dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.\n\nBucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.\n\nKeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.\n\nBeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.\n\nEndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.\n\n\n\n\n\n\n\nLambdaResources (list) --The Python-language Lambda functions for this job.\n\n(dict) --Identifies\n\nLambdaArn (string) --An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.\n\nEventTriggers (list) --The array of ARNs for S3Resource objects to trigger the LambdaResource objects associated with this job.\n\n(dict) --The container for the EventTriggerDefinition$EventResourceARN .\n\nEventResourceARN (string) --The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.\n\n\n\n\n\n\n\n\n\nEc2AmiResources (list) --The Amazon Machine Images (AMIs) associated with this job.\n\n(dict) --A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.\n\nAmiId (string) -- [REQUIRED]The ID of the AMI in Amazon EC2.\n\nSnowballAmiId (string) --The ID of the AMI on the Snowball Edge device.\n\n\n\n\n\n\n

    :type Description: string
    :param Description: An optional description of this specific cluster, for example Environmental Data Cluster-01 .

    :type AddressId: string
    :param AddressId: [REQUIRED]\nThe ID for the address that you want the cluster shipped to.\n

    :type KmsKeyARN: string
    :param KmsKeyARN: The KmsKeyARN value that you want to associate with this cluster. KmsKeyARN values are created by using the CreateKey API action in AWS Key Management Service (AWS KMS).

    :type RoleARN: string
    :param RoleARN: [REQUIRED]\nThe RoleARN that you want to associate with this cluster. RoleArn values are created by using the CreateRole API action in AWS Identity and Access Management (IAM).\n

    :type SnowballType: string
    :param SnowballType: The type of AWS Snowball device to use for this cluster. Currently, the only supported device type for cluster jobs is EDGE .\nFor more information, see Snowball Edge Device Options in the Snowball Edge Developer Guide.\n

    :type ShippingOption: string
    :param ShippingOption: [REQUIRED]\nThe shipping speed for each node in this cluster. This speed doesn\'t dictate how soon you\'ll get each Snowball Edge device, rather it represents how quickly each device moves to its destination while in transit. Regional shipping speeds are as follows:\n\nIn Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day.\nIn the European Union (EU), you have access to express shipping. Typically, Snowball Edges shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.\nIn India, Snowball Edges are delivered in one to seven days.\nIn the US, you have access to one-day shipping and two-day shipping.\n\n

    :type Notification: dict
    :param Notification: The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.\n\nSnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.\nYou can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.\n\nJobStatesToNotify (list) --The list of job states that will trigger a notification for this job.\n\n(string) --\n\n\nNotifyAll (boolean) --Any change in job state will trigger a notification for this job.\n\n\n

    :type ForwardingAddressId: string
    :param ForwardingAddressId: The forwarding address ID for a cluster. This field is not supported in most regions.

    :type TaxDocuments: dict
    :param TaxDocuments: The tax documents required in your AWS Region.\n\nIND (dict) --The tax documents required in AWS Regions in India.\n\nGSTIN (string) --The Goods and Services Tax (GST) documents required in AWS Regions in India.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterId': 'string'
}


Response Structure

(dict) --

ClusterId (string) --
The automatically generated ID for a cluster.







Exceptions

Snowball.Client.exceptions.InvalidResourceException
Snowball.Client.exceptions.KMSRequestFailedException
Snowball.Client.exceptions.InvalidInputCombinationException
Snowball.Client.exceptions.Ec2RequestFailedException

Examples
Creates an empty cluster. Each cluster supports five nodes. You use the CreateJob action separately to create the jobs for each of these nodes. The cluster does not ship until these five node jobs have been created.
response = client.create_cluster(
    AddressId='ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b',
    Description='MyCluster',
    JobType='LOCAL_USE',
    KmsKeyARN='arn:aws:kms:us-east-1:123456789012:key/abcd1234-12ab-34cd-56ef-123456123456',
    Notification={
        'JobStatesToNotify': [
        ],
        'NotifyAll': False,
    },
    Resources={
        'S3Resources': [
            {
                'BucketArn': 'arn:aws:s3:::MyBucket',
                'KeyRange': {
                },
            },
        ],
    },
    RoleARN='arn:aws:iam::123456789012:role/snowball-import-S3-role',
    ShippingOption='SECOND_DAY',
    SnowballType='EDGE',
)

print(response)


Expected Output:
{
    'ClusterId': 'CID123e4567-e89b-12d3-a456-426655440000',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ClusterId': 'string'
    }
    
    
    :returns: 
    Snowball.Client.exceptions.InvalidResourceException
    Snowball.Client.exceptions.KMSRequestFailedException
    Snowball.Client.exceptions.InvalidInputCombinationException
    Snowball.Client.exceptions.Ec2RequestFailedException
    
    """
    pass

def create_job(JobType=None, Resources=None, Description=None, AddressId=None, KmsKeyARN=None, RoleARN=None, SnowballCapacityPreference=None, ShippingOption=None, Notification=None, ClusterId=None, SnowballType=None, ForwardingAddressId=None, TaxDocuments=None):
    """
    Creates a job to import or export data between Amazon S3 and your on-premises data center. Your AWS account must have the right trust policies and permissions in place to create a job for Snowball. If you\'re creating a job for a node in a cluster, you only need to provide the clusterId value; the other job attributes are inherited from the cluster.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Creates a job to import or export data between Amazon S3 and your on-premises data center. Your AWS account must have the right trust policies and permissions in place to create a job for Snowball. If you\'re creating a job for a node in a cluster, you only need to provide the clusterId value; the other job attributes are inherited from the cluster.
    Expected Output:
    
    :example: response = client.create_job(
        JobType='IMPORT'|'EXPORT'|'LOCAL_USE',
        Resources={
            'S3Resources': [
                {
                    'BucketArn': 'string',
                    'KeyRange': {
                        'BeginMarker': 'string',
                        'EndMarker': 'string'
                    }
                },
            ],
            'LambdaResources': [
                {
                    'LambdaArn': 'string',
                    'EventTriggers': [
                        {
                            'EventResourceARN': 'string'
                        },
                    ]
                },
            ],
            'Ec2AmiResources': [
                {
                    'AmiId': 'string',
                    'SnowballAmiId': 'string'
                },
            ]
        },
        Description='string',
        AddressId='string',
        KmsKeyARN='string',
        RoleARN='string',
        SnowballCapacityPreference='T50'|'T80'|'T100'|'T42'|'T98'|'NoPreference',
        ShippingOption='SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
        Notification={
            'SnsTopicARN': 'string',
            'JobStatesToNotify': [
                'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            ],
            'NotifyAll': True|False
        },
        ClusterId='string',
        SnowballType='STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
        ForwardingAddressId='string',
        TaxDocuments={
            'IND': {
                'GSTIN': 'string'
            }
        }
    )
    
    
    :type JobType: string
    :param JobType: Defines the type of job that you\'re creating.

    :type Resources: dict
    :param Resources: Defines the Amazon S3 buckets associated with this job.\nWith IMPORT jobs, you specify the bucket or buckets that your transferred data will be imported into.\nWith EXPORT jobs, you specify the bucket or buckets that your transferred data will be exported from. Optionally, you can also specify a KeyRange value. If you choose to export a range, you define the length of the range by providing either an inclusive BeginMarker value, an inclusive EndMarker value, or both. Ranges are UTF-8 binary sorted.\n\nS3Resources (list) --An array of S3Resource objects.\n\n(dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.\n\nBucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.\n\nKeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.\n\nBeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.\n\nEndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.\n\n\n\n\n\n\n\nLambdaResources (list) --The Python-language Lambda functions for this job.\n\n(dict) --Identifies\n\nLambdaArn (string) --An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.\n\nEventTriggers (list) --The array of ARNs for S3Resource objects to trigger the LambdaResource objects associated with this job.\n\n(dict) --The container for the EventTriggerDefinition$EventResourceARN .\n\nEventResourceARN (string) --The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.\n\n\n\n\n\n\n\n\n\nEc2AmiResources (list) --The Amazon Machine Images (AMIs) associated with this job.\n\n(dict) --A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.\n\nAmiId (string) -- [REQUIRED]The ID of the AMI in Amazon EC2.\n\nSnowballAmiId (string) --The ID of the AMI on the Snowball Edge device.\n\n\n\n\n\n\n

    :type Description: string
    :param Description: Defines an optional description of this specific job, for example Important Photos 2016-08-11 .

    :type AddressId: string
    :param AddressId: The ID for the address that you want the Snowball shipped to.

    :type KmsKeyARN: string
    :param KmsKeyARN: The KmsKeyARN that you want to associate with this job. KmsKeyARN s are created using the CreateKey AWS Key Management Service (KMS) API action.

    :type RoleARN: string
    :param RoleARN: The RoleARN that you want to associate with this job. RoleArn s are created using the CreateRole AWS Identity and Access Management (IAM) API action.

    :type SnowballCapacityPreference: string
    :param SnowballCapacityPreference: If your job is being created in one of the US regions, you have the option of specifying what size Snowball you\'d like for this job. In all other regions, Snowballs come with 80 TB in storage capacity.

    :type ShippingOption: string
    :param ShippingOption: The shipping speed for this job. This speed doesn\'t dictate how soon you\'ll get the Snowball, rather it represents how quickly the Snowball moves to its destination while in transit. Regional shipping speeds are as follows:\n\nIn Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day.\nIn the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.\nIn India, Snowballs are delivered in one to seven days.\nIn the US, you have access to one-day shipping and two-day shipping.\n\n

    :type Notification: dict
    :param Notification: Defines the Amazon Simple Notification Service (Amazon SNS) notification settings for this job.\n\nSnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.\nYou can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.\n\nJobStatesToNotify (list) --The list of job states that will trigger a notification for this job.\n\n(string) --\n\n\nNotifyAll (boolean) --Any change in job state will trigger a notification for this job.\n\n\n

    :type ClusterId: string
    :param ClusterId: The ID of a cluster. If you\'re creating a job for a node in a cluster, you need to provide only this clusterId value. The other job attributes are inherited from the cluster.

    :type SnowballType: string
    :param SnowballType: The type of AWS Snowball device to use for this job. Currently, the only supported device type for cluster jobs is EDGE .\nFor more information, see Snowball Edge Device Options in the Snowball Edge Developer Guide.\n

    :type ForwardingAddressId: string
    :param ForwardingAddressId: The forwarding address ID for a job. This field is not supported in most regions.

    :type TaxDocuments: dict
    :param TaxDocuments: The tax documents required in your AWS Region.\n\nIND (dict) --The tax documents required in AWS Regions in India.\n\nGSTIN (string) --The Goods and Services Tax (GST) documents required in AWS Regions in India.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The automatically generated ID for a job, for example JID123e4567-e89b-12d3-a456-426655440000 .







Exceptions

Snowball.Client.exceptions.InvalidResourceException
Snowball.Client.exceptions.KMSRequestFailedException
Snowball.Client.exceptions.InvalidInputCombinationException
Snowball.Client.exceptions.ClusterLimitExceededException
Snowball.Client.exceptions.Ec2RequestFailedException

Examples
Creates a job to import or export data between Amazon S3 and your on-premises data center. Your AWS account must have the right trust policies and permissions in place to create a job for Snowball. If you\'re creating a job for a node in a cluster, you only need to provide the clusterId value; the other job attributes are inherited from the cluster.
response = client.create_job(
    AddressId='ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b',
    Description='My Job',
    JobType='IMPORT',
    KmsKeyARN='arn:aws:kms:us-east-1:123456789012:key/abcd1234-12ab-34cd-56ef-123456123456',
    Notification={
        'JobStatesToNotify': [
        ],
        'NotifyAll': False,
    },
    Resources={
        'S3Resources': [
            {
                'BucketArn': 'arn:aws:s3:::MyBucket',
                'KeyRange': {
                },
            },
        ],
    },
    RoleARN='arn:aws:iam::123456789012:role/snowball-import-S3-role',
    ShippingOption='SECOND_DAY',
    SnowballCapacityPreference='T80',
    SnowballType='STANDARD',
)

print(response)


Expected Output:
{
    'JobId': 'JID123e4567-e89b-12d3-a456-426655440000',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Snowball.Client.exceptions.InvalidResourceException
    Snowball.Client.exceptions.KMSRequestFailedException
    Snowball.Client.exceptions.InvalidInputCombinationException
    Snowball.Client.exceptions.ClusterLimitExceededException
    Snowball.Client.exceptions.Ec2RequestFailedException
    
    """
    pass

def describe_address(AddressId=None):
    """
    Takes an AddressId and returns specific details about that address in the form of an Address object.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation describes an address for a job.
    Expected Output:
    
    :example: response = client.describe_address(
        AddressId='string'
    )
    
    
    :type AddressId: string
    :param AddressId: [REQUIRED]\nThe automatically generated ID for a specific address.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Address': {
        'AddressId': 'string',
        'Name': 'string',
        'Company': 'string',
        'Street1': 'string',
        'Street2': 'string',
        'Street3': 'string',
        'City': 'string',
        'StateOrProvince': 'string',
        'PrefectureOrDistrict': 'string',
        'Landmark': 'string',
        'Country': 'string',
        'PostalCode': 'string',
        'PhoneNumber': 'string',
        'IsRestricted': True|False
    }
}


Response Structure

(dict) --
Address (dict) --The address that you want the Snowball or Snowballs associated with a specific job to be shipped to.

AddressId (string) --The unique ID for an address.

Name (string) --The name of a person to receive a Snowball at an address.

Company (string) --The name of the company to receive a Snowball at an address.

Street1 (string) --The first line in a street address that a Snowball is to be delivered to.

Street2 (string) --The second line in a street address that a Snowball is to be delivered to.

Street3 (string) --The third line in a street address that a Snowball is to be delivered to.

City (string) --The city in an address that a Snowball is to be delivered to.

StateOrProvince (string) --The state or province in an address that a Snowball is to be delivered to.

PrefectureOrDistrict (string) --This field is no longer used and the value is ignored.

Landmark (string) --This field is no longer used and the value is ignored.

Country (string) --The country in an address that a Snowball is to be delivered to.

PostalCode (string) --The postal code in an address that a Snowball is to be delivered to.

PhoneNumber (string) --The phone number associated with an address that a Snowball is to be delivered to.

IsRestricted (boolean) --If the address you are creating is a primary address, then set this option to true. This field is not supported in most regions.








Exceptions

Snowball.Client.exceptions.InvalidResourceException

Examples
This operation describes an address for a job.
response = client.describe_address(
    AddressId='ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b',
)

print(response)


Expected Output:
{
    'Address': {
        'AddressId': 'ADID5643ec50-3eec-4eb3-9be6-9374c10eb51b',
        'City': 'Seattle',
        'Company': 'My Company',
        'Country': 'US',
        'Name': 'My Name',
        'PhoneNumber': '425-555-5555',
        'PostalCode': '98101',
        'StateOrProvince': 'WA',
        'Street1': '123 Main Street',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Address': {
            'AddressId': 'string',
            'Name': 'string',
            'Company': 'string',
            'Street1': 'string',
            'Street2': 'string',
            'Street3': 'string',
            'City': 'string',
            'StateOrProvince': 'string',
            'PrefectureOrDistrict': 'string',
            'Landmark': 'string',
            'Country': 'string',
            'PostalCode': 'string',
            'PhoneNumber': 'string',
            'IsRestricted': True|False
        }
    }
    
    
    """
    pass

def describe_addresses(MaxResults=None, NextToken=None):
    """
    Returns a specified number of ADDRESS objects. Calling this API in one of the US regions will return addresses from the list of all addresses associated with this account in all US regions.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation describes all the addresses that you\'ve created for AWS Snowball. Calling this API in one of the US regions will return addresses from the list of all addresses associated with this account in all US regions.
    Expected Output:
    
    :example: response = client.describe_addresses(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The number of ADDRESS objects to return.

    :type NextToken: string
    :param NextToken: HTTP requests are stateless. To identify what object comes 'next' in the list of ADDRESS objects, you have the option of specifying a value for NextToken as the starting point for your list of returned addresses.

    :rtype: dict

ReturnsResponse Syntax
{
    'Addresses': [
        {
            'AddressId': 'string',
            'Name': 'string',
            'Company': 'string',
            'Street1': 'string',
            'Street2': 'string',
            'Street3': 'string',
            'City': 'string',
            'StateOrProvince': 'string',
            'PrefectureOrDistrict': 'string',
            'Landmark': 'string',
            'Country': 'string',
            'PostalCode': 'string',
            'PhoneNumber': 'string',
            'IsRestricted': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Addresses (list) --
The Snowball shipping addresses that were created for this account.

(dict) --
The address that you want the Snowball or Snowballs associated with a specific job to be shipped to. Addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. Although no individual elements of the Address are required, if the address is invalid or unsupported, then an exception is thrown.

AddressId (string) --
The unique ID for an address.

Name (string) --
The name of a person to receive a Snowball at an address.

Company (string) --
The name of the company to receive a Snowball at an address.

Street1 (string) --
The first line in a street address that a Snowball is to be delivered to.

Street2 (string) --
The second line in a street address that a Snowball is to be delivered to.

Street3 (string) --
The third line in a street address that a Snowball is to be delivered to.

City (string) --
The city in an address that a Snowball is to be delivered to.

StateOrProvince (string) --
The state or province in an address that a Snowball is to be delivered to.

PrefectureOrDistrict (string) --
This field is no longer used and the value is ignored.

Landmark (string) --
This field is no longer used and the value is ignored.

Country (string) --
The country in an address that a Snowball is to be delivered to.

PostalCode (string) --
The postal code in an address that a Snowball is to be delivered to.

PhoneNumber (string) --
The phone number associated with an address that a Snowball is to be delivered to.

IsRestricted (boolean) --
If the address you are creating is a primary address, then set this option to true. This field is not supported in most regions.





NextToken (string) --
HTTP requests are stateless. If you use the automatically generated NextToken value in your next DescribeAddresses call, your list of returned addresses will start from this point in the array.







Exceptions

Snowball.Client.exceptions.InvalidResourceException
Snowball.Client.exceptions.InvalidNextTokenException

Examples
This operation describes all the addresses that you\'ve created for AWS Snowball. Calling this API in one of the US regions will return addresses from the list of all addresses associated with this account in all US regions.
response = client.describe_addresses(
)

print(response)


Expected Output:
{
    'Addresses': [
        {
            'AddressId': 'ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b',
            'City': 'Seattle',
            'Company': 'My Company',
            'Country': 'US',
            'Name': 'My Name',
            'PhoneNumber': '425-555-5555',
            'PostalCode': '98101',
            'StateOrProvince': 'WA',
            'Street1': '123 Main Street',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Addresses': [
            {
                'AddressId': 'string',
                'Name': 'string',
                'Company': 'string',
                'Street1': 'string',
                'Street2': 'string',
                'Street3': 'string',
                'City': 'string',
                'StateOrProvince': 'string',
                'PrefectureOrDistrict': 'string',
                'Landmark': 'string',
                'Country': 'string',
                'PostalCode': 'string',
                'PhoneNumber': 'string',
                'IsRestricted': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Snowball.Client.exceptions.InvalidResourceException
    Snowball.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def describe_cluster(ClusterId=None):
    """
    Returns information about a specific cluster including shipping information, cluster status, and other important metadata.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns information about a specific cluster including shipping information, cluster status, and other important metadata.
    Expected Output:
    
    :example: response = client.describe_cluster(
        ClusterId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe automatically generated ID for a cluster.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ClusterMetadata': {
        'ClusterId': 'string',
        'Description': 'string',
        'KmsKeyARN': 'string',
        'RoleARN': 'string',
        'ClusterState': 'AwaitingQuorum'|'Pending'|'InUse'|'Complete'|'Cancelled',
        'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
        'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
        'CreationDate': datetime(2015, 1, 1),
        'Resources': {
            'S3Resources': [
                {
                    'BucketArn': 'string',
                    'KeyRange': {
                        'BeginMarker': 'string',
                        'EndMarker': 'string'
                    }
                },
            ],
            'LambdaResources': [
                {
                    'LambdaArn': 'string',
                    'EventTriggers': [
                        {
                            'EventResourceARN': 'string'
                        },
                    ]
                },
            ],
            'Ec2AmiResources': [
                {
                    'AmiId': 'string',
                    'SnowballAmiId': 'string'
                },
            ]
        },
        'AddressId': 'string',
        'ShippingOption': 'SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
        'Notification': {
            'SnsTopicARN': 'string',
            'JobStatesToNotify': [
                'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            ],
            'NotifyAll': True|False
        },
        'ForwardingAddressId': 'string',
        'TaxDocuments': {
            'IND': {
                'GSTIN': 'string'
            }
        }
    }
}


Response Structure

(dict) --
ClusterMetadata (dict) --Information about a specific cluster, including shipping information, cluster status, and other important metadata.

ClusterId (string) --The automatically generated ID for a cluster.

Description (string) --The optional description of the cluster.

KmsKeyARN (string) --The KmsKeyARN Amazon Resource Name (ARN) associated with this cluster. This ARN was created using the CreateKey API action in AWS Key Management Service (AWS KMS).

RoleARN (string) --The role ARN associated with this cluster. This ARN was created using the CreateRole API action in AWS Identity and Access Management (IAM).

ClusterState (string) --The current status of the cluster.

JobType (string) --The type of job for this cluster. Currently, the only job type supported for clusters is LOCAL_USE .

SnowballType (string) --The type of AWS Snowball device to use for this cluster. Currently, the only supported device type for cluster jobs is EDGE .
For more information, see Snowball Edge Device Options in the Snowball Edge Developer Guide.

CreationDate (datetime) --The creation date for this cluster.

Resources (dict) --The arrays of  JobResource objects that can include updated  S3Resource objects or  LambdaResource objects.

S3Resources (list) --An array of S3Resource objects.

(dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.

BucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.

KeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.

BeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.

EndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.







LambdaResources (list) --The Python-language Lambda functions for this job.

(dict) --Identifies

LambdaArn (string) --An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.

EventTriggers (list) --The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.

(dict) --The container for the  EventTriggerDefinition$EventResourceARN .

EventResourceARN (string) --The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.









Ec2AmiResources (list) --The Amazon Machine Images (AMIs) associated with this job.

(dict) --A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

AmiId (string) --The ID of the AMI in Amazon EC2.

SnowballAmiId (string) --The ID of the AMI on the Snowball Edge device.







AddressId (string) --The automatically generated ID for a specific address.

ShippingOption (string) --The shipping speed for each node in this cluster. This speed doesn\'t dictate how soon you\'ll get each Snowball Edge device, rather it represents how quickly each device moves to its destination while in transit. Regional shipping speeds are as follows:

In Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day.
In the European Union (EU), you have access to express shipping. Typically, Snowball Edges shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
In India, Snowball Edges are delivered in one to seven days.
In the US, you have access to one-day shipping and two-day shipping.


Notification (dict) --The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.

SnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.
You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.

JobStatesToNotify (list) --The list of job states that will trigger a notification for this job.

(string) --


NotifyAll (boolean) --Any change in job state will trigger a notification for this job.



ForwardingAddressId (string) --The ID of the address that you want a cluster shipped to, after it will be shipped to its primary address. This field is not supported in most regions.

TaxDocuments (dict) --The tax documents required in your AWS Region.

IND (dict) --The tax documents required in AWS Regions in India.

GSTIN (string) --The Goods and Services Tax (GST) documents required in AWS Regions in India.












Exceptions

Snowball.Client.exceptions.InvalidResourceException

Examples
Returns information about a specific cluster including shipping information, cluster status, and other important metadata.
response = client.describe_cluster(
    ClusterId='CID123e4567-e89b-12d3-a456-426655440000',
)

print(response)


Expected Output:
{
    'ClusterMetadata': {
        'AddressId': 'ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b',
        'ClusterId': 'CID123e4567-e89b-12d3-a456-426655440000',
        'ClusterState': 'Pending',
        'CreationDate': datetime(2016, 11, 30, 3, 11, 57, 2, 335, 0),
        'Description': 'MyCluster',
        'JobType': 'LOCAL_USE',
        'KmsKeyARN': 'arn:aws:kms:us-east-1:123456789012:key/abcd1234-12ab-34cd-56ef-123456123456',
        'Notification': {
            'JobStatesToNotify': [
            ],
            'NotifyAll': False,
        },
        'Resources': {
            'S3Resources': [
                {
                    'BucketArn': 'arn:aws:s3:::MyBucket',
                    'KeyRange': {
                    },
                },
            ],
        },
        'RoleARN': 'arn:aws:iam::123456789012:role/snowball-import-S3-role',
        'ShippingOption': 'SECOND_DAY',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ClusterMetadata': {
            'ClusterId': 'string',
            'Description': 'string',
            'KmsKeyARN': 'string',
            'RoleARN': 'string',
            'ClusterState': 'AwaitingQuorum'|'Pending'|'InUse'|'Complete'|'Cancelled',
            'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
            'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
            'CreationDate': datetime(2015, 1, 1),
            'Resources': {
                'S3Resources': [
                    {
                        'BucketArn': 'string',
                        'KeyRange': {
                            'BeginMarker': 'string',
                            'EndMarker': 'string'
                        }
                    },
                ],
                'LambdaResources': [
                    {
                        'LambdaArn': 'string',
                        'EventTriggers': [
                            {
                                'EventResourceARN': 'string'
                            },
                        ]
                    },
                ],
                'Ec2AmiResources': [
                    {
                        'AmiId': 'string',
                        'SnowballAmiId': 'string'
                    },
                ]
            },
            'AddressId': 'string',
            'ShippingOption': 'SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
            'Notification': {
                'SnsTopicARN': 'string',
                'JobStatesToNotify': [
                    'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
                ],
                'NotifyAll': True|False
            },
            'ForwardingAddressId': 'string',
            'TaxDocuments': {
                'IND': {
                    'GSTIN': 'string'
                }
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_job(JobId=None):
    """
    Returns information about a specific job including shipping information, job status, and other important metadata.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation describes a job you\'ve created for AWS Snowball.
    Expected Output:
    
    :example: response = client.describe_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe automatically generated ID for a job, for example JID123e4567-e89b-12d3-a456-426655440000 .\n

    :rtype: dict
ReturnsResponse Syntax{
    'JobMetadata': {
        'JobId': 'string',
        'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
        'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
        'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
        'CreationDate': datetime(2015, 1, 1),
        'Resources': {
            'S3Resources': [
                {
                    'BucketArn': 'string',
                    'KeyRange': {
                        'BeginMarker': 'string',
                        'EndMarker': 'string'
                    }
                },
            ],
            'LambdaResources': [
                {
                    'LambdaArn': 'string',
                    'EventTriggers': [
                        {
                            'EventResourceARN': 'string'
                        },
                    ]
                },
            ],
            'Ec2AmiResources': [
                {
                    'AmiId': 'string',
                    'SnowballAmiId': 'string'
                },
            ]
        },
        'Description': 'string',
        'KmsKeyARN': 'string',
        'RoleARN': 'string',
        'AddressId': 'string',
        'ShippingDetails': {
            'ShippingOption': 'SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
            'InboundShipment': {
                'Status': 'string',
                'TrackingNumber': 'string'
            },
            'OutboundShipment': {
                'Status': 'string',
                'TrackingNumber': 'string'
            }
        },
        'SnowballCapacityPreference': 'T50'|'T80'|'T100'|'T42'|'T98'|'NoPreference',
        'Notification': {
            'SnsTopicARN': 'string',
            'JobStatesToNotify': [
                'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            ],
            'NotifyAll': True|False
        },
        'DataTransferProgress': {
            'BytesTransferred': 123,
            'ObjectsTransferred': 123,
            'TotalBytes': 123,
            'TotalObjects': 123
        },
        'JobLogInfo': {
            'JobCompletionReportURI': 'string',
            'JobSuccessLogURI': 'string',
            'JobFailureLogURI': 'string'
        },
        'ClusterId': 'string',
        'ForwardingAddressId': 'string',
        'TaxDocuments': {
            'IND': {
                'GSTIN': 'string'
            }
        }
    },
    'SubJobMetadata': [
        {
            'JobId': 'string',
            'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
            'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
            'CreationDate': datetime(2015, 1, 1),
            'Resources': {
                'S3Resources': [
                    {
                        'BucketArn': 'string',
                        'KeyRange': {
                            'BeginMarker': 'string',
                            'EndMarker': 'string'
                        }
                    },
                ],
                'LambdaResources': [
                    {
                        'LambdaArn': 'string',
                        'EventTriggers': [
                            {
                                'EventResourceARN': 'string'
                            },
                        ]
                    },
                ],
                'Ec2AmiResources': [
                    {
                        'AmiId': 'string',
                        'SnowballAmiId': 'string'
                    },
                ]
            },
            'Description': 'string',
            'KmsKeyARN': 'string',
            'RoleARN': 'string',
            'AddressId': 'string',
            'ShippingDetails': {
                'ShippingOption': 'SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
                'InboundShipment': {
                    'Status': 'string',
                    'TrackingNumber': 'string'
                },
                'OutboundShipment': {
                    'Status': 'string',
                    'TrackingNumber': 'string'
                }
            },
            'SnowballCapacityPreference': 'T50'|'T80'|'T100'|'T42'|'T98'|'NoPreference',
            'Notification': {
                'SnsTopicARN': 'string',
                'JobStatesToNotify': [
                    'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
                ],
                'NotifyAll': True|False
            },
            'DataTransferProgress': {
                'BytesTransferred': 123,
                'ObjectsTransferred': 123,
                'TotalBytes': 123,
                'TotalObjects': 123
            },
            'JobLogInfo': {
                'JobCompletionReportURI': 'string',
                'JobSuccessLogURI': 'string',
                'JobFailureLogURI': 'string'
            },
            'ClusterId': 'string',
            'ForwardingAddressId': 'string',
            'TaxDocuments': {
                'IND': {
                    'GSTIN': 'string'
                }
            }
        },
    ]
}


Response Structure

(dict) --
JobMetadata (dict) --Information about a specific job, including shipping information, job status, and other important metadata.

JobId (string) --The automatically generated ID for a job, for example JID123e4567-e89b-12d3-a456-426655440000 .

JobState (string) --The current status of the jobs.

JobType (string) --The type of job.

SnowballType (string) --The type of device used with this job.

CreationDate (datetime) --The creation date for this job.

Resources (dict) --An array of S3Resource objects. Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into.

S3Resources (list) --An array of S3Resource objects.

(dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.

BucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.

KeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.

BeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.

EndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.







LambdaResources (list) --The Python-language Lambda functions for this job.

(dict) --Identifies

LambdaArn (string) --An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.

EventTriggers (list) --The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.

(dict) --The container for the  EventTriggerDefinition$EventResourceARN .

EventResourceARN (string) --The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.









Ec2AmiResources (list) --The Amazon Machine Images (AMIs) associated with this job.

(dict) --A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

AmiId (string) --The ID of the AMI in Amazon EC2.

SnowballAmiId (string) --The ID of the AMI on the Snowball Edge device.







Description (string) --The description of the job, provided at job creation.

KmsKeyARN (string) --The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key associated with this job. This ARN was created using the CreateKey API action in AWS KMS.

RoleARN (string) --The role ARN associated with this job. This ARN was created using the CreateRole API action in AWS Identity and Access Management (IAM).

AddressId (string) --The ID for the address that you want the Snowball shipped to.

ShippingDetails (dict) --A job\'s shipping information, including inbound and outbound tracking numbers and shipping speed options.

ShippingOption (string) --The shipping speed for a particular job. This speed doesn\'t dictate how soon you\'ll get the Snowball from the job\'s creation date. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:

In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day.
In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
In India, Snowballs are delivered in one to seven days.
In the United States of America (US), you have access to one-day shipping and two-day shipping.


InboundShipment (dict) --The Status and TrackingNumber values for a Snowball being returned to AWS for a particular job.

Status (string) --Status information for a shipment.

TrackingNumber (string) --The tracking number for this job. Using this tracking number with your region\'s carrier\'s website, you can track a Snowball as the carrier transports it.
For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.



OutboundShipment (dict) --The Status and TrackingNumber values for a Snowball being delivered to the address that you specified for a particular job.

Status (string) --Status information for a shipment.

TrackingNumber (string) --The tracking number for this job. Using this tracking number with your region\'s carrier\'s website, you can track a Snowball as the carrier transports it.
For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.





SnowballCapacityPreference (string) --The Snowball capacity preference for this job, specified at job creation. In US regions, you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity Snowballs.

Notification (dict) --The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a specific job. The Notification object is returned as a part of the response syntax of the DescribeJob action in the JobMetadata data type.

SnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.
You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.

JobStatesToNotify (list) --The list of job states that will trigger a notification for this job.

(string) --


NotifyAll (boolean) --Any change in job state will trigger a notification for this job.



DataTransferProgress (dict) --A value that defines the real-time status of a Snowball\'s data transfer while the device is at AWS. This data is only available while a job has a JobState value of InProgress , for both import and export jobs.

BytesTransferred (integer) --The number of bytes transferred between a Snowball and Amazon S3.

ObjectsTransferred (integer) --The number of objects transferred between a Snowball and Amazon S3.

TotalBytes (integer) --The total bytes of data for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.

TotalObjects (integer) --The total number of objects for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.



JobLogInfo (dict) --Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job report becomes available at the end of the import process. For export jobs, your job report typically becomes available while the Snowball for your job part is being delivered to you.

JobCompletionReportURI (string) --A link to an Amazon S3 presigned URL where the job completion report is located.

JobSuccessLogURI (string) --A link to an Amazon S3 presigned URL where the job success log is located.

JobFailureLogURI (string) --A link to an Amazon S3 presigned URL where the job failure log is located.



ClusterId (string) --The 39-character ID for the cluster, for example CID123e4567-e89b-12d3-a456-426655440000 .

ForwardingAddressId (string) --The ID of the address that you want a job shipped to, after it will be shipped to its primary address. This field is not supported in most regions.

TaxDocuments (dict) --The metadata associated with the tax documents required in your AWS Region.

IND (dict) --The tax documents required in AWS Regions in India.

GSTIN (string) --The Goods and Services Tax (GST) documents required in AWS Regions in India.







SubJobMetadata (list) --Information about a specific job part (in the case of an export job), including shipping information, job status, and other important metadata.

(dict) --Contains information about a specific job including shipping information, job status, and other important metadata. This information is returned as a part of the response syntax of the DescribeJob action.

JobId (string) --The automatically generated ID for a job, for example JID123e4567-e89b-12d3-a456-426655440000 .

JobState (string) --The current status of the jobs.

JobType (string) --The type of job.

SnowballType (string) --The type of device used with this job.

CreationDate (datetime) --The creation date for this job.

Resources (dict) --An array of S3Resource objects. Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into.

S3Resources (list) --An array of S3Resource objects.

(dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.

BucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.

KeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.

BeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.

EndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.







LambdaResources (list) --The Python-language Lambda functions for this job.

(dict) --Identifies

LambdaArn (string) --An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.

EventTriggers (list) --The array of ARNs for  S3Resource objects to trigger the  LambdaResource objects associated with this job.

(dict) --The container for the  EventTriggerDefinition$EventResourceARN .

EventResourceARN (string) --The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.









Ec2AmiResources (list) --The Amazon Machine Images (AMIs) associated with this job.

(dict) --A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.

AmiId (string) --The ID of the AMI in Amazon EC2.

SnowballAmiId (string) --The ID of the AMI on the Snowball Edge device.







Description (string) --The description of the job, provided at job creation.

KmsKeyARN (string) --The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key associated with this job. This ARN was created using the CreateKey API action in AWS KMS.

RoleARN (string) --The role ARN associated with this job. This ARN was created using the CreateRole API action in AWS Identity and Access Management (IAM).

AddressId (string) --The ID for the address that you want the Snowball shipped to.

ShippingDetails (dict) --A job\'s shipping information, including inbound and outbound tracking numbers and shipping speed options.

ShippingOption (string) --The shipping speed for a particular job. This speed doesn\'t dictate how soon you\'ll get the Snowball from the job\'s creation date. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:

In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day.
In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
In India, Snowballs are delivered in one to seven days.
In the United States of America (US), you have access to one-day shipping and two-day shipping.


InboundShipment (dict) --The Status and TrackingNumber values for a Snowball being returned to AWS for a particular job.

Status (string) --Status information for a shipment.

TrackingNumber (string) --The tracking number for this job. Using this tracking number with your region\'s carrier\'s website, you can track a Snowball as the carrier transports it.
For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.



OutboundShipment (dict) --The Status and TrackingNumber values for a Snowball being delivered to the address that you specified for a particular job.

Status (string) --Status information for a shipment.

TrackingNumber (string) --The tracking number for this job. Using this tracking number with your region\'s carrier\'s website, you can track a Snowball as the carrier transports it.
For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.





SnowballCapacityPreference (string) --The Snowball capacity preference for this job, specified at job creation. In US regions, you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity Snowballs.

Notification (dict) --The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a specific job. The Notification object is returned as a part of the response syntax of the DescribeJob action in the JobMetadata data type.

SnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.
You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.

JobStatesToNotify (list) --The list of job states that will trigger a notification for this job.

(string) --


NotifyAll (boolean) --Any change in job state will trigger a notification for this job.



DataTransferProgress (dict) --A value that defines the real-time status of a Snowball\'s data transfer while the device is at AWS. This data is only available while a job has a JobState value of InProgress , for both import and export jobs.

BytesTransferred (integer) --The number of bytes transferred between a Snowball and Amazon S3.

ObjectsTransferred (integer) --The number of objects transferred between a Snowball and Amazon S3.

TotalBytes (integer) --The total bytes of data for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.

TotalObjects (integer) --The total number of objects for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.



JobLogInfo (dict) --Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job report becomes available at the end of the import process. For export jobs, your job report typically becomes available while the Snowball for your job part is being delivered to you.

JobCompletionReportURI (string) --A link to an Amazon S3 presigned URL where the job completion report is located.

JobSuccessLogURI (string) --A link to an Amazon S3 presigned URL where the job success log is located.

JobFailureLogURI (string) --A link to an Amazon S3 presigned URL where the job failure log is located.



ClusterId (string) --The 39-character ID for the cluster, for example CID123e4567-e89b-12d3-a456-426655440000 .

ForwardingAddressId (string) --The ID of the address that you want a job shipped to, after it will be shipped to its primary address. This field is not supported in most regions.

TaxDocuments (dict) --The metadata associated with the tax documents required in your AWS Region.

IND (dict) --The tax documents required in AWS Regions in India.

GSTIN (string) --The Goods and Services Tax (GST) documents required in AWS Regions in India.














Exceptions

Snowball.Client.exceptions.InvalidResourceException

Examples
This operation describes a job you\'ve created for AWS Snowball.
response = client.describe_job(
    JobId='JID123e4567-e89b-12d3-a456-426655440000',
)

print(response)


Expected Output:
{
    'JobMetadata': {
        'AddressId': 'ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b',
        'CreationDate': datetime(2016, 10, 5, 0, 9, 24, 2, 279, 0),
        'Description': 'My Job',
        'JobId': 'JID123e4567-e89b-12d3-a456-426655440000',
        'JobState': 'New',
        'JobType': 'IMPORT',
        'KmsKeyARN': 'arn:aws:kms:us-east-1:123456789012:key/abcd1234-12ab-34cd-56ef-123456123456',
        'Notification': {
            'JobStatesToNotify': [
            ],
            'NotifyAll': False,
        },
        'Resources': {
            'S3Resources': [
                {
                    'BucketArn': 'arn:aws:s3:::MyBucket',
                    'KeyRange': {
                    },
                },
            ],
        },
        'RoleARN': 'arn:aws:iam::123456789012:role/snowball-import-S3-role',
        'ShippingDetails': {
            'ShippingOption': 'SECOND_DAY',
        },
        'SnowballCapacityPreference': 'T80',
        'SnowballType': 'STANDARD',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'JobMetadata': {
            'JobId': 'string',
            'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
            'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
            'CreationDate': datetime(2015, 1, 1),
            'Resources': {
                'S3Resources': [
                    {
                        'BucketArn': 'string',
                        'KeyRange': {
                            'BeginMarker': 'string',
                            'EndMarker': 'string'
                        }
                    },
                ],
                'LambdaResources': [
                    {
                        'LambdaArn': 'string',
                        'EventTriggers': [
                            {
                                'EventResourceARN': 'string'
                            },
                        ]
                    },
                ],
                'Ec2AmiResources': [
                    {
                        'AmiId': 'string',
                        'SnowballAmiId': 'string'
                    },
                ]
            },
            'Description': 'string',
            'KmsKeyARN': 'string',
            'RoleARN': 'string',
            'AddressId': 'string',
            'ShippingDetails': {
                'ShippingOption': 'SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
                'InboundShipment': {
                    'Status': 'string',
                    'TrackingNumber': 'string'
                },
                'OutboundShipment': {
                    'Status': 'string',
                    'TrackingNumber': 'string'
                }
            },
            'SnowballCapacityPreference': 'T50'|'T80'|'T100'|'T42'|'T98'|'NoPreference',
            'Notification': {
                'SnsTopicARN': 'string',
                'JobStatesToNotify': [
                    'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
                ],
                'NotifyAll': True|False
            },
            'DataTransferProgress': {
                'BytesTransferred': 123,
                'ObjectsTransferred': 123,
                'TotalBytes': 123,
                'TotalObjects': 123
            },
            'JobLogInfo': {
                'JobCompletionReportURI': 'string',
                'JobSuccessLogURI': 'string',
                'JobFailureLogURI': 'string'
            },
            'ClusterId': 'string',
            'ForwardingAddressId': 'string',
            'TaxDocuments': {
                'IND': {
                    'GSTIN': 'string'
                }
            }
        },
        'SubJobMetadata': [
            {
                'JobId': 'string',
                'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
                'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
                'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
                'CreationDate': datetime(2015, 1, 1),
                'Resources': {
                    'S3Resources': [
                        {
                            'BucketArn': 'string',
                            'KeyRange': {
                                'BeginMarker': 'string',
                                'EndMarker': 'string'
                            }
                        },
                    ],
                    'LambdaResources': [
                        {
                            'LambdaArn': 'string',
                            'EventTriggers': [
                                {
                                    'EventResourceARN': 'string'
                                },
                            ]
                        },
                    ],
                    'Ec2AmiResources': [
                        {
                            'AmiId': 'string',
                            'SnowballAmiId': 'string'
                        },
                    ]
                },
                'Description': 'string',
                'KmsKeyARN': 'string',
                'RoleARN': 'string',
                'AddressId': 'string',
                'ShippingDetails': {
                    'ShippingOption': 'SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
                    'InboundShipment': {
                        'Status': 'string',
                        'TrackingNumber': 'string'
                    },
                    'OutboundShipment': {
                        'Status': 'string',
                        'TrackingNumber': 'string'
                    }
                },
                'SnowballCapacityPreference': 'T50'|'T80'|'T100'|'T42'|'T98'|'NoPreference',
                'Notification': {
                    'SnsTopicARN': 'string',
                    'JobStatesToNotify': [
                        'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
                    ],
                    'NotifyAll': True|False
                },
                'DataTransferProgress': {
                    'BytesTransferred': 123,
                    'ObjectsTransferred': 123,
                    'TotalBytes': 123,
                    'TotalObjects': 123
                },
                'JobLogInfo': {
                    'JobCompletionReportURI': 'string',
                    'JobSuccessLogURI': 'string',
                    'JobFailureLogURI': 'string'
                },
                'ClusterId': 'string',
                'ForwardingAddressId': 'string',
                'TaxDocuments': {
                    'IND': {
                        'GSTIN': 'string'
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
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

def get_job_manifest(JobId=None):
    """
    Returns a link to an Amazon S3 presigned URL for the manifest file associated with the specified JobId value. You can access the manifest file for up to 60 minutes after this request has been made. To access the manifest file after 60 minutes have passed, you\'ll have to make another call to the GetJobManifest action.
    The manifest is an encrypted file that you can download after your job enters the WithCustomer status. The manifest is decrypted by using the UnlockCode code value, when you pass both values to the Snowball through the Snowball client when the client is started for the first time.
    As a best practice, we recommend that you don\'t save a copy of an UnlockCode value in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snowball associated with that job.
    The credentials of a given job, including its manifest file and unlock code, expire 90 days after the job is created.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a link to an Amazon S3 presigned URL for the manifest file associated with the specified JobId value. You can access the manifest file for up to 60 minutes after this request has been made. To access the manifest file after 60 minutes have passed, you\'ll have to make another call to the GetJobManifest action.
    
    :example: response = client.get_job_manifest(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID for a job that you want to get the manifest file for, for example JID123e4567-e89b-12d3-a456-426655440000 .\n

    :rtype: dict
ReturnsResponse Syntax{
    'ManifestURI': 'string'
}


Response Structure

(dict) --
ManifestURI (string) --The Amazon S3 presigned URL for the manifest file associated with the specified JobId value.






Exceptions

Snowball.Client.exceptions.InvalidResourceException
Snowball.Client.exceptions.InvalidJobStateException

Examples
Returns a link to an Amazon S3 presigned URL for the manifest file associated with the specified JobId value. You can access the manifest file for up to 60 minutes after this request has been made. To access the manifest file after 60 minutes have passed, you\'ll have to make another call to the GetJobManifest action.

    :return: {
        'ManifestURI': 'string'
    }
    
    
    """
    pass

def get_job_unlock_code(JobId=None):
    """
    Returns the UnlockCode code value for the specified job. A particular UnlockCode value can be accessed for up to 90 days after the associated job has been created.
    The UnlockCode value is a 29-character code with 25 alphanumeric characters and 4 hyphens. This code is used to decrypt the manifest file when it is passed along with the manifest to the Snowball through the Snowball client when the client is started for the first time.
    As a best practice, we recommend that you don\'t save a copy of the UnlockCode in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snowball associated with that job.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns the UnlockCode code value for the specified job. A particular UnlockCode value can be accessed for up to 90 days after the associated job has been created.
    
    :example: response = client.get_job_unlock_code(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID for the job that you want to get the UnlockCode value for, for example JID123e4567-e89b-12d3-a456-426655440000 .\n

    :rtype: dict
ReturnsResponse Syntax{
    'UnlockCode': 'string'
}


Response Structure

(dict) --
UnlockCode (string) --The UnlockCode value for the specified job. The UnlockCode value can be accessed for up to 90 days after the job has been created.






Exceptions

Snowball.Client.exceptions.InvalidResourceException
Snowball.Client.exceptions.InvalidJobStateException

Examples
Returns the UnlockCode code value for the specified job. A particular UnlockCode value can be accessed for up to 90 days after the associated job has been created.

    :return: {
        'UnlockCode': 'string'
    }
    
    
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

def get_snowball_usage():
    """
    Returns information about the Snowball service limit for your account, and also the number of Snowballs your account has in use.
    The default service limit for the number of Snowballs that you can have at one time is 1. If you want to increase your service limit, contact AWS Support.
    See also: AWS API Documentation
    
    Examples
    Returns information about the Snowball service limit for your account, and also the number of Snowballs your account has in use.
    
    :example: response = client.get_snowball_usage()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'SnowballLimit': 123,
    'SnowballsInUse': 123
}


Response Structure

(dict) --
SnowballLimit (integer) --The service limit for number of Snowballs this account can have at once. The default service limit is 1 (one).

SnowballsInUse (integer) --The number of Snowballs that this account is currently using.






Examples
Returns information about the Snowball service limit for your account, and also the number of Snowballs your account has in use.

    :return: {
        'SnowballLimit': 123,
        'SnowballsInUse': 123
    }
    
    
    """
    pass

def get_software_updates(JobId=None):
    """
    Returns an Amazon S3 presigned URL for an update file associated with a specified JobId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_software_updates(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe ID for a job that you want to get the software update file for, for example JID123e4567-e89b-12d3-a456-426655440000 .\n

    :rtype: dict
ReturnsResponse Syntax{
    'UpdatesURI': 'string'
}


Response Structure

(dict) --
UpdatesURI (string) --The Amazon S3 presigned URL for the update file associated with the specified JobId value. The software update will be available for 2 days after this request is made. To access an update after the 2 days have passed, you\'ll have to make another call to GetSoftwareUpdates .






Exceptions

Snowball.Client.exceptions.InvalidResourceException
Snowball.Client.exceptions.InvalidJobStateException


    :return: {
        'UpdatesURI': 'string'
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

def list_cluster_jobs(ClusterId=None, MaxResults=None, NextToken=None):
    """
    Returns an array of JobListEntry objects of the specified length. Each JobListEntry object is for a job in the specified cluster and contains a job\'s state, a job\'s ID, and other information.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns an array of JobListEntry objects of the specified length. Each JobListEntry object is for a job in the specified cluster and contains a job\'s state, a job\'s ID, and other information.
    Expected Output:
    
    :example: response = client.list_cluster_jobs(
        ClusterId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe 39-character ID for the cluster that you want to list, for example CID123e4567-e89b-12d3-a456-426655440000 .\n

    :type MaxResults: integer
    :param MaxResults: The number of JobListEntry objects to return.

    :type NextToken: string
    :param NextToken: HTTP requests are stateless. To identify what object comes 'next' in the list of JobListEntry objects, you have the option of specifying NextToken as the starting point for your returned list.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobListEntries': [
        {
            'JobId': 'string',
            'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            'IsMaster': True|False,
            'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
            'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
            'CreationDate': datetime(2015, 1, 1),
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

JobListEntries (list) --
Each JobListEntry object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of export jobs.

(dict) --
Each JobListEntry object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of an export job.

JobId (string) --
The automatically generated ID for a job, for example JID123e4567-e89b-12d3-a456-426655440000 .

JobState (string) --
The current state of this job.

IsMaster (boolean) --
A value that indicates that this job is a master job. A master job represents a successful request to create an export job. Master jobs aren\'t associated with any Snowballs. Instead, each master job will have at least one job part, and each job part is associated with a Snowball. It might take some time before the job parts associated with a particular master job are listed, because they are created after the master job is created.

JobType (string) --
The type of job.

SnowballType (string) --
The type of device used with this job.

CreationDate (datetime) --
The creation date for this job.

Description (string) --
The optional description of this specific job, for example Important Photos 2016-08-11 .





NextToken (string) --
HTTP requests are stateless. If you use the automatically generated NextToken value in your next ListClusterJobsResult call, your list of returned jobs will start from this point in the array.







Exceptions

Snowball.Client.exceptions.InvalidResourceException
Snowball.Client.exceptions.InvalidNextTokenException

Examples
Returns an array of JobListEntry objects of the specified length. Each JobListEntry object is for a job in the specified cluster and contains a job\'s state, a job\'s ID, and other information.
response = client.list_cluster_jobs(
    ClusterId='CID123e4567-e89b-12d3-a456-426655440000',
)

print(response)


Expected Output:
{
    'JobListEntries': [
        {
            'CreationDate': datetime(2016, 11, 30, 3, 12, 4, 2, 335, 0),
            'Description': 'MyClustrer-node-001',
            'IsMaster': False,
            'JobId': 'JID123e4567-e89b-12d3-a456-426655440000',
            'JobState': 'New',
            'JobType': 'LOCAL_USE',
            'SnowballType': 'EDGE',
        },
        {
            'CreationDate': datetime(2016, 11, 30, 3, 12, 5, 2, 335, 0),
            'Description': 'MyClustrer-node-002',
            'IsMaster': False,
            'JobId': 'JID123e4567-e89b-12d3-a456-426655440001',
            'JobState': 'New',
            'JobType': 'LOCAL_USE',
            'SnowballType': 'EDGE',
        },
        {
            'CreationDate': datetime(2016, 11, 30, 3, 12, 5, 2, 335, 0),
            'Description': 'MyClustrer-node-003',
            'IsMaster': False,
            'JobId': 'JID123e4567-e89b-12d3-a456-426655440002',
            'JobState': 'New',
            'JobType': 'LOCAL_USE',
            'SnowballType': 'EDGE',
        },
        {
            'CreationDate': datetime(2016, 11, 30, 3, 12, 5, 2, 335, 0),
            'Description': 'MyClustrer-node-004',
            'IsMaster': False,
            'JobId': 'JID123e4567-e89b-12d3-a456-426655440003',
            'JobState': 'New',
            'JobType': 'LOCAL_USE',
            'SnowballType': 'EDGE',
        },
        {
            'CreationDate': datetime(2016, 11, 30, 3, 12, 5, 2, 335, 0),
            'Description': 'MyClustrer-node-005',
            'IsMaster': False,
            'JobId': 'JID123e4567-e89b-12d3-a456-426655440004',
            'JobState': 'New',
            'JobType': 'LOCAL_USE',
            'SnowballType': 'EDGE',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'JobListEntries': [
            {
                'JobId': 'string',
                'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
                'IsMaster': True|False,
                'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
                'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
                'CreationDate': datetime(2015, 1, 1),
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Snowball.Client.exceptions.InvalidResourceException
    Snowball.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def list_clusters(MaxResults=None, NextToken=None):
    """
    Returns an array of ClusterListEntry objects of the specified length. Each ClusterListEntry object contains a cluster\'s state, a cluster\'s ID, and other important status information.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns an array of ClusterListEntry objects of the specified length. Each ClusterListEntry object contains a cluster\'s state, a cluster\'s ID, and other important status information.
    Expected Output:
    
    :example: response = client.list_clusters(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The number of ClusterListEntry objects to return.

    :type NextToken: string
    :param NextToken: HTTP requests are stateless. To identify what object comes 'next' in the list of ClusterListEntry objects, you have the option of specifying NextToken as the starting point for your returned list.

    :rtype: dict

ReturnsResponse Syntax
{
    'ClusterListEntries': [
        {
            'ClusterId': 'string',
            'ClusterState': 'AwaitingQuorum'|'Pending'|'InUse'|'Complete'|'Cancelled',
            'CreationDate': datetime(2015, 1, 1),
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ClusterListEntries (list) --
Each ClusterListEntry object contains a cluster\'s state, a cluster\'s ID, and other important status information.

(dict) --
Contains a cluster\'s state, a cluster\'s ID, and other important information.

ClusterId (string) --
The 39-character ID for the cluster that you want to list, for example CID123e4567-e89b-12d3-a456-426655440000 .

ClusterState (string) --
The current state of this cluster. For information about the state of a specific node, see  JobListEntry$JobState .

CreationDate (datetime) --
The creation date for this cluster.

Description (string) --
Defines an optional description of the cluster, for example Environmental Data Cluster-01 .





NextToken (string) --
HTTP requests are stateless. If you use the automatically generated NextToken value in your next ClusterListEntry call, your list of returned clusters will start from this point in the array.







Exceptions

Snowball.Client.exceptions.InvalidNextTokenException

Examples
Returns an array of ClusterListEntry objects of the specified length. Each ClusterListEntry object contains a cluster\'s state, a cluster\'s ID, and other important status information.
response = client.list_clusters(
)

print(response)


Expected Output:
{
    'ClusterListEntries': [
        {
            'ClusterId': 'CID123e4567-e89b-12d3-a456-426655440000',
            'ClusterState': 'Pending',
            'CreationDate': datetime(2016, 11, 30, 3, 11, 57, 2, 335, 0),
            'Description': 'MyCluster',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'ClusterListEntries': [
            {
                'ClusterId': 'string',
                'ClusterState': 'AwaitingQuorum'|'Pending'|'InUse'|'Complete'|'Cancelled',
                'CreationDate': datetime(2015, 1, 1),
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Snowball.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def list_compatible_images(MaxResults=None, NextToken=None):
    """
    This action returns a list of the different Amazon EC2 Amazon Machine Images (AMIs) that are owned by your AWS account that would be supported for use on a Snowball Edge device. Currently, supported AMIs are based on the CentOS 7 (x86_64) - with Updates HVM, Ubuntu Server 14.04 LTS (HVM), and Ubuntu 16.04 LTS - Xenial (HVM) images, available on the AWS Marketplace.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_compatible_images(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results for the list of compatible images. Currently, a Snowball Edge device can store 10 AMIs.

    :type NextToken: string
    :param NextToken: HTTP requests are stateless. To identify what object comes 'next' in the list of compatible images, you can specify a value for NextToken as the starting point for your list of returned images.

    :rtype: dict

ReturnsResponse Syntax
{
    'CompatibleImages': [
        {
            'AmiId': 'string',
            'Name': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

CompatibleImages (list) --
A JSON-formatted object that describes a compatible AMI, including the ID and name for a Snowball Edge AMI.

(dict) --
A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including the ID and name for a Snowball Edge AMI. This AMI is compatible with the device\'s physical hardware requirements, and it should be able to be run in an SBE1 instance on the device.

AmiId (string) --
The unique identifier for an individual Snowball Edge AMI.

Name (string) --
The optional name of a compatible image.





NextToken (string) --
Because HTTP requests are stateless, this is the starting point for your next list of returned images.







Exceptions

Snowball.Client.exceptions.InvalidNextTokenException
Snowball.Client.exceptions.Ec2RequestFailedException


    :return: {
        'CompatibleImages': [
            {
                'AmiId': 'string',
                'Name': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Snowball.Client.exceptions.InvalidNextTokenException
    Snowball.Client.exceptions.Ec2RequestFailedException
    
    """
    pass

def list_jobs(MaxResults=None, NextToken=None):
    """
    Returns an array of JobListEntry objects of the specified length. Each JobListEntry object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of export jobs. Calling this API action in one of the US regions will return jobs from the list of all jobs associated with this account in all US regions.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns an array of JobListEntry objects of the specified length. Each JobListEntry object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of export jobs. Calling this API action in one of the US regions will return jobs from the list of all jobs associated with this account in all US regions.
    Expected Output:
    
    :example: response = client.list_jobs(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The number of JobListEntry objects to return.

    :type NextToken: string
    :param NextToken: HTTP requests are stateless. To identify what object comes 'next' in the list of JobListEntry objects, you have the option of specifying NextToken as the starting point for your returned list.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobListEntries': [
        {
            'JobId': 'string',
            'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            'IsMaster': True|False,
            'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
            'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
            'CreationDate': datetime(2015, 1, 1),
            'Description': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

JobListEntries (list) --
Each JobListEntry object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of export jobs.

(dict) --
Each JobListEntry object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of an export job.

JobId (string) --
The automatically generated ID for a job, for example JID123e4567-e89b-12d3-a456-426655440000 .

JobState (string) --
The current state of this job.

IsMaster (boolean) --
A value that indicates that this job is a master job. A master job represents a successful request to create an export job. Master jobs aren\'t associated with any Snowballs. Instead, each master job will have at least one job part, and each job part is associated with a Snowball. It might take some time before the job parts associated with a particular master job are listed, because they are created after the master job is created.

JobType (string) --
The type of job.

SnowballType (string) --
The type of device used with this job.

CreationDate (datetime) --
The creation date for this job.

Description (string) --
The optional description of this specific job, for example Important Photos 2016-08-11 .





NextToken (string) --
HTTP requests are stateless. If you use this automatically generated NextToken value in your next ListJobs call, your returned JobListEntry objects will start from this point in the array.







Exceptions

Snowball.Client.exceptions.InvalidNextTokenException

Examples
Returns an array of JobListEntry objects of the specified length. Each JobListEntry object contains a job\'s state, a job\'s ID, and a value that indicates whether the job is a job part, in the case of export jobs. Calling this API action in one of the US regions will return jobs from the list of all jobs associated with this account in all US regions.
response = client.list_jobs(
)

print(response)


Expected Output:
{
    'JobListEntries': [
        {
            'CreationDate': datetime(2016, 4, 14, 23, 56, 26, 3, 105, 0),
            'Description': 'MyJob',
            'IsMaster': False,
            'JobId': 'JID123e4567-e89b-12d3-a456-426655440000',
            'JobState': 'New',
            'JobType': 'IMPORT',
            'SnowballType': 'STANDARD',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'JobListEntries': [
            {
                'JobId': 'string',
                'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
                'IsMaster': True|False,
                'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
                'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG'|'EDGE_S',
                'CreationDate': datetime(2015, 1, 1),
                'Description': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Snowball.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def update_cluster(ClusterId=None, RoleARN=None, Description=None, Resources=None, AddressId=None, ShippingOption=None, Notification=None, ForwardingAddressId=None):
    """
    While a cluster\'s ClusterState value is in the AwaitingQuorum state, you can update some of the information associated with a cluster. Once the cluster changes to a different job state, usually 60 minutes after the cluster being created, this action is no longer available.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This action allows you to update certain parameters for a cluster. Once the cluster changes to a different state, usually within 60 minutes of it being created, this action is no longer available.
    Expected Output:
    
    :example: response = client.update_cluster(
        ClusterId='string',
        RoleARN='string',
        Description='string',
        Resources={
            'S3Resources': [
                {
                    'BucketArn': 'string',
                    'KeyRange': {
                        'BeginMarker': 'string',
                        'EndMarker': 'string'
                    }
                },
            ],
            'LambdaResources': [
                {
                    'LambdaArn': 'string',
                    'EventTriggers': [
                        {
                            'EventResourceARN': 'string'
                        },
                    ]
                },
            ],
            'Ec2AmiResources': [
                {
                    'AmiId': 'string',
                    'SnowballAmiId': 'string'
                },
            ]
        },
        AddressId='string',
        ShippingOption='SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
        Notification={
            'SnsTopicARN': 'string',
            'JobStatesToNotify': [
                'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            ],
            'NotifyAll': True|False
        },
        ForwardingAddressId='string'
    )
    
    
    :type ClusterId: string
    :param ClusterId: [REQUIRED]\nThe cluster ID of the cluster that you want to update, for example CID123e4567-e89b-12d3-a456-426655440000 .\n

    :type RoleARN: string
    :param RoleARN: The new role Amazon Resource Name (ARN) that you want to associate with this cluster. To create a role ARN, use the CreateRole API action in AWS Identity and Access Management (IAM).

    :type Description: string
    :param Description: The updated description of this cluster.

    :type Resources: dict
    :param Resources: The updated arrays of JobResource objects that can include updated S3Resource objects or LambdaResource objects.\n\nS3Resources (list) --An array of S3Resource objects.\n\n(dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.\n\nBucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.\n\nKeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.\n\nBeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.\n\nEndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.\n\n\n\n\n\n\n\nLambdaResources (list) --The Python-language Lambda functions for this job.\n\n(dict) --Identifies\n\nLambdaArn (string) --An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.\n\nEventTriggers (list) --The array of ARNs for S3Resource objects to trigger the LambdaResource objects associated with this job.\n\n(dict) --The container for the EventTriggerDefinition$EventResourceARN .\n\nEventResourceARN (string) --The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.\n\n\n\n\n\n\n\n\n\nEc2AmiResources (list) --The Amazon Machine Images (AMIs) associated with this job.\n\n(dict) --A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.\n\nAmiId (string) -- [REQUIRED]The ID of the AMI in Amazon EC2.\n\nSnowballAmiId (string) --The ID of the AMI on the Snowball Edge device.\n\n\n\n\n\n\n

    :type AddressId: string
    :param AddressId: The ID of the updated Address object.

    :type ShippingOption: string
    :param ShippingOption: The updated shipping option value of this cluster\'s ShippingDetails object.

    :type Notification: dict
    :param Notification: The new or updated Notification object.\n\nSnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.\nYou can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.\n\nJobStatesToNotify (list) --The list of job states that will trigger a notification for this job.\n\n(string) --\n\n\nNotifyAll (boolean) --Any change in job state will trigger a notification for this job.\n\n\n

    :type ForwardingAddressId: string
    :param ForwardingAddressId: The updated ID for the forwarding address for a cluster. This field is not supported in most regions.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Snowball.Client.exceptions.InvalidResourceException
Snowball.Client.exceptions.InvalidJobStateException
Snowball.Client.exceptions.KMSRequestFailedException
Snowball.Client.exceptions.InvalidInputCombinationException
Snowball.Client.exceptions.Ec2RequestFailedException

Examples
This action allows you to update certain parameters for a cluster. Once the cluster changes to a different state, usually within 60 minutes of it being created, this action is no longer available.
response = client.update_cluster(
    AddressId='ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b',
    ClusterId='CID123e4567-e89b-12d3-a456-426655440000',
    Description='Updated the address to send this to image processing - RJ',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_job(JobId=None, RoleARN=None, Notification=None, Resources=None, AddressId=None, ShippingOption=None, Description=None, SnowballCapacityPreference=None, ForwardingAddressId=None):
    """
    While a job\'s JobState value is New , you can update some of the information associated with a job. Once the job changes to a different job state, usually within 60 minutes of the job being created, this action is no longer available.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This action allows you to update certain parameters for a job. Once the job changes to a different job state, usually within 60 minutes of the job being created, this action is no longer available.
    Expected Output:
    
    :example: response = client.update_job(
        JobId='string',
        RoleARN='string',
        Notification={
            'SnsTopicARN': 'string',
            'JobStatesToNotify': [
                'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            ],
            'NotifyAll': True|False
        },
        Resources={
            'S3Resources': [
                {
                    'BucketArn': 'string',
                    'KeyRange': {
                        'BeginMarker': 'string',
                        'EndMarker': 'string'
                    }
                },
            ],
            'LambdaResources': [
                {
                    'LambdaArn': 'string',
                    'EventTriggers': [
                        {
                            'EventResourceARN': 'string'
                        },
                    ]
                },
            ],
            'Ec2AmiResources': [
                {
                    'AmiId': 'string',
                    'SnowballAmiId': 'string'
                },
            ]
        },
        AddressId='string',
        ShippingOption='SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
        Description='string',
        SnowballCapacityPreference='T50'|'T80'|'T100'|'T42'|'T98'|'NoPreference',
        ForwardingAddressId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe job ID of the job that you want to update, for example JID123e4567-e89b-12d3-a456-426655440000 .\n

    :type RoleARN: string
    :param RoleARN: The new role Amazon Resource Name (ARN) that you want to associate with this job. To create a role ARN, use the CreateRole AWS Identity and Access Management (IAM) API action.

    :type Notification: dict
    :param Notification: The new or updated Notification object.\n\nSnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.\nYou can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.\n\nJobStatesToNotify (list) --The list of job states that will trigger a notification for this job.\n\n(string) --\n\n\nNotifyAll (boolean) --Any change in job state will trigger a notification for this job.\n\n\n

    :type Resources: dict
    :param Resources: The updated JobResource object, or the updated JobResource object.\n\nS3Resources (list) --An array of S3Resource objects.\n\n(dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.\n\nBucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.\n\nKeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.\n\nBeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.\n\nEndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.\n\n\n\n\n\n\n\nLambdaResources (list) --The Python-language Lambda functions for this job.\n\n(dict) --Identifies\n\nLambdaArn (string) --An Amazon Resource Name (ARN) that represents an AWS Lambda function to be triggered by PUT object actions on the associated local Amazon S3 resource.\n\nEventTriggers (list) --The array of ARNs for S3Resource objects to trigger the LambdaResource objects associated with this job.\n\n(dict) --The container for the EventTriggerDefinition$EventResourceARN .\n\nEventResourceARN (string) --The Amazon Resource Name (ARN) for any local Amazon S3 resource that is an AWS Lambda function\'s event trigger associated with this job.\n\n\n\n\n\n\n\n\n\nEc2AmiResources (list) --The Amazon Machine Images (AMIs) associated with this job.\n\n(dict) --A JSON-formatted object that contains the IDs for an Amazon Machine Image (AMI), including the Amazon EC2 AMI ID and the Snowball Edge AMI ID. Each AMI has these two IDs to simplify identifying the AMI in both the AWS Cloud and on the device.\n\nAmiId (string) -- [REQUIRED]The ID of the AMI in Amazon EC2.\n\nSnowballAmiId (string) --The ID of the AMI on the Snowball Edge device.\n\n\n\n\n\n\n

    :type AddressId: string
    :param AddressId: The ID of the updated Address object.

    :type ShippingOption: string
    :param ShippingOption: The updated shipping option value of this job\'s ShippingDetails object.

    :type Description: string
    :param Description: The updated description of this job\'s JobMetadata object.

    :type SnowballCapacityPreference: string
    :param SnowballCapacityPreference: The updated SnowballCapacityPreference of this job\'s JobMetadata object. The 50 TB Snowballs are only available in the US regions.

    :type ForwardingAddressId: string
    :param ForwardingAddressId: The updated ID for the forwarding address for a job. This field is not supported in most regions.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Snowball.Client.exceptions.InvalidResourceException
Snowball.Client.exceptions.InvalidJobStateException
Snowball.Client.exceptions.KMSRequestFailedException
Snowball.Client.exceptions.InvalidInputCombinationException
Snowball.Client.exceptions.ClusterLimitExceededException
Snowball.Client.exceptions.Ec2RequestFailedException

Examples
This action allows you to update certain parameters for a job. Once the job changes to a different job state, usually within 60 minutes of the job being created, this action is no longer available.
response = client.update_job(
    AddressId='ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b',
    Description='Upgraded to Edge, shipped to Finance Dept, and requested faster shipping speed - TS.',
    JobId='JID123e4567-e89b-12d3-a456-426655440000',
    ShippingOption='NEXT_DAY',
    SnowballCapacityPreference='T100',
)

print(response)


Expected Output:
{
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

