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


def create_alias(Name=None, Description=None, RoutingStrategy=None):
    """
    :param Name: [REQUIRED]
            Descriptive label associated with an alias. Alias names do not need to be unique.
            
    :type Name: string
    :param Description: Human-readable description of an alias.
    :type Description: string
    :param RoutingStrategy: [REQUIRED]
            Object specifying the fleet and routing type to use for the alias.
            Type (string) --Type of routing strategy.
            Possible routing types include the following:
            SIMPLE   The alias resolves to one specific fleet. Use this type when routing to active fleets.
            TERMINAL   The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
            FleetId (string) --Unique identifier for a fleet.
            Message (string) --Message text to be used with a terminal routing strategy.
            
    :type RoutingStrategy: dict
    """
    pass


def create_build(Name=None, Version=None, StorageLocation=None, OperatingSystem=None):
    """
    :param Name: Descriptive label associated with a build. Build names do not need to be unique. A build name can be changed later using `` UpdateBuild `` .
    :type Name: string
    :param Version: Version associated with this build. Version strings do not need to be unique to a build. A build version can be changed later using `` UpdateBuild `` .
    :type Version: string
    :param StorageLocation: Location in Amazon Simple Storage Service (Amazon S3) where a build's files are stored. This location is assigned in response to a CreateBuild call, and is always in the same region as the service used to create the build. For more details see the Amazon S3 documentation .
            Bucket (string) --Amazon S3 bucket identifier.
            Key (string) --Amazon S3 bucket key.
            RoleArn (string) --Amazon resource number for the cross-account access role that allows GameLift access to the S3 bucket.
            
    :type StorageLocation: dict
    :param OperatingSystem: Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.
    :type OperatingSystem: string
    """
    pass


def create_fleet(Name=None, Description=None, BuildId=None, ServerLaunchPath=None, ServerLaunchParameters=None,
                 LogPaths=None, EC2InstanceType=None, EC2InboundPermissions=None, NewGameSessionProtectionPolicy=None,
                 RuntimeConfiguration=None, ResourceCreationLimitPolicy=None):
    """
    :param Name: [REQUIRED]
            Descriptive label associated with a fleet. Fleet names do not need to be unique.
            
    :type Name: string
    :param Description: Human-readable description of a fleet.
    :type Description: string
    :param BuildId: [REQUIRED]
            Unique identifier of the build to be deployed on the new fleet. The build must have been successfully uploaded to GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
            
    :type BuildId: string
    :param ServerLaunchPath: This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. (Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.)
    :type ServerLaunchPath: string
    :param ServerLaunchParameters: This parameter is no longer used. Instead, specify server launch parameters in the RuntimeConfiguration parameter. (Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.)
    :type ServerLaunchParameters: string
    :param LogPaths: Location of default log files. When a server process is shut down, Amazon GameLift captures and stores any log files in this location. These logs are in addition to game session logs; see more on game session logs in the Amazon GameLift Developer Guide . If no default log path for a fleet is specified, GameLift will automatically upload logs stored on each instance at C:\game\logs . Use the GameLift console to access stored logs.
            (string) --
            
    :type LogPaths: list
    :param EC2InstanceType: [REQUIRED]
            Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.
            
    :type EC2InstanceType: string
    :param EC2InboundPermissions: Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. If no inbound permissions are set, including both IP address range and port range, the server processes in the fleet cannot accept connections. You can specify one or more sets of permissions for a fleet.
            (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet's allowed ranges. This combination is included in the GameSession object.
            FromPort (integer) -- [REQUIRED]Starting value for a range of allowed port numbers.
            ToPort (integer) -- [REQUIRED]Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
            IpRange (string) -- [REQUIRED]Range of allowed IP addresses. This value must be expressed in CIDR notation . Example: '000.000.000.000/[subnet mask] ' or optionally the shortened version '0.0.0.0/[subnet mask] '.
            Protocol (string) -- [REQUIRED]Network communication protocol used by the fleet.
            
            
    :type EC2InboundPermissions: list
    :param NewGameSessionProtectionPolicy: Game session protection policy to apply to all instances in this fleet. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy using UpdateFleetAttributes, but this change will only affect sessions created after the policy change. You can also set protection for individual instances using UpdateGameSession .
            NoProtection   The game session can be terminated during a scale-down event.
            FullProtection   If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
            
    :type NewGameSessionProtectionPolicy: string
    :param RuntimeConfiguration: Instructions for launching server processes on each instance in the fleet. The runtime configuration for a fleet has a collection of server process configurations, one for each type of server process to run on an instance. A server process configuration specifies the location of the server executable, launch parameters, and the number of concurrent processes with that configuration to maintain on each instance. A CreateFleet request must include a runtime configuration with at least one server process configuration; otherwise the request will fail with an invalid request exception. (This parameter replaces the parameters ServerLaunchPath and ServerLaunchParameters ; requests that contain values for these parameters instead of a runtime configuration will continue to work.)
            ServerProcesses (list) --Collection of server process configurations describing what server processes to run on each instance in a fleet
            (dict) --A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet's `` RuntimeConfiguration `` .
            LaunchPath (string) -- [REQUIRED]Location in the game build of the server executable. All game builds are installed on instances at the root C:\game\... , so an executable file located at MyGame\latest\server.exe has a launch path of 'C:\game\MyGame\latest\server.exe '.
            Parameters (string) --Optional list of parameters to pass to the server executable on launch.
            ConcurrentExecutions (integer) -- [REQUIRED]Number of server processes using this configuration to run concurrently on an instance.
            
            
    :type RuntimeConfiguration: dict
    :param ResourceCreationLimitPolicy: Policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
            NewGameSessionsPerCreator (integer) --Maximum number of game sessions an individual can create during the policy period.
            PolicyPeriodInMinutes (integer) --Time span used to evaluate the resource creation limit policy.
            
    :type ResourceCreationLimitPolicy: dict
    """
    pass


