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

def describe_entities_detection_v2_job(JobId=None):
    """
    Gets the properties associated with a medical entities detection job. Use this operation to get the status of a detection job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_entities_detection_v2_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier that Amazon Comprehend Medical generated for the job. The StartEntitiesDetectionV2Job operation returns this identifier in its response.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ComprehendMedicalAsyncJobProperties': {
        'JobId': 'string',
        'JobName': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
        'Message': 'string',
        'SubmitTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'ExpirationTime': datetime(2015, 1, 1),
        'InputDataConfig': {
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        'OutputDataConfig': {
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        'LanguageCode': 'en',
        'DataAccessRoleArn': 'string',
        'ManifestFilePath': 'string',
        'KMSKey': 'string',
        'ModelVersion': 'string'
    }
}


Response Structure

(dict) --
ComprehendMedicalAsyncJobProperties (dict) --An object that contains the properties associated with a detection job.

JobId (string) --The identifier assigned to the detection job.

JobName (string) --The name that you assigned to the detection job.

JobStatus (string) --The current status of the detection job. If the status is FAILED , the Message field shows the reason for the failure.

Message (string) --A description of the status of a job.

SubmitTime (datetime) --The time that the detection job was submitted for processing.

EndTime (datetime) --The time that the detection job completed.

ExpirationTime (datetime) --The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the ListEntitiesDetectionV2Job or the ListPHIDetectionJobs operation.

InputDataConfig (dict) --The input data configuration that you supplied when you created the detection job.

S3Bucket (string) --The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.
Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.

S3Key (string) --The path to the input data files in the S3 bucket.



OutputDataConfig (dict) --The output data configuration that you supplied when you created the detection job.

S3Bucket (string) --When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.

S3Key (string) --The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.



LanguageCode (string) --The language code of the input documents.

DataAccessRoleArn (string) --The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.

ManifestFilePath (string) --The path to the file that describes the results of a batch job.

KMSKey (string) --The AWS Key Management Service key, if any, used to encrypt the output files.

ModelVersion (string) --The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.








Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'ComprehendMedicalAsyncJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'OutputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'LanguageCode': 'en',
            'DataAccessRoleArn': 'string',
            'ManifestFilePath': 'string',
            'KMSKey': 'string',
            'ModelVersion': 'string'
        }
    }
    
    
    """
    pass

def describe_icd10_cm_inference_job(JobId=None):
    """
    Gets the properties associated with an InferICD10CM job. Use this operation to get the status of an inference job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_icd10_cm_inference_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier that Amazon Comprehend Medical generated for the job. The StartICD10CMInferenceJob operation returns this identifier in its response.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ComprehendMedicalAsyncJobProperties': {
        'JobId': 'string',
        'JobName': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
        'Message': 'string',
        'SubmitTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'ExpirationTime': datetime(2015, 1, 1),
        'InputDataConfig': {
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        'OutputDataConfig': {
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        'LanguageCode': 'en',
        'DataAccessRoleArn': 'string',
        'ManifestFilePath': 'string',
        'KMSKey': 'string',
        'ModelVersion': 'string'
    }
}


Response Structure

(dict) --
ComprehendMedicalAsyncJobProperties (dict) --An object that contains the properties associated with a detection job.

JobId (string) --The identifier assigned to the detection job.

JobName (string) --The name that you assigned to the detection job.

JobStatus (string) --The current status of the detection job. If the status is FAILED , the Message field shows the reason for the failure.

Message (string) --A description of the status of a job.

SubmitTime (datetime) --The time that the detection job was submitted for processing.

EndTime (datetime) --The time that the detection job completed.

ExpirationTime (datetime) --The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the ListEntitiesDetectionV2Job or the ListPHIDetectionJobs operation.

InputDataConfig (dict) --The input data configuration that you supplied when you created the detection job.

S3Bucket (string) --The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.
Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.

S3Key (string) --The path to the input data files in the S3 bucket.



OutputDataConfig (dict) --The output data configuration that you supplied when you created the detection job.

S3Bucket (string) --When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.

S3Key (string) --The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.



LanguageCode (string) --The language code of the input documents.

DataAccessRoleArn (string) --The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.

ManifestFilePath (string) --The path to the file that describes the results of a batch job.

KMSKey (string) --The AWS Key Management Service key, if any, used to encrypt the output files.

ModelVersion (string) --The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.








Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'ComprehendMedicalAsyncJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'OutputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'LanguageCode': 'en',
            'DataAccessRoleArn': 'string',
            'ManifestFilePath': 'string',
            'KMSKey': 'string',
            'ModelVersion': 'string'
        }
    }
    
    
    """
    pass

def describe_phi_detection_job(JobId=None):
    """
    Gets the properties associated with a protected health information (PHI) detection job. Use this operation to get the status of a detection job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_phi_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier that Amazon Comprehend Medical generated for the job. The StartPHIDetectionJob operation returns this identifier in its response.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ComprehendMedicalAsyncJobProperties': {
        'JobId': 'string',
        'JobName': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
        'Message': 'string',
        'SubmitTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'ExpirationTime': datetime(2015, 1, 1),
        'InputDataConfig': {
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        'OutputDataConfig': {
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        'LanguageCode': 'en',
        'DataAccessRoleArn': 'string',
        'ManifestFilePath': 'string',
        'KMSKey': 'string',
        'ModelVersion': 'string'
    }
}


Response Structure

(dict) --
ComprehendMedicalAsyncJobProperties (dict) --An object that contains the properties associated with a detection job.

JobId (string) --The identifier assigned to the detection job.

JobName (string) --The name that you assigned to the detection job.

JobStatus (string) --The current status of the detection job. If the status is FAILED , the Message field shows the reason for the failure.

Message (string) --A description of the status of a job.

SubmitTime (datetime) --The time that the detection job was submitted for processing.

EndTime (datetime) --The time that the detection job completed.

ExpirationTime (datetime) --The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the ListEntitiesDetectionV2Job or the ListPHIDetectionJobs operation.

InputDataConfig (dict) --The input data configuration that you supplied when you created the detection job.

S3Bucket (string) --The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.
Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.

S3Key (string) --The path to the input data files in the S3 bucket.



OutputDataConfig (dict) --The output data configuration that you supplied when you created the detection job.

S3Bucket (string) --When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.

S3Key (string) --The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.



LanguageCode (string) --The language code of the input documents.

DataAccessRoleArn (string) --The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.

ManifestFilePath (string) --The path to the file that describes the results of a batch job.

KMSKey (string) --The AWS Key Management Service key, if any, used to encrypt the output files.

ModelVersion (string) --The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.








Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'ComprehendMedicalAsyncJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'OutputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'LanguageCode': 'en',
            'DataAccessRoleArn': 'string',
            'ManifestFilePath': 'string',
            'KMSKey': 'string',
            'ModelVersion': 'string'
        }
    }
    
    
    """
    pass

