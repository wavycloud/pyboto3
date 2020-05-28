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

def compare_faces(SourceImage=None, TargetImage=None, SimilarityThreshold=None, QualityFilter=None):
    """
    Compares a face in the source input image with each of the 100 largest faces detected in the target input image.
    You pass the input and target images either as base64-encoded image bytes or as references to images in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn\'t supported. The image must be formatted as a PNG or JPEG file.
    In response, the operation returns an array of face matches ordered by similarity score in descending order. For each face match, the response provides a bounding box of the face, facial landmarks, pose details (pitch, role, and yaw), quality (brightness and sharpness), and confidence value (indicating the level of confidence that the bounding box contains a face). The response also provides a similarity score, which indicates how closely the faces match.
    The QualityFilter input parameter allows you to filter out detected faces that don\xe2\x80\x99t meet a required quality bar. The quality bar is based on a variety of common use cases. Use QualityFilter to set the quality bar by specifying LOW , MEDIUM , or HIGH . If you do not want to filter detected faces, specify NONE . The default value is NONE .
    If the image doesn\'t contain Exif metadata, CompareFaces returns orientation information for the source and target images. Use these values to display the images with the correct image orientation.
    If no faces are detected in the source or target images, CompareFaces returns an InvalidParameterException error.
    For an example, see Comparing Faces in Images in the Amazon Rekognition Developer Guide.
    This operation requires permissions to perform the rekognition:CompareFaces action.
    See also: AWS API Documentation
    
    Exceptions
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
        SimilarityThreshold=...,
        QualityFilter='NONE'|'AUTO'|'LOW'|'MEDIUM'|'HIGH'
    )
    
    
    :type SourceImage: dict
    :param SourceImage: [REQUIRED]\nThe input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.\nIf you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the Bytes field. For more information, see Images in the Amazon Rekognition developer guide.\n\nBytes (bytes) --Blob of image bytes up to 5 MBs.\n\nS3Object (dict) --Identifies an S3 object as the image source.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type TargetImage: dict
    :param TargetImage: [REQUIRED]\nThe target image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.\nIf you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the Bytes field. For more information, see Images in the Amazon Rekognition developer guide.\n\nBytes (bytes) --Blob of image bytes up to 5 MBs.\n\nS3Object (dict) --Identifies an S3 object as the image source.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type SimilarityThreshold: float
    :param SimilarityThreshold: The minimum level of confidence in the face matches that a match must meet to be included in the FaceMatches array.

    :type QualityFilter: string
    :param QualityFilter: A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren\'t compared. If you specify AUTO , Amazon Rekognition chooses the quality bar. If you specify LOW , MEDIUM , or HIGH , filtering removes all faces that don\xe2\x80\x99t meet the chosen quality bar. The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object that\'s misidentified as a face, a face that\'s too blurry, or a face with a pose that\'s too extreme to use. If you specify NONE , no filtering is performed. The default value is NONE .\nTo use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
                    'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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


Response Structure

(dict) --

SourceImageFace (dict) --
The face in the source image that was used for comparison.

BoundingBox (dict) --
Bounding box of the face.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Confidence (float) --
Confidence level that the selected bounding box contains a face.



FaceMatches (list) --
An array of faces in the target image that match the source image face. Each CompareFacesMatch object provides the bounding box, the confidence level that the bounding box contains a face, and the similarity score for the face in the bounding box and the face in the source image.

(dict) --
Provides information about a face in a target image that matches the source image face analyzed by CompareFaces . The Face property contains the bounding box of the face in the target image. The Similarity property is the confidence that the source image face matches the face in the bounding box.

Similarity (float) --
Level of confidence that the faces match.

Face (dict) --
Provides face metadata (bounding box and confidence that the bounding box actually contains a face).

BoundingBox (dict) --
Bounding box of the face.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Confidence (float) --
Level of confidence that what the bounding box contains is a face.

Landmarks (list) --
An array of facial landmarks.

(dict) --
Indicates the location of the landmark on the face.

Type (string) --
Type of landmark.

X (float) --
The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --
The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --
Indicates the pose of the face as determined by its pitch, roll, and yaw.

Roll (float) --
Value representing the face rotation on the roll axis.

Yaw (float) --
Value representing the face rotation on the yaw axis.

Pitch (float) --
Value representing the face rotation on the pitch axis.



Quality (dict) --
Identifies face image brightness and sharpness.

Brightness (float) --
Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --
Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.









UnmatchedFaces (list) --
An array of faces in the target image that did not match the source image face.

(dict) --
Provides face metadata for target image faces that are analyzed by CompareFaces and RecognizeCelebrities .

BoundingBox (dict) --
Bounding box of the face.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Confidence (float) --
Level of confidence that what the bounding box contains is a face.

Landmarks (list) --
An array of facial landmarks.

(dict) --
Indicates the location of the landmark on the face.

Type (string) --
Type of landmark.

X (float) --
The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --
The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --
Indicates the pose of the face as determined by its pitch, roll, and yaw.

Roll (float) --
Value representing the face rotation on the roll axis.

Yaw (float) --
Value representing the face rotation on the yaw axis.

Pitch (float) --
Value representing the face rotation on the pitch axis.



Quality (dict) --
Identifies face image brightness and sharpness.

Brightness (float) --
Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --
Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.







SourceImageOrientationCorrection (string) --
The value of SourceImageOrientationCorrection is always null.
If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image\'s orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don\'t contain Exif metadata.
Amazon Rekognition doesn\xe2\x80\x99t perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates aren\'t translated and represent the object locations before the image is rotated.

TargetImageOrientationCorrection (string) --
The value of TargetImageOrientationCorrection is always null.
If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image\'s orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don\'t contain Exif metadata.
Amazon Rekognition doesn\xe2\x80\x99t perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates aren\'t translated and represent the object locations before the image is rotated.







Exceptions

Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.ImageTooLargeException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.InvalidImageFormatException

Examples
This operation compares the largest face detected in the source image with each face detected in the target image.
response = client.compare_faces(
    SimilarityThreshold=90,
    SourceImage={
        'S3Object': {
            'Bucket': 'mybucket',
            'Name': 'mysourceimage',
        },
    },
    TargetImage={
        'S3Object': {
            'Bucket': 'mybucket',
            'Name': 'mytargetimage',
        },
    },
)

print(response)


Expected Output:
{
    'FaceMatches': [
        {
            'Face': {
                'BoundingBox': {
                    'Height': 0.33481481671333313,
                    'Left': 0.31888890266418457,
                    'Top': 0.4933333396911621,
                    'Width': 0.25,
                },
                'Confidence': 99.9991226196289,
            },
            'Similarity': 100,
        },
    ],
    'SourceImageFace': {
        'BoundingBox': {
            'Height': 0.33481481671333313,
            'Left': 0.31888890266418457,
            'Top': 0.4933333396911621,
            'Width': 0.25,
        },
        'Confidence': 99.9991226196289,
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
    
    
    :returns: 
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.ImageTooLargeException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.InvalidImageFormatException
    
    """
    pass

def create_collection(CollectionId=None):
    """
    Creates a collection in an AWS Region. You can add faces to the collection using the  IndexFaces operation.
    For example, you might create collections, one for each of your application users. A user can then index faces using the IndexFaces operation and persist results in a specific collection. Then, a user can search the collection for faces in the user-specific container.
    When you create a collection, it is associated with the latest version of the face model version.
    This operation requires permissions to perform the rekognition:CreateCollection action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation creates a Rekognition collection for storing image data.
    Expected Output:
    
    :example: response = client.create_collection(
        CollectionId='string'
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]\nID for the collection that you are creating.\n

    :rtype: dict
ReturnsResponse Syntax{
    'StatusCode': 123,
    'CollectionArn': 'string',
    'FaceModelVersion': 'string'
}


Response Structure

(dict) --
StatusCode (integer) --HTTP status code indicating the result of the operation.

CollectionArn (string) --Amazon Resource Name (ARN) of the collection. You can use this to manage permissions on your resources.

FaceModelVersion (string) --Version number of the face detection model associated with the collection you are creating.






Exceptions

Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceAlreadyExistsException

Examples
This operation creates a Rekognition collection for storing image data.
response = client.create_collection(
    CollectionId='myphotos',
)

print(response)


Expected Output:
{
    'CollectionArn': 'aws:rekognition:us-west-2:123456789012:collection/myphotos',
    'StatusCode': 200,
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'StatusCode': 123,
        'CollectionArn': 'string',
        'FaceModelVersion': 'string'
    }
    
    
    """
    pass

def create_project(ProjectName=None):
    """
    Creates a new Amazon Rekognition Custom Labels project. A project is a logical grouping of resources (images, Labels, models) and operations (training, evaluation and detection).
    This operation requires permissions to perform the rekognition:CreateProject action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_project(
        ProjectName='string'
    )
    
    
    :type ProjectName: string
    :param ProjectName: [REQUIRED]\nThe name of the project to create.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ProjectArn': 'string'
}


Response Structure

(dict) --
ProjectArn (string) --The Amazon Resource Name (ARN) of the new project. You can use the ARN to configure IAM access to the project.






Exceptions

Rekognition.Client.exceptions.ResourceInUseException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'ProjectArn': 'string'
    }
    
    
    """
    pass

def create_project_version(ProjectArn=None, VersionName=None, OutputConfig=None, TrainingData=None, TestingData=None):
    """
    Creates a new version of a model and begins training. Models are managed as part of an Amazon Rekognition Custom Labels project. You can specify one training dataset and one testing dataset. The response from CreateProjectVersion is an Amazon Resource Name (ARN) for the version of the model.
    Training takes a while to complete. You can get the current status by calling  DescribeProjectVersions .
    Once training has successfully completed, call  DescribeProjectVersions to get the training results and evaluate the model.
    After evaluating the model, you start the model by calling  StartProjectVersion .
    This operation requires permissions to perform the rekognition:CreateProjectVersion action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_project_version(
        ProjectArn='string',
        VersionName='string',
        OutputConfig={
            'S3Bucket': 'string',
            'S3KeyPrefix': 'string'
        },
        TrainingData={
            'Assets': [
                {
                    'GroundTruthManifest': {
                        'S3Object': {
                            'Bucket': 'string',
                            'Name': 'string',
                            'Version': 'string'
                        }
                    }
                },
            ]
        },
        TestingData={
            'Assets': [
                {
                    'GroundTruthManifest': {
                        'S3Object': {
                            'Bucket': 'string',
                            'Name': 'string',
                            'Version': 'string'
                        }
                    }
                },
            ],
            'AutoCreate': True|False
        }
    )
    
    
    :type ProjectArn: string
    :param ProjectArn: [REQUIRED]\nThe ARN of the Amazon Rekognition Custom Labels project that manages the model that you want to train.\n

    :type VersionName: string
    :param VersionName: [REQUIRED]\nA name for the version of the model. This value must be unique.\n

    :type OutputConfig: dict
    :param OutputConfig: [REQUIRED]\nThe Amazon S3 location to store the results of training.\n\nS3Bucket (string) --The S3 bucket where training output is placed.\n\nS3KeyPrefix (string) --The prefix applied to the training output files.\n\n\n

    :type TrainingData: dict
    :param TrainingData: [REQUIRED]\nThe dataset to use for training.\n\nAssets (list) --A Sagemaker GroundTruth manifest file that contains the training images (assets).\n\n(dict) --Assets are the images that you use to train and evaluate a model version. Assets are referenced by Sagemaker GroundTruth manifest files.\n\nGroundTruthManifest (dict) --The S3 bucket that contains the Ground Truth manifest file.\n\nS3Object (dict) --Provides the S3 bucket name and object name.\nThe region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.\nFor Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition Developer Guide.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n\n\n\n\n\n\n

    :type TestingData: dict
    :param TestingData: [REQUIRED]\nThe dataset to use for testing.\n\nAssets (list) --The assets used for testing.\n\n(dict) --Assets are the images that you use to train and evaluate a model version. Assets are referenced by Sagemaker GroundTruth manifest files.\n\nGroundTruthManifest (dict) --The S3 bucket that contains the Ground Truth manifest file.\n\nS3Object (dict) --Provides the S3 bucket name and object name.\nThe region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.\nFor Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition Developer Guide.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n\n\n\n\n\nAutoCreate (boolean) --If specified, Amazon Rekognition Custom Labels creates a testing dataset with an 80/20 split of the training dataset.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ProjectVersionArn': 'string'
}


Response Structure

(dict) --

ProjectVersionArn (string) --
The ARN of the model version that was created. Use DescribeProjectVersion to get the current status of the training operation.







Exceptions

Rekognition.Client.exceptions.ResourceInUseException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'ProjectVersionArn': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.ResourceInUseException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    
    """
    pass

def create_stream_processor(Input=None, Output=None, Name=None, Settings=None, RoleArn=None):
    """
    Creates an Amazon Rekognition stream processor that you can use to detect and recognize faces in a streaming video.
    Amazon Rekognition Video is a consumer of live video from Amazon Kinesis Video Streams. Amazon Rekognition Video sends analysis results to Amazon Kinesis Data Streams.
    You provide as input a Kinesis video stream (Input ) and a Kinesis data stream (Output ) stream. You also specify the face recognition criteria in Settings . For example, the collection containing faces that you want to recognize. Use Name to assign an identifier for the stream processor. You use Name to manage the stream processor. For example, you can start processing the source video by calling  StartStreamProcessor with the Name field.
    After you have finished analyzing a streaming video, use  StopStreamProcessor to stop processing. You can delete the stream processor by calling  DeleteStreamProcessor .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Input: [REQUIRED]\nKinesis video stream stream that provides the source streaming video. If you are using the AWS CLI, the parameter name is StreamProcessorInput .\n\nKinesisVideoStream (dict) --The Kinesis video stream input stream for the source streaming video.\n\nArn (string) --ARN of the Kinesis video stream stream that streams the source video.\n\n\n\n\n

    :type Output: dict
    :param Output: [REQUIRED]\nKinesis data stream stream to which Amazon Rekognition Video puts the analysis results. If you are using the AWS CLI, the parameter name is StreamProcessorOutput .\n\nKinesisDataStream (dict) --The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor streams the analysis results.\n\nArn (string) --ARN of the output Amazon Kinesis Data Streams stream.\n\n\n\n\n

    :type Name: string
    :param Name: [REQUIRED]\nAn identifier you assign to the stream processor. You can use Name to manage the stream processor. For example, you can get the current status of the stream processor by calling DescribeStreamProcessor . Name is idempotent.\n

    :type Settings: dict
    :param Settings: [REQUIRED]\nFace recognition input parameters to be used by the stream processor. Includes the collection to use for face recognition and the face attributes to detect.\n\nFaceSearch (dict) --Face search settings to use on a streaming video.\n\nCollectionId (string) --The ID of a collection that contains faces that you want to search for.\n\nFaceMatchThreshold (float) --Minimum face match confidence score that must be met to return a result for a recognized face. Default is 80. 0 is the lowest confidence. 100 is the highest confidence.\n\n\n\n\n

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nARN of the IAM role that allows access to the stream processor.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamProcessorArn': 'string'
}


Response Structure

(dict) --

StreamProcessorArn (string) --
ARN for the newly create stream processor.







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.ResourceInUseException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'StreamProcessorArn': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.ResourceInUseException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    
    """
    pass

def delete_collection(CollectionId=None):
    """
    Deletes the specified collection. Note that this operation removes all faces in the collection. For an example, see  delete-collection-procedure .
    This operation requires permissions to perform the rekognition:DeleteCollection action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation deletes a Rekognition collection.
    Expected Output:
    
    :example: response = client.delete_collection(
        CollectionId='string'
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]\nID of the collection to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'StatusCode': 123
}


Response Structure

(dict) --
StatusCode (integer) --HTTP status code that indicates the result of the operation.






Exceptions

Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException

Examples
This operation deletes a Rekognition collection.
response = client.delete_collection(
    CollectionId='myphotos',
)

print(response)


Expected Output:
{
    'StatusCode': 200,
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    Exceptions
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
    :param CollectionId: [REQUIRED]\nCollection from which to remove the specific faces.\n

    :type FaceIds: list
    :param FaceIds: [REQUIRED]\nAn array of face IDs to delete.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DeletedFaces': [
        'string',
    ]
}


Response Structure

(dict) --

DeletedFaces (list) --
An array of strings (face IDs) of the faces that were deleted.

(string) --








Exceptions

Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException

Examples
This operation deletes one or more faces from a Rekognition collection.
response = client.delete_faces(
    CollectionId='myphotos',
    FaceIds=[
        'ff43d742-0c13-5d16-a3e8-03d3f58e980b',
    ],
)

print(response)


Expected Output:
{
    'DeletedFaces': [
        'ff43d742-0c13-5d16-a3e8-03d3f58e980b',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'DeletedFaces': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def delete_project(ProjectArn=None):
    """
    Deletes an Amazon Rekognition Custom Labels project. To delete a project you must first delete all versions of the model associated with the project. To delete a version of a model, see  DeleteProjectVersion .
    This operation requires permissions to perform the rekognition:DeleteProject action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_project(
        ProjectArn='string'
    )
    
    
    :type ProjectArn: string
    :param ProjectArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the project that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Status': 'CREATING'|'CREATED'|'DELETING'
}


Response Structure

(dict) --
Status (string) --The current status of the delete project operation.






Exceptions

Rekognition.Client.exceptions.ResourceInUseException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'Status': 'CREATING'|'CREATED'|'DELETING'
    }
    
    
    """
    pass

def delete_project_version(ProjectVersionArn=None):
    """
    Deletes a version of a model.
    You must first stop the model before you can delete it. To check if a model is running, use the Status field returned from  DescribeProjectVersions . To stop a running model call  StopProjectVersion .
    This operation requires permissions to perform the rekognition:DeleteProjectVersion action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_project_version(
        ProjectVersionArn='string'
    )
    
    
    :type ProjectVersionArn: string
    :param ProjectVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the model version that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Status': 'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'|'TRAINING_FAILED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'|'STOPPED'|'DELETING'
}


Response Structure

(dict) --
Status (string) --The status of the deletion operation.






