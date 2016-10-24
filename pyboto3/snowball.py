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

def cancel_job(JobId=None):
    """
    Cancels the specified job. Note that you can only cancel a job before its JobState value changes to PreparingAppliance . Requesting the ListJobs or DescribeJob action will return a job's JobState as part of the response element data returned.
    
    
    :example: response = client.cancel_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The 39 character job ID for the job that you want to cancel, for example JID123e4567-e89b-12d3-a456-426655440000 .
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def create_address(Address=None):
    """
    Creates an address for a Snowball to be shipped to.
    Addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. If the address is invalid or unsupported, then an exception is thrown.
    
    
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
            'PhoneNumber': 'string'
        }
    )
    
    
    :type Address: dict
    :param Address: [REQUIRED]
            The address that you want the Snowball shipped to.
            AddressId (string) --The unique ID for an address.
            Name (string) --The name of a person to receive a Snowball at an address.
            Company (string) --The name of the company to receive a Snowball at an address.
            Street1 (string) --The first line in a street address that a Snowball is to be delivered to.
            Street2 (string) --The second line in a street address that a Snowball is to be delivered to.
            Street3 (string) --The third line in a street address that a Snowball is to be delivered to.
            City (string) --The city in an address that a Snowball is to be delivered to.
            StateOrProvince (string) --The state or province in an address that a Snowball is to be delivered to.
            PrefectureOrDistrict (string) --The prefecture or district in an address that a Snowball is to be delivered to.
            Landmark (string) --A landmark listed in an address that a Snowball is to be delivered to.
            Country (string) --The country in an address that a Snowball is to be delivered to.
            PostalCode (string) --The postal code in an address that a Snowball is to be delivered to.
            PhoneNumber (string) --The phone number associated with an address that a Snowball is to be delivered to.
            

    :rtype: dict
    :return: {
        'AddressId': 'string'
    }
    
    
    """
    pass

def create_job(JobType=None, Resources=None, Description=None, AddressId=None, KmsKeyARN=None, RoleARN=None, SnowballCapacityPreference=None, ShippingOption=None, Notification=None):
    """
    Creates a job to import or export data between Amazon S3 and your on-premises data center. Note that your AWS account must have the right trust policies and permissions in place to create a job for Snowball. For more information, see  api-reference-policies .
    
    
    :example: response = client.create_job(
        JobType='IMPORT'|'EXPORT',
        Resources={
            'S3Resources': [
                {
                    'BucketArn': 'string',
                    'KeyRange': {
                        'BeginMarker': 'string',
                        'EndMarker': 'string'
                    }
                },
            ]
        },
        Description='string',
        AddressId='string',
        KmsKeyARN='string',
        RoleARN='string',
        SnowballCapacityPreference='T50'|'T80'|'NoPreference',
        ShippingOption='SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
        Notification={
            'SnsTopicARN': 'string',
            'JobStatesToNotify': [
                'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            ],
            'NotifyAll': True|False
        }
    )
    
    
    :type JobType: string
    :param JobType: [REQUIRED]
            Defines the type of job that you're creating.
            

    :type Resources: dict
    :param Resources: [REQUIRED]
            Defines the Amazon S3 buckets associated with this job.
            With IMPORT jobs, you specify the bucket or buckets that your transferred data will be imported into.
            With EXPORT jobs, you specify the bucket or buckets that your transferred data will be exported from. Optionally, you can also specify a KeyRange value. If you choose to export a range, you define the length of the range by providing either an inclusive BeginMarker value, an inclusive EndMarker value, or both. Ranges are UTF-8 binary sorted.
            S3Resources (list) --An array of S3Resource objects.
            (dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.
            BucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.
            KeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.
            BeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
            EndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
            
            
            

    :type Description: string
    :param Description: Defines an optional description of this specific job, for example Important Photos 2016-08-11 .

    :type AddressId: string
    :param AddressId: [REQUIRED]
            The ID for the address that you want the Snowball shipped to.
            

    :type KmsKeyARN: string
    :param KmsKeyARN: The KmsKeyARN that you want to associate with this job. KmsKeyARN s are created using the CreateKey AWS Key Management Service (KMS) API action.

    :type RoleARN: string
    :param RoleARN: [REQUIRED]
            The RoleARN that you want to associate with this job. RoleArn s are created using the CreateRole AWS Identity and Access Management (IAM) API action.
            

    :type SnowballCapacityPreference: string
    :param SnowballCapacityPreference: If your job is being created in one of the US regions, you have the option of specifying what size Snowball you'd like for this job. In all other regions, Snowballs come with 80 TB in storage capacity.

    :type ShippingOption: string
    :param ShippingOption: [REQUIRED]
            The shipping speed for this job. Note that this speed does not dictate how soon you'll get the Snowball, rather it represents how quickly the Snowball moves to its destination while in transit. Regional shipping speeds are as follows:
            In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day.
            In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
            In India, Snowballs are delivered in one to seven days.
            In the US, you have access to one-day shipping and two-day shipping.
            

    :type Notification: dict
    :param Notification: Defines the Amazon Simple Notification Service (Amazon SNS) notification settings for this job.
            SnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.
            Note that you can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.
            JobStatesToNotify (list) --The list of job states that will trigger a notification for this job.
            (string) --
            NotifyAll (boolean) --Any change in job state will trigger a notification for this job.
            

    :rtype: dict
    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

def describe_address(AddressId=None):
    """
    Takes an AddressId and returns specific details about that address in the form of an Address object.
    
    
    :example: response = client.describe_address(
        AddressId='string'
    )
    
    
    :type AddressId: string
    :param AddressId: [REQUIRED]
            The automatically generated ID for a specific address.
            

    :rtype: dict
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
            'PhoneNumber': 'string'
        }
    }
    
    
    """
    pass

def describe_addresses(MaxResults=None, NextToken=None):
    """
    Returns a specified number of ADDRESS objects. Calling this API in one of the US regions will return addresses from the list of all addresses associated with this account in all US regions.
    
    
    :example: response = client.describe_addresses(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The number of ADDRESS objects to return.

    :type NextToken: string
    :param NextToken: HTTP requests are stateless. To identify what object comes 'next' in the list of ADDRESS objects, you have the option of specifying a value for NextToken as the starting point for your list of returned addresses.

    :rtype: dict
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
                'PhoneNumber': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_job(JobId=None):
    """
    Returns information about a specific job including shipping information, job status, and other important metadata.
    
    
    :example: response = client.describe_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The automatically generated ID for a job, for example JID123e4567-e89b-12d3-a456-426655440000 .
            

    :rtype: dict
    :return: {
        'JobMetadata': {
            'JobId': 'string',
            'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
            'JobType': 'IMPORT'|'EXPORT',
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
            'SnowballCapacityPreference': 'T50'|'T80'|'NoPreference',
            'Notification': {
                'SnsTopicARN': 'string',
                'JobStatesToNotify': [
                    'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
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
            }
        },
        'SubJobMetadata': [
            {
                'JobId': 'string',
                'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
                'JobType': 'IMPORT'|'EXPORT',
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
                'SnowballCapacityPreference': 'T50'|'T80'|'NoPreference',
                'Notification': {
                    'SnsTopicARN': 'string',
                    'JobStatesToNotify': [
                        'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
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

def get_job_manifest(JobId=None):
    """
    Returns a link to an Amazon S3 presigned URL for the manifest file associated with the specified JobId value. You can access the manifest file for up to 60 minutes after this request has been made. To access the manifest file after 60 minutes have passed, you'll have to make another call to the GetJobManifest action.
    The manifest is an encrypted file that you can download after your job enters the WithCustomer status. The manifest is decrypted by using the UnlockCode code value, when you pass both values to the Snowball through the Snowball client when the client is started for the first time.
    As a best practice, we recommend that you don't save a copy of an UnlockCode value in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snowball associated with that job.
    Note that the credentials of a given job, including its manifest file and unlock code, expire 90 days after the job is created.
    
    
    :example: response = client.get_job_manifest(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The ID for a job that you want to get the manifest file for, for example JID123e4567-e89b-12d3-a456-426655440000 .
            

    :rtype: dict
    :return: {
        'ManifestURI': 'string'
    }
    
    
    """
    pass

def get_job_unlock_code(JobId=None):
    """
    Returns the UnlockCode code value for the specified job. A particular UnlockCode value can be accessed for up to 90 days after the associated job has been created.
    The UnlockCode value is a 29-character code with 25 alphanumeric characters and 4 hyphens. This code is used to decrypt the manifest file when it is passed along with the manifest to the Snowball through the Snowball client when the client is started for the first time.
    As a best practice, we recommend that you don't save a copy of the UnlockCode in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snowball associated with that job.
    
    
    :example: response = client.get_job_unlock_code(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The ID for the job that you want to get the UnlockCode value for, for example JID123e4567-e89b-12d3-a456-426655440000 .
            

    :rtype: dict
    :return: {
        'UnlockCode': 'string'
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

def get_snowball_usage():
    """
    Returns information about the Snowball service limit for your account, and also the number of Snowballs your account has in use.
    Note that the default service limit for the number of Snowballs that you can have at one time is 1. If you want to increase your service limit, contact AWS Support.
    
    
    :example: response = client.get_snowball_usage()
    
    
    :rtype: dict
    :return: {
        'SnowballLimit': 123,
        'SnowballsInUse': 123
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_jobs(MaxResults=None, NextToken=None):
    """
    Returns an array of JobListEntry objects of the specified length. Each JobListEntry object contains a job's state, a job's ID, and a value that indicates whether the job is a job part, in the case of export jobs. Calling this API action in one of the US regions will return jobs from the list of all jobs associated with this account in all US regions.
    
    
    :example: response = client.list_jobs(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The number of JobListEntry objects to return.

    :type NextToken: string
    :param NextToken: HTTP requests are stateless. To identify what object comes 'next' in the list of JobListEntry objects, you have the option of specifying NextToken as the starting point for your returned list.

    :rtype: dict
    :return: {
        'JobListEntries': [
            {
                'JobId': 'string',
                'JobState': 'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
                'IsMaster': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def update_job(JobId=None, RoleARN=None, Notification=None, Resources=None, AddressId=None, ShippingOption=None, Description=None, SnowballCapacityPreference=None):
    """
    While a job's JobState value is New , you can update some of the information associated with a job. Once the job changes to a different job state, usually within 60 minutes of the job being created, this action is no longer available.
    
    
    :example: response = client.update_job(
        JobId='string',
        RoleARN='string',
        Notification={
            'SnsTopicARN': 'string',
            'JobStatesToNotify': [
                'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'|'InTransitToAWS'|'WithAWS'|'InProgress'|'Complete'|'Cancelled'|'Listing'|'Pending',
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
            ]
        },
        AddressId='string',
        ShippingOption='SECOND_DAY'|'NEXT_DAY'|'EXPRESS'|'STANDARD',
        Description='string',
        SnowballCapacityPreference='T50'|'T80'|'NoPreference'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The job ID of the job that you want to update, for example JID123e4567-e89b-12d3-a456-426655440000 .
            

    :type RoleARN: string
    :param RoleARN: The new role Amazon Resource Name (ARN) that you want to associate with this job. To create a role ARN, use the CreateRole AWS Identity and Access Management (IAM) API action.

    :type Notification: dict
    :param Notification: The new or updated Notification object.
            SnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.
            Note that you can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.
            JobStatesToNotify (list) --The list of job states that will trigger a notification for this job.
            (string) --
            NotifyAll (boolean) --Any change in job state will trigger a notification for this job.
            

    :type Resources: dict
    :param Resources: The updated S3Resource object (for a single Amazon S3 bucket or key range), or the updated JobResource object (for multiple buckets or key ranges).
            S3Resources (list) --An array of S3Resource objects.
            (dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.
            BucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.
            KeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.
            BeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
            EndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
            
            
            

    :type AddressId: string
    :param AddressId: The ID of the updated Address object.

    :type ShippingOption: string
    :param ShippingOption: The updated shipping option value of this job's ShippingDetails object.

    :type Description: string
    :param Description: The updated description of this job's JobMetadata object.

    :type SnowballCapacityPreference: string
    :param SnowballCapacityPreference: The updated SnowballCapacityPreference of this job's JobMetadata object. Note that the 50 TB Snowballs are only available in the US regions.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

