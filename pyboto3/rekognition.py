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

def compare_faces(SourceImage=None, TargetImage=None, SimilarityThreshold=None):
    """
    Compares a face in the source input image with each of the 100 largest faces detected in the target input image.
    You pass the input and target images either as base64-encoded image bytes or as a references to images in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    In response, the operation returns an array of face matches ordered by similarity score in descending order. For each face match, the response provides a bounding box of the face, facial landmarks, pose details (pitch, role, and yaw), quality (brightness and sharpness), and confidence value (indicating the level of confidence that the bounding box contains a face). The response also provides a similarity score, which indicates how closely the faces match.
    If the image doesn't contain Exif metadata, CompareFaces returns orientation information for the source and target images. Use these values to display the images with the correct image orientation.
    If no faces are detected in the source or target images, CompareFaces returns an InvalidParameterException error.
    For an example, see  faces-compare-images .
    This operation requires permissions to perform the rekognition:CompareFaces action.
    See also: AWS API Documentation
    
    Examples
    This operation compares the largest face detected in the source image with each face detected in the target image.
    Expected Output:
    
    :example: response = client.compare_faces(
        SourceImage={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        TargetImage={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        SimilarityThreshold=...
    )
    
    
    :type SourceImage: dict
    :param SourceImage: [REQUIRED]
            The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.
            Bytes (bytes) --Blob of image bytes up to 5 MBs.
            S3Object (dict) --Identifies an S3 object as the image source.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type TargetImage: dict
    :param TargetImage: [REQUIRED]
            The target image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.
            Bytes (bytes) --Blob of image bytes up to 5 MBs.
            S3Object (dict) --Identifies an S3 object as the image source.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type SimilarityThreshold: float
    :param SimilarityThreshold: The minimum level of confidence in the face matches that a match must meet to be included in the FaceMatches array.

    :rtype: dict
    :return: {
        'SourceImageFace': {
            'BoundingBox': {
                'Width': ...,
                'Height': ...,
                'Left': ...,
                'Top': ...
            },
            'Confidence': ...
        },
        'FaceMatches': [
            {
                'Similarity': ...,
                'Face': {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'Confidence': ...,
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                            'X': ...,
                            'Y': ...
                        },
                    ],
                    'Pose': {
                        'Roll': ...,
                        'Yaw': ...,
                        'Pitch': ...
                    },
                    'Quality': {
                        'Brightness': ...,
                        'Sharpness': ...
                    }
                }
            },
        ],
        'UnmatchedFaces': [
            {
                'BoundingBox': {
                    'Width': ...,
                    'Height': ...,
                    'Left': ...,
                    'Top': ...
                },
                'Confidence': ...,
                'Landmarks': [
                    {
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                        'X': ...,
                        'Y': ...
                    },
                ],
                'Pose': {
                    'Roll': ...,
                    'Yaw': ...,
                    'Pitch': ...
                },
                'Quality': {
                    'Brightness': ...,
                    'Sharpness': ...
                }
            },
        ],
        'SourceImageOrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270',
        'TargetImageOrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
    }
    
    
    """
    pass

def create_collection(CollectionId=None):
    """
    Creates a collection in an AWS Region. You can add faces to the collection using the operation.
    For example, you might create collections, one for each of your application users. A user can then index faces using the IndexFaces operation and persist results in a specific collection. Then, a user can search the collection for faces in the user-specific container.
    This operation requires permissions to perform the rekognition:CreateCollection action.
    See also: AWS API Documentation
    
    Examples
    This operation creates a Rekognition collection for storing image data.
    Expected Output:
    
    :example: response = client.create_collection(
        CollectionId='string'
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]
            ID for the collection that you are creating.
            

    :rtype: dict
    :return: {
        'StatusCode': 123,
        'CollectionArn': 'string',
        'FaceModelVersion': 'string'
    }
    
    
    """
    pass

def create_stream_processor(Input=None, Output=None, Name=None, Settings=None, RoleArn=None):
    """
    Creates an Amazon Rekognition stream processor that you can use to detect and recognize faces in a streaming video.
    Rekognition Video is a consumer of live video from Amazon Kinesis Video Streams. Rekognition Video sends analysis results to Amazon Kinesis Data Streams.
    You provide as input a Kinesis video stream (Input ) and a Kinesis data stream (Output ) stream. You also specify the face recognition criteria in Settings . For example, the collection containing faces that you want to recognize. Use Name to assign an identifier for the stream processor. You use Name to manage the stream processor. For example, you can start processing the source video by calling with the Name field.
    After you have finished analyzing a streaming video, use to stop processing. You can delete the stream processor by calling .
    See also: AWS API Documentation
    
    
    :example: response = client.create_stream_processor(
        Input={
            'KinesisVideoStream': {
                'Arn': 'string'
            }
        },
        Output={
            'KinesisDataStream': {
                'Arn': 'string'
            }
        },
        Name='string',
        Settings={
            'FaceSearch': {
                'CollectionId': 'string',
                'FaceMatchThreshold': ...
            }
        },
        RoleArn='string'
    )
    
    
    :type Input: dict
    :param Input: [REQUIRED]
            Kinesis video stream stream that provides the source streaming video. If you are using the AWS CLI, the parameter name is StreamProcessorInput .
            KinesisVideoStream (dict) --The Kinesis video stream input stream for the source streaming video.
            Arn (string) --ARN of the Kinesis video stream stream that streams the source video.
            
            

    :type Output: dict
    :param Output: [REQUIRED]
            Kinesis data stream stream to which Rekognition Video puts the analysis results. If you are using the AWS CLI, the parameter name is StreamProcessorOutput .
            KinesisDataStream (dict) --The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor streams the analysis results.
            Arn (string) --ARN of the output Amazon Kinesis Data Streams stream.
            
            

    :type Name: string
    :param Name: [REQUIRED]
            An identifier you assign to the stream processor. You can use Name to manage the stream processor. For example, you can get the current status of the stream processor by calling . Name is idempotent.
            

    :type Settings: dict
    :param Settings: [REQUIRED]
            Face recognition input parameters to be used by the stream processor. Includes the collection to use for face recognition and the face attributes to detect.
            FaceSearch (dict) --Face search settings to use on a streaming video.
            CollectionId (string) --The ID of a collection that contains faces that you want to search for.
            FaceMatchThreshold (float) --Minimum face match confidence score that must be met to return a result for a recognized face. Default is 70. 0 is the lowest confidence. 100 is the highest confidence.
            
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            ARN of the IAM role that allows access to the stream processor.
            

    :rtype: dict
    :return: {
        'StreamProcessorArn': 'string'
    }
    
    
    """
    pass

