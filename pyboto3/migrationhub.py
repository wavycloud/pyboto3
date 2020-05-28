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

def associate_created_artifact(ProgressUpdateStream=None, MigrationTaskName=None, CreatedArtifact=None, DryRun=None):
    """
    Associates a created artifact of an AWS cloud resource, the target receiving the migration, with the migration task performed by a migration tool. This API has the following traits:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_created_artifact(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        CreatedArtifact={
            'Name': 'string',
            'Description': 'string'
        },
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]\nThe name of the ProgressUpdateStream.\n

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]\nUnique identifier that references the migration task. Do not store personal data in this field.\n

    :type CreatedArtifact: dict
    :param CreatedArtifact: [REQUIRED]\nAn ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)\n\nName (string) -- [REQUIRED]An ARN that uniquely identifies the result of a migration task.\n\nDescription (string) --A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.\n\n\n

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.DryRunOperation
MigrationHub.Client.exceptions.UnauthorizedOperation
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {}
    
    
    :returns: 
    ProgressUpdateStream (string) -- [REQUIRED]
    The name of the ProgressUpdateStream.
    
    MigrationTaskName (string) -- [REQUIRED]
    Unique identifier that references the migration task. Do not store personal data in this field.
    
    CreatedArtifact (dict) -- [REQUIRED]
    An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)
    
    Name (string) -- [REQUIRED]An ARN that uniquely identifies the result of a migration task.
    
    Description (string) --A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.
    
    
    
    DryRun (boolean) -- Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
    
    """
    pass