def create_game_session(FleetId=None, AliasId=None, MaximumPlayerSessionCount=None, Name=None, GameProperties=None,
                        CreatorId=None, GameSessionId=None):
    """
    :param FleetId: Unique identifier for a fleet. Each request must reference either a fleet ID or alias ID, but not both.
    :type FleetId: string
    :param AliasId: Unique identifier for a fleet alias. Each request must reference either a fleet ID or alias ID, but not both.
    :type AliasId: string
    :param MaximumPlayerSessionCount: [REQUIRED]
            Maximum number of players that can be connected simultaneously to the game session.
            
    :type MaximumPlayerSessionCount: integer
    :param Name: Descriptive label associated with a game session. Session names do not need to be unique.
    :type Name: string
    :param GameProperties: Set of properties used to administer a game session. These properties are passed to the server process hosting it.
            (dict) --Set of key-value pairs containing information a server process requires to set up a game session. This object allows you to pass in any set of data needed for your game. For more information, see the Amazon GameLift Developer Guide .
            Key (string) -- [REQUIRED]TBD
            Value (string) -- [REQUIRED]TBD
            
            
    :type GameProperties: list
    :param CreatorId: Player ID identifying the person or entity creating the game session. This ID is used to enforce a resource protection policy (if one exists) that limits the number of concurrent active game sessions one player can have.
    :type CreatorId: string
    :param GameSessionId: Custom string to include in the game session ID, with a maximum length of 48 characters. If this parameter is set, GameLift creates a game session ID in the following format: 'arn:aws:gamelift:region::gamesession/fleet-fleet ID/custom ID string'. For example, this full game session ID: 'arn:aws:gamelift:us-west-2::gamesession/fleet-2ec2aae5-c2c7-43ca-b19d-8249fe5fddf2/my-game-session' includes the custom ID string 'my-game-session'. If this parameter is not set, GameLift creates a game session ID in the same format with an auto-generated ID string.
    :type GameSessionId: string
    """
    pass


def create_player_session(GameSessionId=None, PlayerId=None):
    """
    :param GameSessionId: [REQUIRED]
            Unique identifier for the game session to add a player to. Game session ID format is as follows: 'arn:aws:gamelift:region::gamesession/fleet-fleet ID/ID string'. The value of ID stringis either a custom ID string (if one was specified when the game session was created) an auto-generated string.
            
    :type GameSessionId: string
    :param PlayerId: [REQUIRED]
            Unique identifier for the player to be added.
            
    :type PlayerId: string
    """
    pass


def create_player_sessions(GameSessionId=None, PlayerIds=None):
    """
    :param GameSessionId: [REQUIRED]
            Unique identifier for the game session to add players to. Game session ID format is as follows: 'arn:aws:gamelift:region::gamesession/fleet-fleet ID/ID string'. The value of ID stringis either a custom ID string (if one was specified when the game session was created) an auto-generated string.
            
    :type GameSessionId: string
    :param PlayerIds: [REQUIRED]
            List of unique identifiers for the players to be added.
            (string) --
            
    :type PlayerIds: list
    """
    pass


