"""
The MIT License (MIT)

Copyright (c) 2016 Gehad Shaat

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
"""


def add_tags(Tags=None, ResourceId=None, ResourceType=None):
    """
    :param Tags: [REQUIRED]
            The key-value pairs to use to create tags. If you specify a key without specifying a value, Amazon ML creates a tag with the specified key and a value of null.
            (dict) --A custom key-value pair associated with an ML object, such as an ML model.
            Key (string) --A unique identifier for the tag. Valid characters include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.
            Value (string) --An optional string, typically used to describe or define the tag. Valid characters include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.
            
            
    :type Tags: list
    :param ResourceId: [REQUIRED]
            The ID of the ML object to tag. For example, exampleModelId .
            
    :type ResourceId: string
    :param ResourceType: [REQUIRED]
            The type of the ML object to tag.
            
    :type ResourceType: string
    """
    pass


def can_paginate(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            ReturnsTrue if the operation can be paginated,
            False otherwise.
            
    :type operation_name: string
    """
    pass


def create_batch_prediction(BatchPredictionId=None, BatchPredictionName=None, MLModelId=None,
                            BatchPredictionDataSourceId=None, OutputUri=None):
    """
    :param BatchPredictionId: [REQUIRED]
            A user-supplied ID that uniquely identifies the BatchPrediction .
            
    :type BatchPredictionId: string
    :param BatchPredictionName: A user-supplied name or description of the BatchPrediction . BatchPredictionName can only use the UTF-8 character set.
    :type BatchPredictionName: string
    :param MLModelId: [REQUIRED]
            The ID of the MLModel that will generate predictions for the group of observations.
            
    :type MLModelId: string
    :param BatchPredictionDataSourceId: [REQUIRED]
            The ID of the DataSource that points to the group of observations to predict.
            
    :type BatchPredictionDataSourceId: string
    :param OutputUri: [REQUIRED]
            The location of an Amazon Simple Storage Service (Amazon S3) bucket or directory to store the batch prediction results. The following substrings are not allowed in the s3 key portion of the outputURI field: ':', '//', '/./', '/../'.
            Amazon ML needs permissions to store and retrieve the logs on your behalf. For information about how to set permissions, see the Amazon Machine Learning Developer Guide .
            
    :type OutputUri: string
    """
    pass


def create_data_source_from_rds(DataSourceId=None, DataSourceName=None, RDSData=None, RoleARN=None,
                                ComputeStatistics=None):
    """
    :param DataSourceId: [REQUIRED]
            A user-supplied ID that uniquely identifies the DataSource . Typically, an Amazon Resource Number (ARN) becomes the ID for a DataSource .
            
    :type DataSourceId: string
    :param DataSourceName: A user-supplied name or description of the DataSource .
    :type DataSourceName: string
    :param RDSData: [REQUIRED]
            The data specification of an Amazon RDS DataSource :
            DatabaseInformation -
            DatabaseName - The name of the Amazon RDS database.
            InstanceIdentifier - A unique identifier for the Amazon RDS database instance.
            DatabaseCredentials - AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon RDS database.
            ResourceRole - A role (DataPipelineDefaultResourceRole) assumed by an EC2 instance to carry out the copy task from Amazon RDS to Amazon Simple Storage Service (Amazon S3). For more information, see Role templates for data pipelines.
            ServiceRole - A role (DataPipelineDefaultRole) assumed by the AWS Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see Role templates for data pipelines.
            SecurityInfo - The security information to use to access an RDS DB instance. You need to set up appropriate ingress rules for the security entity IDs provided to allow access to the Amazon RDS instance. Specify a [SubnetId , SecurityGroupIds ] pair for a VPC-based RDS DB instance.
            SelectSqlQuery - A query that is used to retrieve the observation data for the Datasource .
            S3StagingLocation - The Amazon S3 location for staging Amazon RDS data. The data retrieved from Amazon RDS using SelectSqlQuery is stored in this location.
            DataSchemaUri - The Amazon S3 location of the DataSchema .
            DataSchema - A JSON string representing the schema. This is not required if DataSchemaUri is specified.
            DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the Datasource .  Sample - '{\'splitting\':{\'percentBegin\':10,\'percentEnd\':60}}'
            DatabaseInformation (dict) -- [REQUIRED]Describes the DatabaseName and InstanceIdentifier of an Amazon RDS database.
            InstanceIdentifier (string) -- [REQUIRED]The ID of an RDS DB instance.
            DatabaseName (string) -- [REQUIRED]The name of a database hosted on an RDS DB instance.
            SelectSqlQuery (string) -- [REQUIRED]The query that is used to retrieve the observation data for the DataSource .
            DatabaseCredentials (dict) -- [REQUIRED]The AWS Identity and Access Management (IAM) credentials that are used connect to the Amazon RDS database.
            Username (string) -- [REQUIRED]The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an RDSSelectSqlQuery query.
            Password (string) -- [REQUIRED]The password to be used by Amazon ML to connect to a database on an RDS DB instance. The password should have sufficient permissions to execute the RDSSelectQuery query.
            S3StagingLocation (string) -- [REQUIRED]The Amazon S3 location for staging Amazon RDS data. The data retrieved from Amazon RDS using SelectSqlQuery is stored in this location.
            DataRearrangement (string) --A JSON string that represents the splitting and rearrangement processing to be applied to a DataSource . If the DataRearrangement parameter is not provided, all of the input data is used to create the Datasource .
            There are multiple parameters that control what data is used to create a datasource:
            ``percentBegin`` Use percentBegin to indicate the beginning of the range of the data used to create the Datasource. If you do not include percentBegin and percentEnd , Amazon ML includes all of the data when creating the datasource.
            ``percentEnd`` Use percentEnd to indicate the end of the range of the data used to create the Datasource. If you do not include percentBegin and percentEnd , Amazon ML includes all of the data when creating the datasource.
            ``complement`` The complement parameter instructs Amazon ML to use the data that is not included in the range of percentBegin to percentEnd to create a datasource. The complement parameter is useful if you need to create complementary datasources for training and evaluation. To create a complementary datasource, use the same values for percentBegin and percentEnd , along with the complement parameter. For example, the following two datasources do not share any data, and can be used to train and evaluate a model. The first datasource has 25 percent of the data, and the second one has 75 percent of the data. Datasource for evaluation: {'splitting':{'percentBegin':0, 'percentEnd':25}} Datasource for training: {'splitting':{'percentBegin':0, 'percentEnd':25, 'complement':'true'}}
            ``strategy`` To change how Amazon ML splits the data for a datasource, use the strategy parameter. The default value for the strategy parameter is sequential , meaning that Amazon ML takes all of the data records between the percentBegin and percentEnd parameters for the datasource, in the order that the records appear in the input data. The following two DataRearrangement lines are examples of sequentially ordered training and evaluation datasources: Datasource for evaluation: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'sequential'}} Datasource for training: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'sequential', 'complement':'true'}} To randomly split the input data into the proportions indicated by the percentBegin and percentEnd parameters, set the strategy parameter to random and provide a string that is used as the seed value for the random data splitting (for example, you can use the S3 path to your data as the random seed string). If you choose the random split strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then selects the rows that have an assigned number between percentBegin and percentEnd . Pseudo-random numbers are assigned using both the input seed string value and the byte offset as a seed, so changing the data results in a different split. Any existing ordering is preserved. The random splitting strategy ensures that variables in the training and evaluation data are distributed similarly. It is useful in the cases where the input data may have an implicit sort order, which would otherwise result in training and evaluation datasources containing non-similar data records. The following two DataRearrangement lines are examples of non-sequentially ordered training and evaluation datasources: Datasource for evaluation: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'random', 'randomSeed'='s3://my_s3_path/bucket/file.csv'}} Datasource for training: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'random', 'randomSeed'='s3://my_s3_path/bucket/file.csv', 'complement':'true'}}
            DataSchema (string) --A JSON string that represents the schema for an Amazon RDS DataSource . The DataSchema defines the structure of the observation data in the data file(s) referenced in the DataSource .
            A DataSchema is not required if you specify a DataSchemaUri
            Define your DataSchema as a series of key-value pairs. attributes and excludedVariableNames have an array of key-value pairs for their value. Use the following format to define your DataSchema .
            { 'version': '1.0',
            'recordAnnotationFieldName': 'F1',
            'recordWeightFieldName': 'F2',
            'targetFieldName': 'F3',
            'dataFormat': 'CSV',
            'dataFileContainsHeader': true,
            'attributes': [
            { 'fieldName': 'F1', 'fieldType': 'TEXT' }, { 'fieldName': 'F2', 'fieldType': 'NUMERIC' }, { 'fieldName': 'F3', 'fieldType': 'CATEGORICAL' }, { 'fieldName': 'F4', 'fieldType': 'NUMERIC' }, { 'fieldName': 'F5', 'fieldType': 'CATEGORICAL' }, { 'fieldName': 'F6', 'fieldType': 'TEXT' }, { 'fieldName': 'F7', 'fieldType': 'WEIGHTED_INT_SEQUENCE' }, { 'fieldName': 'F8', 'fieldType': 'WEIGHTED_STRING_SEQUENCE' } ],
            'excludedVariableNames': [ 'F6' ] }
            DataSchemaUri (string) --The Amazon S3 location of the DataSchema .
            ResourceRole (string) -- [REQUIRED]The role (DataPipelineDefaultResourceRole) assumed by an Amazon Elastic Compute Cloud (Amazon EC2) instance to carry out the copy operation from Amazon RDS to an Amazon S3 task. For more information, see Role templates for data pipelines.
            ServiceRole (string) -- [REQUIRED]The role (DataPipelineDefaultRole) assumed by AWS Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see Role templates for data pipelines.
            SubnetId (string) -- [REQUIRED]The subnet ID to be used to access a VPC-based RDS DB instance. This attribute is used by Data Pipeline to carry out the copy task from Amazon RDS to Amazon S3.
            SecurityGroupIds (list) -- [REQUIRED]The security group IDs to be used to access a VPC-based RDS DB instance. Ensure that there are appropriate ingress rules set up to allow access to the RDS DB instance. This attribute is used by Data Pipeline to carry out the copy operation from Amazon RDS to an Amazon S3 task.
            (string) --
            
    :type RDSData: dict
    :param RoleARN: [REQUIRED]
            The role that Amazon ML assumes on behalf of the user to create and activate a data pipeline in the user's account and copy data using the SelectSqlQuery query from Amazon RDS to Amazon S3.
            
    :type RoleARN: string
    :param ComputeStatistics: The compute statistics for a DataSource . The statistics are generated from the observation data referenced by a DataSource . Amazon ML uses the statistics internally during MLModel training. This parameter must be set to true if the ```` DataSource```` needs to be used for MLModel training.
    :type ComputeStatistics: boolean
    """
    pass


def create_data_source_from_redshift(DataSourceId=None, DataSourceName=None, DataSpec=None, RoleARN=None,
                                     ComputeStatistics=None):
    """
    :param DataSourceId: [REQUIRED]
            A user-supplied ID that uniquely identifies the DataSource .
            
    :type DataSourceId: string
    :param DataSourceName: A user-supplied name or description of the DataSource .
    :type DataSourceName: string
    :param DataSpec: [REQUIRED]
            The data specification of an Amazon Redshift DataSource :
            DatabaseInformation -
            DatabaseName - The name of the Amazon Redshift database.
            ClusterIdentifier - The unique ID for the Amazon Redshift cluster.
            DatabaseCredentials - The AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon Redshift database.
            SelectSqlQuery - The query that is used to retrieve the observation data for the Datasource .
            S3StagingLocation - The Amazon Simple Storage Service (Amazon S3) location for staging Amazon Redshift data. The data retrieved from Amazon Redshift using the SelectSqlQuery query is stored in this location.
            DataSchemaUri - The Amazon S3 location of the DataSchema .
            DataSchema - A JSON string representing the schema. This is not required if DataSchemaUri is specified.
            DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the DataSource . Sample - '{\'splitting\':{\'percentBegin\':10,\'percentEnd\':60}}'
            DatabaseInformation (dict) -- [REQUIRED]Describes the DatabaseName and ClusterIdentifier for an Amazon Redshift DataSource .
            DatabaseName (string) -- [REQUIRED]The name of a database hosted on an Amazon Redshift cluster.
            ClusterIdentifier (string) -- [REQUIRED]The ID of an Amazon Redshift cluster.
            SelectSqlQuery (string) -- [REQUIRED]Describes the SQL Query to execute on an Amazon Redshift database for an Amazon Redshift DataSource .
            DatabaseCredentials (dict) -- [REQUIRED]Describes AWS Identity and Access Management (IAM) credentials that are used connect to the Amazon Redshift database.
            Username (string) -- [REQUIRED]A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the RedshiftSelectSqlQuery query. The username should be valid for an Amazon Redshift USER .
            Password (string) -- [REQUIRED]A password to be used by Amazon ML to connect to a database on an Amazon Redshift cluster. The password should have sufficient permissions to execute a RedshiftSelectSqlQuery query. The password should be valid for an Amazon Redshift USER .
            S3StagingLocation (string) -- [REQUIRED]Describes an Amazon S3 location to store the result set of the SelectSqlQuery query.
            DataRearrangement (string) --A JSON string that represents the splitting and rearrangement processing to be applied to a DataSource . If the DataRearrangement parameter is not provided, all of the input data is used to create the Datasource .
            There are multiple parameters that control what data is used to create a datasource:
            ``percentBegin`` Use percentBegin to indicate the beginning of the range of the data used to create the Datasource. If you do not include percentBegin and percentEnd , Amazon ML includes all of the data when creating the datasource.
            ``percentEnd`` Use percentEnd to indicate the end of the range of the data used to create the Datasource. If you do not include percentBegin and percentEnd , Amazon ML includes all of the data when creating the datasource.
            ``complement`` The complement parameter instructs Amazon ML to use the data that is not included in the range of percentBegin to percentEnd to create a datasource. The complement parameter is useful if you need to create complementary datasources for training and evaluation. To create a complementary datasource, use the same values for percentBegin and percentEnd , along with the complement parameter. For example, the following two datasources do not share any data, and can be used to train and evaluate a model. The first datasource has 25 percent of the data, and the second one has 75 percent of the data. Datasource for evaluation: {'splitting':{'percentBegin':0, 'percentEnd':25}} Datasource for training: {'splitting':{'percentBegin':0, 'percentEnd':25, 'complement':'true'}}
            ``strategy`` To change how Amazon ML splits the data for a datasource, use the strategy parameter. The default value for the strategy parameter is sequential , meaning that Amazon ML takes all of the data records between the percentBegin and percentEnd parameters for the datasource, in the order that the records appear in the input data. The following two DataRearrangement lines are examples of sequentially ordered training and evaluation datasources: Datasource for evaluation: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'sequential'}} Datasource for training: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'sequential', 'complement':'true'}} To randomly split the input data into the proportions indicated by the percentBegin and percentEnd parameters, set the strategy parameter to random and provide a string that is used as the seed value for the random data splitting (for example, you can use the S3 path to your data as the random seed string). If you choose the random split strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then selects the rows that have an assigned number between percentBegin and percentEnd . Pseudo-random numbers are assigned using both the input seed string value and the byte offset as a seed, so changing the data results in a different split. Any existing ordering is preserved. The random splitting strategy ensures that variables in the training and evaluation data are distributed similarly. It is useful in the cases where the input data may have an implicit sort order, which would otherwise result in training and evaluation datasources containing non-similar data records. The following two DataRearrangement lines are examples of non-sequentially ordered training and evaluation datasources: Datasource for evaluation: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'random', 'randomSeed'='s3://my_s3_path/bucket/file.csv'}} Datasource for training: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'random', 'randomSeed'='s3://my_s3_path/bucket/file.csv', 'complement':'true'}}
            DataSchema (string) --A JSON string that represents the schema for an Amazon Redshift DataSource . The DataSchema defines the structure of the observation data in the data file(s) referenced in the DataSource .
            A DataSchema is not required if you specify a DataSchemaUri .
            Define your DataSchema as a series of key-value pairs. attributes and excludedVariableNames have an array of key-value pairs for their value. Use the following format to define your DataSchema .
            { 'version': '1.0',
            'recordAnnotationFieldName': 'F1',
            'recordWeightFieldName': 'F2',
            'targetFieldName': 'F3',
            'dataFormat': 'CSV',
            'dataFileContainsHeader': true,
            'attributes': [
            { 'fieldName': 'F1', 'fieldType': 'TEXT' }, { 'fieldName': 'F2', 'fieldType': 'NUMERIC' }, { 'fieldName': 'F3', 'fieldType': 'CATEGORICAL' }, { 'fieldName': 'F4', 'fieldType': 'NUMERIC' }, { 'fieldName': 'F5', 'fieldType': 'CATEGORICAL' }, { 'fieldName': 'F6', 'fieldType': 'TEXT' }, { 'fieldName': 'F7', 'fieldType': 'WEIGHTED_INT_SEQUENCE' }, { 'fieldName': 'F8', 'fieldType': 'WEIGHTED_STRING_SEQUENCE' } ],
            'excludedVariableNames': [ 'F6' ] }
            DataSchemaUri (string) --Describes the schema location for an Amazon Redshift DataSource .
            
    :type DataSpec: dict
    :param RoleARN: [REQUIRED]
            A fully specified role Amazon Resource Name (ARN). Amazon ML assumes the role on behalf of the user to create the following:
            A security group to allow Amazon ML to execute the SelectSqlQuery query on an Amazon Redshift cluster
            An Amazon S3 bucket policy to grant Amazon ML read/write permissions on the S3StagingLocation
            
    :type RoleARN: string
    :param ComputeStatistics: The compute statistics for a DataSource . The statistics are generated from the observation data referenced by a DataSource . Amazon ML uses the statistics internally during MLModel training. This parameter must be set to true if the DataSource needs to be used for MLModel training.
    :type ComputeStatistics: boolean
    """
    pass


def create_data_source_from_s3(DataSourceId=None, DataSourceName=None, DataSpec=None, ComputeStatistics=None):
    """
    :param DataSourceId: [REQUIRED]
            A user-supplied identifier that uniquely identifies the DataSource .
            
    :type DataSourceId: string
    :param DataSourceName: A user-supplied name or description of the DataSource .
    :type DataSourceName: string
    :param DataSpec: [REQUIRED]
            The data specification of a DataSource :
            DataLocationS3 - The Amazon S3 location of the observation data.
            DataSchemaLocationS3 - The Amazon S3 location of the DataSchema .
            DataSchema - A JSON string representing the schema. This is not required if DataSchemaUri is specified.
            DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the Datasource . Sample - '{\'splitting\':{\'percentBegin\':10,\'percentEnd\':60}}'
            DataLocationS3 (string) -- [REQUIRED]The location of the data file(s) used by a DataSource . The URI specifies a data file or an Amazon Simple Storage Service (Amazon S3) directory or bucket containing data files.
            DataRearrangement (string) --A JSON string that represents the splitting and rearrangement processing to be applied to a DataSource . If the DataRearrangement parameter is not provided, all of the input data is used to create the Datasource .
            There are multiple parameters that control what data is used to create a datasource:
            ``percentBegin`` Use percentBegin to indicate the beginning of the range of the data used to create the Datasource. If you do not include percentBegin and percentEnd , Amazon ML includes all of the data when creating the datasource.
            ``percentEnd`` Use percentEnd to indicate the end of the range of the data used to create the Datasource. If you do not include percentBegin and percentEnd , Amazon ML includes all of the data when creating the datasource.
            ``complement`` The complement parameter instructs Amazon ML to use the data that is not included in the range of percentBegin to percentEnd to create a datasource. The complement parameter is useful if you need to create complementary datasources for training and evaluation. To create a complementary datasource, use the same values for percentBegin and percentEnd , along with the complement parameter. For example, the following two datasources do not share any data, and can be used to train and evaluate a model. The first datasource has 25 percent of the data, and the second one has 75 percent of the data. Datasource for evaluation: {'splitting':{'percentBegin':0, 'percentEnd':25}} Datasource for training: {'splitting':{'percentBegin':0, 'percentEnd':25, 'complement':'true'}}
            ``strategy`` To change how Amazon ML splits the data for a datasource, use the strategy parameter. The default value for the strategy parameter is sequential , meaning that Amazon ML takes all of the data records between the percentBegin and percentEnd parameters for the datasource, in the order that the records appear in the input data. The following two DataRearrangement lines are examples of sequentially ordered training and evaluation datasources: Datasource for evaluation: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'sequential'}} Datasource for training: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'sequential', 'complement':'true'}} To randomly split the input data into the proportions indicated by the percentBegin and percentEnd parameters, set the strategy parameter to random and provide a string that is used as the seed value for the random data splitting (for example, you can use the S3 path to your data as the random seed string). If you choose the random split strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then selects the rows that have an assigned number between percentBegin and percentEnd . Pseudo-random numbers are assigned using both the input seed string value and the byte offset as a seed, so changing the data results in a different split. Any existing ordering is preserved. The random splitting strategy ensures that variables in the training and evaluation data are distributed similarly. It is useful in the cases where the input data may have an implicit sort order, which would otherwise result in training and evaluation datasources containing non-similar data records. The following two DataRearrangement lines are examples of non-sequentially ordered training and evaluation datasources: Datasource for evaluation: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'random', 'randomSeed'='s3://my_s3_path/bucket/file.csv'}} Datasource for training: {'splitting':{'percentBegin':70, 'percentEnd':100, 'strategy':'random', 'randomSeed'='s3://my_s3_path/bucket/file.csv', 'complement':'true'}}
            DataSchema (string) --A JSON string that represents the schema for an Amazon S3 DataSource . The DataSchema defines the structure of the observation data in the data file(s) referenced in the DataSource .
            You must provide either the DataSchema or the DataSchemaLocationS3 .
            Define your DataSchema as a series of key-value pairs. attributes and excludedVariableNames have an array of key-value pairs for their value. Use the following format to define your DataSchema .
            { 'version': '1.0',
            'recordAnnotationFieldName': 'F1',
            'recordWeightFieldName': 'F2',
            'targetFieldName': 'F3',
            'dataFormat': 'CSV',
            'dataFileContainsHeader': true,
            'attributes': [
            { 'fieldName': 'F1', 'fieldType': 'TEXT' }, { 'fieldName': 'F2', 'fieldType': 'NUMERIC' }, { 'fieldName': 'F3', 'fieldType': 'CATEGORICAL' }, { 'fieldName': 'F4', 'fieldType': 'NUMERIC' }, { 'fieldName': 'F5', 'fieldType': 'CATEGORICAL' }, { 'fieldName': 'F6', 'fieldType': 'TEXT' }, { 'fieldName': 'F7', 'fieldType': 'WEIGHTED_INT_SEQUENCE' }, { 'fieldName': 'F8', 'fieldType': 'WEIGHTED_STRING_SEQUENCE' } ],
            'excludedVariableNames': [ 'F6' ] }
            DataSchemaLocationS3 (string) --Describes the schema location in Amazon S3. You must provide either the DataSchema or the DataSchemaLocationS3 .
            
    :type DataSpec: dict
    :param ComputeStatistics: The compute statistics for a DataSource . The statistics are generated from the observation data referenced by a DataSource . Amazon ML uses the statistics internally during MLModel training. This parameter must be set to true if the ```` DataSource```` needs to be used for MLModel training.
    :type ComputeStatistics: boolean
    """
    pass


def create_evaluation(EvaluationId=None, EvaluationName=None, MLModelId=None, EvaluationDataSourceId=None):
    """
    :param EvaluationId: [REQUIRED]
            A user-supplied ID that uniquely identifies the Evaluation .
            
    :type EvaluationId: string
    :param EvaluationName: A user-supplied name or description of the Evaluation .
    :type EvaluationName: string
    :param MLModelId: [REQUIRED]
            The ID of the MLModel to evaluate.
            The schema used in creating the MLModel must match the schema of the DataSource used in the Evaluation .
            
    :type MLModelId: string
    :param EvaluationDataSourceId: [REQUIRED]
            The ID of the DataSource for the evaluation. The schema of the DataSource must match the schema used to create the MLModel .
            
    :type EvaluationDataSourceId: string
    """
    pass


def create_ml_model(MLModelId=None, MLModelName=None, MLModelType=None, Parameters=None, TrainingDataSourceId=None,
                    Recipe=None, RecipeUri=None):
    """
    :param MLModelId: [REQUIRED]
            A user-supplied ID that uniquely identifies the MLModel .
            
    :type MLModelId: string
    :param MLModelName: A user-supplied name or description of the MLModel .
    :type MLModelName: string
    :param MLModelType: [REQUIRED]
            The category of supervised learning that this MLModel will address. Choose from the following types:
            Choose REGRESSION if the MLModel will be used to predict a numeric value.
            Choose BINARY if the MLModel result has two possible values.
            Choose MULTICLASS if the MLModel result has a limited number of values.
            For more information, see the Amazon Machine Learning Developer Guide .
            
    :type MLModelType: string
    :param Parameters: A list of the training parameters in the MLModel . The list is implemented as a map of key-value pairs.
            The following is the current set of training parameters:
            sgd.maxMLModelSizeInBytes - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance. The value is an integer that ranges from 100000 to 2147483648 . The default value is 33554432 .
            sgd.maxPasses - The number of times that the training process traverses the observations to build the MLModel . The value is an integer that ranges from 1 to 10000 . The default value is 10 .
            sgd.shuffleType - Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are auto and none . The default value is none . We strongly recommend that you shuffle your data.
            sgd.l1RegularizationAmount - The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as 1.0E-08 . The value is a double that ranges from 0 to MAX_DOUBLE . The default is to not use L1 normalization. This parameter can't be used when L2 is specified. Use this parameter sparingly.
            sgd.l2RegularizationAmount - The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as 1.0E-08 . The value is a double that ranges from 0 to MAX_DOUBLE . The default is to not use L2 normalization. This parameter can't be used when L1 is specified. Use this parameter sparingly.
            (string) --String type.
            (string) --String type.
            
            
    :type Parameters: dict
    :param TrainingDataSourceId: [REQUIRED]
            The DataSource that points to the training data.
            
    :type TrainingDataSourceId: string
    :param Recipe: The data recipe for creating the MLModel . You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.
    :type Recipe: string
    :param RecipeUri: The Amazon Simple Storage Service (Amazon S3) location and file name that contains the MLModel recipe. You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.
    :type RecipeUri: string
    """
    pass


def create_realtime_endpoint(MLModelId=None):
    """
    :param MLModelId: [REQUIRED]
            The ID assigned to the MLModel during creation.
            Return typedict
            ReturnsResponse Syntax{
              'MLModelId': 'string',
              'RealtimeEndpointInfo': {
                'PeakRequestsPerSecond': 123,
                'CreatedAt': datetime(2015, 1, 1),
                'EndpointUrl': 'string',
                'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
              }
            }
            Response Structure
            (dict) --Represents the output of an CreateRealtimeEndpoint operation.
            The result contains the MLModelId and the endpoint information for the MLModel .
            Note
            The endpoint information includes the URI of the MLModel ; that is, the location to send online prediction requests for the specified MLModel .
            MLModelId (string) --A user-supplied ID that uniquely identifies the MLModel . This value should be identical to the value of the MLModelId in the request.
            RealtimeEndpointInfo (dict) --The endpoint information of the MLModel
            PeakRequestsPerSecond (integer) --The maximum processing rate for the real-time endpoint for MLModel , measured in incoming requests per second.
            CreatedAt (datetime) --The time that the request to create the real-time endpoint for the MLModel was received. The time is expressed in epoch time.
            EndpointUrl (string) --The URI that specifies where to send real-time prediction requests for the MLModel .
            Note
            Note
            The application must wait until the real-time endpoint is ready before using this URI.
            EndpointStatus (string) --The current status of the real-time endpoint for the MLModel . This element can have one of the following values:
            NONE - Endpoint does not exist or was previously deleted.
            READY - Endpoint is ready to be used for real-time predictions.
            UPDATING - Updating/creating the endpoint.
            
            
            
    :type MLModelId: string
    """
    pass


def delete_batch_prediction(BatchPredictionId=None):
    """
    :param BatchPredictionId: [REQUIRED]
            A user-supplied ID that uniquely identifies the BatchPrediction .
            Return typedict
            ReturnsResponse Syntax{
              'BatchPredictionId': 'string'
            }
            Response Structure
            (dict) --Represents the output of a DeleteBatchPrediction operation.
            You can use the GetBatchPrediction operation and check the value of the Status parameter to see whether a BatchPrediction is marked as DELETED .
            BatchPredictionId (string) --A user-supplied ID that uniquely identifies the BatchPrediction . This value should be identical to the value of the BatchPredictionID in the request.
            
            
    :type BatchPredictionId: string
    """
    pass


def delete_data_source(DataSourceId=None):
    """
    :param DataSourceId: [REQUIRED]
            A user-supplied ID that uniquely identifies the DataSource .
            Return typedict
            ReturnsResponse Syntax{
              'DataSourceId': 'string'
            }
            Response Structure
            (dict) --Represents the output of a DeleteDataSource operation.
            DataSourceId (string) --A user-supplied ID that uniquely identifies the DataSource . This value should be identical to the value of the DataSourceID in the request.
            
            
    :type DataSourceId: string
    """
    pass


def delete_evaluation(EvaluationId=None):
    """
    :param EvaluationId: [REQUIRED]
            A user-supplied ID that uniquely identifies the Evaluation to delete.
            Return typedict
            ReturnsResponse Syntax{
              'EvaluationId': 'string'
            }
            Response Structure
            (dict) --Represents the output of a DeleteEvaluation operation. The output indicates that Amazon Machine Learning (Amazon ML) received the request.
            You can use the GetEvaluation operation and check the value of the Status parameter to see whether an Evaluation is marked as DELETED .
            EvaluationId (string) --A user-supplied ID that uniquely identifies the Evaluation . This value should be identical to the value of the EvaluationId in the request.
            
            
    :type EvaluationId: string
    """
    pass


def delete_ml_model(MLModelId=None):
    """
    :param MLModelId: [REQUIRED]
            A user-supplied ID that uniquely identifies the MLModel .
            Return typedict
            ReturnsResponse Syntax{
              'MLModelId': 'string'
            }
            Response Structure
            (dict) --Represents the output of a DeleteMLModel operation.
            You can use the GetMLModel operation and check the value of the Status parameter to see whether an MLModel is marked as DELETED .
            MLModelId (string) --A user-supplied ID that uniquely identifies the MLModel . This value should be identical to the value of the MLModelID in the request.
            
            
    :type MLModelId: string
    """
    pass


def delete_realtime_endpoint(MLModelId=None):
    """
    :param MLModelId: [REQUIRED]
            The ID assigned to the MLModel during creation.
            Return typedict
            ReturnsResponse Syntax{
              'MLModelId': 'string',
              'RealtimeEndpointInfo': {
                'PeakRequestsPerSecond': 123,
                'CreatedAt': datetime(2015, 1, 1),
                'EndpointUrl': 'string',
                'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
              }
            }
            Response Structure
            (dict) --Represents the output of an DeleteRealtimeEndpoint operation.
            The result contains the MLModelId and the endpoint information for the MLModel .
            MLModelId (string) --A user-supplied ID that uniquely identifies the MLModel . This value should be identical to the value of the MLModelId in the request.
            RealtimeEndpointInfo (dict) --The endpoint information of the MLModel
            PeakRequestsPerSecond (integer) --The maximum processing rate for the real-time endpoint for MLModel , measured in incoming requests per second.
            CreatedAt (datetime) --The time that the request to create the real-time endpoint for the MLModel was received. The time is expressed in epoch time.
            EndpointUrl (string) --The URI that specifies where to send real-time prediction requests for the MLModel .
            Note
            Note
            The application must wait until the real-time endpoint is ready before using this URI.
            EndpointStatus (string) --The current status of the real-time endpoint for the MLModel . This element can have one of the following values:
            NONE - Endpoint does not exist or was previously deleted.
            READY - Endpoint is ready to be used for real-time predictions.
            UPDATING - Updating/creating the endpoint.
            
            
            
    :type MLModelId: string
    """
    pass


def delete_tags(TagKeys=None, ResourceId=None, ResourceType=None):
    """
    :param TagKeys: [REQUIRED]
            One or more tags to delete.
            (string) --
            
    :type TagKeys: list
    :param ResourceId: [REQUIRED]
            The ID of the tagged ML object. For example, exampleModelId .
            
    :type ResourceId: string
    :param ResourceType: [REQUIRED]
            The type of the tagged ML object.
            
    :type ResourceType: string
    """
    pass


def describe_batch_predictions(FilterVariable=None, EQ=None, GT=None, LT=None, GE=None, LE=None, NE=None, Prefix=None,
                               SortOrder=None, NextToken=None, Limit=None):
    """
    :param FilterVariable: Use one of the following variables to filter a list of BatchPrediction :
            CreatedAt - Sets the search criteria to the BatchPrediction creation date.
            Status - Sets the search criteria to the BatchPrediction status.
            Name - Sets the search criteria to the contents of the BatchPrediction **** Name .
            IAMUser - Sets the search criteria to the user account that invoked the BatchPrediction creation.
            MLModelId - Sets the search criteria to the MLModel used in the BatchPrediction .
            DataSourceId - Sets the search criteria to the DataSource used in the BatchPrediction .
            DataURI - Sets the search criteria to the data file(s) used in the BatchPrediction . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
            
    :type FilterVariable: string
    :param EQ: The equal to operator. The BatchPrediction results will have FilterVariable values that exactly match the value specified with EQ .
    :type EQ: string
    :param GT: The greater than operator. The BatchPrediction results will have FilterVariable values that are greater than the value specified with GT .
    :type GT: string
    :param LT: The less than operator. The BatchPrediction results will have FilterVariable values that are less than the value specified with LT .
    :type LT: string
    :param GE: The greater than or equal to operator. The BatchPrediction results will have FilterVariable values that are greater than or equal to the value specified with GE .
    :type GE: string
    :param LE: The less than or equal to operator. The BatchPrediction results will have FilterVariable values that are less than or equal to the value specified with LE .
    :type LE: string
    :param NE: The not equal to operator. The BatchPrediction results will have FilterVariable values not equal to the value specified with NE .
    :type NE: string
    :param Prefix: A string that is found at the beginning of a variable, such as Name or Id .
            For example, a Batch Prediction operation could have the Name 2014-09-09-HolidayGiftMailer . To search for this BatchPrediction , select Name for the FilterVariable and any of the following strings for the Prefix :
            2014-09
            2014-09-09
            2014-09-09-Holiday
            
    :type Prefix: string
    :param SortOrder: A two-value parameter that determines the sequence of the resulting list of MLModel s.
            asc - Arranges the list in ascending order (A-Z, 0-9).
            dsc - Arranges the list in descending order (Z-A, 9-0).
            Results are sorted by FilterVariable .
            
    :type SortOrder: string
    :param NextToken: An ID of the page in the paginated results.
    :type NextToken: string
    :param Limit: The number of pages of information to include in the result. The range of acceptable values is 1 through 100 . The default value is 100 .
    :type Limit: integer
    """
    pass


def describe_data_sources(FilterVariable=None, EQ=None, GT=None, LT=None, GE=None, LE=None, NE=None, Prefix=None,
                          SortOrder=None, NextToken=None, Limit=None):
    """
    :param FilterVariable: Use one of the following variables to filter a list of DataSource :
            CreatedAt - Sets the search criteria to DataSource creation dates.
            Status - Sets the search criteria to DataSource statuses.
            Name - Sets the search criteria to the contents of DataSource **** Name .
            DataUri - Sets the search criteria to the URI of data files used to create the DataSource . The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
            IAMUser - Sets the search criteria to the user account that invoked the DataSource creation.
            
    :type FilterVariable: string
    :param EQ: The equal to operator. The DataSource results will have FilterVariable values that exactly match the value specified with EQ .
    :type EQ: string
    :param GT: The greater than operator. The DataSource results will have FilterVariable values that are greater than the value specified with GT .
    :type GT: string
    :param LT: The less than operator. The DataSource results will have FilterVariable values that are less than the value specified with LT .
    :type LT: string
    :param GE: The greater than or equal to operator. The DataSource results will have FilterVariable values that are greater than or equal to the value specified with GE .
    :type GE: string
    :param LE: The less than or equal to operator. The DataSource results will have FilterVariable values that are less than or equal to the value specified with LE .
    :type LE: string
    :param NE: The not equal to operator. The DataSource results will have FilterVariable values not equal to the value specified with NE .
    :type NE: string
    :param Prefix: A string that is found at the beginning of a variable, such as Name or Id .
            For example, a DataSource could have the Name 2014-09-09-HolidayGiftMailer . To search for this DataSource , select Name for the FilterVariable and any of the following strings for the Prefix :
            2014-09
            2014-09-09
            2014-09-09-Holiday
            
    :type Prefix: string
    :param SortOrder: A two-value parameter that determines the sequence of the resulting list of DataSource .
            asc - Arranges the list in ascending order (A-Z, 0-9).
            dsc - Arranges the list in descending order (Z-A, 9-0).
            Results are sorted by FilterVariable .
            
    :type SortOrder: string
    :param NextToken: The ID of the page in the paginated results.
    :type NextToken: string
    :param Limit: The maximum number of DataSource to include in the result.
    :type Limit: integer
    """
    pass


def describe_evaluations(FilterVariable=None, EQ=None, GT=None, LT=None, GE=None, LE=None, NE=None, Prefix=None,
                         SortOrder=None, NextToken=None, Limit=None):
    """
    :param FilterVariable: Use one of the following variable to filter a list of Evaluation objects:
            CreatedAt - Sets the search criteria to the Evaluation creation date.
            Status - Sets the search criteria to the Evaluation status.
            Name - Sets the search criteria to the contents of Evaluation **** Name .
            IAMUser - Sets the search criteria to the user account that invoked an Evaluation .
            MLModelId - Sets the search criteria to the MLModel that was evaluated.
            DataSourceId - Sets the search criteria to the DataSource used in Evaluation .
            DataUri - Sets the search criteria to the data file(s) used in Evaluation . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
            
    :type FilterVariable: string
    :param EQ: The equal to operator. The Evaluation results will have FilterVariable values that exactly match the value specified with EQ .
    :type EQ: string
    :param GT: The greater than operator. The Evaluation results will have FilterVariable values that are greater than the value specified with GT .
    :type GT: string
    :param LT: The less than operator. The Evaluation results will have FilterVariable values that are less than the value specified with LT .
    :type LT: string
    :param GE: The greater than or equal to operator. The Evaluation results will have FilterVariable values that are greater than or equal to the value specified with GE .
    :type GE: string
    :param LE: The less than or equal to operator. The Evaluation results will have FilterVariable values that are less than or equal to the value specified with LE .
    :type LE: string
    :param NE: The not equal to operator. The Evaluation results will have FilterVariable values not equal to the value specified with NE .
    :type NE: string
    :param Prefix: A string that is found at the beginning of a variable, such as Name or Id .
            For example, an Evaluation could have the Name 2014-09-09-HolidayGiftMailer . To search for this Evaluation , select Name for the FilterVariable and any of the following strings for the Prefix :
            2014-09
            2014-09-09
            2014-09-09-Holiday
            
    :type Prefix: string
    :param SortOrder: A two-value parameter that determines the sequence of the resulting list of Evaluation .
            asc - Arranges the list in ascending order (A-Z, 0-9).
            dsc - Arranges the list in descending order (Z-A, 9-0).
            Results are sorted by FilterVariable .
            
    :type SortOrder: string
    :param NextToken: The ID of the page in the paginated results.
    :type NextToken: string
    :param Limit: The maximum number of Evaluation to include in the result.
    :type Limit: integer
    """
    pass


def describe_ml_models(FilterVariable=None, EQ=None, GT=None, LT=None, GE=None, LE=None, NE=None, Prefix=None,
                       SortOrder=None, NextToken=None, Limit=None):
    """
    :param FilterVariable: Use one of the following variables to filter a list of MLModel :
            CreatedAt - Sets the search criteria to MLModel creation date.
            Status - Sets the search criteria to MLModel status.
            Name - Sets the search criteria to the contents of MLModel **** Name .
            IAMUser - Sets the search criteria to the user account that invoked the MLModel creation.
            TrainingDataSourceId - Sets the search criteria to the DataSource used to train one or more MLModel .
            RealtimeEndpointStatus - Sets the search criteria to the MLModel real-time endpoint status.
            MLModelType - Sets the search criteria to MLModel type: binary, regression, or multi-class.
            Algorithm - Sets the search criteria to the algorithm that the MLModel uses.
            TrainingDataURI - Sets the search criteria to the data file(s) used in training a MLModel . The URL can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
            
    :type FilterVariable: string
    :param EQ: The equal to operator. The MLModel results will have FilterVariable values that exactly match the value specified with EQ .
    :type EQ: string
    :param GT: The greater than operator. The MLModel results will have FilterVariable values that are greater than the value specified with GT .
    :type GT: string
    :param LT: The less than operator. The MLModel results will have FilterVariable values that are less than the value specified with LT .
    :type LT: string
    :param GE: The greater than or equal to operator. The MLModel results will have FilterVariable values that are greater than or equal to the value specified with GE .
    :type GE: string
    :param LE: The less than or equal to operator. The MLModel results will have FilterVariable values that are less than or equal to the value specified with LE .
    :type LE: string
    :param NE: The not equal to operator. The MLModel results will have FilterVariable values not equal to the value specified with NE .
    :type NE: string
    :param Prefix: A string that is found at the beginning of a variable, such as Name or Id .
            For example, an MLModel could have the Name 2014-09-09-HolidayGiftMailer . To search for this MLModel , select Name for the FilterVariable and any of the following strings for the Prefix :
            2014-09
            2014-09-09
            2014-09-09-Holiday
            
    :type Prefix: string
    :param SortOrder: A two-value parameter that determines the sequence of the resulting list of MLModel .
            asc - Arranges the list in ascending order (A-Z, 0-9).
            dsc - Arranges the list in descending order (Z-A, 9-0).
            Results are sorted by FilterVariable .
            
    :type SortOrder: string
    :param NextToken: The ID of the page in the paginated results.
    :type NextToken: string
    :param Limit: The number of pages of information to include in the result. The range of acceptable values is 1 through 100 . The default value is 100 .
    :type Limit: integer
    """
    pass


def describe_tags(ResourceId=None, ResourceType=None):
    """
    :param ResourceId: [REQUIRED]
            The ID of the ML object. For example, exampleModelId .
            
    :type ResourceId: string
    :param ResourceType: [REQUIRED]
            The type of the ML object.
            
    :type ResourceType: string
    """
    pass


def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    :param ClientMethod: The client method to presign for
    :type ClientMethod: string
    :param Params: The parameters normally passed to
            ClientMethod.
    :type Params: dict
    :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
    :type ExpiresIn: int
    :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.
    :type HttpMethod: string
    """
    pass


