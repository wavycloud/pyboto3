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

def associate_entity_to_thing(thingName=None, entityId=None, namespaceVersion=None):
    """
    Associates a device with a concrete thing that is in the user\'s registry.
    A thing can be associated with only one device at a time. If you associate a thing with a new device id, its previous association will be removed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_entity_to_thing(
        thingName='string',
        entityId='string',
        namespaceVersion=123
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing to which the entity is to be associated.\n

    :type entityId: string
    :param entityId: [REQUIRED]\nThe ID of the device to be associated with the thing.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME\n

    :type namespaceVersion: integer
    :param namespaceVersion: The version of the user\'s namespace. Defaults to the latest version of the user\'s namespace.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_flow_template(definition=None, compatibleNamespaceVersion=None):
    """
    Creates a workflow template. Workflows can be created only in the user\'s namespace. (The public namespace contains only entities.) The workflow can contain only entities in the specified namespace. The workflow is validated against the entities in the latest version of the user\'s namespace unless another namespace version is specified in the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_flow_template(
        definition={
            'language': 'GRAPHQL',
            'text': 'string'
        },
        compatibleNamespaceVersion=123
    )
    
    
    :type definition: dict
    :param definition: [REQUIRED]\nThe workflow DefinitionDocument .\n\nlanguage (string) -- [REQUIRED]The language used to define the entity. GRAPHQL is the only valid value.\n\ntext (string) -- [REQUIRED]The GraphQL text that defines the entity.\n\n\n

    :type compatibleNamespaceVersion: integer
    :param compatibleNamespaceVersion: The namespace version in which the workflow is to be created.\nIf no value is specified, the latest version is used by default.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'summary': {
        'id': 'string',
        'arn': 'string',
        'revisionNumber': 123,
        'createdAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

summary (dict) --
The summary object that describes the created workflow.

id (string) --
The ID of the workflow.

arn (string) --
The ARN of the workflow.

revisionNumber (integer) --
The revision number of the workflow.

createdAt (datetime) --
The date when the workflow was created.









Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceAlreadyExistsException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.LimitExceededException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {
        'summary': {
            'id': 'string',
            'arn': 'string',
            'revisionNumber': 123,
            'createdAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ResourceAlreadyExistsException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.LimitExceededException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    
    """
    pass

def create_system_instance(tags=None, definition=None, target=None, greengrassGroupName=None, s3BucketName=None, metricsConfiguration=None, flowActionsRoleArn=None):
    """
    Creates a system instance.
    This action validates the system instance, prepares the deployment-related resources. For Greengrass deployments, it updates the Greengrass group that is specified by the greengrassGroupName parameter. It also adds a file to the S3 bucket specified by the s3BucketName parameter. You need to call DeploySystemInstance after running this action.
    For Greengrass deployments, since this action modifies and adds resources to a Greengrass group and an S3 bucket on the caller\'s behalf, the calling identity must have write permissions to both the specified Greengrass group and S3 bucket. Otherwise, the call will fail with an authorization error.
    For cloud deployments, this action requires a flowActionsRoleArn value. This is an IAM role that has permissions to access AWS services, such as AWS Lambda and AWS IoT, that the flow uses when it executes.
    If the definition document doesn\'t specify a version of the user\'s namespace, the latest version will be used by default.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_system_instance(
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        definition={
            'language': 'GRAPHQL',
            'text': 'string'
        },
        target='GREENGRASS'|'CLOUD',
        greengrassGroupName='string',
        s3BucketName='string',
        metricsConfiguration={
            'cloudMetricEnabled': True|False,
            'metricRuleRoleArn': 'string'
        },
        flowActionsRoleArn='string'
    )
    
    
    :type tags: list
    :param tags: Metadata, consisting of key-value pairs, that can be used to categorize your system instances.\n\n(dict) --Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.\n\nkey (string) -- [REQUIRED]The required name of the tag. The string value can be from 1 to 128 Unicode characters in length.\n\nvalue (string) -- [REQUIRED]The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length.\n\n\n\n\n

    :type definition: dict
    :param definition: [REQUIRED]\nA document that defines an entity.\n\nlanguage (string) -- [REQUIRED]The language used to define the entity. GRAPHQL is the only valid value.\n\ntext (string) -- [REQUIRED]The GraphQL text that defines the entity.\n\n\n

    :type target: string
    :param target: [REQUIRED]\nThe target type of the deployment. Valid values are GREENGRASS and CLOUD .\n

    :type greengrassGroupName: string
    :param greengrassGroupName: The name of the Greengrass group where the system instance will be deployed. This value is required if the value of the target parameter is GREENGRASS .

    :type s3BucketName: string
    :param s3BucketName: The name of the Amazon Simple Storage Service bucket that will be used to store and deploy the system instance\'s resource file. This value is required if the value of the target parameter is GREENGRASS .

    :type metricsConfiguration: dict
    :param metricsConfiguration: An object that specifies whether cloud metrics are collected in a deployment and, if so, what role is used to collect metrics.\n\ncloudMetricEnabled (boolean) --A Boolean that specifies whether cloud metrics are collected.\n\nmetricRuleRoleArn (string) --The ARN of the role that is used to collect cloud metrics.\n\n\n

    :type flowActionsRoleArn: string
    :param flowActionsRoleArn: The ARN of the IAM role that AWS IoT Things Graph will assume when it executes the flow. This role must have read and write access to AWS Lambda and AWS IoT and any other AWS services that the flow uses when it executes. This value is required if the value of the target parameter is CLOUD .

    :rtype: dict

ReturnsResponse Syntax
{
    'summary': {
        'id': 'string',
        'arn': 'string',
        'status': 'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'|'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
        'target': 'GREENGRASS'|'CLOUD',
        'greengrassGroupName': 'string',
        'createdAt': datetime(2015, 1, 1),
        'updatedAt': datetime(2015, 1, 1),
        'greengrassGroupId': 'string',
        'greengrassGroupVersionId': 'string'
    }
}


Response Structure

(dict) --

summary (dict) --
The summary object that describes the new system instance.

id (string) --
The ID of the system instance.

arn (string) --
The ARN of the system instance.

status (string) --
The status of the system instance.

target (string) --
The target of the system instance.

greengrassGroupName (string) --
The ID of the Greengrass group where the system instance is deployed.

createdAt (datetime) --
The date when the system instance was created.

updatedAt (datetime) --
The date and time when the system instance was last updated.

greengrassGroupId (string) --
The ID of the Greengrass group where the system instance is deployed.

greengrassGroupVersionId (string) --
The version of the Greengrass group where the system instance is deployed.









Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceAlreadyExistsException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.LimitExceededException


    :return: {
        'summary': {
            'id': 'string',
            'arn': 'string',
            'status': 'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'|'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
            'target': 'GREENGRASS'|'CLOUD',
            'greengrassGroupName': 'string',
            'createdAt': datetime(2015, 1, 1),
            'updatedAt': datetime(2015, 1, 1),
            'greengrassGroupId': 'string',
            'greengrassGroupVersionId': 'string'
        }
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ResourceAlreadyExistsException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.LimitExceededException
    
    """
    pass

def create_system_template(definition=None, compatibleNamespaceVersion=None):
    """
    Creates a system. The system is validated against the entities in the latest version of the user\'s namespace unless another namespace version is specified in the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_system_template(
        definition={
            'language': 'GRAPHQL',
            'text': 'string'
        },
        compatibleNamespaceVersion=123
    )
    
    
    :type definition: dict
    :param definition: [REQUIRED]\nThe DefinitionDocument used to create the system.\n\nlanguage (string) -- [REQUIRED]The language used to define the entity. GRAPHQL is the only valid value.\n\ntext (string) -- [REQUIRED]The GraphQL text that defines the entity.\n\n\n

    :type compatibleNamespaceVersion: integer
    :param compatibleNamespaceVersion: The namespace version in which the system is to be created.\nIf no value is specified, the latest version is used by default.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'summary': {
        'id': 'string',
        'arn': 'string',
        'revisionNumber': 123,
        'createdAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

summary (dict) --
The summary object that describes the created system.

id (string) --
The ID of the system.

arn (string) --
The ARN of the system.

revisionNumber (integer) --
The revision number of the system.

createdAt (datetime) --
The date when the system was created.









Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceAlreadyExistsException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {
        'summary': {
            'id': 'string',
            'arn': 'string',
            'revisionNumber': 123,
            'createdAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ResourceAlreadyExistsException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_flow_template(id=None):
    """
    Deletes a workflow. Any new system or deployment that contains this workflow will fail to update or deploy. Existing deployments that contain the workflow will continue to run (since they use a snapshot of the workflow taken at the time of deployment).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_flow_template(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the workflow to be deleted.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceInUseException


    :return: {}
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceInUseException
    
    """
    pass

def delete_namespace():
    """
    Deletes the specified namespace. This action deletes all of the entities in the namespace. Delete the systems and flows that use entities in the namespace before performing this action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_namespace()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'namespaceArn': 'string',
    'namespaceName': 'string'
}


Response Structure

(dict) --
namespaceArn (string) --The ARN of the namespace to be deleted.

namespaceName (string) --The name of the namespace to be deleted.






Exceptions

IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ThrottlingException


    :return: {
        'namespaceArn': 'string',
        'namespaceName': 'string'
    }
    
    
    """
    pass

def delete_system_instance(id=None):
    """
    Deletes a system instance. Only system instances that have never been deployed, or that have been undeployed can be deleted.
    Users can create a new system instance that has the same ID as a deleted system instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_system_instance(
        id='string'
    )
    
    
    :type id: string
    :param id: The ID of the system instance to be deleted.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceInUseException


    :return: {}
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceInUseException
    
    """
    pass

def delete_system_template(id=None):
    """
    Deletes a system. New deployments can\'t contain the system after its deletion. Existing deployments that contain the system will continue to work because they use a snapshot of the system that is taken when it is deployed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_system_template(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the system to be deleted.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceInUseException


    :return: {}
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceInUseException
    
    """
    pass

def deploy_system_instance(id=None):
    """
    Deploys the system instance to the target specified in CreateSystemInstance .
    If the system or any workflows and entities have been updated before this action is called, then the deployment will create a new Amazon Simple Storage Service resource file and then deploy it.
    Since this action creates a Greengrass deployment on the caller\'s behalf, the calling identity must have write permissions to the specified Greengrass group. Otherwise, the call will fail with an authorization error.
    For information about the artifacts that get added to your Greengrass core device when you use this API, see AWS IoT Things Graph and AWS IoT Greengrass .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deploy_system_instance(
        id='string'
    )
    
    
    :type id: string
    :param id: The ID of the system instance. This value is returned by the CreateSystemInstance action.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:deployment:DEPLOYMENTNAME\n

    :rtype: dict
ReturnsResponse Syntax{
    'summary': {
        'id': 'string',
        'arn': 'string',
        'status': 'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'|'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
        'target': 'GREENGRASS'|'CLOUD',
        'greengrassGroupName': 'string',
        'createdAt': datetime(2015, 1, 1),
        'updatedAt': datetime(2015, 1, 1),
        'greengrassGroupId': 'string',
        'greengrassGroupVersionId': 'string'
    },
    'greengrassDeploymentId': 'string'
}


Response Structure

(dict) --
summary (dict) --An object that contains summary information about a system instance that was deployed.

id (string) --The ID of the system instance.

arn (string) --The ARN of the system instance.

status (string) --The status of the system instance.

target (string) --The target of the system instance.

greengrassGroupName (string) --The ID of the Greengrass group where the system instance is deployed.

createdAt (datetime) --The date when the system instance was created.

updatedAt (datetime) --The date and time when the system instance was last updated.

greengrassGroupId (string) --The ID of the Greengrass group where the system instance is deployed.

greengrassGroupVersionId (string) --The version of the Greengrass group where the system instance is deployed.



greengrassDeploymentId (string) --The ID of the Greengrass deployment used to deploy the system instance.






Exceptions

IoTThingsGraph.Client.exceptions.ResourceNotFoundException
IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceInUseException


    :return: {
        'summary': {
            'id': 'string',
            'arn': 'string',
            'status': 'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'|'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
            'target': 'GREENGRASS'|'CLOUD',
            'greengrassGroupName': 'string',
            'createdAt': datetime(2015, 1, 1),
            'updatedAt': datetime(2015, 1, 1),
            'greengrassGroupId': 'string',
            'greengrassGroupVersionId': 'string'
        },
        'greengrassDeploymentId': 'string'
    }
    
    
    """
    pass

def deprecate_flow_template(id=None):
    """
    Deprecates the specified workflow. This action marks the workflow for deletion. Deprecated flows can\'t be deployed, but existing deployments will continue to run.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deprecate_flow_template(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the workflow to be deleted.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def deprecate_system_template(id=None):
    """
    Deprecates the specified system.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deprecate_system_template(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the system to delete.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_namespace(namespaceName=None):
    """
    Gets the latest version of the user\'s namespace and the public version that it is tracking.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_namespace(
        namespaceName='string'
    )
    
    
    :type namespaceName: string
    :param namespaceName: The name of the user\'s namespace. Set this to aws to get the public namespace.

    :rtype: dict
ReturnsResponse Syntax{
    'namespaceArn': 'string',
    'namespaceName': 'string',
    'trackingNamespaceName': 'string',
    'trackingNamespaceVersion': 123,
    'namespaceVersion': 123
}


Response Structure

(dict) --
namespaceArn (string) --The ARN of the namespace.

namespaceName (string) --The name of the namespace.

trackingNamespaceName (string) --The name of the public namespace that the latest namespace version is tracking.

trackingNamespaceVersion (integer) --The version of the public namespace that the latest version is tracking.

namespaceVersion (integer) --The version of the user\'s namespace to describe.






Exceptions

IoTThingsGraph.Client.exceptions.ResourceNotFoundException
IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ThrottlingException


    :return: {
        'namespaceArn': 'string',
        'namespaceName': 'string',
        'trackingNamespaceName': 'string',
        'trackingNamespaceVersion': 123,
        'namespaceVersion': 123
    }
    
    
    """
    pass

def dissociate_entity_from_thing(thingName=None, entityType=None):
    """
    Dissociates a device entity from a concrete thing. The action takes only the type of the entity that you need to dissociate because only one entity of a particular type can be associated with a thing.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.dissociate_entity_from_thing(
        thingName='string',
        entityType='DEVICE'|'SERVICE'|'DEVICE_MODEL'|'CAPABILITY'|'STATE'|'ACTION'|'EVENT'|'PROPERTY'|'MAPPING'|'ENUM'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing to disassociate.\n

    :type entityType: string
    :param entityType: [REQUIRED]\nThe entity type from which to disassociate the thing.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def get_entities(ids=None, namespaceVersion=None):
    """
    Gets definitions of the specified entities. Uses the latest version of the user\'s namespace by default. This API returns the following TDM entities.
    This action doesn\'t return definitions for systems, flows, and deployments.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_entities(
        ids=[
            'string',
        ],
        namespaceVersion=123
    )
    
    
    :type ids: list
    :param ids: [REQUIRED]\nAn array of entity IDs.\nThe IDs should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME\n\n(string) --\n\n

    :type namespaceVersion: integer
    :param namespaceVersion: The version of the user\'s namespace. Defaults to the latest version of the user\'s namespace.

    :rtype: dict

ReturnsResponse Syntax
{
    'descriptions': [
        {
            'id': 'string',
            'arn': 'string',
            'type': 'DEVICE'|'SERVICE'|'DEVICE_MODEL'|'CAPABILITY'|'STATE'|'ACTION'|'EVENT'|'PROPERTY'|'MAPPING'|'ENUM',
            'createdAt': datetime(2015, 1, 1),
            'definition': {
                'language': 'GRAPHQL',
                'text': 'string'
            }
        },
    ]
}


Response Structure

(dict) --

descriptions (list) --
An array of descriptions for the specified entities.

(dict) --
Describes the properties of an entity.

id (string) --
The entity ID.

arn (string) --
The entity ARN.

type (string) --
The entity type.

createdAt (datetime) --
The time at which the entity was created.

definition (dict) --
The definition document of the entity.

language (string) --
The language used to define the entity. GRAPHQL is the only valid value.

text (string) --
The GraphQL text that defines the entity.













Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {
        'descriptions': [
            {
                'id': 'string',
                'arn': 'string',
                'type': 'DEVICE'|'SERVICE'|'DEVICE_MODEL'|'CAPABILITY'|'STATE'|'ACTION'|'EVENT'|'PROPERTY'|'MAPPING'|'ENUM',
                'createdAt': datetime(2015, 1, 1),
                'definition': {
                    'language': 'GRAPHQL',
                    'text': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    ids (list) -- [REQUIRED]
    An array of entity IDs.
    The IDs should be in the following format.
    
    urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME
    
    (string) --
    
    
    namespaceVersion (integer) -- The version of the user\'s namespace. Defaults to the latest version of the user\'s namespace.
    
    """
    pass

def get_flow_template(id=None, revisionNumber=None):
    """
    Gets the latest version of the DefinitionDocument and FlowTemplateSummary for the specified workflow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_flow_template(
        id='string',
        revisionNumber=123
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the workflow.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME\n

    :type revisionNumber: integer
    :param revisionNumber: The number of the workflow revision to retrieve.

    :rtype: dict

ReturnsResponse Syntax
{
    'description': {
        'summary': {
            'id': 'string',
            'arn': 'string',
            'revisionNumber': 123,
            'createdAt': datetime(2015, 1, 1)
        },
        'definition': {
            'language': 'GRAPHQL',
            'text': 'string'
        },
        'validatedNamespaceVersion': 123
    }
}


Response Structure

(dict) --

description (dict) --
The object that describes the specified workflow.

summary (dict) --
An object that contains summary information about a workflow.

id (string) --
The ID of the workflow.

arn (string) --
The ARN of the workflow.

revisionNumber (integer) --
The revision number of the workflow.

createdAt (datetime) --
The date when the workflow was created.



definition (dict) --
A workflow\'s definition document.

language (string) --
The language used to define the entity. GRAPHQL is the only valid value.

text (string) --
The GraphQL text that defines the entity.



validatedNamespaceVersion (integer) --
The version of the user\'s namespace against which the workflow was validated. Use this value in your system instance.









Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException


    :return: {
        'description': {
            'summary': {
                'id': 'string',
                'arn': 'string',
                'revisionNumber': 123,
                'createdAt': datetime(2015, 1, 1)
            },
            'definition': {
                'language': 'GRAPHQL',
                'text': 'string'
            },
            'validatedNamespaceVersion': 123
        }
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def get_flow_template_revisions(id=None, nextToken=None, maxResults=None):
    """
    Gets revisions of the specified workflow. Only the last 100 revisions are stored. If the workflow has been deprecated, this action will return revisions that occurred before the deprecation. This action won\'t work for workflows that have been deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_flow_template_revisions(
        id='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the workflow.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME\n

    :type nextToken: string
    :param nextToken: The string that specifies the next page of results. Use this when you\'re paginating results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'summaries': [
        {
            'id': 'string',
            'arn': 'string',
            'revisionNumber': 123,
            'createdAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

summaries (list) --
An array of objects that provide summary data about each revision.

(dict) --
An object that contains summary information about a workflow.

id (string) --
The ID of the workflow.

arn (string) --
The ARN of the workflow.

revisionNumber (integer) --
The revision number of the workflow.

createdAt (datetime) --
The date when the workflow was created.





nextToken (string) --
The string to specify as nextToken when you request the next page of results.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException


    :return: {
        'summaries': [
            {
                'id': 'string',
                'arn': 'string',
                'revisionNumber': 123,
                'createdAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def get_namespace_deletion_status():
    """
    Gets the status of a namespace deletion task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_namespace_deletion_status()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'namespaceArn': 'string',
    'namespaceName': 'string',
    'status': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
    'errorCode': 'VALIDATION_FAILED',
    'errorMessage': 'string'
}


Response Structure

(dict) --
namespaceArn (string) --The ARN of the namespace that is being deleted.

namespaceName (string) --The name of the namespace that is being deleted.

status (string) --The status of the deletion request.

errorCode (string) --An error code returned by the namespace deletion task.

errorMessage (string) --An error code returned by the namespace deletion task.






Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ThrottlingException


    :return: {
        'namespaceArn': 'string',
        'namespaceName': 'string',
        'status': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'errorCode': 'VALIDATION_FAILED',
        'errorMessage': 'string'
    }
    
    
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

def get_system_instance(id=None):
    """
    Gets a system instance.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_system_instance(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the system deployment instance. This value is returned by CreateSystemInstance .\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:deployment:DEPLOYMENTNAME\n

    :rtype: dict
ReturnsResponse Syntax{
    'description': {
        'summary': {
            'id': 'string',
            'arn': 'string',
            'status': 'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'|'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
            'target': 'GREENGRASS'|'CLOUD',
            'greengrassGroupName': 'string',
            'createdAt': datetime(2015, 1, 1),
            'updatedAt': datetime(2015, 1, 1),
            'greengrassGroupId': 'string',
            'greengrassGroupVersionId': 'string'
        },
        'definition': {
            'language': 'GRAPHQL',
            'text': 'string'
        },
        's3BucketName': 'string',
        'metricsConfiguration': {
            'cloudMetricEnabled': True|False,
            'metricRuleRoleArn': 'string'
        },
        'validatedNamespaceVersion': 123,
        'validatedDependencyRevisions': [
            {
                'id': 'string',
                'revisionNumber': 123
            },
        ],
        'flowActionsRoleArn': 'string'
    }
}


Response Structure

(dict) --
description (dict) --An object that describes the system instance.

summary (dict) --An object that contains summary information about a system instance.

id (string) --The ID of the system instance.

arn (string) --The ARN of the system instance.

status (string) --The status of the system instance.

target (string) --The target of the system instance.

greengrassGroupName (string) --The ID of the Greengrass group where the system instance is deployed.

createdAt (datetime) --The date when the system instance was created.

updatedAt (datetime) --The date and time when the system instance was last updated.

greengrassGroupId (string) --The ID of the Greengrass group where the system instance is deployed.

greengrassGroupVersionId (string) --The version of the Greengrass group where the system instance is deployed.



definition (dict) --A document that defines an entity.

language (string) --The language used to define the entity. GRAPHQL is the only valid value.

text (string) --The GraphQL text that defines the entity.



s3BucketName (string) --The Amazon Simple Storage Service bucket where information about a system instance is stored.

metricsConfiguration (dict) --An object that specifies whether cloud metrics are collected in a deployment and, if so, what role is used to collect metrics.

cloudMetricEnabled (boolean) --A Boolean that specifies whether cloud metrics are collected.

metricRuleRoleArn (string) --The ARN of the role that is used to collect cloud metrics.



validatedNamespaceVersion (integer) --The version of the user\'s namespace against which the system instance was validated.

validatedDependencyRevisions (list) --A list of objects that contain all of the IDs and revision numbers of workflows and systems that are used in a system instance.

(dict) --An object that contains the ID and revision number of a workflow or system that is part of a deployment.

id (string) --The ID of the workflow or system.

revisionNumber (integer) --The revision number of the workflow or system.





flowActionsRoleArn (string) --The AWS Identity and Access Management (IAM) role that AWS IoT Things Graph assumes during flow execution in a cloud deployment. This role must have read and write permissionss to AWS Lambda and AWS IoT and to any other AWS services that the flow uses.








Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException


    :return: {
        'description': {
            'summary': {
                'id': 'string',
                'arn': 'string',
                'status': 'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'|'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
                'target': 'GREENGRASS'|'CLOUD',
                'greengrassGroupName': 'string',
                'createdAt': datetime(2015, 1, 1),
                'updatedAt': datetime(2015, 1, 1),
                'greengrassGroupId': 'string',
                'greengrassGroupVersionId': 'string'
            },
            'definition': {
                'language': 'GRAPHQL',
                'text': 'string'
            },
            's3BucketName': 'string',
            'metricsConfiguration': {
                'cloudMetricEnabled': True|False,
                'metricRuleRoleArn': 'string'
            },
            'validatedNamespaceVersion': 123,
            'validatedDependencyRevisions': [
                {
                    'id': 'string',
                    'revisionNumber': 123
                },
            ],
            'flowActionsRoleArn': 'string'
        }
    }
    
    
    """
    pass

def get_system_template(id=None, revisionNumber=None):
    """
    Gets a system.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_system_template(
        id='string',
        revisionNumber=123
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the system to get. This ID must be in the user\'s namespace.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME\n

    :type revisionNumber: integer
    :param revisionNumber: The number that specifies the revision of the system to get.

    :rtype: dict

ReturnsResponse Syntax
{
    'description': {
        'summary': {
            'id': 'string',
            'arn': 'string',
            'revisionNumber': 123,
            'createdAt': datetime(2015, 1, 1)
        },
        'definition': {
            'language': 'GRAPHQL',
            'text': 'string'
        },
        'validatedNamespaceVersion': 123
    }
}


Response Structure

(dict) --

description (dict) --
An object that contains summary data about the system.

summary (dict) --
An object that contains summary information about a system.

id (string) --
The ID of the system.

arn (string) --
The ARN of the system.

revisionNumber (integer) --
The revision number of the system.

createdAt (datetime) --
The date when the system was created.



definition (dict) --
The definition document of a system.

language (string) --
The language used to define the entity. GRAPHQL is the only valid value.

text (string) --
The GraphQL text that defines the entity.



validatedNamespaceVersion (integer) --
The namespace version against which the system was validated. Use this value in your system instance.









Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException


    :return: {
        'description': {
            'summary': {
                'id': 'string',
                'arn': 'string',
                'revisionNumber': 123,
                'createdAt': datetime(2015, 1, 1)
            },
            'definition': {
                'language': 'GRAPHQL',
                'text': 'string'
            },
            'validatedNamespaceVersion': 123
        }
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def get_system_template_revisions(id=None, nextToken=None, maxResults=None):
    """
    Gets revisions made to the specified system template. Only the previous 100 revisions are stored. If the system has been deprecated, this action will return the revisions that occurred before its deprecation. This action won\'t work with systems that have been deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_system_template_revisions(
        id='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the system template.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME\n

    :type nextToken: string
    :param nextToken: The string that specifies the next page of results. Use this when you\'re paginating results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'summaries': [
        {
            'id': 'string',
            'arn': 'string',
            'revisionNumber': 123,
            'createdAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

summaries (list) --
An array of objects that contain summary data about the system template revisions.

(dict) --
An object that contains information about a system.

id (string) --
The ID of the system.

arn (string) --
The ARN of the system.

revisionNumber (integer) --
The revision number of the system.

createdAt (datetime) --
The date when the system was created.





nextToken (string) --
The string to specify as nextToken when you request the next page of results.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException


    :return: {
        'summaries': [
            {
                'id': 'string',
                'arn': 'string',
                'revisionNumber': 123,
                'createdAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def get_upload_status(uploadId=None):
    """
    Gets the status of the specified upload.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_upload_status(
        uploadId='string'
    )
    
    
    :type uploadId: string
    :param uploadId: [REQUIRED]\nThe ID of the upload. This value is returned by the UploadEntityDefinitions action.\n

    :rtype: dict
ReturnsResponse Syntax{
    'uploadId': 'string',
    'uploadStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
    'namespaceArn': 'string',
    'namespaceName': 'string',
    'namespaceVersion': 123,
    'failureReason': [
        'string',
    ],
    'createdDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
uploadId (string) --The ID of the upload.

uploadStatus (string) --The status of the upload. The initial status is IN_PROGRESS . The response show all validation failures if the upload fails.

namespaceArn (string) --The ARN of the upload.

namespaceName (string) --The name of the upload\'s namespace.

namespaceVersion (integer) --The version of the user\'s namespace. Defaults to the latest version of the user\'s namespace.

failureReason (list) --The reason for an upload failure.

(string) --


createdDate (datetime) --The date at which the upload was created.






Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ThrottlingException


    :return: {
        'uploadId': 'string',
        'uploadStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
        'namespaceArn': 'string',
        'namespaceName': 'string',
        'namespaceVersion': 123,
        'failureReason': [
            'string',
        ],
        'createdDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    
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

def list_flow_execution_messages(flowExecutionId=None, nextToken=None, maxResults=None):
    """
    Returns a list of objects that contain information about events in a flow execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_flow_execution_messages(
        flowExecutionId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type flowExecutionId: string
    :param flowExecutionId: [REQUIRED]\nThe ID of the flow execution.\n

    :type nextToken: string
    :param nextToken: The string that specifies the next page of results. Use this when you\'re paginating results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'messages': [
        {
            'messageId': 'string',
            'eventType': 'EXECUTION_STARTED'|'EXECUTION_FAILED'|'EXECUTION_ABORTED'|'EXECUTION_SUCCEEDED'|'STEP_STARTED'|'STEP_FAILED'|'STEP_SUCCEEDED'|'ACTIVITY_SCHEDULED'|'ACTIVITY_STARTED'|'ACTIVITY_FAILED'|'ACTIVITY_SUCCEEDED'|'START_FLOW_EXECUTION_TASK'|'SCHEDULE_NEXT_READY_STEPS_TASK'|'THING_ACTION_TASK'|'THING_ACTION_TASK_FAILED'|'THING_ACTION_TASK_SUCCEEDED'|'ACKNOWLEDGE_TASK_MESSAGE',
            'timestamp': datetime(2015, 1, 1),
            'payload': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

messages (list) --
A list of objects that contain information about events in the specified flow execution.

(dict) --
An object that contains information about a flow event.

messageId (string) --
The unique identifier of the message.

eventType (string) --
The type of flow event .

timestamp (datetime) --
The date and time when the message was last updated.

payload (string) --
A string containing information about the flow event.





nextToken (string) --
The string to specify as nextToken when you request the next page of results.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException


    :return: {
        'messages': [
            {
                'messageId': 'string',
                'eventType': 'EXECUTION_STARTED'|'EXECUTION_FAILED'|'EXECUTION_ABORTED'|'EXECUTION_SUCCEEDED'|'STEP_STARTED'|'STEP_FAILED'|'STEP_SUCCEEDED'|'ACTIVITY_SCHEDULED'|'ACTIVITY_STARTED'|'ACTIVITY_FAILED'|'ACTIVITY_SUCCEEDED'|'START_FLOW_EXECUTION_TASK'|'SCHEDULE_NEXT_READY_STEPS_TASK'|'THING_ACTION_TASK'|'THING_ACTION_TASK_FAILED'|'THING_ACTION_TASK_SUCCEEDED'|'ACKNOWLEDGE_TASK_MESSAGE',
                'timestamp': datetime(2015, 1, 1),
                'payload': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_tags_for_resource(maxResults=None, resourceArn=None, nextToken=None):
    """
    Lists all tags on an AWS IoT Things Graph resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        maxResults=123,
        resourceArn='string',
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of tags to return.

    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource whose tags are to be returned.\n

    :type nextToken: string
    :param nextToken: The token that specifies the next page of results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'tags': [
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

tags (list) --
List of tags returned by the ListTagsForResource operation.

(dict) --
Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.

key (string) --
The required name of the tag. The string value can be from 1 to 128 Unicode characters in length.

value (string) --
The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length.





nextToken (string) --
The token that specifies the next page of results to return.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceAlreadyExistsException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ResourceAlreadyExistsException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    
    """
    pass

def search_entities(entityTypes=None, filters=None, nextToken=None, maxResults=None, namespaceVersion=None):
    """
    Searches for entities of the specified type. You can search for entities in your namespace and the public namespace that you\'re tracking.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_entities(
        entityTypes=[
            'DEVICE'|'SERVICE'|'DEVICE_MODEL'|'CAPABILITY'|'STATE'|'ACTION'|'EVENT'|'PROPERTY'|'MAPPING'|'ENUM',
        ],
        filters=[
            {
                'name': 'NAME'|'NAMESPACE'|'SEMANTIC_TYPE_PATH'|'REFERENCED_ENTITY_ID',
                'value': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123,
        namespaceVersion=123
    )
    
    
    :type entityTypes: list
    :param entityTypes: [REQUIRED]\nThe entity types for which to search.\n\n(string) --\n\n

    :type filters: list
    :param filters: Optional filter to apply to the search. Valid filters are NAME NAMESPACE , SEMANTIC_TYPE_PATH and REFERENCED_ENTITY_ID . REFERENCED_ENTITY_ID filters on entities that are used by the entity in the result set. For example, you can filter on the ID of a property that is used in a state.\nMultiple filters function as OR criteria in the query. Multiple values passed inside the filter function as AND criteria.\n\n(dict) --An object that filters an entity search. Multiple filters function as OR criteria in the search. For example a search that includes a NAMESPACE and a REFERENCED_ENTITY_ID filter searches for entities in the specified namespace that use the entity specified by the value of REFERENCED_ENTITY_ID .\n\nname (string) --The name of the entity search filter field. REFERENCED_ENTITY_ID filters on entities that are used by the entity in the result set. For example, you can filter on the ID of a property that is used in a state.\n\nvalue (list) --An array of string values for the search filter field. Multiple values function as AND criteria in the search.\n\n(string) --\n\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The string that specifies the next page of results. Use this when you\'re paginating results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :type namespaceVersion: integer
    :param namespaceVersion: The version of the user\'s namespace. Defaults to the latest version of the user\'s namespace.

    :rtype: dict

ReturnsResponse Syntax
{
    'descriptions': [
        {
            'id': 'string',
            'arn': 'string',
            'type': 'DEVICE'|'SERVICE'|'DEVICE_MODEL'|'CAPABILITY'|'STATE'|'ACTION'|'EVENT'|'PROPERTY'|'MAPPING'|'ENUM',
            'createdAt': datetime(2015, 1, 1),
            'definition': {
                'language': 'GRAPHQL',
                'text': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

descriptions (list) --
An array of descriptions for each entity returned in the search result.

(dict) --
Describes the properties of an entity.

id (string) --
The entity ID.

arn (string) --
The entity ARN.

type (string) --
The entity type.

createdAt (datetime) --
The time at which the entity was created.

definition (dict) --
The definition document of the entity.

language (string) --
The language used to define the entity. GRAPHQL is the only valid value.

text (string) --
The GraphQL text that defines the entity.







nextToken (string) --
The string to specify as nextToken when you request the next page of results.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ThrottlingException


    :return: {
        'descriptions': [
            {
                'id': 'string',
                'arn': 'string',
                'type': 'DEVICE'|'SERVICE'|'DEVICE_MODEL'|'CAPABILITY'|'STATE'|'ACTION'|'EVENT'|'PROPERTY'|'MAPPING'|'ENUM',
                'createdAt': datetime(2015, 1, 1),
                'definition': {
                    'language': 'GRAPHQL',
                    'text': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    
    """
    pass

def search_flow_executions(systemInstanceId=None, flowExecutionId=None, startTime=None, endTime=None, nextToken=None, maxResults=None):
    """
    Searches for AWS IoT Things Graph workflow execution instances.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_flow_executions(
        systemInstanceId='string',
        flowExecutionId='string',
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        nextToken='string',
        maxResults=123
    )
    
    
    :type systemInstanceId: string
    :param systemInstanceId: [REQUIRED]\nThe ID of the system instance that contains the flow.\n

    :type flowExecutionId: string
    :param flowExecutionId: The ID of a flow execution.

    :type startTime: datetime
    :param startTime: The date and time of the earliest flow execution to return.

    :type endTime: datetime
    :param endTime: The date and time of the latest flow execution to return.

    :type nextToken: string
    :param nextToken: The string that specifies the next page of results. Use this when you\'re paginating results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'summaries': [
        {
            'flowExecutionId': 'string',
            'status': 'RUNNING'|'ABORTED'|'SUCCEEDED'|'FAILED',
            'systemInstanceId': 'string',
            'flowTemplateId': 'string',
            'createdAt': datetime(2015, 1, 1),
            'updatedAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

summaries (list) --
An array of objects that contain summary information about each workflow execution in the result set.

(dict) --
An object that contains summary information about a flow execution.

flowExecutionId (string) --
The ID of the flow execution.

status (string) --
The current status of the flow execution.

systemInstanceId (string) --
The ID of the system instance that contains the flow.

flowTemplateId (string) --
The ID of the flow.

createdAt (datetime) --
The date and time when the flow execution summary was created.

updatedAt (datetime) --
The date and time when the flow execution summary was last updated.





nextToken (string) --
The string to specify as nextToken when you request the next page of results.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException


    :return: {
        'summaries': [
            {
                'flowExecutionId': 'string',
                'status': 'RUNNING'|'ABORTED'|'SUCCEEDED'|'FAILED',
                'systemInstanceId': 'string',
                'flowTemplateId': 'string',
                'createdAt': datetime(2015, 1, 1),
                'updatedAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def search_flow_templates(filters=None, nextToken=None, maxResults=None):
    """
    Searches for summary information about workflows.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_flow_templates(
        filters=[
            {
                'name': 'DEVICE_MODEL_ID',
                'value': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type filters: list
    :param filters: An array of objects that limit the result set. The only valid filter is DEVICE_MODEL_ID .\n\n(dict) --An object that filters a workflow search.\n\nname (string) -- [REQUIRED]The name of the search filter field.\n\nvalue (list) -- [REQUIRED]An array of string values for the search filter field. Multiple values function as AND criteria in the search.\n\n(string) --\n\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The string that specifies the next page of results. Use this when you\'re paginating results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'summaries': [
        {
            'id': 'string',
            'arn': 'string',
            'revisionNumber': 123,
            'createdAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

summaries (list) --
An array of objects that contain summary information about each workflow in the result set.

(dict) --
An object that contains summary information about a workflow.

id (string) --
The ID of the workflow.

arn (string) --
The ARN of the workflow.

revisionNumber (integer) --
The revision number of the workflow.

createdAt (datetime) --
The date when the workflow was created.





nextToken (string) --
The string to specify as nextToken when you request the next page of results.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {
        'summaries': [
            {
                'id': 'string',
                'arn': 'string',
                'revisionNumber': 123,
                'createdAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    
    """
    pass

def search_system_instances(filters=None, nextToken=None, maxResults=None):
    """
    Searches for system instances in the user\'s account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_system_instances(
        filters=[
            {
                'name': 'SYSTEM_TEMPLATE_ID'|'STATUS'|'GREENGRASS_GROUP_NAME',
                'value': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type filters: list
    :param filters: Optional filter to apply to the search. Valid filters are SYSTEM_TEMPLATE_ID , STATUS , and GREENGRASS_GROUP_NAME .\nMultiple filters function as OR criteria in the query. Multiple values passed inside the filter function as AND criteria.\n\n(dict) --An object that filters a system instance search. Multiple filters function as OR criteria in the search. For example a search that includes a GREENGRASS_GROUP_NAME and a STATUS filter searches for system instances in the specified Greengrass group that have the specified status.\n\nname (string) --The name of the search filter field.\n\nvalue (list) --An array of string values for the search filter field. Multiple values function as AND criteria in the search.\n\n(string) --\n\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The string that specifies the next page of results. Use this when you\'re paginating results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'summaries': [
        {
            'id': 'string',
            'arn': 'string',
            'status': 'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'|'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
            'target': 'GREENGRASS'|'CLOUD',
            'greengrassGroupName': 'string',
            'createdAt': datetime(2015, 1, 1),
            'updatedAt': datetime(2015, 1, 1),
            'greengrassGroupId': 'string',
            'greengrassGroupVersionId': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

summaries (list) --
An array of objects that contain summary data abour the system instances in the result set.

(dict) --
An object that contains summary information about a system instance.

id (string) --
The ID of the system instance.

arn (string) --
The ARN of the system instance.

status (string) --
The status of the system instance.

target (string) --
The target of the system instance.

greengrassGroupName (string) --
The ID of the Greengrass group where the system instance is deployed.

createdAt (datetime) --
The date when the system instance was created.

updatedAt (datetime) --
The date and time when the system instance was last updated.

greengrassGroupId (string) --
The ID of the Greengrass group where the system instance is deployed.

greengrassGroupVersionId (string) --
The version of the Greengrass group where the system instance is deployed.





nextToken (string) --
The string to specify as nextToken when you request the next page of results.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {
        'summaries': [
            {
                'id': 'string',
                'arn': 'string',
                'status': 'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'|'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
                'target': 'GREENGRASS'|'CLOUD',
                'greengrassGroupName': 'string',
                'createdAt': datetime(2015, 1, 1),
                'updatedAt': datetime(2015, 1, 1),
                'greengrassGroupId': 'string',
                'greengrassGroupVersionId': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    
    """
    pass

def search_system_templates(filters=None, nextToken=None, maxResults=None):
    """
    Searches for summary information about systems in the user\'s account. You can filter by the ID of a workflow to return only systems that use the specified workflow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_system_templates(
        filters=[
            {
                'name': 'FLOW_TEMPLATE_ID',
                'value': [
                    'string',
                ]
            },
        ],
        nextToken='string',
        maxResults=123
    )
    
    
    :type filters: list
    :param filters: An array of filters that limit the result set. The only valid filter is FLOW_TEMPLATE_ID .\n\n(dict) --An object that filters a system search.\n\nname (string) -- [REQUIRED]The name of the system search filter field.\n\nvalue (list) -- [REQUIRED]An array of string values for the search filter field. Multiple values function as AND criteria in the search.\n\n(string) --\n\n\n\n\n\n

    :type nextToken: string
    :param nextToken: The string that specifies the next page of results. Use this when you\'re paginating results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :rtype: dict

ReturnsResponse Syntax
{
    'summaries': [
        {
            'id': 'string',
            'arn': 'string',
            'revisionNumber': 123,
            'createdAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

summaries (list) --
An array of objects that contain summary information about each system deployment in the result set.

(dict) --
An object that contains information about a system.

id (string) --
The ID of the system.

arn (string) --
The ARN of the system.

revisionNumber (integer) --
The revision number of the system.

createdAt (datetime) --
The date when the system was created.





nextToken (string) --
The string to specify as nextToken when you request the next page of results.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {
        'summaries': [
            {
                'id': 'string',
                'arn': 'string',
                'revisionNumber': 123,
                'createdAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    
    """
    pass

def search_things(entityId=None, nextToken=None, maxResults=None, namespaceVersion=None):
    """
    Searches for things associated with the specified entity. You can search by both device and device model.
    For example, if two different devices, camera1 and camera2, implement the camera device model, the user can associate thing1 to camera1 and thing2 to camera2. SearchThings(camera2) will return only thing2, but SearchThings(camera) will return both thing1 and thing2.
    This action searches for exact matches and doesn\'t perform partial text matching.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_things(
        entityId='string',
        nextToken='string',
        maxResults=123,
        namespaceVersion=123
    )
    
    
    :type entityId: string
    :param entityId: [REQUIRED]\nThe ID of the entity to which the things are associated.\nThe IDs should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME\n

    :type nextToken: string
    :param nextToken: The string that specifies the next page of results. Use this when you\'re paginating results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in the response.

    :type namespaceVersion: integer
    :param namespaceVersion: The version of the user\'s namespace. Defaults to the latest version of the user\'s namespace.

    :rtype: dict

ReturnsResponse Syntax
{
    'things': [
        {
            'thingArn': 'string',
            'thingName': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

things (list) --
An array of things in the result set.

(dict) --
An AWS IoT thing.

thingArn (string) --
The ARN of the thing.

thingName (string) --
The name of the thing.





nextToken (string) --
The string to specify as nextToken when you request the next page of results.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ThrottlingException


    :return: {
        'things': [
            {
                'thingArn': 'string',
                'thingName': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Creates a tag for the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource whose tags are returned.\n

    :type tags: list
    :param tags: [REQUIRED]\nA list of tags to add to the resource.>\n\n(dict) --Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.\n\nkey (string) -- [REQUIRED]The required name of the tag. The string value can be from 1 to 128 Unicode characters in length.\n\nvalue (string) -- [REQUIRED]The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceAlreadyExistsException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def undeploy_system_instance(id=None):
    """
    Removes a system instance from its target (Cloud or Greengrass).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.undeploy_system_instance(
        id='string'
    )
    
    
    :type id: string
    :param id: The ID of the system instance to remove from its target.

    :rtype: dict
ReturnsResponse Syntax{
    'summary': {
        'id': 'string',
        'arn': 'string',
        'status': 'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'|'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
        'target': 'GREENGRASS'|'CLOUD',
        'greengrassGroupName': 'string',
        'createdAt': datetime(2015, 1, 1),
        'updatedAt': datetime(2015, 1, 1),
        'greengrassGroupId': 'string',
        'greengrassGroupVersionId': 'string'
    }
}


Response Structure

(dict) --
summary (dict) --An object that contains summary information about the system instance that was removed from its target.

id (string) --The ID of the system instance.

arn (string) --The ARN of the system instance.

status (string) --The status of the system instance.

target (string) --The target of the system instance.

greengrassGroupName (string) --The ID of the Greengrass group where the system instance is deployed.

createdAt (datetime) --The date when the system instance was created.

updatedAt (datetime) --The date and time when the system instance was last updated.

greengrassGroupId (string) --The ID of the Greengrass group where the system instance is deployed.

greengrassGroupVersionId (string) --The version of the Greengrass group where the system instance is deployed.








Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException
IoTThingsGraph.Client.exceptions.ResourceInUseException


    :return: {
        'summary': {
            'id': 'string',
            'arn': 'string',
            'status': 'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'|'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
            'target': 'GREENGRASS'|'CLOUD',
            'greengrassGroupName': 'string',
            'createdAt': datetime(2015, 1, 1),
            'updatedAt': datetime(2015, 1, 1),
            'greengrassGroupId': 'string',
            'greengrassGroupVersionId': 'string'
        }
    }
    
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes a tag from the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource whose tags are to be removed.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nA list of tag key names to remove from the resource. You don\'t specify the value. Both the key and its associated value are removed.\nThis parameter to the API requires a JSON text string argument. For information on how to format a JSON parameter for the various command line tool environments, see Using JSON for Parameters in the AWS CLI User Guide .\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceAlreadyExistsException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_flow_template(id=None, definition=None, compatibleNamespaceVersion=None):
    """
    Updates the specified workflow. All deployed systems and system instances that use the workflow will see the changes in the flow when it is redeployed. If you don\'t want this behavior, copy the workflow (creating a new workflow with a different ID), and update the copy. The workflow can contain only entities in the specified namespace.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_flow_template(
        id='string',
        definition={
            'language': 'GRAPHQL',
            'text': 'string'
        },
        compatibleNamespaceVersion=123
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the workflow to be updated.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME\n

    :type definition: dict
    :param definition: [REQUIRED]\nThe DefinitionDocument that contains the updated workflow definition.\n\nlanguage (string) -- [REQUIRED]The language used to define the entity. GRAPHQL is the only valid value.\n\ntext (string) -- [REQUIRED]The GraphQL text that defines the entity.\n\n\n

    :type compatibleNamespaceVersion: integer
    :param compatibleNamespaceVersion: The version of the user\'s namespace.\nIf no value is specified, the latest version is used by default. Use the GetFlowTemplateRevisions if you want to find earlier revisions of the flow to update.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'summary': {
        'id': 'string',
        'arn': 'string',
        'revisionNumber': 123,
        'createdAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

summary (dict) --
An object containing summary information about the updated workflow.

id (string) --
The ID of the workflow.

arn (string) --
The ARN of the workflow.

revisionNumber (integer) --
The revision number of the workflow.

createdAt (datetime) --
The date when the workflow was created.









Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {
        'summary': {
            'id': 'string',
            'arn': 'string',
            'revisionNumber': 123,
            'createdAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    
    """
    pass

def update_system_template(id=None, definition=None, compatibleNamespaceVersion=None):
    """
    Updates the specified system. You don\'t need to run this action after updating a workflow. Any deployment that uses the system will see the changes in the system when it is redeployed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_system_template(
        id='string',
        definition={
            'language': 'GRAPHQL',
            'text': 'string'
        },
        compatibleNamespaceVersion=123
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the system to be updated.\nThe ID should be in the following format.\n\nurn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME\n

    :type definition: dict
    :param definition: [REQUIRED]\nThe DefinitionDocument that contains the updated system definition.\n\nlanguage (string) -- [REQUIRED]The language used to define the entity. GRAPHQL is the only valid value.\n\ntext (string) -- [REQUIRED]The GraphQL text that defines the entity.\n\n\n

    :type compatibleNamespaceVersion: integer
    :param compatibleNamespaceVersion: The version of the user\'s namespace. Defaults to the latest version of the user\'s namespace.\nIf no value is specified, the latest version is used by default.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'summary': {
        'id': 'string',
        'arn': 'string',
        'revisionNumber': 123,
        'createdAt': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

summary (dict) --
An object containing summary information about the updated system.

id (string) --
The ID of the system.

arn (string) --
The ARN of the system.

revisionNumber (integer) --
The revision number of the system.

createdAt (datetime) --
The date when the system was created.









Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.ResourceNotFoundException
IoTThingsGraph.Client.exceptions.ThrottlingException
IoTThingsGraph.Client.exceptions.InternalFailureException


    :return: {
        'summary': {
            'id': 'string',
            'arn': 'string',
            'revisionNumber': 123,
            'createdAt': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.ResourceNotFoundException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    
    """
    pass

def upload_entity_definitions(document=None, syncWithPublicNamespace=None, deprecateExistingEntities=None):
    """
    Asynchronously uploads one or more entity definitions to the user\'s namespace. The document parameter is required if syncWithPublicNamespace and deleteExistingEntites are false. If the syncWithPublicNamespace parameter is set to true , the user\'s namespace will synchronize with the latest version of the public namespace. If deprecateExistingEntities is set to true, all entities in the latest version will be deleted before the new DefinitionDocument is uploaded.
    When a user uploads entity definitions for the first time, the service creates a new namespace for the user. The new namespace tracks the public namespace. Currently users can have only one namespace. The namespace version increments whenever a user uploads entity definitions that are backwards-incompatible and whenever a user sets the syncWithPublicNamespace parameter or the deprecateExistingEntities parameter to true .
    The IDs for all of the entities should be in URN format. Each entity must be in the user\'s namespace. Users can\'t create entities in the public namespace, but entity definitions can refer to entities in the public namespace.
    Valid entities are Device , DeviceModel , Service , Capability , State , Action , Event , Property , Mapping , Enum .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.upload_entity_definitions(
        document={
            'language': 'GRAPHQL',
            'text': 'string'
        },
        syncWithPublicNamespace=True|False,
        deprecateExistingEntities=True|False
    )
    
    
    :type document: dict
    :param document: The DefinitionDocument that defines the updated entities.\n\nlanguage (string) -- [REQUIRED]The language used to define the entity. GRAPHQL is the only valid value.\n\ntext (string) -- [REQUIRED]The GraphQL text that defines the entity.\n\n\n

    :type syncWithPublicNamespace: boolean
    :param syncWithPublicNamespace: A Boolean that specifies whether to synchronize with the latest version of the public namespace. If set to true , the upload will create a new namespace version.

    :type deprecateExistingEntities: boolean
    :param deprecateExistingEntities: A Boolean that specifies whether to deprecate all entities in the latest version before uploading the new DefinitionDocument . If set to true , the upload will create a new namespace version.

    :rtype: dict

ReturnsResponse Syntax
{
    'uploadId': 'string'
}


Response Structure

(dict) --

uploadId (string) --
The ID that specifies the upload action. You can use this to track the status of the upload.







Exceptions

IoTThingsGraph.Client.exceptions.InvalidRequestException
IoTThingsGraph.Client.exceptions.InternalFailureException
IoTThingsGraph.Client.exceptions.ThrottlingException


    :return: {
        'uploadId': 'string'
    }
    
    
    :returns: 
    IoTThingsGraph.Client.exceptions.InvalidRequestException
    IoTThingsGraph.Client.exceptions.InternalFailureException
    IoTThingsGraph.Client.exceptions.ThrottlingException
    
    """
    pass

