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

def create_application(ResourceGroupName=None, OpsCenterEnabled=None, CWEMonitorEnabled=None, OpsItemSNSTopicArn=None, Tags=None):
    """
    Adds an application that is created from a resource group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_application(
        ResourceGroupName='string',
        OpsCenterEnabled=True|False,
        CWEMonitorEnabled=True|False,
        OpsItemSNSTopicArn='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type OpsCenterEnabled: boolean
    :param OpsCenterEnabled: When set to true , creates opsItems for any problems detected on an application.

    :type CWEMonitorEnabled: boolean
    :param CWEMonitorEnabled: Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as instance terminated , failed deployment , and others.

    :type OpsItemSNSTopicArn: string
    :param OpsItemSNSTopicArn: The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem.

    :type Tags: list
    :param Tags: List of tags to add to the application. tag key (Key ) and an associated tag value (Value ). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.\n\n(dict) --An object that defines the tags associated with an application. A tag is a label that you optionally define and associate with an application. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria.\nEach tag consists of a required tag key and an associated tag value , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:\n\nTag keys and values are case sensitive.\nFor each associated resource, each tag key must be unique and it can have only one value.\nThe aws: prefix is reserved for use by AWS; you can\xe2\x80\x99t use it in any tag keys or values that you define. In addition, you can\'t edit or remove tag keys or values that use this prefix.\n\n\nKey (string) -- [REQUIRED]One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.\n\nValue (string) -- [REQUIRED]The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don\'t want an application to have a specific tag value, don\'t specify a value for this parameter.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationInfo': {
        'ResourceGroupName': 'string',
        'LifeCycle': 'string',
        'OpsItemSNSTopicArn': 'string',
        'OpsCenterEnabled': True|False,
        'CWEMonitorEnabled': True|False,
        'Remarks': 'string'
    }
}


Response Structure

(dict) --

ApplicationInfo (dict) --
Information about the application.

ResourceGroupName (string) --
The name of the resource group used for the application.

LifeCycle (string) --
The lifecycle of the application.

OpsItemSNSTopicArn (string) --
The SNS topic provided to Application Insights that is associated to the created opsItems to receive SNS notifications for opsItem updates.

OpsCenterEnabled (boolean) --
Indicates whether Application Insights will create opsItems for any problem detected by Application Insights for an application.

CWEMonitorEnabled (boolean) --
Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as instance terminated , failed deployment , and others.

Remarks (string) --
The issues on the user side that block Application Insights from successfully monitoring an application. Example remarks include:

\xe2\x80\x9cConfiguring application, detected 1 Errors, 3 Warnings\xe2\x80\x9d
\xe2\x80\x9cConfiguring application, detected 1 Unconfigured Components\xe2\x80\x9d










Exceptions

ApplicationInsights.Client.exceptions.ResourceInUseException
ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException
ApplicationInsights.Client.exceptions.TagsAlreadyExistException


    :return: {
        'ApplicationInfo': {
            'ResourceGroupName': 'string',
            'LifeCycle': 'string',
            'OpsItemSNSTopicArn': 'string',
            'OpsCenterEnabled': True|False,
            'CWEMonitorEnabled': True|False,
            'Remarks': 'string'
        }
    }
    
    
    :returns: 
    \xe2\x80\x9cConfiguring application, detected 1 Errors, 3 Warnings\xe2\x80\x9d
    \xe2\x80\x9cConfiguring application, detected 1 Unconfigured Components\xe2\x80\x9d
    
    """
    pass

def create_component(ResourceGroupName=None, ComponentName=None, ResourceList=None):
    """
    Creates a custom component by grouping similar standalone instances to monitor.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_component(
        ResourceGroupName='string',
        ComponentName='string',
        ResourceList=[
            'string',
        ]
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type ComponentName: string
    :param ComponentName: [REQUIRED]\nThe name of the component.\n

    :type ResourceList: list
    :param ResourceList: [REQUIRED]\nThe list of resource ARNs that belong to the component.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationInsights.Client.exceptions.ResourceInUseException
ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def create_log_pattern(ResourceGroupName=None, PatternSetName=None, PatternName=None, Pattern=None, Rank=None):
    """
    Adds an log pattern to a LogPatternSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_log_pattern(
        ResourceGroupName='string',
        PatternSetName='string',
        PatternName='string',
        Pattern='string',
        Rank=123
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type PatternSetName: string
    :param PatternSetName: [REQUIRED]\nThe name of the log pattern set.\n

    :type PatternName: string
    :param PatternName: [REQUIRED]\nThe name of the log pattern.\n

    :type Pattern: string
    :param Pattern: [REQUIRED]\nThe log pattern.\n

    :type Rank: integer
    :param Rank: [REQUIRED]\nRank of the log pattern.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'LogPattern': {
        'PatternSetName': 'string',
        'PatternName': 'string',
        'Pattern': 'string',
        'Rank': 123
    },
    'ResourceGroupName': 'string'
}


Response Structure

(dict) --

LogPattern (dict) --
The successfully created log pattern.

PatternSetName (string) --
The name of the log pattern. A log pattern name can contains at many as 30 characters, and it cannot be empty. The characters can be Unicode letters, digits or one of the following symbols: period, dash, underscore.

PatternName (string) --
The name of the log pattern. A log pattern name can contains at many as 50 characters, and it cannot be empty. The characters can be Unicode letters, digits or one of the following symbols: period, dash, underscore.

Pattern (string) --
A regular expression that defines the log pattern. A log pattern can contains at many as 50 characters, and it cannot be empty.

Rank (integer) --
Rank of the log pattern.



ResourceGroupName (string) --
The name of the resource group.







Exceptions

