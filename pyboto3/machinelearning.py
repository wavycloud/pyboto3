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

def add_tags(Tags=None, ResourceId=None, ResourceType=None):
    """
    Adds one or more tags to an object, up to a limit of 10. Each tag consists of a key and an optional value. If you add a tag using a key that is already associated with the ML object, AddTags updates the tag's value.
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags(
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        ResourceId='string',
        ResourceType='BatchPrediction'|'DataSource'|'Evaluation'|'MLModel'
    )
    
    
    :type Tags: list
    :param Tags: [REQUIRED]
            The key-value pairs to use to create tags. If you specify a key without specifying a value, Amazon ML creates a tag with the specified key and a value of null.
            (dict) --A custom key-value pair associated with an ML object, such as an ML model.
            Key (string) --A unique identifier for the tag. Valid characters include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.
            Value (string) --An optional string, typically used to describe or define the tag. Valid characters include Unicode letters, digits, white space, _, ., /, =, +, -, %, and @.
            
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the ML object to tag. For example, exampleModelId .
            

    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            The type of the ML object to tag.
            

    :rtype: dict
    :return: {
        'ResourceId': 'string',
        'ResourceType': 'BatchPrediction'|'DataSource'|'Evaluation'|'MLModel'
    }
    
    
    """
    pass

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

def create_batch_prediction(BatchPredictionId=None, BatchPredictionName=None, MLModelId=None, BatchPredictionDataSourceId=None, OutputUri=None):
    """
    Generates predictions for a group of observations. The observations to process exist in one or more data files referenced by a DataSource . This operation creates a new BatchPrediction , and uses an MLModel and the data files referenced by the DataSource as information sources.
    CreateBatchPrediction is an asynchronous operation. In response to CreateBatchPrediction , Amazon Machine Learning (Amazon ML) immediately returns and sets the BatchPrediction status to PENDING . After the BatchPrediction completes, Amazon ML sets the status to COMPLETED .
    You can poll for status updates by using the  GetBatchPrediction operation and checking the Status parameter of the result. After the COMPLETED status appears, the results are available in the location specified by the OutputUri parameter.
    See also: AWS API Documentation
    
    
    :example: response = client.create_batch_prediction(
        BatchPredictionId='string',
        BatchPredictionName='string',
        MLModelId='string',
        BatchPredictionDataSourceId='string',
        OutputUri='string'
    )
    
    
    :type BatchPredictionId: string
    :param BatchPredictionId: [REQUIRED]
            A user-supplied ID that uniquely identifies the BatchPrediction .
            

    :type BatchPredictionName: string
    :param BatchPredictionName: A user-supplied name or description of the BatchPrediction . BatchPredictionName can only use the UTF-8 character set.

    :type MLModelId: string
    :param MLModelId: [REQUIRED]
            The ID of the MLModel that will generate predictions for the group of observations.
            

    :type BatchPredictionDataSourceId: string
    :param BatchPredictionDataSourceId: [REQUIRED]
            The ID of the DataSource that points to the group of observations to predict.
            

    :type OutputUri: string
    :param OutputUri: [REQUIRED]
            The location of an Amazon Simple Storage Service (Amazon S3) bucket or directory to store the batch prediction results. The following substrings are not allowed in the s3 key portion of the outputURI field: ':', '//', '/./', '/../'.
            Amazon ML needs permissions to store and retrieve the logs on your behalf. For information about how to set permissions, see the Amazon Machine Learning Developer Guide .
            

    :rtype: dict
    :return: {
        'BatchPredictionId': 'string'
    }
    
    
    """
    pass

def create_data_source_from_rds(DataSourceId=None, DataSourceName=None, RDSData=None, RoleARN=None, ComputeStatistics=None):
    """
    Creates a DataSource object from an Amazon Relational Database Service (Amazon RDS). A DataSource references data that can be used to perform CreateMLModel , CreateEvaluation , or CreateBatchPrediction operations.
    CreateDataSourceFromRDS is an asynchronous operation. In response to CreateDataSourceFromRDS , Amazon Machine Learning (Amazon ML) immediately returns and sets the DataSource status to PENDING . After the DataSource is created and ready for use, Amazon ML sets the Status parameter to COMPLETED . DataSource in the COMPLETED or PENDING state can be used only to perform CreateMLModel , CreateEvaluation , or CreateBatchPrediction operations.
    If Amazon ML cannot accept the input source, it sets the Status parameter to FAILED and includes an error message in the Message attribute of the GetDataSource operation response.
    See also: AWS API Documentation
    
    
    :example: response = client.create_data_source_from_rds(
        DataSourceId='string',
        DataSourceName='string',
        RDSData={
            'DatabaseInformation': {
                'InstanceIdentifier': 'string',
                'DatabaseName': 'string'
            },
            'SelectSqlQuery': 'string',
            'DatabaseCredentials': {
                'Username': 'string',
                'Password': 'string'
            },
            'S3StagingLocation': 'string',
            'DataRearrangement': 'string',
            'DataSchema': 'string',
            'DataSchemaUri': 'string',
            'ResourceRole': 'string',
            'ServiceRole': 'string',
            'SubnetId': 'string',
            'SecurityGroupIds': [
                'string',
            ]
        },
        RoleARN='string',
        ComputeStatistics=True|False
    )
    
    
    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]
            A user-supplied ID that uniquely identifies the DataSource . Typically, an Amazon Resource Number (ARN) becomes the ID for a DataSource .
            

    :type DataSourceName: string
    :param DataSourceName: A user-supplied name or description of the DataSource .

    :type RDSData: dict
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
            

    :type RoleARN: string
    :param RoleARN: [REQUIRED]
            The role that Amazon ML assumes on behalf of the user to create and activate a data pipeline in the user's account and copy data using the SelectSqlQuery query from Amazon RDS to Amazon S3.
            

    :type ComputeStatistics: boolean
    :param ComputeStatistics: The compute statistics for a DataSource . The statistics are generated from the observation data referenced by a DataSource . Amazon ML uses the statistics internally during MLModel training. This parameter must be set to true if the ```` DataSource```` needs to be used for MLModel training.

    :rtype: dict
    :return: {
        'DataSourceId': 'string'
    }
    
    
    """
    pass

