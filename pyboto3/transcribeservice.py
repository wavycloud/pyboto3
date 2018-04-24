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

def create_vocabulary(VocabularyName=None, LanguageCode=None, Phrases=None):
    """
    Creates a new custom vocabulary that you can use to change the way Amazon Transcribe handles transcription of an audio file.
    See also: AWS API Documentation
    
    
    :example: response = client.create_vocabulary(
        VocabularyName='string',
        LanguageCode='en-US'|'es-US',
        Phrases=[
            'string',
        ]
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]
            The name of the vocabulary. The name must be unique within an AWS account. The name is case-sensitive.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language code of the vocabulary entries.
            

    :type Phrases: list
    :param Phrases: [REQUIRED]
            An array of strings that contains the vocabulary entries.
            (string) --
            

    :rtype: dict
    :return: {
        'VocabularyName': 'string',
        'LanguageCode': 'en-US'|'es-US',
        'VocabularyState': 'PENDING'|'READY'|'FAILED',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FailureReason': 'string'
    }
    
    
    """
    pass

def delete_vocabulary(VocabularyName=None):
    """
    Deletes a vocabulary from Amazon Transcribe.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_vocabulary(
        VocabularyName='string'
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]
            The name of the vocabulary to delete.
            

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

def get_transcription_job(TranscriptionJobName=None):
    """
    Returns information about a transcription job. To see the status of the job, check the TranscriptionJobStatus field. If the status is COMPLETED , the job is finished and you can find the results at the location specified in the TranscriptionFileUri field.
    See also: AWS API Documentation
    
    
    :example: response = client.get_transcription_job(
        TranscriptionJobName='string'
    )
    
    
    :type TranscriptionJobName: string
    :param TranscriptionJobName: [REQUIRED]
            The name of the job.
            

    :rtype: dict
    :return: {
        'TranscriptionJob': {
            'TranscriptionJobName': 'string',
            'TranscriptionJobStatus': 'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'LanguageCode': 'en-US'|'es-US',
            'MediaSampleRateHertz': 123,
            'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
            'Media': {
                'MediaFileUri': 'string'
            },
            'Transcript': {
                'TranscriptFileUri': 'string'
            },
            'CreationTime': datetime(2015, 1, 1),
            'CompletionTime': datetime(2015, 1, 1),
            'FailureReason': 'string',
            'Settings': {
                'VocabularyName': 'string',
                'ShowSpeakerLabels': True|False,
                'MaxSpeakerLabels': 123
            }
        }
    }
    
    
    """
    pass

def get_vocabulary(VocabularyName=None):
    """
    Gets information about a vocabulary.
    See also: AWS API Documentation
    
    
    :example: response = client.get_vocabulary(
        VocabularyName='string'
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]
            The name of the vocabulary to return information about. The name is case-sensitive.
            

    :rtype: dict
    :return: {
        'VocabularyName': 'string',
        'LanguageCode': 'en-US'|'es-US',
        'VocabularyState': 'PENDING'|'READY'|'FAILED',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FailureReason': 'string',
        'DownloadUri': 'string'
    }
    
    
    """
    pass

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_transcription_jobs(Status=None, JobNameContains=None, NextToken=None, MaxResults=None):
    """
    Lists transcription jobs with the specified status.
    See also: AWS API Documentation
    
    
    :example: response = client.list_transcription_jobs(
        Status='IN_PROGRESS'|'FAILED'|'COMPLETED',
        JobNameContains='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Status: string
    :param Status: When specified, returns only transcription jobs with the specified status.

    :type JobNameContains: string
    :param JobNameContains: When specified, the jobs returned in the list are limited to jobs whose name contains the specified string.

    :type NextToken: string
    :param NextToken: If the result of the previous request to ListTranscriptionJobs was truncated, include the NextToken to fetch the next set of jobs.

    :type MaxResults: integer
    :param MaxResults: The maximum number of jobs to return in the response. If there are fewer results in the list, this response contains only the actual results.

    :rtype: dict
    :return: {
        'Status': 'IN_PROGRESS'|'FAILED'|'COMPLETED',
        'NextToken': 'string',
        'TranscriptionJobSummaries': [
            {
                'TranscriptionJobName': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'CompletionTime': datetime(2015, 1, 1),
                'LanguageCode': 'en-US'|'es-US',
                'TranscriptionJobStatus': 'IN_PROGRESS'|'FAILED'|'COMPLETED',
                'FailureReason': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_vocabularies(NextToken=None, MaxResults=None, StateEquals=None, NameContains=None):
    """
    Returns a list of vocabularies that match the specified criteria. If no criteria are specified, returns the entire list of vocabularies.
    See also: AWS API Documentation
    
    
    :example: response = client.list_vocabularies(
        NextToken='string',
        MaxResults=123,
        StateEquals='PENDING'|'READY'|'FAILED',
        NameContains='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of the previous request to ListVocabularies was truncated, include the NextToken to fetch the next set of jobs.

    :type MaxResults: integer
    :param MaxResults: The maximum number of vocabularies to return in the response. If there are fewer results in the list, this response contains only the actual results.

    :type StateEquals: string
    :param StateEquals: When specified, only returns vocabularies with the VocabularyState field equal to the specified state.

    :type NameContains: string
    :param NameContains: When specified, the vocabularies returned in the list are limited to vocabularies whose name contains the specified string. The search is case-insensitive, ListVocabularies will return both 'vocabularyname' and 'VocabularyName' in the response list.

    :rtype: dict
    :return: {
        'Status': 'IN_PROGRESS'|'FAILED'|'COMPLETED',
        'NextToken': 'string',
        'Vocabularies': [
            {
                'VocabularyName': 'string',
                'LanguageCode': 'en-US'|'es-US',
                'LastModifiedTime': datetime(2015, 1, 1),
                'VocabularyState': 'PENDING'|'READY'|'FAILED'
            },
        ]
    }
    
    
    """
    pass

def start_transcription_job(TranscriptionJobName=None, LanguageCode=None, MediaSampleRateHertz=None, MediaFormat=None, Media=None, Settings=None):
    """
    Starts an asynchronous job to transcribe speech to text.
    See also: AWS API Documentation
    
    
    :example: response = client.start_transcription_job(
        TranscriptionJobName='string',
        LanguageCode='en-US'|'es-US',
        MediaSampleRateHertz=123,
        MediaFormat='mp3'|'mp4'|'wav'|'flac',
        Media={
            'MediaFileUri': 'string'
        },
        Settings={
            'VocabularyName': 'string',
            'ShowSpeakerLabels': True|False,
            'MaxSpeakerLabels': 123
        }
    )
    
    
    :type TranscriptionJobName: string
    :param TranscriptionJobName: [REQUIRED]
            The name of the job. The name must be unique within an AWS account.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language code for the language used in the input media file.
            

    :type MediaSampleRateHertz: integer
    :param MediaSampleRateHertz: The sample rate, in Hertz, of the audio track in the input media file.

    :type MediaFormat: string
    :param MediaFormat: [REQUIRED]
            The format of the input media file.
            

    :type Media: dict
    :param Media: [REQUIRED]
            An object that describes the input media for a transcription job.
            MediaFileUri (string) --The S3 location of the input media file. The URI must be in the same region as the API endpoint that you are calling. The general form is:
            https://aws-region.amazonaws.com/bucket-name/keyprefix/objectkey
            For example:
            https://s3-us-east-1.amazonaws.com/examplebucket/example.mp4https://s3-us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4
            For more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .
            

    :type Settings: dict
    :param Settings: A Settings object that provides optional settings for a transcription job.
            VocabularyName (string) --The name of a vocabulary to use when processing the transcription job.
            ShowSpeakerLabels (boolean) --Determines whether the transcription job should use speaker recognition to identify different speakers in the input audio. If you set the ShowSpeakerLabels field to true, you must also set the maximum number of speaker labels MaxSpeakerLabels field.
            MaxSpeakerLabels (integer) --The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers will be identified as a single speaker. If you specify the MaxSpeakerLabels field, you must set the ShowSpeakerLabels field to true.
            

    :rtype: dict
    :return: {
        'TranscriptionJob': {
            'TranscriptionJobName': 'string',
            'TranscriptionJobStatus': 'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'LanguageCode': 'en-US'|'es-US',
            'MediaSampleRateHertz': 123,
            'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
            'Media': {
                'MediaFileUri': 'string'
            },
            'Transcript': {
                'TranscriptFileUri': 'string'
            },
            'CreationTime': datetime(2015, 1, 1),
            'CompletionTime': datetime(2015, 1, 1),
            'FailureReason': 'string',
            'Settings': {
                'VocabularyName': 'string',
                'ShowSpeakerLabels': True|False,
                'MaxSpeakerLabels': 123
            }
        }
    }
    
    
    """
    pass

def update_vocabulary(VocabularyName=None, LanguageCode=None, Phrases=None):
    """
    Updates an existing vocabulary with new values.
    See also: AWS API Documentation
    
    
    :example: response = client.update_vocabulary(
        VocabularyName='string',
        LanguageCode='en-US'|'es-US',
        Phrases=[
            'string',
        ]
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]
            The name of the vocabulary to update. The name is case-sensitive.
            

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]
            The language code of the vocabulary entries.
            

    :type Phrases: list
    :param Phrases: [REQUIRED]
            An array of strings containing the vocabulary entries.
            (string) --
            

    :rtype: dict
    :return: {
        'VocabularyName': 'string',
        'LanguageCode': 'en-US'|'es-US',
        'LastModifiedTime': datetime(2015, 1, 1),
        'VocabularyState': 'PENDING'|'READY'|'FAILED'
    }
    
    
    """
    pass

