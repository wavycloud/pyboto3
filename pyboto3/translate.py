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

def delete_terminology(Name=None):
    """
    A synchronous action that deletes a custom terminology.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_terminology(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the custom terminology being deleted.\n

    """
    pass

def describe_text_translation_job(JobId=None):
    """
    Gets the properties associated with an asycnhronous batch translation job including name, ID, status, source and target languages, input/output S3 buckets, and so on.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_text_translation_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier that Amazon Translate generated for the job. The StartTextTranslationJob operation returns this identifier in its response.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TextTranslationJobProperties': {
        'JobId': 'string',
        'JobName': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERROR'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
        'JobDetails': {
            'TranslatedDocumentsCount': 123,
            'DocumentsWithErrorsCount': 123,
            'InputDocumentsCount': 123
        },
        'SourceLanguageCode': 'string',
        'TargetLanguageCodes': [
            'string',
        ],
        'TerminologyNames': [
            'string',
        ],
        'Message': 'string',
        'SubmittedTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'InputDataConfig': {
            'S3Uri': 'string',
            'ContentType': 'string'
        },
        'OutputDataConfig': {
            'S3Uri': 'string'
        },
        'DataAccessRoleArn': 'string'
    }
}


Response Structure

(dict) --
TextTranslationJobProperties (dict) --An object that contains the properties associated with an asynchronous batch translation job.

JobId (string) --The ID of the translation job.

JobName (string) --The user-defined name of the translation job.

JobStatus (string) --The status of the translation job.

JobDetails (dict) --The number of documents successfully and unsuccessfully processed during the translation job.

TranslatedDocumentsCount (integer) --The number of documents successfully processed during a translation job.

DocumentsWithErrorsCount (integer) --The number of documents that could not be processed during a translation job.

InputDocumentsCount (integer) --The number of documents used as input in a translation job.



SourceLanguageCode (string) --The language code of the language of the source text. The language must be a language supported by Amazon Translate.

TargetLanguageCodes (list) --The language code of the language of the target text. The language must be a language supported by Amazon Translate.

(string) --


TerminologyNames (list) --A list containing the names of the terminologies applied to a translation job. Only one terminology can be applied per  StartTextTranslationJob request at this time.

(string) --


Message (string) --An explanation of any errors that may have occured during the translation job.

SubmittedTime (datetime) --The time at which the translation job was submitted.

EndTime (datetime) --The time at which the translation job ended.

InputDataConfig (dict) --The input configuration properties that were specified when the job was requested.

S3Uri (string) --The URI of the AWS S3 folder that contains the input file. The folder must be in the same Region as the API endpoint you are calling.

ContentType (string) --The multipurpose internet mail extension (MIME) type of the input files. Valid values are text/plain for plaintext files and text/html for HTML files.



OutputDataConfig (dict) --The output configuration properties that were specified when the job was requested.

S3Uri (string) --The URI of the S3 folder that contains a translation job\'s output file. The folder must be in the same Region as the API endpoint that you are calling.



DataAccessRoleArn (string) --The Amazon Resource Name (ARN) of an AWS Identity Access and Management (IAM) role that granted Amazon Translate read access to the job\'s input data.








Exceptions

Translate.Client.exceptions.ResourceNotFoundException
Translate.Client.exceptions.TooManyRequestsException
Translate.Client.exceptions.InternalServerException


    :return: {
        'TextTranslationJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERROR'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'JobDetails': {
                'TranslatedDocumentsCount': 123,
                'DocumentsWithErrorsCount': 123,
                'InputDocumentsCount': 123
            },
            'SourceLanguageCode': 'string',
            'TargetLanguageCodes': [
                'string',
            ],
            'TerminologyNames': [
                'string',
            ],
            'Message': 'string',
            'SubmittedTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Uri': 'string',
                'ContentType': 'string'
            },
            'OutputDataConfig': {
                'S3Uri': 'string'
            },
            'DataAccessRoleArn': 'string'
        }
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

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_terminology(Name=None, TerminologyDataFormat=None):
    """
    Retrieves a custom terminology.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_terminology(
        Name='string',
        TerminologyDataFormat='CSV'|'TMX'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the custom terminology being retrieved.\n

    :type TerminologyDataFormat: string
    :param TerminologyDataFormat: [REQUIRED]\nThe data format of the custom terminology being retrieved, either CSV or TMX.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TerminologyProperties': {
        'Name': 'string',
        'Description': 'string',
        'Arn': 'string',
        'SourceLanguageCode': 'string',
        'TargetLanguageCodes': [
            'string',
        ],
        'EncryptionKey': {
            'Type': 'KMS',
            'Id': 'string'
        },
        'SizeBytes': 123,
        'TermCount': 123,
        'CreatedAt': datetime(2015, 1, 1),
        'LastUpdatedAt': datetime(2015, 1, 1)
    },
    'TerminologyDataLocation': {
        'RepositoryType': 'string',
        'Location': 'string'
    }
}