def create_data_source_from_redshift(DataSourceId=None, DataSourceName=None, DataSpec=None, RoleARN=None, ComputeStatistics=None):
    """
    Creates a DataSource from a database hosted on an Amazon Redshift cluster. A DataSource references data that can be used to perform either CreateMLModel , CreateEvaluation , or CreateBatchPrediction operations.
    CreateDataSourceFromRedshift is an asynchronous operation. In response to CreateDataSourceFromRedshift , Amazon Machine Learning (Amazon ML) immediately returns and sets the DataSource status to PENDING . After the DataSource is created and ready for use, Amazon ML sets the Status parameter to COMPLETED . DataSource in COMPLETED or PENDING states can be used to perform only CreateMLModel , CreateEvaluation , or CreateBatchPrediction operations.
    If Amazon ML can't accept the input source, it sets the Status parameter to FAILED and includes an error message in the Message attribute of the GetDataSource operation response.
    The observations should be contained in the database hosted on an Amazon Redshift cluster and should be specified by a SelectSqlQuery query. Amazon ML executes an Unload command in Amazon Redshift to transfer the result set of the SelectSqlQuery query to S3StagingLocation .
    After the DataSource has been created, it's ready for use in evaluations and batch predictions. If you plan to use the DataSource to train an MLModel , the DataSource also requires a recipe. A recipe describes how each input variable will be used in training an MLModel . Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.
    You can't change an existing datasource, but you can copy and modify the settings from an existing Amazon Redshift datasource to create a new datasource. To do so, call GetDataSource for an existing datasource and copy the values to a CreateDataSource call. Change the settings that you want to change and make sure that all required fields have the appropriate values.
    See also: AWS API Documentation
    
    
    :example: response = client.create_data_source_from_redshift(
        DataSourceId='string',
        DataSourceName='string',
        DataSpec={
            'DatabaseInformation': {
                'DatabaseName': 'string',
                'ClusterIdentifier': 'string'
            },
            'SelectSqlQuery': 'string',
            'DatabaseCredentials': {
                'Username': 'string',
                'Password': 'string'
            },
            'S3StagingLocation': 'string',
            'DataRearrangement': 'string',
            'DataSchema': 'string',
            'DataSchemaUri': 'string'
        },
        RoleARN='string',
        ComputeStatistics=True|False
    )
    
    
    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]
            A user-supplied ID that uniquely identifies the DataSource .
            

    :type DataSourceName: string
    :param DataSourceName: A user-supplied name or description of the DataSource .

    :type DataSpec: dict
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
            

    :type RoleARN: string
    :param RoleARN: [REQUIRED]
            A fully specified role Amazon Resource Name (ARN). Amazon ML assumes the role on behalf of the user to create the following:
            A security group to allow Amazon ML to execute the SelectSqlQuery query on an Amazon Redshift cluster
            An Amazon S3 bucket policy to grant Amazon ML read/write permissions on the S3StagingLocation
            

    :type ComputeStatistics: boolean
    :param ComputeStatistics: The compute statistics for a DataSource . The statistics are generated from the observation data referenced by a DataSource . Amazon ML uses the statistics internally during MLModel training. This parameter must be set to true if the DataSource needs to be used for MLModel training.

    :rtype: dict
    :return: {
        'DataSourceId': 'string'
    }
    
    
    """
    pass

def create_data_source_from_s3(DataSourceId=None, DataSourceName=None, DataSpec=None, ComputeStatistics=None):
    """
    Creates a DataSource object. A DataSource references data that can be used to perform CreateMLModel , CreateEvaluation , or CreateBatchPrediction operations.
    CreateDataSourceFromS3 is an asynchronous operation. In response to CreateDataSourceFromS3 , Amazon Machine Learning (Amazon ML) immediately returns and sets the DataSource status to PENDING . After the DataSource has been created and is ready for use, Amazon ML sets the Status parameter to COMPLETED . DataSource in the COMPLETED or PENDING state can be used to perform only CreateMLModel , CreateEvaluation or CreateBatchPrediction operations.
    If Amazon ML can't accept the input source, it sets the Status parameter to FAILED and includes an error message in the Message attribute of the GetDataSource operation response.
    The observation data used in a DataSource should be ready to use; that is, it should have a consistent structure, and missing data values should be kept to a minimum. The observation data must reside in one or more .csv files in an Amazon Simple Storage Service (Amazon S3) location, along with a schema that describes the data items by name and type. The same schema must be used for all of the data files referenced by the DataSource .
    After the DataSource has been created, it's ready to use in evaluations and batch predictions. If you plan to use the DataSource to train an MLModel , the DataSource also needs a recipe. A recipe describes how each input variable will be used in training an MLModel . Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.
    See also: AWS API Documentation
    
    
    :example: response = client.create_data_source_from_s3(
        DataSourceId='string',
        DataSourceName='string',
        DataSpec={
            'DataLocationS3': 'string',
            'DataRearrangement': 'string',
            'DataSchema': 'string',
            'DataSchemaLocationS3': 'string'
        },
        ComputeStatistics=True|False
    )
    
    
    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]
            A user-supplied identifier that uniquely identifies the DataSource .
            

    :type DataSourceName: string
    :param DataSourceName: A user-supplied name or description of the DataSource .

    :type DataSpec: dict
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
            

    :type ComputeStatistics: boolean
    :param ComputeStatistics: The compute statistics for a DataSource . The statistics are generated from the observation data referenced by a DataSource . Amazon ML uses the statistics internally during MLModel training. This parameter must be set to true if the ```` DataSource```` needs to be used for MLModel training.

    :rtype: dict
    :return: {
        'DataSourceId': 'string'
    }
    
    
    """
    pass

