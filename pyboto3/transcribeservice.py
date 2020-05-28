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

def create_medical_vocabulary(VocabularyName=None, LanguageCode=None, VocabularyFileUri=None):
    """
    Creates a new custom vocabulary that you can use to change how Amazon Transcribe Medical transcribes your audio file.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_medical_vocabulary(
        VocabularyName='string',
        LanguageCode='en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        VocabularyFileUri='string'
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]\nThe name of the custom vocabulary. This case-sensitive name must be unique within an AWS account. If you try to create a vocabulary with the same name as a previous vocabulary you will receive a ConflictException error.\n

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language code used for the entries within your custom vocabulary. The language code of your custom vocabulary must match the language code of your transcription job. US English (en-US) is the only language code available for Amazon Transcribe Medical.\n

    :type VocabularyFileUri: string
    :param VocabularyFileUri: [REQUIRED]\nThe Amazon S3 location of the text file you use to define your custom vocabulary. The URI must be in the same AWS region as the API endpoint you\'re calling. Enter information about your VocabularyFileUri in the following format:\n\nhttps://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>\nThis is an example of a vocabulary file uri location in Amazon S3:\n\nhttps://s3.us-east-1.amazonaws.com/AWSDOC-EXAMPLE-BUCKET/vocab.txt\nFor more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .\nFor more information about custom vocabularies, see Medical Custom Vocabularies .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VocabularyName': 'string',
    'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
    'VocabularyState': 'PENDING'|'READY'|'FAILED',
    'LastModifiedTime': datetime(2015, 1, 1),
    'FailureReason': 'string'
}


Response Structure

(dict) --

VocabularyName (string) --
The name of the vocabulary. The name must be unique within an AWS account. It is also case-sensitive.

LanguageCode (string) --
The language code you chose to describe the entries in your custom vocabulary. US English (en-US) is the only valid language code for Amazon Transcribe Medical.

VocabularyState (string) --
The processing state of your custom vocabulary in Amazon Transcribe Medical. If the state is READY you can use the vocabulary in a StartMedicalTranscriptionJob request.

LastModifiedTime (datetime) --
The date and time you created the vocabulary.

FailureReason (string) --
If the VocabularyState field is FAILED , this field contains information about why the job failed.







Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.ConflictException


    :return: {
        'VocabularyName': 'string',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'VocabularyState': 'PENDING'|'READY'|'FAILED',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FailureReason': 'string'
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    TranscribeService.Client.exceptions.ConflictException
    
    """
    pass

def create_vocabulary(VocabularyName=None, LanguageCode=None, Phrases=None, VocabularyFileUri=None):
    """
    Creates a new custom vocabulary that you can use to change the way Amazon Transcribe handles transcription of an audio file.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_vocabulary(
        VocabularyName='string',
        LanguageCode='en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        Phrases=[
            'string',
        ],
        VocabularyFileUri='string'
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]\nThe name of the vocabulary. The name must be unique within an AWS account. The name is case-sensitive. If you try to create a vocabulary with the same name as a previous vocabulary you will receive a ConflictException error.\n

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language code of the vocabulary entries.\n

    :type Phrases: list
    :param Phrases: An array of strings that contains the vocabulary entries.\n\n(string) --\n\n

    :type VocabularyFileUri: string
    :param VocabularyFileUri: The S3 location of the text file that contains the definition of the custom vocabulary. The URI must be in the same region as the API endpoint that you are calling. The general form is\nFor more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .\nFor more information about custom vocabularies, see Custom Vocabularies .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VocabularyName': 'string',
    'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
    'VocabularyState': 'PENDING'|'READY'|'FAILED',
    'LastModifiedTime': datetime(2015, 1, 1),
    'FailureReason': 'string'
}


Response Structure

(dict) --

VocabularyName (string) --
The name of the vocabulary.

LanguageCode (string) --
The language code of the vocabulary entries.

VocabularyState (string) --
The processing state of the vocabulary. When the VocabularyState field contains READY the vocabulary is ready to be used in a StartTranscriptionJob request.

LastModifiedTime (datetime) --
The date and time that the vocabulary was created.

FailureReason (string) --
If the VocabularyState field is FAILED , this field contains information about why the job failed.







Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.ConflictException


    :return: {
        'VocabularyName': 'string',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'VocabularyState': 'PENDING'|'READY'|'FAILED',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FailureReason': 'string'
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    TranscribeService.Client.exceptions.ConflictException
    
    """
    pass

def create_vocabulary_filter(VocabularyFilterName=None, LanguageCode=None, Words=None, VocabularyFilterFileUri=None):
    """
    Creates a new vocabulary filter that you can use to filter words, such as profane words, from the output of a transcription job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_vocabulary_filter(
        VocabularyFilterName='string',
        LanguageCode='en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        Words=[
            'string',
        ],
        VocabularyFilterFileUri='string'
    )
    
    
    :type VocabularyFilterName: string
    :param VocabularyFilterName: [REQUIRED]\nThe vocabulary filter name. The name must be unique within the account that contains it.If you try to create a vocabulary filter with the same name as a previous vocabulary filter you will receive a ConflictException error.\n

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language code of the words in the vocabulary filter. All words in the filter must be in the same language. The vocabulary filter can only be used with transcription jobs in the specified language.\n

    :type Words: list
    :param Words: The words to use in the vocabulary filter. Only use characters from the character set defined for custom vocabularies. For a list of character sets, see Character Sets for Custom Vocabularies .\nIf you provide a list of words in the Words parameter, you can\'t use the VocabularyFilterFileUri parameter.\n\n(string) --\n\n

    :type VocabularyFilterFileUri: string
    :param VocabularyFilterFileUri: The Amazon S3 location of a text file used as input to create the vocabulary filter. Only use characters from the character set defined for custom vocabularies. For a list of character sets, see Character Sets for Custom Vocabularies .\nThe specified file must be less than 50 KB of UTF-8 characters.\nIf you provide the location of a list of words in the VocabularyFilterFileUri parameter, you can\'t use the Words parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VocabularyFilterName': 'string',
    'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
    'LastModifiedTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --

VocabularyFilterName (string) --
The name of the vocabulary filter.

LanguageCode (string) --
The language code of the words in the collection.

LastModifiedTime (datetime) --
The date and time that the vocabulary filter was modified.







Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.ConflictException


    :return: {
        'VocabularyFilterName': 'string',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'LastModifiedTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    TranscribeService.Client.exceptions.ConflictException
    
    """
    pass

def delete_medical_transcription_job(MedicalTranscriptionJobName=None):
    """
    Deletes a transcription job generated by Amazon Transcribe Medical and any related information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_medical_transcription_job(
        MedicalTranscriptionJobName='string'
    )
    
    
    :type MedicalTranscriptionJobName: string
    :param MedicalTranscriptionJobName: [REQUIRED]\nThe name you provide to the DeleteMedicalTranscriptionJob object to delete a transcription job.\n

    """
    pass

def delete_medical_vocabulary(VocabularyName=None):
    """
    Deletes a vocabulary from Amazon Transcribe Medical.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_medical_vocabulary(
        VocabularyName='string'
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]\nThe name of the vocabulary you are choosing to delete.\n

    """
    pass

def delete_transcription_job(TranscriptionJobName=None):
    """
    Deletes a previously submitted transcription job along with any other generated results such as the transcription, models, and so on.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_transcription_job(
        TranscriptionJobName='string'
    )
    
    
    :type TranscriptionJobName: string
    :param TranscriptionJobName: [REQUIRED]\nThe name of the transcription job to be deleted.\n

    """
    pass

def delete_vocabulary(VocabularyName=None):
    """
    Deletes a vocabulary from Amazon Transcribe.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_vocabulary(
        VocabularyName='string'
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]\nThe name of the vocabulary to delete.\n

    """
    pass

def delete_vocabulary_filter(VocabularyFilterName=None):
    """
    Removes a vocabulary filter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_vocabulary_filter(
        VocabularyFilterName='string'
    )
    
    
    :type VocabularyFilterName: string
    :param VocabularyFilterName: [REQUIRED]\nThe name of the vocabulary filter to remove.\n

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

def get_medical_transcription_job(MedicalTranscriptionJobName=None):
    """
    Returns information about a transcription job from Amazon Transcribe Medical. To see the status of the job, check the TranscriptionJobStatus field. If the status is COMPLETED , the job is finished. You find the results of the completed job in the TranscriptFileUri field.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_medical_transcription_job(
        MedicalTranscriptionJobName='string'
    )
    
    
    :type MedicalTranscriptionJobName: string
    :param MedicalTranscriptionJobName: [REQUIRED]\nThe name of the medical transcription job.\n

    :rtype: dict
ReturnsResponse Syntax{
    'MedicalTranscriptionJob': {
        'MedicalTranscriptionJobName': 'string',
        'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'MediaSampleRateHertz': 123,
        'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
        'Media': {
            'MediaFileUri': 'string'
        },
        'Transcript': {
            'TranscriptFileUri': 'string'
        },
        'StartTime': datetime(2015, 1, 1),
        'CreationTime': datetime(2015, 1, 1),
        'CompletionTime': datetime(2015, 1, 1),
        'FailureReason': 'string',
        'Settings': {
            'ShowSpeakerLabels': True|False,
            'MaxSpeakerLabels': 123,
            'ChannelIdentification': True|False,
            'ShowAlternatives': True|False,
            'MaxAlternatives': 123,
            'VocabularyName': 'string'
        },
        'Specialty': 'PRIMARYCARE',
        'Type': 'CONVERSATION'|'DICTATION'
    }
}


Response Structure

(dict) --
MedicalTranscriptionJob (dict) --An object that contains the results of the medical transcription job.

MedicalTranscriptionJobName (string) --The name for a given medical transcription job.

TranscriptionJobStatus (string) --The completion status of a medical transcription job.