Response Structure

(dict) --

TerminologyProperties (dict) --
The properties of the custom terminology being retrieved.

Name (string) --
The name of the custom terminology.

Description (string) --
The description of the custom terminology properties.

Arn (string) --
The Amazon Resource Name (ARN) of the custom terminology.

SourceLanguageCode (string) --
The language code for the source text of the translation request for which the custom terminology is being used.

TargetLanguageCodes (list) --
The language codes for the target languages available with the custom terminology file. All possible target languages are returned in array.

(string) --


EncryptionKey (dict) --
The encryption key for the custom terminology.

Type (string) --
The type of encryption key used by Amazon Translate to encrypt custom terminologies.

Id (string) --
The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom terminology.



SizeBytes (integer) --
The size of the file used when importing a custom terminology.

TermCount (integer) --
The number of terms included in the custom terminology.

CreatedAt (datetime) --
The time at which the custom terminology was created, based on the timestamp.

LastUpdatedAt (datetime) --
The time at which the custom terminology was last update, based on the timestamp.



TerminologyDataLocation (dict) --
The data location of the custom terminology being retrieved. The custom terminology file is returned in a presigned url that has a 30 minute expiration.

RepositoryType (string) --
The repository type for the custom terminology data.

Location (string) --
The location of the custom terminology data.









Exceptions

