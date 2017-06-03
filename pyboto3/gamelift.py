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

def create_alias(Name=None, Description=None, RoutingStrategy=None):
    """
    Creates an alias and sets a target fleet. A fleet alias can be used in place of a fleet ID, such as when calling CreateGameSession from a game client or game service or adding destinations to a game session queue. By changing an alias's target fleet, you can switch your players to the new fleet without changing any other component. In production, this feature is particularly useful to redirect your player base seamlessly to the latest game server update.
    Amazon GameLift supports two types of routing strategies for aliases: simple and terminal. Use a simple alias to point to an active fleet. Use a terminal alias to display a message to incoming traffic instead of routing players to an active fleet. This option is useful when a game server is no longer supported but you want to provide better messaging than a standard 404 error.
    To create a fleet alias, specify an alias name, routing strategy, and optional description. If successful, a new alias record is returned, including an alias ID, which you can reference when creating a game session. To reassign the alias to another fleet ID, call  UpdateAlias .
    See also: AWS API Documentation
    
    
    :example: response = client.create_alias(
        Name='string',
        Description='string',
        RoutingStrategy={
            'Type': 'SIMPLE'|'TERMINAL',
            'FleetId': 'string',
            'Message': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Descriptive label that is associated with an alias. Alias names do not need to be unique.
            

    :type Description: string
    :param Description: Human-readable description of an alias.

    :type RoutingStrategy: dict
    :param RoutingStrategy: [REQUIRED]
            Object that specifies the fleet and routing type to use for the alias.
            Type (string) --Type of routing strategy.
            Possible routing types include the following:
            SIMPLE   The alias resolves to one specific fleet. Use this type when routing to active fleets.
            TERMINAL   The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
            FleetId (string) --Unique identifier for a fleet that the alias points to.
            Message (string) --Message text to be used with a terminal routing strategy.
            

    :rtype: dict
    :return: {
        'Alias': {
            'AliasId': 'string',
            'Name': 'string',
            'AliasArn': 'string',
            'Description': 'string',
            'RoutingStrategy': {
                'Type': 'SIMPLE'|'TERMINAL',
                'FleetId': 'string',
                'Message': 'string'
            },
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    SIMPLE  The alias resolves to one specific fleet. Use this type when routing to active fleets.
    TERMINAL  The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
    
    """
    pass

def create_build(Name=None, Version=None, StorageLocation=None, OperatingSystem=None):
    """
    Creates a new Amazon GameLift build from a set of game server binary files stored in an Amazon Simple Storage Service (Amazon S3) location. When using this API call, you must create a .zip file containing all of the build files and store it in an Amazon S3 bucket under your AWS account. For help on packaging your build files and creating a build, see Uploading Your Game to Amazon GameLift .
    To create a new build using CreateBuild , identify the storage location and operating system of your game build. You also have the option of specifying a build name and version. If successful, this action creates a new build record with an unique build ID and in INITIALIZED status. Use the API call  DescribeBuild to check the status of your build. A build must be in READY status before it can be used to create fleets to host your game.
    See also: AWS API Documentation
    
    
    :example: response = client.create_build(
        Name='string',
        Version='string',
        StorageLocation={
            'Bucket': 'string',
            'Key': 'string',
            'RoleArn': 'string'
        },
        OperatingSystem='WINDOWS_2012'|'AMAZON_LINUX'
    )
    
    
    :type Name: string
    :param Name: Descriptive label that is associated with a build. Build names do not need to be unique. You can use UpdateBuild to change this value later.

    :type Version: string
    :param Version: Version that is associated with this build. Version strings do not need to be unique. You can use UpdateBuild to change this value later.

    :type StorageLocation: dict
    :param StorageLocation: Amazon S3 location of the game build files to be uploaded. The S3 bucket must be owned by the same AWS account that you're using to manage Amazon GameLift. It also must in the same region that you want to create a new build in. Before calling CreateBuild with this location, you must allow Amazon GameLift to access your Amazon S3 bucket (see Create a Build with Files in Amazon S3 ).
            Bucket (string) --Amazon S3 bucket identifier. This is the name of your S3 bucket.
            Key (string) --Name of the zip file containing your build files.
            RoleArn (string) --Amazon Resource Name (ARN ) for the access role that allows Amazon GameLift to access your S3 bucket.
            

    :type OperatingSystem: string
    :param OperatingSystem: Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. If your game build contains multiple executables, they all must run on the same operating system.

    :rtype: dict
    :return: {
        'Build': {
            'BuildId': 'string',
            'Name': 'string',
            'Version': 'string',
            'Status': 'INITIALIZED'|'READY'|'FAILED',
            'SizeOnDisk': 123,
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
            'CreationTime': datetime(2015, 1, 1)
        },
        'UploadCredentials': {
            'AccessKeyId': 'string',
            'SecretAccessKey': 'string',
            'SessionToken': 'string'
        },
        'StorageLocation': {
            'Bucket': 'string',
            'Key': 'string',
            'RoleArn': 'string'
        }
    }
    
    
    :returns: 
    INITIALIZED  A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
    READY  The game build has been successfully uploaded. You can now create new fleets for this build.
    FAILED  The game build upload failed. You cannot create new fleets for this build.
    
    """
    pass

def create_fleet(Name=None, Description=None, BuildId=None, ServerLaunchPath=None, ServerLaunchParameters=None, LogPaths=None, EC2InstanceType=None, EC2InboundPermissions=None, NewGameSessionProtectionPolicy=None, RuntimeConfiguration=None, ResourceCreationLimitPolicy=None, MetricGroups=None):
    """
    Creates a new fleet to run your game servers. A fleet is a set of Amazon Elastic Compute Cloud (Amazon EC2) instances, each of which can run multiple server processes to host game sessions. You configure a fleet to create instances with certain hardware specifications (see Amazon EC2 Instance Types for more information), and deploy a specified game build to each instance. A newly created fleet passes through several statuses; once it reaches the ACTIVE status, it can begin hosting game sessions.
    To create a new fleet, you must specify the following: (1) fleet name, (2) build ID of an uploaded game build, (3) an EC2 instance type, and (4) a runtime configuration that describes which server processes to run on each instance in the fleet. (Although the runtime configuration is not a required parameter, the fleet cannot be successfully created without it.) You can also configure the new fleet with the following settings: fleet description, access permissions for inbound traffic, fleet-wide game session protection, and resource creation limit. If you use Amazon CloudWatch for metrics, you can add the new fleet to a metric group, which allows you to view aggregated metrics for a set of fleets. Once you specify a metric group, the new fleet's metrics are included in the metric group's data.
    If the CreateFleet call is successful, Amazon GameLift performs the following tasks:
    After a fleet is created, use the following actions to change fleet properties and configuration:
    See also: AWS API Documentation
    
    
    :example: response = client.create_fleet(
        Name='string',
        Description='string',
        BuildId='string',
        ServerLaunchPath='string',
        ServerLaunchParameters='string',
        LogPaths=[
            'string',
        ],
        EC2InstanceType='t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
        EC2InboundPermissions=[
            {
                'FromPort': 123,
                'ToPort': 123,
                'IpRange': 'string',
                'Protocol': 'TCP'|'UDP'
            },
        ],
        NewGameSessionProtectionPolicy='NoProtection'|'FullProtection',
        RuntimeConfiguration={
            'ServerProcesses': [
                {
                    'LaunchPath': 'string',
                    'Parameters': 'string',
                    'ConcurrentExecutions': 123
                },
            ],
            'MaxConcurrentGameSessionActivations': 123,
            'GameSessionActivationTimeoutSeconds': 123
        },
        ResourceCreationLimitPolicy={
            'NewGameSessionsPerCreator': 123,
            'PolicyPeriodInMinutes': 123
        },
        MetricGroups=[
            'string',
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Descriptive label that is associated with a fleet. Fleet names do not need to be unique.
            

    :type Description: string
    :param Description: Human-readable description of a fleet.

    :type BuildId: string
    :param BuildId: [REQUIRED]
            Unique identifier for a build to be deployed on the new fleet. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
            

    :type ServerLaunchPath: string
    :param ServerLaunchPath: This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. (Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.)

    :type ServerLaunchParameters: string
    :param ServerLaunchParameters: This parameter is no longer used. Instead, specify server launch parameters in the RuntimeConfiguration parameter. (Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.)

    :type LogPaths: list
    :param LogPaths: This parameter is no longer used. Instead, to specify where Amazon GameLift should store log files once a server process shuts down, use the Amazon GameLift server API ProcessReady() and specify one or more directory paths in logParameters . See more information in the Server API Reference .
            (string) --
            

    :type EC2InstanceType: string
    :param EC2InstanceType: [REQUIRED]
            Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.
            

    :type EC2InboundPermissions: list
    :param EC2InboundPermissions: Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. If no inbound permissions are set, including both IP address range and port range, the server processes in the fleet cannot accept connections. You can specify one or more sets of permissions for a fleet.
            (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on Amazon GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet's allowed ranges. This combination is included in the GameSession object.
            FromPort (integer) -- [REQUIRED]Starting value for a range of allowed port numbers.
            ToPort (integer) -- [REQUIRED]Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
            IpRange (string) -- [REQUIRED]Range of allowed IP addresses. This value must be expressed in CIDR notation. Example: '000.000.000.000/[subnet mask] ' or optionally the shortened version '0.0.0.0/[subnet mask] '.
            Protocol (string) -- [REQUIRED]Network communication protocol used by the fleet.
            
            

    :type NewGameSessionProtectionPolicy: string
    :param NewGameSessionProtectionPolicy: Game session protection policy to apply to all instances in this fleet. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy using UpdateFleetAttributes, but this change will only affect sessions created after the policy change. You can also set protection for individual instances using UpdateGameSession .
            NoProtection   The game session can be terminated during a scale-down event.
            FullProtection   If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
            

    :type RuntimeConfiguration: dict
    :param RuntimeConfiguration: Instructions for launching server processes on each instance in the fleet. The runtime configuration for a fleet has a collection of server process configurations, one for each type of server process to run on an instance. A server process configuration specifies the location of the server executable, launch parameters, and the number of concurrent processes with that configuration to maintain on each instance. A CreateFleet request must include a runtime configuration with at least one server process configuration; otherwise the request will fail with an invalid request exception. (This parameter replaces the parameters ServerLaunchPath and ServerLaunchParameters ; requests that contain values for these parameters instead of a runtime configuration will continue to work.)
            ServerProcesses (list) --Collection of server process configurations that describe which server processes to run on each instance in a fleet.
            (dict) --A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet's `` RuntimeConfiguration `` .
            LaunchPath (string) -- [REQUIRED]Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances C:\game , and for Linux instances /local/game . A Windows game build with an executable file located at MyGame\latest\server.exe must have a launch path of 'C:\game\MyGame\latest\server.exe '. A Linux game build with an executable file located at MyGame/latest/server.exe must have a launch path of '/local/game/MyGame/latest/server.exe '.
            Parameters (string) --Optional list of parameters to pass to the server executable on launch.
            ConcurrentExecutions (integer) -- [REQUIRED]Number of server processes using this configuration to run concurrently on an instance.
            
            MaxConcurrentGameSessionActivations (integer) --Maximum number of game sessions with status ACTIVATING to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.
            GameSessionActivationTimeoutSeconds (integer) --Maximum amount of time (in seconds) that a game session can remain in status ACTIVATING. If the game session is not active before the timeout, activation is terminated and the game session status is changed to TERMINATED.
            

    :type ResourceCreationLimitPolicy: dict
    :param ResourceCreationLimitPolicy: Policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
            NewGameSessionsPerCreator (integer) --Maximum number of game sessions that an individual can create during the policy period.
            PolicyPeriodInMinutes (integer) --Time span used in evaluating the resource creation limit policy.
            

    :type MetricGroups: list
    :param MetricGroups: Names of metric groups to add this fleet to. Use an existing metric group name to add this fleet to the group, or use a new name to create a new metric group. Currently, a fleet can only be included in one metric group at a time.
            (string) --
            

    :rtype: dict
    :return: {
        'FleetAttributes': {
            'FleetId': 'string',
            'FleetArn': 'string',
            'Description': 'string',
            'Name': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TerminationTime': datetime(2015, 1, 1),
            'Status': 'NEW'|'DOWNLOADING'|'VALIDATING'|'BUILDING'|'ACTIVATING'|'ACTIVE'|'DELETING'|'ERROR'|'TERMINATED',
            'BuildId': 'string',
            'ServerLaunchPath': 'string',
            'ServerLaunchParameters': 'string',
            'LogPaths': [
                'string',
            ],
            'NewGameSessionProtectionPolicy': 'NoProtection'|'FullProtection',
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
            'ResourceCreationLimitPolicy': {
                'NewGameSessionsPerCreator': 123,
                'PolicyPeriodInMinutes': 123
            },
            'MetricGroups': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    UpdateFleetAttributes -- Update fleet metadata, including name and description.
    UpdateFleetCapacity -- Increase or decrease the number of instances you want the fleet to maintain.
    UpdateFleetPortSettings -- Change the IP address and port ranges that allow access to incoming traffic.
    UpdateRuntimeConfiguration -- Change how server processes are launched in the fleet, including launch path, launch parameters, and the number of concurrent processes.
    PutScalingPolicy -- Create or update rules that are used to set the fleet's capacity (autoscaling).
    
    """
    pass