def create_evaluation(EvaluationId=None, EvaluationName=None, MLModelId=None, EvaluationDataSourceId=None):
    """
    Creates a new Evaluation of an MLModel . An MLModel is evaluated on a set of observations associated to a DataSource . Like a DataSource for an MLModel , the DataSource for an Evaluation contains values for the Target Variable . The Evaluation compares the predicted result for each observation to the actual outcome and provides a summary so that you know how effective the MLModel functions on the test data. Evaluation generates a relevant performance metric, such as BinaryAUC, RegressionRMSE or MulticlassAvgFScore based on the corresponding MLModelType : BINARY , REGRESSION or MULTICLASS .
    CreateEvaluation is an asynchronous operation. In response to CreateEvaluation , Amazon Machine Learning (Amazon ML) immediately returns and sets the evaluation status to PENDING . After the Evaluation is created and ready for use, Amazon ML sets the status to COMPLETED .
    You can use the GetEvaluation operation to check progress of the evaluation during the creation operation.
    See also: AWS API Documentation
    
    
    :example: response = client.create_evaluation(
        EvaluationId='string',
        EvaluationName='string',
        MLModelId='string',
        EvaluationDataSourceId='string'
    )
    
    
    :type EvaluationId: string
    :param EvaluationId: [REQUIRED]
            A user-supplied ID that uniquely identifies the Evaluation .
            

    :type EvaluationName: string
    :param EvaluationName: A user-supplied name or description of the Evaluation .

    :type MLModelId: string
    :param MLModelId: [REQUIRED]
            The ID of the MLModel to evaluate.
            The schema used in creating the MLModel must match the schema of the DataSource used in the Evaluation .
            

    :type EvaluationDataSourceId: string
    :param EvaluationDataSourceId: [REQUIRED]
            The ID of the DataSource for the evaluation. The schema of the DataSource must match the schema used to create the MLModel .
            

    :rtype: dict
    :return: {
        'EvaluationId': 'string'
    }
    
    
    """
    pass

def create_ml_model(MLModelId=None, MLModelName=None, MLModelType=None, Parameters=None, TrainingDataSourceId=None, Recipe=None, RecipeUri=None):
    """
    Creates a new MLModel using the DataSource and the recipe as information sources.
    An MLModel is nearly immutable. Users can update only the MLModelName and the ScoreThreshold in an MLModel without creating a new MLModel .
    CreateMLModel is an asynchronous operation. In response to CreateMLModel , Amazon Machine Learning (Amazon ML) immediately returns and sets the MLModel status to PENDING . After the MLModel has been created and ready is for use, Amazon ML sets the status to COMPLETED .
    You can use the GetMLModel operation to check the progress of the MLModel during the creation operation.
    See also: AWS API Documentation
    
    
    :example: response = client.create_ml_model(
        MLModelId='string',
        MLModelName='string',
        MLModelType='REGRESSION'|'BINARY'|'MULTICLASS',
        Parameters={
            'string': 'string'
        },
        TrainingDataSourceId='string',
        Recipe='string',
        RecipeUri='string'
    )
    
    
    :type MLModelId: string
    :param MLModelId: [REQUIRED]
            A user-supplied ID that uniquely identifies the MLModel .
            

    :type MLModelName: string
    :param MLModelName: A user-supplied name or description of the MLModel .

    :type MLModelType: string
    :param MLModelType: [REQUIRED]
            The category of supervised learning that this MLModel will address. Choose from the following types:
            Choose REGRESSION if the MLModel will be used to predict a numeric value.
            Choose BINARY if the MLModel result has two possible values.
            Choose MULTICLASS if the MLModel result has a limited number of values.
            For more information, see the Amazon Machine Learning Developer Guide .
            

    :type Parameters: dict
    :param Parameters: A list of the training parameters in the MLModel . The list is implemented as a map of key-value pairs.
            The following is the current set of training parameters:
            sgd.maxMLModelSizeInBytes - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance. The value is an integer that ranges from 100000 to 2147483648 . The default value is 33554432 .
            sgd.maxPasses - The number of times that the training process traverses the observations to build the MLModel . The value is an integer that ranges from 1 to 10000 . The default value is 10 .
            sgd.shuffleType - Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are auto and none . The default value is none . We strongly recommend that you shuffle your data.
            sgd.l1RegularizationAmount - The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as 1.0E-08 . The value is a double that ranges from 0 to MAX_DOUBLE . The default is to not use L1 normalization. This parameter can't be used when L2 is specified. Use this parameter sparingly.
            sgd.l2RegularizationAmount - The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as 1.0E-08 . The value is a double that ranges from 0 to MAX_DOUBLE . The default is to not use L2 normalization. This parameter can't be used when L1 is specified. Use this parameter sparingly.
            (string) --String type.
            (string) --String type.
            
            

    :type TrainingDataSourceId: string
    :param TrainingDataSourceId: [REQUIRED]
            The DataSource that points to the training data.
            

    :type Recipe: string
    :param Recipe: The data recipe for creating the MLModel . You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.

    :type RecipeUri: string
    :param RecipeUri: The Amazon Simple Storage Service (Amazon S3) location and file name that contains the MLModel recipe. You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.

    :rtype: dict
    :return: {
        'MLModelId': 'string'
    }
    
    
    """
    pass

def create_realtime_endpoint(MLModelId=None):
    """
    Creates a real-time endpoint for the MLModel . The endpoint contains the URI of the MLModel ; that is, the location to send real-time prediction requests for the specified MLModel .
    See also: AWS API Documentation
    
    
    :example: response = client.create_realtime_endpoint(
        MLModelId='string'
    )
    
    
    :type MLModelId: string
    :param MLModelId: [REQUIRED]
            The ID assigned to the MLModel during creation.
            

    :rtype: dict
    :return: {
        'MLModelId': 'string',
        'RealtimeEndpointInfo': {
            'PeakRequestsPerSecond': 123,
            'CreatedAt': datetime(2015, 1, 1),
            'EndpointUrl': 'string',
            'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
        }
    }
    
    
    """
    pass

