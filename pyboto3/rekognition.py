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
    Compares a face in the source input image with each face detected in the target input image.
    In response, the operation returns an array of face matches ordered by similarity score in descending order. For each face match, the response provides a bounding box of the face, facial landmarks, pose details (pitch, role, and yaw), quality (brightness and sharpness), and confidence value (indicating the level of confidence that the bounding box contains a face). The response also provides a similarity score, which indicates how closely the faces match.
    If the image doesn't contain Exif metadata, CompareFaces returns orientation information for the source and target images. Use these values to display the images with the correct image orientation.
    For an example, see  get-started-exercise-compare-faces .
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
            The source image, either as bytes or as an S3 object.
            Bytes (bytes) --Blob of image bytes up to 5 MBs.
            S3Object (dict) --Identifies an S3 object as the image source.
            Bucket (string) --Name of the S3 bucket.
            Name (string) --S3 object key name.
            Version (string) --If the bucket is versioning enabled, you can specify the object version.
            
            

    :type TargetImage: dict
    :param TargetImage: [REQUIRED]
            The target image, either as bytes or as an S3 object.
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
                            'Type': 'EYE_LEFT'|'EYE_RIGHT'|'NOSE'|'MOUTH_LEFT'|'MOUTH_RIGHT'|'LEFT_EYEBROW_LEFT'|'LEFT_EYEBROW_RIGHT'|'LEFT_EYEBROW_UP'|'RIGHT_EYEBROW_LEFT'|'RIGHT_EYEBROW_RIGHT'|'RIGHT_EYEBROW_UP'|'LEFT_EYE_LEFT'|'LEFT_EYE_RIGHT'|'LEFT_EYE_UP'|'LEFT_EYE_DOWN'|'RIGHT_EYE_LEFT'|'RIGHT_EYE_RIGHT'|'RIGHT_EYE_UP'|'RIGHT_EYE_DOWN'|'NOSE_LEFT'|'NOSE_RIGHT'|'MOUTH_UP'|'MOUTH_DOWN'|'LEFT_PUPIL'|'RIGHT_PUPIL',
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
                        'Type': 'EYE_LEFT'|'EYE_RIGHT'|'NOSE'|'MOUTH_LEFT'|'MOUTH_RIGHT'|'LEFT_EYEBROW_LEFT'|'LEFT_EYEBROW_RIGHT'|'LEFT_EYEBROW_UP'|'RIGHT_EYEBROW_LEFT'|'RIGHT_EYEBROW_RIGHT'|'RIGHT_EYEBROW_UP'|'LEFT_EYE_LEFT'|'LEFT_EYE_RIGHT'|'LEFT_EYE_UP'|'LEFT_EYE_DOWN'|'RIGHT_EYE_LEFT'|'RIGHT_EYE_RIGHT'|'RIGHT_EYE_UP'|'RIGHT_EYE_DOWN'|'NOSE_LEFT'|'NOSE_RIGHT'|'MOUTH_UP'|'MOUTH_DOWN'|'LEFT_PUPIL'|'RIGHT_PUPIL',
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
    For an example, see  example1 .
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
        'CollectionArn': 'string'
    }
    
    
    """
    pass

def delete_collection(CollectionId=None):
    """
    Deletes the specified collection. Note that this operation removes all faces in the collection. For an example, see  example1 .
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

