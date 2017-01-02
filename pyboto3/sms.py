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
    :param operation_name: The operation name. This is the same name
            as the method name on the client. For example, if the
            method name is create_foo, and you'd normally invoke the
            operation as client.create_foo(**kwargs), if the
            create_foo operation can be paginated, you can use the
            call client.get_paginator('create_foo').

    """
    pass

def create_replication_job(serverId=None, seedReplicationTime=None, frequency=None, licenseType=None, roleName=None, description=None):
    """
    The CreateReplicationJob API is used to create a ReplicationJob to replicate a server on AWS. Call this API to first create a ReplicationJob, which will then schedule periodic ReplicationRuns to replicate your server to AWS. Each ReplicationRun will result in the creation of an AWS AMI.
    See also: AWS API Documentation
    
    
    :example: response = client.create_replication_job(
        serverId='string',
        seedReplicationTime=datetime(2015, 1, 1),
        frequency=123,
        licenseType='AWS'|'BYOL',
        roleName='string',
        description='string'
    )
    
    
    :type serverId: string
    :param serverId: [REQUIRED] Unique Identifier for a server

    :type seedReplicationTime: datetime
    :param seedReplicationTime: [REQUIRED] Timestamp of an operation

    :type frequency: integer
    :param frequency: [REQUIRED] Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.

    :type licenseType: string
    :param licenseType: The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.

    :type roleName: string
    :param roleName: Name of service role in customer's account to be used by SMS service.

    :type description: string
    :param description: The description for a Replication Job/Run.

    :rtype: dict
    :return: {
        'replicationJobId': 'string'
    }
    
    
    :returns: 
    (dict) --
    replicationJobId (string) -- The unique identifier for a Replication Job.
    
    
    
    """
    pass

def delete_replication_job(replicationJobId=None):
    """
    The DeleteReplicationJob API is used to delete a ReplicationJob, resulting in no further ReplicationRuns. This will delete the contents of the S3 bucket used to store SMS artifacts, but will not delete any AMIs created by the SMS service.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_replication_job(
        replicationJobId='string'
    )
    
    
    :type replicationJobId: string
    :param replicationJobId: [REQUIRED] The unique identifier for a Replication Job.

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_server_catalog():
    """
    The DeleteServerCatalog API clears all servers from your server catalog. This means that these servers will no longer be accessible to the Server Migration Service.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_server_catalog()
    
    
    :rtype: dict
    :return: {}
    
    
    """
    pass