def delete_alias(AliasId=None):
    """
    :param AliasId: [REQUIRED]
            Unique identifier for a fleet alias. Specify the alias you want to delete.
            ReturnsNone
            
    :type AliasId: string
    """
    pass


def delete_build(BuildId=None):
    """
    :param BuildId: [REQUIRED]
            Unique identifier for the build you want to delete.
            ReturnsNone
            
    :type BuildId: string
    """
    pass


def delete_fleet(FleetId=None):
    """
    :param FleetId: [REQUIRED]
            Unique identifier for the fleet you want to delete.
            ReturnsNone
            
    :type FleetId: string
    """
    pass


def delete_scaling_policy(Name=None, FleetId=None):
    """
    :param Name: [REQUIRED]
            Descriptive label associated with a scaling policy. Policy names do not need to be unique.
            
    :type Name: string
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet.
            
    :type FleetId: string
    """
    pass


def describe_alias(AliasId=None):
    """
    :param AliasId: [REQUIRED]
            Unique identifier for a fleet alias. Specify the alias you want to retrieve.
            Return typedict
            ReturnsResponse Syntax{
              'Alias': {
                'AliasId': 'string',
                'Name': 'string',
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
            Response Structure
            (dict) --Represents the returned data in response to a request action.
            Alias (dict) --Object containing the requested alias.
            AliasId (string) --Unique identifier for a fleet alias.
            Name (string) --Descriptive label associated with an alias. Alias names do not need to be unique.
            Description (string) --Human-readable description of an alias.
            RoutingStrategy (dict) --Routing configuration for a fleet alias.
            Type (string) --Type of routing strategy.
            Possible routing types include the following:
            SIMPLE   The alias resolves to one specific fleet. Use this type when routing to active fleets.
            TERMINAL   The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
            FleetId (string) --Unique identifier for a fleet.
            Message (string) --Message text to be used with a terminal routing strategy.
            CreationTime (datetime) --Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (ex: '1469498468.057'.
            LastUpdatedTime (datetime) --Time stamp indicating when this data object was last modified. Format is a number expressed in Unix time as milliseconds (ex: '1469498468.057'.
            
            
            
    :type AliasId: string
    """
    pass


def describe_build(BuildId=None):
    """
    :param BuildId: [REQUIRED]
            Unique identifier of the build that you want to retrieve properties for.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the returned data in response to a request action.
            Build (dict) --Set of properties describing the requested build.
            BuildId (string) --Unique identifier for a build.
            Name (string) --Descriptive label associated with a build. Build names do not need to be unique. It can be set using CreateBuild or UpdateBuild .
            Version (string) --Version associated with this build. Version strings do not need to be unique to a build. This value can be set using CreateBuild or UpdateBuild .
            Status (string) --Current status of the build.
            Possible build statuses include the following:
            INITIALIZED   A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
            READY   The game build has been successfully uploaded. You can now create new fleets for this build.
            FAILED   The game build upload failed. You cannot create new fleets for this build.
            SizeOnDisk (integer) --File size of the uploaded game build, expressed in bytes. When the build status is INITIALIZED , this value is 0.
            OperatingSystem (string) --Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.
            CreationTime (datetime) --Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (ex: '1469498468.057'.
            
            
            
    :type BuildId: string
    """
    pass


def describe_ec2_instance_limits(EC2InstanceType=None):
    """
    :param EC2InstanceType: Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions. Leave this parameter blank to retrieve limits for all types.
            Return typedict
            ReturnsResponse Syntax{
              'EC2InstanceLimits': [
                {
                  'EC2InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge',
                  'CurrentInstances': 123,
                  'InstanceLimit': 123
                },
              ]
            }
            Response Structure
            (dict) --Represents the returned data in response to a request action.
            EC2InstanceLimits (list) --Object containing the maximum number of instances for the specified instance type.
            (dict) --Maximum number of instances allowed based on the Amazon Elastic Compute Cloud (Amazon EC2) instance type. Instance limits can be retrieved by calling DescribeEC2InstanceLimits .
            EC2InstanceType (string) --Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.
            CurrentInstances (integer) --Number of instances of the specified type that are currently in use by this AWS account.
            InstanceLimit (integer) --Number of instances allowed.
            
            
            
    :type EC2InstanceType: string
    """
    pass


def describe_fleet_attributes(FleetIds=None, Limit=None, NextToken=None):
    """
    :param FleetIds: Unique identifiers for the fleet(s) that you want to retrieve attributes for. To request attributes for all fleets, leave this parameter empty.
            (string) --
            
    :type FleetIds: list
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
    :type NextToken: string
    """
    pass