ApplicationInsights.Client.exceptions.ResourceInUseException
ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'LogPattern': {
            'PatternSetName': 'string',
            'PatternName': 'string',
            'Pattern': 'string',
            'Rank': 123
        },
        'ResourceGroupName': 'string'
    }
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.ResourceInUseException
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    ApplicationInsights.Client.exceptions.ValidationException
    ApplicationInsights.Client.exceptions.InternalServerException
    
    """
    pass

def delete_application(ResourceGroupName=None):
    """
    Removes the specified application from monitoring. Does not delete the application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_application(
        ResourceGroupName='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.BadRequestException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    ApplicationInsights.Client.exceptions.ValidationException
    ApplicationInsights.Client.exceptions.BadRequestException
    ApplicationInsights.Client.exceptions.InternalServerException
    
    """
    pass

def delete_component(ResourceGroupName=None, ComponentName=None):
    """
    Ungroups a custom component. When you ungroup custom components, all applicable monitors that are set up for the component are removed and the instances revert to their standalone status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_component(
        ResourceGroupName='string',
        ComponentName='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type ComponentName: string
    :param ComponentName: [REQUIRED]\nThe name of the component.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_log_pattern(ResourceGroupName=None, PatternSetName=None, PatternName=None):
    """
    Removes the specified log pattern from a LogPatternSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_log_pattern(
        ResourceGroupName='string',
        PatternSetName='string',
        PatternName='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type PatternSetName: string
    :param PatternSetName: [REQUIRED]\nThe name of the log pattern set.\n

    :type PatternName: string
    :param PatternName: [REQUIRED]\nThe name of the log pattern.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.BadRequestException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def describe_application(ResourceGroupName=None):
    """
    Describes the application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_application(
        ResourceGroupName='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ApplicationInfo': {
        'ResourceGroupName': 'string',
        'LifeCycle': 'string',
        'OpsItemSNSTopicArn': 'string',
        'OpsCenterEnabled': True|False,
        'CWEMonitorEnabled': True|False,
        'Remarks': 'string'
    }
}


Response Structure

(dict) --
ApplicationInfo (dict) --Information about the application.

ResourceGroupName (string) --The name of the resource group used for the application.

LifeCycle (string) --The lifecycle of the application.

OpsItemSNSTopicArn (string) --The SNS topic provided to Application Insights that is associated to the created opsItems to receive SNS notifications for opsItem updates.

OpsCenterEnabled (boolean) --Indicates whether Application Insights will create opsItems for any problem detected by Application Insights for an application.

CWEMonitorEnabled (boolean) --Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as instance terminated , failed deployment , and others.

Remarks (string) --The issues on the user side that block Application Insights from successfully monitoring an application. Example remarks include:

\xe2\x80\x9cConfiguring application, detected 1 Errors, 3 Warnings\xe2\x80\x9d
\xe2\x80\x9cConfiguring application, detected 1 Unconfigured Components\xe2\x80\x9d









Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'ApplicationInfo': {
            'ResourceGroupName': 'string',
            'LifeCycle': 'string',
            'OpsItemSNSTopicArn': 'string',
            'OpsCenterEnabled': True|False,
            'CWEMonitorEnabled': True|False,
            'Remarks': 'string'
        }
    }
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    ApplicationInsights.Client.exceptions.ValidationException
    ApplicationInsights.Client.exceptions.InternalServerException
    
    """
    pass

def describe_component(ResourceGroupName=None, ComponentName=None):
    """
    Describes a component and lists the resources that are grouped together in a component.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_component(
        ResourceGroupName='string',
        ComponentName='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type ComponentName: string
    :param ComponentName: [REQUIRED]\nThe name of the component.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationComponent': {
        'ComponentName': 'string',
        'ResourceType': 'string',
        'Tier': 'DEFAULT'|'DOT_NET_CORE'|'DOT_NET_WORKER'|'DOT_NET_WEB'|'SQL_SERVER',
        'Monitor': True|False
    },
    'ResourceList': [
        'string',
    ]
}


Response Structure

(dict) --

ApplicationComponent (dict) --
Describes a standalone resource or similarly grouped resources that the application is made up of.

ComponentName (string) --
The name of the component.

ResourceType (string) --
The resource type. Supported resource types include EC2 instances, Auto Scaling group, Classic ELB, Application ELB, and SQS Queue.

Tier (string) --
The stack tier of the application component.

Monitor (boolean) --
Indicates whether the application component is monitored.



ResourceList (list) --
The list of resource ARNs that belong to the component.

(string) --








Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'ApplicationComponent': {
            'ComponentName': 'string',
            'ResourceType': 'string',
            'Tier': 'DEFAULT'|'DOT_NET_CORE'|'DOT_NET_WORKER'|'DOT_NET_WEB'|'SQL_SERVER',
            'Monitor': True|False
        },
        'ResourceList': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_component_configuration(ResourceGroupName=None, ComponentName=None):
    """
    Describes the monitoring configuration of the component.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_component_configuration(
        ResourceGroupName='string',
        ComponentName='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type ComponentName: string
    :param ComponentName: [REQUIRED]\nThe name of the component.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Monitor': True|False,
    'Tier': 'DEFAULT'|'DOT_NET_CORE'|'DOT_NET_WORKER'|'DOT_NET_WEB'|'SQL_SERVER',
    'ComponentConfiguration': 'string'
}


Response Structure

(dict) --

Monitor (boolean) --
Indicates whether the application component is monitored.

Tier (string) --
The tier of the application component. Supported tiers include DOT_NET_CORE , DOT_NET_WORKER , DOT_NET_WEB , SQL_SERVER , and DEFAULT

ComponentConfiguration (string) --
The configuration settings of the component. The value is the escaped JSON of the configuration.







Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'Monitor': True|False,
        'Tier': 'DEFAULT'|'DOT_NET_CORE'|'DOT_NET_WORKER'|'DOT_NET_WEB'|'SQL_SERVER',
        'ComponentConfiguration': 'string'
    }
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    ApplicationInsights.Client.exceptions.ValidationException
    ApplicationInsights.Client.exceptions.InternalServerException
    
    """
    pass

def describe_component_configuration_recommendation(ResourceGroupName=None, ComponentName=None, Tier=None):
    """
    Describes the recommended monitoring configuration of the component.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_component_configuration_recommendation(
        ResourceGroupName='string',
        ComponentName='string',
        Tier='DEFAULT'|'DOT_NET_CORE'|'DOT_NET_WORKER'|'DOT_NET_WEB'|'SQL_SERVER'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type ComponentName: string
    :param ComponentName: [REQUIRED]\nThe name of the component.\n

    :type Tier: string
    :param Tier: [REQUIRED]\nThe tier of the application component. Supported tiers include DOT_NET_CORE , DOT_NET_WORKER , DOT_NET_WEB , SQL_SERVER , and DEFAULT .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ComponentConfiguration': 'string'
}


Response Structure

(dict) --

ComponentConfiguration (string) --
The recommended configuration settings of the component. The value is the escaped JSON of the configuration.







Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'ComponentConfiguration': 'string'
    }
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    ApplicationInsights.Client.exceptions.ValidationException
    ApplicationInsights.Client.exceptions.InternalServerException
    
    """
    pass

