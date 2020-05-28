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

def associate_assets(assetId=None, hierarchyId=None, childAssetId=None, clientToken=None):
    """
    Associates a child asset with the given parent asset through a hierarchy defined in the parent asset\'s model. For more information, see Associating Assets in the AWS IoT SiteWise User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_assets(
        assetId='string',
        hierarchyId='string',
        childAssetId='string',
        clientToken='string'
    )
    
    
    :type assetId: string
    :param assetId: [REQUIRED]\nThe ID of the parent asset.\n

    :type hierarchyId: string
    :param hierarchyId: [REQUIRED]\nThe ID of a hierarchy in the parent asset\'s model. Hierarchies allow different groupings of assets to be formed that all come from the same asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .\n

    :type childAssetId: string
    :param childAssetId: [REQUIRED]\nThe ID of the child asset to be associated.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.LimitExceededException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def batch_associate_project_assets(projectId=None, assetIds=None, clientToken=None):
    """
    Associates a group (batch) of assets with an AWS IoT SiteWise Monitor project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_associate_project_assets(
        projectId='string',
        assetIds=[
            'string',
        ],
        clientToken='string'
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project to which to associate the assets.\n

    :type assetIds: list
    :param assetIds: [REQUIRED]\nThe IDs of the assets to be associated to the project.\n\n(string) --\n\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'errors': [
        {
            'assetId': 'string',
            'code': 'INTERNAL_FAILURE',
            'message': 'string'
        },
    ]
}


Response Structure

(dict) --

errors (list) --
A list of associated error information, if any.

(dict) --
Contains error details for the requested associate project asset action.

assetId (string) --
The ID of the asset.

code (string) --
The error code.

message (string) --
The error message.











Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.LimitExceededException


    :return: {
        'errors': [
            {
                'assetId': 'string',
                'code': 'INTERNAL_FAILURE',
                'message': 'string'
            },
        ]
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.LimitExceededException
    
    """
    pass

def batch_disassociate_project_assets(projectId=None, assetIds=None, clientToken=None):
    """
    Disassociates a group (batch) of assets from an AWS IoT SiteWise Monitor project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_disassociate_project_assets(
        projectId='string',
        assetIds=[
            'string',
        ],
        clientToken='string'
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project from which to disassociate the assets.\n

    :type assetIds: list
    :param assetIds: [REQUIRED]\nThe IDs of the assets to be disassociated from the project.\n\n(string) --\n\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'errors': [
        {
            'assetId': 'string',
            'code': 'INTERNAL_FAILURE',
            'message': 'string'
        },
    ]
}


Response Structure

(dict) --

errors (list) --
A list of associated error information, if any.

(dict) --
Contains error details for the requested associate project asset action.

assetId (string) --
The ID of the asset.

code (string) --
The error code.

message (string) --
The error message.











Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'errors': [
            {
                'assetId': 'string',
                'code': 'INTERNAL_FAILURE',
                'message': 'string'
            },
        ]
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    
    """
    pass

def batch_put_asset_property_value(entries=None):
    """
    Sends a list of asset property values to AWS IoT SiteWise. Each value is a timestamp-quality-value (TQV) data point. For more information, see Ingesting Data Using the API in the AWS IoT SiteWise User Guide .
    To identify an asset property, you must specify one of the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_put_asset_property_value(
        entries=[
            {
                'entryId': 'string',
                'assetId': 'string',
                'propertyId': 'string',
                'propertyAlias': 'string',
                'propertyValues': [
                    {
                        'value': {
                            'stringValue': 'string',
                            'integerValue': 123,
                            'doubleValue': 123.0,
                            'booleanValue': True|False
                        },
                        'timestamp': {
                            'timeInSeconds': 123,
                            'offsetInNanos': 123
                        },
                        'quality': 'GOOD'|'BAD'|'UNCERTAIN'
                    },
                ]
            },
        ]
    )
    
    
    :type entries: list
    :param entries: [REQUIRED]\nThe list of asset property value entries for the batch put request. You can specify up to 10 entries per request.\n\n(dict) --Contains a list of value updates for an asset property in the list of asset entries consumed by the BatchPutAssetPropertyValue API.\n\nentryId (string) -- [REQUIRED]The user specified ID for the entry. You can use this ID to identify which entries failed.\n\nassetId (string) --The ID of the asset to update.\n\npropertyId (string) --The ID of the asset property for this entry.\n\npropertyAlias (string) --The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping Industrial Data Streams to Asset Properties in the AWS IoT SiteWise User Guide .\n\npropertyValues (list) -- [REQUIRED]The list of property values to upload. You can specify up to 10 propertyValues array elements.\n\n(dict) --Contains asset property value information.\n\nvalue (dict) -- [REQUIRED]The value of the asset property (see Variant ).\n\nstringValue (string) --Asset property data of type string (sequence of characters).\n\nintegerValue (integer) --Asset property data of type integer (whole number).\n\ndoubleValue (float) --Asset property data of type double (floating point number).\n\nbooleanValue (boolean) --Asset property data of type Boolean (true or false).\n\n\n\ntimestamp (dict) -- [REQUIRED]The timestamp of the asset property value.\n\ntimeInSeconds (integer) -- [REQUIRED]The timestamp date, in seconds, in the Unix epoch format. Fractional nanosecond data is provided by offsetInNanos .\n\noffsetInNanos (integer) --The nanosecond offset from timeInSeconds .\n\n\n\nquality (string) --The quality of the asset property value.\n\n\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'errorEntries': [
        {
            'entryId': 'string',
            'errors': [
                {
                    'errorCode': 'ResourceNotFoundException'|'InvalidRequestException'|'InternalFailureException'|'ServiceUnavailableException'|'ThrottlingException'|'LimitExceededException'|'ConflictingOperationException'|'TimestampOutOfRangeException'|'AccessDeniedException',
                    'errorMessage': 'string',
                    'timestamps': [
                        {
                            'timeInSeconds': 123,
                            'offsetInNanos': 123
                        },
                    ]
                },
            ]
        },
    ]
}


Response Structure

(dict) --
errorEntries (list) --A list of the errors (if any) associated with the batch put request. Each error entry contains the entryId of the entry that failed.

(dict) --Contains error information for asset property value entries that are associated with the BatchPutAssetPropertyValue API.

entryId (string) --The ID of the failed entry.

errors (list) --The list of update property value errors.

(dict) --Contains error information from updating a batch of asset property values.

errorCode (string) --The error code.

errorMessage (string) --The associated error message.

timestamps (list) --A list of timestamps for each error, if any.

(dict) --Contains a timestamp with optional nanosecond granularity.

timeInSeconds (integer) --The timestamp date, in seconds, in the Unix epoch format. Fractional nanosecond data is provided by offsetInNanos .

