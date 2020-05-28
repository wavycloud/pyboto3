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

def batch_create_variable(variableEntries=None):
    """
    Creates a batch of variables.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_create_variable(
        variableEntries=[
            {
                'name': 'string',
                'dataType': 'string',
                'dataSource': 'string',
                'defaultValue': 'string',
                'description': 'string',
                'variableType': 'string'
            },
        ]
    )
    
    
    :type variableEntries: list
    :param variableEntries: [REQUIRED]\nThe list of variables for the batch create variable request.\n\n(dict) --The variable entry in a list.\n\nname (string) --The name of the variable entry.\n\ndataType (string) --The data type of the variable entry.\n\ndataSource (string) --The data source of the variable entry.\n\ndefaultValue (string) --The default value of the variable entry.\n\ndescription (string) --The description of the variable entry.\n\nvariableType (string) --The type of the variable entry.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'errors': [
        {
            'name': 'string',
            'code': 123,
            'message': 'string'
        },
    ]
}


Response Structure

(dict) --
errors (list) --Provides the errors for the BatchCreateVariable request.

(dict) --Provides the error of the batch create variable API.

name (string) --The name.

code (integer) --The error code.

message (string) --The error message.










Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'errors': [
            {
                'name': 'string',
                'code': 123,
                'message': 'string'
            },
        ]
    }
    
    
    """
    pass

def batch_get_variable(names=None):
    """
    Gets a batch of variables.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_variable(
        names=[
            'string',
        ]
    )
    
    
    :type names: list
    :param names: [REQUIRED]\nThe list of variable names to get.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'variables': [
        {
            'name': 'string',
            'dataType': 'STRING'|'INTEGER'|'FLOAT'|'BOOLEAN',
            'dataSource': 'EVENT'|'MODEL_SCORE'|'EXTERNAL_MODEL_SCORE',
            'defaultValue': 'string',
            'description': 'string',
            'variableType': 'string',
            'lastUpdatedTime': 'string',
            'createdTime': 'string'
        },
    ],
    'errors': [
        {
            'name': 'string',
            'code': 123,
            'message': 'string'
        },
    ]
}


Response Structure

(dict) --
variables (list) --The returned variables.

(dict) --The variable.

name (string) --The name of the variable.

dataType (string) --The data type of the variable.

dataSource (string) --The data source of the variable.

defaultValue (string) --The default value of the variable.

description (string) --The description of the variable.

variableType (string) --The variable type of the variable.

lastUpdatedTime (string) --The time when variable was last updated.

createdTime (string) --The time when the variable was created.





errors (list) --The errors from the request.

(dict) --Provides the error of the batch get variable API.

name (string) --The error name.

code (integer) --The error code.

message (string) --The error message.










Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'variables': [
            {
                'name': 'string',
                'dataType': 'STRING'|'INTEGER'|'FLOAT'|'BOOLEAN',
                'dataSource': 'EVENT'|'MODEL_SCORE'|'EXTERNAL_MODEL_SCORE',
                'defaultValue': 'string',
                'description': 'string',
                'variableType': 'string',
                'lastUpdatedTime': 'string',
                'createdTime': 'string'
            },
        ],
        'errors': [
            {
                'name': 'string',
                'code': 123,
                'message': 'string'
            },
        ]
    }
    
    
    :returns: 
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_detector_version(detectorId=None, description=None, externalModelEndpoints=None, rules=None, modelVersions=None, ruleExecutionMode=None):
    """
    Creates a detector version. The detector version starts in a DRAFT status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_detector_version(
        detectorId='string',
        description='string',
        externalModelEndpoints=[
            'string',
        ],
        rules=[
            {
                'detectorId': 'string',
                'ruleId': 'string',
                'ruleVersion': 'string'
            },
        ],
        modelVersions=[
            {
                'modelId': 'string',
                'modelType': 'ONLINE_FRAUD_INSIGHTS',
                'modelVersionNumber': 'string'
            },
        ],
        ruleExecutionMode='ALL_MATCHED'|'FIRST_MATCHED'
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe ID of the detector under which you want to create a new version.\n

    :type description: string
    :param description: The description of the detector version.

    :type externalModelEndpoints: list
    :param externalModelEndpoints: The Amazon Sagemaker model endpoints to include in the detector version.\n\n(string) --\n\n

    :type rules: list
    :param rules: [REQUIRED]\nThe rules to include in the detector version.\n\n(dict) --A rule.\n\ndetectorId (string) -- [REQUIRED]The detector for which the rule is associated.\n\nruleId (string) -- [REQUIRED]The rule ID.\n\nruleVersion (string) -- [REQUIRED]The rule version.\n\n\n\n\n

    :type modelVersions: list
    :param modelVersions: The model versions to include in the detector version.\n\n(dict) --The model version.\n\nmodelId (string) -- [REQUIRED]The parent model ID.\n\nmodelType (string) -- [REQUIRED]The model type.\n\nmodelVersionNumber (string) -- [REQUIRED]The model version.\n\n\n\n\n

    :type ruleExecutionMode: string
    :param ruleExecutionMode: The rule execution mode for the rules included in the detector version.\nYou can define and edit the rule mode at the detector version level, when it is in draft status.\nIf you specify FIRST_MATCHED , Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.\nIf you specifiy ALL_MATCHED , Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules.\nThe default behavior is FIRST_MATCHED .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'detectorId': 'string',
    'detectorVersionId': 'string',
    'status': 'DRAFT'|'ACTIVE'|'INACTIVE'
}


Response Structure

(dict) --

detectorId (string) --
The ID for the created version\'s parent detector.

detectorVersionId (string) --
The ID for the created detector.

status (string) --
The status of the detector version.







Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'detectorId': 'string',
        'detectorVersionId': 'string',
        'status': 'DRAFT'|'ACTIVE'|'INACTIVE'
    }
    
    
    :returns: 
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.ResourceNotFoundException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
    """
    pass

def create_model_version(modelId=None, modelType=None, description=None):
    """
    Creates a version of the model using the specified model type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_model_version(
        modelId='string',
        modelType='ONLINE_FRAUD_INSIGHTS',
        description='string'
    )
    
    
    :type modelId: string
    :param modelId: [REQUIRED]\nThe model ID.\n

    :type modelType: string
    :param modelType: [REQUIRED]\nThe model type.\n

    :type description: string
    :param description: The model version description.

    :rtype: dict

