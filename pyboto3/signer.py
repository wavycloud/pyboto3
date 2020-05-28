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

def cancel_signing_profile(profileName=None):
    """
    Changes the state of an ACTIVE signing profile to CANCELED . A canceled profile is still viewable with the ListSigningProfiles operation, but it cannot perform new signing jobs, and is deleted two years after cancelation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_signing_profile(
        profileName='string'
    )
    
    
    :type profileName: string
    :param profileName: [REQUIRED]\nThe name of the signing profile to be canceled.\n

    """
    pass

def describe_signing_job(jobId=None):
    """
    Returns information about a specific code signing job. You specify the job by using the jobId value that is returned by the  StartSigningJob operation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_signing_job(
        jobId='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe ID of the signing job on input.\n

    :rtype: dict
ReturnsResponse Syntax{
    'jobId': 'string',
    'source': {
        's3': {
            'bucketName': 'string',
            'key': 'string',
            'version': 'string'
        }
    },
    'signingMaterial': {
        'certificateArn': 'string'
    },
    'platformId': 'string',
    'profileName': 'string',
    'overrides': {
        'signingConfiguration': {
            'encryptionAlgorithm': 'RSA'|'ECDSA',
            'hashAlgorithm': 'SHA1'|'SHA256'
        },
        'signingImageFormat': 'JSON'|'JSONEmbedded'|'JSONDetached'
    },
    'signingParameters': {
        'string': 'string'
    },
    'createdAt': datetime(2015, 1, 1),
    'completedAt': datetime(2015, 1, 1),
    'requestedBy': 'string',
    'status': 'InProgress'|'Failed'|'Succeeded',
    'statusReason': 'string',
    'signedObject': {
        's3': {
            'bucketName': 'string',
            'key': 'string'
        }
    }
}


Response Structure

(dict) --
jobId (string) --The ID of the signing job on output.

source (dict) --The object that contains the name of your S3 bucket or your raw code.

s3 (dict) --The S3Source object.

bucketName (string) --Name of the S3 bucket.

key (string) --Key name of the bucket object that contains your unsigned code.

version (string) --Version of your source image in your version enabled S3 bucket.





signingMaterial (dict) --The Amazon Resource Name (ARN) of your code signing certificate.

certificateArn (string) --The Amazon Resource Name (ARN) of the certificates that is used to sign your code.



platformId (string) --The microcontroller platform to which your signed code image will be distributed.

profileName (string) --The name of the profile that initiated the signing operation.

overrides (dict) --A list of any overrides that were applied to the signing operation.

signingConfiguration (dict) --A signing configuration that overrides the default encryption or hash algorithm of a signing job.

encryptionAlgorithm (string) --A specified override of the default encryption algorithm that is used in a code signing job.

hashAlgorithm (string) --A specified override of the default hash algorithm that is used in a code signing job.



signingImageFormat (string) --A signed image is a JSON object. When overriding the default signing platform configuration, a customer can select either of two signing formats, JSONEmbedded or JSONDetached . (A third format value, JSON , is reserved for future use.) With JSONEmbedded , the signing image has the payload embedded in it. With JSONDetached , the payload is not be embedded in the signing image.



signingParameters (dict) --Map of user-assigned key-value pairs used during signing. These values contain any information that you specified for use in your signing job.

(string) --
(string) --




createdAt (datetime) --Date and time that the signing job was created.

completedAt (datetime) --Date and time that the signing job was completed.

requestedBy (string) --The IAM principal that requested the signing job.

status (string) --Status of the signing job.

statusReason (string) --String value that contains the status reason.

signedObject (dict) --Name of the S3 bucket where the signed code image is saved by code signing.

s3 (dict) --The S3SignedObject .

bucketName (string) --Name of the S3 bucket.

key (string) --Key name that uniquely identifies a signed code image in your bucket.










Exceptions

signer.Client.exceptions.ResourceNotFoundException
signer.Client.exceptions.AccessDeniedException
signer.Client.exceptions.InternalServiceErrorException


    :return: {
        'jobId': 'string',
        'source': {
            's3': {
                'bucketName': 'string',
                'key': 'string',
                'version': 'string'
            }
        },
        'signingMaterial': {
            'certificateArn': 'string'
        },
        'platformId': 'string',
        'profileName': 'string',
        'overrides': {
            'signingConfiguration': {
                'encryptionAlgorithm': 'RSA'|'ECDSA',
                'hashAlgorithm': 'SHA1'|'SHA256'
            },
            'signingImageFormat': 'JSON'|'JSONEmbedded'|'JSONDetached'
        },
        'signingParameters': {
            'string': 'string'
        },
        'createdAt': datetime(2015, 1, 1),
        'completedAt': datetime(2015, 1, 1),
        'requestedBy': 'string',
        'status': 'InProgress'|'Failed'|'Succeeded',
        'statusReason': 'string',
        'signedObject': {
            's3': {
                'bucketName': 'string',
                'key': 'string'
            }
        }
    }
    
    
    :returns: 
    signer.Client.exceptions.ResourceNotFoundException
    signer.Client.exceptions.AccessDeniedException
    signer.Client.exceptions.InternalServiceErrorException
    
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

def get_signing_platform(platformId=None):
    """
    Returns information on a specific signing platform.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_signing_platform(
        platformId='string'
    )
    
    
    :type platformId: string
    :param platformId: [REQUIRED]\nThe ID of the target signing platform.\n

    :rtype: dict
