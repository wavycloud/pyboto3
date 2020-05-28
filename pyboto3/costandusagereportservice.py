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

def delete_report_definition(ReportName=None):
    """
    Deletes the specified report.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_report_definition(
        ReportName='string'
    )
    
    
    :type ReportName: string
    :param ReportName: The name of the report that you want to create. The name must be unique, is case sensitive, and can\'t include spaces.

    :rtype: dict
ReturnsResponse Syntax{
    'ResponseMessage': 'string'
}


Response Structure

(dict) --If the action is successful, the service sends back an HTTP 200 response.

ResponseMessage (string) --Whether the deletion was successful or not.






Exceptions

CostandUsageReportService.Client.exceptions.InternalErrorException
CostandUsageReportService.Client.exceptions.ValidationException


    :return: {
        'ResponseMessage': 'string'
    }
    
    
    """
    pass

def describe_report_definitions(MaxResults=None, NextToken=None):
    """
    Lists the AWS Cost and  reports available to this account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_report_definitions(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results that AWS returns for the operation.

    :type NextToken: string
    :param NextToken: A generic string.

    :rtype: dict

ReturnsResponse Syntax
{
    'ReportDefinitions': [
        {
            'ReportName': 'string',
            'TimeUnit': 'HOURLY'|'DAILY',
            'Format': 'textORcsv'|'Parquet',
            'Compression': 'ZIP'|'GZIP'|'Parquet',
            'AdditionalSchemaElements': [
                'RESOURCES',
            ],
            'S3Bucket': 'string',
            'S3Prefix': 'string',
            'S3Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'eu-north-1'|'ap-northeast-3'|'ap-east-1',
            'AdditionalArtifacts': [
                'REDSHIFT'|'QUICKSIGHT'|'ATHENA',
            ],
            'RefreshClosedReports': True|False,
            'ReportVersioning': 'CREATE_NEW_REPORT'|'OVERWRITE_REPORT'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
If the action is successful, the service sends back an HTTP 200 response.

ReportDefinitions (list) --
A list of AWS Cost and Usage reports owned by the account.

(dict) --
The definition of AWS Cost and Usage Report. You can specify the report name, time unit, report format, compression format, S3 bucket, additional artifacts, and schema elements in the definition.

ReportName (string) --
The name of the report that you want to create. The name must be unique, is case sensitive, and can\'t include spaces.

TimeUnit (string) --
The length of time covered by the report.

Format (string) --
The format that AWS saves the report in.

Compression (string) --
The compression format that AWS uses for the report.

AdditionalSchemaElements (list) --
A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs.

(string) --
Whether or not AWS includes resource IDs in the report.



S3Bucket (string) --
The S3 bucket where AWS delivers the report.

S3Prefix (string) --
The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can\'t include spaces.

S3Region (string) --
The region of the S3 bucket that AWS delivers the report into.

AdditionalArtifacts (list) --
A list of manifests that you want Amazon Web Services to create for this report.

(string) --
The types of manifest that you want AWS to create for this report.



RefreshClosedReports (boolean) --
Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.

ReportVersioning (string) --
Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.





NextToken (string) --
A generic string.







Exceptions

CostandUsageReportService.Client.exceptions.InternalErrorException


    :return: {
        'ReportDefinitions': [
            {
                'ReportName': 'string',
                'TimeUnit': 'HOURLY'|'DAILY',
                'Format': 'textORcsv'|'Parquet',
                'Compression': 'ZIP'|'GZIP'|'Parquet',
                'AdditionalSchemaElements': [
                    'RESOURCES',
                ],
                'S3Bucket': 'string',
                'S3Prefix': 'string',
                'S3Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'eu-north-1'|'ap-northeast-3'|'ap-east-1',
                'AdditionalArtifacts': [
                    'REDSHIFT'|'QUICKSIGHT'|'ATHENA',
                ],
                'RefreshClosedReports': True|False,
                'ReportVersioning': 'CREATE_NEW_REPORT'|'OVERWRITE_REPORT'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CostandUsageReportService.Client.exceptions.InternalErrorException
    
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def modify_report_definition(ReportName=None, ReportDefinition=None):
    """
    Allows you to programatically update your report preferences.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.modify_report_definition(
        ReportName='string',
        ReportDefinition={
            'ReportName': 'string',
            'TimeUnit': 'HOURLY'|'DAILY',
            'Format': 'textORcsv'|'Parquet',
            'Compression': 'ZIP'|'GZIP'|'Parquet',
            'AdditionalSchemaElements': [
                'RESOURCES',
            ],
            'S3Bucket': 'string',
            'S3Prefix': 'string',
            'S3Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'eu-north-1'|'ap-northeast-3'|'ap-east-1',
            'AdditionalArtifacts': [
                'REDSHIFT'|'QUICKSIGHT'|'ATHENA',
            ],
            'RefreshClosedReports': True|False,
            'ReportVersioning': 'CREATE_NEW_REPORT'|'OVERWRITE_REPORT'
        }
    )
    
    
    :type ReportName: string
    :param ReportName: [REQUIRED]\nThe name of the report that you want to create. The name must be unique, is case sensitive, and can\'t include spaces.\n

    :type ReportDefinition: dict
    :param ReportDefinition: [REQUIRED]\nThe definition of AWS Cost and Usage Report. You can specify the report name, time unit, report format, compression format, S3 bucket, additional artifacts, and schema elements in the definition.\n\nReportName (string) -- [REQUIRED]The name of the report that you want to create. The name must be unique, is case sensitive, and can\'t include spaces.\n\nTimeUnit (string) -- [REQUIRED]The length of time covered by the report.\n\nFormat (string) -- [REQUIRED]The format that AWS saves the report in.\n\nCompression (string) -- [REQUIRED]The compression format that AWS uses for the report.\n\nAdditionalSchemaElements (list) -- [REQUIRED]A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs.\n\n(string) --Whether or not AWS includes resource IDs in the report.\n\n\n\nS3Bucket (string) -- [REQUIRED]The S3 bucket where AWS delivers the report.\n\nS3Prefix (string) -- [REQUIRED]The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can\'t include spaces.\n\nS3Region (string) -- [REQUIRED]The region of the S3 bucket that AWS delivers the report into.\n\nAdditionalArtifacts (list) --A list of manifests that you want Amazon Web Services to create for this report.\n\n(string) --The types of manifest that you want AWS to create for this report.\n\n\n\nRefreshClosedReports (boolean) --Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.\n\nReportVersioning (string) --Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