LanguageCode (string) --The language code for the language spoken in the source audio file. US English (en-US) is the only supported language for medical transcriptions. Any other value you enter for language code results in a BadRequestException error.

MediaSampleRateHertz (integer) --The sample rate, in Hertz, of the source audio containing medical information.
If you don\'t specify the sample rate, Amazon Transcribe Medical determines it for you. If you choose to specify the sample rate, it must match the rate detected by Amazon Transcribe Medical. In most cases, you should leave the MediaSampleHertz blank and let Amazon Transcribe Medical determine the sample rate.

MediaFormat (string) --The format of the input media file.

Media (dict) --Describes the input media file in a transcription request.

MediaFileUri (string) --The S3 object location of the input media file. The URI must be in the same region as the API endpoint that you are calling. The general form is:
For example:
For more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .



Transcript (dict) --An object that contains the MedicalTranscript . The MedicalTranscript contains the TranscriptFileUri .

TranscriptFileUri (string) --The S3 object location of the medical transcript.
Use this URI to access the medical transcript. This URI points to the S3 bucket you created to store the medical transcript.



StartTime (datetime) --A timestamp that shows when the job started processing.

CreationTime (datetime) --A timestamp that shows when the job was created.

CompletionTime (datetime) --A timestamp that shows when the job was completed.

FailureReason (string) --If the TranscriptionJobStatus field is FAILED , this field contains information about why the job failed.
The FailureReason field contains one of the following values:

Unsupported media format - The media format specified in the MediaFormat field of the request isn\'t valid. See the description of the MediaFormat field for a list of valid values.
The media format provided does not match the detected media format - The media format of the audio file doesn\'t match the format specified in the MediaFormat field in the request. Check the media format of your media file and make sure the two values match.
Invalid sample rate for audio file - The sample rate specified in the MediaSampleRateHertz of the request isn\'t valid. The sample rate must be between 8000 and 48000 Hertz.
The sample rate provided does not match the detected sample rate - The sample rate in the audio file doesn\'t match the sample rate specified in the MediaSampleRateHertz field in the request. Check the sample rate of your media file and make sure that the two values match.
Invalid file size: file size too large - The size of your audio file is larger than what Amazon Transcribe Medical can process. For more information, see Guidlines and Quotas in the Amazon Transcribe Medical Guide
Invalid number of channels: number of channels too large - Your audio contains more channels than Amazon Transcribe Medical is configured to process. To request additional channels, see Amazon Transcribe Medical Endpoints and Quotas in the Amazon Web Services General Reference


Settings (dict) --Object that contains object.

ShowSpeakerLabels (boolean) --Determines whether the transcription job uses speaker recognition to identify different speakers in the input audio. Speaker recongition labels individual speakers in the audio file. If you set the ShowSpeakerLabels field to true, you must also set the maximum number of speaker labels in the MaxSpeakerLabels field.
You can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException .

MaxSpeakerLabels (integer) --The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers are identified as a single speaker. If you specify the MaxSpeakerLabels field, you must set the ShowSpeakerLabels field to true.

ChannelIdentification (boolean) --Instructs Amazon Transcribe Medical to process each audio channel separately and then merge the transcription output of each channel into a single transcription.
Amazon Transcribe Medical also produces a transcription of each item detected on an audio channel, including the start time and end time of the item and alternative transcriptions of item. The alternative transcriptions also come with confidence scores provided by Amazon Transcribe Medical.
You can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException

ShowAlternatives (boolean) --Determines whether alternative transcripts are generated along with the transcript that has the highest confidence. If you set ShowAlternatives field to true, you must also set the maximum number of alternatives to return in the MaxAlternatives field.

MaxAlternatives (integer) --The maximum number of alternatives that you tell the service to return. If you specify the MaxAlternatives field, you must set the ShowAlternatives field to true.

VocabularyName (string) --The name of the vocabulary to use when processing a medical transcription job.



Specialty (string) --The medical specialty of any clinicians providing a dictation or having a conversation. PRIMARYCARE is the only available setting for this object. This specialty enables you to generate transcriptions for the following medical fields:

Family Medicine


Type (string) --The type of speech in the transcription job. CONVERSATION is generally used for patient-physician dialogues. DICTATION is the setting for physicians speaking their notes after seeing a patient. For more information, see  how-it-works-med








Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.NotFoundException


    :return: {
        'MedicalTranscriptionJob': {
            'MedicalTranscriptionJobName': 'string',
            'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
            'MediaSampleRateHertz': 123,
            'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
            'Media': {
                'MediaFileUri': 'string'
            },
            'Transcript': {
                'TranscriptFileUri': 'string'
            },
            'StartTime': datetime(2015, 1, 1),
            'CreationTime': datetime(2015, 1, 1),
            'CompletionTime': datetime(2015, 1, 1),
            'FailureReason': 'string',
            'Settings': {
                'ShowSpeakerLabels': True|False,
                'MaxSpeakerLabels': 123,
                'ChannelIdentification': True|False,
                'ShowAlternatives': True|False,
                'MaxAlternatives': 123,
                'VocabularyName': 'string'
            },
            'Specialty': 'PRIMARYCARE',
            'Type': 'CONVERSATION'|'DICTATION'
        }
    }
    
    
    :returns: 
    Family Medicine
    
    """
    pass

def get_medical_vocabulary(VocabularyName=None):
    """
    Retrieve information about a medical vocabulary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_medical_vocabulary(
        VocabularyName='string'
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]\nThe name of the vocabulary you are trying to get information about. The value you enter for this request is case-sensitive.\n

    :rtype: dict
ReturnsResponse Syntax{
    'VocabularyName': 'string',
    'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
    'VocabularyState': 'PENDING'|'READY'|'FAILED',
    'LastModifiedTime': datetime(2015, 1, 1),
    'FailureReason': 'string',
    'DownloadUri': 'string'
}


Response Structure

(dict) --
VocabularyName (string) --The valid name that Amazon Transcribe Medical returns.

LanguageCode (string) --The valid language code returned for your vocabulary entries.

VocabularyState (string) --The processing state of the vocabulary.

LastModifiedTime (datetime) --The date and time the vocabulary was last modified with a text file different from what was previously used.

FailureReason (string) --If the VocabularyState is FAILED , this field contains information about why the job failed.

DownloadUri (string) --The Amazon S3 location where the vocabulary is stored. Use this URI to get the contents of the vocabulary. You can download your vocabulary from the URI for a limited time.






Exceptions

