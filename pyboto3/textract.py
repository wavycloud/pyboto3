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

def analyze_document(Document=None, FeatureTypes=None, HumanLoopConfig=None):
    """
    Analyzes an input document for relationships between detected items.
    The types of information returned are as follows:
    Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT Block object contains information about a selection element, including the selection status.
    You can choose which type of analysis to perform by specifying the FeatureTypes list.
    The output is returned in a list of Block objects.
    For more information, see Document Text Analysis .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.analyze_document(
        Document={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        FeatureTypes=[
            'TABLES'|'FORMS',
        ],
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
    
    
    :type Document: dict
    :param Document: [REQUIRED]\nThe input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can\'t pass image bytes. The document must be an image in JPEG or PNG format.\nIf you\'re using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes that are passed using the Bytes field.\n\nBytes (bytes) --A blob of base64-encoded document bytes. The maximum size of a document that\'s provided in a blob of bytes is 5 MB. The document bytes must be in PNG or JPEG format.\nIf you\'re using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes passed using the Bytes field.\n\nS3Object (dict) --Identifies an S3 object as the document source. The maximum size of a document that\'s stored in an S3 bucket is 5 MB.\n\nBucket (string) --The name of the S3 bucket.\n\nName (string) --The file name of the input document. Synchronous operations can use image files that are in JPEG or PNG format. Asynchronous operations also support PDF format files.\n\nVersion (string) --If the bucket has versioning enabled, you can specify the object version.\n\n\n\n\n

    :type FeatureTypes: list
    :param FeatureTypes: [REQUIRED]\nA list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. To perform both types of analysis, add TABLES and FORMS to FeatureTypes . All lines and words detected in the document are included in the response (including text that isn\'t related to the value of FeatureTypes ).\n\n(string) --\n\n

    :type HumanLoopConfig: dict
    :param HumanLoopConfig: Sets the configuration for the human in the loop workflow for analyzing documents.\n\nHumanLoopName (string) -- [REQUIRED]The name of the human workflow used for this image. This should be kept unique within a region.\n\nFlowDefinitionArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the flow definition.\n\nDataAttributes (dict) --Sets attributes of the input data.\n\nContentClassifiers (list) --Sets whether the input image is free of personally identifiable information or adult content.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'DocumentMetadata': {
        'Pages': 123
    },
    'Blocks': [
        {
            'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
            'Confidence': ...,
            'Text': 'string',
            'RowIndex': 123,
            'ColumnIndex': 123,
            'RowSpan': 123,
            'ColumnSpan': 123,
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
            },
            'Id': 'string',
            'Relationships': [
                {
                    'Type': 'VALUE'|'CHILD',
                    'Ids': [
                        'string',
                    ]
                },
            ],
            'EntityTypes': [
                'KEY'|'VALUE',
            ],
            'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
            'Page': 123
        },
    ],
    'HumanLoopActivationOutput': {
        'HumanLoopArn': 'string',
        'HumanLoopActivationReasons': [
            'string',
        ],
        'HumanLoopActivationConditionsEvaluationResults': 'string'
    },
    'AnalyzeDocumentModelVersion': 'string'
}


Response Structure

(dict) --

DocumentMetadata (dict) --
Metadata about the analyzed document. An example is the number of pages.

Pages (integer) --
The number of pages that are detected in the document.



Blocks (list) --
The items that are detected and analyzed by AnalyzeDocument .

(dict) --
A Block represents items that are recognized in a document within a group of pixels close to each other. The information returned in a Block object depends on the type of operation. In text detection for documents (for example  DetectDocumentText ), you get information about the detected words and lines of text. In text analysis (for example  AnalyzeDocument ), you can also get information about the fields, tables, and selection elements that are detected in the document.
An array of Block objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as  DetectDocumentText , the array of Block objects is the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the array is returned over one or more responses.
For more information, see How Amazon Textract Works .

BlockType (string) --
The type of text item that\'s recognized. In operations for text detection, the following types are returned:

PAGE - Contains a list of the LINE Block objects that are detected on a document page.
WORD - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren\'t separated by spaces.
LINE - A string of tab-delimited, contiguous words that are detected on a document page.

In text analysis operations, the following types are returned:

PAGE - Contains a list of child Block objects that are detected on a document page.
KEY_VALUE_SET - Stores the KEY and VALUE Block objects for linked text that\'s detected on a document page. Use the EntityType field to determine if a KEY_VALUE_SET object is a KEY Block object or a VALUE Block object.
WORD - A word that\'s detected on a document page. A word is one or more ISO basic Latin script characters that aren\'t separated by spaces.
LINE - A string of tab-delimited, contiguous words that are detected on a document page.
TABLE - A table that\'s detected on a document page. A table is grid-based information with two or more rows or columns, with a cell span of one row and one column each.
CELL - A cell within a detected table. The cell is the parent of the block that contains the text in the cell.
SELECTION_ELEMENT - A selection element such as an option button (radio button) or a check box that\'s detected on a document page. Use the value of SelectionStatus to determine the status of the selection element.


Confidence (float) --
The confidence score that Amazon Textract has in the accuracy of the recognized text and the accuracy of the geometry points around the recognized text.

Text (string) --
The word or line of text that\'s recognized by Amazon Textract.

RowIndex (integer) --
The row in which a table cell is located. The first row position is 1. RowIndex isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

ColumnIndex (integer) --
The column in which a table cell appears. The first column position is 1. ColumnIndex isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

RowSpan (integer) --
The number of rows that a table cell spans. Currently this value is always 1, even if the number of rows spanned is greater than 1. RowSpan isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

ColumnSpan (integer) --
The number of columns that a table cell spans. Currently this value is always 1, even if the number of columns spanned is greater than 1. ColumnSpan isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

Geometry (dict) --
The location of the recognized text on the image. It includes an axis-aligned, coarse bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial information.

BoundingBox (dict) --
An axis-aligned coarse representation of the location of the recognized item on the document page.

Width (float) --
The width of the bounding box as a ratio of the overall document page width.

Height (float) --
The height of the bounding box as a ratio of the overall document page height.

Left (float) --
The left coordinate of the bounding box as a ratio of overall document page width.

Top (float) --
The top coordinate of the bounding box as a ratio of overall document page height.



Polygon (list) --
Within the bounding box, a fine-grained polygon around the recognized item.

(dict) --
The X and Y coordinates of a point on a document page. The X and Y values that are returned are ratios of the overall document page size. For example, if the input document is 700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the document page.
An array of Point objects, Polygon , is returned by  DetectDocumentText . Polygon represents a fine-grained polygon around detected text. For more information, see Geometry in the Amazon Textract Developer Guide.

X (float) --
The value of the X coordinate for a point on a Polygon .

Y (float) --
The value of the Y coordinate for a point on a Polygon .







Id (string) --
The identifier for the recognized text. The identifier is only unique for a single operation.

Relationships (list) --
A list of child blocks of the current block. For example, a LINE object has child blocks for each WORD block that\'s part of the line of text. There aren\'t Relationship objects in the list for relationships that don\'t exist, such as when the current block has no child blocks. The list size can be the following:

0 - The block has no child blocks.
1 - The block has child blocks.


(dict) --
Information about how blocks are related to each other. A Block object contains 0 or more Relation objects in a list, Relationships . For more information, see  Block .
The Type element provides the type of the relationship for all blocks in the IDs array.

Type (string) --
The type of relationship that the blocks in the IDs array have with the current block. The relationship can be VALUE or CHILD . A relationship of type VALUE is a list that contains the ID of the VALUE block that\'s associated with the KEY of a key-value pair. A relationship of type CHILD is a list of IDs that identify WORD blocks.

Ids (list) --
An array of IDs for related blocks. You can get the type of the relationship from the Type element.

(string) --






EntityTypes (list) --
The type of entity. The following can be returned:

KEY - An identifier for a field on the document.
VALUE - The field text.


EntityTypes isn\'t returned by DetectDocumentText and GetDocumentTextDetection .


(string) --


SelectionStatus (string) --
The selection status of a selection element, such as an option button or check box.

Page (integer) --
The page on which a block was detected. Page is returned by asynchronous operations. Page values greater than 1 are only returned for multipage documents that are in PDF format. A scanned image (JPEG/PNG), even if it contains multiple document pages, is considered to be a single-page document. The value of Page is always 1. Synchronous operations don\'t return Page because every input document is considered to be a single-page document.





HumanLoopActivationOutput (dict) --
Shows the results of the human in the loop evaluation.

HumanLoopArn (string) --
The Amazon Resource Name (ARN) of the HumanLoop created.

HumanLoopActivationReasons (list) --
Shows if and why human review was needed.

(string) --


HumanLoopActivationConditionsEvaluationResults (string) --
Shows the result of condition evaluations, including those conditions which activated a human review.



AnalyzeDocumentModelVersion (string) --
The version of the model used to analyze the document.







Exceptions

Textract.Client.exceptions.InvalidParameterException
Textract.Client.exceptions.InvalidS3ObjectException
Textract.Client.exceptions.UnsupportedDocumentException
Textract.Client.exceptions.DocumentTooLargeException
Textract.Client.exceptions.BadDocumentException
Textract.Client.exceptions.AccessDeniedException
Textract.Client.exceptions.ProvisionedThroughputExceededException
Textract.Client.exceptions.InternalServerError
Textract.Client.exceptions.ThrottlingException
Textract.Client.exceptions.HumanLoopQuotaExceededException


    :return: {
        'DocumentMetadata': {
            'Pages': 123
        },
        'Blocks': [
            {
                'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
                'Confidence': ...,
                'Text': 'string',
                'RowIndex': 123,
                'ColumnIndex': 123,
                'RowSpan': 123,
                'ColumnSpan': 123,
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
                },
                'Id': 'string',
                'Relationships': [
                    {
                        'Type': 'VALUE'|'CHILD',
                        'Ids': [
                            'string',
                        ]
                    },
                ],
                'EntityTypes': [
                    'KEY'|'VALUE',
                ],
                'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
                'Page': 123
            },
        ],
        'HumanLoopActivationOutput': {
            'HumanLoopArn': 'string',
            'HumanLoopActivationReasons': [
                'string',
            ],
            'HumanLoopActivationConditionsEvaluationResults': 'string'
        },
        'AnalyzeDocumentModelVersion': 'string'
    }
    
    
    :returns: 
    Document (dict) -- [REQUIRED]
    The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can\'t pass image bytes. The document must be an image in JPEG or PNG format.
    If you\'re using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes that are passed using the Bytes field.
    
    Bytes (bytes) --A blob of base64-encoded document bytes. The maximum size of a document that\'s provided in a blob of bytes is 5 MB. The document bytes must be in PNG or JPEG format.
    If you\'re using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes passed using the Bytes field.
    
    S3Object (dict) --Identifies an S3 object as the document source. The maximum size of a document that\'s stored in an S3 bucket is 5 MB.
    
    Bucket (string) --The name of the S3 bucket.
    
    Name (string) --The file name of the input document. Synchronous operations can use image files that are in JPEG or PNG format. Asynchronous operations also support PDF format files.
    
    Version (string) --If the bucket has versioning enabled, you can specify the object version.
    
    
    
    
    
    FeatureTypes (list) -- [REQUIRED]
    A list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. To perform both types of analysis, add TABLES and FORMS to FeatureTypes . All lines and words detected in the document are included in the response (including text that isn\'t related to the value of FeatureTypes ).
    
    (string) --
    
    
    HumanLoopConfig (dict) -- Sets the configuration for the human in the loop workflow for analyzing documents.
    
    HumanLoopName (string) -- [REQUIRED]The name of the human workflow used for this image. This should be kept unique within a region.
    
    FlowDefinitionArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the flow definition.
    
    DataAttributes (dict) --Sets attributes of the input data.
    
    ContentClassifiers (list) --Sets whether the input image is free of personally identifiable information or adult content.
    
    (string) --
    
    
    
    
    
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def detect_document_text(Document=None):
    """
    Detects text in the input document. Amazon Textract can detect lines of text and the words that make up a line of text. The input document must be an image in JPEG or PNG format. DetectDocumentText returns the detected text in an array of  Block objects.
    Each document page has as an associated Block of type PAGE. Each PAGE Block object is the parent of LINE Block objects that represent the lines of detected text on a page. A LINE Block object is a parent for each word that makes up the line. Words are represented by Block objects of type WORD.
    For more information, see Document Text Detection .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detect_document_text(
        Document={
            'Bytes': b'bytes',
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        }
    )
    
    
    :type Document: dict
    :param Document: [REQUIRED]\nThe input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can\'t pass image bytes. The document must be an image in JPEG or PNG format.\nIf you\'re using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes that are passed using the Bytes field.\n\nBytes (bytes) --A blob of base64-encoded document bytes. The maximum size of a document that\'s provided in a blob of bytes is 5 MB. The document bytes must be in PNG or JPEG format.\nIf you\'re using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes passed using the Bytes field.\n\nS3Object (dict) --Identifies an S3 object as the document source. The maximum size of a document that\'s stored in an S3 bucket is 5 MB.\n\nBucket (string) --The name of the S3 bucket.\n\nName (string) --The file name of the input document. Synchronous operations can use image files that are in JPEG or PNG format. Asynchronous operations also support PDF format files.\n\nVersion (string) --If the bucket has versioning enabled, you can specify the object version.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'DocumentMetadata': {
        'Pages': 123
    },
    'Blocks': [
        {
            'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
            'Confidence': ...,
            'Text': 'string',
            'RowIndex': 123,
            'ColumnIndex': 123,
            'RowSpan': 123,
            'ColumnSpan': 123,
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
            },
            'Id': 'string',
            'Relationships': [
                {
                    'Type': 'VALUE'|'CHILD',
                    'Ids': [
                        'string',
                    ]
                },
            ],
            'EntityTypes': [
                'KEY'|'VALUE',
            ],
            'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
            'Page': 123
        },
    ],
    'DetectDocumentTextModelVersion': 'string'
}