def describe_log_pattern(ResourceGroupName=None, PatternSetName=None, PatternName=None):
    """
    Describe a specific log pattern from a LogPatternSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_log_pattern(
        ResourceGroupName='string',
        PatternSetName='string',
        PatternName='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type PatternSetName: string
    :param PatternSetName: [REQUIRED]\nThe name of the log pattern set.\n

    :type PatternName: string
    :param PatternName: [REQUIRED]\nThe name of the log pattern.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceGroupName': 'string',
    'LogPattern': {
        'PatternSetName': 'string',
        'PatternName': 'string',
        'Pattern': 'string',
        'Rank': 123
    }
}


Response Structure

(dict) --

ResourceGroupName (string) --
The name of the resource group.

LogPattern (dict) --
The successfully created log pattern.

PatternSetName (string) --
The name of the log pattern. A log pattern name can contains at many as 30 characters, and it cannot be empty. The characters can be Unicode letters, digits or one of the following symbols: period, dash, underscore.

PatternName (string) --
The name of the log pattern. A log pattern name can contains at many as 50 characters, and it cannot be empty. The characters can be Unicode letters, digits or one of the following symbols: period, dash, underscore.

Pattern (string) --
A regular expression that defines the log pattern. A log pattern can contains at many as 50 characters, and it cannot be empty.

Rank (integer) --
Rank of the log pattern.









Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'ResourceGroupName': 'string',
        'LogPattern': {
            'PatternSetName': 'string',
            'PatternName': 'string',
            'Pattern': 'string',
            'Rank': 123
        }
    }
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    ApplicationInsights.Client.exceptions.ValidationException
    ApplicationInsights.Client.exceptions.InternalServerException
    
    """
    pass

def describe_observation(ObservationId=None):
    """
    Describes an anomaly or error with the application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_observation(
        ObservationId='string'
    )
    
    
    :type ObservationId: string
    :param ObservationId: [REQUIRED]\nThe ID of the observation.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Observation': {
        'Id': 'string',
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'SourceType': 'string',
        'SourceARN': 'string',
        'LogGroup': 'string',
        'LineTime': datetime(2015, 1, 1),
        'LogText': 'string',
        'LogFilter': 'ERROR'|'WARN'|'INFO',
        'MetricNamespace': 'string',
        'MetricName': 'string',
        'Unit': 'string',
        'Value': 123.0,
        'CloudWatchEventId': 'string',
        'CloudWatchEventSource': 'EC2'|'CODE_DEPLOY'|'HEALTH',
        'CloudWatchEventDetailType': 'string',
        'HealthEventArn': 'string',
        'HealthService': 'string',
        'HealthEventTypeCode': 'string',
        'HealthEventTypeCategory': 'string',
        'HealthEventDescription': 'string',
        'CodeDeployDeploymentId': 'string',
        'CodeDeployDeploymentGroup': 'string',
        'CodeDeployState': 'string',
        'CodeDeployApplication': 'string',
        'CodeDeployInstanceGroupId': 'string',
        'Ec2State': 'string',
        'XRayFaultPercent': 123,
        'XRayThrottlePercent': 123,
        'XRayErrorPercent': 123,
        'XRayRequestCount': 123,
        'XRayRequestAverageLatency': 123,
        'XRayNodeName': 'string',
        'XRayNodeType': 'string'
    }
}


Response Structure

(dict) --
Observation (dict) --Information about the observation.

Id (string) --The ID of the observation type.

StartTime (datetime) --The time when the observation was first detected, in epoch seconds.

EndTime (datetime) --The time when the observation ended, in epoch seconds.

SourceType (string) --The source type of the observation.

SourceARN (string) --The source resource ARN of the observation.

LogGroup (string) --The log group name.

LineTime (datetime) --The timestamp in the CloudWatch Logs that specifies when the matched line occurred.

LogText (string) --The log text of the observation.

LogFilter (string) --The log filter of the observation.

MetricNamespace (string) --The namespace of the observation metric.

MetricName (string) --The name of the observation metric.

Unit (string) --The unit of the source observation metric.

Value (float) --The value of the source observation metric.

CloudWatchEventId (string) --The ID of the CloudWatch Event-based observation related to the detected problem.

CloudWatchEventSource (string) --The source of the CloudWatch Event.

CloudWatchEventDetailType (string) --The detail type of the CloudWatch Event-based observation, for example, EC2 Instance State-change Notification .

HealthEventArn (string) --The Amazon Resource Name (ARN) of the AWS Health Event-based observation.

HealthService (string) --The service to which the AWS Health Event belongs, such as EC2.

HealthEventTypeCode (string) --The type of the AWS Health event, for example, AWS_EC2_POWER_CONNECTIVITY_ISSUE .

HealthEventTypeCategory (string) --The category of the AWS Health event, such as issue .

HealthEventDescription (string) --The description of the AWS Health event provided by the service, such as Amazon EC2.

CodeDeployDeploymentId (string) --The deployment ID of the CodeDeploy-based observation related to the detected problem.

CodeDeployDeploymentGroup (string) --The deployment group to which the CodeDeploy deployment belongs.

CodeDeployState (string) --The status of the CodeDeploy deployment, for example SUCCESS or FAILURE .

CodeDeployApplication (string) --The CodeDeploy application to which the deployment belongs.

CodeDeployInstanceGroupId (string) --The instance group to which the CodeDeploy instance belongs.

Ec2State (string) --The state of the instance, such as STOPPING or TERMINATING .

XRayFaultPercent (integer) --The X-Ray request fault percentage for this node.

XRayThrottlePercent (integer) --The X-Ray request throttle percentage for this node.

XRayErrorPercent (integer) --The X-Ray request error percentage for this node.

XRayRequestCount (integer) --The X-Ray request count for this node.

XRayRequestAverageLatency (integer) --The X-Ray node request average latency for this node.

XRayNodeName (string) --The name of the X-Ray node.

XRayNodeType (string) --The type of the X-Ray node.








Exceptions

ApplicationInsights.Client.exceptions.InternalServerException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.ResourceNotFoundException


    :return: {
        'Observation': {
            'Id': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'SourceType': 'string',
            'SourceARN': 'string',
            'LogGroup': 'string',
            'LineTime': datetime(2015, 1, 1),
            'LogText': 'string',
            'LogFilter': 'ERROR'|'WARN'|'INFO',
            'MetricNamespace': 'string',
            'MetricName': 'string',
            'Unit': 'string',
            'Value': 123.0,
            'CloudWatchEventId': 'string',
            'CloudWatchEventSource': 'EC2'|'CODE_DEPLOY'|'HEALTH',
            'CloudWatchEventDetailType': 'string',
            'HealthEventArn': 'string',
            'HealthService': 'string',
            'HealthEventTypeCode': 'string',
            'HealthEventTypeCategory': 'string',
            'HealthEventDescription': 'string',
            'CodeDeployDeploymentId': 'string',
            'CodeDeployDeploymentGroup': 'string',
            'CodeDeployState': 'string',
            'CodeDeployApplication': 'string',
            'CodeDeployInstanceGroupId': 'string',
            'Ec2State': 'string',
            'XRayFaultPercent': 123,
            'XRayThrottlePercent': 123,
            'XRayErrorPercent': 123,
            'XRayRequestCount': 123,
            'XRayRequestAverageLatency': 123,
            'XRayNodeName': 'string',
            'XRayNodeType': 'string'
        }
    }
    
    
    """
    pass