def detect_faces(Image=None, Attributes=None):
    """
    Detects faces within an image (JPEG or PNG) that is provided as input.
    For each face detected, the operation returns face details including a bounding box of the face, a confidence value (that the bounding box contains a face), and a fixed set of attributes such as facial landmarks (for example, coordinates of eye and mouth), gender, presence of beard, sunglasses, etc.
    The face-detection algorithm is most effective on frontal faces. For non-frontal or obscured faces, the algorithm may not detect the faces or might detect faces with lower confidence.
    For an example, see  get-started-exercise-detect-faces .
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
            The image in which you want to detect faces. You can specify a blob or an S3 object.
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
                    'Value': 'MALE'|'FEMALE',
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
                        'Type': 'EYE_LEFT'|'EYE_RIGHT'|'NOSE'|'MOUTH_LEFT'|'MOUTH_RIGHT'|'LEFT_EYEBROW_LEFT'|'LEFT_EYEBROW_RIGHT'|'LEFT_EYEBROW_UP'|'RIGHT_EYEBROW_LEFT'|'RIGHT_EYEBROW_RIGHT'|'RIGHT_EYEBROW_UP'|'LEFT_EYE_LEFT'|'LEFT_EYE_RIGHT'|'LEFT_EYE_UP'|'LEFT_EYE_DOWN'|'RIGHT_EYE_LEFT'|'RIGHT_EYE_RIGHT'|'RIGHT_EYE_UP'|'RIGHT_EYE_DOWN'|'NOSE_LEFT'|'NOSE_RIGHT'|'MOUTH_UP'|'MOUTH_DOWN'|'LEFT_PUPIL'|'RIGHT_PUPIL',
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
    Detects instances of real-world labels within an image (JPEG or PNG) provided as input. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; and concepts like landscape, evening, and nature. For an example, see  get-started-exercise-detect-labels .
    For each object, scene, and concept the API returns one or more labels. Each label provides the object name, and the level of confidence that the image contains the object. For example, suppose the input image has a lighthouse, the sea, and a rock. The response will include all three labels, one for each object.
    In the preceding example, the operation returns one label for each of the three objects. The operation can also return multiple labels for the same object in the image. For example, if the input image shows a flower (for example, a tulip), the operation might return the following three labels.
    In this example, the detection algorithm more precisely identifies the flower as a tulip.
    You can provide the input image as an S3 object or as base64-encoded bytes. In response, the API returns an array of labels. In addition, the response also includes the orientation correction. Optionally, you can specify MinConfidence to control the confidence threshold for the labels returned. The default is 50%. You can also add the MaxLabels parameter to limit the number of labels returned.
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
            The input image. You can provide a blob of image bytes or an S3 object.
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
    To filter images, use the labels returned by DetectModerationLabels to determine which types of content are appropriate. For information about moderation labels, see  howitworks-moderateimage .
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
            Provides the source image either as bytes or an S3 object.
            You pass image bytes to a Rekognition API operation by using the Bytes property. For example, you would use the Bytes property to pass an image loaded from a local file system. Image bytes passed by using the Bytes property must be base64-encoded. Your code may not need to encode image bytes if you are using an AWS SDK to call Rekognition API operations. For more information, see example4 .
            You pass images stored in an S3 bucket to a Rekognition API operation by using the S3Object property. Images stored in an S3 bucket do not need to be base64-encoded.
            The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
            If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes using the Bytes property is not supported. You must first upload the image to an Amazon S3 bucket and then call the operation using the S3Object property.
            For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see manage-access-resource-policies .
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

def index_faces(CollectionId=None, Image=None, ExternalImageId=None, DetectionAttributes=None):
    """
    Detects faces in the input image and adds them to the specified collection.
    Amazon Rekognition does not save the actual faces detected. Instead, the underlying detection algorithm first detects the faces in the input image, and for each face extracts facial features into a feature vector, and stores it in the back-end database. Amazon Rekognition uses feature vectors when performing face match and search operations using the and operations.
    If you provide the optional externalImageID for the input image you provided, Amazon Rekognition associates this ID with all faces that it detects. When you call the operation, the response returns the external ID. You can use this external image ID to create a client-side index to associate the faces with each image. You can then use the index to find all faces in an image.
    In response, the operation returns an array of metadata for all detected faces. This includes, the bounding box of the detected face, confidence value (indicating the bounding box contains a face), a face ID assigned by the service for each face that is detected and stored, and an image ID assigned by the service for the input image If you request all facial attributes (using the detectionAttributes parameter, Amazon Rekognition returns detailed facial attributes such as facial landmarks (for example, location of eye and mount) and other facial attributes such gender. If you provide the same image, specify the same collection, and use the same external ID in the IndexFaces operation, Amazon Rekognition doesn't save duplicate face metadata.
    For an example, see  example2 .
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
            Provides the source image either as bytes or an S3 object.
            You pass image bytes to a Rekognition API operation by using the Bytes property. For example, you would use the Bytes property to pass an image loaded from a local file system. Image bytes passed by using the Bytes property must be base64-encoded. Your code may not need to encode image bytes if you are using an AWS SDK to call Rekognition API operations. For more information, see example4 .
            You pass images stored in an S3 bucket to a Rekognition API operation by using the S3Object property. Images stored in an S3 bucket do not need to be base64-encoded.
            The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
            If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes using the Bytes property is not supported. You must first upload the image to an Amazon S3 bucket and then call the operation using the S3Object property.
            For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see manage-access-resource-policies .
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
                        'Value': 'MALE'|'FEMALE',
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
                            'Type': 'EYE_LEFT'|'EYE_RIGHT'|'NOSE'|'MOUTH_LEFT'|'MOUTH_RIGHT'|'LEFT_EYEBROW_LEFT'|'LEFT_EYEBROW_RIGHT'|'LEFT_EYEBROW_UP'|'RIGHT_EYEBROW_LEFT'|'RIGHT_EYEBROW_RIGHT'|'RIGHT_EYEBROW_UP'|'LEFT_EYE_LEFT'|'LEFT_EYE_RIGHT'|'LEFT_EYE_UP'|'LEFT_EYE_DOWN'|'RIGHT_EYE_LEFT'|'RIGHT_EYE_RIGHT'|'RIGHT_EYE_UP'|'RIGHT_EYE_DOWN'|'NOSE_LEFT'|'NOSE_RIGHT'|'MOUTH_UP'|'MOUTH_DOWN'|'LEFT_PUPIL'|'RIGHT_PUPIL',
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
        'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
    }
    
    
    """
    pass

def list_collections(NextToken=None, MaxResults=None):
    """
    Returns list of collection IDs in your account. If the result is truncated, the response also provides a NextToken that you can use in the subsequent request to fetch the next set of collection IDs.
    For an example, see  example1 .
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
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_faces(CollectionId=None, NextToken=None, MaxResults=None):
    """
    Returns metadata for faces in the specified collection. This metadata includes information such as the bounding box coordinates, the confidence (that the bounding box contains a face), and face ID. For an example, see  example3 .
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
        'NextToken': 'string'
    }
    
    
    """
    pass

