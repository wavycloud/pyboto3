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

def create_batch_inference_job(jobName=None, solutionVersionArn=None, numResults=None, jobInput=None, jobOutput=None, roleArn=None):
    """
    Creates a batch inference job. The operation can handle up to 50 million records and the input file must be in JSON format. For more information, see  recommendations-batch .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_batch_inference_job(
        jobName='string',
        solutionVersionArn='string',
        numResults=123,
        jobInput={
            's3DataSource': {
                'path': 'string',
                'kmsKeyArn': 'string'
            }
        },
        jobOutput={
            's3DataDestination': {
                'path': 'string',
                'kmsKeyArn': 'string'
            }
        },
        roleArn='string'
    )
    
    
    :type jobName: string
    :param jobName: [REQUIRED]\nThe name of the batch inference job to create.\n

    :type solutionVersionArn: string
    :param solutionVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the solution version that will be used to generate the batch inference recommendations.\n

    :type numResults: integer
    :param numResults: The number of recommendations to retreive.

    :type jobInput: dict
    :param jobInput: [REQUIRED]\nThe Amazon S3 path that leads to the input file to base your recommendations on. The input material must be in JSON format.\n\ns3DataSource (dict) -- [REQUIRED]The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket must be in the same region as the API endpoint you are calling.\n\npath (string) -- [REQUIRED]The file path of the Amazon S3 bucket.\n\nkmsKeyArn (string) --The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that Amazon Personalize uses to encrypt or decrypt the input and output files of a batch inference job.\n\n\n\n\n

    :type jobOutput: dict
    :param jobOutput: [REQUIRED]\nThe path to the Amazon S3 bucket where the job\'s output will be stored.\n\ns3DataDestination (dict) -- [REQUIRED]Information on the Amazon S3 bucket in which the batch inference job\'s output is stored.\n\npath (string) -- [REQUIRED]The file path of the Amazon S3 bucket.\n\nkmsKeyArn (string) --The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that Amazon Personalize uses to encrypt or decrypt the input and output files of a batch inference job.\n\n\n\n\n

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe ARN of the Amazon Identity and Access Management role that has permissions to read and write to your input and out Amazon S3 buckets respectively.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'batchInferenceJobArn': 'string'
}


Response Structure

(dict) --

batchInferenceJobArn (string) --
The ARN of the batch inference job.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceAlreadyExistsException
Personalize.Client.exceptions.LimitExceededException
Personalize.Client.exceptions.ResourceNotFoundException
Personalize.Client.exceptions.ResourceInUseException


    :return: {
        'batchInferenceJobArn': 'string'
    }
    
    
    :returns: 
    Personalize.Client.exceptions.InvalidInputException
    Personalize.Client.exceptions.ResourceAlreadyExistsException
    Personalize.Client.exceptions.LimitExceededException
    Personalize.Client.exceptions.ResourceNotFoundException
    Personalize.Client.exceptions.ResourceInUseException
    
    """
    pass

def create_campaign(name=None, solutionVersionArn=None, minProvisionedTPS=None):
    """
    Creates a campaign by deploying a solution version. When a client calls the GetRecommendations and GetPersonalizedRanking APIs, a campaign is specified in the request.
    A transaction is a single GetRecommendations or GetPersonalizedRanking call. Transactions per second (TPS) is the throughput and unit of billing for Amazon Personalize. The minimum provisioned TPS (minProvisionedTPS ) specifies the baseline throughput provisioned by Amazon Personalize, and thus, the minimum billing charge. If your TPS increases beyond minProvisionedTPS , Amazon Personalize auto-scales the provisioned capacity up and down, but never below minProvisionedTPS , to maintain a 70% utilization. There\'s a short time delay while the capacity is increased that might cause loss of transactions. It\'s recommended to start with a low minProvisionedTPS , track your usage using Amazon CloudWatch metrics, and then increase the minProvisionedTPS as necessary.
    A campaign can be in one of the following states:
    To get the campaign status, call  DescribeCampaign .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_campaign(
        name='string',
        solutionVersionArn='string',
        minProvisionedTPS=123
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nA name for the new campaign. The campaign name must be unique within your account.\n

    :type solutionVersionArn: string
    :param solutionVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the solution version to deploy.\n

    :type minProvisionedTPS: integer
    :param minProvisionedTPS: [REQUIRED]\nSpecifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'campaignArn': 'string'
}


Response Structure

(dict) --

campaignArn (string) --
The Amazon Resource Name (ARN) of the campaign.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException
Personalize.Client.exceptions.ResourceAlreadyExistsException
Personalize.Client.exceptions.LimitExceededException
Personalize.Client.exceptions.ResourceInUseException


    :return: {
        'campaignArn': 'string'
    }
    
    
    :returns: 
    ListCampaigns
    DescribeCampaign
    UpdateCampaign
    DeleteCampaign
    
    """
    pass

def create_dataset(name=None, schemaArn=None, datasetGroupArn=None, datasetType=None):
    """
    Creates an empty dataset and adds it to the specified dataset group. Use  CreateDatasetImportJob to import your training data to a dataset.
    There are three types of datasets:
    Each dataset type has an associated schema with required field types. Only the Interactions dataset is required in order to train a model (also referred to as creating a solution).
    A dataset can be in one of the following states:
    To get the status of the dataset, call  DescribeDataset .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_dataset(
        name='string',
        schemaArn='string',
        datasetGroupArn='string',
        datasetType='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name for the dataset.\n

    :type schemaArn: string
    :param schemaArn: [REQUIRED]\nThe ARN of the schema to associate with the dataset. The schema defines the dataset fields.\n

    :type datasetGroupArn: string
    :param datasetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the dataset group to add the dataset to.\n

    :type datasetType: string
    :param datasetType: [REQUIRED]\nThe type of dataset.\nOne of the following (case insensitive) values:\n\nInteractions\nItems\nUsers\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'datasetArn': 'string'
}


Response Structure

(dict) --

datasetArn (string) --
The ARN of the dataset.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException
Personalize.Client.exceptions.ResourceAlreadyExistsException
Personalize.Client.exceptions.LimitExceededException
Personalize.Client.exceptions.ResourceInUseException


    :return: {
        'datasetArn': 'string'
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    DELETE PENDING > DELETE IN_PROGRESS
    
    """
    pass

def create_dataset_group(name=None, roleArn=None, kmsKeyArn=None):
    """
    Creates an empty dataset group. A dataset group contains related datasets that supply data for training a model. A dataset group can contain at most three datasets, one for each type of dataset:
    To train a model (create a solution), a dataset group that contains an Interactions dataset is required. Call  CreateDataset to add a dataset to the group.
    A dataset group can be in one of the following states:
    To get the status of the dataset group, call  DescribeDatasetGroup . If the status shows as CREATE FAILED, the response includes a failureReason key, which describes why the creation failed.
    You can specify an AWS Key Management Service (KMS) key to encrypt the datasets in the group. If you specify a KMS key, you must also include an AWS Identity and Access Management (IAM) role that has permission to access the key.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_dataset_group(
        name='string',
        roleArn='string',
        kmsKeyArn='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name for the new dataset group.\n

    :type roleArn: string
    :param roleArn: The ARN of the IAM role that has permissions to access the KMS key. Supplying an IAM role is only valid when also specifying a KMS key.

    :type kmsKeyArn: string
    :param kmsKeyArn: The Amazon Resource Name (ARN) of a KMS key used to encrypt the datasets.

    :rtype: dict

ReturnsResponse Syntax
{
    'datasetGroupArn': 'string'
}


Response Structure

(dict) --

datasetGroupArn (string) --
The Amazon Resource Name (ARN) of the new dataset group.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceAlreadyExistsException
Personalize.Client.exceptions.LimitExceededException


    :return: {
        'datasetGroupArn': 'string'
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    DELETE PENDING
    
    """
    pass

def create_dataset_import_job(jobName=None, datasetArn=None, dataSource=None, roleArn=None):
    """
    Creates a job that imports training data from your data source (an Amazon S3 bucket) to an Amazon Personalize dataset. To allow Amazon Personalize to import the training data, you must specify an AWS Identity and Access Management (IAM) role that has permission to read from the data source.
    A dataset import job can be in one of the following states:
    To get the status of the import job, call  DescribeDatasetImportJob , providing the Amazon Resource Name (ARN) of the dataset import job. The dataset import is complete when the status shows as ACTIVE. If the status shows as CREATE FAILED, the response includes a failureReason key, which describes why the job failed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_dataset_import_job(
        jobName='string',
        datasetArn='string',
        dataSource={
            'dataLocation': 'string'
        },
        roleArn='string'
    )
    
    
    :type jobName: string
    :param jobName: [REQUIRED]\nThe name for the dataset import job.\n

    :type datasetArn: string
    :param datasetArn: [REQUIRED]\nThe ARN of the dataset that receives the imported data.\n

    :type dataSource: dict
    :param dataSource: [REQUIRED]\nThe Amazon S3 bucket that contains the training data to import.\n\ndataLocation (string) --The path to the Amazon S3 bucket where the data that you want to upload to your dataset is stored. For example:\n\ns3://bucket-name/training-data.csv\n\n\n

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe ARN of the IAM role that has permissions to read from the Amazon S3 data source.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'datasetImportJobArn': 'string'
}


Response Structure

(dict) --

datasetImportJobArn (string) --
The ARN of the dataset import job.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException
Personalize.Client.exceptions.ResourceAlreadyExistsException
Personalize.Client.exceptions.LimitExceededException
Personalize.Client.exceptions.ResourceInUseException


    :return: {
        'datasetImportJobArn': 'string'
    }
    
    
    :returns: 
    ListDatasetImportJobs
    DescribeDatasetImportJob
    
    """
    pass