def describe_fleet_capacity(FleetIds=None, Limit=None, NextToken=None):
    """
    :param FleetIds: Unique identifier for the fleet(s) you want to retrieve capacity information for. To request capacity information for all fleets, leave this parameter empty.
            (string) --
            
    :type FleetIds: list
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
    :type NextToken: string
    """
    pass


def describe_fleet_events(FleetId=None, StartTime=None, EndTime=None, Limit=None, NextToken=None):
    """
    :param FleetId: [REQUIRED]
            Unique identifier for the fleet to get event logs for.
            
    :type FleetId: string
    :param StartTime: Earliest date to retrieve event logs for. If no start time is specified, this call returns entries starting from when the fleet was created to the specified end time. Format is a number expressed in Unix time as milliseconds (ex: '1469498468.057'.
    :type StartTime: datetime
    :param EndTime: Most recent date to retrieve event logs for. If no end time is specified, this call returns entries from the specified start time up to the present. Format is a number expressed in Unix time as milliseconds (ex: '1469498468.057'.
    :type EndTime: datetime
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.
    :type NextToken: string
    """
    pass


def describe_fleet_port_settings(FleetId=None):
    """
    :param FleetId: [REQUIRED]
            Unique identifier for the fleet you want to retrieve port settings for.
            Return typedict
            ReturnsResponse Syntax{
              'InboundPermissions': [
                {
                  'FromPort': 123,
                  'ToPort': 123,
                  'IpRange': 'string',
                  'Protocol': 'TCP'|'UDP'
                },
              ]
            }
            Response Structure
            (dict) --Represents the returned data in response to a request action.
            InboundPermissions (list) --Object containing port settings for the requested fleet ID.
            (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet's allowed ranges. This combination is included in the GameSession object.
            FromPort (integer) --Starting value for a range of allowed port numbers.
            ToPort (integer) --Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
            IpRange (string) --Range of allowed IP addresses. This value must be expressed in CIDR notation . Example: '000.000.000.000/[subnet mask] ' or optionally the shortened version '0.0.0.0/[subnet mask] '.
            Protocol (string) --Network communication protocol used by the fleet.
            
            
            
    :type FleetId: string
    """
    pass


def describe_fleet_utilization(FleetIds=None, Limit=None, NextToken=None):
    """
    :param FleetIds: Unique identifier for the fleet(s) you want to retrieve utilization data for. To request utilization data for all fleets, leave this parameter empty.
            (string) --
            
    :type FleetIds: list
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
    :type NextToken: string
    """
    pass


def describe_game_session_details(FleetId=None, GameSessionId=None, AliasId=None, StatusFilter=None, Limit=None,
                                  NextToken=None):
    """
    :param FleetId: Unique identifier for a fleet. Specify a fleet to retrieve information on all game sessions active on the fleet.
    :type FleetId: string
    :param GameSessionId: Unique identifier for the game session to retrieve information on. Game session ID format is as follows: 'arn:aws:gamelift:region::gamesession/fleet-fleet ID/ID string'. The value of ID stringis either a custom ID string (if one was specified when the game session was created) an auto-generated string.
    :type GameSessionId: string
    :param AliasId: Unique identifier for a fleet alias. Specify an alias to retrieve information on all game sessions active on the fleet.
    :type AliasId: string
    :param StatusFilter: Game session status to filter results on. Possible game session statuses include ACTIVE, TERMINATED , ACTIVATING and TERMINATING (the last two are transitory).
    :type StatusFilter: string
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.
    :type NextToken: string
    """
    pass


def describe_game_sessions(FleetId=None, GameSessionId=None, AliasId=None, StatusFilter=None, Limit=None,
                           NextToken=None):
    """
    :param FleetId: Unique identifier for a fleet. Specify a fleet to retrieve information on all game sessions active on the fleet.
    :type FleetId: string
    :param GameSessionId: Unique identifier for the game session to retrieve information on. Game session ID format is as follows: 'arn:aws:gamelift:region::gamesession/fleet-fleet ID/ID string'. The value of ID stringis either a custom ID string (if one was specified when the game session was created) an auto-generated string.
    :type GameSessionId: string
    :param AliasId: Unique identifier for a fleet alias. Specify an alias to retrieve information on all game sessions active on the fleet.
    :type AliasId: string
    :param StatusFilter: Game session status to filter results on. Possible game session statuses include ACTIVE , TERMINATED , ACTIVATING , and TERMINATING (the last two are transitory).
    :type StatusFilter: string
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.
    :type NextToken: string
    """
    pass