def create_game_session(FleetId=None, AliasId=None, MaximumPlayerSessionCount=None, Name=None, GameProperties=None, CreatorId=None, GameSessionId=None, IdempotencyToken=None):
    """
    Creates a multiplayer game session for players. This action creates a game session record and assigns an available server process in the specified fleet to host the game session. A fleet must have an ACTIVE status before a game session can be created in it.
    To create a game session, specify either fleet ID or alias ID and indicate a maximum number of players to allow in the game session. You can also provide a name and game-specific properties for this game session. If successful, a  GameSession object is returned containing game session properties, including a game session ID with the custom string you provided.
    By default, newly created game sessions allow new players to join. Use  UpdateGameSession to change the game session's player session creation policy.
    See also: AWS API Documentation
    
    
    :example: response = client.create_game_session(
        FleetId='string',
        AliasId='string',
        MaximumPlayerSessionCount=123,
        Name='string',
        GameProperties=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        CreatorId='string',
        GameSessionId='string',
        IdempotencyToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: Unique identifier for a fleet to create a game session in. Each request must reference either a fleet ID or alias ID, but not both.

    :type AliasId: string
    :param AliasId: Unique identifier for an alias associated with the fleet to create a game session in. Each request must reference either a fleet ID or alias ID, but not both.

    :type MaximumPlayerSessionCount: integer
    :param MaximumPlayerSessionCount: [REQUIRED]
            Maximum number of players that can be connected simultaneously to the game session.
            

    :type Name: string
    :param Name: Descriptive label that is associated with a game session. Session names do not need to be unique.

    :type GameProperties: list
    :param GameProperties: Set of developer-defined properties for a game session. These properties are passed to the server process hosting the game session.
            (dict) --Set of key-value pairs containing information a server process requires to set up a game session. This object allows you to pass in any set of data needed for your game. For more information, see the Amazon GameLift Developer Guide .
            Key (string) -- [REQUIRED]TBD
            Value (string) -- [REQUIRED]TBD
            
            

    :type CreatorId: string
    :param CreatorId: Unique identifier for a player or entity creating the game session. This ID is used to enforce a resource protection policy (if one exists) that limits the number of concurrent active game sessions one player can have.

    :type GameSessionId: string
    :param GameSessionId: This parameter is no longer preferred. Please use ``IdempotencyToken`` instead. Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID. (A game session ID has the following format: arn:aws:gamelift:region::gamesession/fleet ID/custom ID string or idempotency token .)

    :type IdempotencyToken: string
    :param IdempotencyToken: Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID. (A game session ID has the following format: arn:aws:gamelift:region::gamesession/fleet ID/custom ID string or idempotency token .)

    :rtype: dict
    :return: {
        'GameSession': {
            'GameSessionId': 'string',
            'Name': 'string',
            'FleetId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TerminationTime': datetime(2015, 1, 1),
            'CurrentPlayerSessionCount': 123,
            'MaximumPlayerSessionCount': 123,
            'Status': 'ACTIVE'|'ACTIVATING'|'TERMINATED'|'TERMINATING'|'ERROR',
            'GameProperties': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'IpAddress': 'string',
            'Port': 123,
            'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
            'CreatorId': 'string'
        }
    }
    
    
    """
    pass

def create_game_session_queue(Name=None, TimeoutInSeconds=None, PlayerLatencyPolicies=None, Destinations=None):
    """
    Establishes a new queue for processing requests to place new game sessions. A queue identifies where new game sessions can be hosted -- by specifying a list of destinations (fleets or aliases) -- and how long requests can wait in the queue before timing out. You can set up a queue to try to place game sessions on fleets in multiple regions. To add placement requests to a queue, call  StartGameSessionPlacement and reference the queue name.
    To create a new queue, provide a name, timeout value, a list of destinations and, if desired, a set of latency policies. If successful, a new queue object is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.create_game_session_queue(
        Name='string',
        TimeoutInSeconds=123,
        PlayerLatencyPolicies=[
            {
                'MaximumIndividualPlayerLatencyMilliseconds': 123,
                'PolicyDurationSeconds': 123
            },
        ],
        Destinations=[
            {
                'DestinationArn': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Descriptive label that is associated with queue. Queue names must be unique within each region.
            

    :type TimeoutInSeconds: integer
    :param TimeoutInSeconds: Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.

    :type PlayerLatencyPolicies: list
    :param PlayerLatencyPolicies: Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. A player latency policy must set a value for MaximumIndividualPlayerLatencyMilliseconds; if none is set, this API requests will fail.
            (dict) --Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
            Latency policy-related operations include:
            CreateGameSessionQueue
            UpdateGameSessionQueue
            StartGameSessionPlacement
            MaximumIndividualPlayerLatencyMilliseconds (integer) --The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
            PolicyDurationSeconds (integer) --The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
            
            

    :type Destinations: list
    :param Destinations: List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.
            (dict) --Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue.
            DestinationArn (string) --Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a region name, provide a unique identifier across all regions.
            
            

    :rtype: dict
    :return: {
        'GameSessionQueue': {
            'Name': 'string',
            'GameSessionQueueArn': 'string',
            'TimeoutInSeconds': 123,
            'PlayerLatencyPolicies': [
                {
                    'MaximumIndividualPlayerLatencyMilliseconds': 123,
                    'PolicyDurationSeconds': 123
                },
            ],
            'Destinations': [
                {
                    'DestinationArn': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CreateGameSessionQueue
    UpdateGameSessionQueue
    StartGameSessionPlacement
    
    """
    pass

def create_player_session(GameSessionId=None, PlayerId=None, PlayerData=None):
    """
    Adds a player to a game session and creates a player session record. Before a player can be added, a game session must have an ACTIVE status, have a creation policy of ALLOW_ALL , and have an open player slot. To add a group of players to a game session, use  CreatePlayerSessions .
    To create a player session, specify a game session ID, player ID, and optionally a string of player data. If successful, the player is added to the game session and a new  PlayerSession object is returned. Player sessions cannot be updated.
    See also: AWS API Documentation
    
    
    :example: response = client.create_player_session(
        GameSessionId='string',
        PlayerId='string',
        PlayerData='string'
    )
    
    
    :type GameSessionId: string
    :param GameSessionId: [REQUIRED]
            Unique identifier for the game session to add a player to.
            

    :type PlayerId: string
    :param PlayerId: [REQUIRED]
            Unique identifier for a player. Player IDs are developer-defined.
            

    :type PlayerData: string
    :param PlayerData: Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.

    :rtype: dict
    :return: {
        'PlayerSession': {
            'PlayerSessionId': 'string',
            'PlayerId': 'string',
            'GameSessionId': 'string',
            'FleetId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TerminationTime': datetime(2015, 1, 1),
            'Status': 'RESERVED'|'ACTIVE'|'COMPLETED'|'TIMEDOUT',
            'IpAddress': 'string',
            'Port': 123,
            'PlayerData': 'string'
        }
    }
    
    
    :returns: 
    RESERVED  The player session request has been received, but the player has not yet connected to the server process and/or been validated.
    ACTIVE  The player has been validated by the server process and is currently connected.
    COMPLETED  The player connection has been dropped.
    TIMEDOUT  A player session request was received, but the player did not connect and/or was not validated within the time-out limit (60 seconds).
    
    """
    pass