def delete_batch_prediction(BatchPredictionId=None):
    """
    Assigns the DELETED status to a BatchPrediction , rendering it unusable.
    After using the DeleteBatchPrediction operation, you can use the  GetBatchPrediction operation to verify that the status of the BatchPrediction changed to DELETED.
    Caution: The result of the DeleteBatchPrediction operation is irreversible.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_batch_prediction(
        BatchPredictionId='string'
    )
    
    
    :type BatchPredictionId: string
    :param BatchPredictionId: [REQUIRED]
            A user-supplied ID that uniquely identifies the BatchPrediction .
            

    :rtype: dict
    :return: {
        'BatchPredictionId': 'string'
    }
    
    
    """
    pass

def delete_data_source(DataSourceId=None):
    """
    Assigns the DELETED status to a DataSource , rendering it unusable.
    After using the DeleteDataSource operation, you can use the  GetDataSource operation to verify that the status of the DataSource changed to DELETED.
    Caution: The results of the DeleteDataSource operation are irreversible.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_data_source(
        DataSourceId='string'
    )
    
    
    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]
            A user-supplied ID that uniquely identifies the DataSource .
            

    :rtype: dict
    :return: {
        'DataSourceId': 'string'
    }
    
    
    """
    pass

def delete_evaluation(EvaluationId=None):
    """
    Assigns the DELETED status to an Evaluation , rendering it unusable.
    After invoking the DeleteEvaluation operation, you can use the GetEvaluation operation to verify that the status of the Evaluation changed to DELETED .
    The results of the DeleteEvaluation operation are irreversible.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_evaluation(
        EvaluationId='string'
    )
    
    
    :type EvaluationId: string
    :param EvaluationId: [REQUIRED]
            A user-supplied ID that uniquely identifies the Evaluation to delete.
            

    :rtype: dict
    :return: {
        'EvaluationId': 'string'
    }
    
    
    """
    pass

def delete_ml_model(MLModelId=None):
    """
    Assigns the DELETED status to an MLModel , rendering it unusable.
    After using the DeleteMLModel operation, you can use the GetMLModel operation to verify that the status of the MLModel changed to DELETED.
    Caution: The result of the DeleteMLModel operation is irreversible.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_ml_model(
        MLModelId='string'
    )
    
    
    :type MLModelId: string
    :param MLModelId: [REQUIRED]
            A user-supplied ID that uniquely identifies the MLModel .
            

    :rtype: dict
    :return: {
        'MLModelId': 'string'
    }
    
    
    """
    pass

def delete_realtime_endpoint(MLModelId=None):
    """
    Deletes a real time endpoint of an MLModel .
    See also: AWS API Documentation
    
    
    :example: response = client.delete_realtime_endpoint(
        MLModelId='string'
    )
    
    
    :type MLModelId: string
    :param MLModelId: [REQUIRED]
            The ID assigned to the MLModel during creation.
            

    :rtype: dict
    :return: {
        'MLModelId': 'string',
        'RealtimeEndpointInfo': {
            'PeakRequestsPerSecond': 123,
            'CreatedAt': datetime(2015, 1, 1),
            'EndpointUrl': 'string',
            'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
        }
    }
    
    
    """
    pass

def delete_tags(TagKeys=None, ResourceId=None, ResourceType=None):
    """
    Deletes the specified tags associated with an ML object. After this operation is complete, you can't recover deleted tags.
    If you specify a tag that doesn't exist, Amazon ML ignores it.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tags(
        TagKeys=[
            'string',
        ],
        ResourceId='string',
        ResourceType='BatchPrediction'|'DataSource'|'Evaluation'|'MLModel'
    )
    
    
    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            One or more tags to delete.
            (string) --
            

    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the tagged ML object. For example, exampleModelId .
            

    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            The type of the tagged ML object.
            

    :rtype: dict
    :return: {
        'ResourceId': 'string',
        'ResourceType': 'BatchPrediction'|'DataSource'|'Evaluation'|'MLModel'
    }
    
    
    """
    pass

def describe_batch_predictions(FilterVariable=None, EQ=None, GT=None, LT=None, GE=None, LE=None, NE=None, Prefix=None, SortOrder=None, NextToken=None, Limit=None):
    """
    Returns a list of BatchPrediction operations that match the search criteria in the request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_batch_predictions(
        FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'MLModelId'|'DataSourceId'|'DataURI',
        EQ='string',
        GT='string',
        LT='string',
        GE='string',
        LE='string',
        NE='string',
        Prefix='string',
        SortOrder='asc'|'dsc',
        NextToken='string',
        Limit=123
    )
    
    
    :type FilterVariable: string
    :param FilterVariable: Use one of the following variables to filter a list of BatchPrediction :
            CreatedAt - Sets the search criteria to the BatchPrediction creation date.
            Status - Sets the search criteria to the BatchPrediction status.
            Name - Sets the search criteria to the contents of the BatchPrediction **** Name .
            IAMUser - Sets the search criteria to the user account that invoked the BatchPrediction creation.
            MLModelId - Sets the search criteria to the MLModel used in the BatchPrediction .
            DataSourceId - Sets the search criteria to the DataSource used in the BatchPrediction .
            DataURI - Sets the search criteria to the data file(s) used in the BatchPrediction . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
            

    :type EQ: string
    :param EQ: The equal to operator. The BatchPrediction results will have FilterVariable values that exactly match the value specified with EQ .

    :type GT: string
    :param GT: The greater than operator. The BatchPrediction results will have FilterVariable values that are greater than the value specified with GT .

    :type LT: string
    :param LT: The less than operator. The BatchPrediction results will have FilterVariable values that are less than the value specified with LT .

    :type GE: string
    :param GE: The greater than or equal to operator. The BatchPrediction results will have FilterVariable values that are greater than or equal to the value specified with GE .

    :type LE: string
    :param LE: The less than or equal to operator. The BatchPrediction results will have FilterVariable values that are less than or equal to the value specified with LE .

    :type NE: string
    :param NE: The not equal to operator. The BatchPrediction results will have FilterVariable values not equal to the value specified with NE .

    :type Prefix: string
    :param Prefix: A string that is found at the beginning of a variable, such as Name or Id .
            For example, a Batch Prediction operation could have the Name 2014-09-09-HolidayGiftMailer . To search for this BatchPrediction , select Name for the FilterVariable and any of the following strings for the Prefix :
            2014-09
            2014-09-09
            2014-09-09-Holiday
            

    :type SortOrder: string
    :param SortOrder: A two-value parameter that determines the sequence of the resulting list of MLModel s.
            asc - Arranges the list in ascending order (A-Z, 0-9).
            dsc - Arranges the list in descending order (Z-A, 9-0).
            Results are sorted by FilterVariable .
            

    :type NextToken: string
    :param NextToken: An ID of the page in the paginated results.

    :type Limit: integer
    :param Limit: The number of pages of information to include in the result. The range of acceptable values is 1 through 100 . The default value is 100 .

    :rtype: dict
    :return: {
        'Results': [
            {
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
                'Message': 'string',
                'ComputeTime': 123,
                'FinishedAt': datetime(2015, 1, 1),
                'StartedAt': datetime(2015, 1, 1),
                'TotalRecordCount': 123,
                'InvalidRecordCount': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    PENDING - Amazon Machine Learning (Amazon ML) submitted a request to generate predictions for a batch of observations.
    INPROGRESS - The process is underway.
    FAILED - The request to perform a batch prediction did not run to completion. It is not usable.
    COMPLETED - The batch prediction process completed successfully.
    DELETED - The BatchPrediction is marked as deleted. It is not usable.
    
    """
    pass

