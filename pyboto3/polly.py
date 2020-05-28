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

def delete_lexicon(Name=None):
    """
    Deletes the specified pronunciation lexicon stored in an AWS Region. A lexicon which has been deleted is not available for speech synthesis, nor is it possible to retrieve it using either the GetLexicon or ListLexicon APIs.
    For more information, see Managing Lexicons .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Deletes a specified pronunciation lexicon stored in an AWS Region.
    Expected Output:
    
    :example: response = client.delete_lexicon(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the lexicon to delete. Must be an existing lexicon in the region.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Polly.Client.exceptions.LexiconNotFoundException
Polly.Client.exceptions.ServiceFailureException

Examples
Deletes a specified pronunciation lexicon stored in an AWS Region.
response = client.delete_lexicon(
    Name='example',
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
    Polly.Client.exceptions.LexiconNotFoundException
    Polly.Client.exceptions.ServiceFailureException
    
    """
    pass

def describe_voices(Engine=None, LanguageCode=None, IncludeAdditionalLanguageCodes=None, NextToken=None):
    """
    Returns the list of voices that are available for use when requesting speech synthesis. Each voice speaks a specified language, is either male or female, and is identified by an ID, which is the ASCII version of the voice name.
    When synthesizing speech ( SynthesizeSpeech ), you provide the voice ID for the voice you want from the list of voices returned by DescribeVoices .
    For example, you want your news reader application to read news in a specific language, but giving a user the option to choose the voice. Using the DescribeVoices operation you can provide the user with a list of available voices to select from.
    You can optionally specify a language code to filter the available voices. For example, if you specify en-US , the operation returns a list of all available US English voices.
    This operation requires permissions to perform the polly:DescribeVoices action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns the list of voices that are available for use when requesting speech synthesis. Displayed languages are those within the specified language code. If no language code is specified, voices for all available languages are displayed.
    Expected Output:
    
    :example: response = client.describe_voices(
        Engine='standard'|'neural',
        LanguageCode='arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
        IncludeAdditionalLanguageCodes=True|False,
        NextToken='string'
    )
    
    
    :type Engine: string
    :param Engine: Specifies the engine (standard or neural ) used by Amazon Polly when processing input text for speech synthesis.

    :type LanguageCode: string
    :param LanguageCode: The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don\'t specify this optional parameter, all available voices are returned.

    :type IncludeAdditionalLanguageCodes: boolean
    :param IncludeAdditionalLanguageCodes: Boolean value indicating whether to return any bilingual voices that use the specified language as an additional language. For instance, if you request all languages that use US English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US English, that voice will be included if you specify yes but not if you specify no .

    :type NextToken: string
    :param NextToken: An opaque pagination token returned from the previous DescribeVoices operation. If present, this indicates where to continue the listing.

    :rtype: dict

ReturnsResponse Syntax
{
    'Voices': [
        {
            'Gender': 'Female'|'Male',
            'Id': 'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
            'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
            'LanguageName': 'string',
            'Name': 'string',
            'AdditionalLanguageCodes': [
                'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
            ],
            'SupportedEngines': [
                'standard'|'neural',
            ]
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Voices (list) --
A list of voices with their properties.

(dict) --
Description of the voice.

Gender (string) --
Gender of the voice.

Id (string) --
Amazon Polly assigned voice ID. This is the ID that you specify when calling the SynthesizeSpeech operation.

LanguageCode (string) --
Language code of the voice.

LanguageName (string) --
Human readable name of the language in English.

Name (string) --
Name of the voice (for example, Salli, Kendra, etc.). This provides a human readable voice name that you might display in your application.

AdditionalLanguageCodes (list) --
Additional codes for languages available for the specified voice in addition to its default language.
For example, the default language for Aditi is Indian English (en-IN) because it was first used for that language. Since Aditi is bilingual and fluent in both Indian English and Hindi, this parameter would show the code hi-IN .

(string) --


SupportedEngines (list) --
Specifies which engines (standard or neural ) that are supported by a given voice.

(string) --






NextToken (string) --
The pagination token to use in the next request to continue the listing of voices. NextToken is returned only if the response is truncated.







Exceptions

Polly.Client.exceptions.InvalidNextTokenException
Polly.Client.exceptions.ServiceFailureException

Examples
Returns the list of voices that are available for use when requesting speech synthesis. Displayed languages are those within the specified language code. If no language code is specified, voices for all available languages are displayed.
response = client.describe_voices(
    LanguageCode='en-GB',
)

print(response)


Expected Output:
{
    'Voices': [
        {
            'Gender': 'Female',
            'Id': 'Emma',
            'LanguageCode': 'en-GB',
            'LanguageName': 'British English',
            'Name': 'Emma',
        },
        {
            'Gender': 'Male',
            'Id': 'Brian',
            'LanguageCode': 'en-GB',
            'LanguageName': 'British English',
            'Name': 'Brian',
        },
        {
            'Gender': 'Female',
            'Id': 'Amy',
            'LanguageCode': 'en-GB',
            'LanguageName': 'British English',
            'Name': 'Amy',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Voices': [
            {
                'Gender': 'Female'|'Male',
                'Id': 'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
                'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                'LanguageName': 'string',
                'Name': 'string',
                'AdditionalLanguageCodes': [
                    'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                ],
                'SupportedEngines': [
                    'standard'|'neural',
                ]
            },
        ],
        'NextToken': 'string'
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

def get_lexicon(Name=None):
    """
    Returns the content of the specified pronunciation lexicon stored in an AWS Region. For more information, see Managing Lexicons .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns the content of the specified pronunciation lexicon stored in an AWS Region.
    Expected Output:
    
    :example: response = client.get_lexicon(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the lexicon.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Lexicon': {
        'Content': 'string',
        'Name': 'string'
    },
    'LexiconAttributes': {
        'Alphabet': 'string',
        'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
        'LastModified': datetime(2015, 1, 1),
        'LexiconArn': 'string',
        'LexemesCount': 123,
        'Size': 123
    }
}