Response Structure

(dict) --
DocumentMetadata (dict) --Metadata about the document. It contains the number of pages that are detected in the document.

Pages (integer) --The number of pages that are detected in the document.



Blocks (list) --An array of Block objects that contain the text that\'s detected in the document.

(dict) --A Block represents items that are recognized in a document within a group of pixels close to each other. The information returned in a Block object depends on the type of operation. In text detection for documents (for example  DetectDocumentText ), you get information about the detected words and lines of text. In text analysis (for example  AnalyzeDocument ), you can also get information about the fields, tables, and selection elements that are detected in the document.
An array of Block objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as  DetectDocumentText , the array of Block objects is the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the array is returned over one or more responses.
For more information, see How Amazon Textract Works .

BlockType (string) --The type of text item that\'s recognized. In operations for text detection, the following types are returned:

PAGE - Contains a list of the LINE Block objects that are detected on a document page.
WORD - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren\'t separated by spaces.
LINE - A string of tab-delimited, contiguous words that are detected on a document page.

In text analysis operations, the following types are returned:

PAGE - Contains a list of child Block objects that are detected on a document page.
KEY_VALUE_SET - Stores the KEY and VALUE Block objects for linked text that\'s detected on a document page. Use the EntityType field to determine if a KEY_VALUE_SET object is a KEY Block object or a VALUE Block object.
WORD - A word that\'s detected on a document page. A word is one or more ISO basic Latin script characters that aren\'t separated by spaces.
LINE - A string of tab-delimited, contiguous words that are detected on a document page.
TABLE - A table that\'s detected on a document page. A table is grid-based information with two or more rows or columns, with a cell span of one row and one column each.
CELL - A cell within a detected table. The cell is the parent of the block that contains the text in the cell.
SELECTION_ELEMENT - A selection element such as an option button (radio button) or a check box that\'s detected on a document page. Use the value of SelectionStatus to determine the status of the selection element.