def create_event_tracker(name=None, datasetGroupArn=None):
    """
    Creates an event tracker that you use when sending event data to the specified dataset group using the PutEvents API.
    When Amazon Personalize creates an event tracker, it also creates an event-interactions dataset in the dataset group associated with the event tracker. The event-interactions dataset stores the event data from the PutEvents call. The contents of this dataset are not available to the user.
    When you send event data you include your tracking ID. The tracking ID identifies the customer and authorizes the customer to send the data.
    The event tracker can be in one of the following states:
    To get the status of the event tracker, call  DescribeEventTracker .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_event_tracker(
        name='string',
        datasetGroupArn='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name for the event tracker.\n

    :type datasetGroupArn: string
    :param datasetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the dataset group that receives the event data.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'eventTrackerArn': 'string',
    'trackingId': 'string'
}


Response Structure

(dict) --

eventTrackerArn (string) --
The ARN of the event tracker.

trackingId (string) --
The ID of the event tracker. Include this ID in requests to the PutEvents API.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceAlreadyExistsException
Personalize.Client.exceptions.ResourceNotFoundException
Personalize.Client.exceptions.LimitExceededException
Personalize.Client.exceptions.ResourceInUseException


    :return: {
        'eventTrackerArn': 'string',
        'trackingId': 'string'
    }
    
    
    :returns: 
    ListEventTrackers
    DescribeEventTracker
    DeleteEventTracker
    
    """
    pass

def create_schema(name=None, schema=None):
    """
    Creates an Amazon Personalize schema from the specified schema string. The schema you create must be in Avro JSON format.
    Amazon Personalize recognizes three schema variants. Each schema is associated with a dataset type and has a set of required field and keywords. You specify a schema when you call  CreateDataset .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_schema(
        name='string',
        schema='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name for the schema.\n

    :type schema: string
    :param schema: [REQUIRED]\nA schema in Avro JSON format.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'schemaArn': 'string'
}


Response Structure

(dict) --

schemaArn (string) --
The Amazon Resource Name (ARN) of the created schema.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceAlreadyExistsException
Personalize.Client.exceptions.LimitExceededException


    :return: {
        'schemaArn': 'string'
    }
    
    
    :returns: 
    name (string) -- [REQUIRED]
    The name for the schema.
    
    schema (string) -- [REQUIRED]
    A schema in Avro JSON format.
    
    
    """
    pass

def create_solution(name=None, performHPO=None, performAutoML=None, recipeArn=None, datasetGroupArn=None, eventType=None, solutionConfig=None):
    """
    Creates the configuration for training a model. A trained model is known as a solution. After the configuration is created, you train the model (create a solution) by calling the  CreateSolutionVersion operation. Every time you call CreateSolutionVersion , a new version of the solution is created.
    After creating a solution version, you check its accuracy by calling  GetSolutionMetrics . When you are satisfied with the version, you deploy it using  CreateCampaign . The campaign provides recommendations to a client through the GetRecommendations API.
    To train a model, Amazon Personalize requires training data and a recipe. The training data comes from the dataset group that you provide in the request. A recipe specifies the training algorithm and a feature transformation. You can specify one of the predefined recipes provided by Amazon Personalize. Alternatively, you can specify performAutoML and Amazon Personalize will analyze your data and select the optimum USER_PERSONALIZATION recipe for you.
    A solution can be in one of the following states:
    To get the status of the solution, call  DescribeSolution . Wait until the status shows as ACTIVE before calling CreateSolutionVersion .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_solution(
        name='string',
        performHPO=True|False,
        performAutoML=True|False,
        recipeArn='string',
        datasetGroupArn='string',
        eventType='string',
        solutionConfig={
            'eventValueThreshold': 'string',
            'hpoConfig': {
                'hpoObjective': {
                    'type': 'string',
                    'metricName': 'string',
                    'metricRegex': 'string'
                },
                'hpoResourceConfig': {
                    'maxNumberOfTrainingJobs': 'string',
                    'maxParallelTrainingJobs': 'string'
                },
                'algorithmHyperParameterRanges': {
                    'integerHyperParameterRanges': [
                        {
                            'name': 'string',
                            'minValue': 123,
                            'maxValue': 123
                        },
                    ],
                    'continuousHyperParameterRanges': [
                        {
                            'name': 'string',
                            'minValue': 123.0,
                            'maxValue': 123.0
                        },
                    ],
                    'categoricalHyperParameterRanges': [
                        {
                            'name': 'string',
                            'values': [
                                'string',
                            ]
                        },
                    ]
                }
            },
            'algorithmHyperParameters': {
                'string': 'string'
            },
            'featureTransformationParameters': {
                'string': 'string'
            },
            'autoMLConfig': {
                'metricName': 'string',
                'recipeList': [
                    'string',
                ]
            }
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name for the solution.\n

    :type performHPO: boolean
    :param performHPO: Whether to perform hyperparameter optimization (HPO) on the specified or selected recipe. The default is false .\nWhen performing AutoML, this parameter is always true and you should not set it to false .\n

    :type performAutoML: boolean
    :param performAutoML: Whether to perform automated machine learning (AutoML). The default is false . For this case, you must specify recipeArn .\nWhen set to true , Amazon Personalize analyzes your training data and selects the optimal USER_PERSONALIZATION recipe and hyperparameters. In this case, you must omit recipeArn . Amazon Personalize determines the optimal recipe by running tests with different values for the hyperparameters. AutoML lengthens the training process as compared to selecting a specific recipe.\n

    :type recipeArn: string
    :param recipeArn: The ARN of the recipe to use for model training. Only specified when performAutoML is false.

    :type datasetGroupArn: string
    :param datasetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the dataset group that provides the training data.\n

    :type eventType: string
    :param eventType: When your have multiple event types (using an EVENT_TYPE schema field), this parameter specifies which event type (for example, \'click\' or \'like\') is used for training the model.

    :type solutionConfig: dict
    :param solutionConfig: The configuration to use with the solution. When performAutoML is set to true, Amazon Personalize only evaluates the autoMLConfig section of the solution configuration.\n\neventValueThreshold (string) --Only events with a value greater than or equal to this threshold are used for training a model.\n\nhpoConfig (dict) --Describes the properties for hyperparameter optimization (HPO).\n\nhpoObjective (dict) --The metric to optimize during HPO.\n\ntype (string) --The type of the metric. Valid values are Maximize and Minimize .\n\nmetricName (string) --The name of the metric.\n\nmetricRegex (string) --A regular expression for finding the metric in the training job logs.\n\n\n\nhpoResourceConfig (dict) --Describes the resource configuration for HPO.\n\nmaxNumberOfTrainingJobs (string) --The maximum number of training jobs when you create a solution version. The maximum value for maxNumberOfTrainingJobs is 40 .\n\nmaxParallelTrainingJobs (string) --The maximum number of parallel training jobs when you create a solution version. The maximum value for maxParallelTrainingJobs is 10 .\n\n\n\nalgorithmHyperParameterRanges (dict) --The hyperparameters and their allowable ranges.\n\nintegerHyperParameterRanges (list) --The integer-valued hyperparameters and their ranges.\n\n(dict) --Provides the name and range of an integer-valued hyperparameter.\n\nname (string) --The name of the hyperparameter.\n\nminValue (integer) --The minimum allowable value for the hyperparameter.\n\nmaxValue (integer) --The maximum allowable value for the hyperparameter.\n\n\n\n\n\ncontinuousHyperParameterRanges (list) --The continuous hyperparameters and their ranges.\n\n(dict) --Provides the name and range of a continuous hyperparameter.\n\nname (string) --The name of the hyperparameter.\n\nminValue (float) --The minimum allowable value for the hyperparameter.\n\nmaxValue (float) --The maximum allowable value for the hyperparameter.\n\n\n\n\n\ncategoricalHyperParameterRanges (list) --The categorical hyperparameters and their ranges.\n\n(dict) --Provides the name and range of a categorical hyperparameter.\n\nname (string) --The name of the hyperparameter.\n\nvalues (list) --A list of the categories for the hyperparameter.\n\n(string) --\n\n\n\n\n\n\n\n\n\n\nalgorithmHyperParameters (dict) --Lists the hyperparameter names and ranges.\n\n(string) --\n(string) --\n\n\n\n\nfeatureTransformationParameters (dict) --Lists the feature transformation parameters.\n\n(string) --\n(string) --\n\n\n\n\nautoMLConfig (dict) --The AutoMLConfig object containing a list of recipes to search when AutoML is performed.\n\nmetricName (string) --The metric to optimize.\n\nrecipeList (list) --The list of candidate recipes.\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'solutionArn': 'string'
}


Response Structure

(dict) --

solutionArn (string) --
The ARN of the solution.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceAlreadyExistsException
Personalize.Client.exceptions.ResourceNotFoundException
Personalize.Client.exceptions.LimitExceededException
Personalize.Client.exceptions.ResourceInUseException


    :return: {
        'solutionArn': 'string'
    }
    
    
    :returns: 
    ListSolutions
    CreateSolutionVersion
    DescribeSolution
    DeleteSolution
    ListSolutionVersions
    DescribeSolutionVersion
    
    """
    pass