def describe_rx_norm_inference_job(JobId=None):
    """
    Gets the properties associated with an InferRxNorm job. Use this operation to get the status of an inference job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_rx_norm_inference_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier that Amazon Comprehend Medical generated for the job. The StartRxNormInferenceJob operation returns this identifier in its response.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ComprehendMedicalAsyncJobProperties': {
        'JobId': 'string',
        'JobName': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
        'Message': 'string',
        'SubmitTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'ExpirationTime': datetime(2015, 1, 1),
        'InputDataConfig': {
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        'OutputDataConfig': {
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        'LanguageCode': 'en',
        'DataAccessRoleArn': 'string',
        'ManifestFilePath': 'string',
        'KMSKey': 'string',
        'ModelVersion': 'string'
    }
}


Response Structure

(dict) --
ComprehendMedicalAsyncJobProperties (dict) --An object that contains the properties associated with a detection job.

JobId (string) --The identifier assigned to the detection job.

JobName (string) --The name that you assigned to the detection job.

JobStatus (string) --The current status of the detection job. If the status is FAILED , the Message field shows the reason for the failure.

Message (string) --A description of the status of a job.

SubmitTime (datetime) --The time that the detection job was submitted for processing.

EndTime (datetime) --The time that the detection job completed.

ExpirationTime (datetime) --The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the ListEntitiesDetectionV2Job or the ListPHIDetectionJobs operation.

InputDataConfig (dict) --The input data configuration that you supplied when you created the detection job.

S3Bucket (string) --The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.
Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.

S3Key (string) --The path to the input data files in the S3 bucket.



OutputDataConfig (dict) --The output data configuration that you supplied when you created the detection job.

S3Bucket (string) --When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.

S3Key (string) --The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.



LanguageCode (string) --The language code of the input documents.

DataAccessRoleArn (string) --The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.

ManifestFilePath (string) --The path to the file that describes the results of a batch job.

KMSKey (string) --The AWS Key Management Service key, if any, used to encrypt the output files.

ModelVersion (string) --The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.








Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'ComprehendMedicalAsyncJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'OutputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'LanguageCode': 'en',
            'DataAccessRoleArn': 'string',
            'ManifestFilePath': 'string',
            'KMSKey': 'string',
            'ModelVersion': 'string'
        }
    }
    
    
    """
    pass

def detect_entities(Text=None):
    """
    The DetectEntities operation is deprecated. You should use the  DetectEntitiesV2 operation instead.
    Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detect_entities(
        Text='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]\nA UTF-8 text string containing the clinical content being examined for entities. Each string must contain fewer than 20,000 bytes of characters.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Entities': [
        {
            'Id': 123,
            'BeginOffset': 123,
            'EndOffset': 123,
            'Score': ...,
            'Text': 'string',
            'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
            'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
            'Traits': [
                {
                    'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                    'Score': ...
                },
            ],
            'Attributes': [
                {
                    'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                    'Score': ...,
                    'RelationshipScore': ...,
                    'RelationshipType': 'EVERY'|'WITH_DOSAGE'|'ADMINISTERED_VIA'|'FOR'|'NEGATIVE'|'OVERLAP'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_VALUE'|'TEST_UNITS'|'DIRECTION',
                    'Id': 123,
                    'BeginOffset': 123,
                    'EndOffset': 123,
                    'Text': 'string',
                    'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                    'Traits': [
                        {
                            'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                            'Score': ...
                        },
                    ]
                },
            ]
        },
    ],
    'UnmappedAttributes': [
        {
            'Type': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
            'Attribute': {
                'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                'Score': ...,
                'RelationshipScore': ...,
                'RelationshipType': 'EVERY'|'WITH_DOSAGE'|'ADMINISTERED_VIA'|'FOR'|'NEGATIVE'|'OVERLAP'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_VALUE'|'TEST_UNITS'|'DIRECTION',
                'Id': 123,
                'BeginOffset': 123,
                'EndOffset': 123,
                'Text': 'string',
                'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                'Traits': [
                    {
                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                        'Score': ...
                    },
                ]
            }
        },
    ],
    'PaginationToken': 'string',
    'ModelVersion': 'string'
}


Response Structure

(dict) --
Entities (list) --The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned.

(dict) --Provides information about an extracted medical entity.

Id (integer) --The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of the detection.

Text (string) --The segment of input text extracted as this entity.

Category (string) --The category of the entity.

Type (string) --Describes the specific type of entity with category of entities.

Traits (list) --Contextual information for the entity.

(dict) --Provides contextual information about the extracted entity.

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.





Attributes (list) --The extracted attributes that relate to this entity.

(dict) --An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken. It contains information about the attribute such as id, begin and end offset within the input text, and the segment of the input text.

Type (string) --The type of attribute.

Score (float) --The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore (float) --The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.

RelationshipType (string) --The type of relationship between the entity and attribute. Type for the relationship is OVERLAP , indicating that the entity occurred at the same time as the Date_Expression .

Id (integer) --The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text (string) --The segment of input text extracted as this attribute.

Category (string) --The category of attribute.

Traits (list) --Contextual information for this attribute.

(dict) --Provides contextual information about the extracted entity.

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.













UnmappedAttributes (list) --Attributes extracted from the input text that we were unable to relate to an entity.

(dict) --An attribute that we extracted, but were unable to relate to an entity.

Type (string) --The type of the attribute, could be one of the following values: "MEDICATION", "MEDICAL_CONDITION", "ANATOMY", "TEST_AND_TREATMENT_PROCEDURE" or "PROTECTED_HEALTH_INFORMATION".

Attribute (dict) --The specific attribute that has been extracted but not mapped to an entity.

Type (string) --The type of attribute.

Score (float) --The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore (float) --The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.

RelationshipType (string) --The type of relationship between the entity and attribute. Type for the relationship is OVERLAP , indicating that the entity occurred at the same time as the Date_Expression .

Id (integer) --The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text (string) --The segment of input text extracted as this attribute.

Category (string) --The category of attribute.

Traits (list) --Contextual information for this attribute.

(dict) --Provides contextual information about the extracted entity.

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.











PaginationToken (string) --If the result of the previous request to DetectEntities was truncated, include the PaginationToken to fetch the next page of entities.

ModelVersion (string) --The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.






Exceptions

ComprehendMedical.Client.exceptions.InternalServerException
ComprehendMedical.Client.exceptions.ServiceUnavailableException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.InvalidEncodingException
ComprehendMedical.Client.exceptions.TextSizeLimitExceededException


    :return: {
        'Entities': [
            {
                'Id': 123,
                'BeginOffset': 123,
                'EndOffset': 123,
                'Score': ...,
                'Text': 'string',
                'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                'Traits': [
                    {
                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                        'Score': ...
                    },
                ],
                'Attributes': [
                    {
                        'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                        'Score': ...,
                        'RelationshipScore': ...,
                        'RelationshipType': 'EVERY'|'WITH_DOSAGE'|'ADMINISTERED_VIA'|'FOR'|'NEGATIVE'|'OVERLAP'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_VALUE'|'TEST_UNITS'|'DIRECTION',
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Text': 'string',
                        'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                        'Traits': [
                            {
                                'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                'Score': ...
                            },
                        ]
                    },
                ]
            },
        ],
        'UnmappedAttributes': [
            {
                'Type': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                'Attribute': {
                    'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                    'Score': ...,
                    'RelationshipScore': ...,
                    'RelationshipType': 'EVERY'|'WITH_DOSAGE'|'ADMINISTERED_VIA'|'FOR'|'NEGATIVE'|'OVERLAP'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_VALUE'|'TEST_UNITS'|'DIRECTION',
                    'Id': 123,
                    'BeginOffset': 123,
                    'EndOffset': 123,
                    'Text': 'string',
                    'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                    'Traits': [
                        {
                            'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                            'Score': ...
                        },
                    ]
                }
            },
        ],
        'PaginationToken': 'string',
        'ModelVersion': 'string'
    }
    
    
    """
    pass