Confidence (float) --The confidence score that Amazon Textract has in the accuracy of the recognized text and the accuracy of the geometry points around the recognized text.

Text (string) --The word or line of text that\'s recognized by Amazon Textract.

RowIndex (integer) --The row in which a table cell is located. The first row position is 1. RowIndex isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

ColumnIndex (integer) --The column in which a table cell appears. The first column position is 1. ColumnIndex isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

RowSpan (integer) --The number of rows that a table cell spans. Currently this value is always 1, even if the number of rows spanned is greater than 1. RowSpan isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

ColumnSpan (integer) --The number of columns that a table cell spans. Currently this value is always 1, even if the number of columns spanned is greater than 1. ColumnSpan isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

Geometry (dict) --The location of the recognized text on the image. It includes an axis-aligned, coarse bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial information.

BoundingBox (dict) --An axis-aligned coarse representation of the location of the recognized item on the document page.

Width (float) --The width of the bounding box as a ratio of the overall document page width.

Height (float) --The height of the bounding box as a ratio of the overall document page height.

Left (float) --The left coordinate of the bounding box as a ratio of overall document page width.

Top (float) --The top coordinate of the bounding box as a ratio of overall document page height.



Polygon (list) --Within the bounding box, a fine-grained polygon around the recognized item.

(dict) --The X and Y coordinates of a point on a document page. The X and Y values that are returned are ratios of the overall document page size. For example, if the input document is 700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the document page.
An array of Point objects, Polygon , is returned by  DetectDocumentText . Polygon represents a fine-grained polygon around detected text. For more information, see Geometry in the Amazon Textract Developer Guide.

X (float) --The value of the X coordinate for a point on a Polygon .

Y (float) --The value of the Y coordinate for a point on a Polygon .







Id (string) --The identifier for the recognized text. The identifier is only unique for a single operation.

Relationships (list) --A list of child blocks of the current block. For example, a LINE object has child blocks for each WORD block that\'s part of the line of text. There aren\'t Relationship objects in the list for relationships that don\'t exist, such as when the current block has no child blocks. The list size can be the following:

0 - The block has no child blocks.
1 - The block has child blocks.


(dict) --Information about how blocks are related to each other. A Block object contains 0 or more Relation objects in a list, Relationships . For more information, see  Block .
The Type element provides the type of the relationship for all blocks in the IDs array.