def create_solution_version(solutionArn=None, trainingMode=None):
    """
    Trains or retrains an active solution. A solution is created using the  CreateSolution operation and must be in the ACTIVE state before calling CreateSolutionVersion . A new version of the solution is created every time you call this operation.
    A solution version can be in one of the following states:
    To get the status of the version, call  DescribeSolutionVersion . Wait until the status shows as ACTIVE before calling CreateCampaign .
    If the status shows as CREATE FAILED, the response includes a failureReason key, which describes why the job failed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_solution_version(
        solutionArn='string',
        trainingMode='FULL'|'UPDATE'
    )
    
    
    :type solutionArn: string
    :param solutionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the solution containing the training configuration information.\n

    :type trainingMode: string
    :param trainingMode: The scope of training to be performed when creating the solution version. The FULL option trains the solution version based on the entirety of the input solution\'s training data, while the UPDATE option processes only the data that has changed in comparison to the input solution. Choose UPDATE when you want to incrementally update your solution version instead of creating an entirely new one.\n\nWarning\nThe UPDATE option can only be used when you already have an active solution version created from the input solution using the FULL option and the input solution was trained with the native-recipe-hrnn-coldstart recipe.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'solutionVersionArn': 'string'
}


Response Structure

(dict) --

solutionVersionArn (string) --
The ARN of the new solution version.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException
Personalize.Client.exceptions.ResourceInUseException


    :return: {
        'solutionVersionArn': 'string'
    }
    
    
    :returns: 
    ListSolutionVersions
    DescribeSolutionVersion
    ListSolutions
    CreateSolution
    DescribeSolution
    DeleteSolution
    
    """
    pass

def delete_campaign(campaignArn=None):
    """
    Removes a campaign by deleting the solution deployment. The solution that the campaign is based on is not deleted and can be redeployed when needed. A deleted campaign can no longer be specified in a GetRecommendations request. For more information on campaigns, see  CreateCampaign .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_campaign(
        campaignArn='string'
    )
    
    
    :type campaignArn: string
    :param campaignArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the campaign to delete.\n

    """
    pass

def delete_dataset(datasetArn=None):
    """
    Deletes a dataset. You can\'t delete a dataset if an associated DatasetImportJob or SolutionVersion is in the CREATE PENDING or IN PROGRESS state. For more information on datasets, see  CreateDataset .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_dataset(
        datasetArn='string'
    )
    
    
    :type datasetArn: string
    :param datasetArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the dataset to delete.\n

    """
    pass

def delete_dataset_group(datasetGroupArn=None):
    """
    Deletes a dataset group. Before you delete a dataset group, you must delete the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_dataset_group(
        datasetGroupArn='string'
    )
    
    
    :type datasetGroupArn: string
    :param datasetGroupArn: [REQUIRED]\nThe ARN of the dataset group to delete.\n

    :returns: 
    Personalize.Client.exceptions.InvalidInputException
    Personalize.Client.exceptions.ResourceNotFoundException
    Personalize.Client.exceptions.ResourceInUseException
    
    """
    pass

def delete_event_tracker(eventTrackerArn=None):
    """
    Deletes the event tracker. Does not delete the event-interactions dataset from the associated dataset group. For more information on event trackers, see  CreateEventTracker .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_event_tracker(
        eventTrackerArn='string'
    )
    
    
    :type eventTrackerArn: string
    :param eventTrackerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the event tracker to delete.\n

    """
    pass

def delete_schema(schemaArn=None):
    """
    Deletes a schema. Before deleting a schema, you must delete all datasets referencing the schema. For more information on schemas, see  CreateSchema .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_schema(
        schemaArn='string'
    )
    
    
    :type schemaArn: string
    :param schemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the schema to delete.\n

    """
    pass

def delete_solution(solutionArn=None):
    """
    Deletes all versions of a solution and the Solution object itself. Before deleting a solution, you must delete all campaigns based on the solution. To determine what campaigns are using the solution, call  ListCampaigns and supply the Amazon Resource Name (ARN) of the solution. You can\'t delete a solution if an associated SolutionVersion is in the CREATE PENDING or IN PROGRESS state. For more information on solutions, see  CreateSolution .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_solution(
        solutionArn='string'
    )
    
    
    :type solutionArn: string
    :param solutionArn: [REQUIRED]\nThe ARN of the solution to delete.\n

    """
    pass

