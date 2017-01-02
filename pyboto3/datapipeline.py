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

def activate_pipeline(pipelineId=None, parameterValues=None, startTimestamp=None):
    """
    Validates the specified pipeline and starts processing pipeline tasks. If the pipeline does not pass validation, activation fails.
    If you need to pause the pipeline to investigate an issue with a component, such as a data source or script, call  DeactivatePipeline .
    To activate a finished pipeline, modify the end date for the pipeline and then activate it.
    See also: AWS API Documentation
    
    
    :example: response = client.activate_pipeline(
        pipelineId='string',
        parameterValues=[
            {
                'id': 'string',
                'stringValue': 'string'
            },
        ],
        startTimestamp=datetime(2015, 1, 1)
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            

    :type parameterValues: list
    :param parameterValues: A list of parameter values to pass to the pipeline at activation.
            (dict) --A value or list of parameter values.
            id (string) -- [REQUIRED]The ID of the parameter value.
            stringValue (string) -- [REQUIRED]The field value, expressed as a String.
            
            

    :type startTimestamp: datetime
    :param startTimestamp: The date and time to resume the pipeline. By default, the pipeline resumes from the last completed execution.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def add_tags(pipelineId=None, tags=None):
    """
    Adds or modifies tags for the specified pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags(
        pipelineId='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            

    :type tags: list
    :param tags: [REQUIRED]
            The tags to add, as key/value pairs.
            (dict) --Tags are key/value pairs defined by a user and associated with a pipeline to control access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            key (string) -- [REQUIRED]The key name of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            value (string) -- [REQUIRED]The optional value portion of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            
            

    :rtype: dict
    :return: {}
    
    
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

def create_pipeline(name=None, uniqueId=None, description=None, tags=None):
    """
    Creates a new, empty pipeline. Use  PutPipelineDefinition to populate the pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.create_pipeline(
        name='string',
        uniqueId='string',
        description='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]
            The name for the pipeline. You can use the same name for multiple pipelines associated with your AWS account, because AWS Data Pipeline assigns each pipeline a unique pipeline identifier.
            

    :type uniqueId: string
    :param uniqueId: [REQUIRED]
            A unique identifier. This identifier is not the same as the pipeline identifier assigned by AWS Data Pipeline. You are responsible for defining the format and ensuring the uniqueness of this identifier. You use this parameter to ensure idempotency during repeated calls to CreatePipeline . For example, if the first call to CreatePipeline does not succeed, you can pass in the same unique identifier and pipeline name combination on a subsequent call to CreatePipeline . CreatePipeline ensures that if a pipeline already exists with the same name and unique identifier, a new pipeline is not created. Instead, you'll receive the pipeline identifier from the previous attempt. The uniqueness of the name and unique identifier combination is scoped to the AWS account or IAM user credentials.
            

    :type description: string
    :param description: The description for the pipeline.

    :type tags: list
    :param tags: A list of tags to associate with the pipeline at creation. Tags let you control access to pipelines. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            (dict) --Tags are key/value pairs defined by a user and associated with a pipeline to control access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            key (string) -- [REQUIRED]The key name of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            value (string) -- [REQUIRED]The optional value portion of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            
            

    :rtype: dict
    :return: {
        'pipelineId': 'string'
    }
    
    
    """
    pass

def deactivate_pipeline(pipelineId=None, cancelActive=None):
    """
    Deactivates the specified running pipeline. The pipeline is set to the DEACTIVATING state until the deactivation process completes.
    To resume a deactivated pipeline, use  ActivatePipeline . By default, the pipeline resumes from the last completed execution. Optionally, you can specify the date and time to resume the pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.deactivate_pipeline(
        pipelineId='string',
        cancelActive=True|False
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            

    :type cancelActive: boolean
    :param cancelActive: Indicates whether to cancel any running objects. The default is true, which sets the state of any running objects to CANCELED . If this value is false, the pipeline is deactivated after all running objects finish.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_pipeline(pipelineId=None):
    """
    Deletes a pipeline, its pipeline definition, and its run history. AWS Data Pipeline attempts to cancel instances associated with the pipeline that are currently being processed by task runners.
    Deleting a pipeline cannot be undone. You cannot query or restore a deleted pipeline. To temporarily pause a pipeline instead of deleting it, call  SetStatus with the status set to PAUSE on individual components. Components that are paused by  SetStatus can be resumed.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_pipeline(
        pipelineId='string'
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            

    """
    pass

def describe_objects(pipelineId=None, objectIds=None, evaluateExpressions=None, marker=None):
    """
    Gets the object definitions for a set of objects associated with the pipeline. Object definitions are composed of a set of fields that define the properties of the object.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_objects(
        pipelineId='string',
        objectIds=[
            'string',
        ],
        evaluateExpressions=True|False,
        marker='string'
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline that contains the object definitions.
            

    :type objectIds: list
    :param objectIds: [REQUIRED]
            The IDs of the pipeline objects that contain the definitions to be described. You can pass as many as 25 identifiers in a single call to DescribeObjects .
            (string) --
            

    :type evaluateExpressions: boolean
    :param evaluateExpressions: Indicates whether any expressions in the object should be evaluated when the object descriptions are returned.

    :type marker: string
    :param marker: The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call DescribeObjects with the marker value from the previous call to retrieve the next set of results.

    :rtype: dict
    :return: {
        'pipelineObjects': [
            {
                'id': 'string',
                'name': 'string',
                'fields': [
                    {
                        'key': 'string',
                        'stringValue': 'string',
                        'refValue': 'string'
                    },
                ]
            },
        ],
        'marker': 'string',
        'hasMoreResults': True|False
    }
    
    
    """
    pass

def describe_pipelines(pipelineIds=None):
    """
    Retrieves metadata about one or more pipelines. The information retrieved includes the name of the pipeline, the pipeline identifier, its current state, and the user account that owns the pipeline. Using account credentials, you can retrieve metadata about pipelines that you or your IAM users have created. If you are using an IAM user account, you can retrieve metadata about only those pipelines for which you have read permissions.
    To retrieve the full pipeline definition instead of metadata about the pipeline, call  GetPipelineDefinition .
    See also: AWS API Documentation
    
    
    :example: response = client.describe_pipelines(
        pipelineIds=[
            'string',
        ]
    )
    
    
    :type pipelineIds: list
    :param pipelineIds: [REQUIRED]
            The IDs of the pipelines to describe. You can pass as many as 25 identifiers in a single call. To obtain pipeline IDs, call ListPipelines .
            (string) --
            

    :rtype: dict
    :return: {
        'pipelineDescriptionList': [
            {
                'pipelineId': 'string',
                'name': 'string',
                'fields': [
                    {
                        'key': 'string',
                        'stringValue': 'string',
                        'refValue': 'string'
                    },
                ],
                'description': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def evaluate_expression(pipelineId=None, objectId=None, expression=None):
    """
    Task runners call EvaluateExpression to evaluate a string in the context of the specified object. For example, a task runner can evaluate SQL queries stored in Amazon S3.
    See also: AWS API Documentation
    
    
    :example: response = client.evaluate_expression(
        pipelineId='string',
        objectId='string',
        expression='string'
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            

    :type objectId: string
    :param objectId: [REQUIRED]
            The ID of the object.
            

    :type expression: string
    :param expression: [REQUIRED]
            The expression to evaluate.
            

    :rtype: dict
    :return: {
        'evaluatedExpression': 'string'
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

def get_pipeline_definition(pipelineId=None, version=None):
    """
    Gets the definition of the specified pipeline. You can call GetPipelineDefinition to retrieve the pipeline definition that you provided using  PutPipelineDefinition .
    See also: AWS API Documentation
    
    
    :example: response = client.get_pipeline_definition(
        pipelineId='string',
        version='string'
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            

    :type version: string
    :param version: The version of the pipeline definition to retrieve. Set this parameter to latest (default) to use the last definition saved to the pipeline or active to use the last definition that was activated.

    :rtype: dict
    :return: {
        'pipelineObjects': [
            {
                'id': 'string',
                'name': 'string',
                'fields': [
                    {
                        'key': 'string',
                        'stringValue': 'string',
                        'refValue': 'string'
                    },
                ]
            },
        ],
        'parameterObjects': [
            {
                'id': 'string',
                'attributes': [
                    {
                        'key': 'string',
                        'stringValue': 'string'
                    },
                ]
            },
        ],
        'parameterValues': [
            {
                'id': 'string',
                'stringValue': 'string'
            },
        ]
    }
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def list_pipelines(marker=None):
    """
    Lists the pipeline identifiers for all active pipelines that you have permission to access.
    See also: AWS API Documentation
    
    
    :example: response = client.list_pipelines(
        marker='string'
    )
    
    
    :type marker: string
    :param marker: The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call ListPipelines with the marker value from the previous call to retrieve the next set of results.

    :rtype: dict
    :return: {
        'pipelineIdList': [
            {
                'id': 'string',
                'name': 'string'
            },
        ],
        'marker': 'string',
        'hasMoreResults': True|False
    }
    
    
    """
    pass

def poll_for_task(workerGroup=None, hostname=None, instanceIdentity=None):
    """
    Task runners call PollForTask to receive a task to perform from AWS Data Pipeline. The task runner specifies which tasks it can perform by setting a value for the workerGroup parameter. The task returned can come from any of the pipelines that match the workerGroup value passed in by the task runner and that was launched using the IAM user credentials specified by the task runner.
    If tasks are ready in the work queue, PollForTask returns a response immediately. If no tasks are available in the queue, PollForTask uses long-polling and holds on to a poll connection for up to a 90 seconds, during which time the first newly scheduled task is handed to the task runner. To accomodate this, set the socket timeout in your task runner to 90 seconds. The task runner should not call PollForTask again on the same workerGroup until it receives a response, and this can take up to 90 seconds.
    See also: AWS API Documentation
    
    
    :example: response = client.poll_for_task(
        workerGroup='string',
        hostname='string',
        instanceIdentity={
            'document': 'string',
            'signature': 'string'
        }
    )
    
    
    :type workerGroup: string
    :param workerGroup: [REQUIRED]
            The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for workerGroup in the call to PollForTask . There are no wildcard values permitted in workerGroup ; the string must be an exact, case-sensitive, match.
            

    :type hostname: string
    :param hostname: The public DNS name of the calling task runner.

    :type instanceIdentity: dict
    :param instanceIdentity: Identity information for the EC2 instance that is hosting the task runner. You can get this value from the instance using http://169.254.169.254/latest/meta-data/instance-id . For more information, see Instance Metadata in the Amazon Elastic Compute Cloud User Guide. Passing in this value proves that your task runner is running on an EC2 instance, and ensures the proper AWS Data Pipeline service charges are applied to your pipeline.
            document (string) --A description of an EC2 instance that is generated when the instance is launched and exposed to the instance via the instance metadata service in the form of a JSON representation of an object.
            signature (string) --A signature which can be used to verify the accuracy and authenticity of the information provided in the instance identity document.
            

    :rtype: dict
    :return: {
        'taskObject': {
            'taskId': 'string',
            'pipelineId': 'string',
            'attemptId': 'string',
            'objects': {
                'string': {
                    'id': 'string',
                    'name': 'string',
                    'fields': [
                        {
                            'key': 'string',
                            'stringValue': 'string',
                            'refValue': 'string'
                        },
                    ]
                }
            }
        }
    }
    
    
    """
    pass

def put_pipeline_definition(pipelineId=None, pipelineObjects=None, parameterObjects=None, parameterValues=None):
    """
    Adds tasks, schedules, and preconditions to the specified pipeline. You can use PutPipelineDefinition to populate a new pipeline.
    Pipeline object definitions are passed to the PutPipelineDefinition action and returned by the  GetPipelineDefinition action.
    See also: AWS API Documentation
    
    
    :example: response = client.put_pipeline_definition(
        pipelineId='string',
        pipelineObjects=[
            {
                'id': 'string',
                'name': 'string',
                'fields': [
                    {
                        'key': 'string',
                        'stringValue': 'string',
                        'refValue': 'string'
                    },
                ]
            },
        ],
        parameterObjects=[
            {
                'id': 'string',
                'attributes': [
                    {
                        'key': 'string',
                        'stringValue': 'string'
                    },
                ]
            },
        ],
        parameterValues=[
            {
                'id': 'string',
                'stringValue': 'string'
            },
        ]
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            

    :type pipelineObjects: list
    :param pipelineObjects: [REQUIRED]
            The objects that define the pipeline. These objects overwrite the existing pipeline definition.
            (dict) --Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.
            id (string) -- [REQUIRED]The ID of the object.
            name (string) -- [REQUIRED]The name of the object.
            fields (list) -- [REQUIRED]Key-value pairs that define the properties of the object.
            (dict) --A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (StringValue ) or a reference to another object (RefValue ) but not as both.
            key (string) -- [REQUIRED]The field identifier.
            stringValue (string) --The field value, expressed as a String.
            refValue (string) --The field value, expressed as the identifier of another object.
            
            
            

    :type parameterObjects: list
    :param parameterObjects: The parameter objects used with the pipeline.
            (dict) --Contains information about a parameter object.
            id (string) -- [REQUIRED]The ID of the parameter object.
            attributes (list) -- [REQUIRED]The attributes of the parameter object.
            (dict) --The attributes allowed or specified with a parameter object.
            key (string) -- [REQUIRED]The field identifier.
            stringValue (string) -- [REQUIRED]The field value, expressed as a String.
            
            
            

    :type parameterValues: list
    :param parameterValues: The parameter values used with the pipeline.
            (dict) --A value or list of parameter values.
            id (string) -- [REQUIRED]The ID of the parameter value.
            stringValue (string) -- [REQUIRED]The field value, expressed as a String.
            
            

    :rtype: dict
    :return: {
        'validationErrors': [
            {
                'id': 'string',
                'errors': [
                    'string',
                ]
            },
        ],
        'validationWarnings': [
            {
                'id': 'string',
                'warnings': [
                    'string',
                ]
            },
        ],
        'errored': True|False
    }
    
    
    :returns: 
    pipelineId (string) -- [REQUIRED]
    The ID of the pipeline.
    
    pipelineObjects (list) -- [REQUIRED]
    The objects that define the pipeline. These objects overwrite the existing pipeline definition.
    
    (dict) --Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.
    
    id (string) -- [REQUIRED]The ID of the object.
    
    name (string) -- [REQUIRED]The name of the object.
    
    fields (list) -- [REQUIRED]Key-value pairs that define the properties of the object.
    
    (dict) --A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (StringValue ) or a reference to another object (RefValue ) but not as both.
    
    key (string) -- [REQUIRED]The field identifier.
    
    stringValue (string) --The field value, expressed as a String.
    
    refValue (string) --The field value, expressed as the identifier of another object.
    
    
    
    
    
    
    
    
    
    parameterObjects (list) -- The parameter objects used with the pipeline.
    
    (dict) --Contains information about a parameter object.
    
    id (string) -- [REQUIRED]The ID of the parameter object.
    
    attributes (list) -- [REQUIRED]The attributes of the parameter object.
    
    (dict) --The attributes allowed or specified with a parameter object.
    
    key (string) -- [REQUIRED]The field identifier.
    
    stringValue (string) -- [REQUIRED]The field value, expressed as a String.
    
    
    
    
    
    
    
    
    
    parameterValues (list) -- The parameter values used with the pipeline.
    
    (dict) --A value or list of parameter values.
    
    id (string) -- [REQUIRED]The ID of the parameter value.
    
    stringValue (string) -- [REQUIRED]The field value, expressed as a String.
    
    
    
    
    
    
    """
    pass

def query_objects(pipelineId=None, query=None, sphere=None, marker=None, limit=None):
    """
    Queries the specified pipeline for the names of objects that match the specified set of conditions.
    See also: AWS API Documentation
    
    
    :example: response = client.query_objects(
        pipelineId='string',
        query={
            'selectors': [
                {
                    'fieldName': 'string',
                    'operator': {
                        'type': 'EQ'|'REF_EQ'|'LE'|'GE'|'BETWEEN',
                        'values': [
                            'string',
                        ]
                    }
                },
            ]
        },
        sphere='string',
        marker='string',
        limit=123
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            

    :type query: dict
    :param query: The query that defines the objects to be returned. The Query object can contain a maximum of ten selectors. The conditions in the query are limited to top-level String fields in the object. These filters can be applied to components, instances, and attempts.
            selectors (list) --List of selectors that define the query. An object must satisfy all of the selectors to match the query.
            (dict) --A comparision that is used to determine whether a query should return this object.
            fieldName (string) --The name of the field that the operator will be applied to. The field name is the 'key' portion of the field definition in the pipeline definition syntax that is used by the AWS Data Pipeline API. If the field is not set on the object, the condition fails.
            operator (dict) --Contains a logical operation for comparing the value of a field with a specified value.
            type (string) --The logical operation to be performed: equal (EQ ), equal reference (REF_EQ ), less than or equal (LE ), greater than or equal (GE ), or between (BETWEEN ). Equal reference (REF_EQ ) can be used only with reference fields. The other comparison types can be used only with String fields. The comparison types you can use apply only to certain object fields, as detailed below.
            The comparison operators EQ and REF_EQ act on the following fields:
            name
            @sphere
            parent
            @componentParent
            @instanceParent
            @status
            @scheduledStartTime
            @scheduledEndTime
            @actualStartTime
            @actualEndTime
            The comparison operators GE , LE , and BETWEEN act on the following fields:
            @scheduledStartTime
            @scheduledEndTime
            @actualStartTime
            @actualEndTime
            Note that fields beginning with the at sign (@) are read-only and set by the web service. When you name fields, you should choose names containing only alpha-numeric values, as symbols may be reserved by AWS Data Pipeline. User-defined fields that you add to a pipeline should prefix their name with the string 'my'.
            values (list) --The value that the actual field value will be compared with.
            (string) --
            
            
            

    :type sphere: string
    :param sphere: [REQUIRED]
            Indicates whether the query applies to components or instances. The possible values are: COMPONENT , INSTANCE , and ATTEMPT .
            

    :type marker: string
    :param marker: The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call QueryObjects with the marker value from the previous call to retrieve the next set of results.

    :type limit: integer
    :param limit: The maximum number of object names that QueryObjects will return in a single call. The default value is 100.

    :rtype: dict
    :return: {
        'ids': [
            'string',
        ],
        'marker': 'string',
        'hasMoreResults': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def remove_tags(pipelineId=None, tagKeys=None):
    """
    Removes existing tags from the specified pipeline.
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags(
        pipelineId='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            

    :type tagKeys: list
    :param tagKeys: [REQUIRED]
            The keys of the tags to remove.
            (string) --
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def report_task_progress(taskId=None, fields=None):
    """
    Task runners call ReportTaskProgress when assigned a task to acknowledge that it has the task. If the web service does not receive this acknowledgement within 2 minutes, it assigns the task in a subsequent  PollForTask call. After this initial acknowledgement, the task runner only needs to report progress every 15 minutes to maintain its ownership of the task. You can change this reporting time from 15 minutes by specifying a reportProgressTimeout field in your pipeline.
    If a task runner does not report its status after 5 minutes, AWS Data Pipeline assumes that the task runner is unable to process the task and reassigns the task in a subsequent response to  PollForTask . Task runners should call ReportTaskProgress every 60 seconds.
    See also: AWS API Documentation
    
    
    :example: response = client.report_task_progress(
        taskId='string',
        fields=[
            {
                'key': 'string',
                'stringValue': 'string',
                'refValue': 'string'
            },
        ]
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]
            The ID of the task assigned to the task runner. This value is provided in the response for PollForTask .
            

    :type fields: list
    :param fields: Key-value pairs that define the properties of the ReportTaskProgressInput object.
            (dict) --A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (StringValue ) or a reference to another object (RefValue ) but not as both.
            key (string) -- [REQUIRED]The field identifier.
            stringValue (string) --The field value, expressed as a String.
            refValue (string) --The field value, expressed as the identifier of another object.
            
            

    :rtype: dict
    :return: {
        'canceled': True|False
    }
    
    
    """
    pass

def report_task_runner_heartbeat(taskrunnerId=None, workerGroup=None, hostname=None):
    """
    Task runners call ReportTaskRunnerHeartbeat every 15 minutes to indicate that they are operational. If the AWS Data Pipeline Task Runner is launched on a resource managed by AWS Data Pipeline, the web service can use this call to detect when the task runner application has failed and restart a new instance.
    See also: AWS API Documentation
    
    
    :example: response = client.report_task_runner_heartbeat(
        taskrunnerId='string',
        workerGroup='string',
        hostname='string'
    )
    
    
    :type taskrunnerId: string
    :param taskrunnerId: [REQUIRED]
            The ID of the task runner. This value should be unique across your AWS account. In the case of AWS Data Pipeline Task Runner launched on a resource managed by AWS Data Pipeline, the web service provides a unique identifier when it launches the application. If you have written a custom task runner, you should assign a unique identifier for the task runner.
            

    :type workerGroup: string
    :param workerGroup: The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for workerGroup . There are no wildcard values permitted in workerGroup ; the string must be an exact, case-sensitive, match.

    :type hostname: string
    :param hostname: The public DNS name of the task runner.

    :rtype: dict
    :return: {
        'terminate': True|False
    }
    
    
    """
    pass

def set_status(pipelineId=None, objectIds=None, status=None):
    """
    Requests that the status of the specified physical or logical pipeline objects be updated in the specified pipeline. This update might not occur immediately, but is eventually consistent. The status that can be set depends on the type of object (for example, DataNode or Activity). You cannot perform this operation on FINISHED pipelines and attempting to do so returns InvalidRequestException .
    See also: AWS API Documentation
    
    
    :example: response = client.set_status(
        pipelineId='string',
        objectIds=[
            'string',
        ],
        status='string'
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline that contains the objects.
            

    :type objectIds: list
    :param objectIds: [REQUIRED]
            The IDs of the objects. The corresponding objects can be either physical or components, but not a mix of both types.
            (string) --
            

    :type status: string
    :param status: [REQUIRED]
            The status to be set on all the objects specified in objectIds . For components, use PAUSE or RESUME . For instances, use TRY_CANCEL , RERUN , or MARK_FINISHED .
            

    """
    pass

def set_task_status(taskId=None, taskStatus=None, errorId=None, errorMessage=None, errorStackTrace=None):
    """
    Task runners call SetTaskStatus to notify AWS Data Pipeline that a task is completed and provide information about the final status. A task runner makes this call regardless of whether the task was sucessful. A task runner does not need to call SetTaskStatus for tasks that are canceled by the web service during a call to  ReportTaskProgress .
    See also: AWS API Documentation
    
    
    :example: response = client.set_task_status(
        taskId='string',
        taskStatus='FINISHED'|'FAILED'|'FALSE',
        errorId='string',
        errorMessage='string',
        errorStackTrace='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]
            The ID of the task assigned to the task runner. This value is provided in the response for PollForTask .
            

    :type taskStatus: string
    :param taskStatus: [REQUIRED]
            If FINISHED , the task successfully completed. If FAILED , the task ended unsuccessfully. Preconditions use false.
            

    :type errorId: string
    :param errorId: If an error occurred during the task, this value specifies the error code. This value is set on the physical attempt object. It is used to display error information to the user. It should not start with string 'Service_' which is reserved by the system.

    :type errorMessage: string
    :param errorMessage: If an error occurred during the task, this value specifies a text description of the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.

    :type errorStackTrace: string
    :param errorStackTrace: If an error occurred during the task, this value specifies the stack trace associated with the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def validate_pipeline_definition(pipelineId=None, pipelineObjects=None, parameterObjects=None, parameterValues=None):
    """
    Validates the specified pipeline definition to ensure that it is well formed and can be run without error.
    See also: AWS API Documentation
    
    
    :example: response = client.validate_pipeline_definition(
        pipelineId='string',
        pipelineObjects=[
            {
                'id': 'string',
                'name': 'string',
                'fields': [
                    {
                        'key': 'string',
                        'stringValue': 'string',
                        'refValue': 'string'
                    },
                ]
            },
        ],
        parameterObjects=[
            {
                'id': 'string',
                'attributes': [
                    {
                        'key': 'string',
                        'stringValue': 'string'
                    },
                ]
            },
        ],
        parameterValues=[
            {
                'id': 'string',
                'stringValue': 'string'
            },
        ]
    )
    
    
    :type pipelineId: string
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            

    :type pipelineObjects: list
    :param pipelineObjects: [REQUIRED]
            The objects that define the pipeline changes to validate against the pipeline.
            (dict) --Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.
            id (string) -- [REQUIRED]The ID of the object.
            name (string) -- [REQUIRED]The name of the object.
            fields (list) -- [REQUIRED]Key-value pairs that define the properties of the object.
            (dict) --A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (StringValue ) or a reference to another object (RefValue ) but not as both.
            key (string) -- [REQUIRED]The field identifier.
            stringValue (string) --The field value, expressed as a String.
            refValue (string) --The field value, expressed as the identifier of another object.
            
            
            

    :type parameterObjects: list
    :param parameterObjects: The parameter objects used with the pipeline.
            (dict) --Contains information about a parameter object.
            id (string) -- [REQUIRED]The ID of the parameter object.
            attributes (list) -- [REQUIRED]The attributes of the parameter object.
            (dict) --The attributes allowed or specified with a parameter object.
            key (string) -- [REQUIRED]The field identifier.
            stringValue (string) -- [REQUIRED]The field value, expressed as a String.
            
            
            

    :type parameterValues: list
    :param parameterValues: The parameter values used with the pipeline.
            (dict) --A value or list of parameter values.
            id (string) -- [REQUIRED]The ID of the parameter value.
            stringValue (string) -- [REQUIRED]The field value, expressed as a String.
            
            

    :rtype: dict
    :return: {
        'validationErrors': [
            {
                'id': 'string',
                'errors': [
                    'string',
                ]
            },
        ],
        'validationWarnings': [
            {
                'id': 'string',
                'warnings': [
                    'string',
                ]
            },
        ],
        'errored': True|False
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

