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

def delete_report_definition(ReportName=None):
    """
    Delete a specified report definition
    See also: AWS API Documentation
    
    
    :example: response = client.delete_report_definition(
        ReportName='string'
    )
    
    
    :type ReportName: string
    :param ReportName: Preferred name for a report, it has to be unique. Must starts with a number/letter, case sensitive. Limited to 256 characters.

    :rtype: dict
    :return: {
        'ResponseMessage': 'string'
    }
    
    
    """
    pass

def describe_report_definitions(MaxResults=None, NextToken=None):
    """
    Describe a list of report definitions owned by the account
    See also: AWS API Documentation
    
    
    :example: response = client.describe_report_definitions(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The max number of results returned by the operation.

    :type NextToken: string
    :param NextToken: A generic string.

    :rtype: dict
    :return: {
        'ReportDefinitions': [
            {
                'ReportName': 'string',
                'TimeUnit': 'HOURLY'|'DAILY',
                'Format': 'textORcsv',
                'Compression': 'ZIP'|'GZIP',
                'AdditionalSchemaElements': [
                    'RESOURCES',
                ],
                'S3Bucket': 'string',
                'S3Prefix': 'string',
                'S3Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1',
                'AdditionalArtifacts': [
                    'REDSHIFT'|'QUICKSIGHT',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- Response of DescribeReportDefinitions
    ReportDefinitions (list) -- A list of report definitions.
    (dict) -- The definition of AWS Cost and Usage Report. Customer can specify the report name, time unit, report format, compression format, S3 bucket and additional artifacts and schema elements in the definition.
    ReportName (string) -- Preferred name for a report, it has to be unique. Must starts with a number/letter, case sensitive. Limited to 256 characters.
    TimeUnit (string) -- The frequency on which report data are measured and displayed.
    Format (string) -- Preferred format for report.
    Compression (string) -- Preferred compression format for report.
    AdditionalSchemaElements (list) -- A list of schema elements.
    (string) -- Preference of including Resource IDs. You can include additional details about individual resource IDs in your report.
    
    
    S3Bucket (string) -- Name of customer S3 bucket.
    S3Prefix (string) -- Preferred report path prefix. Limited to 256 characters.
    S3Region (string) -- Region of customer S3 bucket.
    AdditionalArtifacts (list) -- A list of additional artifacts.
    (string) -- Enable support for Redshift and/or QuickSight.
    
    
    
    
    
    
    NextToken (string) -- A generic string.
    
    
    
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

def get_waiter():
    """
    
    """
    pass

def put_report_definition(ReportDefinition=None):
    """
    Create a new report definition
    See also: AWS API Documentation
    
    
    :example: response = client.put_report_definition(
        ReportDefinition={
            'ReportName': 'string',
            'TimeUnit': 'HOURLY'|'DAILY',
            'Format': 'textORcsv',
            'Compression': 'ZIP'|'GZIP',
            'AdditionalSchemaElements': [
                'RESOURCES',
            ],
            'S3Bucket': 'string',
            'S3Prefix': 'string',
            'S3Region': 'us-east-1'|'us-west-1'|'us-west-2'|'eu-central-1'|'eu-west-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1',
            'AdditionalArtifacts': [
                'REDSHIFT'|'QUICKSIGHT',
            ]
        }
    )
    
    
    :type ReportDefinition: dict
    :param ReportDefinition: [REQUIRED] The definition of AWS Cost and Usage Report. Customer can specify the report name, time unit, report format, compression format, S3 bucket and additional artifacts and schema elements in the definition.
            ReportName (string) -- [REQUIRED] Preferred name for a report, it has to be unique. Must starts with a number/letter, case sensitive. Limited to 256 characters.
            TimeUnit (string) -- [REQUIRED] The frequency on which report data are measured and displayed.
            Format (string) -- [REQUIRED] Preferred format for report.
            Compression (string) -- [REQUIRED] Preferred compression format for report.
            AdditionalSchemaElements (list) -- [REQUIRED] A list of schema elements.
            (string) -- Preference of including Resource IDs. You can include additional details about individual resource IDs in your report.
            S3Bucket (string) -- [REQUIRED] Name of customer S3 bucket.
            S3Prefix (string) -- [REQUIRED] Preferred report path prefix. Limited to 256 characters.
            S3Region (string) -- [REQUIRED] Region of customer S3 bucket.
            AdditionalArtifacts (list) -- A list of additional artifacts.
            (string) -- Enable support for Redshift and/or QuickSight.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) -- Response of PutReportDefinition
    
    """
    pass