def describe_instances(FleetId=None, InstanceId=None, Limit=None, NextToken=None):
    """
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet. Specify the fleet to retrieve instance information for.
            
    :type FleetId: string
    :param InstanceId: Unique identifier for an instance. Specify an instance to retrieve information for or leave blank to get information on all instances in the fleet.
    :type InstanceId: string
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.
    :type NextToken: string
    """
    pass


def describe_player_sessions(GameSessionId=None, PlayerId=None, PlayerSessionId=None, PlayerSessionStatusFilter=None,
                             Limit=None, NextToken=None):
    """
    :param GameSessionId: Unique identifier for the game session to get player sessions for.Game session ID format is as follows: 'arn:aws:gamelift:region::gamesession/fleet-fleet ID/ID string'. The value of ID stringis either a custom ID string (if one was specified when the game session was created) an auto-generated string.
    :type GameSessionId: string
    :param PlayerId: Unique identifier for a player.
    :type PlayerId: string
    :param PlayerSessionId: Unique identifier for a player session.
    :type PlayerSessionId: string
    :param PlayerSessionStatusFilter: Player session status to filter results on.
            Possible player session statuses include the following:
            RESERVED   The player session request has been received, but the player has not yet connected to the server process and/or been validated.
            ACTIVE   The player has been validated by the server process and is currently connected.
            COMPLETED   The player connection has been dropped.
            TIMEDOUT   A player session request was received, but the player did not connect and/or was not validated within the time-out limit (60 seconds).
            
    :type PlayerSessionStatusFilter: string
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. If a player session ID is specified, this parameter is ignored.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored.
    :type NextToken: string
    """
    pass


def describe_runtime_configuration(FleetId=None):
    """
    :param FleetId: [REQUIRED]
            Unique identifier of the fleet to get the runtime configuration for.
            Return typedict
            ReturnsResponse Syntax{
              'RuntimeConfiguration': {
                'ServerProcesses': [
                  {
                    'LaunchPath': 'string',
                    'Parameters': 'string',
                    'ConcurrentExecutions': 123
                  },
                ]
              }
            }
            Response Structure
            (dict) --Represents the returned data in response to a request action.
            RuntimeConfiguration (dict) --Instructions describing how server processes should be launched and maintained on each instance in the fleet.
            ServerProcesses (list) --Collection of server process configurations describing what server processes to run on each instance in a fleet
            (dict) --A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet's `` RuntimeConfiguration `` .
            LaunchPath (string) --Location in the game build of the server executable. All game builds are installed on instances at the root C:\game\... , so an executable file located at MyGame\latest\server.exe has a launch path of 'C:\game\MyGame\latest\server.exe '.
            Parameters (string) --Optional list of parameters to pass to the server executable on launch.
            ConcurrentExecutions (integer) --Number of server processes using this configuration to run concurrently on an instance.
            
            
            
            
    :type FleetId: string
    """
    pass


def describe_scaling_policies(FleetId=None, StatusFilter=None, Limit=None, NextToken=None):
    """
    :param FleetId: [REQUIRED]
            Unique identifier for a fleet. Specify the fleet to retrieve scaling policies for.
            
    :type FleetId: string
    :param StatusFilter: Scaling policy status to filter results on. A scaling policy is only in force when in an ACTIVE status.
            ACTIVE   The scaling policy is currently in force.
            UPDATEREQUESTED   A request to update the scaling policy has been received.
            UPDATING   A change is being made to the scaling policy.
            DELETEREQUESTED   A request to delete the scaling policy has been received.
            DELETING   The scaling policy is being deleted.
            DELETED   The scaling policy has been deleted.
            ERROR   An error occurred in creating the policy. It should be removed and recreated.
            
    :type StatusFilter: string
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.
    :type NextToken: string
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


def get_game_session_log_url(GameSessionId=None):
    """
    :param GameSessionId: [REQUIRED]
            Unique identifier for the game session to get logs for. Game session ID format is as follows: 'arn:aws:gamelift:region::gamesession/fleet-fleet ID/ID string'. The value of ID stringis either a custom ID string (if one was specified when the game session was created) an auto-generated string.
            Return typedict
            ReturnsResponse Syntax{
              'PreSignedUrl': 'string'
            }
            Response Structure
            (dict) --Represents the returned data in response to a request action.
            PreSignedUrl (string) --Location of the requested game session logs, available for download.
            
            
    :type GameSessionId: string
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


