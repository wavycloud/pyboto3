"""
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
"""


def can_paginate(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
    :type operation_name: string
    """
    pass


def cancel_job(JobId=None):
    """
    :param JobId: [REQUIRED]
            The 39 character job ID for the job that you want to cancel, for example JID123e4567-e89b-12d3-a456-426655440000 .
            Return typedict
            ReturnsResponse Syntax{}
            Response Structure
            (dict) --
            
    :type JobId: string
    """
    pass


def create_address(Address=None):
    """
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
            Return typedict
            ReturnsResponse Syntax{
              'AddressId': 'string'
            }
            Response Structure
            (dict) --
            AddressId (string) --The automatically generated ID for a specific address. You'll use this ID when you create a job to specify which address you want the Snowball for that job shipped to.
            
            
    :type Address: dict
    """
    pass


def create_job(JobType=None, Resources=None, Description=None, AddressId=None, KmsKeyARN=None, RoleARN=None,
               SnowballCapacityPreference=None, ShippingOption=None, Notification=None):
    """
    :param JobType: [REQUIRED]
            Defines the type of job that you're creating.
            
    :type JobType: string
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
            
            
            
    :type Resources: dict
    :param Description: Defines an optional description of this specific job, for example Important Photos 2016-08-11 .
    :type Description: string
    :param AddressId: [REQUIRED]
            The ID for the address that you want the Snowball shipped to.
            
    :type AddressId: string
    :param KmsKeyARN: The KmsKeyARN that you want to associate with this job. KmsKeyARN s are created using the CreateKey AWS Key Management Service (KMS) API action.
    :type KmsKeyARN: string
    :param RoleARN: [REQUIRED]
            The RoleARN that you want to associate with this job. RoleArn s are created using the CreateRole AWS Identity and Access Management (IAM) API action.
            
    :type RoleARN: string
    :param SnowballCapacityPreference: If your job is being created in one of the US regions, you have the option of specifying what size Snowball you'd like for this job. In all other regions, Snowballs come with 80 TB in storage capacity.
    :type SnowballCapacityPreference: string
    :param ShippingOption: [REQUIRED]
            The shipping speed for this job. Note that this speed does not dictate how soon you'll get the Snowball, rather it represents how quickly the Snowball moves to its destination while in transit. Regional shipping speeds are as follows:
            In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day.
            In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
            In India, Snowballs are delivered in one to seven days.
            In the US, you have access to one-day shipping and two-day shipping.
            
    :type ShippingOption: string
    :param Notification: Defines the Amazon Simple Notification Service (Amazon SNS) notification settings for this job.
            SnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.
            Note that you can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.
            JobStatesToNotify (list) --The list of job states that will trigger a notification for this job.
            (string) --
            NotifyAll (boolean) --Any change in job state will trigger a notification for this job.
            
    :type Notification: dict
    """
    pass


def describe_address(AddressId=None):
    """
    :param AddressId: [REQUIRED]
            The automatically generated ID for a specific address.
            Return typedict
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
                'PhoneNumber': 'string'
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
            PrefectureOrDistrict (string) --The prefecture or district in an address that a Snowball is to be delivered to.
            Landmark (string) --A landmark listed in an address that a Snowball is to be delivered to.
            Country (string) --The country in an address that a Snowball is to be delivered to.
            PostalCode (string) --The postal code in an address that a Snowball is to be delivered to.
            PhoneNumber (string) --The phone number associated with an address that a Snowball is to be delivered to.
            
            
            
    :type AddressId: string
    """
    pass


def describe_addresses(MaxResults=None, NextToken=None):
    """
    :param MaxResults: The number of ADDRESS objects to return.
    :type MaxResults: integer
    :param NextToken: HTTP requests are stateless. To identify what object comes 'next' in the list of ADDRESS objects, you have the option of specifying a value for NextToken as the starting point for your list of returned addresses.
    :type NextToken: string
    """
    pass


def describe_job(JobId=None):
    """
    :param JobId: [REQUIRED]
            The automatically generated ID for a job, for example JID123e4567-e89b-12d3-a456-426655440000 .
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --
            JobMetadata (dict) --Information about a specific job, including shipping information, job status, and other important metadata.
            JobId (string) --The automatically generated ID for a job, for example JID123e4567-e89b-12d3-a456-426655440000 .
            JobState (string) --The current state of the jobs.
            JobType (string) --The type of job.
            CreationDate (datetime) --The creation date for this job.
            Resources (dict) --An array of S3Resource objects. Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into.
            S3Resources (list) --An array of S3Resource objects.
            (dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.
            BucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.
            KeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.
            BeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
            EndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
            
            
            Description (string) --The description of the job, provided at job creation.
            KmsKeyARN (string) --The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key associated with this job. This ARN was created using the CreateKey API action in AWS KMS.
            RoleARN (string) --The role ARN associated with this job. This ARN was created using the CreateRole API action in AWS Identity and Access Management (IAM).
            AddressId (string) --The ID for the address that you want the Snowball shipped to.
            ShippingDetails (dict) --A job's shipping information, including inbound and outbound tracking numbers and shipping speed options.
            ShippingOption (string) --The shipping speed for a particular job. Note that this speed does not dictate how soon you'll get the Snowball from the job's creation date. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:
            In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day.
            In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
            In India, Snowballs are delivered in one to seven days.
            In the United States of America (US), you have access to one-day shipping and two-day shipping.
            InboundShipment (dict) --The Status and TrackingNumber values for a Snowball being delivered to the address that you specified for a particular job.
            Status (string) --Status information for a shipment. Valid statuses include NEW , IN_TRANSIT , and DELIVERED .
            TrackingNumber (string) --The tracking number for this job. Using this tracking number with your region's carrier's website, you can track a Snowball as the carrier transports it.
            For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
            OutboundShipment (dict) --The Status and TrackingNumber values for a Snowball being returned to AWS for a particular job.
            Status (string) --Status information for a shipment. Valid statuses include NEW , IN_TRANSIT , and DELIVERED .
            TrackingNumber (string) --The tracking number for this job. Using this tracking number with your region's carrier's website, you can track a Snowball as the carrier transports it.
            For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
            
            SnowballCapacityPreference (string) --The Snowball capacity preference for this job, specified at job creation. In US regions, you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity Snowballs.
            Notification (dict) --The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a specific job. The Notification object is returned as a part of the response syntax of the DescribeJob action in the JobMetadata data type.
            SnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.
            Note that you can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.
            JobStatesToNotify (list) --The list of job states that will trigger a notification for this job.
            (string) --
            NotifyAll (boolean) --Any change in job state will trigger a notification for this job.
            DataTransferProgress (dict) --A value that defines the real-time status of a Snowball's data transfer while the appliance is at AWS. Note that this data is only available while a job has a JobState value of InProgress , for both import and export jobs.
            BytesTransferred (integer) --The number of bytes transferred between a Snowball and Amazon S3.
            ObjectsTransferred (integer) --The number of objects transferred between a Snowball and Amazon S3.
            TotalBytes (integer) --The total bytes of data for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.
            TotalObjects (integer) --The total number of objects for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.
            JobLogInfo (dict) --Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job report becomes available at the end of the import process. For export jobs, your job report typically becomes available while the Snowball for your job part is being delivered to you.
            JobCompletionReportURI (string) --A link to an Amazon S3 presigned URL where the job completion report is located.
            JobSuccessLogURI (string) --A link to an Amazon S3 presigned URL where the job success log is located.
            JobFailureLogURI (string) --A link to an Amazon S3 presigned URL where the job failure log is located.
            
            SubJobMetadata (list) --Information about a specific job part (in the case of an export job), including shipping information, job status, and other important metadata.
            (dict) --Contains information about a specific job including shipping information, job status, and other important metadata. This information is returned as a part of the response syntax of the DescribeJob action.
            JobId (string) --The automatically generated ID for a job, for example JID123e4567-e89b-12d3-a456-426655440000 .
            JobState (string) --The current state of the jobs.
            JobType (string) --The type of job.
            CreationDate (datetime) --The creation date for this job.
            Resources (dict) --An array of S3Resource objects. Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into.
            S3Resources (list) --An array of S3Resource objects.
            (dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.
            BucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.
            KeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.
            BeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
            EndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
            
            
            Description (string) --The description of the job, provided at job creation.
            KmsKeyARN (string) --The Amazon Resource Name (ARN) for the AWS Key Management Service (AWS KMS) key associated with this job. This ARN was created using the CreateKey API action in AWS KMS.
            RoleARN (string) --The role ARN associated with this job. This ARN was created using the CreateRole API action in AWS Identity and Access Management (IAM).
            AddressId (string) --The ID for the address that you want the Snowball shipped to.
            ShippingDetails (dict) --A job's shipping information, including inbound and outbound tracking numbers and shipping speed options.
            ShippingOption (string) --The shipping speed for a particular job. Note that this speed does not dictate how soon you'll get the Snowball from the job's creation date. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:
            In Australia, you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day.
            In the European Union (EU), you have access to express shipping. Typically, Snowballs shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.
            In India, Snowballs are delivered in one to seven days.
            In the United States of America (US), you have access to one-day shipping and two-day shipping.
            InboundShipment (dict) --The Status and TrackingNumber values for a Snowball being delivered to the address that you specified for a particular job.
            Status (string) --Status information for a shipment. Valid statuses include NEW , IN_TRANSIT , and DELIVERED .
            TrackingNumber (string) --The tracking number for this job. Using this tracking number with your region's carrier's website, you can track a Snowball as the carrier transports it.
            For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
            OutboundShipment (dict) --The Status and TrackingNumber values for a Snowball being returned to AWS for a particular job.
            Status (string) --Status information for a shipment. Valid statuses include NEW , IN_TRANSIT , and DELIVERED .
            TrackingNumber (string) --The tracking number for this job. Using this tracking number with your region's carrier's website, you can track a Snowball as the carrier transports it.
            For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.
            
            SnowballCapacityPreference (string) --The Snowball capacity preference for this job, specified at job creation. In US regions, you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity Snowballs.
            Notification (dict) --The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a specific job. The Notification object is returned as a part of the response syntax of the DescribeJob action in the JobMetadata data type.
            SnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.
            Note that you can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.
            JobStatesToNotify (list) --The list of job states that will trigger a notification for this job.
            (string) --
            NotifyAll (boolean) --Any change in job state will trigger a notification for this job.
            DataTransferProgress (dict) --A value that defines the real-time status of a Snowball's data transfer while the appliance is at AWS. Note that this data is only available while a job has a JobState value of InProgress , for both import and export jobs.
            BytesTransferred (integer) --The number of bytes transferred between a Snowball and Amazon S3.
            ObjectsTransferred (integer) --The number of objects transferred between a Snowball and Amazon S3.
            TotalBytes (integer) --The total bytes of data for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.
            TotalObjects (integer) --The total number of objects for a transfer between a Snowball and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.
            JobLogInfo (dict) --Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job report becomes available at the end of the import process. For export jobs, your job report typically becomes available while the Snowball for your job part is being delivered to you.
            JobCompletionReportURI (string) --A link to an Amazon S3 presigned URL where the job completion report is located.
            JobSuccessLogURI (string) --A link to an Amazon S3 presigned URL where the job success log is located.
            JobFailureLogURI (string) --A link to an Amazon S3 presigned URL where the job failure log is located.
            
            
            
            
    :type JobId: string
    """
    pass


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    :param ClientMethod: The client method to presign for
    :type ClientMethod: string
    :param Params: The parameters normally passed to
            ClientMethod.
    :type Params: dict
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
    :type ExpiresIn: int
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
    :type HttpMethod: string
    """
    pass


def get_job_manifest(JobId=None):
    """
    :param JobId: [REQUIRED]
            The ID for a job that you want to get the manifest file for, for example JID123e4567-e89b-12d3-a456-426655440000 .
            Return typedict
            ReturnsResponse Syntax{
              'ManifestURI': 'string'
            }
            Response Structure
            (dict) --
            ManifestURI (string) --The Amazon S3 presigned URL for the manifest file associated with the specified JobId value.
            
            
    :type JobId: string
    """
    pass


def get_job_unlock_code(JobId=None):
    """
    :param JobId: [REQUIRED]
            The ID for the job that you want to get the UnlockCode value for, for example JID123e4567-e89b-12d3-a456-426655440000 .
            Return typedict
            ReturnsResponse Syntax{
              'UnlockCode': 'string'
            }
            Response Structure
            (dict) --
            UnlockCode (string) --The UnlockCode value for the specified job. The UnlockCode value can be accessed for up to 90 days after the job has been created.
            
            
    :type JobId: string
    """
    pass


def get_paginator(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
    :type operation_name: string
    """
    pass


def get_snowball_usage():
    """
    """
    pass


def get_waiter():
    """
    """
    pass


def list_jobs(MaxResults=None, NextToken=None):
    """
    :param MaxResults: The number of JobListEntry objects to return.
    :type MaxResults: integer
    :param NextToken: HTTP requests are stateless. To identify what object comes 'next' in the list of JobListEntry objects, you have the option of specifying NextToken as the starting point for your returned list.
    :type NextToken: string
    """
    pass


def update_job(JobId=None, RoleARN=None, Notification=None, Resources=None, AddressId=None, ShippingOption=None,
               Description=None, SnowballCapacityPreference=None):
    """
    :param JobId: [REQUIRED]
            The job ID of the job that you want to update, for example JID123e4567-e89b-12d3-a456-426655440000 .
            
    :type JobId: string
    :param RoleARN: The new role Amazon Resource Name (ARN) that you want to associate with this job. To create a role ARN, use the CreateRole AWS Identity and Access Management (IAM) API action.
    :type RoleARN: string
    :param Notification: The new or updated Notification object.
            SnsTopicARN (string) --The new SNS TopicArn that you want to associate with this job. You can create Amazon Resource Names (ARNs) for topics by using the CreateTopic Amazon SNS API action.
            Note that you can subscribe email addresses to an Amazon SNS topic through the AWS Management Console, or by using the Subscribe AWS Simple Notification Service (SNS) API action.
            JobStatesToNotify (list) --The list of job states that will trigger a notification for this job.
            (string) --
            NotifyAll (boolean) --Any change in job state will trigger a notification for this job.
            
    :type Notification: dict
    :param Resources: The updated S3Resource object (for a single Amazon S3 bucket or key range), or the updated JobResource object (for multiple buckets or key ranges).
            S3Resources (list) --An array of S3Resource objects.
            (dict) --Each S3Resource object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional KeyRange value. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.
            BucketArn (string) --The Amazon Resource Name (ARN) of an Amazon S3 bucket.
            KeyRange (dict) --For export jobs, you can provide an optional KeyRange within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive BeginMarker , an inclusive EndMarker , or both. Ranges are UTF-8 binary sorted.
            BeginMarker (string) --The key that starts an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
            EndMarker (string) --The key that ends an optional key range for an export job. Ranges are inclusive and UTF-8 binary sorted.
            
            
            
    :type Resources: dict
    :param AddressId: The ID of the updated Address object.
    :type AddressId: string
    :param ShippingOption: The updated shipping option value of this job's ShippingDetails object.
    :type ShippingOption: string
    :param Description: The updated description of this job's JobMetadata object.
    :type Description: string
    :param SnowballCapacityPreference: The updated SnowballCapacityPreference of this job's JobMetadata object. Note that the 50 TB Snowballs are only available in the US regions.
    :type SnowballCapacityPreference: string
    """
    pass
