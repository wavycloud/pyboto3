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

def batch_detect_dominant_language(TextList=None):
    """
    Determines the dominant language of the input text for a batch of documents. For a list of languages that Amazon Comprehend can detect, see Amazon Comprehend Supported Languages .
    See also: AWS API Documentation
    
    
    :example: response = client.batch_detect_dominant_language(
        TextList=[
            'string',
        ]
    )
    
    
    :type TextList: list
    :param TextList: [REQUIRED]
            A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document should contain at least 20 characters and must contain fewer than 5,000 bytes of UTF-8 encoded characters.
            (string) --
            

    :rtype: dict
    :return: {
        'ResultList': [
            {
                'Index': 123,
                'Languages': [
                    {
                        'LanguageCode': 'string',
                        'Score': ...
                    },
                ]
            },
        ],
        'ErrorList': [
            {
                'Index': 123,
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_detect_entities(TextList=None, LanguageCode=None):
    """
    Inspects the text of a batch of documents and returns information about them. For more information about entities, see  how-entities
    See also: AWS API Documentation
    
    
    :example: response = client.batch_detect_entities(
        TextList=[
            'string',
        ],
        LanguageCode='string'
    )
    
    
    :type TextList: list
    :param TextList: [REQUIRED]
            A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer than 5,000 bytes of UTF-8 encoded characters.
            (string) --
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'ResultList': [
            {
                'Index': 123,
                'Entities': [
                    {
                        'Score': ...,
                        'Type': 'PERSON'|'LOCATION'|'ORGANIZATION'|'COMMERCIAL_ITEM'|'EVENT'|'DATE'|'QUANTITY'|'TITLE'|'OTHER',
                        'Text': 'string',
                        'BeginOffset': 123,
                        'EndOffset': 123
                    },
                ]
            },
        ],
        'ErrorList': [
            {
                'Index': 123,
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_detect_key_phrases(TextList=None, LanguageCode=None):
    """
    Detects the key noun phrases found in a batch of documents.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_detect_key_phrases(
        TextList=[
            'string',
        ],
        LanguageCode='string'
    )
    
    
    :type TextList: list
    :param TextList: [REQUIRED]
            A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            (string) --
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'ResultList': [
            {
                'Index': 123,
                'KeyPhrases': [
                    {
                        'Score': ...,
                        'Text': 'string',
                        'BeginOffset': 123,
                        'EndOffset': 123
                    },
                ]
            },
        ],
        'ErrorList': [
            {
                'Index': 123,
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_detect_sentiment(TextList=None, LanguageCode=None):
    """
    Inspects a batch of documents and returns an inference of the prevailing sentiment, POSITIVE , NEUTRAL , MIXED , or NEGATIVE , in each one.
    See also: AWS API Documentation
    
    
    :example: response = client.batch_detect_sentiment(
        TextList=[
            'string',
        ],
        LanguageCode='string'
    )
    
    
    :type TextList: list
    :param TextList: [REQUIRED]
            A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            (string) --
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language of the input documents. All documents must be in the same language.
            

    :rtype: dict
    :return: {
        'ResultList': [
            {
                'Index': 123,
                'Sentiment': 'POSITIVE'|'NEGATIVE'|'NEUTRAL'|'MIXED',
                'SentimentScore': {
                    'Positive': ...,
                    'Negative': ...,
                    'Neutral': ...,
                    'Mixed': ...
                }
            },
        ],
        'ErrorList': [
            {
                'Index': 123,
                'ErrorCode': 'string',
                'ErrorMessage': 'string'
            },
        ]
    }
    
    
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

def describe_topics_detection_job(JobId=None):
    """
    Gets the properties associated with a topic detection job. Use this operation to get the status of a detection job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_topics_detection_job(
        JobId='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier assigned by the user to the detection job.
            

    :rtype: dict
    :return: {
        'TopicsDetectionJobProperties': {
            'JobId': 'string',
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED',
            'Message': 'string',
            'SubmitTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'InputDataConfig': {
                'S3Uri': 'string',
                'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
            },
            'OutputDataConfig': {
                'S3Uri': 'string'
            },
            'NumberOfTopics': 123
        }
    }
    
    
    """
    pass

def detect_dominant_language(Text=None):
    """
    Determines the dominant language of the input text. For a list of languages that Amazon Comprehend can detect, see Amazon Comprehend Supported Languages .
    See also: AWS API Documentation
    
    
    :example: response = client.detect_dominant_language(
        Text='string'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 text string. Each string should contain at least 20 characters and must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            

    :rtype: dict
    :return: {
        'Languages': [
            {
                'LanguageCode': 'string',
                'Score': ...
            },
        ]
    }
    
    
    """
    pass

def detect_entities(Text=None, LanguageCode=None):
    """
    Inspects text for entities, and returns information about them. For more information, about entities, see  how-entities .
    See also: AWS API Documentation
    
    
    :example: response = client.detect_entities(
        Text='string',
        LanguageCode='en'|'es'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The RFC 5646 language code of the input text. If the request does not specify the language code, the service detects the dominant language. If you specify a language code that the service does not support, it returns UnsupportedLanguageException exception. For more information about RFC 5646, see Tags for Identifying Languages on the IETF Tools web site.
            

    :rtype: dict
    :return: {
        'Entities': [
            {
                'Score': ...,
                'Type': 'PERSON'|'LOCATION'|'ORGANIZATION'|'COMMERCIAL_ITEM'|'EVENT'|'DATE'|'QUANTITY'|'TITLE'|'OTHER',
                'Text': 'string',
                'BeginOffset': 123,
                'EndOffset': 123
            },
        ]
    }
    
    
    """
    pass

def detect_key_phrases(Text=None, LanguageCode=None):
    """
    Detects the key noun phrases found in the text.
    See also: AWS API Documentation
    
    
    :example: response = client.detect_key_phrases(
        Text='string',
        LanguageCode='en'|'es'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The RFC 5646 language code for the input text. If you don't specify a language code, Amazon Comprehend detects the dominant language. If you specify the code for a language that Amazon Comprehend does not support, it returns and UnsupportedLanguageException . For more information about RFC 5646, see Tags for Identifying Languages on the IETF Tools web site.
            

    :rtype: dict
    :return: {
        'KeyPhrases': [
            {
                'Score': ...,
                'Text': 'string',
                'BeginOffset': 123,
                'EndOffset': 123
            },
        ]
    }
    
    
    """
    pass

def detect_sentiment(Text=None, LanguageCode=None):
    """
    Inspects text and returns an inference of the prevailing sentiment (POSITIVE , NEUTRAL , MIXED , or NEGATIVE ).
    See also: AWS API Documentation
    
    
    :example: response = client.detect_sentiment(
        Text='string',
        LanguageCode='en'|'es'
    )
    
    
    :type Text: string
    :param Text: [REQUIRED]
            A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The RFC 5646 language code for the input text. If you don't specify a language code, Amazon Comprehend detects the dominant language. If you specify the code for a language that Amazon Comprehend does not support, it returns and UnsupportedLanguageException . For more information about RFC 5646, see Tags for Identifying Languages on the IETF Tools web site.
            

    :rtype: dict
    :return: {
        'Sentiment': 'POSITIVE'|'NEGATIVE'|'NEUTRAL'|'MIXED',
        'SentimentScore': {
            'Positive': ...,
            'Negative': ...,
            'Neutral': ...,
            'Mixed': ...
        }
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

def get_waiter():
    """
    
    """
    pass

def list_topics_detection_jobs(Filter=None, NextToken=None, MaxResults=None):
    """
    Gets a list of the topic detection jobs that you have submitted.
    See also: AWS API Documentation
    
    
    :example: response = client.list_topics_detection_jobs(
        Filter={
            'JobName': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED',
            'SubmitTimeBefore': datetime(2015, 1, 1),
            'SubmitTimeAfter': datetime(2015, 1, 1)
        },
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Filter: dict
    :param Filter: Filters the jobs that are returned. Jobs can be filtered on their name, status, or the date and time that they were submitted. You can set only one filter at a time.
            JobName (string) --
            JobStatus (string) --Filters the list of topic detection jobs based on job status. Returns only jobs with the specified status.
            SubmitTimeBefore (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted before the specified time. Jobs are returned in descending order, newest to oldest.
            SubmitTimeAfter (datetime) --Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted after the specified time. Jobs are returned in ascending order, oldest to newest.
            

    :type NextToken: string
    :param NextToken: Identifies the next page of results to return.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in each page.

    :rtype: dict
    :return: {
        'TopicsDetectionJobPropertiesList': [
            {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Uri': 'string',
                    'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                },
                'OutputDataConfig': {
                    'S3Uri': 'string'
                },
                'NumberOfTopics': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
    ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
    
    """
    pass

def start_topics_detection_job(InputDataConfig=None, OutputDataConfig=None, DataAccessRoleArn=None, JobName=None, NumberOfTopics=None, ClientRequestToken=None):
    """
    Starts an asynchronous topic detection job. Use the DescribeTopicDetectionJob operation to track the status of a job.
    See also: AWS API Documentation
    
    
    :example: response = client.start_topics_detection_job(
        InputDataConfig={
            'S3Uri': 'string',
            'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
        },
        OutputDataConfig={
            'S3Uri': 'string'
        },
        DataAccessRoleArn='string',
        JobName='string',
        NumberOfTopics=123,
        ClientRequestToken='string'
    )
    
    
    :type InputDataConfig: dict
    :param InputDataConfig: [REQUIRED]
            Specifies the format and location of the input data for the job.
            S3Uri (string) -- [REQUIRED]The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files.
            For example, if you use the URI S3://bucketName/prefix , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
            InputFormat (string) --Specifies how the text in an input file should be processed:
            ONE_DOC_PER_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
            ONE_DOC_PER_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
            

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]
            Specifies where to send the output files.
            S3Uri (string) -- [REQUIRED]The Amazon S3 URI where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling.
            The service creates an output file called output.tar.gz . It is a compressed archive that contains two files, topic-terms.csv that lists the terms associated with each topic, and doc-topics.csv that lists the documents associated with each topic. For more information, see topic-modeling .
            

    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data.
            

    :type JobName: string
    :param JobName: The identifier of the job.

    :type NumberOfTopics: integer
    :param NumberOfTopics: The number of topics to detect.

    :type ClientRequestToken: string
    :param ClientRequestToken: A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.
            This field is autopopulated if not provided.
            

    :rtype: dict
    :return: {
        'JobId': 'string',
        'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'
    }
    
    
    :returns: 
    SUBMITTED - The job has been received and is queued for processing.
    IN_PROGRESS - Amazon Comprehend is processing the job.
    COMPLETED - The job was successfully completed and the output is available.
    FAILED - The job did not complete. To get details, use the DescribeTopicDetectionJob operation.
    
    """
    pass