Type (string) --The type of relationship that the blocks in the IDs array have with the current block. The relationship can be VALUE or CHILD . A relationship of type VALUE is a list that contains the ID of the VALUE block that\'s associated with the KEY of a key-value pair. A relationship of type CHILD is a list of IDs that identify WORD blocks.

Ids (list) --An array of IDs for related blocks. You can get the type of the relationship from the Type element.

(string) --






EntityTypes (list) --The type of entity. The following can be returned:

KEY - An identifier for a field on the document.
VALUE - The field text.


EntityTypes isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

(string) --


SelectionStatus (string) --The selection status of a selection element, such as an option button or check box.

Page (integer) --The page on which a block was detected. Page is returned by asynchronous operations. Page values greater than 1 are only returned for multipage documents that are in PDF format. A scanned image (JPEG/PNG), even if it contains multiple document pages, is considered to be a single-page document. The value of Page is always 1. Synchronous operations don\'t return Page because every input document is considered to be a single-page document.





DetectDocumentTextModelVersion (string) --





Exceptions

Textract.Client.exceptions.InvalidParameterException
Textract.Client.exceptions.InvalidS3ObjectException
Textract.Client.exceptions.UnsupportedDocumentException
Textract.Client.exceptions.DocumentTooLargeException
Textract.Client.exceptions.BadDocumentException
Textract.Client.exceptions.AccessDeniedException
Textract.Client.exceptions.ProvisionedThroughputExceededException
Textract.Client.exceptions.InternalServerError
Textract.Client.exceptions.ThrottlingException


    :return: {
        'DocumentMetadata': {
            'Pages': 123
        },
        'Blocks': [
            {
                'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
                'Confidence': ...,
                'Text': 'string',
                'RowIndex': 123,
                'ColumnIndex': 123,
                'RowSpan': 123,
                'ColumnSpan': 123,
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
                },
                'Id': 'string',
                'Relationships': [
                    {
                        'Type': 'VALUE'|'CHILD',
                        'Ids': [
                            'string',
                        ]
                    },
                ],
                'EntityTypes': [
                    'KEY'|'VALUE',
                ],
                'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
                'Page': 123
            },
        ],
        'DetectDocumentTextModelVersion': 'string'
    }
    
    
    :returns: 
    PAGE - Contains a list of child Block objects that are detected on a document page.
    KEY_VALUE_SET - Stores the KEY and VALUE Block objects for linked text that\'s detected on a document page. Use the EntityType field to determine if a KEY_VALUE_SET object is a KEY Block object or a VALUE Block object.
    WORD - A word that\'s detected on a document page. A word is one or more ISO basic Latin script characters that aren\'t separated by spaces.
    LINE - A string of tab-delimited, contiguous words that are detected on a document page.
    TABLE - A table that\'s detected on a document page. A table is grid-based information with two or more rows or columns, with a cell span of one row and one column each.
    CELL - A cell within a detected table. The cell is the parent of the block that contains the text in the cell.
    SELECTION_ELEMENT - A selection element such as an option button (radio button) or a check box that\'s detected on a document page. Use the value of SelectionStatus to determine the status of the selection element.
    
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

