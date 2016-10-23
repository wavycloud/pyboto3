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


def activate_pipeline(pipelineId=None, parameterValues=None, startTimestamp=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            
    :type pipelineId: string
    :param parameterValues: A list of parameter values to pass to the pipeline at activation.
            (dict) --A value or list of parameter values.
            id (string) -- [REQUIRED]The ID of the parameter value.
            stringValue (string) -- [REQUIRED]The field value, expressed as a String.
            
            
    :type parameterValues: list
    :param startTimestamp: The date and time to resume the pipeline. By default, the pipeline resumes from the last completed execution.
    :type startTimestamp: datetime
    """
    pass


def add_tags(pipelineId=None, tags=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            
    :type pipelineId: string
    :param tags: [REQUIRED]
            The tags to add, as key/value pairs.
            (dict) --Tags are key/value pairs defined by a user and associated with a pipeline to control access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            key (string) -- [REQUIRED]The key name of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            value (string) -- [REQUIRED]The optional value portion of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            
            
    :type tags: list
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


def create_pipeline(name=None, uniqueId=None, description=None, tags=None):
    """
    :param name: [REQUIRED]
            The name for the pipeline. You can use the same name for multiple pipelines associated with your AWS account, because AWS Data Pipeline assigns each pipeline a unique pipeline identifier.
            
    :type name: string
    :param uniqueId: [REQUIRED]
            A unique identifier. This identifier is not the same as the pipeline identifier assigned by AWS Data Pipeline. You are responsible for defining the format and ensuring the uniqueness of this identifier. You use this parameter to ensure idempotency during repeated calls to CreatePipeline . For example, if the first call to CreatePipeline does not succeed, you can pass in the same unique identifier and pipeline name combination on a subsequent call to CreatePipeline . CreatePipeline ensures that if a pipeline already exists with the same name and unique identifier, a new pipeline is not created. Instead, you'll receive the pipeline identifier from the previous attempt. The uniqueness of the name and unique identifier combination is scoped to the AWS account or IAM user credentials.
            
    :type uniqueId: string
    :param description: The description for the pipeline.
    :type description: string
    :param tags: A list of tags to associate with the pipeline at creation. Tags let you control access to pipelines. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            (dict) --Tags are key/value pairs defined by a user and associated with a pipeline to control access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            key (string) -- [REQUIRED]The key name of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            value (string) -- [REQUIRED]The optional value portion of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            
            
    :type tags: list
    """
    pass


def deactivate_pipeline(pipelineId=None, cancelActive=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            
    :type pipelineId: string
    :param cancelActive: Indicates whether to cancel any running objects. The default is true, which sets the state of any running objects to CANCELED . If this value is false, the pipeline is deactivated after all running objects finish.
    :type cancelActive: boolean
    """
    pass


def delete_pipeline(pipelineId=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            ReturnsNone
            
    :type pipelineId: string
    """
    pass


def describe_objects(pipelineId=None, objectIds=None, evaluateExpressions=None, marker=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline that contains the object definitions.
            
    :type pipelineId: string
    :param objectIds: [REQUIRED]
            The IDs of the pipeline objects that contain the definitions to be described. You can pass as many as 25 identifiers in a single call to DescribeObjects .
            (string) --
            
    :type objectIds: list
    :param evaluateExpressions: Indicates whether any expressions in the object should be evaluated when the object descriptions are returned.
    :type evaluateExpressions: boolean
    :param marker: The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call DescribeObjects with the marker value from the previous call to retrieve the next set of results.
    :type marker: string
    """
    pass


def describe_pipelines(pipelineIds=None):
    """
    :param pipelineIds: [REQUIRED]
            The IDs of the pipelines to describe. You can pass as many as 25 identifiers in a single call. To obtain pipeline IDs, call ListPipelines .
            (string) --
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Contains the output of DescribePipelines.
            pipelineDescriptionList (list) --An array of descriptions for the specified pipelines.
            (dict) --Contains pipeline metadata.
            pipelineId (string) --The pipeline identifier that was assigned by AWS Data Pipeline. This is a string of the form df-297EG78HU43EEXAMPLE .
            name (string) --The name of the pipeline.
            fields (list) --A list of read-only fields that contain metadata about the pipeline: @userId, @accountId, and @pipelineState.
            (dict) --A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (StringValue ) or a reference to another object (RefValue ) but not as both.
            key (string) --The field identifier.
            stringValue (string) --The field value, expressed as a String.
            refValue (string) --The field value, expressed as the identifier of another object.
            
            description (string) --Description of the pipeline.
            tags (list) --A list of tags to associated with a pipeline. Tags let you control access to pipelines. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            (dict) --Tags are key/value pairs defined by a user and associated with a pipeline to control access. AWS Data Pipeline allows you to associate ten tags per pipeline. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            key (string) --The key name of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            value (string) --The optional value portion of a tag defined by a user. For more information, see Controlling User Access to Pipelines in the AWS Data Pipeline Developer Guide .
            
            
            
            
    :type pipelineIds: list
    """
    pass


def evaluate_expression(pipelineId=None, objectId=None, expression=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            
    :type pipelineId: string
    :param objectId: [REQUIRED]
            The ID of the object.
            
    :type objectId: string
    :param expression: [REQUIRED]
            The expression to evaluate.
            
    :type expression: string
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


def get_pipeline_definition(pipelineId=None, version=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            
    :type pipelineId: string
    :param version: The version of the pipeline definition to retrieve. Set this parameter to latest (default) to use the last definition saved to the pipeline or active to use the last definition that was activated.
    :type version: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_pipelines(marker=None):
    """
    :param marker: The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call ListPipelines with the marker value from the previous call to retrieve the next set of results.
            Return typedict
            ReturnsResponse Syntax{
              'pipelineIdList': [
                {
                  'id': 'string',
                  'name': 'string'
                },
              ],
              'marker': 'string',
              'hasMoreResults': True|False
            }
            Response Structure
            (dict) --Contains the output of ListPipelines.
            pipelineIdList (list) --The pipeline identifiers. If you require additional information about the pipelines, you can use these identifiers to call DescribePipelines and GetPipelineDefinition .
            (dict) --Contains the name and identifier of a pipeline.
            id (string) --The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the form df-297EG78HU43EEXAMPLE .
            name (string) --The name of the pipeline.
            
            marker (string) --The starting point for the next page of results. To view the next page of results, call ListPipelinesOutput again with this marker value. If the value is null, there are no more results.
            hasMoreResults (boolean) --Indicates whether there are more results that can be obtained by a subsequent call.
            
            
    :type marker: string
    """
    pass


def poll_for_task(workerGroup=None, hostname=None, instanceIdentity=None):
    """
    :param workerGroup: [REQUIRED]
            The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for workerGroup in the call to PollForTask . There are no wildcard values permitted in workerGroup ; the string must be an exact, case-sensitive, match.
            
    :type workerGroup: string
    :param hostname: The public DNS name of the calling task runner.
    :type hostname: string
    :param instanceIdentity: Identity information for the EC2 instance that is hosting the task runner. You can get this value from the instance using http://169.254.169.254/latest/meta-data/instance-id . For more information, see Instance Metadata in the Amazon Elastic Compute Cloud User Guide. Passing in this value proves that your task runner is running on an EC2 instance, and ensures the proper AWS Data Pipeline service charges are applied to your pipeline.
            document (string) --A description of an EC2 instance that is generated when the instance is launched and exposed to the instance via the instance metadata service in the form of a JSON representation of an object.
            signature (string) --A signature which can be used to verify the accuracy and authenticity of the information provided in the instance identity document.
            
    :type instanceIdentity: dict
    """
    pass


def put_pipeline_definition(pipelineId=None, pipelineObjects=None, parameterObjects=None, parameterValues=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            
    :type pipelineId: string
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
            
            
            
    :type pipelineObjects: list
    :param parameterObjects: The parameter objects used with the pipeline.
            (dict) --Contains information about a parameter object.
            id (string) -- [REQUIRED]The ID of the parameter object.
            attributes (list) -- [REQUIRED]The attributes of the parameter object.
            (dict) --The attributes allowed or specified with a parameter object.
            key (string) -- [REQUIRED]The field identifier.
            stringValue (string) -- [REQUIRED]The field value, expressed as a String.
            
            
            
    :type parameterObjects: list
    :param parameterValues: The parameter values used with the pipeline.
            (dict) --A value or list of parameter values.
            id (string) -- [REQUIRED]The ID of the parameter value.
            stringValue (string) -- [REQUIRED]The field value, expressed as a String.
            
            
    :type parameterValues: list
    """
    pass


def query_objects(pipelineId=None, query=None, sphere=None, marker=None, limit=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            
    :type pipelineId: string
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
            
            
            
    :type query: dict
    :param sphere: [REQUIRED]
            Indicates whether the query applies to components or instances. The possible values are: COMPONENT , INSTANCE , and ATTEMPT .
            
    :type sphere: string
    :param marker: The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call QueryObjects with the marker value from the previous call to retrieve the next set of results.
    :type marker: string
    :param limit: The maximum number of object names that QueryObjects will return in a single call. The default value is 100.
    :type limit: integer
    """
    pass


def remove_tags(pipelineId=None, tagKeys=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            
    :type pipelineId: string
    :param tagKeys: [REQUIRED]
            The keys of the tags to remove.
            (string) --
            
    :type tagKeys: list
    """
    pass


def report_task_progress(taskId=None, fields=None):
    """
    :param taskId: [REQUIRED]
            The ID of the task assigned to the task runner. This value is provided in the response for PollForTask .
            
    :type taskId: string
    :param fields: Key-value pairs that define the properties of the ReportTaskProgressInput object.
            (dict) --A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (StringValue ) or a reference to another object (RefValue ) but not as both.
            key (string) -- [REQUIRED]The field identifier.
            stringValue (string) --The field value, expressed as a String.
            refValue (string) --The field value, expressed as the identifier of another object.
            
            
    :type fields: list
    """
    pass


def report_task_runner_heartbeat(taskrunnerId=None, workerGroup=None, hostname=None):
    """
    :param taskrunnerId: [REQUIRED]
            The ID of the task runner. This value should be unique across your AWS account. In the case of AWS Data Pipeline Task Runner launched on a resource managed by AWS Data Pipeline, the web service provides a unique identifier when it launches the application. If you have written a custom task runner, you should assign a unique identifier for the task runner.
            
    :type taskrunnerId: string
    :param workerGroup: The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for workerGroup . There are no wildcard values permitted in workerGroup ; the string must be an exact, case-sensitive, match.
    :type workerGroup: string
    :param hostname: The public DNS name of the task runner.
    :type hostname: string
    """
    pass


def set_status(pipelineId=None, objectIds=None, status=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline that contains the objects.
            
    :type pipelineId: string
    :param objectIds: [REQUIRED]
            The IDs of the objects. The corresponding objects can be either physical or components, but not a mix of both types.
            (string) --
            
    :type objectIds: list
    :param status: [REQUIRED]
            The status to be set on all the objects specified in objectIds . For components, use PAUSE or RESUME . For instances, use TRY_CANCEL , RERUN , or MARK_FINISHED .
            
    :type status: string
    """
    pass


def set_task_status(taskId=None, taskStatus=None, errorId=None, errorMessage=None, errorStackTrace=None):
    """
    :param taskId: [REQUIRED]
            The ID of the task assigned to the task runner. This value is provided in the response for PollForTask .
            
    :type taskId: string
    :param taskStatus: [REQUIRED]
            If FINISHED , the task successfully completed. If FAILED , the task ended unsuccessfully. Preconditions use false.
            
    :type taskStatus: string
    :param errorId: If an error occurred during the task, this value specifies the error code. This value is set on the physical attempt object. It is used to display error information to the user. It should not start with string 'Service_' which is reserved by the system.
    :type errorId: string
    :param errorMessage: If an error occurred during the task, this value specifies a text description of the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.
    :type errorMessage: string
    :param errorStackTrace: If an error occurred during the task, this value specifies the stack trace associated with the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.
    :type errorStackTrace: string
    """
    pass


def validate_pipeline_definition(pipelineId=None, pipelineObjects=None, parameterObjects=None, parameterValues=None):
    """
    :param pipelineId: [REQUIRED]
            The ID of the pipeline.
            
    :type pipelineId: string
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
            
            
            
    :type pipelineObjects: list
    :param parameterObjects: The parameter objects used with the pipeline.
            (dict) --Contains information about a parameter object.
            id (string) -- [REQUIRED]The ID of the parameter object.
            attributes (list) -- [REQUIRED]The attributes of the parameter object.
            (dict) --The attributes allowed or specified with a parameter object.
            key (string) -- [REQUIRED]The field identifier.
            stringValue (string) -- [REQUIRED]The field value, expressed as a String.
            
            
            
    :type parameterObjects: list
    :param parameterValues: The parameter values used with the pipeline.
            (dict) --A value or list of parameter values.
            id (string) -- [REQUIRED]The ID of the parameter value.
            stringValue (string) -- [REQUIRED]The field value, expressed as a String.
            
            
    :type parameterValues: list
    """
    pass