def describe_data_sources(FilterVariable=None, EQ=None, GT=None, LT=None, GE=None, LE=None, NE=None, Prefix=None, SortOrder=None, NextToken=None, Limit=None):
    """
    Returns a list of DataSource that match the search criteria in the request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_data_sources(
        FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'DataLocationS3'|'IAMUser',
        EQ='string',
        GT='string',
        LT='string',
        GE='string',
        LE='string',
        NE='string',
        Prefix='string',
        SortOrder='asc'|'dsc',
        NextToken='string',
        Limit=123
    )
    
    
    :type FilterVariable: string
    :param FilterVariable: Use one of the following variables to filter a list of DataSource :
            CreatedAt - Sets the search criteria to DataSource creation dates.
            Status - Sets the search criteria to DataSource statuses.
            Name - Sets the search criteria to the contents of DataSource **** Name .
            DataUri - Sets the search criteria to the URI of data files used to create the DataSource . The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
            IAMUser - Sets the search criteria to the user account that invoked the DataSource creation.
            

    :type EQ: string
    :param EQ: The equal to operator. The DataSource results will have FilterVariable values that exactly match the value specified with EQ .

    :type GT: string
    :param GT: The greater than operator. The DataSource results will have FilterVariable values that are greater than the value specified with GT .

    :type LT: string
    :param LT: The less than operator. The DataSource results will have FilterVariable values that are less than the value specified with LT .

    :type GE: string
    :param GE: The greater than or equal to operator. The DataSource results will have FilterVariable values that are greater than or equal to the value specified with GE .

    :type LE: string
    :param LE: The less than or equal to operator. The DataSource results will have FilterVariable values that are less than or equal to the value specified with LE .

    :type NE: string
    :param NE: The not equal to operator. The DataSource results will have FilterVariable values not equal to the value specified with NE .

    :type Prefix: string
    :param Prefix: A string that is found at the beginning of a variable, such as Name or Id .
            For example, a DataSource could have the Name 2014-09-09-HolidayGiftMailer . To search for this DataSource , select Name for the FilterVariable and any of the following strings for the Prefix :
            2014-09
            2014-09-09
            2014-09-09-Holiday
            

    :type SortOrder: string
    :param SortOrder: A two-value parameter that determines the sequence of the resulting list of DataSource .
            asc - Arranges the list in ascending order (A-Z, 0-9).
            dsc - Arranges the list in descending order (Z-A, 9-0).
            Results are sorted by FilterVariable .
            

    :type NextToken: string
    :param NextToken: The ID of the page in the paginated results.

    :type Limit: integer
    :param Limit: The maximum number of DataSource to include in the result.

    :rtype: dict
    :return: {
        'Results': [
            {
                'DataSourceId': 'string',
                'DataLocationS3': 'string',
                'DataRearrangement': 'string',
                'CreatedByIamUser': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'LastUpdatedAt': datetime(2015, 1, 1),
                'DataSizeInBytes': 123,
                'NumberOfFiles': 123,
                'Name': 'string',
                'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
                'Message': 'string',
                'RedshiftMetadata': {
                    'RedshiftDatabase': {
                        'DatabaseName': 'string',
                        'ClusterIdentifier': 'string'
                    },
                    'DatabaseUserName': 'string',
                    'SelectSqlQuery': 'string'
                },
                'RDSMetadata': {
                    'Database': {
                        'InstanceIdentifier': 'string',
                        'DatabaseName': 'string'
                    },
                    'DatabaseUserName': 'string',
                    'SelectSqlQuery': 'string',
                    'ResourceRole': 'string',
                    'ServiceRole': 'string',
                    'DataPipelineId': 'string'
                },
                'RoleARN': 'string',
                'ComputeStatistics': True|False,
                'ComputeTime': 123,
                'FinishedAt': datetime(2015, 1, 1),
                'StartedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a DataSource .
    INPROGRESS - The creation process is underway.
    FAILED - The request to create a DataSource did not run to completion. It is not usable.
    COMPLETED - The creation process completed successfully.
    DELETED - The DataSource is marked as deleted. It is not usable.
    
    """
    pass