def create_player_sessions(GameSessionId=None, PlayerIds=None, PlayerDataMap=None):
    """
    Adds a group of players to a game session. This action is useful with a team matching feature. Before players can be added, a game session must have an ACTIVE status, have a creation policy of ALLOW_ALL , and have an open player slot. To add a single player to a game session, use  CreatePlayerSession .
    To create player sessions, specify a game session ID, a list of player IDs, and optionally a set of player data strings. If successful, the players are added to the game session and a set of new  PlayerSession objects is returned. Player sessions cannot be updated.
    See also: AWS API Documentation
    
    
    :example: response = client.create_player_sessions(
        GameSessionId='string',
        PlayerIds=[
            'string',
        ],
        PlayerDataMap={
            'string': 'string'
        }
    )
    
    
    :type GameSessionId: string
    :param GameSessionId: [REQUIRED]
            Unique identifier for the game session to add players to.
            

    :type PlayerIds: list
    :param PlayerIds: [REQUIRED]
            List of unique identifiers for the players to be added.
            (string) --
            

    :type PlayerDataMap: dict
    :param PlayerDataMap: Map of string pairs, each specifying a player ID and a set of developer-defined information related to the player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game. Player data strings for player IDs not included in the PlayerIds parameter are ignored.
            (string) --
            (string) --
            

    :rtype: dict
    :return: {
        'PlayerSessions': [
            {
                'PlayerSessionId': 'string',
                'PlayerId': 'string',
                'GameSessionId': 'string',
                'FleetId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TerminationTime': datetime(2015, 1, 1),
                'Status': 'RESERVED'|'ACTIVE'|'COMPLETED'|'TIMEDOUT',
                'IpAddress': 'string',
                'Port': 123,
                'PlayerData': 'string'
            },
        ]
    }
    
    
    :returns: 
    CreatePlayerSession
    CreatePlayerSessions
    DescribePlayerSessions
    
    """
    pass

def delete_alias(AliasId=None):
    """
    Deletes a fleet alias. This action removes all record of the alias. Game clients attempting to access a server process using the deleted alias receive an error. To delete an alias, specify the alias ID to be deleted.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_alias(
        AliasId='string'
    )
    
    
    :type AliasId: string
    :param AliasId: [REQUIRED]
            Unique identifier for a fleet alias. Specify the alias you want to delete.
            

    """
    pass

def delete_build(BuildId=None):
    """
    Deletes a build. This action permanently deletes the build record and any uploaded build files.
    To delete a build, specify its ID. Deleting a build does not affect the status of any active fleets using the build, but you can no longer create new fleets with the deleted build.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_build(
        BuildId='string'
    )
    
    
    :type BuildId: string
    :param BuildId: [REQUIRED]
            Unique identifier for a build to delete.
            

    """
    pass

def delete_fleet(FleetId=None):
    """
    Deletes everything related to a fleet. Before deleting a fleet, you must set the fleet's desired capacity to zero. See  UpdateFleetCapacity .
    This action removes the fleet's resources and the fleet record. Once a fleet is deleted, you can no longer use that fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_fleet(
        FleetId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to be deleted.
            

    """
    pass

def delete_game_session_queue(Name=None):
    """
    Deletes a game session queue. This action means that any  StartGameSessionPlacement requests that reference this queue will fail. To delete a queue, specify the queue name.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_game_session_queue(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Descriptive label that is associated with queue. Queue names must be unique within each region.
            

    :rtype: dict
    :return: {}
    
    
    """
    pass

def delete_scaling_policy(Name=None, FleetId=None):
    """
    Deletes a fleet scaling policy. This action means that the policy is no longer in force and removes all record of it. To delete a scaling policy, specify both the scaling policy name and the fleet ID it is associated with.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_scaling_policy(
        Name='string',
        FleetId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Descriptive label that is associated with a scaling policy. Policy names do not need to be unique.
            

    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to be deleted.
            

    """
    pass