def get_document_analysis(JobId=None, MaxResults=None, NextToken=None):
    """
    Gets the results for an Amazon Textract asynchronous operation that analyzes text in a document.
    You start asynchronous text analysis by calling  StartDocumentAnalysis , which returns a job identifier (JobId ). When the text analysis operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that\'s registered in the initial call to StartDocumentAnalysis . To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call GetDocumentAnalysis , and pass the job identifier (JobId ) from the initial call to StartDocumentAnalysis .
    Selection elements such as check boxes and option buttons (radio buttons) can be detected in form data and in tables. A SELECTION_ELEMENT Block object contains information about a selection element, including the selection status.
    Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetDocumentAnalysis , and populate the NextToken request parameter with the token value that\'s returned from the previous call to GetDocumentAnalysis .
    For more information, see Document Text Analysis .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_document_analysis(
        JobId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nA unique identifier for the text-detection job. The JobId is returned from StartDocumentAnalysis . A JobId value is only valid for 7 days.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per paginated call. The largest value that you can specify is 1,000. If you specify a value greater than 1,000, a maximum of 1,000 results is returned. The default value is 1,000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.

    :rtype: dict

ReturnsResponse Syntax
{
    'DocumentMetadata': {
        'Pages': 123
    },
    'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'PARTIAL_SUCCESS',
    'NextToken': 'string',
    'Blocks': [
        {
            'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
            'Confidence': ...,
            'Text': 'string',
            'RowIndex': 123,
            'ColumnIndex': 123,
            'RowSpan': 123,
            'ColumnSpan': 123,
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
            },
            'Id': 'string',
            'Relationships': [
                {
                    'Type': 'VALUE'|'CHILD',
                    'Ids': [
                        'string',
                    ]
                },
            ],
            'EntityTypes': [
                'KEY'|'VALUE',
            ],
            'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
            'Page': 123
        },
    ],
    'Warnings': [
        {
            'ErrorCode': 'string',
            'Pages': [
                123,
            ]
        },
    ],
    'StatusMessage': 'string',
    'AnalyzeDocumentModelVersion': 'string'
}


Response Structure

(dict) --

DocumentMetadata (dict) --
Information about a document that Amazon Textract processed. DocumentMetadata is returned in every page of paginated responses from an Amazon Textract video operation.

Pages (integer) --
The number of pages that are detected in the document.



JobStatus (string) --
The current status of the text detection job.

NextToken (string) --
If the response is truncated, Amazon Textract returns this token. You can use this token in the subsequent request to retrieve the next set of text detection results.

Blocks (list) --
The results of the text-analysis operation.

(dict) --
A Block represents items that are recognized in a document within a group of pixels close to each other. The information returned in a Block object depends on the type of operation. In text detection for documents (for example  DetectDocumentText ), you get information about the detected words and lines of text. In text analysis (for example  AnalyzeDocument ), you can also get information about the fields, tables, and selection elements that are detected in the document.
An array of Block objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as  DetectDocumentText , the array of Block objects is the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the array is returned over one or more responses.
For more information, see How Amazon Textract Works .

BlockType (string) --
The type of text item that\'s recognized. In operations for text detection, the following types are returned:

PAGE - Contains a list of the LINE Block objects that are detected on a document page.
WORD - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren\'t separated by spaces.
LINE - A string of tab-delimited, contiguous words that are detected on a document page.

In text analysis operations, the following types are returned:

PAGE - Contains a list of child Block objects that are detected on a document page.
KEY_VALUE_SET - Stores the KEY and VALUE Block objects for linked text that\'s detected on a document page. Use the EntityType field to determine if a KEY_VALUE_SET object is a KEY Block object or a VALUE Block object.
WORD - A word that\'s detected on a document page. A word is one or more ISO basic Latin script characters that aren\'t separated by spaces.
LINE - A string of tab-delimited, contiguous words that are detected on a document page.
TABLE - A table that\'s detected on a document page. A table is grid-based information with two or more rows or columns, with a cell span of one row and one column each.
CELL - A cell within a detected table. The cell is the parent of the block that contains the text in the cell.
SELECTION_ELEMENT - A selection element such as an option button (radio button) or a check box that\'s detected on a document page. Use the value of SelectionStatus to determine the status of the selection element.


Confidence (float) --
The confidence score that Amazon Textract has in the accuracy of the recognized text and the accuracy of the geometry points around the recognized text.

Text (string) --
The word or line of text that\'s recognized by Amazon Textract.

RowIndex (integer) --
The row in which a table cell is located. The first row position is 1. RowIndex isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

ColumnIndex (integer) --
The column in which a table cell appears. The first column position is 1. ColumnIndex isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

RowSpan (integer) --
The number of rows that a table cell spans. Currently this value is always 1, even if the number of rows spanned is greater than 1. RowSpan isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

ColumnSpan (integer) --
The number of columns that a table cell spans. Currently this value is always 1, even if the number of columns spanned is greater than 1. ColumnSpan isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

Geometry (dict) --
The location of the recognized text on the image. It includes an axis-aligned, coarse bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial information.

BoundingBox (dict) --
An axis-aligned coarse representation of the location of the recognized item on the document page.

Width (float) --
The width of the bounding box as a ratio of the overall document page width.

Height (float) --
The height of the bounding box as a ratio of the overall document page height.

Left (float) --
The left coordinate of the bounding box as a ratio of overall document page width.

Top (float) --
The top coordinate of the bounding box as a ratio of overall document page height.



Polygon (list) --
Within the bounding box, a fine-grained polygon around the recognized item.

(dict) --
The X and Y coordinates of a point on a document page. The X and Y values that are returned are ratios of the overall document page size. For example, if the input document is 700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the document page.
An array of Point objects, Polygon , is returned by  DetectDocumentText . Polygon represents a fine-grained polygon around detected text. For more information, see Geometry in the Amazon Textract Developer Guide.

X (float) --
The value of the X coordinate for a point on a Polygon .

Y (float) --
The value of the Y coordinate for a point on a Polygon .







Id (string) --
The identifier for the recognized text. The identifier is only unique for a single operation.

Relationships (list) --
A list of child blocks of the current block. For example, a LINE object has child blocks for each WORD block that\'s part of the line of text. There aren\'t Relationship objects in the list for relationships that don\'t exist, such as when the current block has no child blocks. The list size can be the following:

0 - The block has no child blocks.
1 - The block has child blocks.


(dict) --
Information about how blocks are related to each other. A Block object contains 0 or more Relation objects in a list, Relationships . For more information, see  Block .
The Type element provides the type of the relationship for all blocks in the IDs array.

Type (string) --
The type of relationship that the blocks in the IDs array have with the current block. The relationship can be VALUE or CHILD . A relationship of type VALUE is a list that contains the ID of the VALUE block that\'s associated with the KEY of a key-value pair. A relationship of type CHILD is a list of IDs that identify WORD blocks.

Ids (list) --
An array of IDs for related blocks. You can get the type of the relationship from the Type element.

(string) --






EntityTypes (list) --
The type of entity. The following can be returned:

KEY - An identifier for a field on the document.
VALUE - The field text.


EntityTypes isn\'t returned by DetectDocumentText and GetDocumentTextDetection .


(string) --


SelectionStatus (string) --
The selection status of a selection element, such as an option button or check box.

Page (integer) --
The page on which a block was detected. Page is returned by asynchronous operations. Page values greater than 1 are only returned for multipage documents that are in PDF format. A scanned image (JPEG/PNG), even if it contains multiple document pages, is considered to be a single-page document. The value of Page is always 1. Synchronous operations don\'t return Page because every input document is considered to be a single-page document.





Warnings (list) --
A list of warnings that occurred during the document-analysis operation.

(dict) --
A warning about an issue that occurred during asynchronous text analysis ( StartDocumentAnalysis ) or asynchronous document text detection ( StartDocumentTextDetection ).

ErrorCode (string) --
The error code for the warning.

Pages (list) --
A list of the pages that the warning applies to.

(integer) --






StatusMessage (string) --
The current status of an asynchronous document-analysis operation.

AnalyzeDocumentModelVersion (string) --







Exceptions

Textract.Client.exceptions.InvalidParameterException
Textract.Client.exceptions.AccessDeniedException
Textract.Client.exceptions.ProvisionedThroughputExceededException
Textract.Client.exceptions.InvalidJobIdException
Textract.Client.exceptions.InternalServerError
Textract.Client.exceptions.ThrottlingException


    :return: {
        'DocumentMetadata': {
            'Pages': 123
        },
        'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'PARTIAL_SUCCESS',
        'NextToken': 'string',
        'Blocks': [
            {
                'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
                'Confidence': ...,
                'Text': 'string',
                'RowIndex': 123,
                'ColumnIndex': 123,
                'RowSpan': 123,
                'ColumnSpan': 123,
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
                },
                'Id': 'string',
                'Relationships': [
                    {
                        'Type': 'VALUE'|'CHILD',
                        'Ids': [
                            'string',
                        ]
                    },
                ],
                'EntityTypes': [
                    'KEY'|'VALUE',
                ],
                'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
                'Page': 123
            },
        ],
        'Warnings': [
            {
                'ErrorCode': 'string',
                'Pages': [
                    123,
                ]
            },
        ],
        'StatusMessage': 'string',
        'AnalyzeDocumentModelVersion': 'string'
    }
    
    
    :returns: 
    JobId (string) -- [REQUIRED]
    A unique identifier for the text-detection job. The JobId is returned from StartDocumentAnalysis . A JobId value is only valid for 7 days.
    
    MaxResults (integer) -- The maximum number of results to return per paginated call. The largest value that you can specify is 1,000. If you specify a value greater than 1,000, a maximum of 1,000 results is returned. The default value is 1,000.
    NextToken (string) -- If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.
    
    """
    pass