def get_batch_prediction(BatchPredictionId=None):
    """
    :param BatchPredictionId: [REQUIRED]
            An ID assigned to the BatchPrediction at creation.
            Return typedict
            ReturnsResponse Syntax{
              'BatchPredictionId': 'string',
              'MLModelId': 'string',
              'BatchPredictionDataSourceId': 'string',
              'InputDataLocationS3': 'string',
              'CreatedByIamUser': 'string',
              'CreatedAt': datetime(2015, 1, 1),
              'LastUpdatedAt': datetime(2015, 1, 1),
              'Name': 'string',
              'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
              'OutputUri': 'string',
              'LogUri': 'string',
              'Message': 'string',
              'ComputeTime': 123,
              'FinishedAt': datetime(2015, 1, 1),
              'StartedAt': datetime(2015, 1, 1),
              'TotalRecordCount': 123,
              'InvalidRecordCount': 123
            }
            Response Structure
            (dict) --Represents the output of a GetBatchPrediction operation and describes a BatchPrediction .
            BatchPredictionId (string) --An ID assigned to the BatchPrediction at creation. This value should be identical to the value of the BatchPredictionID in the request.
            MLModelId (string) --The ID of the MLModel that generated predictions for the BatchPrediction request.
            BatchPredictionDataSourceId (string) --The ID of the DataSource that was used to create the BatchPrediction .
            InputDataLocationS3 (string) --The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).
            CreatedByIamUser (string) --The AWS user account that invoked the BatchPrediction . The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
            CreatedAt (datetime) --The time when the BatchPrediction was created. The time is expressed in epoch time.
            LastUpdatedAt (datetime) --The time of the most recent edit to BatchPrediction . The time is expressed in epoch time.
            Name (string) --A user-supplied name or description of the BatchPrediction .
            Status (string) --The status of the BatchPrediction , which can be one of the following values:
            PENDING - Amazon Machine Learning (Amazon ML) submitted a request to generate batch predictions.
            INPROGRESS - The batch predictions are in progress.
            FAILED - The request to perform a batch prediction did not run to completion. It is not usable.
            COMPLETED - The batch prediction process completed successfully.
            DELETED - The BatchPrediction is marked as deleted. It is not usable.
            OutputUri (string) --The location of an Amazon S3 bucket or directory to receive the operation results.
            LogUri (string) --A link to the file that contains logs of the CreateBatchPrediction operation.
            Message (string) --A description of the most recent details about processing the batch prediction request.
            ComputeTime (integer) --The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the BatchPrediction , normalized and scaled on computation resources. ComputeTime is only available if the BatchPrediction is in the COMPLETED state.
            FinishedAt (datetime) --The epoch time when Amazon Machine Learning marked the BatchPrediction as COMPLETED or FAILED . FinishedAt is only available when the BatchPrediction is in the COMPLETED or FAILED state.
            StartedAt (datetime) --The epoch time when Amazon Machine Learning marked the BatchPrediction as INPROGRESS . StartedAt isn't available if the BatchPrediction is in the PENDING state.
            TotalRecordCount (integer) --The number of total records that Amazon Machine Learning saw while processing the BatchPrediction .
            InvalidRecordCount (integer) --The number of invalid records that Amazon Machine Learning saw while processing the BatchPrediction .
            
            
    :type BatchPredictionId: string
    """
    pass