def detect_entities_v2(Text=None):
    """
    Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information. Amazon Comprehend Medical only detects medical entities in English language texts.
    The DetectEntitiesV2 operation replaces the  DetectEntities operation. This new action uses a different model for determining the entities in your medical text and changes the way that some entities are returned in the output. You should use the DetectEntitiesV2 operation in all new applications.
    The DetectEntitiesV2 operation returns the Acuity and Direction entities as attributes instead of types.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detect_entities_v2(
        Text='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]\nA UTF-8 string containing the clinical content being examined for entities. Each string must contain fewer than 20,000 bytes of characters.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Entities': [
        {
            'Id': 123,
            'BeginOffset': 123,
            'EndOffset': 123,
            'Score': ...,
            'Text': 'string',
            'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
            'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
            'Traits': [
                {
                    'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                    'Score': ...
                },
            ],
            'Attributes': [
                {
                    'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                    'Score': ...,
                    'RelationshipScore': ...,
                    'RelationshipType': 'EVERY'|'WITH_DOSAGE'|'ADMINISTERED_VIA'|'FOR'|'NEGATIVE'|'OVERLAP'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_VALUE'|'TEST_UNITS'|'DIRECTION',
                    'Id': 123,
                    'BeginOffset': 123,
                    'EndOffset': 123,
                    'Text': 'string',
                    'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                    'Traits': [
                        {
                            'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                            'Score': ...
                        },
                    ]
                },
            ]
        },
    ],
    'UnmappedAttributes': [
        {
            'Type': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
            'Attribute': {
                'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                'Score': ...,
                'RelationshipScore': ...,
                'RelationshipType': 'EVERY'|'WITH_DOSAGE'|'ADMINISTERED_VIA'|'FOR'|'NEGATIVE'|'OVERLAP'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_VALUE'|'TEST_UNITS'|'DIRECTION',
                'Id': 123,
                'BeginOffset': 123,
                'EndOffset': 123,
                'Text': 'string',
                'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                'Traits': [
                    {
                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                        'Score': ...
                    },
                ]
            }
        },
    ],
    'PaginationToken': 'string',
    'ModelVersion': 'string'
}


Response Structure

(dict) --
Entities (list) --The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence in the detection and analysis. Attributes and traits of the entity are also returned.

(dict) --Provides information about an extracted medical entity.

Id (integer) --The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of the detection.

Text (string) --The segment of input text extracted as this entity.

Category (string) --The category of the entity.

Type (string) --Describes the specific type of entity with category of entities.

Traits (list) --Contextual information for the entity.

(dict) --Provides contextual information about the extracted entity.

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.





Attributes (list) --The extracted attributes that relate to this entity.

(dict) --An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken. It contains information about the attribute such as id, begin and end offset within the input text, and the segment of the input text.

Type (string) --The type of attribute.

Score (float) --The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore (float) --The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.

RelationshipType (string) --The type of relationship between the entity and attribute. Type for the relationship is OVERLAP , indicating that the entity occurred at the same time as the Date_Expression .

Id (integer) --The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text (string) --The segment of input text extracted as this attribute.

Category (string) --The category of attribute.

Traits (list) --Contextual information for this attribute.

(dict) --Provides contextual information about the extracted entity.

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.













UnmappedAttributes (list) --Attributes extracted from the input text that couldn\'t be related to an entity.

(dict) --An attribute that we extracted, but were unable to relate to an entity.

Type (string) --The type of the attribute, could be one of the following values: "MEDICATION", "MEDICAL_CONDITION", "ANATOMY", "TEST_AND_TREATMENT_PROCEDURE" or "PROTECTED_HEALTH_INFORMATION".

Attribute (dict) --The specific attribute that has been extracted but not mapped to an entity.

Type (string) --The type of attribute.

Score (float) --The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore (float) --The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.

RelationshipType (string) --The type of relationship between the entity and attribute. Type for the relationship is OVERLAP , indicating that the entity occurred at the same time as the Date_Expression .

Id (integer) --The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text (string) --The segment of input text extracted as this attribute.

Category (string) --The category of attribute.

Traits (list) --Contextual information for this attribute.

(dict) --Provides contextual information about the extracted entity.

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.











PaginationToken (string) --If the result to the DetectEntitiesV2 operation was truncated, include the PaginationToken to fetch the next page of entities.

ModelVersion (string) --The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.






Exceptions

ComprehendMedical.Client.exceptions.InternalServerException
ComprehendMedical.Client.exceptions.ServiceUnavailableException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.InvalidEncodingException
ComprehendMedical.Client.exceptions.TextSizeLimitExceededException


    :return: {
        'Entities': [
            {
                'Id': 123,
                'BeginOffset': 123,
                'EndOffset': 123,
                'Score': ...,
                'Text': 'string',
                'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                'Traits': [
                    {
                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                        'Score': ...
                    },
                ],
                'Attributes': [
                    {
                        'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                        'Score': ...,
                        'RelationshipScore': ...,
                        'RelationshipType': 'EVERY'|'WITH_DOSAGE'|'ADMINISTERED_VIA'|'FOR'|'NEGATIVE'|'OVERLAP'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_VALUE'|'TEST_UNITS'|'DIRECTION',
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Text': 'string',
                        'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                        'Traits': [
                            {
                                'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                'Score': ...
                            },
                        ]
                    },
                ]
            },
        ],
        'UnmappedAttributes': [
            {
                'Type': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                'Attribute': {
                    'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                    'Score': ...,
                    'RelationshipScore': ...,
                    'RelationshipType': 'EVERY'|'WITH_DOSAGE'|'ADMINISTERED_VIA'|'FOR'|'NEGATIVE'|'OVERLAP'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_VALUE'|'TEST_UNITS'|'DIRECTION',
                    'Id': 123,
                    'BeginOffset': 123,
                    'EndOffset': 123,
                    'Text': 'string',
                    'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                    'Traits': [
                        {
                            'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                            'Score': ...
                        },
                    ]
                }
            },
        ],
        'PaginationToken': 'string',
        'ModelVersion': 'string'
    }
    
    
    """
    pass