Exceptions

Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ResourceInUseException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'Status': 'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'|'TRAINING_FAILED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'|'STOPPED'|'DELETING'
    }
    
    
    """
    pass

def delete_stream_processor(Name=None):
    """
    Deletes the stream processor identified by Name . You assign the value for Name when you create the stream processor with  CreateStreamProcessor . You might not be able to use the same name for a stream processor for a few seconds after calling DeleteStreamProcessor .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_stream_processor(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the stream processor you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ResourceInUseException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {}
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ResourceInUseException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    
    """
    pass

def describe_collection(CollectionId=None):
    """
    Describes the specified collection. You can use DescribeCollection to get information, such as the number of faces indexed into a collection and the version of the model used by the collection for face detection.
    For more information, see Describing a Collection in the Amazon Rekognition Developer Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_collection(
        CollectionId='string'
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]\nThe ID of the collection to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'FaceCount': 123,
    'FaceModelVersion': 'string',
    'CollectionARN': 'string',
    'CreationTimestamp': datetime(2015, 1, 1)
}


Response Structure

(dict) --
FaceCount (integer) --The number of faces that are indexed into the collection. To index faces into a collection, use  IndexFaces .

FaceModelVersion (string) --The version of the face model that\'s used by the collection for face detection.
For more information, see Model Versioning in the Amazon Rekognition Developer Guide.

CollectionARN (string) --The Amazon Resource Name (ARN) of the collection.

CreationTimestamp (datetime) --The number of milliseconds since the Unix epoch time until the creation of the collection. The Unix epoch time is 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970.