def search_faces(CollectionId=None, FaceId=None, MaxFaces=None, FaceMatchThreshold=None):
    """
    For a given input face ID, searches for matching faces in the collection the face belongs to. You get a face ID when you add a face to the collection using the  IndexFaces operation. The operation compares the features of the input face with faces in the specified collection.
    The operation response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match that is found. Along with the metadata, the response also includes a confidence value for each face match, indicating the confidence that the specific face matches the input face.
    For an example, see  example3 .
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
        ]
    }
    
    
    """
    pass

def search_faces_by_image(CollectionId=None, Image=None, MaxFaces=None, FaceMatchThreshold=None):
    """
    For a given input image, first detects the largest face in the image, and then searches the specified collection for matching faces. The operation compares the features of the input face with faces in the specified collection.
    The response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match found. Along with the metadata, the response also includes a similarity indicating how similar the face is to the input face. In the response, the operation also returns the bounding box (and a confidence level that the bounding box contains a face) of the face that Amazon Rekognition used for the input image.
    For an example, see  example3 .
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
            Provides the source image either as bytes or an S3 object.
            You pass image bytes to a Rekognition API operation by using the Bytes property. For example, you would use the Bytes property to pass an image loaded from a local file system. Image bytes passed by using the Bytes property must be base64-encoded. Your code may not need to encode image bytes if you are using an AWS SDK to call Rekognition API operations. For more information, see example4 .
            You pass images stored in an S3 bucket to a Rekognition API operation by using the S3Object property. Images stored in an S3 bucket do not need to be base64-encoded.
            The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
            If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes using the Bytes property is not supported. You must first upload the image to an Amazon S3 bucket and then call the operation using the S3Object property.
            For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see manage-access-resource-policies .
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
        ]
    }
    
    
    """
    pass