def describe_algorithm(algorithmArn=None):
    """
    Describes the given algorithm.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_algorithm(
        algorithmArn='string'
    )
    
    
    :type algorithmArn: string
    :param algorithmArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the algorithm to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'algorithm': {
        'name': 'string',
        'algorithmArn': 'string',
        'algorithmImage': {
            'name': 'string',
            'dockerURI': 'string'
        },
        'defaultHyperParameters': {
            'string': 'string'
        },
        'defaultHyperParameterRanges': {
            'integerHyperParameterRanges': [
                {
                    'name': 'string',
                    'minValue': 123,
                    'maxValue': 123,
                    'isTunable': True|False
                },
            ],
            'continuousHyperParameterRanges': [
                {
                    'name': 'string',
                    'minValue': 123.0,
                    'maxValue': 123.0,
                    'isTunable': True|False
                },
            ],
            'categoricalHyperParameterRanges': [
                {
                    'name': 'string',
                    'values': [
                        'string',
                    ],
                    'isTunable': True|False
                },
            ]
        },
        'defaultResourceConfig': {
            'string': 'string'
        },
        'trainingInputMode': 'string',
        'roleArn': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
algorithm (dict) --A listing of the properties of the algorithm.

name (string) --The name of the algorithm.

algorithmArn (string) --The Amazon Resource Name (ARN) of the algorithm.

algorithmImage (dict) --The URI of the Docker container for the algorithm image.

name (string) --The name of the algorithm image.

dockerURI (string) --The URI of the Docker container for the algorithm image.



defaultHyperParameters (dict) --Specifies the default hyperparameters.

(string) --
(string) --




defaultHyperParameterRanges (dict) --Specifies the default hyperparameters, their ranges, and whether they are tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).

integerHyperParameterRanges (list) --The integer-valued hyperparameters and their default ranges.

(dict) --Provides the name and default range of a integer-valued hyperparameter and whether the hyperparameter is tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).

name (string) --The name of the hyperparameter.

minValue (integer) --The minimum allowable value for the hyperparameter.

maxValue (integer) --The maximum allowable value for the hyperparameter.

isTunable (boolean) --Indicates whether the hyperparameter is tunable.





continuousHyperParameterRanges (list) --The continuous hyperparameters and their default ranges.

(dict) --Provides the name and default range of a continuous hyperparameter and whether the hyperparameter is tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).

name (string) --The name of the hyperparameter.

minValue (float) --The minimum allowable value for the hyperparameter.

maxValue (float) --The maximum allowable value for the hyperparameter.

isTunable (boolean) --Whether the hyperparameter is tunable.





categoricalHyperParameterRanges (list) --The categorical hyperparameters and their default ranges.

(dict) --Provides the name and default range of a categorical hyperparameter and whether the hyperparameter is tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).

name (string) --The name of the hyperparameter.

values (list) --A list of the categories for the hyperparameter.

(string) --


isTunable (boolean) --Whether the hyperparameter is tunable.







defaultResourceConfig (dict) --Specifies the default maximum number of training jobs and parallel training jobs.

(string) --
(string) --




trainingInputMode (string) --The training input mode.

roleArn (string) --The Amazon Resource Name (ARN) of the role.

creationDateTime (datetime) --The date and time (in Unix time) that the algorithm was created.

lastUpdatedDateTime (datetime) --The date and time (in Unix time) that the algorithm was last updated.








Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'algorithm': {
            'name': 'string',
            'algorithmArn': 'string',
            'algorithmImage': {
                'name': 'string',
                'dockerURI': 'string'
            },
            'defaultHyperParameters': {
                'string': 'string'
            },
            'defaultHyperParameterRanges': {
                'integerHyperParameterRanges': [
                    {
                        'name': 'string',
                        'minValue': 123,
                        'maxValue': 123,
                        'isTunable': True|False
                    },
                ],
                'continuousHyperParameterRanges': [
                    {
                        'name': 'string',
                        'minValue': 123.0,
                        'maxValue': 123.0,
                        'isTunable': True|False
                    },
                ],
                'categoricalHyperParameterRanges': [
                    {
                        'name': 'string',
                        'values': [
                            'string',
                        ],
                        'isTunable': True|False
                    },
                ]
            },
            'defaultResourceConfig': {
                'string': 'string'
            },
            'trainingInputMode': 'string',
            'roleArn': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_batch_inference_job(batchInferenceJobArn=None):
    """
    Gets the properties of a batch inference job including name, Amazon Resource Name (ARN), status, input and output configurations, and the ARN of the solution version used to generate the recommendations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_batch_inference_job(
        batchInferenceJobArn='string'
    )
    
    
    :type batchInferenceJobArn: string
    :param batchInferenceJobArn: [REQUIRED]\nThe ARN of the batch inference job to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'batchInferenceJob': {
        'jobName': 'string',
        'batchInferenceJobArn': 'string',
        'failureReason': 'string',
        'solutionVersionArn': 'string',
        'numResults': 123,
        'jobInput': {
            's3DataSource': {
                'path': 'string',
                'kmsKeyArn': 'string'
            }
        },
        'jobOutput': {
            's3DataDestination': {
                'path': 'string',
                'kmsKeyArn': 'string'
            }
        },
        'roleArn': 'string',
        'status': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
batchInferenceJob (dict) --Information on the specified batch inference job.

jobName (string) --The name of the batch inference job.

batchInferenceJobArn (string) --The Amazon Resource Name (ARN) of the batch inference job.

failureReason (string) --If the batch inference job failed, the reason for the failure.

solutionVersionArn (string) --The Amazon Resource Name (ARN) of the solution version from which the batch inference job was created.

numResults (integer) --The number of recommendations generated by the batch inference job. This number includes the error messages generated for failed input records.

jobInput (dict) --The Amazon S3 path that leads to the input data used to generate the batch inference job.

s3DataSource (dict) --The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket must be in the same region as the API endpoint you are calling.

path (string) --The file path of the Amazon S3 bucket.

kmsKeyArn (string) --The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that Amazon Personalize uses to encrypt or decrypt the input and output files of a batch inference job.





jobOutput (dict) --The Amazon S3 bucket that contains the output data generated by the batch inference job.

s3DataDestination (dict) --Information on the Amazon S3 bucket in which the batch inference job\'s output is stored.

path (string) --The file path of the Amazon S3 bucket.

kmsKeyArn (string) --The Amazon Resource Name (ARN) of the Amazon Key Management Service (KMS) key that Amazon Personalize uses to encrypt or decrypt the input and output files of a batch inference job.





roleArn (string) --The ARN of the Amazon Identity and Access Management (IAM) role that requested the batch inference job.

status (string) --The status of the batch inference job. The status is one of the following values:

PENDING
IN PROGRESS
ACTIVE
CREATE FAILED


creationDateTime (datetime) --The time at which the batch inference job was created.

lastUpdatedDateTime (datetime) --The time at which the batch inference job was last updated.








Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'batchInferenceJob': {
            'jobName': 'string',
            'batchInferenceJobArn': 'string',
            'failureReason': 'string',
            'solutionVersionArn': 'string',
            'numResults': 123,
            'jobInput': {
                's3DataSource': {
                    'path': 'string',
                    'kmsKeyArn': 'string'
                }
            },
            'jobOutput': {
                's3DataDestination': {
                    'path': 'string',
                    'kmsKeyArn': 'string'
                }
            },
            'roleArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Personalize.Client.exceptions.InvalidInputException
    Personalize.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_campaign(campaignArn=None):
    """
    Describes the given campaign, including its status.
    A campaign can be in one of the following states:
    When the status is CREATE FAILED , the response includes the failureReason key, which describes why.
    For more information on campaigns, see  CreateCampaign .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_campaign(
        campaignArn='string'
    )
    
    
    :type campaignArn: string
    :param campaignArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the campaign.\n

    :rtype: dict
ReturnsResponse Syntax{
    'campaign': {
        'name': 'string',
        'campaignArn': 'string',
        'solutionVersionArn': 'string',
        'minProvisionedTPS': 123,
        'status': 'string',
        'failureReason': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1),
        'latestCampaignUpdate': {
            'solutionVersionArn': 'string',
            'minProvisionedTPS': 123,
            'status': 'string',
            'failureReason': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        }
    }
}


Response Structure

(dict) --
campaign (dict) --The properties of the campaign.

name (string) --The name of the campaign.

campaignArn (string) --The Amazon Resource Name (ARN) of the campaign.

solutionVersionArn (string) --The Amazon Resource Name (ARN) of a specific version of the solution.

minProvisionedTPS (integer) --Specifies the requested minimum provisioned transactions (recommendations) per second.

status (string) --The status of the campaign.
A campaign can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING > DELETE IN_PROGRESS


failureReason (string) --If a campaign fails, the reason behind the failure.

creationDateTime (datetime) --The date and time (in Unix format) that the campaign was created.

lastUpdatedDateTime (datetime) --The date and time (in Unix format) that the campaign was last updated.

latestCampaignUpdate (dict) --Provides a summary of the properties of a campaign update. For a complete listing, call the  DescribeCampaign API.

solutionVersionArn (string) --The Amazon Resource Name (ARN) of the deployed solution version.

minProvisionedTPS (integer) --Specifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support.

status (string) --The status of the campaign update.
A campaign update can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING > DELETE IN_PROGRESS


failureReason (string) --If a campaign update fails, the reason behind the failure.

creationDateTime (datetime) --The date and time (in Unix time) that the campaign update was created.

lastUpdatedDateTime (datetime) --The date and time (in Unix time) that the campaign update was last updated.










Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'campaign': {
            'name': 'string',
            'campaignArn': 'string',
            'solutionVersionArn': 'string',
            'minProvisionedTPS': 123,
            'status': 'string',
            'failureReason': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'latestCampaignUpdate': {
                'solutionVersionArn': 'string',
                'minProvisionedTPS': 123,
                'status': 'string',
                'failureReason': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1)
            }
        }
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    DELETE PENDING > DELETE IN_PROGRESS
    
    """
    pass

def describe_dataset(datasetArn=None):
    """
    Describes the given dataset. For more information on datasets, see  CreateDataset .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_dataset(
        datasetArn='string'
    )
    
    
    :type datasetArn: string
    :param datasetArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the dataset to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'dataset': {
        'name': 'string',
        'datasetArn': 'string',
        'datasetGroupArn': 'string',
        'datasetType': 'string',
        'schemaArn': 'string',
        'status': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
dataset (dict) --A listing of the dataset\'s properties.

name (string) --The name of the dataset.

datasetArn (string) --The Amazon Resource Name (ARN) of the dataset that you want metadata for.

datasetGroupArn (string) --The Amazon Resource Name (ARN) of the dataset group.

datasetType (string) --One of the following values:

Interactions
Items
Users


schemaArn (string) --The ARN of the associated schema.

status (string) --The status of the dataset.
A dataset can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING > DELETE IN_PROGRESS


creationDateTime (datetime) --The creation date and time (in Unix time) of the dataset.

lastUpdatedDateTime (datetime) --A time stamp that shows when the dataset was updated.








Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'dataset': {
            'name': 'string',
            'datasetArn': 'string',
            'datasetGroupArn': 'string',
            'datasetType': 'string',
            'schemaArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    DELETE PENDING > DELETE IN_PROGRESS
    
    """
    pass

def describe_dataset_group(datasetGroupArn=None):
    """
    Describes the given dataset group. For more information on dataset groups, see  CreateDatasetGroup .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_dataset_group(
        datasetGroupArn='string'
    )
    
    
    :type datasetGroupArn: string
    :param datasetGroupArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the dataset group to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'datasetGroup': {
        'name': 'string',
        'datasetGroupArn': 'string',
        'status': 'string',
        'roleArn': 'string',
        'kmsKeyArn': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1),
        'failureReason': 'string'
    }
}


Response Structure

(dict) --
datasetGroup (dict) --A listing of the dataset group\'s properties.

name (string) --The name of the dataset group.

datasetGroupArn (string) --The Amazon Resource Name (ARN) of the dataset group.

status (string) --The current status of the dataset group.
A dataset group can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING


roleArn (string) --The ARN of the IAM role that has permissions to create the dataset group.

kmsKeyArn (string) --The Amazon Resource Name (ARN) of the KMS key used to encrypt the datasets.

creationDateTime (datetime) --The creation date and time (in Unix time) of the dataset group.

lastUpdatedDateTime (datetime) --The last update date and time (in Unix time) of the dataset group.

failureReason (string) --If creating a dataset group fails, provides the reason why.








Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'datasetGroup': {
            'name': 'string',
            'datasetGroupArn': 'string',
            'status': 'string',
            'roleArn': 'string',
            'kmsKeyArn': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'failureReason': 'string'
        }
    }
    
    
    :returns: 
    Personalize.Client.exceptions.InvalidInputException
    Personalize.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_dataset_import_job(datasetImportJobArn=None):
    """
    Describes the dataset import job created by  CreateDatasetImportJob , including the import job status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_dataset_import_job(
        datasetImportJobArn='string'
    )
    
    
    :type datasetImportJobArn: string
    :param datasetImportJobArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the dataset import job to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'datasetImportJob': {
        'jobName': 'string',
        'datasetImportJobArn': 'string',
        'datasetArn': 'string',
        'dataSource': {
            'dataLocation': 'string'
        },
        'roleArn': 'string',
        'status': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1),
        'failureReason': 'string'
    }
}


Response Structure

(dict) --
datasetImportJob (dict) --Information about the dataset import job, including the status.
The status is one of the following values:

CREATE PENDING
CREATE IN_PROGRESS
ACTIVE
CREATE FAILED


jobName (string) --The name of the import job.

datasetImportJobArn (string) --The ARN of the dataset import job.

datasetArn (string) --The Amazon Resource Name (ARN) of the dataset that receives the imported data.

dataSource (dict) --The Amazon S3 bucket that contains the training data to import.

dataLocation (string) --The path to the Amazon S3 bucket where the data that you want to upload to your dataset is stored. For example:

s3://bucket-name/training-data.csv



roleArn (string) --The ARN of the AWS Identity and Access Management (IAM) role that has permissions to read from the Amazon S3 data source.

status (string) --The status of the dataset import job.
A dataset import job can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED


creationDateTime (datetime) --The creation date and time (in Unix time) of the dataset import job.

lastUpdatedDateTime (datetime) --The date and time (in Unix time) the dataset was last updated.