def detect_phi(Text=None):
    """
    Inspects the clinical text for protected health information (PHI) entities and returns the entity category, location, and confidence score for each entity. Amazon Comprehend Medical only detects entities in English language texts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detect_phi(
        Text='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]\nA UTF-8 text string containing the clinical content being examined for PHI entities. Each string must contain fewer than 20,000 bytes of characters.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Entities': [
        {
            'Id': 123,
            'BeginOffset': 123,
            'EndOffset': 123,
            'Score': ...,
            'Text': 'string',
            'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
            'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
            'Traits': [
                {
                    'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                    'Score': ...
                },
            ],
            'Attributes': [
                {
                    'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                    'Score': ...,
                    'RelationshipScore': ...,
                    'RelationshipType': 'EVERY'|'WITH_DOSAGE'|'ADMINISTERED_VIA'|'FOR'|'NEGATIVE'|'OVERLAP'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_VALUE'|'TEST_UNITS'|'DIRECTION',
                    'Id': 123,
                    'BeginOffset': 123,
                    'EndOffset': 123,
                    'Text': 'string',
                    'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                    'Traits': [
                        {
                            'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                            'Score': ...
                        },
                    ]
                },
            ]
        },
    ],
    'PaginationToken': 'string',
    'ModelVersion': 'string'
}


Response Structure

(dict) --
Entities (list) --The collection of PHI entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in its detection.

(dict) --Provides information about an extracted medical entity.

Id (integer) --The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of the detection.

Text (string) --The segment of input text extracted as this entity.

Category (string) --The category of the entity.

Type (string) --Describes the specific type of entity with category of entities.

Traits (list) --Contextual information for the entity.

(dict) --Provides contextual information about the extracted entity.

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.





Attributes (list) --The extracted attributes that relate to this entity.

(dict) --An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken. It contains information about the attribute such as id, begin and end offset within the input text, and the segment of the input text.

Type (string) --The type of attribute.

Score (float) --The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore (float) --The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.

RelationshipType (string) --The type of relationship between the entity and attribute. Type for the relationship is OVERLAP , indicating that the entity occurred at the same time as the Date_Expression .

Id (integer) --The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text (string) --The segment of input text extracted as this attribute.

Category (string) --The category of attribute.

Traits (list) --Contextual information for this attribute.

(dict) --Provides contextual information about the extracted entity.

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.













PaginationToken (string) --If the result of the previous request to DetectPHI was truncated, include the PaginationToken to fetch the next page of PHI entities.

ModelVersion (string) --The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.






Exceptions

ComprehendMedical.Client.exceptions.InternalServerException
ComprehendMedical.Client.exceptions.ServiceUnavailableException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.InvalidEncodingException
ComprehendMedical.Client.exceptions.TextSizeLimitExceededException


    :return: {
        'Entities': [
            {
                'Id': 123,
                'BeginOffset': 123,
                'EndOffset': 123,
                'Score': ...,
                'Text': 'string',
                'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                'Traits': [
                    {
                        'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                        'Score': ...
                    },
                ],
                'Attributes': [
                    {
                        'Type': 'NAME'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'GENERIC_NAME'|'BRAND_NAME'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_NAME'|'TEST_VALUE'|'TEST_UNITS'|'PROCEDURE_NAME'|'TREATMENT_NAME'|'DATE'|'AGE'|'CONTACT_POINT'|'EMAIL'|'IDENTIFIER'|'URL'|'ADDRESS'|'PROFESSION'|'SYSTEM_ORGAN_SITE'|'DIRECTION'|'QUALITY'|'QUANTITY'|'TIME_EXPRESSION'|'TIME_TO_MEDICATION_NAME'|'TIME_TO_DX_NAME'|'TIME_TO_TEST_NAME'|'TIME_TO_PROCEDURE_NAME'|'TIME_TO_TREATMENT_NAME',
                        'Score': ...,
                        'RelationshipScore': ...,
                        'RelationshipType': 'EVERY'|'WITH_DOSAGE'|'ADMINISTERED_VIA'|'FOR'|'NEGATIVE'|'OVERLAP'|'DOSAGE'|'ROUTE_OR_MODE'|'FORM'|'FREQUENCY'|'DURATION'|'STRENGTH'|'RATE'|'ACUITY'|'TEST_VALUE'|'TEST_UNITS'|'DIRECTION',
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Text': 'string',
                        'Category': 'MEDICATION'|'MEDICAL_CONDITION'|'PROTECTED_HEALTH_INFORMATION'|'TEST_TREATMENT_PROCEDURE'|'ANATOMY'|'TIME_EXPRESSION',
                        'Traits': [
                            {
                                'Name': 'SIGN'|'SYMPTOM'|'DIAGNOSIS'|'NEGATION',
                                'Score': ...
                            },
                        ]
                    },
                ]
            },
        ],
        'PaginationToken': 'string',
        'ModelVersion': 'string'
    }
    
    
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

def infer_icd10_cm(Text=None):
    """
    InferICD10CM detects medical conditions as entities listed in a patient record and links those entities to normalized concept identifiers in the ICD-10-CM knowledge base from the Centers for Disease Control. Amazon Comprehend Medical only detects medical entities in English language texts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.infer_icd10_cm(
        Text='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]\nThe input text used for analysis. The input for InferICD10CM is a string from 1 to 10000 characters.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Entities': [
        {
            'Id': 123,
            'Text': 'string',
            'Category': 'MEDICAL_CONDITION',
            'Type': 'DX_NAME',
            'Score': ...,
            'BeginOffset': 123,
            'EndOffset': 123,
            'Attributes': [
                {
                    'Type': 'ACUITY'|'DIRECTION'|'SYSTEM_ORGAN_SITE'|'QUALITY'|'QUANTITY',
                    'Score': ...,
                    'RelationshipScore': ...,
                    'Id': 123,
                    'BeginOffset': 123,
                    'EndOffset': 123,
                    'Text': 'string',
                    'Traits': [
                        {
                            'Name': 'NEGATION'|'DIAGNOSIS'|'SIGN'|'SYMPTOM',
                            'Score': ...
                        },
                    ]
                },
            ],
            'Traits': [
                {
                    'Name': 'NEGATION'|'DIAGNOSIS'|'SIGN'|'SYMPTOM',
                    'Score': ...
                },
            ],
            'ICD10CMConcepts': [
                {
                    'Description': 'string',
                    'Code': 'string',
                    'Score': ...
                },
            ]
        },
    ],
    'PaginationToken': 'string',
    'ModelVersion': 'string'
}


Response Structure

(dict) --
Entities (list) --The medical conditions detected in the text linked to ICD-10-CM concepts. If the action is successful, the service sends back an HTTP 200 response, as well as the entities detected.

(dict) --The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned.

Id (integer) --The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.

Text (string) --The segment of input text that is matched to the detected entity.

Category (string) --The category of the entity. InferICD10CM detects entities in the MEDICAL_CONDITION category.

Type (string) --Describes the specific type of entity with category of entities. InferICD10CM detects entities of the type DX_NAME .

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of the detection.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.

Attributes (list) --The detected attributes that relate to the entity. An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the nature of a medical condition.

(dict) --The detected attributes that relate to an entity. This includes an extracted segment of the text that is an attribute of an entity, or otherwise related to an entity. InferICD10CM detects the following attributes: Direction , System, Organ or Site , and Acuity .