def get_document_text_detection(JobId=None, MaxResults=None, NextToken=None):
    """
    Gets the results for an Amazon Textract asynchronous operation that detects text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.
    You start asynchronous text detection by calling  StartDocumentTextDetection , which returns a job identifier (JobId ). When the text detection operation finishes, Amazon Textract publishes a completion status to the Amazon Simple Notification Service (Amazon SNS) topic that\'s registered in the initial call to StartDocumentTextDetection . To get the results of the text-detection operation, first check that the status value published to the Amazon SNS topic is SUCCEEDED . If so, call GetDocumentTextDetection , and pass the job identifier (JobId ) from the initial call to StartDocumentTextDetection .
    Each document page has as an associated Block of type PAGE. Each PAGE Block object is the parent of LINE Block objects that represent the lines of detected text on a page. A LINE Block object is a parent for each word that makes up the line. Words are represented by Block objects of type WORD.
    Use the MaxResults parameter to limit the number of blocks that are returned. If there are more results than specified in MaxResults , the value of NextToken in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call GetDocumentTextDetection , and populate the NextToken request parameter with the token value that\'s returned from the previous call to GetDocumentTextDetection .
    For more information, see Document Text Detection .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_document_text_detection(
        JobId='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type JobId: string
    :param JobId: [REQUIRED]\nA unique identifier for the text detection job. The JobId is returned from StartDocumentTextDetection . A JobId value is only valid for 7 days.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per paginated call. The largest value you can specify is 1,000. If you specify a value greater than 1,000, a maximum of 1,000 results is returned. The default value is 1,000.

    :type NextToken: string
    :param NextToken: If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.

    :rtype: dict

ReturnsResponse Syntax
{
    'DocumentMetadata': {
        'Pages': 123
    },
    'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'PARTIAL_SUCCESS',
    'NextToken': 'string',
    'Blocks': [
        {
            'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
            'Confidence': ...,
            'Text': 'string',
            'RowIndex': 123,
            'ColumnIndex': 123,
            'RowSpan': 123,
            'ColumnSpan': 123,
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
            },
            'Id': 'string',
            'Relationships': [
                {
                    'Type': 'VALUE'|'CHILD',
                    'Ids': [
                        'string',
                    ]
                },
            ],
            'EntityTypes': [
                'KEY'|'VALUE',
            ],
            'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
            'Page': 123
        },
    ],
    'Warnings': [
        {
            'ErrorCode': 'string',
            'Pages': [
                123,
            ]
        },
    ],
    'StatusMessage': 'string',
    'DetectDocumentTextModelVersion': 'string'
}


Response Structure

(dict) --

DocumentMetadata (dict) --
Information about a document that Amazon Textract processed. DocumentMetadata is returned in every page of paginated responses from an Amazon Textract video operation.

Pages (integer) --
The number of pages that are detected in the document.



JobStatus (string) --
The current status of the text detection job.

NextToken (string) --
If the response is truncated, Amazon Textract returns this token. You can use this token in the subsequent request to retrieve the next set of text-detection results.

Blocks (list) --
The results of the text-detection operation.

(dict) --
A Block represents items that are recognized in a document within a group of pixels close to each other. The information returned in a Block object depends on the type of operation. In text detection for documents (for example  DetectDocumentText ), you get information about the detected words and lines of text. In text analysis (for example  AnalyzeDocument ), you can also get information about the fields, tables, and selection elements that are detected in the document.
An array of Block objects is returned by both synchronous and asynchronous operations. In synchronous operations, such as  DetectDocumentText , the array of Block objects is the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the array is returned over one or more responses.
For more information, see How Amazon Textract Works .

BlockType (string) --
The type of text item that\'s recognized. In operations for text detection, the following types are returned:

PAGE - Contains a list of the LINE Block objects that are detected on a document page.
WORD - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren\'t separated by spaces.
LINE - A string of tab-delimited, contiguous words that are detected on a document page.

In text analysis operations, the following types are returned:

PAGE - Contains a list of child Block objects that are detected on a document page.
KEY_VALUE_SET - Stores the KEY and VALUE Block objects for linked text that\'s detected on a document page. Use the EntityType field to determine if a KEY_VALUE_SET object is a KEY Block object or a VALUE Block object.
WORD - A word that\'s detected on a document page. A word is one or more ISO basic Latin script characters that aren\'t separated by spaces.
LINE - A string of tab-delimited, contiguous words that are detected on a document page.
TABLE - A table that\'s detected on a document page. A table is grid-based information with two or more rows or columns, with a cell span of one row and one column each.
CELL - A cell within a detected table. The cell is the parent of the block that contains the text in the cell.
SELECTION_ELEMENT - A selection element such as an option button (radio button) or a check box that\'s detected on a document page. Use the value of SelectionStatus to determine the status of the selection element.


Confidence (float) --
The confidence score that Amazon Textract has in the accuracy of the recognized text and the accuracy of the geometry points around the recognized text.

Text (string) --
The word or line of text that\'s recognized by Amazon Textract.

RowIndex (integer) --
The row in which a table cell is located. The first row position is 1. RowIndex isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

ColumnIndex (integer) --
The column in which a table cell appears. The first column position is 1. ColumnIndex isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

RowSpan (integer) --
The number of rows that a table cell spans. Currently this value is always 1, even if the number of rows spanned is greater than 1. RowSpan isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

ColumnSpan (integer) --
The number of columns that a table cell spans. Currently this value is always 1, even if the number of columns spanned is greater than 1. ColumnSpan isn\'t returned by DetectDocumentText and GetDocumentTextDetection .

Geometry (dict) --
The location of the recognized text on the image. It includes an axis-aligned, coarse bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial information.

BoundingBox (dict) --
An axis-aligned coarse representation of the location of the recognized item on the document page.

Width (float) --
The width of the bounding box as a ratio of the overall document page width.

Height (float) --
The height of the bounding box as a ratio of the overall document page height.

Left (float) --
The left coordinate of the bounding box as a ratio of overall document page width.

Top (float) --
The top coordinate of the bounding box as a ratio of overall document page height.



Polygon (list) --
Within the bounding box, a fine-grained polygon around the recognized item.

(dict) --
The X and Y coordinates of a point on a document page. The X and Y values that are returned are ratios of the overall document page size. For example, if the input document is 700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the document page.
An array of Point objects, Polygon , is returned by  DetectDocumentText . Polygon represents a fine-grained polygon around detected text. For more information, see Geometry in the Amazon Textract Developer Guide.

X (float) --
The value of the X coordinate for a point on a Polygon .

Y (float) --
The value of the Y coordinate for a point on a Polygon .







Id (string) --
The identifier for the recognized text. The identifier is only unique for a single operation.

Relationships (list) --
A list of child blocks of the current block. For example, a LINE object has child blocks for each WORD block that\'s part of the line of text. There aren\'t Relationship objects in the list for relationships that don\'t exist, such as when the current block has no child blocks. The list size can be the following:

0 - The block has no child blocks.
1 - The block has child blocks.


(dict) --
Information about how blocks are related to each other. A Block object contains 0 or more Relation objects in a list, Relationships . For more information, see  Block .
The Type element provides the type of the relationship for all blocks in the IDs array.

Type (string) --
The type of relationship that the blocks in the IDs array have with the current block. The relationship can be VALUE or CHILD . A relationship of type VALUE is a list that contains the ID of the VALUE block that\'s associated with the KEY of a key-value pair. A relationship of type CHILD is a list of IDs that identify WORD blocks.

Ids (list) --
An array of IDs for related blocks. You can get the type of the relationship from the Type element.

(string) --






EntityTypes (list) --
The type of entity. The following can be returned:

KEY - An identifier for a field on the document.
VALUE - The field text.


EntityTypes isn\'t returned by DetectDocumentText and GetDocumentTextDetection .


(string) --


SelectionStatus (string) --
The selection status of a selection element, such as an option button or check box.

Page (integer) --
The page on which a block was detected. Page is returned by asynchronous operations. Page values greater than 1 are only returned for multipage documents that are in PDF format. A scanned image (JPEG/PNG), even if it contains multiple document pages, is considered to be a single-page document. The value of Page is always 1. Synchronous operations don\'t return Page because every input document is considered to be a single-page document.





Warnings (list) --
A list of warnings that occurred during the text-detection operation for the document.

(dict) --
A warning about an issue that occurred during asynchronous text analysis ( StartDocumentAnalysis ) or asynchronous document text detection ( StartDocumentTextDetection ).

ErrorCode (string) --
The error code for the warning.

Pages (list) --
A list of the pages that the warning applies to.

(integer) --






StatusMessage (string) --
The current status of an asynchronous text-detection operation for the document.

DetectDocumentTextModelVersion (string) --







Exceptions

Textract.Client.exceptions.InvalidParameterException
Textract.Client.exceptions.AccessDeniedException
Textract.Client.exceptions.ProvisionedThroughputExceededException
Textract.Client.exceptions.InvalidJobIdException
Textract.Client.exceptions.InternalServerError
Textract.Client.exceptions.ThrottlingException


    :return: {
        'DocumentMetadata': {
            'Pages': 123
        },
        'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'PARTIAL_SUCCESS',
        'NextToken': 'string',
        'Blocks': [
            {
                'BlockType': 'KEY_VALUE_SET'|'PAGE'|'LINE'|'WORD'|'TABLE'|'CELL'|'SELECTION_ELEMENT',
                'Confidence': ...,
                'Text': 'string',
                'RowIndex': 123,
                'ColumnIndex': 123,
                'RowSpan': 123,
                'ColumnSpan': 123,
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
                },
                'Id': 'string',
                'Relationships': [
                    {
                        'Type': 'VALUE'|'CHILD',
                        'Ids': [
                            'string',
                        ]
                    },
                ],
                'EntityTypes': [
                    'KEY'|'VALUE',
                ],
                'SelectionStatus': 'SELECTED'|'NOT_SELECTED',
                'Page': 123
            },
        ],
        'Warnings': [
            {
                'ErrorCode': 'string',
                'Pages': [
                    123,
                ]
            },
        ],
        'StatusMessage': 'string',
        'DetectDocumentTextModelVersion': 'string'
    }
    
    
    :returns: 
    PAGE - Contains a list of the LINE Block objects that are detected on a document page.
    WORD - A word detected on a document page. A word is one or more ISO basic Latin script characters that aren\'t separated by spaces.
    LINE - A string of tab-delimited, contiguous words that are detected on a document page.
    
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

def start_document_analysis(DocumentLocation=None, FeatureTypes=None, ClientRequestToken=None, JobTag=None, NotificationChannel=None):
    """
    Starts the asynchronous analysis of an input document for relationships between detected items such as key-value pairs, tables, and selection elements.
    For more information, see Document Text Analysis .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_document_analysis(
        DocumentLocation={
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        FeatureTypes=[
            'TABLES'|'FORMS',
        ],
        ClientRequestToken='string',
        JobTag='string',
        NotificationChannel={
            'SNSTopicArn': 'string',
            'RoleArn': 'string'
        }
    )
    
    
    :type DocumentLocation: dict
    :param DocumentLocation: [REQUIRED]\nThe location of the document to be processed.\n\nS3Object (dict) --The Amazon S3 bucket that contains the input document.\n\nBucket (string) --The name of the S3 bucket.\n\nName (string) --The file name of the input document. Synchronous operations can use image files that are in JPEG or PNG format. Asynchronous operations also support PDF format files.\n\nVersion (string) --If the bucket has versioning enabled, you can specify the object version.\n\n\n\n\n

    :type FeatureTypes: list
    :param FeatureTypes: [REQUIRED]\nA list of the types of analysis to perform. Add TABLES to the list to return information about the tables that are detected in the input document. Add FORMS to return detected form data. To perform both types of analysis, add TABLES and FORMS to FeatureTypes . All lines and words detected in the document are included in the response (including text that isn\'t related to the value of FeatureTypes ).\n\n(string) --\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: The idempotent token that you use to identify the start request. If you use the same token with multiple StartDocumentAnalysis requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidentally started more than once. For more information, see Calling Amazon Textract Asynchronous Operations .

    :type JobTag: string
    :param JobTag: An identifier that you specify that\'s included in the completion notification published to the Amazon SNS topic. For example, you can use JobTag to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to.\n\nSNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic that Amazon Textract posts the completion status to.\n\nRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an IAM role that gives Amazon Textract publishing permissions to the Amazon SNS topic.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier for the document text detection job. Use JobId to identify the job in a subsequent call to GetDocumentAnalysis . A JobId value is only valid for 7 days.







Exceptions

Textract.Client.exceptions.InvalidParameterException
Textract.Client.exceptions.InvalidS3ObjectException
Textract.Client.exceptions.UnsupportedDocumentException
Textract.Client.exceptions.DocumentTooLargeException
Textract.Client.exceptions.BadDocumentException
Textract.Client.exceptions.AccessDeniedException
Textract.Client.exceptions.ProvisionedThroughputExceededException
Textract.Client.exceptions.InternalServerError
Textract.Client.exceptions.IdempotentParameterMismatchException
Textract.Client.exceptions.ThrottlingException
Textract.Client.exceptions.LimitExceededException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Textract.Client.exceptions.InvalidParameterException
    Textract.Client.exceptions.InvalidS3ObjectException
    Textract.Client.exceptions.UnsupportedDocumentException
    Textract.Client.exceptions.DocumentTooLargeException
    Textract.Client.exceptions.BadDocumentException
    Textract.Client.exceptions.AccessDeniedException
    Textract.Client.exceptions.ProvisionedThroughputExceededException
    Textract.Client.exceptions.InternalServerError
    Textract.Client.exceptions.IdempotentParameterMismatchException
    Textract.Client.exceptions.ThrottlingException
    Textract.Client.exceptions.LimitExceededException
    
    """
    pass

def start_document_text_detection(DocumentLocation=None, ClientRequestToken=None, JobTag=None, NotificationChannel=None):
    """
    Starts the asynchronous detection of text in a document. Amazon Textract can detect lines of text and the words that make up a line of text.
    For more information, see Document Text Detection .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_document_text_detection(
        DocumentLocation={
            'S3Object': {
                'Bucket': 'string',
                'Name': 'string',
                'Version': 'string'
            }
        },
        ClientRequestToken='string',
        JobTag='string',
        NotificationChannel={
            'SNSTopicArn': 'string',
            'RoleArn': 'string'
        }
    )
    
    
    :type DocumentLocation: dict
    :param DocumentLocation: [REQUIRED]\nThe location of the document to be processed.\n\nS3Object (dict) --The Amazon S3 bucket that contains the input document.\n\nBucket (string) --The name of the S3 bucket.\n\nName (string) --The file name of the input document. Synchronous operations can use image files that are in JPEG or PNG format. Asynchronous operations also support PDF format files.\n\nVersion (string) --If the bucket has versioning enabled, you can specify the object version.\n\n\n\n\n

    :type ClientRequestToken: string
    :param ClientRequestToken: The idempotent token that\'s used to identify the start request. If you use the same token with multiple StartDocumentTextDetection requests, the same JobId is returned. Use ClientRequestToken to prevent the same job from being accidentally started more than once. For more information, see Calling Amazon Textract Asynchronous Operations .

    :type JobTag: string
    :param JobTag: An identifier that you specify that\'s included in the completion notification published to the Amazon SNS topic. For example, you can use JobTag to identify the type of document that the completion notification corresponds to (such as a tax form or a receipt).

    :type NotificationChannel: dict
    :param NotificationChannel: The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the operation to.\n\nSNSTopicArn (string) -- [REQUIRED]The Amazon SNS topic that Amazon Textract posts the completion status to.\n\nRoleArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of an IAM role that gives Amazon Textract publishing permissions to the Amazon SNS topic.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'JobId': 'string'
}


Response Structure

(dict) --

JobId (string) --
The identifier of the text detection job for the document. Use JobId to identify the job in a subsequent call to GetDocumentTextDetection . A JobId value is only valid for 7 days.







Exceptions

Textract.Client.exceptions.InvalidParameterException
Textract.Client.exceptions.InvalidS3ObjectException
Textract.Client.exceptions.UnsupportedDocumentException
Textract.Client.exceptions.DocumentTooLargeException
Textract.Client.exceptions.BadDocumentException
Textract.Client.exceptions.AccessDeniedException
Textract.Client.exceptions.ProvisionedThroughputExceededException
Textract.Client.exceptions.InternalServerError
Textract.Client.exceptions.IdempotentParameterMismatchException
Textract.Client.exceptions.ThrottlingException
Textract.Client.exceptions.LimitExceededException


    :return: {
        'JobId': 'string'
    }
    
    
    :returns: 
    Textract.Client.exceptions.InvalidParameterException
    Textract.Client.exceptions.InvalidS3ObjectException
    Textract.Client.exceptions.UnsupportedDocumentException
    Textract.Client.exceptions.DocumentTooLargeException
    Textract.Client.exceptions.BadDocumentException
    Textract.Client.exceptions.AccessDeniedException
    Textract.Client.exceptions.ProvisionedThroughputExceededException
    Textract.Client.exceptions.InternalServerError
    Textract.Client.exceptions.IdempotentParameterMismatchException
    Textract.Client.exceptions.ThrottlingException
    Textract.Client.exceptions.LimitExceededException
    
    """
    pass

