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

def accept_match(TicketId=None, PlayerIds=None, AcceptanceType=None):
    """
    Registers a player's acceptance or rejection of a proposed FlexMatch match. A matchmaking configuration may require player acceptance; if so, then matches built with that configuration cannot be completed unless all players accept the proposed match within a specified time limit.
    When FlexMatch builds a match, all the matchmaking tickets involved in the proposed match are placed into status REQUIRES_ACCEPTANCE . This is a trigger for your game to get acceptance from all players in the ticket. Acceptances are only valid for tickets when they are in this status; all other acceptances result in an error.
    To register acceptance, specify the ticket ID, a response, and one or more players. Once all players have registered acceptance, the matchmaking tickets advance to status PLACING , where a new game session is created for the match.
    If any player rejects the match, or if acceptances are not received before a specified timeout, the proposed match is dropped. The matchmaking tickets are then handled in one of two ways: For tickets where all players accepted the match, the ticket status is returned to SEARCHING to find a new match. For tickets where one or more players failed to accept the match, the ticket status is set to FAILED , and processing is terminated. A new matchmaking request for these players can be submitted as needed.
    Matchmaking-related operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.accept_match(
        TicketId='string',
        PlayerIds=[
            'string',
        ],
        AcceptanceType='ACCEPT'|'REJECT'
    )
    
    
    :type TicketId: string
    :param TicketId: [REQUIRED]
            Unique identifier for a matchmaking ticket. The ticket must be in status REQUIRES_ACCEPTANCE ; otherwise this request will fail.
            

    :type PlayerIds: list
    :param PlayerIds: [REQUIRED]
            Unique identifier for a player delivering the response. This parameter can include one or multiple player IDs.
            (string) --
            

    :type AcceptanceType: string
    :param AcceptanceType: [REQUIRED]
            Player response to the proposed match.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    TicketId (string) -- [REQUIRED]
    Unique identifier for a matchmaking ticket. The ticket must be in status REQUIRES_ACCEPTANCE ; otherwise this request will fail.
    
    PlayerIds (list) -- [REQUIRED]
    Unique identifier for a player delivering the response. This parameter can include one or multiple player IDs.
    
    (string) --
    
    
    AcceptanceType (string) -- [REQUIRED]
    Player response to the proposed match.
    
    
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

def create_alias(Name=None, Description=None, RoutingStrategy=None):
    """
    Creates an alias for a fleet. In most situations, you can use an alias ID in place of a fleet ID. By using a fleet alias instead of a specific fleet ID, you can switch gameplay and players to a new fleet without changing your game client or other game components. For example, for games in production, using an alias allows you to seamlessly redirect your player base to a new game server update.
    Amazon GameLift supports two types of routing strategies for aliases: simple and terminal. A simple alias points to an active fleet. A terminal alias is used to display messaging or link to a URL instead of routing players to an active fleet. For example, you might use a terminal alias when a game version is no longer supported and you want to direct players to an upgrade site.
    To create a fleet alias, specify an alias name, routing strategy, and optional description. Each simple alias can point to only one fleet, but a fleet can have multiple aliases. If successful, a new alias record is returned, including an alias ID, which you can reference when creating a game session. You can reassign an alias to another fleet by calling UpdateAlias .
    Alias-related operations include:
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
            SIMPLE -- The alias resolves to one specific fleet. Use this type when routing to active fleets.
            TERMINAL -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
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
    Name (string) -- [REQUIRED]
    Descriptive label that is associated with an alias. Alias names do not need to be unique.
    
    Description (string) -- Human-readable description of an alias.
    RoutingStrategy (dict) -- [REQUIRED]
    Object that specifies the fleet and routing type to use for the alias.
    
    Type (string) --Type of routing strategy.
    Possible routing types include the following:
    
    SIMPLE -- The alias resolves to one specific fleet. Use this type when routing to active fleets.
    TERMINAL -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
    
    
    FleetId (string) --Unique identifier for a fleet that the alias points to.
    
    Message (string) --Message text to be used with a terminal routing strategy.
    
    
    
    
    """
    pass

def create_build(Name=None, Version=None, StorageLocation=None, OperatingSystem=None):
    """
    Creates a new Amazon GameLift build record for your game server binary files and points to the location of your game server build files in an Amazon Simple Storage Service (Amazon S3) location.
    Game server binaries must be combined into a .zip file for use with Amazon GameLift. See Uploading Your Game for more information.
    The CreateBuild operation should be used only when you need to manually upload your build files, as in the following scenarios:
    If successful, this operation creates a new build record with a unique build ID and places it in INITIALIZED status. You can use  DescribeBuild to check the status of your build. A build must be in READY status before it can be used to create fleets.
    Build-related operations include:
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
    :param StorageLocation: Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key, as well as a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket must be in the same region that you want to create a new build in.
            Bucket (string) --Amazon S3 bucket identifier. This is the name of your S3 bucket.
            Key (string) --Name of the zip file containing your build files.
            RoleArn (string) --Amazon Resource Name (ARN ) for the access role that allows Amazon GameLift to access your S3 bucket.
            

    :type OperatingSystem: string
    :param OperatingSystem: Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. If your game build contains multiple executables, they all must run on the same operating system. If an operating system is not specified when creating a build, Amazon GameLift uses the default value (WINDOWS_2012). This value cannot be changed later.

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
    CreateBuild
    ListBuilds
    DescribeBuild
    UpdateBuild
    DeleteBuild
    
    """
    pass

def create_fleet(Name=None, Description=None, BuildId=None, ServerLaunchPath=None, ServerLaunchParameters=None, LogPaths=None, EC2InstanceType=None, EC2InboundPermissions=None, NewGameSessionProtectionPolicy=None, RuntimeConfiguration=None, ResourceCreationLimitPolicy=None, MetricGroups=None, PeerVpcAwsAccountId=None, PeerVpcId=None, FleetType=None):
    """
    Creates a new fleet to run your game servers. A fleet is a set of Amazon Elastic Compute Cloud (Amazon EC2) instances, each of which can run multiple server processes to host game sessions. You set up a fleet to use instances with certain hardware specifications (see Amazon EC2 Instance Types for more information), and deploy your game build to run on each instance.
    To create a new fleet, you must specify the following: (1) a fleet name, (2) the build ID of a successfully uploaded game build, (3) an EC2 instance type, and (4) a run-time configuration, which describes the server processes to run on each instance in the fleet. If you don't specify a fleet type (on-demand or spot), the new fleet uses on-demand instances by default.
    You can also configure the new fleet with the following settings:
    If you use Amazon CloudWatch for metrics, you can add the new fleet to a metric group. By adding multiple fleets to a metric group, you can view aggregated metrics for all the fleets in the group.
    If the CreateFleet call is successful, Amazon GameLift performs the following tasks. You can track the process of a fleet by checking the fleet status or by monitoring fleet creation events:
    Fleet-related operations include:
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
        EC2InstanceType='t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
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
        ],
        PeerVpcAwsAccountId='string',
        PeerVpcId='string',
        FleetType='ON_DEMAND'|'SPOT'
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
    :param ServerLaunchPath: This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. (Requests that specify a server launch path and launch parameters instead of a run-time configuration will continue to work.)

    :type ServerLaunchParameters: string
    :param ServerLaunchParameters: This parameter is no longer used. Instead, specify server launch parameters in the RuntimeConfiguration parameter. (Requests that specify a server launch path and launch parameters instead of a run-time configuration will continue to work.)

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
            NoProtection -- The game session can be terminated during a scale-down event.
            FullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
            

    :type RuntimeConfiguration: dict
    :param RuntimeConfiguration: Instructions for launching server processes on each instance in the fleet. The run-time configuration for a fleet has a collection of server process configurations, one for each type of server process to run on an instance. A server process configuration specifies the location of the server executable, launch parameters, and the number of concurrent processes with that configuration to maintain on each instance. A CreateFleet request must include a run-time configuration with at least one server process configuration; otherwise the request fails with an invalid request exception. (This parameter replaces the parameters ServerLaunchPath and ServerLaunchParameters ; requests that contain values for these parameters instead of a run-time configuration will continue to work.)
            ServerProcesses (list) --Collection of server process configurations that describe which server processes to run on each instance in a fleet.
            (dict) --A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet's `` RuntimeConfiguration `` .
            LaunchPath (string) -- [REQUIRED]Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances C:\game , and for Linux instances /local/game . A Windows game build with an executable file located at MyGame\latest\server.exe must have a launch path of 'C:\game\MyGame\latest\server.exe '. A Linux game build with an executable file located at MyGame/latest/server.exe must have a launch path of '/local/game/MyGame/latest/server.exe '.
            Parameters (string) --Optional list of parameters to pass to the server executable on launch.
            ConcurrentExecutions (integer) -- [REQUIRED]Number of server processes using this configuration to run concurrently on an instance.
            
            MaxConcurrentGameSessionActivations (integer) --Maximum number of game sessions with status ACTIVATING to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.
            GameSessionActivationTimeoutSeconds (integer) --Maximum amount of time (in seconds) that a game session can remain in status ACTIVATING . If the game session is not active before the timeout, activation is terminated and the game session status is changed to TERMINATED .
            

    :type ResourceCreationLimitPolicy: dict
    :param ResourceCreationLimitPolicy: Policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
            NewGameSessionsPerCreator (integer) --Maximum number of game sessions that an individual can create during the policy period.
            PolicyPeriodInMinutes (integer) --Time span used in evaluating the resource creation limit policy.
            

    :type MetricGroups: list
    :param MetricGroups: Name of a metric group to add this fleet to. A metric group tracks metrics across all fleets in the group. Use an existing metric group name to add this fleet to the group, or use a new name to create a new metric group. A fleet can only be included in one metric group at a time.
            (string) --
            

    :type PeerVpcAwsAccountId: string
    :param PeerVpcAwsAccountId: Unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your Account ID in the AWS Management Console under account settings.

    :type PeerVpcId: string
    :param PeerVpcId: Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.

    :type FleetType: string
    :param FleetType: Indicates whether to use on-demand instances or spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations, based on the instance type selected for this fleet. You can acquire on-demand instances at any time for a fixed price and keep them as long as you need them. Spot instances have lower prices, but spot pricing is variable, and while in use they can be interrupted (with a two-minute notification). Learn more about Amazon GameLift spot instances with at Choose Computing Resources .

    :rtype: dict
    :return: {
        'FleetAttributes': {
            'FleetId': 'string',
            'FleetArn': 'string',
            'FleetType': 'ON_DEMAND'|'SPOT',
            'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
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
    Creates a fleet record. Status: NEW .
    Begins writing events to the fleet event log, which can be accessed in the Amazon GameLift console. Sets the fleet's target capacity to 1 (desired instances), which triggers Amazon GameLift to start one new EC2 instance.
    Downloads the game build to the new instance and installs it. Statuses: DOWNLOADING , VALIDATING , BUILDING .
    Starts launching server processes on the instance. If the fleet is configured to run multiple server processes per instance, Amazon GameLift staggers each launch by a few seconds. Status: ACTIVATING .
    Sets the fleet's status to ACTIVE as soon as one server process is ready to host a game session.
    
    """
    pass

def create_game_session(FleetId=None, AliasId=None, MaximumPlayerSessionCount=None, Name=None, GameProperties=None, CreatorId=None, GameSessionId=None, IdempotencyToken=None, GameSessionData=None):
    """
    Creates a multiplayer game session for players. This action creates a game session record and assigns an available server process in the specified fleet to host the game session. A fleet must have an ACTIVE status before a game session can be created in it.
    To create a game session, specify either fleet ID or alias ID and indicate a maximum number of players to allow in the game session. You can also provide a name and game-specific properties for this game session. If successful, a  GameSession object is returned containing the game session properties and other settings you specified.
    Game-session-related operations include:
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
        IdempotencyToken='string',
        GameSessionData='string'
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
    :param GameProperties: Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ).
            (dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the Amazon GameLift Developer Guide .
            Key (string) -- [REQUIRED]Game property identifier.
            Value (string) -- [REQUIRED]Game property value.
            
            

    :type CreatorId: string
    :param CreatorId: Unique identifier for a player or entity creating the game session. This ID is used to enforce a resource protection policy (if one exists) that limits the number of concurrent active game sessions one player can have.

    :type GameSessionId: string
    :param GameSessionId: This parameter is no longer preferred. Please use ``IdempotencyToken`` instead. Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID. (A game session ARN has the following format: arn:aws:gamelift:region::gamesession/fleet ID/custom ID string or idempotency token .)

    :type IdempotencyToken: string
    :param IdempotencyToken: Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID. (A game session ARN has the following format: arn:aws:gamelift:region::gamesession/fleet ID/custom ID string or idempotency token .) Idempotency tokens remain in use for 30 days after a game session has ended; game session objects are retained for this time period and then deleted.

    :type GameSessionData: string
    :param GameSessionData: Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ).

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
            'StatusReason': 'INTERRUPTED',
            'GameProperties': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'IpAddress': 'string',
            'Port': 123,
            'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
            'CreatorId': 'string',
            'GameSessionData': 'string',
            'MatchmakerData': 'string'
        }
    }
    
    
    :returns: 
    FleetId (string) -- Unique identifier for a fleet to create a game session in. Each request must reference either a fleet ID or alias ID, but not both.
    AliasId (string) -- Unique identifier for an alias associated with the fleet to create a game session in. Each request must reference either a fleet ID or alias ID, but not both.
    MaximumPlayerSessionCount (integer) -- [REQUIRED]
    Maximum number of players that can be connected simultaneously to the game session.
    
    Name (string) -- Descriptive label that is associated with a game session. Session names do not need to be unique.
    GameProperties (list) -- Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).
    
    (dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the Amazon GameLift Developer Guide .
    
    Key (string) -- [REQUIRED]Game property identifier.
    
    Value (string) -- [REQUIRED]Game property value.
    
    
    
    
    
    CreatorId (string) -- Unique identifier for a player or entity creating the game session. This ID is used to enforce a resource protection policy (if one exists) that limits the number of concurrent active game sessions one player can have.
    GameSessionId (string) -- This parameter is no longer preferred. Please use ``IdempotencyToken`` instead. Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID. (A game session ARN has the following format: arn:aws:gamelift:region::gamesession/fleet ID/custom ID string or idempotency token .)
    IdempotencyToken (string) -- Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID. (A game session ARN has the following format: arn:aws:gamelift:region::gamesession/fleet ID/custom ID string or idempotency token .) Idempotency tokens remain in use for 30 days after a game session has ended; game session objects are retained for this time period and then deleted.
    GameSessionData (string) -- Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).
    
    """
    pass

def create_game_session_queue(Name=None, TimeoutInSeconds=None, PlayerLatencyPolicies=None, Destinations=None):
    """
    Establishes a new queue for processing requests to place new game sessions. A queue identifies where new game sessions can be hosted -- by specifying a list of destinations (fleets or aliases) -- and how long requests can wait in the queue before timing out. You can set up a queue to try to place game sessions on fleets in multiple regions. To add placement requests to a queue, call  StartGameSessionPlacement and reference the queue name.
    To create a new queue, provide a name, timeout value, a list of destinations and, if desired, a set of latency policies. If successful, a new queue object is returned.
    Queue-related operations include:
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
            Descriptive label that is associated with game session queue. Queue names must be unique within each region.
            

    :type TimeoutInSeconds: integer
    :param TimeoutInSeconds: Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.

    :type PlayerLatencyPolicies: list
    :param PlayerLatencyPolicies: Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. A player latency policy must set a value for MaximumIndividualPlayerLatencyMilliseconds; if none is set, this API requests will fail.
            (dict) --Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
            Queue-related operations include:
            CreateGameSessionQueue
            DescribeGameSessionQueues
            UpdateGameSessionQueue
            DeleteGameSessionQueue
            MaximumIndividualPlayerLatencyMilliseconds (integer) --The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
            PolicyDurationSeconds (integer) --The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
            
            

    :type Destinations: list
    :param Destinations: List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.
            (dict) --Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue.
            Queue-related operations include:
            CreateGameSessionQueue
            DescribeGameSessionQueues
            UpdateGameSessionQueue
            DeleteGameSessionQueue
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
    Name (string) -- [REQUIRED]
    Descriptive label that is associated with game session queue. Queue names must be unique within each region.
    
    TimeoutInSeconds (integer) -- Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.
    PlayerLatencyPolicies (list) -- Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. A player latency policy must set a value for MaximumIndividualPlayerLatencyMilliseconds; if none is set, this API requests will fail.
    
    (dict) --Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
    Queue-related operations include:
    
    CreateGameSessionQueue
    DescribeGameSessionQueues
    UpdateGameSessionQueue
    DeleteGameSessionQueue
    
    
    MaximumIndividualPlayerLatencyMilliseconds (integer) --The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
    
    PolicyDurationSeconds (integer) --The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
    
    
    
    
    
    Destinations (list) -- List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.
    
    (dict) --Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue.
    Queue-related operations include:
    
    CreateGameSessionQueue
    DescribeGameSessionQueues
    UpdateGameSessionQueue
    DeleteGameSessionQueue
    
    
    DestinationArn (string) --Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a region name, provide a unique identifier across all regions.
    
    
    
    
    
    
    """
    pass

def create_matchmaking_configuration(Name=None, Description=None, GameSessionQueueArns=None, RequestTimeoutSeconds=None, AcceptanceTimeoutSeconds=None, AcceptanceRequired=None, RuleSetName=None, NotificationTarget=None, AdditionalPlayerCount=None, CustomEventData=None, GameProperties=None, GameSessionData=None):
    """
    Defines a new matchmaking configuration for use with FlexMatch. A matchmaking configuration sets out guidelines for matching players and getting the matches into games. You can set up multiple matchmaking configurations to handle the scenarios needed for your game. Each matchmaking ticket ( StartMatchmaking or  StartMatchBackfill ) specifies a configuration for the match and provides player attributes to support the configuration being used.
    To create a matchmaking configuration, at a minimum you must specify the following: configuration name; a rule set that governs how to evaluate players and find acceptable matches; a game session queue to use when placing a new game session for the match; and the maximum time allowed for a matchmaking attempt.
    Operations related to match configurations and rule sets include:
    See also: AWS API Documentation
    
    
    :example: response = client.create_matchmaking_configuration(
        Name='string',
        Description='string',
        GameSessionQueueArns=[
            'string',
        ],
        RequestTimeoutSeconds=123,
        AcceptanceTimeoutSeconds=123,
        AcceptanceRequired=True|False,
        RuleSetName='string',
        NotificationTarget='string',
        AdditionalPlayerCount=123,
        CustomEventData='string',
        GameProperties=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        GameSessionData='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
            

    :type Description: string
    :param Description: Meaningful description of the matchmaking configuration.

    :type GameSessionQueueArns: list
    :param GameSessionQueueArns: [REQUIRED]
            Amazon Resource Name (ARN ) that is assigned to a game session queue and uniquely identifies it. Format is arn:aws:gamelift:region::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912 . These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any region.
            (string) --
            

    :type RequestTimeoutSeconds: integer
    :param RequestTimeoutSeconds: [REQUIRED]
            Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that time out can be resubmitted as needed.
            

    :type AcceptanceTimeoutSeconds: integer
    :param AcceptanceTimeoutSeconds: Length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.

    :type AcceptanceRequired: boolean
    :param AcceptanceRequired: [REQUIRED]
            Flag that determines whether or not a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.
            

    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]
            Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same region.
            

    :type NotificationTarget: string
    :param NotificationTarget: SNS topic ARN that is set up to receive matchmaking notifications.

    :type AdditionalPlayerCount: integer
    :param AdditionalPlayerCount: Number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match.

    :type CustomEventData: string
    :param CustomEventData: Information to attached to all events related to the matchmaking configuration.

    :type GameProperties: list
    :param GameProperties: Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new GameSession object that is created for a successful match.
            (dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the Amazon GameLift Developer Guide .
            Key (string) -- [REQUIRED]Game property identifier.
            Value (string) -- [REQUIRED]Game property value.
            
            

    :type GameSessionData: string
    :param GameSessionData: Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new GameSession object that is created for a successful match.

    :rtype: dict
    :return: {
        'Configuration': {
            'Name': 'string',
            'Description': 'string',
            'GameSessionQueueArns': [
                'string',
            ],
            'RequestTimeoutSeconds': 123,
            'AcceptanceTimeoutSeconds': 123,
            'AcceptanceRequired': True|False,
            'RuleSetName': 'string',
            'NotificationTarget': 'string',
            'AdditionalPlayerCount': 123,
            'CustomEventData': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'GameProperties': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'GameSessionData': 'string'
        }
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    Unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
    
    Description (string) -- Meaningful description of the matchmaking configuration.
    GameSessionQueueArns (list) -- [REQUIRED]
    Amazon Resource Name (ARN ) that is assigned to a game session queue and uniquely identifies it. Format is arn:aws:gamelift:region::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912 . These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any region.
    
    (string) --
    
    
    RequestTimeoutSeconds (integer) -- [REQUIRED]
    Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that time out can be resubmitted as needed.
    
    AcceptanceTimeoutSeconds (integer) -- Length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
    AcceptanceRequired (boolean) -- [REQUIRED]
    Flag that determines whether or not a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.
    
    RuleSetName (string) -- [REQUIRED]
    Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same region.
    
    NotificationTarget (string) -- SNS topic ARN that is set up to receive matchmaking notifications.
    AdditionalPlayerCount (integer) -- Number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match.
    CustomEventData (string) -- Information to attached to all events related to the matchmaking configuration.
    GameProperties (list) -- Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.
    
    (dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the Amazon GameLift Developer Guide .
    
    Key (string) -- [REQUIRED]Game property identifier.
    
    Value (string) -- [REQUIRED]Game property value.
    
    
    
    
    
    GameSessionData (string) -- Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.
    
    """
    pass

def create_matchmaking_rule_set(Name=None, RuleSetBody=None):
    """
    Creates a new rule set for FlexMatch matchmaking. A rule set describes the type of match to create, such as the number and size of teams, and sets the parameters for acceptable player matches, such as minimum skill level or character type. Rule sets are used in matchmaking configurations, which define how matchmaking requests are handled. Each  MatchmakingConfiguration uses one rule set; you can set up multiple rule sets to handle the scenarios that suit your game (such as for different game modes), and create a separate matchmaking configuration for each rule set. See additional information on rule set content in the  MatchmakingRuleSet structure. For help creating rule sets, including useful examples, see the topic Adding FlexMatch to Your Game .
    Once created, matchmaking rule sets cannot be changed or deleted, so we recommend checking the rule set syntax using  ValidateMatchmakingRuleSet before creating the rule set.
    To create a matchmaking rule set, provide the set of rules and a unique name. Rule sets must be defined in the same region as the matchmaking configuration they will be used with. Rule sets cannot be edited or deleted. If you need to change a rule set, create a new one with the necessary edits and then update matchmaking configurations to use the new rule set.
    Operations related to match configurations and rule sets include:
    See also: AWS API Documentation
    
    
    :example: response = client.create_matchmaking_rule_set(
        Name='string',
        RuleSetBody='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Unique identifier for a matchmaking rule set. This name is used to identify the rule set associated with a matchmaking configuration.
            

    :type RuleSetBody: string
    :param RuleSetBody: [REQUIRED]
            Collection of matchmaking rules, formatted as a JSON string. (Note that comments are not allowed in JSON, but most elements support a description field.)
            

    :rtype: dict
    :return: {
        'RuleSet': {
            'RuleSetName': 'string',
            'RuleSetBody': 'string',
            'CreationTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    Unique identifier for a matchmaking rule set. This name is used to identify the rule set associated with a matchmaking configuration.
    
    RuleSetBody (string) -- [REQUIRED]
    Collection of matchmaking rules, formatted as a JSON string. (Note that comments are not allowed in JSON, but most elements support a description field.)
    
    
    """
    pass

def create_player_session(GameSessionId=None, PlayerId=None, PlayerData=None):
    """
    Adds a player to a game session and creates a player session record. Before a player can be added, a game session must have an ACTIVE status, have a creation policy of ALLOW_ALL , and have an open player slot. To add a group of players to a game session, use  CreatePlayerSessions .
    To create a player session, specify a game session ID, player ID, and optionally a string of player data. If successful, the player is added to the game session and a new  PlayerSession object is returned. Player sessions cannot be updated.
    Player-session-related operations include:
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
    GameSessionId (string) -- [REQUIRED]
    Unique identifier for the game session to add a player to.
    
    PlayerId (string) -- [REQUIRED]
    Unique identifier for a player. Player IDs are developer-defined.
    
    PlayerData (string) -- Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.
    
    """
    pass

def create_player_sessions(GameSessionId=None, PlayerIds=None, PlayerDataMap=None):
    """
    Adds a group of players to a game session. This action is useful with a team matching feature. Before players can be added, a game session must have an ACTIVE status, have a creation policy of ALLOW_ALL , and have an open player slot. To add a single player to a game session, use  CreatePlayerSession .
    To create player sessions, specify a game session ID, a list of player IDs, and optionally a set of player data strings. If successful, the players are added to the game session and a set of new  PlayerSession objects is returned. Player sessions cannot be updated.
    Player-session-related operations include:
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
    GameSessionId (string) -- [REQUIRED]
    Unique identifier for the game session to add players to.
    
    PlayerIds (list) -- [REQUIRED]
    List of unique identifiers for the players to be added.
    
    (string) --
    
    
    PlayerDataMap (dict) -- Map of string pairs, each specifying a player ID and a set of developer-defined information related to the player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game. Player data strings for player IDs not included in the PlayerIds parameter are ignored.
    
    (string) --
    (string) --
    
    
    
    
    
    """
    pass

def create_vpc_peering_authorization(GameLiftAwsAccountId=None, PeerVpcId=None):
    """
    Requests authorization to create or delete a peer connection between the VPC for your Amazon GameLift fleet and a virtual private cloud (VPC) in your AWS account. VPC peering enables the game servers on your fleet to communicate directly with other AWS resources. Once you've received authorization, call  CreateVpcPeeringConnection to establish the peering connection. For more information, see VPC Peering with Amazon GameLift Fleets .
    You can peer with VPCs that are owned by any AWS account you have access to, including the account that you use to manage your Amazon GameLift fleets. You cannot peer with VPCs that are in different regions.
    To request authorization to create a connection, call this operation from the AWS account with the VPC that you want to peer to your Amazon GameLift fleet. For example, to enable your game servers to retrieve data from a DynamoDB table, use the account that manages that DynamoDB resource. Identify the following values: (1) The ID of the VPC that you want to peer with, and (2) the ID of the AWS account that you use to manage Amazon GameLift. If successful, VPC peering is authorized for the specified VPC.
    To request authorization to delete a connection, call this operation from the AWS account with the VPC that is peered with your Amazon GameLift fleet. Identify the following values: (1) VPC ID that you want to delete the peering connection for, and (2) ID of the AWS account that you use to manage Amazon GameLift.
    The authorization remains valid for 24 hours unless it is canceled by a call to  DeleteVpcPeeringAuthorization . You must create or delete the peering connection while the authorization is valid.
    VPC peering connection operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.create_vpc_peering_authorization(
        GameLiftAwsAccountId='string',
        PeerVpcId='string'
    )
    
    
    :type GameLiftAwsAccountId: string
    :param GameLiftAwsAccountId: [REQUIRED]
            Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
            

    :type PeerVpcId: string
    :param PeerVpcId: [REQUIRED]
            Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
            

    :rtype: dict
    :return: {
        'VpcPeeringAuthorization': {
            'GameLiftAwsAccountId': 'string',
            'PeerVpcAwsAccountId': 'string',
            'PeerVpcId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'ExpirationTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    GameLiftAwsAccountId (string) -- [REQUIRED]
    Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
    
    PeerVpcId (string) -- [REQUIRED]
    Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
    
    
    """
    pass

def create_vpc_peering_connection(FleetId=None, PeerVpcAwsAccountId=None, PeerVpcId=None):
    """
    Establishes a VPC peering connection between a virtual private cloud (VPC) in an AWS account with the VPC for your Amazon GameLift fleet. VPC peering enables the game servers on your fleet to communicate directly with other AWS resources. You can peer with VPCs in any AWS account that you have access to, including the account that you use to manage your Amazon GameLift fleets. You cannot peer with VPCs that are in different regions. For more information, see VPC Peering with Amazon GameLift Fleets .
    Before calling this operation to establish the peering connection, you first need to call  CreateVpcPeeringAuthorization and identify the VPC you want to peer with. Once the authorization for the specified VPC is issued, you have 24 hours to establish the connection. These two operations handle all tasks necessary to peer the two VPCs, including acceptance, updating routing tables, etc.
    To establish the connection, call this operation from the AWS account that is used to manage the Amazon GameLift fleets. Identify the following values: (1) The ID of the fleet you want to be enable a VPC peering connection for; (2) The AWS account with the VPC that you want to peer with; and (3) The ID of the VPC you want to peer with. This operation is asynchronous. If successful, a  VpcPeeringConnection request is created. You can use continuous polling to track the request's status using  DescribeVpcPeeringConnections , or by monitoring fleet events for success or failure using  DescribeFleetEvents .
    VPC peering connection operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.create_vpc_peering_connection(
        FleetId='string',
        PeerVpcAwsAccountId='string',
        PeerVpcId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet. This tells Amazon GameLift which GameLift VPC to peer with.
            

    :type PeerVpcAwsAccountId: string
    :param PeerVpcAwsAccountId: [REQUIRED]
            Unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your Account ID in the AWS Management Console under account settings.
            

    :type PeerVpcId: string
    :param PeerVpcId: [REQUIRED]
            Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    Unique identifier for a fleet. This tells Amazon GameLift which GameLift VPC to peer with.
    
    PeerVpcAwsAccountId (string) -- [REQUIRED]
    Unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your Account ID in the AWS Management Console under account settings.
    
    PeerVpcId (string) -- [REQUIRED]
    Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
    
    
    """
    pass

def delete_alias(AliasId=None):
    """
    Deletes an alias. This action removes all record of the alias. Game clients attempting to access a server process using the deleted alias receive an error. To delete an alias, specify the alias ID to be deleted.
    Alias-related operations include:
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
    Build-related operations include:
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
    Fleet-related operations include:
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
    Queue-related operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_game_session_queue(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Descriptive label that is associated with game session queue. Queue names must be unique within each region.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_matchmaking_configuration(Name=None):
    """
    Permanently removes a FlexMatch matchmaking configuration. To delete, specify the configuration name. A matchmaking configuration cannot be deleted if it is being used in any active matchmaking tickets.
    Operations related to match configurations and rule sets include:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_matchmaking_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Unique identifier for a matchmaking configuration
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_scaling_policy(Name=None, FleetId=None):
    """
    Deletes a fleet scaling policy. This action means that the policy is no longer in force and removes all record of it. To delete a scaling policy, specify both the scaling policy name and the fleet ID it is associated with.
    Fleet-related operations include:
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
            

    :returns: 
    Name (string) -- [REQUIRED]
    Descriptive label that is associated with a scaling policy. Policy names do not need to be unique.
    
    FleetId (string) -- [REQUIRED]
    Unique identifier for a fleet to be deleted.
    
    
    """
    pass

def delete_vpc_peering_authorization(GameLiftAwsAccountId=None, PeerVpcId=None):
    """
    Cancels a pending VPC peering authorization for the specified VPC. If the authorization has already been used to create a peering connection, call  DeleteVpcPeeringConnection to remove the connection.
    VPC peering connection operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_vpc_peering_authorization(
        GameLiftAwsAccountId='string',
        PeerVpcId='string'
    )
    
    
    :type GameLiftAwsAccountId: string
    :param GameLiftAwsAccountId: [REQUIRED]
            Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
            

    :type PeerVpcId: string
    :param PeerVpcId: [REQUIRED]
            Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    GameLiftAwsAccountId (string) -- [REQUIRED]
    Unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
    
    PeerVpcId (string) -- [REQUIRED]
    Unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same region where your fleet is deployed. To get VPC information, including IDs, use the Virtual Private Cloud service tools, including the VPC Dashboard in the AWS Management Console.
    
    
    """
    pass

def delete_vpc_peering_connection(FleetId=None, VpcPeeringConnectionId=None):
    """
    Removes a VPC peering connection. To delete the connection, you must have a valid authorization for the VPC peering connection that you want to delete. You can check for an authorization by calling  DescribeVpcPeeringAuthorizations or request a new one using  CreateVpcPeeringAuthorization .
    Once a valid authorization exists, call this operation from the AWS account that is used to manage the Amazon GameLift fleets. Identify the connection to delete by the connection ID and fleet ID. If successful, the connection is removed.
    VPC peering connection operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.delete_vpc_peering_connection(
        FleetId='string',
        VpcPeeringConnectionId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet. This value must match the fleet ID referenced in the VPC peering connection record.
            

    :type VpcPeeringConnectionId: string
    :param VpcPeeringConnectionId: [REQUIRED]
            Unique identifier for a VPC peering connection. This value is included in the VpcPeeringConnection object, which can be retrieved by calling DescribeVpcPeeringConnections .
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    Unique identifier for a fleet. This value must match the fleet ID referenced in the VPC peering connection record.
    
    VpcPeeringConnectionId (string) -- [REQUIRED]
    Unique identifier for a VPC peering connection. This value is included in the  VpcPeeringConnection object, which can be retrieved by calling  DescribeVpcPeeringConnections .
    
    
    """
    pass

def describe_alias(AliasId=None):
    """
    Retrieves properties for an alias. This operation returns all alias metadata and settings. To get an alias's target fleet ID only, use ResolveAlias .
    To get alias properties, specify the alias ID. If successful, the requested alias record is returned.
    Alias-related operations include:
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
    
    
    :returns: 
    SIMPLE -- The alias resolves to one specific fleet. Use this type when routing to active fleets.
    TERMINAL -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
    
    """
    pass

def describe_build(BuildId=None):
    """
    Retrieves properties for a build. To request a build record, specify a build ID. If successful, an object containing the build properties is returned.
    Build-related operations include:
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
    
    
    :returns: 
    INITIALIZED -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
    READY -- The game build has been successfully uploaded. You can now create new fleets for this build.
    FAILED -- The game build upload failed. You cannot create new fleets for this build.
    
    """
    pass

def describe_ec2_instance_limits(EC2InstanceType=None):
    """
    Retrieves the following information for the specified EC2 instance type:
    Service limits vary depending on region. Available regions for Amazon GameLift can be found in the AWS Management Console for Amazon GameLift (see the drop-down list in the upper right corner).
    Fleet-related operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_ec2_instance_limits(
        EC2InstanceType='t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'
    )
    
    
    :type EC2InstanceType: string
    :param EC2InstanceType: Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions. Leave this parameter blank to retrieve limits for all types.

    :rtype: dict
    :return: {
        'EC2InstanceLimits': [
            {
                'EC2InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
                'CurrentInstances': 123,
                'InstanceLimit': 123
            },
        ]
    }
    
    
    :returns: 
    CreateFleet
    ListFleets
    Describe fleets:
    DescribeFleetAttributes
    DescribeFleetPortSettings
    DescribeFleetUtilization
    DescribeRuntimeConfiguration
    DescribeFleetEvents
    
    
    Update fleets:
    UpdateFleetAttributes
    UpdateFleetCapacity
    UpdateFleetPortSettings
    UpdateRuntimeConfiguration
    
    
    Manage fleet capacity:
    DescribeFleetCapacity
    UpdateFleetCapacity
    PutScalingPolicy (automatic scaling)
    DescribeScalingPolicies (automatic scaling)
    DeleteScalingPolicy (automatic scaling)
    DescribeEC2InstanceLimits
    
    
    DeleteFleet
    
    """
    pass

def describe_fleet_attributes(FleetIds=None, Limit=None, NextToken=None):
    """
    Retrieves fleet properties, including metadata, status, and configuration, for one or more fleets. You can request attributes for all fleets, or specify a list of one or more fleet IDs. When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  FleetAttributes object is returned for each requested fleet ID. When specifying a list of fleet IDs, attribute objects are returned only for fleets that currently exist.
    Fleet-related operations include:
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
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :rtype: dict
    :return: {
        'FleetAttributes': [
            {
                'FleetId': 'string',
                'FleetArn': 'string',
                'FleetType': 'ON_DEMAND'|'SPOT',
                'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
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
    FleetIds (list) -- Unique identifier for a fleet(s) to retrieve attributes for. To request attributes for all fleets, leave this parameter empty.
    
    (string) --
    
    
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
    
    """
    pass

def describe_fleet_capacity(FleetIds=None, Limit=None, NextToken=None):
    """
    Retrieves the current status of fleet capacity for one or more fleets. This information includes the number of instances that have been requested for the fleet and the number currently active. You can request capacity for all fleets, or specify a list of one or more fleet IDs. When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  FleetCapacity object is returned for each requested fleet ID. When specifying a list of fleet IDs, attribute objects are returned only for fleets that currently exist.
    Fleet-related operations include:
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
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :rtype: dict
    :return: {
        'FleetCapacity': [
            {
                'FleetId': 'string',
                'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
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
    
    
    :returns: 
    FleetIds (list) -- Unique identifier for a fleet(s) to retrieve capacity information for. To request capacity information for all fleets, leave this parameter empty.
    
    (string) --
    
    
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
    
    """
    pass

def describe_fleet_events(FleetId=None, StartTime=None, EndTime=None, Limit=None, NextToken=None):
    """
    Retrieves entries from the specified fleet's event log. You can specify a time range to limit the result set. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a collection of event log entries matching the request are returned.
    Fleet-related operations include:
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
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'Events': [
            {
                'EventId': 'string',
                'ResourceId': 'string',
                'EventCode': 'GENERIC_EVENT'|'FLEET_CREATED'|'FLEET_DELETED'|'FLEET_SCALING_EVENT'|'FLEET_STATE_DOWNLOADING'|'FLEET_STATE_VALIDATING'|'FLEET_STATE_BUILDING'|'FLEET_STATE_ACTIVATING'|'FLEET_STATE_ACTIVE'|'FLEET_STATE_ERROR'|'FLEET_INITIALIZATION_FAILED'|'FLEET_BINARY_DOWNLOAD_FAILED'|'FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND'|'FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE'|'FLEET_VALIDATION_TIMED_OUT'|'FLEET_ACTIVATION_FAILED'|'FLEET_ACTIVATION_FAILED_NO_INSTANCES'|'FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED'|'SERVER_PROCESS_INVALID_PATH'|'SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT'|'SERVER_PROCESS_PROCESS_READY_TIMEOUT'|'SERVER_PROCESS_CRASHED'|'SERVER_PROCESS_TERMINATED_UNHEALTHY'|'SERVER_PROCESS_FORCE_TERMINATED'|'SERVER_PROCESS_PROCESS_EXIT_TIMEOUT'|'GAME_SESSION_ACTIVATION_TIMEOUT'|'FLEET_CREATION_EXTRACTING_BUILD'|'FLEET_CREATION_RUNNING_INSTALLER'|'FLEET_CREATION_VALIDATING_RUNTIME_CONFIG'|'FLEET_VPC_PEERING_SUCCEEDED'|'FLEET_VPC_PEERING_FAILED'|'FLEET_VPC_PEERING_DELETED'|'INSTANCE_INTERRUPTED',
                'Message': 'string',
                'EventTime': datetime(2015, 1, 1),
                'PreSignedLogUrl': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    Unique identifier for a fleet to get event logs for.
    
    StartTime (datetime) -- Earliest date to retrieve event logs for. If no start time is specified, this call returns entries starting from when the fleet was created to the specified end time. Format is a number expressed in Unix time as milliseconds (ex: "1469498468.057").
    EndTime (datetime) -- Most recent date to retrieve event logs for. If no end time is specified, this call returns entries from the specified start time up to the present. Format is a number expressed in Unix time as milliseconds (ex: "1469498468.057").
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_fleet_port_settings(FleetId=None):
    """
    Retrieves the inbound connection permissions for a fleet. Connection permissions include a range of IP addresses and port settings that incoming traffic can use to access server processes in the fleet. To get a fleet's inbound connection permissions, specify a fleet ID. If successful, a collection of  IpPermission objects is returned for the requested fleet ID. If the requested fleet has been deleted, the result set is empty.
    Fleet-related operations include:
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
    Fleet-related operations include:
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
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.

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
    
    
    :returns: 
    FleetIds (list) -- Unique identifier for a fleet(s) to retrieve utilization data for. To request utilization data for all fleets, leave this parameter empty.
    
    (string) --
    
    
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
    
    """
    pass

def describe_game_session_details(FleetId=None, GameSessionId=None, AliasId=None, StatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves properties, including the protection policy in force, for one or more game sessions. This action can be used in several ways: (1) provide a GameSessionId or GameSessionArn to request details for a specific game session; (2) provide either a FleetId or an AliasId to request properties for all game sessions running on a fleet.
    To get game session record(s), specify just one of the following: game session ID, fleet ID, or alias ID. You can filter this request by game session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSessionDetail object is returned for each session matching the request.
    Game-session-related operations include:
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
    :param StatusFilter: Game session status to filter results on. Possible game session statuses include ACTIVE , TERMINATED , ACTIVATING and TERMINATING (the last two are transitory).

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

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
                    'StatusReason': 'INTERRUPTED',
                    'GameProperties': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'IpAddress': 'string',
                    'Port': 123,
                    'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
                    'CreatorId': 'string',
                    'GameSessionData': 'string',
                    'MatchmakerData': 'string'
                },
                'ProtectionPolicy': 'NoProtection'|'FullProtection'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    FleetId (string) -- Unique identifier for a fleet to retrieve all game sessions active on the fleet.
    GameSessionId (string) -- Unique identifier for the game session to retrieve.
    AliasId (string) -- Unique identifier for an alias associated with the fleet to retrieve all game sessions for.
    StatusFilter (string) -- Game session status to filter results on. Possible game session statuses include ACTIVE , TERMINATED , ACTIVATING and TERMINATING (the last two are transitory).
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_game_session_placement(PlacementId=None):
    """
    Retrieves properties and current status of a game session placement request. To get game session placement details, specify the placement ID. If successful, a  GameSessionPlacement object is returned.
    Game-session-related operations include:
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
            ],
            'GameSessionData': 'string',
            'MatchmakerData': 'string'
        }
    }
    
    
    :returns: 
    PENDING -- The placement request is currently in the queue waiting to be processed.
    FULFILLED -- A new game session and player sessions (if requested) have been successfully created. Values for GameSessionArn and GameSessionRegion are available.
    CANCELLED -- The placement request was canceled with a call to  StopGameSessionPlacement .
    TIMED_OUT -- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed.
    
    """
    pass

def describe_game_session_queues(Names=None, Limit=None, NextToken=None):
    """
    Retrieves the properties for one or more game session queues. When requesting multiple queues, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSessionQueue object is returned for each requested queue. When specifying a list of queues, objects are returned only for queues that currently exist in the region.
    Queue-related operations include:
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
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

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
    Names (list) -- List of queue names to retrieve information for. To request settings for all queues, leave this parameter empty.
    
    (string) --
    
    
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_game_sessions(FleetId=None, GameSessionId=None, AliasId=None, StatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves a set of one or more game sessions. Request a specific game session or request all game sessions on a fleet. Alternatively, use  SearchGameSessions to request a set of active game sessions that are filtered by certain criteria. To retrieve protection policy settings for game sessions, use  DescribeGameSessionDetails .
    To get game sessions, specify one of the following: game session ID, fleet ID, or alias ID. You can filter this request by game session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSession object is returned for each game session matching the request.
    Game-session-related operations include:
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
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

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
                'StatusReason': 'INTERRUPTED',
                'GameProperties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'IpAddress': 'string',
                'Port': 123,
                'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
                'CreatorId': 'string',
                'GameSessionData': 'string',
                'MatchmakerData': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    FleetId (string) -- Unique identifier for a fleet to retrieve all game sessions for.
    GameSessionId (string) -- Unique identifier for the game session to retrieve. You can use either a GameSessionId or GameSessionArn value.
    AliasId (string) -- Unique identifier for an alias associated with the fleet to retrieve all game sessions for.
    StatusFilter (string) -- Game session status to filter results on. Possible game session statuses include ACTIVE , TERMINATED , ACTIVATING , and TERMINATING (the last two are transitory).
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
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
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'Instances': [
            {
                'FleetId': 'string',
                'InstanceId': 'string',
                'IpAddress': 'string',
                'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX',
                'Type': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
                'Status': 'PENDING'|'ACTIVE'|'TERMINATING',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    PENDING -- The instance is in the process of being created and launching server processes as defined in the fleet's run-time configuration.
    ACTIVE -- The instance has been successfully created and at least one server process has successfully launched and reported back to Amazon GameLift that it is ready to host a game session. The instance is now considered ready to host game sessions.
    TERMINATING -- The instance is in the process of shutting down. This may happen to reduce capacity during a scaling down event or to recycle resources in the event of a problem.
    
    """
    pass

def describe_matchmaking(TicketIds=None):
    """
    Retrieves one or more matchmaking tickets. Use this operation to retrieve ticket information, including status and--once a successful match is made--acquire connection information for the resulting new game session.
    You can use this operation to track the progress of matchmaking requests (through polling) as an alternative to using event notifications. See more details on tracking matchmaking requests through polling or notifications in  StartMatchmaking .
    To request matchmaking tickets, provide a list of up to 10 ticket IDs. If the request is successful, a ticket object is returned for each requested ID that currently exists.
    Matchmaking-related operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_matchmaking(
        TicketIds=[
            'string',
        ]
    )
    
    
    :type TicketIds: list
    :param TicketIds: [REQUIRED]
            Unique identifier for a matchmaking ticket. You can include up to 10 ID values.
            (string) --
            

    :rtype: dict
    :return: {
        'TicketList': [
            {
                'TicketId': 'string',
                'ConfigurationName': 'string',
                'Status': 'CANCELLED'|'COMPLETED'|'FAILED'|'PLACING'|'QUEUED'|'REQUIRES_ACCEPTANCE'|'SEARCHING'|'TIMED_OUT',
                'StatusReason': 'string',
                'StatusMessage': 'string',
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'Players': [
                    {
                        'PlayerId': 'string',
                        'PlayerAttributes': {
                            'string': {
                                'S': 'string',
                                'N': 123.0,
                                'SL': [
                                    'string',
                                ],
                                'SDM': {
                                    'string': 123.0
                                }
                            }
                        },
                        'Team': 'string',
                        'LatencyInMs': {
                            'string': 123
                        }
                    },
                ],
                'GameSessionConnectionInfo': {
                    'GameSessionArn': 'string',
                    'IpAddress': 'string',
                    'Port': 123,
                    'MatchedPlayerSessions': [
                        {
                            'PlayerId': 'string',
                            'PlayerSessionId': 'string'
                        },
                    ]
                },
                'EstimatedWaitTime': 123
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_matchmaking_configurations(Names=None, RuleSetName=None, Limit=None, NextToken=None):
    """
    Retrieves the details of FlexMatch matchmaking configurations. with this operation, you have the following options: (1) retrieve all existing configurations, (2) provide the names of one or more configurations to retrieve, or (3) retrieve all configurations that use a specified rule set name. When requesting multiple items, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a configuration is returned for each requested name. When specifying a list of names, only configurations that currently exist are returned.
    Operations related to match configurations and rule sets include:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_matchmaking_configurations(
        Names=[
            'string',
        ],
        RuleSetName='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: Unique identifier for a matchmaking configuration(s) to retrieve. To request all existing configurations, leave this parameter empty.
            (string) --
            

    :type RuleSetName: string
    :param RuleSetName: Unique identifier for a matchmaking rule set. Use this parameter to retrieve all matchmaking configurations that use this rule set.

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is limited to 10.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'Configurations': [
            {
                'Name': 'string',
                'Description': 'string',
                'GameSessionQueueArns': [
                    'string',
                ],
                'RequestTimeoutSeconds': 123,
                'AcceptanceTimeoutSeconds': 123,
                'AcceptanceRequired': True|False,
                'RuleSetName': 'string',
                'NotificationTarget': 'string',
                'AdditionalPlayerCount': 123,
                'CustomEventData': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'GameProperties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'GameSessionData': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Names (list) -- Unique identifier for a matchmaking configuration(s) to retrieve. To request all existing configurations, leave this parameter empty.
    
    (string) --
    
    
    RuleSetName (string) -- Unique identifier for a matchmaking rule set. Use this parameter to retrieve all matchmaking configurations that use this rule set.
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is limited to 10.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_matchmaking_rule_sets(Names=None, Limit=None, NextToken=None):
    """
    Retrieves the details for FlexMatch matchmaking rule sets. You can request all existing rule sets for the region, or provide a list of one or more rule set names. When requesting multiple items, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a rule set is returned for each requested name.
    Operations related to match configurations and rule sets include:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_matchmaking_rule_sets(
        Names=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: Unique identifier for a matchmaking rule set. This name is used to identify the rule set associated with a matchmaking configuration.
            (string) --
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'RuleSets': [
            {
                'RuleSetName': 'string',
                'RuleSetBody': 'string',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Names (list) -- Unique identifier for a matchmaking rule set. This name is used to identify the rule set associated with a matchmaking configuration.
    
    (string) --
    
    
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_player_sessions(GameSessionId=None, PlayerId=None, PlayerSessionId=None, PlayerSessionStatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves properties for one or more player sessions. This action can be used in several ways: (1) provide a PlayerSessionId to request properties for a specific player session; (2) provide a GameSessionId to request properties for all player sessions in the specified game session; (3) provide a PlayerId to request properties for all player sessions of a specified player.
    To get game session record(s), specify only one of the following: a player session ID, a game session ID, or a player ID. You can filter this request by player session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  PlayerSession object is returned for each session matching the request.
    Player-session-related operations include:
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
            RESERVED -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.
            ACTIVE -- The player has been validated by the server process and is currently connected.
            COMPLETED -- The player connection has been dropped.
            TIMEDOUT -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. If a player session ID is specified, this parameter is ignored.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored.

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
    GameSessionId (string) -- Unique identifier for the game session to retrieve player sessions for.
    PlayerId (string) -- Unique identifier for a player to retrieve player sessions for.
    PlayerSessionId (string) -- Unique identifier for a player session to retrieve.
    PlayerSessionStatusFilter (string) -- Player session status to filter results on.
    Possible player session statuses include the following:
    
    RESERVED -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.
    ACTIVE -- The player has been validated by the server process and is currently connected.
    COMPLETED -- The player connection has been dropped.
    TIMEDOUT -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).
    
    
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. If a player session ID is specified, this parameter is ignored.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored.
    
    """
    pass

def describe_runtime_configuration(FleetId=None):
    """
    Retrieves the current run-time configuration for the specified fleet. The run-time configuration tells Amazon GameLift how to launch server processes on instances in the fleet.
    Fleet-related operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_runtime_configuration(
        FleetId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet to get the run-time configuration for.
            

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
    Fleet-related operations include:
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
            ACTIVE -- The scaling policy is currently in force.
            UPDATEREQUESTED -- A request to update the scaling policy has been received.
            UPDATING -- A change is being made to the scaling policy.
            DELETEREQUESTED -- A request to delete the scaling policy has been received.
            DELETING -- The scaling policy is being deleted.
            DELETED -- The scaling policy has been deleted.
            ERROR -- An error occurred in creating the policy. It should be removed and recreated.
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

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
    FleetId (string) -- [REQUIRED]
    Unique identifier for a fleet to retrieve scaling policies for.
    
    StatusFilter (string) -- Scaling policy status to filter results on. A scaling policy is only in force when in an ACTIVE status.
    
    ACTIVE -- The scaling policy is currently in force.
    UPDATEREQUESTED -- A request to update the scaling policy has been received.
    UPDATING -- A change is being made to the scaling policy.
    DELETEREQUESTED -- A request to delete the scaling policy has been received.
    DELETING -- The scaling policy is being deleted.
    DELETED -- The scaling policy has been deleted.
    ERROR -- An error occurred in creating the policy. It should be removed and recreated.
    
    
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_vpc_peering_authorizations():
    """
    Retrieves valid VPC peering authorizations that are pending for the AWS account. This operation returns all VPC peering authorizations and requests for peering. This includes those initiated and received by this account.
    VPC peering connection operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_vpc_peering_authorizations()
    
    
    :rtype: dict
    :return: {
        'VpcPeeringAuthorizations': [
            {
                'GameLiftAwsAccountId': 'string',
                'PeerVpcAwsAccountId': 'string',
                'PeerVpcId': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'ExpirationTime': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    CreateVpcPeeringAuthorization
    DescribeVpcPeeringAuthorizations
    DeleteVpcPeeringAuthorization
    CreateVpcPeeringConnection
    DescribeVpcPeeringConnections
    DeleteVpcPeeringConnection
    
    """
    pass

def describe_vpc_peering_connections(FleetId=None):
    """
    Retrieves information on VPC peering connections. Use this operation to get peering information for all fleets or for one specific fleet ID.
    To retrieve connection information, call this operation from the AWS account that is used to manage the Amazon GameLift fleets. Specify a fleet ID or leave the parameter empty to retrieve all connection records. If successful, the retrieved information includes both active and pending connections. Active connections identify the IpV4 CIDR block that the VPC uses to connect.
    VPC peering connection operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.describe_vpc_peering_connections(
        FleetId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: Unique identifier for a fleet.

    :rtype: dict
    :return: {
        'VpcPeeringConnections': [
            {
                'FleetId': 'string',
                'IpV4CidrBlock': 'string',
                'VpcPeeringConnectionId': 'string',
                'Status': {
                    'Code': 'string',
                    'Message': 'string'
                },
                'PeerVpcId': 'string',
                'GameLiftVpcId': 'string'
            },
        ]
    }
    
    
    :returns: 
    CreateVpcPeeringAuthorization
    DescribeVpcPeeringAuthorizations
    DeleteVpcPeeringAuthorization
    CreateVpcPeeringConnection
    DescribeVpcPeeringConnections
    DeleteVpcPeeringConnection
    
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
    Retrieves the location of stored game session logs for a specified game session. When a game session is terminated, Amazon GameLift automatically stores the logs in Amazon S3 and retains them for 14 days. Use this URL to download the logs.
    Game-session-related operations include:
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

def get_waiter(waiter_name=None):
    """
    
    :type waiter_name: 
    :param waiter_name: 

    """
    pass

def list_aliases(RoutingStrategyType=None, Name=None, Limit=None, NextToken=None):
    """
    Retrieves all aliases for this AWS account. You can filter the result set by alias name and/or routing strategy type. Use the pagination parameters to retrieve results in sequential pages.
    Alias-related operations include:
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
            SIMPLE -- The alias resolves to one specific fleet. Use this type when routing to active fleets.
            TERMINAL -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
            

    :type Name: string
    :param Name: Descriptive label that is associated with an alias. Alias names do not need to be unique.

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

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
    RoutingStrategyType (string) -- Type of routing to filter results on. Use this parameter to retrieve only aliases of a certain type. To retrieve all aliases, leave this parameter empty.
    Possible routing types include the following:
    
    SIMPLE -- The alias resolves to one specific fleet. Use this type when routing to active fleets.
    TERMINAL -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
    
    
    Name (string) -- Descriptive label that is associated with an alias. Alias names do not need to be unique.
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def list_builds(Status=None, Limit=None, NextToken=None):
    """
    Retrieves build records for all builds associated with the AWS account in use. You can limit results to builds that are in a specific status by using the Status parameter. Use the pagination parameters to retrieve results in a set of sequential pages.
    Build-related operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.list_builds(
        Status='INITIALIZED'|'READY'|'FAILED',
        Limit=123,
        NextToken='string'
    )
    
    
    :type Status: string
    :param Status: Build status to filter results by. To retrieve all builds, leave this parameter empty.
            Possible build statuses include the following:
            INITIALIZED -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
            READY -- The game build has been successfully uploaded. You can now create new fleets for this build.
            FAILED -- The game build upload failed. You cannot create new fleets for this build.
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

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
    Status (string) -- Build status to filter results by. To retrieve all builds, leave this parameter empty.
    Possible build statuses include the following:
    
    INITIALIZED -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
    READY -- The game build has been successfully uploaded. You can now create new fleets for this build.
    FAILED -- The game build upload failed. You cannot create new fleets for this build.
    
    
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def list_fleets(BuildId=None, Limit=None, NextToken=None):
    """
    Retrieves a collection of fleet records for this AWS account. You can filter the result set by build ID. Use the pagination parameters to retrieve results in sequential pages.
    Fleet-related operations include:
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
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict
    :return: {
        'FleetIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    BuildId (string) -- Unique identifier for a build to return fleets for. Use this parameter to return only fleets using the specified build. To retrieve all fleets, leave this parameter empty.
    Limit (integer) -- Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
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
    Fleet-related operations include:
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
            ChangeInCapacity -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
            ExactCapacity -- set the instance count to the scaling adjustment value.
            PercentChangeInCapacity -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of '-10' scales the fleet down by 10%.
            

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
            ActivatingGameSessions -- number of game sessions in the process of being created (game session status = ACTIVATING ).
            ActiveGameSessions -- number of game sessions currently running (game session status = ACTIVE ).
            CurrentPlayerSessions -- number of active or reserved player sessions (player session status = ACTIVE or RESERVED ).
            AvailablePlayerSessions -- number of player session slots currently available in active game sessions across the fleet, calculated by subtracting a game session's current player session count from its maximum player session count. This number includes game sessions that are not currently accepting players (game session PlayerSessionCreationPolicy = DENY_ALL ).
            ActiveInstances -- number of instances currently running a game session.
            IdleInstances -- number of instances not currently running a game session.
            

    :rtype: dict
    :return: {
        'Name': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    Descriptive label that is associated with a scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.
    
    FleetId (string) -- [REQUIRED]
    Unique identifier for a fleet to apply this policy to.
    
    ScalingAdjustment (integer) -- [REQUIRED]
    Amount of adjustment to make, based on the scaling adjustment type.
    
    ScalingAdjustmentType (string) -- [REQUIRED]
    Type of adjustment to make to a fleet's instance count (see  FleetCapacity ):
    
    ChangeInCapacity -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
    ExactCapacity -- set the instance count to the scaling adjustment value.
    PercentChangeInCapacity -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of "-10" scales the fleet down by 10%.
    
    
    Threshold (float) -- [REQUIRED]
    Metric value used to trigger a scaling event.
    
    ComparisonOperator (string) -- [REQUIRED]
    Comparison operator to use when measuring the metric against the threshold value.
    
    EvaluationPeriods (integer) -- [REQUIRED]
    Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
    
    MetricName (string) -- [REQUIRED]
    Name of the Amazon GameLift-defined metric that is used to trigger an adjustment.
    
    ActivatingGameSessions -- number of game sessions in the process of being created (game session status = ACTIVATING ).
    ActiveGameSessions -- number of game sessions currently running (game session status = ACTIVE ).
    CurrentPlayerSessions -- number of active or reserved player sessions (player session status = ACTIVE or RESERVED ).
    AvailablePlayerSessions -- number of player session slots currently available in active game sessions across the fleet, calculated by subtracting a game session's current player session count from its maximum player session count. This number includes game sessions that are not currently accepting players (game session PlayerSessionCreationPolicy = DENY_ALL ).
    ActiveInstances -- number of instances currently running a game session.
    IdleInstances -- number of instances not currently running a game session.
    
    
    
    """
    pass

def request_upload_credentials(BuildId=None):
    """
    Retrieves a fresh set of credentials for use when uploading a new set of game build files to Amazon GameLift's Amazon S3. This is done as part of the build creation process; see  CreateBuild .
    To request new credentials, specify the build ID as returned with an initial CreateBuild request. If successful, a new set of credentials are returned, along with the S3 storage location associated with the build ID.
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
    Alias-related operations include:
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
    Retrieves all active game sessions that match a set of search criteria and sorts them in a specified order. You can search or sort by the following game session attributes:
    To search or sort, specify either a fleet ID or an alias ID, and provide a search filter expression, a sort expression, or both. If successful, a collection of  GameSession objects matching the request is returned. Use the pagination parameters to retrieve results as a set of sequential pages.
    You can search for game sessions one fleet at a time only. To find game sessions across multiple fleets, you must search each fleet separately and combine the results. This search feature finds only game sessions that are in ACTIVE status. To locate games in statuses other than active, use  DescribeGameSessionDetails .
    Game-session-related operations include:
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
            Operand -- Name of a game session attribute. Valid values are gameSessionName , gameSessionId , gameSessionProperties , maximumSessions , creationTimeMillis , playerSessionCount , hasAvailablePlayerSessions .
            Comparator -- Valid comparators are: = , , , , = , = .
            Value -- Value to be searched for. Values may be numbers, boolean values (true/false) or strings depending on the operand. String values are case sensitive and must be enclosed in single quotes. Special characters must be escaped. Boolean and string values can only be used with the comparators = and . For example, the following filter expression searches on gameSessionName : 'FilterExpression': 'gameSessionName = 'Matt\\'s Awesome Game 1'' .
            To chain multiple conditions in a single expression, use the logical keywords AND , OR , and NOT and parentheses as needed. For example: x AND y AND NOT z , NOT (x OR y) .
            Session search evaluates conditions from left to right using the following precedence rules:
            = , , , , = , =
            Parentheses
            NOT
            AND
            OR
            For example, this filter expression retrieves game sessions hosting at least ten players that have an open player slot: 'maximumSessions=10 AND hasAvailablePlayerSessions=true' .
            

    :type SortExpression: string
    :param SortExpression: Instructions on how to sort the search results. If no sort expression is included, the request returns results in random order. A sort expression consists of the following elements:
            Operand -- Name of a game session attribute. Valid values are gameSessionName , gameSessionId , gameSessionProperties , maximumSessions , creationTimeMillis , playerSessionCount , hasAvailablePlayerSessions .
            Order -- Valid sort orders are ASC (ascending) and DESC (descending).
            For example, this sort expression returns the oldest active sessions first: 'SortExpression': 'creationTimeMillis ASC' . Results with a null value for the sort operand are returned at the end of the list.
            

    :type Limit: integer
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. The maximum number of results returned is 20, even if this value is not set or is set higher than 20.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

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
                'StatusReason': 'INTERRUPTED',
                'GameProperties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'IpAddress': 'string',
                'Port': 123,
                'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
                'CreatorId': 'string',
                'GameSessionData': 'string',
                'MatchmakerData': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CreateGameSession
    DescribeGameSessions
    DescribeGameSessionDetails
    SearchGameSessions
    UpdateGameSession
    GetGameSessionLogUrl
    Game session placements
    StartGameSessionPlacement
    DescribeGameSessionPlacement
    StopGameSessionPlacement
    
    
    
    """
    pass

def start_game_session_placement(PlacementId=None, GameSessionQueueName=None, GameProperties=None, MaximumPlayerSessionCount=None, GameSessionName=None, PlayerLatencies=None, DesiredPlayerSessions=None, GameSessionData=None):
    """
    Places a request for a new game session in a queue (see  CreateGameSessionQueue ). When processing a placement request, Amazon GameLift searches for available resources on the queue's destinations, scanning each until it finds resources or the placement request times out.
    A game session placement request can also request player sessions. When a new game session is successfully created, Amazon GameLift creates a player session for each player included in the request.
    When placing a game session, by default Amazon GameLift tries each fleet in the order they are listed in the queue configuration. Ideally, a queue's destinations are listed in preference order.
    Alternatively, when requesting a game session with players, you can also provide latency data for each player in relevant regions. Latency data indicates the performance lag a player experiences when connected to a fleet in the region. Amazon GameLift uses latency data to reorder the list of destinations to place the game session in a region with minimal lag. If latency data is provided for multiple players, Amazon GameLift calculates each region's average lag for all players and reorders to get the best game play across all players.
    To place a new game session request, specify the following:
    If successful, a new game session placement is created.
    To track the status of a placement request, call  DescribeGameSessionPlacement and check the request's status. If the status is FULFILLED , a new game session has been created and a game session ARN and region are referenced. If the placement request times out, you can resubmit the request or retry it with a different queue.
    Game-session-related operations include:
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
        ],
        GameSessionData='string'
    )
    
    
    :type PlacementId: string
    :param PlacementId: [REQUIRED]
            Unique identifier to assign to the new game session placement. This value is developer-defined. The value must be unique across all regions and cannot be reused unless you are resubmitting a canceled or timed-out placement request.
            

    :type GameSessionQueueName: string
    :param GameSessionQueueName: [REQUIRED]
            Name of the queue to use to place the new game session.
            

    :type GameProperties: list
    :param GameProperties: Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ).
            (dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the Amazon GameLift Developer Guide .
            Key (string) -- [REQUIRED]Game property identifier.
            Value (string) -- [REQUIRED]Game property value.
            
            

    :type MaximumPlayerSessionCount: integer
    :param MaximumPlayerSessionCount: [REQUIRED]
            Maximum number of players that can be connected simultaneously to the game session.
            

    :type GameSessionName: string
    :param GameSessionName: Descriptive label that is associated with a game session. Session names do not need to be unique.

    :type PlayerLatencies: list
    :param PlayerLatencies: Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions. This information is used to try to place the new game session where it can offer the best possible gameplay experience for the players.
            (dict) --Regional latency information for a player, used when requesting a new game session with StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified region. The relative difference between a player's latency values for multiple regions are used to determine which fleets are best suited to place a new game session for the player.
            PlayerId (string) --Unique identifier for a player associated with the latency data.
            RegionIdentifier (string) --Name of the region that is associated with the latency value.
            LatencyInMilliseconds (float) --Amount of time that represents the time lag experienced by the player when connected to the specified region.
            
            

    :type DesiredPlayerSessions: list
    :param DesiredPlayerSessions: Set of information on each player to create a player session for.
            (dict) --Player information for use when creating player sessions using a game session placement request with StartGameSessionPlacement .
            PlayerId (string) --Unique identifier for a player to associate with the player session.
            PlayerData (string) --Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.
            
            

    :type GameSessionData: string
    :param GameSessionData: Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ).

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
            ],
            'GameSessionData': 'string',
            'MatchmakerData': 'string'
        }
    }
    
    
    :returns: 
    CreateGameSession
    DescribeGameSessions
    DescribeGameSessionDetails
    SearchGameSessions
    UpdateGameSession
    GetGameSessionLogUrl
    Game session placements
    StartGameSessionPlacement
    DescribeGameSessionPlacement
    StopGameSessionPlacement
    
    
    
    """
    pass

def start_match_backfill(TicketId=None, ConfigurationName=None, GameSessionArn=None, Players=None):
    """
    Finds new players to fill open slots in an existing game session. This operation can be used to add players to matched games that start with fewer than the maximum number of players or to replace players when they drop out. By backfilling with the same matchmaker used to create the original match, you ensure that new players meet the match criteria and maintain a consistent experience throughout the game session. You can backfill a match anytime after a game session has been created.
    To request a match backfill, specify a unique ticket ID, the existing game session's ARN, a matchmaking configuration, and a set of data that describes all current players in the game session. If successful, a match backfill ticket is created and returned with status set to QUEUED. The ticket is placed in the matchmaker's ticket pool and processed. Track the status of the ticket to respond as needed. For more detail how to set up backfilling, see Backfill Existing Games with FlexMatch .
    The process of finding backfill matches is essentially identical to the initial matchmaking process. The matchmaker searches the pool and groups tickets together to form potential matches, allowing only one backfill ticket per potential match. Once the a match is formed, the matchmaker creates player sessions for the new players. All tickets in the match are updated with the game session's connection information, and the  GameSession object is updated to include matchmaker data on the new players. For more detail on how match backfill requests are processed, see How Amazon GameLift FlexMatch Works .
    Matchmaking-related operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.start_match_backfill(
        TicketId='string',
        ConfigurationName='string',
        GameSessionArn='string',
        Players=[
            {
                'PlayerId': 'string',
                'PlayerAttributes': {
                    'string': {
                        'S': 'string',
                        'N': 123.0,
                        'SL': [
                            'string',
                        ],
                        'SDM': {
                            'string': 123.0
                        }
                    }
                },
                'Team': 'string',
                'LatencyInMs': {
                    'string': 123
                }
            },
        ]
    )
    
    
    :type TicketId: string
    :param TicketId: Unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift will generate one in the form of a UUID. Use this identifier to track the match backfill ticket status and retrieve match results.

    :type ConfigurationName: string
    :param ConfigurationName: [REQUIRED]
            Name of the matchmaker to use for this request. The name of the matchmaker that was used with the original game session is listed in the GameSession object, MatchmakerData property. This property contains a matchmaking configuration ARN value, which includes the matchmaker name. (In the ARN value 'arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MM-4v4', the matchmaking configuration name is 'MM-4v4'.) Use only the name for this parameter.
            

    :type GameSessionArn: string
    :param GameSessionArn: [REQUIRED]
            Amazon Resource Name (ARN ) that is assigned to a game session and uniquely identifies it.
            

    :type Players: list
    :param Players: [REQUIRED]
            Match information on all players that are currently assigned to the game session. This information is used by the matchmaker to find new players and add them to the existing game.
            PlayerID, PlayerAttributes, Team -\- This information is maintained in the GameSession object, MatchmakerData property, for all players who are currently assigned to the game session. The matchmaker data is in JSON syntax, formatted as a string. For more details, see Match Data .
            LatencyInMs -\- If the matchmaker uses player latency, include a latency value, in milliseconds, for the region that the game session is currently in. Do not include latency values for any other region.
            (dict) --Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
            PlayerId (string) --Unique identifier for a player
            PlayerAttributes (dict) --Collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the playerAttributes used in a matchmaking rule set. Example: 'PlayerAttributes': {'skill': {'N': '23'}, 'gameMode': {'S': 'deathmatch'}} .
            (string) --
            (dict) --Values for use in Player attribute key:value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array or data map. Each AttributeValue object can use only one of the available properties.
            S (string) --For single string values. Maximum string length is 100 characters.
            N (float) --For number values, expressed as double.
            SL (list) --For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
            (string) --
            SDM (dict) --For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.
            (string) --
            (float) --
            
            
            Team (string) --Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.
            LatencyInMs (dict) --Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions. If this property is present, FlexMatch considers placing the match only in regions for which latency is reported.
            If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no regions are available to the player and the ticket is not matchable.
            (string) --
            (integer) --
            
            

    :rtype: dict
    :return: {
        'MatchmakingTicket': {
            'TicketId': 'string',
            'ConfigurationName': 'string',
            'Status': 'CANCELLED'|'COMPLETED'|'FAILED'|'PLACING'|'QUEUED'|'REQUIRES_ACCEPTANCE'|'SEARCHING'|'TIMED_OUT',
            'StatusReason': 'string',
            'StatusMessage': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'Players': [
                {
                    'PlayerId': 'string',
                    'PlayerAttributes': {
                        'string': {
                            'S': 'string',
                            'N': 123.0,
                            'SL': [
                                'string',
                            ],
                            'SDM': {
                                'string': 123.0
                            }
                        }
                    },
                    'Team': 'string',
                    'LatencyInMs': {
                        'string': 123
                    }
                },
            ],
            'GameSessionConnectionInfo': {
                'GameSessionArn': 'string',
                'IpAddress': 'string',
                'Port': 123,
                'MatchedPlayerSessions': [
                    {
                        'PlayerId': 'string',
                        'PlayerSessionId': 'string'
                    },
                ]
            },
            'EstimatedWaitTime': 123
        }
    }
    
    
    :returns: 
    TicketId (string) -- Unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift will generate one in the form of a UUID. Use this identifier to track the match backfill ticket status and retrieve match results.
    ConfigurationName (string) -- [REQUIRED]
    Name of the matchmaker to use for this request. The name of the matchmaker that was used with the original game session is listed in the  GameSession object, MatchmakerData property. This property contains a matchmaking configuration ARN value, which includes the matchmaker name. (In the ARN value "arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MM-4v4", the matchmaking configuration name is "MM-4v4".) Use only the name for this parameter.
    
    GameSessionArn (string) -- [REQUIRED]
    Amazon Resource Name (ARN ) that is assigned to a game session and uniquely identifies it.
    
    Players (list) -- [REQUIRED]
    Match information on all players that are currently assigned to the game session. This information is used by the matchmaker to find new players and add them to the existing game.
    
    PlayerID, PlayerAttributes, Team -\- This information is maintained in the  GameSession object, MatchmakerData property, for all players who are currently assigned to the game session. The matchmaker data is in JSON syntax, formatted as a string. For more details, see Match Data .
    LatencyInMs -\- If the matchmaker uses player latency, include a latency value, in milliseconds, for the region that the game session is currently in. Do not include latency values for any other region.
    
    
    (dict) --Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
    
    PlayerId (string) --Unique identifier for a player
    
    PlayerAttributes (dict) --Collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the playerAttributes used in a matchmaking rule set. Example: "PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}} .
    
    (string) --
    (dict) --Values for use in  Player attribute key:value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array or data map. Each AttributeValue object can use only one of the available properties.
    
    S (string) --For single string values. Maximum string length is 100 characters.
    
    N (float) --For number values, expressed as double.
    
    SL (list) --For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
    
    (string) --
    
    
    SDM (dict) --For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.
    
    (string) --
    (float) --
    
    
    
    
    
    
    
    
    
    
    Team (string) --Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.
    
    LatencyInMs (dict) --Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions. If this property is present, FlexMatch considers placing the match only in regions for which latency is reported.
    If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no regions are available to the player and the ticket is not matchable.
    
    (string) --
    (integer) --
    
    
    
    
    
    
    
    
    
    """
    pass

def start_matchmaking(TicketId=None, ConfigurationName=None, Players=None):
    """
    Uses FlexMatch to create a game match for a group of players based on custom matchmaking rules, and starts a new game for the matched players. Each matchmaking request specifies the type of match to build (team configuration, rules for an acceptable match, etc.). The request also specifies the players to find a match for and where to host the new game session for optimal performance. A matchmaking request might start with a single player or a group of players who want to play together. FlexMatch finds additional players as needed to fill the match. Match type, rules, and the queue used to place a new game session are defined in a MatchmakingConfiguration . For complete information on setting up and using FlexMatch, see the topic Adding FlexMatch to Your Game .
    To start matchmaking, provide a unique ticket ID, specify a matchmaking configuration, and include the players to be matched. You must also include a set of player attributes relevant for the matchmaking configuration. If successful, a matchmaking ticket is returned with status set to QUEUED . Track the status of the ticket to respond as needed and acquire game session connection information for successfully completed matches.
    Matchmaking-related operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.start_matchmaking(
        TicketId='string',
        ConfigurationName='string',
        Players=[
            {
                'PlayerId': 'string',
                'PlayerAttributes': {
                    'string': {
                        'S': 'string',
                        'N': 123.0,
                        'SL': [
                            'string',
                        ],
                        'SDM': {
                            'string': 123.0
                        }
                    }
                },
                'Team': 'string',
                'LatencyInMs': {
                    'string': 123
                }
            },
        ]
    )
    
    
    :type TicketId: string
    :param TicketId: Unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift will generate one in the form of a UUID. Use this identifier to track the matchmaking ticket status and retrieve match results.

    :type ConfigurationName: string
    :param ConfigurationName: [REQUIRED]
            Name of the matchmaking configuration to use for this request. Matchmaking configurations must exist in the same region as this request.
            

    :type Players: list
    :param Players: [REQUIRED]
            Information on each player to be matched. This information must include a player ID, and may contain player attributes and latency data to be used in the matchmaking process. After a successful match, Player objects contain the name of the team the player is assigned to.
            (dict) --Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
            PlayerId (string) --Unique identifier for a player
            PlayerAttributes (dict) --Collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the playerAttributes used in a matchmaking rule set. Example: 'PlayerAttributes': {'skill': {'N': '23'}, 'gameMode': {'S': 'deathmatch'}} .
            (string) --
            (dict) --Values for use in Player attribute key:value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array or data map. Each AttributeValue object can use only one of the available properties.
            S (string) --For single string values. Maximum string length is 100 characters.
            N (float) --For number values, expressed as double.
            SL (list) --For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
            (string) --
            SDM (dict) --For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.
            (string) --
            (float) --
            
            
            Team (string) --Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.
            LatencyInMs (dict) --Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS regions. If this property is present, FlexMatch considers placing the match only in regions for which latency is reported.
            If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no regions are available to the player and the ticket is not matchable.
            (string) --
            (integer) --
            
            

    :rtype: dict
    :return: {
        'MatchmakingTicket': {
            'TicketId': 'string',
            'ConfigurationName': 'string',
            'Status': 'CANCELLED'|'COMPLETED'|'FAILED'|'PLACING'|'QUEUED'|'REQUIRES_ACCEPTANCE'|'SEARCHING'|'TIMED_OUT',
            'StatusReason': 'string',
            'StatusMessage': 'string',
            'StartTime': datetime(2015, 1, 1),
            'EndTime': datetime(2015, 1, 1),
            'Players': [
                {
                    'PlayerId': 'string',
                    'PlayerAttributes': {
                        'string': {
                            'S': 'string',
                            'N': 123.0,
                            'SL': [
                                'string',
                            ],
                            'SDM': {
                                'string': 123.0
                            }
                        }
                    },
                    'Team': 'string',
                    'LatencyInMs': {
                        'string': 123
                    }
                },
            ],
            'GameSessionConnectionInfo': {
                'GameSessionArn': 'string',
                'IpAddress': 'string',
                'Port': 123,
                'MatchedPlayerSessions': [
                    {
                        'PlayerId': 'string',
                        'PlayerSessionId': 'string'
                    },
                ]
            },
            'EstimatedWaitTime': 123
        }
    }
    
    
    :returns: 
    Your client code submits a StartMatchmaking request for one or more players and tracks the status of the request ticket.
    FlexMatch uses this ticket and others in process to build an acceptable match. When a potential match is identified, all tickets in the proposed match are advanced to the next status.
    If the match requires player acceptance (set in the matchmaking configuration), the tickets move into status REQUIRES_ACCEPTANCE . This status triggers your client code to solicit acceptance from all players in every ticket involved in the match, and then call  AcceptMatch for each player. If any player rejects or fails to accept the match before a specified timeout, the proposed match is dropped (see AcceptMatch for more details).
    Once a match is proposed and accepted, the matchmaking tickets move into status PLACING . FlexMatch locates resources for a new game session using the game session queue (set in the matchmaking configuration) and creates the game session based on the match data.
    When the match is successfully placed, the matchmaking tickets move into COMPLETED status. Connection information (including game session endpoint and player session) is added to the matchmaking tickets. Matched players can use the connection information to join the game.
    
    """
    pass

def stop_game_session_placement(PlacementId=None):
    """
    Cancels a game session placement that is in PENDING status. To stop a placement, provide the placement ID values. If successful, the placement is moved to CANCELLED status.
    Game-session-related operations include:
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
            ],
            'GameSessionData': 'string',
            'MatchmakerData': 'string'
        }
    }
    
    
    :returns: 
    PENDING -- The placement request is currently in the queue waiting to be processed.
    FULFILLED -- A new game session and player sessions (if requested) have been successfully created. Values for GameSessionArn and GameSessionRegion are available.
    CANCELLED -- The placement request was canceled with a call to  StopGameSessionPlacement .
    TIMED_OUT -- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed.
    
    """
    pass

def stop_matchmaking(TicketId=None):
    """
    Cancels a matchmaking ticket that is currently being processed. To stop the matchmaking operation, specify the ticket ID. If successful, work on the ticket is stopped, and the ticket status is changed to CANCELLED .
    Matchmaking-related operations include:
    See also: AWS API Documentation
    
    
    :example: response = client.stop_matchmaking(
        TicketId='string'
    )
    
    
    :type TicketId: string
    :param TicketId: [REQUIRED]
            Unique identifier for a matchmaking ticket.
            

    :rtype: dict
    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_alias(AliasId=None, Name=None, Description=None, RoutingStrategy=None):
    """
    Updates properties for an alias. To update properties, specify the alias ID to be updated and provide the information to be changed. To reassign an alias to another fleet, provide an updated routing strategy. If successful, the updated alias record is returned.
    Alias-related operations include:
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
            SIMPLE -- The alias resolves to one specific fleet. Use this type when routing to active fleets.
            TERMINAL -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
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
    AliasId (string) -- [REQUIRED]
    Unique identifier for a fleet alias. Specify the alias you want to update.
    
    Name (string) -- Descriptive label that is associated with an alias. Alias names do not need to be unique.
    Description (string) -- Human-readable description of an alias.
    RoutingStrategy (dict) -- Object that specifies the fleet and routing type to use for the alias.
    
    Type (string) --Type of routing strategy.
    Possible routing types include the following:
    
    SIMPLE -- The alias resolves to one specific fleet. Use this type when routing to active fleets.
    TERMINAL -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
    
    
    FleetId (string) --Unique identifier for a fleet that the alias points to.
    
    Message (string) --Message text to be used with a terminal routing strategy.
    
    
    
    
    """
    pass

def update_build(BuildId=None, Name=None, Version=None):
    """
    Updates metadata in a build record, including the build name and version. To update the metadata, specify the build ID to update and provide the new values. If successful, a build object containing the updated metadata is returned.
    Build-related operations include:
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
    BuildId (string) -- [REQUIRED]
    Unique identifier for a build to update.
    
    Name (string) -- Descriptive label that is associated with a build. Build names do not need to be unique.
    Version (string) -- Version that is associated with this build. Version strings do not need to be unique.
    
    """
    pass

def update_fleet_attributes(FleetId=None, Name=None, Description=None, NewGameSessionProtectionPolicy=None, ResourceCreationLimitPolicy=None, MetricGroups=None):
    """
    Updates fleet properties, including name and description, for a fleet. To update metadata, specify the fleet ID and the property values that you want to change. If successful, the fleet ID for the updated fleet is returned.
    Fleet-related operations include:
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
            NoProtection -- The game session can be terminated during a scale-down event.
            FullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
            

    :type ResourceCreationLimitPolicy: dict
    :param ResourceCreationLimitPolicy: Policy that limits the number of game sessions an individual player can create over a span of time.
            NewGameSessionsPerCreator (integer) --Maximum number of game sessions that an individual can create during the policy period.
            PolicyPeriodInMinutes (integer) --Time span used in evaluating the resource creation limit policy.
            

    :type MetricGroups: list
    :param MetricGroups: Names of metric groups to include this fleet in. Amazon CloudWatch uses a fleet metric group is to aggregate metrics from multiple fleets. Use an existing metric group name to add this fleet to the group. Or use a new name to create a new metric group. A fleet can only be included in one metric group at a time.
            (string) --
            

    :rtype: dict
    :return: {
        'FleetId': 'string'
    }
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    Unique identifier for a fleet to update attribute metadata for.
    
    Name (string) -- Descriptive label that is associated with a fleet. Fleet names do not need to be unique.
    Description (string) -- Human-readable description of a fleet.
    NewGameSessionProtectionPolicy (string) -- Game session protection policy to apply to all new instances created in this fleet. Instances that already exist are not affected. You can set protection for individual instances using  UpdateGameSession .
    
    NoProtection -- The game session can be terminated during a scale-down event.
    FullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
    
    
    ResourceCreationLimitPolicy (dict) -- Policy that limits the number of game sessions an individual player can create over a span of time.
    
    NewGameSessionsPerCreator (integer) --Maximum number of game sessions that an individual can create during the policy period.
    
    PolicyPeriodInMinutes (integer) --Time span used in evaluating the resource creation limit policy.
    
    
    
    MetricGroups (list) -- Names of metric groups to include this fleet in. Amazon CloudWatch uses a fleet metric group is to aggregate metrics from multiple fleets. Use an existing metric group name to add this fleet to the group. Or use a new name to create a new metric group. A fleet can only be included in one metric group at a time.
    
    (string) --
    
    
    
    """
    pass

def update_fleet_capacity(FleetId=None, DesiredInstances=None, MinSize=None, MaxSize=None):
    """
    Updates capacity settings for a fleet. Use this action to specify the number of EC2 instances (hosts) that you want this fleet to contain. Before calling this action, you may want to call  DescribeEC2InstanceLimits to get the maximum capacity based on the fleet's EC2 instance type.
    If you're using autoscaling (see  PutScalingPolicy ), you may want to specify a minimum and/or maximum capacity. If you don't provide these, autoscaling can set capacity anywhere between zero and the service limits .
    To update fleet capacity, specify the fleet ID and the number of instances you want the fleet to host. If successful, Amazon GameLift starts or terminates instances so that the fleet's active instance count matches the desired instance count. You can view a fleet's current capacity information by calling  DescribeFleetCapacity . If the desired instance count is higher than the instance type's limit, the "Limit Exceeded" exception occurs.
    Fleet-related operations include:
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
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    Unique identifier for a fleet to update capacity for.
    
    DesiredInstances (integer) -- Number of EC2 instances you want this fleet to host.
    MinSize (integer) -- Minimum value allowed for the fleet's instance count. Default if not set is 0.
    MaxSize (integer) -- Maximum value allowed for the fleet's instance count. Default if not set is 1.
    
    """
    pass

def update_fleet_port_settings(FleetId=None, InboundPermissionAuthorizations=None, InboundPermissionRevocations=None):
    """
    Updates port settings for a fleet. To update settings, specify the fleet ID to be updated and list the permissions you want to update. List the permissions you want to add in InboundPermissionAuthorizations , and permissions you want to remove in InboundPermissionRevocations . Permissions to be removed must match existing fleet permissions. If successful, the fleet ID for the updated fleet is returned.
    Fleet-related operations include:
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
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    Unique identifier for a fleet to update port settings for.
    
    InboundPermissionAuthorizations (list) -- Collection of port settings to be added to the fleet record.
    
    (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on Amazon GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet's allowed ranges. This combination is included in the  GameSession object.
    
    FromPort (integer) -- [REQUIRED]Starting value for a range of allowed port numbers.
    
    ToPort (integer) -- [REQUIRED]Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
    
    IpRange (string) -- [REQUIRED]Range of allowed IP addresses. This value must be expressed in CIDR notation. Example: "000.000.000.000/[subnet mask] " or optionally the shortened version "0.0.0.0/[subnet mask] ".
    
    Protocol (string) -- [REQUIRED]Network communication protocol used by the fleet.
    
    
    
    
    
    InboundPermissionRevocations (list) -- Collection of port settings to be removed from the fleet record.
    
    (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on Amazon GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet's allowed ranges. This combination is included in the  GameSession object.
    
    FromPort (integer) -- [REQUIRED]Starting value for a range of allowed port numbers.
    
    ToPort (integer) -- [REQUIRED]Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
    
    IpRange (string) -- [REQUIRED]Range of allowed IP addresses. This value must be expressed in CIDR notation. Example: "000.000.000.000/[subnet mask] " or optionally the shortened version "0.0.0.0/[subnet mask] ".
    
    Protocol (string) -- [REQUIRED]Network communication protocol used by the fleet.
    
    
    
    
    
    
    """
    pass

def update_game_session(GameSessionId=None, MaximumPlayerSessionCount=None, Name=None, PlayerSessionCreationPolicy=None, ProtectionPolicy=None):
    """
    Updates game session properties. This includes the session name, maximum player count, protection policy, which controls whether or not an active game session can be terminated during a scale-down event, and the player session creation policy, which controls whether or not new players can join the session. To update a game session, specify the game session ID and the values you want to change. If successful, an updated  GameSession object is returned.
    Game-session-related operations include:
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
            NoProtection -- The game session can be terminated during a scale-down event.
            FullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
            

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
            'StatusReason': 'INTERRUPTED',
            'GameProperties': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'IpAddress': 'string',
            'Port': 123,
            'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
            'CreatorId': 'string',
            'GameSessionData': 'string',
            'MatchmakerData': 'string'
        }
    }
    
    
    :returns: 
    GameSessionId (string) -- [REQUIRED]
    Unique identifier for the game session to update.
    
    MaximumPlayerSessionCount (integer) -- Maximum number of players that can be connected simultaneously to the game session.
    Name (string) -- Descriptive label that is associated with a game session. Session names do not need to be unique.
    PlayerSessionCreationPolicy (string) -- Policy determining whether or not the game session accepts new players.
    ProtectionPolicy (string) -- Game session protection policy to apply to this game session only.
    
    NoProtection -- The game session can be terminated during a scale-down event.
    FullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
    
    
    
    """
    pass

def update_game_session_queue(Name=None, TimeoutInSeconds=None, PlayerLatencyPolicies=None, Destinations=None):
    """
    Updates settings for a game session queue, which determines how new game session requests in the queue are processed. To update settings, specify the queue name to be updated and provide the new settings. When updating destinations, provide a complete list of destinations.
    Queue-related operations include:
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
            Descriptive label that is associated with game session queue. Queue names must be unique within each region.
            

    :type TimeoutInSeconds: integer
    :param TimeoutInSeconds: Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.

    :type PlayerLatencyPolicies: list
    :param PlayerLatencyPolicies: Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. When updating policies, provide a complete collection of policies.
            (dict) --Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
            Queue-related operations include:
            CreateGameSessionQueue
            DescribeGameSessionQueues
            UpdateGameSessionQueue
            DeleteGameSessionQueue
            MaximumIndividualPlayerLatencyMilliseconds (integer) --The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
            PolicyDurationSeconds (integer) --The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
            
            

    :type Destinations: list
    :param Destinations: List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order. When updating this list, provide a complete list of destinations.
            (dict) --Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue.
            Queue-related operations include:
            CreateGameSessionQueue
            DescribeGameSessionQueues
            UpdateGameSessionQueue
            DeleteGameSessionQueue
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
    Name (string) -- [REQUIRED]
    Descriptive label that is associated with game session queue. Queue names must be unique within each region.
    
    TimeoutInSeconds (integer) -- Maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.
    PlayerLatencyPolicies (list) -- Collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, it is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. When updating policies, provide a complete collection of policies.
    
    (dict) --Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed at any destination in a region where a player is reporting latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
    Queue-related operations include:
    
    CreateGameSessionQueue
    DescribeGameSessionQueues
    UpdateGameSessionQueue
    DeleteGameSessionQueue
    
    
    MaximumIndividualPlayerLatencyMilliseconds (integer) --The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
    
    PolicyDurationSeconds (integer) --The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
    
    
    
    
    
    Destinations (list) -- List of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order. When updating this list, provide a complete list of destinations.
    
    (dict) --Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination configured for a queue.
    Queue-related operations include:
    
    CreateGameSessionQueue
    DescribeGameSessionQueues
    UpdateGameSessionQueue
    DeleteGameSessionQueue
    
    
    DestinationArn (string) --Amazon Resource Name (ARN) assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a region name, provide a unique identifier across all regions.
    
    
    
    
    
    
    """
    pass

def update_matchmaking_configuration(Name=None, Description=None, GameSessionQueueArns=None, RequestTimeoutSeconds=None, AcceptanceTimeoutSeconds=None, AcceptanceRequired=None, RuleSetName=None, NotificationTarget=None, AdditionalPlayerCount=None, CustomEventData=None, GameProperties=None, GameSessionData=None):
    """
    Updates settings for a FlexMatch matchmaking configuration. To update settings, specify the configuration name to be updated and provide the new settings.
    Operations related to match configurations and rule sets include:
    See also: AWS API Documentation
    
    
    :example: response = client.update_matchmaking_configuration(
        Name='string',
        Description='string',
        GameSessionQueueArns=[
            'string',
        ],
        RequestTimeoutSeconds=123,
        AcceptanceTimeoutSeconds=123,
        AcceptanceRequired=True|False,
        RuleSetName='string',
        NotificationTarget='string',
        AdditionalPlayerCount=123,
        CustomEventData='string',
        GameProperties=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        GameSessionData='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            Unique identifier for a matchmaking configuration to update.
            

    :type Description: string
    :param Description: Descriptive label that is associated with matchmaking configuration.

    :type GameSessionQueueArns: list
    :param GameSessionQueueArns: Amazon Resource Name (ARN ) that is assigned to a game session queue and uniquely identifies it. Format is arn:aws:gamelift:region::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912 . These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any region.
            (string) --
            

    :type RequestTimeoutSeconds: integer
    :param RequestTimeoutSeconds: Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that time out can be resubmitted as needed.

    :type AcceptanceTimeoutSeconds: integer
    :param AcceptanceTimeoutSeconds: Length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.

    :type AcceptanceRequired: boolean
    :param AcceptanceRequired: Flag that determines whether or not a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.

    :type RuleSetName: string
    :param RuleSetName: Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same region.

    :type NotificationTarget: string
    :param NotificationTarget: SNS topic ARN that is set up to receive matchmaking notifications. See Setting up Notifications for Matchmaking for more information.

    :type AdditionalPlayerCount: integer
    :param AdditionalPlayerCount: Number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match.

    :type CustomEventData: string
    :param CustomEventData: Information to attached to all events related to the matchmaking configuration.

    :type GameProperties: list
    :param GameProperties: Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new GameSession object that is created for a successful match.
            (dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the Amazon GameLift Developer Guide .
            Key (string) -- [REQUIRED]Game property identifier.
            Value (string) -- [REQUIRED]Game property value.
            
            

    :type GameSessionData: string
    :param GameSessionData: Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new GameSession object that is created for a successful match.

    :rtype: dict
    :return: {
        'Configuration': {
            'Name': 'string',
            'Description': 'string',
            'GameSessionQueueArns': [
                'string',
            ],
            'RequestTimeoutSeconds': 123,
            'AcceptanceTimeoutSeconds': 123,
            'AcceptanceRequired': True|False,
            'RuleSetName': 'string',
            'NotificationTarget': 'string',
            'AdditionalPlayerCount': 123,
            'CustomEventData': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'GameProperties': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'GameSessionData': 'string'
        }
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    Unique identifier for a matchmaking configuration to update.
    
    Description (string) -- Descriptive label that is associated with matchmaking configuration.
    GameSessionQueueArns (list) -- Amazon Resource Name (ARN ) that is assigned to a game session queue and uniquely identifies it. Format is arn:aws:gamelift:region::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912 . These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any region.
    
    (string) --
    
    
    RequestTimeoutSeconds (integer) -- Maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that time out can be resubmitted as needed.
    AcceptanceTimeoutSeconds (integer) -- Length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
    AcceptanceRequired (boolean) -- Flag that determines whether or not a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.
    RuleSetName (string) -- Unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same region.
    NotificationTarget (string) -- SNS topic ARN that is set up to receive matchmaking notifications. See Setting up Notifications for Matchmaking for more information.
    AdditionalPlayerCount (integer) -- Number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match.
    CustomEventData (string) -- Information to attached to all events related to the matchmaking configuration.
    GameProperties (list) -- Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.
    
    (dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session, such as to specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session; the server process uses the properties as appropriate. For more information, see the Amazon GameLift Developer Guide .
    
    Key (string) -- [REQUIRED]Game property identifier.
    
    Value (string) -- [REQUIRED]Game property value.
    
    
    
    
    
    GameSessionData (string) -- Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.
    
    """
    pass

def update_runtime_configuration(FleetId=None, RuntimeConfiguration=None):
    """
    Updates the current run-time configuration for the specified fleet, which tells Amazon GameLift how to launch server processes on instances in the fleet. You can update a fleet's run-time configuration at any time after the fleet is created; it does not need to be in an ACTIVE status.
    To update run-time configuration, specify the fleet ID and provide a RuntimeConfiguration object with the updated collection of server process configurations.
    Each instance in a Amazon GameLift fleet checks regularly for an updated run-time configuration and changes how it launches server processes to comply with the latest version. Existing server processes are not affected by the update; they continue to run until they end, while Amazon GameLift simply adds new server processes to fit the current run-time configuration. As a result, the run-time configuration changes are applied gradually as existing processes shut down and new processes are launched in Amazon GameLift's normal process recycling activity.
    Fleet-related operations include:
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
            Unique identifier for a fleet to update run-time configuration for.
            

    :type RuntimeConfiguration: dict
    :param RuntimeConfiguration: [REQUIRED]
            Instructions for launching server processes on each instance in the fleet. The run-time configuration for a fleet has a collection of server process configurations, one for each type of server process to run on an instance. A server process configuration specifies the location of the server executable, launch parameters, and the number of concurrent processes with that configuration to maintain on each instance.
            ServerProcesses (list) --Collection of server process configurations that describe which server processes to run on each instance in a fleet.
            (dict) --A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet's `` RuntimeConfiguration `` .
            LaunchPath (string) -- [REQUIRED]Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances C:\game , and for Linux instances /local/game . A Windows game build with an executable file located at MyGame\latest\server.exe must have a launch path of 'C:\game\MyGame\latest\server.exe '. A Linux game build with an executable file located at MyGame/latest/server.exe must have a launch path of '/local/game/MyGame/latest/server.exe '.
            Parameters (string) --Optional list of parameters to pass to the server executable on launch.
            ConcurrentExecutions (integer) -- [REQUIRED]Number of server processes using this configuration to run concurrently on an instance.
            
            MaxConcurrentGameSessionActivations (integer) --Maximum number of game sessions with status ACTIVATING to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.
            GameSessionActivationTimeoutSeconds (integer) --Maximum amount of time (in seconds) that a game session can remain in status ACTIVATING . If the game session is not active before the timeout, activation is terminated and the game session status is changed to TERMINATED .
            

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
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    Unique identifier for a fleet to update run-time configuration for.
    
    RuntimeConfiguration (dict) -- [REQUIRED]
    Instructions for launching server processes on each instance in the fleet. The run-time configuration for a fleet has a collection of server process configurations, one for each type of server process to run on an instance. A server process configuration specifies the location of the server executable, launch parameters, and the number of concurrent processes with that configuration to maintain on each instance.
    
    ServerProcesses (list) --Collection of server process configurations that describe which server processes to run on each instance in a fleet.
    
    (dict) --A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet's ``  RuntimeConfiguration `` .
    
    LaunchPath (string) -- [REQUIRED]Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances C:\game , and for Linux instances /local/game . A Windows game build with an executable file located at MyGame\latest\server.exe must have a launch path of "C:\game\MyGame\latest\server.exe ". A Linux game build with an executable file located at MyGame/latest/server.exe must have a launch path of "/local/game/MyGame/latest/server.exe ".
    
    Parameters (string) --Optional list of parameters to pass to the server executable on launch.
    
    ConcurrentExecutions (integer) -- [REQUIRED]Number of server processes using this configuration to run concurrently on an instance.
    
    
    
    
    
    MaxConcurrentGameSessionActivations (integer) --Maximum number of game sessions with status ACTIVATING to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.
    
    GameSessionActivationTimeoutSeconds (integer) --Maximum amount of time (in seconds) that a game session can remain in status ACTIVATING . If the game session is not active before the timeout, activation is terminated and the game session status is changed to TERMINATED .
    
    
    
    
    """
    pass

def validate_matchmaking_rule_set(RuleSetBody=None):
    """
    Validates the syntax of a matchmaking rule or rule set. This operation checks that the rule set uses syntactically correct JSON and that it conforms to allowed property expressions. To validate syntax, provide a rule set string.
    Operations related to match configurations and rule sets include:
    See also: AWS API Documentation
    
    
    :example: response = client.validate_matchmaking_rule_set(
        RuleSetBody='string'
    )
    
    
    :type RuleSetBody: string
    :param RuleSetBody: [REQUIRED]
            Collection of matchmaking rules to validate, formatted as a JSON string.
            

    :rtype: dict
    :return: {
        'Valid': True|False
    }
    
    
    """
    pass