def describe_evaluations(FilterVariable=None, EQ=None, GT=None, LT=None, GE=None, LE=None, NE=None, Prefix=None, SortOrder=None, NextToken=None, Limit=None):
    """
    Returns a list of DescribeEvaluations that match the search criteria in the request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_evaluations(
        FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'MLModelId'|'DataSourceId'|'DataURI',
        EQ='string',
        GT='string',
        LT='string',
        GE='string',
        LE='string',
        NE='string',
        Prefix='string',
        SortOrder='asc'|'dsc',
        NextToken='string',
        Limit=123
    )
    
    
    :type FilterVariable: string
    :param FilterVariable: Use one of the following variable to filter a list of Evaluation objects:
            CreatedAt - Sets the search criteria to the Evaluation creation date.
            Status - Sets the search criteria to the Evaluation status.
            Name - Sets the search criteria to the contents of Evaluation **** Name .
            IAMUser - Sets the search criteria to the user account that invoked an Evaluation .
            MLModelId - Sets the search criteria to the MLModel that was evaluated.
            DataSourceId - Sets the search criteria to the DataSource used in Evaluation .
            DataUri - Sets the search criteria to the data file(s) used in Evaluation . The URL can identify either a file or an Amazon Simple Storage Solution (Amazon S3) bucket or directory.
            

    :type EQ: string
    :param EQ: The equal to operator. The Evaluation results will have FilterVariable values that exactly match the value specified with EQ .

    :type GT: string
    :param GT: The greater than operator. The Evaluation results will have FilterVariable values that are greater than the value specified with GT .

    :type LT: string
    :param LT: The less than operator. The Evaluation results will have FilterVariable values that are less than the value specified with LT .

    :type GE: string
    :param GE: The greater than or equal to operator. The Evaluation results will have FilterVariable values that are greater than or equal to the value specified with GE .

    :type LE: string
    :param LE: The less than or equal to operator. The Evaluation results will have FilterVariable values that are less than or equal to the value specified with LE .

    :type NE: string
    :param NE: The not equal to operator. The Evaluation results will have FilterVariable values not equal to the value specified with NE .

    :type Prefix: string
    :param Prefix: A string that is found at the beginning of a variable, such as Name or Id .
            For example, an Evaluation could have the Name 2014-09-09-HolidayGiftMailer . To search for this Evaluation , select Name for the FilterVariable and any of the following strings for the Prefix :
            2014-09
            2014-09-09
            2014-09-09-Holiday
            

    :type SortOrder: string
    :param SortOrder: A two-value parameter that determines the sequence of the resulting list of Evaluation .
            asc - Arranges the list in ascending order (A-Z, 0-9).
            dsc - Arranges the list in descending order (Z-A, 9-0).
            Results are sorted by FilterVariable .
            

    :type NextToken: string
    :param NextToken: The ID of the page in the paginated results.

    :type Limit: integer
    :param Limit: The maximum number of Evaluation to include in the result.

    :rtype: dict
    :return: {
        'Results': [
            {
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
                'Message': 'string',
                'ComputeTime': 123,
                'FinishedAt': datetime(2015, 1, 1),
                'StartedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    PENDING - Amazon Machine Learning (Amazon ML) submitted a request to evaluate an MLModel .
    INPROGRESS - The evaluation is underway.
    FAILED - The request to evaluate an MLModel did not run to completion. It is not usable.
    COMPLETED - The evaluation process completed successfully.
    DELETED - The Evaluation is marked as deleted. It is not usable.
    
    """
    pass

def describe_ml_models(FilterVariable=None, EQ=None, GT=None, LT=None, GE=None, LE=None, NE=None, Prefix=None, SortOrder=None, NextToken=None, Limit=None):
    """
    Returns a list of MLModel that match the search criteria in the request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_ml_models(
        FilterVariable='CreatedAt'|'LastUpdatedAt'|'Status'|'Name'|'IAMUser'|'TrainingDataSourceId'|'RealtimeEndpointStatus'|'MLModelType'|'Algorithm'|'TrainingDataURI',
        EQ='string',
        GT='string',
        LT='string',
        GE='string',
        LE='string',
        NE='string',
        Prefix='string',
        SortOrder='asc'|'dsc',
        NextToken='string',
        Limit=123
    )
    
    
    :type FilterVariable: string
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
            

    :type EQ: string
    :param EQ: The equal to operator. The MLModel results will have FilterVariable values that exactly match the value specified with EQ .

    :type GT: string
    :param GT: The greater than operator. The MLModel results will have FilterVariable values that are greater than the value specified with GT .

    :type LT: string
    :param LT: The less than operator. The MLModel results will have FilterVariable values that are less than the value specified with LT .

    :type GE: string
    :param GE: The greater than or equal to operator. The MLModel results will have FilterVariable values that are greater than or equal to the value specified with GE .

    :type LE: string
    :param LE: The less than or equal to operator. The MLModel results will have FilterVariable values that are less than or equal to the value specified with LE .

    :type NE: string
    :param NE: The not equal to operator. The MLModel results will have FilterVariable values not equal to the value specified with NE .

    :type Prefix: string
    :param Prefix: A string that is found at the beginning of a variable, such as Name or Id .
            For example, an MLModel could have the Name 2014-09-09-HolidayGiftMailer . To search for this MLModel , select Name for the FilterVariable and any of the following strings for the Prefix :
            2014-09
            2014-09-09
            2014-09-09-Holiday
            

    :type SortOrder: string
    :param SortOrder: A two-value parameter that determines the sequence of the resulting list of MLModel .
            asc - Arranges the list in ascending order (A-Z, 0-9).
            dsc - Arranges the list in descending order (Z-A, 9-0).
            Results are sorted by FilterVariable .
            

    :type NextToken: string
    :param NextToken: The ID of the page in the paginated results.

    :type Limit: integer
    :param Limit: The number of pages of information to include in the result. The range of acceptable values is 1 through 100 . The default value is 100 .

    :rtype: dict
    :return: {
        'Results': [
            {
                'MLModelId': 'string',
                'TrainingDataSourceId': 'string',
                'CreatedByIamUser': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'LastUpdatedAt': datetime(2015, 1, 1),
                'Name': 'string',
                'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
                'SizeInBytes': 123,
                'EndpointInfo': {
                    'PeakRequestsPerSecond': 123,
                    'CreatedAt': datetime(2015, 1, 1),
                    'EndpointUrl': 'string',
                    'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
                },
                'TrainingParameters': {
                    'string': 'string'
                },
                'InputDataLocationS3': 'string',
                'Algorithm': 'sgd',
                'MLModelType': 'REGRESSION'|'BINARY'|'MULTICLASS',
                'ScoreThreshold': ...,
                'ScoreThresholdLastUpdatedAt': datetime(2015, 1, 1),
                'Message': 'string',
                'ComputeTime': 123,
                'FinishedAt': datetime(2015, 1, 1),
                'StartedAt': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create an MLModel .
    INPROGRESS - The creation process is underway.
    FAILED - The request to create an MLModel didn't run to completion. The model isn't usable.
    COMPLETED - The creation process completed successfully.
    DELETED - The MLModel is marked as deleted. It isn't usable.
    
    """
    pass