ReturnsResponse Syntax
{
    'modelId': 'string',
    'modelType': 'ONLINE_FRAUD_INSIGHTS',
    'modelVersionNumber': 'string',
    'status': 'string'
}


Response Structure

(dict) --

modelId (string) --
The model ID.

modelType (string) --
The model type.

modelVersionNumber (string) --
The version of the model.

status (string) --
The model version status.







Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'modelId': 'string',
        'modelType': 'ONLINE_FRAUD_INSIGHTS',
        'modelVersionNumber': 'string',
        'status': 'string'
    }
    
    
    :returns: 
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.ResourceNotFoundException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
    """
    pass

def create_rule(ruleId=None, detectorId=None, description=None, expression=None, language=None, outcomes=None):
    """
    Creates a rule for use with the specified detector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_rule(
        ruleId='string',
        detectorId='string',
        description='string',
        expression='string',
        language='DETECTORPL',
        outcomes=[
            'string',
        ]
    )
    
    
    :type ruleId: string
    :param ruleId: [REQUIRED]\nThe rule ID.\n

    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe detector ID for the rule\'s parent detector.\n

    :type description: string
    :param description: The rule description.

    :type expression: string
    :param expression: [REQUIRED]\nThe rule expression.\n

    :type language: string
    :param language: [REQUIRED]\nThe language of the rule.\n

    :type outcomes: list
    :param outcomes: [REQUIRED]\nThe outcome or outcomes returned when the rule expression matches.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'rule': {
        'detectorId': 'string',
        'ruleId': 'string',
        'ruleVersion': 'string'
    }
}


Response Structure

(dict) --

rule (dict) --
The created rule.

detectorId (string) --
The detector for which the rule is associated.

ruleId (string) --
The rule ID.