def get_waiter():
    """
    """
    pass


def list_aliases(RoutingStrategyType=None, Name=None, Limit=None, NextToken=None):
    """
    :param RoutingStrategyType: Type of routing to filter results on. Use this parameter to retrieve only aliases of a certain type. To retrieve all aliases, leave this parameter empty.
            Possible routing types include the following:
            SIMPLE   The alias resolves to one specific fleet. Use this type when routing to active fleets.
            TERMINAL   The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
            
    :type RoutingStrategyType: string
    :param Name: Descriptive label associated with an alias. Alias names do not need to be unique.
    :type Name: string
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.
    :type NextToken: string
    """
    pass


def list_builds(Status=None, Limit=None, NextToken=None):
    """
    :param Status: Build status to filter results by. To retrieve all builds, leave this parameter empty.
            Possible build statuses include the following:
            INITIALIZED   A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
            READY   The game build has been successfully uploaded. You can now create new fleets for this build.
            FAILED   The game build upload failed. You cannot create new fleets for this build.
            
    :type Status: string
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.
    :type NextToken: string
    """
    pass


def list_fleets(BuildId=None, Limit=None, NextToken=None):
    """
    :param BuildId: Unique identifier of the build to return fleets for. Use this parameter to return only fleets using the specified build. To retrieve all fleets, leave this parameter empty.
    :type BuildId: string
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.
    :type NextToken: string
    """
    pass


def put_scaling_policy(Name=None, FleetId=None, ScalingAdjustment=None, ScalingAdjustmentType=None, Threshold=None,
                       ComparisonOperator=None, EvaluationPeriods=None, MetricName=None):
    """
    :param Name: [REQUIRED]
            Descriptive label associated with a scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.
            
    :type Name: string
    :param FleetId: [REQUIRED]
            Unique identity for the fleet to scale with this policy.
            
    :type FleetId: string
    :param ScalingAdjustment: [REQUIRED]
            Amount of adjustment to make, based on the scaling adjustment type.
            
    :type ScalingAdjustment: integer
    :param ScalingAdjustmentType: [REQUIRED]
            Type of adjustment to make to a fleet's instance count (see FleetCapacity ):
            ChangeInCapacity   add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
            ExactCapacity   set the instance count to the scaling adjustment value.
            PercentChangeInCapacity   increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of '-10' scales the fleet down by 10%.
            
    :type ScalingAdjustmentType: string
    :param Threshold: [REQUIRED]
            Metric value used to trigger a scaling event.
            
    :type Threshold: float
    :param ComparisonOperator: [REQUIRED]
            Comparison operator to use when measuring the metric against the threshold value.
            
    :type ComparisonOperator: string
    :param EvaluationPeriods: [REQUIRED]
            Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
            
    :type EvaluationPeriods: integer
    :param MetricName: [REQUIRED]
            Name of the Amazon GameLift-defined metric that is used to trigger an adjustment.
            ActivatingGameSessions   number of game sessions in the process of being created (game session status = ACTIVATING ).
            ActiveGameSessions   number of game sessions currently running (game session status = ACTIVE ).
            CurrentPlayerSessions   number of active or reserved player sessions (player session status = ACTIVE or RESERVED ).
            AvailablePlayerSessions   number of player session slots currently available in active game sessions across the fleet, calculated by subtracting a game session's current player session count from its maximum player session count. This number includes game sessions that are not currently accepting players (game session PlayerSessionCreationPolicy = DENY_ALL ).
            ActiveInstances   number of instances currently running a game session.
            IdleInstances   number of instances not currently running a game session.
            
    :type MetricName: string
    """
    pass


def request_upload_credentials(BuildId=None):
    """
    :param BuildId: [REQUIRED]
            Unique identifier for the build you want to get credentials for.
            Return typedict
            ReturnsResponse Syntax{
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
            Response Structure
            (dict) --Represents the returned data in response to a request action.
            UploadCredentials (dict) --AWS credentials required when uploading a game build to the storage location. These credentials have a limited lifespan and are valid only for the build they were issued for.
            AccessKeyId (string) --Access key for an AWS account.
            SecretAccessKey (string) --Secret key for an AWS account.
            SessionToken (string) --Token specific to a build ID.
            StorageLocation (dict) --Amazon S3 path and key, identifying where the game build files are stored.
            Bucket (string) --Amazon S3 bucket identifier.
            Key (string) --Amazon S3 bucket key.
            RoleArn (string) --Amazon resource number for the cross-account access role that allows GameLift access to the S3 bucket.
            
            
            
    :type BuildId: string
    """
    pass


