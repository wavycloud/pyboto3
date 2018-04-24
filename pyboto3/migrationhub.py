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
    :param ProgressUpdateStream: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]
            Unique identifier that references the migration task.
            

    :type CreatedArtifact: dict
    :param CreatedArtifact: [REQUIRED]
            An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)
            Name (string) -- [REQUIRED]An ARN that uniquely identifies the result of a migration task.
            Description (string) --A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.
            

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    ProgressUpdateStream (string) -- [REQUIRED]
    The name of the ProgressUpdateStream.
    
    MigrationTaskName (string) -- [REQUIRED]
    Unique identifier that references the migration task.
    
    CreatedArtifact (dict) -- [REQUIRED]
    An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)
    
    Name (string) -- [REQUIRED]An ARN that uniquely identifies the result of a migration task.
    
    Description (string) --A description that can be free-form text to record additional detail about the artifact for clarity or for later reference.
    
    
    
    DryRun (boolean) -- Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
    
    """
    pass

def associate_discovered_resource(ProgressUpdateStream=None, MigrationTaskName=None, DiscoveredResource=None, DryRun=None):
    """
    Associates a discovered resource ID from Application Discovery Service (ADS) with a migration task.
    See also: AWS API Documentation
    
    
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
    :param ProgressUpdateStream: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]
            The identifier given to the MigrationTask.
            

    :type DiscoveredResource: dict
    :param DiscoveredResource: [REQUIRED]
            Object representing a Resource.
            ConfigurationId (string) -- [REQUIRED]The configurationId in ADS that uniquely identifies the on-premise resource.
            Description (string) --A description that can be free-form text to record additional detail about the discovered resource for clarity or later reference.
            

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
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

def create_progress_update_stream(ProgressUpdateStreamName=None, DryRun=None):
    """
    Creates a progress update stream which is an AWS resource used for access control as well as a namespace for migration task names that is implicitly linked to your AWS account. It must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.
    See also: AWS API Documentation
    
    
    :example: response = client.create_progress_update_stream(
        ProgressUpdateStreamName='string',
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStreamName: string
    :param ProgressUpdateStreamName: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_progress_update_stream(ProgressUpdateStreamName=None, DryRun=None):
    """
    Deletes a progress update stream, including all of its tasks, which was previously created as an AWS resource used for access control. This API has the following traits:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_progress_update_stream(
        ProgressUpdateStreamName='string',
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStreamName: string
    :param ProgressUpdateStreamName: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    ProgressUpdateStreamName (string) -- [REQUIRED]
    The name of the ProgressUpdateStream.
    
    DryRun (boolean) -- Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
    
    """
    pass

def describe_application_state(ApplicationId=None):
    """
    Gets the migration status of an application.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_application_state(
        ApplicationId='string'
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The configurationId in ADS that uniquely identifies the grouped application.
            

    :rtype: dict
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
    
    
    :example: response = client.describe_migration_task(
        ProgressUpdateStream='string',
        MigrationTaskName='string'
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]
            The identifier given to the MigrationTask.
            

    :rtype: dict
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
    
    
    """
    pass

def disassociate_created_artifact(ProgressUpdateStream=None, MigrationTaskName=None, CreatedArtifactName=None, DryRun=None):
    """
    Disassociates a created artifact of an AWS resource with a migration task performed by a migration tool that was previously associated. This API has the following traits:
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_created_artifact(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        CreatedArtifactName='string',
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]
            Unique identifier that references the migration task to be disassociated with the artifact.
            

    :type CreatedArtifactName: string
    :param CreatedArtifactName: [REQUIRED]
            An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)
            

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    ProgressUpdateStream (string) -- [REQUIRED]
    The name of the ProgressUpdateStream.
    
    MigrationTaskName (string) -- [REQUIRED]
    Unique identifier that references the migration task to be disassociated with the artifact.
    
    CreatedArtifactName (string) -- [REQUIRED]
    An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)
    
    DryRun (boolean) -- Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
    
    """
    pass

def disassociate_discovered_resource(ProgressUpdateStream=None, MigrationTaskName=None, ConfigurationId=None, DryRun=None):
    """
    Disassociate an Application Discovery Service (ADS) discovered resource from a migration task.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_discovered_resource(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        ConfigurationId='string',
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]
            The identifier given to the MigrationTask.
            

    :type ConfigurationId: string
    :param ConfigurationId: [REQUIRED]
            ConfigurationId of the ADS resource to be disassociated.
            

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict
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