Type (string) --The type of attribute. InferICD10CM detects entities of the type DX_NAME .

Score (float) --The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore (float) --The level of confidence that Amazon Comprehend Medical has that this attribute is correctly related to this entity.

Id (integer) --The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text (string) --The segment of input text which contains the detected attribute.

Traits (list) --The contextual information for the attribute. The traits recognized by InferICD10CM are DIAGNOSIS , SIGN , SYMPTOM , and NEGATION .

(dict) --Contextual information for the entity. The traits recognized by InferICD10CM are DIAGNOSIS , SIGN , SYMPTOM , and NEGATION .

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as a trait.









Traits (list) --Provides Contextual information for the entity. The traits recognized by InferICD10CM are DIAGNOSIS , SIGN , SYMPTOM , and NEGATION.

(dict) --Contextual information for the entity. The traits recognized by InferICD10CM are DIAGNOSIS , SIGN , SYMPTOM , and NEGATION .

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as a trait.





ICD10CMConcepts (list) --The ICD-10-CM concepts that the entity could refer to, along with a score indicating the likelihood of the match.

(dict) --The ICD-10-CM concepts that the entity could refer to, along with a score indicating the likelihood of the match.

Description (string) --The long description of the ICD-10-CM code in the ontology.

Code (string) --The ICD-10-CM code that identifies the concept found in the knowledge base from the Centers for Disease Control.

Score (float) --The level of confidence that Amazon Comprehend Medical has that the entity is accurately linked to an ICD-10-CM concept.









PaginationToken (string) --If the result of the previous request to InferICD10CM was truncated, include the PaginationToken to fetch the next page of medical condition entities.

ModelVersion (string) --The version of the model used to analyze the documents, in the format n .*n* .*n* You can use this information to track the model used for a particular batch of documents.






Exceptions

ComprehendMedical.Client.exceptions.InternalServerException
ComprehendMedical.Client.exceptions.ServiceUnavailableException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.InvalidEncodingException
ComprehendMedical.Client.exceptions.TextSizeLimitExceededException


    :return: {
        'Entities': [
            {
                'Id': 123,
                'Text': 'string',
                'Category': 'MEDICAL_CONDITION',
                'Type': 'DX_NAME',
                'Score': ...,
                'BeginOffset': 123,
                'EndOffset': 123,
                'Attributes': [
                    {
                        'Type': 'ACUITY'|'DIRECTION'|'SYSTEM_ORGAN_SITE'|'QUALITY'|'QUANTITY',
                        'Score': ...,
                        'RelationshipScore': ...,
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Text': 'string',
                        'Traits': [
                            {
                                'Name': 'NEGATION'|'DIAGNOSIS'|'SIGN'|'SYMPTOM',
                                'Score': ...
                            },
                        ]
                    },
                ],
                'Traits': [
                    {
                        'Name': 'NEGATION'|'DIAGNOSIS'|'SIGN'|'SYMPTOM',
                        'Score': ...
                    },
                ],
                'ICD10CMConcepts': [
                    {
                        'Description': 'string',
                        'Code': 'string',
                        'Score': ...
                    },
                ]
            },
        ],
        'PaginationToken': 'string',
        'ModelVersion': 'string'
    }
    
    
    """
    pass

def infer_rx_norm(Text=None):
    """
    InferRxNorm detects medications as entities listed in a patient record and links to the normalized concept identifiers in the RxNorm database from the National Library of Medicine. Amazon Comprehend Medical only detects medical entities in English language texts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.infer_rx_norm(
        Text='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]\nThe input text used for analysis. The input for InferRxNorm is a string from 1 to 10000 characters.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Entities': [
        {
            'Id': 123,
            'Text': 'string',
            'Category': 'MEDICATION',
            'Type': 'BRAND_NAME'|'GENERIC_NAME',
            'Score': ...,
            'BeginOffset': 123,
            'EndOffset': 123,
            'Attributes': [
                {
                    'Type': 'DOSAGE'|'DURATION'|'FORM'|'FREQUENCY'|'RATE'|'ROUTE_OR_MODE'|'STRENGTH',
                    'Score': ...,
                    'RelationshipScore': ...,
                    'Id': 123,
                    'BeginOffset': 123,
                    'EndOffset': 123,
                    'Text': 'string',
                    'Traits': [
                        {
                            'Name': 'NEGATION',
                            'Score': ...
                        },
                    ]
                },
            ],
            'Traits': [
                {
                    'Name': 'NEGATION',
                    'Score': ...
                },
            ],
            'RxNormConcepts': [
                {
                    'Description': 'string',
                    'Code': 'string',
                    'Score': ...
                },
            ]
        },
    ],
    'PaginationToken': 'string',
    'ModelVersion': 'string'
}


Response Structure

(dict) --
Entities (list) --The medication entities detected in the text linked to RxNorm concepts. If the action is successful, the service sends back an HTTP 200 response, as well as the entities detected.

(dict) --The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned.

Id (integer) --The numeric identifier for the entity. This is a monotonically increasing id unique within this response rather than a global unique identifier.

Text (string) --The segment of input text extracted from which the entity was detected.

Category (string) --The category of the entity. The recognized categories are GENERIC or BRAND_NAME .

Type (string) --Describes the specific type of entity. For InferRxNorm, the recognized entity type is MEDICATION .

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected entity.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the entity begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the entity ends. The offset returns the UTF-8 code point in the string.

Attributes (list) --The extracted attributes that relate to the entity. The attributes recognized by InferRxNorm are DOSAGE , DURATION , FORM , FREQUENCY , RATE , ROUTE_OR_MODE , and STRENGTH .

(dict) --The extracted attributes that relate to this entity. The attributes recognized by InferRxNorm are DOSAGE , DURATION , FORM , FREQUENCY , RATE , ROUTE_OR_MODE .

Type (string) --The type of attribute. The types of attributes recognized by InferRxNorm are BRAND_NAME and GENERIC_NAME .

Score (float) --The level of confidence that Comprehend Medical has that the segment of text is correctly recognized as an attribute.

RelationshipScore (float) --The level of confidence that Amazon Comprehend Medical has that the attribute is accurately linked to an entity.

Id (integer) --The numeric identifier for this attribute. This is a monotonically increasing id unique within this response rather than a global unique identifier.

BeginOffset (integer) --The 0-based character offset in the input text that shows where the attribute begins. The offset returns the UTF-8 code point in the string.

EndOffset (integer) --The 0-based character offset in the input text that shows where the attribute ends. The offset returns the UTF-8 code point in the string.

Text (string) --The segment of input text which corresponds to the detected attribute.

Traits (list) --Contextual information for the attribute. InferRxNorm recognizes the trait NEGATION for attributes, i.e. that the patient is not taking a specific dose or form of a medication.

(dict) --The contextual information for the entity. InferRxNorm recognizes the trait NEGATION , which is any indication that the patient is not taking a medication.

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected trait.









Traits (list) --Contextual information for the entity.