def describe_tags(ResourceId=None, ResourceType=None):
    """
    Describes one or more of the tags for your Amazon ML object.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_tags(
        ResourceId='string',
        ResourceType='BatchPrediction'|'DataSource'|'Evaluation'|'MLModel'
    )
    
    
    :type ResourceId: string
    :param ResourceId: [REQUIRED]
            The ID of the ML object. For example, exampleModelId .
            

    :type ResourceType: string
    :param ResourceType: [REQUIRED]
            The type of the ML object.
            

    :rtype: dict
    :return: {
        'ResourceId': 'string',
        'ResourceType': 'BatchPrediction'|'DataSource'|'Evaluation'|'MLModel',
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
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

def get_batch_prediction(BatchPredictionId=None):
    """
    Returns a BatchPrediction that includes detailed metadata, status, and data file information for a Batch Prediction request.
    See also: AWS API Documentation
    
    
    :example: response = client.get_batch_prediction(
        BatchPredictionId='string'
    )
    
    
    :type BatchPredictionId: string
    :param BatchPredictionId: [REQUIRED]
            An ID assigned to the BatchPrediction at creation.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def get_data_source(DataSourceId=None, Verbose=None):
    """
    Returns a DataSource that includes metadata and data file information, as well as the current status of the DataSource .
    GetDataSource provides results in normal or verbose format. The verbose format adds the schema description and the list of files pointed to by the DataSource to the normal format.
    See also: AWS API Documentation
    
    
    :example: response = client.get_data_source(
        DataSourceId='string',
        Verbose=True|False
    )
    
    
    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]
            The ID assigned to the DataSource at creation.
            

    :type Verbose: boolean
    :param Verbose: Specifies whether the GetDataSource operation should return DataSourceSchema .
            If true, DataSourceSchema is returned.
            If false, DataSourceSchema is not returned.
            

    :rtype: dict
    :return: {
        'DataSourceId': 'string',
        'DataLocationS3': 'string',
        'DataRearrangement': 'string',
        'CreatedByIamUser': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'LastUpdatedAt': datetime(2015, 1, 1),
        'DataSizeInBytes': 123,
        'NumberOfFiles': 123,
        'Name': 'string',
        'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
        'LogUri': 'string',
        'Message': 'string',
        'RedshiftMetadata': {
            'RedshiftDatabase': {
                'DatabaseName': 'string',
                'ClusterIdentifier': 'string'
            },
            'DatabaseUserName': 'string',
            'SelectSqlQuery': 'string'
        },
        'RDSMetadata': {
            'Database': {
                'InstanceIdentifier': 'string',
                'DatabaseName': 'string'
            },
            'DatabaseUserName': 'string',
            'SelectSqlQuery': 'string',
            'ResourceRole': 'string',
            'ServiceRole': 'string',
            'DataPipelineId': 'string'
        },
        'RoleARN': 'string',
        'ComputeStatistics': True|False,
        'ComputeTime': 123,
        'FinishedAt': datetime(2015, 1, 1),
        'StartedAt': datetime(2015, 1, 1),
        'DataSourceSchema': 'string'
    }
    
    
    :returns: 
    PENDING - Amazon ML submitted a request to create a DataSource .
    INPROGRESS - The creation process is underway.
    FAILED - The request to create a DataSource did not run to completion. It is not usable.
    COMPLETED - The creation process completed successfully.
    DELETED - The DataSource is marked as deleted. It is not usable.
    
    """
    pass

def get_evaluation(EvaluationId=None):
    """
    Returns an Evaluation that includes metadata as well as the current status of the Evaluation .
    See also: AWS API Documentation
    
    
    :example: response = client.get_evaluation(
        EvaluationId='string'
    )
    
    
    :type EvaluationId: string
    :param EvaluationId: [REQUIRED]
            The ID of the Evaluation to retrieve. The evaluation of each MLModel is recorded and cataloged. The ID provides the means to access the information.
            

    :rtype: dict
    :return: {
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
    
    
    :returns: 
    BinaryAUC: A binary MLModel uses the Area Under the Curve (AUC) technique to measure performance.
    RegressionRMSE: A regression MLModel uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.
    MulticlassAvgFScore: A multiclass MLModel uses the F1 score technique to measure performance.
    
    """
    pass