def resolve_alias(AliasId=None):
    """
    :param AliasId: [REQUIRED]
            Unique identifier for the alias you want to resolve.
            Return typedict
            ReturnsResponse Syntax{
              'FleetId': 'string'
            }
            Response Structure
            (dict) --Represents the returned data in response to a request action.
            FleetId (string) --Fleet ID associated with the requested alias.
            
            
    :type AliasId: string
    """
    pass


def search_game_sessions(FleetId=None, AliasId=None, FilterExpression=None, SortExpression=None, Limit=None,
                         NextToken=None):
    """
    :param FleetId: Unique identifier for a fleet. Each request must reference either a fleet ID or alias ID, but not both.
    :type FleetId: string
    :param AliasId: Unique identifier for a fleet alias. Each request must reference either a fleet ID or alias ID, but not both.
    :type AliasId: string
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
            
    :type FilterExpression: string
    :param SortExpression: Instructions on how to sort the search results. If no sort expression is included, the request returns results in random order. A sort expression consists of the following elements:
            Operand -- Name of a game session attribute. Valid values are gameSessionName , gameSessionId , creationTimeMillis , playerSessionCount , maximumSessions , hasAvailablePlayerSessions .
            Order -- Valid sort orders are ASC (ascending) and DESC (descending).
            For example, this sort expression returns the oldest active sessions first: 'SortExpression': 'creationTimeMillis ASC' . Results with a null value for the sort operand are returned at the end of the list.
            
    :type SortExpression: string
    :param Limit: Maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. The maximum number of results returned is 20, even if this value is not set or is set higher than 20.
    :type Limit: integer
    :param NextToken: Token indicating the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To specify the start of the result set, do not specify a value.
    :type NextToken: string
    """
    pass


def update_alias(AliasId=None, Name=None, Description=None, RoutingStrategy=None):
    """
    :param AliasId: [REQUIRED]
            Unique identifier for a fleet alias. Specify the alias you want to update.
            
    :type AliasId: string
    :param Name: Descriptive label associated with an alias. Alias names do not need to be unique.
    :type Name: string
    :param Description: Human-readable description of an alias.
    :type Description: string
    :param RoutingStrategy: Object specifying the fleet and routing type to use for the alias.
            Type (string) --Type of routing strategy.
            Possible routing types include the following:
            SIMPLE   The alias resolves to one specific fleet. Use this type when routing to active fleets.
            TERMINAL   The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.
            FleetId (string) --Unique identifier for a fleet.
            Message (string) --Message text to be used with a terminal routing strategy.
            
    :type RoutingStrategy: dict
    """
    pass


def update_build(BuildId=None, Name=None, Version=None):
    """
    :param BuildId: [REQUIRED]
            Unique identifier of the build you want to update.
            
    :type BuildId: string
    :param Name: Descriptive label associated with a build. Build names do not need to be unique.
    :type Name: string
    :param Version: Version associated with this build. Version strings do not need to be unique to a build.
    :type Version: string
    """
    pass


def update_fleet_attributes(FleetId=None, Name=None, Description=None, NewGameSessionProtectionPolicy=None,
                            ResourceCreationLimitPolicy=None):
    """
    :param FleetId: [REQUIRED]
            Unique identifier for the fleet you want to update attribute metadata for.
            
    :type FleetId: string
    :param Name: Descriptive label associated with a fleet. Fleet names do not need to be unique.
    :type Name: string
    :param Description: Human-readable description of a fleet.
    :type Description: string
    :param NewGameSessionProtectionPolicy: Game session protection policy to apply to all new instances created in this fleet. Instances that already exist are not affected. You can set protection for individual instances using UpdateGameSession .
            NoProtection   The game session can be terminated during a scale-down event.
            FullProtection   If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
            
    :type NewGameSessionProtectionPolicy: string
    :param ResourceCreationLimitPolicy: Policy that limits the number of game sessions an individual player can create over a span of time.
            NewGameSessionsPerCreator (integer) --Maximum number of game sessions an individual can create during the policy period.
            PolicyPeriodInMinutes (integer) --Time span used to evaluate the resource creation limit policy.
            
    :type ResourceCreationLimitPolicy: dict
    """
    pass