(dict) --The contextual information for the entity. InferRxNorm recognizes the trait NEGATION , which is any indication that the patient is not taking a medication.

Name (string) --Provides a name or contextual description about the trait.

Score (float) --The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected trait.





RxNormConcepts (list) --The RxNorm concepts that the entity could refer to, along with a score indicating the likelihood of the match.

(dict) --The RxNorm concept that the entity could refer to, along with a score indicating the likelihood of the match.

Description (string) --The description of the RxNorm concept.

Code (string) --RxNorm concept ID, also known as the RxCUI.

Score (float) --The level of confidence that Amazon Comprehend Medical has that the entity is accurately linked to the reported RxNorm concept.









PaginationToken (string) --If the result of the previous request to InferRxNorm was truncated, include the PaginationToken to fetch the next page of medication entities.

ModelVersion (string) --The version of the model used to analyze the documents, in the format n .*n* .*n* You can use this information to track the model used for a particular batch of documents.






Exceptions

ComprehendMedical.Client.exceptions.InternalServerException
ComprehendMedical.Client.exceptions.ServiceUnavailableException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.InvalidEncodingException
ComprehendMedical.Client.exceptions.TextSizeLimitExceededException


    :return: {
        'Entities': [
            {
                'Id': 123,
                'Text': 'string',
                'Category': 'MEDICATION',
                'Type': 'BRAND_NAME'|'GENERIC_NAME',
                'Score': ...,
                'BeginOffset': 123,
                'EndOffset': 123,
                'Attributes': [
                    {
                        'Type': 'DOSAGE'|'DURATION'|'FORM'|'FREQUENCY'|'RATE'|'ROUTE_OR_MODE'|'STRENGTH',
                        'Score': ...,
                        'RelationshipScore': ...,
                        'Id': 123,
                        'BeginOffset': 123,
                        'EndOffset': 123,
                        'Text': 'string',
                        'Traits': [
                            {
                                'Name': 'NEGATION',
                                'Score': ...
                            },
                        ]
                    },
                ],
                'Traits': [
                    {
                        'Name': 'NEGATION',
                        'Score': ...
                    },
                ],
                'RxNormConcepts': [
                    {
                        'Description': 'string',
                        'Code': 'string',
                        'Score': ...
                    },
                ]
            },
        ],
        'PaginationToken': 'string',
        'ModelVersion': 'string'
    }
    
    
    """
    pass

def list_entities_detection_v2_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of medical entity detection jobs that you have submitted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_entities_detection_v2_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.\n\nJobName (string) --Filters on the name of the job.\n\nJobStatus (string) --Filters the list of jobs based on job status. Returns only jobs with the specified status.\n\nSubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.\n\nSubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.\n\n\n

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'ComprehendMedicalAsyncJobPropertiesList': [
        {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'OutputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'LanguageCode': 'en',
            'DataAccessRoleArn': 'string',
            'ManifestFilePath': 'string',
            'KMSKey': 'string',
            'ModelVersion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ComprehendMedicalAsyncJobPropertiesList (list) --
A list containing the properties of each job returned.

(dict) --
Provides information about a detection job.

JobId (string) --
The identifier assigned to the detection job.

JobName (string) --
The name that you assigned to the detection job.

JobStatus (string) --
The current status of the detection job. If the status is FAILED , the Message field shows the reason for the failure.

Message (string) --
A description of the status of a job.

SubmitTime (datetime) --
The time that the detection job was submitted for processing.

EndTime (datetime) --
The time that the detection job completed.

ExpirationTime (datetime) --
The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the ListEntitiesDetectionV2Job or the ListPHIDetectionJobs operation.

InputDataConfig (dict) --
The input data configuration that you supplied when you created the detection job.

S3Bucket (string) --
The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.
Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.

S3Key (string) --
The path to the input data files in the S3 bucket.



OutputDataConfig (dict) --
The output data configuration that you supplied when you created the detection job.

S3Bucket (string) --
When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.

S3Key (string) --
The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.



LanguageCode (string) --
The language code of the input documents.

DataAccessRoleArn (string) --
The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.

ManifestFilePath (string) --
The path to the file that describes the results of a batch job.

KMSKey (string) --
The AWS Key Management Service key, if any, used to encrypt the output files.

ModelVersion (string) --
The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.





NextToken (string) --
Identifies the next page of results to return.







Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.ValidationException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'ComprehendMedicalAsyncJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'ExpirationTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'OutputDataConfig': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'LanguageCode': 'en',
                'DataAccessRoleArn': 'string',
                'ManifestFilePath': 'string',
                'KMSKey': 'string',
                'ModelVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ComprehendMedical.Client.exceptions.InvalidRequestException
    ComprehendMedical.Client.exceptions.ValidationException
    ComprehendMedical.Client.exceptions.TooManyRequestsException
    ComprehendMedical.Client.exceptions.InternalServerException
    
    """
    pass