def delete_collection(CollectionId=None):
    """
    Deletes the specified collection. Note that this operation removes all faces in the collection. For an example, see  delete-collection-procedure .
    This operation requires permissions to perform the rekognition:DeleteCollection action.
    See also: AWS API Documentation
    
    Examples
    This operation deletes a Rekognition collection.
    Expected Output:
    
    :example: response = client.delete_collection(
        CollectionId='string'
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]
            ID of the collection to delete.
            

    :rtype: dict
    :return: {
        'StatusCode': 123
    }
    
    
    """
    pass

def delete_faces(CollectionId=None, FaceIds=None):
    """
    Deletes faces from a collection. You specify a collection ID and an array of face IDs to remove from the collection.
    This operation requires permissions to perform the rekognition:DeleteFaces action.
    See also: AWS API Documentation
    
    Examples
    This operation deletes one or more faces from a Rekognition collection.
    Expected Output:
    
    :example: response = client.delete_faces(
        CollectionId='string',
        FaceIds=[
            'string',
        ]
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]
            Collection from which to remove the specific faces.
            

    :type FaceIds: list
    :param FaceIds: [REQUIRED]
            An array of face IDs to delete.
            (string) --
            

    :rtype: dict
    :return: {
        'DeletedFaces': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_stream_processor(Name=None):
    """
    Deletes the stream processor identified by Name . You assign the value for Name when you create the stream processor with . You might not be able to use the same name for a stream processor for a few seconds after calling DeleteStreamProcessor .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_stream_processor(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the stream processor you want to delete.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def describe_stream_processor(Name=None):
    """
    Provides information about a stream processor created by . You can get information about the input and output streams, the input parameters for the face recognition being performed, and the current status of the stream processor.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_stream_processor(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Name of the stream processor for which you want information.
            

    :rtype: dict
    :return: {
        'Name': 'string',
        'StreamProcessorArn': 'string',
        'Status': 'STOPPED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING',
        'StatusMessage': 'string',
        'CreationTimestamp': datetime(2015, 1, 1),
        'LastUpdateTimestamp': datetime(2015, 1, 1),
        'Input': {
            'KinesisVideoStream': {
                'Arn': 'string'
            }
        },
        'Output': {
            'KinesisDataStream': {
                'Arn': 'string'
            }
        },
        'RoleArn': 'string',
        'Settings': {
            'FaceSearch': {
                'CollectionId': 'string',
                'FaceMatchThreshold': ...
            }
        }
    }
    
    
    """
    pass

def detect_faces(Image=None, Attributes=None):
    """
    Detects faces within an image that is provided as input.
    The face-detection algorithm is most effective on frontal faces. For non-frontal or obscured faces, the algorithm may not detect the faces or might detect faces with lower confidence.
    You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    For an example, see  procedure-detecting-faces-in-images .
    This operation requires permissions to perform the rekognition:DetectFaces action.
    See also: AWS API Documentation
    
    Examples
    This operation detects faces in an image stored in an AWS S3 bucket.
    Expected Output:
    
    :example: response = client.detect_faces(
        Image={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        Attributes=[
            'DEFAULT'|'ALL',
        ]
    )
    
    
    :type Image: dict
    :param Image: [REQUIRED]
            The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.
            Bytes (bytes) --Blob of image bytes up to 5 MBs.
            S3Object (dict) --Identifies an S3 object as the image source.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type Attributes: list
    :param Attributes: An array of facial attributes you want to be returned. This can be the default list of attributes or all attributes. If you don't specify a value for Attributes or if you specify ['DEFAULT'] , the API returns the following subset of facial attributes: BoundingBox , Confidence , Pose , Quality and Landmarks . If you provide ['ALL'] , all facial attributes are returned but the operation will take longer to complete.
            If you provide both, ['ALL', 'DEFAULT'] , the service uses a logical AND operator to determine which attributes to return (in this case, all attributes).
            (string) --
            

    :rtype: dict
    :return: {
        'FaceDetails': [
            {
                'BoundingBox': {
                    'Width': ...,
                    'Height': ...,
                    'Left': ...,
                    'Top': ...
                },
                'AgeRange': {
                    'Low': 123,
                    'High': 123
                },
                'Smile': {
                    'Value': True|False,
                    'Confidence': ...
                },
                'Eyeglasses': {
                    'Value': True|False,
                    'Confidence': ...
                },
                'Sunglasses': {
                    'Value': True|False,
                    'Confidence': ...
                },
                'Gender': {
                    'Value': 'Male'|'Female',
                    'Confidence': ...
                },
                'Beard': {
                    'Value': True|False,
                    'Confidence': ...
                },
                'Mustache': {
                    'Value': True|False,
                    'Confidence': ...
                },
                'EyesOpen': {
                    'Value': True|False,
                    'Confidence': ...
                },
                'MouthOpen': {
                    'Value': True|False,
                    'Confidence': ...
                },
                'Emotions': [
                    {
                        'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                        'Confidence': ...
                    },
                ],
                'Landmarks': [
                    {
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                        'X': ...,
                        'Y': ...
                    },
                ],
                'Pose': {
                    'Roll': ...,
                    'Yaw': ...,
                    'Pitch': ...
                },
                'Quality': {
                    'Brightness': ...,
                    'Sharpness': ...
                },
                'Confidence': ...
            },
        ],
        'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
    }
    
    
    """
    pass

def detect_labels(Image=None, MaxLabels=None, MinConfidence=None):
    """
    Detects instances of real-world entities within an image (JPEG or PNG) provided as input. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; and concepts like landscape, evening, and nature. For an example, see  images-s3 .
    You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    For each object, scene, and concept the API returns one or more labels. Each label provides the object name, and the level of confidence that the image contains the object. For example, suppose the input image has a lighthouse, the sea, and a rock. The response will include all three labels, one for each object.
    In the preceding example, the operation returns one label for each of the three objects. The operation can also return multiple labels for the same object in the image. For example, if the input image shows a flower (for example, a tulip), the operation might return the following three labels.
    In this example, the detection algorithm more precisely identifies the flower as a tulip.
    In response, the API returns an array of labels. In addition, the response also includes the orientation correction. Optionally, you can specify MinConfidence to control the confidence threshold for the labels returned. The default is 50%. You can also add the MaxLabels parameter to limit the number of labels returned.
    This is a stateless API operation. That is, the operation does not persist any data.
    This operation requires permissions to perform the rekognition:DetectLabels action.
    See also: AWS API Documentation
    
    Examples
    This operation detects labels in the supplied image
    Expected Output:
    
    :example: response = client.detect_labels(
        Image={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        MaxLabels=123,
        MinConfidence=...
    )
    
    
    :type Image: dict
    :param Image: [REQUIRED]
            The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.
            Bytes (bytes) --Blob of image bytes up to 5 MBs.
            S3Object (dict) --Identifies an S3 object as the image source.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type MaxLabels: integer
    :param MaxLabels: Maximum number of labels you want the service to return in the response. The service returns the specified number of highest confidence labels.

    :type MinConfidence: float
    :param MinConfidence: Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with confidence lower than this specified value.
            If MinConfidence is not specified, the operation returns labels with a confidence values greater than or equal to 50 percent.
            

    :rtype: dict
    :return: {
        'Labels': [
            {
                'Name': 'string',
                'Confidence': ...
            },
        ],
        'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
    }
    
    
    """
    pass

def detect_moderation_labels(Image=None, MinConfidence=None):
    """
    Detects explicit or suggestive adult content in a specified JPEG or PNG format image. Use DetectModerationLabels to moderate images depending on your requirements. For example, you might want to filter images that contain nudity, but not images containing suggestive content.
    To filter images, use the labels returned by DetectModerationLabels to determine which types of content are appropriate. For information about moderation labels, see  moderation .
    You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    See also: AWS API Documentation
    
    
    :example: response = client.detect_moderation_labels(
        Image={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        MinConfidence=...
    )
    
    
    :type Image: dict
    :param Image: [REQUIRED]
            The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.
            Bytes (bytes) --Blob of image bytes up to 5 MBs.
            S3Object (dict) --Identifies an S3 object as the image source.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type MinConfidence: float
    :param MinConfidence: Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with a confidence level lower than this specified value.
            If you don't specify MinConfidence , the operation returns labels with confidence values greater than or equal to 50 percent.
            

    :rtype: dict
    :return: {
        'ModerationLabels': [
            {
                'Confidence': ...,
                'Name': 'string',
                'ParentName': 'string'
            },
        ]
    }
    
    
    """
    pass

def detect_text(Image=None):
    """
    Detects text in the input image and converts it into machine-readable text.
    Pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, you must pass it as a reference to an image in an Amazon S3 bucket. For the AWS CLI, passing image bytes is not supported. The image must be either a .png or .jpeg formatted file.
    The DetectText operation returns text in an array of elements, TextDetections . Each TextDetection element provides information about a single word or line of text that was detected in the image.
    A word is one or more ISO basic latin script characters that are not separated by spaces. DetectText can detect up to 50 words in an image.
    A line is a string of equally spaced words. A line isn't necessarily a complete sentence. For example, a driver's license number is detected as a line. A line ends when there is no aligned text after it. Also, a line ends when there is a large gap between words, relative to the length of the words. This means, depending on the gap between words, Amazon Rekognition may detect multiple lines in text aligned in the same direction. Periods don't represent the end of a line. If a sentence spans multiple lines, the DetectText operation returns multiple lines.
    To determine whether a TextDetection element is a line of text or a word, use the TextDetection object Type field.
    To be detected, text must be within +/- 30 degrees orientation of the horizontal axis.
    For more information, see  text-detection .
    See also: AWS API Documentation
    
    
    :example: response = client.detect_text(
        Image={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        }
    )
    
    
    :type Image: dict
    :param Image: [REQUIRED]
            The input image as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Rekognition operations, you can't pass image bytes.
            Bytes (bytes) --Blob of image bytes up to 5 MBs.
            S3Object (dict) --Identifies an S3 object as the image source.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :rtype: dict
    :return: {
        'TextDetections': [
            {
                'DetectedText': 'string',
                'Type': 'LINE'|'WORD',
                'Id': 123,
                'ParentId': 123,
                'Confidence': ...,
                'Geometry': {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'Polygon': [
                        {
                            'X': ...,
                            'Y': ...
                        },
                    ]
                }
            },
        ]
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

def get_celebrity_info(Id=None):
    """
    Gets the name and additional information about a celebrity based on his or her Rekognition ID. The additional information is returned as an array of URLs. If there is no additional information about the celebrity, this list is empty. For more information, see  get-celebrity-info-procedure .
    This operation requires permissions to perform the rekognition:GetCelebrityInfo action.
    See also: AWS API Documentation
    
    
    :example: response = client.get_celebrity_info(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]
            The ID for the celebrity. You get the celebrity ID from a call to the operation, which recognizes celebrities in an image.
            

    :rtype: dict
    :return: {
        'Urls': [
            'string',
        ],
        'Name': 'string'
    }
    
    
    """
    pass

def get_celebrity_recognition(JobId=None, MaxResults=None, NextToken=None, SortBy=None):
    """
    Gets the celebrity recognition results for a Rekognition Video analysis started by .
    Celebrity recognition in a video is an asynchronous operation. Analysis is started by a call to which returns a job identifier (JobId ). When the celebrity recognition operation finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartCelebrityRecognition . To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call GetCelebrityDetection and pass the job identifier (JobId ) from the initial call to StartCelebrityDetection . For more information, see  video .
    By default, the Celebrities array is sorted by time (milliseconds from the start of the video). You can also sort the array by celebrity by specifying the value ID in the SortBy input parameter.
    The CelebrityDetail object includes the celebrity identifer and additional information urls. If you don't store the additional information urls, you can get them later by calling with the celebrity identifer.
    No information is returned for faces not recognized as celebrities.
    Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetCelebrityDetection and populate the NextToken request parameter with the token value returned from the previous call to GetCelebrityRecognition .
    See also: AWS API Documentation
    
    
    :example: response = client.get_celebrity_recognition(
        JobId='string',
        MaxResults=123,
        NextToken='string',
        SortBy='ID'|'TIMESTAMP'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            Job identifier for the required celebrity recognition analysis. You can get the job identifer from a call to StartCelebrityRecognition .
            

    :type MaxResults: integer
    :param MaxResults: Maximum number of celebrities you want Rekognition Video to return in the response. The default is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more recognized celebrities to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of celebrities.

    :type SortBy: string
    :param SortBy: Sort to use for celebrities returned in Celebrities field. Specify ID to sort by the celebrity identifier, specify TIMESTAMP to sort by the time the celebrity was recognized.

    :rtype: dict
    :return: {
        'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'StatusMessage': 'string',
        'VideoMetadata': {
            'Codec': 'string',
            'DurationMillis': 123,
            'Format': 'string',
            'FrameRate': ...,
            'FrameHeight': 123,
            'FrameWidth': 123
        },
        'NextToken': 'string',
        'Celebrities': [
            {
                'Timestamp': 123,
                'Celebrity': {
                    'Urls': [
                        'string',
                    ],
                    'Name': 'string',
                    'Id': 'string',
                    'Confidence': ...,
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'Face': {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'AgeRange': {
                            'Low': 123,
                            'High': 123
                        },
                        'Smile': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Eyeglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Sunglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Gender': {
                            'Value': 'Male'|'Female',
                            'Confidence': ...
                        },
                        'Beard': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Mustache': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'EyesOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'MouthOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Emotions': [
                            {
                                'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                                'Confidence': ...
                            },
                        ],
                        'Landmarks': [
                            {
                                'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                                'X': ...,
                                'Y': ...
                            },
                        ],
                        'Pose': {
                            'Roll': ...,
                            'Yaw': ...,
                            'Pitch': ...
                        },
                        'Quality': {
                            'Brightness': ...,
                            'Sharpness': ...
                        },
                        'Confidence': ...
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_content_moderation(JobId=None, MaxResults=None, NextToken=None, SortBy=None):
    """
    Gets the content moderation analysis results for a Rekognition Video analysis started by .
    Content moderation analysis of a video is an asynchronous operation. You start analysis by calling . which returns a job identifier (JobId ). When analysis finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartContentModeration . To get the results of the content moderation analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call GetCelebrityDetection and pass the job identifier (JobId ) from the initial call to StartCelebrityDetection . For more information, see  video .
    By default, the moderated labels are returned sorted by time, in milliseconds from the start of the video. You can also sort them by moderated label by specifying NAME for the SortBy input parameter.
    Since video analysis can return a large number of results, use the MaxResults parameter to limit the number of labels returned in a single call to GetContentModeration . If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetContentModeration and populate the NextToken request parameter with the value of NextToken returned from the previous call to GetContentModeration .
    For more information, see  moderation .
    See also: AWS API Documentation
    
    
    :example: response = client.get_content_moderation(
        JobId='string',
        MaxResults=123,
        NextToken='string',
        SortBy='NAME'|'TIMESTAMP'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier for the content moderation job. Use JobId to identify the job in a subsequent call to GetContentModeration .
            

    :type MaxResults: integer
    :param MaxResults: Maximum number of content moderation labels to return. The default is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of content moderation labels.

    :type SortBy: string
    :param SortBy: Sort to use for elements in the ModerationLabelDetections array. Use TIMESTAMP to sort array elements by the time labels are detected. Use NAME to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by TIMESTAMP .

    :rtype: dict
    :return: {
        'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'StatusMessage': 'string',
        'VideoMetadata': {
            'Codec': 'string',
            'DurationMillis': 123,
            'Format': 'string',
            'FrameRate': ...,
            'FrameHeight': 123,
            'FrameWidth': 123
        },
        'ModerationLabels': [
            {
                'Timestamp': 123,
                'ModerationLabel': {
                    'Confidence': ...,
                    'Name': 'string',
                    'ParentName': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def get_face_detection(JobId=None, MaxResults=None, NextToken=None):
    """
    Gets face detection results for a Rekognition Video analysis started by .
    Face detection with Rekognition Video is an asynchronous operation. You start face detection by calling which returns a job identifier (JobId ). When the face detection operation finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartFaceDetection . To get the results of the face detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call and pass the job identifier (JobId ) from the initial call to StartFaceDetection .
    Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetFaceDetection and populate the NextToken request parameter with the token value returned from the previous call to GetFaceDetection .
    See also: AWS API Documentation
    
    
    :example: response = client.get_face_detection(
        JobId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            Unique identifier for the face detection job. The JobId is returned from StartFaceDetection .
            

    :type MaxResults: integer
    :param MaxResults: Maximum number of detected faces to return. The default is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more faces to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of faces.

    :rtype: dict
    :return: {
        'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'StatusMessage': 'string',
        'VideoMetadata': {
            'Codec': 'string',
            'DurationMillis': 123,
            'Format': 'string',
            'FrameRate': ...,
            'FrameHeight': 123,
            'FrameWidth': 123
        },
        'NextToken': 'string',
        'Faces': [
            {
                'Timestamp': 123,
                'Face': {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'AgeRange': {
                        'Low': 123,
                        'High': 123
                    },
                    'Smile': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Eyeglasses': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Sunglasses': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Gender': {
                        'Value': 'Male'|'Female',
                        'Confidence': ...
                    },
                    'Beard': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Mustache': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'EyesOpen': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'MouthOpen': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Emotions': [
                        {
                            'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                            'Confidence': ...
                        },
                    ],
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                            'X': ...,
                            'Y': ...
                        },
                    ],
                    'Pose': {
                        'Roll': ...,
                        'Yaw': ...,
                        'Pitch': ...
                    },
                    'Quality': {
                        'Brightness': ...,
                        'Sharpness': ...
                    },
                    'Confidence': ...
                }
            },
        ]
    }
    
    
    """
    pass

def get_face_search(JobId=None, MaxResults=None, NextToken=None, SortBy=None):
    """
    Gets the face search results for Rekognition Video face search started by . The search returns faces in a collection that match the faces of persons detected in a video. It also includes the time(s) that faces are matched in the video.
    Face search in a video is an asynchronous operation. You start face search by calling to which returns a job identifier (JobId ). When the search operation finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartFaceSearch . To get the search results, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call GetFaceSearch and pass the job identifier (JobId ) from the initial call to StartFaceSearch . For more information, see  collections .
    The search results are retured in an array, Persons , of objects. Each``PersonMatch`` element contains details about the matching faces in the input collection, person information for the matched person, and the time the person was matched in the video.
    By default, the Persons array is sorted by the time, in milliseconds from the start of the video, persons are matched. You can also sort by persons by specifying INDEX for the SORTBY input parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.get_face_search(
        JobId='string',
        MaxResults=123,
        NextToken='string',
        SortBy='INDEX'|'TIMESTAMP'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The job identifer for the search request. You get the job identifier from an initial call to StartFaceSearch .
            

    :type MaxResults: integer
    :param MaxResults: Maximum number of search results you want Rekognition Video to return in the response. The default is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more search results to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of search results.

    :type SortBy: string
    :param SortBy: Sort to use for grouping faces in the response. Use TIMESTAMP to group faces by the time that they are recognized. Use INDEX to sort by recognized faces.

    :rtype: dict
    :return: {
        'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'StatusMessage': 'string',
        'NextToken': 'string',
        'VideoMetadata': {
            'Codec': 'string',
            'DurationMillis': 123,
            'Format': 'string',
            'FrameRate': ...,
            'FrameHeight': 123,
            'FrameWidth': 123
        },
        'Persons': [
            {
                'Timestamp': 123,
                'Person': {
                    'Index': 123,
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'Face': {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'AgeRange': {
                            'Low': 123,
                            'High': 123
                        },
                        'Smile': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Eyeglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Sunglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Gender': {
                            'Value': 'Male'|'Female',
                            'Confidence': ...
                        },
                        'Beard': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Mustache': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'EyesOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'MouthOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Emotions': [
                            {
                                'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                                'Confidence': ...
                            },
                        ],
                        'Landmarks': [
                            {
                                'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                                'X': ...,
                                'Y': ...
                            },
                        ],
                        'Pose': {
                            'Roll': ...,
                            'Yaw': ...,
                            'Pitch': ...
                        },
                        'Quality': {
                            'Brightness': ...,
                            'Sharpness': ...
                        },
                        'Confidence': ...
                    }
                },
                'FaceMatches': [
                    {
                        'Similarity': ...,
                        'Face': {
                            'FaceId': 'string',
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'ImageId': 'string',
                            'ExternalImageId': 'string',
                            'Confidence': ...
                        }
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def get_label_detection(JobId=None, MaxResults=None, NextToken=None, SortBy=None):
    """
    Gets the label detection results of a Rekognition Video analysis started by .
    The label detection operation is started by a call to which returns a job identifier (JobId ). When the label detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartlabelDetection . To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call and pass the job identifier (JobId ) from the initial call to StartLabelDetection .
    The labels returned include the label name, the percentage confidence in the accuracy of the detected label, and the time the label was detected in the video.
    Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetlabelDetection and populate the NextToken request parameter with the token value returned from the previous call to GetLabelDetection .
    See also: AWS API Documentation
    
    
    :example: response = client.get_label_detection(
        JobId='string',
        MaxResults=123,
        NextToken='string',
        SortBy='NAME'|'TIMESTAMP'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            Job identifier for the label detection operation for which you want results returned. You get the job identifer from an initial call to StartlabelDetection .
            

    :type MaxResults: integer
    :param MaxResults: Maximum number of labels you want Amazon Rekognition to return in the response. The default is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more labels to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of labels.

    :type SortBy: string
    :param SortBy: Sort to use for elements in the Labels array. Use TIMESTAMP to sort array elements by the time labels are detected. Use NAME to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by TIMESTAMP .

    :rtype: dict
    :return: {
        'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'StatusMessage': 'string',
        'VideoMetadata': {
            'Codec': 'string',
            'DurationMillis': 123,
            'Format': 'string',
            'FrameRate': ...,
            'FrameHeight': 123,
            'FrameWidth': 123
        },
        'NextToken': 'string',
        'Labels': [
            {
                'Timestamp': 123,
                'Label': {
                    'Name': 'string',
                    'Confidence': ...
                }
            },
        ]
    }
    
    
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

def get_person_tracking(JobId=None, MaxResults=None, NextToken=None, SortBy=None):
    """
    Gets the person tracking results of a Rekognition Video analysis started by .
    The person detection operation is started by a call to StartPersonTracking which returns a job identifier (JobId ). When the person detection operation finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartPersonTracking .
    To get the results of the person tracking operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call and pass the job identifier (JobId ) from the initial call to StartPersonTracking .
    By default, the array is sorted by the time(s) a person is tracked in the video. You can sort by tracked persons by specifying INDEX for the SortBy input parameter.
    Use the MaxResults parameter to limit the number of items returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetPersonTracking and populate the NextToken request parameter with the token value returned from the previous call to GetPersonTracking .
    See also: AWS API Documentation
    
    
    :example: response = client.get_person_tracking(
        JobId='string',
        MaxResults=123,
        NextToken='string',
        SortBy='INDEX'|'TIMESTAMP'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]
            The identifier for a job that tracks persons in a video. You get the JobId from a call to StartPersonTracking .
            

    :type MaxResults: integer
    :param MaxResults: Maximum number of tracked persons to return. The default is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more persons to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of persons.

    :type SortBy: string
    :param SortBy: Sort to use for elements in the Persons array. Use TIMESTAMP to sort array elements by the time persons are detected. Use INDEX to sort by the tracked persons. If you sort by INDEX , the array elements for each person are sorted by detection confidence. The default sort is by TIMESTAMP .

    :rtype: dict
    :return: {
        'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'StatusMessage': 'string',
        'VideoMetadata': {
            'Codec': 'string',
            'DurationMillis': 123,
            'Format': 'string',
            'FrameRate': ...,
            'FrameHeight': 123,
            'FrameWidth': 123
        },
        'NextToken': 'string',
        'Persons': [
            {
                'Timestamp': 123,
                'Person': {
                    'Index': 123,
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'Face': {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'AgeRange': {
                            'Low': 123,
                            'High': 123
                        },
                        'Smile': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Eyeglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Sunglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Gender': {
                            'Value': 'Male'|'Female',
                            'Confidence': ...
                        },
                        'Beard': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Mustache': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'EyesOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'MouthOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Emotions': [
                            {
                                'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                                'Confidence': ...
                            },
                        ],
                        'Landmarks': [
                            {
                                'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                                'X': ...,
                                'Y': ...
                            },
                        ],
                        'Pose': {
                            'Roll': ...,
                            'Yaw': ...,
                            'Pitch': ...
                        },
                        'Quality': {
                            'Brightness': ...,
                            'Sharpness': ...
                        },
                        'Confidence': ...
                    }
                }
            },
        ]
    }
    
    
    """
    pass

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def index_faces(CollectionId=None, Image=None, ExternalImageId=None, DetectionAttributes=None):
    """
    Detects faces in the input image and adds them to the specified collection.
    Amazon Rekognition does not save the actual faces detected. Instead, the underlying detection algorithm first detects the faces in the input image, and for each face extracts facial features into a feature vector, and stores it in the back-end database. Amazon Rekognition uses feature vectors when performing face match and search operations using the and operations.
    If you are using version 1.0 of the face detection model, IndexFaces indexes the 15 largest faces in the input image. Later versions of the face detection model index the 100 largest faces in the input image. To determine which version of the model you are using, check the the value of FaceModelVersion in the response from IndexFaces . For more information, see  face-detection-model .
    If you provide the optional ExternalImageID for the input image you provided, Amazon Rekognition associates this ID with all faces that it detects. When you call the operation, the response returns the external ID. You can use this external image ID to create a client-side index to associate the faces with each image. You can then use the index to find all faces in an image.
    In response, the operation returns an array of metadata for all detected faces. This includes, the bounding box of the detected face, confidence value (indicating the bounding box contains a face), a face ID assigned by the service for each face that is detected and stored, and an image ID assigned by the service for the input image. If you request all facial attributes (using the detectionAttributes parameter, Amazon Rekognition returns detailed facial attributes such as facial landmarks (for example, location of eye and mount) and other facial attributes such gender. If you provide the same image, specify the same collection, and use the same external ID in the IndexFaces operation, Amazon Rekognition doesn't save duplicate face metadata.
    The input image is passed either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    This operation requires permissions to perform the rekognition:IndexFaces action.
    See also: AWS API Documentation
    
    Examples
    This operation detects faces in an image and adds them to the specified Rekognition collection.
    Expected Output:
    
    :example: response = client.index_faces(
        CollectionId='string',
        Image={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        ExternalImageId='string',
        DetectionAttributes=[
            'DEFAULT'|'ALL',
        ]
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]
            The ID of an existing collection to which you want to add the faces that are detected in the input images.
            

    :type Image: dict
    :param Image: [REQUIRED]
            The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.
            Bytes (bytes) --Blob of image bytes up to 5 MBs.
            S3Object (dict) --Identifies an S3 object as the image source.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type ExternalImageId: string
    :param ExternalImageId: ID you want to assign to all the faces detected in the image.

    :type DetectionAttributes: list
    :param DetectionAttributes: An array of facial attributes that you want to be returned. This can be the default list of attributes or all attributes. If you don't specify a value for Attributes or if you specify ['DEFAULT'] , the API returns the following subset of facial attributes: BoundingBox , Confidence , Pose , Quality and Landmarks . If you provide ['ALL'] , all facial attributes are returned but the operation will take longer to complete.
            If you provide both, ['ALL', 'DEFAULT'] , the service uses a logical AND operator to determine which attributes to return (in this case, all attributes).
            (string) --
            

    :rtype: dict
    :return: {
        'FaceRecords': [
            {
                'Face': {
                    'FaceId': 'string',
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'ImageId': 'string',
                    'ExternalImageId': 'string',
                    'Confidence': ...
                },
                'FaceDetail': {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'AgeRange': {
                        'Low': 123,
                        'High': 123
                    },
                    'Smile': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Eyeglasses': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Sunglasses': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Gender': {
                        'Value': 'Male'|'Female',
                        'Confidence': ...
                    },
                    'Beard': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Mustache': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'EyesOpen': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'MouthOpen': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Emotions': [
                        {
                            'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                            'Confidence': ...
                        },
                    ],
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                            'X': ...,
                            'Y': ...
                        },
                    ],
                    'Pose': {
                        'Roll': ...,
                        'Yaw': ...,
                        'Pitch': ...
                    },
                    'Quality': {
                        'Brightness': ...,
                        'Sharpness': ...
                    },
                    'Confidence': ...
                }
            },
        ],
        'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270',
        'FaceModelVersion': 'string'
    }
    
    
    """
    pass

def list_collections(NextToken=None, MaxResults=None):
    """
    Returns list of collection IDs in your account. If the result is truncated, the response also provides a NextToken that you can use in the subsequent request to fetch the next set of collection IDs.
    For an example, see  list-collection-procedure .
    This operation requires permissions to perform the rekognition:ListCollections action.
    See also: AWS API Documentation
    
    Examples
    This operation returns a list of Rekognition collections.
    Expected Output:
    
    :example: response = client.list_collections(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: Pagination token from the previous response.

    :type MaxResults: integer
    :param MaxResults: Maximum number of collection IDs to return.

    :rtype: dict
    :return: {
        'CollectionIds': [
            'string',
        ],
        'NextToken': 'string',
        'FaceModelVersions': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_faces(CollectionId=None, NextToken=None, MaxResults=None):
    """
    Returns metadata for faces in the specified collection. This metadata includes information such as the bounding box coordinates, the confidence (that the bounding box contains a face), and face ID. For an example, see  list-faces-in-collection-procedure .
    This operation requires permissions to perform the rekognition:ListFaces action.
    See also: AWS API Documentation
    
    Examples
    This operation lists the faces in a Rekognition collection.
    Expected Output:
    
    :example: response = client.list_faces(
        CollectionId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]
            ID of the collection from which to list the faces.
            

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of faces.

    :type MaxResults: integer
    :param MaxResults: Maximum number of faces to return.

    :rtype: dict
    :return: {
        'Faces': [
            {
                'FaceId': 'string',
                'BoundingBox': {
                    'Width': ...,
                    'Height': ...,
                    'Left': ...,
                    'Top': ...
                },
                'ImageId': 'string',
                'ExternalImageId': 'string',
                'Confidence': ...
            },
        ],
        'NextToken': 'string',
        'FaceModelVersion': 'string'
    }
    
    
    """
    pass

def list_stream_processors(NextToken=None, MaxResults=None):
    """
    Gets a list of stream processors that you have created with .
    See also: AWS API Documentation
    
    
    :example: response = client.list_stream_processors(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more stream processors to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of stream processors.

    :type MaxResults: integer
    :param MaxResults: Maximum number of stream processors you want Rekognition Video to return in the response. The default is 1000.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'StreamProcessors': [
            {
                'Name': 'string',
                'Status': 'STOPPED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'
            },
        ]
    }
    
    
    """
    pass

def recognize_celebrities(Image=None):
    """
    Returns an array of celebrities recognized in the input image. For more information, see  celebrities .
    For each celebrity recognized, the RecognizeCelebrities returns a Celebrity object. The Celebrity object contains the celebrity name, ID, URL links to additional information, match confidence, and a ComparedFace object that you can use to locate the celebrity's face on the image.
    Rekognition does not retain information about which images a celebrity has been recognized in. Your application must store this information and use the Celebrity ID property as a unique identifier for the celebrity. If you don't store the celebrity name or additional information URLs returned by RecognizeCelebrities , you will need the ID to identify the celebrity in a call to the operation.
    You pass the imput image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    For an example, see  celebrities-procedure-image .
    This operation requires permissions to perform the rekognition:RecognizeCelebrities operation.
    See also: AWS API Documentation
    
    
    :example: response = client.recognize_celebrities(
        Image={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        }
    )
    
    
    :type Image: dict
    :param Image: [REQUIRED]
            The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.
            Bytes (bytes) --Blob of image bytes up to 5 MBs.
            S3Object (dict) --Identifies an S3 object as the image source.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :rtype: dict
    :return: {
        'CelebrityFaces': [
            {
                'Urls': [
                    'string',
                ],
                'Name': 'string',
                'Id': 'string',
                'Face': {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'Confidence': ...,
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                            'X': ...,
                            'Y': ...
                        },
                    ],
                    'Pose': {
                        'Roll': ...,
                        'Yaw': ...,
                        'Pitch': ...
                    },
                    'Quality': {
                        'Brightness': ...,
                        'Sharpness': ...
                    }
                },
                'MatchConfidence': ...
            },
        ],
        'UnrecognizedFaces': [
            {
                'BoundingBox': {
                    'Width': ...,
                    'Height': ...,
                    'Left': ...,
                    'Top': ...
                },
                'Confidence': ...,
                'Landmarks': [
                    {
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                        'X': ...,
                        'Y': ...
                    },
                ],
                'Pose': {
                    'Roll': ...,
                    'Yaw': ...,
                    'Pitch': ...
                },
                'Quality': {
                    'Brightness': ...,
                    'Sharpness': ...
                }
            },
        ],
        'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
    }
    
    
    """
    pass

def search_faces(CollectionId=None, FaceId=None, MaxFaces=None, FaceMatchThreshold=None):
    """
    For a given input face ID, searches for matching faces in the collection the face belongs to. You get a face ID when you add a face to the collection using the  IndexFaces operation. The operation compares the features of the input face with faces in the specified collection.
    The operation response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match that is found. Along with the metadata, the response also includes a confidence value for each face match, indicating the confidence that the specific face matches the input face.
    For an example, see  search-face-with-id-procedure .
    This operation requires permissions to perform the rekognition:SearchFaces action.
    See also: AWS API Documentation
    
    Examples
    This operation searches for matching faces in the collection the supplied face belongs to.
    Expected Output:
    
    :example: response = client.search_faces(
        CollectionId='string',
        FaceId='string',
        MaxFaces=123,
        FaceMatchThreshold=...
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]
            ID of the collection the face belongs to.
            

    :type FaceId: string
    :param FaceId: [REQUIRED]
            ID of a face to find matches for in the collection.
            

    :type MaxFaces: integer
    :param MaxFaces: Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.

    :type FaceMatchThreshold: float
    :param FaceMatchThreshold: Optional value specifying the minimum confidence in the face match to return. For example, don't return any matches where confidence in matches is less than 70%.

    :rtype: dict
    :return: {
        'SearchedFaceId': 'string',
        'FaceMatches': [
            {
                'Similarity': ...,
                'Face': {
                    'FaceId': 'string',
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'ImageId': 'string',
                    'ExternalImageId': 'string',
                    'Confidence': ...
                }
            },
        ],
        'FaceModelVersion': 'string'
    }
    
    
    """
    pass

def search_faces_by_image(CollectionId=None, Image=None, MaxFaces=None, FaceMatchThreshold=None):
    """
    For a given input image, first detects the largest face in the image, and then searches the specified collection for matching faces. The operation compares the features of the input face with faces in the specified collection.
    You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    The response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match found. Along with the metadata, the response also includes a similarity indicating how similar the face is to the input face. In the response, the operation also returns the bounding box (and a confidence level that the bounding box contains a face) of the face that Amazon Rekognition used for the input image.
    For an example, see  search-face-with-image-procedure .
    This operation requires permissions to perform the rekognition:SearchFacesByImage action.
    See also: AWS API Documentation
    
    Examples
    This operation searches for faces in a Rekognition collection that match the largest face in an S3 bucket stored image.
    Expected Output:
    
    :example: response = client.search_faces_by_image(
        CollectionId='string',
        Image={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        MaxFaces=123,
        FaceMatchThreshold=...
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]
            ID of the collection to search.
            

    :type Image: dict
    :param Image: [REQUIRED]
            The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.
            Bytes (bytes) --Blob of image bytes up to 5 MBs.
            S3Object (dict) --Identifies an S3 object as the image source.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type MaxFaces: integer
    :param MaxFaces: Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.

    :type FaceMatchThreshold: float
    :param FaceMatchThreshold: (Optional) Specifies the minimum confidence in the face match to return. For example, don't return any matches where confidence in matches is less than 70%.

    :rtype: dict
    :return: {
        'SearchedFaceBoundingBox': {
            'Width': ...,
            'Height': ...,
            'Left': ...,
            'Top': ...
        },
        'SearchedFaceConfidence': ...,
        'FaceMatches': [
            {
                'Similarity': ...,
                'Face': {
                    'FaceId': 'string',
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'ImageId': 'string',
                    'ExternalImageId': 'string',
                    'Confidence': ...
                }
            },
        ],
        'FaceModelVersion': 'string'
    }
    
    
    """
    pass

def start_celebrity_recognition(Video=None, ClientRequestToken=None, NotificationChannel=None, JobTag=None):
    """
    Starts asynchronous recognition of celebrities in a stored video.
    Rekognition Video can detect celebrities in a video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartCelebrityRecognition returns a job identifier (JobId ) which you use to get the results of the analysis. When celebrity recognition analysis is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel . To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call and pass the job identifier (JobId ) from the initial call to StartCelebrityRecognition . For more information, see  celebrities .
    See also: AWS API Documentation
    
    
    :example: response = client.start_celebrity_recognition(
        Video={
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        ClientRequestToken='string',
        NotificationChannel={
            'SNSTopicArn': 'string',
            'RoleArn': 'string'
        },
        JobTag='string'
    )
    
    
    :type Video: dict
    :param Video: [REQUIRED]
            The video in which you want to recognize celebrities. The video must be stored in an Amazon S3 bucket.
            S3Object (dict) --The Amazon S3 bucket name and file name for the video.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartCelebrityRecognition requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon SNS topic ARN that you want Rekognition Video to publish the completion status of the celebrity recognition analysis to.
            SNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
            RoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.
            

    :type JobTag: string
    :param JobTag: Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic.

    :rtype: dict
    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

def start_content_moderation(Video=None, MinConfidence=None, ClientRequestToken=None, NotificationChannel=None, JobTag=None):
    """
    Starts asynchronous detection of explicit or suggestive adult content in a stored video.
    Rekognition Video can moderate content in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartContentModeration returns a job identifier (JobId ) which you use to get the results of the analysis. When content moderation analysis is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel .
    To get the results of the content moderation analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call and pass the job identifier (JobId ) from the initial call to StartContentModeration . For more information, see  moderation .
    See also: AWS API Documentation
    
    
    :example: response = client.start_content_moderation(
        Video={
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        MinConfidence=...,
        ClientRequestToken='string',
        NotificationChannel={
            'SNSTopicArn': 'string',
            'RoleArn': 'string'
        },
        JobTag='string'
    )
    
    
    :type Video: dict
    :param Video: [REQUIRED]
            The video in which you want to moderate content. The video must be stored in an Amazon S3 bucket.
            S3Object (dict) --The Amazon S3 bucket name and file name for the video.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type MinConfidence: float
    :param MinConfidence: Specifies the minimum confidence that Amazon Rekognition must have in order to return a moderated content label. Confidence represents how certain Amazon Rekognition is that the moderated content is correctly identified. 0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition doesn't return any moderated content labels with a confidence level lower than this specified value.

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartContentModeration requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon SNS topic ARN that you want Rekognition Video to publish the completion status of the content moderation analysis to.
            SNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
            RoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.
            

    :type JobTag: string
    :param JobTag: Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic.

    :rtype: dict
    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

def start_face_detection(Video=None, ClientRequestToken=None, NotificationChannel=None, FaceAttributes=None, JobTag=None):
    """
    Starts asynchronous detection of faces in a stored video.
    Rekognition Video can detect faces in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartFaceDetection returns a job identifier (JobId ) that you use to get the results of the operation. When face detection is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel . To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call and pass the job identifier (JobId ) from the initial call to StartFaceDetection . For more information, see  faces-video .
    See also: AWS API Documentation
    
    
    :example: response = client.start_face_detection(
        Video={
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        ClientRequestToken='string',
        NotificationChannel={
            'SNSTopicArn': 'string',
            'RoleArn': 'string'
        },
        FaceAttributes='DEFAULT'|'ALL',
        JobTag='string'
    )
    
    
    :type Video: dict
    :param Video: [REQUIRED]
            The video in which you want to detect faces. The video must be stored in an Amazon S3 bucket.
            S3Object (dict) --The Amazon S3 bucket name and file name for the video.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartFaceDetection requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type NotificationChannel: dict
    :param NotificationChannel: The ARN of the Amazon SNS topic to which you want Rekognition Video to publish the completion status of the face detection operation.
            SNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
            RoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.
            

    :type FaceAttributes: string
    :param FaceAttributes: The face attributes you want returned.
            DEFAULT - The following subset of facial attributes are returned: BoundingBox, Confidence, Pose, Quality and Landmarks.ALL - All facial attributes are returned.
            

    :type JobTag: string
    :param JobTag: Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic.

    :rtype: dict
    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

def start_face_search(Video=None, ClientRequestToken=None, FaceMatchThreshold=None, CollectionId=None, NotificationChannel=None, JobTag=None):
    """
    Starts the asynchronous search for faces in a collection that match the faces of persons detected in a stored video.
    The video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartFaceSearch returns a job identifier (JobId ) which you use to get the search results once the search has completed. When searching is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel . To get the search results, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call and pass the job identifier (JobId ) from the initial call to StartFaceSearch . For more information, see  collections-search-person .
    See also: AWS API Documentation
    
    
    :example: response = client.start_face_search(
        Video={
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        ClientRequestToken='string',
        FaceMatchThreshold=...,
        CollectionId='string',
        NotificationChannel={
            'SNSTopicArn': 'string',
            'RoleArn': 'string'
        },
        JobTag='string'
    )
    
    
    :type Video: dict
    :param Video: [REQUIRED]
            The video you want to search. The video must be stored in an Amazon S3 bucket.
            S3Object (dict) --The Amazon S3 bucket name and file name for the video.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartFaceSearch requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type FaceMatchThreshold: float
    :param FaceMatchThreshold: The minimum confidence in the person match to return. For example, don't return any matches where confidence in matches is less than 70%.

    :type CollectionId: string
    :param CollectionId: [REQUIRED]
            ID of the collection that contains the faces you want to search for.
            

    :type NotificationChannel: dict
    :param NotificationChannel: The ARN of the Amazon SNS topic to which you want Rekognition Video to publish the completion status of the search.
            SNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
            RoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.
            

    :type JobTag: string
    :param JobTag: Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic.

    :rtype: dict
    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

def start_label_detection(Video=None, ClientRequestToken=None, MinConfidence=None, NotificationChannel=None, JobTag=None):
    """
    Starts asynchronous detection of labels in a stored video.
    Rekognition Video can detect labels in a video. Labels are instances of real-world entities. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; concepts like landscape, evening, and nature; and activities like a person getting out of a car or a person skiing.
    The video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartLabelDetection returns a job identifier (JobId ) which you use to get the results of the operation. When label detection is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel .
    To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call and pass the job identifier (JobId ) from the initial call to StartLabelDetection .
    See also: AWS API Documentation
    
    
    :example: response = client.start_label_detection(
        Video={
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        ClientRequestToken='string',
        MinConfidence=...,
        NotificationChannel={
            'SNSTopicArn': 'string',
            'RoleArn': 'string'
        },
        JobTag='string'
    )
    
    
    :type Video: dict
    :param Video: [REQUIRED]
            The video in which you want to detect labels. The video must be stored in an Amazon S3 bucket.
            S3Object (dict) --The Amazon S3 bucket name and file name for the video.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartLabelDetection requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type MinConfidence: float
    :param MinConfidence: Specifies the minimum confidence that Rekognition Video must have in order to return a detected label. Confidence represents how certain Amazon Rekognition is that a label is correctly identified.0 is the lowest confidence. 100 is the highest confidence. Rekognition Video doesn't return any labels with a confidence level lower than this specified value.
            If you don't specify MinConfidence , the operation returns labels with confidence values greater than or equal to 50 percent.
            

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon SNS topic ARN you want Rekognition Video to publish the completion status of the label detection operation to.
            SNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
            RoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.
            

    :type JobTag: string
    :param JobTag: Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic.

    :rtype: dict
    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

def start_person_tracking(Video=None, ClientRequestToken=None, NotificationChannel=None, JobTag=None):
    """
    Starts the asynchronous tracking of persons in a stored video.
    Rekognition Video can track persons in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartPersonTracking returns a job identifier (JobId ) which you use to get the results of the operation. When label detection is finished, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel .
    To get the results of the person detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call and pass the job identifier (JobId ) from the initial call to StartPersonTracking .
    See also: AWS API Documentation
    
    
    :example: response = client.start_person_tracking(
        Video={
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        ClientRequestToken='string',
        NotificationChannel={
            'SNSTopicArn': 'string',
            'RoleArn': 'string'
        },
        JobTag='string'
    )
    
    
    :type Video: dict
    :param Video: [REQUIRED]
            The video in which you want to detect people. The video must be stored in an Amazon S3 bucket.
            S3Object (dict) --The Amazon S3 bucket name and file name for the video.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartPersonTracking requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon SNS topic ARN you want Rekognition Video to publish the completion status of the people detection operation to.
            SNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
            RoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.
            

    :type JobTag: string
    :param JobTag: Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic.

    :rtype: dict
    :return: {
        'JobId': 'string'
    }
    
    
    """
    pass

def start_stream_processor(Name=None):
    """
    Starts processing a stream processor. You create a stream processor by calling . To tell StartStreamProcessor which stream processor to start, use the value of the Name field specified in the call to CreateStreamProcessor .
    See also: AWS API Documentation
    
    
    :example: response = client.start_stream_processor(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the stream processor to start processing.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def stop_stream_processor(Name=None):
    """
    Stops a running stream processor that was created by .
    See also: AWS API Documentation
    
    
    :example: response = client.stop_stream_processor(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of a stream processor created by .
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