CostandUsageReportService.Client.exceptions.InternalErrorException
CostandUsageReportService.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_report_definition(ReportDefinition=None):
    """
    Creates a new report using the description that you provide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_report_definition(
        ReportDefinition={
            'ReportName': 'string',
            'TimeUnit': 'HOURLY'|'DAILY',
            'Format': 'textORcsv'|'Parquet',
            'Compression': 'ZIP'|'GZIP'|'Parquet',
            'AdditionalSchemaElements': [
                'RESOURCES',
            ],
            'S3Bucket': 'string',
            'S3Prefix': 'string',
            'S3Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'eu-north-1'|'ap-northeast-3'|'ap-east-1',
            'AdditionalArtifacts': [
                'REDSHIFT'|'QUICKSIGHT'|'ATHENA',
            ],
            'RefreshClosedReports': True|False,
            'ReportVersioning': 'CREATE_NEW_REPORT'|'OVERWRITE_REPORT'
        }
    )
    
    
    :type ReportDefinition: dict
    :param ReportDefinition: [REQUIRED]\nRepresents the output of the PutReportDefinition operation. The content consists of the detailed metadata and data file information.\n\nReportName (string) -- [REQUIRED]The name of the report that you want to create. The name must be unique, is case sensitive, and can\'t include spaces.\n\nTimeUnit (string) -- [REQUIRED]The length of time covered by the report.\n\nFormat (string) -- [REQUIRED]The format that AWS saves the report in.\n\nCompression (string) -- [REQUIRED]The compression format that AWS uses for the report.\n\nAdditionalSchemaElements (list) -- [REQUIRED]A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs.\n\n(string) --Whether or not AWS includes resource IDs in the report.\n\n\n\nS3Bucket (string) -- [REQUIRED]The S3 bucket where AWS delivers the report.\n\nS3Prefix (string) -- [REQUIRED]The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can\'t include spaces.\n\nS3Region (string) -- [REQUIRED]The region of the S3 bucket that AWS delivers the report into.\n\nAdditionalArtifacts (list) --A list of manifests that you want Amazon Web Services to create for this report.\n\n(string) --The types of manifest that you want AWS to create for this report.\n\n\n\nRefreshClosedReports (boolean) --Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.\n\nReportVersioning (string) --Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.




Exceptions

CostandUsageReportService.Client.exceptions.DuplicateReportNameException
CostandUsageReportService.Client.exceptions.ReportLimitReachedException
CostandUsageReportService.Client.exceptions.InternalErrorException
CostandUsageReportService.Client.exceptions.ValidationException


    :return: {}
    
    
    """
    pass