def list_icd10_cm_inference_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of InferICD10CM jobs that you have submitted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_icd10_cm_inference_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.\n\nJobName (string) --Filters on the name of the job.\n\nJobStatus (string) --Filters the list of jobs based on job status. Returns only jobs with the specified status.\n\nSubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.\n\nSubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.\n\n\n

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'ComprehendMedicalAsyncJobPropertiesList': [
        {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'OutputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'LanguageCode': 'en',
            'DataAccessRoleArn': 'string',
            'ManifestFilePath': 'string',
            'KMSKey': 'string',
            'ModelVersion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ComprehendMedicalAsyncJobPropertiesList (list) --
A list containing the properties of each job that is returned.

(dict) --
Provides information about a detection job.

JobId (string) --
The identifier assigned to the detection job.

JobName (string) --
The name that you assigned to the detection job.

JobStatus (string) --
The current status of the detection job. If the status is FAILED , the Message field shows the reason for the failure.

Message (string) --
A description of the status of a job.

SubmitTime (datetime) --
The time that the detection job was submitted for processing.

EndTime (datetime) --
The time that the detection job completed.

ExpirationTime (datetime) --
The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the ListEntitiesDetectionV2Job or the ListPHIDetectionJobs operation.

InputDataConfig (dict) --
The input data configuration that you supplied when you created the detection job.

S3Bucket (string) --
The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.
Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.

S3Key (string) --
The path to the input data files in the S3 bucket.



OutputDataConfig (dict) --
The output data configuration that you supplied when you created the detection job.

S3Bucket (string) --
When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.

S3Key (string) --
The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.



LanguageCode (string) --
The language code of the input documents.

DataAccessRoleArn (string) --
The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.

ManifestFilePath (string) --
The path to the file that describes the results of a batch job.

KMSKey (string) --
The AWS Key Management Service key, if any, used to encrypt the output files.

ModelVersion (string) --
The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.





NextToken (string) --
Identifies the next page of results to return.







Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.ValidationException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'ComprehendMedicalAsyncJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'ExpirationTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'OutputDataConfig': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'LanguageCode': 'en',
                'DataAccessRoleArn': 'string',
                'ManifestFilePath': 'string',
                'KMSKey': 'string',
                'ModelVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ComprehendMedical.Client.exceptions.InvalidRequestException
    ComprehendMedical.Client.exceptions.ValidationException
    ComprehendMedical.Client.exceptions.TooManyRequestsException
    ComprehendMedical.Client.exceptions.InternalServerException
    
    """
    pass

def list_phi_detection_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of protected health information (PHI) detection jobs that you have submitted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_phi_detection_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.\n\nJobName (string) --Filters on the name of the job.\n\nJobStatus (string) --Filters the list of jobs based on job status. Returns only jobs with the specified status.\n\nSubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.\n\nSubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.\n\n\n

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page. The default is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'ComprehendMedicalAsyncJobPropertiesList': [
        {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'OutputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'LanguageCode': 'en',
            'DataAccessRoleArn': 'string',
            'ManifestFilePath': 'string',
            'KMSKey': 'string',
            'ModelVersion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ComprehendMedicalAsyncJobPropertiesList (list) --
A list containing the properties of each job returned.

(dict) --
Provides information about a detection job.

JobId (string) --
The identifier assigned to the detection job.

JobName (string) --
The name that you assigned to the detection job.

JobStatus (string) --
The current status of the detection job. If the status is FAILED , the Message field shows the reason for the failure.

Message (string) --
A description of the status of a job.

SubmitTime (datetime) --
The time that the detection job was submitted for processing.

EndTime (datetime) --
The time that the detection job completed.

ExpirationTime (datetime) --
The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the ListEntitiesDetectionV2Job or the ListPHIDetectionJobs operation.

InputDataConfig (dict) --
The input data configuration that you supplied when you created the detection job.

S3Bucket (string) --
The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.
Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.

S3Key (string) --
The path to the input data files in the S3 bucket.



OutputDataConfig (dict) --
The output data configuration that you supplied when you created the detection job.

S3Bucket (string) --
When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.

S3Key (string) --
The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.



LanguageCode (string) --
The language code of the input documents.

DataAccessRoleArn (string) --
The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.

ManifestFilePath (string) --
The path to the file that describes the results of a batch job.

KMSKey (string) --
The AWS Key Management Service key, if any, used to encrypt the output files.

ModelVersion (string) --
The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.





NextToken (string) --
Identifies the next page of results to return.







Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.ValidationException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'ComprehendMedicalAsyncJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'ExpirationTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'OutputDataConfig': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'LanguageCode': 'en',
                'DataAccessRoleArn': 'string',
                'ManifestFilePath': 'string',
                'KMSKey': 'string',
                'ModelVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ComprehendMedical.Client.exceptions.InvalidRequestException
    ComprehendMedical.Client.exceptions.ValidationException
    ComprehendMedical.Client.exceptions.TooManyRequestsException
    ComprehendMedical.Client.exceptions.InternalServerException
    
    """
    pass

def list_rx_norm_inference_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of InferRxNorm jobs that you have submitted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_rx_norm_inference_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.\n\nJobName (string) --Filters on the name of the job.\n\nJobStatus (string) --Filters the list of jobs based on job status. Returns only jobs with the specified status.\n\nSubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.\n\nSubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.\n\n\n

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: Identifies the next page of results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'ComprehendMedicalAsyncJobPropertiesList': [
        {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'OutputDataConfig': {
                'S3Bucket': 'string',
                'S3Key': 'string'
            },
            'LanguageCode': 'en',
            'DataAccessRoleArn': 'string',
            'ManifestFilePath': 'string',
            'KMSKey': 'string',
            'ModelVersion': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ComprehendMedicalAsyncJobPropertiesList (list) --
The maximum number of results to return in each page. The default is 100.

(dict) --
Provides information about a detection job.

JobId (string) --
The identifier assigned to the detection job.

JobName (string) --
The name that you assigned to the detection job.

JobStatus (string) --
The current status of the detection job. If the status is FAILED , the Message field shows the reason for the failure.

Message (string) --
A description of the status of a job.

SubmitTime (datetime) --
The time that the detection job was submitted for processing.

EndTime (datetime) --
The time that the detection job completed.

ExpirationTime (datetime) --
The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the ListEntitiesDetectionV2Job or the ListPHIDetectionJobs operation.

InputDataConfig (dict) --
The input data configuration that you supplied when you created the detection job.

S3Bucket (string) --
The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.
Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.

S3Key (string) --
The path to the input data files in the S3 bucket.



OutputDataConfig (dict) --
The output data configuration that you supplied when you created the detection job.

S3Bucket (string) --
When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.

S3Key (string) --
The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.



LanguageCode (string) --
The language code of the input documents.

DataAccessRoleArn (string) --
The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.

ManifestFilePath (string) --
The path to the file that describes the results of a batch job.

KMSKey (string) --
The AWS Key Management Service key, if any, used to encrypt the output files.

ModelVersion (string) --
The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.





NextToken (string) --
Identifies the next page of results to return.







Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.ValidationException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'ComprehendMedicalAsyncJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'PARTIAL_SUCCESS'|'FAILED'|'STOP_REQUESTED'|'STOPPED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'ExpirationTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'OutputDataConfig': {
                    'S3Bucket': 'string',
                    'S3Key': 'string'
                },
                'LanguageCode': 'en',
                'DataAccessRoleArn': 'string',
                'ManifestFilePath': 'string',
                'KMSKey': 'string',
                'ModelVersion': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ComprehendMedical.Client.exceptions.InvalidRequestException
    ComprehendMedical.Client.exceptions.ValidationException
    ComprehendMedical.Client.exceptions.TooManyRequestsException
    ComprehendMedical.Client.exceptions.InternalServerException
    
    """
    pass

def start_entities_detection_v2_job(InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, JobName=None, ClientRequestToken=None, KMSKey=None, LanguageCode=None):
    """
    Starts an asynchronous medical entity detection job for a collection of documents. Use the DescribeEntitiesDetectionV2Job operation to track the status of a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_entities_detection_v2_job(
        InputDataConfig={
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        OutputDataConfig={
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        DataAccessRoleArn='string',
        JobName='string',
        ClientRequestToken='string',
        KMSKey='string',
        LanguageCode='en'
    )
    
    
    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]\nSpecifies the format and location of the input data for the job.\n\nS3Bucket (string) -- [REQUIRED]The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.\nEach file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.\n\nS3Key (string) --The path to the input data files in the S3 bucket.\n\n\n

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]\nSpecifies where to send the output files.\n\nS3Bucket (string) -- [REQUIRED]When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.\n\nS3Key (string) --The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.\n\n\n

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. For more information, see Role-Based Permissions Required for Asynchronous Operations .\n

    :type JobName: string
    :param JobName: The identifier of the job.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you don\'t set the client request token, Amazon Comprehend Medical generates one.\nThis field is autopopulated if not provided.\n

    :type KMSKey: string
    :param KMSKey: An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language of the input documents. All documents must be in the same language.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier generated for the job. To get the status of a job, use this identifier with the DescribeEntitiesDetectionV2Job operation.







Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    ComprehendMedical.Client.exceptions.InvalidRequestException
    ComprehendMedical.Client.exceptions.TooManyRequestsException
    ComprehendMedical.Client.exceptions.ResourceNotFoundException
    ComprehendMedical.Client.exceptions.InternalServerException
    
    """
    pass

def start_icd10_cm_inference_job(InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, JobName=None, ClientRequestToken=None, KMSKey=None, LanguageCode=None):
    """
    Starts an asynchronous job to detect medical conditions and link them to the ICD-10-CM ontology. Use the DescribeICD10CMInferenceJob operation to track the status of a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_icd10_cm_inference_job(
        InputDataConfig={
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        OutputDataConfig={
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        DataAccessRoleArn='string',
        JobName='string',
        ClientRequestToken='string',
        KMSKey='string',
        LanguageCode='en'
    )
    
    
    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]\nSpecifies the format and location of the input data for the job.\n\nS3Bucket (string) -- [REQUIRED]The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.\nEach file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.\n\nS3Key (string) --The path to the input data files in the S3 bucket.\n\n\n

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]\nSpecifies where to send the output files.\n\nS3Bucket (string) -- [REQUIRED]When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.\n\nS3Key (string) --The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.\n\n\n

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. For more information, see Role-Based Permissions Required for Asynchronous Operations .\n

    :type JobName: string
    :param JobName: The identifier of the job.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you don\'t set the client request token, Amazon Comprehend Medical generates one.\nThis field is autopopulated if not provided.\n

    :type KMSKey: string
    :param KMSKey: An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language of the input documents. All documents must be in the same language.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier generated for the job. To get the status of a job, use this identifier with the StartICD10CMInferenceJob operation.







Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    ComprehendMedical.Client.exceptions.InvalidRequestException
    ComprehendMedical.Client.exceptions.TooManyRequestsException
    ComprehendMedical.Client.exceptions.ResourceNotFoundException
    ComprehendMedical.Client.exceptions.InternalServerException
    
    """
    pass

def start_phi_detection_job(InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, JobName=None, ClientRequestToken=None, KMSKey=None, LanguageCode=None):
    """
    Starts an asynchronous job to detect protected health information (PHI). Use the DescribePHIDetectionJob operation to track the status of a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_phi_detection_job(
        InputDataConfig={
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        OutputDataConfig={
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        DataAccessRoleArn='string',
        JobName='string',
        ClientRequestToken='string',
        KMSKey='string',
        LanguageCode='en'
    )
    
    
    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]\nSpecifies the format and location of the input data for the job.\n\nS3Bucket (string) -- [REQUIRED]The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.\nEach file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.\n\nS3Key (string) --The path to the input data files in the S3 bucket.\n\n\n

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]\nSpecifies where to send the output files.\n\nS3Bucket (string) -- [REQUIRED]When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.\n\nS3Key (string) --The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.\n\n\n

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. For more information, see Role-Based Permissions Required for Asynchronous Operations .\n

    :type JobName: string
    :param JobName: The identifier of the job.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you don\'t set the client request token, Amazon Comprehend Medical generates one.\nThis field is autopopulated if not provided.\n

    :type KMSKey: string
    :param KMSKey: An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language of the input documents. All documents must be in the same language.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier generated for the job. To get the status of a job, use this identifier with the DescribePHIDetectionJob operation.







Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    ComprehendMedical.Client.exceptions.InvalidRequestException
    ComprehendMedical.Client.exceptions.TooManyRequestsException
    ComprehendMedical.Client.exceptions.ResourceNotFoundException
    ComprehendMedical.Client.exceptions.InternalServerException
    
    """
    pass

def start_rx_norm_inference_job(InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, JobName=None, ClientRequestToken=None, KMSKey=None, LanguageCode=None):
    """
    Starts an asynchronous job to detect medication entities and link them to the RxNorm ontology. Use the DescribeRxNormInferenceJob operation to track the status of a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_rx_norm_inference_job(
        InputDataConfig={
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        OutputDataConfig={
            'S3Bucket': 'string',
            'S3Key': 'string'
        },
        DataAccessRoleArn='string',
        JobName='string',
        ClientRequestToken='string',
        KMSKey='string',
        LanguageCode='en'
    )
    
    
    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]\nSpecifies the format and location of the input data for the job.\n\nS3Bucket (string) -- [REQUIRED]The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.\nEach file in the document collection must be less than 40 KB. You can store a maximum of 30 GB in the bucket.\n\nS3Key (string) --The path to the input data files in the S3 bucket.\n\n\n

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]\nSpecifies where to send the output files.\n\nS3Bucket (string) -- [REQUIRED]When you use the OutputDataConfig object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.\n\nS3Key (string) --The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.\n\n\n

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. For more information, see Role-Based Permissions Required for Asynchronous Operations .\n

    :type JobName: string
    :param JobName: The identifier of the job.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you don\'t set the client request token, Amazon Comprehend Medical generates one.\nThis field is autopopulated if not provided.\n

    :type KMSKey: string
    :param KMSKey: An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language of the input documents. All documents must be in the same language.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier of the job.







Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.TooManyRequestsException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    ComprehendMedical.Client.exceptions.InvalidRequestException
    ComprehendMedical.Client.exceptions.TooManyRequestsException
    ComprehendMedical.Client.exceptions.ResourceNotFoundException
    ComprehendMedical.Client.exceptions.InternalServerException
    
    """
    pass

def stop_entities_detection_v2_job(JobId=None):
    """
    Stops a medical entities detection job in progress.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_entities_detection_v2_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier of the medical entities job to stop.\n

    :rtype: dict
ReturnsResponse Syntax{
    'JobId': 'string'
}


Response Structure

(dict) --
JobId (string) --The identifier of the medical entities detection job that was stopped.






Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

def stop_icd10_cm_inference_job(JobId=None):
    """
    Stops an InferICD10CM inference job in progress.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_icd10_cm_inference_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier of the job.\n

    :rtype: dict
ReturnsResponse Syntax{
    'JobId': 'string'
}


Response Structure

(dict) --
JobId (string) --The identifier generated for the job. To get the status of job, use this identifier with the DescribeICD10CMInferenceJob operation.






Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

def stop_phi_detection_job(JobId=None):
    """
    Stops a protected health information (PHI) detection job in progress.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_phi_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier of the PHI detection job to stop.\n

    :rtype: dict
ReturnsResponse Syntax{
    'JobId': 'string'
}


Response Structure

(dict) --
JobId (string) --The identifier of the PHI detection job that was stopped.






Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

def stop_rx_norm_inference_job(JobId=None):
    """
    Stops an InferRxNorm inference job in progress.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_rx_norm_inference_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier of the job.\n

    :rtype: dict
ReturnsResponse Syntax{
    'JobId': 'string'
}


Response Structure

(dict) --
JobId (string) --The identifier generated for the job. To get the status of job, use this identifier with the DescribeRxNormInferenceJob operation.






Exceptions

ComprehendMedical.Client.exceptions.InvalidRequestException
ComprehendMedical.Client.exceptions.ResourceNotFoundException
ComprehendMedical.Client.exceptions.InternalServerException


    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