def get_ml_model(MLModelId=None, Verbose=None):
    """
    Returns an MLModel that includes detailed metadata, data source information, and the current status of the MLModel .
    GetMLModel provides results in normal or verbose format.
    See also: AWS API Documentation
    
    
    :example: response = client.get_ml_model(
        MLModelId='string',
        Verbose=True|False
    )
    
    
    :type MLModelId: string
    :param MLModelId: [REQUIRED]
            The ID assigned to the MLModel at creation.
            

    :type Verbose: boolean
    :param Verbose: Specifies whether the GetMLModel operation should return Recipe .
            If true, Recipe is returned.
            If false, Recipe is not returned.
            

    :rtype: dict
    :return: {
        'MLModelId': 'string',
        'TrainingDataSourceId': 'string',
        'CreatedByIamUser': 'string',
        'CreatedAt': datetime(2015, 1, 1),
        'LastUpdatedAt': datetime(2015, 1, 1),
        'Name': 'string',
        'Status': 'PENDING'|'INPROGRESS'|'FAILED'|'COMPLETED'|'DELETED',
        'SizeInBytes': 123,
        'EndpointInfo': {
            'PeakRequestsPerSecond': 123,
            'CreatedAt': datetime(2015, 1, 1),
            'EndpointUrl': 'string',
            'EndpointStatus': 'NONE'|'READY'|'UPDATING'|'FAILED'
        },
        'TrainingParameters': {
            'string': 'string'
        },
        'InputDataLocationS3': 'string',
        'MLModelType': 'REGRESSION'|'BINARY'|'MULTICLASS',
        'ScoreThreshold': ...,
        'ScoreThresholdLastUpdatedAt': datetime(2015, 1, 1),
        'LogUri': 'string',
        'Message': 'string',
        'ComputeTime': 123,
        'FinishedAt': datetime(2015, 1, 1),
        'StartedAt': datetime(2015, 1, 1),
        'Recipe': 'string',
        'Schema': 'string'
    }
    
    
    :returns: 
    PENDING - Amazon Machine Learning (Amazon ML) submitted a request to describe a MLModel .
    INPROGRESS - The request is processing.
    FAILED - The request did not run to completion. The ML model isn't usable.
    COMPLETED - The request completed successfully.
    DELETED - The MLModel is marked as deleted. It isn't usable.
    
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

def predict(MLModelId=None, Record=None, PredictEndpoint=None):
    """
    Generates a prediction for the observation using the specified ML Model .
    See also: AWS API Documentation
    
    
    :example: response = client.predict(
        MLModelId='string',
        Record={
            'string': 'string'
        },
        PredictEndpoint='string'
    )
    
    
    :type MLModelId: string
    :param MLModelId: [REQUIRED]
            A unique identifier of the MLModel .
            

    :type Record: dict
    :param Record: [REQUIRED]
            A map of variable name-value pairs that represent an observation.
            (string) --The name of a variable. Currently it's used to specify the name of the target value, label, weight, and tags.
            (string) --The value of a variable. Currently it's used to specify values of the target value, weights, and tag variables and for filtering variable values.
            
            

    :type PredictEndpoint: string
    :param PredictEndpoint: [REQUIRED]

    :rtype: dict
    :return: {
        'Prediction': {
            'predictedLabel': 'string',
            'predictedValue': ...,
            'predictedScores': {
                'string': ...
            },
            'details': {
                'string': 'string'
            }
        }
    }
    
    
    :returns: 
    Details - Contains the following attributes: DetailsAttributes.PREDICTIVE_MODEL_TYPE - REGRESSION | BINARY | MULTICLASS DetailsAttributes.ALGORITHM - SGD
    PredictedLabel - Present for either a BINARY or MULTICLASS MLModel request.
    PredictedScores - Contains the raw classification score corresponding to each label.
    PredictedValue - Present for a REGRESSION MLModel request.
    
    """
    pass

def update_batch_prediction(BatchPredictionId=None, BatchPredictionName=None):
    """
    Updates the BatchPredictionName of a BatchPrediction .
    You can use the GetBatchPrediction operation to view the contents of the updated data element.
    See also: AWS API Documentation
    
    
    :example: response = client.update_batch_prediction(
        BatchPredictionId='string',
        BatchPredictionName='string'
    )
    
    
    :type BatchPredictionId: string
    :param BatchPredictionId: [REQUIRED]
            The ID assigned to the BatchPrediction during creation.
            

    :type BatchPredictionName: string
    :param BatchPredictionName: [REQUIRED]
            A new user-supplied name or description of the BatchPrediction .
            

    :rtype: dict
    :return: {
        'BatchPredictionId': 'string'
    }
    
    
    """
    pass

def update_data_source(DataSourceId=None, DataSourceName=None):
    """
    Updates the DataSourceName of a DataSource .
    You can use the GetDataSource operation to view the contents of the updated data element.
    See also: AWS API Documentation
    
    
    :example: response = client.update_data_source(
        DataSourceId='string',
        DataSourceName='string'
    )
    
    
    :type DataSourceId: string
    :param DataSourceId: [REQUIRED]
            The ID assigned to the DataSource during creation.
            

    :type DataSourceName: string
    :param DataSourceName: [REQUIRED]
            A new user-supplied name or description of the DataSource that will replace the current description.
            

    :rtype: dict
    :return: {
        'DataSourceId': 'string'
    }
    
    
    """
    pass

def update_evaluation(EvaluationId=None, EvaluationName=None):
    """
    Updates the EvaluationName of an Evaluation .
    You can use the GetEvaluation operation to view the contents of the updated data element.
    See also: AWS API Documentation
    
    
    :example: response = client.update_evaluation(
        EvaluationId='string',
        EvaluationName='string'
    )
    
    
    :type EvaluationId: string
    :param EvaluationId: [REQUIRED]
            The ID assigned to the Evaluation during creation.
            

    :type EvaluationName: string
    :param EvaluationName: [REQUIRED]
            A new user-supplied name or description of the Evaluation that will replace the current content.
            

    :rtype: dict
    :return: {
        'EvaluationId': 'string'
    }
    
    
    """
    pass

def update_ml_model(MLModelId=None, MLModelName=None, ScoreThreshold=None):
    """
    Updates the MLModelName and the ScoreThreshold of an MLModel .
    You can use the GetMLModel operation to view the contents of the updated data element.
    See also: AWS API Documentation
    
    
    :example: response = client.update_ml_model(
        MLModelId='string',
        MLModelName='string',
        ScoreThreshold=...
    )
    
    
    :type MLModelId: string
    :param MLModelId: [REQUIRED]
            The ID assigned to the MLModel during creation.
            

    :type MLModelName: string
    :param MLModelName: A user-supplied name or description of the MLModel .

    :type ScoreThreshold: float
    :param ScoreThreshold: The ScoreThreshold used in binary classification MLModel that marks the boundary between a positive prediction and a negative prediction.
            Output values greater than or equal to the ScoreThreshold receive a positive result from the MLModel , such as true . Output values less than the ScoreThreshold receive a negative response from the MLModel , such as false .
            

    :rtype: dict
    :return: {
        'MLModelId': 'string'
    }
    
    
    """
    pass