def associate_discovered_resource(ProgressUpdateStream=None, MigrationTaskName=None, DiscoveredResource=None, DryRun=None):
    """
    Associates a discovered resource ID from Application Discovery Service with a migration task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_discovered_resource(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        DiscoveredResource={
            'ConfigurationId': 'string',
            'Description': 'string'
        },
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]\nThe name of the ProgressUpdateStream.\n

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]\nThe identifier given to the MigrationTask. Do not store personal data in this field.\n

    :type DiscoveredResource: dict
    :param DiscoveredResource: [REQUIRED]\nObject representing a Resource.\n\nConfigurationId (string) -- [REQUIRED]The configurationId in Application Discovery Service that uniquely identifies the on-premise resource.\n\nDescription (string) --A description that can be free-form text to record additional detail about the discovered resource for clarity or later reference.\n\n\n

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.DryRunOperation
MigrationHub.Client.exceptions.UnauthorizedOperation
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.PolicyErrorException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


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

def create_progress_update_stream(ProgressUpdateStreamName=None, DryRun=None):
    """
    Creates a progress update stream which is an AWS resource used for access control as well as a namespace for migration task names that is implicitly linked to your AWS account. It must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_progress_update_stream(
        ProgressUpdateStreamName='string',
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStreamName: string
    :param ProgressUpdateStreamName: [REQUIRED]\nThe name of the ProgressUpdateStream. Do not store personal data in this field.\n

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.DryRunOperation
MigrationHub.Client.exceptions.UnauthorizedOperation
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_progress_update_stream(ProgressUpdateStreamName=None, DryRun=None):
    """
    Deletes a progress update stream, including all of its tasks, which was previously created as an AWS resource used for access control. This API has the following traits:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_progress_update_stream(
        ProgressUpdateStreamName='string',
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStreamName: string
    :param ProgressUpdateStreamName: [REQUIRED]\nThe name of the ProgressUpdateStream. Do not store personal data in this field.\n

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.DryRunOperation
MigrationHub.Client.exceptions.UnauthorizedOperation
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {}
    
    
    :returns: 
    ProgressUpdateStreamName (string) -- [REQUIRED]
    The name of the ProgressUpdateStream. Do not store personal data in this field.
    
    DryRun (boolean) -- Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
    
    """
    pass

def describe_application_state(ApplicationId=None):
    """
    Gets the migration status of an application.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_application_state(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe configurationId in Application Discovery Service that uniquely identifies the grouped application.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ApplicationStatus': 'NOT_STARTED'|'IN_PROGRESS'|'COMPLETED',
    'LastUpdatedTime': datetime(2015, 1, 1)
}


Response Structure

(dict) --
ApplicationStatus (string) --Status of the application - Not Started, In-Progress, Complete.

LastUpdatedTime (datetime) --The timestamp when the application status was last updated.






Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.PolicyErrorException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {
        'ApplicationStatus': 'NOT_STARTED'|'IN_PROGRESS'|'COMPLETED',
        'LastUpdatedTime': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_migration_task(ProgressUpdateStream=None, MigrationTaskName=None):
    """
    Retrieves a list of all attributes associated with a specific migration task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_migration_task(
        ProgressUpdateStream='string',
        MigrationTaskName='string'
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]\nThe name of the ProgressUpdateStream.\n

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]\nThe identifier given to the MigrationTask. Do not store personal data in this field.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'MigrationTask': {
        'ProgressUpdateStream': 'string',
        'MigrationTaskName': 'string',
        'Task': {
            'Status': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'StatusDetail': 'string',
            'ProgressPercent': 123
        },
        'UpdateDateTime': datetime(2015, 1, 1),
        'ResourceAttributeList': [
            {
                'Type': 'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MAC_ADDRESS'|'FQDN'|'VM_MANAGER_ID'|'VM_MANAGED_OBJECT_REFERENCE'|'VM_NAME'|'VM_PATH'|'BIOS_ID'|'MOTHERBOARD_SERIAL_NUMBER',
                'Value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

MigrationTask (dict) --
Object encapsulating information about the migration task.

ProgressUpdateStream (string) --
A name that identifies the vendor of the migration tool being used.

MigrationTaskName (string) --
Unique identifier that references the migration task. Do not store personal data in this field.

Task (dict) --
Task object encapsulating task information.

Status (string) --
Status of the task - Not Started, In-Progress, Complete.

StatusDetail (string) --
Details of task status as notified by a migration tool. A tool might use this field to provide clarifying information about the status that is unique to that tool or that explains an error state.

ProgressPercent (integer) --
Indication of the percentage completion of the task.



UpdateDateTime (datetime) --
The timestamp when the task was gathered.

ResourceAttributeList (list) --
Information about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service repository.

(dict) --
Attribute associated with a resource.
Note the corresponding format required per type listed below:


IPV4

x.x.x.x
where x is an integer in the range [0,255]

IPV6

y : y : y : y : y : y : y : y
where y is a hexadecimal between 0 and FFFF. [0, FFFF]

MAC_ADDRESS

^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$

FQDN

^[^<>{}\\\\\\\\/?,=\\\\p{Cntrl}]{1,256}$


Type (string) --
Type of resource.

Value (string) --
Value of the resource type.













Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {
        'MigrationTask': {
            'ProgressUpdateStream': 'string',
            'MigrationTaskName': 'string',
            'Task': {
                'Status': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
                'StatusDetail': 'string',
                'ProgressPercent': 123
            },
            'UpdateDateTime': datetime(2015, 1, 1),
            'ResourceAttributeList': [
                {
                    'Type': 'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MAC_ADDRESS'|'FQDN'|'VM_MANAGER_ID'|'VM_MANAGED_OBJECT_REFERENCE'|'VM_NAME'|'VM_PATH'|'BIOS_ID'|'MOTHERBOARD_SERIAL_NUMBER',
                    'Value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    MigrationHub.Client.exceptions.AccessDeniedException
    MigrationHub.Client.exceptions.ThrottlingException
    MigrationHub.Client.exceptions.InternalServerError
    MigrationHub.Client.exceptions.ServiceUnavailableException
    MigrationHub.Client.exceptions.InvalidInputException
    MigrationHub.Client.exceptions.ResourceNotFoundException
    MigrationHub.Client.exceptions.HomeRegionNotSetException
    
    """
    pass

def disassociate_created_artifact(ProgressUpdateStream=None, MigrationTaskName=None, CreatedArtifactName=None, DryRun=None):
    """
    Disassociates a created artifact of an AWS resource with a migration task performed by a migration tool that was previously associated. This API has the following traits:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_created_artifact(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        CreatedArtifactName='string',
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]\nThe name of the ProgressUpdateStream.\n

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]\nUnique identifier that references the migration task to be disassociated with the artifact. Do not store personal data in this field.\n

    :type CreatedArtifactName: string
    :param CreatedArtifactName: [REQUIRED]\nAn ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)\n

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.DryRunOperation
MigrationHub.Client.exceptions.UnauthorizedOperation
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {}
    
    
    :returns: 
    ProgressUpdateStream (string) -- [REQUIRED]
    The name of the ProgressUpdateStream.
    
    MigrationTaskName (string) -- [REQUIRED]
    Unique identifier that references the migration task to be disassociated with the artifact. Do not store personal data in this field.
    
    CreatedArtifactName (string) -- [REQUIRED]
    An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)
    
    DryRun (boolean) -- Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
    
    """
    pass

def disassociate_discovered_resource(ProgressUpdateStream=None, MigrationTaskName=None, ConfigurationId=None, DryRun=None):
    """
    Disassociate an Application Discovery Service discovered resource from a migration task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_discovered_resource(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        ConfigurationId='string',
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]\nThe name of the ProgressUpdateStream.\n

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]\nThe identifier given to the MigrationTask. Do not store personal data in this field.\n

    :type ConfigurationId: string
    :param ConfigurationId: [REQUIRED]\nConfigurationId of the Application Discovery Service resource to be disassociated.\n

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.DryRunOperation
MigrationHub.Client.exceptions.UnauthorizedOperation
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


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

def import_migration_task(ProgressUpdateStream=None, MigrationTaskName=None, DryRun=None):
    """
    Registers a new migration task which represents a server, database, etc., being migrated to AWS by a migration tool.
    This API is a prerequisite to calling the NotifyMigrationTaskState API as the migration tool must first register the migration task with Migration Hub.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.import_migration_task(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]\nThe name of the ProgressUpdateStream. >\n

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]\nUnique identifier that references the migration task. Do not store personal data in this field.\n

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.DryRunOperation
MigrationHub.Client.exceptions.UnauthorizedOperation
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def list_application_states(ApplicationIds=None, NextToken=None, MaxResults=None):
    """
    Lists all the migration statuses for your applications. If you use the optional ApplicationIds parameter, only the migration statuses for those applications will be returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_application_states(
        ApplicationIds=[
            'string',
        ],
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ApplicationIds: list
    :param ApplicationIds: The configurationIds from the Application Discovery Service that uniquely identifies your applications.\n\n(string) --\n\n

    :type NextToken: string
    :param NextToken: If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to be returned per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'ApplicationStateList': [
        {
            'ApplicationId': 'string',
            'ApplicationStatus': 'NOT_STARTED'|'IN_PROGRESS'|'COMPLETED',
            'LastUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ApplicationStateList (list) --
A list of Applications that exist in Application Discovery Service.

(dict) --
The state of an application discovered through Migration Hub import, the AWS Agentless Discovery Connector, or the AWS Application Discovery Agent.

ApplicationId (string) --
The configurationId from the Application Discovery Service that uniquely identifies an application.

ApplicationStatus (string) --
The current status of an application.

LastUpdatedTime (datetime) --
The timestamp when the application status was last updated.





NextToken (string) --
If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .







Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {
        'ApplicationStateList': [
            {
                'ApplicationId': 'string',
                'ApplicationStatus': 'NOT_STARTED'|'IN_PROGRESS'|'COMPLETED',
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    MigrationHub.Client.exceptions.AccessDeniedException
    MigrationHub.Client.exceptions.ThrottlingException
    MigrationHub.Client.exceptions.InternalServerError
    MigrationHub.Client.exceptions.ServiceUnavailableException
    MigrationHub.Client.exceptions.InvalidInputException
    MigrationHub.Client.exceptions.HomeRegionNotSetException
    
    """
    pass

def list_created_artifacts(ProgressUpdateStream=None, MigrationTaskName=None, NextToken=None, MaxResults=None):
    """
    Lists the created artifacts attached to a given migration task in an update stream. This API has the following traits:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_created_artifacts(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]\nThe name of the ProgressUpdateStream.\n

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]\nUnique identifier that references the migration task. Do not store personal data in this field.\n

    :type NextToken: string
    :param NextToken: If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to be returned per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'CreatedArtifactList': [
        {
            'Name': 'string',
            'Description': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If there are more created artifacts than the max result, return the next token to be passed to the next call as a bookmark of where to start from.

CreatedArtifactList (list) --
List of created artifacts up to the maximum number of results specified in the request.

(dict) --
An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance, RDS instance, etc.).

Name (string) --
An ARN that uniquely identifies the result of a migration task.

Description (string) --
A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.











Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {
        'NextToken': 'string',
        'CreatedArtifactList': [
            {
                'Name': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    :returns: 
    ProgressUpdateStream (string) -- [REQUIRED]
    The name of the ProgressUpdateStream.
    
    MigrationTaskName (string) -- [REQUIRED]
    Unique identifier that references the migration task. Do not store personal data in this field.
    
    NextToken (string) -- If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .
    MaxResults (integer) -- Maximum number of results to be returned per page.
    
    """
    pass

def list_discovered_resources(ProgressUpdateStream=None, MigrationTaskName=None, NextToken=None, MaxResults=None):
    """
    Lists discovered resources associated with the given MigrationTask .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_discovered_resources(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]\nThe name of the ProgressUpdateStream.\n

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]\nThe name of the MigrationTask. Do not store personal data in this field.\n

    :type NextToken: string
    :param NextToken: If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results returned per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'DiscoveredResourceList': [
        {
            'ConfigurationId': 'string',
            'Description': 'string'
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If there are more discovered resources than the max result, return the next token to be passed to the next call as a bookmark of where to start from.

DiscoveredResourceList (list) --
Returned list of discovered resources associated with the given MigrationTask.

(dict) --
Object representing the on-premises resource being migrated.

ConfigurationId (string) --
The configurationId in Application Discovery Service that uniquely identifies the on-premise resource.

Description (string) --
A description that can be free-form text to record additional detail about the discovered resource for clarity or later reference.











Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {
        'NextToken': 'string',
        'DiscoveredResourceList': [
            {
                'ConfigurationId': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    :returns: 
    MigrationHub.Client.exceptions.AccessDeniedException
    MigrationHub.Client.exceptions.ThrottlingException
    MigrationHub.Client.exceptions.InternalServerError
    MigrationHub.Client.exceptions.ServiceUnavailableException
    MigrationHub.Client.exceptions.InvalidInputException
    MigrationHub.Client.exceptions.ResourceNotFoundException
    MigrationHub.Client.exceptions.HomeRegionNotSetException
    
    """
    pass

def list_migration_tasks(NextToken=None, MaxResults=None, ResourceName=None):
    """
    Lists all, or filtered by resource name, migration tasks associated with the user account making this call. This API has the following traits:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_migration_tasks(
        NextToken='string',
        MaxResults=123,
        ResourceName='string'
    )
    
    
    :type NextToken: string
    :param NextToken: If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .

    :type MaxResults: integer
    :param MaxResults: Value to specify how many results are returned per page.

    :type ResourceName: string
    :param ResourceName: Filter migration tasks by discovered resource name.

    :rtype: dict

ReturnsResponse Syntax
{
    'NextToken': 'string',
    'MigrationTaskSummaryList': [
        {
            'ProgressUpdateStream': 'string',
            'MigrationTaskName': 'string',
            'Status': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'ProgressPercent': 123,
            'StatusDetail': 'string',
            'UpdateDateTime': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

NextToken (string) --
If there are more migration tasks than the max result, return the next token to be passed to the next call as a bookmark of where to start from.

MigrationTaskSummaryList (list) --
Lists the migration task\'s summary which includes: MigrationTaskName , ProgressPercent , ProgressUpdateStream , Status , and the UpdateDateTime for each task.

(dict) --
MigrationTaskSummary includes MigrationTaskName , ProgressPercent , ProgressUpdateStream , Status , and UpdateDateTime for each task.

ProgressUpdateStream (string) --
An AWS resource used for access control. It should uniquely identify the migration tool as it is used for all updates made by the tool.

MigrationTaskName (string) --
Unique identifier that references the migration task. Do not store personal data in this field.

Status (string) --
Status of the task.

ProgressPercent (integer) --
Indication of the percentage completion of the task.

StatusDetail (string) --
Detail information of what is being done within the overall status state.

UpdateDateTime (datetime) --
The timestamp when the task was gathered.











Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.PolicyErrorException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {
        'NextToken': 'string',
        'MigrationTaskSummaryList': [
            {
                'ProgressUpdateStream': 'string',
                'MigrationTaskName': 'string',
                'Status': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
                'ProgressPercent': 123,
                'StatusDetail': 'string',
                'UpdateDateTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    NextToken (string) -- If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .
    MaxResults (integer) -- Value to specify how many results are returned per page.
    ResourceName (string) -- Filter migration tasks by discovered resource name.
    
    """
    pass

def list_progress_update_streams(NextToken=None, MaxResults=None):
    """
    Lists progress update streams associated with the user account making this call.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_progress_update_streams(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .

    :type MaxResults: integer
    :param MaxResults: Filter to limit the maximum number of results to list per page.

    :rtype: dict

ReturnsResponse Syntax
{
    'ProgressUpdateStreamSummaryList': [
        {
            'ProgressUpdateStreamName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

ProgressUpdateStreamSummaryList (list) --
List of progress update streams up to the max number of results passed in the input.

(dict) --
Summary of the AWS resource used for access control that is implicitly linked to your AWS account.

ProgressUpdateStreamName (string) --
The name of the ProgressUpdateStream. Do not store personal data in this field.





NextToken (string) --
If there are more streams created than the max result, return the next token to be passed to the next call as a bookmark of where to start from.







Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {
        'ProgressUpdateStreamSummaryList': [
            {
                'ProgressUpdateStreamName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    MigrationHub.Client.exceptions.AccessDeniedException
    MigrationHub.Client.exceptions.ThrottlingException
    MigrationHub.Client.exceptions.InternalServerError
    MigrationHub.Client.exceptions.ServiceUnavailableException
    MigrationHub.Client.exceptions.InvalidInputException
    MigrationHub.Client.exceptions.HomeRegionNotSetException
    
    """
    pass

def notify_application_state(ApplicationId=None, Status=None, UpdateDateTime=None, DryRun=None):
    """
    Sets the migration state of an application. For a given application identified by the value passed to ApplicationId , its status is set or updated by passing one of three values to Status : NOT_STARTED | IN_PROGRESS | COMPLETED .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.notify_application_state(
        ApplicationId='string',
        Status='NOT_STARTED'|'IN_PROGRESS'|'COMPLETED',
        UpdateDateTime=datetime(2015, 1, 1),
        DryRun=True|False
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]\nThe configurationId in Application Discovery Service that uniquely identifies the grouped application.\n

    :type Status: string
    :param Status: [REQUIRED]\nStatus of the application - Not Started, In-Progress, Complete.\n

    :type UpdateDateTime: datetime
    :param UpdateDateTime: The timestamp when the application state changed.

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.DryRunOperation
MigrationHub.Client.exceptions.UnauthorizedOperation
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.PolicyErrorException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def notify_migration_task_state(ProgressUpdateStream=None, MigrationTaskName=None, Task=None, UpdateDateTime=None, NextUpdateSeconds=None, DryRun=None):
    """
    Notifies Migration Hub of the current status, progress, or other detail regarding a migration task. This API has the following traits:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.notify_migration_task_state(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        Task={
            'Status': 'NOT_STARTED'|'IN_PROGRESS'|'FAILED'|'COMPLETED',
            'StatusDetail': 'string',
            'ProgressPercent': 123
        },
        UpdateDateTime=datetime(2015, 1, 1),
        NextUpdateSeconds=123,
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]\nThe name of the ProgressUpdateStream.\n

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]\nUnique identifier that references the migration task. Do not store personal data in this field.\n

    :type Task: dict
    :param Task: [REQUIRED]\nInformation about the task\'s progress and status.\n\nStatus (string) -- [REQUIRED]Status of the task - Not Started, In-Progress, Complete.\n\nStatusDetail (string) --Details of task status as notified by a migration tool. A tool might use this field to provide clarifying information about the status that is unique to that tool or that explains an error state.\n\nProgressPercent (integer) --Indication of the percentage completion of the task.\n\n\n

    :type UpdateDateTime: datetime
    :param UpdateDateTime: [REQUIRED]\nThe timestamp when the task was gathered.\n

    :type NextUpdateSeconds: integer
    :param NextUpdateSeconds: [REQUIRED]\nNumber of seconds after the UpdateDateTime within which the Migration Hub can expect an update. If Migration Hub does not receive an update within the specified interval, then the migration task will be considered stale.\n

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.DryRunOperation
MigrationHub.Client.exceptions.UnauthorizedOperation
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {}
    
    
    :returns: 
    ProgressUpdateStream (string) -- [REQUIRED]
    The name of the ProgressUpdateStream.
    
    MigrationTaskName (string) -- [REQUIRED]
    Unique identifier that references the migration task. Do not store personal data in this field.
    
    Task (dict) -- [REQUIRED]
    Information about the task\'s progress and status.
    
    Status (string) -- [REQUIRED]Status of the task - Not Started, In-Progress, Complete.
    
    StatusDetail (string) --Details of task status as notified by a migration tool. A tool might use this field to provide clarifying information about the status that is unique to that tool or that explains an error state.
    
    ProgressPercent (integer) --Indication of the percentage completion of the task.
    
    
    
    UpdateDateTime (datetime) -- [REQUIRED]
    The timestamp when the task was gathered.
    
    NextUpdateSeconds (integer) -- [REQUIRED]
    Number of seconds after the UpdateDateTime within which the Migration Hub can expect an update. If Migration Hub does not receive an update within the specified interval, then the migration task will be considered stale.
    
    DryRun (boolean) -- Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
    
    """
    pass

def put_resource_attributes(ProgressUpdateStream=None, MigrationTaskName=None, ResourceAttributeList=None, DryRun=None):
    """
    Provides identifying details of the resource being migrated so that it can be associated in the Application Discovery Service repository. This association occurs asynchronously after PutResourceAttributes returns.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_resource_attributes(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        ResourceAttributeList=[
            {
                'Type': 'IPV4_ADDRESS'|'IPV6_ADDRESS'|'MAC_ADDRESS'|'FQDN'|'VM_MANAGER_ID'|'VM_MANAGED_OBJECT_REFERENCE'|'VM_NAME'|'VM_PATH'|'BIOS_ID'|'MOTHERBOARD_SERIAL_NUMBER',
                'Value': 'string'
            },
        ],
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]\nThe name of the ProgressUpdateStream.\n

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]\nUnique identifier that references the migration task. Do not store personal data in this field.\n

    :type ResourceAttributeList: list
    :param ResourceAttributeList: [REQUIRED]\nInformation about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service repository.\n\nNote\nTakes the object array of ResourceAttribute where the Type field is reserved for the following values: IPV4_ADDRESS | IPV6_ADDRESS | MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER where the identifying value can be a string up to 256 characters.\n\n\nWarning\n\nIf any 'VM' related value is set for a ResourceAttribute object, it is required that VM_MANAGER_ID , as a minimum, is always set. If VM_MANAGER_ID is not set, then all 'VM' fields will be discarded and 'VM' fields will not be used for matching the migration task to a server in Application Discovery Service repository. See the Example section below for a use case of specifying 'VM' related values.\nIf a server you are trying to match has multiple IP or MAC addresses, you should provide as many as you know in separate type/value pairs passed to the ResourceAttributeList parameter to maximize the chances of matching.\n\n\n\n(dict) --Attribute associated with a resource.\nNote the corresponding format required per type listed below:\n\n\nIPV4\nx.x.x.x\nwhere x is an integer in the range [0,255]\n\nIPV6\ny : y : y : y : y : y : y : y\nwhere y is a hexadecimal between 0 and FFFF. [0, FFFF]\n\nMAC_ADDRESS\n^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$\n\nFQDN\n^[^<>{}\\\\\\\\/?,=\\\\p{Cntrl}]{1,256}$\n\n\nType (string) -- [REQUIRED]Type of resource.\n\nValue (string) -- [REQUIRED]Value of the resource type.\n\n\n\n\n

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

MigrationHub.Client.exceptions.AccessDeniedException
MigrationHub.Client.exceptions.ThrottlingException
MigrationHub.Client.exceptions.InternalServerError
MigrationHub.Client.exceptions.ServiceUnavailableException
MigrationHub.Client.exceptions.DryRunOperation
MigrationHub.Client.exceptions.UnauthorizedOperation
MigrationHub.Client.exceptions.InvalidInputException
MigrationHub.Client.exceptions.ResourceNotFoundException
MigrationHub.Client.exceptions.HomeRegionNotSetException


    :return: {}
    
    
    :returns: 
    ProgressUpdateStream (string) -- [REQUIRED]
    The name of the ProgressUpdateStream.
    
    MigrationTaskName (string) -- [REQUIRED]
    Unique identifier that references the migration task. Do not store personal data in this field.
    
    ResourceAttributeList (list) -- [REQUIRED]
    Information about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service repository.
    
    Note
    Takes the object array of ResourceAttribute where the Type field is reserved for the following values: IPV4_ADDRESS | IPV6_ADDRESS | MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER where the identifying value can be a string up to 256 characters.
    
    
    Warning
    
    If any "VM" related value is set for a ResourceAttribute object, it is required that VM_MANAGER_ID , as a minimum, is always set. If VM_MANAGER_ID is not set, then all "VM" fields will be discarded and "VM" fields will not be used for matching the migration task to a server in Application Discovery Service repository. See the Example section below for a use case of specifying "VM" related values.
    If a server you are trying to match has multiple IP or MAC addresses, you should provide as many as you know in separate type/value pairs passed to the ResourceAttributeList parameter to maximize the chances of matching.
    
    
    
    (dict) --Attribute associated with a resource.
    Note the corresponding format required per type listed below:
    
    
    IPV4
    x.x.x.x
    where x is an integer in the range [0,255]
    
    IPV6
    y : y : y : y : y : y : y : y
    where y is a hexadecimal between 0 and FFFF. [0, FFFF]
    
    MAC_ADDRESS
    ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$
    
    FQDN
    ^[^<>{}\\\\\\\\/?,=\\\\p{Cntrl}]{1,256}$
    
    
    Type (string) -- [REQUIRED]Type of resource.
    
    Value (string) -- [REQUIRED]Value of the resource type.
    
    
    
    
    
    DryRun (boolean) -- Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
    
    """
    pass