def describe_problem(ProblemId=None):
    """
    Describes an application problem.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_problem(
        ProblemId='string'
    )
    
    
    :type ProblemId: string
    :param ProblemId: [REQUIRED]\nThe ID of the problem.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Problem': {
        'Id': 'string',
        'Title': 'string',
        'Insights': 'string',
        'Status': 'IGNORE'|'RESOLVED'|'PENDING',
        'AffectedResource': 'string',
        'StartTime': datetime(2015, 1, 1),
        'EndTime': datetime(2015, 1, 1),
        'SeverityLevel': 'Low'|'Medium'|'High',
        'ResourceGroupName': 'string',
        'Feedback': {
            'string': 'NOT_SPECIFIED'|'USEFUL'|'NOT_USEFUL'
        }
    }
}


Response Structure

(dict) --
Problem (dict) --Information about the problem.

Id (string) --The ID of the problem.

Title (string) --The name of the problem.

Insights (string) --A detailed analysis of the problem using machine learning.

Status (string) --The status of the problem.

AffectedResource (string) --The resource affected by the problem.

StartTime (datetime) --The time when the problem started, in epoch seconds.

EndTime (datetime) --The time when the problem ended, in epoch seconds.

SeverityLevel (string) --A measure of the level of impact of the problem.

ResourceGroupName (string) --The name of the resource group affected by the problem.

Feedback (dict) --Feedback provided by the user about the problem.

(string) --
(string) --











Exceptions

ApplicationInsights.Client.exceptions.InternalServerException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.ResourceNotFoundException


    :return: {
        'Problem': {
            'Id': 'string',
            'Title': 'string',
            'Insights': 'string',
            'Status': 'IGNORE'|'RESOLVED'|'PENDING',
            'AffectedResource': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'SeverityLevel': 'Low'|'Medium'|'High',
            'ResourceGroupName': 'string',
            'Feedback': {
                'string': 'NOT_SPECIFIED'|'USEFUL'|'NOT_USEFUL'
            }
        }
    }
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.InternalServerException
    ApplicationInsights.Client.exceptions.ValidationException
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_problem_observations(ProblemId=None):
    """
    Describes the anomalies or errors associated with the problem.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_problem_observations(
        ProblemId='string'
    )
    
    
    :type ProblemId: string
    :param ProblemId: [REQUIRED]\nThe ID of the problem.\n

    :rtype: dict