Exceptions

Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException


    :return: {
        'FaceCount': 123,
        'FaceModelVersion': 'string',
        'CollectionARN': 'string',
        'CreationTimestamp': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_project_versions(ProjectArn=None, VersionNames=None, NextToken=None, MaxResults=None):
    """
    Lists and describes the models in an Amazon Rekognition Custom Labels project. You can specify up to 10 model versions in ProjectVersionArns . If you don\'t specify a value, descriptions for all models are returned.
    This operation requires permissions to perform the rekognition:DescribeProjectVersions action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_project_versions(
        ProjectArn='string',
        VersionNames=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ProjectArn: string
    :param ProjectArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the project that contains the models you want to describe.\n

    :type VersionNames: list
    :param VersionNames: A list of model version names that you want to describe. You can add up to 10 model version names to the list. If you don\'t specify a value, all model descriptions are returned.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'ProjectVersionDescriptions': [
        {
            'ProjectVersionArn': 'string',
            'CreationTimestamp': datetime(2015, 1, 1),
            'MinInferenceUnits': 123,
            'Status': 'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'|'TRAINING_FAILED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'|'STOPPED'|'DELETING',
            'StatusMessage': 'string',
            'BillableTrainingTimeInSeconds': 123,
            'TrainingEndTimestamp': datetime(2015, 1, 1),
            'OutputConfig': {
                'S3Bucket': 'string',
                'S3KeyPrefix': 'string'
            },
            'TrainingDataResult': {
                'Input': {
                    'Assets': [
                        {
                            'GroundTruthManifest': {
                                'S3Object': {
                                    'Bucket': 'string',
                                    'Name': 'string',
                                    'Version': 'string'
                                }
                            }
                        },
                    ]
                },
                'Output': {
                    'Assets': [
                        {
                            'GroundTruthManifest': {
                                'S3Object': {
                                    'Bucket': 'string',
                                    'Name': 'string',
                                    'Version': 'string'
                                }
                            }
                        },
                    ]
                }
            },
            'TestingDataResult': {
                'Input': {
                    'Assets': [
                        {
                            'GroundTruthManifest': {
                                'S3Object': {
                                    'Bucket': 'string',
                                    'Name': 'string',
                                    'Version': 'string'
                                }
                            }
                        },
                    ],
                    'AutoCreate': True|False
                },
                'Output': {
                    'Assets': [
                        {
                            'GroundTruthManifest': {
                                'S3Object': {
                                    'Bucket': 'string',
                                    'Name': 'string',
                                    'Version': 'string'
                                }
                            }
                        },
                    ],
                    'AutoCreate': True|False
                }
            },
            'EvaluationResult': {
                'F1Score': ...,
                'Summary': {
                    'S3Object': {
                        'Bucket': 'string',
                        'Name': 'string',
                        'Version': 'string'
                    }
                }
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ProjectVersionDescriptions (list) --
A list of model descriptions. The list is sorted by the creation date and time of the model versions, latest to earliest.

(dict) --
The description of a version of a model.

ProjectVersionArn (string) --
The Amazon Resource Name (ARN) of the model version.

CreationTimestamp (datetime) --
The Unix datetime for the date and time that training started.

MinInferenceUnits (integer) --
The minimum number of inference units used by the model. For more information, see  StartProjectVersion .

Status (string) --
The current status of the model version.

StatusMessage (string) --
A descriptive message for an error or warning that occurred.

BillableTrainingTimeInSeconds (integer) --
The duration, in seconds, that the model version has been billed for training. This value is only returned if the model version has been successfully trained.

TrainingEndTimestamp (datetime) --
The Unix date and time that training of the model ended.

OutputConfig (dict) --
The location where training results are saved.

S3Bucket (string) --
The S3 bucket where training output is placed.

S3KeyPrefix (string) --
The prefix applied to the training output files.



TrainingDataResult (dict) --
The manifest file that represents the training results.

Input (dict) --
The training assets that you supplied for training.

Assets (list) --
A Sagemaker GroundTruth manifest file that contains the training images (assets).

(dict) --
Assets are the images that you use to train and evaluate a model version. Assets are referenced by Sagemaker GroundTruth manifest files.

GroundTruthManifest (dict) --
The S3 bucket that contains the Ground Truth manifest file.

S3Object (dict) --
Provides the S3 bucket name and object name.
The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition Developer Guide.

Bucket (string) --
Name of the S3 bucket.

Name (string) --
S3 object key name.

Version (string) --
If the bucket is versioning enabled, you can specify the object version.











Output (dict) --
The images (assets) that were actually trained by Amazon Rekognition Custom Labels.

Assets (list) --
A Sagemaker GroundTruth manifest file that contains the training images (assets).

(dict) --
Assets are the images that you use to train and evaluate a model version. Assets are referenced by Sagemaker GroundTruth manifest files.

GroundTruthManifest (dict) --
The S3 bucket that contains the Ground Truth manifest file.

S3Object (dict) --
Provides the S3 bucket name and object name.
The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition Developer Guide.

Bucket (string) --
Name of the S3 bucket.

Name (string) --
S3 object key name.

Version (string) --
If the bucket is versioning enabled, you can specify the object version.













TestingDataResult (dict) --
The manifest file that represents the testing results.

Input (dict) --
The testing dataset that was supplied for training.

Assets (list) --
The assets used for testing.

(dict) --
Assets are the images that you use to train and evaluate a model version. Assets are referenced by Sagemaker GroundTruth manifest files.

GroundTruthManifest (dict) --
The S3 bucket that contains the Ground Truth manifest file.

S3Object (dict) --
Provides the S3 bucket name and object name.
The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition Developer Guide.

Bucket (string) --
Name of the S3 bucket.

Name (string) --
S3 object key name.

Version (string) --
If the bucket is versioning enabled, you can specify the object version.









AutoCreate (boolean) --
If specified, Amazon Rekognition Custom Labels creates a testing dataset with an 80/20 split of the training dataset.



Output (dict) --
The subset of the dataset that was actually tested. Some images (assets) might not be tested due to file formatting and other issues.

Assets (list) --
The assets used for testing.

(dict) --
Assets are the images that you use to train and evaluate a model version. Assets are referenced by Sagemaker GroundTruth manifest files.

GroundTruthManifest (dict) --
The S3 bucket that contains the Ground Truth manifest file.

S3Object (dict) --
Provides the S3 bucket name and object name.
The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition Developer Guide.

Bucket (string) --
Name of the S3 bucket.

Name (string) --
S3 object key name.

Version (string) --
If the bucket is versioning enabled, you can specify the object version.









AutoCreate (boolean) --
If specified, Amazon Rekognition Custom Labels creates a testing dataset with an 80/20 split of the training dataset.





EvaluationResult (dict) --
The training results. EvaluationResult is only returned if training is successful.

F1Score (float) --
The F1 score for the evaluation of all labels. The F1 score metric evaluates the overall precision and recall performance of the model as a single value. A higher value indicates better precision and recall performance. A lower score indicates that precision, recall, or both are performing poorly.

Summary (dict) --
The S3 bucket that contains the training summary.

S3Object (dict) --
Provides the S3 bucket name and object name.
The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition Developer Guide.

Bucket (string) --
Name of the S3 bucket.

Name (string) --
S3 object key name.

Version (string) --
If the bucket is versioning enabled, you can specify the object version.











NextToken (string) --
If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.







Exceptions

Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'ProjectVersionDescriptions': [
            {
                'ProjectVersionArn': 'string',
                'CreationTimestamp': datetime(2015, 1, 1),
                'MinInferenceUnits': 123,
                'Status': 'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'|'TRAINING_FAILED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'|'STOPPED'|'DELETING',
                'StatusMessage': 'string',
                'BillableTrainingTimeInSeconds': 123,
                'TrainingEndTimestamp': datetime(2015, 1, 1),
                'OutputConfig': {
                    'S3Bucket': 'string',
                    'S3KeyPrefix': 'string'
                },
                'TrainingDataResult': {
                    'Input': {
                        'Assets': [
                            {
                                'GroundTruthManifest': {
                                    'S3Object': {
                                        'Bucket': 'string',
                                        'Name': 'string',
                                        'Version': 'string'
                                    }
                                }
                            },
                        ]
                    },
                    'Output': {
                        'Assets': [
                            {
                                'GroundTruthManifest': {
                                    'S3Object': {
                                        'Bucket': 'string',
                                        'Name': 'string',
                                        'Version': 'string'
                                    }
                                }
                            },
                        ]
                    }
                },
                'TestingDataResult': {
                    'Input': {
                        'Assets': [
                            {
                                'GroundTruthManifest': {
                                    'S3Object': {
                                        'Bucket': 'string',
                                        'Name': 'string',
                                        'Version': 'string'
                                    }
                                }
                            },
                        ],
                        'AutoCreate': True|False
                    },
                    'Output': {
                        'Assets': [
                            {
                                'GroundTruthManifest': {
                                    'S3Object': {
                                        'Bucket': 'string',
                                        'Name': 'string',
                                        'Version': 'string'
                                    }
                                }
                            },
                        ],
                        'AutoCreate': True|False
                    }
                },
                'EvaluationResult': {
                    'F1Score': ...,
                    'Summary': {
                        'S3Object': {
                            'Bucket': 'string',
                            'Name': 'string',
                            'Version': 'string'
                        }
                    }
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.InvalidPaginationTokenException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    
    """
    pass

def describe_projects(NextToken=None, MaxResults=None):
    """
    Lists and gets information about your Amazon Rekognition Custom Labels projects.
    This operation requires permissions to perform the rekognition:DescribeProjects action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_projects(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'ProjectDescriptions': [
        {
            'ProjectArn': 'string',
            'CreationTimestamp': datetime(2015, 1, 1),
            'Status': 'CREATING'|'CREATED'|'DELETING'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ProjectDescriptions (list) --
A list of project descriptions. The list is sorted by the date and time the projects are created.

(dict) --
A description of a Amazon Rekognition Custom Labels project.

ProjectArn (string) --
The Amazon Resource Name (ARN) of the project.

CreationTimestamp (datetime) --
The Unix timestamp for the date and time that the project was created.

Status (string) --
The current status of the project.





NextToken (string) --
If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.







Exceptions

Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'ProjectDescriptions': [
            {
                'ProjectArn': 'string',
                'CreationTimestamp': datetime(2015, 1, 1),
                'Status': 'CREATING'|'CREATED'|'DELETING'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.InvalidPaginationTokenException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    
    """
    pass

def describe_stream_processor(Name=None):
    """
    Provides information about a stream processor created by  CreateStreamProcessor . You can get information about the input and output streams, the input parameters for the face recognition being performed, and the current status of the stream processor.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stream_processor(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nName of the stream processor for which you want information.\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --
Name (string) --Name of the stream processor.

StreamProcessorArn (string) --ARN of the stream processor.

Status (string) --Current status of the stream processor.

StatusMessage (string) --Detailed status message about the stream processor.

CreationTimestamp (datetime) --Date and time the stream processor was created

LastUpdateTimestamp (datetime) --The time, in Unix format, the stream processor was last updated. For example, when the stream processor moves from a running state to a failed state, or when the user starts or stops the stream processor.

Input (dict) --Kinesis video stream that provides the source streaming video.

KinesisVideoStream (dict) --The Kinesis video stream input stream for the source streaming video.

Arn (string) --ARN of the Kinesis video stream stream that streams the source video.





Output (dict) --Kinesis data stream to which Amazon Rekognition Video puts the analysis results.

KinesisDataStream (dict) --The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor streams the analysis results.

Arn (string) --ARN of the output Amazon Kinesis Data Streams stream.





RoleArn (string) --ARN of the IAM role that allows access to the stream processor.

Settings (dict) --Face recognition input parameters that are being used by the stream processor. Includes the collection to use for face recognition and the face attributes to detect.

FaceSearch (dict) --Face search settings to use on a streaming video.

CollectionId (string) --The ID of a collection that contains faces that you want to search for.

FaceMatchThreshold (float) --Minimum face match confidence score that must be met to return a result for a recognized face. Default is 80. 0 is the lowest confidence. 100 is the highest confidence.










Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


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

def detect_custom_labels(ProjectVersionArn=None, Image=None, MaxResults=None, MinConfidence=None):
    """
    Detects custom labels in a supplied image by using an Amazon Rekognition Custom Labels model.
    You specify which version of a model version to use by using the ProjectVersionArn input parameter.
    You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    For each object that the model version detects on an image, the API returns a (CustomLabel ) object in an array (CustomLabels ). Each CustomLabel object provides the label name (Name ), the level of confidence that the image contains the object (Confidence ), and object location information, if it exists, for the label on the image (Geometry ).
    During training model calculates a threshold value that determines if a prediction for a label is true. By default, DetectCustomLabels doesn\'t return labels whose confidence value is below the model\'s calculated threshold value. To filter labels that are returned, specify a value for MinConfidence that is higher than the model\'s calculated threshold. You can get the model\'s calculated threshold from the model\'s training results shown in the Amazon Rekognition Custom Labels console. To get all labels, regardless of confidence, specify a MinConfidence value of 0.
    You can also add the MaxResults parameter to limit the number of labels returned.
    This is a stateless API operation. That is, the operation does not persist any data.
    This operation requires permissions to perform the rekognition:DetectCustomLabels action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detect_custom_labels(
        ProjectVersionArn='string',
        Image={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        MaxResults=123,
        MinConfidence=...
    )
    
    
    :type ProjectVersionArn: string
    :param ProjectVersionArn: [REQUIRED]\nThe ARN of the model version that you want to use.\n

    :type Image: dict
    :param Image: [REQUIRED]\nProvides the input image either as bytes or an S3 object.\nYou pass image bytes to an Amazon Rekognition API operation by using the Bytes property. For example, you would use the Bytes property to pass an image loaded from a local file system. Image bytes passed by using the Bytes property must be base64-encoded. Your code may not need to encode image bytes if you are using an AWS SDK to call Amazon Rekognition API operations.\nFor more information, see Analyzing an Image Loaded from a Local File System in the Amazon Rekognition Developer Guide.\nYou pass images stored in an S3 bucket to an Amazon Rekognition API operation by using the S3Object property. Images stored in an S3 bucket do not need to be base64-encoded.\nThe region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.\nIf you use the AWS CLI to call Amazon Rekognition operations, passing image bytes using the Bytes property is not supported. You must first upload the image to an Amazon S3 bucket and then call the operation using the S3Object property.\nFor Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see Resource Based Policies in the Amazon Rekognition Developer Guide.\n\nBytes (bytes) --Blob of image bytes up to 5 MBs.\n\nS3Object (dict) --Identifies an S3 object as the image source.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results you want the service to return in the response. The service returns the specified number of highest confidence labels ranked from highest confidence to lowest.

    :type MinConfidence: float
    :param MinConfidence: Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn\'t return any labels with a confidence lower than this specified value. If you specify a value of 0, all labels are return, regardless of the default thresholds that the model version applies.

    :rtype: dict

ReturnsResponse Syntax
{
    'CustomLabels': [
        {
            'Name': 'string',
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


Response Structure

(dict) --

CustomLabels (list) --
An array of custom labels detected in the input image.

(dict) --
A custom label detected in an image by a call to  DetectCustomLabels .

Name (string) --
The name of the custom label.

Confidence (float) --
The confidence that the model has in the detection of the custom label. The range is 0-100. A higher value indicates a higher confidence.

Geometry (dict) --
The location of the detected object on the image that corresponds to the custom label. Includes an axis aligned coarse bounding box surrounding the object and a finer grain polygon for more accurate spatial information.

BoundingBox (dict) --
An axis-aligned coarse representation of the detected item\'s location on the image.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Polygon (list) --
Within the bounding box, a fine-grained polygon around the detected item.

(dict) --
The X and Y coordinates of a point on an image. The X and Y values returned are ratios of the overall image size. For example, if the input image is 700x200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the image.
An array of Point objects, Polygon , is returned by  DetectText and by  DetectCustomLabels . Polygon represents a fine-grained polygon around a detected item. For more information, see Geometry in the Amazon Rekognition Developer Guide.

X (float) --
The value of the X coordinate for a point on a Polygon .

Y (float) --
The value of the Y coordinate for a point on a Polygon .

















Exceptions

Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ResourceNotReadyException
Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ImageTooLargeException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.InvalidImageFormatException


    :return: {
        'CustomLabels': [
            {
                'Name': 'string',
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
    
    
    :returns: 
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ResourceNotReadyException
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.ImageTooLargeException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.InvalidImageFormatException
    
    """
    pass

def detect_faces(Image=None, Attributes=None):
    """
    Detects faces within an image that is provided as input.
    The face-detection algorithm is most effective on frontal faces. For non-frontal or obscured faces, the algorithm might not detect the faces or might detect faces with lower confidence.
    You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    This operation requires permissions to perform the rekognition:DetectFaces action.
    See also: AWS API Documentation
    
    Exceptions
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
    :param Image: [REQUIRED]\nThe input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.\nIf you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the Bytes field. For more information, see Images in the Amazon Rekognition developer guide.\n\nBytes (bytes) --Blob of image bytes up to 5 MBs.\n\nS3Object (dict) --Identifies an S3 object as the image source.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type Attributes: list
    :param Attributes: An array of facial attributes you want to be returned. This can be the default list of attributes or all attributes. If you don\'t specify a value for Attributes or if you specify ['DEFAULT'] , the API returns the following subset of facial attributes: BoundingBox , Confidence , Pose , Quality , and Landmarks . If you provide ['ALL'] , all facial attributes are returned, but the operation takes longer to complete.\nIf you provide both, ['ALL', 'DEFAULT'] , the service uses a logical AND operator to determine which attributes to return (in this case, all attributes).\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                    'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                    'Confidence': ...
                },
            ],
            'Landmarks': [
                {
                    'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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


Response Structure

(dict) --

FaceDetails (list) --
Details of each face found in the image.

(dict) --
Structure containing attributes of the face that the algorithm detected.
A FaceDetail object contains either the default facial attributes or all facial attributes. The default attributes are BoundingBox , Confidence , Landmarks , Pose , and Quality .

GetFaceDetection is the only Amazon Rekognition Video stored video operation that can return a FaceDetail object with all attributes. To specify which attributes to return, use the FaceAttributes input parameter for  StartFaceDetection . The following Amazon Rekognition Video operations return only the default attributes. The corresponding Start operations don\'t have a FaceAttributes input parameter.


GetCelebrityRecognition
GetPersonTracking
GetFaceSearch

The Amazon Rekognition Image  DetectFaces and  IndexFaces operations can return all facial attributes. To specify which attributes to return, use the Attributes input parameter for DetectFaces . For IndexFaces , use the DetectAttributes input parameter.

BoundingBox (dict) --
Bounding box of the face. Default attribute.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



AgeRange (dict) --
The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

Low (integer) --
The lowest estimated age.

High (integer) --
The highest estimated age.



Smile (dict) --
Indicates whether or not the face is smiling, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is smiling or not.

Confidence (float) --
Level of confidence in the determination.



Eyeglasses (dict) --
Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing eye glasses or not.

Confidence (float) --
Level of confidence in the determination.



Sunglasses (dict) --
Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing sunglasses or not.

Confidence (float) --
Level of confidence in the determination.



Gender (dict) --
The predicted gender of a detected face.

Value (string) --
The predicted gender of the face.

Confidence (float) --
Level of confidence in the prediction.



Beard (dict) --
Indicates whether or not the face has a beard, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has beard or not.

Confidence (float) --
Level of confidence in the determination.



Mustache (dict) --
Indicates whether or not the face has a mustache, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has mustache or not.

Confidence (float) --
Level of confidence in the determination.



EyesOpen (dict) --
Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the eyes on the face are open.

Confidence (float) --
Level of confidence in the determination.



MouthOpen (dict) --
Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the mouth on the face is open or not.

Confidence (float) --
Level of confidence in the determination.



Emotions (list) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

(dict) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

Type (string) --
Type of emotion detected.

Confidence (float) --
Level of confidence in the determination.





Landmarks (list) --
Indicates the location of landmarks on the face. Default attribute.

(dict) --
Indicates the location of the landmark on the face.

Type (string) --
Type of landmark.

X (float) --
The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --
The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --
Indicates the pose of the face as determined by its pitch, roll, and yaw. Default attribute.

Roll (float) --
Value representing the face rotation on the roll axis.

Yaw (float) --
Value representing the face rotation on the yaw axis.

Pitch (float) --
Value representing the face rotation on the pitch axis.



Quality (dict) --
Identifies image brightness and sharpness. Default attribute.

Brightness (float) --
Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --
Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.



Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree). Default attribute.





OrientationCorrection (string) --
The value of OrientationCorrection is always null.
If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image\'s orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don\'t contain Exif metadata.
Amazon Rekognition doesn\xe2\x80\x99t perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates aren\'t translated and represent the object locations before the image is rotated.







Exceptions

Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ImageTooLargeException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.InvalidImageFormatException

Examples
This operation detects faces in an image stored in an AWS S3 bucket.
response = client.detect_faces(
    Image={
        'S3Object': {
            'Bucket': 'mybucket',
            'Name': 'myphoto',
        },
    },
)

print(response)


Expected Output:
{
    'FaceDetails': [
        {
            'BoundingBox': {
                'Height': 0.18000000715255737,
                'Left': 0.5555555820465088,
                'Top': 0.33666667342185974,
                'Width': 0.23999999463558197,
            },
            'Confidence': 100,
            'Landmarks': [
                {
                    'Type': 'eyeLeft',
                    'X': 0.6394737362861633,
                    'Y': 0.40819624066352844,
                },
                {
                    'Type': 'eyeRight',
                    'X': 0.7266660928726196,
                    'Y': 0.41039225459098816,
                },
                {
                    'Type': 'eyeRight',
                    'X': 0.6912462115287781,
                    'Y': 0.44240960478782654,
                },
                {
                    'Type': 'mouthDown',
                    'X': 0.6306198239326477,
                    'Y': 0.46700039505958557,
                },
                {
                    'Type': 'mouthUp',
                    'X': 0.7215608954429626,
                    'Y': 0.47114261984825134,
                },
            ],
            'Pose': {
                'Pitch': 4.050806522369385,
                'Roll': 0.9950747489929199,
                'Yaw': 13.693790435791016,
            },
            'Quality': {
                'Brightness': 37.60169982910156,
                'Sharpness': 80,
            },
        },
    ],
    'OrientationCorrection': 'ROTATE_0',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                        'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                        'Confidence': ...
                    },
                ],
                'Landmarks': [
                    {
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
    
    
    :returns: 
    GetCelebrityRecognition
    GetPersonTracking
    GetFaceSearch
    
    """
    pass

def detect_labels(Image=None, MaxLabels=None, MinConfidence=None):
    """
    Detects instances of real-world entities within an image (JPEG or PNG) provided as input. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; and concepts like landscape, evening, and nature.
    For an example, see Analyzing Images Stored in an Amazon S3 Bucket in the Amazon Rekognition Developer Guide.
    You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    For each object, scene, and concept the API returns one or more labels. Each label provides the object name, and the level of confidence that the image contains the object. For example, suppose the input image has a lighthouse, the sea, and a rock. The response includes all three labels, one for each object.
    In the preceding example, the operation returns one label for each of the three objects. The operation can also return multiple labels for the same object in the image. For example, if the input image shows a flower (for example, a tulip), the operation might return the following three labels.
    In this example, the detection algorithm more precisely identifies the flower as a tulip.
    In response, the API returns an array of labels. In addition, the response also includes the orientation correction. Optionally, you can specify MinConfidence to control the confidence threshold for the labels returned. The default is 55%. You can also add the MaxLabels parameter to limit the number of labels returned.
    This is a stateless API operation. That is, the operation does not persist any data.
    This operation requires permissions to perform the rekognition:DetectLabels action.
    See also: AWS API Documentation
    
    Exceptions
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
    :param Image: [REQUIRED]\nThe input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. Images stored in an S3 Bucket do not need to be base64-encoded.\nIf you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the Bytes field. For more information, see Images in the Amazon Rekognition developer guide.\n\nBytes (bytes) --Blob of image bytes up to 5 MBs.\n\nS3Object (dict) --Identifies an S3 object as the image source.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type MaxLabels: integer
    :param MaxLabels: Maximum number of labels you want the service to return in the response. The service returns the specified number of highest confidence labels.

    :type MinConfidence: float
    :param MinConfidence: Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn\'t return any labels with confidence lower than this specified value.\nIf MinConfidence is not specified, the operation returns labels with a confidence values greater than or equal to 55 percent.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Labels': [
        {
            'Name': 'string',
            'Confidence': ...,
            'Instances': [
                {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'Confidence': ...
                },
            ],
            'Parents': [
                {
                    'Name': 'string'
                },
            ]
        },
    ],
    'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270',
    'LabelModelVersion': 'string'
}


Response Structure

(dict) --

Labels (list) --
An array of labels for the real-world objects detected.

(dict) --
Structure containing details about the detected label, including the name, detected instances, parent labels, and level of confidence.

Name (string) --
The name (label) of the object or scene.

Confidence (float) --
Level of confidence.

Instances (list) --
If Label represents an object, Instances contains the bounding boxes for each instance of the detected object. Bounding boxes are returned for common object labels such as people, cars, furniture, apparel or pets.

(dict) --
An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or by Amazon Rekognition Video ( GetLabelDetection ).

BoundingBox (dict) --
The position of the label instance on the image.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Confidence (float) --
The confidence that Amazon Rekognition has in the accuracy of the bounding box.





Parents (list) --
The parent labels for a label. The response includes all ancestor labels.

(dict) --
A parent label for a label. A label can have 0, 1, or more parents.

Name (string) --
The name of the parent label.









OrientationCorrection (string) --
The value of OrientationCorrection is always null.
If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image\'s orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don\'t contain Exif metadata.
Amazon Rekognition doesn\xe2\x80\x99t perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates aren\'t translated and represent the object locations before the image is rotated.

LabelModelVersion (string) --
Version number of the label detection model that was used to detect labels.







Exceptions

Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ImageTooLargeException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.InvalidImageFormatException

Examples
This operation detects labels in the supplied image
response = client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'mybucket',
            'Name': 'myphoto',
        },
    },
    MaxLabels=123,
    MinConfidence=70,
)

print(response)


Expected Output:
{
    'Labels': [
        {
            'Confidence': 99.25072479248047,
            'Name': 'People',
        },
        {
            'Confidence': 99.25074005126953,
            'Name': 'Person',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Labels': [
            {
                'Name': 'string',
                'Confidence': ...,
                'Instances': [
                    {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'Confidence': ...
                    },
                ],
                'Parents': [
                    {
                        'Name': 'string'
                    },
                ]
            },
        ],
        'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270',
        'LabelModelVersion': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.ImageTooLargeException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.InvalidImageFormatException
    
    """
    pass

def detect_moderation_labels(Image=None, MinConfidence=None, HumanLoopConfig=None):
    """
    Detects unsafe content in a specified JPEG or PNG format image. Use DetectModerationLabels to moderate images depending on your requirements. For example, you might want to filter images that contain nudity, but not images containing suggestive content.
    To filter images, use the labels returned by DetectModerationLabels to determine which types of content are appropriate.
    For information about moderation labels, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.
    You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detect_moderation_labels(
        Image={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        MinConfidence=...,
        HumanLoopConfig={
            'HumanLoopName': 'string',
            'FlowDefinitionArn': 'string',
            'DataAttributes': {
                'ContentClassifiers': [
                    'FreeOfPersonallyIdentifiableInformation'|'FreeOfAdultContent',
                ]
            }
        }
    )
    
    
    :type Image: dict
    :param Image: [REQUIRED]\nThe input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.\nIf you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the Bytes field. For more information, see Images in the Amazon Rekognition developer guide.\n\nBytes (bytes) --Blob of image bytes up to 5 MBs.\n\nS3Object (dict) --Identifies an S3 object as the image source.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type MinConfidence: float
    :param MinConfidence: Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn\'t return any labels with a confidence level lower than this specified value.\nIf you don\'t specify MinConfidence , the operation returns labels with confidence values greater than or equal to 50 percent.\n

    :type HumanLoopConfig: dict
    :param HumanLoopConfig: Sets up the configuration for human evaluation, including the FlowDefinition the image will be sent to.\n\nHumanLoopName (string) -- [REQUIRED]The name of the human review used for this image. This should be kept unique within a region.\n\nFlowDefinitionArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the flow definition.\n\nDataAttributes (dict) --Sets attributes of the input data.\n\nContentClassifiers (list) --Sets whether the input image is free of personally identifiable information.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ModerationLabels': [
        {
            'Confidence': ...,
            'Name': 'string',
            'ParentName': 'string'
        },
    ],
    'ModerationModelVersion': 'string',
    'HumanLoopActivationOutput': {
        'HumanLoopArn': 'string',
        'HumanLoopActivationReasons': [
            'string',
        ],
        'HumanLoopActivationConditionsEvaluationResults': 'string'
    }
}


Response Structure

(dict) --

ModerationLabels (list) --
Array of detected Moderation labels and the time, in milliseconds from the start of the video, they were detected.

(dict) --
Provides information about a single type of unsafe content found in an image or video. Each type of moderated content has a label within a hierarchical taxonomy. For more information, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.

Confidence (float) --
Specifies the confidence that Amazon Rekognition has that the label has been correctly identified.
If you don\'t specify the MinConfidence parameter in the call to DetectModerationLabels , the operation returns labels with a confidence value greater than or equal to 50 percent.

Name (string) --
The label name for the type of unsafe content detected in the image.

ParentName (string) --
The name for the parent label. Labels at the top level of the hierarchy have the parent label "" .





ModerationModelVersion (string) --
Version number of the moderation detection model that was used to detect unsafe content.

HumanLoopActivationOutput (dict) --
Shows the results of the human in the loop evaluation.

HumanLoopArn (string) --
The Amazon Resource Name (ARN) of the HumanLoop created.

HumanLoopActivationReasons (list) --
Shows if and why human review was needed.

(string) --


HumanLoopActivationConditionsEvaluationResults (string) --
Shows the result of condition evaluations, including those conditions which activated a human review.









Exceptions

Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ImageTooLargeException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.InvalidImageFormatException
Rekognition.Client.exceptions.HumanLoopQuotaExceededException


    :return: {
        'ModerationLabels': [
            {
                'Confidence': ...,
                'Name': 'string',
                'ParentName': 'string'
            },
        ],
        'ModerationModelVersion': 'string',
        'HumanLoopActivationOutput': {
            'HumanLoopArn': 'string',
            'HumanLoopActivationReasons': [
                'string',
            ],
            'HumanLoopActivationConditionsEvaluationResults': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def detect_text(Image=None, Filters=None):
    """
    Detects text in the input image and converts it into machine-readable text.
    Pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, you must pass it as a reference to an image in an Amazon S3 bucket. For the AWS CLI, passing image bytes is not supported. The image must be either a .png or .jpeg formatted file.
    The DetectText operation returns text in an array of  TextDetection elements, TextDetections . Each TextDetection element provides information about a single word or line of text that was detected in the image.
    A word is one or more ISO basic latin script characters that are not separated by spaces. DetectText can detect up to 50 words in an image.
    A line is a string of equally spaced words. A line isn\'t necessarily a complete sentence. For example, a driver\'s license number is detected as a line. A line ends when there is no aligned text after it. Also, a line ends when there is a large gap between words, relative to the length of the words. This means, depending on the gap between words, Amazon Rekognition may detect multiple lines in text aligned in the same direction. Periods don\'t represent the end of a line. If a sentence spans multiple lines, the DetectText operation returns multiple lines.
    To determine whether a TextDetection element is a line of text or a word, use the TextDetection object Type field.
    To be detected, text must be within +/- 90 degrees orientation of the horizontal axis.
    For more information, see DetectText in the Amazon Rekognition Developer Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detect_text(
        Image={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        Filters={
            'WordFilter': {
                'MinConfidence': ...,
                'MinBoundingBoxHeight': ...,
                'MinBoundingBoxWidth': ...
            },
            'RegionsOfInterest': [
                {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    }
                },
            ]
        }
    )
    
    
    :type Image: dict
    :param Image: [REQUIRED]\nThe input image as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Rekognition operations, you can\'t pass image bytes.\nIf you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the Bytes field. For more information, see Images in the Amazon Rekognition developer guide.\n\nBytes (bytes) --Blob of image bytes up to 5 MBs.\n\nS3Object (dict) --Identifies an S3 object as the image source.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type Filters: dict
    :param Filters: Optional parameters that let you set the criteria that the text must meet to be included in your response.\n\nWordFilter (dict) --A set of parameters that allow you to filter out certain results from your returned results.\n\nMinConfidence (float) --Sets confidence of word detection. Words with detection confidence below this will be excluded from the result. Values should be between 0.5 and 1 as Text in Video will not return any result below 0.5.\n\nMinBoundingBoxHeight (float) --Sets the minimum height of the word bounding box. Words with bounding box heights lesser than this value will be excluded from the result. Value is relative to the video frame height.\n\nMinBoundingBoxWidth (float) --Sets the minimum width of the word bounding box. Words with bounding boxes widths lesser than this value will be excluded from the result. Value is relative to the video frame width.\n\n\n\nRegionsOfInterest (list) --A Filter focusing on a certain area of the image. Uses a BoundingBox object to set the region of the image.\n\n(dict) --Specifies a location within the frame that Rekognition checks for text. Uses a BoundingBox object to set a region of the screen.\nA word is included in the region if the word is more than half in that region. If there is more than one region, the word will be compared with all regions of the screen. Any word more than half in a region is kept in the results.\n\nBoundingBox (dict) --The box representing a region of interest on screen.\n\nWidth (float) --Width of the bounding box as a ratio of the overall image width.\n\nHeight (float) --Height of the bounding box as a ratio of the overall image height.\n\nLeft (float) --Left coordinate of the bounding box as a ratio of overall image width.\n\nTop (float) --Top coordinate of the bounding box as a ratio of overall image height.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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
    ],
    'TextModelVersion': 'string'
}


Response Structure

(dict) --

TextDetections (list) --
An array of text that was detected in the input image.

(dict) --
Information about a word or line of text detected by  DetectText .
The DetectedText field contains the text that Amazon Rekognition detected in the image.
Every word and line has an identifier (Id ). Each word belongs to a line and has a parent identifier (ParentId ) that identifies the line of text in which the word appears. The word Id is also an index for the word within a line of words.
For more information, see Detecting Text in the Amazon Rekognition Developer Guide.

DetectedText (string) --
The word or line of text recognized by Amazon Rekognition.

Type (string) --
The type of text that was detected.

Id (integer) --
The identifier for the detected text. The identifier is only unique for a single call to DetectText .

ParentId (integer) --
The Parent identifier for the detected text identified by the value of ID . If the type of detected text is LINE , the value of ParentId is Null .

Confidence (float) --
The confidence that Amazon Rekognition has in the accuracy of the detected text and the accuracy of the geometry points around the detected text.

Geometry (dict) --
The location of the detected text on the image. Includes an axis aligned coarse bounding box surrounding the text and a finer grain polygon for more accurate spatial information.

BoundingBox (dict) --
An axis-aligned coarse representation of the detected item\'s location on the image.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Polygon (list) --
Within the bounding box, a fine-grained polygon around the detected item.

(dict) --
The X and Y coordinates of a point on an image. The X and Y values returned are ratios of the overall image size. For example, if the input image is 700x200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the image.
An array of Point objects, Polygon , is returned by  DetectText and by  DetectCustomLabels . Polygon represents a fine-grained polygon around a detected item. For more information, see Geometry in the Amazon Rekognition Developer Guide.

X (float) --
The value of the X coordinate for a point on a Polygon .

Y (float) --
The value of the Y coordinate for a point on a Polygon .











TextModelVersion (string) --
The model version used to detect text.







Exceptions

Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ImageTooLargeException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.InvalidImageFormatException


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
        ],
        'TextModelVersion': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.ImageTooLargeException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.InvalidImageFormatException
    
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

def get_celebrity_info(Id=None):
    """
    Gets the name and additional information about a celebrity based on his or her Amazon Rekognition ID. The additional information is returned as an array of URLs. If there is no additional information about the celebrity, this list is empty.
    For more information, see Recognizing Celebrities in an Image in the Amazon Rekognition Developer Guide.
    This operation requires permissions to perform the rekognition:GetCelebrityInfo action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_celebrity_info(
        Id='string'
    )
    
    
    :type Id: string
    :param Id: [REQUIRED]\nThe ID for the celebrity. You get the celebrity ID from a call to the RecognizeCelebrities operation, which recognizes celebrities in an image.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Urls': [
        'string',
    ],
    'Name': 'string'
}


Response Structure

(dict) --
Urls (list) --An array of URLs pointing to additional celebrity information.

(string) --


Name (string) --The name of the celebrity.






Exceptions

Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException


    :return: {
        'Urls': [
            'string',
        ],
        'Name': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def get_celebrity_recognition(JobId=None, MaxResults=None, NextToken=None, SortBy=None):
    """
    Gets the celebrity recognition results for a Amazon Rekognition Video analysis started by  StartCelebrityRecognition .
    Celebrity recognition in a video is an asynchronous operation. Analysis is started by a call to  StartCelebrityRecognition which returns a job identifier (JobId ). When the celebrity recognition operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartCelebrityRecognition . To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call GetCelebrityDetection and pass the job identifier (JobId ) from the initial call to StartCelebrityDetection .
    For more information, see Working With Stored Videos in the Amazon Rekognition Developer Guide.
    By default, the Celebrities array is sorted by time (milliseconds from the start of the video). You can also sort the array by celebrity by specifying the value ID in the SortBy input parameter.
    The CelebrityDetail object includes the celebrity identifer and additional information urls. If you don\'t store the additional information urls, you can get them later by calling  GetCelebrityInfo with the celebrity identifer.
    No information is returned for faces not recognized as celebrities.
    Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetCelebrityDetection and populate the NextToken request parameter with the token value returned from the previous call to GetCelebrityRecognition .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_celebrity_recognition(
        JobId='string',
        MaxResults=123,
        NextToken='string',
        SortBy='ID'|'TIMESTAMP'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nJob identifier for the required celebrity recognition analysis. You can get the job identifer from a call to StartCelebrityRecognition .\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more recognized celebrities to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of celebrities.

    :type SortBy: string
    :param SortBy: Sort to use for celebrities returned in Celebrities field. Specify ID to sort by the celebrity identifier, specify TIMESTAMP to sort by the time the celebrity was recognized.

    :rtype: dict

ReturnsResponse Syntax
{
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
                            'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                            'Confidence': ...
                        },
                    ],
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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


Response Structure

(dict) --

JobStatus (string) --
The current status of the celebrity recognition job.

StatusMessage (string) --
If the job fails, StatusMessage provides a descriptive error message.

VideoMetadata (dict) --
Information about a video that Amazon Rekognition Video analyzed. Videometadata is returned in every page of paginated responses from a Amazon Rekognition Video operation.

Codec (string) --
Type of compression used in the analyzed video.

DurationMillis (integer) --
Length of the video in milliseconds.

Format (string) --
Format of the analyzed video. Possible values are MP4, MOV and AVI.

FrameRate (float) --
Number of frames per second in the video.

FrameHeight (integer) --
Vertical pixel dimension of the video.

FrameWidth (integer) --
Horizontal pixel dimension of the video.



NextToken (string) --
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of celebrities.

Celebrities (list) --
Array of celebrities recognized in the video.

(dict) --
Information about a detected celebrity and the time the celebrity was detected in a stored video. For more information, see GetCelebrityRecognition in the Amazon Rekognition Developer Guide.

Timestamp (integer) --
The time, in milliseconds from the start of the video, that the celebrity was recognized.

Celebrity (dict) --
Information about a recognized celebrity.

Urls (list) --
An array of URLs pointing to additional celebrity information.

(string) --


Name (string) --
The name of the celebrity.

Id (string) --
The unique identifier for the celebrity.

Confidence (float) --
The confidence, in percentage, that Amazon Rekognition has that the recognized face is the celebrity.

BoundingBox (dict) --
Bounding box around the body of a celebrity.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Face (dict) --
Face details for the recognized celebrity.

BoundingBox (dict) --
Bounding box of the face. Default attribute.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



AgeRange (dict) --
The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

Low (integer) --
The lowest estimated age.

High (integer) --
The highest estimated age.



Smile (dict) --
Indicates whether or not the face is smiling, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is smiling or not.

Confidence (float) --
Level of confidence in the determination.



Eyeglasses (dict) --
Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing eye glasses or not.

Confidence (float) --
Level of confidence in the determination.



Sunglasses (dict) --
Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing sunglasses or not.

Confidence (float) --
Level of confidence in the determination.



Gender (dict) --
The predicted gender of a detected face.

Value (string) --
The predicted gender of the face.

Confidence (float) --
Level of confidence in the prediction.



Beard (dict) --
Indicates whether or not the face has a beard, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has beard or not.

Confidence (float) --
Level of confidence in the determination.



Mustache (dict) --
Indicates whether or not the face has a mustache, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has mustache or not.

Confidence (float) --
Level of confidence in the determination.



EyesOpen (dict) --
Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the eyes on the face are open.

Confidence (float) --
Level of confidence in the determination.



MouthOpen (dict) --
Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the mouth on the face is open or not.

Confidence (float) --
Level of confidence in the determination.



Emotions (list) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

(dict) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

Type (string) --
Type of emotion detected.

Confidence (float) --
Level of confidence in the determination.





Landmarks (list) --
Indicates the location of landmarks on the face. Default attribute.

(dict) --
Indicates the location of the landmark on the face.

Type (string) --
Type of landmark.

X (float) --
The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --
The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --
Indicates the pose of the face as determined by its pitch, roll, and yaw. Default attribute.

Roll (float) --
Value representing the face rotation on the roll axis.

Yaw (float) --
Value representing the face rotation on the yaw axis.

Pitch (float) --
Value representing the face rotation on the pitch axis.



Quality (dict) --
Identifies image brightness and sharpness. Default attribute.

Brightness (float) --
Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --
Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.



Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree). Default attribute.















Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ThrottlingException


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
                                'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                                'Confidence': ...
                            },
                        ],
                        'Landmarks': [
                            {
                                'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
    Gets the unsafe content analysis results for a Amazon Rekognition Video analysis started by  StartContentModeration .
    Unsafe content analysis of a video is an asynchronous operation. You start analysis by calling  StartContentModeration which returns a job identifier (JobId ). When analysis finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartContentModeration . To get the results of the unsafe content analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call GetContentModeration and pass the job identifier (JobId ) from the initial call to StartContentModeration .
    For more information, see Working with Stored Videos in the Amazon Rekognition Devlopers Guide.
    By default, the moderated labels are returned sorted by time, in milliseconds from the start of the video. You can also sort them by moderated label by specifying NAME for the SortBy input parameter.
    Since video analysis can return a large number of results, use the MaxResults parameter to limit the number of labels returned in a single call to GetContentModeration . If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetContentModeration and populate the NextToken request parameter with the value of NextToken returned from the previous call to GetContentModeration .
    For more information, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_content_moderation(
        JobId='string',
        MaxResults=123,
        NextToken='string',
        SortBy='NAME'|'TIMESTAMP'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier for the unsafe content job. Use JobId to identify the job in a subsequent call to GetContentModeration .\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of unsafe content labels.

    :type SortBy: string
    :param SortBy: Sort to use for elements in the ModerationLabelDetections array. Use TIMESTAMP to sort array elements by the time labels are detected. Use NAME to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by TIMESTAMP .

    :rtype: dict

ReturnsResponse Syntax
{
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
    'NextToken': 'string',
    'ModerationModelVersion': 'string'
}


Response Structure

(dict) --

JobStatus (string) --
The current status of the unsafe content analysis job.

StatusMessage (string) --
If the job fails, StatusMessage provides a descriptive error message.

VideoMetadata (dict) --
Information about a video that Amazon Rekognition analyzed. Videometadata is returned in every page of paginated responses from GetContentModeration .

Codec (string) --
Type of compression used in the analyzed video.

DurationMillis (integer) --
Length of the video in milliseconds.

Format (string) --
Format of the analyzed video. Possible values are MP4, MOV and AVI.

FrameRate (float) --
Number of frames per second in the video.

FrameHeight (integer) --
Vertical pixel dimension of the video.

FrameWidth (integer) --
Horizontal pixel dimension of the video.



ModerationLabels (list) --
The detected unsafe content labels and the time(s) they were detected.

(dict) --
Information about an unsafe content label detection in a stored video.

Timestamp (integer) --
Time, in milliseconds from the beginning of the video, that the unsafe content label was detected.

ModerationLabel (dict) --
The unsafe content label detected by in the stored video.

Confidence (float) --
Specifies the confidence that Amazon Rekognition has that the label has been correctly identified.
If you don\'t specify the MinConfidence parameter in the call to DetectModerationLabels , the operation returns labels with a confidence value greater than or equal to 50 percent.

Name (string) --
The label name for the type of unsafe content detected in the image.

ParentName (string) --
The name for the parent label. Labels at the top level of the hierarchy have the parent label "" .







NextToken (string) --
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of unsafe content labels.

ModerationModelVersion (string) --
Version number of the moderation detection model that was used to detect unsafe content.







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ThrottlingException


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
        'NextToken': 'string',
        'ModerationModelVersion': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidPaginationTokenException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def get_face_detection(JobId=None, MaxResults=None, NextToken=None):
    """
    Gets face detection results for a Amazon Rekognition Video analysis started by  StartFaceDetection .
    Face detection with Amazon Rekognition Video is an asynchronous operation. You start face detection by calling  StartFaceDetection which returns a job identifier (JobId ). When the face detection operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartFaceDetection . To get the results of the face detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call  GetFaceDetection and pass the job identifier (JobId ) from the initial call to StartFaceDetection .
    Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetFaceDetection and populate the NextToken request parameter with the token value returned from the previous call to GetFaceDetection .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_face_detection(
        JobId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nUnique identifier for the face detection job. The JobId is returned from StartFaceDetection .\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more faces to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of faces.

    :rtype: dict

ReturnsResponse Syntax
{
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
                        'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                        'Confidence': ...
                    },
                ],
                'Landmarks': [
                    {
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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


Response Structure

(dict) --

JobStatus (string) --
The current status of the face detection job.

StatusMessage (string) --
If the job fails, StatusMessage provides a descriptive error message.

VideoMetadata (dict) --
Information about a video that Amazon Rekognition Video analyzed. Videometadata is returned in every page of paginated responses from a Amazon Rekognition video operation.

Codec (string) --
Type of compression used in the analyzed video.

DurationMillis (integer) --
Length of the video in milliseconds.

Format (string) --
Format of the analyzed video. Possible values are MP4, MOV and AVI.

FrameRate (float) --
Number of frames per second in the video.

FrameHeight (integer) --
Vertical pixel dimension of the video.

FrameWidth (integer) --
Horizontal pixel dimension of the video.



NextToken (string) --
If the response is truncated, Amazon Rekognition returns this token that you can use in the subsequent request to retrieve the next set of faces.

Faces (list) --
An array of faces detected in the video. Each element contains a detected face\'s details and the time, in milliseconds from the start of the video, the face was detected.

(dict) --
Information about a face detected in a video analysis request and the time the face was detected in the video.

Timestamp (integer) --
Time, in milliseconds from the start of the video, that the face was detected.

Face (dict) --
The face properties for the detected face.

BoundingBox (dict) --
Bounding box of the face. Default attribute.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



AgeRange (dict) --
The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

Low (integer) --
The lowest estimated age.

High (integer) --
The highest estimated age.



Smile (dict) --
Indicates whether or not the face is smiling, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is smiling or not.

Confidence (float) --
Level of confidence in the determination.



Eyeglasses (dict) --
Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing eye glasses or not.

Confidence (float) --
Level of confidence in the determination.



Sunglasses (dict) --
Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing sunglasses or not.

Confidence (float) --
Level of confidence in the determination.



Gender (dict) --
The predicted gender of a detected face.

Value (string) --
The predicted gender of the face.

Confidence (float) --
Level of confidence in the prediction.



Beard (dict) --
Indicates whether or not the face has a beard, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has beard or not.

Confidence (float) --
Level of confidence in the determination.



Mustache (dict) --
Indicates whether or not the face has a mustache, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has mustache or not.

Confidence (float) --
Level of confidence in the determination.



EyesOpen (dict) --
Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the eyes on the face are open.

Confidence (float) --
Level of confidence in the determination.



MouthOpen (dict) --
Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the mouth on the face is open or not.

Confidence (float) --
Level of confidence in the determination.



Emotions (list) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

(dict) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

Type (string) --
Type of emotion detected.

Confidence (float) --
Level of confidence in the determination.





Landmarks (list) --
Indicates the location of landmarks on the face. Default attribute.

(dict) --
Indicates the location of the landmark on the face.

Type (string) --
Type of landmark.

X (float) --
The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --
The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --
Indicates the pose of the face as determined by its pitch, roll, and yaw. Default attribute.

Roll (float) --
Value representing the face rotation on the roll axis.

Yaw (float) --
Value representing the face rotation on the yaw axis.

Pitch (float) --
Value representing the face rotation on the pitch axis.



Quality (dict) --
Identifies image brightness and sharpness. Default attribute.

Brightness (float) --
Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --
Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.



Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree). Default attribute.













Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ThrottlingException


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
                            'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                            'Confidence': ...
                        },
                    ],
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidPaginationTokenException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def get_face_search(JobId=None, MaxResults=None, NextToken=None, SortBy=None):
    """
    Gets the face search results for Amazon Rekognition Video face search started by  StartFaceSearch . The search returns faces in a collection that match the faces of persons detected in a video. It also includes the time(s) that faces are matched in the video.
    Face search in a video is an asynchronous operation. You start face search by calling to  StartFaceSearch which returns a job identifier (JobId ). When the search operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartFaceSearch . To get the search results, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call GetFaceSearch and pass the job identifier (JobId ) from the initial call to StartFaceSearch .
    For more information, see Searching Faces in a Collection in the Amazon Rekognition Developer Guide.
    The search results are retured in an array, Persons , of  PersonMatch objects. Each``PersonMatch`` element contains details about the matching faces in the input collection, person information (facial attributes, bounding boxes, and person identifer) for the matched person, and the time the person was matched in the video.
    By default, the Persons array is sorted by the time, in milliseconds from the start of the video, persons are matched. You can also sort by persons by specifying INDEX for the SORTBY input parameter.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_face_search(
        JobId='string',
        MaxResults=123,
        NextToken='string',
        SortBy='INDEX'|'TIMESTAMP'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe job identifer for the search request. You get the job identifier from an initial call to StartFaceSearch .\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more search results to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of search results.

    :type SortBy: string
    :param SortBy: Sort to use for grouping faces in the response. Use TIMESTAMP to group faces by the time that they are recognized. Use INDEX to sort by recognized faces.

    :rtype: dict

ReturnsResponse Syntax
{
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
                            'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                            'Confidence': ...
                        },
                    ],
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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


Response Structure

(dict) --

JobStatus (string) --
The current status of the face search job.

StatusMessage (string) --
If the job fails, StatusMessage provides a descriptive error message.

NextToken (string) --
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of search results.

VideoMetadata (dict) --
Information about a video that Amazon Rekognition analyzed. Videometadata is returned in every page of paginated responses from a Amazon Rekognition Video operation.

Codec (string) --
Type of compression used in the analyzed video.

DurationMillis (integer) --
Length of the video in milliseconds.

Format (string) --
Format of the analyzed video. Possible values are MP4, MOV and AVI.

FrameRate (float) --
Number of frames per second in the video.

FrameHeight (integer) --
Vertical pixel dimension of the video.

FrameWidth (integer) --
Horizontal pixel dimension of the video.



Persons (list) --
An array of persons,  PersonMatch , in the video whose face(s) match the face(s) in an Amazon Rekognition collection. It also includes time information for when persons are matched in the video. You specify the input collection in an initial call to StartFaceSearch . Each Persons element includes a time the person was matched, face match details (FaceMatches ) for matching faces in the collection, and person information (Person ) for the matched person.

(dict) --
Information about a person whose face matches a face(s) in an Amazon Rekognition collection. Includes information about the faces in the Amazon Rekognition collection ( FaceMatch ), information about the person ( PersonDetail ), and the time stamp for when the person was detected in a video. An array of PersonMatch objects is returned by  GetFaceSearch .

Timestamp (integer) --
The time, in milliseconds from the beginning of the video, that the person was matched in the video.

Person (dict) --
Information about the matched person.

Index (integer) --
Identifier for the person detected person within a video. Use to keep track of the person throughout the video. The identifier is not stored by Amazon Rekognition.

BoundingBox (dict) --
Bounding box around the detected person.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Face (dict) --
Face details for the detected person.

BoundingBox (dict) --
Bounding box of the face. Default attribute.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



AgeRange (dict) --
The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

Low (integer) --
The lowest estimated age.

High (integer) --
The highest estimated age.



Smile (dict) --
Indicates whether or not the face is smiling, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is smiling or not.

Confidence (float) --
Level of confidence in the determination.



Eyeglasses (dict) --
Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing eye glasses or not.

Confidence (float) --
Level of confidence in the determination.



Sunglasses (dict) --
Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing sunglasses or not.

Confidence (float) --
Level of confidence in the determination.



Gender (dict) --
The predicted gender of a detected face.

Value (string) --
The predicted gender of the face.

Confidence (float) --
Level of confidence in the prediction.



Beard (dict) --
Indicates whether or not the face has a beard, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has beard or not.

Confidence (float) --
Level of confidence in the determination.



Mustache (dict) --
Indicates whether or not the face has a mustache, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has mustache or not.

Confidence (float) --
Level of confidence in the determination.



EyesOpen (dict) --
Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the eyes on the face are open.

Confidence (float) --
Level of confidence in the determination.



MouthOpen (dict) --
Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the mouth on the face is open or not.

Confidence (float) --
Level of confidence in the determination.



Emotions (list) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

(dict) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

Type (string) --
Type of emotion detected.

Confidence (float) --
Level of confidence in the determination.





Landmarks (list) --
Indicates the location of landmarks on the face. Default attribute.

(dict) --
Indicates the location of the landmark on the face.

Type (string) --
Type of landmark.

X (float) --
The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --
The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --
Indicates the pose of the face as determined by its pitch, roll, and yaw. Default attribute.

Roll (float) --
Value representing the face rotation on the roll axis.

Yaw (float) --
Value representing the face rotation on the yaw axis.

Pitch (float) --
Value representing the face rotation on the pitch axis.



Quality (dict) --
Identifies image brightness and sharpness. Default attribute.

Brightness (float) --
Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --
Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.



Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree). Default attribute.





FaceMatches (list) --
Information about the faces in the input collection that match the face of a person in the video.

(dict) --
Provides face metadata. In addition, it also provides the confidence in the match of this face with the input face.

Similarity (float) --
Confidence in the match of this face with the input face.

Face (dict) --
Describes the face properties such as the bounding box, face ID, image ID of the source image, and external image ID that you assigned.

FaceId (string) --
Unique identifier that Amazon Rekognition assigns to the face.

BoundingBox (dict) --
Bounding box of the face.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



ImageId (string) --
Unique identifier that Amazon Rekognition assigns to the input image.

ExternalImageId (string) --
Identifier that you assign to all the faces in the input image.

Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree).

















Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ThrottlingException


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
                                'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                                'Confidence': ...
                            },
                        ],
                        'Landmarks': [
                            {
                                'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidPaginationTokenException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def get_label_detection(JobId=None, MaxResults=None, NextToken=None, SortBy=None):
    """
    Gets the label detection results of a Amazon Rekognition Video analysis started by  StartLabelDetection .
    The label detection operation is started by a call to  StartLabelDetection which returns a job identifier (JobId ). When the label detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartlabelDetection . To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call  GetLabelDetection and pass the job identifier (JobId ) from the initial call to StartLabelDetection .
    The labels returned include the label name, the percentage confidence in the accuracy of the detected label, and the time the label was detected in the video.
    The returned labels also include bounding box information for common objects, a hierarchical taxonomy of detected labels, and the version of the label model used for detection.
    Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetlabelDetection and populate the NextToken request parameter with the token value returned from the previous call to GetLabelDetection .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_label_detection(
        JobId='string',
        MaxResults=123,
        NextToken='string',
        SortBy='NAME'|'TIMESTAMP'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nJob identifier for the label detection operation for which you want results returned. You get the job identifer from an initial call to StartlabelDetection .\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more labels to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of labels.

    :type SortBy: string
    :param SortBy: Sort to use for elements in the Labels array. Use TIMESTAMP to sort array elements by the time labels are detected. Use NAME to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by TIMESTAMP .

    :rtype: dict

ReturnsResponse Syntax
{
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
                'Confidence': ...,
                'Instances': [
                    {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'Confidence': ...
                    },
                ],
                'Parents': [
                    {
                        'Name': 'string'
                    },
                ]
            }
        },
    ],
    'LabelModelVersion': 'string'
}


Response Structure

(dict) --

JobStatus (string) --
The current status of the label detection job.

StatusMessage (string) --
If the job fails, StatusMessage provides a descriptive error message.

VideoMetadata (dict) --
Information about a video that Amazon Rekognition Video analyzed. Videometadata is returned in every page of paginated responses from a Amazon Rekognition video operation.

Codec (string) --
Type of compression used in the analyzed video.

DurationMillis (integer) --
Length of the video in milliseconds.

Format (string) --
Format of the analyzed video. Possible values are MP4, MOV and AVI.

FrameRate (float) --
Number of frames per second in the video.

FrameHeight (integer) --
Vertical pixel dimension of the video.

FrameWidth (integer) --
Horizontal pixel dimension of the video.



NextToken (string) --
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of labels.

Labels (list) --
An array of labels detected in the video. Each element contains the detected label and the time, in milliseconds from the start of the video, that the label was detected.

(dict) --
Information about a label detected in a video analysis request and the time the label was detected in the video.

Timestamp (integer) --
Time, in milliseconds from the start of the video, that the label was detected.

Label (dict) --
Details about the detected label.

Name (string) --
The name (label) of the object or scene.

Confidence (float) --
Level of confidence.

Instances (list) --
If Label represents an object, Instances contains the bounding boxes for each instance of the detected object. Bounding boxes are returned for common object labels such as people, cars, furniture, apparel or pets.

(dict) --
An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or by Amazon Rekognition Video ( GetLabelDetection ).

BoundingBox (dict) --
The position of the label instance on the image.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Confidence (float) --
The confidence that Amazon Rekognition has in the accuracy of the bounding box.





Parents (list) --
The parent labels for a label. The response includes all ancestor labels.

(dict) --
A parent label for a label. A label can have 0, 1, or more parents.

Name (string) --
The name of the parent label.











LabelModelVersion (string) --
Version number of the label detection model that was used to detect labels.







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ThrottlingException


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
                    'Confidence': ...,
                    'Instances': [
                        {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Confidence': ...
                        },
                    ],
                    'Parents': [
                        {
                            'Name': 'string'
                        },
                    ]
                }
            },
        ],
        'LabelModelVersion': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidPaginationTokenException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ThrottlingException
    
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