failureReason (string) --If a dataset import job fails, provides the reason why.








Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'datasetImportJob': {
            'jobName': 'string',
            'datasetImportJobArn': 'string',
            'datasetArn': 'string',
            'dataSource': {
                'dataLocation': 'string'
            },
            'roleArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'failureReason': 'string'
        }
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    
    """
    pass

def describe_event_tracker(eventTrackerArn=None):
    """
    Describes an event tracker. The response includes the trackingId and status of the event tracker. For more information on event trackers, see  CreateEventTracker .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_tracker(
        eventTrackerArn='string'
    )
    
    
    :type eventTrackerArn: string
    :param eventTrackerArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the event tracker to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'eventTracker': {
        'name': 'string',
        'eventTrackerArn': 'string',
        'accountId': 'string',
        'trackingId': 'string',
        'datasetGroupArn': 'string',
        'status': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
eventTracker (dict) --An object that describes the event tracker.

name (string) --The name of the event tracker.

eventTrackerArn (string) --The ARN of the event tracker.

accountId (string) --The Amazon AWS account that owns the event tracker.

trackingId (string) --The ID of the event tracker. Include this ID in requests to the PutEvents API.

datasetGroupArn (string) --The Amazon Resource Name (ARN) of the dataset group that receives the event data.

status (string) --The status of the event tracker.
An event tracker can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING > DELETE IN_PROGRESS


creationDateTime (datetime) --The date and time (in Unix format) that the event tracker was created.

lastUpdatedDateTime (datetime) --The date and time (in Unix time) that the event tracker was last updated.








Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'eventTracker': {
            'name': 'string',
            'eventTrackerArn': 'string',
            'accountId': 'string',
            'trackingId': 'string',
            'datasetGroupArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Personalize.Client.exceptions.InvalidInputException
    Personalize.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_feature_transformation(featureTransformationArn=None):
    """
    Describes the given feature transformation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_feature_transformation(
        featureTransformationArn='string'
    )
    
    
    :type featureTransformationArn: string
    :param featureTransformationArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the feature transformation to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'featureTransformation': {
        'name': 'string',
        'featureTransformationArn': 'string',
        'defaultParameters': {
            'string': 'string'
        },
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1),
        'status': 'string'
    }
}


Response Structure

(dict) --
featureTransformation (dict) --A listing of the FeatureTransformation properties.

name (string) --The name of the feature transformation.

featureTransformationArn (string) --The Amazon Resource Name (ARN) of the FeatureTransformation object.

defaultParameters (dict) --Provides the default parameters for feature transformation.

(string) --
(string) --




creationDateTime (datetime) --The creation date and time (in Unix time) of the feature transformation.

lastUpdatedDateTime (datetime) --The last update date and time (in Unix time) of the feature transformation.

status (string) --The status of the feature transformation.
A feature transformation can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED









Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'featureTransformation': {
            'name': 'string',
            'featureTransformationArn': 'string',
            'defaultParameters': {
                'string': 'string'
            },
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'status': 'string'
        }
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    
    """
    pass

def describe_recipe(recipeArn=None):
    """
    Describes a recipe.
    A recipe contains three items:
    Amazon Personalize provides a set of predefined recipes. You specify a recipe when you create a solution with the  CreateSolution API. CreateSolution trains a model by using the algorithm in the specified recipe and a training dataset. The solution, when deployed as a campaign, can provide recommendations using the GetRecommendations API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_recipe(
        recipeArn='string'
    )
    
    
    :type recipeArn: string
    :param recipeArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the recipe to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'recipe': {
        'name': 'string',
        'recipeArn': 'string',
        'algorithmArn': 'string',
        'featureTransformationArn': 'string',
        'status': 'string',
        'description': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'recipeType': 'string',
        'lastUpdatedDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
recipe (dict) --An object that describes the recipe.

name (string) --The name of the recipe.

recipeArn (string) --The Amazon Resource Name (ARN) of the recipe.

algorithmArn (string) --The Amazon Resource Name (ARN) of the algorithm that Amazon Personalize uses to train the model.

featureTransformationArn (string) --The ARN of the FeatureTransformation object.

status (string) --The status of the recipe.

description (string) --The description of the recipe.

creationDateTime (datetime) --The date and time (in Unix format) that the recipe was created.

recipeType (string) --One of the following values:

PERSONALIZED_RANKING
RELATED_ITEMS
USER_PERSONALIZATION


lastUpdatedDateTime (datetime) --The date and time (in Unix format) that the recipe was last updated.








Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'recipe': {
            'name': 'string',
            'recipeArn': 'string',
            'algorithmArn': 'string',
            'featureTransformationArn': 'string',
            'status': 'string',
            'description': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'recipeType': 'string',
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    PERSONALIZED_RANKING
    RELATED_ITEMS
    USER_PERSONALIZATION
    
    """
    pass

def describe_schema(schemaArn=None):
    """
    Describes a schema. For more information on schemas, see  CreateSchema .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_schema(
        schemaArn='string'
    )
    
    
    :type schemaArn: string
    :param schemaArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the schema to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'schema': {
        'name': 'string',
        'schemaArn': 'string',
        'schema': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
schema (dict) --The requested schema.

name (string) --The name of the schema.

schemaArn (string) --The Amazon Resource Name (ARN) of the schema.

schema (string) --The schema.

creationDateTime (datetime) --The date and time (in Unix time) that the schema was created.

lastUpdatedDateTime (datetime) --The date and time (in Unix time) that the schema was last updated.








Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'schema': {
            'name': 'string',
            'schemaArn': 'string',
            'schema': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def describe_solution(solutionArn=None):
    """
    Describes a solution. For more information on solutions, see  CreateSolution .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_solution(
        solutionArn='string'
    )
    
    
    :type solutionArn: string
    :param solutionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the solution to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'solution': {
        'name': 'string',
        'solutionArn': 'string',
        'performHPO': True|False,
        'performAutoML': True|False,
        'recipeArn': 'string',
        'datasetGroupArn': 'string',
        'eventType': 'string',
        'solutionConfig': {
            'eventValueThreshold': 'string',
            'hpoConfig': {
                'hpoObjective': {
                    'type': 'string',
                    'metricName': 'string',
                    'metricRegex': 'string'
                },
                'hpoResourceConfig': {
                    'maxNumberOfTrainingJobs': 'string',
                    'maxParallelTrainingJobs': 'string'
                },
                'algorithmHyperParameterRanges': {
                    'integerHyperParameterRanges': [
                        {
                            'name': 'string',
                            'minValue': 123,
                            'maxValue': 123
                        },
                    ],
                    'continuousHyperParameterRanges': [
                        {
                            'name': 'string',
                            'minValue': 123.0,
                            'maxValue': 123.0
                        },
                    ],
                    'categoricalHyperParameterRanges': [
                        {
                            'name': 'string',
                            'values': [
                                'string',
                            ]
                        },
                    ]
                }
            },
            'algorithmHyperParameters': {
                'string': 'string'
            },
            'featureTransformationParameters': {
                'string': 'string'
            },
            'autoMLConfig': {
                'metricName': 'string',
                'recipeList': [
                    'string',
                ]
            }
        },
        'autoMLResult': {
            'bestRecipeArn': 'string'
        },
        'status': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1),
        'latestSolutionVersion': {
            'solutionVersionArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'failureReason': 'string'
        }
    }
}


Response Structure

(dict) --
solution (dict) --An object that describes the solution.

name (string) --The name of the solution.

solutionArn (string) --The ARN of the solution.

performHPO (boolean) --Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is false .

performAutoML (boolean) --When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from the list specified in the solution configuration (recipeArn must not be specified). When false (the default), Amazon Personalize uses recipeArn for training.

recipeArn (string) --The ARN of the recipe used to create the solution.

datasetGroupArn (string) --The Amazon Resource Name (ARN) of the dataset group that provides the training data.