TranscribeService.Client.exceptions.NotFoundException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.BadRequestException


    :return: {
        'VocabularyName': 'string',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'VocabularyState': 'PENDING'|'READY'|'FAILED',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FailureReason': 'string',
        'DownloadUri': 'string'
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

def get_transcription_job(TranscriptionJobName=None):
    """
    Returns information about a transcription job. To see the status of the job, check the TranscriptionJobStatus field. If the status is COMPLETED , the job is finished and you can find the results at the location specified in the TranscriptFileUri field. If you enable content redaction, the redacted transcript appears in RedactedTranscriptFileUri .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_transcription_job(
        TranscriptionJobName='string'
    )
    
    
    :type TranscriptionJobName: string
    :param TranscriptionJobName: [REQUIRED]\nThe name of the job.\n

    :rtype: dict
ReturnsResponse Syntax{
    'TranscriptionJob': {
        'TranscriptionJobName': 'string',
        'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'MediaSampleRateHertz': 123,
        'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
        'Media': {
            'MediaFileUri': 'string'
        },
        'Transcript': {
            'TranscriptFileUri': 'string',
            'RedactedTranscriptFileUri': 'string'
        },
        'StartTime': datetime(2015, 1, 1),
        'CreationTime': datetime(2015, 1, 1),
        'CompletionTime': datetime(2015, 1, 1),
        'FailureReason': 'string',
        'Settings': {
            'VocabularyName': 'string',
            'ShowSpeakerLabels': True|False,
            'MaxSpeakerLabels': 123,
            'ChannelIdentification': True|False,
            'ShowAlternatives': True|False,
            'MaxAlternatives': 123,
            'VocabularyFilterName': 'string',
            'VocabularyFilterMethod': 'remove'|'mask'
        },
        'JobExecutionSettings': {
            'AllowDeferredExecution': True|False,
            'DataAccessRoleArn': 'string'
        },
        'ContentRedaction': {
            'RedactionType': 'PII',
            'RedactionOutput': 'redacted'|'redacted_and_unredacted'
        }
    }
}


Response Structure

(dict) --
TranscriptionJob (dict) --An object that contains the results of the transcription job.

TranscriptionJobName (string) --The name of the transcription job.

TranscriptionJobStatus (string) --The status of the transcription job.

LanguageCode (string) --The language code for the input speech.

MediaSampleRateHertz (integer) --The sample rate, in Hertz, of the audio track in the input media file.

MediaFormat (string) --The format of the input media file.

Media (dict) --An object that describes the input media for the transcription job.

MediaFileUri (string) --The S3 object location of the input media file. The URI must be in the same region as the API endpoint that you are calling. The general form is:
For example:
For more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .



Transcript (dict) --An object that describes the output of the transcription job.

TranscriptFileUri (string) --The S3 object location of the the transcript.
Use this URI to access the transcript. If you specified an S3 bucket in the OutputBucketName field when you created the job, this is the URI of that bucket. If you chose to store the transcript in Amazon Transcribe, this is a shareable URL that provides secure access to that location.

RedactedTranscriptFileUri (string) --The S3 object location of the redacted transcript.
Use this URI to access the redacated transcript. If you specified an S3 bucket in the OutputBucketName field when you created the job, this is the URI of that bucket. If you chose to store the transcript in Amazon Transcribe, this is a shareable URL that provides secure access to that location.



StartTime (datetime) --A timestamp that shows with the job was started processing.

CreationTime (datetime) --A timestamp that shows when the job was created.

CompletionTime (datetime) --A timestamp that shows when the job was completed.

FailureReason (string) --If the TranscriptionJobStatus field is FAILED , this field contains information about why the job failed.
The FailureReason field can contain one of the following values:

Unsupported media format - The media format specified in the MediaFormat field of the request isn\'t valid. See the description of the MediaFormat field for a list of valid values.
The media format provided does not match the detected media format - The media format of the audio file doesn\'t match the format specified in the MediaFormat field in the request. Check the media format of your media file and make sure that the two values match.
Invalid sample rate for audio file - The sample rate specified in the MediaSampleRateHertz of the request isn\'t valid. The sample rate must be between 8000 and 48000 Hertz.
The sample rate provided does not match the detected sample rate - The sample rate in the audio file doesn\'t match the sample rate specified in the MediaSampleRateHertz field in the request. Check the sample rate of your media file and make sure that the two values match.
Invalid file size: file size too large - The size of your audio file is larger than Amazon Transcribe can process. For more information, see Limits in the Amazon Transcribe Developer Guide .
Invalid number of channels: number of channels too large - Your audio contains more channels than Amazon Transcribe is configured to process. To request additional channels, see Amazon Transcribe Limits in the Amazon Web Services General Reference .


Settings (dict) --Optional settings for the transcription job. Use these settings to turn on speaker recognition, to set the maximum number of speakers that should be identified and to specify a custom vocabulary to use when processing the transcription job.

VocabularyName (string) --The name of a vocabulary to use when processing the transcription job.

ShowSpeakerLabels (boolean) --Determines whether the transcription job uses speaker recognition to identify different speakers in the input audio. Speaker recognition labels individual speakers in the audio file. If you set the ShowSpeakerLabels field to true, you must also set the maximum number of speaker labels MaxSpeakerLabels field.
You can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException .

MaxSpeakerLabels (integer) --The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers are identified as a single speaker. If you specify the MaxSpeakerLabels field, you must set the ShowSpeakerLabels field to true.

ChannelIdentification (boolean) --Instructs Amazon Transcribe to process each audio channel separately and then merge the transcription output of each channel into a single transcription.
Amazon Transcribe also produces a transcription of each item detected on an audio channel, including the start time and end time of the item and alternative transcriptions of the item including the confidence that Amazon Transcribe has in the transcription.
You can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException .

ShowAlternatives (boolean) --Determines whether the transcription contains alternative transcriptions. If you set the ShowAlternatives field to true, you must also set the maximum number of alternatives to return in the MaxAlternatives field.

MaxAlternatives (integer) --The number of alternative transcriptions that the service should return. If you specify the MaxAlternatives field, you must set the ShowAlternatives field to true.

VocabularyFilterName (string) --The name of the vocabulary filter to use when transcribing the audio. The filter that you specify must have the same language code as the transcription job.

VocabularyFilterMethod (string) --Set to mask to remove filtered text from the transcript and replace it with three asterisks ("***") as placeholder text. Set to remove to remove filtered text from the transcript without using placeholder text.



JobExecutionSettings (dict) --Provides information about how a transcription job is executed.

AllowDeferredExecution (boolean) --Indicates whether a job should be queued by Amazon Transcribe when the concurrent execution limit is exceeded. When the AllowDeferredExecution field is true, jobs are queued and executed when the number of executing jobs falls below the concurrent execution limit. If the field is false, Amazon Transcribe returns a LimitExceededException exception.
If you specify the AllowDeferredExecution field, you must specify the DataAccessRoleArn field.

DataAccessRoleArn (string) --The Amazon Resource Name (ARN) of a role that has access to the S3 bucket that contains the input files. Amazon Transcribe assumes this role to read queued media files. If you have specified an output S3 bucket for the transcription results, this role should have access to the output bucket as well.
If you specify the AllowDeferredExecution field, you must specify the DataAccessRoleArn field.



ContentRedaction (dict) --An object that describes content redaction settings for the transcription job.

RedactionType (string) --Request parameter that defines the entities to be redacted. The only accepted value is PII .

RedactionOutput (string) --The output transcript file stored in either the default S3 bucket or in a bucket you specify.
When you choose redacted Amazon Transcribe outputs only the redacted transcript.
When you choose redacted_and_unredacted Amazon Transcribe outputs both the redacted and unredacted transcripts.










Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.NotFoundException


    :return: {
        'TranscriptionJob': {
            'TranscriptionJobName': 'string',
            'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
            'MediaSampleRateHertz': 123,
            'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
            'Media': {
                'MediaFileUri': 'string'
            },
            'Transcript': {
                'TranscriptFileUri': 'string',
                'RedactedTranscriptFileUri': 'string'
            },
            'StartTime': datetime(2015, 1, 1),
            'CreationTime': datetime(2015, 1, 1),
            'CompletionTime': datetime(2015, 1, 1),
            'FailureReason': 'string',
            'Settings': {
                'VocabularyName': 'string',
                'ShowSpeakerLabels': True|False,
                'MaxSpeakerLabels': 123,
                'ChannelIdentification': True|False,
                'ShowAlternatives': True|False,
                'MaxAlternatives': 123,
                'VocabularyFilterName': 'string',
                'VocabularyFilterMethod': 'remove'|'mask'
            },
            'JobExecutionSettings': {
                'AllowDeferredExecution': True|False,
                'DataAccessRoleArn': 'string'
            },
            'ContentRedaction': {
                'RedactionType': 'PII',
                'RedactionOutput': 'redacted'|'redacted_and_unredacted'
            }
        }
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    TranscribeService.Client.exceptions.NotFoundException
    
    """
    pass

def get_vocabulary(VocabularyName=None):
    """
    Gets information about a vocabulary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_vocabulary(
        VocabularyName='string'
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]\nThe name of the vocabulary to return information about. The name is case-sensitive.\n

    :rtype: dict
ReturnsResponse Syntax{
    'VocabularyName': 'string',
    'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
    'VocabularyState': 'PENDING'|'READY'|'FAILED',
    'LastModifiedTime': datetime(2015, 1, 1),
    'FailureReason': 'string',
    'DownloadUri': 'string'
}


Response Structure

(dict) --
VocabularyName (string) --The name of the vocabulary to return.

LanguageCode (string) --The language code of the vocabulary entries.

VocabularyState (string) --The processing state of the vocabulary.

LastModifiedTime (datetime) --The date and time that the vocabulary was last modified.

FailureReason (string) --If the VocabularyState field is FAILED , this field contains information about why the job failed.

DownloadUri (string) --The S3 location where the vocabulary is stored. Use this URI to get the contents of the vocabulary. The URI is available for a limited time.






Exceptions

TranscribeService.Client.exceptions.NotFoundException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.BadRequestException


    :return: {
        'VocabularyName': 'string',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'VocabularyState': 'PENDING'|'READY'|'FAILED',
        'LastModifiedTime': datetime(2015, 1, 1),
        'FailureReason': 'string',
        'DownloadUri': 'string'
    }
    
    
    """
    pass

def get_vocabulary_filter(VocabularyFilterName=None):
    """
    Returns information about a vocabulary filter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_vocabulary_filter(
        VocabularyFilterName='string'
    )
    
    
    :type VocabularyFilterName: string
    :param VocabularyFilterName: [REQUIRED]\nThe name of the vocabulary filter for which to return information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'VocabularyFilterName': 'string',
    'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
    'LastModifiedTime': datetime(2015, 1, 1),
    'DownloadUri': 'string'
}


Response Structure

(dict) --
VocabularyFilterName (string) --The name of the vocabulary filter.

LanguageCode (string) --The language code of the words in the vocabulary filter.

LastModifiedTime (datetime) --The date and time that the contents of the vocabulary filter were updated.

DownloadUri (string) --The URI of the list of words in the vocabulary filter. You can use this URI to get the list of words.






Exceptions

TranscribeService.Client.exceptions.NotFoundException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.BadRequestException


    :return: {
        'VocabularyFilterName': 'string',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'LastModifiedTime': datetime(2015, 1, 1),
        'DownloadUri': 'string'
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

def list_medical_transcription_jobs(Status=None, JobNameContains=None, NextToken=None, MaxResults=None):
    """
    Lists medical transcription jobs with a specified status or substring that matches their names.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_medical_transcription_jobs(
        Status='QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
        JobNameContains='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Status: string
    :param Status: When specified, returns only medical transcription jobs with the specified status. Jobs are ordered by creation date, with the newest jobs returned first. If you don\'t specify a status, Amazon Transcribe Medical returns all transcription jobs ordered by creation date.

    :type JobNameContains: string
    :param JobNameContains: When specified, the jobs returned in the list are limited to jobs whose name contains the specified string.

    :type NextToken: string
    :param NextToken: If you a receive a truncated result in the previous request of ListMedicalTranscriptionJobs , include NextToken to fetch the next set of jobs.

    :type MaxResults: integer
    :param MaxResults: The maximum number of medical transcription jobs to return in the response. IF there are fewer results in the list, this response contains only the actual results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
    'NextToken': 'string',
    'MedicalTranscriptionJobSummaries': [
        {
            'MedicalTranscriptionJobName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'StartTime': datetime(2015, 1, 1),
            'CompletionTime': datetime(2015, 1, 1),
            'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
            'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'FailureReason': 'string',
            'OutputLocationType': 'CUSTOMER_BUCKET'|'SERVICE_BUCKET',
            'Specialty': 'PRIMARYCARE',
            'Type': 'CONVERSATION'|'DICTATION'
        },
    ]
}


Response Structure

(dict) --

Status (string) --
The requested status of the medical transcription jobs returned.

NextToken (string) --
The ListMedicalTranscriptionJobs operation returns a page of jobs at a time. The maximum size of the page is set by the MaxResults parameter. If the number of jobs exceeds what can fit on a page, Amazon Transcribe Medical returns the NextPage token. Include the token in the next request to the ListMedicalTranscriptionJobs operation to return in the next page of jobs.

MedicalTranscriptionJobSummaries (list) --
A list of objects containing summary information for a transcription job.

(dict) --
Provides summary information about a transcription job.

MedicalTranscriptionJobName (string) --
The name of a medical transcription job.

CreationTime (datetime) --
A timestamp that shows when the medical transcription job was created.

StartTime (datetime) --
A timestamp that shows when the job began processing.

CompletionTime (datetime) --
A timestamp that shows when the job was completed.

LanguageCode (string) --
The language of the transcript in the source audio file.

TranscriptionJobStatus (string) --
The status of the medical transcription job.

FailureReason (string) --
If the TranscriptionJobStatus field is FAILED , a description of the error.

OutputLocationType (string) --
Indicates the location of the transcription job\'s output.
The CUSTOMER_BUCKET is the S3 location provided in the OutputBucketName field when the

Specialty (string) --
The medical specialty of the transcription job. Primary care is the only valid value.

Type (string) --
The speech of the clinician in the input audio.











Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException


    :return: {
        'Status': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
        'NextToken': 'string',
        'MedicalTranscriptionJobSummaries': [
            {
                'MedicalTranscriptionJobName': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'StartTime': datetime(2015, 1, 1),
                'CompletionTime': datetime(2015, 1, 1),
                'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
                'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
                'FailureReason': 'string',
                'OutputLocationType': 'CUSTOMER_BUCKET'|'SERVICE_BUCKET',
                'Specialty': 'PRIMARYCARE',
                'Type': 'CONVERSATION'|'DICTATION'
            },
        ]
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    
    """
    pass

def list_medical_vocabularies(NextToken=None, MaxResults=None, StateEquals=None, NameContains=None):
    """
    Returns a list of vocabularies that match the specified criteria. You get the entire list of vocabularies if you don\'t enter a value in any of the request parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_medical_vocabularies(
        NextToken='string',
        MaxResults=123,
        StateEquals='PENDING'|'READY'|'FAILED',
        NameContains='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of your previous request to ListMedicalVocabularies was truncated, include the NextToken to fetch the next set of jobs.

    :type MaxResults: integer
    :param MaxResults: The maximum number of vocabularies to return in the response.

    :type StateEquals: string
    :param StateEquals: When specified, only returns vocabularies with the VocabularyState equal to the specified vocabulary state.

    :type NameContains: string
    :param NameContains: Returns vocabularies in the list whose name contains the specified string. The search is case-insensitive, ListMedicalVocabularies returns both 'vocabularyname' and 'VocabularyName' in the response list.

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 'PENDING'|'READY'|'FAILED',
    'NextToken': 'string',
    'Vocabularies': [
        {
            'VocabularyName': 'string',
            'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
            'LastModifiedTime': datetime(2015, 1, 1),
            'VocabularyState': 'PENDING'|'READY'|'FAILED'
        },
    ]
}


Response Structure

(dict) --

Status (string) --
The requested vocabulary state.

NextToken (string) --
The ListMedicalVocabularies operation returns a page of vocabularies at a time. The maximum size of the page is set by the MaxResults parameter. If there are more jobs in the list than the page size, Amazon Transcribe Medical returns the NextPage token. Include the token in the next request to the ListMedicalVocabularies operation to return the next page of jobs.

Vocabularies (list) --
A list of objects that describe the vocabularies that match the search criteria in the request.

(dict) --
Provides information about a custom vocabulary.

VocabularyName (string) --
The name of the vocabulary.

LanguageCode (string) --
The language code of the vocabulary entries.

LastModifiedTime (datetime) --
The date and time that the vocabulary was last modified.

VocabularyState (string) --
The processing state of the vocabulary. If the state is READY you can use the vocabulary in a StartTranscriptionJob request.











Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException


    :return: {
        'Status': 'PENDING'|'READY'|'FAILED',
        'NextToken': 'string',
        'Vocabularies': [
            {
                'VocabularyName': 'string',
                'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
                'LastModifiedTime': datetime(2015, 1, 1),
                'VocabularyState': 'PENDING'|'READY'|'FAILED'
            },
        ]
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    
    """
    pass

def list_transcription_jobs(Status=None, JobNameContains=None, NextToken=None, MaxResults=None):
    """
    Lists transcription jobs with the specified status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_transcription_jobs(
        Status='QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
        JobNameContains='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type Status: string
    :param Status: When specified, returns only transcription jobs with the specified status. Jobs are ordered by creation date, with the newest jobs returned first. If you don\xe2\x80\x99t specify a status, Amazon Transcribe returns all transcription jobs ordered by creation date.

    :type JobNameContains: string
    :param JobNameContains: When specified, the jobs returned in the list are limited to jobs whose name contains the specified string.

    :type NextToken: string
    :param NextToken: If the result of the previous request to ListTranscriptionJobs was truncated, include the NextToken to fetch the next set of jobs.

    :type MaxResults: integer
    :param MaxResults: The maximum number of jobs to return in the response. If there are fewer results in the list, this response contains only the actual results.

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
    'NextToken': 'string',
    'TranscriptionJobSummaries': [
        {
            'TranscriptionJobName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'StartTime': datetime(2015, 1, 1),
            'CompletionTime': datetime(2015, 1, 1),
            'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
            'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'FailureReason': 'string',
            'OutputLocationType': 'CUSTOMER_BUCKET'|'SERVICE_BUCKET',
            'ContentRedaction': {
                'RedactionType': 'PII',
                'RedactionOutput': 'redacted'|'redacted_and_unredacted'
            }
        },
    ]
}


Response Structure

(dict) --

Status (string) --
The requested status of the jobs returned.

NextToken (string) --
The ListTranscriptionJobs operation returns a page of jobs at a time. The maximum size of the page is set by the MaxResults parameter. If there are more jobs in the list than the page size, Amazon Transcribe returns the NextPage token. Include the token in the next request to the ListTranscriptionJobs operation to return in the next page of jobs.

TranscriptionJobSummaries (list) --
A list of objects containing summary information for a transcription job.

(dict) --
Provides a summary of information about a transcription job.

TranscriptionJobName (string) --
The name of the transcription job.

CreationTime (datetime) --
A timestamp that shows when the job was created.

StartTime (datetime) --
A timestamp that shows when the job started processing.

CompletionTime (datetime) --
A timestamp that shows when the job was completed.

LanguageCode (string) --
The language code for the input speech.

TranscriptionJobStatus (string) --
The status of the transcription job. When the status is COMPLETED , use the GetTranscriptionJob operation to get the results of the transcription.

FailureReason (string) --
If the TranscriptionJobStatus field is FAILED , a description of the error.

OutputLocationType (string) --
Indicates the location of the output of the transcription job.
If the value is CUSTOMER_BUCKET then the location is the S3 bucket specified in the outputBucketName field when the transcription job was started with the StartTranscriptionJob operation.
If the value is SERVICE_BUCKET then the output is stored by Amazon Transcribe and can be retrieved using the URI in the GetTranscriptionJob response\'s TranscriptFileUri field.

ContentRedaction (dict) --
The content redaction settings of the transcription job.

RedactionType (string) --
Request parameter that defines the entities to be redacted. The only accepted value is PII .

RedactionOutput (string) --
The output transcript file stored in either the default S3 bucket or in a bucket you specify.
When you choose redacted Amazon Transcribe outputs only the redacted transcript.
When you choose redacted_and_unredacted Amazon Transcribe outputs both the redacted and unredacted transcripts.













Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException


    :return: {
        'Status': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
        'NextToken': 'string',
        'TranscriptionJobSummaries': [
            {
                'TranscriptionJobName': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'StartTime': datetime(2015, 1, 1),
                'CompletionTime': datetime(2015, 1, 1),
                'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
                'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
                'FailureReason': 'string',
                'OutputLocationType': 'CUSTOMER_BUCKET'|'SERVICE_BUCKET',
                'ContentRedaction': {
                    'RedactionType': 'PII',
                    'RedactionOutput': 'redacted'|'redacted_and_unredacted'
                }
            },
        ]
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    
    """
    pass

def list_vocabularies(NextToken=None, MaxResults=None, StateEquals=None, NameContains=None):
    """
    Returns a list of vocabularies that match the specified criteria. If no criteria are specified, returns the entire list of vocabularies.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param NameContains: When specified, the vocabularies returned in the list are limited to vocabularies whose name contains the specified string. The search is case-insensitive, ListVocabularies returns both 'vocabularyname' and 'VocabularyName' in the response list.

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 'PENDING'|'READY'|'FAILED',
    'NextToken': 'string',
    'Vocabularies': [
        {
            'VocabularyName': 'string',
            'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
            'LastModifiedTime': datetime(2015, 1, 1),
            'VocabularyState': 'PENDING'|'READY'|'FAILED'
        },
    ]
}


Response Structure

(dict) --

Status (string) --
The requested vocabulary state.

NextToken (string) --
The ListVocabularies operation returns a page of vocabularies at a time. The maximum size of the page is set by the MaxResults parameter. If there are more jobs in the list than the page size, Amazon Transcribe returns the NextPage token. Include the token in the next request to the ListVocabularies operation to return in the next page of jobs.

Vocabularies (list) --
A list of objects that describe the vocabularies that match the search criteria in the request.

(dict) --
Provides information about a custom vocabulary.

VocabularyName (string) --
The name of the vocabulary.

LanguageCode (string) --
The language code of the vocabulary entries.

LastModifiedTime (datetime) --
The date and time that the vocabulary was last modified.

VocabularyState (string) --
The processing state of the vocabulary. If the state is READY you can use the vocabulary in a StartTranscriptionJob request.











Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException


    :return: {
        'Status': 'PENDING'|'READY'|'FAILED',
        'NextToken': 'string',
        'Vocabularies': [
            {
                'VocabularyName': 'string',
                'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
                'LastModifiedTime': datetime(2015, 1, 1),
                'VocabularyState': 'PENDING'|'READY'|'FAILED'
            },
        ]
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    
    """
    pass

def list_vocabulary_filters(NextToken=None, MaxResults=None, NameContains=None):
    """
    Gets information about vocabulary filters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_vocabulary_filters(
        NextToken='string',
        MaxResults=123,
        NameContains='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of the previous request to ListVocabularyFilters was truncated, include the NextToken to fetch the next set of collections.

    :type MaxResults: integer
    :param MaxResults: The maximum number of filters to return in the response. If there are fewer results in the list, this response contains only the actual results.

    :type NameContains: string
    :param NameContains: Filters the response so that it only contains vocabulary filters whose name contains the specified string.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'VocabularyFilters': [
        {
            'VocabularyFilterName': 'string',
            'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
            'LastModifiedTime': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
The ListVocabularyFilters operation returns a page of collections at a time. The maximum size of the page is set by the MaxResults parameter. If there are more jobs in the list than the page size, Amazon Transcribe returns the NextPage token. Include the token in the next request to the ListVocabularyFilters operation to return in the next page of jobs.

VocabularyFilters (list) --
The list of vocabulary filters. It contains at most MaxResults number of filters. If there are more filters, call the ListVocabularyFilters operation again with the NextToken parameter in the request set to the value of the NextToken field in the response.

(dict) --
Provides information about a vocabulary filter.

VocabularyFilterName (string) --
The name of the vocabulary filter. The name must be unique in the account that holds the filter.

LanguageCode (string) --
The language code of the words in the vocabulary filter.

LastModifiedTime (datetime) --
The date and time that the vocabulary was last updated.











Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException


    :return: {
        'NextToken': 'string',
        'VocabularyFilters': [
            {
                'VocabularyFilterName': 'string',
                'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
                'LastModifiedTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    
    """
    pass

def start_medical_transcription_job(MedicalTranscriptionJobName=None, LanguageCode=None, MediaSampleRateHertz=None, MediaFormat=None, Media=None, OutputBucketName=None, OutputEncryptionKMSKeyId=None, Settings=None, Specialty=None, Type=None):
    """
    Start a batch job to transcribe medical speech to text.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_medical_transcription_job(
        MedicalTranscriptionJobName='string',
        LanguageCode='en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        MediaSampleRateHertz=123,
        MediaFormat='mp3'|'mp4'|'wav'|'flac',
        Media={
            'MediaFileUri': 'string'
        },
        OutputBucketName='string',
        OutputEncryptionKMSKeyId='string',
        Settings={
            'ShowSpeakerLabels': True|False,
            'MaxSpeakerLabels': 123,
            'ChannelIdentification': True|False,
            'ShowAlternatives': True|False,
            'MaxAlternatives': 123,
            'VocabularyName': 'string'
        },
        Specialty='PRIMARYCARE',
        Type='CONVERSATION'|'DICTATION'
    )
    
    
    :type MedicalTranscriptionJobName: string
    :param MedicalTranscriptionJobName: [REQUIRED]\nThe name of the medical transcription job. You can\'t use the strings '.' or '..' by themselves as the job name. The name must also be unique within an AWS account. If you try to create a medical transcription job with the same name as a previous medical transcription job you will receive a ConflictException error.\n

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language code for the language spoken in the input media file. US English (en-US) is the valid value for medical transcription jobs. Any other value you enter for language code results in a BadRequestException error.\n

    :type MediaSampleRateHertz: integer
    :param MediaSampleRateHertz: The sample rate, in Hertz, of the audio track in the input media file.\nIf you do not specify the media sample rate, Amazon Transcribe Medical determines the sample rate. If you specify the sample rate, it must match the rate detected by Amazon Transcribe Medical. In most cases, you should leave the MediaSampleRateHertz field blank and let Amazon Transcribe Medical determine the sample rate.\n

    :type MediaFormat: string
    :param MediaFormat: The audio format of the input media file.

    :type Media: dict
    :param Media: [REQUIRED]\nDescribes the input media file in a transcription request.\n\nMediaFileUri (string) --The S3 object location of the input media file. The URI must be in the same region as the API endpoint that you are calling. The general form is:\nFor example:\nFor more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .\n\n\n

    :type OutputBucketName: string
    :param OutputBucketName: [REQUIRED]\nThe Amazon S3 location where the transcription is stored.\nYou must set OutputBucketName for Amazon Transcribe Medical to store the transcription results. Your transcript appears in the S3 location you specify. When you call the GetMedicalTranscriptionJob , the operation returns this location in the TranscriptFileUri field. The S3 bucket must have permissions that allow Amazon Transcribe Medical to put files in the bucket. For more information, see Permissions Required for IAM User Roles .\nYou can specify an AWS Key Management Service (KMS) key to encrypt the output of your transcription using the OutputEncryptionKMSKeyId parameter. If you don\'t specify a KMS key, Amazon Transcribe Medical uses the default Amazon S3 key for server-side encryption of transcripts that are placed in your S3 bucket.\n

    :type OutputEncryptionKMSKeyId: string
    :param OutputEncryptionKMSKeyId: The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt the output of the transcription job. The user calling the StartMedicalTranscriptionJob operation must have permission to use the specified KMS key.\nYou use either of the following to identify a KMS key in the current account:\n\nKMS Key ID: '1234abcd-12ab-34cd-56ef-1234567890ab'\nKMS Key Alias: 'alias/ExampleAlias'\n\nYou can use either of the following to identify a KMS key in the current account or another account:\n\nAmazon Resource Name (ARN) of a KMS key in the current account or another account: 'arn:aws:kms:region:account ID:key/1234abcd-12ab-34cd-56ef-1234567890ab'\nARN of a KMS Key Alias: 'arn:aws:kms:region:account ID:alias/ExampleAlias'\n\nIf you don\'t specify an encryption key, the output of the medical transcription job is encrypted with the default Amazon S3 key (SSE-S3).\nIf you specify a KMS key to encrypt your output, you must also specify an output location in the OutputBucketName parameter.\n

    :type Settings: dict
    :param Settings: Optional settings for the medical transcription job.\n\nShowSpeakerLabels (boolean) --Determines whether the transcription job uses speaker recognition to identify different speakers in the input audio. Speaker recongition labels individual speakers in the audio file. If you set the ShowSpeakerLabels field to true, you must also set the maximum number of speaker labels in the MaxSpeakerLabels field.\nYou can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException .\n\nMaxSpeakerLabels (integer) --The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers are identified as a single speaker. If you specify the MaxSpeakerLabels field, you must set the ShowSpeakerLabels field to true.\n\nChannelIdentification (boolean) --Instructs Amazon Transcribe Medical to process each audio channel separately and then merge the transcription output of each channel into a single transcription.\nAmazon Transcribe Medical also produces a transcription of each item detected on an audio channel, including the start time and end time of the item and alternative transcriptions of item. The alternative transcriptions also come with confidence scores provided by Amazon Transcribe Medical.\nYou can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException\n\nShowAlternatives (boolean) --Determines whether alternative transcripts are generated along with the transcript that has the highest confidence. If you set ShowAlternatives field to true, you must also set the maximum number of alternatives to return in the MaxAlternatives field.\n\nMaxAlternatives (integer) --The maximum number of alternatives that you tell the service to return. If you specify the MaxAlternatives field, you must set the ShowAlternatives field to true.\n\nVocabularyName (string) --The name of the vocabulary to use when processing a medical transcription job.\n\n\n

    :type Specialty: string
    :param Specialty: [REQUIRED]\nThe medical specialty of any clinician speaking in the input media.\n

    :type Type: string
    :param Type: [REQUIRED]\nThe type of speech in the input audio. CONVERSATION refers to conversations between two or more speakers, e.g., a conversations between doctors and patients. DICTATION refers to single-speaker dictated speech, e.g., for clinical notes.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'MedicalTranscriptionJob': {
        'MedicalTranscriptionJobName': 'string',
        'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'MediaSampleRateHertz': 123,
        'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
        'Media': {
            'MediaFileUri': 'string'
        },
        'Transcript': {
            'TranscriptFileUri': 'string'
        },
        'StartTime': datetime(2015, 1, 1),
        'CreationTime': datetime(2015, 1, 1),
        'CompletionTime': datetime(2015, 1, 1),
        'FailureReason': 'string',
        'Settings': {
            'ShowSpeakerLabels': True|False,
            'MaxSpeakerLabels': 123,
            'ChannelIdentification': True|False,
            'ShowAlternatives': True|False,
            'MaxAlternatives': 123,
            'VocabularyName': 'string'
        },
        'Specialty': 'PRIMARYCARE',
        'Type': 'CONVERSATION'|'DICTATION'
    }
}


Response Structure

(dict) --

MedicalTranscriptionJob (dict) --
A batch job submitted to transcribe medical speech to text.

MedicalTranscriptionJobName (string) --
The name for a given medical transcription job.

TranscriptionJobStatus (string) --
The completion status of a medical transcription job.

LanguageCode (string) --
The language code for the language spoken in the source audio file. US English (en-US) is the only supported language for medical transcriptions. Any other value you enter for language code results in a BadRequestException error.

MediaSampleRateHertz (integer) --
The sample rate, in Hertz, of the source audio containing medical information.
If you don\'t specify the sample rate, Amazon Transcribe Medical determines it for you. If you choose to specify the sample rate, it must match the rate detected by Amazon Transcribe Medical. In most cases, you should leave the MediaSampleHertz blank and let Amazon Transcribe Medical determine the sample rate.

MediaFormat (string) --
The format of the input media file.

Media (dict) --
Describes the input media file in a transcription request.

MediaFileUri (string) --
The S3 object location of the input media file. The URI must be in the same region as the API endpoint that you are calling. The general form is:
For example:
For more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .



Transcript (dict) --
An object that contains the MedicalTranscript . The MedicalTranscript contains the TranscriptFileUri .

TranscriptFileUri (string) --
The S3 object location of the medical transcript.
Use this URI to access the medical transcript. This URI points to the S3 bucket you created to store the medical transcript.



StartTime (datetime) --
A timestamp that shows when the job started processing.

CreationTime (datetime) --
A timestamp that shows when the job was created.

CompletionTime (datetime) --
A timestamp that shows when the job was completed.

FailureReason (string) --
If the TranscriptionJobStatus field is FAILED , this field contains information about why the job failed.
The FailureReason field contains one of the following values:

Unsupported media format - The media format specified in the MediaFormat field of the request isn\'t valid. See the description of the MediaFormat field for a list of valid values.
The media format provided does not match the detected media format - The media format of the audio file doesn\'t match the format specified in the MediaFormat field in the request. Check the media format of your media file and make sure the two values match.
Invalid sample rate for audio file - The sample rate specified in the MediaSampleRateHertz of the request isn\'t valid. The sample rate must be between 8000 and 48000 Hertz.
The sample rate provided does not match the detected sample rate - The sample rate in the audio file doesn\'t match the sample rate specified in the MediaSampleRateHertz field in the request. Check the sample rate of your media file and make sure that the two values match.
Invalid file size: file size too large - The size of your audio file is larger than what Amazon Transcribe Medical can process. For more information, see Guidlines and Quotas in the Amazon Transcribe Medical Guide
Invalid number of channels: number of channels too large - Your audio contains more channels than Amazon Transcribe Medical is configured to process. To request additional channels, see Amazon Transcribe Medical Endpoints and Quotas in the Amazon Web Services General Reference


Settings (dict) --
Object that contains object.

ShowSpeakerLabels (boolean) --
Determines whether the transcription job uses speaker recognition to identify different speakers in the input audio. Speaker recongition labels individual speakers in the audio file. If you set the ShowSpeakerLabels field to true, you must also set the maximum number of speaker labels in the MaxSpeakerLabels field.
You can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException .

MaxSpeakerLabels (integer) --
The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers are identified as a single speaker. If you specify the MaxSpeakerLabels field, you must set the ShowSpeakerLabels field to true.

ChannelIdentification (boolean) --
Instructs Amazon Transcribe Medical to process each audio channel separately and then merge the transcription output of each channel into a single transcription.
Amazon Transcribe Medical also produces a transcription of each item detected on an audio channel, including the start time and end time of the item and alternative transcriptions of item. The alternative transcriptions also come with confidence scores provided by Amazon Transcribe Medical.
You can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException

ShowAlternatives (boolean) --
Determines whether alternative transcripts are generated along with the transcript that has the highest confidence. If you set ShowAlternatives field to true, you must also set the maximum number of alternatives to return in the MaxAlternatives field.

MaxAlternatives (integer) --
The maximum number of alternatives that you tell the service to return. If you specify the MaxAlternatives field, you must set the ShowAlternatives field to true.

VocabularyName (string) --
The name of the vocabulary to use when processing a medical transcription job.



Specialty (string) --
The medical specialty of any clinicians providing a dictation or having a conversation. PRIMARYCARE is the only available setting for this object. This specialty enables you to generate transcriptions for the following medical fields:

Family Medicine


Type (string) --
The type of speech in the transcription job. CONVERSATION is generally used for patient-physician dialogues. DICTATION is the setting for physicians speaking their notes after seeing a patient. For more information, see  how-it-works-med









Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.ConflictException


    :return: {
        'MedicalTranscriptionJob': {
            'MedicalTranscriptionJobName': 'string',
            'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
            'MediaSampleRateHertz': 123,
            'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
            'Media': {
                'MediaFileUri': 'string'
            },
            'Transcript': {
                'TranscriptFileUri': 'string'
            },
            'StartTime': datetime(2015, 1, 1),
            'CreationTime': datetime(2015, 1, 1),
            'CompletionTime': datetime(2015, 1, 1),
            'FailureReason': 'string',
            'Settings': {
                'ShowSpeakerLabels': True|False,
                'MaxSpeakerLabels': 123,
                'ChannelIdentification': True|False,
                'ShowAlternatives': True|False,
                'MaxAlternatives': 123,
                'VocabularyName': 'string'
            },
            'Specialty': 'PRIMARYCARE',
            'Type': 'CONVERSATION'|'DICTATION'
        }
    }
    
    
    :returns: 
    Unsupported media format - The media format specified in the MediaFormat field of the request isn\'t valid. See the description of the MediaFormat field for a list of valid values.
    The media format provided does not match the detected media format - The media format of the audio file doesn\'t match the format specified in the MediaFormat field in the request. Check the media format of your media file and make sure the two values match.
    Invalid sample rate for audio file - The sample rate specified in the MediaSampleRateHertz of the request isn\'t valid. The sample rate must be between 8000 and 48000 Hertz.
    The sample rate provided does not match the detected sample rate - The sample rate in the audio file doesn\'t match the sample rate specified in the MediaSampleRateHertz field in the request. Check the sample rate of your media file and make sure that the two values match.
    Invalid file size: file size too large - The size of your audio file is larger than what Amazon Transcribe Medical can process. For more information, see Guidlines and Quotas in the Amazon Transcribe Medical Guide
    Invalid number of channels: number of channels too large - Your audio contains more channels than Amazon Transcribe Medical is configured to process. To request additional channels, see Amazon Transcribe Medical Endpoints and Quotas in the Amazon Web Services General Reference
    
    """
    pass

def start_transcription_job(TranscriptionJobName=None, LanguageCode=None, MediaSampleRateHertz=None, MediaFormat=None, Media=None, OutputBucketName=None, OutputEncryptionKMSKeyId=None, Settings=None, JobExecutionSettings=None, ContentRedaction=None):
    """
    Starts an asynchronous job to transcribe speech to text.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_transcription_job(
        TranscriptionJobName='string',
        LanguageCode='en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        MediaSampleRateHertz=123,
        MediaFormat='mp3'|'mp4'|'wav'|'flac',
        Media={
            'MediaFileUri': 'string'
        },
        OutputBucketName='string',
        OutputEncryptionKMSKeyId='string',
        Settings={
            'VocabularyName': 'string',
            'ShowSpeakerLabels': True|False,
            'MaxSpeakerLabels': 123,
            'ChannelIdentification': True|False,
            'ShowAlternatives': True|False,
            'MaxAlternatives': 123,
            'VocabularyFilterName': 'string',
            'VocabularyFilterMethod': 'remove'|'mask'
        },
        JobExecutionSettings={
            'AllowDeferredExecution': True|False,
            'DataAccessRoleArn': 'string'
        },
        ContentRedaction={
            'RedactionType': 'PII',
            'RedactionOutput': 'redacted'|'redacted_and_unredacted'
        }
    )
    
    
    :type TranscriptionJobName: string
    :param TranscriptionJobName: [REQUIRED]\nThe name of the job. Note that you can\'t use the strings '.' or '..' by themselves as the job name. The name must also be unique within an AWS account. If you try to create a transcription job with the same name as a previous transcription job you will receive a ConflictException error.\n

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language code for the language used in the input media file.\n

    :type MediaSampleRateHertz: integer
    :param MediaSampleRateHertz: The sample rate, in Hertz, of the audio track in the input media file.\nIf you do not specify the media sample rate, Amazon Transcribe determines the sample rate. If you specify the sample rate, it must match the sample rate detected by Amazon Transcribe. In most cases, you should leave the MediaSampleRateHertz field blank and let Amazon Transcribe determine the sample rate.\n

    :type MediaFormat: string
    :param MediaFormat: The format of the input media file.

    :type Media: dict
    :param Media: [REQUIRED]\nAn object that describes the input media for a transcription job.\n\nMediaFileUri (string) --The S3 object location of the input media file. The URI must be in the same region as the API endpoint that you are calling. The general form is:\nFor example:\nFor more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .\n\n\n

    :type OutputBucketName: string
    :param OutputBucketName: The location where the transcription is stored.\nIf you set the OutputBucketName , Amazon Transcribe puts the transcript in the specified S3 bucket. When you call the GetTranscriptionJob operation, the operation returns this location in the TranscriptFileUri field. If you enable content redaction, the redacted transcript appears in RedactedTranscriptFileUri . If you enable content redaction and choose to output an unredacted transcript, that transcript\'s location still appears in the TranscriptFileUri . The S3 bucket must have permissions that allow Amazon Transcribe to put files in the bucket. For more information, see Permissions Required for IAM User Roles .\nYou can specify an AWS Key Management Service (KMS) key to encrypt the output of your transcription using the OutputEncryptionKMSKeyId parameter. If you don\'t specify a KMS key, Amazon Transcribe uses the default Amazon S3 key for server-side encryption of transcripts that are placed in your S3 bucket.\nIf you don\'t set the OutputBucketName , Amazon Transcribe generates a pre-signed URL, a shareable URL that provides secure access to your transcription, and returns it in the TranscriptFileUri field. Use this URL to download the transcription.\n

    :type OutputEncryptionKMSKeyId: string
    :param OutputEncryptionKMSKeyId: The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt the output of the transcription job. The user calling the StartTranscriptionJob operation must have permission to use the specified KMS key.\nYou can use either of the following to identify a KMS key in the current account:\n\nKMS Key ID: '1234abcd-12ab-34cd-56ef-1234567890ab'\nKMS Key Alias: 'alias/ExampleAlias'\n\nYou can use either of the following to identify a KMS key in the current account or another account:\n\nAmazon Resource Name (ARN) of a KMS Key: 'arn:aws:kms:region:account ID:key/1234abcd-12ab-34cd-56ef-1234567890ab'\nARN of a KMS Key Alias: 'arn:aws:kms:region:account ID:alias/ExampleAlias'\n\nIf you don\'t specify an encryption key, the output of the transcription job is encrypted with the default Amazon S3 key (SSE-S3).\nIf you specify a KMS key to encrypt your output, you must also specify an output location in the OutputBucketName parameter.\n

    :type Settings: dict
    :param Settings: A Settings object that provides optional settings for a transcription job.\n\nVocabularyName (string) --The name of a vocabulary to use when processing the transcription job.\n\nShowSpeakerLabels (boolean) --Determines whether the transcription job uses speaker recognition to identify different speakers in the input audio. Speaker recognition labels individual speakers in the audio file. If you set the ShowSpeakerLabels field to true, you must also set the maximum number of speaker labels MaxSpeakerLabels field.\nYou can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException .\n\nMaxSpeakerLabels (integer) --The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers are identified as a single speaker. If you specify the MaxSpeakerLabels field, you must set the ShowSpeakerLabels field to true.\n\nChannelIdentification (boolean) --Instructs Amazon Transcribe to process each audio channel separately and then merge the transcription output of each channel into a single transcription.\nAmazon Transcribe also produces a transcription of each item detected on an audio channel, including the start time and end time of the item and alternative transcriptions of the item including the confidence that Amazon Transcribe has in the transcription.\nYou can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException .\n\nShowAlternatives (boolean) --Determines whether the transcription contains alternative transcriptions. If you set the ShowAlternatives field to true, you must also set the maximum number of alternatives to return in the MaxAlternatives field.\n\nMaxAlternatives (integer) --The number of alternative transcriptions that the service should return. If you specify the MaxAlternatives field, you must set the ShowAlternatives field to true.\n\nVocabularyFilterName (string) --The name of the vocabulary filter to use when transcribing the audio. The filter that you specify must have the same language code as the transcription job.\n\nVocabularyFilterMethod (string) --Set to mask to remove filtered text from the transcript and replace it with three asterisks ('***') as placeholder text. Set to remove to remove filtered text from the transcript without using placeholder text.\n\n\n

    :type JobExecutionSettings: dict
    :param JobExecutionSettings: Provides information about how a transcription job is executed. Use this field to indicate that the job can be queued for deferred execution if the concurrency limit is reached and there are no slots available to immediately run the job.\n\nAllowDeferredExecution (boolean) --Indicates whether a job should be queued by Amazon Transcribe when the concurrent execution limit is exceeded. When the AllowDeferredExecution field is true, jobs are queued and executed when the number of executing jobs falls below the concurrent execution limit. If the field is false, Amazon Transcribe returns a LimitExceededException exception.\nIf you specify the AllowDeferredExecution field, you must specify the DataAccessRoleArn field.\n\nDataAccessRoleArn (string) --The Amazon Resource Name (ARN) of a role that has access to the S3 bucket that contains the input files. Amazon Transcribe assumes this role to read queued media files. If you have specified an output S3 bucket for the transcription results, this role should have access to the output bucket as well.\nIf you specify the AllowDeferredExecution field, you must specify the DataAccessRoleArn field.\n\n\n

    :type ContentRedaction: dict
    :param ContentRedaction: An object that contains the request parameters for content redaction.\n\nRedactionType (string) -- [REQUIRED]Request parameter that defines the entities to be redacted. The only accepted value is PII .\n\nRedactionOutput (string) -- [REQUIRED]The output transcript file stored in either the default S3 bucket or in a bucket you specify.\nWhen you choose redacted Amazon Transcribe outputs only the redacted transcript.\nWhen you choose redacted_and_unredacted Amazon Transcribe outputs both the redacted and unredacted transcripts.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'TranscriptionJob': {
        'TranscriptionJobName': 'string',
        'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'MediaSampleRateHertz': 123,
        'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
        'Media': {
            'MediaFileUri': 'string'
        },
        'Transcript': {
            'TranscriptFileUri': 'string',
            'RedactedTranscriptFileUri': 'string'
        },
        'StartTime': datetime(2015, 1, 1),
        'CreationTime': datetime(2015, 1, 1),
        'CompletionTime': datetime(2015, 1, 1),
        'FailureReason': 'string',
        'Settings': {
            'VocabularyName': 'string',
            'ShowSpeakerLabels': True|False,
            'MaxSpeakerLabels': 123,
            'ChannelIdentification': True|False,
            'ShowAlternatives': True|False,
            'MaxAlternatives': 123,
            'VocabularyFilterName': 'string',
            'VocabularyFilterMethod': 'remove'|'mask'
        },
        'JobExecutionSettings': {
            'AllowDeferredExecution': True|False,
            'DataAccessRoleArn': 'string'
        },
        'ContentRedaction': {
            'RedactionType': 'PII',
            'RedactionOutput': 'redacted'|'redacted_and_unredacted'
        }
    }
}


Response Structure

(dict) --

TranscriptionJob (dict) --
An object containing details of the asynchronous transcription job.

TranscriptionJobName (string) --
The name of the transcription job.

TranscriptionJobStatus (string) --
The status of the transcription job.

LanguageCode (string) --
The language code for the input speech.

MediaSampleRateHertz (integer) --
The sample rate, in Hertz, of the audio track in the input media file.

MediaFormat (string) --
The format of the input media file.

Media (dict) --
An object that describes the input media for the transcription job.

MediaFileUri (string) --
The S3 object location of the input media file. The URI must be in the same region as the API endpoint that you are calling. The general form is:
For example:
For more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .



Transcript (dict) --
An object that describes the output of the transcription job.

TranscriptFileUri (string) --
The S3 object location of the the transcript.
Use this URI to access the transcript. If you specified an S3 bucket in the OutputBucketName field when you created the job, this is the URI of that bucket. If you chose to store the transcript in Amazon Transcribe, this is a shareable URL that provides secure access to that location.

RedactedTranscriptFileUri (string) --
The S3 object location of the redacted transcript.
Use this URI to access the redacated transcript. If you specified an S3 bucket in the OutputBucketName field when you created the job, this is the URI of that bucket. If you chose to store the transcript in Amazon Transcribe, this is a shareable URL that provides secure access to that location.



StartTime (datetime) --
A timestamp that shows with the job was started processing.

CreationTime (datetime) --
A timestamp that shows when the job was created.

CompletionTime (datetime) --
A timestamp that shows when the job was completed.

FailureReason (string) --
If the TranscriptionJobStatus field is FAILED , this field contains information about why the job failed.
The FailureReason field can contain one of the following values:

Unsupported media format - The media format specified in the MediaFormat field of the request isn\'t valid. See the description of the MediaFormat field for a list of valid values.
The media format provided does not match the detected media format - The media format of the audio file doesn\'t match the format specified in the MediaFormat field in the request. Check the media format of your media file and make sure that the two values match.
Invalid sample rate for audio file - The sample rate specified in the MediaSampleRateHertz of the request isn\'t valid. The sample rate must be between 8000 and 48000 Hertz.
The sample rate provided does not match the detected sample rate - The sample rate in the audio file doesn\'t match the sample rate specified in the MediaSampleRateHertz field in the request. Check the sample rate of your media file and make sure that the two values match.
Invalid file size: file size too large - The size of your audio file is larger than Amazon Transcribe can process. For more information, see Limits in the Amazon Transcribe Developer Guide .
Invalid number of channels: number of channels too large - Your audio contains more channels than Amazon Transcribe is configured to process. To request additional channels, see Amazon Transcribe Limits in the Amazon Web Services General Reference .


Settings (dict) --
Optional settings for the transcription job. Use these settings to turn on speaker recognition, to set the maximum number of speakers that should be identified and to specify a custom vocabulary to use when processing the transcription job.

VocabularyName (string) --
The name of a vocabulary to use when processing the transcription job.

ShowSpeakerLabels (boolean) --
Determines whether the transcription job uses speaker recognition to identify different speakers in the input audio. Speaker recognition labels individual speakers in the audio file. If you set the ShowSpeakerLabels field to true, you must also set the maximum number of speaker labels MaxSpeakerLabels field.
You can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException .

MaxSpeakerLabels (integer) --
The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers are identified as a single speaker. If you specify the MaxSpeakerLabels field, you must set the ShowSpeakerLabels field to true.

ChannelIdentification (boolean) --
Instructs Amazon Transcribe to process each audio channel separately and then merge the transcription output of each channel into a single transcription.
Amazon Transcribe also produces a transcription of each item detected on an audio channel, including the start time and end time of the item and alternative transcriptions of the item including the confidence that Amazon Transcribe has in the transcription.
You can\'t set both ShowSpeakerLabels and ChannelIdentification in the same request. If you set both, your request returns a BadRequestException .

ShowAlternatives (boolean) --
Determines whether the transcription contains alternative transcriptions. If you set the ShowAlternatives field to true, you must also set the maximum number of alternatives to return in the MaxAlternatives field.

MaxAlternatives (integer) --
The number of alternative transcriptions that the service should return. If you specify the MaxAlternatives field, you must set the ShowAlternatives field to true.

VocabularyFilterName (string) --
The name of the vocabulary filter to use when transcribing the audio. The filter that you specify must have the same language code as the transcription job.

VocabularyFilterMethod (string) --
Set to mask to remove filtered text from the transcript and replace it with three asterisks ("***") as placeholder text. Set to remove to remove filtered text from the transcript without using placeholder text.



JobExecutionSettings (dict) --
Provides information about how a transcription job is executed.

AllowDeferredExecution (boolean) --
Indicates whether a job should be queued by Amazon Transcribe when the concurrent execution limit is exceeded. When the AllowDeferredExecution field is true, jobs are queued and executed when the number of executing jobs falls below the concurrent execution limit. If the field is false, Amazon Transcribe returns a LimitExceededException exception.
If you specify the AllowDeferredExecution field, you must specify the DataAccessRoleArn field.

DataAccessRoleArn (string) --
The Amazon Resource Name (ARN) of a role that has access to the S3 bucket that contains the input files. Amazon Transcribe assumes this role to read queued media files. If you have specified an output S3 bucket for the transcription results, this role should have access to the output bucket as well.
If you specify the AllowDeferredExecution field, you must specify the DataAccessRoleArn field.



ContentRedaction (dict) --
An object that describes content redaction settings for the transcription job.

RedactionType (string) --
Request parameter that defines the entities to be redacted. The only accepted value is PII .

RedactionOutput (string) --
The output transcript file stored in either the default S3 bucket or in a bucket you specify.
When you choose redacted Amazon Transcribe outputs only the redacted transcript.
When you choose redacted_and_unredacted Amazon Transcribe outputs both the redacted and unredacted transcripts.











Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.ConflictException


    :return: {
        'TranscriptionJob': {
            'TranscriptionJobName': 'string',
            'TranscriptionJobStatus': 'QUEUED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
            'MediaSampleRateHertz': 123,
            'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
            'Media': {
                'MediaFileUri': 'string'
            },
            'Transcript': {
                'TranscriptFileUri': 'string',
                'RedactedTranscriptFileUri': 'string'
            },
            'StartTime': datetime(2015, 1, 1),
            'CreationTime': datetime(2015, 1, 1),
            'CompletionTime': datetime(2015, 1, 1),
            'FailureReason': 'string',
            'Settings': {
                'VocabularyName': 'string',
                'ShowSpeakerLabels': True|False,
                'MaxSpeakerLabels': 123,
                'ChannelIdentification': True|False,
                'ShowAlternatives': True|False,
                'MaxAlternatives': 123,
                'VocabularyFilterName': 'string',
                'VocabularyFilterMethod': 'remove'|'mask'
            },
            'JobExecutionSettings': {
                'AllowDeferredExecution': True|False,
                'DataAccessRoleArn': 'string'
            },
            'ContentRedaction': {
                'RedactionType': 'PII',
                'RedactionOutput': 'redacted'|'redacted_and_unredacted'
            }
        }
    }
    
    
    :returns: 
    Unsupported media format - The media format specified in the MediaFormat field of the request isn\'t valid. See the description of the MediaFormat field for a list of valid values.
    The media format provided does not match the detected media format - The media format of the audio file doesn\'t match the format specified in the MediaFormat field in the request. Check the media format of your media file and make sure that the two values match.
    Invalid sample rate for audio file - The sample rate specified in the MediaSampleRateHertz of the request isn\'t valid. The sample rate must be between 8000 and 48000 Hertz.
    The sample rate provided does not match the detected sample rate - The sample rate in the audio file doesn\'t match the sample rate specified in the MediaSampleRateHertz field in the request. Check the sample rate of your media file and make sure that the two values match.
    Invalid file size: file size too large - The size of your audio file is larger than Amazon Transcribe can process. For more information, see Limits in the Amazon Transcribe Developer Guide .
    Invalid number of channels: number of channels too large - Your audio contains more channels than Amazon Transcribe is configured to process. To request additional channels, see Amazon Transcribe Limits in the Amazon Web Services General Reference .
    
    """
    pass

def update_medical_vocabulary(VocabularyName=None, LanguageCode=None, VocabularyFileUri=None):
    """
    Updates an existing vocabulary with new values in a different text file. The UpdateMedicalVocabulary operation overwrites all of the existing information with the values that you provide in the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_medical_vocabulary(
        VocabularyName='string',
        LanguageCode='en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        VocabularyFileUri='string'
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]\nThe name of the vocabulary to update. The name is case-sensitive. If you try to update a vocabulary with the same name as a previous vocabulary you will receive a ConflictException error.\n

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language code of the entries in the updated vocabulary. US English (en-US) is the only valid language code in Amazon Transcribe Medical.\n

    :type VocabularyFileUri: string
    :param VocabularyFileUri: The Amazon S3 location of the text file containing the definition of the custom vocabulary. The URI must be in the same AWS region as the API endpoint you are calling. You can see the fields you need to enter for you Amazon S3 location in the example URI here:\n\nhttps://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>\nFor example:\n\nhttps://s3.us-east-1.amazonaws.com/AWSDOC-EXAMPLE-BUCKET/vocab.txt\nFor more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .\nFor more information about custom vocabularies in Amazon Transcribe Medical, see Medical Custom Vocabularies .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VocabularyName': 'string',
    'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
    'LastModifiedTime': datetime(2015, 1, 1),
    'VocabularyState': 'PENDING'|'READY'|'FAILED'
}


Response Structure

(dict) --

VocabularyName (string) --
The name of the updated vocabulary.

LanguageCode (string) --
The language code for the text file used to update the custom vocabulary. US English (en-US) is the only language supported in Amazon Transcribe Medical.

LastModifiedTime (datetime) --
The date and time the vocabulary was updated.

VocabularyState (string) --
The processing state of the update to the vocabulary. When the VocabularyState field is READY the vocabulary is ready to be used in a StartMedicalTranscriptionJob request.







Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.NotFoundException
TranscribeService.Client.exceptions.ConflictException


    :return: {
        'VocabularyName': 'string',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'LastModifiedTime': datetime(2015, 1, 1),
        'VocabularyState': 'PENDING'|'READY'|'FAILED'
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    TranscribeService.Client.exceptions.NotFoundException
    TranscribeService.Client.exceptions.ConflictException
    
    """
    pass

def update_vocabulary(VocabularyName=None, LanguageCode=None, Phrases=None, VocabularyFileUri=None):
    """
    Updates an existing vocabulary with new values. The UpdateVocabulary operation overwrites all of the existing information with the values that you provide in the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_vocabulary(
        VocabularyName='string',
        LanguageCode='en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        Phrases=[
            'string',
        ],
        VocabularyFileUri='string'
    )
    
    
    :type VocabularyName: string
    :param VocabularyName: [REQUIRED]\nThe name of the vocabulary to update. The name is case-sensitive. If you try to update a vocabulary with the same name as a previous vocabulary you will receive a ConflictException error.\n

    :type LanguageCode: string
    :param LanguageCode: [REQUIRED]\nThe language code of the vocabulary entries.\n

    :type Phrases: list
    :param Phrases: An array of strings containing the vocabulary entries.\n\n(string) --\n\n

    :type VocabularyFileUri: string
    :param VocabularyFileUri: The S3 location of the text file that contains the definition of the custom vocabulary. The URI must be in the same region as the API endpoint that you are calling. The general form is\nFor example:\nFor more information about S3 object names, see Object Keys in the Amazon S3 Developer Guide .\nFor more information about custom vocabularies, see Custom Vocabularies .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VocabularyName': 'string',
    'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
    'LastModifiedTime': datetime(2015, 1, 1),
    'VocabularyState': 'PENDING'|'READY'|'FAILED'
}


Response Structure

(dict) --

VocabularyName (string) --
The name of the vocabulary that was updated.

LanguageCode (string) --
The language code of the vocabulary entries.

LastModifiedTime (datetime) --
The date and time that the vocabulary was updated.

VocabularyState (string) --
The processing state of the vocabulary. When the VocabularyState field contains READY the vocabulary is ready to be used in a StartTranscriptionJob request.







Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.NotFoundException
TranscribeService.Client.exceptions.ConflictException


    :return: {
        'VocabularyName': 'string',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'LastModifiedTime': datetime(2015, 1, 1),
        'VocabularyState': 'PENDING'|'READY'|'FAILED'
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    TranscribeService.Client.exceptions.NotFoundException
    TranscribeService.Client.exceptions.ConflictException
    
    """
    pass

def update_vocabulary_filter(VocabularyFilterName=None, Words=None, VocabularyFilterFileUri=None):
    """
    Updates a vocabulary filter with a new list of filtered words.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_vocabulary_filter(
        VocabularyFilterName='string',
        Words=[
            'string',
        ],
        VocabularyFilterFileUri='string'
    )
    
    
    :type VocabularyFilterName: string
    :param VocabularyFilterName: [REQUIRED]\nThe name of the vocabulary filter to update. If you try to update a vocabulary filter with the same name as a previous vocabulary filter you will receive a ConflictException error.\n

    :type Words: list
    :param Words: The words to use in the vocabulary filter. Only use characters from the character set defined for custom vocabularies. For a list of character sets, see Character Sets for Custom Vocabularies .\nIf you provide a list of words in the Words parameter, you can\'t use the VocabularyFilterFileUri parameter.\n\n(string) --\n\n

    :type VocabularyFilterFileUri: string
    :param VocabularyFilterFileUri: The Amazon S3 location of a text file used as input to create the vocabulary filter. Only use characters from the character set defined for custom vocabularies. For a list of character sets, see Character Sets for Custom Vocabularies .\nThe specified file must be less than 50 KB of UTF-8 characters.\nIf you provide the location of a list of words in the VocabularyFilterFileUri parameter, you can\'t use the Words parameter.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VocabularyFilterName': 'string',
    'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
    'LastModifiedTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --

VocabularyFilterName (string) --
The name of the updated vocabulary filter.

LanguageCode (string) --
The language code of the words in the vocabulary filter.

LastModifiedTime (datetime) --
The date and time that the vocabulary filter was updated.







Exceptions

TranscribeService.Client.exceptions.BadRequestException
TranscribeService.Client.exceptions.LimitExceededException
TranscribeService.Client.exceptions.InternalFailureException
TranscribeService.Client.exceptions.NotFoundException


    :return: {
        'VocabularyFilterName': 'string',
        'LanguageCode': 'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
        'LastModifiedTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    TranscribeService.Client.exceptions.BadRequestException
    TranscribeService.Client.exceptions.LimitExceededException
    TranscribeService.Client.exceptions.InternalFailureException
    TranscribeService.Client.exceptions.NotFoundException
    
    """
    pass