ReturnsResponse Syntax{
    'platformId': 'string',
    'displayName': 'string',
    'partner': 'string',
    'target': 'string',
    'category': 'AWSIoT',
    'signingConfiguration': {
        'encryptionAlgorithmOptions': {
            'allowedValues': [
                'RSA'|'ECDSA',
            ],
            'defaultValue': 'RSA'|'ECDSA'
        },
        'hashAlgorithmOptions': {
            'allowedValues': [
                'SHA1'|'SHA256',
            ],
            'defaultValue': 'SHA1'|'SHA256'
        }
    },
    'signingImageFormat': {
        'supportedFormats': [
            'JSON'|'JSONEmbedded'|'JSONDetached',
        ],
        'defaultFormat': 'JSON'|'JSONEmbedded'|'JSONDetached'
    },
    'maxSizeInMB': 123
}


Response Structure

(dict) --
platformId (string) --The ID of the target signing platform.

displayName (string) --The display name of the target signing platform.

partner (string) --A list of partner entities that use the target signing platform.

target (string) --The validation template that is used by the target signing platform.

category (string) --The category type of the target signing platform.

signingConfiguration (dict) --A list of configurations applied to the target platform at signing.

encryptionAlgorithmOptions (dict) --The encryption algorithm options that are available for a code signing job.

allowedValues (list) --The set of accepted encryption algorithms that are allowed in a code signing job.

(string) --


defaultValue (string) --The default encryption algorithm that is used by a code signing job.



hashAlgorithmOptions (dict) --The hash algorithm options that are available for a code signing job.

allowedValues (list) --The set of accepted hash algorithms allowed in a code signing job.

(string) --


defaultValue (string) --The default hash algorithm that is used in a code signing job.





signingImageFormat (dict) --The format of the target platform\'s signing image.

supportedFormats (list) --The supported formats of a code signing image.

(string) --


defaultFormat (string) --The default format of a code signing image.



maxSizeInMB (integer) --The maximum size (in MB) of the payload that can be signed by the target platform.






Exceptions