def get_person_tracking(JobId=None, MaxResults=None, NextToken=None, SortBy=None):
    """
    Gets the path tracking results of a Amazon Rekognition Video analysis started by  StartPersonTracking .
    The person path tracking operation is started by a call to StartPersonTracking which returns a job identifier (JobId ). When the operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartPersonTracking .
    To get the results of the person path tracking operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call  GetPersonTracking and pass the job identifier (JobId ) from the initial call to StartPersonTracking .
    By default, the array is sorted by the time(s) a person\'s path is tracked in the video. You can sort by tracked persons by specifying INDEX for the SortBy input parameter.
    Use the MaxResults parameter to limit the number of items returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetPersonTracking and populate the NextToken request parameter with the token value returned from the previous call to GetPersonTracking .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_person_tracking(
        JobId='string',
        MaxResults=123,
        NextToken='string',
        SortBy='INDEX'|'TIMESTAMP'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nThe identifier for a job that tracks persons in a video. You get the JobId from a call to StartPersonTracking .\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more persons to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of persons.

    :type SortBy: string
    :param SortBy: Sort to use for elements in the Persons array. Use TIMESTAMP to sort array elements by the time persons are detected. Use INDEX to sort by the tracked persons. If you sort by INDEX , the array elements for each person are sorted by detection confidence. The default sort is by TIMESTAMP .

    :rtype: dict

ReturnsResponse Syntax
{
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
                            'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                            'Confidence': ...
                        },
                    ],
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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


Response Structure

(dict) --

JobStatus (string) --
The current status of the person tracking job.

StatusMessage (string) --
If the job fails, StatusMessage provides a descriptive error message.

VideoMetadata (dict) --
Information about a video that Amazon Rekognition Video analyzed. Videometadata is returned in every page of paginated responses from a Amazon Rekognition Video operation.

Codec (string) --
Type of compression used in the analyzed video.

DurationMillis (integer) --
Length of the video in milliseconds.

Format (string) --
Format of the analyzed video. Possible values are MP4, MOV and AVI.

FrameRate (float) --
Number of frames per second in the video.

FrameHeight (integer) --
Vertical pixel dimension of the video.

FrameWidth (integer) --
Horizontal pixel dimension of the video.



NextToken (string) --
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of persons.

Persons (list) --
An array of the persons detected in the video and the time(s) their path was tracked throughout the video. An array element will exist for each time a person\'s path is tracked.

(dict) --
Details and path tracking information for a single time a person\'s path is tracked in a video. Amazon Rekognition operations that track people\'s paths return an array of PersonDetection objects with elements for each time a person\'s path is tracked in a video.
For more information, see GetPersonTracking in the Amazon Rekognition Developer Guide.

Timestamp (integer) --
The time, in milliseconds from the start of the video, that the person\'s path was tracked.

Person (dict) --
Details about a person whose path was tracked in a video.

Index (integer) --
Identifier for the person detected person within a video. Use to keep track of the person throughout the video. The identifier is not stored by Amazon Rekognition.

BoundingBox (dict) --
Bounding box around the detected person.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Face (dict) --
Face details for the detected person.

BoundingBox (dict) --
Bounding box of the face. Default attribute.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



AgeRange (dict) --
The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

Low (integer) --
The lowest estimated age.

High (integer) --
The highest estimated age.



Smile (dict) --
Indicates whether or not the face is smiling, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is smiling or not.

Confidence (float) --
Level of confidence in the determination.



Eyeglasses (dict) --
Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing eye glasses or not.

Confidence (float) --
Level of confidence in the determination.



Sunglasses (dict) --
Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing sunglasses or not.

Confidence (float) --
Level of confidence in the determination.



Gender (dict) --
The predicted gender of a detected face.

Value (string) --
The predicted gender of the face.

Confidence (float) --
Level of confidence in the prediction.



Beard (dict) --
Indicates whether or not the face has a beard, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has beard or not.

Confidence (float) --
Level of confidence in the determination.



Mustache (dict) --
Indicates whether or not the face has a mustache, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has mustache or not.

Confidence (float) --
Level of confidence in the determination.



EyesOpen (dict) --
Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the eyes on the face are open.

Confidence (float) --
Level of confidence in the determination.



MouthOpen (dict) --
Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the mouth on the face is open or not.

Confidence (float) --
Level of confidence in the determination.



Emotions (list) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

(dict) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

Type (string) --
Type of emotion detected.

Confidence (float) --
Level of confidence in the determination.





Landmarks (list) --
Indicates the location of landmarks on the face. Default attribute.

(dict) --
Indicates the location of the landmark on the face.

Type (string) --
Type of landmark.

X (float) --
The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --
The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --
Indicates the pose of the face as determined by its pitch, roll, and yaw. Default attribute.

Roll (float) --
Value representing the face rotation on the roll axis.

Yaw (float) --
Value representing the face rotation on the yaw axis.

Pitch (float) --
Value representing the face rotation on the pitch axis.



Quality (dict) --
Identifies image brightness and sharpness. Default attribute.

Brightness (float) --
Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --
Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.



Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree). Default attribute.















Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ThrottlingException


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
                                'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                                'Confidence': ...
                            },
                        ],
                        'Landmarks': [
                            {
                                'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidPaginationTokenException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def get_text_detection(JobId=None, MaxResults=None, NextToken=None):
    """
    Gets the text detection results of a Amazon Rekognition Video analysis started by  StartTextDetection .
    Text detection with Amazon Rekognition Video is an asynchronous operation. You start text detection by calling  StartTextDetection which returns a job identifier (JobId ) When the text detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to StartTextDetection . To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . if so, call GetTextDetection and pass the job identifier (JobId ) from the initial call of StartLabelDetection .
    Each element of the array includes the detected text, the precentage confidence in the acuracy of the detected text, the time the text was detected, bounding box information for where the text was located, and unique identifiers for words and their lines.
    Use MaxResults parameter to limit the number of text detections returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetTextDetection and populate the NextToken request parameter with the token value returned from the previous call to GetTextDetection .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_text_detection(
        JobId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nJob identifier for the label detection operation for which you want results returned. You get the job identifer from an initial call to StartTextDetection .\n

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to return per paginated call. The largest value you can specify is 1000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more labels to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of text.

    :rtype: dict

ReturnsResponse Syntax
{
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
    'TextDetections': [
        {
            'Timestamp': 123,
            'TextDetection': {
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
            }
        },
    ],
    'NextToken': 'string',
    'TextModelVersion': 'string'
}


Response Structure

(dict) --

JobStatus (string) --
Current status of the text detection job.

StatusMessage (string) --
If the job fails, StatusMessage provides a descriptive error message.

VideoMetadata (dict) --
Information about a video that Amazon Rekognition analyzed. Videometadata is returned in every page of paginated responses from a Amazon Rekognition video operation.

Codec (string) --
Type of compression used in the analyzed video.

DurationMillis (integer) --
Length of the video in milliseconds.

Format (string) --
Format of the analyzed video. Possible values are MP4, MOV and AVI.

FrameRate (float) --
Number of frames per second in the video.

FrameHeight (integer) --
Vertical pixel dimension of the video.

FrameWidth (integer) --
Horizontal pixel dimension of the video.



TextDetections (list) --
An array of text detected in the video. Each element contains the detected text, the time in milliseconds from the start of the video that the text was detected, and where it was detected on the screen.

(dict) --
Information about text detected in a video. Incudes the detected text, the time in milliseconds from the start of the video that the text was detected, and where it was detected on the screen.

Timestamp (integer) --
The time, in milliseconds from the start of the video, that the text was detected.

TextDetection (dict) --
Details about text detected in a video.

DetectedText (string) --
The word or line of text recognized by Amazon Rekognition.

Type (string) --
The type of text that was detected.

Id (integer) --
The identifier for the detected text. The identifier is only unique for a single call to DetectText .

ParentId (integer) --
The Parent identifier for the detected text identified by the value of ID . If the type of detected text is LINE , the value of ParentId is Null .

Confidence (float) --
The confidence that Amazon Rekognition has in the accuracy of the detected text and the accuracy of the geometry points around the detected text.

Geometry (dict) --
The location of the detected text on the image. Includes an axis aligned coarse bounding box surrounding the text and a finer grain polygon for more accurate spatial information.

BoundingBox (dict) --
An axis-aligned coarse representation of the detected item\'s location on the image.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



Polygon (list) --
Within the bounding box, a fine-grained polygon around the detected item.

(dict) --
The X and Y coordinates of a point on an image. The X and Y values returned are ratios of the overall image size. For example, if the input image is 700x200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the image.
An array of Point objects, Polygon , is returned by  DetectText and by  DetectCustomLabels . Polygon represents a fine-grained polygon around a detected item. For more information, see Geometry in the Amazon Rekognition Developer Guide.

X (float) --
The value of the X coordinate for a point on a Polygon .

Y (float) --
The value of the Y coordinate for a point on a Polygon .













NextToken (string) --
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of text.

TextModelVersion (string) --
Version number of the text detection model that was used to detect text.







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ThrottlingException


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
        'TextDetections': [
            {
                'Timestamp': 123,
                'TextDetection': {
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
                }
            },
        ],
        'NextToken': 'string',
        'TextModelVersion': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidPaginationTokenException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ThrottlingException
    
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

def index_faces(CollectionId=None, Image=None, ExternalImageId=None, DetectionAttributes=None, MaxFaces=None, QualityFilter=None):
    """
    Detects faces in the input image and adds them to the specified collection.
    Amazon Rekognition doesn\'t save the actual faces that are detected. Instead, the underlying detection algorithm first detects the faces in the input image. For each face, the algorithm extracts facial features into a feature vector, and stores it in the backend database. Amazon Rekognition uses feature vectors when it performs face match and search operations using the  SearchFaces and  SearchFacesByImage operations.
    For more information, see Adding Faces to a Collection in the Amazon Rekognition Developer Guide.
    To get the number of faces in a collection, call  DescribeCollection .
    If you\'re using version 1.0 of the face detection model, IndexFaces indexes the 15 largest faces in the input image. Later versions of the face detection model index the 100 largest faces in the input image.
    If you\'re using version 4 or later of the face model, image orientation information is not returned in the OrientationCorrection field.
    To determine which version of the model you\'re using, call  DescribeCollection and supply the collection ID. You can also get the model version from the value of FaceModelVersion in the response from IndexFaces
    For more information, see Model Versioning in the Amazon Rekognition Developer Guide.
    If you provide the optional ExternalImageID for the input image you provided, Amazon Rekognition associates this ID with all faces that it detects. When you call the  ListFaces operation, the response returns the external ID. You can use this external image ID to create a client-side index to associate the faces with each image. You can then use the index to find all faces in an image.
    You can specify the maximum number of faces to index with the MaxFaces input parameter. This is useful when you want to index the largest faces in an image and don\'t want to index smaller faces, such as those belonging to people standing in the background.
    The QualityFilter input parameter allows you to filter out detected faces that don\xe2\x80\x99t meet a required quality bar. The quality bar is based on a variety of common use cases. By default, IndexFaces chooses the quality bar that\'s used to filter faces. You can also explicitly choose the quality bar. Use QualityFilter , to set the quality bar by specifying LOW , MEDIUM , or HIGH . If you do not want to filter detected faces, specify NONE .
    Information about faces detected in an image, but not indexed, is returned in an array of  UnindexedFace objects, UnindexedFaces . Faces aren\'t indexed for reasons such as:
    In response, the IndexFaces operation returns an array of metadata for all detected faces, FaceRecords . This includes:
    If you request all facial attributes (by using the detectionAttributes parameter), Amazon Rekognition returns detailed facial attributes, such as facial landmarks (for example, location of eye and mouth) and other facial attributes. If you provide the same image, specify the same collection, and use the same external ID in the IndexFaces operation, Amazon Rekognition doesn\'t save duplicate face metadata.
    The input image is passed either as base64-encoded image bytes, or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn\'t supported. The image must be formatted as a PNG or JPEG file.
    This operation requires permissions to perform the rekognition:IndexFaces action.
    See also: AWS API Documentation
    
    Exceptions
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
        ],
        MaxFaces=123,
        QualityFilter='NONE'|'AUTO'|'LOW'|'MEDIUM'|'HIGH'
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]\nThe ID of an existing collection to which you want to add the faces that are detected in the input images.\n

    :type Image: dict
    :param Image: [REQUIRED]\nThe input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes isn\'t supported.\nIf you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the Bytes field. For more information, see Images in the Amazon Rekognition developer guide.\n\nBytes (bytes) --Blob of image bytes up to 5 MBs.\n\nS3Object (dict) --Identifies an S3 object as the image source.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type ExternalImageId: string
    :param ExternalImageId: The ID you want to assign to all the faces detected in the image.

    :type DetectionAttributes: list
    :param DetectionAttributes: An array of facial attributes that you want to be returned. This can be the default list of attributes or all attributes. If you don\'t specify a value for Attributes or if you specify ['DEFAULT'] , the API returns the following subset of facial attributes: BoundingBox , Confidence , Pose , Quality , and Landmarks . If you provide ['ALL'] , all facial attributes are returned, but the operation takes longer to complete.\nIf you provide both, ['ALL', 'DEFAULT'] , the service uses a logical AND operator to determine which attributes to return (in this case, all attributes).\n\n(string) --\n\n

    :type MaxFaces: integer
    :param MaxFaces: The maximum number of faces to index. The value of MaxFaces must be greater than or equal to 1. IndexFaces returns no more than 100 detected faces in an image, even if you specify a larger value for MaxFaces .\nIf IndexFaces detects more faces than the value of MaxFaces , the faces with the lowest quality are filtered out first. If there are still more faces than the value of MaxFaces , the faces with the smallest bounding boxes are filtered out (up to the number that\'s needed to satisfy the value of MaxFaces ). Information about the unindexed faces is available in the UnindexedFaces array.\nThe faces that are returned by IndexFaces are sorted by the largest face bounding box size to the smallest size, in descending order.\n\nMaxFaces can be used with a collection associated with any version of the face model.\n

    :type QualityFilter: string
    :param QualityFilter: A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren\'t indexed. If you specify AUTO , Amazon Rekognition chooses the quality bar. If you specify LOW , MEDIUM , or HIGH , filtering removes all faces that don\xe2\x80\x99t meet the chosen quality bar. The default value is AUTO . The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object that\'s misidentified as a face, a face that\'s too blurry, or a face with a pose that\'s too extreme to use. If you specify NONE , no filtering is performed.\nTo use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.\n

    :rtype: dict

ReturnsResponse Syntax
{
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
                        'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                        'Confidence': ...
                    },
                ],
                'Landmarks': [
                    {
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
    'FaceModelVersion': 'string',
    'UnindexedFaces': [
        {
            'Reasons': [
                'EXCEEDS_MAX_FACES'|'EXTREME_POSE'|'LOW_BRIGHTNESS'|'LOW_SHARPNESS'|'LOW_CONFIDENCE'|'SMALL_BOUNDING_BOX'|'LOW_FACE_QUALITY',
            ],
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
                        'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                        'Confidence': ...
                    },
                ],
                'Landmarks': [
                    {
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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


Response Structure

(dict) --

FaceRecords (list) --
An array of faces detected and added to the collection. For more information, see Searching Faces in a Collection in the Amazon Rekognition Developer Guide.

(dict) --
Object containing both the face metadata (stored in the backend database), and facial attributes that are detected but aren\'t stored in the database.

Face (dict) --
Describes the face properties such as the bounding box, face ID, image ID of the input image, and external image ID that you assigned.

FaceId (string) --
Unique identifier that Amazon Rekognition assigns to the face.

BoundingBox (dict) --
Bounding box of the face.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



ImageId (string) --
Unique identifier that Amazon Rekognition assigns to the input image.

ExternalImageId (string) --
Identifier that you assign to all the faces in the input image.

Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree).



FaceDetail (dict) --
Structure containing attributes of the face that the algorithm detected.

BoundingBox (dict) --
Bounding box of the face. Default attribute.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



AgeRange (dict) --
The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

Low (integer) --
The lowest estimated age.

High (integer) --
The highest estimated age.



Smile (dict) --
Indicates whether or not the face is smiling, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is smiling or not.

Confidence (float) --
Level of confidence in the determination.



Eyeglasses (dict) --
Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing eye glasses or not.

Confidence (float) --
Level of confidence in the determination.



Sunglasses (dict) --
Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing sunglasses or not.

Confidence (float) --
Level of confidence in the determination.



Gender (dict) --
The predicted gender of a detected face.

Value (string) --
The predicted gender of the face.

Confidence (float) --
Level of confidence in the prediction.



Beard (dict) --
Indicates whether or not the face has a beard, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has beard or not.

Confidence (float) --
Level of confidence in the determination.



Mustache (dict) --
Indicates whether or not the face has a mustache, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has mustache or not.

Confidence (float) --
Level of confidence in the determination.



EyesOpen (dict) --
Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the eyes on the face are open.

Confidence (float) --
Level of confidence in the determination.



MouthOpen (dict) --
Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the mouth on the face is open or not.

Confidence (float) --
Level of confidence in the determination.



Emotions (list) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

(dict) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

Type (string) --
Type of emotion detected.

Confidence (float) --
Level of confidence in the determination.





Landmarks (list) --
Indicates the location of landmarks on the face. Default attribute.

(dict) --
Indicates the location of the landmark on the face.

Type (string) --
Type of landmark.

X (float) --
The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --
The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --
Indicates the pose of the face as determined by its pitch, roll, and yaw. Default attribute.

Roll (float) --
Value representing the face rotation on the roll axis.

Yaw (float) --
Value representing the face rotation on the yaw axis.

Pitch (float) --
Value representing the face rotation on the pitch axis.



Quality (dict) --
Identifies image brightness and sharpness. Default attribute.

Brightness (float) --
Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --
Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.



Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree). Default attribute.







OrientationCorrection (string) --
If your collection is associated with a face detection model that\'s later than version 3.0, the value of OrientationCorrection is always null and no orientation information is returned.
If your collection is associated with a face detection model that\'s version 3.0 or earlier, the following applies:

If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image\'s orientation. Amazon Rekognition uses this orientation information to perform image correction - the bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don\'t contain Exif metadata. The value of OrientationCorrection is null.
If the image doesn\'t contain orientation information in its Exif metadata, Amazon Rekognition returns an estimated orientation (ROTATE_0, ROTATE_90, ROTATE_180, ROTATE_270). Amazon Rekognition doesn\xe2\x80\x99t perform image correction for images. The bounding box coordinates aren\'t translated and represent the object locations before the image is rotated.

Bounding box information is returned in the FaceRecords array. You can get the version of the face detection model by calling  DescribeCollection .

FaceModelVersion (string) --
The version number of the face detection model that\'s associated with the input collection (CollectionId ).

UnindexedFaces (list) --
An array of faces that were detected in the image but weren\'t indexed. They weren\'t indexed because the quality filter identified them as low quality, or the MaxFaces request parameter filtered them out. To use the quality filter, you specify the QualityFilter request parameter.

(dict) --
A face that  IndexFaces detected, but didn\'t index. Use the Reasons response attribute to determine why a face wasn\'t indexed.

Reasons (list) --
An array of reasons that specify why a face wasn\'t indexed.

EXTREME_POSE - The face is at a pose that can\'t be detected. For example, the head is turned too far away from the camera.
EXCEEDS_MAX_FACES - The number of faces detected is already higher than that specified by the MaxFaces input parameter for IndexFaces .
LOW_BRIGHTNESS - The image is too dark.
LOW_SHARPNESS - The image is too blurry.
LOW_CONFIDENCE - The face was detected with a low confidence.
SMALL_BOUNDING_BOX - The bounding box around the face is too small.


(string) --


FaceDetail (dict) --
The structure that contains attributes of a face that IndexFaces detected, but didn\'t index.

BoundingBox (dict) --
Bounding box of the face. Default attribute.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



AgeRange (dict) --
The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

Low (integer) --
The lowest estimated age.

High (integer) --
The highest estimated age.



Smile (dict) --
Indicates whether or not the face is smiling, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is smiling or not.

Confidence (float) --
Level of confidence in the determination.



Eyeglasses (dict) --
Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing eye glasses or not.

Confidence (float) --
Level of confidence in the determination.



Sunglasses (dict) --
Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face is wearing sunglasses or not.

Confidence (float) --
Level of confidence in the determination.



Gender (dict) --
The predicted gender of a detected face.

Value (string) --
The predicted gender of the face.

Confidence (float) --
Level of confidence in the prediction.



Beard (dict) --
Indicates whether or not the face has a beard, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has beard or not.

Confidence (float) --
Level of confidence in the determination.



Mustache (dict) --
Indicates whether or not the face has a mustache, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the face has mustache or not.

Confidence (float) --
Level of confidence in the determination.



EyesOpen (dict) --
Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the eyes on the face are open.

Confidence (float) --
Level of confidence in the determination.



MouthOpen (dict) --
Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

Value (boolean) --
Boolean value that indicates whether the mouth on the face is open or not.

Confidence (float) --
Level of confidence in the determination.



Emotions (list) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

(dict) --
The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person\'s face. It is not a determination of the person\xe2\x80\x99s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.

Type (string) --
Type of emotion detected.

Confidence (float) --
Level of confidence in the determination.





Landmarks (list) --
Indicates the location of landmarks on the face. Default attribute.

(dict) --
Indicates the location of the landmark on the face.

Type (string) --
Type of landmark.

X (float) --
The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --
The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --
Indicates the pose of the face as determined by its pitch, roll, and yaw. Default attribute.

Roll (float) --
Value representing the face rotation on the roll axis.

Yaw (float) --
Value representing the face rotation on the yaw axis.

Pitch (float) --
Value representing the face rotation on the pitch axis.



Quality (dict) --
Identifies image brightness and sharpness. Default attribute.

Brightness (float) --
Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --
Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.



Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree). Default attribute.













Exceptions

Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ImageTooLargeException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.InvalidImageFormatException

Examples
This operation detects faces in an image and adds them to the specified Rekognition collection.
response = client.index_faces(
    CollectionId='myphotos',
    DetectionAttributes=[
    ],
    ExternalImageId='myphotoid',
    Image={
        'S3Object': {
            'Bucket': 'mybucket',
            'Name': 'myphoto',
        },
    },
)

print(response)


Expected Output:
{
    'FaceRecords': [
        {
            'Face': {
                'BoundingBox': {
                    'Height': 0.33481481671333313,
                    'Left': 0.31888890266418457,
                    'Top': 0.4933333396911621,
                    'Width': 0.25,
                },
                'Confidence': 99.9991226196289,
                'FaceId': 'ff43d742-0c13-5d16-a3e8-03d3f58e980b',
                'ImageId': '465f4e93-763e-51d0-b030-b9667a2d94b1',
            },
            'FaceDetail': {
                'BoundingBox': {
                    'Height': 0.33481481671333313,
                    'Left': 0.31888890266418457,
                    'Top': 0.4933333396911621,
                    'Width': 0.25,
                },
                'Confidence': 99.9991226196289,
                'Landmarks': [
                    {
                        'Type': 'eyeLeft',
                        'X': 0.3976764678955078,
                        'Y': 0.6248345971107483,
                    },
                    {
                        'Type': 'eyeRight',
                        'X': 0.4810936450958252,
                        'Y': 0.6317117214202881,
                    },
                    {
                        'Type': 'noseLeft',
                        'X': 0.41986238956451416,
                        'Y': 0.7111940383911133,
                    },
                    {
                        'Type': 'mouthDown',
                        'X': 0.40525302290916443,
                        'Y': 0.7497701048851013,
                    },
                    {
                        'Type': 'mouthUp',
                        'X': 0.4753248989582062,
                        'Y': 0.7558549642562866,
                    },
                ],
                'Pose': {
                    'Pitch': -9.713645935058594,
                    'Roll': 4.707281112670898,
                    'Yaw': -24.438663482666016,
                },
                'Quality': {
                    'Brightness': 29.23358917236328,
                    'Sharpness': 80,
                },
            },
        },
        {
            'Face': {
                'BoundingBox': {
                    'Height': 0.32592591643333435,
                    'Left': 0.5144444704055786,
                    'Top': 0.15111111104488373,
                    'Width': 0.24444444477558136,
                },
                'Confidence': 99.99950408935547,
                'FaceId': '8be04dba-4e58-520d-850e-9eae4af70eb2',
                'ImageId': '465f4e93-763e-51d0-b030-b9667a2d94b1',
            },
            'FaceDetail': {
                'BoundingBox': {
                    'Height': 0.32592591643333435,
                    'Left': 0.5144444704055786,
                    'Top': 0.15111111104488373,
                    'Width': 0.24444444477558136,
                },
                'Confidence': 99.99950408935547,
                'Landmarks': [
                    {
                        'Type': 'eyeLeft',
                        'X': 0.6006892323493958,
                        'Y': 0.290842205286026,
                    },
                    {
                        'Type': 'eyeRight',
                        'X': 0.6808141469955444,
                        'Y': 0.29609042406082153,
                    },
                    {
                        'Type': 'noseLeft',
                        'X': 0.6395332217216492,
                        'Y': 0.3522595763206482,
                    },
                    {
                        'Type': 'mouthDown',
                        'X': 0.5892083048820496,
                        'Y': 0.38689887523651123,
                    },
                    {
                        'Type': 'mouthUp',
                        'X': 0.674560010433197,
                        'Y': 0.394125759601593,
                    },
                ],
                'Pose': {
                    'Pitch': -4.683138370513916,
                    'Roll': 2.1029529571533203,
                    'Yaw': 6.716655254364014,
                },
                'Quality': {
                    'Brightness': 34.951698303222656,
                    'Sharpness': 160,
                },
            },
        },
    ],
    'OrientationCorrection': 'ROTATE_0',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
                            'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                            'Confidence': ...
                        },
                    ],
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
        'FaceModelVersion': 'string',
        'UnindexedFaces': [
            {
                'Reasons': [
                    'EXCEEDS_MAX_FACES'|'EXTREME_POSE'|'LOW_BRIGHTNESS'|'LOW_SHARPNESS'|'LOW_CONFIDENCE'|'SMALL_BOUNDING_BOX'|'LOW_FACE_QUALITY',
                ],
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
                            'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                            'Confidence': ...
                        },
                    ],
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
    
    
    :returns: 
    The bounding box, BoundingBox , of the detected face.
    A confidence value, Confidence , which indicates the confidence that the bounding box contains a face.
    A face ID, FaceId , assigned by the service for each face that\'s detected and stored.
    An image ID, ImageId , assigned by the service for the input image.
    
    """
    pass

def list_collections(NextToken=None, MaxResults=None):
    """
    Returns list of collection IDs in your account. If the result is truncated, the response also provides a NextToken that you can use in the subsequent request to fetch the next set of collection IDs.
    For an example, see Listing Collections in the Amazon Rekognition Developer Guide.
    This operation requires permissions to perform the rekognition:ListCollections action.
    See also: AWS API Documentation
    
    Exceptions
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

ReturnsResponse Syntax
{
    'CollectionIds': [
        'string',
    ],
    'NextToken': 'string',
    'FaceModelVersions': [
        'string',
    ]
}


Response Structure

(dict) --

CollectionIds (list) --
An array of collection IDs.

(string) --


NextToken (string) --
If the result is truncated, the response provides a NextToken that you can use in the subsequent request to fetch the next set of collection IDs.

FaceModelVersions (list) --
Version numbers of the face detection models associated with the collections in the array CollectionIds . For example, the value of FaceModelVersions[2] is the version number for the face detection model used by the collection in CollectionId[2] .

(string) --








Exceptions

Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.ResourceNotFoundException

Examples
This operation returns a list of Rekognition collections.
response = client.list_collections(
)

print(response)


Expected Output:
{
    'CollectionIds': [
        'myphotos',
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Returns metadata for faces in the specified collection. This metadata includes information such as the bounding box coordinates, the confidence (that the bounding box contains a face), and face ID. For an example, see Listing Faces in a Collection in the Amazon Rekognition Developer Guide.
    This operation requires permissions to perform the rekognition:ListFaces action.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    This operation lists the faces in a Rekognition collection.
    Expected Output:
    
    :example: response = client.list_faces(
        CollectionId='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]\nID of the collection from which to list the faces.\n

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of faces.

    :type MaxResults: integer
    :param MaxResults: Maximum number of faces to return.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

Faces (list) --
An array of Face objects.

(dict) --
Describes the face properties such as the bounding box, face ID, image ID of the input image, and external image ID that you assigned.

FaceId (string) --
Unique identifier that Amazon Rekognition assigns to the face.

BoundingBox (dict) --
Bounding box of the face.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



ImageId (string) --
Unique identifier that Amazon Rekognition assigns to the input image.

ExternalImageId (string) --
Identifier that you assign to all the faces in the input image.

Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree).





NextToken (string) --
If the response is truncated, Amazon Rekognition returns this token that you can use in the subsequent request to retrieve the next set of faces.

FaceModelVersion (string) --
Version number of the face detection model associated with the input collection (CollectionId ).







Exceptions

Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.ResourceNotFoundException

Examples
This operation lists the faces in a Rekognition collection.
response = client.list_faces(
    CollectionId='myphotos',
    MaxResults=20,
)

print(response)


Expected Output:
{
    'Faces': [
        {
            'BoundingBox': {
                'Height': 0.18000000715255737,
                'Left': 0.5555559992790222,
                'Top': 0.336667001247406,
                'Width': 0.23999999463558197,
            },
            'Confidence': 100,
            'FaceId': '1c62e8b5-69a7-5b7d-b3cd-db4338a8a7e7',
            'ImageId': '147fdf82-7a71-52cf-819b-e786c7b9746e',
        },
        {
            'BoundingBox': {
                'Height': 0.16555599868297577,
                'Left': 0.30963000655174255,
                'Top': 0.7066670060157776,
                'Width': 0.22074100375175476,
            },
            'Confidence': 100,
            'FaceId': '29a75abe-397b-5101-ba4f-706783b2246c',
            'ImageId': '147fdf82-7a71-52cf-819b-e786c7b9746e',
        },
        {
            'BoundingBox': {
                'Height': 0.3234420120716095,
                'Left': 0.3233329951763153,
                'Top': 0.5,
                'Width': 0.24222199618816376,
            },
            'Confidence': 99.99829864501953,
            'FaceId': '38271d79-7bc2-5efb-b752-398a8d575b85',
            'ImageId': 'd5631190-d039-54e4-b267-abd22c8647c5',
        },
        {
            'BoundingBox': {
                'Height': 0.03555560111999512,
                'Left': 0.37388700246810913,
                'Top': 0.2477779984474182,
                'Width': 0.04747769981622696,
            },
            'Confidence': 99.99210357666016,
            'FaceId': '3b01bef0-c883-5654-ba42-d5ad28b720b3',
            'ImageId': '812d9f04-86f9-54fc-9275-8d0dcbcb6784',
        },
        {
            'BoundingBox': {
                'Height': 0.05333330109715462,
                'Left': 0.2937690019607544,
                'Top': 0.35666701197624207,
                'Width': 0.07121659815311432,
            },
            'Confidence': 99.99919891357422,
            'FaceId': '4839a608-49d0-566c-8301-509d71b534d1',
            'ImageId': '812d9f04-86f9-54fc-9275-8d0dcbcb6784',
        },
        {
            'BoundingBox': {
                'Height': 0.3249259889125824,
                'Left': 0.5155559778213501,
                'Top': 0.1513350009918213,
                'Width': 0.24333299696445465,
            },
            'Confidence': 99.99949645996094,
            'FaceId': '70008e50-75e4-55d0-8e80-363fb73b3a14',
            'ImageId': 'd5631190-d039-54e4-b267-abd22c8647c5',
        },
        {
            'BoundingBox': {
                'Height': 0.03777780011296272,
                'Left': 0.7002969980239868,
                'Top': 0.18777799606323242,
                'Width': 0.05044509842991829,
            },
            'Confidence': 99.92639923095703,
            'FaceId': '7f5f88ed-d684-5a88-b0df-01e4a521552b',
            'ImageId': '812d9f04-86f9-54fc-9275-8d0dcbcb6784',
        },
        {
            'BoundingBox': {
                'Height': 0.05555560067296028,
                'Left': 0.13946600258350372,
                'Top': 0.46333301067352295,
                'Width': 0.07270029932260513,
            },
            'Confidence': 99.99469757080078,
            'FaceId': '895b4e2c-81de-5902-a4bd-d1792bda00b2',
            'ImageId': '812d9f04-86f9-54fc-9275-8d0dcbcb6784',
        },
        {
            'BoundingBox': {
                'Height': 0.3259260058403015,
                'Left': 0.5144439935684204,
                'Top': 0.15111100673675537,
                'Width': 0.24444399774074554,
            },
            'Confidence': 99.99949645996094,
            'FaceId': '8be04dba-4e58-520d-850e-9eae4af70eb2',
            'ImageId': '465f4e93-763e-51d0-b030-b9667a2d94b1',
        },
        {
            'BoundingBox': {
                'Height': 0.18888899683952332,
                'Left': 0.3783380091190338,
                'Top': 0.2355560064315796,
                'Width': 0.25222599506378174,
            },
            'Confidence': 99.9999008178711,
            'FaceId': '908544ad-edc3-59df-8faf-6a87cc256cf5',
            'ImageId': '3c731605-d772-541a-a5e7-0375dbc68a07',
        },
        {
            'BoundingBox': {
                'Height': 0.33481499552726746,
                'Left': 0.31888899207115173,
                'Top': 0.49333301186561584,
                'Width': 0.25,
            },
            'Confidence': 99.99909973144531,
            'FaceId': 'ff43d742-0c13-5d16-a3e8-03d3f58e980b',
            'ImageId': '465f4e93-763e-51d0-b030-b9667a2d94b1',
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.InvalidPaginationTokenException
    Rekognition.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_stream_processors(NextToken=None, MaxResults=None):
    """
    Gets a list of stream processors that you have created with  CreateStreamProcessor .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_stream_processors(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more stream processors to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of stream processors.

    :type MaxResults: integer
    :param MaxResults: Maximum number of stream processors you want Amazon Rekognition Video to return in the response. The default is 1000.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'StreamProcessors': [
        {
            'Name': 'string',
            'Status': 'STOPPED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of stream processors.

StreamProcessors (list) --
List of stream processors that you have created.

(dict) --
An object that recognizes faces in a streaming video. An Amazon Rekognition stream processor is created by a call to  CreateStreamProcessor . The request parameters for CreateStreamProcessor describe the Kinesis video stream source for the streaming video, face recognition parameters, and where to stream the analysis resullts.

Name (string) --
Name of the Amazon Rekognition stream processor.

Status (string) --
Current status of the Amazon Rekognition stream processor.











Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidPaginationTokenException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'NextToken': 'string',
        'StreamProcessors': [
            {
                'Name': 'string',
                'Status': 'STOPPED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'
            },
        ]
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidPaginationTokenException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    
    """
    pass

def recognize_celebrities(Image=None):
    """
    Returns an array of celebrities recognized in the input image. For more information, see Recognizing Celebrities in the Amazon Rekognition Developer Guide.
    For each celebrity recognized, RecognizeCelebrities returns a Celebrity object. The Celebrity object contains the celebrity name, ID, URL links to additional information, match confidence, and a ComparedFace object that you can use to locate the celebrity\'s face on the image.
    Amazon Rekognition doesn\'t retain information about which images a celebrity has been recognized in. Your application must store this information and use the Celebrity ID property as a unique identifier for the celebrity. If you don\'t store the celebrity name or additional information URLs returned by RecognizeCelebrities , you will need the ID to identify the celebrity in a call to the  GetCelebrityInfo operation.
    You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    For an example, see Recognizing Celebrities in an Image in the Amazon Rekognition Developer Guide.
    This operation requires permissions to perform the rekognition:RecognizeCelebrities operation.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Image: [REQUIRED]\nThe input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.\nIf you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the Bytes field. For more information, see Images in the Amazon Rekognition developer guide.\n\nBytes (bytes) --Blob of image bytes up to 5 MBs.\n\nS3Object (dict) --Identifies an S3 object as the image source.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
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
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
                    'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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


Response Structure

(dict) --
CelebrityFaces (list) --Details about each celebrity found in the image. Amazon Rekognition can detect a maximum of 15 celebrities in an image.

(dict) --Provides information about a celebrity recognized by the  RecognizeCelebrities operation.

Urls (list) --An array of URLs pointing to additional information about the celebrity. If there is no additional information about the celebrity, this list is empty.

(string) --


Name (string) --The name of the celebrity.

Id (string) --A unique identifier for the celebrity.

Face (dict) --Provides information about the celebrity\'s face, such as its location on the image.

BoundingBox (dict) --Bounding box of the face.

Width (float) --Width of the bounding box as a ratio of the overall image width.

Height (float) --Height of the bounding box as a ratio of the overall image height.

Left (float) --Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --Top coordinate of the bounding box as a ratio of overall image height.



Confidence (float) --Level of confidence that what the bounding box contains is a face.

Landmarks (list) --An array of facial landmarks.

(dict) --Indicates the location of the landmark on the face.

Type (string) --Type of landmark.

X (float) --The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --Indicates the pose of the face as determined by its pitch, roll, and yaw.

Roll (float) --Value representing the face rotation on the roll axis.

Yaw (float) --Value representing the face rotation on the yaw axis.

Pitch (float) --Value representing the face rotation on the pitch axis.



Quality (dict) --Identifies face image brightness and sharpness.

Brightness (float) --Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.





MatchConfidence (float) --The confidence, in percentage, that Amazon Rekognition has that the recognized face is the celebrity.





UnrecognizedFaces (list) --Details about each unrecognized face in the image.

(dict) --Provides face metadata for target image faces that are analyzed by CompareFaces and RecognizeCelebrities .

BoundingBox (dict) --Bounding box of the face.

Width (float) --Width of the bounding box as a ratio of the overall image width.

Height (float) --Height of the bounding box as a ratio of the overall image height.

Left (float) --Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --Top coordinate of the bounding box as a ratio of overall image height.



Confidence (float) --Level of confidence that what the bounding box contains is a face.

Landmarks (list) --An array of facial landmarks.

(dict) --Indicates the location of the landmark on the face.

Type (string) --Type of landmark.

X (float) --The x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the image is 700 x 200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5.

Y (float) --The y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the image is 700 x 200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.





Pose (dict) --Indicates the pose of the face as determined by its pitch, roll, and yaw.

Roll (float) --Value representing the face rotation on the roll axis.

Yaw (float) --Value representing the face rotation on the yaw axis.

Pitch (float) --Value representing the face rotation on the pitch axis.



Quality (dict) --Identifies face image brightness and sharpness.

Brightness (float) --Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

Sharpness (float) --Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.







OrientationCorrection (string) --The orientation of the input image (counterclockwise direction). If your application displays the image, you can use this value to correct the orientation. The bounding box coordinates returned in CelebrityFaces and UnrecognizedFaces represent face locations before the image orientation is corrected.

Note
If the input image is in .jpeg format, it might contain exchangeable image (Exif) metadata that includes the image\'s orientation. If so, and the Exif metadata for the input image populates the orientation field, the value of OrientationCorrection is null. The CelebrityFaces and UnrecognizedFaces bounding box coordinates represent face locations after Exif metadata is used to correct the image orientation. Images in .png format don\'t contain Exif metadata.







Exceptions

Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidImageFormatException
Rekognition.Client.exceptions.ImageTooLargeException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.InvalidImageFormatException


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
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
                        'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil'|'upperJawlineLeft'|'midJawlineLeft'|'chinBottom'|'midJawlineRight'|'upperJawlineRight',
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
    
    
    :returns: 
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidImageFormatException
    Rekognition.Client.exceptions.ImageTooLargeException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.InvalidImageFormatException
    
    """
    pass

def search_faces(CollectionId=None, FaceId=None, MaxFaces=None, FaceMatchThreshold=None):
    """
    For a given input face ID, searches for matching faces in the collection the face belongs to. You get a face ID when you add a face to the collection using the  IndexFaces operation. The operation compares the features of the input face with faces in the specified collection.
    The operation response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match that is found. Along with the metadata, the response also includes a confidence value for each face match, indicating the confidence that the specific face matches the input face.
    For an example, see Searching for a Face Using Its Face ID in the Amazon Rekognition Developer Guide.
    This operation requires permissions to perform the rekognition:SearchFaces action.
    See also: AWS API Documentation
    
    Exceptions
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
    :param CollectionId: [REQUIRED]\nID of the collection the face belongs to.\n

    :type FaceId: string
    :param FaceId: [REQUIRED]\nID of a face to find matches for in the collection.\n

    :type MaxFaces: integer
    :param MaxFaces: Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.

    :type FaceMatchThreshold: float
    :param FaceMatchThreshold: Optional value specifying the minimum confidence in the face match to return. For example, don\'t return any matches where confidence in matches is less than 70%. The default value is 80%.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

SearchedFaceId (string) --
ID of the face that was searched for matches in a collection.

FaceMatches (list) --
An array of faces that matched the input face, along with the confidence in the match.

(dict) --
Provides face metadata. In addition, it also provides the confidence in the match of this face with the input face.

Similarity (float) --
Confidence in the match of this face with the input face.

Face (dict) --
Describes the face properties such as the bounding box, face ID, image ID of the source image, and external image ID that you assigned.

FaceId (string) --
Unique identifier that Amazon Rekognition assigns to the face.

BoundingBox (dict) --
Bounding box of the face.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



ImageId (string) --
Unique identifier that Amazon Rekognition assigns to the input image.

ExternalImageId (string) --
Identifier that you assign to all the faces in the input image.

Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree).







FaceModelVersion (string) --
Version number of the face detection model associated with the input collection (CollectionId ).







Exceptions

Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException

Examples
This operation searches for matching faces in the collection the supplied face belongs to.
response = client.search_faces(
    CollectionId='myphotos',
    FaceId='70008e50-75e4-55d0-8e80-363fb73b3a14',
    FaceMatchThreshold=90,
    MaxFaces=10,
)

print(response)


Expected Output:
{
    'FaceMatches': [
        {
            'Face': {
                'BoundingBox': {
                    'Height': 0.3259260058403015,
                    'Left': 0.5144439935684204,
                    'Top': 0.15111100673675537,
                    'Width': 0.24444399774074554,
                },
                'Confidence': 99.99949645996094,
                'FaceId': '8be04dba-4e58-520d-850e-9eae4af70eb2',
                'ImageId': '465f4e93-763e-51d0-b030-b9667a2d94b1',
            },
            'Similarity': 99.97222137451172,
        },
        {
            'Face': {
                'BoundingBox': {
                    'Height': 0.16555599868297577,
                    'Left': 0.30963000655174255,
                    'Top': 0.7066670060157776,
                    'Width': 0.22074100375175476,
                },
                'Confidence': 100,
                'FaceId': '29a75abe-397b-5101-ba4f-706783b2246c',
                'ImageId': '147fdf82-7a71-52cf-819b-e786c7b9746e',
            },
            'Similarity': 97.04154968261719,
        },
        {
            'Face': {
                'BoundingBox': {
                    'Height': 0.18888899683952332,
                    'Left': 0.3783380091190338,
                    'Top': 0.2355560064315796,
                    'Width': 0.25222599506378174,
                },
                'Confidence': 99.9999008178711,
                'FaceId': '908544ad-edc3-59df-8faf-6a87cc256cf5',
                'ImageId': '3c731605-d772-541a-a5e7-0375dbc68a07',
            },
            'Similarity': 95.94520568847656,
        },
    ],
    'SearchedFaceId': '70008e50-75e4-55d0-8e80-363fb73b3a14',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def search_faces_by_image(CollectionId=None, Image=None, MaxFaces=None, FaceMatchThreshold=None, QualityFilter=None):
    """
    For a given input image, first detects the largest face in the image, and then searches the specified collection for matching faces. The operation compares the features of the input face with faces in the specified collection.
    You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.
    The response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match found. Along with the metadata, the response also includes a similarity indicating how similar the face is to the input face. In the response, the operation also returns the bounding box (and a confidence level that the bounding box contains a face) of the face that Amazon Rekognition used for the input image.
    For an example, Searching for a Face Using an Image in the Amazon Rekognition Developer Guide.
    The QualityFilter input parameter allows you to filter out detected faces that don\xe2\x80\x99t meet a required quality bar. The quality bar is based on a variety of common use cases. Use QualityFilter to set the quality bar for filtering by specifying LOW , MEDIUM , or HIGH . If you do not want to filter detected faces, specify NONE . The default value is NONE .
    This operation requires permissions to perform the rekognition:SearchFacesByImage action.
    See also: AWS API Documentation
    
    Exceptions
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
        FaceMatchThreshold=...,
        QualityFilter='NONE'|'AUTO'|'LOW'|'MEDIUM'|'HIGH'
    )
    
    
    :type CollectionId: string
    :param CollectionId: [REQUIRED]\nID of the collection to search.\n

    :type Image: dict
    :param Image: [REQUIRED]\nThe input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.\nIf you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the Bytes field. For more information, see Images in the Amazon Rekognition developer guide.\n\nBytes (bytes) --Blob of image bytes up to 5 MBs.\n\nS3Object (dict) --Identifies an S3 object as the image source.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type MaxFaces: integer
    :param MaxFaces: Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.

    :type FaceMatchThreshold: float
    :param FaceMatchThreshold: (Optional) Specifies the minimum confidence in the face match to return. For example, don\'t return any matches where confidence in matches is less than 70%. The default value is 80%.

    :type QualityFilter: string
    :param QualityFilter: A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren\'t searched for in the collection. If you specify AUTO , Amazon Rekognition chooses the quality bar. If you specify LOW , MEDIUM , or HIGH , filtering removes all faces that don\xe2\x80\x99t meet the chosen quality bar. The quality bar is based on a variety of common use cases. Low-quality detections can occur for a number of reasons. Some examples are an object that\'s misidentified as a face, a face that\'s too blurry, or a face with a pose that\'s too extreme to use. If you specify NONE , no filtering is performed. The default value is NONE .\nTo use quality filtering, the collection you are using must be associated with version 3 of the face model or higher.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --

SearchedFaceBoundingBox (dict) --
The bounding box around the face in the input image that Amazon Rekognition used for the search.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



SearchedFaceConfidence (float) --
The level of confidence that the searchedFaceBoundingBox , contains a face.

FaceMatches (list) --
An array of faces that match the input face, along with the confidence in the match.

(dict) --
Provides face metadata. In addition, it also provides the confidence in the match of this face with the input face.

Similarity (float) --
Confidence in the match of this face with the input face.

Face (dict) --
Describes the face properties such as the bounding box, face ID, image ID of the source image, and external image ID that you assigned.

FaceId (string) --
Unique identifier that Amazon Rekognition assigns to the face.

BoundingBox (dict) --
Bounding box of the face.

Width (float) --
Width of the bounding box as a ratio of the overall image width.

Height (float) --
Height of the bounding box as a ratio of the overall image height.

Left (float) --
Left coordinate of the bounding box as a ratio of overall image width.

Top (float) --
Top coordinate of the bounding box as a ratio of overall image height.



ImageId (string) --
Unique identifier that Amazon Rekognition assigns to the input image.

ExternalImageId (string) --
Identifier that you assign to all the faces in the input image.

Confidence (float) --
Confidence level that the bounding box contains a face (and not a different object such as a tree).







FaceModelVersion (string) --
Version number of the face detection model associated with the input collection (CollectionId ).







Exceptions

Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ImageTooLargeException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.InvalidImageFormatException

Examples
This operation searches for faces in a Rekognition collection that match the largest face in an S3 bucket stored image.
response = client.search_faces_by_image(
    CollectionId='myphotos',
    FaceMatchThreshold=95,
    Image={
        'S3Object': {
            'Bucket': 'mybucket',
            'Name': 'myphoto',
        },
    },
    MaxFaces=5,
)

print(response)


Expected Output:
{
    'FaceMatches': [
        {
            'Face': {
                'BoundingBox': {
                    'Height': 0.3234420120716095,
                    'Left': 0.3233329951763153,
                    'Top': 0.5,
                    'Width': 0.24222199618816376,
                },
                'Confidence': 99.99829864501953,
                'FaceId': '38271d79-7bc2-5efb-b752-398a8d575b85',
                'ImageId': 'd5631190-d039-54e4-b267-abd22c8647c5',
            },
            'Similarity': 99.97036743164062,
        },
    ],
    'SearchedFaceBoundingBox': {
        'Height': 0.33481481671333313,
        'Left': 0.31888890266418457,
        'Top': 0.4933333396911621,
        'Width': 0.25,
    },
    'SearchedFaceConfidence': 99.9991226196289,
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.ImageTooLargeException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.InvalidImageFormatException
    
    """
    pass

def start_celebrity_recognition(Video=None, ClientRequestToken=None, NotificationChannel=None, JobTag=None):
    """
    Starts asynchronous recognition of celebrities in a stored video.
    Amazon Rekognition Video can detect celebrities in a video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartCelebrityRecognition returns a job identifier (JobId ) which you use to get the results of the analysis. When celebrity recognition analysis is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel . To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call  GetCelebrityRecognition and pass the job identifier (JobId ) from the initial call to StartCelebrityRecognition .
    For more information, see Recognizing Celebrities in the Amazon Rekognition Developer Guide.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Video: [REQUIRED]\nThe video in which you want to recognize celebrities. The video must be stored in an Amazon S3 bucket.\n\nS3Object (dict) --The Amazon S3 bucket name and file name for the video.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartCelebrityRecognition requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status of the celebrity recognition analysis to.\n\nSNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.\n\nRoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.\n\n\n

    :type JobTag: string
    :param JobTag: An identifier you specify that\'s returned in the completion notification that\'s published to your Amazon Simple Notification Service topic. For example, you can use JobTag to group related jobs and identify them in the completion notification.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier for the celebrity recognition analysis job. Use JobId to identify the job in a subsequent call to GetCelebrityRecognition .







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.IdempotentParameterMismatchException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.VideoTooLargeException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.ThrottlingException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.IdempotentParameterMismatchException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.VideoTooLargeException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def start_content_moderation(Video=None, MinConfidence=None, ClientRequestToken=None, NotificationChannel=None, JobTag=None):
    """
    Starts asynchronous detection of unsafe content in a stored video.
    Amazon Rekognition Video can moderate content in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartContentModeration returns a job identifier (JobId ) which you use to get the results of the analysis. When unsafe content analysis is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel .
    To get the results of the unsafe content analysis, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call  GetContentModeration and pass the job identifier (JobId ) from the initial call to StartContentModeration .
    For more information, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Video: [REQUIRED]\nThe video in which you want to detect unsafe content. The video must be stored in an Amazon S3 bucket.\n\nS3Object (dict) --The Amazon S3 bucket name and file name for the video.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type MinConfidence: float
    :param MinConfidence: Specifies the minimum confidence that Amazon Rekognition must have in order to return a moderated content label. Confidence represents how certain Amazon Rekognition is that the moderated content is correctly identified. 0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition doesn\'t return any moderated content labels with a confidence level lower than this specified value. If you don\'t specify MinConfidence , GetContentModeration returns labels with confidence values greater than or equal to 50 percent.

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartContentModeration requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status of the unsafe content analysis to.\n\nSNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.\n\nRoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.\n\n\n

    :type JobTag: string
    :param JobTag: An identifier you specify that\'s returned in the completion notification that\'s published to your Amazon Simple Notification Service topic. For example, you can use JobTag to group related jobs and identify them in the completion notification.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier for the unsafe content analysis job. Use JobId to identify the job in a subsequent call to GetContentModeration .







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.IdempotentParameterMismatchException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.VideoTooLargeException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.ThrottlingException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.IdempotentParameterMismatchException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.VideoTooLargeException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def start_face_detection(Video=None, ClientRequestToken=None, NotificationChannel=None, FaceAttributes=None, JobTag=None):
    """
    Starts asynchronous detection of faces in a stored video.
    Amazon Rekognition Video can detect faces in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartFaceDetection returns a job identifier (JobId ) that you use to get the results of the operation. When face detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel . To get the results of the face detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call  GetFaceDetection and pass the job identifier (JobId ) from the initial call to StartFaceDetection .
    For more information, see Detecting Faces in a Stored Video in the Amazon Rekognition Developer Guide.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Video: [REQUIRED]\nThe video in which you want to detect faces. The video must be stored in an Amazon S3 bucket.\n\nS3Object (dict) --The Amazon S3 bucket name and file name for the video.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartFaceDetection requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type NotificationChannel: dict
    :param NotificationChannel: The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the face detection operation.\n\nSNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.\n\nRoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.\n\n\n

    :type FaceAttributes: string
    :param FaceAttributes: The face attributes you want returned.\n\nDEFAULT - The following subset of facial attributes are returned: BoundingBox, Confidence, Pose, Quality and Landmarks.ALL - All facial attributes are returned.\n\n

    :type JobTag: string
    :param JobTag: An identifier you specify that\'s returned in the completion notification that\'s published to your Amazon Simple Notification Service topic. For example, you can use JobTag to group related jobs and identify them in the completion notification.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier for the face detection job. Use JobId to identify the job in a subsequent call to GetFaceDetection .







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.IdempotentParameterMismatchException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.VideoTooLargeException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.ThrottlingException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.IdempotentParameterMismatchException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.VideoTooLargeException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def start_face_search(Video=None, ClientRequestToken=None, FaceMatchThreshold=None, CollectionId=None, NotificationChannel=None, JobTag=None):
    """
    Starts the asynchronous search for faces in a collection that match the faces of persons detected in a stored video.
    The video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartFaceSearch returns a job identifier (JobId ) which you use to get the search results once the search has completed. When searching is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel . To get the search results, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call  GetFaceSearch and pass the job identifier (JobId ) from the initial call to StartFaceSearch . For more information, see  procedure-person-search-videos .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Video: [REQUIRED]\nThe video you want to search. The video must be stored in an Amazon S3 bucket.\n\nS3Object (dict) --The Amazon S3 bucket name and file name for the video.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartFaceSearch requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type FaceMatchThreshold: float
    :param FaceMatchThreshold: The minimum confidence in the person match to return. For example, don\'t return any matches where confidence in matches is less than 70%. The default value is 80%.

    :type CollectionId: string
    :param CollectionId: [REQUIRED]\nID of the collection that contains the faces you want to search for.\n

    :type NotificationChannel: dict
    :param NotificationChannel: The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the search.\n\nSNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.\n\nRoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.\n\n\n

    :type JobTag: string
    :param JobTag: An identifier you specify that\'s returned in the completion notification that\'s published to your Amazon Simple Notification Service topic. For example, you can use JobTag to group related jobs and identify them in the completion notification.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier for the search job. Use JobId to identify the job in a subsequent call to GetFaceSearch .







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.IdempotentParameterMismatchException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.VideoTooLargeException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ThrottlingException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.IdempotentParameterMismatchException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.VideoTooLargeException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def start_label_detection(Video=None, ClientRequestToken=None, MinConfidence=None, NotificationChannel=None, JobTag=None):
    """
    Starts asynchronous detection of labels in a stored video.
    Amazon Rekognition Video can detect labels in a video. Labels are instances of real-world entities. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; concepts like landscape, evening, and nature; and activities like a person getting out of a car or a person skiing.
    The video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartLabelDetection returns a job identifier (JobId ) which you use to get the results of the operation. When label detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel .
    To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call  GetLabelDetection and pass the job identifier (JobId ) from the initial call to StartLabelDetection .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Video: [REQUIRED]\nThe video in which you want to detect labels. The video must be stored in an Amazon S3 bucket.\n\nS3Object (dict) --The Amazon S3 bucket name and file name for the video.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartLabelDetection requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type MinConfidence: float
    :param MinConfidence: Specifies the minimum confidence that Amazon Rekognition Video must have in order to return a detected label. Confidence represents how certain Amazon Rekognition is that a label is correctly identified.0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition Video doesn\'t return any labels with a confidence level lower than this specified value.\nIf you don\'t specify MinConfidence , the operation returns labels with confidence values greater than or equal to 50 percent.\n

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion status of the label detection operation to.\n\nSNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.\n\nRoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.\n\n\n

    :type JobTag: string
    :param JobTag: An identifier you specify that\'s returned in the completion notification that\'s published to your Amazon Simple Notification Service topic. For example, you can use JobTag to group related jobs and identify them in the completion notification.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier for the label detection job. Use JobId to identify the job in a subsequent call to GetLabelDetection .







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.IdempotentParameterMismatchException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.VideoTooLargeException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.ThrottlingException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.IdempotentParameterMismatchException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.VideoTooLargeException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def start_person_tracking(Video=None, ClientRequestToken=None, NotificationChannel=None, JobTag=None):
    """
    Starts the asynchronous tracking of a person\'s path in a stored video.
    Amazon Rekognition Video can track the path of people in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartPersonTracking returns a job identifier (JobId ) which you use to get the results of the operation. When label detection is finished, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel .
    To get the results of the person detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call  GetPersonTracking and pass the job identifier (JobId ) from the initial call to StartPersonTracking .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Video: [REQUIRED]\nThe video in which you want to detect people. The video must be stored in an Amazon S3 bucket.\n\nS3Object (dict) --The Amazon S3 bucket name and file name for the video.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartPersonTracking requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidently started more than once.

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion status of the people detection operation to.\n\nSNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.\n\nRoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.\n\n\n

    :type JobTag: string
    :param JobTag: An identifier you specify that\'s returned in the completion notification that\'s published to your Amazon Simple Notification Service topic. For example, you can use JobTag to group related jobs and identify them in the completion notification.

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier for the person detection job. Use JobId to identify the job in a subsequent call to GetPersonTracking .







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.IdempotentParameterMismatchException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.VideoTooLargeException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.ThrottlingException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.IdempotentParameterMismatchException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.VideoTooLargeException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def start_project_version(ProjectVersionArn=None, MinInferenceUnits=None):
    """
    Starts the running of the version of a model. Starting a model takes a while to complete. To check the current state of the model, use  DescribeProjectVersions .
    Once the model is running, you can detect custom labels in new images by calling  DetectCustomLabels .
    This operation requires permissions to perform the rekognition:StartProjectVersion action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_project_version(
        ProjectVersionArn='string',
        MinInferenceUnits=123
    )
    
    
    :type ProjectVersionArn: string
    :param ProjectVersionArn: [REQUIRED]\nThe Amazon Resource Name(ARN) of the model version that you want to start.\n

    :type MinInferenceUnits: integer
    :param MinInferenceUnits: [REQUIRED]\nThe minimum number of inference units to use. A single inference unit represents 1 hour of processing and can support up to 5 Transaction Pers Second (TPS). Use a higher number to increase the TPS throughput of your model. You are charged for the number of inference units that you use.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Status': 'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'|'TRAINING_FAILED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'|'STOPPED'|'DELETING'
}


Response Structure

(dict) --

Status (string) --
The current running status of the model.







Exceptions

Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ResourceInUseException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'Status': 'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'|'TRAINING_FAILED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'|'STOPPED'|'DELETING'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ResourceInUseException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    
    """
    pass

def start_stream_processor(Name=None):
    """
    Starts processing a stream processor. You create a stream processor by calling  CreateStreamProcessor . To tell StartStreamProcessor which stream processor to start, use the value of the Name field specified in the call to CreateStreamProcessor .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_stream_processor(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the stream processor to start processing.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ResourceInUseException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {}
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ResourceInUseException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    
    """
    pass

def start_text_detection(Video=None, ClientRequestToken=None, NotificationChannel=None, JobTag=None, Filters=None):
    """
    Starts asynchronous detection of text in a stored video.
    Amazon Rekognition Video can detect text in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. StartTextDetection returns a job identifier (JobId ) which you use to get the results of the operation. When text detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in NotificationChannel .
    To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . if so, call  GetTextDetection and pass the job identifier (JobId ) from the initial call to StartTextDetection .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_text_detection(
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
        JobTag='string',
        Filters={
            'WordFilter': {
                'MinConfidence': ...,
                'MinBoundingBoxHeight': ...,
                'MinBoundingBoxWidth': ...
            },
            'RegionsOfInterest': [
                {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    }
                },
            ]
        }
    )
    
    
    :type Video: dict
    :param Video: [REQUIRED]\nVideo file stored in an Amazon S3 bucket. Amazon Rekognition video start operations such as StartLabelDetection use Video to specify a video for analysis. The supported file formats are .mp4, .mov and .avi.\n\nS3Object (dict) --The Amazon S3 bucket name and file name for the video.\n\nBucket (string) --Name of the S3 bucket.\n\nName (string) --S3 object key name.\n\nVersion (string) --If the bucket is versioning enabled, you can specify the object version.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: Idempotent token used to identify the start request. If you use the same token with multiple StartTextDetection requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidentaly started more than once.

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the completion status of a video analysis operation. For more information, see api-video .\n\nSNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic to which Amazon Rekognition to posts the completion status.\n\nRoleArn (string) -- [REQUIRED]The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic.\n\n\n

    :type JobTag: string
    :param JobTag: An identifier returned in the completion status published by your Amazon Simple Notification Service topic. For example, you can use JobTag to group related jobs and identify them in the completion notification.

    :type Filters: dict
    :param Filters: Optional parameters that let you set criteria the text must meet to be included in your response.\n\nWordFilter (dict) --Filters focusing on qualities of the text, such as confidence or size.\n\nMinConfidence (float) --Sets confidence of word detection. Words with detection confidence below this will be excluded from the result. Values should be between 0.5 and 1 as Text in Video will not return any result below 0.5.\n\nMinBoundingBoxHeight (float) --Sets the minimum height of the word bounding box. Words with bounding box heights lesser than this value will be excluded from the result. Value is relative to the video frame height.\n\nMinBoundingBoxWidth (float) --Sets the minimum width of the word bounding box. Words with bounding boxes widths lesser than this value will be excluded from the result. Value is relative to the video frame width.\n\n\n\nRegionsOfInterest (list) --Filter focusing on a certain area of the frame. Uses a BoundingBox object to set the region of the screen.\n\n(dict) --Specifies a location within the frame that Rekognition checks for text. Uses a BoundingBox object to set a region of the screen.\nA word is included in the region if the word is more than half in that region. If there is more than one region, the word will be compared with all regions of the screen. Any word more than half in a region is kept in the results.\n\nBoundingBox (dict) --The box representing a region of interest on screen.\n\nWidth (float) --Width of the bounding box as a ratio of the overall image width.\n\nHeight (float) --Height of the bounding box as a ratio of the overall image height.\n\nLeft (float) --Left coordinate of the bounding box as a ratio of overall image width.\n\nTop (float) --Top coordinate of the bounding box as a ratio of overall image height.\n\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
Identifier for the text detection job. Use JobId to identify the job in a subsequent call to GetTextDetection .







Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.IdempotentParameterMismatchException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.InvalidS3ObjectException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.VideoTooLargeException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException
Rekognition.Client.exceptions.LimitExceededException
Rekognition.Client.exceptions.ThrottlingException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.IdempotentParameterMismatchException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.InvalidS3ObjectException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.VideoTooLargeException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    Rekognition.Client.exceptions.LimitExceededException
    Rekognition.Client.exceptions.ThrottlingException
    
    """
    pass

def stop_project_version(ProjectVersionArn=None):
    """
    Stops a running model. The operation might take a while to complete. To check the current status, call  DescribeProjectVersions .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_project_version(
        ProjectVersionArn='string'
    )
    
    
    :type ProjectVersionArn: string
    :param ProjectVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the model version that you want to delete.\nThis operation requires permissions to perform the rekognition:StopProjectVersion action.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Status': 'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'|'TRAINING_FAILED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'|'STOPPED'|'DELETING'
}


Response Structure

(dict) --
Status (string) --The current status of the stop operation.






Exceptions

Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ResourceInUseException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {
        'Status': 'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'|'TRAINING_FAILED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'|'STOPPED'|'DELETING'
    }
    
    
    """
    pass

def stop_stream_processor(Name=None):
    """
    Stops a running stream processor that was created by  CreateStreamProcessor .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_stream_processor(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of a stream processor created by CreateStreamProcessor .\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

Rekognition.Client.exceptions.AccessDeniedException
Rekognition.Client.exceptions.InternalServerError
Rekognition.Client.exceptions.ThrottlingException
Rekognition.Client.exceptions.InvalidParameterException
Rekognition.Client.exceptions.ResourceNotFoundException
Rekognition.Client.exceptions.ResourceInUseException
Rekognition.Client.exceptions.ProvisionedThroughputExceededException


    :return: {}
    
    
    :returns: 
    Rekognition.Client.exceptions.AccessDeniedException
    Rekognition.Client.exceptions.InternalServerError
    Rekognition.Client.exceptions.ThrottlingException
    Rekognition.Client.exceptions.InvalidParameterException
    Rekognition.Client.exceptions.ResourceNotFoundException
    Rekognition.Client.exceptions.ResourceInUseException
    Rekognition.Client.exceptions.ProvisionedThroughputExceededException
    
    """
    pass