def import_migration_task(ProgressUpdateStream=None, MigrationTaskName=None, DryRun=None):
    """
    Registers a new migration task which represents a server, database, etc., being migrated to AWS by a migration tool.
    This API is a prerequisite to calling the NotifyMigrationTaskState API as the migration tool must first register the migration task with Migration Hub.
    See also: AWS API Documentation
    
    
    :example: response = client.import_migration_task(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        DryRun=True|False
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]
            Unique identifier that references the migration task.
            

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def list_created_artifacts(ProgressUpdateStream=None, MigrationTaskName=None, NextToken=None, MaxResults=None):
    """
    Lists the created artifacts attached to a given migration task in an update stream. This API has the following traits:
    See also: AWS API Documentation
    
    
    :example: response = client.list_created_artifacts(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]
            Unique identifier that references the migration task.
            

    :type NextToken: string
    :param NextToken: If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .

    :type MaxResults: integer
    :param MaxResults: Maximum number of results to be returned per page.

    :rtype: dict
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
    Unique identifier that references the migration task.
    
    NextToken (string) -- If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .
    MaxResults (integer) -- Maximum number of results to be returned per page.
    
    """
    pass

def list_discovered_resources(ProgressUpdateStream=None, MigrationTaskName=None, NextToken=None, MaxResults=None):
    """
    Lists discovered resources associated with the given MigrationTask .
    See also: AWS API Documentation
    
    
    :example: response = client.list_discovered_resources(
        ProgressUpdateStream='string',
        MigrationTaskName='string',
        NextToken='string',
        MaxResults=123
    )
    
    
    :type ProgressUpdateStream: string
    :param ProgressUpdateStream: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]
            The name of the MigrationTask.
            

    :type NextToken: string
    :param NextToken: If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .

    :type MaxResults: integer
    :param MaxResults: The maximum number of results returned per page.

    :rtype: dict
    :return: {
        'NextToken': 'string',
        'DiscoveredResourceList': [
            {
                'ConfigurationId': 'string',
                'Description': 'string'
            },
        ]
    }
    
    
    """
    pass

def list_migration_tasks(NextToken=None, MaxResults=None, ResourceName=None):
    """
    Lists all, or filtered by resource name, migration tasks associated with the user account making this call. This API has the following traits:
    See also: AWS API Documentation
    
    
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
    
    
    :example: response = client.list_progress_update_streams(
        NextToken='string',
        MaxResults=123
    )
    
    
    :type NextToken: string
    :param NextToken: If a NextToken was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in NextToken .

    :type MaxResults: integer
    :param MaxResults: Filter to limit the maximum number of results to list per page.

    :rtype: dict
    :return: {
        'ProgressUpdateStreamSummaryList': [
            {
                'ProgressUpdateStreamName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def notify_application_state(ApplicationId=None, Status=None, DryRun=None):
    """
    Sets the migration state of an application. For a given application identified by the value passed to ApplicationId , its status is set or updated by passing one of three values to Status : NOT_STARTED | IN_PROGRESS | COMPLETED .
    See also: AWS API Documentation
    
    
    :example: response = client.notify_application_state(
        ApplicationId='string',
        Status='NOT_STARTED'|'IN_PROGRESS'|'COMPLETED',
        DryRun=True|False
    )
    
    
    :type ApplicationId: string
    :param ApplicationId: [REQUIRED]
            The configurationId in ADS that uniquely identifies the grouped application.
            

    :type Status: string
    :param Status: [REQUIRED]
            Status of the application - Not Started, In-Progress, Complete.
            

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def notify_migration_task_state(ProgressUpdateStream=None, MigrationTaskName=None, Task=None, UpdateDateTime=None, NextUpdateSeconds=None, DryRun=None):
    """
    Notifies Migration Hub of the current status, progress, or other detail regarding a migration task. This API has the following traits:
    See also: AWS API Documentation
    
    
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
    :param ProgressUpdateStream: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]
            Unique identifier that references the migration task.
            

    :type Task: dict
    :param Task: [REQUIRED]
            Information about the task's progress and status.
            Status (string) -- [REQUIRED]Status of the task - Not Started, In-Progress, Complete.
            StatusDetail (string) --Details of task status as notified by a migration tool. A tool might use this field to provide clarifying information about the status that is unique to that tool or that explains an error state.
            ProgressPercent (integer) --Indication of the percentage completion of the task.
            

    :type UpdateDateTime: datetime
    :param UpdateDateTime: [REQUIRED]
            The timestamp when the task was gathered.
            

    :type NextUpdateSeconds: integer
    :param NextUpdateSeconds: [REQUIRED]
            Number of seconds after the UpdateDateTime within which the Migration Hub can expect an update. If Migration Hub does not receive an update within the specified interval, then the migration task will be considered stale.
            

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    ProgressUpdateStream (string) -- [REQUIRED]
    The name of the ProgressUpdateStream.
    
    MigrationTaskName (string) -- [REQUIRED]
    Unique identifier that references the migration task.
    
    Task (dict) -- [REQUIRED]
    Information about the task's progress and status.
    
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
    Provides identifying details of the resource being migrated so that it can be associated in the Application Discovery Service (ADS)'s repository. This association occurs asynchronously after PutResourceAttributes returns.
    See also: AWS API Documentation
    
    
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
    :param ProgressUpdateStream: [REQUIRED]
            The name of the ProgressUpdateStream.
            

    :type MigrationTaskName: string
    :param MigrationTaskName: [REQUIRED]
            Unique identifier that references the migration task.
            

    :type ResourceAttributeList: list
    :param ResourceAttributeList: [REQUIRED]
            Information about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service (ADS)'s repository.
            Note
            In the ResourceAttribute object array, the Type field is reserved for the following values: IPV4_ADDRESS | IPV6_ADDRESS | MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER , and the identifying value can be a string up to 256 characters.
            Warning
            If any 'VM' related value is used for a ResourceAttribute object, it is required that VM_MANAGER_ID , as a minimum, is always used. If it is not used, the server will not be associated in the Application Discovery Service (ADS)'s repository using any of the other 'VM' related values, and you will experience data loss. See the Example section below for a use case of specifying 'VM' related values.
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
            ^[^{}\\\\/?,=\\p{Cntrl}]{1,256}$
            Type (string) -- [REQUIRED]Type of resource.
            Value (string) -- [REQUIRED]Value of the resource type.
            
            

    :type DryRun: boolean
    :param DryRun: Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    ProgressUpdateStream (string) -- [REQUIRED]
    The name of the ProgressUpdateStream.
    
    MigrationTaskName (string) -- [REQUIRED]
    Unique identifier that references the migration task.
    
    ResourceAttributeList (list) -- [REQUIRED]
    Information about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service (ADS)'s repository.
    
    Note
    In the ResourceAttribute object array, the Type field is reserved for the following values: IPV4_ADDRESS | IPV6_ADDRESS | MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER , and the identifying value can be a string up to 256 characters.
    
    
    Warning
    If any "VM" related value is used for a ResourceAttribute object, it is required that VM_MANAGER_ID , as a minimum, is always used. If it is not used, the server will not be associated in the Application Discovery Service (ADS)'s repository using any of the other "VM" related values, and you will experience data loss. See the Example section below for a use case of specifying "VM" related values.
    
    
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
    ^[^{}\\\\/?,=\\p{Cntrl}]{1,256}$
    
    
    Type (string) -- [REQUIRED]Type of resource.
    
    Value (string) -- [REQUIRED]Value of the resource type.
    
    
    
    
    
    DryRun (boolean) -- Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.
    
    """
    pass