def get_data_source(DataSourceId=None, Verbose=None):
    """
    :param DataSourceId: [REQUIRED]
            The ID assigned to the DataSource at creation.
            
    :type DataSourceId: string
    :param Verbose: Specifies whether the GetDataSource operation should return DataSourceSchema .
            If true, DataSourceSchema is returned.
            If false, DataSourceSchema is not returned.
            
    :type Verbose: boolean
    """
    pass


def get_evaluation(EvaluationId=None):
    """
    :param EvaluationId: [REQUIRED]
            The ID of the Evaluation to retrieve. The evaluation of each MLModel is recorded and cataloged. The ID provides the means to access the information.
            Return typedict
            ReturnsResponse Syntax{
              'EvaluationId': 'string',
              'MLModelId': 'string',
              'EvaluationDataSourceId': 'string',
              'InputDataLocationS3': 'string',
              'CreatedByIamUser': 'string',
              'CreatedAt': datetime(2015, 1, 1),
              'LastUpdatedAt': datetime(2015, 1, 1),
              'Name': 'string',
              'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
              'PerformanceMetrics': {
                'Properties': {
                  'string': 'string'
                }
              },
              'LogUri': 'string',
              'Message': 'string',
              'ComputeTime': 123,
              'FinishedAt': datetime(2015, 1, 1),
              'StartedAt': datetime(2015, 1, 1)
            }
            Response Structure
            (dict) --Represents the output of a GetEvaluation operation and describes an Evaluation .
            EvaluationId (string) --The evaluation ID which is same as the EvaluationId in the request.
            MLModelId (string) --The ID of the MLModel that was the focus of the evaluation.
            EvaluationDataSourceId (string) --The DataSource used for this evaluation.
            InputDataLocationS3 (string) --The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).
            CreatedByIamUser (string) --The AWS user account that invoked the evaluation. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.
            CreatedAt (datetime) --The time that the Evaluation was created. The time is expressed in epoch time.
            LastUpdatedAt (datetime) --The time of the most recent edit to the Evaluation . The time is expressed in epoch time.
            Name (string) --A user-supplied name or description of the Evaluation .
            Status (string) --The status of the evaluation. This element can have one of the following values:
            PENDING - Amazon Machine Language (Amazon ML) submitted a request to evaluate an MLModel .
            INPROGRESS - The evaluation is underway.
            FAILED - The request to evaluate an MLModel did not run to completion. It is not usable.
            COMPLETED - The evaluation process completed successfully.
            DELETED - The Evaluation is marked as deleted. It is not usable.
            PerformanceMetrics (dict) --Measurements of how well the MLModel performed using observations referenced by the DataSource . One of the following metric is returned based on the type of the MLModel :
            BinaryAUC: A binary MLModel uses the Area Under the Curve (AUC) technique to measure performance.
            RegressionRMSE: A regression MLModel uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.
            MulticlassAvgFScore: A multiclass MLModel uses the F1 score technique to measure performance.
            For more information about performance metrics, please see the Amazon Machine Learning Developer Guide .
            Properties (dict) --
            (string) --
            (string) --
            
            LogUri (string) --A link to the file that contains logs of the CreateEvaluation operation.
            Message (string) --A description of the most recent details about evaluating the MLModel .
            ComputeTime (integer) --The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the Evaluation , normalized and scaled on computation resources. ComputeTime is only available if the Evaluation is in the COMPLETED state.
            FinishedAt (datetime) --The epoch time when Amazon Machine Learning marked the Evaluation as COMPLETED or FAILED . FinishedAt is only available when the Evaluation is in the COMPLETED or FAILED state.
            StartedAt (datetime) --The epoch time when Amazon Machine Learning marked the Evaluation as INPROGRESS . StartedAt isn't available if the Evaluation is in the PENDING state.
            
            
    :type EvaluationId: string
    """
    pass


