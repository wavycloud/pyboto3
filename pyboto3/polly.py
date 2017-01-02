'''

The MIT License (MIT)

Copyright (c) 2016 Simon Leiner

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

def can_paginate(operation_name):
    """
    Check if an operation can be paginated.

    :type operation_name string
    :param operation_name:
            The operation name. This is the same name as the method name on the client. For example, if the method name is create_foo, and you'd normally invoke the operation as client.create_foo(**kwargs), if the create_foo operation can be paginated, you can use the call client.get_paginator("create_foo").

    :rtype bool
    :return:
            True if the operation can be paginated, False otherwise.
    """
    pass

def delete_lexicon(Name):
    """
    Deletes the specified pronunciation lexicon stored in an AWS Region. A lexicon which has been deleted is not available for speech synthesis, nor is it possible to retrieve it using either the GetLexicon or ListLexicon APIs.

    For more information, see http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html .

    See also AWS API Documentation: https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DeleteLexicon

    :type Name string
    :param Name: [REQUIRED]
            The name of the lexicon to delete. Must be an existing lexicon in the region.

    :rtype dict
    """
    pass

def describe_voices(LanguageCode, NextToken):
    """
    Returns the list of voices that are available for use when requesting speech synthesis. Each voice speaks a specified language, is either male or female, and is identified by an ID, which is the ASCII version of the voice name.
    When synthesizing speech (SynthesizeSpeech), you provide the voice ID for the voice you want from the list of voices returned by DescribeVoices.
    For example, you want your news reader application to read news in a specific language, but giving a user the option to choose the voice. Using the DescribeVoices operation you can provide the user with a list of available voices to select from.
    You can optionally specify a language code to filter the available voices. For example, if you specify en-US, the operation returns a list of all available US English voices.
    This operation requires permissions to perform the polly:DescribeVoices action.

    See also AWS API Documentation: https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DescribeVoices

    :type LanguageCode string
    :param LanguageCode:
            The language identification tag (ISO 639 code for the language name-ISO 3166 country code)
            for filtering the list of voices returned. If you don't specify this optional parameter,
            all available voices are returned.

    :type NextToken string
    :param NextToken:
             An opaque pagination token returned from the previous DescribeVoices operation.
             If present, this indicates where to continue the listing.

    :rtype: dict
    :return:
            {
                'Voices': [
                    {
                        'Gender': 'Female'|'Male',
                        'Id': 'Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz',
                        'LanguageCode': 'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                        'LanguageName': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }

    :returns:
    NextToken:  The pagination token to use in the next request to continue the listing of voices. NextToken is returned only if the response is truncated.
    """
    pass

def generate_presigned_url(ClientMethod, Params=None, ExpiresIn=3600, HttpMethod=None):
    """
    Generate a presigned url given a client, its method, and arguments

    :type ClientMethod string
    :param ClientMethod:
            The client method to presign for

    :type Params dict
    :param Params:
            The parameters normally passed to ClientMethod.

    :type ExpiresIn int
    :param ExpiresIn:
            The number of seconds the presigned url is valid for. By default it expires in an hour (3600 seconds)

    :type HttpMethod string
    :param HttpMethod:
            The http method to use on the generated url. By default, the http method is whatever is used in the method's model.

    :return: The presigned url
    """
    pass

def get_lexicon(Name):
    """
    Returns the content of the specified pronunciation lexicon stored in an AWS Region. For more information, see http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html

    See also AWS API Documentation: https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/GetLexicon

    :type Name string
    :param Name: [REQUIRED]
            Name of the lexicon.

    :return: {
                'Lexicon': {
                    'Content': 'string',
                    'Name': 'string'
                },
                'LexiconAttributes': {
                    'Alphabet': 'string',
                    'LanguageCode': 'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                    'LastModified': datetime(2015, 1, 1),
                    'LexiconArn': 'string',
                    'LexemesCount': 123,
                    'Size': 123
                }
            }

    :returns:
    Lexicon: Lexicon object that provides name and the string content of the lexicon.
    Content: Lexicon content in string format. The content of a lexicon must be in PLS format.
    Name: Name of the lexicon.
    LexiconAttributes: Metadata of the lexicon, including phonetic alphabetic used, language code, lexicon ARN, number of lexemes defined in the lexicon, and size of lexicon in bytes.
    Alphabet: Phonetic alphabet used in the lexicon. Valid values are ipa and x-sampa.
    LanguageCode: Language code that the lexicon applies to. A lexicon with a language code such as "en" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.
    LastModified: Date lexicon was last modified (a timestamp value).
    LexiconArn: Amazon Resource Name (ARN) of the lexicon.
    LexemesCount: Number of lexemes in the lexicon.
    Size: Total size of the lexicon, in characters.
    """
    pass

def get_waiter(waiter_name):
    pass

def list_lexicons(NextToken):
    """
    Returns a list of pronunciation lexicons stored in an AWS Region. For more information, see http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html

    See also AWS API Documentation: https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/ListLexicons

    :type NextToken string
    :param NextToken:  An opaque pagination token returned from previous ListLexicons operation. If present, indicates where to continue the list of lexicons.

    :rtype dict
    :return: {
                'Lexicons': [
                    {
                        'Name': 'string',
                        'Attributes': {
                            'Alphabet': 'string',
                            'LanguageCode': 'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ja-JP'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                            'LastModified': datetime(2015, 1, 1),
                            'LexiconArn': 'string',
                            'LexemesCount': 123,
                            'Size': 123
                        }
                    },
                ],
                'NextToken': 'string'
            }
    :returns:
    Lexicons: A list of lexicon names and attributes.
    Name: Name of the lexicon.
    LexiconAttributes: Metadata of the lexicon, including phonetic alphabetic used, language code, lexicon ARN, number of lexemes defined in the lexicon, and size of lexicon in bytes.
    Alphabet: Phonetic alphabet used in the lexicon. Valid values are ipa and x-sampa.
    LanguageCode: Language code that the lexicon applies to. A lexicon with a language code such as "en" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.
    LastModified: Date lexicon was last modified (a timestamp value).
    LexiconArn: Amazon Resource Name (ARN) of the lexicon.
    LexemesCount: Number of lexemes in the lexicon.
    Size: Total size of the lexicon, in characters.
    NextToken: The pagination token to use in the next request to continue the listing of lexicons. NextToken is returned only if the response is truncated.
    """
    pass

def put_lexicon(Name, Content):
    """
    Stores a pronunciation lexicon in an AWS Region. If a lexicon with the same name already exists in the region, it is overwritten by the new lexicon. Lexicon operations have eventual consistency, therefore, it might take some time before the lexicon is available to the SynthesizeSpeech operation.
    For more information, see http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html

    See also AWS API Documentation: https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/PutLexicon

    :type Name string
    :param Name: [REQUIRED]
            Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long.

    :type Content string
    :param Content: [REQUIRED]
            Content of the PLS lexicon as string data.

    :rtype dict
    """
    pass

def synthesize_speech(LexiconNames, OutputFormat, SampleRate, Text, TextType, VoiceId):
    """
    Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid, well-formed SSML. Some alphabets might not be available with all the voices (for example, Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For more information, see http://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-works.html

    See also AWS API Documentation: https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/SynthesizeSpeech

    :type LexiconNames list
    :param LexiconNames:
            List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see http://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html

    :type OutputFormat string
    :param OutputFormat: [REQUIRED]
            The audio format in which the resulting stream will be encoded.

    :type SampleRate string
    :param SampleRate:
            The audio frequency specified in Hz.
            The valid values for mp3 and ogg_vorbis are "8000", "16000", and "22050". The default value is "22050".
            Valid values for pcm are "8000" and "16000" The default value is "16000".

    :type Text string
    :param Text: [REQUIRED]
            Input text to synthesize. If you specify ssml as the TextType , follow the SSML format for the input text.

    :type TextType string
    :param TextType:
            Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see http://docs.aws.amazon.com/polly/latest/dg/ssml.html

    :type VoiceId string
    :param VoiceId: [REQUIRED]
            Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the DescribeVoices operation.

    :rtype: dict
    :return: {
                'AudioStream': StreamingBody(),
                'ContentType': 'string',
                'RequestCharacters': 123
            }
    :returns:
    AudioStream: Stream containing the synthesized speech.
    ContentType: Specifies the type audio stream. This should reflect the OutputFormat parameter in your request.
        - If you request mp3 as the OutputFormat , the ContentType returned is audio/mpeg.
        - If you request ogg_vorbis as the OutputFormat , the ContentType returned is audio/ogg.
        - If you request pcm as the OutputFormat , the ContentType returned is audio/pcm.
    RequestCharacters: Number of characters synthesized.
    """
    pass