offsetInNanos (integer) --The nanosecond offset from timeInSeconds .


















Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.LimitExceededException
IoTSiteWise.Client.exceptions.ServiceUnavailableException
IoTSiteWise.Client.exceptions.ConflictingOperationException


    :return: {
        'errorEntries': [
            {
                'entryId': 'string',
                'errors': [
                    {
                        'errorCode': 'ResourceNotFoundException'|'InvalidRequestException'|'InternalFailureException'|'ServiceUnavailableException'|'ThrottlingException'|'LimitExceededException'|'ConflictingOperationException'|'TimestampOutOfRangeException'|'AccessDeniedException',
                        'errorMessage': 'string',
                        'timestamps': [
                            {
                                'timeInSeconds': 123,
                                'offsetInNanos': 123
                            },
                        ]
                    },
                ]
            },
        ]
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.LimitExceededException
    IoTSiteWise.Client.exceptions.ServiceUnavailableException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_access_policy(accessPolicyIdentity=None, accessPolicyResource=None, accessPolicyPermission=None, clientToken=None, tags=None):
    """
    Creates an access policy that grants the specified AWS Single Sign-On user or group access to the specified AWS IoT SiteWise Monitor portal or project resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_access_policy(
        accessPolicyIdentity={
            'user': {
                'id': 'string'
            },
            'group': {
                'id': 'string'
            }
        },
        accessPolicyResource={
            'portal': {
                'id': 'string'
            },
            'project': {
                'id': 'string'
            }
        },
        accessPolicyPermission='ADMINISTRATOR'|'VIEWER',
        clientToken='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type accessPolicyIdentity: dict
    :param accessPolicyIdentity: [REQUIRED]\nThe identity for this access policy. Choose either a user or a group but not both.\n\nuser (dict) --A user identity.\n\nid (string) -- [REQUIRED]The AWS SSO ID of the user.\n\n\n\ngroup (dict) --A group identity.\n\nid (string) -- [REQUIRED]The AWS SSO ID of the group.\n\n\n\n\n

    :type accessPolicyResource: dict
    :param accessPolicyResource: [REQUIRED]\nThe AWS IoT SiteWise Monitor resource for this access policy. Choose either portal or project but not both.\n\nportal (dict) --A portal resource.\n\nid (string) -- [REQUIRED]The ID of the portal.\n\n\n\nproject (dict) --A project resource.\n\nid (string) -- [REQUIRED]The ID of the project.\n\n\n\n\n

    :type accessPolicyPermission: string
    :param accessPolicyPermission: [REQUIRED]\nThe permission level for this access policy. Note that a project ADMINISTRATOR is also known as a project owner.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :type tags: dict
    :param tags: A list of key-value pairs that contain metadata for the access policy. For more information, see Tagging your AWS IoT SiteWise resources in the AWS IoT SiteWise User Guide .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'accessPolicyId': 'string',
    'accessPolicyArn': 'string'
}


Response Structure

(dict) --

accessPolicyId (string) --
The ID of the access policy.

accessPolicyArn (string) --
The ARN of the access policy, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:access-policy/${AccessPolicyId}








Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.LimitExceededException


    :return: {
        'accessPolicyId': 'string',
        'accessPolicyArn': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.LimitExceededException
    
    """
    pass

def create_asset(assetName=None, assetModelId=None, clientToken=None, tags=None):
    """
    Creates an asset from an existing asset model. For more information, see Creating Assets in the AWS IoT SiteWise User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_asset(
        assetName='string',
        assetModelId='string',
        clientToken='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type assetName: string
    :param assetName: [REQUIRED]\nA unique, friendly name for the asset.\n

    :type assetModelId: string
    :param assetModelId: [REQUIRED]\nThe ID of the asset model from which to create the asset.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :type tags: dict
    :param tags: A list of key-value pairs that contain metadata for the asset. For more information, see Tagging your AWS IoT SiteWise resources in the AWS IoT SiteWise User Guide .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'assetId': 'string',
    'assetArn': 'string',
    'assetStatus': {
        'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
        'error': {
            'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --

assetId (string) --
The ID of the asset. This ID uniquely identifies the asset within AWS IoT SiteWise and can be used with other AWS IoT SiteWise APIs.

assetArn (string) --
The ARN of the asset, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}


assetStatus (dict) --
The status of the asset, which contains a state (CREATING after successfully calling this operation) and any error message.

state (string) --
The current status of the asset.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.











Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceAlreadyExistsException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.LimitExceededException
IoTSiteWise.Client.exceptions.ConflictingOperationException


    :return: {
        'assetId': 'string',
        'assetArn': 'string',
        'assetStatus': {
            'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
            'error': {
                'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                'message': 'string'
            }
        }
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceAlreadyExistsException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.LimitExceededException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def create_asset_model(assetModelName=None, assetModelDescription=None, assetModelProperties=None, assetModelHierarchies=None, clientToken=None, tags=None):
    """
    Creates an asset model from specified property and hierarchy definitions. You create assets from asset models. With asset models, you can easily create assets of the same type that have standardized definitions. Each asset created from a model inherits the asset model\'s property and hierarchy definitions. For more information, see Defining Asset Models in the AWS IoT SiteWise User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_asset_model(
        assetModelName='string',
        assetModelDescription='string',
        assetModelProperties=[
            {
                'name': 'string',
                'dataType': 'STRING'|'INTEGER'|'DOUBLE'|'BOOLEAN',
                'unit': 'string',
                'type': {
                    'attribute': {
                        'defaultValue': 'string'
                    },
                    'measurement': {}
                    ,
                    'transform': {
                        'expression': 'string',
                        'variables': [
                            {
                                'name': 'string',
                                'value': {
                                    'propertyId': 'string',
                                    'hierarchyId': 'string'
                                }
                            },
                        ]
                    },
                    'metric': {
                        'expression': 'string',
                        'variables': [
                            {
                                'name': 'string',
                                'value': {
                                    'propertyId': 'string',
                                    'hierarchyId': 'string'
                                }
                            },
                        ],
                        'window': {
                            'tumbling': {
                                'interval': 'string'
                            }
                        }
                    }
                }
            },
        ],
        assetModelHierarchies=[
            {
                'name': 'string',
                'childAssetModelId': 'string'
            },
        ],
        clientToken='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type assetModelName: string
    :param assetModelName: [REQUIRED]\nA unique, friendly name for the asset model.\n

    :type assetModelDescription: string
    :param assetModelDescription: A description for the asset model.

    :type assetModelProperties: list
    :param assetModelProperties: The property definitions of the asset model. For more information, see Asset Properties in the AWS IoT SiteWise User Guide .\nYou can specify up to 200 properties per asset model. For more information, see Quotas in the AWS IoT SiteWise User Guide .\n\n(dict) --Contains an asset model property definition. This property definition is applied to all assets created from the asset model.\n\nname (string) -- [REQUIRED]The name of the property definition.\n\ndataType (string) -- [REQUIRED]The data type of the property definition.\n\nunit (string) --The unit of the property definition, such as Newtons or RPM .\n\ntype (dict) -- [REQUIRED]The property definition type (see PropertyType ). You can only specify one type in a property definition.\n\nattribute (dict) --Specifies an asset attribute property. An attribute generally contains static information, such as the serial number of an IIoT wind turbine.\n\ndefaultValue (string) --The default value of the asset model property attribute. All assets that you create from the asset model contain this attribute value. You can update an attribute\'s value after you create an asset. For more information, see Updating Attribute Values in the AWS IoT SiteWise User Guide .\n\n\n\nmeasurement (dict) --Specifies an asset measurement property. A measurement represents a device\'s raw sensor data stream, such as timestamped temperature values or timestamped power values.\n\ntransform (dict) --Specifies an asset transform property. A transform contains a mathematical expression that maps a property\'s data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.\n\nexpression (string) -- [REQUIRED]The mathematical expression that defines the transformation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.\nFor more information, see Quotas in the AWS IoT SiteWise User Guide .\n\nvariables (list) -- [REQUIRED]The list of variables used in the expression.\n\n(dict) --Contains expression variable information.\n\nname (string) -- [REQUIRED]The friendly name of the variable to be used in the expression.\n\nvalue (dict) -- [REQUIRED]The variable that identifies an asset property from which to use values.\n\npropertyId (string) -- [REQUIRED]The ID of the property to use as the variable. You can use the property name if it\'s from the same asset model.\n\nhierarchyId (string) --The ID of the hierarchy to query for the property ID. You can use the hierarchy\'s name instead of the hierarchy\'s ID.\nYou use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same propertyId . For example, you might have separately grouped assets that come from the same asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .\n\n\n\n\n\n\n\n\n\nmetric (dict) --Specifies an asset metric property. A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.\n\nexpression (string) -- [REQUIRED]The mathematical expression that defines the metric aggregation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.\nFor more information, see Quotas in the AWS IoT SiteWise User Guide .\n\nvariables (list) -- [REQUIRED]The list of variables used in the expression.\n\n(dict) --Contains expression variable information.\n\nname (string) -- [REQUIRED]The friendly name of the variable to be used in the expression.\n\nvalue (dict) -- [REQUIRED]The variable that identifies an asset property from which to use values.\n\npropertyId (string) -- [REQUIRED]The ID of the property to use as the variable. You can use the property name if it\'s from the same asset model.\n\nhierarchyId (string) --The ID of the hierarchy to query for the property ID. You can use the hierarchy\'s name instead of the hierarchy\'s ID.\nYou use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same propertyId . For example, you might have separately grouped assets that come from the same asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .\n\n\n\n\n\n\n\nwindow (dict) -- [REQUIRED]The window (time interval) over which AWS IoT SiteWise computes the metric\'s aggregation expression. AWS IoT SiteWise computes one data point per window .\n\ntumbling (dict) --The tumbling time interval window.\n\ninterval (string) -- [REQUIRED]The time interval for the tumbling window. Note that w represents weeks, d represents days, h represents hours, and m represents minutes. AWS IoT SiteWise computes the 1w interval the end of Sunday at midnight each week (UTC), the 1d interval at the end of each day at midnight (UTC), the 1h interval at the end of each hour, and so on.\nWhen AWS IoT SiteWise aggregates data points for metric computations, the start of each interval is exclusive and the end of each interval is inclusive. AWS IoT SiteWise places the computed data point at the end of the interval.\n\n\n\n\n\n\n\n\n\n\n\n\n

    :type assetModelHierarchies: list
    :param assetModelHierarchies: The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .\nYou can specify up to 10 hierarchies per asset model. For more information, see Quotas in the AWS IoT SiteWise User Guide .\n\n(dict) --Contains an asset model hierarchy used in asset model creation. An asset model hierarchy determines the kind (or type) of asset that can belong to a hierarchy.\n\nname (string) -- [REQUIRED]The name of the asset model hierarchy definition (as specified in CreateAssetModel or UpdateAssetModel ).\n\nchildAssetModelId (string) -- [REQUIRED]The ID of an asset model for this hierarchy.\n\n\n\n\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :type tags: dict
    :param tags: A list of key-value pairs that contain metadata for the asset model. For more information, see Tagging your AWS IoT SiteWise resources in the AWS IoT SiteWise User Guide .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'assetModelId': 'string',
    'assetModelArn': 'string',
    'assetModelStatus': {
        'state': 'CREATING'|'ACTIVE'|'UPDATING'|'PROPAGATING'|'DELETING'|'FAILED',
        'error': {
            'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --

assetModelId (string) --
The ID of the asset model. You can use this ID when you call other AWS IoT SiteWise APIs.

assetModelArn (string) --
The ARN of the asset model, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}


assetModelStatus (dict) --
The status of the asset model, which contains a state (CREATING after successfully calling this operation) and any error message.

state (string) --
The current state of the asset model.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.











Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceAlreadyExistsException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.LimitExceededException
IoTSiteWise.Client.exceptions.ConflictingOperationException


    :return: {
        'assetModelId': 'string',
        'assetModelArn': 'string',
        'assetModelStatus': {
            'state': 'CREATING'|'ACTIVE'|'UPDATING'|'PROPAGATING'|'DELETING'|'FAILED',
            'error': {
                'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                'message': 'string'
            }
        }
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceAlreadyExistsException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.LimitExceededException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def create_dashboard(projectId=None, dashboardName=None, dashboardDescription=None, dashboardDefinition=None, clientToken=None, tags=None):
    """
    Creates a dashboard in an AWS IoT SiteWise Monitor project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_dashboard(
        projectId='string',
        dashboardName='string',
        dashboardDescription='string',
        dashboardDefinition='string',
        clientToken='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project in which to create the dashboard.\n

    :type dashboardName: string
    :param dashboardName: [REQUIRED]\nA friendly name for the dashboard.\n

    :type dashboardDescription: string
    :param dashboardDescription: A description for the dashboard.

    :type dashboardDefinition: string
    :param dashboardDefinition: [REQUIRED]\nThe dashboard definition specified in a JSON literal. For detailed information, see Creating Dashboards (CLI) in the AWS IoT SiteWise User Guide .\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :type tags: dict
    :param tags: A list of key-value pairs that contain metadata for the dashboard. For more information, see Tagging your AWS IoT SiteWise resources in the AWS IoT SiteWise User Guide .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'dashboardId': 'string',
    'dashboardArn': 'string'
}


Response Structure

(dict) --

dashboardId (string) --
The ID of the dashboard.

dashboardArn (string) --
The ARN of the dashboard, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:dashboard/${DashboardId}








Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.LimitExceededException


    :return: {
        'dashboardId': 'string',
        'dashboardArn': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.LimitExceededException
    
    """
    pass

def create_gateway(gatewayName=None, gatewayPlatform=None, tags=None):
    """
    Creates a gateway, which is a virtual or edge device that delivers industrial data streams from local servers to AWS IoT SiteWise. For more information, see Ingesting data using a gateway in the AWS IoT SiteWise User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_gateway(
        gatewayName='string',
        gatewayPlatform={
            'greengrass': {
                'groupArn': 'string'
            }
        },
        tags={
            'string': 'string'
        }
    )
    
    
    :type gatewayName: string
    :param gatewayName: [REQUIRED]\nA unique, friendly name for the gateway.\n

    :type gatewayPlatform: dict
    :param gatewayPlatform: [REQUIRED]\nThe gateway\'s platform. You can only specify one platform in a gateway.\n\ngreengrass (dict) -- [REQUIRED]A gateway that runs on AWS IoT Greengrass.\n\ngroupArn (string) -- [REQUIRED]The ARN of the Greengrass group. For more information about how to find a group\'s ARN, see ListGroups and GetGroup in the AWS IoT Greengrass API Reference .\n\n\n\n\n

    :type tags: dict
    :param tags: A list of key-value pairs that contain metadata for the gateway. For more information, see Tagging your AWS IoT SiteWise resources in the AWS IoT SiteWise User Guide .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'gatewayId': 'string',
    'gatewayArn': 'string'
}


Response Structure

(dict) --

gatewayId (string) --
The ID of the gateway device. You can use this ID when you call other AWS IoT SiteWise APIs.

gatewayArn (string) --
The ARN of the gateway, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:gateway/${GatewayId}








Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceAlreadyExistsException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.LimitExceededException


    :return: {
        'gatewayId': 'string',
        'gatewayArn': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceAlreadyExistsException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.LimitExceededException
    
    """
    pass

def create_portal(portalName=None, portalDescription=None, portalContactEmail=None, clientToken=None, portalLogoImageFile=None, roleArn=None, tags=None):
    """
    Creates a portal, which can contain projects and dashboards. Before you can create a portal, you must configure AWS Single Sign-On in the current Region. AWS IoT SiteWise Monitor uses AWS SSO to manage user permissions. For more information, see Enabling AWS SSO in the AWS IoT SiteWise User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_portal(
        portalName='string',
        portalDescription='string',
        portalContactEmail='string',
        clientToken='string',
        portalLogoImageFile={
            'data': b'bytes',
            'type': 'PNG'
        },
        roleArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type portalName: string
    :param portalName: [REQUIRED]\nA friendly name for the portal.\n

    :type portalDescription: string
    :param portalDescription: A description for the portal.

    :type portalContactEmail: string
    :param portalContactEmail: [REQUIRED]\nThe AWS administrator\'s contact email address.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :type portalLogoImageFile: dict
    :param portalLogoImageFile: A logo image to display in the portal. Upload a square, high-resolution image. The image is displayed on a dark background.\n\ndata (bytes) -- [REQUIRED]The image file contents, represented as a base64-encoded string. The file size must be less than 1 MB.\n\ntype (string) -- [REQUIRED]The file type of the image.\n\n\n

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe ARN of a service role that allows the portal\'s users to access your AWS IoT SiteWise resources on your behalf. For more information, see Using service roles for AWS IoT SiteWise Monitor in the AWS IoT SiteWise User Guide .\n

    :type tags: dict
    :param tags: A list of key-value pairs that contain metadata for the portal. For more information, see Tagging your AWS IoT SiteWise resources in the AWS IoT SiteWise User Guide .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'portalId': 'string',
    'portalArn': 'string',
    'portalStartUrl': 'string',
    'portalStatus': {
        'state': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'FAILED',
        'error': {
            'code': 'INTERNAL_FAILURE',
            'message': 'string'
        }
    },
    'ssoApplicationId': 'string'
}


Response Structure

(dict) --

portalId (string) --
The ID of the created portal.

portalArn (string) --
The ARN of the portal, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:portal/${PortalId}


portalStartUrl (string) --
The public URL for the AWS IoT SiteWise Monitor portal.

portalStatus (dict) --
The status of the portal, which contains a state (CREATING after successfully calling this operation) and any error message.

state (string) --
The current state of the portal.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.





ssoApplicationId (string) --
The associated AWS SSO application Id.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.LimitExceededException


    :return: {
        'portalId': 'string',
        'portalArn': 'string',
        'portalStartUrl': 'string',
        'portalStatus': {
            'state': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'FAILED',
            'error': {
                'code': 'INTERNAL_FAILURE',
                'message': 'string'
            }
        },
        'ssoApplicationId': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.LimitExceededException
    
    """
    pass

def create_project(portalId=None, projectName=None, projectDescription=None, clientToken=None, tags=None):
    """
    Creates a project in the specified portal.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_project(
        portalId='string',
        projectName='string',
        projectDescription='string',
        clientToken='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type portalId: string
    :param portalId: [REQUIRED]\nThe ID of the portal in which to create the project.\n

    :type projectName: string
    :param projectName: [REQUIRED]\nA friendly name for the project.\n

    :type projectDescription: string
    :param projectDescription: A description for the project.

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :type tags: dict
    :param tags: A list of key-value pairs that contain metadata for the project. For more information, see Tagging your AWS IoT SiteWise resources in the AWS IoT SiteWise User Guide .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'projectId': 'string',
    'projectArn': 'string'
}


Response Structure

(dict) --

projectId (string) --
The ID of the project.

projectArn (string) --
The ARN of the project, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:project/${ProjectId}








Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.LimitExceededException


    :return: {
        'projectId': 'string',
        'projectArn': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.LimitExceededException
    
    """
    pass

def delete_access_policy(accessPolicyId=None, clientToken=None):
    """
    Deletes an access policy that grants the specified AWS Single Sign-On identity access to the specified AWS IoT SiteWise Monitor resource. You can use this operation to revoke access to an AWS IoT SiteWise Monitor resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_access_policy(
        accessPolicyId='string',
        clientToken='string'
    )
    
    
    :type accessPolicyId: string
    :param accessPolicyId: [REQUIRED]\nThe ID of the access policy to be deleted.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_asset(assetId=None, clientToken=None):
    """
    Deletes an asset. This action can\'t be undone. For more information, see Deleting Assets and Models in the AWS IoT SiteWise User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_asset(
        assetId='string',
        clientToken='string'
    )
    
    
    :type assetId: string
    :param assetId: [REQUIRED]\nThe ID of the asset to delete.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'assetStatus': {
        'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
        'error': {
            'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --

assetStatus (dict) --
The status of the asset, which contains a state (DELETING after successfully calling this operation) and any error message.

state (string) --
The current status of the asset.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.











Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ConflictingOperationException


    :return: {
        'assetStatus': {
            'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
            'error': {
                'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                'message': 'string'
            }
        }
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def delete_asset_model(assetModelId=None, clientToken=None):
    """
    Deletes an asset model. This action can\'t be undone. You must delete all assets created from an asset model before you can delete the model. Also, you can\'t delete an asset model if a parent asset model exists that contains a property formula expression that depends on the asset model that you want to delete. For more information, see Deleting Assets and Models in the AWS IoT SiteWise User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_asset_model(
        assetModelId='string',
        clientToken='string'
    )
    
    
    :type assetModelId: string
    :param assetModelId: [REQUIRED]\nThe ID of the asset model to delete.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'assetModelStatus': {
        'state': 'CREATING'|'ACTIVE'|'UPDATING'|'PROPAGATING'|'DELETING'|'FAILED',
        'error': {
            'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --

assetModelStatus (dict) --
The status of the asset model, which contains a state (DELETING after successfully calling this operation) and any error message.

state (string) --
The current state of the asset model.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.











Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ConflictingOperationException


    :return: {
        'assetModelStatus': {
            'state': 'CREATING'|'ACTIVE'|'UPDATING'|'PROPAGATING'|'DELETING'|'FAILED',
            'error': {
                'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                'message': 'string'
            }
        }
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def delete_dashboard(dashboardId=None, clientToken=None):
    """
    Deletes a dashboard from AWS IoT SiteWise Monitor.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_dashboard(
        dashboardId='string',
        clientToken='string'
    )
    
    
    :type dashboardId: string
    :param dashboardId: [REQUIRED]\nThe ID of the dashboard to delete.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_gateway(gatewayId=None):
    """
    Deletes a gateway from AWS IoT SiteWise. When you delete a gateway, some of the gateway\'s files remain in your gateway\'s file system. For more information, see Data retention in the AWS IoT SiteWise User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_gateway(
        gatewayId='string'
    )
    
    
    :type gatewayId: string
    :param gatewayId: [REQUIRED]\nThe ID of the gateway to delete.\n

    """
    pass

def delete_portal(portalId=None, clientToken=None):
    """
    Deletes a portal from AWS IoT SiteWise Monitor.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_portal(
        portalId='string',
        clientToken='string'
    )
    
    
    :type portalId: string
    :param portalId: [REQUIRED]\nThe ID of the portal to delete.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'portalStatus': {
        'state': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'FAILED',
        'error': {
            'code': 'INTERNAL_FAILURE',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --

portalStatus (dict) --
The status of the portal, which contains a state (DELETING after successfully calling this operation) and any error message.

state (string) --
The current state of the portal.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.











Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ConflictingOperationException


    :return: {
        'portalStatus': {
            'state': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'FAILED',
            'error': {
                'code': 'INTERNAL_FAILURE',
                'message': 'string'
            }
        }
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def delete_project(projectId=None, clientToken=None):
    """
    Deletes a project from AWS IoT SiteWise Monitor.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_project(
        projectId='string',
        clientToken='string'
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_access_policy(accessPolicyId=None):
    """
    Describes an access policy, which specifies an AWS SSO user or group\'s access to an AWS IoT SiteWise Monitor portal or project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_access_policy(
        accessPolicyId='string'
    )
    
    
    :type accessPolicyId: string
    :param accessPolicyId: [REQUIRED]\nThe ID of the access policy.\n

    :rtype: dict
ReturnsResponse Syntax{
    'accessPolicyId': 'string',
    'accessPolicyArn': 'string',
    'accessPolicyIdentity': {
        'user': {
            'id': 'string'
        },
        'group': {
            'id': 'string'
        }
    },
    'accessPolicyResource': {
        'portal': {
            'id': 'string'
        },
        'project': {
            'id': 'string'
        }
    },
    'accessPolicyPermission': 'ADMINISTRATOR'|'VIEWER',
    'accessPolicyCreationDate': datetime(2015, 1, 1),
    'accessPolicyLastUpdateDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
accessPolicyId (string) --The ID of the access policy.

accessPolicyArn (string) --The ARN of the access policy, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:access-policy/${AccessPolicyId}

accessPolicyIdentity (dict) --The AWS SSO identity (user or group) to which this access policy applies.

user (dict) --A user identity.

id (string) --The AWS SSO ID of the user.



group (dict) --A group identity.

id (string) --The AWS SSO ID of the group.





accessPolicyResource (dict) --The AWS IoT SiteWise Monitor resource (portal or project) to which this access policy provides access.

portal (dict) --A portal resource.

id (string) --The ID of the portal.



project (dict) --A project resource.

id (string) --The ID of the project.





accessPolicyPermission (string) --The access policy permission. Note that a project ADMINISTRATOR is also known as a project owner.

accessPolicyCreationDate (datetime) --The date the access policy was created, in Unix epoch time.

accessPolicyLastUpdateDate (datetime) --The date the access policy was last updated, in Unix epoch time.






Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'accessPolicyId': 'string',
        'accessPolicyArn': 'string',
        'accessPolicyIdentity': {
            'user': {
                'id': 'string'
            },
            'group': {
                'id': 'string'
            }
        },
        'accessPolicyResource': {
            'portal': {
                'id': 'string'
            },
            'project': {
                'id': 'string'
            }
        },
        'accessPolicyPermission': 'ADMINISTRATOR'|'VIEWER',
        'accessPolicyCreationDate': datetime(2015, 1, 1),
        'accessPolicyLastUpdateDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_asset(assetId=None):
    """
    Retrieves information about an asset.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_asset(
        assetId='string'
    )
    
    
    :type assetId: string
    :param assetId: [REQUIRED]\nThe ID of the asset.\n

    :rtype: dict
ReturnsResponse Syntax{
    'assetId': 'string',
    'assetArn': 'string',
    'assetName': 'string',
    'assetModelId': 'string',
    'assetProperties': [
        {
            'id': 'string',
            'name': 'string',
            'alias': 'string',
            'notification': {
                'topic': 'string',
                'state': 'ENABLED'|'DISABLED'
            },
            'dataType': 'STRING'|'INTEGER'|'DOUBLE'|'BOOLEAN',
            'unit': 'string'
        },
    ],
    'assetHierarchies': [
        {
            'id': 'string',
            'name': 'string'
        },
    ],
    'assetCreationDate': datetime(2015, 1, 1),
    'assetLastUpdateDate': datetime(2015, 1, 1),
    'assetStatus': {
        'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
        'error': {
            'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --
assetId (string) --The ID of the asset.

assetArn (string) --The ARN of the asset, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}

assetName (string) --The name of the asset.

assetModelId (string) --The ID of the asset model that was used to create the asset.

assetProperties (list) --The list of asset properties for the asset.

(dict) --Contains asset property information.

id (string) --The ID of the asset property.

name (string) --The name of the property.

alias (string) --The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping Industrial Data Streams to Asset Properties in the AWS IoT SiteWise User Guide .

notification (dict) --The asset property\'s notification topic and state. For more information, see UpdateAssetProperty

topic (string) --The MQTT topic to which AWS IoT SiteWise publishes property value update notifications.

state (string) --The current notification state.



dataType (string) --The data type of the asset property.

unit (string) --The unit (such as Newtons or RPM ) of the asset property.





assetHierarchies (list) --A list of asset hierarchies that each contain a hierarchyId . A hierarchy specifies allowed parent/child asset relationships.

(dict) --Describes an asset hierarchy that contains a hierarchy\'s name and ID.

id (string) --The ID of the hierarchy. This ID is a hierarchyId .

name (string) --The hierarchy name provided in the CreateAssetModel or UpdateAssetModel API.





assetCreationDate (datetime) --The date the asset was created, in Unix epoch time.

assetLastUpdateDate (datetime) --The date the asset was last updated, in Unix epoch time.

assetStatus (dict) --The current status of the asset, which contains a state and any error message.

state (string) --The current status of the asset.

error (dict) --Contains associated error information, if any.

code (string) --The error code.

message (string) --The error message.










Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'assetId': 'string',
        'assetArn': 'string',
        'assetName': 'string',
        'assetModelId': 'string',
        'assetProperties': [
            {
                'id': 'string',
                'name': 'string',
                'alias': 'string',
                'notification': {
                    'topic': 'string',
                    'state': 'ENABLED'|'DISABLED'
                },
                'dataType': 'STRING'|'INTEGER'|'DOUBLE'|'BOOLEAN',
                'unit': 'string'
            },
        ],
        'assetHierarchies': [
            {
                'id': 'string',
                'name': 'string'
            },
        ],
        'assetCreationDate': datetime(2015, 1, 1),
        'assetLastUpdateDate': datetime(2015, 1, 1),
        'assetStatus': {
            'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
            'error': {
                'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                'message': 'string'
            }
        }
    }
    
    
    """
    pass

def describe_asset_model(assetModelId=None):
    """
    Retrieves information about an asset model.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_asset_model(
        assetModelId='string'
    )
    
    
    :type assetModelId: string
    :param assetModelId: [REQUIRED]\nThe ID of the asset model.\n

    :rtype: dict
ReturnsResponse Syntax{
    'assetModelId': 'string',
    'assetModelArn': 'string',
    'assetModelName': 'string',
    'assetModelDescription': 'string',
    'assetModelProperties': [
        {
            'id': 'string',
            'name': 'string',
            'dataType': 'STRING'|'INTEGER'|'DOUBLE'|'BOOLEAN',
            'unit': 'string',
            'type': {
                'attribute': {
                    'defaultValue': 'string'
                },
                'measurement': {},
                'transform': {
                    'expression': 'string',
                    'variables': [
                        {
                            'name': 'string',
                            'value': {
                                'propertyId': 'string',
                                'hierarchyId': 'string'
                            }
                        },
                    ]
                },
                'metric': {
                    'expression': 'string',
                    'variables': [
                        {
                            'name': 'string',
                            'value': {
                                'propertyId': 'string',
                                'hierarchyId': 'string'
                            }
                        },
                    ],
                    'window': {
                        'tumbling': {
                            'interval': 'string'
                        }
                    }
                }
            }
        },
    ],
    'assetModelHierarchies': [
        {
            'id': 'string',
            'name': 'string',
            'childAssetModelId': 'string'
        },
    ],
    'assetModelCreationDate': datetime(2015, 1, 1),
    'assetModelLastUpdateDate': datetime(2015, 1, 1),
    'assetModelStatus': {
        'state': 'CREATING'|'ACTIVE'|'UPDATING'|'PROPAGATING'|'DELETING'|'FAILED',
        'error': {
            'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --
assetModelId (string) --The ID of the asset model.

assetModelArn (string) --The ARN of the asset model, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}

assetModelName (string) --The name of the asset model.

assetModelDescription (string) --The asset model\'s description.

assetModelProperties (list) --The list of asset properties for the asset model.

(dict) --Contains information about an asset model property.

id (string) --The ID of the asset model property.

name (string) --The name of the asset model property.

dataType (string) --The data type of the asset model property.

unit (string) --The unit of the asset model property, such as Newtons or RPM .

type (dict) --The property type (see PropertyType ).

attribute (dict) --Specifies an asset attribute property. An attribute generally contains static information, such as the serial number of an IIoT wind turbine.

defaultValue (string) --The default value of the asset model property attribute. All assets that you create from the asset model contain this attribute value. You can update an attribute\'s value after you create an asset. For more information, see Updating Attribute Values in the AWS IoT SiteWise User Guide .



measurement (dict) --Specifies an asset measurement property. A measurement represents a device\'s raw sensor data stream, such as timestamped temperature values or timestamped power values.

transform (dict) --Specifies an asset transform property. A transform contains a mathematical expression that maps a property\'s data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.

expression (string) --The mathematical expression that defines the transformation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.
For more information, see Quotas in the AWS IoT SiteWise User Guide .

variables (list) --The list of variables used in the expression.

(dict) --Contains expression variable information.

name (string) --The friendly name of the variable to be used in the expression.

value (dict) --The variable that identifies an asset property from which to use values.

propertyId (string) --The ID of the property to use as the variable. You can use the property name if it\'s from the same asset model.

hierarchyId (string) --The ID of the hierarchy to query for the property ID. You can use the hierarchy\'s name instead of the hierarchy\'s ID.
You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same propertyId . For example, you might have separately grouped assets that come from the same asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .









metric (dict) --Specifies an asset metric property. A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.

expression (string) --The mathematical expression that defines the metric aggregation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.
For more information, see Quotas in the AWS IoT SiteWise User Guide .

variables (list) --The list of variables used in the expression.

(dict) --Contains expression variable information.

name (string) --The friendly name of the variable to be used in the expression.

value (dict) --The variable that identifies an asset property from which to use values.

propertyId (string) --The ID of the property to use as the variable. You can use the property name if it\'s from the same asset model.

hierarchyId (string) --The ID of the hierarchy to query for the property ID. You can use the hierarchy\'s name instead of the hierarchy\'s ID.
You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same propertyId . For example, you might have separately grouped assets that come from the same asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .







window (dict) --The window (time interval) over which AWS IoT SiteWise computes the metric\'s aggregation expression. AWS IoT SiteWise computes one data point per window .

tumbling (dict) --The tumbling time interval window.

interval (string) --The time interval for the tumbling window. Note that w represents weeks, d represents days, h represents hours, and m represents minutes. AWS IoT SiteWise computes the 1w interval the end of Sunday at midnight each week (UTC), the 1d interval at the end of each day at midnight (UTC), the 1h interval at the end of each hour, and so on.
When AWS IoT SiteWise aggregates data points for metric computations, the start of each interval is exclusive and the end of each interval is inclusive. AWS IoT SiteWise places the computed data point at the end of the interval.













assetModelHierarchies (list) --A list of asset model hierarchies that each contain a childAssetModelId and a hierarchyId (named id ). A hierarchy specifies allowed parent/child asset relationships for an asset model.

(dict) --Describes an asset hierarchy that contains a hierarchy\'s name, ID, and child asset model ID that specifies the type of asset that can be in this hierarchy.

id (string) --The ID of the asset model hierarchy. This ID is a hierarchyId .

name (string) --The name of the asset model hierarchy that you specify by using the CreateAssetModel or UpdateAssetModel API.

childAssetModelId (string) --The ID of the asset model. All assets in this hierarchy must be instances of the childAssetModelId asset model.





assetModelCreationDate (datetime) --The date the asset model was created, in Unix epoch time.

assetModelLastUpdateDate (datetime) --The date the asset model was last updated, in Unix epoch time.

assetModelStatus (dict) --The current status of the asset model, which contains a state and any error message.

state (string) --The current state of the asset model.

error (dict) --Contains associated error information, if any.

code (string) --The error code.

message (string) --The error message.










Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'assetModelId': 'string',
        'assetModelArn': 'string',
        'assetModelName': 'string',
        'assetModelDescription': 'string',
        'assetModelProperties': [
            {
                'id': 'string',
                'name': 'string',
                'dataType': 'STRING'|'INTEGER'|'DOUBLE'|'BOOLEAN',
                'unit': 'string',
                'type': {
                    'attribute': {
                        'defaultValue': 'string'
                    },
                    'measurement': {},
                    'transform': {
                        'expression': 'string',
                        'variables': [
                            {
                                'name': 'string',
                                'value': {
                                    'propertyId': 'string',
                                    'hierarchyId': 'string'
                                }
                            },
                        ]
                    },
                    'metric': {
                        'expression': 'string',
                        'variables': [
                            {
                                'name': 'string',
                                'value': {
                                    'propertyId': 'string',
                                    'hierarchyId': 'string'
                                }
                            },
                        ],
                        'window': {
                            'tumbling': {
                                'interval': 'string'
                            }
                        }
                    }
                }
            },
        ],
        'assetModelHierarchies': [
            {
                'id': 'string',
                'name': 'string',
                'childAssetModelId': 'string'
            },
        ],
        'assetModelCreationDate': datetime(2015, 1, 1),
        'assetModelLastUpdateDate': datetime(2015, 1, 1),
        'assetModelStatus': {
            'state': 'CREATING'|'ACTIVE'|'UPDATING'|'PROPAGATING'|'DELETING'|'FAILED',
            'error': {
                'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                'message': 'string'
            }
        }
    }
    
    
    """
    pass

def describe_asset_property(assetId=None, propertyId=None):
    """
    Retrieves information about an asset\'s property.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_asset_property(
        assetId='string',
        propertyId='string'
    )
    
    
    :type assetId: string
    :param assetId: [REQUIRED]\nThe ID of the asset.\n

    :type propertyId: string
    :param propertyId: [REQUIRED]\nThe ID of the asset property.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'assetId': 'string',
    'assetName': 'string',
    'assetModelId': 'string',
    'assetProperty': {
        'id': 'string',
        'name': 'string',
        'alias': 'string',
        'notification': {
            'topic': 'string',
            'state': 'ENABLED'|'DISABLED'
        },
        'dataType': 'STRING'|'INTEGER'|'DOUBLE'|'BOOLEAN',
        'unit': 'string',
        'type': {
            'attribute': {
                'defaultValue': 'string'
            },
            'measurement': {},
            'transform': {
                'expression': 'string',
                'variables': [
                    {
                        'name': 'string',
                        'value': {
                            'propertyId': 'string',
                            'hierarchyId': 'string'
                        }
                    },
                ]
            },
            'metric': {
                'expression': 'string',
                'variables': [
                    {
                        'name': 'string',
                        'value': {
                            'propertyId': 'string',
                            'hierarchyId': 'string'
                        }
                    },
                ],
                'window': {
                    'tumbling': {
                        'interval': 'string'
                    }
                }
            }
        }
    }
}


Response Structure

(dict) --

assetId (string) --
The ID of the asset.

assetName (string) --
The name of the asset.

assetModelId (string) --
The ID of the asset model.

assetProperty (dict) --
The asset property\'s definition, alias, and notification state.

id (string) --
The ID of the asset property.

name (string) --
The name of the property.

alias (string) --
The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping Industrial Data Streams to Asset Properties in the AWS IoT SiteWise User Guide .

notification (dict) --
The asset property\'s notification topic and state. For more information, see UpdateAssetProperty

topic (string) --
The MQTT topic to which AWS IoT SiteWise publishes property value update notifications.

state (string) --
The current notification state.



dataType (string) --
The property data type.

unit (string) --
The unit (such as Newtons or RPM ) of the asset property.

type (dict) --
The property type (see PropertyType ). A property contains one type.

attribute (dict) --
Specifies an asset attribute property. An attribute generally contains static information, such as the serial number of an IIoT wind turbine.

defaultValue (string) --
The default value of the asset model property attribute. All assets that you create from the asset model contain this attribute value. You can update an attribute\'s value after you create an asset. For more information, see Updating Attribute Values in the AWS IoT SiteWise User Guide .



measurement (dict) --
Specifies an asset measurement property. A measurement represents a device\'s raw sensor data stream, such as timestamped temperature values or timestamped power values.

transform (dict) --
Specifies an asset transform property. A transform contains a mathematical expression that maps a property\'s data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.

expression (string) --
The mathematical expression that defines the transformation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.
For more information, see Quotas in the AWS IoT SiteWise User Guide .

variables (list) --
The list of variables used in the expression.

(dict) --
Contains expression variable information.

name (string) --
The friendly name of the variable to be used in the expression.

value (dict) --
The variable that identifies an asset property from which to use values.

propertyId (string) --
The ID of the property to use as the variable. You can use the property name if it\'s from the same asset model.

hierarchyId (string) --
The ID of the hierarchy to query for the property ID. You can use the hierarchy\'s name instead of the hierarchy\'s ID.
You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same propertyId . For example, you might have separately grouped assets that come from the same asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .









metric (dict) --
Specifies an asset metric property. A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.

expression (string) --
The mathematical expression that defines the metric aggregation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.
For more information, see Quotas in the AWS IoT SiteWise User Guide .

variables (list) --
The list of variables used in the expression.

(dict) --
Contains expression variable information.

name (string) --
The friendly name of the variable to be used in the expression.

value (dict) --
The variable that identifies an asset property from which to use values.

propertyId (string) --
The ID of the property to use as the variable. You can use the property name if it\'s from the same asset model.

hierarchyId (string) --
The ID of the hierarchy to query for the property ID. You can use the hierarchy\'s name instead of the hierarchy\'s ID.
You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same propertyId . For example, you might have separately grouped assets that come from the same asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .







window (dict) --
The window (time interval) over which AWS IoT SiteWise computes the metric\'s aggregation expression. AWS IoT SiteWise computes one data point per window .

tumbling (dict) --
The tumbling time interval window.

interval (string) --
The time interval for the tumbling window. Note that w represents weeks, d represents days, h represents hours, and m represents minutes. AWS IoT SiteWise computes the 1w interval the end of Sunday at midnight each week (UTC), the 1d interval at the end of each day at midnight (UTC), the 1h interval at the end of each hour, and so on.
When AWS IoT SiteWise aggregates data points for metric computations, the start of each interval is exclusive and the end of each interval is inclusive. AWS IoT SiteWise places the computed data point at the end of the interval.

















Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'assetId': 'string',
        'assetName': 'string',
        'assetModelId': 'string',
        'assetProperty': {
            'id': 'string',
            'name': 'string',
            'alias': 'string',
            'notification': {
                'topic': 'string',
                'state': 'ENABLED'|'DISABLED'
            },
            'dataType': 'STRING'|'INTEGER'|'DOUBLE'|'BOOLEAN',
            'unit': 'string',
            'type': {
                'attribute': {
                    'defaultValue': 'string'
                },
                'measurement': {},
                'transform': {
                    'expression': 'string',
                    'variables': [
                        {
                            'name': 'string',
                            'value': {
                                'propertyId': 'string',
                                'hierarchyId': 'string'
                            }
                        },
                    ]
                },
                'metric': {
                    'expression': 'string',
                    'variables': [
                        {
                            'name': 'string',
                            'value': {
                                'propertyId': 'string',
                                'hierarchyId': 'string'
                            }
                        },
                    ],
                    'window': {
                        'tumbling': {
                            'interval': 'string'
                        }
                    }
                }
            }
        }
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    
    """
    pass

def describe_dashboard(dashboardId=None):
    """
    Retrieves information about a dashboard.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_dashboard(
        dashboardId='string'
    )
    
    
    :type dashboardId: string
    :param dashboardId: [REQUIRED]\nThe ID of the dashboard.\n

    :rtype: dict
ReturnsResponse Syntax{
    'dashboardId': 'string',
    'dashboardArn': 'string',
    'dashboardName': 'string',
    'projectId': 'string',
    'dashboardDescription': 'string',
    'dashboardDefinition': 'string',
    'dashboardCreationDate': datetime(2015, 1, 1),
    'dashboardLastUpdateDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
dashboardId (string) --The ID of the dashboard.

dashboardArn (string) --The ARN of the dashboard, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:dashboard/${DashboardId}

dashboardName (string) --The name of the dashboard.

projectId (string) --The ID of the project that the dashboard is in.

dashboardDescription (string) --The dashboard\'s description.

dashboardDefinition (string) --The dashboard\'s definition JSON literal. For detailed information, see Creating Dashboards (CLI) in the AWS IoT SiteWise User Guide .

dashboardCreationDate (datetime) --The date the dashboard was created, in Unix epoch time.

dashboardLastUpdateDate (datetime) --The date the dashboard was last updated, in Unix epoch time.






Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'dashboardId': 'string',
        'dashboardArn': 'string',
        'dashboardName': 'string',
        'projectId': 'string',
        'dashboardDescription': 'string',
        'dashboardDefinition': 'string',
        'dashboardCreationDate': datetime(2015, 1, 1),
        'dashboardLastUpdateDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_gateway(gatewayId=None):
    """
    Retrieves information about a gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_gateway(
        gatewayId='string'
    )
    
    
    :type gatewayId: string
    :param gatewayId: [REQUIRED]\nThe ID of the gateway device.\n

    :rtype: dict
ReturnsResponse Syntax{
    'gatewayId': 'string',
    'gatewayName': 'string',
    'gatewayArn': 'string',
    'gatewayPlatform': {
        'greengrass': {
            'groupArn': 'string'
        }
    },
    'gatewayCapabilitySummaries': [
        {
            'capabilityNamespace': 'string',
            'capabilitySyncStatus': 'IN_SYNC'|'OUT_OF_SYNC'|'SYNC_FAILED'
        },
    ],
    'creationDate': datetime(2015, 1, 1),
    'lastUpdateDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
gatewayId (string) --The ID of the gateway device.

gatewayName (string) --The name of the gateway.

gatewayArn (string) --The ARN of the gateway, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:gateway/${GatewayId}

gatewayPlatform (dict) --The gateway\'s platform.

greengrass (dict) --A gateway that runs on AWS IoT Greengrass.

groupArn (string) --The ARN of the Greengrass group. For more information about how to find a group\'s ARN, see ListGroups and GetGroup in the AWS IoT Greengrass API Reference .





gatewayCapabilitySummaries (list) --A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration\'s definition, use DescribeGatewayCapabilityConfiguration .

(dict) --Contains a summary of a gateway capability configuration.

capabilityNamespace (string) --The namespace of the capability configuration. For example, if you configure OPC-UA sources from the AWS IoT SiteWise console, your OPC-UA capability configuration has the namespace iotsitewise:opcuacollector:version , where version is a number such as 1 .

capabilitySyncStatus (string) --The synchronization status of the capability configuration. The sync status can be one of the following:

IN_SYNC \xe2\x80\x93 The gateway is running the capability configuration.
OUT_OF_SYNC \xe2\x80\x93 The gateway hasn\'t received the capability configuration.
SYNC_FAILED \xe2\x80\x93 The gateway rejected the capability configuration.






creationDate (datetime) --The date the gateway was created, in Unix epoch time.

lastUpdateDate (datetime) --The date the gateway was last updated, in Unix epoch time.






Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'gatewayId': 'string',
        'gatewayName': 'string',
        'gatewayArn': 'string',
        'gatewayPlatform': {
            'greengrass': {
                'groupArn': 'string'
            }
        },
        'gatewayCapabilitySummaries': [
            {
                'capabilityNamespace': 'string',
                'capabilitySyncStatus': 'IN_SYNC'|'OUT_OF_SYNC'|'SYNC_FAILED'
            },
        ],
        'creationDate': datetime(2015, 1, 1),
        'lastUpdateDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    
    """
    pass

def describe_gateway_capability_configuration(gatewayId=None, capabilityNamespace=None):
    """
    Retrieves information about a gateway capability configuration. Each gateway capability defines data sources for a gateway. A capability configuration can contain multiple data source configurations. If you define OPC-UA sources for a gateway in the AWS IoT SiteWise console, all of your OPC-UA sources are stored in one capability configuration. To list all capability configurations for a gateway, use DescribeGateway .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_gateway_capability_configuration(
        gatewayId='string',
        capabilityNamespace='string'
    )
    
    
    :type gatewayId: string
    :param gatewayId: [REQUIRED]\nThe ID of the gateway that defines the capability configuration.\n

    :type capabilityNamespace: string
    :param capabilityNamespace: [REQUIRED]\nThe namespace of the capability configuration. For example, if you configure OPC-UA sources from the AWS IoT SiteWise console, your OPC-UA capability configuration has the namespace iotsitewise:opcuacollector:version , where version is a number such as 1 .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'gatewayId': 'string',
    'capabilityNamespace': 'string',
    'capabilityConfiguration': 'string',
    'capabilitySyncStatus': 'IN_SYNC'|'OUT_OF_SYNC'|'SYNC_FAILED'
}


Response Structure

(dict) --

gatewayId (string) --
The ID of the gateway that defines the capability configuration.

capabilityNamespace (string) --
The namespace of the gateway capability.

capabilityConfiguration (string) --
The JSON document that defines the gateway capability\'s configuration. For more information, see Configuring data sources (CLI) in the AWS IoT SiteWise User Guide .

capabilitySyncStatus (string) --
The synchronization status of the capability configuration. The sync status can be one of the following:

IN_SYNC \xe2\x80\x93 The gateway is running the capability configuration.
OUT_OF_SYNC \xe2\x80\x93 The gateway hasn\'t received the capability configuration.
SYNC_FAILED \xe2\x80\x93 The gateway rejected the capability configuration.








Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'gatewayId': 'string',
        'capabilityNamespace': 'string',
        'capabilityConfiguration': 'string',
        'capabilitySyncStatus': 'IN_SYNC'|'OUT_OF_SYNC'|'SYNC_FAILED'
    }
    
    
    :returns: 
    IN_SYNC \xe2\x80\x93 The gateway is running the capability configuration.
    OUT_OF_SYNC \xe2\x80\x93 The gateway hasn\'t received the capability configuration.
    SYNC_FAILED \xe2\x80\x93 The gateway rejected the capability configuration.
    
    """
    pass

def describe_logging_options():
    """
    Retrieves the current AWS IoT SiteWise logging options.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_logging_options()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'loggingOptions': {
        'level': 'ERROR'|'INFO'|'OFF'
    }
}


Response Structure

(dict) --
loggingOptions (dict) --The current logging options.

level (string) --The AWS IoT SiteWise logging verbosity level.








Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ResourceNotFoundException


    :return: {
        'loggingOptions': {
            'level': 'ERROR'|'INFO'|'OFF'
        }
    }
    
    
    """
    pass

def describe_portal(portalId=None):
    """
    Retrieves information about a portal.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_portal(
        portalId='string'
    )
    
    
    :type portalId: string
    :param portalId: [REQUIRED]\nThe ID of the portal.\n

    :rtype: dict
ReturnsResponse Syntax{
    'portalId': 'string',
    'portalArn': 'string',
    'portalName': 'string',
    'portalDescription': 'string',
    'portalClientId': 'string',
    'portalStartUrl': 'string',
    'portalContactEmail': 'string',
    'portalStatus': {
        'state': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'FAILED',
        'error': {
            'code': 'INTERNAL_FAILURE',
            'message': 'string'
        }
    },
    'portalCreationDate': datetime(2015, 1, 1),
    'portalLastUpdateDate': datetime(2015, 1, 1),
    'portalLogoImageLocation': {
        'id': 'string',
        'url': 'string'
    },
    'roleArn': 'string'
}


Response Structure

(dict) --
portalId (string) --The ID of the portal.

portalArn (string) --The ARN of the portal, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:portal/${PortalId}

portalName (string) --The name of the portal.

portalDescription (string) --The portal\'s description.

portalClientId (string) --The AWS SSO application generated client ID (used with AWS SSO APIs).

portalStartUrl (string) --The public root URL for the AWS IoT AWS IoT SiteWise Monitor application portal.

portalContactEmail (string) --The AWS administrator\'s contact email address.

portalStatus (dict) --The current status of the portal, which contains a state and any error message.

state (string) --The current state of the portal.

error (dict) --Contains associated error information, if any.

code (string) --The error code.

message (string) --The error message.





portalCreationDate (datetime) --The date the portal was created, in Unix epoch time.

portalLastUpdateDate (datetime) --The date the portal was last updated, in Unix epoch time.

portalLogoImageLocation (dict) --The portal\'s logo image, which is available at a URL.

id (string) --The ID of the image.

url (string) --The URL where the image is available. The URL is valid for 15 minutes so that you can view and download the image



roleArn (string) --The ARN of the service role that allows the portal\'s users to access your AWS IoT SiteWise resources on your behalf. For more information, see Using service roles for AWS IoT SiteWise Monitor in the AWS IoT SiteWise User Guide .






Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'portalId': 'string',
        'portalArn': 'string',
        'portalName': 'string',
        'portalDescription': 'string',
        'portalClientId': 'string',
        'portalStartUrl': 'string',
        'portalContactEmail': 'string',
        'portalStatus': {
            'state': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'FAILED',
            'error': {
                'code': 'INTERNAL_FAILURE',
                'message': 'string'
            }
        },
        'portalCreationDate': datetime(2015, 1, 1),
        'portalLastUpdateDate': datetime(2015, 1, 1),
        'portalLogoImageLocation': {
            'id': 'string',
            'url': 'string'
        },
        'roleArn': 'string'
    }
    
    
    """
    pass

def describe_project(projectId=None):
    """
    Retrieves information about a project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_project(
        projectId='string'
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project.\n

    :rtype: dict
ReturnsResponse Syntax{
    'projectId': 'string',
    'projectArn': 'string',
    'projectName': 'string',
    'portalId': 'string',
    'projectDescription': 'string',
    'projectCreationDate': datetime(2015, 1, 1),
    'projectLastUpdateDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
projectId (string) --The ID of the project.

projectArn (string) --The ARN of the project, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:project/${ProjectId}

projectName (string) --The name of the project.

portalId (string) --The ID of the portal that the project is in.

projectDescription (string) --The project\'s description.

projectCreationDate (datetime) --The date the project was created, in Unix epoch time.

projectLastUpdateDate (datetime) --The date the project was last updated, in Unix epoch time.






Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'projectId': 'string',
        'projectArn': 'string',
        'projectName': 'string',
        'portalId': 'string',
        'projectDescription': 'string',
        'projectCreationDate': datetime(2015, 1, 1),
        'projectLastUpdateDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def disassociate_assets(assetId=None, hierarchyId=None, childAssetId=None, clientToken=None):
    """
    Disassociates a child asset from the given parent asset through a hierarchy defined in the parent asset\'s model.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_assets(
        assetId='string',
        hierarchyId='string',
        childAssetId='string',
        clientToken='string'
    )
    
    
    :type assetId: string
    :param assetId: [REQUIRED]\nThe ID of the parent asset from which to disassociate the child asset.\n

    :type hierarchyId: string
    :param hierarchyId: [REQUIRED]\nThe ID of a hierarchy in the parent asset\'s model. Hierarchies allow different groupings of assets to be formed that all come from the same asset model. You can use the hierarchy ID to identify the correct asset to disassociate. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .\n

    :type childAssetId: string
    :param childAssetId: [REQUIRED]\nThe ID of the child asset to disassociate.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
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

def get_asset_property_aggregates(assetId=None, propertyId=None, propertyAlias=None, aggregateTypes=None, resolution=None, qualities=None, startDate=None, endDate=None, timeOrdering=None, nextToken=None, maxResults=None):
    """
    Gets aggregated values for an asset property. For more information, see Querying Aggregated Property Values in the AWS IoT SiteWise User Guide .
    To identify an asset property, you must specify one of the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_asset_property_aggregates(
        assetId='string',
        propertyId='string',
        propertyAlias='string',
        aggregateTypes=[
            'AVERAGE'|'COUNT'|'MAXIMUM'|'MINIMUM'|'SUM'|'STANDARD_DEVIATION',
        ],
        resolution='string',
        qualities=[
            'GOOD'|'BAD'|'UNCERTAIN',
        ],
        startDate=datetime(2015, 1, 1),
        endDate=datetime(2015, 1, 1),
        timeOrdering='ASCENDING'|'DESCENDING',
        nextToken='string',
        maxResults=123
    )
    
    
    :type assetId: string
    :param assetId: The ID of the asset.

    :type propertyId: string
    :param propertyId: The ID of the asset property.

    :type propertyAlias: string
    :param propertyAlias: The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping Industrial Data Streams to Asset Properties in the AWS IoT SiteWise User Guide .

    :type aggregateTypes: list
    :param aggregateTypes: [REQUIRED]\nThe data aggregating function.\n\n(string) --\n\n

    :type resolution: string
    :param resolution: [REQUIRED]\nThe time interval over which to aggregate data.\n

    :type qualities: list
    :param qualities: The quality by which to filter asset data.\n\n(string) --\n\n

    :type startDate: datetime
    :param startDate: [REQUIRED]\nThe exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.\n

    :type endDate: datetime
    :param endDate: [REQUIRED]\nThe inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.\n

    :type timeOrdering: string
    :param timeOrdering: The chronological sorting order of the requested information.

    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :rtype: dict

ReturnsResponse Syntax
{
    'aggregatedValues': [
        {
            'timestamp': datetime(2015, 1, 1),
            'quality': 'GOOD'|'BAD'|'UNCERTAIN',
            'value': {
                'average': 123.0,
                'count': 123.0,
                'maximum': 123.0,
                'minimum': 123.0,
                'sum': 123.0,
                'standardDeviation': 123.0
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

aggregatedValues (list) --
The requested aggregated values.

(dict) --
Contains aggregated asset property values (for example, average, minimum, and maximum).

timestamp (datetime) --
The date the aggregating computations occurred, in Unix epoch time.

quality (string) --
The quality of the aggregated data.

value (dict) --
The value of the aggregates.

average (float) --
The average (mean) value of the time series over a time interval window.

count (float) --
The count of data points in the time series over a time interval window.

maximum (float) --
The maximum value of the time series over a time interval window.

minimum (float) --
The minimum value of the time series over a time interval window.

sum (float) --
The sum of the time series over a time interval window.

standardDeviation (float) --
The standard deviation of the time series over a time interval window.







nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ServiceUnavailableException


    :return: {
        'aggregatedValues': [
            {
                'timestamp': datetime(2015, 1, 1),
                'quality': 'GOOD'|'BAD'|'UNCERTAIN',
                'value': {
                    'average': 123.0,
                    'count': 123.0,
                    'maximum': 123.0,
                    'minimum': 123.0,
                    'sum': 123.0,
                    'standardDeviation': 123.0
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    assetId (string) -- The ID of the asset.
    propertyId (string) -- The ID of the asset property.
    propertyAlias (string) -- The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping Industrial Data Streams to Asset Properties in the AWS IoT SiteWise User Guide .
    aggregateTypes (list) -- [REQUIRED]
    The data aggregating function.
    
    (string) --
    
    
    resolution (string) -- [REQUIRED]
    The time interval over which to aggregate data.
    
    qualities (list) -- The quality by which to filter asset data.
    
    (string) --
    
    
    startDate (datetime) -- [REQUIRED]
    The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
    
    endDate (datetime) -- [REQUIRED]
    The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
    
    timeOrdering (string) -- The chronological sorting order of the requested information.
    nextToken (string) -- The token to be used for the next set of paginated results.
    maxResults (integer) -- The maximum number of results to be returned per paginated request.
    
    """
    pass

def get_asset_property_value(assetId=None, propertyId=None, propertyAlias=None):
    """
    Gets an asset property\'s current value. For more information, see Querying Current Property Values in the AWS IoT SiteWise User Guide .
    To identify an asset property, you must specify one of the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_asset_property_value(
        assetId='string',
        propertyId='string',
        propertyAlias='string'
    )
    
    
    :type assetId: string
    :param assetId: The ID of the asset.

    :type propertyId: string
    :param propertyId: The ID of the asset property.

    :type propertyAlias: string
    :param propertyAlias: The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping Industrial Data Streams to Asset Properties in the AWS IoT SiteWise User Guide .

    :rtype: dict

ReturnsResponse Syntax
{
    'propertyValue': {
        'value': {
            'stringValue': 'string',
            'integerValue': 123,
            'doubleValue': 123.0,
            'booleanValue': True|False
        },
        'timestamp': {
            'timeInSeconds': 123,
            'offsetInNanos': 123
        },
        'quality': 'GOOD'|'BAD'|'UNCERTAIN'
    }
}


Response Structure

(dict) --

propertyValue (dict) --
The current asset property value.

value (dict) --
The value of the asset property (see Variant ).

stringValue (string) --
Asset property data of type string (sequence of characters).

integerValue (integer) --
Asset property data of type integer (whole number).

doubleValue (float) --
Asset property data of type double (floating point number).

booleanValue (boolean) --
Asset property data of type Boolean (true or false).



timestamp (dict) --
The timestamp of the asset property value.

timeInSeconds (integer) --
The timestamp date, in seconds, in the Unix epoch format. Fractional nanosecond data is provided by offsetInNanos .

offsetInNanos (integer) --
The nanosecond offset from timeInSeconds .



quality (string) --
The quality of the asset property value.









Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ServiceUnavailableException


    :return: {
        'propertyValue': {
            'value': {
                'stringValue': 'string',
                'integerValue': 123,
                'doubleValue': 123.0,
                'booleanValue': True|False
            },
            'timestamp': {
                'timeInSeconds': 123,
                'offsetInNanos': 123
            },
            'quality': 'GOOD'|'BAD'|'UNCERTAIN'
        }
    }
    
    
    :returns: 
    assetId (string) -- The ID of the asset.
    propertyId (string) -- The ID of the asset property.
    propertyAlias (string) -- The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping Industrial Data Streams to Asset Properties in the AWS IoT SiteWise User Guide .
    
    """
    pass

def get_asset_property_value_history(assetId=None, propertyId=None, propertyAlias=None, startDate=None, endDate=None, qualities=None, timeOrdering=None, nextToken=None, maxResults=None):
    """
    Gets the history of an asset property\'s values. For more information, see Querying Historical Property Values in the AWS IoT SiteWise User Guide .
    To identify an asset property, you must specify one of the following:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_asset_property_value_history(
        assetId='string',
        propertyId='string',
        propertyAlias='string',
        startDate=datetime(2015, 1, 1),
        endDate=datetime(2015, 1, 1),
        qualities=[
            'GOOD'|'BAD'|'UNCERTAIN',
        ],
        timeOrdering='ASCENDING'|'DESCENDING',
        nextToken='string',
        maxResults=123
    )
    
    
    :type assetId: string
    :param assetId: The ID of the asset.

    :type propertyId: string
    :param propertyId: The ID of the asset property.

    :type propertyAlias: string
    :param propertyAlias: The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping Industrial Data Streams to Asset Properties in the AWS IoT SiteWise User Guide .

    :type startDate: datetime
    :param startDate: [REQUIRED]\nThe exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.\n

    :type endDate: datetime
    :param endDate: [REQUIRED]\nThe inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.\n

    :type qualities: list
    :param qualities: The quality by which to filter asset data.\n\n(string) --\n\n

    :type timeOrdering: string
    :param timeOrdering: The chronological sorting order of the requested information.

    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :rtype: dict

ReturnsResponse Syntax
{
    'assetPropertyValueHistory': [
        {
            'value': {
                'stringValue': 'string',
                'integerValue': 123,
                'doubleValue': 123.0,
                'booleanValue': True|False
            },
            'timestamp': {
                'timeInSeconds': 123,
                'offsetInNanos': 123
            },
            'quality': 'GOOD'|'BAD'|'UNCERTAIN'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

assetPropertyValueHistory (list) --
The asset property\'s value history.

(dict) --
Contains asset property value information.

value (dict) --
The value of the asset property (see Variant ).

stringValue (string) --
Asset property data of type string (sequence of characters).

integerValue (integer) --
Asset property data of type integer (whole number).

doubleValue (float) --
Asset property data of type double (floating point number).

booleanValue (boolean) --
Asset property data of type Boolean (true or false).



timestamp (dict) --
The timestamp of the asset property value.

timeInSeconds (integer) --
The timestamp date, in seconds, in the Unix epoch format. Fractional nanosecond data is provided by offsetInNanos .

offsetInNanos (integer) --
The nanosecond offset from timeInSeconds .



quality (string) --
The quality of the asset property value.





nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ServiceUnavailableException


    :return: {
        'assetPropertyValueHistory': [
            {
                'value': {
                    'stringValue': 'string',
                    'integerValue': 123,
                    'doubleValue': 123.0,
                    'booleanValue': True|False
                },
                'timestamp': {
                    'timeInSeconds': 123,
                    'offsetInNanos': 123
                },
                'quality': 'GOOD'|'BAD'|'UNCERTAIN'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    assetId (string) -- The ID of the asset.
    propertyId (string) -- The ID of the asset property.
    propertyAlias (string) -- The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping Industrial Data Streams to Asset Properties in the AWS IoT SiteWise User Guide .
    startDate (datetime) -- [REQUIRED]
    The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
    
    endDate (datetime) -- [REQUIRED]
    The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
    
    qualities (list) -- The quality by which to filter asset data.
    
    (string) --
    
    
    timeOrdering (string) -- The chronological sorting order of the requested information.
    nextToken (string) -- The token to be used for the next set of paginated results.
    maxResults (integer) -- The maximum number of results to be returned per paginated request.
    
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

def list_access_policies(identityType=None, identityId=None, resourceType=None, resourceId=None, nextToken=None, maxResults=None):
    """
    Retrieves a paginated list of access policies for an AWS SSO identity (a user or group) or an AWS IoT SiteWise Monitor resource (a portal or project).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_access_policies(
        identityType='USER'|'GROUP',
        identityId='string',
        resourceType='PORTAL'|'PROJECT',
        resourceId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type identityType: string
    :param identityType: The type of identity (user or group). This parameter is required if you specify identityId .

    :type identityId: string
    :param identityId: The ID of the identity. This parameter is required if you specify identityType .

    :type resourceType: string
    :param resourceType: The type of resource (portal or project). This parameter is required if you specify resourceId .

    :type resourceId: string
    :param resourceId: The ID of the resource. This parameter is required if you specify resourceType .

    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :rtype: dict

ReturnsResponse Syntax
{
    'accessPolicySummaries': [
        {
            'id': 'string',
            'identity': {
                'user': {
                    'id': 'string'
                },
                'group': {
                    'id': 'string'
                }
            },
            'resource': {
                'portal': {
                    'id': 'string'
                },
                'project': {
                    'id': 'string'
                }
            },
            'permission': 'ADMINISTRATOR'|'VIEWER',
            'creationDate': datetime(2015, 1, 1),
            'lastUpdateDate': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

accessPolicySummaries (list) --
A list that summarizes each access policy.

(dict) --
Contains an access policy that defines an AWS SSO identity\'s access to an AWS IoT SiteWise Monitor resource.

id (string) --
The ID of the access policy.

identity (dict) --
The AWS SSO identity (a user or group).

user (dict) --
A user identity.

id (string) --
The AWS SSO ID of the user.



group (dict) --
A group identity.

id (string) --
The AWS SSO ID of the group.





resource (dict) --
The AWS IoT SiteWise Monitor resource (a portal or project).

portal (dict) --
A portal resource.

id (string) --
The ID of the portal.



project (dict) --
A project resource.

id (string) --
The ID of the project.





permission (string) --
The permissions for the access policy. Note that a project ADMINISTRATOR is also known as a project owner.

creationDate (datetime) --
The date the access policy was created, in Unix epoch time.

lastUpdateDate (datetime) --
The date the access policy was last updated, in Unix epoch time.





nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'accessPolicySummaries': [
            {
                'id': 'string',
                'identity': {
                    'user': {
                        'id': 'string'
                    },
                    'group': {
                        'id': 'string'
                    }
                },
                'resource': {
                    'portal': {
                        'id': 'string'
                    },
                    'project': {
                        'id': 'string'
                    }
                },
                'permission': 'ADMINISTRATOR'|'VIEWER',
                'creationDate': datetime(2015, 1, 1),
                'lastUpdateDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    
    """
    pass

def list_asset_models(nextToken=None, maxResults=None):
    """
    Retrieves a paginated list of summaries of all asset models.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_asset_models(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :rtype: dict

ReturnsResponse Syntax
{
    'assetModelSummaries': [
        {
            'id': 'string',
            'arn': 'string',
            'name': 'string',
            'description': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastUpdateDate': datetime(2015, 1, 1),
            'status': {
                'state': 'CREATING'|'ACTIVE'|'UPDATING'|'PROPAGATING'|'DELETING'|'FAILED',
                'error': {
                    'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                    'message': 'string'
                }
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

assetModelSummaries (list) --
A list that summarizes each asset model.

(dict) --
Contains a summary of an asset model.

id (string) --
The ID of the asset model (used with AWS IoT SiteWise APIs).

arn (string) --
The ARN of the asset model, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}


name (string) --
The name of the asset model.

description (string) --
The asset model description.

creationDate (datetime) --
The date the asset model was created, in Unix epoch time.

lastUpdateDate (datetime) --
The date the asset model was last updated, in Unix epoch time.

status (dict) --
The current status of the asset model.

state (string) --
The current state of the asset model.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.









nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'assetModelSummaries': [
            {
                'id': 'string',
                'arn': 'string',
                'name': 'string',
                'description': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastUpdateDate': datetime(2015, 1, 1),
                'status': {
                    'state': 'CREATING'|'ACTIVE'|'UPDATING'|'PROPAGATING'|'DELETING'|'FAILED',
                    'error': {
                        'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                        'message': 'string'
                    }
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    
    """
    pass

def list_assets(nextToken=None, maxResults=None, assetModelId=None, filter=None):
    """
    Retrieves a paginated list of asset summaries.
    You can use this operation to do the following:
    You can\'t use this operation to list all assets. To retrieve summaries for all of your assets, use ListAssetModels to get all of your asset model IDs. Then, use ListAssets to get all assets for each asset model.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_assets(
        nextToken='string',
        maxResults=123,
        assetModelId='string',
        filter='ALL'|'TOP_LEVEL'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :type assetModelId: string
    :param assetModelId: The ID of the asset model by which to filter the list of assets. This parameter is required if you choose ALL for filter .

    :type filter: string
    :param filter: The filter for the requested list of assets. Choose one of the following options. Defaults to ALL .\n\nALL \xe2\x80\x93 The list includes all assets for a given asset model ID. The assetModelId parameter is required if you filter by ALL .\nTOP_LEVEL \xe2\x80\x93 The list includes only top-level assets in the asset hierarchy tree.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'assetSummaries': [
        {
            'id': 'string',
            'arn': 'string',
            'name': 'string',
            'assetModelId': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastUpdateDate': datetime(2015, 1, 1),
            'status': {
                'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
                'error': {
                    'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                    'message': 'string'
                }
            },
            'hierarchies': [
                {
                    'id': 'string',
                    'name': 'string'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

assetSummaries (list) --
A list that summarizes each asset.

(dict) --
Contains a summary of an asset.

id (string) --
The ID of the asset.

arn (string) --
The ARN of the asset, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}


name (string) --
The name of the asset.

assetModelId (string) --
The ID of the asset model used to create this asset.

creationDate (datetime) --
The date the asset was created, in Unix epoch time.

lastUpdateDate (datetime) --
The date the asset was last updated, in Unix epoch time.

status (dict) --
The current status of the asset.

state (string) --
The current status of the asset.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.





hierarchies (list) --
A list of asset hierarchies that each contain a hierarchyId . A hierarchy specifies allowed parent/child asset relationships.

(dict) --
Describes an asset hierarchy that contains a hierarchy\'s name and ID.

id (string) --
The ID of the hierarchy. This ID is a hierarchyId .

name (string) --
The hierarchy name provided in the CreateAssetModel or UpdateAssetModel API.









nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'assetSummaries': [
            {
                'id': 'string',
                'arn': 'string',
                'name': 'string',
                'assetModelId': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastUpdateDate': datetime(2015, 1, 1),
                'status': {
                    'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
                    'error': {
                        'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                        'message': 'string'
                    }
                },
                'hierarchies': [
                    {
                        'id': 'string',
                        'name': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    nextToken (string) -- The token to be used for the next set of paginated results.
    maxResults (integer) -- The maximum number of results to be returned per paginated request.
    assetModelId (string) -- The ID of the asset model by which to filter the list of assets. This parameter is required if you choose ALL for filter .
    filter (string) -- The filter for the requested list of assets. Choose one of the following options. Defaults to ALL .
    
    ALL \xe2\x80\x93 The list includes all assets for a given asset model ID. The assetModelId parameter is required if you filter by ALL .
    TOP_LEVEL \xe2\x80\x93 The list includes only top-level assets in the asset hierarchy tree.
    
    
    
    """
    pass

def list_associated_assets(assetId=None, hierarchyId=None, nextToken=None, maxResults=None):
    """
    Retrieves a paginated list of the assets associated to a parent asset (assetId ) by a given hierarchy (hierarchyId ).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_associated_assets(
        assetId='string',
        hierarchyId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type assetId: string
    :param assetId: [REQUIRED]\nThe ID of the parent asset.\n

    :type hierarchyId: string
    :param hierarchyId: [REQUIRED]\nThe hierarchy ID (of the parent asset model) whose associated assets are returned. To find a hierarchy ID, use the DescribeAsset or DescribeAssetModel actions.\nFor more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .\n

    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :rtype: dict

ReturnsResponse Syntax
{
    'assetSummaries': [
        {
            'id': 'string',
            'arn': 'string',
            'name': 'string',
            'assetModelId': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastUpdateDate': datetime(2015, 1, 1),
            'status': {
                'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
                'error': {
                    'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                    'message': 'string'
                }
            },
            'hierarchies': [
                {
                    'id': 'string',
                    'name': 'string'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

assetSummaries (list) --
A list that summarizes the associated assets.

(dict) --
Contains a summary of an associated asset.

id (string) --
The ID of the asset.

arn (string) --
The ARN of the asset, which has the following format.

arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}


name (string) --
The name of the asset.

assetModelId (string) --
The ID of the asset model used to create the asset.

creationDate (datetime) --
The date the asset was created, in Unix epoch time.

lastUpdateDate (datetime) --
The date the asset was last updated, in Unix epoch time.

status (dict) --
The current status of the asset.

state (string) --
The current status of the asset.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.





hierarchies (list) --
A list of asset hierarchies that each contain a hierarchyId . A hierarchy specifies allowed parent/child asset relationships.

(dict) --
Describes an asset hierarchy that contains a hierarchy\'s name and ID.

id (string) --
The ID of the hierarchy. This ID is a hierarchyId .

name (string) --
The hierarchy name provided in the CreateAssetModel or UpdateAssetModel API.









nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'assetSummaries': [
            {
                'id': 'string',
                'arn': 'string',
                'name': 'string',
                'assetModelId': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastUpdateDate': datetime(2015, 1, 1),
                'status': {
                    'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
                    'error': {
                        'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                        'message': 'string'
                    }
                },
                'hierarchies': [
                    {
                        'id': 'string',
                        'name': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.ThrottlingException
    
    """
    pass

def list_dashboards(projectId=None, nextToken=None, maxResults=None):
    """
    Retrieves a paginated list of dashboards for an AWS IoT SiteWise Monitor project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_dashboards(
        projectId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project.\n

    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :rtype: dict

ReturnsResponse Syntax
{
    'dashboardSummaries': [
        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastUpdateDate': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

dashboardSummaries (list) --
A list that summarizes each dashboard in the project.

(dict) --
Contains a dashboard summary.

id (string) --
The ID of the dashboard.

name (string) --
The name of the dashboard

description (string) --
The dashboard\'s description.

creationDate (datetime) --
The date the dashboard was created, in Unix epoch time.

lastUpdateDate (datetime) --
The date the dashboard was last updated, in Unix epoch time.





nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'dashboardSummaries': [
            {
                'id': 'string',
                'name': 'string',
                'description': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastUpdateDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    
    """
    pass

def list_gateways(nextToken=None, maxResults=None):
    """
    Retrieves a paginated list of gateways.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_gateways(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :rtype: dict

ReturnsResponse Syntax
{
    'gatewaySummaries': [
        {
            'gatewayId': 'string',
            'gatewayName': 'string',
            'gatewayCapabilitySummaries': [
                {
                    'capabilityNamespace': 'string',
                    'capabilitySyncStatus': 'IN_SYNC'|'OUT_OF_SYNC'|'SYNC_FAILED'
                },
            ],
            'creationDate': datetime(2015, 1, 1),
            'lastUpdateDate': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

gatewaySummaries (list) --
A list that summarizes each gateway.

(dict) --
Contains a summary of a gateway.

gatewayId (string) --
The ID of the gateway device.

gatewayName (string) --
The name of the asset.

gatewayCapabilitySummaries (list) --
A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration\'s definition, use DescribeGatewayCapabilityConfiguration .

(dict) --
Contains a summary of a gateway capability configuration.

capabilityNamespace (string) --
The namespace of the capability configuration. For example, if you configure OPC-UA sources from the AWS IoT SiteWise console, your OPC-UA capability configuration has the namespace iotsitewise:opcuacollector:version , where version is a number such as 1 .

capabilitySyncStatus (string) --
The synchronization status of the capability configuration. The sync status can be one of the following:

IN_SYNC \xe2\x80\x93 The gateway is running the capability configuration.
OUT_OF_SYNC \xe2\x80\x93 The gateway hasn\'t received the capability configuration.
SYNC_FAILED \xe2\x80\x93 The gateway rejected the capability configuration.






creationDate (datetime) --
The date the gateway was created, in Unix epoch time.

lastUpdateDate (datetime) --
The date the gateway was last updated, in Unix epoch time.





nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'gatewaySummaries': [
            {
                'gatewayId': 'string',
                'gatewayName': 'string',
                'gatewayCapabilitySummaries': [
                    {
                        'capabilityNamespace': 'string',
                        'capabilitySyncStatus': 'IN_SYNC'|'OUT_OF_SYNC'|'SYNC_FAILED'
                    },
                ],
                'creationDate': datetime(2015, 1, 1),
                'lastUpdateDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IN_SYNC \xe2\x80\x93 The gateway is running the capability configuration.
    OUT_OF_SYNC \xe2\x80\x93 The gateway hasn\'t received the capability configuration.
    SYNC_FAILED \xe2\x80\x93 The gateway rejected the capability configuration.
    
    """
    pass

def list_portals(nextToken=None, maxResults=None):
    """
    Retrieves a paginated list of AWS IoT SiteWise Monitor portals.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_portals(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :rtype: dict

ReturnsResponse Syntax
{
    'portalSummaries': [
        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'startUrl': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastUpdateDate': datetime(2015, 1, 1),
            'roleArn': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

portalSummaries (list) --
A list that summarizes each portal.

(dict) --
Contains a portal summary.

id (string) --
The ID of the portal.

name (string) --
The name of the portal.

description (string) --
The portal\'s description.

startUrl (string) --
The public root URL for the AWS IoT AWS IoT SiteWise Monitor application portal.

creationDate (datetime) --
The date the portal was created, in Unix epoch time.

lastUpdateDate (datetime) --
The date the portal was last updated, in Unix epoch time.

roleArn (string) --
The ARN of the service role that allows the portal\'s users to access your AWS IoT SiteWise resources on your behalf. For more information, see Using service roles for AWS IoT SiteWise Monitor in the AWS IoT SiteWise User Guide .





nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'portalSummaries': [
            {
                'id': 'string',
                'name': 'string',
                'description': 'string',
                'startUrl': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastUpdateDate': datetime(2015, 1, 1),
                'roleArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    
    """
    pass

def list_project_assets(projectId=None, nextToken=None, maxResults=None):
    """
    Retrieves a paginated list of assets associated with an AWS IoT SiteWise Monitor project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_project_assets(
        projectId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project.\n

    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :rtype: dict

ReturnsResponse Syntax
{
    'assetIds': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

assetIds (list) --
A list that contains the IDs of each asset associated with the project.

(string) --


nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'assetIds': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_projects(portalId=None, nextToken=None, maxResults=None):
    """
    Retrieves a paginated list of projects for an AWS IoT SiteWise Monitor portal.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_projects(
        portalId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type portalId: string
    :param portalId: [REQUIRED]\nThe ID of the portal.\n

    :type nextToken: string
    :param nextToken: The token to be used for the next set of paginated results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per paginated request.

    :rtype: dict

ReturnsResponse Syntax
{
    'projectSummaries': [
        {
            'id': 'string',
            'name': 'string',
            'description': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastUpdateDate': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

projectSummaries (list) --
A list that summarizes each project in the portal.

(dict) --
Contains project summary information.

id (string) --
The ID of the project.

name (string) --
The name of the project.

description (string) --
The project\'s description.

creationDate (datetime) --
The date the project was created, in Unix epoch time.

lastUpdateDate (datetime) --
The date the project was last updated, in Unix epoch time.





nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {
        'projectSummaries': [
            {
                'id': 'string',
                'name': 'string',
                'description': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastUpdateDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Retrieves the list of tags for an AWS IoT SiteWise resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
tags (dict) --The list of key-value pairs that contain metadata for the resource. For more information, see Tagging your AWS IoT SiteWise resources in the AWS IoT SiteWise User Guide .

(string) --
(string) --









Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ResourceNotFoundException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def put_logging_options(loggingOptions=None):
    """
    Sets logging options for AWS IoT SiteWise.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_logging_options(
        loggingOptions={
            'level': 'ERROR'|'INFO'|'OFF'
        }
    )
    
    
    :type loggingOptions: dict
    :param loggingOptions: [REQUIRED]\nThe logging options to set.\n\nlevel (string) -- [REQUIRED]The AWS IoT SiteWise logging verbosity level.\n\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ConflictingOperationException
IoTSiteWise.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds tags to an AWS IoT SiteWise resource. If a tag already exists for the resource, this operation updates the tag\'s value.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource to tag.\n

    :type tags: dict
    :param tags: [REQUIRED]\nA list of key-value pairs that contain metadata for the resource. For more information, see Tagging your AWS IoT SiteWise resources in the AWS IoT SiteWise User Guide .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.TooManyTagsException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes a tag from an AWS IoT SiteWise resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource to untag.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nA list of keys for tags to remove from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_access_policy(accessPolicyId=None, accessPolicyIdentity=None, accessPolicyResource=None, accessPolicyPermission=None, clientToken=None):
    """
    Updates an existing access policy that specifies an AWS SSO user or group\'s access to an AWS IoT SiteWise Monitor portal or project resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_access_policy(
        accessPolicyId='string',
        accessPolicyIdentity={
            'user': {
                'id': 'string'
            },
            'group': {
                'id': 'string'
            }
        },
        accessPolicyResource={
            'portal': {
                'id': 'string'
            },
            'project': {
                'id': 'string'
            }
        },
        accessPolicyPermission='ADMINISTRATOR'|'VIEWER',
        clientToken='string'
    )
    
    
    :type accessPolicyId: string
    :param accessPolicyId: [REQUIRED]\nThe ID of the access policy.\n

    :type accessPolicyIdentity: dict
    :param accessPolicyIdentity: [REQUIRED]\nThe identity for this access policy. Choose either a user or a group but not both.\n\nuser (dict) --A user identity.\n\nid (string) -- [REQUIRED]The AWS SSO ID of the user.\n\n\n\ngroup (dict) --A group identity.\n\nid (string) -- [REQUIRED]The AWS SSO ID of the group.\n\n\n\n\n

    :type accessPolicyResource: dict
    :param accessPolicyResource: [REQUIRED]\nThe AWS IoT SiteWise Monitor resource for this access policy. Choose either portal or project but not both.\n\nportal (dict) --A portal resource.\n\nid (string) -- [REQUIRED]The ID of the portal.\n\n\n\nproject (dict) --A project resource.\n\nid (string) -- [REQUIRED]The ID of the project.\n\n\n\n\n

    :type accessPolicyPermission: string
    :param accessPolicyPermission: [REQUIRED]\nThe permission level for this access policy. Note that a project ADMINISTRATOR is also known as a project owner.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_asset(assetId=None, assetName=None, clientToken=None):
    """
    Updates an asset\'s name. For more information, see Updating Assets and Models in the AWS IoT SiteWise User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_asset(
        assetId='string',
        assetName='string',
        clientToken='string'
    )
    
    
    :type assetId: string
    :param assetId: [REQUIRED]\nThe ID of the asset to update.\n

    :type assetName: string
    :param assetName: [REQUIRED]\nA unique, friendly name for the asset.\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'assetStatus': {
        'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
        'error': {
            'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --

assetStatus (dict) --
The status of the asset, which contains a state (UPDATING after successfully calling this operation) and any error message.

state (string) --
The current status of the asset.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.











Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceAlreadyExistsException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ConflictingOperationException


    :return: {
        'assetStatus': {
            'state': 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED',
            'error': {
                'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                'message': 'string'
            }
        }
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceAlreadyExistsException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def update_asset_model(assetModelId=None, assetModelName=None, assetModelDescription=None, assetModelProperties=None, assetModelHierarchies=None, clientToken=None):
    """
    Updates an asset model and all of the assets that were created from the model. Each asset created from the model inherits the updated asset model\'s property and hierarchy definitions. For more information, see Updating Assets and Models in the AWS IoT SiteWise User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_asset_model(
        assetModelId='string',
        assetModelName='string',
        assetModelDescription='string',
        assetModelProperties=[
            {
                'id': 'string',
                'name': 'string',
                'dataType': 'STRING'|'INTEGER'|'DOUBLE'|'BOOLEAN',
                'unit': 'string',
                'type': {
                    'attribute': {
                        'defaultValue': 'string'
                    },
                    'measurement': {}
                    ,
                    'transform': {
                        'expression': 'string',
                        'variables': [
                            {
                                'name': 'string',
                                'value': {
                                    'propertyId': 'string',
                                    'hierarchyId': 'string'
                                }
                            },
                        ]
                    },
                    'metric': {
                        'expression': 'string',
                        'variables': [
                            {
                                'name': 'string',
                                'value': {
                                    'propertyId': 'string',
                                    'hierarchyId': 'string'
                                }
                            },
                        ],
                        'window': {
                            'tumbling': {
                                'interval': 'string'
                            }
                        }
                    }
                }
            },
        ],
        assetModelHierarchies=[
            {
                'id': 'string',
                'name': 'string',
                'childAssetModelId': 'string'
            },
        ],
        clientToken='string'
    )
    
    
    :type assetModelId: string
    :param assetModelId: [REQUIRED]\nThe ID of the asset model to update.\n

    :type assetModelName: string
    :param assetModelName: [REQUIRED]\nA unique, friendly name for the asset model.\n

    :type assetModelDescription: string
    :param assetModelDescription: A description for the asset model.

    :type assetModelProperties: list
    :param assetModelProperties: The updated property definitions of the asset model. For more information, see Asset Properties in the AWS IoT SiteWise User Guide .\nYou can specify up to 200 properties per asset model. For more information, see Quotas in the AWS IoT SiteWise User Guide .\n\n(dict) --Contains information about an asset model property.\n\nid (string) --The ID of the asset model property.\n\nname (string) -- [REQUIRED]The name of the asset model property.\n\ndataType (string) -- [REQUIRED]The data type of the asset model property.\n\nunit (string) --The unit of the asset model property, such as Newtons or RPM .\n\ntype (dict) -- [REQUIRED]The property type (see PropertyType ).\n\nattribute (dict) --Specifies an asset attribute property. An attribute generally contains static information, such as the serial number of an IIoT wind turbine.\n\ndefaultValue (string) --The default value of the asset model property attribute. All assets that you create from the asset model contain this attribute value. You can update an attribute\'s value after you create an asset. For more information, see Updating Attribute Values in the AWS IoT SiteWise User Guide .\n\n\n\nmeasurement (dict) --Specifies an asset measurement property. A measurement represents a device\'s raw sensor data stream, such as timestamped temperature values or timestamped power values.\n\ntransform (dict) --Specifies an asset transform property. A transform contains a mathematical expression that maps a property\'s data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.\n\nexpression (string) -- [REQUIRED]The mathematical expression that defines the transformation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.\nFor more information, see Quotas in the AWS IoT SiteWise User Guide .\n\nvariables (list) -- [REQUIRED]The list of variables used in the expression.\n\n(dict) --Contains expression variable information.\n\nname (string) -- [REQUIRED]The friendly name of the variable to be used in the expression.\n\nvalue (dict) -- [REQUIRED]The variable that identifies an asset property from which to use values.\n\npropertyId (string) -- [REQUIRED]The ID of the property to use as the variable. You can use the property name if it\'s from the same asset model.\n\nhierarchyId (string) --The ID of the hierarchy to query for the property ID. You can use the hierarchy\'s name instead of the hierarchy\'s ID.\nYou use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same propertyId . For example, you might have separately grouped assets that come from the same asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .\n\n\n\n\n\n\n\n\n\nmetric (dict) --Specifies an asset metric property. A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.\n\nexpression (string) -- [REQUIRED]The mathematical expression that defines the metric aggregation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.\nFor more information, see Quotas in the AWS IoT SiteWise User Guide .\n\nvariables (list) -- [REQUIRED]The list of variables used in the expression.\n\n(dict) --Contains expression variable information.\n\nname (string) -- [REQUIRED]The friendly name of the variable to be used in the expression.\n\nvalue (dict) -- [REQUIRED]The variable that identifies an asset property from which to use values.\n\npropertyId (string) -- [REQUIRED]The ID of the property to use as the variable. You can use the property name if it\'s from the same asset model.\n\nhierarchyId (string) --The ID of the hierarchy to query for the property ID. You can use the hierarchy\'s name instead of the hierarchy\'s ID.\nYou use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same propertyId . For example, you might have separately grouped assets that come from the same asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .\n\n\n\n\n\n\n\nwindow (dict) -- [REQUIRED]The window (time interval) over which AWS IoT SiteWise computes the metric\'s aggregation expression. AWS IoT SiteWise computes one data point per window .\n\ntumbling (dict) --The tumbling time interval window.\n\ninterval (string) -- [REQUIRED]The time interval for the tumbling window. Note that w represents weeks, d represents days, h represents hours, and m represents minutes. AWS IoT SiteWise computes the 1w interval the end of Sunday at midnight each week (UTC), the 1d interval at the end of each day at midnight (UTC), the 1h interval at the end of each hour, and so on.\nWhen AWS IoT SiteWise aggregates data points for metric computations, the start of each interval is exclusive and the end of each interval is inclusive. AWS IoT SiteWise places the computed data point at the end of the interval.\n\n\n\n\n\n\n\n\n\n\n\n\n

    :type assetModelHierarchies: list
    :param assetModelHierarchies: The updated hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see Asset Hierarchies in the AWS IoT SiteWise User Guide .\nYou can specify up to 10 hierarchies per asset model. For more information, see Quotas in the AWS IoT SiteWise User Guide .\n\n(dict) --Describes an asset hierarchy that contains a hierarchy\'s name, ID, and child asset model ID that specifies the type of asset that can be in this hierarchy.\n\nid (string) --The ID of the asset model hierarchy. This ID is a hierarchyId .\n\nname (string) -- [REQUIRED]The name of the asset model hierarchy that you specify by using the CreateAssetModel or UpdateAssetModel API.\n\nchildAssetModelId (string) -- [REQUIRED]The ID of the asset model. All assets in this hierarchy must be instances of the childAssetModelId asset model.\n\n\n\n\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'assetModelStatus': {
        'state': 'CREATING'|'ACTIVE'|'UPDATING'|'PROPAGATING'|'DELETING'|'FAILED',
        'error': {
            'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --

assetModelStatus (dict) --
The status of the asset model, which contains a state (UPDATING after successfully calling this operation) and any error message.

state (string) --
The current state of the asset model.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.











Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceAlreadyExistsException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.LimitExceededException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ConflictingOperationException


    :return: {
        'assetModelStatus': {
            'state': 'CREATING'|'ACTIVE'|'UPDATING'|'PROPAGATING'|'DELETING'|'FAILED',
            'error': {
                'code': 'VALIDATION_ERROR'|'INTERNAL_FAILURE',
                'message': 'string'
            }
        }
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceAlreadyExistsException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.LimitExceededException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def update_asset_property(assetId=None, propertyId=None, propertyAlias=None, propertyNotificationState=None, clientToken=None):
    """
    Updates an asset property\'s alias and notification state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_asset_property(
        assetId='string',
        propertyId='string',
        propertyAlias='string',
        propertyNotificationState='ENABLED'|'DISABLED',
        clientToken='string'
    )
    
    
    :type assetId: string
    :param assetId: [REQUIRED]\nThe ID of the asset to be updated.\n

    :type propertyId: string
    :param propertyId: [REQUIRED]\nThe ID of the asset property to be updated.\n

    :type propertyAlias: string
    :param propertyAlias: The property alias that identifies the property, such as an OPC-UA server data stream path (for example, /company/windfarm/3/turbine/7/temperature ). For more information, see Mapping Industrial Data Streams to Asset Properties in the AWS IoT SiteWise User Guide .\nIf you omit this parameter, the alias is removed from the property.\n

    :type propertyNotificationState: string
    :param propertyNotificationState: The MQTT notification state (enabled or disabled) for this asset property. When the notification state is enabled, AWS IoT SiteWise publishes property value updates to a unique MQTT topic. For more information, see Interacting with Other Services in the AWS IoT SiteWise User Guide .\nIf you omit this parameter, the notification state is set to DISABLED .\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def update_dashboard(dashboardId=None, dashboardName=None, dashboardDescription=None, dashboardDefinition=None, clientToken=None):
    """
    Updates an AWS IoT SiteWise Monitor dashboard.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_dashboard(
        dashboardId='string',
        dashboardName='string',
        dashboardDescription='string',
        dashboardDefinition='string',
        clientToken='string'
    )
    
    
    :type dashboardId: string
    :param dashboardId: [REQUIRED]\nThe ID of the dashboard to update.\n

    :type dashboardName: string
    :param dashboardName: [REQUIRED]\nA new friendly name for the dashboard.\n

    :type dashboardDescription: string
    :param dashboardDescription: A new description for the dashboard.

    :type dashboardDefinition: string
    :param dashboardDefinition: [REQUIRED]\nThe new dashboard definition, as specified in a JSON literal. For detailed information, see Creating Dashboards (CLI) in the AWS IoT SiteWise User Guide .\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_gateway(gatewayId=None, gatewayName=None):
    """
    Updates a gateway\'s name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_gateway(
        gatewayId='string',
        gatewayName='string'
    )
    
    
    :type gatewayId: string
    :param gatewayId: [REQUIRED]\nThe ID of the gateway to update.\n

    :type gatewayName: string
    :param gatewayName: [REQUIRED]\nA unique, friendly name for the gateway.\n

    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    
    """
    pass

def update_gateway_capability_configuration(gatewayId=None, capabilityNamespace=None, capabilityConfiguration=None):
    """
    Updates a gateway capability configuration or defines a new capability configuration. Each gateway capability defines data sources for a gateway. A capability configuration can contain multiple data source configurations. If you define OPC-UA sources for a gateway in the AWS IoT SiteWise console, all of your OPC-UA sources are stored in one capability configuration. To list all capability configurations for a gateway, use DescribeGateway .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_gateway_capability_configuration(
        gatewayId='string',
        capabilityNamespace='string',
        capabilityConfiguration='string'
    )
    
    
    :type gatewayId: string
    :param gatewayId: [REQUIRED]\nThe ID of the gateway to be updated.\n

    :type capabilityNamespace: string
    :param capabilityNamespace: [REQUIRED]\nThe namespace of the gateway capability configuration to be updated. For example, if you configure OPC-UA sources from the AWS IoT SiteWise console, your OPC-UA capability configuration has the namespace iotsitewise:opcuacollector:version , where version is a number such as 1 .\n

    :type capabilityConfiguration: string
    :param capabilityConfiguration: [REQUIRED]\nThe JSON document that defines the configuration for the gateway capability. For more information, see Configuring data sources (CLI) in the AWS IoT SiteWise User Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'capabilityNamespace': 'string',
    'capabilitySyncStatus': 'IN_SYNC'|'OUT_OF_SYNC'|'SYNC_FAILED'
}


Response Structure

(dict) --

capabilityNamespace (string) --
The namespace of the gateway capability.

capabilitySyncStatus (string) --
The synchronization status of the capability configuration. The sync status can be one of the following:

IN_SYNC \xe2\x80\x93 The gateway is running the capability configuration.
OUT_OF_SYNC \xe2\x80\x93 The gateway hasn\'t received the capability configuration.
SYNC_FAILED \xe2\x80\x93 The gateway rejected the capability configuration.

After you update a capability configuration, its sync status is OUT_OF_SYNC until the gateway receives and applies or rejects the updated configuration.







Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.ConflictingOperationException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.LimitExceededException


    :return: {
        'capabilityNamespace': 'string',
        'capabilitySyncStatus': 'IN_SYNC'|'OUT_OF_SYNC'|'SYNC_FAILED'
    }
    
    
    :returns: 
    IN_SYNC \xe2\x80\x93 The gateway is running the capability configuration.
    OUT_OF_SYNC \xe2\x80\x93 The gateway hasn\'t received the capability configuration.
    SYNC_FAILED \xe2\x80\x93 The gateway rejected the capability configuration.
    
    """
    pass

def update_portal(portalId=None, portalName=None, portalDescription=None, portalContactEmail=None, portalLogoImage=None, roleArn=None, clientToken=None):
    """
    Updates an AWS IoT SiteWise Monitor portal.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_portal(
        portalId='string',
        portalName='string',
        portalDescription='string',
        portalContactEmail='string',
        portalLogoImage={
            'id': 'string',
            'file': {
                'data': b'bytes',
                'type': 'PNG'
            }
        },
        roleArn='string',
        clientToken='string'
    )
    
    
    :type portalId: string
    :param portalId: [REQUIRED]\nThe ID of the portal to update.\n

    :type portalName: string
    :param portalName: [REQUIRED]\nA new friendly name for the portal.\n

    :type portalDescription: string
    :param portalDescription: A new description for the portal.

    :type portalContactEmail: string
    :param portalContactEmail: [REQUIRED]\nThe AWS administrator\'s contact email address.\n

    :type portalLogoImage: dict
    :param portalLogoImage: Contains an image that is one of the following:\n\nAn image file. Choose this option to upload a new image.\nThe ID of an existing image. Choose this option to keep an existing image.\n\n\nid (string) --The ID of an existing image. Specify this parameter to keep an existing image.\n\nfile (dict) --Contains an image file.\n\ndata (bytes) -- [REQUIRED]The image file contents, represented as a base64-encoded string. The file size must be less than 1 MB.\n\ntype (string) -- [REQUIRED]The file type of the image.\n\n\n\n\n

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe ARN of a service role that allows the portal\'s users to access your AWS IoT SiteWise resources on your behalf. For more information, see Using service roles for AWS IoT SiteWise Monitor in the AWS IoT SiteWise User Guide .\n

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'portalStatus': {
        'state': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'FAILED',
        'error': {
            'code': 'INTERNAL_FAILURE',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --

portalStatus (dict) --
The status of the portal, which contains a state (UPDATING after successfully calling this operation) and any error message.

state (string) --
The current state of the portal.

error (dict) --
Contains associated error information, if any.

code (string) --
The error code.

message (string) --
The error message.











Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException
IoTSiteWise.Client.exceptions.ConflictingOperationException


    :return: {
        'portalStatus': {
            'state': 'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'FAILED',
            'error': {
                'code': 'INTERNAL_FAILURE',
                'message': 'string'
            }
        }
    }
    
    
    :returns: 
    IoTSiteWise.Client.exceptions.InvalidRequestException
    IoTSiteWise.Client.exceptions.ResourceNotFoundException
    IoTSiteWise.Client.exceptions.InternalFailureException
    IoTSiteWise.Client.exceptions.ThrottlingException
    IoTSiteWise.Client.exceptions.ConflictingOperationException
    
    """
    pass

def update_project(projectId=None, projectName=None, projectDescription=None, clientToken=None):
    """
    Updates an AWS IoT SiteWise Monitor project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_project(
        projectId='string',
        projectName='string',
        projectDescription='string',
        clientToken='string'
    )
    
    
    :type projectId: string
    :param projectId: [REQUIRED]\nThe ID of the project to update.\n

    :type projectName: string
    :param projectName: [REQUIRED]\nA new friendly name for the project.\n

    :type projectDescription: string
    :param projectDescription: A new description for the project.

    :type clientToken: string
    :param clientToken: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don\'t reuse this client token if a new idempotent request is required.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoTSiteWise.Client.exceptions.InvalidRequestException
IoTSiteWise.Client.exceptions.ResourceNotFoundException
IoTSiteWise.Client.exceptions.InternalFailureException
IoTSiteWise.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