Translate.Client.exceptions.ResourceNotFoundException
Translate.Client.exceptions.InvalidParameterValueException
Translate.Client.exceptions.TooManyRequestsException
Translate.Client.exceptions.InternalServerException


    :return: {
        'TerminologyProperties': {
            'Name': 'string',
            'Description': 'string',
            'Arn': 'string',
            'SourceLanguageCode': 'string',
            'TargetLanguageCodes': [
                'string',
            ],
            'EncryptionKey': {
                'Type': 'KMS',
                'Id': 'string'
            },
            'SizeBytes': 123,
            'TermCount': 123,
            'CreatedAt': datetime(2015, 1, 1),
            'LastUpdatedAt': datetime(2015, 1, 1)
        },
        'TerminologyDataLocation': {
            'RepositoryType': 'string',
            'Location': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
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

def import_terminology(Name=None, MergeStrategy=None, Description=None, TerminologyData=None, EncryptionKey=None):
    """
    Creates or updates a custom terminology, depending on whether or not one already exists for the given terminology name. Importing a terminology with the same name as an existing one will merge the terminologies based on the chosen merge strategy. Currently, the only supported merge strategy is OVERWRITE, and so the imported terminology will overwrite an existing terminology of the same name.
    If you import a terminology that overwrites an existing one, the new terminology take up to 10 minutes to fully propagate and be available for use in a translation due to cache policies with the DataPlane service that performs the translations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.import_terminology(
        Name='string',
        MergeStrategy='OVERWRITE',
        Description='string',
        TerminologyData={
            'File': b'bytes',
            'Format': 'CSV'|'TMX'
        },
        EncryptionKey={
            'Type': 'KMS',
            'Id': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the custom terminology being imported.\n

    :type MergeStrategy: string
    :param MergeStrategy: [REQUIRED]\nThe merge strategy of the custom terminology being imported. Currently, only the OVERWRITE merge strategy is supported. In this case, the imported terminology will overwrite an existing terminology of the same name.\n

    :type Description: string
    :param Description: The description of the custom terminology being imported.

    :type TerminologyData: dict
    :param TerminologyData: [REQUIRED]\nThe terminology data for the custom terminology being imported.\n\nFile (bytes) -- [REQUIRED]The file containing the custom terminology data. Your version of the AWS SDK performs a Base64-encoding on this field before sending a request to the AWS service. Users of the SDK should not perform Base64-encoding themselves.\n\nFormat (string) -- [REQUIRED]The data format of the custom terminology. Either CSV or TMX.\n\n\n

    :type EncryptionKey: dict
    :param EncryptionKey: The encryption key for the custom terminology being imported.\n\nType (string) -- [REQUIRED]The type of encryption key used by Amazon Translate to encrypt custom terminologies.\n\nId (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom terminology.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TerminologyProperties': {
        'Name': 'string',
        'Description': 'string',
        'Arn': 'string',
        'SourceLanguageCode': 'string',
        'TargetLanguageCodes': [
            'string',
        ],
        'EncryptionKey': {
            'Type': 'KMS',
            'Id': 'string'
        },
        'SizeBytes': 123,
        'TermCount': 123,
        'CreatedAt': datetime(2015, 1, 1),
        'LastUpdatedAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

TerminologyProperties (dict) --
The properties of the custom terminology being imported.

Name (string) --
The name of the custom terminology.

Description (string) --
The description of the custom terminology properties.

Arn (string) --
The Amazon Resource Name (ARN) of the custom terminology.

SourceLanguageCode (string) --
The language code for the source text of the translation request for which the custom terminology is being used.

TargetLanguageCodes (list) --
The language codes for the target languages available with the custom terminology file. All possible target languages are returned in array.

(string) --


EncryptionKey (dict) --
The encryption key for the custom terminology.

Type (string) --
The type of encryption key used by Amazon Translate to encrypt custom terminologies.

Id (string) --
The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom terminology.



SizeBytes (integer) --
The size of the file used when importing a custom terminology.

TermCount (integer) --
The number of terms included in the custom terminology.

CreatedAt (datetime) --
The time at which the custom terminology was created, based on the timestamp.

LastUpdatedAt (datetime) --
The time at which the custom terminology was last update, based on the timestamp.









Exceptions

Translate.Client.exceptions.InvalidParameterValueException
Translate.Client.exceptions.LimitExceededException
Translate.Client.exceptions.TooManyRequestsException
Translate.Client.exceptions.InternalServerException


    :return: {
        'TerminologyProperties': {
            'Name': 'string',
            'Description': 'string',
            'Arn': 'string',
            'SourceLanguageCode': 'string',
            'TargetLanguageCodes': [
                'string',
            ],
            'EncryptionKey': {
                'Type': 'KMS',
                'Id': 'string'
            },
            'SizeBytes': 123,
            'TermCount': 123,
            'CreatedAt': datetime(2015, 1, 1),
            'LastUpdatedAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_terminologies(NextToken=None, MaxResults=None):
    """
    Provides a list of custom terminologies associated with your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_terminologies(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of the request to ListTerminologies was truncated, include the NextToken to fetch the next group of custom terminologies.

    :type MaxResults: integer
    :param MaxResults: The maximum number of custom terminologies returned per list request.

    :rtype: dict

ReturnsResponse Syntax
{
    'TerminologyPropertiesList': [
        {
            'Name': 'string',
            'Description': 'string',
            'Arn': 'string',
            'SourceLanguageCode': 'string',
            'TargetLanguageCodes': [
                'string',
            ],
            'EncryptionKey': {
                'Type': 'KMS',
                'Id': 'string'
            },
            'SizeBytes': 123,
            'TermCount': 123,
            'CreatedAt': datetime(2015, 1, 1),
            'LastUpdatedAt': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TerminologyPropertiesList (list) --
The properties list of the custom terminologies returned on the list request.

(dict) --
The properties of the custom terminology.

Name (string) --
The name of the custom terminology.

Description (string) --
The description of the custom terminology properties.

Arn (string) --
The Amazon Resource Name (ARN) of the custom terminology.

SourceLanguageCode (string) --
The language code for the source text of the translation request for which the custom terminology is being used.

TargetLanguageCodes (list) --
The language codes for the target languages available with the custom terminology file. All possible target languages are returned in array.

(string) --


EncryptionKey (dict) --
The encryption key for the custom terminology.

Type (string) --
The type of encryption key used by Amazon Translate to encrypt custom terminologies.

Id (string) --
The Amazon Resource Name (ARN) of the encryption key being used to encrypt the custom terminology.



SizeBytes (integer) --
The size of the file used when importing a custom terminology.

TermCount (integer) --
The number of terms included in the custom terminology.

CreatedAt (datetime) --
The time at which the custom terminology was created, based on the timestamp.

LastUpdatedAt (datetime) --
The time at which the custom terminology was last update, based on the timestamp.





NextToken (string) --
If the response to the ListTerminologies was truncated, the NextToken fetches the next group of custom terminologies.







Exceptions

Translate.Client.exceptions.InvalidParameterValueException
Translate.Client.exceptions.TooManyRequestsException
Translate.Client.exceptions.InternalServerException


    :return: {
        'TerminologyPropertiesList': [
            {
                'Name': 'string',
                'Description': 'string',
                'Arn': 'string',
                'SourceLanguageCode': 'string',
                'TargetLanguageCodes': [
                    'string',
                ],
                'EncryptionKey': {
                    'Type': 'KMS',
                    'Id': 'string'
                },
                'SizeBytes': 123,
                'TermCount': 123,
                'CreatedAt': datetime(2015, 1, 1),
                'LastUpdatedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_text_translation_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of the batch translation jobs that you have submitted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_text_translation_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERROR'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmittedBeforeTime': datetime(2015, 1, 1),
            'SubmittedAfterTime': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: The parameters that specify which batch translation jobs to retrieve. Filters include job name, job status, and submission time. You can only set one filter at a time.\n\nJobName (string) --Filters the list of jobs by name.\n\nJobStatus (string) --Filters the list of jobs based by job status.\n\nSubmittedBeforeTime (datetime) --Filters the list of jobs based on the time that the job was submitted for processing and returns only the jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.\n\nSubmittedAfterTime (datetime) --Filters the list of jobs based on the time that the job was submitted for processing and returns only the jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.\n\n\n

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default value is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'TextTranslationJobPropertiesList': [
        {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERROR'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'JobDetails': {
                'TranslatedDocumentsCount': 123,
                'DocumentsWithErrorsCount': 123,
                'InputDocumentsCount': 123
            },
            'SourceLanguageCode': 'string',
            'TargetLanguageCodes': [
                'string',
            ],
            'TerminologyNames': [
                'string',
            ],
            'Message': 'string',
            'SubmittedTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Uri': 'string',
                'ContentType': 'string'
            },
            'OutputDataConfig': {
                'S3Uri': 'string'
            },
            'DataAccessRoleArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

TextTranslationJobPropertiesList (list) --
A list containing the properties of each job that is returned.

(dict) --
Provides information about a translation job.

JobId (string) --
The ID of the translation job.

JobName (string) --
The user-defined name of the translation job.

JobStatus (string) --
The status of the translation job.

JobDetails (dict) --
The number of documents successfully and unsuccessfully processed during the translation job.

TranslatedDocumentsCount (integer) --
The number of documents successfully processed during a translation job.

DocumentsWithErrorsCount (integer) --
The number of documents that could not be processed during a translation job.

InputDocumentsCount (integer) --
The number of documents used as input in a translation job.



SourceLanguageCode (string) --
The language code of the language of the source text. The language must be a language supported by Amazon Translate.

TargetLanguageCodes (list) --
The language code of the language of the target text. The language must be a language supported by Amazon Translate.

(string) --


TerminologyNames (list) --
A list containing the names of the terminologies applied to a translation job. Only one terminology can be applied per  StartTextTranslationJob request at this time.

(string) --


Message (string) --
An explanation of any errors that may have occured during the translation job.

SubmittedTime (datetime) --
The time at which the translation job was submitted.

EndTime (datetime) --
The time at which the translation job ended.

InputDataConfig (dict) --
The input configuration properties that were specified when the job was requested.

S3Uri (string) --
The URI of the AWS S3 folder that contains the input file. The folder must be in the same Region as the API endpoint you are calling.

ContentType (string) --
The multipurpose internet mail extension (MIME) type of the input files. Valid values are text/plain for plaintext files and text/html for HTML files.



OutputDataConfig (dict) --
The output configuration properties that were specified when the job was requested.

S3Uri (string) --
The URI of the S3 folder that contains a translation job\'s output file. The folder must be in the same Region as the API endpoint that you are calling.



DataAccessRoleArn (string) --
The Amazon Resource Name (ARN) of an AWS Identity Access and Management (IAM) role that granted Amazon Translate read access to the job\'s input data.





NextToken (string) --
The token to use to retreive the next page of results. This value is null when there are no more results to return.







Exceptions

Translate.Client.exceptions.InvalidRequestException
Translate.Client.exceptions.TooManyRequestsException
Translate.Client.exceptions.InvalidFilterException
Translate.Client.exceptions.InternalServerException


    :return: {
        'TextTranslationJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERROR'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'JobDetails': {
                    'TranslatedDocumentsCount': 123,
                    'DocumentsWithErrorsCount': 123,
                    'InputDocumentsCount': 123
                },
                'SourceLanguageCode': 'string',
                'TargetLanguageCodes': [
                    'string',
                ],
                'TerminologyNames': [
                    'string',
                ],
                'Message': 'string',
                'SubmittedTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Uri': 'string',
                    'ContentType': 'string'
                },
                'OutputDataConfig': {
                    'S3Uri': 'string'
                },
                'DataAccessRoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def start_text_translation_job(JobName=None, InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, SourceLanguageCode=None, TargetLanguageCodes=None, TerminologyNames=None, ClientToken=None):
    """
    Starts an asynchronous batch translation job. Batch translation jobs can be used to translate large volumes of text across multiple documents at once. For more information, see  async .
    Batch translation jobs can be described with the  DescribeTextTranslationJob operation, listed with the  ListTextTranslationJobs operation, and stopped with the  StopTextTranslationJob operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_text_translation_job(
        JobName='string',
        InputDataConfig={
            'S3Uri': 'string',
            'ContentType': 'string'
        },
        OutputDataConfig={
            'S3Uri': 'string'
        },
        DataAccessRoleArn='string',
        SourceLanguageCode='string',
        TargetLanguageCodes=[
            'string',
        ],
        TerminologyNames=[
            'string',
        ],
        ClientToken='string'
    )
    
    
    :type JobName: string
    :param JobName: The name of the batch translation job to be performed.

    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]\nSpecifies the format and S3 location of the input documents for the translation job.\n\nS3Uri (string) -- [REQUIRED]The URI of the AWS S3 folder that contains the input file. The folder must be in the same Region as the API endpoint you are calling.\n\nContentType (string) -- [REQUIRED]The multipurpose internet mail extension (MIME) type of the input files. Valid values are text/plain for plaintext files and text/html for HTML files.\n\n\n

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]\nSpecifies the S3 folder to which your job output will be saved.\n\nS3Uri (string) -- [REQUIRED]The URI of the S3 folder that contains a translation job\'s output file. The folder must be in the same Region as the API endpoint that you are calling.\n\n\n

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of an AWS Identity Access and Management (IAM) role that grants Amazon Translate read access to your input data. For more nformation, see identity-and-access-management .\n

    :type SourceLanguageCode: string
    :param SourceLanguageCode: [REQUIRED]\nThe language code of the input language. For a list of language codes, see what-is-languages .\nAmazon Translate does not automatically detect a source language during batch translation jobs.\n

    :type TargetLanguageCodes: list
    :param TargetLanguageCodes: [REQUIRED]\nThe language code of the output language.\n\n(string) --\n\n

    :type TerminologyNames: list
    :param TerminologyNames: The name of the terminology to use in the batch translation job. For a list of available terminologies, use the ListTerminologies operation.\n\n(string) --\n\n

    :type ClientToken: string
    :param ClientToken: [REQUIRED]\nThe client token of the EC2 instance calling the request. This token is auto-generated when using the Amazon Translate SDK. Otherwise, use the DescribeInstances EC2 operation to retreive an instance\'s client token. For more information, see Client Tokens in the EC2 User Guide.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string',
    'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERROR'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
}


Response Structure

(dict) --

JobId (string) --
The identifier generated for the job. To get the status of a job, use this ID with the  DescribeTextTranslationJob operation.

JobStatus (string) --
The status of the job. Possible values include:

SUBMITTED - The job has been received and is queued for processing.
IN_PROGRESS - Amazon Translate is processing the job.
COMPLETED - The job was successfully completed and the output is available.
COMPLETED_WITH_ERRORS - The job was completed with errors. The errors can be analyzed in the job\'s output.
FAILED - The job did not complete. To get details, use the  DescribeTextTranslationJob operation.
STOP_REQUESTED - The user who started the job has requested that it be stopped.
STOPPED - The job has been stopped.








Exceptions

Translate.Client.exceptions.TooManyRequestsException
Translate.Client.exceptions.UnsupportedLanguagePairException
Translate.Client.exceptions.InvalidRequestException
Translate.Client.exceptions.ResourceNotFoundException
Translate.Client.exceptions.InternalServerException


    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERROR'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    :returns: 
    SUBMITTED - The job has been received and is queued for processing.
    IN_PROGRESS - Amazon Translate is processing the job.
    COMPLETED - The job was successfully completed and the output is available.
    COMPLETED_WITH_ERRORS - The job was completed with errors. The errors can be analyzed in the job\'s output.
    FAILED - The job did not complete. To get details, use the  DescribeTextTranslationJob operation.
    STOP_REQUESTED - The user who started the job has requested that it be stopped.
    STOPPED - The job has been stopped.
    
    """
    pass

def stop_text_translation_job(JobId=None):
    """
    Stops an asynchronous batch translation job that is in progress.
    If the job\'s state is IN_PROGRESS , the job will be marked for termination and put into the STOP_REQUESTED state. If the job completes before it can be stopped, it is put into the COMPLETED state. Otherwise, the job is put into the STOPPED state.
    Asynchronous batch translation jobs are started with the  StartTextTranslationJob operation. You can use the  DescribeTextTranslationJob or  ListTextTranslationJobs operations to get a batch translation job\'s JobId .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_text_translation_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe job ID of the job to be stopped.\n

    :rtype: dict
ReturnsResponse Syntax{
    'JobId': 'string',
    'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERROR'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
}


Response Structure

(dict) --
JobId (string) --The job ID of the stopped batch translation job.

JobStatus (string) --The status of the designated job. Upon successful completion, the job\'s status will be STOPPED .






Exceptions

Translate.Client.exceptions.ResourceNotFoundException
Translate.Client.exceptions.TooManyRequestsException
Translate.Client.exceptions.InternalServerException


    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'COMPLETED_WITH_ERROR'|'FAILED'|'STOP_REQUESTED'|'STOPPED'
    }
    
    
    """
    pass

def translate_text(Text=None, TerminologyNames=None, SourceLanguageCode=None, TargetLanguageCode=None):
    """
    Translates input text from the source language to the target language. For a list of available languages and language codes, see  what-is-languages .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.translate_text(
        Text='string',
        TerminologyNames=[
            'string',
        ],
        SourceLanguageCode='string',
        TargetLanguageCode='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]\nThe text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters.\n

    :type TerminologyNames: list
    :param TerminologyNames: The name of the terminology list file to be used in the TranslateText request. You can use 1 terminology list at most in a TranslateText request. Terminology lists can contain a maximum of 256 terms.\n\n(string) --\n\n

    :type SourceLanguageCode: string
    :param SourceLanguageCode: [REQUIRED]\nThe language code for the language of the source text. The language must be a language supported by Amazon Translate. For a list of language codes, see what-is-languages .\nTo have Amazon Translate determine the source language of your text, you can specify auto in the SourceLanguageCode field. If you specify auto , Amazon Translate will call Amazon Comprehend to determine the source language.\n

    :type TargetLanguageCode: string
    :param TargetLanguageCode: [REQUIRED]\nThe language code requested for the language of the target text. The language must be a language supported by Amazon Translate.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TranslatedText': 'string',
    'SourceLanguageCode': 'string',
    'TargetLanguageCode': 'string',
    'AppliedTerminologies': [
        {
            'Name': 'string',
            'Terms': [
                {
                    'SourceText': 'string',
                    'TargetText': 'string'
                },
            ]
        },
    ]
}


Response Structure

(dict) --

TranslatedText (string) --
The translated text.

SourceLanguageCode (string) --
The language code for the language of the source text.

TargetLanguageCode (string) --
The language code for the language of the target text.

AppliedTerminologies (list) --
The names of the custom terminologies applied to the input text by Amazon Translate for the translated text response.

(dict) --
The custom terminology applied to the input text by Amazon Translate for the translated text response. This is optional in the response and will only be present if you specified terminology input in the request. Currently, only one terminology can be applied per TranslateText request.

Name (string) --
The name of the custom terminology applied to the input text by Amazon Translate for the translated text response.

Terms (list) --
The specific terms of the custom terminology applied to the input text by Amazon Translate for the translated text response. A maximum of 250 terms will be returned, and the specific terms applied will be the first 250 terms in the source text.

(dict) --
The term being translated by the custom terminology.

SourceText (string) --
The source text of the term being translated by the custom terminology.

TargetText (string) --
The target text of the term being translated by the custom terminology.















Exceptions

Translate.Client.exceptions.InvalidRequestException
Translate.Client.exceptions.TextSizeLimitExceededException
Translate.Client.exceptions.TooManyRequestsException
Translate.Client.exceptions.UnsupportedLanguagePairException
Translate.Client.exceptions.DetectedLanguageLowConfidenceException
Translate.Client.exceptions.ResourceNotFoundException
Translate.Client.exceptions.InternalServerException
Translate.Client.exceptions.ServiceUnavailableException


    :return: {
        'TranslatedText': 'string',
        'SourceLanguageCode': 'string',
        'TargetLanguageCode': 'string',
        'AppliedTerminologies': [
            {
                'Name': 'string',
                'Terms': [
                    {
                        'SourceText': 'string',
                        'TargetText': 'string'
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    Translate.Client.exceptions.InvalidRequestException
    Translate.Client.exceptions.TextSizeLimitExceededException
    Translate.Client.exceptions.TooManyRequestsException
    Translate.Client.exceptions.UnsupportedLanguagePairException
    Translate.Client.exceptions.DetectedLanguageLowConfidenceException
    Translate.Client.exceptions.ResourceNotFoundException
    Translate.Client.exceptions.InternalServerException
    Translate.Client.exceptions.ServiceUnavailableException
    
    """
    pass