ReturnsResponse Syntax{
    'RelatedObservations': {
        'ObservationList': [
            {
                'Id': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'SourceType': 'string',
                'SourceARN': 'string',
                'LogGroup': 'string',
                'LineTime': datetime(2015, 1, 1),
                'LogText': 'string',
                'LogFilter': 'ERROR'|'WARN'|'INFO',
                'MetricNamespace': 'string',
                'MetricName': 'string',
                'Unit': 'string',
                'Value': 123.0,
                'CloudWatchEventId': 'string',
                'CloudWatchEventSource': 'EC2'|'CODE_DEPLOY'|'HEALTH',
                'CloudWatchEventDetailType': 'string',
                'HealthEventArn': 'string',
                'HealthService': 'string',
                'HealthEventTypeCode': 'string',
                'HealthEventTypeCategory': 'string',
                'HealthEventDescription': 'string',
                'CodeDeployDeploymentId': 'string',
                'CodeDeployDeploymentGroup': 'string',
                'CodeDeployState': 'string',
                'CodeDeployApplication': 'string',
                'CodeDeployInstanceGroupId': 'string',
                'Ec2State': 'string',
                'XRayFaultPercent': 123,
                'XRayThrottlePercent': 123,
                'XRayErrorPercent': 123,
                'XRayRequestCount': 123,
                'XRayRequestAverageLatency': 123,
                'XRayNodeName': 'string',
                'XRayNodeType': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
RelatedObservations (dict) --Observations related to the problem.

ObservationList (list) --The list of observations related to the problem.

(dict) --Describes an anomaly or error with the application.

Id (string) --The ID of the observation type.

StartTime (datetime) --The time when the observation was first detected, in epoch seconds.

EndTime (datetime) --The time when the observation ended, in epoch seconds.

SourceType (string) --The source type of the observation.

SourceARN (string) --The source resource ARN of the observation.

LogGroup (string) --The log group name.

LineTime (datetime) --The timestamp in the CloudWatch Logs that specifies when the matched line occurred.

LogText (string) --The log text of the observation.

LogFilter (string) --The log filter of the observation.

MetricNamespace (string) --The namespace of the observation metric.

MetricName (string) --The name of the observation metric.

Unit (string) --The unit of the source observation metric.

Value (float) --The value of the source observation metric.

CloudWatchEventId (string) --The ID of the CloudWatch Event-based observation related to the detected problem.

CloudWatchEventSource (string) --The source of the CloudWatch Event.

CloudWatchEventDetailType (string) --The detail type of the CloudWatch Event-based observation, for example, EC2 Instance State-change Notification .

HealthEventArn (string) --The Amazon Resource Name (ARN) of the AWS Health Event-based observation.

HealthService (string) --The service to which the AWS Health Event belongs, such as EC2.

HealthEventTypeCode (string) --The type of the AWS Health event, for example, AWS_EC2_POWER_CONNECTIVITY_ISSUE .

HealthEventTypeCategory (string) --The category of the AWS Health event, such as issue .

HealthEventDescription (string) --The description of the AWS Health event provided by the service, such as Amazon EC2.

CodeDeployDeploymentId (string) --The deployment ID of the CodeDeploy-based observation related to the detected problem.

CodeDeployDeploymentGroup (string) --The deployment group to which the CodeDeploy deployment belongs.

CodeDeployState (string) --The status of the CodeDeploy deployment, for example SUCCESS or FAILURE .

CodeDeployApplication (string) --The CodeDeploy application to which the deployment belongs.

CodeDeployInstanceGroupId (string) --The instance group to which the CodeDeploy instance belongs.

Ec2State (string) --The state of the instance, such as STOPPING or TERMINATING .

XRayFaultPercent (integer) --The X-Ray request fault percentage for this node.

XRayThrottlePercent (integer) --The X-Ray request throttle percentage for this node.

XRayErrorPercent (integer) --The X-Ray request error percentage for this node.

XRayRequestCount (integer) --The X-Ray request count for this node.

XRayRequestAverageLatency (integer) --The X-Ray node request average latency for this node.

XRayNodeName (string) --The name of the X-Ray node.

XRayNodeType (string) --The type of the X-Ray node.












Exceptions

ApplicationInsights.Client.exceptions.InternalServerException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.ResourceNotFoundException


    :return: {
        'RelatedObservations': {
            'ObservationList': [
                {
                    'Id': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'SourceType': 'string',
                    'SourceARN': 'string',
                    'LogGroup': 'string',
                    'LineTime': datetime(2015, 1, 1),
                    'LogText': 'string',
                    'LogFilter': 'ERROR'|'WARN'|'INFO',
                    'MetricNamespace': 'string',
                    'MetricName': 'string',
                    'Unit': 'string',
                    'Value': 123.0,
                    'CloudWatchEventId': 'string',
                    'CloudWatchEventSource': 'EC2'|'CODE_DEPLOY'|'HEALTH',
                    'CloudWatchEventDetailType': 'string',
                    'HealthEventArn': 'string',
                    'HealthService': 'string',
                    'HealthEventTypeCode': 'string',
                    'HealthEventTypeCategory': 'string',
                    'HealthEventDescription': 'string',
                    'CodeDeployDeploymentId': 'string',
                    'CodeDeployDeploymentGroup': 'string',
                    'CodeDeployState': 'string',
                    'CodeDeployApplication': 'string',
                    'CodeDeployInstanceGroupId': 'string',
                    'Ec2State': 'string',
                    'XRayFaultPercent': 123,
                    'XRayThrottlePercent': 123,
                    'XRayErrorPercent': 123,
                    'XRayRequestCount': 123,
                    'XRayRequestAverageLatency': 123,
                    'XRayNodeName': 'string',
                    'XRayNodeType': 'string'
                },
            ]
        }
    }
    
    
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

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def list_applications(MaxResults=None, NextToken=None):
    """
    Lists the IDs of the applications that you are monitoring.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_applications(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationInfoList': [
        {
            'ResourceGroupName': 'string',
            'LifeCycle': 'string',
            'OpsItemSNSTopicArn': 'string',
            'OpsCenterEnabled': True|False,
            'CWEMonitorEnabled': True|False,
            'Remarks': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ApplicationInfoList (list) --
The list of applications.

(dict) --
Describes the status of the application.

ResourceGroupName (string) --
The name of the resource group used for the application.

LifeCycle (string) --
The lifecycle of the application.

OpsItemSNSTopicArn (string) --
The SNS topic provided to Application Insights that is associated to the created opsItems to receive SNS notifications for opsItem updates.

OpsCenterEnabled (boolean) --
Indicates whether Application Insights will create opsItems for any problem detected by Application Insights for an application.

CWEMonitorEnabled (boolean) --
Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as instance terminated , failed deployment , and others.

Remarks (string) --
The issues on the user side that block Application Insights from successfully monitoring an application. Example remarks include:

\xe2\x80\x9cConfiguring application, detected 1 Errors, 3 Warnings\xe2\x80\x9d
\xe2\x80\x9cConfiguring application, detected 1 Unconfigured Components\xe2\x80\x9d






NextToken (string) --
The token used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'ApplicationInfoList': [
            {
                'ResourceGroupName': 'string',
                'LifeCycle': 'string',
                'OpsItemSNSTopicArn': 'string',
                'OpsCenterEnabled': True|False,
                'CWEMonitorEnabled': True|False,
                'Remarks': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    \xe2\x80\x9cConfiguring application, detected 1 Errors, 3 Warnings\xe2\x80\x9d
    \xe2\x80\x9cConfiguring application, detected 1 Unconfigured Components\xe2\x80\x9d
    
    """
    pass

def list_components(ResourceGroupName=None, MaxResults=None, NextToken=None):
    """
    Lists the auto-grouped, standalone, and custom components of the application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_components(
        ResourceGroupName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationComponentList': [
        {
            'ComponentName': 'string',
            'ResourceType': 'string',
            'Tier': 'DEFAULT'|'DOT_NET_CORE'|'DOT_NET_WORKER'|'DOT_NET_WEB'|'SQL_SERVER',
            'Monitor': True|False
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ApplicationComponentList (list) --
The list of application components.

(dict) --
Describes a standalone resource or similarly grouped resources that the application is made up of.

ComponentName (string) --
The name of the component.

ResourceType (string) --
The resource type. Supported resource types include EC2 instances, Auto Scaling group, Classic ELB, Application ELB, and SQS Queue.

Tier (string) --
The stack tier of the application component.

Monitor (boolean) --
Indicates whether the application component is monitored.





NextToken (string) --
The token to request the next page of results.







Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'ApplicationComponentList': [
            {
                'ComponentName': 'string',
                'ResourceType': 'string',
                'Tier': 'DEFAULT'|'DOT_NET_CORE'|'DOT_NET_WORKER'|'DOT_NET_WEB'|'SQL_SERVER',
                'Monitor': True|False
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    ApplicationInsights.Client.exceptions.ValidationException
    ApplicationInsights.Client.exceptions.InternalServerException
    
    """
    pass

def list_configuration_history(ResourceGroupName=None, StartTime=None, EndTime=None, EventStatus=None, MaxResults=None, NextToken=None):
    """
    Lists the INFO, WARN, and ERROR events for periodic configuration updates performed by Application Insights. Examples of events represented are:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_configuration_history(
        ResourceGroupName='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        EventStatus='INFO'|'WARN'|'ERROR',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: Resource group to which the application belongs.

    :type StartTime: datetime
    :param StartTime: The start time of the event.

    :type EndTime: datetime
    :param EndTime: The end time of the event.

    :type EventStatus: string
    :param EventStatus: The status of the configuration update event. Possible values include INFO, WARN, and ERROR.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results returned by ListConfigurationHistory in paginated output. When this parameter is used, ListConfigurationHistory returns only MaxResults in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another ListConfigurationHistory request with the returned NextToken value. If this parameter is not used, then ListConfigurationHistory returns all results.

    :type NextToken: string
    :param NextToken: The NextToken value returned from a previous paginated ListConfigurationHistory request where MaxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the NextToken value. This value is null when there are no more results to return.

    :rtype: dict

ReturnsResponse Syntax
{
    'EventList': [
        {
            'MonitoredResourceARN': 'string',
            'EventStatus': 'INFO'|'WARN'|'ERROR',
            'EventResourceType': 'CLOUDWATCH_ALARM'|'CLOUDFORMATION'|'SSM_ASSOCIATION',
            'EventTime': datetime(2015, 1, 1),
            'EventDetail': 'string',
            'EventResourceName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

EventList (list) --
The list of configuration events and their corresponding details.

(dict) --
The event information.

MonitoredResourceARN (string) --
The resource monitored by Application Insights.

EventStatus (string) --
The status of the configuration update event. Possible values include INFO, WARN, and ERROR.

EventResourceType (string) --
The resource type that Application Insights attempted to configure, for example, CLOUDWATCH_ALARM.

EventTime (datetime) --
The timestamp of the event.

EventDetail (string) --
The details of the event in plain text.

EventResourceName (string) --
The name of the resource Application Insights attempted to configure.





NextToken (string) --
The NextToken value to include in a future ListConfigurationHistory request. When the results of a ListConfigurationHistory request exceed MaxResults , this value can be used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'EventList': [
            {
                'MonitoredResourceARN': 'string',
                'EventStatus': 'INFO'|'WARN'|'ERROR',
                'EventResourceType': 'CLOUDWATCH_ALARM'|'CLOUDFORMATION'|'SSM_ASSOCIATION',
                'EventTime': datetime(2015, 1, 1),
                'EventDetail': 'string',
                'EventResourceName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ResourceGroupName (string) -- Resource group to which the application belongs.
    StartTime (datetime) -- The start time of the event.
    EndTime (datetime) -- The end time of the event.
    EventStatus (string) -- The status of the configuration update event. Possible values include INFO, WARN, and ERROR.
    MaxResults (integer) -- The maximum number of results returned by ListConfigurationHistory in paginated output. When this parameter is used, ListConfigurationHistory returns only MaxResults in a single page along with a NextToken response element. The remaining results of the initial request can be seen by sending another ListConfigurationHistory request with the returned NextToken value. If this parameter is not used, then ListConfigurationHistory returns all results.
    NextToken (string) -- The NextToken value returned from a previous paginated ListConfigurationHistory request where MaxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the NextToken value. This value is null when there are no more results to return.
    
    """
    pass

def list_log_pattern_sets(ResourceGroupName=None, MaxResults=None, NextToken=None):
    """
    Lists the log pattern sets in the specific application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_log_pattern_sets(
        ResourceGroupName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceGroupName': 'string',
    'LogPatternSets': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ResourceGroupName (string) --
The name of the resource group.

LogPatternSets (list) --
The list of log pattern sets.

(string) --


NextToken (string) --
The token used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'ResourceGroupName': 'string',
        'LogPatternSets': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_log_patterns(ResourceGroupName=None, PatternSetName=None, MaxResults=None, NextToken=None):
    """
    Lists the log patterns in the specific log LogPatternSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_log_patterns(
        ResourceGroupName='string',
        PatternSetName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type PatternSetName: string
    :param PatternSetName: The name of the log pattern set.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceGroupName': 'string',
    'LogPatterns': [
        {
            'PatternSetName': 'string',
            'PatternName': 'string',
            'Pattern': 'string',
            'Rank': 123
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ResourceGroupName (string) --
The name of the resource group.

LogPatterns (list) --
The list of log patterns.

(dict) --
An object that defines the log patterns that belongs to a LogPatternSet .

PatternSetName (string) --
The name of the log pattern. A log pattern name can contains at many as 30 characters, and it cannot be empty. The characters can be Unicode letters, digits or one of the following symbols: period, dash, underscore.

PatternName (string) --
The name of the log pattern. A log pattern name can contains at many as 50 characters, and it cannot be empty. The characters can be Unicode letters, digits or one of the following symbols: period, dash, underscore.

Pattern (string) --
A regular expression that defines the log pattern. A log pattern can contains at many as 50 characters, and it cannot be empty.

Rank (integer) --
Rank of the log pattern.





NextToken (string) --
The token used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'ResourceGroupName': 'string',
        'LogPatterns': [
            {
                'PatternSetName': 'string',
                'PatternName': 'string',
                'Pattern': 'string',
                'Rank': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    ApplicationInsights.Client.exceptions.ValidationException
    ApplicationInsights.Client.exceptions.InternalServerException
    
    """
    pass

def list_problems(ResourceGroupName=None, StartTime=None, EndTime=None, MaxResults=None, NextToken=None):
    """
    Lists the problems with your application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_problems(
        ResourceGroupName='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: The name of the resource group.

    :type StartTime: datetime
    :param StartTime: The time when the problem was detected, in epoch seconds. If you don\'t specify a time frame for the request, problems within the past seven days are returned.

    :type EndTime: datetime
    :param EndTime: The time when the problem ended, in epoch seconds. If not specified, problems within the past seven days are returned.

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.

    :type NextToken: string
    :param NextToken: The token to request the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'ProblemList': [
        {
            'Id': 'string',
            'Title': 'string',
            'Insights': 'string',
            'Status': 'IGNORE'|'RESOLVED'|'PENDING',
            'AffectedResource': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'SeverityLevel': 'Low'|'Medium'|'High',
            'ResourceGroupName': 'string',
            'Feedback': {
                'string': 'NOT_SPECIFIED'|'USEFUL'|'NOT_USEFUL'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ProblemList (list) --
The list of problems.

(dict) --
Describes a problem that is detected by correlating observations.

Id (string) --
The ID of the problem.

Title (string) --
The name of the problem.

Insights (string) --
A detailed analysis of the problem using machine learning.

Status (string) --
The status of the problem.

AffectedResource (string) --
The resource affected by the problem.

StartTime (datetime) --
The time when the problem started, in epoch seconds.

EndTime (datetime) --
The time when the problem ended, in epoch seconds.

SeverityLevel (string) --
A measure of the level of impact of the problem.

ResourceGroupName (string) --
The name of the resource group affected by the problem.

Feedback (dict) --
Feedback provided by the user about the problem.

(string) --
(string) --








NextToken (string) --
The token used to retrieve the next page of results. This value is null when there are no more results to return.







Exceptions

ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'ProblemList': [
            {
                'Id': 'string',
                'Title': 'string',
                'Insights': 'string',
                'Status': 'IGNORE'|'RESOLVED'|'PENDING',
                'AffectedResource': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'SeverityLevel': 'Low'|'Medium'|'High',
                'ResourceGroupName': 'string',
                'Feedback': {
                    'string': 'NOT_SPECIFIED'|'USEFUL'|'NOT_USEFUL'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_tags_for_resource(ResourceARN=None):
    """
    Retrieve a list of the tags (keys and values) that are associated with a specified application. A tag is a label that you optionally define and associate with an application. Each tag consists of a required tag key and an optional associated tag value . A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string'
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application that you want to retrieve tag information for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}


Response Structure

(dict) --
Tags (list) --An array that lists all the tags that are associated with the application. Each tag consists of a required tag key (Key ) and an associated tag value (Value ).

(dict) --An object that defines the tags associated with an application. A tag is a label that you optionally define and associate with an application. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria.
Each tag consists of a required tag key and an associated tag value , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:

Tag keys and values are case sensitive.
For each associated resource, each tag key must be unique and it can have only one value.
The aws: prefix is reserved for use by AWS; you can\xe2\x80\x99t use it in any tag keys or values that you define. In addition, you can\'t edit or remove tag keys or values that use this prefix.


Key (string) --One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.

Value (string) --The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don\'t want an application to have a specific tag value, don\'t specify a value for this parameter.










Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    ApplicationInsights.Client.exceptions.ValidationException
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Add one or more tags (keys and values) to a specified application. A tag is a label that you optionally define and associate with an application. Tags can help you categorize and manage application in different ways, such as by purpose, owner, environment, or other criteria.
    Each tag consists of a required tag key and an associated tag value , both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceARN='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application that you want to add one or more tags to.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA list of tags that to add to the application. A tag consists of a required tag key (Key ) and an associated tag value (Value ). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.\n\n(dict) --An object that defines the tags associated with an application. A tag is a label that you optionally define and associate with an application. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria.\nEach tag consists of a required tag key and an associated tag value , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:\n\nTag keys and values are case sensitive.\nFor each associated resource, each tag key must be unique and it can have only one value.\nThe aws: prefix is reserved for use by AWS; you can\xe2\x80\x99t use it in any tag keys or values that you define. In addition, you can\'t edit or remove tag keys or values that use this prefix.\n\n\nKey (string) -- [REQUIRED]One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.\n\nValue (string) -- [REQUIRED]The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don\'t want an application to have a specific tag value, don\'t specify a value for this parameter.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.TooManyTagsException
ApplicationInsights.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Remove one or more tags (keys and values) from a specified application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN) of the application that you want to remove one or more tags from.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.\nTo remove more than one tag from the application, append the TagKeys parameter and argument for each additional tag to remove, separated by an ampersand.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_application(ResourceGroupName=None, OpsCenterEnabled=None, CWEMonitorEnabled=None, OpsItemSNSTopicArn=None, RemoveSNSTopic=None):
    """
    Updates the application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_application(
        ResourceGroupName='string',
        OpsCenterEnabled=True|False,
        CWEMonitorEnabled=True|False,
        OpsItemSNSTopicArn='string',
        RemoveSNSTopic=True|False
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type OpsCenterEnabled: boolean
    :param OpsCenterEnabled: When set to true , creates opsItems for any problems detected on an application.

    :type CWEMonitorEnabled: boolean
    :param CWEMonitorEnabled: Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as instance terminated , failed deployment , and others.

    :type OpsItemSNSTopicArn: string
    :param OpsItemSNSTopicArn: The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem.

    :type RemoveSNSTopic: boolean
    :param RemoveSNSTopic: Disassociates the SNS topic from the opsItem created for detected problems.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationInfo': {
        'ResourceGroupName': 'string',
        'LifeCycle': 'string',
        'OpsItemSNSTopicArn': 'string',
        'OpsCenterEnabled': True|False,
        'CWEMonitorEnabled': True|False,
        'Remarks': 'string'
    }
}


Response Structure

(dict) --

ApplicationInfo (dict) --
Information about the application.

ResourceGroupName (string) --
The name of the resource group used for the application.

LifeCycle (string) --
The lifecycle of the application.

OpsItemSNSTopicArn (string) --
The SNS topic provided to Application Insights that is associated to the created opsItems to receive SNS notifications for opsItem updates.

OpsCenterEnabled (boolean) --
Indicates whether Application Insights will create opsItems for any problem detected by Application Insights for an application.

CWEMonitorEnabled (boolean) --
Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as instance terminated , failed deployment , and others.

Remarks (string) --
The issues on the user side that block Application Insights from successfully monitoring an application. Example remarks include:

\xe2\x80\x9cConfiguring application, detected 1 Errors, 3 Warnings\xe2\x80\x9d
\xe2\x80\x9cConfiguring application, detected 1 Unconfigured Components\xe2\x80\x9d










Exceptions

ApplicationInsights.Client.exceptions.InternalServerException
ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException


    :return: {
        'ApplicationInfo': {
            'ResourceGroupName': 'string',
            'LifeCycle': 'string',
            'OpsItemSNSTopicArn': 'string',
            'OpsCenterEnabled': True|False,
            'CWEMonitorEnabled': True|False,
            'Remarks': 'string'
        }
    }
    
    
    :returns: 
    \xe2\x80\x9cConfiguring application, detected 1 Errors, 3 Warnings\xe2\x80\x9d
    \xe2\x80\x9cConfiguring application, detected 1 Unconfigured Components\xe2\x80\x9d
    
    """
    pass

def update_component(ResourceGroupName=None, ComponentName=None, NewComponentName=None, ResourceList=None):
    """
    Updates the custom component name and/or the list of resources that make up the component.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_component(
        ResourceGroupName='string',
        ComponentName='string',
        NewComponentName='string',
        ResourceList=[
            'string',
        ]
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type ComponentName: string
    :param ComponentName: [REQUIRED]\nThe name of the component.\n

    :type NewComponentName: string
    :param NewComponentName: The new name of the component.

    :type ResourceList: list
    :param ResourceList: The list of resource ARNs that belong to the component.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationInsights.Client.exceptions.ResourceInUseException
ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_component_configuration(ResourceGroupName=None, ComponentName=None, Monitor=None, Tier=None, ComponentConfiguration=None):
    """
    Updates the monitoring configurations for the component. The configuration input parameter is an escaped JSON of the configuration and should match the schema of what is returned by DescribeComponentConfigurationRecommendation .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_component_configuration(
        ResourceGroupName='string',
        ComponentName='string',
        Monitor=True|False,
        Tier='DEFAULT'|'DOT_NET_CORE'|'DOT_NET_WORKER'|'DOT_NET_WEB'|'SQL_SERVER',
        ComponentConfiguration='string'
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type ComponentName: string
    :param ComponentName: [REQUIRED]\nThe name of the component.\n

    :type Monitor: boolean
    :param Monitor: Indicates whether the application component is monitored.

    :type Tier: string
    :param Tier: The tier of the application component. Supported tiers include DOT_NET_WORKER , DOT_NET_WEB , DOT_NET_CORE , SQL_SERVER , and DEFAULT .

    :type ComponentConfiguration: string
    :param ComponentConfiguration: The configuration settings of the component. The value is the escaped JSON of the configuration. For more information about the JSON format, see Working with JSON . You can send a request to DescribeComponentConfigurationRecommendation to see the recommended configuration for a component. For the complete format of the component configuration file, see Component Configuration .

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_log_pattern(ResourceGroupName=None, PatternSetName=None, PatternName=None, Pattern=None, Rank=None):
    """
    Adds a log pattern to a LogPatternSet .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_log_pattern(
        ResourceGroupName='string',
        PatternSetName='string',
        PatternName='string',
        Pattern='string',
        Rank=123
    )
    
    
    :type ResourceGroupName: string
    :param ResourceGroupName: [REQUIRED]\nThe name of the resource group.\n

    :type PatternSetName: string
    :param PatternSetName: [REQUIRED]\nThe name of the log pattern set.\n

    :type PatternName: string
    :param PatternName: [REQUIRED]\nThe name of the log pattern.\n

    :type Pattern: string
    :param Pattern: The log pattern.

    :type Rank: integer
    :param Rank: Rank of the log pattern.

    :rtype: dict

ReturnsResponse Syntax
{
    'ResourceGroupName': 'string',
    'LogPattern': {
        'PatternSetName': 'string',
        'PatternName': 'string',
        'Pattern': 'string',
        'Rank': 123
    }
}


Response Structure

(dict) --

ResourceGroupName (string) --
The name of the resource group.

LogPattern (dict) --
The successfully created log pattern.

PatternSetName (string) --
The name of the log pattern. A log pattern name can contains at many as 30 characters, and it cannot be empty. The characters can be Unicode letters, digits or one of the following symbols: period, dash, underscore.

PatternName (string) --
The name of the log pattern. A log pattern name can contains at many as 50 characters, and it cannot be empty. The characters can be Unicode letters, digits or one of the following symbols: period, dash, underscore.

Pattern (string) --
A regular expression that defines the log pattern. A log pattern can contains at many as 50 characters, and it cannot be empty.

Rank (integer) --
Rank of the log pattern.









Exceptions

ApplicationInsights.Client.exceptions.ResourceInUseException
ApplicationInsights.Client.exceptions.ResourceNotFoundException
ApplicationInsights.Client.exceptions.ValidationException
ApplicationInsights.Client.exceptions.InternalServerException


    :return: {
        'ResourceGroupName': 'string',
        'LogPattern': {
            'PatternSetName': 'string',
            'PatternName': 'string',
            'Pattern': 'string',
            'Rank': 123
        }
    }
    
    
    :returns: 
    ApplicationInsights.Client.exceptions.ResourceInUseException
    ApplicationInsights.Client.exceptions.ResourceNotFoundException
    ApplicationInsights.Client.exceptions.ValidationException
    ApplicationInsights.Client.exceptions.InternalServerException
    
    """
    pass