def update_fleet_capacity(FleetId=None, DesiredInstances=None, MinSize=None, MaxSize=None):
    """
    :param FleetId: [REQUIRED]
            Unique identifier for the fleet you want to update capacity for.
            
    :type FleetId: string
    :param DesiredInstances: Number of EC2 instances you want this fleet to host.
    :type DesiredInstances: integer
    :param MinSize: Minimum value allowed for the fleet's instance count. Default if not set is 0.
    :type MinSize: integer
    :param MaxSize: Maximum value allowed for the fleet's instance count. Default if not set is 1.
    :type MaxSize: integer
    """
    pass


def update_fleet_port_settings(FleetId=None, InboundPermissionAuthorizations=None, InboundPermissionRevocations=None):
    """
    :param FleetId: [REQUIRED]
            Unique identifier for the fleet you want to update port settings for.
            
    :type FleetId: string
    :param InboundPermissionAuthorizations: Collection of port settings to be added to the fleet record.
            (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet's allowed ranges. This combination is included in the GameSession object.
            FromPort (integer) -- [REQUIRED]Starting value for a range of allowed port numbers.
            ToPort (integer) -- [REQUIRED]Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
            IpRange (string) -- [REQUIRED]Range of allowed IP addresses. This value must be expressed in CIDR notation . Example: '000.000.000.000/[subnet mask] ' or optionally the shortened version '0.0.0.0/[subnet mask] '.
            Protocol (string) -- [REQUIRED]Network communication protocol used by the fleet.
            
            
    :type InboundPermissionAuthorizations: list
    :param InboundPermissionRevocations: Collection of port settings to be removed from the fleet record.
            (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on GameLift. Each game session hosted on a fleet is assigned a unique combination of IP address and port number, which must fall into the fleet's allowed ranges. This combination is included in the GameSession object.
            FromPort (integer) -- [REQUIRED]Starting value for a range of allowed port numbers.
            ToPort (integer) -- [REQUIRED]Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
            IpRange (string) -- [REQUIRED]Range of allowed IP addresses. This value must be expressed in CIDR notation . Example: '000.000.000.000/[subnet mask] ' or optionally the shortened version '0.0.0.0/[subnet mask] '.
            Protocol (string) -- [REQUIRED]Network communication protocol used by the fleet.
            
            
    :type InboundPermissionRevocations: list
    """
    pass


def update_game_session(GameSessionId=None, MaximumPlayerSessionCount=None, Name=None, PlayerSessionCreationPolicy=None,
                        ProtectionPolicy=None):
    """
    :param GameSessionId: [REQUIRED]
            Unique identifier for the game session to update. Game session ID format is as follows: 'arn:aws:gamelift:region::gamesession/fleet-fleet ID/ID string'. The value of ID stringis either a custom ID string (if one was specified when the game session was created) an auto-generated string.
            
    :type GameSessionId: string
    :param MaximumPlayerSessionCount: Maximum number of players that can be simultaneously connected to the game session.
    :type MaximumPlayerSessionCount: integer
    :param Name: Descriptive label associated with a game session. Session names do not need to be unique.
    :type Name: string
    :param PlayerSessionCreationPolicy: Policy determining whether or not the game session accepts new players.
    :type PlayerSessionCreationPolicy: string
    :param ProtectionPolicy: Game session protection policy to apply to this game session only.
            NoProtection   The game session can be terminated during a scale-down event.
            FullProtection   If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
            
    :type ProtectionPolicy: string
    """
    pass


def update_runtime_configuration(FleetId=None, RuntimeConfiguration=None):
    """
    :param FleetId: [REQUIRED]
            Unique identifier of the fleet to update runtime configuration for.
            
    :type FleetId: string
    :param RuntimeConfiguration: [REQUIRED]
            Instructions for launching server processes on each instance in the fleet. The runtime configuration for a fleet has a collection of server process configurations, one for each type of server process to run on an instance. A server process configuration specifies the location of the server executable, launch parameters, and the number of concurrent processes with that configuration to maintain on each instance.
            ServerProcesses (list) --Collection of server process configurations describing what server processes to run on each instance in a fleet
            (dict) --A set of instructions for launching server processes on each instance in a fleet. Each instruction set identifies the location of the server executable, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet's `` RuntimeConfiguration `` .
            LaunchPath (string) -- [REQUIRED]Location in the game build of the server executable. All game builds are installed on instances at the root C:\game\... , so an executable file located at MyGame\latest\server.exe has a launch path of 'C:\game\MyGame\latest\server.exe '.
            Parameters (string) --Optional list of parameters to pass to the server executable on launch.
            ConcurrentExecutions (integer) -- [REQUIRED]Number of server processes using this configuration to run concurrently on an instance.
            
            
    :type RuntimeConfiguration: dict
    """
    pass