ruleVersion (string) --
The rule version.









Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'rule': {
            'detectorId': 'string',
            'ruleId': 'string',
            'ruleVersion': 'string'
        }
    }
    
    
    :returns: 
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
    """
    pass

def create_variable(name=None, dataType=None, dataSource=None, defaultValue=None, description=None, variableType=None):
    """
    Creates a variable.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_variable(
        name='string',
        dataType='STRING'|'INTEGER'|'FLOAT'|'BOOLEAN',
        dataSource='EVENT'|'MODEL_SCORE'|'EXTERNAL_MODEL_SCORE',
        defaultValue='string',
        description='string',
        variableType='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the variable.\n

    :type dataType: string
    :param dataType: [REQUIRED]\nThe data type.\n

    :type dataSource: string
    :param dataSource: [REQUIRED]\nThe source of the data.\n

    :type defaultValue: string
    :param defaultValue: [REQUIRED]\nThe default value for the variable when no value is received.\n

    :type description: string
    :param description: The description.

    :type variableType: string
    :param variableType: The variable type.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_detector(detectorId=None):
    """
    Deletes the detector. Before deleting a detector, you must first delete all detector versions and rule versions associated with the detector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_detector(
        detectorId='string'
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe ID of the detector to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

FraudDetector.Client.exceptions.ConflictException
FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    FraudDetector.Client.exceptions.ConflictException
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
    """
    pass

def delete_detector_version(detectorId=None, detectorVersionId=None):
    """
    Deletes the detector version. You cannot delete detector versions that are in ACTIVE status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_detector_version(
        detectorId='string',
        detectorVersionId='string'
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe ID of the parent detector for the detector version to delete.\n

    :type detectorVersionId: string
    :param detectorVersionId: [REQUIRED]\nThe ID of the detector version to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException
FraudDetector.Client.exceptions.ConflictException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_event(eventId=None):
    """
    Deletes the specified event.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_event(
        eventId='string'
    )
    
    
    :type eventId: string
    :param eventId: [REQUIRED]\nThe ID of the event to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
    """
    pass

def delete_rule_version(detectorId=None, ruleId=None, ruleVersion=None):
    """
    Deletes the rule version. You cannot delete a rule version if it is used by an ACTIVE or INACTIVE detector version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_rule_version(
        detectorId='string',
        ruleId='string',
        ruleVersion='string'
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe ID of the detector that includes the rule version to delete.\n

    :type ruleId: string
    :param ruleId: [REQUIRED]\nThe rule ID of the rule version to delete.\n

    :type ruleVersion: string
    :param ruleVersion: [REQUIRED]\nThe rule version to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ConflictException
FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_detector(detectorId=None, nextToken=None, maxResults=None):
    """
    Gets all versions for a specified detector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_detector(
        detectorId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe detector ID.\n

    :type nextToken: string
    :param nextToken: The next token from the previous response.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return for the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'detectorId': 'string',
    'detectorVersionSummaries': [
        {
            'detectorVersionId': 'string',
            'status': 'DRAFT'|'ACTIVE'|'INACTIVE',
            'description': 'string',
            'lastUpdatedTime': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

detectorId (string) --
The detector ID.

detectorVersionSummaries (list) --
The status and description for each detector version.

(dict) --
The summary of the detector version.

detectorVersionId (string) --
The detector version ID.

status (string) --
The detector version status.

description (string) --
The detector version description.

lastUpdatedTime (string) --
Timestamp of when the detector version was last updated.





nextToken (string) --
The next token to be used for subsequent requests.







Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'detectorId': 'string',
        'detectorVersionSummaries': [
            {
                'detectorVersionId': 'string',
                'status': 'DRAFT'|'ACTIVE'|'INACTIVE',
                'description': 'string',
                'lastUpdatedTime': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.ResourceNotFoundException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
    """
    pass

def describe_model_versions(modelId=None, modelVersionNumber=None, modelType=None, nextToken=None, maxResults=None):
    """
    Gets all of the model versions for the specified model type or for the specified model type and model ID. You can also get details for a single, specified model version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_model_versions(
        modelId='string',
        modelVersionNumber='string',
        modelType='ONLINE_FRAUD_INSIGHTS',
        nextToken='string',
        maxResults=123
    )
    
    
    :type modelId: string
    :param modelId: The model ID.

    :type modelVersionNumber: string
    :param modelVersionNumber: The model version.

    :type modelType: string
    :param modelType: The model type.

    :type nextToken: string
    :param nextToken: The next token from the previous results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'modelVersionDetails': [
        {
            'modelId': 'string',
            'modelType': 'ONLINE_FRAUD_INSIGHTS',
            'modelVersionNumber': 'string',
            'description': 'string',
            'status': 'string',
            'trainingDataSource': {
                'dataLocation': 'string',
                'dataAccessRoleArn': 'string'
            },
            'modelVariables': [
                {
                    'name': 'string',
                    'index': 123
                },
            ],
            'labelSchema': {
                'labelKey': 'string',
                'labelMapper': {
                    'string': [
                        'string',
                    ]
                }
            },
            'validationMetrics': {
                'string': 'string'
            },
            'trainingMetrics': {
                'string': 'string'
            },
            'lastUpdatedTime': 'string',
            'createdTime': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

modelVersionDetails (list) --
The model version details.

(dict) --
Provides the model version details.

modelId (string) --
The model ID.

modelType (string) --
The model type.

modelVersionNumber (string) --
The model version.

description (string) --
The model description.

status (string) --
The model status.

trainingDataSource (dict) --
The model training data source.

dataLocation (string) --
The data location of the training data source.

dataAccessRoleArn (string) --
The data access role ARN for the training data source.



modelVariables (list) --
The model variables.

(dict) --
The model variable.>

name (string) --
The model variable\'s name.>

index (integer) --
The model variable\'s index.>





labelSchema (dict) --
The model label schema.

labelKey (string) --
The label key.

labelMapper (dict) --
The label mapper maps the Amazon Fraud Detector supported label to the appropriate source labels. For example, if "FRAUD" and "LEGIT" are Amazon Fraud Detector supported labels, this mapper could be: {"FRAUD" => ["0"] , "LEGIT" => ["1"]} or {"FRAUD" => ["false"], "LEGIT" => ["true"]} or {"FRAUD" => ["fraud", "abuse"], "LEGIT" => ["legit", "safe"]} . The value part of the mapper is a list, because you may have multiple variants for a single Amazon Fraud Detector label.

(string) --
(list) --
(string) --








validationMetrics (dict) --
The model validation metrics.

(string) --
(string) --




trainingMetrics (dict) --
The model training metrics.

(string) --
(string) --




lastUpdatedTime (string) --
The timestamp when the model was last updated.

createdTime (string) --
The timestamp when the model was created.





nextToken (string) --
The next token.







Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'modelVersionDetails': [
            {
                'modelId': 'string',
                'modelType': 'ONLINE_FRAUD_INSIGHTS',
                'modelVersionNumber': 'string',
                'description': 'string',
                'status': 'string',
                'trainingDataSource': {
                    'dataLocation': 'string',
                    'dataAccessRoleArn': 'string'
                },
                'modelVariables': [
                    {
                        'name': 'string',
                        'index': 123
                    },
                ],
                'labelSchema': {
                    'labelKey': 'string',
                    'labelMapper': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'validationMetrics': {
                    'string': 'string'
                },
                'trainingMetrics': {
                    'string': 'string'
                },
                'lastUpdatedTime': 'string',
                'createdTime': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (list) --
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

def get_detector_version(detectorId=None, detectorVersionId=None):
    """
    Gets a particular detector version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_detector_version(
        detectorId='string',
        detectorVersionId='string'
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe detector ID.\n

    :type detectorVersionId: string
    :param detectorVersionId: [REQUIRED]\nThe detector version ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'detectorId': 'string',
    'detectorVersionId': 'string',
    'description': 'string',
    'externalModelEndpoints': [
        'string',
    ],
    'modelVersions': [
        {
            'modelId': 'string',
            'modelType': 'ONLINE_FRAUD_INSIGHTS',
            'modelVersionNumber': 'string'
        },
    ],
    'rules': [
        {
            'detectorId': 'string',
            'ruleId': 'string',
            'ruleVersion': 'string'
        },
    ],
    'status': 'DRAFT'|'ACTIVE'|'INACTIVE',
    'lastUpdatedTime': 'string',
    'createdTime': 'string',
    'ruleExecutionMode': 'ALL_MATCHED'|'FIRST_MATCHED'
}


Response Structure

(dict) --

detectorId (string) --
The detector ID.

detectorVersionId (string) --
The detector version ID.

description (string) --
The detector version description.

externalModelEndpoints (list) --
The Amazon SageMaker model endpoints included in the detector version.

(string) --


modelVersions (list) --
The model versions included in the detector version.

(dict) --
The model version.

modelId (string) --
The parent model ID.

modelType (string) --
The model type.

modelVersionNumber (string) --
The model version.





rules (list) --
The rules included in the detector version.

(dict) --
A rule.

detectorId (string) --
The detector for which the rule is associated.

ruleId (string) --
The rule ID.

ruleVersion (string) --
The rule version.





status (string) --
The status of the detector version.

lastUpdatedTime (string) --
The timestamp when the detector version was last updated.

createdTime (string) --
The timestamp when the detector version was created.

ruleExecutionMode (string) --
The execution mode of the rule in the dectector

FIRST_MATCHED indicates that Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.
ALL_MATCHED indicates that Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules. You can define and edit the rule mode at the detector version level, when it is in draft status.








Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'detectorId': 'string',
        'detectorVersionId': 'string',
        'description': 'string',
        'externalModelEndpoints': [
            'string',
        ],
        'modelVersions': [
            {
                'modelId': 'string',
                'modelType': 'ONLINE_FRAUD_INSIGHTS',
                'modelVersionNumber': 'string'
            },
        ],
        'rules': [
            {
                'detectorId': 'string',
                'ruleId': 'string',
                'ruleVersion': 'string'
            },
        ],
        'status': 'DRAFT'|'ACTIVE'|'INACTIVE',
        'lastUpdatedTime': 'string',
        'createdTime': 'string',
        'ruleExecutionMode': 'ALL_MATCHED'|'FIRST_MATCHED'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_detectors(detectorId=None, nextToken=None, maxResults=None):
    """
    Gets all of detectors. This is a paginated API. If you provide a null maxSizePerPage , this actions retrieves a maximum of 10 records per page. If you provide a maxSizePerPage , the value must be between 5 and 10. To get the next page results, provide the pagination token from the GetEventTypesResponse as part of your request. A null pagination token fetches the records from the beginning.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_detectors(
        detectorId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type detectorId: string
    :param detectorId: The detector ID.

    :type nextToken: string
    :param nextToken: The next token for the subsequent request.

    :type maxResults: integer
    :param maxResults: The maximum number of objects to return for the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'detectors': [
        {
            'detectorId': 'string',
            'description': 'string',
            'lastUpdatedTime': 'string',
            'createdTime': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

detectors (list) --
The detectors.

(dict) --
The detector.

detectorId (string) --
The detector ID.

description (string) --
The detector description.

lastUpdatedTime (string) --
Timestamp of when the detector was last updated.

createdTime (string) --
Timestamp of when the detector was created.





nextToken (string) --
The next page token.







Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'detectors': [
            {
                'detectorId': 'string',
                'description': 'string',
                'lastUpdatedTime': 'string',
                'createdTime': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.ResourceNotFoundException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
    """
    pass

def get_external_models(modelEndpoint=None, nextToken=None, maxResults=None):
    """
    Gets the details for one or more Amazon SageMaker models that have been imported into the service. This is a paginated API. If you provide a null maxSizePerPage , this actions retrieves a maximum of 10 records per page. If you provide a maxSizePerPage , the value must be between 5 and 10. To get the next page results, provide the pagination token from the GetExternalModelsResult as part of your request. A null pagination token fetches the records from the beginning.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_external_models(
        modelEndpoint='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type modelEndpoint: string
    :param modelEndpoint: The Amazon SageMaker model endpoint.

    :type nextToken: string
    :param nextToken: The next page token for the request.

    :type maxResults: integer
    :param maxResults: The maximum number of objects to return for the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'externalModels': [
        {
            'modelEndpoint': 'string',
            'modelSource': 'SAGEMAKER',
            'role': {
                'arn': 'string',
                'name': 'string'
            },
            'inputConfiguration': {
                'format': 'TEXT_CSV'|'APPLICATION_JSON',
                'isOpaque': True|False,
                'jsonInputTemplate': 'string',
                'csvInputTemplate': 'string'
            },
            'outputConfiguration': {
                'format': 'TEXT_CSV'|'APPLICATION_JSONLINES',
                'jsonKeyToVariableMap': {
                    'string': 'string'
                },
                'csvIndexToVariableMap': {
                    'string': 'string'
                }
            },
            'modelEndpointStatus': 'ASSOCIATED'|'DISSOCIATED',
            'lastUpdatedTime': 'string',
            'createdTime': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

externalModels (list) --
Gets the Amazon SageMaker models.

(dict) --
The Amazon SageMaker model.

modelEndpoint (string) --
The Amazon SageMaker model endpoints.

modelSource (string) --
The source of the model.

role (dict) --
The role used to invoke the model.

arn (string) --
The role ARN.

name (string) --
The role name.



inputConfiguration (dict) --
The input configuration.

format (string) --
The format of the model input configuration. The format differs depending on if it is passed through to SageMaker or constructed by Amazon Fraud Detector.

isOpaque (boolean) --
For an opaque-model, the input to the model will be a ByteBuffer blob provided in the getPrediction request, and will be passed to SageMaker as-is. For non-opaque models, the input will be constructed by Amazon Fraud Detector based on the model-configuration.

jsonInputTemplate (string) --
Template for constructing the JSON input-data sent to SageMaker. At event-evaluation, the placeholders for variable names in the template will be replaced with the variable values before being sent to SageMaker.

csvInputTemplate (string) --
Template for constructing the CSV input-data sent to SageMaker. At event-evaluation, the placeholders for variable-names in the template will be replaced with the variable values before being sent to SageMaker.



outputConfiguration (dict) --
The output configuration.

format (string) --
The format of the model output configuration.

jsonKeyToVariableMap (dict) --
A map of JSON keys in response from SageMaker to the Amazon Fraud Detector variables.

(string) --
(string) --




csvIndexToVariableMap (dict) --
A map of CSV index values in the SageMaker response to the Amazon Fraud Detector variables.

(string) --
(string) --






modelEndpointStatus (string) --
The Amazon Fraud Detector status for the external model endpoint

lastUpdatedTime (string) --
Timestamp of when the model was last updated.

createdTime (string) --
Timestamp of when the model was last created.





nextToken (string) --
The next page token to be used in subsequent requests.







Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'externalModels': [
            {
                'modelEndpoint': 'string',
                'modelSource': 'SAGEMAKER',
                'role': {
                    'arn': 'string',
                    'name': 'string'
                },
                'inputConfiguration': {
                    'format': 'TEXT_CSV'|'APPLICATION_JSON',
                    'isOpaque': True|False,
                    'jsonInputTemplate': 'string',
                    'csvInputTemplate': 'string'
                },
                'outputConfiguration': {
                    'format': 'TEXT_CSV'|'APPLICATION_JSONLINES',
                    'jsonKeyToVariableMap': {
                        'string': 'string'
                    },
                    'csvIndexToVariableMap': {
                        'string': 'string'
                    }
                },
                'modelEndpointStatus': 'ASSOCIATED'|'DISSOCIATED',
                'lastUpdatedTime': 'string',
                'createdTime': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_model_version(modelId=None, modelType=None, modelVersionNumber=None):
    """
    Gets a model version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_model_version(
        modelId='string',
        modelType='ONLINE_FRAUD_INSIGHTS',
        modelVersionNumber='string'
    )
    
    
    :type modelId: string
    :param modelId: [REQUIRED]\nThe model ID.\n

    :type modelType: string
    :param modelType: [REQUIRED]\nThe model type.\n

    :type modelVersionNumber: string
    :param modelVersionNumber: [REQUIRED]\nThe model version.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'modelId': 'string',
    'modelType': 'ONLINE_FRAUD_INSIGHTS',
    'modelVersionNumber': 'string',
    'description': 'string',
    'status': 'string'
}


Response Structure

(dict) --

modelId (string) --
The model ID.

modelType (string) --
The model type.

modelVersionNumber (string) --
The model version.

description (string) --
The model version description.

status (string) --
The model version status.







Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'modelId': 'string',
        'modelType': 'ONLINE_FRAUD_INSIGHTS',
        'modelVersionNumber': 'string',
        'description': 'string',
        'status': 'string'
    }
    
    
    :returns: 
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.ResourceNotFoundException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
    """
    pass

def get_models(modelType=None, modelId=None, nextToken=None, maxResults=None):
    """
    Gets all of the models for the AWS account, or the specified model type, or gets a single model for the specified model type, model ID combination.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_models(
        modelType='ONLINE_FRAUD_INSIGHTS',
        modelId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type modelType: string
    :param modelType: The model type.

    :type modelId: string
    :param modelId: The model ID.

    :type nextToken: string
    :param nextToken: The next token for the request.

    :type maxResults: integer
    :param maxResults: The maximum results to return for the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'models': [
        {
            'modelId': 'string',
            'modelType': 'ONLINE_FRAUD_INSIGHTS',
            'description': 'string',
            'trainingDataSource': {
                'dataLocation': 'string',
                'dataAccessRoleArn': 'string'
            },
            'modelVariables': [
                {
                    'name': 'string',
                    'index': 123
                },
            ],
            'labelSchema': {
                'labelKey': 'string',
                'labelMapper': {
                    'string': [
                        'string',
                    ]
                }
            },
            'lastUpdatedTime': 'string',
            'createdTime': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The next token for subsequent requests.

models (list) --
The returned models.

(dict) --
The model.

modelId (string) --
The model ID.

modelType (string) --
The model type.

description (string) --
The model description.

trainingDataSource (dict) --
The model training data source in Amazon S3.

dataLocation (string) --
The data location of the training data source.

dataAccessRoleArn (string) --
The data access role ARN for the training data source.



modelVariables (list) --
The model input variables.

(dict) --
The model variable.>

name (string) --
The model variable\'s name.>

index (integer) --
The model variable\'s index.>





labelSchema (dict) --
The model label schema.

labelKey (string) --
The label key.

labelMapper (dict) --
The label mapper maps the Amazon Fraud Detector supported label to the appropriate source labels. For example, if "FRAUD" and "LEGIT" are Amazon Fraud Detector supported labels, this mapper could be: {"FRAUD" => ["0"] , "LEGIT" => ["1"]} or {"FRAUD" => ["false"], "LEGIT" => ["true"]} or {"FRAUD" => ["fraud", "abuse"], "LEGIT" => ["legit", "safe"]} . The value part of the mapper is a list, because you may have multiple variants for a single Amazon Fraud Detector label.

(string) --
(list) --
(string) --








lastUpdatedTime (string) --
Timestamp of last time the model was updated.

createdTime (string) --
Timestamp of when the model was created.











Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'nextToken': 'string',
        'models': [
            {
                'modelId': 'string',
                'modelType': 'ONLINE_FRAUD_INSIGHTS',
                'description': 'string',
                'trainingDataSource': {
                    'dataLocation': 'string',
                    'dataAccessRoleArn': 'string'
                },
                'modelVariables': [
                    {
                        'name': 'string',
                        'index': 123
                    },
                ],
                'labelSchema': {
                    'labelKey': 'string',
                    'labelMapper': {
                        'string': [
                            'string',
                        ]
                    }
                },
                'lastUpdatedTime': 'string',
                'createdTime': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    (list) --
    (string) --
    
    
    
    
    
    """
    pass

def get_outcomes(name=None, nextToken=None, maxResults=None):
    """
    Gets one or more outcomes. This is a paginated API. If you provide a null maxSizePerPage , this actions retrieves a maximum of 10 records per page. If you provide a maxSizePerPage , the value must be between 50 and 100. To get the next page results, provide the pagination token from the GetOutcomesResult as part of your request. A null pagination token fetches the records from the beginning.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_outcomes(
        name='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: The name of the outcome or outcomes to get.

    :type nextToken: string
    :param nextToken: The next page token for the request.

    :type maxResults: integer
    :param maxResults: The maximum number of objects to return for the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'outcomes': [
        {
            'name': 'string',
            'description': 'string',
            'lastUpdatedTime': 'string',
            'createdTime': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

outcomes (list) --
The outcomes.

(dict) --
The outcome.

name (string) --
The outcome name.

description (string) --
The outcome description.

lastUpdatedTime (string) --
The timestamp when the outcome was last updated.

createdTime (string) --
The timestamp when the outcome was created.





nextToken (string) --
The next page token for subsequent requests.







Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'outcomes': [
            {
                'name': 'string',
                'description': 'string',
                'lastUpdatedTime': 'string',
                'createdTime': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.ResourceNotFoundException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
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

def get_prediction(detectorId=None, detectorVersionId=None, eventId=None, eventAttributes=None, externalModelEndpointDataBlobs=None):
    """
    Evaluates an event against a detector version. If a version ID is not provided, the detector\xe2\x80\x99s (ACTIVE ) version is used.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_prediction(
        detectorId='string',
        detectorVersionId='string',
        eventId='string',
        eventAttributes={
            'string': 'string'
        },
        externalModelEndpointDataBlobs={
            'string': {
                'byteBuffer': b'bytes',
                'contentType': 'string'
            }
        }
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe detector ID.\n

    :type detectorVersionId: string
    :param detectorVersionId: The detector version ID.

    :type eventId: string
    :param eventId: [REQUIRED]\nThe unique ID used to identify the event.\n

    :type eventAttributes: dict
    :param eventAttributes: Names of variables you defined in Amazon Fraud Detector to represent event data elements and their corresponding values for the event you are sending for evaluation.\n\n(string) --\n(string) --\n\n\n\n

    :type externalModelEndpointDataBlobs: dict
    :param externalModelEndpointDataBlobs: The Amazon SageMaker model endpoint input data blobs.\n\n(string) --\n(dict) --A pre-formed Amazon SageMaker model input you can include if your detector version includes an imported Amazon SageMaker model endpoint with pass-through input configuration.\n\nbyteBuffer (bytes) --The byte buffer of the Amazon SageMaker model endpoint input data blob.\n\ncontentType (string) --The content type of the Amazon SageMaker model endpoint input data blob.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'outcomes': [
        'string',
    ],
    'modelScores': [
        {
            'modelVersion': {
                'modelId': 'string',
                'modelType': 'ONLINE_FRAUD_INSIGHTS',
                'modelVersionNumber': 'string'
            },
            'scores': {
                'string': ...
            }
        },
    ],
    'ruleResults': [
        {
            'ruleId': 'string',
            'outcomes': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --

outcomes (list) --
The prediction outcomes.

(string) --


modelScores (list) --
The model scores for models used in the detector version.

(dict) --
The fraud prediction scores.

modelVersion (dict) --
The model version.

modelId (string) --
The parent model ID.

modelType (string) --
The model type.

modelVersionNumber (string) --
The model version.



scores (dict) --
The model\'s fraud prediction scores.

(string) --
(float) --








ruleResults (list) --
The rule results in the prediction.

(dict) --
The rule results.

ruleId (string) --
The rule ID that was matched, based on the rule execution mode.

outcomes (list) --
The outcomes of the matched rule, based on the rule execution mode.

(string) --












Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'outcomes': [
            'string',
        ],
        'modelScores': [
            {
                'modelVersion': {
                    'modelId': 'string',
                    'modelType': 'ONLINE_FRAUD_INSIGHTS',
                    'modelVersionNumber': 'string'
                },
                'scores': {
                    'string': ...
                }
            },
        ],
        'ruleResults': [
            {
                'ruleId': 'string',
                'outcomes': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_rules(ruleId=None, detectorId=None, ruleVersion=None, nextToken=None, maxResults=None):
    """
    Gets all rules available for the specified detector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_rules(
        ruleId='string',
        detectorId='string',
        ruleVersion='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type ruleId: string
    :param ruleId: The rule ID.

    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe detector ID.\n

    :type ruleVersion: string
    :param ruleVersion: The rule version.

    :type nextToken: string
    :param nextToken: The next page token.

    :type maxResults: integer
    :param maxResults: The maximum number of rules to return for the request.

    :rtype: dict

ReturnsResponse Syntax
{
    'ruleDetails': [
        {
            'ruleId': 'string',
            'description': 'string',
            'detectorId': 'string',
            'ruleVersion': 'string',
            'expression': 'string',
            'language': 'DETECTORPL',
            'outcomes': [
                'string',
            ],
            'lastUpdatedTime': 'string',
            'createdTime': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

ruleDetails (list) --
The details of the requested rule.

(dict) --
The details of the rule.

ruleId (string) --
The rule ID.

description (string) --
The rule description.

detectorId (string) --
The detector for which the rule is associated.

ruleVersion (string) --
The rule version.

expression (string) --
The rule expression.

language (string) --
The rule language.

outcomes (list) --
The rule outcomes.

(string) --


lastUpdatedTime (string) --
Timestamp of the last time the rule was updated.

createdTime (string) --
The timestamp of when the rule was created.





nextToken (string) --
The next page token to be used in subsequent requests.







Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'ruleDetails': [
            {
                'ruleId': 'string',
                'description': 'string',
                'detectorId': 'string',
                'ruleVersion': 'string',
                'expression': 'string',
                'language': 'DETECTORPL',
                'outcomes': [
                    'string',
                ],
                'lastUpdatedTime': 'string',
                'createdTime': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_variables(name=None, nextToken=None, maxResults=None):
    """
    Gets all of the variables or the specific variable. This is a paginated API. Providing null maxSizePerPage results in retrieving maximum of 100 records per page. If you provide maxSizePerPage the value must be between 50 and 100. To get the next page result, a provide a pagination token from GetVariablesResult as part of your request. Null pagination token fetches the records from the beginning.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_variables(
        name='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type name: string
    :param name: The name of the variable.

    :type nextToken: string
    :param nextToken: The next page token of the get variable request.

    :type maxResults: integer
    :param maxResults: The max size per page determined for the get variable request.

    :rtype: dict

ReturnsResponse Syntax
{
    'variables': [
        {
            'name': 'string',
            'dataType': 'STRING'|'INTEGER'|'FLOAT'|'BOOLEAN',
            'dataSource': 'EVENT'|'MODEL_SCORE'|'EXTERNAL_MODEL_SCORE',
            'defaultValue': 'string',
            'description': 'string',
            'variableType': 'string',
            'lastUpdatedTime': 'string',
            'createdTime': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

variables (list) --
The names of the variables returned.

(dict) --
The variable.

name (string) --
The name of the variable.

dataType (string) --
The data type of the variable.

dataSource (string) --
The data source of the variable.

defaultValue (string) --
The default value of the variable.

description (string) --
The description of the variable.

variableType (string) --
The variable type of the variable.

lastUpdatedTime (string) --
The time when variable was last updated.

createdTime (string) --
The time when the variable was created.





nextToken (string) --
The next page token to be used in subsequent requests.







Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'variables': [
            {
                'name': 'string',
                'dataType': 'STRING'|'INTEGER'|'FLOAT'|'BOOLEAN',
                'dataSource': 'EVENT'|'MODEL_SCORE'|'EXTERNAL_MODEL_SCORE',
                'defaultValue': 'string',
                'description': 'string',
                'variableType': 'string',
                'lastUpdatedTime': 'string',
                'createdTime': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.ResourceNotFoundException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
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

def put_detector(detectorId=None, description=None):
    """
    Creates or updates a detector.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_detector(
        detectorId='string',
        description='string'
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe detector ID.\n

    :type description: string
    :param description: The description of the detector.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_external_model(modelEndpoint=None, modelSource=None, role=None, inputConfiguration=None, outputConfiguration=None, modelEndpointStatus=None):
    """
    Creates or updates an Amazon SageMaker model endpoint. You can also use this action to update the configuration of the model endpoint, including the IAM role and/or the mapped variables.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_external_model(
        modelEndpoint='string',
        modelSource='SAGEMAKER',
        role={
            'arn': 'string',
            'name': 'string'
        },
        inputConfiguration={
            'format': 'TEXT_CSV'|'APPLICATION_JSON',
            'isOpaque': True|False,
            'jsonInputTemplate': 'string',
            'csvInputTemplate': 'string'
        },
        outputConfiguration={
            'format': 'TEXT_CSV'|'APPLICATION_JSONLINES',
            'jsonKeyToVariableMap': {
                'string': 'string'
            },
            'csvIndexToVariableMap': {
                'string': 'string'
            }
        },
        modelEndpointStatus='ASSOCIATED'|'DISSOCIATED'
    )
    
    
    :type modelEndpoint: string
    :param modelEndpoint: [REQUIRED]\nThe model endpoints name.\n

    :type modelSource: string
    :param modelSource: [REQUIRED]\nThe source of the model.\n

    :type role: dict
    :param role: [REQUIRED]\nThe IAM role used to invoke the model endpoint.\n\narn (string) -- [REQUIRED]The role ARN.\n\nname (string) -- [REQUIRED]The role name.\n\n\n

    :type inputConfiguration: dict
    :param inputConfiguration: [REQUIRED]\nThe model endpoint input configuration.\n\nformat (string) --The format of the model input configuration. The format differs depending on if it is passed through to SageMaker or constructed by Amazon Fraud Detector.\n\nisOpaque (boolean) -- [REQUIRED]For an opaque-model, the input to the model will be a ByteBuffer blob provided in the getPrediction request, and will be passed to SageMaker as-is. For non-opaque models, the input will be constructed by Amazon Fraud Detector based on the model-configuration.\n\njsonInputTemplate (string) --Template for constructing the JSON input-data sent to SageMaker. At event-evaluation, the placeholders for variable names in the template will be replaced with the variable values before being sent to SageMaker.\n\ncsvInputTemplate (string) --Template for constructing the CSV input-data sent to SageMaker. At event-evaluation, the placeholders for variable-names in the template will be replaced with the variable values before being sent to SageMaker.\n\n\n

    :type outputConfiguration: dict
    :param outputConfiguration: [REQUIRED]\nThe model endpoint output configuration.\n\nformat (string) -- [REQUIRED]The format of the model output configuration.\n\njsonKeyToVariableMap (dict) --A map of JSON keys in response from SageMaker to the Amazon Fraud Detector variables.\n\n(string) --\n(string) --\n\n\n\n\ncsvIndexToVariableMap (dict) --A map of CSV index values in the SageMaker response to the Amazon Fraud Detector variables.\n\n(string) --\n(string) --\n\n\n\n\n\n

    :type modelEndpointStatus: string
    :param modelEndpointStatus: [REQUIRED]\nThe model endpoint\xe2\x80\x99s status in Amazon Fraud Detector.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_model(modelId=None, modelType=None, description=None, trainingDataSource=None, modelVariables=None, labelSchema=None):
    """
    Creates or updates a model.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_model(
        modelId='string',
        modelType='ONLINE_FRAUD_INSIGHTS',
        description='string',
        trainingDataSource={
            'dataLocation': 'string',
            'dataAccessRoleArn': 'string'
        },
        modelVariables=[
            {
                'name': 'string',
                'index': 123
            },
        ],
        labelSchema={
            'labelKey': 'string',
            'labelMapper': {
                'string': [
                    'string',
                ]
            }
        }
    )
    
    
    :type modelId: string
    :param modelId: [REQUIRED]\nThe model ID.\n

    :type modelType: string
    :param modelType: [REQUIRED]\nThe model type.\n

    :type description: string
    :param description: The model description.

    :type trainingDataSource: dict
    :param trainingDataSource: [REQUIRED]\nThe training data source location in Amazon S3.\n\ndataLocation (string) -- [REQUIRED]The data location of the training data source.\n\ndataAccessRoleArn (string) -- [REQUIRED]The data access role ARN for the training data source.\n\n\n

    :type modelVariables: list
    :param modelVariables: [REQUIRED]\nThe model input variables.\n\n(dict) --The model variable.>\n\nname (string) -- [REQUIRED]The model variable\'s name.>\n\nindex (integer) --The model variable\'s index.>\n\n\n\n\n

    :type labelSchema: dict
    :param labelSchema: [REQUIRED]\nThe label schema.\n\nlabelKey (string) -- [REQUIRED]The label key.\n\nlabelMapper (dict) -- [REQUIRED]The label mapper maps the Amazon Fraud Detector supported label to the appropriate source labels. For example, if 'FRAUD' and 'LEGIT' are Amazon Fraud Detector supported labels, this mapper could be: {'FRAUD' => ['0'] , 'LEGIT' => ['1']} or {'FRAUD' => ['false'], 'LEGIT' => ['true']} or {'FRAUD' => ['fraud', 'abuse'], 'LEGIT' => ['legit', 'safe']} . The value part of the mapper is a list, because you may have multiple variants for a single Amazon Fraud Detector label.\n\n(string) --\n(list) --\n(string) --\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def put_outcome(name=None, description=None):
    """
    Creates or updates an outcome.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_outcome(
        name='string',
        description='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the outcome.\n

    :type description: string
    :param description: The outcome description.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_detector_version(detectorId=None, detectorVersionId=None, externalModelEndpoints=None, rules=None, description=None, modelVersions=None, ruleExecutionMode=None):
    """
    Updates a detector version. The detector version attributes that you can update include models, external model endpoints, rules, and description. You can only update a DRAFT detector version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_detector_version(
        detectorId='string',
        detectorVersionId='string',
        externalModelEndpoints=[
            'string',
        ],
        rules=[
            {
                'detectorId': 'string',
                'ruleId': 'string',
                'ruleVersion': 'string'
            },
        ],
        description='string',
        modelVersions=[
            {
                'modelId': 'string',
                'modelType': 'ONLINE_FRAUD_INSIGHTS',
                'modelVersionNumber': 'string'
            },
        ],
        ruleExecutionMode='ALL_MATCHED'|'FIRST_MATCHED'
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe parent detector ID for the detector version you want to update.\n

    :type detectorVersionId: string
    :param detectorVersionId: [REQUIRED]\nThe detector version ID.\n

    :type externalModelEndpoints: list
    :param externalModelEndpoints: [REQUIRED]\nThe Amazon SageMaker model endpoints to include in the detector version.\n\n(string) --\n\n

    :type rules: list
    :param rules: [REQUIRED]\nThe rules to include in the detector version.\n\n(dict) --A rule.\n\ndetectorId (string) -- [REQUIRED]The detector for which the rule is associated.\n\nruleId (string) -- [REQUIRED]The rule ID.\n\nruleVersion (string) -- [REQUIRED]The rule version.\n\n\n\n\n

    :type description: string
    :param description: The detector version description.

    :type modelVersions: list
    :param modelVersions: The model versions to include in the detector version.\n\n(dict) --The model version.\n\nmodelId (string) -- [REQUIRED]The parent model ID.\n\nmodelType (string) -- [REQUIRED]The model type.\n\nmodelVersionNumber (string) -- [REQUIRED]The model version.\n\n\n\n\n

    :type ruleExecutionMode: string
    :param ruleExecutionMode: The rule execution mode to add to the detector.\nIf you specify FIRST_MATCHED , Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.\nIf you specifiy ALL_MATCHED , Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules. You can define and edit the rule mode at the detector version level, when it is in draft status.\nThe default behavior is FIRST_MATCHED .\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_detector_version_metadata(detectorId=None, detectorVersionId=None, description=None):
    """
    Updates the detector version\'s description. You can update the metadata for any detector version (DRAFT, ACTIVE, or INACTIVE ).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_detector_version_metadata(
        detectorId='string',
        detectorVersionId='string',
        description='string'
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe detector ID.\n

    :type detectorVersionId: string
    :param detectorVersionId: [REQUIRED]\nThe detector version ID.\n

    :type description: string
    :param description: [REQUIRED]\nThe description.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_detector_version_status(detectorId=None, detectorVersionId=None, status=None):
    """
    Updates the detector version\xe2\x80\x99s status. You can perform the following promotions or demotions using UpdateDetectorVersionStatus : DRAFT to ACTIVE , ACTIVE to INACTIVE , and INACTIVE to ACTIVE .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_detector_version_status(
        detectorId='string',
        detectorVersionId='string',
        status='DRAFT'|'ACTIVE'|'INACTIVE'
    )
    
    
    :type detectorId: string
    :param detectorId: [REQUIRED]\nThe detector ID.\n

    :type detectorVersionId: string
    :param detectorVersionId: [REQUIRED]\nThe detector version ID.\n

    :type status: string
    :param status: [REQUIRED]\nThe new status.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_model_version(modelId=None, modelType=None, modelVersionNumber=None, description=None, status=None):
    """
    Updates a model version. You can update the description and status attributes using this action. You can perform the following status updates:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_model_version(
        modelId='string',
        modelType='ONLINE_FRAUD_INSIGHTS',
        modelVersionNumber='string',
        description='string',
        status='TRAINING_IN_PROGRESS'|'TRAINING_COMPLETE'|'ACTIVATE_REQUESTED'|'ACTIVATE_IN_PROGRESS'|'ACTIVE'|'INACTIVATE_IN_PROGRESS'|'INACTIVE'|'ERROR'
    )
    
    
    :type modelId: string
    :param modelId: [REQUIRED]\nThe model ID.\n

    :type modelType: string
    :param modelType: [REQUIRED]\nThe model type.\n

    :type modelVersionNumber: string
    :param modelVersionNumber: [REQUIRED]\nThe model version.\n

    :type description: string
    :param description: [REQUIRED]\nThe model description.\n

    :type status: string
    :param status: [REQUIRED]\nThe new model status.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    modelId (string) -- [REQUIRED]
    The model ID.
    
    modelType (string) -- [REQUIRED]
    The model type.
    
    modelVersionNumber (string) -- [REQUIRED]
    The model version.
    
    description (string) -- [REQUIRED]
    The model description.
    
    status (string) -- [REQUIRED]
    The new model status.
    
    
    """
    pass

def update_rule_metadata(rule=None, description=None):
    """
    Updates a rule\'s metadata.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_rule_metadata(
        rule={
            'detectorId': 'string',
            'ruleId': 'string',
            'ruleVersion': 'string'
        },
        description='string'
    )
    
    
    :type rule: dict
    :param rule: [REQUIRED]\nThe rule to update.\n\ndetectorId (string) -- [REQUIRED]The detector for which the rule is associated.\n\nruleId (string) -- [REQUIRED]The rule ID.\n\nruleVersion (string) -- [REQUIRED]The rule version.\n\n\n

    :type description: string
    :param description: [REQUIRED]\nThe rule description.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_rule_version(rule=None, description=None, expression=None, language=None, outcomes=None):
    """
    Updates a rule version resulting in a new rule version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_rule_version(
        rule={
            'detectorId': 'string',
            'ruleId': 'string',
            'ruleVersion': 'string'
        },
        description='string',
        expression='string',
        language='DETECTORPL',
        outcomes=[
            'string',
        ]
    )
    
    
    :type rule: dict
    :param rule: [REQUIRED]\nThe rule to update.\n\ndetectorId (string) -- [REQUIRED]The detector for which the rule is associated.\n\nruleId (string) -- [REQUIRED]The rule ID.\n\nruleVersion (string) -- [REQUIRED]The rule version.\n\n\n

    :type description: string
    :param description: The description.

    :type expression: string
    :param expression: [REQUIRED]\nThe rule expression.\n

    :type language: string
    :param language: [REQUIRED]\nThe language.\n

    :type outcomes: list
    :param outcomes: [REQUIRED]\nThe outcomes.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'rule': {
        'detectorId': 'string',
        'ruleId': 'string',
        'ruleVersion': 'string'
    }
}


Response Structure

(dict) --

rule (dict) --
The new rule version that was created.

detectorId (string) --
The detector for which the rule is associated.

ruleId (string) --
The rule ID.

ruleVersion (string) --
The rule version.









Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {
        'rule': {
            'detectorId': 'string',
            'ruleId': 'string',
            'ruleVersion': 'string'
        }
    }
    
    
    :returns: 
    FraudDetector.Client.exceptions.ValidationException
    FraudDetector.Client.exceptions.ResourceNotFoundException
    FraudDetector.Client.exceptions.InternalServerException
    FraudDetector.Client.exceptions.ThrottlingException
    
    """
    pass

def update_variable(name=None, defaultValue=None, description=None, variableType=None):
    """
    Updates a variable.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_variable(
        name='string',
        defaultValue='string',
        description='string',
        variableType='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the variable.\n

    :type defaultValue: string
    :param defaultValue: The new default value of the variable.

    :type description: string
    :param description: The new description.

    :type variableType: string
    :param variableType: The variable type.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

FraudDetector.Client.exceptions.ValidationException
FraudDetector.Client.exceptions.ResourceNotFoundException
FraudDetector.Client.exceptions.InternalServerException
FraudDetector.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