def disassociate_connector(connectorId=None):
    """
    The DisassociateConnector API will disassociate a connector from the Server Migration Service, rendering it unavailable to support replication jobs.
    See also: AWS API Documentation
    
    
    :example: response = client.disassociate_connector(
        connectorId='string'
    )
    
    
    :type connectorId: string
    :param connectorId: [REQUIRED] Unique Identifier for Connector

    :rtype: dict
    :return: {}
    
    
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

def get_connectors(nextToken=None, maxResults=None):
    """
    The GetConnectors API returns a list of connectors that are registered with the Server Migration Service.
    See also: AWS API Documentation
    
    
    :example: response = client.get_connectors(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: Pagination token to pass as input to API call

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.

    :rtype: dict
    :return: {
        'connectorList': [
            {
                'connectorId': 'string',
                'version': 'string',
                'status': 'HEALTHY'|'UNHEALTHY',
                'capabilityList': [
                    'VSPHERE',
                ],
                'vmManagerName': 'string',
                'vmManagerType': 'VSPHERE',
                'vmManagerId': 'string',
                'ipAddress': 'string',
                'macAddress': 'string',
                'associatedOn': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    connectorList (list) -- List of connectors
    (dict) -- Object representing a Connector
    connectorId (string) -- Unique Identifier for Connector
    version (string) -- Connector version string
    status (string) -- Status of on-premise Connector
    capabilityList (list) -- List of Connector Capabilities
    (string) -- Capabilities for a Connector
    
    
    vmManagerName (string) -- VM Manager Name
    vmManagerType (string) -- VM Management Product
    vmManagerId (string) -- Unique Identifier for VM Manager
    ipAddress (string) -- Internet Protocol (IP) Address
    macAddress (string) -- Hardware (MAC) address
    associatedOn (datetime) -- Timestamp of an operation
    
    
    
    
    nextToken (string) -- Pagination token to pass as input to API call
    
    
    
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

def get_replication_jobs(replicationJobId=None, nextToken=None, maxResults=None):
    """
    The GetReplicationJobs API will return all of your ReplicationJobs and their details. This API returns a paginated list, that may be consecutively called with nextToken to retrieve all ReplicationJobs.
    See also: AWS API Documentation
    
    
    :example: response = client.get_replication_jobs(
        replicationJobId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type replicationJobId: string
    :param replicationJobId: The unique identifier for a Replication Job.

    :type nextToken: string
    :param nextToken: Pagination token to pass as input to API call

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.

    :rtype: dict
    :return: {
        'replicationJobList': [
            {
                'replicationJobId': 'string',
                'serverId': 'string',
                'serverType': 'VIRTUAL_MACHINE',
                'vmServer': {
                    'vmServerAddress': {
                        'vmManagerId': 'string',
                        'vmId': 'string'
                    },
                    'vmName': 'string',
                    'vmManagerName': 'string',
                    'vmManagerType': 'VSPHERE',
                    'vmPath': 'string'
                },
                'seedReplicationTime': datetime(2015, 1, 1),
                'frequency': 123,
                'nextReplicationRunStartTime': datetime(2015, 1, 1),
                'licenseType': 'AWS'|'BYOL',
                'roleName': 'string',
                'latestAmiId': 'string',
                'state': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                'statusMessage': 'string',
                'description': 'string',
                'replicationRunList': [
                    {
                        'replicationRunId': 'string',
                        'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                        'type': 'ON_DEMAND'|'AUTOMATIC',
                        'statusMessage': 'string',
                        'amiId': 'string',
                        'scheduledStartTime': datetime(2015, 1, 1),
                        'completedTime': datetime(2015, 1, 1),
                        'description': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    replicationJobList (list) -- List of Replication Jobs
    (dict) -- Object representing a Replication Job
    replicationJobId (string) -- The unique identifier for a Replication Job.
    serverId (string) -- Unique Identifier for a server
    serverType (string) -- Type of server.
    vmServer (dict) -- Object representing a VM server
    vmServerAddress (dict) -- Object representing a server's location
    vmManagerId (string) -- Unique Identifier for VM Manager
    vmId (string) -- Unique Identifier for a VM
    
    
    vmName (string) -- Name of Virtual Machine
    vmManagerName (string) -- VM Manager Name
    vmManagerType (string) -- VM Management Product
    vmPath (string) -- Path to VM
    
    
    seedReplicationTime (datetime) -- Timestamp of an operation
    frequency (integer) -- Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.
    nextReplicationRunStartTime (datetime) -- Timestamp of an operation
    licenseType (string) -- The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.
    roleName (string) -- Name of service role in customer's account to be used by SMS service.
    latestAmiId (string) -- The AMI id for the image resulting from a Replication Run.
    state (string) -- Current state of Replication Job
    statusMessage (string) -- String describing current status of Replication Job
    description (string) -- The description for a Replication Job/Run.
    replicationRunList (list) -- List of Replication Runs
    (dict) -- Object representing a Replication Run
    replicationRunId (string) -- The unique identifier for a Replication Run.
    state (string) -- Current state of Replication Run
    type (string) -- Type of Replication Run
    statusMessage (string) -- String describing current status of Replication Run
    amiId (string) -- The AMI id for the image resulting from a Replication Run.
    scheduledStartTime (datetime) -- Timestamp of an operation
    completedTime (datetime) -- Timestamp of an operation
    description (string) -- The description for a Replication Job/Run.
    
    
    
    
    
    
    
    
    nextToken (string) -- Pagination token to pass as input to API call
    
    
    
    """
    pass

def get_replication_runs(replicationJobId=None, nextToken=None, maxResults=None):
    """
    The GetReplicationRuns API will return all ReplicationRuns for a given ReplicationJob. This API returns a paginated list, that may be consecutively called with nextToken to retrieve all ReplicationRuns for a ReplicationJob.
    See also: AWS API Documentation
    
    
    :example: response = client.get_replication_runs(
        replicationJobId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type replicationJobId: string
    :param replicationJobId: [REQUIRED] The unique identifier for a Replication Job.

    :type nextToken: string
    :param nextToken: Pagination token to pass as input to API call

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.

    :rtype: dict
    :return: {
        'replicationJob': {
            'replicationJobId': 'string',
            'serverId': 'string',
            'serverType': 'VIRTUAL_MACHINE',
            'vmServer': {
                'vmServerAddress': {
                    'vmManagerId': 'string',
                    'vmId': 'string'
                },
                'vmName': 'string',
                'vmManagerName': 'string',
                'vmManagerType': 'VSPHERE',
                'vmPath': 'string'
            },
            'seedReplicationTime': datetime(2015, 1, 1),
            'frequency': 123,
            'nextReplicationRunStartTime': datetime(2015, 1, 1),
            'licenseType': 'AWS'|'BYOL',
            'roleName': 'string',
            'latestAmiId': 'string',
            'state': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
            'statusMessage': 'string',
            'description': 'string',
            'replicationRunList': [
                {
                    'replicationRunId': 'string',
                    'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                    'type': 'ON_DEMAND'|'AUTOMATIC',
                    'statusMessage': 'string',
                    'amiId': 'string',
                    'scheduledStartTime': datetime(2015, 1, 1),
                    'completedTime': datetime(2015, 1, 1),
                    'description': 'string'
                },
            ]
        },
        'replicationRunList': [
            {
                'replicationRunId': 'string',
                'state': 'PENDING'|'MISSED'|'ACTIVE'|'FAILED'|'COMPLETED'|'DELETING'|'DELETED',
                'type': 'ON_DEMAND'|'AUTOMATIC',
                'statusMessage': 'string',
                'amiId': 'string',
                'scheduledStartTime': datetime(2015, 1, 1),
                'completedTime': datetime(2015, 1, 1),
                'description': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    replicationJob (dict) -- Object representing a Replication Job
    replicationJobId (string) -- The unique identifier for a Replication Job.
    serverId (string) -- Unique Identifier for a server
    serverType (string) -- Type of server.
    vmServer (dict) -- Object representing a VM server
    vmServerAddress (dict) -- Object representing a server's location
    vmManagerId (string) -- Unique Identifier for VM Manager
    vmId (string) -- Unique Identifier for a VM
    
    
    vmName (string) -- Name of Virtual Machine
    vmManagerName (string) -- VM Manager Name
    vmManagerType (string) -- VM Management Product
    vmPath (string) -- Path to VM
    
    
    seedReplicationTime (datetime) -- Timestamp of an operation
    frequency (integer) -- Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.
    nextReplicationRunStartTime (datetime) -- Timestamp of an operation
    licenseType (string) -- The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.
    roleName (string) -- Name of service role in customer's account to be used by SMS service.
    latestAmiId (string) -- The AMI id for the image resulting from a Replication Run.
    state (string) -- Current state of Replication Job
    statusMessage (string) -- String describing current status of Replication Job
    description (string) -- The description for a Replication Job/Run.
    replicationRunList (list) -- List of Replication Runs
    (dict) -- Object representing a Replication Run
    replicationRunId (string) -- The unique identifier for a Replication Run.
    state (string) -- Current state of Replication Run
    type (string) -- Type of Replication Run
    statusMessage (string) -- String describing current status of Replication Run
    amiId (string) -- The AMI id for the image resulting from a Replication Run.
    scheduledStartTime (datetime) -- Timestamp of an operation
    completedTime (datetime) -- Timestamp of an operation
    description (string) -- The description for a Replication Job/Run.
    
    
    
    
    
    
    replicationRunList (list) -- List of Replication Runs
    (dict) -- Object representing a Replication Run
    replicationRunId (string) -- The unique identifier for a Replication Run.
    state (string) -- Current state of Replication Run
    type (string) -- Type of Replication Run
    statusMessage (string) -- String describing current status of Replication Run
    amiId (string) -- The AMI id for the image resulting from a Replication Run.
    scheduledStartTime (datetime) -- Timestamp of an operation
    completedTime (datetime) -- Timestamp of an operation
    description (string) -- The description for a Replication Job/Run.
    
    
    
    
    nextToken (string) -- Pagination token to pass as input to API call
    
    
    
    """
    pass

def get_servers(nextToken=None, maxResults=None):
    """
    The GetServers API returns a list of all servers in your server catalog. For this call to succeed, you must previously have called ImportServerCatalog.
    See also: AWS API Documentation
    
    
    :example: response = client.get_servers(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: Pagination token to pass as input to API call

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in one API call. If left empty, this will default to 50.

    :rtype: dict
    :return: {
        'lastModifiedOn': datetime(2015, 1, 1),
        'serverCatalogStatus': 'NOT_IMPORTED'|'IMPORTING'|'AVAILABLE'|'DELETED'|'EXPIRED',
        'serverList': [
            {
                'serverId': 'string',
                'serverType': 'VIRTUAL_MACHINE',
                'vmServer': {
                    'vmServerAddress': {
                        'vmManagerId': 'string',
                        'vmId': 'string'
                    },
                    'vmName': 'string',
                    'vmManagerName': 'string',
                    'vmManagerType': 'VSPHERE',
                    'vmPath': 'string'
                },
                'replicationJobId': 'string',
                'replicationJobTerminated': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (dict) --
    lastModifiedOn (datetime) -- Timestamp of an operation
    serverCatalogStatus (string) -- Status of Server catalog
    serverList (list) -- List of servers from catalog
    (dict) -- Object representing a server
    serverId (string) -- Unique Identifier for a server
    serverType (string) -- Type of server.
    vmServer (dict) -- Object representing a VM server
    vmServerAddress (dict) -- Object representing a server's location
    vmManagerId (string) -- Unique Identifier for VM Manager
    vmId (string) -- Unique Identifier for a VM
    
    
    vmName (string) -- Name of Virtual Machine
    vmManagerName (string) -- VM Manager Name
    vmManagerType (string) -- VM Management Product
    vmPath (string) -- Path to VM
    
    
    replicationJobId (string) -- The unique identifier for a Replication Job.
    replicationJobTerminated (boolean) -- An indicator of the Replication Job being deleted or failed.
    
    
    
    
    nextToken (string) -- Pagination token to pass as input to API call
    
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

def import_server_catalog():
    """
    The ImportServerCatalog API is used to gather the complete list of on-premises servers on your premises. This API call requires connectors to be installed and monitoring all servers you would like imported. This API call returns immediately, but may take some time to retrieve all of the servers.
    See also: AWS API Documentation
    
    
    :example: response = client.import_server_catalog()
    
    
    :rtype: dict
    :return: {}
    
    
    """
    pass

def start_on_demand_replication_run(replicationJobId=None, description=None):
    """
    The StartOnDemandReplicationRun API is used to start a ReplicationRun on demand (in addition to those that are scheduled based on your frequency). This ReplicationRun will start immediately. StartOnDemandReplicationRun is subject to limits on how many on demand ReplicationRuns you may call per 24-hour period.
    See also: AWS API Documentation
    
    
    :example: response = client.start_on_demand_replication_run(
        replicationJobId='string',
        description='string'
    )
    
    
    :type replicationJobId: string
    :param replicationJobId: [REQUIRED] The unique identifier for a Replication Job.

    :type description: string
    :param description: The description for a Replication Job/Run.

    :rtype: dict
    :return: {
        'replicationRunId': 'string'
    }
    
    
    :returns: 
    (dict) --
    replicationRunId (string) -- The unique identifier for a Replication Run.
    
    
    
    """
    pass

def update_replication_job(replicationJobId=None, frequency=None, nextReplicationRunStartTime=None, licenseType=None, roleName=None, description=None):
    """
    The UpdateReplicationJob API is used to change the settings of your existing ReplicationJob created using CreateReplicationJob. Calling this API will affect the next scheduled ReplicationRun.
    See also: AWS API Documentation
    
    
    :example: response = client.update_replication_job(
        replicationJobId='string',
        frequency=123,
        nextReplicationRunStartTime=datetime(2015, 1, 1),
        licenseType='AWS'|'BYOL',
        roleName='string',
        description='string'
    )
    
    
    :type replicationJobId: string
    :param replicationJobId: [REQUIRED] The unique identifier for a Replication Job.

    :type frequency: integer
    :param frequency: Interval between Replication Runs. This value is specified in hours, and represents the time between consecutive Replication Runs.

    :type nextReplicationRunStartTime: datetime
    :param nextReplicationRunStartTime: Timestamp of an operation

    :type licenseType: string
    :param licenseType: The license type to be used for the Amazon Machine Image (AMI) created after a successful ReplicationRun.

    :type roleName: string
    :param roleName: Name of service role in customer's account to be used by SMS service.

    :type description: string
    :param description: The description for a Replication Job/Run.

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