def describe_alias(AliasId=None):
    """
    Retrieves properties for a fleet alias. This operation returns all alias metadata and settings. To get just the fleet ID an alias is currently pointing to, use  ResolveAlias .
    To get alias properties, specify the alias ID. If successful, an  Alias object is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_alias(
        AliasId='string'
    )
    
    
    :type AliasId: string
    :param AliasId: [REQUIRED]
            Unique identifier for a fleet alias. Specify the alias you want to retrieve.
            

    :rtype: dict
    :return: {
        'Alias': {
            'AliasId': 'string',
            'Name': 'string',
            'AliasArn': 'string',
            'Description': 'string',
            'RoutingStrategy': {
                'Type': 'SIMPLE'|'TERMINAL',
                'FleetId': 'string',
                'Message': 'string'
            },
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def describe_build(BuildId=None):
    """
    Retrieves properties for a build. To get a build record, specify a build ID. If successful, an object containing the build properties is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_build(
        BuildId='string'
    )
    
    
    :type BuildId: string
    :param BuildId: [REQUIRED]
            Unique identifier for a build to retrieve properties for.
            

    :rtype: dict
    :return: {
        'Build': {
            'BuildId': 'string',
            'Name': 'string',
            'Version': 'string',
            'Status': 'INITIALIZED'|'READY'|'FAILED',
            'SizeOnDisk': 123,
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
            'CreationTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def describe_ec2_instance_limits(EC2InstanceType=None):
    """
    Retrieves the following information for the specified EC2 instance type:
    Service limits vary depending on region. Available regions for Amazon GameLift can be found in the AWS Management Console for Amazon GameLift (see the drop-down list in the upper right corner).
    See also: AWS API Documentation
    
    
    :example: response = client.describe_ec2_instance_limits(
        EC2InstanceType='t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'
    )
    
    
    :type EC2InstanceType: string
    :param EC2InstanceType: Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions. Leave this parameter blank to retrieve limits for all types.

    :rtype: dict
    :return: {
        'EC2InstanceLimits': [
            {
                'EC2InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
                'CurrentInstances': 123,
                'InstanceLimit': 123
            },
        ]
    }
    
    
    """
    pass

def describe_fleet_attributes(FleetIds=None, Limit=None, NextToken=None):
    """
    Retrieves fleet properties, including metadata, status, and configuration, for one or more fleets. You can request attributes for all fleets, or specify a list of one or more fleet IDs. When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  FleetAttributes object is returned for each requested fleet ID. When specifying a list of fleet IDs, attribute objects are returned only for fleets that currently exist.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_fleet_attributes(
        FleetIds=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetIds: list
    :param FleetIds: Unique identifier for a fleet(s) to retrieve attributes for. To request attributes for all fleets, leave this parameter empty.
            (string) --
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :rtype: dict
    :return: {
        'FleetAttributes': [
            {
                'FleetId': 'string',
                'FleetArn': 'string',
                'Description': 'string',
                'Name': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TerminationTime': datetime(2015, 1, 1),
                'Status': 'NEW'|'DOWNLOADING'|'VALIDATING'|'BUILDING'|'ACTIVATING'|'ACTIVE'|'DELETING'|'ERROR'|'TERMINATED',
                'BuildId': 'string',
                'ServerLaunchPath': 'string',
                'ServerLaunchParameters': 'string',
                'LogPaths': [
                    'string',
                ],
                'NewGameSessionProtectionPolicy': 'NoProtection'|'FullProtection',
                'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
                'ResourceCreationLimitPolicy': {
                    'NewGameSessionsPerCreator': 123,
                    'PolicyPeriodInMinutes': 123
                },
                'MetricGroups': [
                    'string',
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    NEW  A new fleet has been defined and desired instances is set to 1.
    DOWNLOADING/VALIDATING/BUILDING/ACTIVATING  Amazon GameLift is setting up the new fleet, creating new instances with the game build and starting server processes.
    ACTIVE  Hosts can now accept game sessions.
    ERROR  An error occurred when downloading, validating, building, or activating the fleet.
    DELETING  Hosts are responding to a delete fleet request.
    TERMINATED  The fleet no longer exists.
    
    """
    pass

def describe_fleet_capacity(FleetIds=None, Limit=None, NextToken=None):
    """
    Retrieves the current status of fleet capacity for one or more fleets. This information includes the number of instances that have been requested for the fleet and the number currently active. You can request capacity for all fleets, or specify a list of one or more fleet IDs. When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  FleetCapacity object is returned for each requested fleet ID. When specifying a list of fleet IDs, attribute objects are returned only for fleets that currently exist.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_fleet_capacity(
        FleetIds=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetIds: list
    :param FleetIds: Unique identifier for a fleet(s) to retrieve capacity information for. To request capacity information for all fleets, leave this parameter empty.
            (string) --
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :rtype: dict
    :return: {
        'FleetCapacity': [
            {
                'FleetId': 'string',
                'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
                'InstanceCounts': {
                    'DESIRED': 123,
                    'MINIMUM': 123,
                    'MAXIMUM': 123,
                    'PENDING': 123,
                    'ACTIVE': 123,
                    'IDLE': 123,
                    'TERMINATING': 123
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_fleet_events(FleetId=None, StartTime=None, EndTime=None, Limit=None, NextToken=None):
    """
    Retrieves entries from the specified fleet's event log. You can specify a time range to limit the result set. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a collection of event log entries matching the request are returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_fleet_events(
        FleetId='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to get event logs for.
            

    :type StartTime: datetime
    :param StartTime: Earliest date to retrieve event logs for. If no start time is specified, this call returns entries starting from when the fleet was created to the specified end time. Format is a number expressed in Unix time as milliseconds (ex: '1469498468.057').

    :type EndTime: datetime
    :param EndTime: Most recent date to retrieve event logs for. If no end time is specified, this call returns entries from the specified start time up to the present. Format is a number expressed in Unix time as milliseconds (ex: '1469498468.057').

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'Events': [
            {
                'EventId': 'string',
                'ResourceId': 'string',
                'EventCode': 'GENERIC_EVENT'|'FLEET_CREATED'|'FLEET_DELETED'|'FLEET_SCALING_EVENT'|'FLEET_STATE_DOWNLOADING'|'FLEET_STATE_VALIDATING'|'FLEET_STATE_BUILDING'|'FLEET_STATE_ACTIVATING'|'FLEET_STATE_ACTIVE'|'FLEET_STATE_ERROR'|'FLEET_INITIALIZATION_FAILED'|'FLEET_BINARY_DOWNLOAD_FAILED'|'FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND'|'FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE'|'FLEET_VALIDATION_TIMED_OUT'|'FLEET_ACTIVATION_FAILED'|'FLEET_ACTIVATION_FAILED_NO_INSTANCES'|'FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED'|'SERVER_PROCESS_INVALID_PATH'|'SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT'|'SERVER_PROCESS_PROCESS_READY_TIMEOUT'|'SERVER_PROCESS_CRASHED'|'SERVER_PROCESS_TERMINATED_UNHEALTHY'|'SERVER_PROCESS_FORCE_TERMINATED'|'SERVER_PROCESS_PROCESS_EXIT_TIMEOUT'|'GAME_SESSION_ACTIVATION_TIMEOUT',
                'Message': 'string',
                'EventTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_fleet_port_settings(FleetId=None):
    """
    Retrieves the inbound connection permissions for a fleet. Connection permissions include a range of IP addresses and port settings that incoming traffic can use to access server processes in the fleet. To get a fleet's inbound connection permissions, specify a fleet ID. If successful, a collection of  IpPermission objects is returned for the requested fleet ID. If the requested fleet has been deleted, the result set is empty.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_fleet_port_settings(
        FleetId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to retrieve port settings for.
            

    :rtype: dict
    :return: {
        'InboundPermissions': [
            {
                'FromPort': 123,
                'ToPort': 123,
                'IpRange': 'string',
                'Protocol': 'TCP'|'UDP'
            },
        ]
    }
    
    
    """
    pass

def describe_fleet_utilization(FleetIds=None, Limit=None, NextToken=None):
    """
    Retrieves utilization statistics for one or more fleets. You can request utilization data for all fleets, or specify a list of one or more fleet IDs. When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  FleetUtilization object is returned for each requested fleet ID. When specifying a list of fleet IDs, utilization objects are returned only for fleets that currently exist.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_fleet_utilization(
        FleetIds=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetIds: list
    :param FleetIds: Unique identifier for a fleet(s) to retrieve utilization data for. To request utilization data for all fleets, leave this parameter empty.
            (string) --
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :rtype: dict
    :return: {
        'FleetUtilization': [
            {
                'FleetId': 'string',
                'ActiveServerProcessCount': 123,
                'ActiveGameSessionCount': 123,
                'CurrentPlayerSessionCount': 123,
                'MaximumPlayerSessionCount': 123
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_game_session_details(FleetId=None, GameSessionId=None, AliasId=None, StatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves properties, including the protection policy in force, for one or more game sessions. This action can be used in several ways: (1) provide a GameSessionId or GameSessionArn to request details for a specific game session; (2) provide either a FleetId or an AliasId to request properties for all game sessions running on a fleet.
    To get game session record(s), specify just one of the following: game session ID, fleet ID, or alias ID. You can filter this request by game session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSessionDetail object is returned for each session matching the request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_game_session_details(
        FleetId='string',
        GameSessionId='string',
        AliasId='string',
        StatusFilter='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: Unique identifier for a fleet to retrieve all game sessions active on the fleet.

    :type GameSessionId: string
    :param GameSessionId: Unique identifier for the game session to retrieve.

    :type AliasId: string
    :param AliasId: Unique identifier for an alias associated with the fleet to retrieve all game sessions for.

    :type StatusFilter: string
    :param StatusFilter: Game session status to filter results on. Possible game session statuses include ACTIVE, TERMINATED , ACTIVATING and TERMINATING (the last two are transitory).

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'GameSessionDetails': [
            {
                'GameSession': {
                    'GameSessionId': 'string',
                    'Name': 'string',
                    'FleetId': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'TerminationTime': datetime(2015, 1, 1),
                    'CurrentPlayerSessionCount': 123,
                    'MaximumPlayerSessionCount': 123,
                    'Status': 'ACTIVE'|'ACTIVATING'|'TERMINATED'|'TERMINATING'|'ERROR',
                    'GameProperties': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'IpAddress': 'string',
                    'Port': 123,
                    'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
                    'CreatorId': 'string'
                },
                'ProtectionPolicy': 'NoProtection'|'FullProtection'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    NoProtection  The game session can be terminated during a scale-down event.
    FullProtection  If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
    
    """
    pass

def describe_game_session_placement(PlacementId=None):
    """
    Retrieves properties and current status of a game session placement request. To get game session placement details, specify the placement ID. If successful, a  GameSessionPlacement object is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_game_session_placement(
        PlacementId='string'
    )
    
    
    :type PlacementId: string
    :param PlacementId: [REQUIRED]
            Unique identifier for a game session placement to retrieve.
            

    :rtype: dict
    :return: {
        'GameSessionPlacement': {
            'PlacementId': 'string',
            'GameSessionQueueName': 'string',
            'Status': 'PENDING'|'FULFILLED'|'CANCELLED'|'TIMED_OUT',
            'GameProperties': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'MaximumPlayerSessionCount': 123,
            'GameSessionName': 'string',
            'GameSessionId': 'string',
            'GameSessionArn': 'string',
            'GameSessionRegion': 'string',
            'PlayerLatencies': [
                {
                    'PlayerId': 'string',
                    'RegionIdentifier': 'string',
                    'LatencyInMilliseconds': ...
                },
            ],
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'IpAddress': 'string',
            'Port': 123,
            'PlacedPlayerSessions': [
                {
                    'PlayerId': 'string',
                    'PlayerSessionId': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def describe_game_session_queues(Names=None, Limit=None, NextToken=None):
    """
    Retrieves the properties for one or more game session queues. When requesting multiple queues, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSessionQueue object is returned for each requested queue. When specifying a list of queues, objects are returned only for queues that currently exist in the region.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_game_session_queues(
        Names=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: List of queue names to retrieve information for. To request settings for all queues, leave this parameter empty.
            (string) --
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'GameSessionQueues': [
            {
                'Name': 'string',
                'GameSessionQueueArn': 'string',
                'TimeoutInSeconds': 123,
                'PlayerLatencyPolicies': [
                    {
                        'MaximumIndividualPlayerLatencyMilliseconds': 123,
                        'PolicyDurationSeconds': 123
                    },
                ],
                'Destinations': [
                    {
                        'DestinationArn': 'string'
                    },
                ]
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    The destinations where a new game session can potentially be hosted. Amazon GameLift tries these destinations in an order based on either the queue's default order or player latency information, if provided in a placement request. With latency information, Amazon GameLift can place game sessions where the majority of players are reporting the lowest possible latency.
    The length of time that placement requests can wait in the queue before timing out.
    A set of optional latency policies that protect individual players from high latencies, preventing game sessions from being placed where any individual player is reporting latency higher than a policy's maximum.
    
    """
    pass

def describe_game_sessions(FleetId=None, GameSessionId=None, AliasId=None, StatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves a set of one or more game sessions. Request a specific game session or request all game sessions on a fleet. Alternatively, use  SearchGameSessions to request a set of active game sessions that are filtered by certain criteria. To retrieve protection policy settings for game sessions, use  DescribeGameSessionDetails .
    To get game sessions, specify one of the following: game session ID, fleet ID, or alias ID. You can filter this request by game session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSession object is returned for each game session matching the request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_game_sessions(
        FleetId='string',
        GameSessionId='string',
        AliasId='string',
        StatusFilter='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: Unique identifier for a fleet to retrieve all game sessions for.

    :type GameSessionId: string
    :param GameSessionId: Unique identifier for the game session to retrieve. You can use either a GameSessionId or GameSessionArn value.

    :type AliasId: string
    :param AliasId: Unique identifier for an alias associated with the fleet to retrieve all game sessions for.

    :type StatusFilter: string
    :param StatusFilter: Game session status to filter results on. Possible game session statuses include ACTIVE , TERMINATED , ACTIVATING , and TERMINATING (the last two are transitory).

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'GameSessions': [
            {
                'GameSessionId': 'string',
                'Name': 'string',
                'FleetId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TerminationTime': datetime(2015, 1, 1),
                'CurrentPlayerSessionCount': 123,
                'MaximumPlayerSessionCount': 123,
                'Status': 'ACTIVE'|'ACTIVATING'|'TERMINATED'|'TERMINATING'|'ERROR',
                'GameProperties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'IpAddress': 'string',
                'Port': 123,
                'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
                'CreatorId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def describe_instances(FleetId=None, InstanceId=None, Limit=None, NextToken=None):
    """
    Retrieves information about a fleet's instances, including instance IDs. Use this action to get details on all instances in the fleet or get details on one specific instance.
    To get a specific instance, specify fleet ID and instance ID. To get all instances in a fleet, specify a fleet ID only. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, an  Instance object is returned for each result.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_instances(
        FleetId='string',
        InstanceId='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to retrieve instance information for.
            

    :type InstanceId: string
    :param InstanceId: Unique identifier for an instance to retrieve. Specify an instance ID or leave blank to retrieve all instances in the fleet.

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'Instances': [
            {
                'FleetId': 'string',
                'InstanceId': 'string',
                'IpAddress': 'string',
                'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
                'Type': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
                'Status': 'PENDING'|'ACTIVE'|'TERMINATING',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    PENDING  The instance is in the process of being created and launching server processes as defined in the fleet's runtime configuration.
    ACTIVE  The instance has been successfully created and at least one server process has successfully launched and reported back to Amazon GameLift that it is ready to host a game session. The instance is now considered ready to host game sessions.
    TERMINATING  The instance is in the process of shutting down. This may happen to reduce capacity during a scaling down event or to recycle resources in the event of a problem.
    
    """
    pass

def describe_player_sessions(GameSessionId=None, PlayerId=None, PlayerSessionId=None, PlayerSessionStatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves properties for one or more player sessions. This action can be used in several ways: (1) provide a PlayerSessionId to request properties for a specific player session; (2) provide a GameSessionId to request properties for all player sessions in the specified game session; (3) provide a PlayerId to request properties for all player sessions of a specified player.
    To get game session record(s), specify only one of the following: a player session ID, a game session ID, or a player ID. You can filter this request by player session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  PlayerSession object is returned for each session matching the request.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_player_sessions(
        GameSessionId='string',
        PlayerId='string',
        PlayerSessionId='string',
        PlayerSessionStatusFilter='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type GameSessionId: string
    :param GameSessionId: Unique identifier for the game session to retrieve player sessions for.

    :type PlayerId: string
    :param PlayerId: Unique identifier for a player to retrieve player sessions for.

    :type PlayerSessionId: string
    :param PlayerSessionId: Unique identifier for a player session to retrieve.

    :type PlayerSessionStatusFilter: string
    :param PlayerSessionStatusFilter: Player session status to filter results on.
            Possible player session statuses include the following:
            RESERVED   The player session request has been received, but the player has not yet connected to the server process and/or been validated.
            ACTIVE   The player has been validated by the server process and is currently connected.
            COMPLETED   The player connection has been dropped.
            TIMEDOUT   A player session request was received, but the player did not connect and/or was not validated within the time-out limit (60 seconds).
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. If a player session ID is specified, this parameter is ignored.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored.

    :rtype: dict
    :return: {
        'PlayerSessions': [
            {
                'PlayerSessionId': 'string',
                'PlayerId': 'string',
                'GameSessionId': 'string',
                'FleetId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TerminationTime': datetime(2015, 1, 1),
                'Status': 'RESERVED'|'ACTIVE'|'COMPLETED'|'TIMEDOUT',
                'IpAddress': 'string',
                'Port': 123,
                'PlayerData': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CreatePlayerSession
    CreatePlayerSessions
    DescribePlayerSessions
    
    """
    pass

def describe_runtime_configuration(FleetId=None):
    """
    Retrieves the current runtime configuration for the specified fleet. The runtime configuration tells Amazon GameLift how to launch server processes on instances in the fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_runtime_configuration(
        FleetId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to get the runtime configuration for.
            

    :rtype: dict
    :return: {
        'RuntimeConfiguration': {
            'ServerProcesses': [
                {
                    'LaunchPath': 'string',
                    'Parameters': 'string',
                    'ConcurrentExecutions': 123
                },
            ],
            'MaxConcurrentGameSessionActivations': 123,
            'GameSessionActivationTimeoutSeconds': 123
        }
    }
    
    
    """
    pass

def describe_scaling_policies(FleetId=None, StatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves all scaling policies applied to a fleet.
    To get a fleet's scaling policies, specify the fleet ID. You can filter this request by policy status, such as to retrieve only active scaling policies. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, set of  ScalingPolicy objects is returned for the fleet.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_scaling_policies(
        FleetId='string',
        StatusFilter='ACTIVE'|'UPDATE_REQUESTED'|'UPDATING'|'DELETE_REQUESTED'|'DELETING'|'DELETED'|'ERROR',
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to retrieve scaling policies for.
            

    :type StatusFilter: string
    :param StatusFilter: Scaling policy status to filter results on. A scaling policy is only in force when in an ACTIVE status.
            ACTIVE   The scaling policy is currently in force.
            UPDATEREQUESTED   A request to update the scaling policy has been received.
            UPDATING   A change is being made to the scaling policy.
            DELETEREQUESTED   A request to delete the scaling policy has been received.
            DELETING   The scaling policy is being deleted.
            DELETED   The scaling policy has been deleted.
            ERROR   An error occurred in creating the policy. It should be removed and recreated.
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'ScalingPolicies': [
            {
                'FleetId': 'string',
                'Name': 'string',
                'Status': 'ACTIVE'|'UPDATE_REQUESTED'|'UPDATING'|'DELETE_REQUESTED'|'DELETING'|'DELETED'|'ERROR',
                'ScalingAdjustment': 123,
                'ScalingAdjustmentType': 'ChangeInCapacity'|'ExactCapacity'|'PercentChangeInCapacity',
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
                'Threshold': 123.0,
                'EvaluationPeriods': 123,
                'MetricName': 'ActivatingGameSessions'|'ActiveGameSessions'|'ActiveInstances'|'AvailableGameSessions'|'AvailablePlayerSessions'|'CurrentPlayerSessions'|'IdleInstances'|'PercentAvailableGameSessions'|'PercentIdleInstances'|'QueueDepth'|'WaitTime'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    ACTIVE  The scaling policy is currently in force.
    UPDATE_REQUESTED  A request to update the scaling policy has been received.
    UPDATING  A change is being made to the scaling policy.
    DELETE_REQUESTED  A request to delete the scaling policy has been received.
    DELETING  The scaling policy is being deleted.
    DELETED  The scaling policy has been deleted.
    ERROR  An error occurred in creating the policy. It should be removed and recreated.
    
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

def get_game_session_log_url(GameSessionId=None):
    """
    Retrieves the location of stored game session logs for a specified game session. When a game session is terminated, Amazon GameLift automatically stores the logs in Amazon S3. Use this URL to download the logs.
    See also: AWS API Documentation
    
    
    :example: response = client.get_game_session_log_url(
        GameSessionId='string'
    )
    
    
    :type GameSessionId: string
    :param GameSessionId: [REQUIRED]
            Unique identifier for the game session to get logs for.
            

    :rtype: dict
    :return: {
        'PreSignedUrl': 'string'
    }
    
    
    """
    pass

def get_instance_access(FleetId=None, InstanceId=None):
    """
    Requests remote access to a fleet instance. Remote access is useful for debugging, gathering benchmarking data, or watching activity in real time.
    Access requires credentials that match the operating system of the instance. For a Windows instance, Amazon GameLift returns a user name and password as strings for use with a Windows Remote Desktop client. For a Linux instance, Amazon GameLift returns a user name and RSA private key, also as strings, for use with an SSH client. The private key must be saved in the proper format to a .pem file before using. If you're making this request using the AWS CLI, saving the secret can be handled as part of the GetInstanceAccess request. (See the example later in this topic). For more information on remote access, see Remotely Accessing an Instance .
    To request access to a specific instance, specify the IDs of the instance and the fleet it belongs to. If successful, an  InstanceAccess object is returned containing the instance's IP address and a set of credentials.
    See also: AWS API Documentation
    
    
    :example: response = client.get_instance_access(
        FleetId='string',
        InstanceId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet that contains the instance you want access to. The fleet can be in any of the following statuses: ACTIVATING , ACTIVE , or ERROR . Fleets with an ERROR status may be accessible for a short time before they are deleted.
            

    :type InstanceId: string
    :param InstanceId: [REQUIRED]
            Unique identifier for an instance you want to get access to. You can access an instance in any status.
            

    :rtype: dict
    :return: {
        'InstanceAccess': {
            'FleetId': 'string',
            'InstanceId': 'string',
            'IpAddress': 'string',
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
            'Credentials': {
                'UserName': 'string',
                'Secret': 'string'
            }
        }
    }
    
    
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

def list_aliases(RoutingStrategyType=None, Name=None, Limit=None, NextToken=None):
    """
    Retrieves a collection of alias records for this AWS account. You can filter the result set by alias name and/or routing strategy type. Use the pagination parameters to retrieve results in sequential pages.
    See also: AWS API Documentation
    
    
    :example: response = client.list_aliases(
        RoutingStrategyType='SIMPLE'|'TERMINAL',
        Name='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type RoutingStrategyType: string
    :param RoutingStrategyType: Type of routing to filter results on. Use this parameter to retrieve only aliases of a certain type. To retrieve all aliases, leave this parameter empty.
            Possible routing types include the following:
            SIMPLE   The alias resolves to one specific fleet. Use this type when routing to active fleets.
            TERMINAL   The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
            

    :type Name: string
    :param Name: Descriptive label that is associated with an alias. Alias names do not need to be unique.

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'Aliases': [
            {
                'AliasId': 'string',
                'Name': 'string',
                'AliasArn': 'string',
                'Description': 'string',
                'RoutingStrategy': {
                    'Type': 'SIMPLE'|'TERMINAL',
                    'FleetId': 'string',
                    'Message': 'string'
                },
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CreateAlias
    ListAliases
    DescribeAlias
    UpdateAlias
    DeleteAlias
    
    """
    pass

def list_builds(Status=None, Limit=None, NextToken=None):
    """
    Retrieves build records for all builds associated with the AWS account in use. You can limit results to builds that are in a specific status by using the Status parameter. Use the pagination parameters to retrieve results in a set of sequential pages.
    See also: AWS API Documentation
    
    
    :example: response = client.list_builds(
        Status='INITIALIZED'|'READY'|'FAILED',
        Limit=123,
        NextToken='string'
    )
    
    
    :type Status: string
    :param Status: Build status to filter results by. To retrieve all builds, leave this parameter empty.
            Possible build statuses include the following:
            INITIALIZED   A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
            READY   The game build has been successfully uploaded. You can now create new fleets for this build.
            FAILED   The game build upload failed. You cannot create new fleets for this build.
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'Builds': [
            {
                'BuildId': 'string',
                'Name': 'string',
                'Version': 'string',
                'Status': 'INITIALIZED'|'READY'|'FAILED',
                'SizeOnDisk': 123,
                'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CreateBuild
    ListBuilds
    DescribeBuild
    UpdateBuild
    DeleteBuild
    
    """
    pass

def list_fleets(BuildId=None, Limit=None, NextToken=None):
    """
    Retrieves a collection of fleet records for this AWS account. You can filter the result set by build ID. Use the pagination parameters to retrieve results in sequential pages.
    See also: AWS API Documentation
    
    
    :example: response = client.list_fleets(
        BuildId='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type BuildId: string
    :param BuildId: Unique identifier for a build to return fleets for. Use this parameter to return only fleets using the specified build. To retrieve all fleets, leave this parameter empty.

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'FleetIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def put_scaling_policy(Name=None, FleetId=None, ScalingAdjustment=None, ScalingAdjustmentType=None, Threshold=None, ComparisonOperator=None, EvaluationPeriods=None, MetricName=None):
    """
    Creates or updates a scaling policy for a fleet. An active scaling policy prompts Amazon GameLift to track a certain metric for a fleet and automatically change the fleet's capacity in specific circumstances. Each scaling policy contains one rule statement. Fleets can have multiple scaling policies in force simultaneously.
    A scaling policy rule statement has the following structure:
    If [MetricName] is [ComparisonOperator] [Threshold] for [EvaluationPeriods] minutes, then [ScalingAdjustmentType] to/by [ScalingAdjustment] .
    For example, this policy: "If the number of idle instances exceeds 20 for more than 15 minutes, then reduce the fleet capacity by 10 instances" could be implemented as the following rule statement:
    If [IdleInstances] is [GreaterThanOrEqualToThreshold] [20] for [15] minutes, then [ChangeInCapacity] by [-10].
    To create or update a scaling policy, specify a unique combination of name and fleet ID, and set the rule values. All parameters for this action are required. If successful, the policy name is returned. Scaling policies cannot be suspended or made inactive. To stop enforcing a scaling policy, call  DeleteScalingPolicy .
    See also: AWS API Documentation
    
    
    :example: response = client.put_scaling_policy(
        Name='string',
        FleetId='string',
        ScalingAdjustment=123,
        ScalingAdjustmentType='ChangeInCapacity'|'ExactCapacity'|'PercentChangeInCapacity',
        Threshold=123.0,
        ComparisonOperator='GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
        EvaluationPeriods=123,
        MetricName='ActivatingGameSessions'|'ActiveGameSessions'|'ActiveInstances'|'AvailableGameSessions'|'AvailablePlayerSessions'|'CurrentPlayerSessions'|'IdleInstances'|'PercentAvailableGameSessions'|'PercentIdleInstances'|'QueueDepth'|'WaitTime'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Descriptive label that is associated with a scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.
            

    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to apply this policy to.
            

    :type ScalingAdjustment: integer
    :param ScalingAdjustment: [REQUIRED]
            Amount of adjustment to make, based on the scaling adjustment type.
            

    :type ScalingAdjustmentType: string
    :param ScalingAdjustmentType: [REQUIRED]
            Type of adjustment to make to a fleet's instance count (see FleetCapacity ):
            ChangeInCapacity   add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
            ExactCapacity   set the instance count to the scaling adjustment value.
            PercentChangeInCapacity   increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of '-10' scales the fleet down by 10%.
            

    :type Threshold: float
    :param Threshold: [REQUIRED]
            Metric value used to trigger a scaling event.
            

    :type ComparisonOperator: string
    :param ComparisonOperator: [REQUIRED]
            Comparison operator to use when measuring the metric against the threshold value.
            

    :type EvaluationPeriods: integer
    :param EvaluationPeriods: [REQUIRED]
            Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
            

    :type MetricName: string
    :param MetricName: [REQUIRED]
            Name of the Amazon GameLift-defined metric that is used to trigger an adjustment.
            ActivatingGameSessions   number of game sessions in the process of being created (game session status = ACTIVATING ).
            ActiveGameSessions   number of game sessions currently running (game session status = ACTIVE ).
            CurrentPlayerSessions   number of active or reserved player sessions (player session status = ACTIVE or RESERVED ).
            AvailablePlayerSessions   number of player session slots currently available in active game sessions across the fleet, calculated by subtracting a game session's current player session count from its maximum player session count. This number includes game sessions that are not currently accepting players (game session PlayerSessionCreationPolicy = DENY_ALL ).
            ActiveInstances   number of instances currently running a game session.
            IdleInstances   number of instances not currently running a game session.
            

    :rtype: dict
    :return: {
        'Name': 'string'
    }
    
    
    """
    pass

def request_upload_credentials(BuildId=None):
    """
    See also: AWS API Documentation
    
    
    :example: response = client.request_upload_credentials(
        BuildId='string'
    )
    
    
    :type BuildId: string
    :param BuildId: [REQUIRED]
            Unique identifier for a build to get credentials for.
            

    :rtype: dict
    :return: {
        'UploadCredentials': {
            'AccessKeyId': 'string',
            'SecretAccessKey': 'string',
            'SessionToken': 'string'
        },
        'StorageLocation': {
            'Bucket': 'string',
            'Key': 'string',
            'RoleArn': 'string'
        }
    }
    
    
    """
    pass

def resolve_alias(AliasId=None):
    """
    Retrieves the fleet ID that a specified alias is currently pointing to.
    See also: AWS API Documentation
    
    
    :example: response = client.resolve_alias(
        AliasId='string'
    )
    
    
    :type AliasId: string
    :param AliasId: [REQUIRED]
            Unique identifier for the alias you want to resolve.
            

    :rtype: dict
    :return: {
        'FleetId': 'string'
    }
    
    
    """
    pass

def search_game_sessions(FleetId=None, AliasId=None, FilterExpression=None, SortExpression=None, Limit=None, NextToken=None):
    """
    Retrieves a set of game sessions that match a set of search criteria and sorts them in a specified order. Currently a game session search is limited to a single fleet. Search results include only game sessions that are in ACTIVE status. If you need to retrieve game sessions with a status other than active, use  DescribeGameSessions . If you need to retrieve the protection policy for each game session, use  DescribeGameSessionDetails .
    You can search or sort by the following game session attributes:
    To search or sort, specify either a fleet ID or an alias ID, and provide a search filter expression, a sort expression, or both. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a collection of  GameSession objects matching the request is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.search_game_sessions(
        FleetId='string',
        AliasId='string',
        FilterExpression='string',
        SortExpression='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: Unique identifier for a fleet to search for active game sessions. Each request must reference either a fleet ID or alias ID, but not both.

    :type AliasId: string
    :param AliasId: Unique identifier for an alias associated with the fleet to search for active game sessions. Each request must reference either a fleet ID or alias ID, but not both.

    :type FilterExpression: string
    :param FilterExpression: String containing the search criteria for the session search. If no filter expression is included, the request returns results for all game sessions in the fleet that are in ACTIVE status.
            A filter expression can contain one or multiple conditions. Each condition consists of the following:
            Operand -- Name of a game session attribute. Valid values are gameSessionName , gameSessionId , creationTimeMillis , playerSessionCount , maximumSessions , hasAvailablePlayerSessions .
            Comparator -- Valid comparators are: = , ```` , ```` , ```` , = , = .
            Value -- Value to be searched for. Values can be numbers, boolean values (true/false) or strings. String values are case sensitive, enclosed in single quotes. Special characters must be escaped. Boolean and string values can only be used with the comparators = and ```` . For example, the following filter expression searches on gameSessionName : 'FilterExpression': 'gameSessionName = 'Matt\\'s Awesome Game 1'' .
            To chain multiple conditions in a single expression, use the logical keywords AND , OR , and NOT and parentheses as needed. For example: x AND y AND NOT z , NOT (x OR y) .
            Session search evaluates conditions from left to right using the following precedence rules:
            = , ```` , ```` , ```` , = , =
            Parentheses
            NOT
            AND
            OR
            For example, this filter expression retrieves game sessions hosting at least ten players that have an open player slot: 'maximumSessions=10 AND hasAvailablePlayerSessions=true' .
            

    :type SortExpression: string
    :param SortExpression: Instructions on how to sort the search results. If no sort expression is included, the request returns results in random order. A sort expression consists of the following elements:
            Operand -- Name of a game session attribute. Valid values are gameSessionName , gameSessionId , creationTimeMillis , playerSessionCount , maximumSessions , hasAvailablePlayerSessions .
            Order -- Valid sort orders are ASC (ascending) and DESC (descending).
            For example, this sort expression returns the oldest active sessions first: 'SortExpression': 'creationTimeMillis ASC' . Results with a null value for the sort operand are returned at the end of the list.
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. The maximum number of results returned is 20, even if this value is not set or is set higher than 20.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'GameSessions': [
            {
                'GameSessionId': 'string',
                'Name': 'string',
                'FleetId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TerminationTime': datetime(2015, 1, 1),
                'CurrentPlayerSessionCount': 123,
                'MaximumPlayerSessionCount': 123,
                'Status': 'ACTIVE'|'ACTIVATING'|'TERMINATED'|'TERMINATING'|'ERROR',
                'GameProperties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'IpAddress': 'string',
                'Port': 123,
                'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
                'CreatorId': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    FleetId (string) -- Unique identifier for a fleet to search for active game sessions. Each request must reference either a fleet ID or alias ID, but not both.
    AliasId (string) -- Unique identifier for an alias associated with the fleet to search for active game sessions. Each request must reference either a fleet ID or alias ID, but not both.
    FilterExpression (string) -- String containing the search criteria for the session search. If no filter expression is included, the request returns results for all game sessions in the fleet that are in ACTIVE status.
    A filter expression can contain one or multiple conditions. Each condition consists of the following:
    
    Operand -- Name of a game session attribute. Valid values are gameSessionName , gameSessionId , creationTimeMillis , playerSessionCount , maximumSessions , hasAvailablePlayerSessions .
    Comparator -- Valid comparators are: = , ```` , ```` , ```` , = , = .
    Value -- Value to be searched for. Values can be numbers, boolean values (true/false) or strings. String values are case sensitive, enclosed in single quotes. Special characters must be escaped. Boolean and string values can only be used with the comparators = and ```` . For example, the following filter expression searches on gameSessionName : "FilterExpression": "gameSessionName = 'Matt\\'s Awesome Game 1'" .
    
    To chain multiple conditions in a single expression, use the logical keywords AND , OR , and NOT and parentheses as needed. For example: x AND y AND NOT z , NOT (x OR y) .
    Session search evaluates conditions from left to right using the following precedence rules:
    
    = , ```` , ```` , ```` , = , =
    Parentheses
    NOT
    AND
    OR
    
    For example, this filter expression retrieves game sessions hosting at least ten players that have an open player slot: "maximumSessions=10 AND hasAvailablePlayerSessions=true" .
    
    SortExpression (string) -- Instructions on how to sort the search results. If no sort expression is included, the request returns results in random order. A sort expression consists of the following elements:
    
    Operand -- Name of a game session attribute. Valid values are gameSessionName , gameSessionId , creationTimeMillis , playerSessionCount , maximumSessions , hasAvailablePlayerSessions .
    Order -- Valid sort orders are ASC (ascending) and DESC (descending).
    
    For example, this sort expression returns the oldest active sessions first: "SortExpression": "creationTimeMillis ASC" . Results with a null value for the sort operand are returned at the end of the list.
    
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. The maximum number of results returned is 20, even if this value is not set or is set higher than 20.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.
    
    """
    pass

def start_game_session_placement(PlacementId=None, GameSessionQueueName=None, GameProperties=None, MaximumPlayerSessionCount=None, GameSessionName=None, PlayerLatencies=None, DesiredPlayerSessions=None):
    """
    Places a request for a new game session in a queue (see  CreateGameSessionQueue ). When processing a placement request, Amazon GameLift searches for available resources on the queue's destinations, scanning each until it finds resources or the placement request times out.
    A game session placement request can also request player sessions. When a new game session is successfully created, Amazon GameLift creates a player session for each player included in the request.
    When placing a game session, by default Amazon GameLift tries each fleet in the order they are listed in the queue configuration. Ideally, a queue's destinations are listed in preference order.
    Alternatively, when requesting a game session with players, you can also provide latency data for each player in relevant regions. Latency data indicates the performance lag a player experiences when connected to a fleet in the region. Amazon GameLift uses latency data to reorder the list of destinations to place the game session in a region with minimal lag. If latency data is provided for multiple players, Amazon GameLift calculates each region's average lag for all players and reorders to get the best game play across all players.
    To place a new game session request, specify the following:
    If successful, a new game session placement is created.
    To track the status of a placement request, call  DescribeGameSessionPlacement and check the request's status. If the status is Fulfilled , a new game session has been created and a game session ARN and region are referenced. If the placement request times out, you can resubmit the request or retry it with a different queue.
    See also: AWS API Documentation
    
    
    :example: response = client.start_game_session_placement(
        PlacementId='string',
        GameSessionQueueName='string',
        GameProperties=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        MaximumPlayerSessionCount=123,
        GameSessionName='string',
        PlayerLatencies=[
            {
                'PlayerId': 'string',
                'RegionIdentifier': 'string',
                'LatencyInMilliseconds': ...
            },
        ],
        DesiredPlayerSessions=[
            {
                'PlayerId': 'string',
                'PlayerData': 'string'
            },
        ]
    )
    
    
    :type PlacementId: string
    :param PlacementId: [REQUIRED]
            Unique identifier to assign to the new game session placement. This value is developer-defined. The value must be unique across all regions and cannot be reused unless you are resubmitting a canceled or timed-out placement request.
            

    :type GameSessionQueueName: string
    :param GameSessionQueueName: [REQUIRED]
            Name of the queue to use to place the new game session.
            

    :type GameProperties: list
    :param GameProperties: Set of developer-defined properties for a game session. These properties are passed to the server process hosting the game session.
            (dict) --Set of key-value pairs containing information a server process requires to set up a game session. This object allows you to pass in any set of data needed for your game. For more information, see the Amazon GameLift Developer Guide .
            Key (string) -- [REQUIRED]TBD
            Value (string) -- [REQUIRED]TBD
            
            

    :type MaximumPlayerSessionCount: integer
    :param MaximumPlayerSessionCount: [REQUIRED]
            Maximum number of players that can be connected simultaneously to the game session.
            

    :type GameSessionName: string
    :param GameSessionName: Descriptive label that is associated with a game session. Session names do not need to be unique.

    :type PlayerLatencies: list
    :param PlayerLatencies: Set of values, expressed in milliseconds, indicating the amount of latency that players are experiencing when connected to AWS regions. This information is used to try to place the new game session where it can offer the best possible gameplay experience for the players.
            (dict) --Regional latency information for a player, used when requesting a new game session with StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified region. The relative difference between a player's latency values for multiple regions are used to determine which fleets are best suited to place a new game session for the player.
            PlayerId (string) --Unique identifier for a player associated with the latency data.
            RegionIdentifier (string) --Name of the region that is associated with the latency value.
            LatencyInMilliseconds (float) --Amount of time that represents the time lag experienced by the player when connected to the specified region.
            
            

    :type DesiredPlayerSessions: list
    :param DesiredPlayerSessions: Set of information on each player to create a player session for.
            (dict) --Player information for use when creating player sessions using a game session placement request with StartGameSessionPlacement .
            PlayerId (string) --Unique identifier for a player to associate with the player session.
            PlayerData (string) --Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.
            
            

    :rtype: dict
    :return: {
        'GameSessionPlacement': {
            'PlacementId': 'string',
            'GameSessionQueueName': 'string',
            'Status': 'PENDING'|'FULFILLED'|'CANCELLED'|'TIMED_OUT',
            'GameProperties': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'MaximumPlayerSessionCount': 123,
            'GameSessionName': 'string',
            'GameSessionId': 'string',
            'GameSessionArn': 'string',
            'GameSessionRegion': 'string',
            'PlayerLatencies': [
                {
                    'PlayerId': 'string',
                    'RegionIdentifier': 'string',
                    'LatencyInMilliseconds': ...
                },
            ],
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'IpAddress': 'string',
            'Port': 123,
            'PlacedPlayerSessions': [
                {
                    'PlayerId': 'string',
                    'PlayerSessionId': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    PlacementId (string) -- [REQUIRED]
    Unique identifier to assign to the new game session placement. This value is developer-defined. The value must be unique across all regions and cannot be reused unless you are resubmitting a canceled or timed-out placement request.
    
    GameSessionQueueName (string) -- [REQUIRED]
    Name of the queue to use to place the new game session.
    
    GameProperties (list) -- Set of developer-defined properties for a game session. These properties are passed to the server process hosting the game session.
    
    (dict) --Set of key-value pairs containing information a server process requires to set up a game session. This object allows you to pass in any set of data needed for your game. For more information, see the Amazon GameLift Developer Guide .
    
    Key (string) -- [REQUIRED]TBD
    
    Value (string) -- [REQUIRED]TBD
    
    
    
    
    
    MaximumPlayerSessionCount (integer) -- [REQUIRED]
    Maximum number of players that can be connected simultaneously to the game session.
    
    GameSessionName (string) -- Descriptive label that is associated with a game session. Session names do not need to be unique.
    PlayerLatencies (list) -- Set of values, expressed in milliseconds, indicating the amount of latency that players are experiencing when connected to AWS regions. This information is used to try to place the new game session where it can offer the best possible gameplay experience for the players.
    
    (dict) --Regional latency information for a player, used when requesting a new game session with  StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified region. The relative difference between a player's latency values for multiple regions are used to determine which fleets are best suited to place a new game session for the player.
    
    PlayerId (string) --Unique identifier for a player associated with the latency data.
    
    RegionIdentifier (string) --Name of the region that is associated with the latency value.
    
    LatencyInMilliseconds (float) --Amount of time that represents the time lag experienced by the player when connected to the specified region.
    
    
    
    
    
    DesiredPlayerSessions (list) -- Set of information on each player to create a player session for.
    
    (dict) --Player information for use when creating player sessions using a game session placement request with  StartGameSessionPlacement .
    
    PlayerId (string) --Unique identifier for a player to associate with the player session.
    
    PlayerData (string) --Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.
    
    
    
    
    
    
    """
    pass

def stop_game_session_placement(PlacementId=None):
    """
    Cancels a game session placement that is in Pending status. To stop a placement, provide the placement ID values. If successful, the placement is moved to Cancelled status.
    See also: AWS API Documentation
    
    
    :example: response = client.stop_game_session_placement(
        PlacementId='string'
    )
    
    
    :type PlacementId: string
    :param PlacementId: [REQUIRED]
            Unique identifier for a game session placement to cancel.
            

    :rtype: dict
    :return: {
        'GameSessionPlacement': {
            'PlacementId': 'string',
            'GameSessionQueueName': 'string',
            'Status': 'PENDING'|'FULFILLED'|'CANCELLED'|'TIMED_OUT',
            'GameProperties': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'MaximumPlayerSessionCount': 123,
            'GameSessionName': 'string',
            'GameSessionId': 'string',
            'GameSessionArn': 'string',
            'GameSessionRegion': 'string',
            'PlayerLatencies': [
                {
                    'PlayerId': 'string',
                    'RegionIdentifier': 'string',
                    'LatencyInMilliseconds': ...
                },
            ],
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'IpAddress': 'string',
            'Port': 123,
            'PlacedPlayerSessions': [
                {
                    'PlayerId': 'string',
                    'PlayerSessionId': 'string'
                },
            ]
        }
    }
    
    
    """
    pass

def update_alias(AliasId=None, Name=None, Description=None, RoutingStrategy=None):
    """
    Updates properties for a fleet alias. To update properties, specify the alias ID to be updated and provide the information to be changed. To reassign an alias to another fleet, provide an updated routing strategy. If successful, the updated alias record is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.update_alias(
        AliasId='string',
        Name='string',
        Description='string',
        RoutingStrategy={
            'Type': 'SIMPLE'|'TERMINAL',
            'FleetId': 'string',
            'Message': 'string'
        }
    )
    
    
    :type AliasId: string
    :param AliasId: [REQUIRED]
            Unique identifier for a fleet alias. Specify the alias you want to update.
            

    :type Name: string
    :param Name: Descriptive label that is associated with an alias. Alias names do not need to be unique.

    :type Description: string
    :param Description: Human-readable description of an alias.

    :type RoutingStrategy: dict
    :param RoutingStrategy: Object that specifies the fleet and routing type to use for the alias.
            Type (string) --Type of routing strategy.
            Possible routing types include the following:
            SIMPLE   The alias resolves to one specific fleet. Use this type when routing to active fleets.
            TERMINAL   The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
            FleetId (string) --Unique identifier for a fleet that the alias points to.
            Message (string) --Message text to be used with a terminal routing strategy.
            

    :rtype: dict
    :return: {
        'Alias': {
            'AliasId': 'string',
            'Name': 'string',
            'AliasArn': 'string',
            'Description': 'string',
            'RoutingStrategy': {
                'Type': 'SIMPLE'|'TERMINAL',
                'FleetId': 'string',
                'Message': 'string'
            },
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    SIMPLE  The alias resolves to one specific fleet. Use this type when routing to active fleets.
    TERMINAL  The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
    
    """
    pass

def update_build(BuildId=None, Name=None, Version=None):
    """
    Updates metadata in a build record, including the build name and version. To update the metadata, specify the build ID to update and provide the new values. If successful, a build object containing the updated metadata is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.update_build(
        BuildId='string',
        Name='string',
        Version='string'
    )
    
    
    :type BuildId: string
    :param BuildId: [REQUIRED]
            Unique identifier for a build to update.
            

    :type Name: string
    :param Name: Descriptive label that is associated with a build. Build names do not need to be unique.

    :type Version: string
    :param Version: Version that is associated with this build. Version strings do not need to be unique.

    :rtype: dict
    :return: {
        'Build': {
            'BuildId': 'string',
            'Name': 'string',
            'Version': 'string',
            'Status': 'INITIALIZED'|'READY'|'FAILED',
            'SizeOnDisk': 123,
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
            'CreationTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    INITIALIZED  A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
    READY  The game build has been successfully uploaded. You can now create new fleets for this build.
    FAILED  The game build upload failed. You cannot create new fleets for this build.
    
    """
    pass

def update_fleet_attributes(FleetId=None, Name=None, Description=None, NewGameSessionProtectionPolicy=None, ResourceCreationLimitPolicy=None, MetricGroups=None):
    """
    Updates fleet properties, including name and description, for a fleet. To update metadata, specify the fleet ID and the property values you want to change. If successful, the fleet ID for the updated fleet is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.update_fleet_attributes(
        FleetId='string',
        Name='string',
        Description='string',
        NewGameSessionProtectionPolicy='NoProtection'|'FullProtection',
        ResourceCreationLimitPolicy={
            'NewGameSessionsPerCreator': 123,
            'PolicyPeriodInMinutes': 123
        },
        MetricGroups=[
            'string',
        ]
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to update attribute metadata for.
            

    :type Name: string
    :param Name: Descriptive label that is associated with a fleet. Fleet names do not need to be unique.

    :type Description: string
    :param Description: Human-readable description of a fleet.

    :type NewGameSessionProtectionPolicy: string
    :param NewGameSessionProtectionPolicy: Game session protection policy to apply to all new instances created in this fleet. Instances that already exist are not affected. You can set protection for individual instances using UpdateGameSession .
            NoProtection   The game session can be terminated during a scale-down event.
            FullProtection   If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
            

    :type ResourceCreationLimitPolicy: dict
    :param ResourceCreationLimitPolicy: Policy that limits the number of game sessions an individual player can create over a span of time.
            NewGameSessionsPerCreator (integer) --Maximum number of game sessions that an individual can create during the policy period.
            PolicyPeriodInMinutes (integer) --Time span used in evaluating the resource creation limit policy.
            

    :type MetricGroups: list
    :param MetricGroups: Names of metric groups to include this fleet with. A fleet metric group is used in Amazon CloudWatch to aggregate metrics from multiple fleets. Use an existing metric group name to add this fleet to the group, or use a new name to create a new metric group. Currently, a fleet can only be included in one metric group at a time.
            (string) --
            

    :rtype: dict
    :return: {
        'FleetId': 'string'
    }
    
    
    """
    pass

def update_fleet_capacity(FleetId=None, DesiredInstances=None, MinSize=None, MaxSize=None):
    """
    Updates capacity settings for a fleet. Use this action to specify the number of EC2 instances (hosts) that you want this fleet to contain. Before calling this action, you may want to call  DescribeEC2InstanceLimits to get the maximum capacity based on the fleet's EC2 instance type.
    If you're using autoscaling (see  PutScalingPolicy ), you may want to specify a minimum and/or maximum capacity. If you don't provide these, autoscaling can set capacity anywhere between zero and the service limits .
    To update fleet capacity, specify the fleet ID and the number of instances you want the fleet to host. If successful, Amazon GameLift starts or terminates instances so that the fleet's active instance count matches the desired instance count. You can view a fleet's current capacity information by calling  DescribeFleetCapacity . If the desired instance count is higher than the instance type's limit, the "Limit Exceeded" exception occurs.
    See also: AWS API Documentation
    
    
    :example: response = client.update_fleet_capacity(
        FleetId='string',
        DesiredInstances=123,
        MinSize=123,
        MaxSize=123
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to update capacity for.
            

    :type DesiredInstances: integer
    :param DesiredInstances: Number of EC2 instances you want this fleet to host.

    :type MinSize: integer
    :param MinSize: Minimum value allowed for the fleet's instance count. Default if not set is 0.

    :type MaxSize: integer
    :param MaxSize: Maximum value allowed for the fleet's instance count. Default if not set is 1.

    :rtype: dict
    :return: {
        'FleetId': 'string'
    }
    
    
    """
    pass

def update_fleet_port_settings(FleetId=None, InboundPermissionAuthorizations=None, InboundPermissionRevocations=None):
    """
    Updates port settings for a fleet. To update settings, specify the fleet ID to be updated and list the permissions you want to update. List the permissions you want to add in InboundPermissionAuthorizations , and permissions you want to remove in InboundPermissionRevocations . Permissions to be removed must match existing fleet permissions. If successful, the fleet ID for the updated fleet is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.update_fleet_port_settings(
        FleetId='string',
        InboundPermissionAuthorizations=[
            {
                'FromPort': 123,
                'ToPort': 123,
                'IpRange': 'string',
                'Protocol': 'TCP'|'UDP'
            },
        ],
        InboundPermissionRevocations=[
            {
                'FromPort': 123,
                'ToPort': 123,
                'IpRange': 'string',
                'Protocol': 'TCP'|'UDP'
            },
        ]
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to update port settings for.
            

    :type InboundPermissionAuthorizations: list
    :param InboundPermissionAuthorizations: Collection of port settings to be added to the fleet record.
            (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on Amazon GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet's allowed ranges. This combination is included in the GameSession object.
            FromPort (integer) -- [REQUIRED]Starting value for a range of allowed port numbers.
            ToPort (integer) -- [REQUIRED]Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
            IpRange (string) -- [REQUIRED]Range of allowed IP addresses. This value must be expressed in CIDR notation. Example: '000.000.000.000/[subnet mask] ' or optionally the shortened version '0.0.0.0/[subnet mask] '.
            Protocol (string) -- [REQUIRED]Network communication protocol used by the fleet.
            
            

    :type InboundPermissionRevocations: list
    :param InboundPermissionRevocations: Collection of port settings to be removed from the fleet record.
            (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on Amazon GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet's allowed ranges. This combination is included in the GameSession object.
            FromPort (integer) -- [REQUIRED]Starting value for a range of allowed port numbers.
            ToPort (integer) -- [REQUIRED]Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
            IpRange (string) -- [REQUIRED]Range of allowed IP addresses. This value must be expressed in CIDR notation. Example: '000.000.000.000/[subnet mask] ' or optionally the shortened version '0.0.0.0/[subnet mask] '.
            Protocol (string) -- [REQUIRED]Network communication protocol used by the fleet.
            
            

    :rtype: dict
    :return: {
        'FleetId': 'string'
    }
    
    
    """
    pass

def update_game_session(GameSessionId=None, MaximumPlayerSessionCount=None, Name=None, PlayerSessionCreationPolicy=None, ProtectionPolicy=None):
    """
    Updates game session properties. This includes the session name, maximum player count, protection policy, which controls whether or not an active game session can be terminated during a scale-down event, and the player session creation policy, which controls whether or not new players can join the session. To update a game session, specify the game session ID and the values you want to change. If successful, an updated  GameSession object is returned.
    See also: AWS API Documentation
    
    
    :example: response = client.update_game_session(
        GameSessionId='string',
        MaximumPlayerSessionCount=123,
        Name='string',
        PlayerSessionCreationPolicy='ACCEPT_ALL'|'DENY_ALL',
        ProtectionPolicy='NoProtection'|'FullProtection'
    )
    
    
    :type GameSessionId: string
    :param GameSessionId: [REQUIRED]
            Unique identifier for the game session to update.
            

    :type MaximumPlayerSessionCount: integer
    :param MaximumPlayerSessionCount: Maximum number of players that can be connected simultaneously to the game session.

    :type Name: string
    :param Name: Descriptive label that is associated with a game session. Session names do not need to be unique.

    :type PlayerSessionCreationPolicy: string
    :param PlayerSessionCreationPolicy: Policy determining whether or not the game session accepts new players.

    :type ProtectionPolicy: string
    :param ProtectionPolicy: Game session protection policy to apply to this game session only.
            NoProtection   The game session can be terminated during a scale-down event.
            FullProtection   If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
            

    :rtype: dict
    :return: {
        'GameSession': {
            'GameSessionId': 'string',
            'Name': 'string',
            'FleetId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TerminationTime': datetime(2015, 1, 1),
            'CurrentPlayerSessionCount': 123,
            'MaximumPlayerSessionCount': 123,
            'Status': 'ACTIVE'|'ACTIVATING'|'TERMINATED'|'TERMINATING'|'ERROR',
            'GameProperties': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'IpAddress': 'string',
            'Port': 123,
            'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
            'CreatorId': 'string'
        }
    }
    
    
    """
    pass

def update_game_session_queue(Name=None, TimeoutInSeconds=None, PlayerLatencyPolicies=None, Destinations=None):
    """
    Updates settings for a game session queue, which determines how new game session requests in the queue are processed. To update settings, specify the queue name to be updated and provide the new settings. When updating destinations, provide a complete list of destinations.
    See also: AWS API Documentation
    
    
    :example: response = client.update_game_session_queue(
        Name='string',
        TimeoutInSeconds=123,
        PlayerLatencyPolicies=[
            {
                'MaximumIndividualPlayerLatencyMilliseconds': 123,
                'PolicyDurationSeconds': 123
            },
        ],
        Destinations=[
            {
                'DestinationArn': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Descriptive label that is associated with queue. Queue names must be unique within each region.
            

    :type TimeoutInSeconds: integer
    :param TimeoutInSeconds: Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.

    :type PlayerLatencyPolicies: list
    :param PlayerLatencyPolicies: Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. When updating policies, provide a complete collection of policies.
            (dict) --Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
            Latency policy-related operations include:
            CreateGameSessionQueue
            UpdateGameSessionQueue
            StartGameSessionPlacement
            MaximumIndividualPlayerLatencyMilliseconds (integer) --The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
            PolicyDurationSeconds (integer) --The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
            
            

    :type Destinations: list
    :param Destinations: List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order. When updating this list, provide a complete list of destinations.
            (dict) --Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue.
            DestinationArn (string) --Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a region name, provide a unique identifier across all regions.
            
            

    :rtype: dict
    :return: {
        'GameSessionQueue': {
            'Name': 'string',
            'GameSessionQueueArn': 'string',
            'TimeoutInSeconds': 123,
            'PlayerLatencyPolicies': [
                {
                    'MaximumIndividualPlayerLatencyMilliseconds': 123,
                    'PolicyDurationSeconds': 123
                },
            ],
            'Destinations': [
                {
                    'DestinationArn': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    CreateGameSessionQueue
    UpdateGameSessionQueue
    StartGameSessionPlacement
    
    """
    pass

def update_runtime_configuration(FleetId=None, RuntimeConfiguration=None):
    """
    Updates the current runtime configuration for the specified fleet, which tells Amazon GameLift how to launch server processes on instances in the fleet. You can update a fleet's runtime configuration at any time after the fleet is created; it does not need to be in an ACTIVE status.
    To update runtime configuration, specify the fleet ID and provide a RuntimeConfiguration object with the updated collection of server process configurations.
    Each instance in a Amazon GameLift fleet checks regularly for an updated runtime configuration and changes how it launches server processes to comply with the latest version. Existing server processes are not affected by the update; they continue to run until they end, while Amazon GameLift simply adds new server processes to fit the current runtime configuration. As a result, the runtime configuration changes are applied gradually as existing processes shut down and new processes are launched in Amazon GameLift's normal process recycling activity.
    See also: AWS API Documentation
    
    
    :example: response = client.update_runtime_configuration(
        FleetId='string',
        RuntimeConfiguration={
            'ServerProcesses': [
                {
                    'LaunchPath': 'string',
                    'Parameters': 'string',
                    'ConcurrentExecutions': 123
                },
            ],
            'MaxConcurrentGameSessionActivations': 123,
            'GameSessionActivationTimeoutSeconds': 123
        }
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to update runtime configuration for.
            

    :type RuntimeConfiguration: dict
    :param RuntimeConfiguration: [REQUIRED]
            Instructions for launching server processes on each instance in the fleet. The runtime configuration for a fleet has a collection of server process configurations, one for each type of server process to run on an instance. A server process configuration specifies the location of the server executable, launch parameters, and the number of concurrent processes with that configuration to maintain on each instance.
            ServerProcesses (list) --Collection of server process configurations that describe which server processes to run on each instance in a fleet.
            (dict) --A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet's `` RuntimeConfiguration `` .
            LaunchPath (string) -- [REQUIRED]Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances C:\game , and for Linux instances /local/game . A Windows game build with an executable file located at MyGame\latest\server.exe must have a launch path of 'C:\game\MyGame\latest\server.exe '. A Linux game build with an executable file located at MyGame/latest/server.exe must have a launch path of '/local/game/MyGame/latest/server.exe '.
            Parameters (string) --Optional list of parameters to pass to the server executable on launch.
            ConcurrentExecutions (integer) -- [REQUIRED]Number of server processes using this configuration to run concurrently on an instance.
            
            MaxConcurrentGameSessionActivations (integer) --Maximum number of game sessions with status ACTIVATING to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.
            GameSessionActivationTimeoutSeconds (integer) --Maximum amount of time (in seconds) that a game session can remain in status ACTIVATING. If the game session is not active before the timeout, activation is terminated and the game session status is changed to TERMINATED.
            

    :rtype: dict
    :return: {
        'RuntimeConfiguration': {
            'ServerProcesses': [
                {
                    'LaunchPath': 'string',
                    'Parameters': 'string',
                    'ConcurrentExecutions': 123
                },
            ],
            'MaxConcurrentGameSessionActivations': 123,
            'GameSessionActivationTimeoutSeconds': 123
        }
    }
    
    
    """
    pass