eventType (string) --The event type (for example, \'click\' or \'like\') that is used for training the model.

solutionConfig (dict) --Describes the configuration properties for the solution.

eventValueThreshold (string) --Only events with a value greater than or equal to this threshold are used for training a model.

hpoConfig (dict) --Describes the properties for hyperparameter optimization (HPO).

hpoObjective (dict) --The metric to optimize during HPO.

type (string) --The type of the metric. Valid values are Maximize and Minimize .

metricName (string) --The name of the metric.

metricRegex (string) --A regular expression for finding the metric in the training job logs.



hpoResourceConfig (dict) --Describes the resource configuration for HPO.

maxNumberOfTrainingJobs (string) --The maximum number of training jobs when you create a solution version. The maximum value for maxNumberOfTrainingJobs is 40 .

maxParallelTrainingJobs (string) --The maximum number of parallel training jobs when you create a solution version. The maximum value for maxParallelTrainingJobs is 10 .



algorithmHyperParameterRanges (dict) --The hyperparameters and their allowable ranges.

integerHyperParameterRanges (list) --The integer-valued hyperparameters and their ranges.

(dict) --Provides the name and range of an integer-valued hyperparameter.

name (string) --The name of the hyperparameter.

minValue (integer) --The minimum allowable value for the hyperparameter.

maxValue (integer) --The maximum allowable value for the hyperparameter.





continuousHyperParameterRanges (list) --The continuous hyperparameters and their ranges.

(dict) --Provides the name and range of a continuous hyperparameter.

name (string) --The name of the hyperparameter.

minValue (float) --The minimum allowable value for the hyperparameter.

maxValue (float) --The maximum allowable value for the hyperparameter.





categoricalHyperParameterRanges (list) --The categorical hyperparameters and their ranges.

(dict) --Provides the name and range of a categorical hyperparameter.

name (string) --The name of the hyperparameter.

values (list) --A list of the categories for the hyperparameter.

(string) --










algorithmHyperParameters (dict) --Lists the hyperparameter names and ranges.

(string) --
(string) --




featureTransformationParameters (dict) --Lists the feature transformation parameters.

(string) --
(string) --




autoMLConfig (dict) --The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

metricName (string) --The metric to optimize.

recipeList (list) --The list of candidate recipes.

(string) --






autoMLResult (dict) --When performAutoML is true, specifies the best recipe found.

bestRecipeArn (string) --The Amazon Resource Name (ARN) of the best recipe.



status (string) --The status of the solution.
A solution can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING > DELETE IN_PROGRESS


creationDateTime (datetime) --The creation date and time (in Unix time) of the solution.

lastUpdatedDateTime (datetime) --The date and time (in Unix time) that the solution was last updated.

latestSolutionVersion (dict) --Describes the latest version of the solution, including the status and the ARN.

solutionVersionArn (string) --The Amazon Resource Name (ARN) of the solution version.

status (string) --The status of the solution version.
A solution version can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED


creationDateTime (datetime) --The date and time (in Unix time) that this version of a solution was created.

lastUpdatedDateTime (datetime) --The date and time (in Unix time) that the solution version was last updated.

failureReason (string) --If a solution version fails, the reason behind the failure.










Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'solution': {
            'name': 'string',
            'solutionArn': 'string',
            'performHPO': True|False,
            'performAutoML': True|False,
            'recipeArn': 'string',
            'datasetGroupArn': 'string',
            'eventType': 'string',
            'solutionConfig': {
                'eventValueThreshold': 'string',
                'hpoConfig': {
                    'hpoObjective': {
                        'type': 'string',
                        'metricName': 'string',
                        'metricRegex': 'string'
                    },
                    'hpoResourceConfig': {
                        'maxNumberOfTrainingJobs': 'string',
                        'maxParallelTrainingJobs': 'string'
                    },
                    'algorithmHyperParameterRanges': {
                        'integerHyperParameterRanges': [
                            {
                                'name': 'string',
                                'minValue': 123,
                                'maxValue': 123
                            },
                        ],
                        'continuousHyperParameterRanges': [
                            {
                                'name': 'string',
                                'minValue': 123.0,
                                'maxValue': 123.0
                            },
                        ],
                        'categoricalHyperParameterRanges': [
                            {
                                'name': 'string',
                                'values': [
                                    'string',
                                ]
                            },
                        ]
                    }
                },
                'algorithmHyperParameters': {
                    'string': 'string'
                },
                'featureTransformationParameters': {
                    'string': 'string'
                },
                'autoMLConfig': {
                    'metricName': 'string',
                    'recipeList': [
                        'string',
                    ]
                }
            },
            'autoMLResult': {
                'bestRecipeArn': 'string'
            },
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'latestSolutionVersion': {
                'solutionVersionArn': 'string',
                'status': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1),
                'failureReason': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_solution_version(solutionVersionArn=None):
    """
    Describes a specific version of a solution. For more information on solutions, see  CreateSolution .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_solution_version(
        solutionVersionArn='string'
    )
    
    
    :type solutionVersionArn: string
    :param solutionVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the solution version.\n

    :rtype: dict
ReturnsResponse Syntax{
    'solutionVersion': {
        'solutionVersionArn': 'string',
        'solutionArn': 'string',
        'performHPO': True|False,
        'performAutoML': True|False,
        'recipeArn': 'string',
        'eventType': 'string',
        'datasetGroupArn': 'string',
        'solutionConfig': {
            'eventValueThreshold': 'string',
            'hpoConfig': {
                'hpoObjective': {
                    'type': 'string',
                    'metricName': 'string',
                    'metricRegex': 'string'
                },
                'hpoResourceConfig': {
                    'maxNumberOfTrainingJobs': 'string',
                    'maxParallelTrainingJobs': 'string'
                },
                'algorithmHyperParameterRanges': {
                    'integerHyperParameterRanges': [
                        {
                            'name': 'string',
                            'minValue': 123,
                            'maxValue': 123
                        },
                    ],
                    'continuousHyperParameterRanges': [
                        {
                            'name': 'string',
                            'minValue': 123.0,
                            'maxValue': 123.0
                        },
                    ],
                    'categoricalHyperParameterRanges': [
                        {
                            'name': 'string',
                            'values': [
                                'string',
                            ]
                        },
                    ]
                }
            },
            'algorithmHyperParameters': {
                'string': 'string'
            },
            'featureTransformationParameters': {
                'string': 'string'
            },
            'autoMLConfig': {
                'metricName': 'string',
                'recipeList': [
                    'string',
                ]
            }
        },
        'trainingHours': 123.0,
        'trainingMode': 'FULL'|'UPDATE',
        'tunedHPOParams': {
            'algorithmHyperParameters': {
                'string': 'string'
            }
        },
        'status': 'string',
        'failureReason': 'string',
        'creationDateTime': datetime(2015, 1, 1),
        'lastUpdatedDateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
solutionVersion (dict) --The solution version.

solutionVersionArn (string) --The ARN of the solution version.

solutionArn (string) --The ARN of the solution.

performHPO (boolean) --Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is false .

performAutoML (boolean) --When true, Amazon Personalize searches for the most optimal recipe according to the solution configuration. When false (the default), Amazon Personalize uses recipeArn .

recipeArn (string) --The ARN of the recipe used in the solution.

eventType (string) --The event type (for example, \'click\' or \'like\') that is used for training the model.

datasetGroupArn (string) --The Amazon Resource Name (ARN) of the dataset group providing the training data.

solutionConfig (dict) --Describes the configuration properties for the solution.

eventValueThreshold (string) --Only events with a value greater than or equal to this threshold are used for training a model.

hpoConfig (dict) --Describes the properties for hyperparameter optimization (HPO).

hpoObjective (dict) --The metric to optimize during HPO.

type (string) --The type of the metric. Valid values are Maximize and Minimize .

metricName (string) --The name of the metric.

metricRegex (string) --A regular expression for finding the metric in the training job logs.



hpoResourceConfig (dict) --Describes the resource configuration for HPO.

maxNumberOfTrainingJobs (string) --The maximum number of training jobs when you create a solution version. The maximum value for maxNumberOfTrainingJobs is 40 .

maxParallelTrainingJobs (string) --The maximum number of parallel training jobs when you create a solution version. The maximum value for maxParallelTrainingJobs is 10 .



algorithmHyperParameterRanges (dict) --The hyperparameters and their allowable ranges.

integerHyperParameterRanges (list) --The integer-valued hyperparameters and their ranges.

(dict) --Provides the name and range of an integer-valued hyperparameter.

name (string) --The name of the hyperparameter.

minValue (integer) --The minimum allowable value for the hyperparameter.

maxValue (integer) --The maximum allowable value for the hyperparameter.





continuousHyperParameterRanges (list) --The continuous hyperparameters and their ranges.

(dict) --Provides the name and range of a continuous hyperparameter.

name (string) --The name of the hyperparameter.

minValue (float) --The minimum allowable value for the hyperparameter.

maxValue (float) --The maximum allowable value for the hyperparameter.





categoricalHyperParameterRanges (list) --The categorical hyperparameters and their ranges.

(dict) --Provides the name and range of a categorical hyperparameter.

name (string) --The name of the hyperparameter.

values (list) --A list of the categories for the hyperparameter.

(string) --










algorithmHyperParameters (dict) --Lists the hyperparameter names and ranges.

(string) --
(string) --




featureTransformationParameters (dict) --Lists the feature transformation parameters.

(string) --
(string) --




autoMLConfig (dict) --The  AutoMLConfig object containing a list of recipes to search when AutoML is performed.

metricName (string) --The metric to optimize.

recipeList (list) --The list of candidate recipes.

(string) --






trainingHours (float) --The time used to train the model. You are billed for the time it takes to train a model. This field is visible only after Amazon Personalize successfully trains a model.

trainingMode (string) --The scope of training used to create the solution version. The FULL option trains the solution version based on the entirety of the input solution\'s training data, while the UPDATE option processes only the training data that has changed since the creation of the last solution version. Choose UPDATE when you want to start recommending items added to the dataset without retraining the model.

Warning
The UPDATE option can only be used after you\'ve created a solution version with the FULL option and the training solution uses the  native-recipe-hrnn-coldstart .


tunedHPOParams (dict) --If hyperparameter optimization was performed, contains the hyperparameter values of the best performing model.

algorithmHyperParameters (dict) --A list of the hyperparameter values of the best performing model.

(string) --
(string) --






status (string) --The status of the solution version.
A solution version can be in one of the following states:

CREATE PENDING
CREATE IN_PROGRESS
ACTIVE
CREATE FAILED


failureReason (string) --If training a solution version fails, the reason for the failure.

creationDateTime (datetime) --The date and time (in Unix time) that this version of the solution was created.

lastUpdatedDateTime (datetime) --The date and time (in Unix time) that the solution was last updated.








Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException


    :return: {
        'solutionVersion': {
            'solutionVersionArn': 'string',
            'solutionArn': 'string',
            'performHPO': True|False,
            'performAutoML': True|False,
            'recipeArn': 'string',
            'eventType': 'string',
            'datasetGroupArn': 'string',
            'solutionConfig': {
                'eventValueThreshold': 'string',
                'hpoConfig': {
                    'hpoObjective': {
                        'type': 'string',
                        'metricName': 'string',
                        'metricRegex': 'string'
                    },
                    'hpoResourceConfig': {
                        'maxNumberOfTrainingJobs': 'string',
                        'maxParallelTrainingJobs': 'string'
                    },
                    'algorithmHyperParameterRanges': {
                        'integerHyperParameterRanges': [
                            {
                                'name': 'string',
                                'minValue': 123,
                                'maxValue': 123
                            },
                        ],
                        'continuousHyperParameterRanges': [
                            {
                                'name': 'string',
                                'minValue': 123.0,
                                'maxValue': 123.0
                            },
                        ],
                        'categoricalHyperParameterRanges': [
                            {
                                'name': 'string',
                                'values': [
                                    'string',
                                ]
                            },
                        ]
                    }
                },
                'algorithmHyperParameters': {
                    'string': 'string'
                },
                'featureTransformationParameters': {
                    'string': 'string'
                },
                'autoMLConfig': {
                    'metricName': 'string',
                    'recipeList': [
                        'string',
                    ]
                }
            },
            'trainingHours': 123.0,
            'trainingMode': 'FULL'|'UPDATE',
            'tunedHPOParams': {
                'algorithmHyperParameters': {
                    'string': 'string'
                }
            },
            'status': 'string',
            'failureReason': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    (string) --
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

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_solution_metrics(solutionVersionArn=None):
    """
    Gets the metrics for the specified solution version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_solution_metrics(
        solutionVersionArn='string'
    )
    
    
    :type solutionVersionArn: string
    :param solutionVersionArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the solution version for which to get metrics.\n

    :rtype: dict
ReturnsResponse Syntax{
    'solutionVersionArn': 'string',
    'metrics': {
        'string': 123.0
    }
}


Response Structure

(dict) --
solutionVersionArn (string) --The same solution version ARN as specified in the request.

metrics (dict) --The metrics for the solution version.

(string) --
(float) --









Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException
Personalize.Client.exceptions.ResourceInUseException


    :return: {
        'solutionVersionArn': 'string',
        'metrics': {
            'string': 123.0
        }
    }
    
    
    :returns: 
    Personalize.Client.exceptions.InvalidInputException
    Personalize.Client.exceptions.ResourceNotFoundException
    Personalize.Client.exceptions.ResourceInUseException
    
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

def list_batch_inference_jobs(solutionVersionArn=None, nextToken=None, maxResults=None):
    """
    Gets a list of the batch inference jobs that have been performed off of a solution version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_batch_inference_jobs(
        solutionVersionArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type solutionVersionArn: string
    :param solutionVersionArn: The Amazon Resource Name (ARN) of the solution version from which the batch inference jobs were created.

    :type nextToken: string
    :param nextToken: The token to request the next page of results.

    :type maxResults: integer
    :param maxResults: The maximum number of batch inference job results to return in each page. The default value is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'batchInferenceJobs': [
        {
            'batchInferenceJobArn': 'string',
            'jobName': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'failureReason': 'string',
            'solutionVersionArn': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

batchInferenceJobs (list) --
A list containing information on each job that is returned.

(dict) --
A truncated version of the  BatchInferenceJob datatype. The  ListBatchInferenceJobs operation returns a list of batch inference job summaries.

batchInferenceJobArn (string) --
The Amazon Resource Name (ARN) of the batch inference job.

jobName (string) --
The name of the batch inference job.

status (string) --
The status of the batch inference job. The status is one of the following values:

PENDING
IN PROGRESS
ACTIVE
CREATE FAILED


creationDateTime (datetime) --
The time at which the batch inference job was created.

lastUpdatedDateTime (datetime) --
The time at which the batch inference job was last updated.

failureReason (string) --
If the batch inference job failed, the reason for the failure.

solutionVersionArn (string) --
The ARN of the solution version used by the batch inference job.





nextToken (string) --
The token to use to retreive the next page of results. The value is null when there are no more results to return.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.InvalidNextTokenException


    :return: {
        'batchInferenceJobs': [
            {
                'batchInferenceJobArn': 'string',
                'jobName': 'string',
                'status': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1),
                'failureReason': 'string',
                'solutionVersionArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    PENDING
    IN PROGRESS
    ACTIVE
    CREATE FAILED
    
    """
    pass

def list_campaigns(solutionArn=None, nextToken=None, maxResults=None):
    """
    Returns a list of campaigns that use the given solution. When a solution is not specified, all the campaigns associated with the account are listed. The response provides the properties for each campaign, including the Amazon Resource Name (ARN). For more information on campaigns, see  CreateCampaign .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_campaigns(
        solutionArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type solutionArn: string
    :param solutionArn: The Amazon Resource Name (ARN) of the solution to list the campaigns for. When a solution is not specified, all the campaigns associated with the account are listed.

    :type nextToken: string
    :param nextToken: A token returned from the previous call to ListCampaigns for getting the next set of campaigns (if they exist).

    :type maxResults: integer
    :param maxResults: The maximum number of campaigns to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'campaigns': [
        {
            'name': 'string',
            'campaignArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'failureReason': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

campaigns (list) --
A list of the campaigns.

(dict) --
Provides a summary of the properties of a campaign. For a complete listing, call the  DescribeCampaign API.

name (string) --
The name of the campaign.

campaignArn (string) --
The Amazon Resource Name (ARN) of the campaign.

status (string) --
The status of the campaign.
A campaign can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING > DELETE IN_PROGRESS


creationDateTime (datetime) --
The date and time (in Unix time) that the campaign was created.

lastUpdatedDateTime (datetime) --
The date and time (in Unix time) that the campaign was last updated.

failureReason (string) --
If a campaign fails, the reason behind the failure.





nextToken (string) --
A token for getting the next set of campaigns (if they exist).







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.InvalidNextTokenException


    :return: {
        'campaigns': [
            {
                'name': 'string',
                'campaignArn': 'string',
                'status': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1),
                'failureReason': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    DELETE PENDING > DELETE IN_PROGRESS
    
    """
    pass

def list_dataset_groups(nextToken=None, maxResults=None):
    """
    Returns a list of dataset groups. The response provides the properties for each dataset group, including the Amazon Resource Name (ARN). For more information on dataset groups, see  CreateDatasetGroup .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_dataset_groups(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: A token returned from the previous call to ListDatasetGroups for getting the next set of dataset groups (if they exist).

    :type maxResults: integer
    :param maxResults: The maximum number of dataset groups to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'datasetGroups': [
        {
            'name': 'string',
            'datasetGroupArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'failureReason': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

datasetGroups (list) --
The list of your dataset groups.

(dict) --
Provides a summary of the properties of a dataset group. For a complete listing, call the  DescribeDatasetGroup API.

name (string) --
The name of the dataset group.

datasetGroupArn (string) --
The Amazon Resource Name (ARN) of the dataset group.

status (string) --
The status of the dataset group.
A dataset group can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING


creationDateTime (datetime) --
The date and time (in Unix time) that the dataset group was created.

lastUpdatedDateTime (datetime) --
The date and time (in Unix time) that the dataset group was last updated.

failureReason (string) --
If creating a dataset group fails, the reason behind the failure.





nextToken (string) --
A token for getting the next set of dataset groups (if they exist).







Exceptions

Personalize.Client.exceptions.InvalidNextTokenException


    :return: {
        'datasetGroups': [
            {
                'name': 'string',
                'datasetGroupArn': 'string',
                'status': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1),
                'failureReason': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    DELETE PENDING
    
    """
    pass

def list_dataset_import_jobs(datasetArn=None, nextToken=None, maxResults=None):
    """
    Returns a list of dataset import jobs that use the given dataset. When a dataset is not specified, all the dataset import jobs associated with the account are listed. The response provides the properties for each dataset import job, including the Amazon Resource Name (ARN). For more information on dataset import jobs, see  CreateDatasetImportJob . For more information on datasets, see  CreateDataset .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_dataset_import_jobs(
        datasetArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type datasetArn: string
    :param datasetArn: The Amazon Resource Name (ARN) of the dataset to list the dataset import jobs for.

    :type nextToken: string
    :param nextToken: A token returned from the previous call to ListDatasetImportJobs for getting the next set of dataset import jobs (if they exist).

    :type maxResults: integer
    :param maxResults: The maximum number of dataset import jobs to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'datasetImportJobs': [
        {
            'datasetImportJobArn': 'string',
            'jobName': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'failureReason': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

datasetImportJobs (list) --
The list of dataset import jobs.

(dict) --
Provides a summary of the properties of a dataset import job. For a complete listing, call the  DescribeDatasetImportJob API.

datasetImportJobArn (string) --
The Amazon Resource Name (ARN) of the dataset import job.

jobName (string) --
The name of the dataset import job.

status (string) --
The status of the dataset import job.
A dataset import job can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED


creationDateTime (datetime) --
The date and time (in Unix time) that the dataset import job was created.

lastUpdatedDateTime (datetime) --
The date and time (in Unix time) that the dataset was last updated.

failureReason (string) --
If a dataset import job fails, the reason behind the failure.





nextToken (string) --
A token for getting the next set of dataset import jobs (if they exist).







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.InvalidNextTokenException


    :return: {
        'datasetImportJobs': [
            {
                'datasetImportJobArn': 'string',
                'jobName': 'string',
                'status': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1),
                'failureReason': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    
    """
    pass

def list_datasets(datasetGroupArn=None, nextToken=None, maxResults=None):
    """
    Returns the list of datasets contained in the given dataset group. The response provides the properties for each dataset, including the Amazon Resource Name (ARN). For more information on datasets, see  CreateDataset .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_datasets(
        datasetGroupArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type datasetGroupArn: string
    :param datasetGroupArn: The Amazon Resource Name (ARN) of the dataset group that contains the datasets to list.

    :type nextToken: string
    :param nextToken: A token returned from the previous call to ListDatasetImportJobs for getting the next set of dataset import jobs (if they exist).

    :type maxResults: integer
    :param maxResults: The maximum number of datasets to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'datasets': [
        {
            'name': 'string',
            'datasetArn': 'string',
            'datasetType': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

datasets (list) --
An array of Dataset objects. Each object provides metadata information.

(dict) --
Provides a summary of the properties of a dataset. For a complete listing, call the  DescribeDataset API.

name (string) --
The name of the dataset.

datasetArn (string) --
The Amazon Resource Name (ARN) of the dataset.

datasetType (string) --
The dataset type. One of the following values:

Interactions
Items
Users
Event-Interactions


status (string) --
The status of the dataset.
A dataset can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING > DELETE IN_PROGRESS


creationDateTime (datetime) --
The date and time (in Unix time) that the dataset was created.

lastUpdatedDateTime (datetime) --
The date and time (in Unix time) that the dataset was last updated.





nextToken (string) --
A token for getting the next set of datasets (if they exist).







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.InvalidNextTokenException


    :return: {
        'datasets': [
            {
                'name': 'string',
                'datasetArn': 'string',
                'datasetType': 'string',
                'status': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Interactions
    Items
    Users
    Event-Interactions
    
    """
    pass

def list_event_trackers(datasetGroupArn=None, nextToken=None, maxResults=None):
    """
    Returns the list of event trackers associated with the account. The response provides the properties for each event tracker, including the Amazon Resource Name (ARN) and tracking ID. For more information on event trackers, see  CreateEventTracker .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_event_trackers(
        datasetGroupArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type datasetGroupArn: string
    :param datasetGroupArn: The ARN of a dataset group used to filter the response.

    :type nextToken: string
    :param nextToken: A token returned from the previous call to ListEventTrackers for getting the next set of event trackers (if they exist).

    :type maxResults: integer
    :param maxResults: The maximum number of event trackers to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'eventTrackers': [
        {
            'name': 'string',
            'eventTrackerArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

eventTrackers (list) --
A list of event trackers.

(dict) --
Provides a summary of the properties of an event tracker. For a complete listing, call the  DescribeEventTracker API.

name (string) --
The name of the event tracker.

eventTrackerArn (string) --
The Amazon Resource Name (ARN) of the event tracker.

status (string) --
The status of the event tracker.
An event tracker can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING > DELETE IN_PROGRESS


creationDateTime (datetime) --
The date and time (in Unix time) that the event tracker was created.

lastUpdatedDateTime (datetime) --
The date and time (in Unix time) that the event tracker was last updated.





nextToken (string) --
A token for getting the next set of event trackers (if they exist).







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.InvalidNextTokenException


    :return: {
        'eventTrackers': [
            {
                'name': 'string',
                'eventTrackerArn': 'string',
                'status': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    DELETE PENDING > DELETE IN_PROGRESS
    
    """
    pass

def list_recipes(recipeProvider=None, nextToken=None, maxResults=None):
    """
    Returns a list of available recipes. The response provides the properties for each recipe, including the recipe\'s Amazon Resource Name (ARN).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_recipes(
        recipeProvider='SERVICE',
        nextToken='string',
        maxResults=123
    )
    
    
    :type recipeProvider: string
    :param recipeProvider: The default is SERVICE .

    :type nextToken: string
    :param nextToken: A token returned from the previous call to ListRecipes for getting the next set of recipes (if they exist).

    :type maxResults: integer
    :param maxResults: The maximum number of recipes to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'recipes': [
        {
            'name': 'string',
            'recipeArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

recipes (list) --
The list of available recipes.

(dict) --
Provides a summary of the properties of a recipe. For a complete listing, call the  DescribeRecipe API.

name (string) --
The name of the recipe.

recipeArn (string) --
The Amazon Resource Name (ARN) of the recipe.

status (string) --
The status of the recipe.

creationDateTime (datetime) --
The date and time (in Unix time) that the recipe was created.

lastUpdatedDateTime (datetime) --
The date and time (in Unix time) that the recipe was last updated.





nextToken (string) --
A token for getting the next set of recipes.







Exceptions

Personalize.Client.exceptions.InvalidNextTokenException


    :return: {
        'recipes': [
            {
                'name': 'string',
                'recipeArn': 'string',
                'status': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Personalize.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def list_schemas(nextToken=None, maxResults=None):
    """
    Returns the list of schemas associated with the account. The response provides the properties for each schema, including the Amazon Resource Name (ARN). For more information on schemas, see  CreateSchema .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_schemas(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: A token returned from the previous call to ListSchemas for getting the next set of schemas (if they exist).

    :type maxResults: integer
    :param maxResults: The maximum number of schemas to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'schemas': [
        {
            'name': 'string',
            'schemaArn': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

schemas (list) --
A list of schemas.

(dict) --
Provides a summary of the properties of a dataset schema. For a complete listing, call the  DescribeSchema API.

name (string) --
The name of the schema.

schemaArn (string) --
The Amazon Resource Name (ARN) of the schema.

creationDateTime (datetime) --
The date and time (in Unix time) that the schema was created.

lastUpdatedDateTime (datetime) --
The date and time (in Unix time) that the schema was last updated.





nextToken (string) --
A token used to get the next set of schemas (if they exist).







Exceptions

Personalize.Client.exceptions.InvalidNextTokenException


    :return: {
        'schemas': [
            {
                'name': 'string',
                'schemaArn': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Personalize.Client.exceptions.InvalidNextTokenException
    
    """
    pass

def list_solution_versions(solutionArn=None, nextToken=None, maxResults=None):
    """
    Returns a list of solution versions for the given solution. When a solution is not specified, all the solution versions associated with the account are listed. The response provides the properties for each solution version, including the Amazon Resource Name (ARN). For more information on solutions, see  CreateSolution .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_solution_versions(
        solutionArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type solutionArn: string
    :param solutionArn: The Amazon Resource Name (ARN) of the solution.

    :type nextToken: string
    :param nextToken: A token returned from the previous call to ListSolutionVersions for getting the next set of solution versions (if they exist).

    :type maxResults: integer
    :param maxResults: The maximum number of solution versions to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'solutionVersions': [
        {
            'solutionVersionArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1),
            'failureReason': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

solutionVersions (list) --
A list of solution versions describing the version properties.

(dict) --
Provides a summary of the properties of a solution version. For a complete listing, call the  DescribeSolutionVersion API.

solutionVersionArn (string) --
The Amazon Resource Name (ARN) of the solution version.

status (string) --
The status of the solution version.
A solution version can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED


creationDateTime (datetime) --
The date and time (in Unix time) that this version of a solution was created.

lastUpdatedDateTime (datetime) --
The date and time (in Unix time) that the solution version was last updated.

failureReason (string) --
If a solution version fails, the reason behind the failure.





nextToken (string) --
A token for getting the next set of solution versions (if they exist).







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException
Personalize.Client.exceptions.InvalidNextTokenException


    :return: {
        'solutionVersions': [
            {
                'solutionVersionArn': 'string',
                'status': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1),
                'failureReason': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    
    """
    pass

def list_solutions(datasetGroupArn=None, nextToken=None, maxResults=None):
    """
    Returns a list of solutions that use the given dataset group. When a dataset group is not specified, all the solutions associated with the account are listed. The response provides the properties for each solution, including the Amazon Resource Name (ARN). For more information on solutions, see  CreateSolution .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_solutions(
        datasetGroupArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type datasetGroupArn: string
    :param datasetGroupArn: The Amazon Resource Name (ARN) of the dataset group.

    :type nextToken: string
    :param nextToken: A token returned from the previous call to ListSolutions for getting the next set of solutions (if they exist).

    :type maxResults: integer
    :param maxResults: The maximum number of solutions to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'solutions': [
        {
            'name': 'string',
            'solutionArn': 'string',
            'status': 'string',
            'creationDateTime': datetime(2015, 1, 1),
            'lastUpdatedDateTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

solutions (list) --
A list of the current solutions.

(dict) --
Provides a summary of the properties of a solution. For a complete listing, call the  DescribeSolution API.

name (string) --
The name of the solution.

solutionArn (string) --
The Amazon Resource Name (ARN) of the solution.

status (string) --
The status of the solution.
A solution can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
DELETE PENDING > DELETE IN_PROGRESS


creationDateTime (datetime) --
The date and time (in Unix time) that the solution was created.

lastUpdatedDateTime (datetime) --
The date and time (in Unix time) that the solution was last updated.





nextToken (string) --
A token for getting the next set of solutions (if they exist).







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.InvalidNextTokenException


    :return: {
        'solutions': [
            {
                'name': 'string',
                'solutionArn': 'string',
                'status': 'string',
                'creationDateTime': datetime(2015, 1, 1),
                'lastUpdatedDateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    DELETE PENDING > DELETE IN_PROGRESS
    
    """
    pass

def update_campaign(campaignArn=None, solutionVersionArn=None, minProvisionedTPS=None):
    """
    Updates a campaign by either deploying a new solution or changing the value of the campaign\'s minProvisionedTPS parameter.
    To update a campaign, the campaign status must be ACTIVE or CREATE FAILED. Check the campaign status using the  DescribeCampaign API.
    For more information on campaigns, see  CreateCampaign .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_campaign(
        campaignArn='string',
        solutionVersionArn='string',
        minProvisionedTPS=123
    )
    
    
    :type campaignArn: string
    :param campaignArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the campaign.\n

    :type solutionVersionArn: string
    :param solutionVersionArn: The ARN of a new solution version to deploy.

    :type minProvisionedTPS: integer
    :param minProvisionedTPS: Specifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support.

    :rtype: dict

ReturnsResponse Syntax
{
    'campaignArn': 'string'
}


Response Structure

(dict) --

campaignArn (string) --
The same campaign ARN as given in the request.







Exceptions

Personalize.Client.exceptions.InvalidInputException
Personalize.Client.exceptions.ResourceNotFoundException
Personalize.Client.exceptions.ResourceInUseException


    :return: {
        'campaignArn': 'string'
    }
    
    
    :returns: 
    Personalize.Client.exceptions.InvalidInputException
    Personalize.Client.exceptions.ResourceNotFoundException
    Personalize.Client.exceptions.ResourceInUseException
    
    """
    pass