def get_ml_model(MLModelId=None, Verbose=None):
    """
    :param MLModelId: [REQUIRED]
            The ID assigned to the MLModel at creation.
            
    :type MLModelId: string
    :param Verbose: Specifies whether the GetMLModel operation should return Recipe .
            If true, Recipe is returned.
            If false, Recipe is not returned.
            
    :type Verbose: boolean
    """
    pass


def get_paginator(operation_name=None):
    """
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').
            Raises OperationNotPageableErrorRaised if the operation is not
            pageable. You can use the client.can_paginate method to
            check if an operation is pageable.
            Return typeL{botocore.paginate.Paginator}
            ReturnsA paginator object.
            
    :type operation_name: string
    """
    pass


def get_waiter():
    """
    """
    pass


def predict(MLModelId=None, Record=None, PredictEndpoint=None):
    """
    :param MLModelId: [REQUIRED]
            A unique identifier of the MLModel .
            
    :type MLModelId: string
    :param Record: [REQUIRED]
            A map of variable name-value pairs that represent an observation.
            (string) --The name of a variable. Currently it's used to specify the name of the target value, label, weight, and tags.
            (string) --The value of a variable. Currently it's used to specify values of the target value, weights, and tag variables and for filtering variable values.
            
            
    :type Record: dict
    :param PredictEndpoint: [REQUIRED]
    :type PredictEndpoint: string
    """
    pass


