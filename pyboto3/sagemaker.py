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

def add_tags(ResourceArn=None, Tags=None):
    """
    Adds or overwrites one or more tags for the specified Amazon SageMaker resource. You can add tags to notebook instances, training jobs, models, endpoint configurations, and endpoints.
    Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags(
        ResourceArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource that you want to tag.
            

    :type Tags: list
    :param Tags: [REQUIRED]
            An array of Tag objects. Each tag is a key-value pair. Only the key parameter is required. If you don't specify a value, Amazon SageMaker sets the value to an empty string.
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
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

def create_endpoint(EndpointName=None, EndpointConfigName=None, Tags=None):
    """
    Creates an endpoint using the endpoint configuration specified in the request. Amazon SageMaker uses the endpoint to provision resources and deploy models. You create the endpoint configuration with the CreateEndpointConfig API.
    The endpoint name must be unique within an AWS Region in your AWS account.
    When it receives the request, Amazon SageMaker creates the endpoint, launches the resources (ML compute instances), and deploys the model(s) on them.
    When Amazon SageMaker receives the request, it sets the endpoint status to Creating . After it creates the endpoint, it sets the status to InService . Amazon SageMaker can then process incoming requests for inferences. To check the status of an endpoint, use the DescribeEndpoint API.
    For an example, see Exercise 1: Using the K-Means Algorithm Provided by Amazon SageMaker .
    See also: AWS API Documentation
    
    
    :example: response = client.create_endpoint(
        EndpointName='string',
        EndpointConfigName='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of the endpoint. The name must be unique within an AWS Region in your AWS account.
            

    :type EndpointConfigName: string
    :param EndpointConfigName: [REQUIRED]
            The name of an endpoint configuration. For more information, see CreateEndpointConfig .
            

    :type Tags: list
    :param Tags: An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :rtype: dict
    :return: {
        'EndpointArn': 'string'
    }
    
    
    """
    pass

def create_endpoint_config(EndpointConfigName=None, ProductionVariants=None, Tags=None, KmsKeyId=None):
    """
    Creates an endpoint configuration that Amazon SageMaker hosting services uses to deploy models. In the configuration, you identify one or more models, created using the CreateModel API, to deploy and the resources that you want Amazon SageMaker to provision. Then you call the CreateEndpoint API.
    In the request, you define one or more ProductionVariant s, each of which identifies a model. Each ProductionVariant parameter also describes the resources that you want Amazon SageMaker to provision. This includes the number and type of ML compute instances to deploy.
    If you are hosting multiple models, you also assign a VariantWeight to specify how much traffic you want to allocate to each model. For example, suppose that you want to host two models, A and B, and you assign traffic weight 2 for model A and 1 for model B. Amazon SageMaker distributes two-thirds of the traffic to Model A, and one-third to model B.
    See also: AWS API Documentation
    
    
    :example: response = client.create_endpoint_config(
        EndpointConfigName='string',
        ProductionVariants=[
            {
                'VariantName': 'string',
                'ModelName': 'string',
                'InitialInstanceCount': 123,
                'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                'InitialVariantWeight': ...
            },
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        KmsKeyId='string'
    )
    
    
    :type EndpointConfigName: string
    :param EndpointConfigName: [REQUIRED]
            The name of the endpoint configuration. You specify this name in a CreateEndpoint request.
            

    :type ProductionVariants: list
    :param ProductionVariants: [REQUIRED]
            An array of ProductionVariant objects, one for each model that you want to host at this endpoint.
            (dict) --Identifies a model that you want to host and the resources to deploy for hosting it. If you are deploying multiple models, tell Amazon SageMaker how to distribute traffic among the models by specifying variant weights.
            VariantName (string) -- [REQUIRED]The name of the production variant.
            ModelName (string) -- [REQUIRED]The name of the model that you want to host. This is the name that you specified when creating the model.
            InitialInstanceCount (integer) -- [REQUIRED]Number of instances to launch initially.
            InstanceType (string) -- [REQUIRED]The ML compute instance type.
            InitialVariantWeight (float) --Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the VariantWeight to the sum of all VariantWeight values across all ProductionVariants. If unspecified, it defaults to 1.0.
            
            

    :type Tags: list
    :param Tags: An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :type KmsKeyId: string
    :param KmsKeyId: The Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.

    :rtype: dict
    :return: {
        'EndpointConfigArn': 'string'
    }
    
    
    """
    pass

def create_model(ModelName=None, PrimaryContainer=None, ExecutionRoleArn=None, Tags=None):
    """
    Creates a model in Amazon SageMaker. In the request, you name the model and describe one or more containers. For each container, you specify the docker image containing inference code, artifacts (from prior training), and custom environment map that the inference code uses when you deploy the model into production.
    Use this API to create a model only if you want to use Amazon SageMaker hosting services. To host your model, you create an endpoint configuration with the CreateEndpointConfig API, and then create an endpoint with the CreateEndpoint API.
    Amazon SageMaker then deploys all of the containers that you defined for the model in the hosting environment.
    In the CreateModel request, you must define a container with the PrimaryContainer parameter.
    In the request, you also provide an IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute hosting instances. In addition, you also use the IAM role to manage permissions the inference code needs. For example, if the inference code access any other AWS resources, you grant necessary permissions via this role.
    See also: AWS API Documentation
    
    
    :example: response = client.create_model(
        ModelName='string',
        PrimaryContainer={
            'ContainerHostname': 'string',
            'Image': 'string',
            'ModelDataUrl': 'string',
            'Environment': {
                'string': 'string'
            }
        },
        ExecutionRoleArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ModelName: string
    :param ModelName: [REQUIRED]
            The name of the new model.
            

    :type PrimaryContainer: dict
    :param PrimaryContainer: [REQUIRED]
            The location of the primary docker image containing inference code, associated artifacts, and custom environment map that the inference code uses when the model is deployed into production.
            ContainerHostname (string) --The DNS host name for the container after Amazon SageMaker deploys it.
            Image (string) -- [REQUIRED]The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. For more information, see Using Your Own Algorithms with Amazon SageMaker
            ModelDataUrl (string) --The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).
            Environment (dict) --The environment variables to set in the Docker container. Each key and value in the Environment string to string map can have length of up to 1024. We support up to 16 entries in the map.
            (string) --
            (string) --
            
            

    :type ExecutionRoleArn: string
    :param ExecutionRoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute instances. Deploying on ML compute instances is part of model hosting. For more information, see Amazon SageMaker Roles .
            

    :type Tags: list
    :param Tags: An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :rtype: dict
    :return: {
        'ModelArn': 'string'
    }
    
    
    """
    pass

def create_notebook_instance(NotebookInstanceName=None, InstanceType=None, SubnetId=None, SecurityGroupIds=None, RoleArn=None, KmsKeyId=None, Tags=None, LifecycleConfigName=None, DirectInternetAccess=None):
    """
    Creates an Amazon SageMaker notebook instance. A notebook instance is a machine learning (ML) compute instance running on a Jupyter notebook.
    In a CreateNotebookInstance request, specify the type of ML compute instance that you want to run. Amazon SageMaker launches the instance, installs common libraries that you can use to explore datasets for model training, and attaches an ML storage volume to the notebook instance.
    Amazon SageMaker also provides a set of example notebooks. Each notebook demonstrates how to use Amazon SageMaker with a specific algorithm or with a machine learning framework.
    After receiving the request, Amazon SageMaker does the following:
    After creating the notebook instance, Amazon SageMaker returns its Amazon Resource Name (ARN).
    After Amazon SageMaker creates the notebook instance, you can connect to the Jupyter server and work in Jupyter notebooks. For example, you can write code to explore a dataset that you can use for model training, train a model, host models by creating Amazon SageMaker endpoints, and validate hosted models.
    For more information, see How It Works .
    See also: AWS API Documentation
    
    
    :example: response = client.create_notebook_instance(
        NotebookInstanceName='string',
        InstanceType='ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
        SubnetId='string',
        SecurityGroupIds=[
            'string',
        ],
        RoleArn='string',
        KmsKeyId='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        LifecycleConfigName='string',
        DirectInternetAccess='Enabled'|'Disabled'
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the new notebook instance.
            

    :type InstanceType: string
    :param InstanceType: [REQUIRED]
            The type of ML compute instance to launch for the notebook instance.
            

    :type SubnetId: string
    :param SubnetId: The ID of the subnet in a VPC to which you would like to have a connectivity from your ML compute instance.

    :type SecurityGroupIds: list
    :param SecurityGroupIds: The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet.
            (string) --
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            When you send any requests to AWS resources from the notebook instance, Amazon SageMaker assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so Amazon SageMaker can perform these tasks. The policy must allow the Amazon SageMaker service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see Amazon SageMaker Roles .
            

    :type KmsKeyId: string
    :param KmsKeyId: If you provide a AWS KMS key ID, Amazon SageMaker uses it to encrypt data at rest on the ML storage volume that is attached to your notebook instance.

    :type Tags: list
    :param Tags: A list of tags to associate with the notebook instance. You can add tags later by using the CreateTags API.
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :type LifecycleConfigName: string
    :param LifecycleConfigName: The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see notebook-lifecycle-config .

    :type DirectInternetAccess: string
    :param DirectInternetAccess: Sets whether Amazon SageMaker provides internet access to the notebook instance. If you set this to Disabled this notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.
            For more information, see appendix-notebook-and-internet-access . You can set the value of this parameter to Disabled only if you set a value for the SubnetId parameter.
            

    :rtype: dict
    :return: {
        'NotebookInstanceArn': 'string'
    }
    
    
    :returns: 
    NotebookInstanceName (string) -- [REQUIRED]
    The name of the new notebook instance.
    
    InstanceType (string) -- [REQUIRED]
    The type of ML compute instance to launch for the notebook instance.
    
    SubnetId (string) -- The ID of the subnet in a VPC to which you would like to have a connectivity from your ML compute instance.
    SecurityGroupIds (list) -- The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet.
    
    (string) --
    
    
    RoleArn (string) -- [REQUIRED]
    When you send any requests to AWS resources from the notebook instance, Amazon SageMaker assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so Amazon SageMaker can perform these tasks. The policy must allow the Amazon SageMaker service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see Amazon SageMaker Roles .
    
    KmsKeyId (string) -- If you provide a AWS KMS key ID, Amazon SageMaker uses it to encrypt data at rest on the ML storage volume that is attached to your notebook instance.
    Tags (list) -- A list of tags to associate with the notebook instance. You can add tags later by using the CreateTags API.
    
    (dict) --Describes a tag.
    
    Key (string) -- [REQUIRED]The tag key.
    
    Value (string) -- [REQUIRED]The tag value.
    
    
    
    
    
    LifecycleConfigName (string) -- The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see  notebook-lifecycle-config .
    DirectInternetAccess (string) -- Sets whether Amazon SageMaker provides internet access to the notebook instance. If you set this to Disabled this notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.
    For more information, see  appendix-notebook-and-internet-access . You can set the value of this parameter to Disabled only if you set a value for the SubnetId parameter.
    
    
    """
    pass

def create_notebook_instance_lifecycle_config(NotebookInstanceLifecycleConfigName=None, OnCreate=None, OnStart=None):
    """
    Creates a lifecycle configuration that you can associate with a notebook instance. A lifecycle configuration is a collection of shell scripts that run when you create or start a notebook instance.
    Each lifecycle configuration script has a limit of 16384 characters.
    The value of the $PATH environment variable that is available to both scripts is /sbin:bin:/usr/sbin:/usr/bin .
    View CloudWatch Logs for notebook instance lifecycle configurations in log group /aws/sagemaker/NotebookInstances in log stream [notebook-instance-name]/[LifecycleConfigHook] .
    Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
    For information about notebook instance lifestyle configurations, see  notebook-lifecycle-config .
    See also: AWS API Documentation
    
    
    :example: response = client.create_notebook_instance_lifecycle_config(
        NotebookInstanceLifecycleConfigName='string',
        OnCreate=[
            {
                'Content': 'string'
            },
        ],
        OnStart=[
            {
                'Content': 'string'
            },
        ]
    )
    
    
    :type NotebookInstanceLifecycleConfigName: string
    :param NotebookInstanceLifecycleConfigName: [REQUIRED]
            The name of the lifecycle configuration.
            

    :type OnCreate: list
    :param OnCreate: A shell script that runs only once, when you create a notebook instance.
            (dict) --Contains the notebook instance lifecycle configuration script.
            Each lifecycle configuration script has a limit of 16384 characters.
            The value of the $PATH environment variable that is available to both scripts is /sbin:bin:/usr/sbin:/usr/bin .
            View CloudWatch Logs for notebook instance lifecycle configurations in log group /aws/sagemaker/NotebookInstances in log stream [notebook-instance-name]/[LifecycleConfigHook] .
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
            For information about notebook instance lifestyle configurations, see notebook-lifecycle-config .
            Content (string) --A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
            
            

    :type OnStart: list
    :param OnStart: A shell script that runs every time you start a notebook instance, including when you create the notebook instance.
            (dict) --Contains the notebook instance lifecycle configuration script.
            Each lifecycle configuration script has a limit of 16384 characters.
            The value of the $PATH environment variable that is available to both scripts is /sbin:bin:/usr/sbin:/usr/bin .
            View CloudWatch Logs for notebook instance lifecycle configurations in log group /aws/sagemaker/NotebookInstances in log stream [notebook-instance-name]/[LifecycleConfigHook] .
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
            For information about notebook instance lifestyle configurations, see notebook-lifecycle-config .
            Content (string) --A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
            
            

    :rtype: dict
    :return: {
        'NotebookInstanceLifecycleConfigArn': 'string'
    }
    
    
    """
    pass

def create_presigned_notebook_instance_url(NotebookInstanceName=None, SessionExpirationDurationInSeconds=None):
    """
    Returns a URL that you can use to connect to the Juypter server from a notebook instance. In the Amazon SageMaker console, when you choose Open next to a notebook instance, Amazon SageMaker opens a new tab showing the Jupyter server home page from the notebook instance. The console uses this API to get the URL and show the page.
    See also: AWS API Documentation
    
    
    :example: response = client.create_presigned_notebook_instance_url(
        NotebookInstanceName='string',
        SessionExpirationDurationInSeconds=123
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the notebook instance.
            

    :type SessionExpirationDurationInSeconds: integer
    :param SessionExpirationDurationInSeconds: The duration of the session, in seconds. The default is 12 hours.

    :rtype: dict
    :return: {
        'AuthorizedUrl': 'string'
    }
    
    
    """
    pass

def create_training_job(TrainingJobName=None, HyperParameters=None, AlgorithmSpecification=None, RoleArn=None, InputDataConfig=None, OutputDataConfig=None, ResourceConfig=None, StoppingCondition=None, Tags=None):
    """
    Starts a model training job. After training completes, Amazon SageMaker saves the resulting model artifacts to an Amazon S3 location that you specify.
    If you choose to host your model using Amazon SageMaker hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts in a deep learning service other than Amazon SageMaker, provided that you know how to use them for inferences.
    In the request body, you provide the following:
    For more information about Amazon SageMaker, see How It Works .
    See also: AWS API Documentation
    
    
    :example: response = client.create_training_job(
        TrainingJobName='string',
        HyperParameters={
            'string': 'string'
        },
        AlgorithmSpecification={
            'TrainingImage': 'string',
            'TrainingInputMode': 'Pipe'|'File'
        },
        RoleArn='string',
        InputDataConfig=[
            {
                'ChannelName': 'string',
                'DataSource': {
                    'S3DataSource': {
                        'S3DataType': 'ManifestFile'|'S3Prefix',
                        'S3Uri': 'string',
                        'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key'
                    }
                },
                'ContentType': 'string',
                'CompressionType': 'None'|'Gzip',
                'RecordWrapperType': 'None'|'RecordIO'
            },
        ],
        OutputDataConfig={
            'KmsKeyId': 'string',
            'S3OutputPath': 'string'
        },
        ResourceConfig={
            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
            'InstanceCount': 123,
            'VolumeSizeInGB': 123,
            'VolumeKmsKeyId': 'string'
        },
        StoppingCondition={
            'MaxRuntimeInSeconds': 123
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type TrainingJobName: string
    :param TrainingJobName: [REQUIRED]
            The name of the training job. The name must be unique within an AWS Region in an AWS account. It appears in the Amazon SageMaker console.
            

    :type HyperParameters: dict
    :param HyperParameters: Algorithm-specific parameters. You set hyperparameters before you start the learning process. Hyperparameters influence the quality of the model. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see Algorithms .
            You can specify a maximum of 100 hyperparameters. Each hyperparameter is a key-value pair. Each key and value is limited to 256 characters, as specified by the Length Constraint .
            (string) --
            (string) --
            

    :type AlgorithmSpecification: dict
    :param AlgorithmSpecification: [REQUIRED]
            The registry path of the Docker image that contains the training algorithm and algorithm-specific metadata, including the input mode. For more information about algorithms provided by Amazon SageMaker, see Algorithms . For information about providing your own algorithms, see your-algorithms .
            TrainingImage (string) -- [REQUIRED]The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for built-in algorithms, see sagemaker-algo-docker-registry-paths .
            TrainingInputMode (string) -- [REQUIRED]The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see Algorithms . If an algorithm supports the File input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the Pipe input mode, Amazon SageMaker streams data directly from S3 to the container.
            In File mode, make sure you provision ML storage volume with sufficient capacity to accommodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any.
            For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training.
            

    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
            During model training, Amazon SageMaker needs your permission to read input data from an S3 bucket, download a Docker image that contains training code, write model artifacts to an S3 bucket, write logs to Amazon CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant permissions for all of these tasks to an IAM role. For more information, see Amazon SageMaker Roles .
            

    :type InputDataConfig: list
    :param InputDataConfig: [REQUIRED]
            An array of Channel objects. Each channel is a named input source. InputDataConfig describes the input data and its location.
            Algorithms can accept input data from one or more channels. For example, an algorithm might have two channels of input data, training_data and validation_data . The configuration for each channel provides the S3 location where the input data is stored. It also provides information about the stored data: the MIME type, compression method, and whether the data is wrapped in RecordIO format.
            Depending on the input mode that the algorithm supports, Amazon SageMaker either copies input data files from an S3 bucket to a local directory in the Docker container, or makes it available as input streams.
            (dict) --A channel is a named input source that training algorithms can consume.
            ChannelName (string) -- [REQUIRED]The name of the channel.
            DataSource (dict) -- [REQUIRED]The location of the channel data.
            S3DataSource (dict) -- [REQUIRED]The S3 location of the data source that is associated with a channel.
            S3DataType (string) -- [REQUIRED]If you choose S3Prefix , S3Uri identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for model training.
            If you choose ManifestFile , S3Uri identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training.
            S3Uri (string) -- [REQUIRED]Depending on the value specified for the S3DataType , identifies either a key name prefix or a manifest. For example:
            A key name prefix might look like this: s3://bucketname/exampleprefix .
            A manifest might look like this: s3://bucketname/example.manifest  The manifest is an S3 object which is a JSON file with the following format:  [ {'prefix': 's3://customer_bucket/some/prefix/'}, 'relative/path/to/custdata-1', 'relative/path/custdata-2', ... ]  The preceding JSON matches the following s3Uris :  s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-1 ...  The complete set of s3uris in this manifest constitutes the input data for the channel for this datasource. The object that each s3uris points to must readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
            S3DataDistributionType (string) --If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify FullyReplicated .
            If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ShardedByS3Key . If there are n ML compute instances launched for a training job, each instance gets approximately 1/n of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.
            Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both FILE and PIPE modes. Keep this in mind when developing algorithms.
            In distributed training, where you use multiple ML compute EC2 instances, you might choose ShardedByS3Key . If the algorithm requires copying training data to the ML storage volume (when TrainingInputMode is set to File ), this copies 1/n of the number of objects.
            
            ContentType (string) --The MIME type of the data.
            CompressionType (string) --If training data is compressed, the compression type. The default value is None . CompressionType is used only in PIPE input mode. In FILE mode, leave this field unset or set it to None.
            RecordWrapperType (string) --Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format, in which caseAmazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see Create a Dataset Using RecordIO .
            In FILE mode, leave this field unset or set it to None.
            
            

    :type OutputDataConfig: dict
    :param OutputDataConfig: [REQUIRED]
            Specifies the path to the S3 bucket where you want to store model artifacts. Amazon SageMaker creates subfolders for the artifacts.
            KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
            Note
            If the configuration of the output S3 bucket requires server-side encryption for objects, and you don't provide the KMS key ID, Amazon SageMaker uses the default service key. For more information, see KMS-Managed Encryption Keys in Amazon Simple Storage Service developer guide.
            Note
            The KMS key policy must grant permission to the IAM role you specify in your CreateTrainingJob request. Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide.
            S3OutputPath (string) -- [REQUIRED]Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, s3://bucket-name/key-name-prefix .
            

    :type ResourceConfig: dict
    :param ResourceConfig: [REQUIRED]
            The resources, including the ML compute instances and ML storage volumes, to use for model training.
            ML storage volumes store model artifacts and incremental states. Training algorithms might also use ML storage volumes for scratch space. If you want Amazon SageMaker to use the ML storage volume to store the training data, choose File as the TrainingInputMode in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.
            InstanceType (string) -- [REQUIRED]The ML compute instance type.
            InstanceCount (integer) -- [REQUIRED]The number of ML compute instances to use. For distributed training, provide a value greater than 1.
            VolumeSizeInGB (integer) -- [REQUIRED]The size of the ML storage volume that you want to provision.
            ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose File as the TrainingInputMode in the algorithm specification.
            You must specify sufficient ML storage for your scenario.
            Note
            Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type.
            VolumeKmsKeyId (string) --The Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.
            

    :type StoppingCondition: dict
    :param StoppingCondition: [REQUIRED]
            Sets a duration for training. Use this parameter to cap model training costs. To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
            When Amazon SageMaker terminates a job because the stopping condition has been met, training algorithms provided by Amazon SageMaker save the intermediate results of the job. This intermediate data is a valid model artifact. You can use it to create a model using the CreateModel API.
            MaxRuntimeInSeconds (integer) --The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
            

    :type Tags: list
    :param Tags: An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
            (dict) --Describes a tag.
            Key (string) -- [REQUIRED]The tag key.
            Value (string) -- [REQUIRED]The tag value.
            
            

    :rtype: dict
    :return: {
        'TrainingJobArn': 'string'
    }
    
    
    :returns: 
    TrainingJobName (string) -- [REQUIRED]
    The name of the training job. The name must be unique within an AWS Region in an AWS account. It appears in the Amazon SageMaker console.
    
    HyperParameters (dict) -- Algorithm-specific parameters. You set hyperparameters before you start the learning process. Hyperparameters influence the quality of the model. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see Algorithms .
    You can specify a maximum of 100 hyperparameters. Each hyperparameter is a key-value pair. Each key and value is limited to 256 characters, as specified by the Length Constraint .
    
    (string) --
    (string) --
    
    
    
    
    AlgorithmSpecification (dict) -- [REQUIRED]
    The registry path of the Docker image that contains the training algorithm and algorithm-specific metadata, including the input mode. For more information about algorithms provided by Amazon SageMaker, see Algorithms . For information about providing your own algorithms, see  your-algorithms .
    
    TrainingImage (string) -- [REQUIRED]The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for built-in algorithms, see  sagemaker-algo-docker-registry-paths .
    
    TrainingInputMode (string) -- [REQUIRED]The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see Algorithms . If an algorithm supports the File input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the Pipe input mode, Amazon SageMaker streams data directly from S3 to the container.
    In File mode, make sure you provision ML storage volume with sufficient capacity to accommodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any.
    For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training.
    
    
    
    RoleArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
    During model training, Amazon SageMaker needs your permission to read input data from an S3 bucket, download a Docker image that contains training code, write model artifacts to an S3 bucket, write logs to Amazon CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant permissions for all of these tasks to an IAM role. For more information, see Amazon SageMaker Roles .
    
    InputDataConfig (list) -- [REQUIRED]
    An array of Channel objects. Each channel is a named input source. InputDataConfig describes the input data and its location.
    Algorithms can accept input data from one or more channels. For example, an algorithm might have two channels of input data, training_data and validation_data . The configuration for each channel provides the S3 location where the input data is stored. It also provides information about the stored data: the MIME type, compression method, and whether the data is wrapped in RecordIO format.
    Depending on the input mode that the algorithm supports, Amazon SageMaker either copies input data files from an S3 bucket to a local directory in the Docker container, or makes it available as input streams.
    
    (dict) --A channel is a named input source that training algorithms can consume.
    
    ChannelName (string) -- [REQUIRED]The name of the channel.
    
    DataSource (dict) -- [REQUIRED]The location of the channel data.
    
    S3DataSource (dict) -- [REQUIRED]The S3 location of the data source that is associated with a channel.
    
    S3DataType (string) -- [REQUIRED]If you choose S3Prefix , S3Uri identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for model training.
    If you choose ManifestFile , S3Uri identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training.
    
    S3Uri (string) -- [REQUIRED]Depending on the value specified for the S3DataType , identifies either a key name prefix or a manifest. For example:
    
    A key name prefix might look like this: s3://bucketname/exampleprefix .
    A manifest might look like this: s3://bucketname/example.manifest   The manifest is an S3 object which is a JSON file with the following format:   [ {"prefix": "s3://customer_bucket/some/prefix/"}, "relative/path/to/custdata-1", "relative/path/custdata-2", ... ]   The preceding JSON matches the following s3Uris :   s3://customer_bucket/some/prefix/relative/path/to/custdata-1 s3://customer_bucket/some/prefix/relative/path/custdata-1 ...   The complete set of s3uris in this manifest constitutes the input data for the channel for this datasource. The object that each s3uris points to must readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.
    
    
    S3DataDistributionType (string) --If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify FullyReplicated .
    If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ShardedByS3Key . If there are n ML compute instances launched for a training job, each instance gets approximately 1/n of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.
    Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both FILE and PIPE modes. Keep this in mind when developing algorithms.
    In distributed training, where you use multiple ML compute EC2 instances, you might choose ShardedByS3Key . If the algorithm requires copying training data to the ML storage volume (when TrainingInputMode is set to File ), this copies 1/n of the number of objects.
    
    
    
    
    
    ContentType (string) --The MIME type of the data.
    
    CompressionType (string) --If training data is compressed, the compression type. The default value is None . CompressionType is used only in PIPE input mode. In FILE mode, leave this field unset or set it to None.
    
    RecordWrapperType (string) --Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format, in which caseAmazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see Create a Dataset Using RecordIO .
    In FILE mode, leave this field unset or set it to None.
    
    
    
    
    
    OutputDataConfig (dict) -- [REQUIRED]
    Specifies the path to the S3 bucket where you want to store model artifacts. Amazon SageMaker creates subfolders for the artifacts.
    
    KmsKeyId (string) --The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
    
    Note
    If the configuration of the output S3 bucket requires server-side encryption for objects, and you don't provide the KMS key ID, Amazon SageMaker uses the default service key. For more information, see KMS-Managed Encryption Keys in Amazon Simple Storage Service developer guide.
    
    
    Note
    The KMS key policy must grant permission to the IAM role you specify in your CreateTrainingJob request. Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide.
    
    
    S3OutputPath (string) -- [REQUIRED]Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, s3://bucket-name/key-name-prefix .
    
    
    
    ResourceConfig (dict) -- [REQUIRED]
    The resources, including the ML compute instances and ML storage volumes, to use for model training.
    ML storage volumes store model artifacts and incremental states. Training algorithms might also use ML storage volumes for scratch space. If you want Amazon SageMaker to use the ML storage volume to store the training data, choose File as the TrainingInputMode in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.
    
    InstanceType (string) -- [REQUIRED]The ML compute instance type.
    
    InstanceCount (integer) -- [REQUIRED]The number of ML compute instances to use. For distributed training, provide a value greater than 1.
    
    VolumeSizeInGB (integer) -- [REQUIRED]The size of the ML storage volume that you want to provision.
    ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose File as the TrainingInputMode in the algorithm specification.
    You must specify sufficient ML storage for your scenario.
    
    Note
    Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type.
    
    
    VolumeKmsKeyId (string) --The Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.
    
    
    
    StoppingCondition (dict) -- [REQUIRED]
    Sets a duration for training. Use this parameter to cap model training costs. To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts.
    When Amazon SageMaker terminates a job because the stopping condition has been met, training algorithms provided by Amazon SageMaker save the intermediate results of the job. This intermediate data is a valid model artifact. You can use it to create a model using the CreateModel API.
    
    MaxRuntimeInSeconds (integer) --The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.
    
    
    
    Tags (list) -- An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide .
    
    (dict) --Describes a tag.
    
    Key (string) -- [REQUIRED]The tag key.
    
    Value (string) -- [REQUIRED]The tag value.
    
    
    
    
    
    
    """
    pass

def delete_endpoint(EndpointName=None):
    """
    Deletes an endpoint. Amazon SageMaker frees up all of the resources that were deployed when the endpoint was created.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_endpoint(
        EndpointName='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of the endpoint that you want to delete.
            

    """
    pass

def delete_endpoint_config(EndpointConfigName=None):
    """
    Deletes an endpoint configuration. The DeleteEndpoingConfig API deletes only the specified configuration. It does not delete endpoints created using the configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_endpoint_config(
        EndpointConfigName='string'
    )
    
    
    :type EndpointConfigName: string
    :param EndpointConfigName: [REQUIRED]
            The name of the endpoint configuration that you want to delete.
            

    """
    pass

def delete_model(ModelName=None):
    """
    Deletes a model. The DeleteModel API deletes only the model entry that was created in Amazon SageMaker when you called the CreateModel API. It does not delete model artifacts, inference code, or the IAM role that you specified when creating the model.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_model(
        ModelName='string'
    )
    
    
    :type ModelName: string
    :param ModelName: [REQUIRED]
            The name of the model to delete.
            

    """
    pass

def delete_notebook_instance(NotebookInstanceName=None):
    """
    Deletes an Amazon SageMaker notebook instance. Before you can delete a notebook instance, you must call the StopNotebookInstance API.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_notebook_instance(
        NotebookInstanceName='string'
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the Amazon SageMaker notebook instance to delete.
            

    """
    pass

def delete_notebook_instance_lifecycle_config(NotebookInstanceLifecycleConfigName=None):
    """
    Deletes a notebook instance lifecycle configuration.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_notebook_instance_lifecycle_config(
        NotebookInstanceLifecycleConfigName='string'
    )
    
    
    :type NotebookInstanceLifecycleConfigName: string
    :param NotebookInstanceLifecycleConfigName: [REQUIRED]
            The name of the lifecycle configuration to delete.
            

    """
    pass

def delete_tags(ResourceArn=None, TagKeys=None):
    """
    Deletes the specified tags from an Amazon SageMaker resource.
    To list a resource's tags, use the ListTags API.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_tags(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource whose tags you want to delete.
            

    :type TagKeys: list
    :param TagKeys: [REQUIRED]
            An array or one or more tag keys to delete.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_endpoint(EndpointName=None):
    """
    Returns the description of an endpoint.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_endpoint(
        EndpointName='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of the endpoint.
            

    :rtype: dict
    :return: {
        'EndpointName': 'string',
        'EndpointArn': 'string',
        'EndpointConfigName': 'string',
        'ProductionVariants': [
            {
                'VariantName': 'string',
                'CurrentWeight': ...,
                'DesiredWeight': ...,
                'CurrentInstanceCount': 123,
                'DesiredInstanceCount': 123
            },
        ],
        'EndpointStatus': 'OutOfService'|'Creating'|'Updating'|'RollingBack'|'InService'|'Deleting'|'Failed',
        'FailureReason': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_endpoint_config(EndpointConfigName=None):
    """
    Returns the description of an endpoint configuration created using the CreateEndpointConfig API.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_endpoint_config(
        EndpointConfigName='string'
    )
    
    
    :type EndpointConfigName: string
    :param EndpointConfigName: [REQUIRED]
            The name of the endpoint configuration.
            

    :rtype: dict
    :return: {
        'EndpointConfigName': 'string',
        'EndpointConfigArn': 'string',
        'ProductionVariants': [
            {
                'VariantName': 'string',
                'ModelName': 'string',
                'InitialInstanceCount': 123,
                'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.large'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.large'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                'InitialVariantWeight': ...
            },
        ],
        'KmsKeyId': 'string',
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_model(ModelName=None):
    """
    Describes a model that you created using the CreateModel API.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_model(
        ModelName='string'
    )
    
    
    :type ModelName: string
    :param ModelName: [REQUIRED]
            The name of the model.
            

    :rtype: dict
    :return: {
        'ModelName': 'string',
        'PrimaryContainer': {
            'ContainerHostname': 'string',
            'Image': 'string',
            'ModelDataUrl': 'string',
            'Environment': {
                'string': 'string'
            }
        },
        'ExecutionRoleArn': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'ModelArn': 'string'
    }
    
    
    """
    pass

def describe_notebook_instance(NotebookInstanceName=None):
    """
    Returns information about a notebook instance.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_notebook_instance(
        NotebookInstanceName='string'
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the notebook instance that you want information about.
            

    :rtype: dict
    :return: {
        'NotebookInstanceArn': 'string',
        'NotebookInstanceName': 'string',
        'NotebookInstanceStatus': 'Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting',
        'FailureReason': 'string',
        'Url': 'string',
        'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
        'SubnetId': 'string',
        'SecurityGroups': [
            'string',
        ],
        'RoleArn': 'string',
        'KmsKeyId': 'string',
        'NetworkInterfaceId': 'string',
        'LastModifiedTime': datetime(2015, 1, 1),
        'CreationTime': datetime(2015, 1, 1),
        'NotebookInstanceLifecycleConfigName': 'string',
        'DirectInternetAccess': 'Enabled'|'Disabled'
    }
    
    
    """
    pass

def describe_notebook_instance_lifecycle_config(NotebookInstanceLifecycleConfigName=None):
    """
    Returns a description of a notebook instance lifecycle configuration.
    For information about notebook instance lifestyle configurations, see  notebook-lifecycle-config .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_notebook_instance_lifecycle_config(
        NotebookInstanceLifecycleConfigName='string'
    )
    
    
    :type NotebookInstanceLifecycleConfigName: string
    :param NotebookInstanceLifecycleConfigName: [REQUIRED]
            The name of the lifecycle configuration to describe.
            

    :rtype: dict
    :return: {
        'NotebookInstanceLifecycleConfigArn': 'string',
        'NotebookInstanceLifecycleConfigName': 'string',
        'OnCreate': [
            {
                'Content': 'string'
            },
        ],
        'OnStart': [
            {
                'Content': 'string'
            },
        ],
        'LastModifiedTime': datetime(2015, 1, 1),
        'CreationTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_training_job(TrainingJobName=None):
    """
    Returns information about a training job.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_training_job(
        TrainingJobName='string'
    )
    
    
    :type TrainingJobName: string
    :param TrainingJobName: [REQUIRED]
            The name of the training job.
            

    :rtype: dict
    :return: {
        'TrainingJobName': 'string',
        'TrainingJobArn': 'string',
        'ModelArtifacts': {
            'S3ModelArtifacts': 'string'
        },
        'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
        'SecondaryStatus': 'Starting'|'Downloading'|'Training'|'Uploading'|'Stopping'|'Stopped'|'MaxRuntimeExceeded'|'Completed'|'Failed',
        'FailureReason': 'string',
        'HyperParameters': {
            'string': 'string'
        },
        'AlgorithmSpecification': {
            'TrainingImage': 'string',
            'TrainingInputMode': 'Pipe'|'File'
        },
        'RoleArn': 'string',
        'InputDataConfig': [
            {
                'ChannelName': 'string',
                'DataSource': {
                    'S3DataSource': {
                        'S3DataType': 'ManifestFile'|'S3Prefix',
                        'S3Uri': 'string',
                        'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key'
                    }
                },
                'ContentType': 'string',
                'CompressionType': 'None'|'Gzip',
                'RecordWrapperType': 'None'|'RecordIO'
            },
        ],
        'OutputDataConfig': {
            'KmsKeyId': 'string',
            'S3OutputPath': 'string'
        },
        'ResourceConfig': {
            'InstanceType': 'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.m5.large'|'ml.m5.xlarge'|'ml.m5.2xlarge'|'ml.m5.4xlarge'|'ml.m5.12xlarge'|'ml.m5.24xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.4xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
            'InstanceCount': 123,
            'VolumeSizeInGB': 123,
            'VolumeKmsKeyId': 'string'
        },
        'StoppingCondition': {
            'MaxRuntimeInSeconds': 123
        },
        'CreationTime': datetime(2015, 1, 1),
        'TrainingStartTime': datetime(2015, 1, 1),
        'TrainingEndTime': datetime(2015, 1, 1),
        'LastModifiedTime': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    MaxRuntimeExceeded - Job stopped as a result of maximum allowed runtime exceeded.
    
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

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_endpoint_configs(SortBy=None, SortOrder=None, NextToken=None, MaxResults=None, NameContains=None, CreationTimeBefore=None, CreationTimeAfter=None):
    """
    Lists endpoint configurations.
    See also: AWS API Documentation
    
    
    :example: response = client.list_endpoint_configs(
        SortBy='Name'|'CreationTime',
        SortOrder='Ascending'|'Descending',
        NextToken='string',
        MaxResults=123,
        NameContains='string',
        CreationTimeBefore=datetime(2015, 1, 1),
        CreationTimeAfter=datetime(2015, 1, 1)
    )
    
    
    :type SortBy: string
    :param SortBy: The field to sort results by. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :type NextToken: string
    :param NextToken: If the result of the previous ListEndpointConfig request was truncated, the response includes a NextToken . To retrieve the next set of endpoint configurations, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of training jobs to return in the response.

    :type NameContains: string
    :param NameContains: A string in the endpoint configuration name. This filter returns only endpoint configurations whose name contains the specified string.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only endpoint configurations created before the specified time (timestamp).

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only endpoint configurations created after the specified time (timestamp).

    :rtype: dict
    :return: {
        'EndpointConfigs': [
            {
                'EndpointConfigName': 'string',
                'EndpointConfigArn': 'string',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_endpoints(SortBy=None, SortOrder=None, NextToken=None, MaxResults=None, NameContains=None, CreationTimeBefore=None, CreationTimeAfter=None, LastModifiedTimeBefore=None, LastModifiedTimeAfter=None, StatusEquals=None):
    """
    Lists endpoints.
    See also: AWS API Documentation
    
    
    :example: response = client.list_endpoints(
        SortBy='Name'|'CreationTime'|'Status',
        SortOrder='Ascending'|'Descending',
        NextToken='string',
        MaxResults=123,
        NameContains='string',
        CreationTimeBefore=datetime(2015, 1, 1),
        CreationTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        StatusEquals='OutOfService'|'Creating'|'Updating'|'RollingBack'|'InService'|'Deleting'|'Failed'
    )
    
    
    :type SortBy: string
    :param SortBy: Sorts the list of results. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :type NextToken: string
    :param NextToken: If the result of a ListEndpoints request was truncated, the response includes a NextToken . To retrieve the next set of endpoints, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of endpoints to return in the response.

    :type NameContains: string
    :param NameContains: A string in endpoint names. This filter returns only endpoints whose name contains the specified string.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only endpoints that were created before the specified time (timestamp).

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only endpoints that were created after the specified time (timestamp).

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only endpoints that were modified before the specified timestamp.

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only endpoints that were modified after the specified timestamp.

    :type StatusEquals: string
    :param StatusEquals: A filter that returns only endpoints with the specified status.

    :rtype: dict
    :return: {
        'Endpoints': [
            {
                'EndpointName': 'string',
                'EndpointArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'EndpointStatus': 'OutOfService'|'Creating'|'Updating'|'RollingBack'|'InService'|'Deleting'|'Failed'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_models(SortBy=None, SortOrder=None, NextToken=None, MaxResults=None, NameContains=None, CreationTimeBefore=None, CreationTimeAfter=None):
    """
    Lists models created with the CreateModel API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_models(
        SortBy='Name'|'CreationTime',
        SortOrder='Ascending'|'Descending',
        NextToken='string',
        MaxResults=123,
        NameContains='string',
        CreationTimeBefore=datetime(2015, 1, 1),
        CreationTimeAfter=datetime(2015, 1, 1)
    )
    
    
    :type SortBy: string
    :param SortBy: Sorts the list of results. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :type NextToken: string
    :param NextToken: If the response to a previous ListModels request was truncated, the response includes a NextToken . To retrieve the next set of models, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of models to return in the response.

    :type NameContains: string
    :param NameContains: A string in the training job name. This filter returns only models in the training job whose name contains the specified string.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only models created before the specified time (timestamp).

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only models created after the specified time (timestamp).

    :rtype: dict
    :return: {
        'Models': [
            {
                'ModelName': 'string',
                'ModelArn': 'string',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_notebook_instance_lifecycle_configs(NextToken=None, MaxResults=None, SortBy=None, SortOrder=None, NameContains=None, CreationTimeBefore=None, CreationTimeAfter=None, LastModifiedTimeBefore=None, LastModifiedTimeAfter=None):
    """
    Lists notebook instance lifestyle configurations created with the API.
    See also: AWS API Documentation
    
    
    :example: response = client.list_notebook_instance_lifecycle_configs(
        NextToken='string',
        MaxResults=123,
        SortBy='Name'|'CreationTime'|'LastModifiedTime',
        SortOrder='Ascending'|'Descending',
        NameContains='string',
        CreationTimeBefore=datetime(2015, 1, 1),
        CreationTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1)
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of a ListNotebookInstanceLifecycleConfigs request was truncated, the response includes a NextToken . To get the next set of lifecycle configurations, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of lifecycle configurations to return in the response.

    :type SortBy: string
    :param SortBy: Sorts the list of results. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results.

    :type NameContains: string
    :param NameContains: A string in the lifecycle configuration name. This filter returns only lifecycle configurations whose name contains the specified string.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only lifecycle configurations that were created before the specified time (timestamp).

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only lifecycle configurations that were created after the specified time (timestamp).

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only lifecycle configurations that were modified before the specified time (timestamp).

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only lifecycle configurations that were modified after the specified time (timestamp).

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'NotebookInstanceLifecycleConfigs': [
            {
                'NotebookInstanceLifecycleConfigName': 'string',
                'NotebookInstanceLifecycleConfigArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def list_notebook_instances(NextToken=None, MaxResults=None, SortBy=None, SortOrder=None, NameContains=None, CreationTimeBefore=None, CreationTimeAfter=None, LastModifiedTimeBefore=None, LastModifiedTimeAfter=None, StatusEquals=None, NotebookInstanceLifecycleConfigNameContains=None):
    """
    Returns a list of the Amazon SageMaker notebook instances in the requester's account in an AWS Region.
    See also: AWS API Documentation
    
    
    :example: response = client.list_notebook_instances(
        NextToken='string',
        MaxResults=123,
        SortBy='Name'|'CreationTime'|'Status',
        SortOrder='Ascending'|'Descending',
        NameContains='string',
        CreationTimeBefore=datetime(2015, 1, 1),
        CreationTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        StatusEquals='Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting',
        NotebookInstanceLifecycleConfigNameContains='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If the previous call to the ListNotebookInstances is truncated, the response includes a NextToken . You can use this token in your subsequent ListNotebookInstances request to fetch the next set of notebook instances.
            Note
            You might specify a filter or a sort order in your request. When response is truncated, you must use the same values for the filer and sort order in the next request.
            

    :type MaxResults: integer
    :param MaxResults: The maximum number of notebook instances to return.

    :type SortBy: string
    :param SortBy: The field to sort results by. The default is Name .

    :type SortOrder: string
    :param SortOrder: The sort order for results.

    :type NameContains: string
    :param NameContains: A string in the notebook instances' name. This filter returns only notebook instances whose name contains the specified string.

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only notebook instances that were created before the specified time (timestamp).

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that returns only notebook instances that were created after the specified time (timestamp).

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only notebook instances that were modified before the specified time (timestamp).

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only notebook instances that were modified after the specified time (timestamp).

    :type StatusEquals: string
    :param StatusEquals: A filter that returns only notebook instances with the specified status.

    :type NotebookInstanceLifecycleConfigNameContains: string
    :param NotebookInstanceLifecycleConfigNameContains: A string in the name of a notebook instances lifecycle configuration associated with this notebook instance. This filter returns only notebook instances associated with a lifecycle configuration with a name that contains the specified string.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'NotebookInstances': [
            {
                'NotebookInstanceName': 'string',
                'NotebookInstanceArn': 'string',
                'NotebookInstanceStatus': 'Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting',
                'Url': 'string',
                'InstanceType': 'ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
                'CreationTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'NotebookInstanceLifecycleConfigName': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_tags(ResourceArn=None, NextToken=None, MaxResults=None):
    """
    Returns the tags for the specified Amazon SageMaker resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags(
        ResourceArn='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.
            

    :type NextToken: string
    :param NextToken: If the response to the previous ListTags request is truncated, Amazon SageMaker returns this token. To retrieve the next set of tags, use it in the subsequent request.

    :type MaxResults: integer
    :param MaxResults: Maximum number of tags to return.

    :rtype: dict
    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_training_jobs(NextToken=None, MaxResults=None, CreationTimeAfter=None, CreationTimeBefore=None, LastModifiedTimeAfter=None, LastModifiedTimeBefore=None, NameContains=None, StatusEquals=None, SortBy=None, SortOrder=None):
    """
    Lists training jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.list_training_jobs(
        NextToken='string',
        MaxResults=123,
        CreationTimeAfter=datetime(2015, 1, 1),
        CreationTimeBefore=datetime(2015, 1, 1),
        LastModifiedTimeAfter=datetime(2015, 1, 1),
        LastModifiedTimeBefore=datetime(2015, 1, 1),
        NameContains='string',
        StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
        SortBy='Name'|'CreationTime'|'Status',
        SortOrder='Ascending'|'Descending'
    )
    
    
    :type NextToken: string
    :param NextToken: If the result of the previous ListTrainingJobs request was truncated, the response includes a NextToken . To retrieve the next set of training jobs, use the token in the next request.

    :type MaxResults: integer
    :param MaxResults: The maximum number of training jobs to return in the response.

    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: A filter that only training jobs created after the specified time (timestamp).

    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: A filter that returns only training jobs created before the specified time (timestamp).

    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: A filter that returns only training jobs modified after the specified time (timestamp).

    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: A filter that returns only training jobs modified before the specified time (timestamp).

    :type NameContains: string
    :param NameContains: A string in the training job name. This filter returns only models whose name contains the specified string.

    :type StatusEquals: string
    :param StatusEquals: A filter that retrieves only training jobs with a specific status.

    :type SortBy: string
    :param SortBy: The field to sort results by. The default is CreationTime .

    :type SortOrder: string
    :param SortOrder: The sort order for results. The default is Ascending .

    :rtype: dict
    :return: {
        'TrainingJobSummaries': [
            {
                'TrainingJobName': 'string',
                'TrainingJobArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TrainingEndTime': datetime(2015, 1, 1),
                'LastModifiedTime': datetime(2015, 1, 1),
                'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def start_notebook_instance(NotebookInstanceName=None):
    """
    Launches an ML compute instance with the latest version of the libraries and attaches your ML storage volume. After configuring the notebook instance, Amazon SageMaker sets the notebook instance status to InService . A notebook instance's status must be InService before you can connect to your Jupyter notebook.
    See also: AWS API Documentation
    
    
    :example: response = client.start_notebook_instance(
        NotebookInstanceName='string'
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the notebook instance to start.
            

    """
    pass

def stop_notebook_instance(NotebookInstanceName=None):
    """
    Terminates the ML compute instance. Before terminating the instance, Amazon SageMaker disconnects the ML storage volume from it. Amazon SageMaker preserves the ML storage volume.
    To access data on the ML storage volume for a notebook instance that has been terminated, call the StartNotebookInstance API. StartNotebookInstance launches another ML compute instance, configures it, and attaches the preserved ML storage volume so you can continue your work.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_notebook_instance(
        NotebookInstanceName='string'
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the notebook instance to terminate.
            

    """
    pass

def stop_training_job(TrainingJobName=None):
    """
    Stops a training job. To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts, so the results of the training is not lost.
    Training algorithms provided by Amazon SageMaker save the intermediate results of a model training job. This intermediate data is a valid model artifact. You can use the model artifacts that are saved when Amazon SageMaker stops a training job to create a model.
    When it receives a StopTrainingJob request, Amazon SageMaker changes the status of the job to Stopping . After Amazon SageMaker stops the job, it sets the status to Stopped .
    See also: AWS API Documentation
    
    
    :example: response = client.stop_training_job(
        TrainingJobName='string'
    )
    
    
    :type TrainingJobName: string
    :param TrainingJobName: [REQUIRED]
            The name of the training job to stop.
            

    """
    pass

def update_endpoint(EndpointName=None, EndpointConfigName=None):
    """
    Deploys the new EndpointConfig specified in the request, switches to using newly created endpoint, and then deletes resources provisioned for the endpoint using the previous EndpointConfig (there is no availability loss).
    When Amazon SageMaker receives the request, it sets the endpoint status to Updating . After updating the endpoint, it sets the status to InService . To check the status of an endpoint, use the DescribeEndpoint API.
    See also: AWS API Documentation
    
    
    :example: response = client.update_endpoint(
        EndpointName='string',
        EndpointConfigName='string'
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of the endpoint whose configuration you want to update.
            

    :type EndpointConfigName: string
    :param EndpointConfigName: [REQUIRED]
            The name of the new endpoint configuration.
            

    :rtype: dict
    :return: {
        'EndpointArn': 'string'
    }
    
    
    """
    pass

def update_endpoint_weights_and_capacities(EndpointName=None, DesiredWeightsAndCapacities=None):
    """
    Updates variant weight of one or more variants associated with an existing endpoint, or capacity of one variant associated with an existing endpoint. When it receives the request, Amazon SageMaker sets the endpoint status to Updating . After updating the endpoint, it sets the status to InService . To check the status of an endpoint, use the DescribeEndpoint API.
    See also: AWS API Documentation
    
    
    :example: response = client.update_endpoint_weights_and_capacities(
        EndpointName='string',
        DesiredWeightsAndCapacities=[
            {
                'VariantName': 'string',
                'DesiredWeight': ...,
                'DesiredInstanceCount': 123
            },
        ]
    )
    
    
    :type EndpointName: string
    :param EndpointName: [REQUIRED]
            The name of an existing Amazon SageMaker endpoint.
            

    :type DesiredWeightsAndCapacities: list
    :param DesiredWeightsAndCapacities: [REQUIRED]
            An object that provides new capacity and weight values for a variant.
            (dict) --Specifies weight and capacity values for a production variant.
            VariantName (string) -- [REQUIRED]The name of the variant to update.
            DesiredWeight (float) --The variant's weight.
            DesiredInstanceCount (integer) --The variant's capacity.
            
            

    :rtype: dict
    :return: {
        'EndpointArn': 'string'
    }
    
    
    """
    pass

def update_notebook_instance(NotebookInstanceName=None, InstanceType=None, RoleArn=None):
    """
    Updates a notebook instance. NotebookInstance updates include upgrading or downgrading the ML compute instance used for your notebook instance to accommodate changes in your workload requirements. You can also update the VPC security groups.
    See also: AWS API Documentation
    
    
    :example: response = client.update_notebook_instance(
        NotebookInstanceName='string',
        InstanceType='ml.t2.medium'|'ml.t2.large'|'ml.t2.xlarge'|'ml.t2.2xlarge'|'ml.m4.xlarge'|'ml.m4.2xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.m4.16xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge',
        RoleArn='string'
    )
    
    
    :type NotebookInstanceName: string
    :param NotebookInstanceName: [REQUIRED]
            The name of the notebook instance to update.
            

    :type InstanceType: string
    :param InstanceType: The Amazon ML compute instance type.

    :type RoleArn: string
    :param RoleArn: Amazon Resource Name (ARN) of the IAM role to associate with the instance.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_notebook_instance_lifecycle_config(NotebookInstanceLifecycleConfigName=None, OnCreate=None, OnStart=None):
    """
    Updates a notebook instance lifecycle configuration created with the API.
    See also: AWS API Documentation
    
    
    :example: response = client.update_notebook_instance_lifecycle_config(
        NotebookInstanceLifecycleConfigName='string',
        OnCreate=[
            {
                'Content': 'string'
            },
        ],
        OnStart=[
            {
                'Content': 'string'
            },
        ]
    )
    
    
    :type NotebookInstanceLifecycleConfigName: string
    :param NotebookInstanceLifecycleConfigName: [REQUIRED]
            The name of the lifecycle configuration.
            

    :type OnCreate: list
    :param OnCreate: The shell script that runs only once, when you create a notebook instance
            (dict) --Contains the notebook instance lifecycle configuration script.
            Each lifecycle configuration script has a limit of 16384 characters.
            The value of the $PATH environment variable that is available to both scripts is /sbin:bin:/usr/sbin:/usr/bin .
            View CloudWatch Logs for notebook instance lifecycle configurations in log group /aws/sagemaker/NotebookInstances in log stream [notebook-instance-name]/[LifecycleConfigHook] .
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
            For information about notebook instance lifestyle configurations, see notebook-lifecycle-config .
            Content (string) --A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
            
            

    :type OnStart: list
    :param OnStart: The shell script that runs every time you start a notebook instance, including when you create the notebook instance.
            (dict) --Contains the notebook instance lifecycle configuration script.
            Each lifecycle configuration script has a limit of 16384 characters.
            The value of the $PATH environment variable that is available to both scripts is /sbin:bin:/usr/sbin:/usr/bin .
            View CloudWatch Logs for notebook instance lifecycle configurations in log group /aws/sagemaker/NotebookInstances in log stream [notebook-instance-name]/[LifecycleConfigHook] .
            Lifecycle configuration scripts cannot run for longer than 5 minutes. If a script runs for longer than 5 minutes, it fails and the notebook instance is not created or started.
            For information about notebook instance lifestyle configurations, see notebook-lifecycle-config .
            Content (string) --A base64-encoded string that contains a shell script for a notebook instance lifecycle configuration.
            
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