signer.Client.exceptions.ResourceNotFoundException
signer.Client.exceptions.AccessDeniedException
signer.Client.exceptions.InternalServiceErrorException


    :return: {
        'platformId': 'string',
        'displayName': 'string',
        'partner': 'string',
        'target': 'string',
        'category': 'AWSIoT',
        'signingConfiguration': {
            'encryptionAlgorithmOptions': {
                'allowedValues': [
                    'RSA'|'ECDSA',
                ],
                'defaultValue': 'RSA'|'ECDSA'
            },
            'hashAlgorithmOptions': {
                'allowedValues': [
                    'SHA1'|'SHA256',
                ],
                'defaultValue': 'SHA1'|'SHA256'
            }
        },
        'signingImageFormat': {
            'supportedFormats': [
                'JSON'|'JSONEmbedded'|'JSONDetached',
            ],
            'defaultFormat': 'JSON'|'JSONEmbedded'|'JSONDetached'
        },
        'maxSizeInMB': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_signing_profile(profileName=None):
    """
    Returns information on a specific signing profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_signing_profile(
        profileName='string'
    )
    
    
    :type profileName: string
    :param profileName: [REQUIRED]\nThe name of the target signing profile.\n

    :rtype: dict
ReturnsResponse Syntax{
    'profileName': 'string',
    'signingMaterial': {
        'certificateArn': 'string'
    },
    'platformId': 'string',
    'overrides': {
        'signingConfiguration': {
            'encryptionAlgorithm': 'RSA'|'ECDSA',
            'hashAlgorithm': 'SHA1'|'SHA256'
        },
        'signingImageFormat': 'JSON'|'JSONEmbedded'|'JSONDetached'
    },
    'signingParameters': {
        'string': 'string'
    },
    'status': 'Active'|'Canceled',
    'arn': 'string',
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
profileName (string) --The name of the target signing profile.

signingMaterial (dict) --The ARN of the certificate that the target profile uses for signing operations.

certificateArn (string) --The Amazon Resource Name (ARN) of the certificates that is used to sign your code.



platformId (string) --The ID of the platform that is used by the target signing profile.

overrides (dict) --A list of overrides applied by the target signing profile for signing operations.

signingConfiguration (dict) --A signing configuration that overrides the default encryption or hash algorithm of a signing job.

encryptionAlgorithm (string) --A specified override of the default encryption algorithm that is used in a code signing job.

hashAlgorithm (string) --A specified override of the default hash algorithm that is used in a code signing job.



signingImageFormat (string) --A signed image is a JSON object. When overriding the default signing platform configuration, a customer can select either of two signing formats, JSONEmbedded or JSONDetached . (A third format value, JSON , is reserved for future use.) With JSONEmbedded , the signing image has the payload embedded in it. With JSONDetached , the payload is not be embedded in the signing image.



signingParameters (dict) --A map of key-value pairs for signing operations that is attached to the target signing profile.

(string) --
(string) --




status (string) --The status of the target signing profile.

arn (string) --The Amazon Resource Name (ARN) for the signing profile.

tags (dict) --A list of tags associated with the signing profile.

(string) --
(string) --









Exceptions

signer.Client.exceptions.ResourceNotFoundException
signer.Client.exceptions.AccessDeniedException
signer.Client.exceptions.ThrottlingException
signer.Client.exceptions.InternalServiceErrorException


    :return: {
        'profileName': 'string',
        'signingMaterial': {
            'certificateArn': 'string'
        },
        'platformId': 'string',
        'overrides': {
            'signingConfiguration': {
                'encryptionAlgorithm': 'RSA'|'ECDSA',
                'hashAlgorithm': 'SHA1'|'SHA256'
            },
            'signingImageFormat': 'JSON'|'JSONEmbedded'|'JSONDetached'
        },
        'signingParameters': {
            'string': 'string'
        },
        'status': 'Active'|'Canceled',
        'arn': 'string',
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
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

def list_signing_jobs(status=None, platformId=None, requestedBy=None, maxResults=None, nextToken=None):
    """
    Lists all your signing jobs. You can use the maxResults parameter to limit the number of signing jobs that are returned in the response. If additional jobs remain to be listed, code signing returns a nextToken value. Use this value in subsequent calls to ListSigningJobs to fetch the remaining values. You can continue calling ListSigningJobs with your maxResults parameter and with new values that code signing returns in the nextToken parameter until all of your signing jobs have been returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_signing_jobs(
        status='InProgress'|'Failed'|'Succeeded',
        platformId='string',
        requestedBy='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type status: string
    :param status: A status value with which to filter your results.

    :type platformId: string
    :param platformId: The ID of microcontroller platform that you specified for the distribution of your code image.

    :type requestedBy: string
    :param requestedBy: The IAM principal that requested the signing job.

    :type maxResults: integer
    :param maxResults: Specifies the maximum number of items to return in the response. Use this parameter when paginating results. If additional items exist beyond the number you specify, the nextToken element is set in the response. Use the nextToken value in a subsequent request to retrieve additional items.

    :type nextToken: string
    :param nextToken: String for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of nextToken from the response that you just received.

    :rtype: dict

ReturnsResponse Syntax
{
    'jobs': [
        {
            'jobId': 'string',
            'source': {
                's3': {
                    'bucketName': 'string',
                    'key': 'string',
                    'version': 'string'
                }
            },
            'signedObject': {
                's3': {
                    'bucketName': 'string',
                    'key': 'string'
                }
            },
            'signingMaterial': {
                'certificateArn': 'string'
            },
            'createdAt': datetime(2015, 1, 1),
            'status': 'InProgress'|'Failed'|'Succeeded'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

jobs (list) --
A list of your signing jobs.

(dict) --
Contains information about a signing job.

jobId (string) --
The ID of the signing job.

source (dict) --
A Source that contains information about a signing job\'s code image source.

s3 (dict) --
The S3Source object.

bucketName (string) --
Name of the S3 bucket.

key (string) --
Key name of the bucket object that contains your unsigned code.

version (string) --
Version of your source image in your version enabled S3 bucket.





signedObject (dict) --
A SignedObject structure that contains information about a signing job\'s signed code image.

s3 (dict) --
The S3SignedObject .

bucketName (string) --
Name of the S3 bucket.

key (string) --
Key name that uniquely identifies a signed code image in your bucket.





signingMaterial (dict) --
A SigningMaterial object that contains the Amazon Resource Name (ARN) of the certificate used for the signing job.

certificateArn (string) --
The Amazon Resource Name (ARN) of the certificates that is used to sign your code.



createdAt (datetime) --
The date and time that the signing job was created.

status (string) --
The status of the signing job.





nextToken (string) --
String for specifying the next set of paginated results.







Exceptions

signer.Client.exceptions.ValidationException
signer.Client.exceptions.AccessDeniedException
signer.Client.exceptions.ThrottlingException
signer.Client.exceptions.InternalServiceErrorException


    :return: {
        'jobs': [
            {
                'jobId': 'string',
                'source': {
                    's3': {
                        'bucketName': 'string',
                        'key': 'string',
                        'version': 'string'
                    }
                },
                'signedObject': {
                    's3': {
                        'bucketName': 'string',
                        'key': 'string'
                    }
                },
                'signingMaterial': {
                    'certificateArn': 'string'
                },
                'createdAt': datetime(2015, 1, 1),
                'status': 'InProgress'|'Failed'|'Succeeded'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    signer.Client.exceptions.ValidationException
    signer.Client.exceptions.AccessDeniedException
    signer.Client.exceptions.ThrottlingException
    signer.Client.exceptions.InternalServiceErrorException
    
    """
    pass

def list_signing_platforms(category=None, partner=None, target=None, maxResults=None, nextToken=None):
    """
    Lists all signing platforms available in code signing that match the request parameters. If additional jobs remain to be listed, code signing returns a nextToken value. Use this value in subsequent calls to ListSigningJobs to fetch the remaining values. You can continue calling ListSigningJobs with your maxResults parameter and with new values that code signing returns in the nextToken parameter until all of your signing jobs have been returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_signing_platforms(
        category='string',
        partner='string',
        target='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type category: string
    :param category: The category type of a signing platform.

    :type partner: string
    :param partner: Any partner entities connected to a signing platform.

    :type target: string
    :param target: The validation template that is used by the target signing platform.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned by this operation.

    :type nextToken: string
    :param nextToken: Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of nextToken from the response that you just received.

    :rtype: dict

ReturnsResponse Syntax
{
    'platforms': [
        {
            'platformId': 'string',
            'displayName': 'string',
            'partner': 'string',
            'target': 'string',
            'category': 'AWSIoT',
            'signingConfiguration': {
                'encryptionAlgorithmOptions': {
                    'allowedValues': [
                        'RSA'|'ECDSA',
                    ],
                    'defaultValue': 'RSA'|'ECDSA'
                },
                'hashAlgorithmOptions': {
                    'allowedValues': [
                        'SHA1'|'SHA256',
                    ],
                    'defaultValue': 'SHA1'|'SHA256'
                }
            },
            'signingImageFormat': {
                'supportedFormats': [
                    'JSON'|'JSONEmbedded'|'JSONDetached',
                ],
                'defaultFormat': 'JSON'|'JSONEmbedded'|'JSONDetached'
            },
            'maxSizeInMB': 123
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

platforms (list) --
A list of all platforms that match the request parameters.

(dict) --
Contains information about the signing configurations and parameters that are used to perform a code signing job.

platformId (string) --
The ID of a code signing; platform.

displayName (string) --
The display name of a code signing platform.

partner (string) --
Any partner entities linked to a code signing platform.

target (string) --
The types of targets that can be signed by a code signing platform.

category (string) --
The category of a code signing platform.

signingConfiguration (dict) --
The configuration of a code signing platform. This includes the designated hash algorithm and encryption algorithm of a signing platform.

encryptionAlgorithmOptions (dict) --
The encryption algorithm options that are available for a code signing job.

allowedValues (list) --
The set of accepted encryption algorithms that are allowed in a code signing job.

(string) --


defaultValue (string) --
The default encryption algorithm that is used by a code signing job.



hashAlgorithmOptions (dict) --
The hash algorithm options that are available for a code signing job.

allowedValues (list) --
The set of accepted hash algorithms allowed in a code signing job.

(string) --


defaultValue (string) --
The default hash algorithm that is used in a code signing job.





signingImageFormat (dict) --
The image format of a code signing platform or profile.

supportedFormats (list) --
The supported formats of a code signing image.

(string) --


defaultFormat (string) --
The default format of a code signing image.



maxSizeInMB (integer) --
The maximum size (in MB) of code that can be signed by a code signing platform.





nextToken (string) --
Value for specifying the next set of paginated results to return.







Exceptions

signer.Client.exceptions.ValidationException
signer.Client.exceptions.AccessDeniedException
signer.Client.exceptions.ThrottlingException
signer.Client.exceptions.InternalServiceErrorException


    :return: {
        'platforms': [
            {
                'platformId': 'string',
                'displayName': 'string',
                'partner': 'string',
                'target': 'string',
                'category': 'AWSIoT',
                'signingConfiguration': {
                    'encryptionAlgorithmOptions': {
                        'allowedValues': [
                            'RSA'|'ECDSA',
                        ],
                        'defaultValue': 'RSA'|'ECDSA'
                    },
                    'hashAlgorithmOptions': {
                        'allowedValues': [
                            'SHA1'|'SHA256',
                        ],
                        'defaultValue': 'SHA1'|'SHA256'
                    }
                },
                'signingImageFormat': {
                    'supportedFormats': [
                        'JSON'|'JSONEmbedded'|'JSONDetached',
                    ],
                    'defaultFormat': 'JSON'|'JSONEmbedded'|'JSONDetached'
                },
                'maxSizeInMB': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_signing_profiles(includeCanceled=None, maxResults=None, nextToken=None):
    """
    Lists all available signing profiles in your AWS account. Returns only profiles with an ACTIVE status unless the includeCanceled request field is set to true . If additional jobs remain to be listed, code signing returns a nextToken value. Use this value in subsequent calls to ListSigningJobs to fetch the remaining values. You can continue calling ListSigningJobs with your maxResults parameter and with new values that code signing returns in the nextToken parameter until all of your signing jobs have been returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_signing_profiles(
        includeCanceled=True|False,
        maxResults=123,
        nextToken='string'
    )
    
    
    :type includeCanceled: boolean
    :param includeCanceled: Designates whether to include profiles with the status of CANCELED .

    :type maxResults: integer
    :param maxResults: The maximum number of profiles to be returned.

    :type nextToken: string
    :param nextToken: Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of nextToken from the response that you just received.

    :rtype: dict

ReturnsResponse Syntax
{
    'profiles': [
        {
            'profileName': 'string',
            'signingMaterial': {
                'certificateArn': 'string'
            },
            'platformId': 'string',
            'signingParameters': {
                'string': 'string'
            },
            'status': 'Active'|'Canceled',
            'arn': 'string',
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

profiles (list) --
A list of profiles that are available in the AWS account. This includes profiles with the status of CANCELED if the includeCanceled parameter is set to true .

(dict) --
Contains information about the ACM certificates and code signing configuration parameters that can be used by a given code signing user.

profileName (string) --
The name of the signing profile.

signingMaterial (dict) --
The ACM certificate that is available for use by a signing profile.

certificateArn (string) --
The Amazon Resource Name (ARN) of the certificates that is used to sign your code.



platformId (string) --
The ID of a platform that is available for use by a signing profile.

signingParameters (dict) --
The parameters that are available for use by a code signing user.

(string) --
(string) --




status (string) --
The status of a code signing profile.

arn (string) --
The Amazon Resource Name (ARN) for the signing profile.

tags (dict) --
A list of tags associated with the signing profile.

(string) --
(string) --








nextToken (string) --
Value for specifying the next set of paginated results to return.







Exceptions

signer.Client.exceptions.AccessDeniedException
signer.Client.exceptions.ThrottlingException
signer.Client.exceptions.InternalServiceErrorException


    :return: {
        'profiles': [
            {
                'profileName': 'string',
                'signingMaterial': {
                    'certificateArn': 'string'
                },
                'platformId': 'string',
                'signingParameters': {
                    'string': 'string'
                },
                'status': 'Active'|'Canceled',
                'arn': 'string',
                'tags': {
                    'string': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Returns a list of the tags associated with a signing profile resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the signing profile.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
tags (dict) --A list of tags associated with the signing profile.

(string) --
(string) --









Exceptions

signer.Client.exceptions.InternalServiceErrorException
signer.Client.exceptions.BadRequestException
signer.Client.exceptions.NotFoundException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    signer.Client.exceptions.InternalServiceErrorException
    signer.Client.exceptions.BadRequestException
    signer.Client.exceptions.NotFoundException
    
    """
    pass

def put_signing_profile(profileName=None, signingMaterial=None, platformId=None, overrides=None, signingParameters=None, tags=None):
    """
    Creates a signing profile. A signing profile is a code signing template that can be used to carry out a pre-defined signing job. For more information, see http://docs.aws.amazon.com/signer/latest/developerguide/gs-profile.html
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_signing_profile(
        profileName='string',
        signingMaterial={
            'certificateArn': 'string'
        },
        platformId='string',
        overrides={
            'signingConfiguration': {
                'encryptionAlgorithm': 'RSA'|'ECDSA',
                'hashAlgorithm': 'SHA1'|'SHA256'
            },
            'signingImageFormat': 'JSON'|'JSONEmbedded'|'JSONDetached'
        },
        signingParameters={
            'string': 'string'
        },
        tags={
            'string': 'string'
        }
    )
    
    
    :type profileName: string
    :param profileName: [REQUIRED]\nThe name of the signing profile to be created.\n

    :type signingMaterial: dict
    :param signingMaterial: [REQUIRED]\nThe AWS Certificate Manager certificate that will be used to sign code with the new signing profile.\n\ncertificateArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the certificates that is used to sign your code.\n\n\n

    :type platformId: string
    :param platformId: [REQUIRED]\nThe ID of the signing platform to be created.\n

    :type overrides: dict
    :param overrides: A subfield of platform . This specifies any different configuration options that you want to apply to the chosen platform (such as a different hash-algorithm or signing-algorithm ).\n\nsigningConfiguration (dict) --A signing configuration that overrides the default encryption or hash algorithm of a signing job.\n\nencryptionAlgorithm (string) --A specified override of the default encryption algorithm that is used in a code signing job.\n\nhashAlgorithm (string) --A specified override of the default hash algorithm that is used in a code signing job.\n\n\n\nsigningImageFormat (string) --A signed image is a JSON object. When overriding the default signing platform configuration, a customer can select either of two signing formats, JSONEmbedded or JSONDetached . (A third format value, JSON , is reserved for future use.) With JSONEmbedded , the signing image has the payload embedded in it. With JSONDetached , the payload is not be embedded in the signing image.\n\n\n

    :type signingParameters: dict
    :param signingParameters: Map of key-value pairs for signing. These can include any information that you want to use during signing.\n\n(string) --\n(string) --\n\n\n\n

    :type tags: dict
    :param tags: Tags to be associated with the signing profile that is being created.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string'
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the signing profile created.







Exceptions

signer.Client.exceptions.ResourceNotFoundException
signer.Client.exceptions.AccessDeniedException
signer.Client.exceptions.ValidationException
signer.Client.exceptions.ThrottlingException
signer.Client.exceptions.InternalServiceErrorException


    :return: {
        'arn': 'string'
    }
    
    
    :returns: 
    signer.Client.exceptions.ResourceNotFoundException
    signer.Client.exceptions.AccessDeniedException
    signer.Client.exceptions.ValidationException
    signer.Client.exceptions.ThrottlingException
    signer.Client.exceptions.InternalServiceErrorException
    
    """
    pass

def start_signing_job(source=None, destination=None, profileName=None, clientRequestToken=None):
    """
    Initiates a signing job to be performed on the code provided. Signing jobs are viewable by the ListSigningJobs operation for two years after they are performed. Note the following requirements:
    You can call the  DescribeSigningJob and the  ListSigningJobs actions after you call StartSigningJob .
    For a Java example that shows how to use this action, see http://docs.aws.amazon.com/acm/latest/userguide/
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_signing_job(
        source={
            's3': {
                'bucketName': 'string',
                'key': 'string',
                'version': 'string'
            }
        },
        destination={
            's3': {
                'bucketName': 'string',
                'prefix': 'string'
            }
        },
        profileName='string',
        clientRequestToken='string'
    )
    
    
    :type source: dict
    :param source: [REQUIRED]\nThe S3 bucket that contains the object to sign or a BLOB that contains your raw code.\n\ns3 (dict) --The S3Source object.\n\nbucketName (string) -- [REQUIRED]Name of the S3 bucket.\n\nkey (string) -- [REQUIRED]Key name of the bucket object that contains your unsigned code.\n\nversion (string) -- [REQUIRED]Version of your source image in your version enabled S3 bucket.\n\n\n\n\n

    :type destination: dict
    :param destination: [REQUIRED]\nThe S3 bucket in which to save your signed object. The destination contains the name of your bucket and an optional prefix.\n\ns3 (dict) --The S3Destination object.\n\nbucketName (string) --Name of the S3 bucket.\n\nprefix (string) --An Amazon S3 prefix that you can use to limit responses to those that begin with the specified prefix.\n\n\n\n\n

    :type profileName: string
    :param profileName: The name of the signing profile.

    :type clientRequestToken: string
    :param clientRequestToken: [REQUIRED]\nString that identifies the signing request. All calls after the first that use this token return the same response as the first call.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobId': 'string'
}


Response Structure

(dict) --

jobId (string) --
The ID of your signing job.







Exceptions

signer.Client.exceptions.ValidationException
signer.Client.exceptions.ResourceNotFoundException
signer.Client.exceptions.AccessDeniedException
signer.Client.exceptions.ThrottlingException
signer.Client.exceptions.InternalServiceErrorException


    :return: {
        'jobId': 'string'
    }
    
    
    :returns: 
    source (dict) -- [REQUIRED]
    The S3 bucket that contains the object to sign or a BLOB that contains your raw code.
    
    s3 (dict) --The S3Source object.
    
    bucketName (string) -- [REQUIRED]Name of the S3 bucket.
    
    key (string) -- [REQUIRED]Key name of the bucket object that contains your unsigned code.
    
    version (string) -- [REQUIRED]Version of your source image in your version enabled S3 bucket.
    
    
    
    
    
    destination (dict) -- [REQUIRED]
    The S3 bucket in which to save your signed object. The destination contains the name of your bucket and an optional prefix.
    
    s3 (dict) --The S3Destination object.
    
    bucketName (string) --Name of the S3 bucket.
    
    prefix (string) --An Amazon S3 prefix that you can use to limit responses to those that begin with the specified prefix.
    
    
    
    
    
    profileName (string) -- The name of the signing profile.
    clientRequestToken (string) -- [REQUIRED]
    String that identifies the signing request. All calls after the first that use this token return the same response as the first call.
    This field is autopopulated if not provided.
    
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds one or more tags to a signing profile. Tags are labels that you can use to identify and organize your AWS resources. Each tag consists of a key and an optional value. To specify the signing profile, use its Amazon Resource Name (ARN). To specify the tag, use a key-value pair.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the signing profile.\n

    :type tags: dict
    :param tags: [REQUIRED]\nOne or more tags to be associated with the signing profile.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

signer.Client.exceptions.InternalServiceErrorException
signer.Client.exceptions.BadRequestException
signer.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes one or more tags from a signing profile. To remove the tags, specify a list of tag keys.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for the signing profile.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nA list of tag keys to be removed from the signing profile.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

signer.Client.exceptions.InternalServiceErrorException
signer.Client.exceptions.BadRequestException
signer.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