def update_batch_prediction(BatchPredictionId=None, BatchPredictionName=None):
    """
    :param BatchPredictionId: [REQUIRED]
            The ID assigned to the BatchPrediction during creation.
            
    :type BatchPredictionId: string
    :param BatchPredictionName: [REQUIRED]
            A new user-supplied name or description of the BatchPrediction .
            
    :type BatchPredictionName: string
    """
    pass


def update_data_source(DataSourceId=None, DataSourceName=None):
    """
    :param DataSourceId: [REQUIRED]
            The ID assigned to the DataSource during creation.
            
    :type DataSourceId: string
    :param DataSourceName: [REQUIRED]
            A new user-supplied name or description of the DataSource that will replace the current description.
            
    :type DataSourceName: string
    """
    pass


def update_evaluation(EvaluationId=None, EvaluationName=None):
    """
    :param EvaluationId: [REQUIRED]
            The ID assigned to the Evaluation during creation.
            
    :type EvaluationId: string
    :param EvaluationName: [REQUIRED]
            A new user-supplied name or description of the Evaluation that will replace the current content.
            
    :type EvaluationName: string
    """
    pass


def update_ml_model(MLModelId=None, MLModelName=None, ScoreThreshold=None):
    """
    :param MLModelId: [REQUIRED]
            The ID assigned to the MLModel during creation.
            
    :type MLModelId: string
    :param MLModelName: A user-supplied name or description of the MLModel .
    :type MLModelName: string
    :param ScoreThreshold: The ScoreThreshold used in binary classification MLModel that marks the boundary between a positive prediction and a negative prediction.
            Output values greater than or equal to the ScoreThreshold receive a positive result from the MLModel , such as true . Output values less than the ScoreThreshold receive a negative response from the MLModel , such as false .
            
    :type ScoreThreshold: float
    """
    pass