Response Structure

(dict) --
Lexicon (dict) --Lexicon object that provides name and the string content of the lexicon.

Content (string) --Lexicon content in string format. The content of a lexicon must be in PLS format.

Name (string) --Name of the lexicon.



LexiconAttributes (dict) --Metadata of the lexicon, including phonetic alphabetic used, language code, lexicon ARN, number of lexemes defined in the lexicon, and size of lexicon in bytes.

Alphabet (string) --Phonetic alphabet used in the lexicon. Valid values are ipa and x-sampa .

LanguageCode (string) --Language code that the lexicon applies to. A lexicon with a language code such as "en" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

LastModified (datetime) --Date lexicon was last modified (a timestamp value).

LexiconArn (string) --Amazon Resource Name (ARN) of the lexicon.

LexemesCount (integer) --Number of lexemes in the lexicon.

Size (integer) --Total size of the lexicon, in characters.








Exceptions

Polly.Client.exceptions.LexiconNotFoundException
Polly.Client.exceptions.ServiceFailureException

Examples
Returns the content of the specified pronunciation lexicon stored in an AWS Region.
response = client.get_lexicon(
    Name='',
)

print(response)


Expected Output:
{
    'Lexicon': {
        'Content': '<?xml version="1.0" encoding="UTF-8"?>\\r\
<lexicon version="1.0" \\r\
      xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"\\r\
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \\r\
      xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon \\r\
        http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"\\r\
      alphabet="ipa" \\r\
      xml:lang="en-US">\\r\
  <lexeme>\\r\
    <grapheme>W3C</grapheme>\\r\
    <alias>World Wide Web Consortium</alias>\\r\
  </lexeme>\\r\
</lexicon>',
        'Name': 'example',
    },
    'LexiconAttributes': {
        'Alphabet': 'ipa',
        'LanguageCode': 'en-US',
        'LastModified': 1478542980.117,
        'LexemesCount': 1,
        'LexiconArn': 'arn:aws:polly:us-east-1:123456789012:lexicon/example',
        'Size': 503,
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Lexicon': {
            'Content': 'string',
            'Name': 'string'
        },
        'LexiconAttributes': {
            'Alphabet': 'string',
            'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
            'LastModified': datetime(2015, 1, 1),
            'LexiconArn': 'string',
            'LexemesCount': 123,
            'Size': 123
        }
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

def get_speech_synthesis_task(TaskId=None):
    """
    Retrieves a specific SpeechSynthesisTask object based on its TaskID. This object contains information about the given speech synthesis task, including the status of the task, and a link to the S3 bucket containing the output of the task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_speech_synthesis_task(
        TaskId='string'
    )
    
    
    :type TaskId: string
    :param TaskId: [REQUIRED]\nThe Amazon Polly generated identifier for a speech synthesis task.\n

    :rtype: dict
ReturnsResponse Syntax{
    'SynthesisTask': {
        'Engine': 'standard'|'neural',
        'TaskId': 'string',
        'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
        'TaskStatusReason': 'string',
        'OutputUri': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'RequestCharacters': 123,
        'SnsTopicArn': 'string',
        'LexiconNames': [
            'string',
        ],
        'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
        'SampleRate': 'string',
        'SpeechMarkTypes': [
            'sentence'|'ssml'|'viseme'|'word',
        ],
        'TextType': 'ssml'|'text',
        'VoiceId': 'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
        'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
    }
}


Response Structure

(dict) --
SynthesisTask (dict) --SynthesisTask object that provides information from the requested task, including output format, creation time, task status, and so on.

Engine (string) --Specifies the engine (standard or neural ) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.

TaskId (string) --The Amazon Polly generated identifier for a speech synthesis task.

TaskStatus (string) --Current status of the individual speech synthesis task.

TaskStatusReason (string) --Reason for the current status of a specific speech synthesis task, including errors if the task has failed.

OutputUri (string) --Pathway for the output speech file.

CreationTime (datetime) --Timestamp for the time the synthesis task was started.

RequestCharacters (integer) --Number of billable characters synthesized.

SnsTopicArn (string) --ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.

LexiconNames (list) --List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice.

(string) --


OutputFormat (string) --The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

SampleRate (string) --The audio frequency specified in Hz.
The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The default value for standard voices is "22050". The default value for neural voices is "24000".
Valid values for pcm are "8000" and "16000" The default value is "16000".

SpeechMarkTypes (list) --The type of speech marks returned for the input text.

(string) --


TextType (string) --Specifies whether the input text is plain text or SSML. The default value is plain text.

VoiceId (string) --Voice ID to use for the synthesis.

LanguageCode (string) --Optional language code for a synthesis task. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).
If a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the DescribeVoices operation for the LanguageCode parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.








Exceptions

Polly.Client.exceptions.InvalidTaskIdException
Polly.Client.exceptions.ServiceFailureException
Polly.Client.exceptions.SynthesisTaskNotFoundException


    :return: {
        'SynthesisTask': {
            'Engine': 'standard'|'neural',
            'TaskId': 'string',
            'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
            'TaskStatusReason': 'string',
            'OutputUri': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'RequestCharacters': 123,
            'SnsTopicArn': 'string',
            'LexiconNames': [
                'string',
            ],
            'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
            'SampleRate': 'string',
            'SpeechMarkTypes': [
                'sentence'|'ssml'|'viseme'|'word',
            ],
            'TextType': 'ssml'|'text',
            'VoiceId': 'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
            'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
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

def list_lexicons(NextToken=None):
    """
    Returns a list of pronunciation lexicons stored in an AWS Region. For more information, see Managing Lexicons .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Returns a list of pronunciation lexicons stored in an AWS Region.
    Expected Output:
    
    :example: response = client.list_lexicons(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: An opaque pagination token returned from previous ListLexicons operation. If present, indicates where to continue the list of lexicons.

    :rtype: dict
ReturnsResponse Syntax{
    'Lexicons': [
        {
            'Name': 'string',
            'Attributes': {
                'Alphabet': 'string',
                'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                'LastModified': datetime(2015, 1, 1),
                'LexiconArn': 'string',
                'LexemesCount': 123,
                'Size': 123
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Lexicons (list) --A list of lexicon names and attributes.

(dict) --Describes the content of the lexicon.

Name (string) --Name of the lexicon.

Attributes (dict) --Provides lexicon metadata.

Alphabet (string) --Phonetic alphabet used in the lexicon. Valid values are ipa and x-sampa .

LanguageCode (string) --Language code that the lexicon applies to. A lexicon with a language code such as "en" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

LastModified (datetime) --Date lexicon was last modified (a timestamp value).

LexiconArn (string) --Amazon Resource Name (ARN) of the lexicon.

LexemesCount (integer) --Number of lexemes in the lexicon.

Size (integer) --Total size of the lexicon, in characters.







NextToken (string) --The pagination token to use in the next request to continue the listing of lexicons. NextToken is returned only if the response is truncated.






Exceptions

Polly.Client.exceptions.InvalidNextTokenException
Polly.Client.exceptions.ServiceFailureException

Examples
Returns a list of pronunciation lexicons stored in an AWS Region.
response = client.list_lexicons(
)

print(response)


Expected Output:
{
    'Lexicons': [
        {
            'Attributes': {
                'Alphabet': 'ipa',
                'LanguageCode': 'en-US',
                'LastModified': 1478542980.117,
                'LexemesCount': 1,
                'LexiconArn': 'arn:aws:polly:us-east-1:123456789012:lexicon/example',
                'Size': 503,
            },
            'Name': 'example',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Lexicons': [
            {
                'Name': 'string',
                'Attributes': {
                    'Alphabet': 'string',
                    'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                    'LastModified': datetime(2015, 1, 1),
                    'LexiconArn': 'string',
                    'LexemesCount': 123,
                    'Size': 123
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_speech_synthesis_tasks(MaxResults=None, NextToken=None, Status=None):
    """
    Returns a list of SpeechSynthesisTask objects ordered by their creation date. This operation can filter the tasks by their status, for example, allowing users to list only tasks that are completed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_speech_synthesis_tasks(
        MaxResults=123,
        NextToken='string',
        Status='scheduled'|'inProgress'|'completed'|'failed'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: Maximum number of speech synthesis tasks returned in a List operation.

    :type NextToken: string
    :param NextToken: The pagination token to use in the next request to continue the listing of speech synthesis tasks.

    :type Status: string
    :param Status: Status of the speech synthesis tasks returned in a List operation

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'SynthesisTasks': [
        {
            'Engine': 'standard'|'neural',
            'TaskId': 'string',
            'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
            'TaskStatusReason': 'string',
            'OutputUri': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'RequestCharacters': 123,
            'SnsTopicArn': 'string',
            'LexiconNames': [
                'string',
            ],
            'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
            'SampleRate': 'string',
            'SpeechMarkTypes': [
                'sentence'|'ssml'|'viseme'|'word',
            ],
            'TextType': 'ssml'|'text',
            'VoiceId': 'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
            'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
An opaque pagination token returned from the previous List operation in this request. If present, this indicates where to continue the listing.

SynthesisTasks (list) --
List of SynthesisTask objects that provides information from the specified task in the list request, including output format, creation time, task status, and so on.

(dict) --
SynthesisTask object that provides information about a speech synthesis task.

Engine (string) --
Specifies the engine (standard or neural ) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.

TaskId (string) --
The Amazon Polly generated identifier for a speech synthesis task.

TaskStatus (string) --
Current status of the individual speech synthesis task.

TaskStatusReason (string) --
Reason for the current status of a specific speech synthesis task, including errors if the task has failed.

OutputUri (string) --
Pathway for the output speech file.

CreationTime (datetime) --
Timestamp for the time the synthesis task was started.

RequestCharacters (integer) --
Number of billable characters synthesized.

SnsTopicArn (string) --
ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.

LexiconNames (list) --
List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice.

(string) --


OutputFormat (string) --
The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

SampleRate (string) --
The audio frequency specified in Hz.
The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The default value for standard voices is "22050". The default value for neural voices is "24000".
Valid values for pcm are "8000" and "16000" The default value is "16000".

SpeechMarkTypes (list) --
The type of speech marks returned for the input text.

(string) --


TextType (string) --
Specifies whether the input text is plain text or SSML. The default value is plain text.

VoiceId (string) --
Voice ID to use for the synthesis.

LanguageCode (string) --
Optional language code for a synthesis task. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).
If a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the DescribeVoices operation for the LanguageCode parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.











Exceptions

Polly.Client.exceptions.InvalidNextTokenException
Polly.Client.exceptions.ServiceFailureException


    :return: {
        'NextToken': 'string',
        'SynthesisTasks': [
            {
                'Engine': 'standard'|'neural',
                'TaskId': 'string',
                'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
                'TaskStatusReason': 'string',
                'OutputUri': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'RequestCharacters': 123,
                'SnsTopicArn': 'string',
                'LexiconNames': [
                    'string',
                ],
                'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
                'SampleRate': 'string',
                'SpeechMarkTypes': [
                    'sentence'|'ssml'|'viseme'|'word',
                ],
                'TextType': 'ssml'|'text',
                'VoiceId': 'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
                'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_lexicon(Name=None, Content=None):
    """
    Stores a pronunciation lexicon in an AWS Region. If a lexicon with the same name already exists in the region, it is overwritten by the new lexicon. Lexicon operations have eventual consistency, therefore, it might take some time before the lexicon is available to the SynthesizeSpeech operation.
    For more information, see Managing Lexicons .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Stores a pronunciation lexicon in an AWS Region.
    Expected Output:
    
    :example: response = client.put_lexicon(
        Name='string',
        Content='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long.\n

    :type Content: string
    :param Content: [REQUIRED]\nContent of the PLS lexicon as string data.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

Polly.Client.exceptions.InvalidLexiconException
Polly.Client.exceptions.UnsupportedPlsAlphabetException
Polly.Client.exceptions.UnsupportedPlsLanguageException
Polly.Client.exceptions.LexiconSizeExceededException
Polly.Client.exceptions.MaxLexemeLengthExceededException
Polly.Client.exceptions.MaxLexiconsNumberExceededException
Polly.Client.exceptions.ServiceFailureException

Examples
Stores a pronunciation lexicon in an AWS Region.
response = client.put_lexicon(
    Content='file://example.pls',
    Name='W3C',
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

def start_speech_synthesis_task(Engine=None, LanguageCode=None, LexiconNames=None, OutputFormat=None, OutputS3BucketName=None, OutputS3KeyPrefix=None, SampleRate=None, SnsTopicArn=None, SpeechMarkTypes=None, Text=None, TextType=None, VoiceId=None):
    """
    Allows the creation of an asynchronous synthesis task, by starting a new SpeechSynthesisTask . This operation requires all the standard information needed for speech synthesis, plus the name of an Amazon S3 bucket for the service to store the output of the synthesis task and two optional parameters (OutputS3KeyPrefix and SnsTopicArn). Once the synthesis task is created, this operation will return a SpeechSynthesisTask object, which will include an identifier of this task as well as the current status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_speech_synthesis_task(
        Engine='standard'|'neural',
        LanguageCode='arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
        LexiconNames=[
            'string',
        ],
        OutputFormat='json'|'mp3'|'ogg_vorbis'|'pcm',
        OutputS3BucketName='string',
        OutputS3KeyPrefix='string',
        SampleRate='string',
        SnsTopicArn='string',
        SpeechMarkTypes=[
            'sentence'|'ssml'|'viseme'|'word',
        ],
        Text='string',
        TextType='ssml'|'text',
        VoiceId='Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu'
    )
    
    
    :type Engine: string
    :param Engine: Specifies the engine (standard or neural ) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.

    :type LanguageCode: string
    :param LanguageCode: Optional language code for the Speech Synthesis request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).\nIf a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the DescribeVoices operation for the LanguageCode parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.\n

    :type LexiconNames: list
    :param LexiconNames: List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice.\n\n(string) --\n\n

    :type OutputFormat: string
    :param OutputFormat: [REQUIRED]\nThe format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.\n

    :type OutputS3BucketName: string
    :param OutputS3BucketName: [REQUIRED]\nAmazon S3 bucket name to which the output file will be saved.\n

    :type OutputS3KeyPrefix: string
    :param OutputS3KeyPrefix: The Amazon S3 key prefix for the output speech file.

    :type SampleRate: string
    :param SampleRate: The audio frequency specified in Hz.\nThe valid values for mp3 and ogg_vorbis are '8000', '16000', '22050', and '24000'. The default value for standard voices is '22050'. The default value for neural voices is '24000'.\nValid values for pcm are '8000' and '16000' The default value is '16000'.\n

    :type SnsTopicArn: string
    :param SnsTopicArn: ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.

    :type SpeechMarkTypes: list
    :param SpeechMarkTypes: The type of speech marks returned for the input text.\n\n(string) --\n\n

    :type Text: string
    :param Text: [REQUIRED]\nThe input text to synthesize. If you specify ssml as the TextType, follow the SSML format for the input text.\n

    :type TextType: string
    :param TextType: Specifies whether the input text is plain text or SSML. The default value is plain text.

    :type VoiceId: string
    :param VoiceId: [REQUIRED]\nVoice ID to use for the synthesis.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'SynthesisTask': {
        'Engine': 'standard'|'neural',
        'TaskId': 'string',
        'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
        'TaskStatusReason': 'string',
        'OutputUri': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'RequestCharacters': 123,
        'SnsTopicArn': 'string',
        'LexiconNames': [
            'string',
        ],
        'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
        'SampleRate': 'string',
        'SpeechMarkTypes': [
            'sentence'|'ssml'|'viseme'|'word',
        ],
        'TextType': 'ssml'|'text',
        'VoiceId': 'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
        'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
    }
}


Response Structure

(dict) --

SynthesisTask (dict) --
SynthesisTask object that provides information and attributes about a newly submitted speech synthesis task.

Engine (string) --
Specifies the engine (standard or neural ) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.

TaskId (string) --
The Amazon Polly generated identifier for a speech synthesis task.

TaskStatus (string) --
Current status of the individual speech synthesis task.

TaskStatusReason (string) --
Reason for the current status of a specific speech synthesis task, including errors if the task has failed.

OutputUri (string) --
Pathway for the output speech file.

CreationTime (datetime) --
Timestamp for the time the synthesis task was started.

RequestCharacters (integer) --
Number of billable characters synthesized.

SnsTopicArn (string) --
ARN for the SNS topic optionally used for providing status notification for a speech synthesis task.

LexiconNames (list) --
List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice.

(string) --


OutputFormat (string) --
The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.

SampleRate (string) --
The audio frequency specified in Hz.
The valid values for mp3 and ogg_vorbis are "8000", "16000", "22050", and "24000". The default value for standard voices is "22050". The default value for neural voices is "24000".
Valid values for pcm are "8000" and "16000" The default value is "16000".

SpeechMarkTypes (list) --
The type of speech marks returned for the input text.

(string) --


TextType (string) --
Specifies whether the input text is plain text or SSML. The default value is plain text.

VoiceId (string) --
Voice ID to use for the synthesis.

LanguageCode (string) --
Optional language code for a synthesis task. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).
If a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the DescribeVoices operation for the LanguageCode parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.









Exceptions

Polly.Client.exceptions.TextLengthExceededException
Polly.Client.exceptions.InvalidS3BucketException
Polly.Client.exceptions.InvalidS3KeyException
Polly.Client.exceptions.InvalidSampleRateException
Polly.Client.exceptions.InvalidSnsTopicArnException
Polly.Client.exceptions.InvalidSsmlException
Polly.Client.exceptions.EngineNotSupportedException
Polly.Client.exceptions.LexiconNotFoundException
Polly.Client.exceptions.ServiceFailureException
Polly.Client.exceptions.MarksNotSupportedForFormatException
Polly.Client.exceptions.SsmlMarksNotSupportedForTextTypeException
Polly.Client.exceptions.LanguageNotSupportedException


    :return: {
        'SynthesisTask': {
            'Engine': 'standard'|'neural',
            'TaskId': 'string',
            'TaskStatus': 'scheduled'|'inProgress'|'completed'|'failed',
            'TaskStatusReason': 'string',
            'OutputUri': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'RequestCharacters': 123,
            'SnsTopicArn': 'string',
            'LexiconNames': [
                'string',
            ],
            'OutputFormat': 'json'|'mp3'|'ogg_vorbis'|'pcm',
            'SampleRate': 'string',
            'SpeechMarkTypes': [
                'sentence'|'ssml'|'viseme'|'word',
            ],
            'TextType': 'ssml'|'text',
            'VoiceId': 'Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu',
            'LanguageCode': 'arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def synthesize_speech(Engine=None, LanguageCode=None, LexiconNames=None, OutputFormat=None, SampleRate=None, SpeechMarkTypes=None, Text=None, TextType=None, VoiceId=None):
    """
    Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid, well-formed SSML. Some alphabets might not be available with all the voices (for example, Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For more information, see How it Works .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Synthesizes plain text or SSML into a file of human-like speech.
    Expected Output:
    
    :example: response = client.synthesize_speech(
        Engine='standard'|'neural',
        LanguageCode='arb'|'cmn-CN'|'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-MX'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'hi-IN'|'ko-KR'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
        LexiconNames=[
            'string',
        ],
        OutputFormat='json'|'mp3'|'ogg_vorbis'|'pcm',
        SampleRate='string',
        SpeechMarkTypes=[
            'sentence'|'ssml'|'viseme'|'word',
        ],
        Text='string',
        TextType='ssml'|'text',
        VoiceId='Aditi'|'Amy'|'Astrid'|'Bianca'|'Brian'|'Camila'|'Carla'|'Carmen'|'Celine'|'Chantal'|'Conchita'|'Cristiano'|'Dora'|'Emma'|'Enrique'|'Ewa'|'Filiz'|'Geraint'|'Giorgio'|'Gwyneth'|'Hans'|'Ines'|'Ivy'|'Jacek'|'Jan'|'Joanna'|'Joey'|'Justin'|'Karl'|'Kendra'|'Kimberly'|'Lea'|'Liv'|'Lotte'|'Lucia'|'Lupe'|'Mads'|'Maja'|'Marlene'|'Mathieu'|'Matthew'|'Maxim'|'Mia'|'Miguel'|'Mizuki'|'Naja'|'Nicole'|'Penelope'|'Raveena'|'Ricardo'|'Ruben'|'Russell'|'Salli'|'Seoyeon'|'Takumi'|'Tatyana'|'Vicki'|'Vitoria'|'Zeina'|'Zhiyu'
    )
    
    
    :type Engine: string
    :param Engine: Specifies the engine (standard or neural ) for Amazon Polly to use when processing input text for speech synthesis. Using a voice that is not supported for the engine selected will result in an error.

    :type LanguageCode: string
    :param LanguageCode: Optional language code for the Synthesize Speech request. This is only necessary if using a bilingual voice, such as Aditi, which can be used for either Indian English (en-IN) or Hindi (hi-IN).\nIf a bilingual voice is used and no language code is specified, Amazon Polly will use the default language of the bilingual voice. The default language for any voice is the one returned by the DescribeVoices operation for the LanguageCode parameter. For example, if no language code is specified, Aditi will use Indian English rather than Hindi.\n

    :type LexiconNames: list
    :param LexiconNames: List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see PutLexicon .\n\n(string) --\n\n

    :type OutputFormat: string
    :param OutputFormat: [REQUIRED]\nThe format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.\nWhen pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.\n

    :type SampleRate: string
    :param SampleRate: The audio frequency specified in Hz.\nThe valid values for mp3 and ogg_vorbis are '8000', '16000', '22050', and '24000'. The default value for standard voices is '22050'. The default value for neural voices is '24000'.\nValid values for pcm are '8000' and '16000' The default value is '16000'.\n

    :type SpeechMarkTypes: list
    :param SpeechMarkTypes: The type of speech marks returned for the input text.\n\n(string) --\n\n

    :type Text: string
    :param Text: [REQUIRED]\nInput text to synthesize. If you specify ssml as the TextType , follow the SSML format for the input text.\n

    :type TextType: string
    :param TextType: Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see Using SSML .

    :type VoiceId: string
    :param VoiceId: [REQUIRED]\nVoice ID to use for the synthesis. You can get a list of available voice IDs by calling the DescribeVoices operation.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'AudioStream': StreamingBody(),
    'ContentType': 'string',
    'RequestCharacters': 123
}


Response Structure

(dict) --

AudioStream (StreamingBody) --
Stream containing the synthesized speech.

ContentType (string) --
Specifies the type audio stream. This should reflect the OutputFormat parameter in your request.

If you request mp3 as the OutputFormat , the ContentType returned is audio/mpeg.
If you request ogg_vorbis as the OutputFormat , the ContentType returned is audio/ogg.
If you request pcm as the OutputFormat , the ContentType returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.
If you request json as the OutputFormat , the ContentType returned is audio/json.


RequestCharacters (integer) --
Number of characters synthesized.







Exceptions

Polly.Client.exceptions.TextLengthExceededException
Polly.Client.exceptions.InvalidSampleRateException
Polly.Client.exceptions.InvalidSsmlException
Polly.Client.exceptions.LexiconNotFoundException
Polly.Client.exceptions.ServiceFailureException
Polly.Client.exceptions.MarksNotSupportedForFormatException
Polly.Client.exceptions.SsmlMarksNotSupportedForTextTypeException
Polly.Client.exceptions.LanguageNotSupportedException
Polly.Client.exceptions.EngineNotSupportedException

Examples
Synthesizes plain text or SSML into a file of human-like speech.
response = client.synthesize_speech(
    LexiconNames=[
        'example',
    ],
    OutputFormat='mp3',
    SampleRate='8000',
    Text='All Gaul is divided into three parts',
    TextType='text',
    VoiceId='Joanna',
)

print(response)


Expected Output:
{
    'AudioStream': 'TEXT',
    'ContentType': 'audio/mpeg',
    'RequestCharacters': 37,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'AudioStream': StreamingBody(),
        'ContentType': 'string',
        'RequestCharacters': 123
    }
    
    
    :returns: 
    If you request mp3 as the OutputFormat , the ContentType returned is audio/mpeg.
    If you request ogg_vorbis as the OutputFormat , the ContentType returned is audio/ogg.
    If you request pcm as the OutputFormat , the ContentType returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.
    If you request json as the OutputFormat , the ContentType returned is audio/json.
    
    """
    pass

