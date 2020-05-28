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
    Registers a player\'s acceptance or rejection of a proposed FlexMatch match. A matchmaking configuration may require player acceptance; if so, then matches built with that configuration cannot be completed unless all players accept the proposed match within a specified time limit.
    When FlexMatch builds a match, all the matchmaking tickets involved in the proposed match are placed into status REQUIRES_ACCEPTANCE . This is a trigger for your game to get acceptance from all players in the ticket. Acceptances are only valid for tickets when they are in this status; all other acceptances result in an error.
    To register acceptance, specify the ticket ID, a response, and one or more players. Once all players have registered acceptance, the matchmaking tickets advance to status PLACING , where a new game session is created for the match.
    If any player rejects the match, or if acceptances are not received before a specified timeout, the proposed match is dropped. The matchmaking tickets are then handled in one of two ways: For tickets where one or more players rejected the match, the ticket status is returned to SEARCHING to find a new match. For tickets where one or more players failed to respond, the ticket status is set to CANCELLED , and processing is terminated. A new matchmaking request for these players can be submitted as needed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_match(
        TicketId='string',
        PlayerIds=[
            'string',
        ],
        AcceptanceType='ACCEPT'|'REJECT'
    )
    
    
    :type TicketId: string
    :param TicketId: [REQUIRED]\nA unique identifier for a matchmaking ticket. The ticket must be in status REQUIRES_ACCEPTANCE ; otherwise this request will fail.\n

    :type PlayerIds: list
    :param PlayerIds: [REQUIRED]\nA unique identifier for a player delivering the response. This parameter can include one or multiple player IDs.\n\n(string) --\n\n

    :type AcceptanceType: string
    :param AcceptanceType: [REQUIRED]\nPlayer response to the proposed match.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException


    :return: {}
    
    
    :returns: 
    TicketId (string) -- [REQUIRED]
    A unique identifier for a matchmaking ticket. The ticket must be in status REQUIRES_ACCEPTANCE ; otherwise this request will fail.
    
    PlayerIds (list) -- [REQUIRED]
    A unique identifier for a player delivering the response. This parameter can include one or multiple player IDs.
    
    (string) --
    
    
    AcceptanceType (string) -- [REQUIRED]
    Player response to the proposed match.
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def claim_game_server(GameServerGroupName=None, GameServerId=None, GameServerData=None):
    """
    Locates an available game server and temporarily reserves it to host gameplay and players. This action is called by a game client or client service (such as a matchmaker) to request hosting resources for a new game session. In response, GameLift FleetIQ searches for an available game server in the specified game server group, places the game server in "claimed" status for 60 seconds, and returns connection information back to the requester so that players can connect to the game server.
    There are two ways you can claim a game server. For the first option, you provide a game server group ID only, which prompts GameLift FleetIQ to search for an available game server in the specified group and claim it. With this option, GameLift FleetIQ attempts to consolidate gameplay on as few instances as possible to minimize hosting costs. For the second option, you request a specific game server by its ID. This option results in a less efficient claiming process because it does not take advantage of consolidation and may fail if the requested game server is unavailable.
    To claim a game server, identify a game server group and (optionally) a game server ID. If your game requires that game data be provided to the game server at the start of a game, such as a game map or player information, you can provide it in your claim request.
    When a game server is successfully claimed, connection information is returned. A claimed game server\'s utilization status remains AVAILABLE, while the claim status is set to CLAIMED for up to 60 seconds. This time period allows the game server to be prompted to update its status to UTILIZED (using  UpdateGameServer ). If the game server\'s status is not updated within 60 seconds, the game server reverts to unclaimed status and is available to be claimed by another request.
    If you try to claim a specific game server, this request will fail in the following cases: (1) if the game server utilization status is UTILIZED, (2) if the game server claim status is CLAIMED, or (3) if the instance that the game server is running on is flagged as draining.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.claim_game_server(
        GameServerGroupName='string',
        GameServerId='string',
        GameServerData='string'
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nAn identifier for the game server group. When claiming a specific game server, this is the game server group whether the game server is located. When requesting that GameLift FleetIQ locate an available game server, this is the game server group to search on. You can use either the GameServerGroup name or ARN value.\n

    :type GameServerId: string
    :param GameServerId: A custom string that uniquely identifies the game server to claim. If this parameter is left empty, GameLift FleetIQ searches for an available game server in the specified game server group.

    :type GameServerData: string
    :param GameServerData: A set of custom game server properties, formatted as a single string value, to be passed to the claimed game server.

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServer': {
        'GameServerGroupName': 'string',
        'GameServerGroupArn': 'string',
        'GameServerId': 'string',
        'InstanceId': 'string',
        'ConnectionInfo': 'string',
        'GameServerData': 'string',
        'CustomSortKey': 'string',
        'ClaimStatus': 'CLAIMED',
        'UtilizationStatus': 'AVAILABLE'|'UTILIZED',
        'RegistrationTime': datetime(2015, 1, 1),
        'LastClaimTime': datetime(2015, 1, 1),
        'LastHealthCheckTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

GameServer (dict) --
Object that describes the newly claimed game server resource.

GameServerGroupName (string) --
The name identifier for the game server group where the game server is located.

GameServerGroupArn (string) --
The ARN identifier for the game server group where the game server is located.

GameServerId (string) --
A custom string that uniquely identifies the game server. Game server IDs are developer-defined and are unique across all game server groups in an AWS account.

InstanceId (string) --
The unique identifier for the instance where the game server is located.

ConnectionInfo (string) --
The port and IP address that must be used to establish a client connection to the game server.

GameServerData (string) --
A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service in response to requests  ListGameServers or  ClaimGameServer . This property can be updated using  UpdateGameServer .

CustomSortKey (string) --
A game server tag that can be used to request sorted lists of game servers when calling  ListGameServers . Custom sort keys are developer-defined. This property can be updated using  UpdateGameServer .

ClaimStatus (string) --
Indicates when an available game server has been reserved but has not yet started hosting a game. Once it is claimed, game server remains in CLAIMED status for a maximum of one minute. During this time, game clients must connect to the game server and start the game, which triggers the game server to update its utilization status. After one minute, the game server claim status reverts to null.

UtilizationStatus (string) --
Indicates whether the game server is currently available for new games or is busy. Possible statuses include:

AVAILABLE - The game server is available to be claimed. A game server that has been claimed remains in this status until it reports game hosting activity.
IN_USE - The game server is currently hosting a game session with players.


RegistrationTime (datetime) --
Time stamp indicating when the game server resource was created with a  RegisterGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastClaimTime (datetime) --
Time stamp indicating the last time the game server was claimed with a  ClaimGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057"). This value is used to calculate when the game server\'s claim status.

LastHealthCheckTime (datetime) --
Time stamp indicating the last time the game server was updated with health status using an  UpdateGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057"). After game server registration, this property is only changed when a game server update specifies a health check value.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.OutOfCapacityException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'GameServer': {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'GameServerId': 'string',
            'InstanceId': 'string',
            'ConnectionInfo': 'string',
            'GameServerData': 'string',
            'CustomSortKey': 'string',
            'ClaimStatus': 'CLAIMED',
            'UtilizationStatus': 'AVAILABLE'|'UTILIZED',
            'RegistrationTime': datetime(2015, 1, 1),
            'LastClaimTime': datetime(2015, 1, 1),
            'LastHealthCheckTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    GameServerGroupName (string) -- [REQUIRED]
    An identifier for the game server group. When claiming a specific game server, this is the game server group whether the game server is located. When requesting that GameLift FleetIQ locate an available game server, this is the game server group to search on. You can use either the  GameServerGroup name or ARN value.
    
    GameServerId (string) -- A custom string that uniquely identifies the game server to claim. If this parameter is left empty, GameLift FleetIQ searches for an available game server in the specified game server group.
    GameServerData (string) -- A set of custom game server properties, formatted as a single string value, to be passed to the claimed game server.
    
    """
    pass

def create_alias(Name=None, Description=None, RoutingStrategy=None, Tags=None):
    """
    Creates an alias for a fleet. In most situations, you can use an alias ID in place of a fleet ID. An alias provides a level of abstraction for a fleet that is useful when redirecting player traffic from one fleet to another, such as when updating your game build.
    Amazon GameLift supports two types of routing strategies for aliases: simple and terminal. A simple alias points to an active fleet. A terminal alias is used to display messaging or link to a URL instead of routing players to an active fleet. For example, you might use a terminal alias when a game version is no longer supported and you want to direct players to an upgrade site.
    To create a fleet alias, specify an alias name, routing strategy, and optional description. Each simple alias can point to only one fleet, but a fleet can have multiple aliases. If successful, a new alias record is returned, including an alias ID and an ARN. You can reassign an alias to another fleet by calling UpdateAlias .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_alias(
        Name='string',
        Description='string',
        RoutingStrategy={
            'Type': 'SIMPLE'|'TERMINAL',
            'FleetId': 'string',
            'Message': 'string'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA descriptive label that is associated with an alias. Alias names do not need to be unique.\n

    :type Description: string
    :param Description: A human-readable description of the alias.

    :type RoutingStrategy: dict
    :param RoutingStrategy: [REQUIRED]\nThe routing configuration, including routing type and fleet target, for the alias.\n\nType (string) --The type of routing strategy for the alias.\nPossible routing types include the following:\n\nSIMPLE - The alias resolves to one specific fleet. Use this type when routing to active fleets.\nTERMINAL - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.\n\n\nFleetId (string) --The unique identifier for a fleet that the alias points to. This value is the fleet ID, not the fleet ARN.\n\nMessage (string) --The message text to be used with a terminal routing strategy.\n\n\n

    :type Tags: list
    :param Tags: A list of labels to assign to the new alias resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use TagResource , UntagResource , and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.\n\n(dict) --A label that can be assigned to a GameLift resource.\n\nLearn moreTagging AWS Resources in the AWS General Reference\nAWS Tagging Strategies\nRelated operations\n\n\nTagResource\nUntagResource\nListTagsForResource\n\n\nKey (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.\n\nValue (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

Alias (dict) --
The newly created alias resource.

AliasId (string) --
A unique identifier for an alias. Alias IDs are unique within a Region.

Name (string) --
A descriptive label that is associated with an alias. Alias names do not need to be unique.

AliasArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift alias resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift alias ARN, the resource ID matches the alias ID value.

Description (string) --
A human-readable description of an alias.

RoutingStrategy (dict) --
The routing configuration, including routing type and fleet target, for the alias.

Type (string) --
The type of routing strategy for the alias.
Possible routing types include the following:

SIMPLE - The alias resolves to one specific fleet. Use this type when routing to active fleets.
TERMINAL - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.


FleetId (string) --
The unique identifier for a fleet that the alias points to. This value is the fleet ID, not the fleet ARN.

Message (string) --
The message text to be used with a terminal routing strategy.



CreationTime (datetime) --
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --
The time that this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").









Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.LimitExceededException
GameLift.Client.exceptions.TaggingFailedException


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
    A descriptive label that is associated with an alias. Alias names do not need to be unique.
    
    Description (string) -- A human-readable description of the alias.
    RoutingStrategy (dict) -- [REQUIRED]
    The routing configuration, including routing type and fleet target, for the alias.
    
    Type (string) --The type of routing strategy for the alias.
    Possible routing types include the following:
    
    SIMPLE - The alias resolves to one specific fleet. Use this type when routing to active fleets.
    TERMINAL - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
    
    
    FleetId (string) --The unique identifier for a fleet that the alias points to. This value is the fleet ID, not the fleet ARN.
    
    Message (string) --The message text to be used with a terminal routing strategy.
    
    
    
    Tags (list) -- A list of labels to assign to the new alias resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use  TagResource ,  UntagResource , and  ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
    
    (dict) --A label that can be assigned to a GameLift resource.
    
    Learn moreTagging AWS Resources in the AWS General Reference
    AWS Tagging Strategies
    Related operations
    
    
    TagResource
    UntagResource
    ListTagsForResource
    
    
    Key (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.
    
    Value (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.
    
    
    
    
    
    
    """
    pass

def create_build(Name=None, Version=None, StorageLocation=None, OperatingSystem=None, Tags=None):
    """
    Creates a new Amazon GameLift build resource for your game server binary files. Game server binaries must be combined into a zip file for use with Amazon GameLift.
    The CreateBuild operation can used in the following scenarios:
    If successful, this operation creates a new build resource with a unique build ID and places it in INITIALIZED status. A build must be in READY status before you can create fleets with it.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_build(
        Name='string',
        Version='string',
        StorageLocation={
            'Bucket': 'string',
            'Key': 'string',
            'RoleArn': 'string',
            'ObjectVersion': 'string'
        },
        OperatingSystem='WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: A descriptive label that is associated with a build. Build names do not need to be unique. You can use UpdateBuild to change this value later.

    :type Version: string
    :param Version: Version information that is associated with a build or script. Version strings do not need to be unique. You can use UpdateBuild to change this value later.

    :type StorageLocation: dict
    :param StorageLocation: Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an S3 bucket that you own. The storage location must specify an S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift to access your S3 bucket. The S3 bucket and your new build must be in the same Region.\n\nBucket (string) --An S3 bucket identifier. This is the name of the S3 bucket.\n\nKey (string) --The name of the zip file that contains the build files or script files.\n\nRoleArn (string) --The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access the S3 bucket.\n\nObjectVersion (string) --The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.\n\n\n

    :type OperatingSystem: string
    :param OperatingSystem: The operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. If your game build contains multiple executables, they all must run on the same operating system. If an operating system is not specified when creating a build, Amazon GameLift uses the default value (WINDOWS_2012). This value cannot be changed later.

    :type Tags: list
    :param Tags: A list of labels to assign to the new build resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use TagResource , UntagResource , and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.\n\n(dict) --A label that can be assigned to a GameLift resource.\n\nLearn moreTagging AWS Resources in the AWS General Reference\nAWS Tagging Strategies\nRelated operations\n\n\nTagResource\nUntagResource\nListTagsForResource\n\n\nKey (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.\n\nValue (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Build': {
        'BuildId': 'string',
        'BuildArn': 'string',
        'Name': 'string',
        'Version': 'string',
        'Status': 'INITIALIZED'|'READY'|'FAILED',
        'SizeOnDisk': 123,
        'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
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
        'RoleArn': 'string',
        'ObjectVersion': 'string'
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

Build (dict) --
The newly created build resource, including a unique build IDs and status.

BuildId (string) --
A unique identifier for a build.

BuildArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift build resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift build ARN, the resource ID matches the BuildId value.

Name (string) --
A descriptive label that is associated with a build. Build names do not need to be unique. It can be set using  CreateBuild or  UpdateBuild .

Version (string) --
Version information that is associated with a build or script. Version strings do not need to be unique. This value can be set using  CreateBuild or  UpdateBuild .

Status (string) --
Current status of the build.
Possible build statuses include the following:

INITIALIZED -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
READY -- The game build has been successfully uploaded. You can now create new fleets for this build.
FAILED -- The game build upload failed. You cannot create new fleets for this build.


SizeOnDisk (integer) --
File size of the uploaded game build, expressed in bytes. When the build status is INITIALIZED , this value is 0.

OperatingSystem (string) --
Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").



UploadCredentials (dict) --
This element is returned only when the operation is called without a storage location. It contains credentials to use when you are uploading a build file to an S3 bucket that is owned by Amazon GameLift. Credentials have a limited life span. To refresh these credentials, call  RequestUploadCredentials .

AccessKeyId (string) --
Temporary key allowing access to the Amazon GameLift S3 account.

SecretAccessKey (string) --
Temporary secret key allowing access to the Amazon GameLift S3 account.

SessionToken (string) --
Token used to associate a specific build ID with the files uploaded using these credentials.



StorageLocation (dict) --
Amazon S3 location for your game build file, including bucket name and key.

Bucket (string) --
An S3 bucket identifier. This is the name of the S3 bucket.

Key (string) --
The name of the zip file that contains the build files or script files.

RoleArn (string) --
The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access the S3 bucket.

ObjectVersion (string) --
The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.









Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.TaggingFailedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'Build': {
            'BuildId': 'string',
            'BuildArn': 'string',
            'Name': 'string',
            'Version': 'string',
            'Status': 'INITIALIZED'|'READY'|'FAILED',
            'SizeOnDisk': 123,
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
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
            'RoleArn': 'string',
            'ObjectVersion': 'string'
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

def create_fleet(Name=None, Description=None, BuildId=None, ScriptId=None, ServerLaunchPath=None, ServerLaunchParameters=None, LogPaths=None, EC2InstanceType=None, EC2InboundPermissions=None, NewGameSessionProtectionPolicy=None, RuntimeConfiguration=None, ResourceCreationLimitPolicy=None, MetricGroups=None, PeerVpcAwsAccountId=None, PeerVpcId=None, FleetType=None, InstanceRoleArn=None, CertificateConfiguration=None, Tags=None):
    """
    Creates a new fleet to run your game servers. whether they are custom game builds or Realtime Servers with game-specific script. A fleet is a set of Amazon Elastic Compute Cloud (Amazon EC2) instances, each of which can host multiple game sessions. When creating a fleet, you choose the hardware specifications, set some configuration options, and specify the game server to deploy on the new fleet.
    To create a new fleet, provide the following: (1) a fleet name, (2) an EC2 instance type and fleet type (spot or on-demand), (3) the build ID for your game build or script ID if using Realtime Servers, and (4) a runtime configuration, which determines how game servers will run on each instance in the fleet.
    If the CreateFleet call is successful, Amazon GameLift performs the following tasks. You can track the process of a fleet by checking the fleet status or by monitoring fleet creation events:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_fleet(
        Name='string',
        Description='string',
        BuildId='string',
        ScriptId='string',
        ServerLaunchPath='string',
        ServerLaunchParameters='string',
        LogPaths=[
            'string',
        ],
        EC2InstanceType='t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
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
        FleetType='ON_DEMAND'|'SPOT',
        InstanceRoleArn='string',
        CertificateConfiguration={
            'CertificateType': 'DISABLED'|'GENERATED'
        },
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA descriptive label that is associated with a fleet. Fleet names do not need to be unique.\n

    :type Description: string
    :param Description: A human-readable description of a fleet.

    :type BuildId: string
    :param BuildId: A unique identifier for a build to be deployed on the new fleet. You can use either the build ID or ARN value. The custom game server build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.

    :type ScriptId: string
    :param ScriptId: A unique identifier for a Realtime script to be deployed on the new fleet. You can use either the script ID or ARN value. The Realtime script must have been successfully uploaded to Amazon GameLift. This fleet setting cannot be changed once the fleet is created.

    :type ServerLaunchPath: string
    :param ServerLaunchPath: This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.

    :type ServerLaunchParameters: string
    :param ServerLaunchParameters: This parameter is no longer used. Instead, specify server launch parameters in the RuntimeConfiguration parameter. (Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.)

    :type LogPaths: list
    :param LogPaths: This parameter is no longer used. Instead, to specify where Amazon GameLift should store log files once a server process shuts down, use the Amazon GameLift server API ProcessReady() and specify one or more directory paths in logParameters . See more information in the Server API Reference .\n\n(string) --\n\n

    :type EC2InstanceType: string
    :param EC2InstanceType: [REQUIRED]\nThe name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.\n

    :type EC2InboundPermissions: list
    :param EC2InboundPermissions: Range of IP addresses and port settings that permit inbound traffic to access game sessions that are running on the fleet. For fleets using a custom game build, this parameter is required before game sessions running on the fleet can accept connections. For Realtime Servers fleets, Amazon GameLift automatically sets TCP and UDP ranges for use by the Realtime servers. You can specify multiple permission settings or add more by updating the fleet.\n\n(dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift hosting resource. New game sessions that are started on the fleet are assigned an IP address/port number combination, which must fall into the fleet\'s allowed ranges. For fleets created with a custom game server, the ranges reflect the server\'s game session assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP for use by the Realtime servers.\n\nFromPort (integer) -- [REQUIRED]A starting value for a range of allowed port numbers.\n\nToPort (integer) -- [REQUIRED]An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .\n\nIpRange (string) -- [REQUIRED]A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: '000.000.000.000/[subnet mask] ' or optionally the shortened version '0.0.0.0/[subnet mask] '.\n\nProtocol (string) -- [REQUIRED]The network communication protocol used by the fleet.\n\n\n\n\n

    :type NewGameSessionProtectionPolicy: string
    :param NewGameSessionProtectionPolicy: A game session protection policy to apply to all instances in this fleet. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet\'s protection policy using UpdateFleetAttributes , but this change will only affect sessions created after the policy change. You can also set protection for individual instances using UpdateGameSession .\n\nNoProtection - The game session can be terminated during a scale-down event.\nFullProtection - If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.\n\n

    :type RuntimeConfiguration: dict
    :param RuntimeConfiguration: Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception. (This parameter replaces the parameters ServerLaunchPath and ServerLaunchParameters , although requests that contain values for these parameters instead of a runtime configuration will continue to work.) This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration replaced these parameters, but fleets that use them will continue to work.\n\nServerProcesses (list) --A collection of server process configurations that describe which server processes to run on each instance in a fleet.\n\n(dict) --A set of instructions for launching server processes on each instance in a fleet. Server processes run either a custom game build executable or a Realtime Servers script. Each instruction set identifies the location of the custom game build executable or Realtime launch script, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet\'s `` RuntimeConfiguration `` .\n\nLaunchPath (string) -- [REQUIRED]The location of the server executable in a custom game build or the name of the Realtime script file that contains the Init() function. Game builds and Realtime scripts are installed on instances at the root:\n\nWindows (for custom game builds only): C:\\game . Example: 'C:\\game\\MyGame\\server.exe '\nLinux: /local/game . Examples: '/local/game/MyGame/server.exe ' or '/local/game/MyRealtimeScript.js '\n\n\nParameters (string) --An optional list of parameters to pass to the server executable or Realtime script on launch.\n\nConcurrentExecutions (integer) -- [REQUIRED]The number of server processes that use this configuration to run concurrently on an instance.\n\n\n\n\n\nMaxConcurrentGameSessionActivations (integer) --The maximum number of game sessions with status ACTIVATING to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.\n\nGameSessionActivationTimeoutSeconds (integer) --The maximum amount of time (in seconds) that a game session can remain in status ACTIVATING . If the game session is not active before the timeout, activation is terminated and the game session status is changed to TERMINATED .\n\n\n

    :type ResourceCreationLimitPolicy: dict
    :param ResourceCreationLimitPolicy: A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.\n\nNewGameSessionsPerCreator (integer) --The maximum number of game sessions that an individual can create during the policy period.\n\nPolicyPeriodInMinutes (integer) --The time span used in evaluating the resource creation limit policy.\n\n\n

    :type MetricGroups: list
    :param MetricGroups: The name of an Amazon CloudWatch metric group to add this fleet to. A metric group aggregates the metrics for all fleets in the group. Specify an existing metric group name, or provide a new name to create a new metric group. A fleet can only be included in one metric group at a time.\n\n(string) --\n\n

    :type PeerVpcAwsAccountId: string
    :param PeerVpcAwsAccountId: A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your account ID in the AWS Management Console under account settings.

    :type PeerVpcId: string
    :param PeerVpcId: A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .

    :type FleetType: string
    :param FleetType: Indicates whether to use On-Demand instances or Spot instances for this fleet. If empty, the default is ON_DEMAND . Both categories of instances use identical hardware and configurations based on the instance type selected for this fleet. Learn more about On-Demand versus Spot Instances .

    :type InstanceRoleArn: string
    :param InstanceRoleArn: A unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role\'s ARN from the IAM dashboard in the AWS Management Console. Learn more about using on-box credentials for your game servers at Access external resources from a game server .

    :type CertificateConfiguration: dict
    :param CertificateConfiguration: Indicates whether to generate a TLS/SSL certificate for the new fleet. TLS certificates are used for encrypting traffic between game clients and game servers running on GameLift. If this parameter is not specified, the default value, DISABLED, is used. This fleet setting cannot be changed once the fleet is created. Learn more at Securing Client/Server Communication .\nNote: This feature requires the AWS Certificate Manager (ACM) service, which is available in the AWS global partition but not in all other partitions. When working in a partition that does not support this feature, a request for a new fleet with certificate generation results fails with a 4xx unsupported Region error.\nValid values include:\n\nGENERATED - Generate a TLS/SSL certificate for this fleet.\nDISABLED - (default) Do not generate a TLS/SSL certificate for this fleet.\n\n\nCertificateType (string) -- [REQUIRED]Indicates whether a TLS/SSL certificate was generated for a fleet.\n\n\n

    :type Tags: list
    :param Tags: A list of labels to assign to the new fleet resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use TagResource , UntagResource , and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.\n\n(dict) --A label that can be assigned to a GameLift resource.\n\nLearn moreTagging AWS Resources in the AWS General Reference\nAWS Tagging Strategies\nRelated operations\n\n\nTagResource\nUntagResource\nListTagsForResource\n\n\nKey (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.\n\nValue (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FleetAttributes': {
        'FleetId': 'string',
        'FleetArn': 'string',
        'FleetType': 'ON_DEMAND'|'SPOT',
        'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
        'Description': 'string',
        'Name': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'TerminationTime': datetime(2015, 1, 1),
        'Status': 'NEW'|'DOWNLOADING'|'VALIDATING'|'BUILDING'|'ACTIVATING'|'ACTIVE'|'DELETING'|'ERROR'|'TERMINATED',
        'BuildId': 'string',
        'BuildArn': 'string',
        'ScriptId': 'string',
        'ScriptArn': 'string',
        'ServerLaunchPath': 'string',
        'ServerLaunchParameters': 'string',
        'LogPaths': [
            'string',
        ],
        'NewGameSessionProtectionPolicy': 'NoProtection'|'FullProtection',
        'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
        'ResourceCreationLimitPolicy': {
            'NewGameSessionsPerCreator': 123,
            'PolicyPeriodInMinutes': 123
        },
        'MetricGroups': [
            'string',
        ],
        'StoppedActions': [
            'AUTO_SCALING',
        ],
        'InstanceRoleArn': 'string',
        'CertificateConfiguration': {
            'CertificateType': 'DISABLED'|'GENERATED'
        }
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

FleetAttributes (dict) --
Properties for the newly created fleet.

FleetId (string) --
A unique identifier for a fleet.

FleetArn (string) --
The Amazon Resource Name (ARN ) that is assigned to a GameLift fleet resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift fleet ARN, the resource ID matches the FleetId value.

FleetType (string) --
Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may be interrupted with a two-minute notification.

InstanceType (string) --
EC2 instance type indicating the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. See Amazon EC2 Instance Types for detailed descriptions.

Description (string) --
Human-readable description of the fleet.

Name (string) --
A descriptive label that is associated with a fleet. Fleet names do not need to be unique.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

TerminationTime (datetime) --
Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

Status (string) --
Current status of the fleet.
Possible fleet statuses include the following:

NEW -- A new fleet has been defined and desired instances is set to 1.
DOWNLOADING/VALIDATING/BUILDING/ACTIVATING -- Amazon GameLift is setting up the new fleet, creating new instances with the game build or Realtime script and starting server processes.
ACTIVE -- Hosts can now accept game sessions.
ERROR -- An error occurred when downloading, validating, building, or activating the fleet.
DELETING -- Hosts are responding to a delete fleet request.
TERMINATED -- The fleet no longer exists.


BuildId (string) --
A unique identifier for a build.

BuildArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift build resource that is deployed on instances in this fleet. In a GameLift build ARN, the resource ID matches the BuildId value.

ScriptId (string) --
A unique identifier for a Realtime script.

ScriptArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift script resource that is deployed on instances in this fleet. In a GameLift script ARN, the resource ID matches the ScriptId value.

ServerLaunchPath (string) --
Path to a game server executable in the fleet\'s build, specified for fleets created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after this date are specified in the fleet\'s  RuntimeConfiguration .

ServerLaunchParameters (string) --
Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch parameters for fleets created after this date are specified in the fleet\'s  RuntimeConfiguration .

LogPaths (list) --
Location of default log files. When a server process is shut down, Amazon GameLift captures and stores any log files in this location. These logs are in addition to game session logs; see more on game session logs in the Amazon GameLift Developer Guide . If no default log path for a fleet is specified, Amazon GameLift automatically uploads logs that are stored on each instance at C:\\game\\logs (for Windows) or /local/game/logs (for Linux). Use the Amazon GameLift console to access stored logs.

(string) --


NewGameSessionProtectionPolicy (string) --
The type of game session protection to set for all new instances started in the fleet.

NoProtection -- The game session can be terminated during a scale-down event.
FullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.


OperatingSystem (string) --
Operating system of the fleet\'s computing resources. A fleet\'s operating system depends on the OS specified for the build that is deployed on this fleet.

ResourceCreationLimitPolicy (dict) --
Fleet policy to limit the number of game sessions an individual player can create over a span of time.

NewGameSessionsPerCreator (integer) --
The maximum number of game sessions that an individual can create during the policy period.

PolicyPeriodInMinutes (integer) --
The time span used in evaluating the resource creation limit policy.



MetricGroups (list) --
Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view metrics for an individual fleet or aggregated metrics for fleets that are in a fleet metric group. A fleet can be included in only one metric group at a time.

(string) --


StoppedActions (list) --
List of fleet actions that have been suspended using  StopFleetActions . This includes auto-scaling.

(string) --


InstanceRoleArn (string) --
A unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role\'s ARN from the IAM dashboard in the AWS Management Console. Learn more about using on-box credentials for your game servers at Access external resources from a game server .

CertificateConfiguration (dict) --
Indicates whether a TLS/SSL certificate was generated for the fleet.

CertificateType (string) --
Indicates whether a TLS/SSL certificate was generated for a fleet.











Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.LimitExceededException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.TaggingFailedException


    :return: {
        'FleetAttributes': {
            'FleetId': 'string',
            'FleetArn': 'string',
            'FleetType': 'ON_DEMAND'|'SPOT',
            'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
            'Description': 'string',
            'Name': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TerminationTime': datetime(2015, 1, 1),
            'Status': 'NEW'|'DOWNLOADING'|'VALIDATING'|'BUILDING'|'ACTIVATING'|'ACTIVE'|'DELETING'|'ERROR'|'TERMINATED',
            'BuildId': 'string',
            'BuildArn': 'string',
            'ScriptId': 'string',
            'ScriptArn': 'string',
            'ServerLaunchPath': 'string',
            'ServerLaunchParameters': 'string',
            'LogPaths': [
                'string',
            ],
            'NewGameSessionProtectionPolicy': 'NoProtection'|'FullProtection',
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
            'ResourceCreationLimitPolicy': {
                'NewGameSessionsPerCreator': 123,
                'PolicyPeriodInMinutes': 123
            },
            'MetricGroups': [
                'string',
            ],
            'StoppedActions': [
                'AUTO_SCALING',
            ],
            'InstanceRoleArn': 'string',
            'CertificateConfiguration': {
                'CertificateType': 'DISABLED'|'GENERATED'
            }
        }
    }
    
    
    :returns: 
    CreateFleet
    ListFleets
    DeleteFleet
    DescribeFleetAttributes
    UpdateFleetAttributes
    StartFleetActions or  StopFleetActions
    
    """
    pass

def create_game_server_group(GameServerGroupName=None, RoleArn=None, MinSize=None, MaxSize=None, LaunchTemplate=None, InstanceDefinitions=None, AutoScalingPolicy=None, BalancingStrategy=None, GameServerProtectionPolicy=None, VpcSubnets=None, Tags=None):
    """
    Creates a GameLift FleetIQ game server group to manage a collection of EC2 instances for game hosting. In addition to creating the game server group, this action also creates an Auto Scaling group in your AWS account and establishes a link between the two groups. You have full control over configuration of the Auto Scaling group, but GameLift FleetIQ routinely certain Auto Scaling group properties in order to optimize the group\'s instances for low-cost game hosting. You can view the status of your game server groups in the GameLift Console. Game server group metrics and events are emitted to Amazon CloudWatch.
    Prior creating a new game server group, you must set up the following:
    To create a new game server group, provide a name and specify the IAM role and EC2 launch template. You also need to provide a list of instance types to be used in the group and set initial maximum and minimum limits on the group\'s instance count. You can optionally set an autoscaling policy with target tracking based on a GameLift FleetIQ metric.
    Once the game server group and corresponding Auto Scaling group are created, you have full access to change the Auto Scaling group\'s configuration as needed. Keep in mind, however, that some properties are periodically updated by GameLift FleetIQ as it balances the group\'s instances based on availability and cost.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_game_server_group(
        GameServerGroupName='string',
        RoleArn='string',
        MinSize=123,
        MaxSize=123,
        LaunchTemplate={
            'LaunchTemplateId': 'string',
            'LaunchTemplateName': 'string',
            'Version': 'string'
        },
        InstanceDefinitions=[
            {
                'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'WeightedCapacity': 'string'
            },
        ],
        AutoScalingPolicy={
            'EstimatedInstanceWarmup': 123,
            'TargetTrackingConfiguration': {
                'TargetValue': 123.0
            }
        },
        BalancingStrategy='SPOT_ONLY'|'SPOT_PREFERRED',
        GameServerProtectionPolicy='NO_PROTECTION'|'FULL_PROTECTION',
        VpcSubnets=[
            'string',
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nAn identifier for the new game server group. This value is used to generate unique ARN identifiers for the EC2 Auto Scaling group and the GameLift FleetIQ game server group. The name must be unique per Region per AWS account.\n

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups. The submitted role is validated to ensure that it contains the necessary permissions for game server groups.\n

    :type MinSize: integer
    :param MinSize: [REQUIRED]\nThe minimum number of instances allowed in the EC2 Auto Scaling group. During autoscaling events, GameLift FleetIQ and EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1.\n

    :type MaxSize: integer
    :param MaxSize: [REQUIRED]\nThe maximum number of instances allowed in the EC2 Auto Scaling group. During autoscaling events, GameLift FleetIQ and EC2 do not scale up the group above this maximum.\n

    :type LaunchTemplate: dict
    :param LaunchTemplate: [REQUIRED]\nThe EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. You can specify the template using either the template name or ID. For help with creating a launch template, see Creating a Launch Template for an Auto Scaling Group in the Amazon EC2 Auto Scaling User Guide .\n\nLaunchTemplateId (string) --A unique identifier for an existing EC2 launch template.\n\nLaunchTemplateName (string) --A readable identifier for an existing EC2 launch template.\n\nVersion (string) --The version of the EC2 launch template to use. If no version is specified, the default version will be used. EC2 allows you to specify a default version for a launch template, if none is set, the default is the first version created.\n\n\n

    :type InstanceDefinitions: list
    :param InstanceDefinitions: [REQUIRED]\nA set of EC2 instance types to use when creating instances in the group. The instance definitions must specify at least two different instance types that are supported by GameLift FleetIQ. For more information on instance types, see EC2 Instance Types in the Amazon EC2 User Guide .\n\n(dict) --\nThis data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.\nAn allowed instance type for your game server group. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.\n\nInstanceType (string) -- [REQUIRED]An EC2 instance type designation.\n\nWeightedCapacity (string) --Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by GameLift FleetIQ to calculate the instance type\'s cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see Instance Weighting in the Amazon EC2 Auto Scaling User Guide . Default value is '1'.\n\n\n\n\n

    :type AutoScalingPolicy: dict
    :param AutoScalingPolicy: Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. The scaling policy uses the metric 'PercentUtilizedGameServers' to maintain a buffer of idle game servers that can immediately accommodate new games and players. Once the game server and Auto Scaling groups are created, you can update the scaling policy settings directly in Auto Scaling Groups.\n\nEstimatedInstanceWarmup (integer) --Length of time, in seconds, it takes for a new instance to start new game server processes and register with GameLift FleetIQ. Specifying a warm-up time can be useful, particularly with game servers that take a long time to start up, because it avoids prematurely starting new instances\n\nTargetTrackingConfiguration (dict) -- [REQUIRED]Settings for a target-based scaling policy applied to Auto Scaling group. These settings are used to create a target-based policy that tracks the GameLift FleetIQ metric 'PercentUtilizedGameServers' and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.\n\nTargetValue (float) -- [REQUIRED]Desired value to use with a game server group target-based scaling policy.\n\n\n\n\n

    :type BalancingStrategy: string
    :param BalancingStrategy: The fallback balancing method to use for the game server group when Spot instances in a Region become unavailable or are not viable for game hosting. Once triggered, this method remains active until Spot instances can once again be used. Method options include:\n\nSPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.\nSPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.\n\n

    :type GameServerProtectionPolicy: string
    :param GameServerProtectionPolicy: A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running may by terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running. An exception to this is Spot Instances, which may be terminated by AWS regardless of protection status. This property is set to NO_PROTECTION by default.

    :type VpcSubnets: list
    :param VpcSubnets: A list of virtual private cloud (VPC) subnets to use with instances in the game server group. By default, all GameLift FleetIQ-supported availability zones are used; this parameter allows you to specify VPCs that you\'ve set up.\n\n(string) --\n\n

    :type Tags: list
    :param Tags: A list of labels to assign to the new game server group resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management, and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use TagResource , UntagResource , and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.\n\n(dict) --A label that can be assigned to a GameLift resource.\n\nLearn moreTagging AWS Resources in the AWS General Reference\nAWS Tagging Strategies\nRelated operations\n\n\nTagResource\nUntagResource\nListTagsForResource\n\n\nKey (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.\n\nValue (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServerGroup': {
        'GameServerGroupName': 'string',
        'GameServerGroupArn': 'string',
        'RoleArn': 'string',
        'InstanceDefinitions': [
            {
                'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'WeightedCapacity': 'string'
            },
        ],
        'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
        'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
        'AutoScalingGroupArn': 'string',
        'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
        'StatusReason': 'string',
        'SuspendedActions': [
            'REPLACE_INSTANCE_TYPES',
        ],
        'CreationTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

GameServerGroup (dict) --
The newly created game server group object, including the new ARN value for the GameLift FleetIQ game server group and the object\'s status. The EC2 Auto Scaling group ARN is initially null, since the group has not yet been created. This value is added once the game server group status reaches ACTIVE.

GameServerGroupName (string) --
A developer-defined identifier for the game server group. The name is unique per Region per AWS account.

GameServerGroupArn (string) --
A generated unique ID for the game server group.

RoleArn (string) --
The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups. The submitted role is validated to ensure that it contains the necessary permissions for game server groups.

InstanceDefinitions (list) --
The set of EC2 instance types that GameLift FleetIQ can use when rebalancing and autoscaling instances in the group.

(dict) --

This data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.

An allowed instance type for your game server group. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

InstanceType (string) --
An EC2 instance type designation.

WeightedCapacity (string) --
Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by GameLift FleetIQ to calculate the instance type\'s cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see Instance Weighting in the Amazon EC2 Auto Scaling User Guide . Default value is "1".





BalancingStrategy (string) --
The fallback balancing method to use for the game server group when Spot instances in a Region become unavailable or are not viable for game hosting. Once triggered, this method remains active until Spot instances can once again be used. Method options include:

SPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.
SPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.


GameServerProtectionPolicy (string) --
A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running may be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see  DeleteGameServerGroup ). An exception to this is Spot Instances, which may be terminated by AWS regardless of protection status.

AutoScalingGroupArn (string) --
A generated unique ID for the EC2 Auto Scaling group with is associated with this game server group.

Status (string) --
The current status of the game server group. Possible statuses include:

NEW - GameLift FleetIQ has validated the CreateGameServerGroup() request.
ACTIVATING - GameLift FleetIQ is setting up a game server group, which includes creating an autoscaling group in your AWS account.
ACTIVE - The game server group has been successfully created.
DELETE_SCHEDULED - A request to delete the game server group has been received.
DELETING - GameLift FleetIQ has received a valid DeleteGameServerGroup() request and is processing it. GameLift FleetIQ must first complete and release hosts before it deletes the autoscaling group and the game server group.
DELETED - The game server group has been successfully deleted.
ERROR - The asynchronous processes of activating or deleting a game server group has failed, resulting in an error state.


StatusReason (string) --
Additional information about the current game server group status. This information may provide additional insight on groups that in ERROR status.

SuspendedActions (list) --
A list of activities that are currently suspended for this game server group. If this property is empty, all activities are occurring.

(string) --


CreationTime (datetime) --
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --
A time stamp indicating when this game server group was last updated.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.LimitExceededException


    :return: {
        'GameServerGroup': {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'RoleArn': 'string',
            'InstanceDefinitions': [
                {
                    'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                    'WeightedCapacity': 'string'
                },
            ],
            'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
            'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
            'AutoScalingGroupArn': 'string',
            'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
            'StatusReason': 'string',
            'SuspendedActions': [
                'REPLACE_INSTANCE_TYPES',
            ],
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CreateGameServerGroup
    ListGameServerGroups
    DescribeGameServerGroup
    UpdateGameServerGroup
    DeleteGameServerGroup
    ResumeGameServerGroup
    SuspendGameServerGroup
    
    """
    pass

def create_game_session(FleetId=None, AliasId=None, MaximumPlayerSessionCount=None, Name=None, GameProperties=None, CreatorId=None, GameSessionId=None, IdempotencyToken=None, GameSessionData=None):
    """
    Creates a multiplayer game session for players. This action creates a game session record and assigns an available server process in the specified fleet to host the game session. A fleet must have an ACTIVE status before a game session can be created in it.
    To create a game session, specify either fleet ID or alias ID and indicate a maximum number of players to allow in the game session. You can also provide a name and game-specific properties for this game session. If successful, a  GameSession object is returned containing the game session properties and other settings you specified.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param FleetId: A unique identifier for a fleet to create a game session in. You can use either the fleet ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.

    :type AliasId: string
    :param AliasId: A unique identifier for an alias associated with the fleet to create a game session in. You can use either the alias ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.

    :type MaximumPlayerSessionCount: integer
    :param MaximumPlayerSessionCount: [REQUIRED]\nThe maximum number of players that can be connected simultaneously to the game session.\n

    :type Name: string
    :param Name: A descriptive label that is associated with a game session. Session names do not need to be unique.

    :type GameProperties: list
    :param GameProperties: Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ).\n\n(dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .\n\nKey (string) -- [REQUIRED]The game property identifier.\n\nValue (string) -- [REQUIRED]The game property value.\n\n\n\n\n

    :type CreatorId: string
    :param CreatorId: A unique identifier for a player or entity creating the game session. This ID is used to enforce a resource protection policy (if one exists) that limits the number of concurrent active game sessions one player can have.

    :type GameSessionId: string
    :param GameSessionId: This parameter is no longer preferred. Please use ``IdempotencyToken`` instead. Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session\'s ID. (A game session ARN has the following format: arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token> .)

    :type IdempotencyToken: string
    :param IdempotencyToken: Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session\'s ID. (A game session ARN has the following format: arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token> .) Idempotency tokens remain in use for 30 days after a game session has ended; game session objects are retained for this time period and then deleted.

    :type GameSessionData: string
    :param GameSessionData: Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ).

    :rtype: dict

ReturnsResponse Syntax
{
    'GameSession': {
        'GameSessionId': 'string',
        'Name': 'string',
        'FleetId': 'string',
        'FleetArn': 'string',
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
        'DnsName': 'string',
        'Port': 123,
        'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
        'CreatorId': 'string',
        'GameSessionData': 'string',
        'MatchmakerData': 'string'
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

GameSession (dict) --
Object that describes the newly created game session record.

GameSessionId (string) --
A unique identifier for the game session. A game session ARN has the following format: arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token> .

Name (string) --
A descriptive label that is associated with a game session. Session names do not need to be unique.

FleetId (string) --
A unique identifier for a fleet that the game session is running on.

FleetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift fleet that this game session is running on.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

TerminationTime (datetime) --
Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

CurrentPlayerSessionCount (integer) --
Number of players currently in the game session.

MaximumPlayerSessionCount (integer) --
The maximum number of players that can be connected simultaneously to the game session.

Status (string) --
Current status of the game session. A game session must have an ACTIVE status to have player sessions.

StatusReason (string) --
Provides additional information about game session status. INTERRUPTED indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.

GameProperties (list) --
Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). You can search for active game sessions based on this custom data with  SearchGameSessions .

(dict) --
Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --
The game property identifier.

Value (string) --
The game property value.





IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

PlayerSessionCreationPolicy (string) --
Indicates whether or not the game session is accepting new players.

CreatorId (string) --
A unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.

GameSessionData (string) --
Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

MatchmakerData (string) --
Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see Match Data . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ).









Exceptions

GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidFleetStatusException
GameLift.Client.exceptions.TerminalRoutingStrategyException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.FleetCapacityExceededException
GameLift.Client.exceptions.LimitExceededException
GameLift.Client.exceptions.IdempotentParameterMismatchException


    :return: {
        'GameSession': {
            'GameSessionId': 'string',
            'Name': 'string',
            'FleetId': 'string',
            'FleetArn': 'string',
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
            'DnsName': 'string',
            'Port': 123,
            'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
            'CreatorId': 'string',
            'GameSessionData': 'string',
            'MatchmakerData': 'string'
        }
    }
    
    
    :returns: 
    FleetId (string) -- A unique identifier for a fleet to create a game session in. You can use either the fleet ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.
    AliasId (string) -- A unique identifier for an alias associated with the fleet to create a game session in. You can use either the alias ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.
    MaximumPlayerSessionCount (integer) -- [REQUIRED]
    The maximum number of players that can be connected simultaneously to the game session.
    
    Name (string) -- A descriptive label that is associated with a game session. Session names do not need to be unique.
    GameProperties (list) -- Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).
    
    (dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .
    
    Key (string) -- [REQUIRED]The game property identifier.
    
    Value (string) -- [REQUIRED]The game property value.
    
    
    
    
    
    CreatorId (string) -- A unique identifier for a player or entity creating the game session. This ID is used to enforce a resource protection policy (if one exists) that limits the number of concurrent active game sessions one player can have.
    GameSessionId (string) -- This parameter is no longer preferred. Please use ``IdempotencyToken`` instead. Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session\'s ID. (A game session ARN has the following format: arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token> .)
    IdempotencyToken (string) -- Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session\'s ID. (A game session ARN has the following format: arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token> .) Idempotency tokens remain in use for 30 days after a game session has ended; game session objects are retained for this time period and then deleted.
    GameSessionData (string) -- Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).
    
    """
    pass

def create_game_session_queue(Name=None, TimeoutInSeconds=None, PlayerLatencyPolicies=None, Destinations=None, Tags=None):
    """
    Establishes a new queue for processing requests to place new game sessions. A queue identifies where new game sessions can be hosted -- by specifying a list of destinations (fleets or aliases) -- and how long requests can wait in the queue before timing out. You can set up a queue to try to place game sessions on fleets in multiple Regions. To add placement requests to a queue, call  StartGameSessionPlacement and reference the queue name.
    To create a new queue, provide a name, timeout value, a list of destinations and, if desired, a set of latency policies. If successful, a new queue object is returned.
    See also: AWS API Documentation
    
    Exceptions
    
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
        ],
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA descriptive label that is associated with game session queue. Queue names must be unique within each Region.\n

    :type TimeoutInSeconds: integer
    :param TimeoutInSeconds: The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.

    :type PlayerLatencyPolicies: list
    :param PlayerLatencyPolicies: A collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, the policy is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. A player latency policy must set a value for MaximumIndividualPlayerLatencyMilliseconds . If none is set, this API request fails.\n\n(dict) --Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed with any fleet in a Region where a player reports latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.\n\nCreateGameSessionQueue\nDescribeGameSessionQueues\nUpdateGameSessionQueue\nDeleteGameSessionQueue\n\n\nMaximumIndividualPlayerLatencyMilliseconds (integer) --The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.\n\nPolicyDurationSeconds (integer) --The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.\n\n\n\n\n

    :type Destinations: list
    :param Destinations: A list of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.\n\n(dict) --Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination that is configured for a queue.\n\nCreateGameSessionQueue\nDescribeGameSessionQueues\nUpdateGameSessionQueue\nDeleteGameSessionQueue\n\n\nDestinationArn (string) --The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.\n\n\n\n\n

    :type Tags: list
    :param Tags: A list of labels to assign to the new game session queue resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use TagResource , UntagResource , and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.\n\n(dict) --A label that can be assigned to a GameLift resource.\n\nLearn moreTagging AWS Resources in the AWS General Reference\nAWS Tagging Strategies\nRelated operations\n\n\nTagResource\nUntagResource\nListTagsForResource\n\n\nKey (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.\n\nValue (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

GameSessionQueue (dict) --
An object that describes the newly created game session queue.

Name (string) --
A descriptive label that is associated with game session queue. Queue names must be unique within each Region.

GameSessionQueueArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift game session queue ARN, the resource ID matches the Name value.

TimeoutInSeconds (integer) --
The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.

PlayerLatencyPolicies (list) --
A collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, the policy is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement.

(dict) --
Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed with any fleet in a Region where a player reports latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.

CreateGameSessionQueue
DescribeGameSessionQueues
UpdateGameSessionQueue
DeleteGameSessionQueue


MaximumIndividualPlayerLatencyMilliseconds (integer) --
The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.

PolicyDurationSeconds (integer) --
The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.





Destinations (list) --
A list of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.

(dict) --
Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination that is configured for a queue.

CreateGameSessionQueue
DescribeGameSessionQueues
UpdateGameSessionQueue
DeleteGameSessionQueue


DestinationArn (string) --
The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.













Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.LimitExceededException
GameLift.Client.exceptions.TaggingFailedException


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
    A descriptive label that is associated with game session queue. Queue names must be unique within each Region.
    
    TimeoutInSeconds (integer) -- The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.
    PlayerLatencyPolicies (list) -- A collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, the policy is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. A player latency policy must set a value for MaximumIndividualPlayerLatencyMilliseconds . If none is set, this API request fails.
    
    (dict) --Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed with any fleet in a Region where a player reports latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
    
    CreateGameSessionQueue
    DescribeGameSessionQueues
    UpdateGameSessionQueue
    DeleteGameSessionQueue
    
    
    MaximumIndividualPlayerLatencyMilliseconds (integer) --The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
    
    PolicyDurationSeconds (integer) --The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
    
    
    
    
    
    Destinations (list) -- A list of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.
    
    (dict) --Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination that is configured for a queue.
    
    CreateGameSessionQueue
    DescribeGameSessionQueues
    UpdateGameSessionQueue
    DeleteGameSessionQueue
    
    
    DestinationArn (string) --The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.
    
    
    
    
    
    Tags (list) -- A list of labels to assign to the new game session queue resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use  TagResource ,  UntagResource , and  ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
    
    (dict) --A label that can be assigned to a GameLift resource.
    
    Learn moreTagging AWS Resources in the AWS General Reference
    AWS Tagging Strategies
    Related operations
    
    
    TagResource
    UntagResource
    ListTagsForResource
    
    
    Key (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.
    
    Value (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.
    
    
    
    
    
    
    """
    pass

def create_matchmaking_configuration(Name=None, Description=None, GameSessionQueueArns=None, RequestTimeoutSeconds=None, AcceptanceTimeoutSeconds=None, AcceptanceRequired=None, RuleSetName=None, NotificationTarget=None, AdditionalPlayerCount=None, CustomEventData=None, GameProperties=None, GameSessionData=None, BackfillMode=None, Tags=None):
    """
    Defines a new matchmaking configuration for use with FlexMatch. A matchmaking configuration sets out guidelines for matching players and getting the matches into games. You can set up multiple matchmaking configurations to handle the scenarios needed for your game. Each matchmaking ticket ( StartMatchmaking or  StartMatchBackfill ) specifies a configuration for the match and provides player attributes to support the configuration being used.
    To create a matchmaking configuration, at a minimum you must specify the following: configuration name; a rule set that governs how to evaluate players and find acceptable matches; a game session queue to use when placing a new game session for the match; and the maximum time allowed for a matchmaking attempt.
    There are two ways to track the progress of matchmaking tickets: (1) polling ticket status with  DescribeMatchmaking ; or (2) receiving notifications with Amazon Simple Notification Service (SNS). To use notifications, you first need to set up an SNS topic to receive the notifications, and provide the topic ARN in the matchmaking configuration. Since notifications promise only "best effort" delivery, we recommend calling DescribeMatchmaking if no notifications are received within 30 seconds.
    See also: AWS API Documentation
    
    Exceptions
    
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
        GameSessionData='string',
        BackfillMode='AUTOMATIC'|'MANUAL',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.\n

    :type Description: string
    :param Description: A human-readable description of the matchmaking configuration.

    :type GameSessionQueueArns: list
    :param GameSessionQueueArns: [REQUIRED]\nAmazon Resource Name (ARN ) that is assigned to a GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any Region.\n\n(string) --\n\n

    :type RequestTimeoutSeconds: integer
    :param RequestTimeoutSeconds: [REQUIRED]\nThe maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.\n

    :type AcceptanceTimeoutSeconds: integer
    :param AcceptanceTimeoutSeconds: The length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.

    :type AcceptanceRequired: boolean
    :param AcceptanceRequired: [REQUIRED]\nA flag that determines whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE .\n

    :type RuleSetName: string
    :param RuleSetName: [REQUIRED]\nA unique identifier for a matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.\n

    :type NotificationTarget: string
    :param NotificationTarget: An SNS topic ARN that is set up to receive matchmaking notifications.

    :type AdditionalPlayerCount: integer
    :param AdditionalPlayerCount: The number of player slots in a match to keep open for future players. For example, assume that the configuration\'s rule set specifies a match for a single 12-person team. If the additional player count is set to 2, only 10 players are initially selected for the match.

    :type CustomEventData: string
    :param CustomEventData: Information to be added to all events related to this matchmaking configuration.

    :type GameProperties: list
    :param GameProperties: A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new GameSession object that is created for a successful match.\n\n(dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .\n\nKey (string) -- [REQUIRED]The game property identifier.\n\nValue (string) -- [REQUIRED]The game property value.\n\n\n\n\n

    :type GameSessionData: string
    :param GameSessionData: A set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new GameSession object that is created for a successful match.

    :type BackfillMode: string
    :param BackfillMode: The method used to backfill game sessions that are created with this matchmaking configuration. Specify MANUAL when your game manages backfill requests manually or does not use the match backfill feature. Specify AUTOMATIC to have GameLift create a StartMatchBackfill request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in Backfill Existing Games with FlexMatch .

    :type Tags: list
    :param Tags: A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use TagResource , UntagResource , and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.\n\n(dict) --A label that can be assigned to a GameLift resource.\n\nLearn moreTagging AWS Resources in the AWS General Reference\nAWS Tagging Strategies\nRelated operations\n\n\nTagResource\nUntagResource\nListTagsForResource\n\n\nKey (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.\n\nValue (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Configuration': {
        'Name': 'string',
        'ConfigurationArn': 'string',
        'Description': 'string',
        'GameSessionQueueArns': [
            'string',
        ],
        'RequestTimeoutSeconds': 123,
        'AcceptanceTimeoutSeconds': 123,
        'AcceptanceRequired': True|False,
        'RuleSetName': 'string',
        'RuleSetArn': 'string',
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
        'GameSessionData': 'string',
        'BackfillMode': 'AUTOMATIC'|'MANUAL'
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

Configuration (dict) --
Object that describes the newly created matchmaking configuration.

Name (string) --
A unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.

ConfigurationArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift matchmaking configuration resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift configuration ARN, the resource ID matches the Name value.

Description (string) --
A descriptive label that is associated with matchmaking configuration.

GameSessionQueueArns (list) --
Amazon Resource Name (ARN ) that is assigned to a GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. GameLift uses the listed queues when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any Region.

(string) --


RequestTimeoutSeconds (integer) --
The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.

AcceptanceTimeoutSeconds (integer) --
The length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.

AcceptanceRequired (boolean) --
A flag that indicates whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.

RuleSetName (string) --
A unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same Region.

RuleSetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift matchmaking rule set resource that this configuration uses.

NotificationTarget (string) --
An SNS topic ARN that is set up to receive matchmaking notifications.

AdditionalPlayerCount (integer) --
The number of player slots in a match to keep open for future players. For example, assume that the configuration\'s rule set specifies a match for a single 12-person team. If the additional player count is set to 2, only 10 players are initially selected for the match.

CustomEventData (string) --
Information to attach to all events related to the matchmaking configuration.

CreationTime (datetime) --
The time stamp indicating when this data object was created. The format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

GameProperties (list) --
A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.

(dict) --
Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --
The game property identifier.

Value (string) --
The game property value.





GameSessionData (string) --
A set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.

BackfillMode (string) --
The method used to backfill game sessions created with this matchmaking configuration. MANUAL indicates that the game makes backfill requests or does not use the match backfill feature. AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever a game session has one or more open slots. Learn more about manual and automatic backfill in Backfill Existing Games with FlexMatch .









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.LimitExceededException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException
GameLift.Client.exceptions.TaggingFailedException


    :return: {
        'Configuration': {
            'Name': 'string',
            'ConfigurationArn': 'string',
            'Description': 'string',
            'GameSessionQueueArns': [
                'string',
            ],
            'RequestTimeoutSeconds': 123,
            'AcceptanceTimeoutSeconds': 123,
            'AcceptanceRequired': True|False,
            'RuleSetName': 'string',
            'RuleSetArn': 'string',
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
            'GameSessionData': 'string',
            'BackfillMode': 'AUTOMATIC'|'MANUAL'
        }
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
    
    Description (string) -- A human-readable description of the matchmaking configuration.
    GameSessionQueueArns (list) -- [REQUIRED]
    Amazon Resource Name (ARN ) that is assigned to a GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any Region.
    
    (string) --
    
    
    RequestTimeoutSeconds (integer) -- [REQUIRED]
    The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.
    
    AcceptanceTimeoutSeconds (integer) -- The length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
    AcceptanceRequired (boolean) -- [REQUIRED]
    A flag that determines whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE .
    
    RuleSetName (string) -- [REQUIRED]
    A unique identifier for a matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.
    
    NotificationTarget (string) -- An SNS topic ARN that is set up to receive matchmaking notifications.
    AdditionalPlayerCount (integer) -- The number of player slots in a match to keep open for future players. For example, assume that the configuration\'s rule set specifies a match for a single 12-person team. If the additional player count is set to 2, only 10 players are initially selected for the match.
    CustomEventData (string) -- Information to be added to all events related to this matchmaking configuration.
    GameProperties (list) -- A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.
    
    (dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .
    
    Key (string) -- [REQUIRED]The game property identifier.
    
    Value (string) -- [REQUIRED]The game property value.
    
    
    
    
    
    GameSessionData (string) -- A set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.
    BackfillMode (string) -- The method used to backfill game sessions that are created with this matchmaking configuration. Specify MANUAL when your game manages backfill requests manually or does not use the match backfill feature. Specify AUTOMATIC to have GameLift create a  StartMatchBackfill request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in Backfill Existing Games with FlexMatch .
    Tags (list) -- A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use  TagResource ,  UntagResource , and  ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
    
    (dict) --A label that can be assigned to a GameLift resource.
    
    Learn moreTagging AWS Resources in the AWS General Reference
    AWS Tagging Strategies
    Related operations
    
    
    TagResource
    UntagResource
    ListTagsForResource
    
    
    Key (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.
    
    Value (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.
    
    
    
    
    
    
    """
    pass

def create_matchmaking_rule_set(Name=None, RuleSetBody=None, Tags=None):
    """
    Creates a new rule set for FlexMatch matchmaking. A rule set describes the type of match to create, such as the number and size of teams. It also sets the parameters for acceptable player matches, such as minimum skill level or character type. A rule set is used by a  MatchmakingConfiguration .
    To create a matchmaking rule set, provide unique rule set name and the rule set body in JSON format. Rule sets must be defined in the same Region as the matchmaking configuration they are used with.
    Since matchmaking rule sets cannot be edited, it is a good idea to check the rule set syntax using  ValidateMatchmakingRuleSet before creating a new rule set.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_matchmaking_rule_set(
        Name='string',
        RuleSetBody='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA unique identifier for a matchmaking rule set. A matchmaking configuration identifies the rule set it uses by this name value. Note that the rule set name is different from the optional name field in the rule set body.\n

    :type RuleSetBody: string
    :param RuleSetBody: [REQUIRED]\nA collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.\n

    :type Tags: list
    :param Tags: A list of labels to assign to the new matchmaking rule set resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use TagResource , UntagResource , and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.\n\n(dict) --A label that can be assigned to a GameLift resource.\n\nLearn moreTagging AWS Resources in the AWS General Reference\nAWS Tagging Strategies\nRelated operations\n\n\nTagResource\nUntagResource\nListTagsForResource\n\n\nKey (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.\n\nValue (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'RuleSet': {
        'RuleSetName': 'string',
        'RuleSetArn': 'string',
        'RuleSetBody': 'string',
        'CreationTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

RuleSet (dict) --
The newly created matchmaking rule set.

RuleSetName (string) --
A unique identifier for a matchmaking rule set

RuleSetArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift matchmaking rule set resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift rule set ARN, the resource ID matches the RuleSetName value.

RuleSetBody (string) --
A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.

CreationTime (datetime) --
The time stamp indicating when this data object was created. The format is a number expressed in Unix time as milliseconds (for example "1469498468.057").









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException
GameLift.Client.exceptions.TaggingFailedException


    :return: {
        'RuleSet': {
            'RuleSetName': 'string',
            'RuleSetArn': 'string',
            'RuleSetBody': 'string',
            'CreationTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CreateMatchmakingConfiguration
    DescribeMatchmakingConfigurations
    UpdateMatchmakingConfiguration
    DeleteMatchmakingConfiguration
    CreateMatchmakingRuleSet
    DescribeMatchmakingRuleSets
    ValidateMatchmakingRuleSet
    DeleteMatchmakingRuleSet
    
    """
    pass

def create_player_session(GameSessionId=None, PlayerId=None, PlayerData=None):
    """
    Reserves an open player slot in an active game session. Before a player can be added, a game session must have an ACTIVE status, have a creation policy of ALLOW_ALL , and have an open player slot. To add a group of players to a game session, use  CreatePlayerSessions . When the player connects to the game server and references a player session ID, the game server contacts the Amazon GameLift service to validate the player reservation and accept the player.
    To create a player session, specify a game session ID, player ID, and optionally a string of player data. If successful, a slot is reserved in the game session for the player and a new  PlayerSession object is returned. Player sessions cannot be updated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_player_session(
        GameSessionId='string',
        PlayerId='string',
        PlayerData='string'
    )
    
    
    :type GameSessionId: string
    :param GameSessionId: [REQUIRED]\nA unique identifier for the game session to add a player to.\n

    :type PlayerId: string
    :param PlayerId: [REQUIRED]\nA unique identifier for a player. Player IDs are developer-defined.\n

    :type PlayerData: string
    :param PlayerData: Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.

    :rtype: dict

ReturnsResponse Syntax
{
    'PlayerSession': {
        'PlayerSessionId': 'string',
        'PlayerId': 'string',
        'GameSessionId': 'string',
        'FleetId': 'string',
        'FleetArn': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'TerminationTime': datetime(2015, 1, 1),
        'Status': 'RESERVED'|'ACTIVE'|'COMPLETED'|'TIMEDOUT',
        'IpAddress': 'string',
        'DnsName': 'string',
        'Port': 123,
        'PlayerData': 'string'
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

PlayerSession (dict) --
Object that describes the newly created player session record.

PlayerSessionId (string) --
A unique identifier for a player session.

PlayerId (string) --
A unique identifier for a player that is associated with this player session.

GameSessionId (string) --
A unique identifier for the game session that the player session is connected to.

FleetId (string) --
A unique identifier for a fleet that the player\'s game session is running on.

FleetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift fleet that the player\'s game session is running on.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

TerminationTime (datetime) --
Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

Status (string) --
Current status of the player session.
Possible player session statuses include the following:

RESERVED -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.
ACTIVE -- The player has been validated by the server process and is currently connected.
COMPLETED -- The player connection has been dropped.
TIMEDOUT -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).


IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift server process, an app needs both the IP address and port number.

PlayerData (string) --
Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.









Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidGameSessionStatusException
GameLift.Client.exceptions.GameSessionFullException
GameLift.Client.exceptions.TerminalRoutingStrategyException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException


    :return: {
        'PlayerSession': {
            'PlayerSessionId': 'string',
            'PlayerId': 'string',
            'GameSessionId': 'string',
            'FleetId': 'string',
            'FleetArn': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TerminationTime': datetime(2015, 1, 1),
            'Status': 'RESERVED'|'ACTIVE'|'COMPLETED'|'TIMEDOUT',
            'IpAddress': 'string',
            'DnsName': 'string',
            'Port': 123,
            'PlayerData': 'string'
        }
    }
    
    
    :returns: 
    GameSessionId (string) -- [REQUIRED]
    A unique identifier for the game session to add a player to.
    
    PlayerId (string) -- [REQUIRED]
    A unique identifier for a player. Player IDs are developer-defined.
    
    PlayerData (string) -- Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.
    
    """
    pass

def create_player_sessions(GameSessionId=None, PlayerIds=None, PlayerDataMap=None):
    """
    Reserves open slots in a game session for a group of players. Before players can be added, a game session must have an ACTIVE status, have a creation policy of ALLOW_ALL , and have an open player slot. To add a single player to a game session, use  CreatePlayerSession . When a player connects to the game server and references a player session ID, the game server contacts the Amazon GameLift service to validate the player reservation and accept the player.
    To create player sessions, specify a game session ID, a list of player IDs, and optionally a set of player data strings. If successful, a slot is reserved in the game session for each player and a set of new  PlayerSession objects is returned. Player sessions cannot be updated.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param GameSessionId: [REQUIRED]\nA unique identifier for the game session to add players to.\n

    :type PlayerIds: list
    :param PlayerIds: [REQUIRED]\nList of unique identifiers for the players to be added.\n\n(string) --\n\n

    :type PlayerDataMap: dict
    :param PlayerDataMap: Map of string pairs, each specifying a player ID and a set of developer-defined information related to the player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game. Player data strings for player IDs not included in the PlayerIds parameter are ignored.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'PlayerSessions': [
        {
            'PlayerSessionId': 'string',
            'PlayerId': 'string',
            'GameSessionId': 'string',
            'FleetId': 'string',
            'FleetArn': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TerminationTime': datetime(2015, 1, 1),
            'Status': 'RESERVED'|'ACTIVE'|'COMPLETED'|'TIMEDOUT',
            'IpAddress': 'string',
            'DnsName': 'string',
            'Port': 123,
            'PlayerData': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

PlayerSessions (list) --
A collection of player session objects created for the added players.

(dict) --
Properties describing a player session. Player session objects are created either by creating a player session for a specific game session, or as part of a game session placement. A player session represents either a player reservation for a game session (status RESERVED ) or actual player activity in a game session (status ACTIVE ). A player session object (including player data) is automatically passed to a game session when the player connects to the game session and is validated.
When a player disconnects, the player session status changes to COMPLETED . Once the session ends, the player session object is retained for 30 days and then removed.

CreatePlayerSession
CreatePlayerSessions
DescribePlayerSessions
Game session placements
StartGameSessionPlacement
DescribeGameSessionPlacement
StopGameSessionPlacement




PlayerSessionId (string) --
A unique identifier for a player session.

PlayerId (string) --
A unique identifier for a player that is associated with this player session.

GameSessionId (string) --
A unique identifier for the game session that the player session is connected to.

FleetId (string) --
A unique identifier for a fleet that the player\'s game session is running on.

FleetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift fleet that the player\'s game session is running on.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

TerminationTime (datetime) --
Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

Status (string) --
Current status of the player session.
Possible player session statuses include the following:

RESERVED -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.
ACTIVE -- The player has been validated by the server process and is currently connected.
COMPLETED -- The player connection has been dropped.
TIMEDOUT -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).


IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift server process, an app needs both the IP address and port number.

PlayerData (string) --
Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.











Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidGameSessionStatusException
GameLift.Client.exceptions.GameSessionFullException
GameLift.Client.exceptions.TerminalRoutingStrategyException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException


    :return: {
        'PlayerSessions': [
            {
                'PlayerSessionId': 'string',
                'PlayerId': 'string',
                'GameSessionId': 'string',
                'FleetId': 'string',
                'FleetArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TerminationTime': datetime(2015, 1, 1),
                'Status': 'RESERVED'|'ACTIVE'|'COMPLETED'|'TIMEDOUT',
                'IpAddress': 'string',
                'DnsName': 'string',
                'Port': 123,
                'PlayerData': 'string'
            },
        ]
    }
    
    
    :returns: 
    GameSessionId (string) -- [REQUIRED]
    A unique identifier for the game session to add players to.
    
    PlayerIds (list) -- [REQUIRED]
    List of unique identifiers for the players to be added.
    
    (string) --
    
    
    PlayerDataMap (dict) -- Map of string pairs, each specifying a player ID and a set of developer-defined information related to the player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game. Player data strings for player IDs not included in the PlayerIds parameter are ignored.
    
    (string) --
    (string) --
    
    
    
    
    
    """
    pass

def create_script(Name=None, Version=None, StorageLocation=None, ZipFile=None, Tags=None):
    """
    Creates a new script record for your Realtime Servers script. Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Realtime Servers fleet to host your game sessions. Script logic is executed during an active game session.
    To create a new script record, specify a script name and provide the script file(s). The script files and all dependencies must be zipped into a single file. You can pull the zip file from either of these locations:
    If the call is successful, a new script record is created with a unique script ID. If the script file is provided as a local file, the file is uploaded to an Amazon GameLift-owned S3 bucket and the script record\'s storage location reflects this location. If the script file is provided as an S3 bucket, Amazon GameLift accesses the file at this storage location as needed for deployment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_script(
        Name='string',
        Version='string',
        StorageLocation={
            'Bucket': 'string',
            'Key': 'string',
            'RoleArn': 'string',
            'ObjectVersion': 'string'
        },
        ZipFile=b'bytes',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: A descriptive label that is associated with a script. Script names do not need to be unique. You can use UpdateScript to change this value later.

    :type Version: string
    :param Version: The version that is associated with a build or script. Version strings do not need to be unique. You can use UpdateScript to change this value later.

    :type StorageLocation: dict
    :param StorageLocation: The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the 'key'), and a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ObjectVersion parameter to specify an earlier version.\n\nBucket (string) --An S3 bucket identifier. This is the name of the S3 bucket.\n\nKey (string) --The name of the zip file that contains the build files or script files.\n\nRoleArn (string) --The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access the S3 bucket.\n\nObjectVersion (string) --The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.\n\n\n

    :type ZipFile: bytes
    :param ZipFile: A data object containing your Realtime scripts and dependencies as a zip file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.\nWhen using the AWS CLI tool to create a script, this parameter is set to the zip file name. It must be prepended with the string 'fileb://' to indicate that the file data is a binary object. For example: --zip-file fileb://myRealtimeScript.zip .\n

    :type Tags: list
    :param Tags: A list of labels to assign to the new script resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use TagResource , UntagResource , and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.\n\n(dict) --A label that can be assigned to a GameLift resource.\n\nLearn moreTagging AWS Resources in the AWS General Reference\nAWS Tagging Strategies\nRelated operations\n\n\nTagResource\nUntagResource\nListTagsForResource\n\n\nKey (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.\n\nValue (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Script': {
        'ScriptId': 'string',
        'ScriptArn': 'string',
        'Name': 'string',
        'Version': 'string',
        'SizeOnDisk': 123,
        'CreationTime': datetime(2015, 1, 1),
        'StorageLocation': {
            'Bucket': 'string',
            'Key': 'string',
            'RoleArn': 'string',
            'ObjectVersion': 'string'
        }
    }
}


Response Structure

(dict) --

Script (dict) --
The newly created script record with a unique script ID and ARN. The new script\'s storage location reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your account, the storage location reflects the information that was provided in the CreateScript request; (2) If the script file was uploaded from a local zip file, the storage location reflects an S3 location controls by the Amazon GameLift service.

ScriptId (string) --
A unique identifier for a Realtime script

ScriptArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift script resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift script ARN, the resource ID matches the ScriptId value.

Name (string) --
A descriptive label that is associated with a script. Script names do not need to be unique.

Version (string) --
The version that is associated with a build or script. Version strings do not need to be unique.

SizeOnDisk (integer) --
The file size of the uploaded Realtime script, expressed in bytes. When files are uploaded from an S3 location, this value remains at "0".

CreationTime (datetime) --
A time stamp indicating when this data object was created. The format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

StorageLocation (dict) --
The location in S3 where build or script files are stored for access by Amazon GameLift. This location is specified in  CreateBuild ,  CreateScript , and  UpdateScript requests.

Bucket (string) --
An S3 bucket identifier. This is the name of the S3 bucket.

Key (string) --
The name of the zip file that contains the build files or script files.

RoleArn (string) --
The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access the S3 bucket.

ObjectVersion (string) --
The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.











Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.TaggingFailedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'Script': {
            'ScriptId': 'string',
            'ScriptArn': 'string',
            'Name': 'string',
            'Version': 'string',
            'SizeOnDisk': 123,
            'CreationTime': datetime(2015, 1, 1),
            'StorageLocation': {
                'Bucket': 'string',
                'Key': 'string',
                'RoleArn': 'string',
                'ObjectVersion': 'string'
            }
        }
    }
    
    
    :returns: 
    CreateScript
    ListScripts
    DescribeScript
    UpdateScript
    DeleteScript
    
    """
    pass

def create_vpc_peering_authorization(GameLiftAwsAccountId=None, PeerVpcId=None):
    """
    Requests authorization to create or delete a peer connection between the VPC for your Amazon GameLift fleet and a virtual private cloud (VPC) in your AWS account. VPC peering enables the game servers on your fleet to communicate directly with other AWS resources. Once you\'ve received authorization, call  CreateVpcPeeringConnection to establish the peering connection. For more information, see VPC Peering with Amazon GameLift Fleets .
    You can peer with VPCs that are owned by any AWS account you have access to, including the account that you use to manage your Amazon GameLift fleets. You cannot peer with VPCs that are in different Regions.
    To request authorization to create a connection, call this operation from the AWS account with the VPC that you want to peer to your Amazon GameLift fleet. For example, to enable your game servers to retrieve data from a DynamoDB table, use the account that manages that DynamoDB resource. Identify the following values: (1) The ID of the VPC that you want to peer with, and (2) the ID of the AWS account that you use to manage Amazon GameLift. If successful, VPC peering is authorized for the specified VPC.
    To request authorization to delete a connection, call this operation from the AWS account with the VPC that is peered with your Amazon GameLift fleet. Identify the following values: (1) VPC ID that you want to delete the peering connection for, and (2) ID of the AWS account that you use to manage Amazon GameLift.
    The authorization remains valid for 24 hours unless it is canceled by a call to  DeleteVpcPeeringAuthorization . You must create or delete the peering connection while the authorization is valid.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_vpc_peering_authorization(
        GameLiftAwsAccountId='string',
        PeerVpcId='string'
    )
    
    
    :type GameLiftAwsAccountId: string
    :param GameLiftAwsAccountId: [REQUIRED]\nA unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.\n

    :type PeerVpcId: string
    :param PeerVpcId: [REQUIRED]\nA unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'VpcPeeringAuthorization': {
        'GameLiftAwsAccountId': 'string',
        'PeerVpcAwsAccountId': 'string',
        'PeerVpcId': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'ExpirationTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

VpcPeeringAuthorization (dict) --
Details on the requested VPC peering authorization, including expiration.

GameLiftAwsAccountId (string) --
A unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.

PeerVpcAwsAccountId (string) --

PeerVpcId (string) --
A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .

CreationTime (datetime) --
Time stamp indicating when this authorization was issued. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

ExpirationTime (datetime) --
Time stamp indicating when this authorization expires (24 hours after issuance). Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").









Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


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
    A unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
    
    PeerVpcId (string) -- [REQUIRED]
    A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .
    
    
    """
    pass

def create_vpc_peering_connection(FleetId=None, PeerVpcAwsAccountId=None, PeerVpcId=None):
    """
    Establishes a VPC peering connection between a virtual private cloud (VPC) in an AWS account with the VPC for your Amazon GameLift fleet. VPC peering enables the game servers on your fleet to communicate directly with other AWS resources. You can peer with VPCs in any AWS account that you have access to, including the account that you use to manage your Amazon GameLift fleets. You cannot peer with VPCs that are in different Regions. For more information, see VPC Peering with Amazon GameLift Fleets .
    Before calling this operation to establish the peering connection, you first need to call  CreateVpcPeeringAuthorization and identify the VPC you want to peer with. Once the authorization for the specified VPC is issued, you have 24 hours to establish the connection. These two operations handle all tasks necessary to peer the two VPCs, including acceptance, updating routing tables, etc.
    To establish the connection, call this operation from the AWS account that is used to manage the Amazon GameLift fleets. Identify the following values: (1) The ID of the fleet you want to be enable a VPC peering connection for; (2) The AWS account with the VPC that you want to peer with; and (3) The ID of the VPC you want to peer with. This operation is asynchronous. If successful, a  VpcPeeringConnection request is created. You can use continuous polling to track the request\'s status using  DescribeVpcPeeringConnections , or by monitoring fleet events for success or failure using  DescribeFleetEvents .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_vpc_peering_connection(
        FleetId='string',
        PeerVpcAwsAccountId='string',
        PeerVpcId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet. You can use either the fleet ID or ARN value. This tells Amazon GameLift which GameLift VPC to peer with.\n

    :type PeerVpcAwsAccountId: string
    :param PeerVpcAwsAccountId: [REQUIRED]\nA unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your Account ID in the AWS Management Console under account settings.\n

    :type PeerVpcId: string
    :param PeerVpcId: [REQUIRED]\nA unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


    :return: {}
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet. You can use either the fleet ID or ARN value. This tells Amazon GameLift which GameLift VPC to peer with.
    
    PeerVpcAwsAccountId (string) -- [REQUIRED]
    A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your Account ID in the AWS Management Console under account settings.
    
    PeerVpcId (string) -- [REQUIRED]
    A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .
    
    
    """
    pass

def delete_alias(AliasId=None):
    """
    Deletes an alias. This action removes all record of the alias. Game clients attempting to access a server process using the deleted alias receive an error. To delete an alias, specify the alias ID to be deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_alias(
        AliasId='string'
    )
    
    
    :type AliasId: string
    :param AliasId: [REQUIRED]\nA unique identifier of the alias that you want to delete. You can use either the alias ID or ARN value.\n

    :returns: 
    GameLift.Client.exceptions.UnauthorizedException
    GameLift.Client.exceptions.NotFoundException
    GameLift.Client.exceptions.InvalidRequestException
    GameLift.Client.exceptions.TaggingFailedException
    GameLift.Client.exceptions.InternalServiceException
    
    """
    pass

def delete_build(BuildId=None):
    """
    Deletes a build. This action permanently deletes the build resource and any uploaded build files. Deleting a build does not affect the status of any active fleets using the build, but you can no longer create new fleets with the deleted build.
    To delete a build, specify the build ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_build(
        BuildId='string'
    )
    
    
    :type BuildId: string
    :param BuildId: [REQUIRED]\nA unique identifier for a build to delete. You can use either the build ID or ARN value.\n

    :returns: 
    GameLift.Client.exceptions.UnauthorizedException
    GameLift.Client.exceptions.NotFoundException
    GameLift.Client.exceptions.InternalServiceException
    GameLift.Client.exceptions.TaggingFailedException
    GameLift.Client.exceptions.InvalidRequestException
    
    """
    pass

def delete_fleet(FleetId=None):
    """
    Deletes everything related to a fleet. Before deleting a fleet, you must set the fleet\'s desired capacity to zero. See  UpdateFleetCapacity .
    If the fleet being deleted has a VPC peering connection, you first need to get a valid authorization (good for 24 hours) by calling  CreateVpcPeeringAuthorization . You do not need to explicitly delete the VPC peering connection--this is done as part of the delete fleet process.
    This action removes the fleet and its resources. Once a fleet is deleted, you can no longer use any of the resource in that fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_fleet(
        FleetId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to be deleted. You can use either the fleet ID or ARN value.\n

    :returns: 
    GameLift.Client.exceptions.NotFoundException
    GameLift.Client.exceptions.InternalServiceException
    GameLift.Client.exceptions.InvalidFleetStatusException
    GameLift.Client.exceptions.UnauthorizedException
    GameLift.Client.exceptions.InvalidRequestException
    GameLift.Client.exceptions.TaggingFailedException
    
    """
    pass

def delete_game_server_group(GameServerGroupName=None, DeleteOption=None):
    """
    Terminates a game server group and permanently deletes the game server group record. You have several options for how these resources are impacted when deleting the game server group. Depending on the type of delete action selected, this action may affect three types of resources: the game server group, the corresponding Auto Scaling group, and all game servers currently running in the group.
    To delete a game server group, identify the game server group to delete and specify the type of delete action to initiate. Game server groups can only be deleted if they are in ACTIVE or ERROR status.
    If the delete request is successful, a series of actions are kicked off. The game server group status is changed to DELETE_SCHEDULED, which prevents new game servers from being registered and stops autoscaling activity. Once all game servers in the game server group are de-registered, GameLift FleetIQ can begin deleting resources. If any of the delete actions fail, the game server group is placed in ERROR status.
    GameLift FleetIQ emits delete events to Amazon CloudWatch.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_game_server_group(
        GameServerGroupName='string',
        DeleteOption='SAFE_DELETE'|'FORCE_DELETE'|'RETAIN'
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nThe unique identifier of the game server group to delete. Use either the GameServerGroup name or ARN value.\n

    :type DeleteOption: string
    :param DeleteOption: The type of delete to perform. Options include:\n\nSAFE_DELETE \xe2\x80\x93 Terminates the game server group and EC2 Auto Scaling group only when it has no game servers that are in IN_USE status.\nFORCE_DELETE \xe2\x80\x93 Terminates the game server group, including all active game servers regardless of their utilization status, and the EC2 Auto Scaling group.\nRETAIN \xe2\x80\x93 Does a safe delete of the game server group but retains the EC2 Auto Scaling group as is.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServerGroup': {
        'GameServerGroupName': 'string',
        'GameServerGroupArn': 'string',
        'RoleArn': 'string',
        'InstanceDefinitions': [
            {
                'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'WeightedCapacity': 'string'
            },
        ],
        'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
        'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
        'AutoScalingGroupArn': 'string',
        'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
        'StatusReason': 'string',
        'SuspendedActions': [
            'REPLACE_INSTANCE_TYPES',
        ],
        'CreationTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

GameServerGroup (dict) --
An object that describes the deleted game server group resource, with status updated to DELETE_SCHEDULED.

GameServerGroupName (string) --
A developer-defined identifier for the game server group. The name is unique per Region per AWS account.

GameServerGroupArn (string) --
A generated unique ID for the game server group.

RoleArn (string) --
The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups. The submitted role is validated to ensure that it contains the necessary permissions for game server groups.

InstanceDefinitions (list) --
The set of EC2 instance types that GameLift FleetIQ can use when rebalancing and autoscaling instances in the group.

(dict) --

This data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.

An allowed instance type for your game server group. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

InstanceType (string) --
An EC2 instance type designation.

WeightedCapacity (string) --
Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by GameLift FleetIQ to calculate the instance type\'s cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see Instance Weighting in the Amazon EC2 Auto Scaling User Guide . Default value is "1".





BalancingStrategy (string) --
The fallback balancing method to use for the game server group when Spot instances in a Region become unavailable or are not viable for game hosting. Once triggered, this method remains active until Spot instances can once again be used. Method options include:

SPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.
SPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.


GameServerProtectionPolicy (string) --
A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running may be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see  DeleteGameServerGroup ). An exception to this is Spot Instances, which may be terminated by AWS regardless of protection status.

AutoScalingGroupArn (string) --
A generated unique ID for the EC2 Auto Scaling group with is associated with this game server group.

Status (string) --
The current status of the game server group. Possible statuses include:

NEW - GameLift FleetIQ has validated the CreateGameServerGroup() request.
ACTIVATING - GameLift FleetIQ is setting up a game server group, which includes creating an autoscaling group in your AWS account.
ACTIVE - The game server group has been successfully created.
DELETE_SCHEDULED - A request to delete the game server group has been received.
DELETING - GameLift FleetIQ has received a valid DeleteGameServerGroup() request and is processing it. GameLift FleetIQ must first complete and release hosts before it deletes the autoscaling group and the game server group.
DELETED - The game server group has been successfully deleted.
ERROR - The asynchronous processes of activating or deleting a game server group has failed, resulting in an error state.


StatusReason (string) --
Additional information about the current game server group status. This information may provide additional insight on groups that in ERROR status.

SuspendedActions (list) --
A list of activities that are currently suspended for this game server group. If this property is empty, all activities are occurring.

(string) --


CreationTime (datetime) --
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --
A time stamp indicating when this game server group was last updated.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'GameServerGroup': {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'RoleArn': 'string',
            'InstanceDefinitions': [
                {
                    'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                    'WeightedCapacity': 'string'
                },
            ],
            'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
            'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
            'AutoScalingGroupArn': 'string',
            'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
            'StatusReason': 'string',
            'SuspendedActions': [
                'REPLACE_INSTANCE_TYPES',
            ],
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    GameServerGroupName (string) -- [REQUIRED]
    The unique identifier of the game server group to delete. Use either the  GameServerGroup name or ARN value.
    
    DeleteOption (string) -- The type of delete to perform. Options include:
    
    SAFE_DELETE \xe2\x80\x93 Terminates the game server group and EC2 Auto Scaling group only when it has no game servers that are in IN_USE status.
    FORCE_DELETE \xe2\x80\x93 Terminates the game server group, including all active game servers regardless of their utilization status, and the EC2 Auto Scaling group.
    RETAIN \xe2\x80\x93 Does a safe delete of the game server group but retains the EC2 Auto Scaling group as is.
    
    
    
    """
    pass

def delete_game_session_queue(Name=None):
    """
    Deletes a game session queue. This action means that any  StartGameSessionPlacement requests that reference this queue will fail. To delete a queue, specify the queue name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_game_session_queue(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA descriptive label that is associated with game session queue. Queue names must be unique within each Region. You can use either the queue ID or ARN value.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.TaggingFailedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_matchmaking_configuration(Name=None):
    """
    Permanently removes a FlexMatch matchmaking configuration. To delete, specify the configuration name. A matchmaking configuration cannot be deleted if it is being used in any active matchmaking tickets.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_matchmaking_configuration(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA unique identifier for a matchmaking configuration. You can use either the configuration name or ARN value.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException
GameLift.Client.exceptions.TaggingFailedException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_matchmaking_rule_set(Name=None):
    """
    Deletes an existing matchmaking rule set. To delete the rule set, provide the rule set name. Rule sets cannot be deleted if they are currently being used by a matchmaking configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_matchmaking_rule_set(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA unique identifier for a matchmaking rule set to be deleted. (Note: The rule set name is different from the optional 'name' field in the rule set body.) You can use either the rule set name or ARN value.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --Represents the returned data in response to a request action.




Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.TaggingFailedException


    :return: {}
    
    
    :returns: 
    CreateMatchmakingConfiguration
    DescribeMatchmakingConfigurations
    UpdateMatchmakingConfiguration
    DeleteMatchmakingConfiguration
    CreateMatchmakingRuleSet
    DescribeMatchmakingRuleSets
    ValidateMatchmakingRuleSet
    DeleteMatchmakingRuleSet
    
    """
    pass

def delete_scaling_policy(Name=None, FleetId=None):
    """
    Deletes a fleet scaling policy. This action means that the policy is no longer in force and removes all record of it. To delete a scaling policy, specify both the scaling policy name and the fleet ID it is associated with.
    To temporarily suspend scaling policies, call  StopFleetActions . This operation suspends all policies for the fleet.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_scaling_policy(
        Name='string',
        FleetId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA descriptive label that is associated with a scaling policy. Policy names do not need to be unique.\n

    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to be deleted. You can use either the fleet ID or ARN value.\n

    :returns: 
    Name (string) -- [REQUIRED]
    A descriptive label that is associated with a scaling policy. Policy names do not need to be unique.
    
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet to be deleted. You can use either the fleet ID or ARN value.
    
    
    """
    pass

def delete_script(ScriptId=None):
    """
    Deletes a Realtime script. This action permanently deletes the script record. If script files were uploaded, they are also deleted (files stored in an S3 bucket are not deleted).
    To delete a script, specify the script ID. Before deleting a script, be sure to terminate all fleets that are deployed with the script being deleted. Fleet instances periodically check for script updates, and if the script record no longer exists, the instance will go into an error state and be unable to host game sessions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_script(
        ScriptId='string'
    )
    
    
    :type ScriptId: string
    :param ScriptId: [REQUIRED]\nA unique identifier for a Realtime script to delete. You can use either the script ID or ARN value.\n

    :returns: 
    GameLift.Client.exceptions.InvalidRequestException
    GameLift.Client.exceptions.UnauthorizedException
    GameLift.Client.exceptions.NotFoundException
    GameLift.Client.exceptions.TaggingFailedException
    GameLift.Client.exceptions.InternalServiceException
    
    """
    pass

def delete_vpc_peering_authorization(GameLiftAwsAccountId=None, PeerVpcId=None):
    """
    Cancels a pending VPC peering authorization for the specified VPC. If you need to delete an existing VPC peering connection, call  DeleteVpcPeeringConnection .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_vpc_peering_authorization(
        GameLiftAwsAccountId='string',
        PeerVpcId='string'
    )
    
    
    :type GameLiftAwsAccountId: string
    :param GameLiftAwsAccountId: [REQUIRED]\nA unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.\n

    :type PeerVpcId: string
    :param PeerVpcId: [REQUIRED]\nA unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


    :return: {}
    
    
    :returns: 
    GameLiftAwsAccountId (string) -- [REQUIRED]
    A unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.
    
    PeerVpcId (string) -- [REQUIRED]
    A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .
    
    
    """
    pass

def delete_vpc_peering_connection(FleetId=None, VpcPeeringConnectionId=None):
    """
    Removes a VPC peering connection. To delete the connection, you must have a valid authorization for the VPC peering connection that you want to delete. You can check for an authorization by calling  DescribeVpcPeeringAuthorizations or request a new one using  CreateVpcPeeringAuthorization .
    Once a valid authorization exists, call this operation from the AWS account that is used to manage the Amazon GameLift fleets. Identify the connection to delete by the connection ID and fleet ID. If successful, the connection is removed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_vpc_peering_connection(
        FleetId='string',
        VpcPeeringConnectionId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet. This fleet specified must match the fleet referenced in the VPC peering connection record. You can use either the fleet ID or ARN value.\n

    :type VpcPeeringConnectionId: string
    :param VpcPeeringConnectionId: [REQUIRED]\nA unique identifier for a VPC peering connection. This value is included in the VpcPeeringConnection object, which can be retrieved by calling DescribeVpcPeeringConnections .\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


    :return: {}
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet. This fleet specified must match the fleet referenced in the VPC peering connection record. You can use either the fleet ID or ARN value.
    
    VpcPeeringConnectionId (string) -- [REQUIRED]
    A unique identifier for a VPC peering connection. This value is included in the  VpcPeeringConnection object, which can be retrieved by calling  DescribeVpcPeeringConnections .
    
    
    """
    pass

def deregister_game_server(GameServerGroupName=None, GameServerId=None):
    """
    Removes the game server resource from the game server group. As a result of this action, the de-registered game server can no longer be claimed and will not returned in a list of active game servers.
    To de-register a game server, specify the game server group and game server ID. If successful, this action emits a CloudWatch event with termination time stamp and reason.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deregister_game_server(
        GameServerGroupName='string',
        GameServerId='string'
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nAn identifier for the game server group where the game server to be de-registered is running. Use either the GameServerGroup name or ARN value.\n

    :type GameServerId: string
    :param GameServerId: [REQUIRED]\nThe identifier for the game server to be de-registered.\n

    :returns: 
    GameServerGroupName (string) -- [REQUIRED]
    An identifier for the game server group where the game server to be de-registered is running. Use either the  GameServerGroup name or ARN value.
    
    GameServerId (string) -- [REQUIRED]
    The identifier for the game server to be de-registered.
    
    
    """
    pass

def describe_alias(AliasId=None):
    """
    Retrieves properties for an alias. This operation returns all alias metadata and settings. To get an alias\'s target fleet ID only, use ResolveAlias .
    To get alias properties, specify the alias ID. If successful, the requested alias record is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_alias(
        AliasId='string'
    )
    
    
    :type AliasId: string
    :param AliasId: [REQUIRED]\nThe unique identifier for the fleet alias that you want to retrieve. You can use either the alias ID or ARN value.\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --Represents the returned data in response to a request action.

Alias (dict) --The requested alias resource.

AliasId (string) --A unique identifier for an alias. Alias IDs are unique within a Region.

Name (string) --A descriptive label that is associated with an alias. Alias names do not need to be unique.

AliasArn (string) --Amazon Resource Name (ARN ) that is assigned to a GameLift alias resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift alias ARN, the resource ID matches the alias ID value.

Description (string) --A human-readable description of an alias.

RoutingStrategy (dict) --The routing configuration, including routing type and fleet target, for the alias.

Type (string) --The type of routing strategy for the alias.
Possible routing types include the following:

SIMPLE - The alias resolves to one specific fleet. Use this type when routing to active fleets.
TERMINAL - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.


FleetId (string) --The unique identifier for a fleet that the alias points to. This value is the fleet ID, not the fleet ARN.

Message (string) --The message text to be used with a terminal routing strategy.



CreationTime (datetime) --A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --The time that this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").








Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


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
    SIMPLE - The alias resolves to one specific fleet. Use this type when routing to active fleets.
    TERMINAL - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
    
    """
    pass

def describe_build(BuildId=None):
    """
    Retrieves properties for a custom game build. To request a build resource, specify a build ID. If successful, an object containing the build properties is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_build(
        BuildId='string'
    )
    
    
    :type BuildId: string
    :param BuildId: [REQUIRED]\nA unique identifier for a build to retrieve properties for. You can use either the build ID or ARN value.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Build': {
        'BuildId': 'string',
        'BuildArn': 'string',
        'Name': 'string',
        'Version': 'string',
        'Status': 'INITIALIZED'|'READY'|'FAILED',
        'SizeOnDisk': 123,
        'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
        'CreationTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --Represents the returned data in response to a request action.

Build (dict) --Set of properties describing the requested build.

BuildId (string) --A unique identifier for a build.

BuildArn (string) --Amazon Resource Name (ARN ) that is assigned to a GameLift build resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift build ARN, the resource ID matches the BuildId value.

Name (string) --A descriptive label that is associated with a build. Build names do not need to be unique. It can be set using  CreateBuild or  UpdateBuild .

Version (string) --Version information that is associated with a build or script. Version strings do not need to be unique. This value can be set using  CreateBuild or  UpdateBuild .

Status (string) --Current status of the build.
Possible build statuses include the following:

INITIALIZED -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
READY -- The game build has been successfully uploaded. You can now create new fleets for this build.
FAILED -- The game build upload failed. You cannot create new fleets for this build.


SizeOnDisk (integer) --File size of the uploaded game build, expressed in bytes. When the build status is INITIALIZED , this value is 0.

OperatingSystem (string) --Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.

CreationTime (datetime) --Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").








Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'Build': {
            'BuildId': 'string',
            'BuildArn': 'string',
            'Name': 'string',
            'Version': 'string',
            'Status': 'INITIALIZED'|'READY'|'FAILED',
            'SizeOnDisk': 123,
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
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
    To learn more about the capabilities of each instance type, see Amazon EC2 Instance Types . Note that the instance types offered may vary depending on the region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_ec2_instance_limits(
        EC2InstanceType='t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge'
    )
    
    
    :type EC2InstanceType: string
    :param EC2InstanceType: Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions. Leave this parameter blank to retrieve limits for all types.

    :rtype: dict
ReturnsResponse Syntax{
    'EC2InstanceLimits': [
        {
            'EC2InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
            'CurrentInstances': 123,
            'InstanceLimit': 123
        },
    ]
}


Response Structure

(dict) --Represents the returned data in response to a request action.

EC2InstanceLimits (list) --The maximum number of instances for the specified instance type.

(dict) --The maximum number of instances allowed based on the Amazon Elastic Compute Cloud (Amazon EC2) instance type. Instance limits can be retrieved by calling  DescribeEC2InstanceLimits .

EC2InstanceType (string) --Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.

CurrentInstances (integer) --Number of instances of the specified type that are currently in use by this AWS account.

InstanceLimit (integer) --Number of instances allowed.










Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'EC2InstanceLimits': [
            {
                'EC2InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'CurrentInstances': 123,
                'InstanceLimit': 123
            },
        ]
    }
    
    
    :returns: 
    CreateFleet
    ListFleets
    DeleteFleet
    DescribeFleetAttributes
    UpdateFleetAttributes
    StartFleetActions or  StopFleetActions
    
    """
    pass

def describe_fleet_attributes(FleetIds=None, Limit=None, NextToken=None):
    """
    Retrieves core properties, including configuration, status, and metadata, for a fleet.
    To get attributes for one or more fleets, provide a list of fleet IDs or fleet ARNs. To get attributes for all fleets, do not specify a fleet identifier. When requesting attributes for multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  FleetAttributes object is returned for each fleet requested, unless the fleet identifier is not found.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_fleet_attributes(
        FleetIds=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetIds: list
    :param FleetIds: A list of unique fleet identifiers to retrieve attributes for. You can use either the fleet ID or ARN value. To retrieve attributes for all current fleets, do not include this parameter. If the list of fleet identifiers includes fleets that don\'t currently exist, the request succeeds but no attributes for that fleet are returned.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :rtype: dict

ReturnsResponse Syntax
{
    'FleetAttributes': [
        {
            'FleetId': 'string',
            'FleetArn': 'string',
            'FleetType': 'ON_DEMAND'|'SPOT',
            'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
            'Description': 'string',
            'Name': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TerminationTime': datetime(2015, 1, 1),
            'Status': 'NEW'|'DOWNLOADING'|'VALIDATING'|'BUILDING'|'ACTIVATING'|'ACTIVE'|'DELETING'|'ERROR'|'TERMINATED',
            'BuildId': 'string',
            'BuildArn': 'string',
            'ScriptId': 'string',
            'ScriptArn': 'string',
            'ServerLaunchPath': 'string',
            'ServerLaunchParameters': 'string',
            'LogPaths': [
                'string',
            ],
            'NewGameSessionProtectionPolicy': 'NoProtection'|'FullProtection',
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
            'ResourceCreationLimitPolicy': {
                'NewGameSessionsPerCreator': 123,
                'PolicyPeriodInMinutes': 123
            },
            'MetricGroups': [
                'string',
            ],
            'StoppedActions': [
                'AUTO_SCALING',
            ],
            'InstanceRoleArn': 'string',
            'CertificateConfiguration': {
                'CertificateType': 'DISABLED'|'GENERATED'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

FleetAttributes (list) --
A collection of objects containing attribute metadata for each requested fleet ID. Attribute objects are returned only for fleets that currently exist.

(dict) --
General properties describing a fleet.

CreateFleet
ListFleets
DeleteFleet
DescribeFleetAttributes
UpdateFleetAttributes
StartFleetActions or  StopFleetActions


FleetId (string) --
A unique identifier for a fleet.

FleetArn (string) --
The Amazon Resource Name (ARN ) that is assigned to a GameLift fleet resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift fleet ARN, the resource ID matches the FleetId value.

FleetType (string) --
Indicates whether the fleet uses on-demand or spot instances. A spot instance in use may be interrupted with a two-minute notification.

InstanceType (string) --
EC2 instance type indicating the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. See Amazon EC2 Instance Types for detailed descriptions.

Description (string) --
Human-readable description of the fleet.

Name (string) --
A descriptive label that is associated with a fleet. Fleet names do not need to be unique.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

TerminationTime (datetime) --
Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

Status (string) --
Current status of the fleet.
Possible fleet statuses include the following:

NEW -- A new fleet has been defined and desired instances is set to 1.
DOWNLOADING/VALIDATING/BUILDING/ACTIVATING -- Amazon GameLift is setting up the new fleet, creating new instances with the game build or Realtime script and starting server processes.
ACTIVE -- Hosts can now accept game sessions.
ERROR -- An error occurred when downloading, validating, building, or activating the fleet.
DELETING -- Hosts are responding to a delete fleet request.
TERMINATED -- The fleet no longer exists.


BuildId (string) --
A unique identifier for a build.

BuildArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift build resource that is deployed on instances in this fleet. In a GameLift build ARN, the resource ID matches the BuildId value.

ScriptId (string) --
A unique identifier for a Realtime script.

ScriptArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift script resource that is deployed on instances in this fleet. In a GameLift script ARN, the resource ID matches the ScriptId value.

ServerLaunchPath (string) --
Path to a game server executable in the fleet\'s build, specified for fleets created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch paths for fleets created after this date are specified in the fleet\'s  RuntimeConfiguration .

ServerLaunchParameters (string) --
Game server launch parameters specified for fleets created before 2016-08-04 (or AWS SDK v. 0.12.16). Server launch parameters for fleets created after this date are specified in the fleet\'s  RuntimeConfiguration .

LogPaths (list) --
Location of default log files. When a server process is shut down, Amazon GameLift captures and stores any log files in this location. These logs are in addition to game session logs; see more on game session logs in the Amazon GameLift Developer Guide . If no default log path for a fleet is specified, Amazon GameLift automatically uploads logs that are stored on each instance at C:\\game\\logs (for Windows) or /local/game/logs (for Linux). Use the Amazon GameLift console to access stored logs.

(string) --


NewGameSessionProtectionPolicy (string) --
The type of game session protection to set for all new instances started in the fleet.

NoProtection -- The game session can be terminated during a scale-down event.
FullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.


OperatingSystem (string) --
Operating system of the fleet\'s computing resources. A fleet\'s operating system depends on the OS specified for the build that is deployed on this fleet.

ResourceCreationLimitPolicy (dict) --
Fleet policy to limit the number of game sessions an individual player can create over a span of time.

NewGameSessionsPerCreator (integer) --
The maximum number of game sessions that an individual can create during the policy period.

PolicyPeriodInMinutes (integer) --
The time span used in evaluating the resource creation limit policy.



MetricGroups (list) --
Names of metric groups that this fleet is included in. In Amazon CloudWatch, you can view metrics for an individual fleet or aggregated metrics for fleets that are in a fleet metric group. A fleet can be included in only one metric group at a time.

(string) --


StoppedActions (list) --
List of fleet actions that have been suspended using  StopFleetActions . This includes auto-scaling.

(string) --


InstanceRoleArn (string) --
A unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role\'s ARN from the IAM dashboard in the AWS Management Console. Learn more about using on-box credentials for your game servers at Access external resources from a game server .

CertificateConfiguration (dict) --
Indicates whether a TLS/SSL certificate was generated for the fleet.

CertificateType (string) --
Indicates whether a TLS/SSL certificate was generated for a fleet.







NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'FleetAttributes': [
            {
                'FleetId': 'string',
                'FleetArn': 'string',
                'FleetType': 'ON_DEMAND'|'SPOT',
                'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'Description': 'string',
                'Name': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TerminationTime': datetime(2015, 1, 1),
                'Status': 'NEW'|'DOWNLOADING'|'VALIDATING'|'BUILDING'|'ACTIVATING'|'ACTIVE'|'DELETING'|'ERROR'|'TERMINATED',
                'BuildId': 'string',
                'BuildArn': 'string',
                'ScriptId': 'string',
                'ScriptArn': 'string',
                'ServerLaunchPath': 'string',
                'ServerLaunchParameters': 'string',
                'LogPaths': [
                    'string',
                ],
                'NewGameSessionProtectionPolicy': 'NoProtection'|'FullProtection',
                'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
                'ResourceCreationLimitPolicy': {
                    'NewGameSessionsPerCreator': 123,
                    'PolicyPeriodInMinutes': 123
                },
                'MetricGroups': [
                    'string',
                ],
                'StoppedActions': [
                    'AUTO_SCALING',
                ],
                'InstanceRoleArn': 'string',
                'CertificateConfiguration': {
                    'CertificateType': 'DISABLED'|'GENERATED'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    FleetIds (list) -- A list of unique fleet identifiers to retrieve attributes for. You can use either the fleet ID or ARN value. To retrieve attributes for all current fleets, do not include this parameter. If the list of fleet identifiers includes fleets that don\'t currently exist, the request succeeds but no attributes for that fleet are returned.
    
    (string) --
    
    
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
    
    """
    pass

def describe_fleet_capacity(FleetIds=None, Limit=None, NextToken=None):
    """
    Retrieves the current capacity statistics for one or more fleets. These statistics present a snapshot of the fleet\'s instances and provide insight on current or imminent scaling activity. To get statistics on game hosting activity in the fleet, see  DescribeFleetUtilization .
    You can request capacity for all fleets or specify a list of one or more fleet identifiers. When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  FleetCapacity object is returned for each requested fleet ID. When a list of fleet IDs is provided, attribute objects are returned only for fleets that currently exist.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_fleet_capacity(
        FleetIds=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetIds: list
    :param FleetIds: A unique identifier for a fleet(s) to retrieve capacity information for. You can use either the fleet ID or ARN value.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :rtype: dict

ReturnsResponse Syntax
{
    'FleetCapacity': [
        {
            'FleetId': 'string',
            'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

FleetCapacity (list) --
A collection of objects containing capacity information for each requested fleet ID. Leave this parameter empty to retrieve capacity information for all fleets.

(dict) --
Information about the fleet\'s capacity. Fleet capacity is measured in EC2 instances. By default, new fleets have a capacity of one instance, but can be updated as needed. The maximum number of instances for a fleet is determined by the fleet\'s instance type.

CreateFleet
ListFleets
DeleteFleet
DescribeFleetAttributes
UpdateFleetAttributes
StartFleetActions or  StopFleetActions


FleetId (string) --
A unique identifier for a fleet.

InstanceType (string) --
Name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.

InstanceCounts (dict) --
Current status of fleet capacity.

DESIRED (integer) --
Ideal number of active instances in the fleet.

MINIMUM (integer) --
The minimum value allowed for the fleet\'s instance count.

MAXIMUM (integer) --
The maximum value allowed for the fleet\'s instance count.

PENDING (integer) --
Number of instances in the fleet that are starting but not yet active.

ACTIVE (integer) --
Actual number of active instances in the fleet.

IDLE (integer) --
Number of active instances in the fleet that are not currently hosting a game session.

TERMINATING (integer) --
Number of instances in the fleet that are no longer active but haven\'t yet been terminated.







NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'FleetCapacity': [
            {
                'FleetId': 'string',
                'InstanceType': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
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
    FleetIds (list) -- A unique identifier for a fleet(s) to retrieve capacity information for. You can use either the fleet ID or ARN value.
    
    (string) --
    
    
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
    
    """
    pass

def describe_fleet_events(FleetId=None, StartTime=None, EndTime=None, Limit=None, NextToken=None):
    """
    Retrieves entries from the specified fleet\'s event log. You can specify a time range to limit the result set. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a collection of event log entries matching the request are returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_fleet_events(
        FleetId='string',
        StartTime=datetime(2015, 1, 1),
        EndTime=datetime(2015, 1, 1),
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to get event logs for. You can use either the fleet ID or ARN value.\n

    :type StartTime: datetime
    :param StartTime: Earliest date to retrieve event logs for. If no start time is specified, this call returns entries starting from when the fleet was created to the specified end time. Format is a number expressed in Unix time as milliseconds (ex: '1469498468.057').

    :type EndTime: datetime
    :param EndTime: Most recent date to retrieve event logs for. If no end time is specified, this call returns entries from the specified start time up to the present. Format is a number expressed in Unix time as milliseconds (ex: '1469498468.057').

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

Events (list) --
A collection of objects containing event log entries for the specified fleet.

(dict) --
Log entry describing an event that involves Amazon GameLift resources (such as a fleet). In addition to tracking activity, event codes and messages can provide additional information for troubleshooting and debugging problems.

EventId (string) --
A unique identifier for a fleet event.

ResourceId (string) --
A unique identifier for an event resource, such as a fleet ID.

EventCode (string) --
The type of event being logged.

Fleet creation events (ordered by fleet creation activity):


FLEET_CREATED -- A fleet resource was successfully created with a status of NEW . Event messaging includes the fleet ID.
FLEET_STATE_DOWNLOADING -- Fleet status changed from NEW to DOWNLOADING . The compressed build has started downloading to a fleet instance for installation.
FLEET_BINARY_DOWNLOAD_FAILED -- The build failed to download to the fleet instance.
FLEET_CREATION_EXTRACTING_BUILD \xe2\x80\x93 The game server build was successfully downloaded to an instance, and the build files are now being extracted from the uploaded build and saved to an instance. Failure at this stage prevents a fleet from moving to ACTIVE status. Logs for this stage display a list of the files that are extracted and saved on the instance. Access the logs by using the URL in PreSignedLogUrl .
FLEET_CREATION_RUNNING_INSTALLER \xe2\x80\x93 The game server build files were successfully extracted, and the Amazon GameLift is now running the build\'s install script (if one is included). Failure in this stage prevents a fleet from moving to ACTIVE status. Logs for this stage list the installation steps and whether or not the install completed successfully. Access the logs by using the URL in PreSignedLogUrl .
FLEET_CREATION_VALIDATING_RUNTIME_CONFIG -- The build process was successful, and the Amazon GameLift is now verifying that the game server launch paths, which are specified in the fleet\'s runtime configuration, exist. If any listed launch path exists, Amazon GameLift tries to launch a game server process and waits for the process to report ready. Failures in this stage prevent a fleet from moving to ACTIVE status. Logs for this stage list the launch paths in the runtime configuration and indicate whether each is found. Access the logs by using the URL in PreSignedLogUrl .
FLEET_STATE_VALIDATING -- Fleet status changed from DOWNLOADING to VALIDATING .
FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND -- Validation of the runtime configuration failed because the executable specified in a launch path does not exist on the instance.
FLEET_STATE_BUILDING -- Fleet status changed from VALIDATING to BUILDING .
FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE -- Validation of the runtime configuration failed because the executable specified in a launch path failed to run on the fleet instance.
FLEET_STATE_ACTIVATING -- Fleet status changed from BUILDING to ACTIVATING .
FLEET_ACTIVATION_FAILED - The fleet failed to successfully complete one of the steps in the fleet activation process. This event code indicates that the game build was successfully downloaded to a fleet instance, built, and validated, but was not able to start a server process. Learn more at Debug Fleet Creation Issues
FLEET_STATE_ACTIVE -- The fleet\'s status changed from ACTIVATING to ACTIVE . The fleet is now ready to host game sessions.


VPC peering events:


FLEET_VPC_PEERING_SUCCEEDED -- A VPC peering connection has been established between the VPC for an Amazon GameLift fleet and a VPC in your AWS account.
FLEET_VPC_PEERING_FAILED -- A requested VPC peering connection has failed. Event details and status information (see  DescribeVpcPeeringConnections ) provide additional detail. A common reason for peering failure is that the two VPCs have overlapping CIDR blocks of IPv4 addresses. To resolve this, change the CIDR block for the VPC in your AWS account. For more information on VPC peering failures, see https://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html
FLEET_VPC_PEERING_DELETED -- A VPC peering connection has been successfully deleted.


Spot instance events:


INSTANCE_INTERRUPTED -- A spot instance was interrupted by EC2 with a two-minute notification.


Other fleet events:


FLEET_SCALING_EVENT -- A change was made to the fleet\'s capacity settings (desired instances, minimum/maximum scaling limits). Event messaging includes the new capacity settings.
FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED -- A change was made to the fleet\'s game session protection policy setting. Event messaging includes both the old and new policy setting.
FLEET_DELETED -- A request to delete a fleet was initiated.
GENERIC_EVENT -- An unspecified event has occurred.


Message (string) --
Additional information related to the event.

EventTime (datetime) --
Time stamp indicating when this event occurred. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

PreSignedLogUrl (string) --
Location of stored logs with additional detail that is related to the event. This is useful for debugging issues. The URL is valid for 15 minutes. You can also access fleet creation logs through the Amazon GameLift console.





NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException


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
    A unique identifier for a fleet to get event logs for. You can use either the fleet ID or ARN value.
    
    StartTime (datetime) -- Earliest date to retrieve event logs for. If no start time is specified, this call returns entries starting from when the fleet was created to the specified end time. Format is a number expressed in Unix time as milliseconds (ex: "1469498468.057").
    EndTime (datetime) -- Most recent date to retrieve event logs for. If no end time is specified, this call returns entries from the specified start time up to the present. Format is a number expressed in Unix time as milliseconds (ex: "1469498468.057").
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_fleet_port_settings(FleetId=None):
    """
    Retrieves a fleet\'s inbound connection permissions. Connection permissions specify the range of IP addresses and port settings that incoming traffic can use to access server processes in the fleet. Game sessions that are running on instances in the fleet use connections that fall in this range.
    To get a fleet\'s inbound connection permissions, specify the fleet\'s unique identifier. If successful, a collection of  IpPermission objects is returned for the requested fleet ID. If the requested fleet has been deleted, the result set is empty.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_fleet_port_settings(
        FleetId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to retrieve port settings for. You can use either the fleet ID or ARN value.\n

    :rtype: dict
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

InboundPermissions (list) --The port settings for the requested fleet ID.

(dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift hosting resource. New game sessions that are started on the fleet are assigned an IP address/port number combination, which must fall into the fleet\'s allowed ranges. For fleets created with a custom game server, the ranges reflect the server\'s game session assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP for use by the Realtime servers.

FromPort (integer) --A starting value for a range of allowed port numbers.

ToPort (integer) --An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .

IpRange (string) --A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: "000.000.000.000/[subnet mask] " or optionally the shortened version "0.0.0.0/[subnet mask] ".

Protocol (string) --The network communication protocol used by the fleet.










Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException


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
    
    
    :returns: 
    GameLift.Client.exceptions.InternalServiceException
    GameLift.Client.exceptions.NotFoundException
    GameLift.Client.exceptions.InvalidRequestException
    GameLift.Client.exceptions.UnauthorizedException
    
    """
    pass

def describe_fleet_utilization(FleetIds=None, Limit=None, NextToken=None):
    """
    Retrieves utilization statistics for one or more fleets. These statistics provide insight into how available hosting resources are currently being used. To get statistics on available hosting resources, see  DescribeFleetCapacity .
    You can request utilization data for all fleets, or specify a list of one or more fleet IDs. When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  FleetUtilization object is returned for each requested fleet ID, unless the fleet identifier is not found.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_fleet_utilization(
        FleetIds=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetIds: list
    :param FleetIds: A unique identifier for a fleet(s) to retrieve utilization data for. You can use either the fleet ID or ARN value. To retrieve attributes for all current fleets, do not include this parameter. If the list of fleet identifiers includes fleets that don\'t currently exist, the request succeeds but no attributes for that fleet are returned.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

FleetUtilization (list) --
A collection of objects containing utilization information for each requested fleet ID.

(dict) --
Current status of fleet utilization, including the number of game and player sessions being hosted.

CreateFleet
ListFleets
DeleteFleet
DescribeFleetAttributes
UpdateFleetAttributes
StartFleetActions or  StopFleetActions


FleetId (string) --
A unique identifier for a fleet.

ActiveServerProcessCount (integer) --
Number of server processes in an ACTIVE status currently running across all instances in the fleet

ActiveGameSessionCount (integer) --
Number of active game sessions currently being hosted on all instances in the fleet.

CurrentPlayerSessionCount (integer) --
Number of active player sessions currently being hosted on all instances in the fleet.

MaximumPlayerSessionCount (integer) --
The maximum number of players allowed across all game sessions currently being hosted on all instances in the fleet.





NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException


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
    FleetIds (list) -- A unique identifier for a fleet(s) to retrieve utilization data for. You can use either the fleet ID or ARN value. To retrieve attributes for all current fleets, do not include this parameter. If the list of fleet identifiers includes fleets that don\'t currently exist, the request succeeds but no attributes for that fleet are returned.
    
    (string) --
    
    
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.
    
    """
    pass

def describe_game_server(GameServerGroupName=None, GameServerId=None):
    """
    Retrieves information for a game server resource. Information includes the game server statuses, health check info, and the instance the game server is running on.
    To retrieve game server information, specify the game server ID. If successful, the requested game server object is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_game_server(
        GameServerGroupName='string',
        GameServerId='string'
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nAn identifier for the game server group where the game server is running. Use either the GameServerGroup name or ARN value.\n

    :type GameServerId: string
    :param GameServerId: [REQUIRED]\nThe identifier for the game server to be retrieved.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServer': {
        'GameServerGroupName': 'string',
        'GameServerGroupArn': 'string',
        'GameServerId': 'string',
        'InstanceId': 'string',
        'ConnectionInfo': 'string',
        'GameServerData': 'string',
        'CustomSortKey': 'string',
        'ClaimStatus': 'CLAIMED',
        'UtilizationStatus': 'AVAILABLE'|'UTILIZED',
        'RegistrationTime': datetime(2015, 1, 1),
        'LastClaimTime': datetime(2015, 1, 1),
        'LastHealthCheckTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

GameServer (dict) --
Object that describes the requested game server resource.

GameServerGroupName (string) --
The name identifier for the game server group where the game server is located.

GameServerGroupArn (string) --
The ARN identifier for the game server group where the game server is located.

GameServerId (string) --
A custom string that uniquely identifies the game server. Game server IDs are developer-defined and are unique across all game server groups in an AWS account.

InstanceId (string) --
The unique identifier for the instance where the game server is located.

ConnectionInfo (string) --
The port and IP address that must be used to establish a client connection to the game server.

GameServerData (string) --
A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service in response to requests  ListGameServers or  ClaimGameServer . This property can be updated using  UpdateGameServer .

CustomSortKey (string) --
A game server tag that can be used to request sorted lists of game servers when calling  ListGameServers . Custom sort keys are developer-defined. This property can be updated using  UpdateGameServer .

ClaimStatus (string) --
Indicates when an available game server has been reserved but has not yet started hosting a game. Once it is claimed, game server remains in CLAIMED status for a maximum of one minute. During this time, game clients must connect to the game server and start the game, which triggers the game server to update its utilization status. After one minute, the game server claim status reverts to null.

UtilizationStatus (string) --
Indicates whether the game server is currently available for new games or is busy. Possible statuses include:

AVAILABLE - The game server is available to be claimed. A game server that has been claimed remains in this status until it reports game hosting activity.
IN_USE - The game server is currently hosting a game session with players.


RegistrationTime (datetime) --
Time stamp indicating when the game server resource was created with a  RegisterGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastClaimTime (datetime) --
Time stamp indicating the last time the game server was claimed with a  ClaimGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057"). This value is used to calculate when the game server\'s claim status.

LastHealthCheckTime (datetime) --
Time stamp indicating the last time the game server was updated with health status using an  UpdateGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057"). After game server registration, this property is only changed when a game server update specifies a health check value.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'GameServer': {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'GameServerId': 'string',
            'InstanceId': 'string',
            'ConnectionInfo': 'string',
            'GameServerData': 'string',
            'CustomSortKey': 'string',
            'ClaimStatus': 'CLAIMED',
            'UtilizationStatus': 'AVAILABLE'|'UTILIZED',
            'RegistrationTime': datetime(2015, 1, 1),
            'LastClaimTime': datetime(2015, 1, 1),
            'LastHealthCheckTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    GameServerGroupName (string) -- [REQUIRED]
    An identifier for the game server group where the game server is running. Use either the  GameServerGroup name or ARN value.
    
    GameServerId (string) -- [REQUIRED]
    The identifier for the game server to be retrieved.
    
    
    """
    pass

def describe_game_server_group(GameServerGroupName=None):
    """
    Retrieves information on a game server group.
    To get attributes for a game server group, provide a group name or ARN value. If successful, a  GameServerGroup object is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_game_server_group(
        GameServerGroupName='string'
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nThe unique identifier for the game server group being requested. Use either the GameServerGroup name or ARN value.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GameServerGroup': {
        'GameServerGroupName': 'string',
        'GameServerGroupArn': 'string',
        'RoleArn': 'string',
        'InstanceDefinitions': [
            {
                'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'WeightedCapacity': 'string'
            },
        ],
        'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
        'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
        'AutoScalingGroupArn': 'string',
        'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
        'StatusReason': 'string',
        'SuspendedActions': [
            'REPLACE_INSTANCE_TYPES',
        ],
        'CreationTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
GameServerGroup (dict) --An object that describes the requested game server group resource.

GameServerGroupName (string) --A developer-defined identifier for the game server group. The name is unique per Region per AWS account.

GameServerGroupArn (string) --A generated unique ID for the game server group.

RoleArn (string) --The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups. The submitted role is validated to ensure that it contains the necessary permissions for game server groups.

InstanceDefinitions (list) --The set of EC2 instance types that GameLift FleetIQ can use when rebalancing and autoscaling instances in the group.

(dict) --
This data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.
An allowed instance type for your game server group. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

InstanceType (string) --An EC2 instance type designation.

WeightedCapacity (string) --Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by GameLift FleetIQ to calculate the instance type\'s cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see Instance Weighting in the Amazon EC2 Auto Scaling User Guide . Default value is "1".





BalancingStrategy (string) --The fallback balancing method to use for the game server group when Spot instances in a Region become unavailable or are not viable for game hosting. Once triggered, this method remains active until Spot instances can once again be used. Method options include:

SPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.
SPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.


GameServerProtectionPolicy (string) --A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running may be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see  DeleteGameServerGroup ). An exception to this is Spot Instances, which may be terminated by AWS regardless of protection status.

AutoScalingGroupArn (string) --A generated unique ID for the EC2 Auto Scaling group with is associated with this game server group.

Status (string) --The current status of the game server group. Possible statuses include:

NEW - GameLift FleetIQ has validated the CreateGameServerGroup() request.
ACTIVATING - GameLift FleetIQ is setting up a game server group, which includes creating an autoscaling group in your AWS account.
ACTIVE - The game server group has been successfully created.
DELETE_SCHEDULED - A request to delete the game server group has been received.
DELETING - GameLift FleetIQ has received a valid DeleteGameServerGroup() request and is processing it. GameLift FleetIQ must first complete and release hosts before it deletes the autoscaling group and the game server group.
DELETED - The game server group has been successfully deleted.
ERROR - The asynchronous processes of activating or deleting a game server group has failed, resulting in an error state.


StatusReason (string) --Additional information about the current game server group status. This information may provide additional insight on groups that in ERROR status.

SuspendedActions (list) --A list of activities that are currently suspended for this game server group. If this property is empty, all activities are occurring.

(string) --


CreationTime (datetime) --A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --A time stamp indicating when this game server group was last updated.








Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'GameServerGroup': {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'RoleArn': 'string',
            'InstanceDefinitions': [
                {
                    'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                    'WeightedCapacity': 'string'
                },
            ],
            'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
            'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
            'AutoScalingGroupArn': 'string',
            'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
            'StatusReason': 'string',
            'SuspendedActions': [
                'REPLACE_INSTANCE_TYPES',
            ],
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    SPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.
    SPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.
    
    """
    pass

def describe_game_session_details(FleetId=None, GameSessionId=None, AliasId=None, StatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves properties, including the protection policy in force, for one or more game sessions. This action can be used in several ways: (1) provide a GameSessionId or GameSessionArn to request details for a specific game session; (2) provide either a FleetId or an AliasId to request properties for all game sessions running on a fleet.
    To get game session record(s), specify just one of the following: game session ID, fleet ID, or alias ID. You can filter this request by game session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSessionDetail object is returned for each session matching the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_game_session_details(
        FleetId='string',
        GameSessionId='string',
        AliasId='string',
        StatusFilter='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: A unique identifier for a fleet to retrieve all game sessions active on the fleet. You can use either the fleet ID or ARN value.

    :type GameSessionId: string
    :param GameSessionId: A unique identifier for the game session to retrieve.

    :type AliasId: string
    :param AliasId: A unique identifier for an alias associated with the fleet to retrieve all game sessions for. You can use either the alias ID or ARN value.

    :type StatusFilter: string
    :param StatusFilter: Game session status to filter results on. Possible game session statuses include ACTIVE , TERMINATED , ACTIVATING and TERMINATING (the last two are transitory).

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'GameSessionDetails': [
        {
            'GameSession': {
                'GameSessionId': 'string',
                'Name': 'string',
                'FleetId': 'string',
                'FleetArn': 'string',
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
                'DnsName': 'string',
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

GameSessionDetails (list) --
A collection of objects containing game session properties and the protection policy currently in force for each session matching the request.

(dict) --
A game session\'s properties plus the protection policy currently in force.

GameSession (dict) --
Object that describes a game session.

GameSessionId (string) --
A unique identifier for the game session. A game session ARN has the following format: arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token> .

Name (string) --
A descriptive label that is associated with a game session. Session names do not need to be unique.

FleetId (string) --
A unique identifier for a fleet that the game session is running on.

FleetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift fleet that this game session is running on.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

TerminationTime (datetime) --
Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

CurrentPlayerSessionCount (integer) --
Number of players currently in the game session.

MaximumPlayerSessionCount (integer) --
The maximum number of players that can be connected simultaneously to the game session.

Status (string) --
Current status of the game session. A game session must have an ACTIVE status to have player sessions.

StatusReason (string) --
Provides additional information about game session status. INTERRUPTED indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.

GameProperties (list) --
Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). You can search for active game sessions based on this custom data with  SearchGameSessions .

(dict) --
Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --
The game property identifier.

Value (string) --
The game property value.





IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

PlayerSessionCreationPolicy (string) --
Indicates whether or not the game session is accepting new players.

CreatorId (string) --
A unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.

GameSessionData (string) --
Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

MatchmakerData (string) --
Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see Match Data . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ).



ProtectionPolicy (string) --
Current status of protection for the game session.

NoProtection -- The game session can be terminated during a scale-down event.
FullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.






NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.TerminalRoutingStrategyException


    :return: {
        'GameSessionDetails': [
            {
                'GameSession': {
                    'GameSessionId': 'string',
                    'Name': 'string',
                    'FleetId': 'string',
                    'FleetArn': 'string',
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
                    'DnsName': 'string',
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
    FleetId (string) -- A unique identifier for a fleet to retrieve all game sessions active on the fleet. You can use either the fleet ID or ARN value.
    GameSessionId (string) -- A unique identifier for the game session to retrieve.
    AliasId (string) -- A unique identifier for an alias associated with the fleet to retrieve all game sessions for. You can use either the alias ID or ARN value.
    StatusFilter (string) -- Game session status to filter results on. Possible game session statuses include ACTIVE , TERMINATED , ACTIVATING and TERMINATING (the last two are transitory).
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_game_session_placement(PlacementId=None):
    """
    Retrieves properties and current status of a game session placement request. To get game session placement details, specify the placement ID. If successful, a  GameSessionPlacement object is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_game_session_placement(
        PlacementId='string'
    )
    
    
    :type PlacementId: string
    :param PlacementId: [REQUIRED]\nA unique identifier for a game session placement to retrieve.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GameSessionPlacement': {
        'PlacementId': 'string',
        'GameSessionQueueName': 'string',
        'Status': 'PENDING'|'FULFILLED'|'CANCELLED'|'TIMED_OUT'|'FAILED',
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
        'DnsName': 'string',
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


Response Structure

(dict) --Represents the returned data in response to a request action.

GameSessionPlacement (dict) --Object that describes the requested game session placement.

PlacementId (string) --A unique identifier for a game session placement.

GameSessionQueueName (string) --A descriptive label that is associated with game session queue. Queue names must be unique within each Region.

Status (string) --Current status of the game session placement request.

PENDING -- The placement request is currently in the queue waiting to be processed.
FULFILLED -- A new game session and player sessions (if requested) have been successfully created. Values for GameSessionArn and GameSessionRegion are available.
CANCELLED -- The placement request was canceled with a call to  StopGameSessionPlacement .
TIMED_OUT -- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed.
FAILED -- GameLift is not able to complete the process of placing the game session. Common reasons are the game session terminated before the placement process was completed, or an unexpected internal error.


GameProperties (list) --Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

(dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --The game property identifier.

Value (string) --The game property value.





MaximumPlayerSessionCount (integer) --The maximum number of players that can be connected simultaneously to the game session.

GameSessionName (string) --A descriptive label that is associated with a game session. Session names do not need to be unique.

GameSessionId (string) --A unique identifier for the game session. This value is set once the new game session is placed (placement status is FULFILLED ).

GameSessionArn (string) --Identifier for the game session created by this placement request. This value is set once the new game session is placed (placement status is FULFILLED ). This identifier is unique across all Regions. You can use this value as a GameSessionId value as needed.

GameSessionRegion (string) --Name of the Region where the game session created by this placement request is running. This value is set once the new game session is placed (placement status is FULFILLED ).

PlayerLatencies (list) --Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions.

(dict) --Regional latency information for a player, used when requesting a new game session with  StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified Region. The relative difference between a player\'s latency values for multiple Regions are used to determine which fleets are best suited to place a new game session for the player.

PlayerId (string) --A unique identifier for a player associated with the latency data.

RegionIdentifier (string) --Name of the Region that is associated with the latency value.

LatencyInMilliseconds (float) --Amount of time that represents the time lag experienced by the player when connected to the specified Region.





StartTime (datetime) --Time stamp indicating when this request was placed in the queue. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

EndTime (datetime) --Time stamp indicating when this request was completed, canceled, or timed out.

IpAddress (string) --IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number. This value is set once the new game session is placed (placement status is FULFILLED ).

DnsName (string) --DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value is set once the new game session is placed (placement status is FULFILLED ).

PlacedPlayerSessions (list) --A collection of information on player sessions created in response to the game session placement request. These player sessions are created only once a new game session is successfully placed (placement status is FULFILLED ). This information includes the player ID (as provided in the placement request) and the corresponding player session ID. Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.

(dict) --Information about a player session that was created as part of a  StartGameSessionPlacement request. This object contains only the player ID and player session ID. To retrieve full details on a player session, call  DescribePlayerSessions with the player session ID.

CreatePlayerSession
CreatePlayerSessions
DescribePlayerSessions
Game session placements
StartGameSessionPlacement
DescribeGameSessionPlacement
StopGameSessionPlacement




PlayerId (string) --A unique identifier for a player that is associated with this player session.

PlayerSessionId (string) --A unique identifier for a player session.





GameSessionData (string) --Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

MatchmakerData (string) --Information on the matchmaking process for this game. Data is in JSON syntax, formatted as a string. It identifies the matchmaking configuration used to create the match, and contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see Match Data .








Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'GameSessionPlacement': {
            'PlacementId': 'string',
            'GameSessionQueueName': 'string',
            'Status': 'PENDING'|'FULFILLED'|'CANCELLED'|'TIMED_OUT'|'FAILED',
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
            'DnsName': 'string',
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
    FAILED -- GameLift is not able to complete the process of placing the game session. Common reasons are the game session terminated before the placement process was completed, or an unexpected internal error.
    
    """
    pass

def describe_game_session_queues(Names=None, Limit=None, NextToken=None):
    """
    Retrieves the properties for one or more game session queues. When requesting multiple queues, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSessionQueue object is returned for each requested queue. When specifying a list of queues, objects are returned only for queues that currently exist in the Region.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_game_session_queues(
        Names=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: A list of queue names to retrieve information for. You can use either the queue ID or ARN value. To request settings for all queues, leave this parameter empty.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

GameSessionQueues (list) --
A collection of objects that describe the requested game session queues.

(dict) --
Configuration of a queue that is used to process game session placement requests. The queue configuration identifies several game features:

The destinations where a new game session can potentially be hosted. Amazon GameLift tries these destinations in an order based on either the queue\'s default order or player latency information, if provided in a placement request. With latency information, Amazon GameLift can place game sessions where the majority of players are reporting the lowest possible latency.
The length of time that placement requests can wait in the queue before timing out.
A set of optional latency policies that protect individual players from high latencies, preventing game sessions from being placed where any individual player is reporting latency higher than a policy\'s maximum.
CreateGameSessionQueue
DescribeGameSessionQueues
UpdateGameSessionQueue
DeleteGameSessionQueue


Name (string) --
A descriptive label that is associated with game session queue. Queue names must be unique within each Region.

GameSessionQueueArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift game session queue ARN, the resource ID matches the Name value.

TimeoutInSeconds (integer) --
The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.

PlayerLatencyPolicies (list) --
A collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, the policy is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement.

(dict) --
Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed with any fleet in a Region where a player reports latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.

CreateGameSessionQueue
DescribeGameSessionQueues
UpdateGameSessionQueue
DeleteGameSessionQueue


MaximumIndividualPlayerLatencyMilliseconds (integer) --
The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.

PolicyDurationSeconds (integer) --
The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.





Destinations (list) --
A list of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.

(dict) --
Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination that is configured for a queue.

CreateGameSessionQueue
DescribeGameSessionQueues
UpdateGameSessionQueue
DeleteGameSessionQueue


DestinationArn (string) --
The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.









NextToken (string) --
A token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException


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
    Names (list) -- A list of queue names to retrieve information for. You can use either the queue ID or ARN value. To request settings for all queues, leave this parameter empty.
    
    (string) --
    
    
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_game_sessions(FleetId=None, GameSessionId=None, AliasId=None, StatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves a set of one or more game sessions. Request a specific game session or request all game sessions on a fleet. Alternatively, use  SearchGameSessions to request a set of active game sessions that are filtered by certain criteria. To retrieve protection policy settings for game sessions, use  DescribeGameSessionDetails .
    To get game sessions, specify one of the following: game session ID, fleet ID, or alias ID. You can filter this request by game session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  GameSession object is returned for each game session matching the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_game_sessions(
        FleetId='string',
        GameSessionId='string',
        AliasId='string',
        StatusFilter='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: A unique identifier for a fleet to retrieve all game sessions for. You can use either the fleet ID or ARN value.

    :type GameSessionId: string
    :param GameSessionId: A unique identifier for the game session to retrieve.

    :type AliasId: string
    :param AliasId: A unique identifier for an alias associated with the fleet to retrieve all game sessions for. You can use either the alias ID or ARN value.

    :type StatusFilter: string
    :param StatusFilter: Game session status to filter results on. Possible game session statuses include ACTIVE , TERMINATED , ACTIVATING , and TERMINATING (the last two are transitory).

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'GameSessions': [
        {
            'GameSessionId': 'string',
            'Name': 'string',
            'FleetId': 'string',
            'FleetArn': 'string',
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
            'DnsName': 'string',
            'Port': 123,
            'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
            'CreatorId': 'string',
            'GameSessionData': 'string',
            'MatchmakerData': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

GameSessions (list) --
A collection of objects containing game session properties for each session matching the request.

(dict) --
Properties describing a game session.
A game session in ACTIVE status can host players. When a game session ends, its status is set to TERMINATED .
Once the session ends, the game session object is retained for 30 days. This means you can reuse idempotency token values after this time. Game session logs are retained for 14 days.

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




GameSessionId (string) --
A unique identifier for the game session. A game session ARN has the following format: arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token> .

Name (string) --
A descriptive label that is associated with a game session. Session names do not need to be unique.

FleetId (string) --
A unique identifier for a fleet that the game session is running on.

FleetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift fleet that this game session is running on.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

TerminationTime (datetime) --
Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

CurrentPlayerSessionCount (integer) --
Number of players currently in the game session.

MaximumPlayerSessionCount (integer) --
The maximum number of players that can be connected simultaneously to the game session.

Status (string) --
Current status of the game session. A game session must have an ACTIVE status to have player sessions.

StatusReason (string) --
Provides additional information about game session status. INTERRUPTED indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.

GameProperties (list) --
Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). You can search for active game sessions based on this custom data with  SearchGameSessions .

(dict) --
Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --
The game property identifier.

Value (string) --
The game property value.





IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

PlayerSessionCreationPolicy (string) --
Indicates whether or not the game session is accepting new players.

CreatorId (string) --
A unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.

GameSessionData (string) --
Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

MatchmakerData (string) --
Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see Match Data . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ).





NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.TerminalRoutingStrategyException


    :return: {
        'GameSessions': [
            {
                'GameSessionId': 'string',
                'Name': 'string',
                'FleetId': 'string',
                'FleetArn': 'string',
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
                'DnsName': 'string',
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
    FleetId (string) -- A unique identifier for a fleet to retrieve all game sessions for. You can use either the fleet ID or ARN value.
    GameSessionId (string) -- A unique identifier for the game session to retrieve.
    AliasId (string) -- A unique identifier for an alias associated with the fleet to retrieve all game sessions for. You can use either the alias ID or ARN value.
    StatusFilter (string) -- Game session status to filter results on. Possible game session statuses include ACTIVE , TERMINATED , ACTIVATING , and TERMINATING (the last two are transitory).
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_instances(FleetId=None, InstanceId=None, Limit=None, NextToken=None):
    """
    Retrieves information about a fleet\'s instances, including instance IDs. Use this action to get details on all instances in the fleet or get details on one specific instance.
    To get a specific instance, specify fleet ID and instance ID. To get all instances in a fleet, specify a fleet ID only. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, an  Instance object is returned for each result.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_instances(
        FleetId='string',
        InstanceId='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to retrieve instance information for. You can use either the fleet ID or ARN value.\n

    :type InstanceId: string
    :param InstanceId: A unique identifier for an instance to retrieve. Specify an instance ID or leave blank to retrieve all instances in the fleet.

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'Instances': [
        {
            'FleetId': 'string',
            'InstanceId': 'string',
            'IpAddress': 'string',
            'DnsName': 'string',
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
            'Type': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
            'Status': 'PENDING'|'ACTIVE'|'TERMINATING',
            'CreationTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

Instances (list) --
A collection of objects containing properties for each instance returned.

(dict) --
Properties that describe an instance of a virtual computing resource that hosts one or more game servers. A fleet may contain zero or more instances.

FleetId (string) --
A unique identifier for a fleet that the instance is in.

InstanceId (string) --
A unique identifier for an instance.

IpAddress (string) --
IP address that is assigned to the instance.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

OperatingSystem (string) --
Operating system that is running on this instance.

Type (string) --
EC2 instance type that defines the computing resources of this instance.

Status (string) --
Current status of the instance. Possible statuses include the following:

PENDING -- The instance is in the process of being created and launching server processes as defined in the fleet\'s run-time configuration.
ACTIVE -- The instance has been successfully created and at least one server process has successfully launched and reported back to Amazon GameLift that it is ready to host a game session. The instance is now considered ready to host game sessions.
TERMINATING -- The instance is in the process of shutting down. This may happen to reduce capacity during a scaling down event or to recycle resources in the event of a problem.


CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").





NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'Instances': [
            {
                'FleetId': 'string',
                'InstanceId': 'string',
                'IpAddress': 'string',
                'DnsName': 'string',
                'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
                'Type': 't2.micro'|'t2.small'|'t2.medium'|'t2.large'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'Status': 'PENDING'|'ACTIVE'|'TERMINATING',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet to retrieve instance information for. You can use either the fleet ID or ARN value.
    
    InstanceId (string) -- A unique identifier for an instance to retrieve. Specify an instance ID or leave blank to retrieve all instances in the fleet.
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_matchmaking(TicketIds=None):
    """
    Retrieves one or more matchmaking tickets. Use this operation to retrieve ticket information, including status and--once a successful match is made--acquire connection information for the resulting new game session.
    You can use this operation to track the progress of matchmaking requests (through polling) as an alternative to using event notifications. See more details on tracking matchmaking requests through polling or notifications in  StartMatchmaking .
    To request matchmaking tickets, provide a list of up to 10 ticket IDs. If the request is successful, a ticket object is returned for each requested ID that currently exists.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_matchmaking(
        TicketIds=[
            'string',
        ]
    )
    
    
    :type TicketIds: list
    :param TicketIds: [REQUIRED]\nA unique identifier for a matchmaking ticket. You can include up to 10 ID values.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'TicketList': [
        {
            'TicketId': 'string',
            'ConfigurationName': 'string',
            'ConfigurationArn': 'string',
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
                'DnsName': 'string',
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


Response Structure

(dict) --Represents the returned data in response to a request action.

TicketList (list) --A collection of existing matchmaking ticket objects matching the request.

(dict) --Ticket generated to track the progress of a matchmaking request. Each ticket is uniquely identified by a ticket ID, supplied by the requester, when creating a matchmaking request with  StartMatchmaking . Tickets can be retrieved by calling  DescribeMatchmaking with the ticket ID.

TicketId (string) --A unique identifier for a matchmaking ticket.

ConfigurationName (string) --Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking configurations determine how players are grouped into a match and how a new game session is created for the match.

ConfigurationArn (string) --The Amazon Resource Name (ARN ) associated with the GameLift matchmaking configuration resource that is used with this ticket.

Status (string) --Current status of the matchmaking request.

QUEUED -- The matchmaking request has been received and is currently waiting to be processed.
SEARCHING -- The matchmaking request is currently being processed.
REQUIRES_ACCEPTANCE -- A match has been proposed and the players must accept the match (see  AcceptMatch ). This status is used only with requests that use a matchmaking configuration with a player acceptance requirement.
PLACING -- The FlexMatch engine has matched players and is in the process of placing a new game session for the match.
COMPLETED -- Players have been matched and a game session is ready to host the players. A ticket in this state contains the necessary connection information for players.
FAILED -- The matchmaking request was not completed.
CANCELLED -- The matchmaking request was canceled. This may be the result of a call to  StopMatchmaking or a proposed match that one or more players failed to accept.
TIMED_OUT -- The matchmaking request was not successful within the duration specified in the matchmaking configuration.


Note
Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED, TIMED_OUT) can be resubmitted as new requests with new ticket IDs.


StatusReason (string) --Code to explain the current status. For example, a status reason may indicate when a ticket has returned to SEARCHING status after a proposed match fails to receive player acceptances.

StatusMessage (string) --Additional information about the current status.

StartTime (datetime) --Time stamp indicating when this matchmaking request was received. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

EndTime (datetime) --Time stamp indicating when this matchmaking request stopped being processed due to success, failure, or cancellation. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

Players (list) --A set of Player objects, each representing a player to find matches for. Players are identified by a unique player ID and may include latency data for use during matchmaking. If the ticket is in status COMPLETED , the Player objects include the team the players were assigned to in the resulting match.

(dict) --Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.

PlayerId (string) --A unique identifier for a player

PlayerAttributes (dict) --A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the playerAttributes used in a matchmaking rule set. Example: "PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}} .

(string) --
(dict) --Values for use in  Player attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each AttributeValue object can use only one of the available properties.

S (string) --For single string values. Maximum string length is 100 characters.

N (float) --For number values, expressed as double.

SL (list) --For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.

(string) --


SDM (dict) --For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.

(string) --
(float) --










Team (string) --Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.

LatencyInMs (dict) --Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions. If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported.
If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable.

(string) --
(integer) --








GameSessionConnectionInfo (dict) --Identifier and connection information of the game session created for the match. This information is added to the ticket only after the matchmaking request has been successfully completed.

GameSessionArn (string) --Amazon Resource Name (ARN ) that is assigned to a game session and uniquely identifies it.

IpAddress (string) --IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

MatchedPlayerSessions (list) --A collection of player session IDs, one for each player ID that was included in the original matchmaking request.

(dict) --Represents a new player session that is created as a result of a successful FlexMatch match. A successful match automatically creates new player sessions for every player ID in the original matchmaking request.
When players connect to the match\'s game session, they must include both player ID and player session ID in order to claim their assigned player slot.

PlayerId (string) --A unique identifier for a player

PlayerSessionId (string) --A unique identifier for a player session







EstimatedWaitTime (integer) --Average amount of time (in seconds) that players are currently waiting for a match. If there is not enough recent data, this property may be empty.










Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException


    :return: {
        'TicketList': [
            {
                'TicketId': 'string',
                'ConfigurationName': 'string',
                'ConfigurationArn': 'string',
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
                    'DnsName': 'string',
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
    Retrieves the details of FlexMatch matchmaking configurations. With this operation, you have the following options: (1) retrieve all existing configurations, (2) provide the names of one or more configurations to retrieve, or (3) retrieve all configurations that use a specified rule set name. When requesting multiple items, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a configuration is returned for each requested name. When specifying a list of names, only configurations that currently exist are returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_matchmaking_configurations(
        Names=[
            'string',
        ],
        RuleSetName='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: A unique identifier for a matchmaking configuration(s) to retrieve. You can use either the configuration name or ARN value. To request all existing configurations, leave this parameter empty.\n\n(string) --\n\n

    :type RuleSetName: string
    :param RuleSetName: A unique identifier for a matchmaking rule set. You can use either the rule set name or ARN value. Use this parameter to retrieve all matchmaking configurations that use this rule set.

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is limited to 10.

    :type NextToken: string
    :param NextToken: A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'Configurations': [
        {
            'Name': 'string',
            'ConfigurationArn': 'string',
            'Description': 'string',
            'GameSessionQueueArns': [
                'string',
            ],
            'RequestTimeoutSeconds': 123,
            'AcceptanceTimeoutSeconds': 123,
            'AcceptanceRequired': True|False,
            'RuleSetName': 'string',
            'RuleSetArn': 'string',
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
            'GameSessionData': 'string',
            'BackfillMode': 'AUTOMATIC'|'MANUAL'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

Configurations (list) --
A collection of requested matchmaking configurations.

(dict) --
Guidelines for use with FlexMatch to match players into games. All matchmaking requests must specify a matchmaking configuration.

Name (string) --
A unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.

ConfigurationArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift matchmaking configuration resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift configuration ARN, the resource ID matches the Name value.

Description (string) --
A descriptive label that is associated with matchmaking configuration.

GameSessionQueueArns (list) --
Amazon Resource Name (ARN ) that is assigned to a GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. GameLift uses the listed queues when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any Region.

(string) --


RequestTimeoutSeconds (integer) --
The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.

AcceptanceTimeoutSeconds (integer) --
The length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.

AcceptanceRequired (boolean) --
A flag that indicates whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.

RuleSetName (string) --
A unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same Region.

RuleSetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift matchmaking rule set resource that this configuration uses.

NotificationTarget (string) --
An SNS topic ARN that is set up to receive matchmaking notifications.

AdditionalPlayerCount (integer) --
The number of player slots in a match to keep open for future players. For example, assume that the configuration\'s rule set specifies a match for a single 12-person team. If the additional player count is set to 2, only 10 players are initially selected for the match.

CustomEventData (string) --
Information to attach to all events related to the matchmaking configuration.

CreationTime (datetime) --
The time stamp indicating when this data object was created. The format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

GameProperties (list) --
A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.

(dict) --
Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --
The game property identifier.

Value (string) --
The game property value.





GameSessionData (string) --
A set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.

BackfillMode (string) --
The method used to backfill game sessions created with this matchmaking configuration. MANUAL indicates that the game makes backfill requests or does not use the match backfill feature. AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever a game session has one or more open slots. Learn more about manual and automatic backfill in Backfill Existing Games with FlexMatch .





NextToken (string) --
A token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException


    :return: {
        'Configurations': [
            {
                'Name': 'string',
                'ConfigurationArn': 'string',
                'Description': 'string',
                'GameSessionQueueArns': [
                    'string',
                ],
                'RequestTimeoutSeconds': 123,
                'AcceptanceTimeoutSeconds': 123,
                'AcceptanceRequired': True|False,
                'RuleSetName': 'string',
                'RuleSetArn': 'string',
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
                'GameSessionData': 'string',
                'BackfillMode': 'AUTOMATIC'|'MANUAL'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Names (list) -- A unique identifier for a matchmaking configuration(s) to retrieve. You can use either the configuration name or ARN value. To request all existing configurations, leave this parameter empty.
    
    (string) --
    
    
    RuleSetName (string) -- A unique identifier for a matchmaking rule set. You can use either the rule set name or ARN value. Use this parameter to retrieve all matchmaking configurations that use this rule set.
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. This parameter is limited to 10.
    NextToken (string) -- A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_matchmaking_rule_sets(Names=None, Limit=None, NextToken=None):
    """
    Retrieves the details for FlexMatch matchmaking rule sets. You can request all existing rule sets for the Region, or provide a list of one or more rule set names. When requesting multiple items, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a rule set is returned for each requested name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_matchmaking_rule_sets(
        Names=[
            'string',
        ],
        Limit=123,
        NextToken='string'
    )
    
    
    :type Names: list
    :param Names: A list of one or more matchmaking rule set names to retrieve details for. (Note: The rule set name is different from the optional 'name' field in the rule set body.) You can use either the rule set name or ARN value.\n\n(string) --\n\n

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'RuleSets': [
        {
            'RuleSetName': 'string',
            'RuleSetArn': 'string',
            'RuleSetBody': 'string',
            'CreationTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

RuleSets (list) --
A collection of requested matchmaking rule set objects.

(dict) --
Set of rule statements, used with FlexMatch, that determine how to build your player matches. Each rule set describes a type of group to be created and defines the parameters for acceptable player matches. Rule sets are used in  MatchmakingConfiguration objects.
A rule set may define the following elements for a match. For detailed information and examples showing how to construct a rule set, see Build a FlexMatch Rule Set .

Teams -- Required. A rule set must define one or multiple teams for the match and set minimum and maximum team sizes. For example, a rule set might describe a 4x4 match that requires all eight slots to be filled.
Player attributes -- Optional. These attributes specify a set of player characteristics to evaluate when looking for a match. Matchmaking requests that use a rule set with player attributes must provide the corresponding attribute values. For example, an attribute might specify a player\'s skill or level.
Rules -- Optional. Rules define how to evaluate potential players for a match based on player attributes. A rule might specify minimum requirements for individual players, teams, or entire matches. For example, a rule might require each player to meet a certain skill level, each team to have at least one player in a certain role, or the match to have a minimum average skill level. or may describe an entire group--such as all teams must be evenly matched or have at least one player in a certain role.
Expansions -- Optional. Expansions allow you to relax the rules after a period of time when no acceptable matches are found. This feature lets you balance getting players into games in a reasonable amount of time instead of making them wait indefinitely for the best possible match. For example, you might use an expansion to increase the maximum skill variance between players after 30 seconds.


RuleSetName (string) --
A unique identifier for a matchmaking rule set

RuleSetArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift matchmaking rule set resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift rule set ARN, the resource ID matches the RuleSetName value.

RuleSetBody (string) --
A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.

CreationTime (datetime) --
The time stamp indicating when this data object was created. The format is a number expressed in Unix time as milliseconds (for example "1469498468.057").





NextToken (string) --
A token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnsupportedRegionException


    :return: {
        'RuleSets': [
            {
                'RuleSetName': 'string',
                'RuleSetArn': 'string',
                'RuleSetBody': 'string',
                'CreationTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    CreateMatchmakingConfiguration
    DescribeMatchmakingConfigurations
    UpdateMatchmakingConfiguration
    DeleteMatchmakingConfiguration
    CreateMatchmakingRuleSet
    DescribeMatchmakingRuleSets
    ValidateMatchmakingRuleSet
    DeleteMatchmakingRuleSet
    
    """
    pass

def describe_player_sessions(GameSessionId=None, PlayerId=None, PlayerSessionId=None, PlayerSessionStatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves properties for one or more player sessions. This action can be used in several ways: (1) provide a PlayerSessionId to request properties for a specific player session; (2) provide a GameSessionId to request properties for all player sessions in the specified game session; (3) provide a PlayerId to request properties for all player sessions of a specified player.
    To get game session record(s), specify only one of the following: a player session ID, a game session ID, or a player ID. You can filter this request by player session status. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, a  PlayerSession object is returned for each session matching the request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_player_sessions(
        GameSessionId='string',
        PlayerId='string',
        PlayerSessionId='string',
        PlayerSessionStatusFilter='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type GameSessionId: string
    :param GameSessionId: A unique identifier for the game session to retrieve player sessions for.

    :type PlayerId: string
    :param PlayerId: A unique identifier for a player to retrieve player sessions for.

    :type PlayerSessionId: string
    :param PlayerSessionId: A unique identifier for a player session to retrieve.

    :type PlayerSessionStatusFilter: string
    :param PlayerSessionStatusFilter: Player session status to filter results on.\nPossible player session statuses include the following:\n\nRESERVED -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.\nACTIVE -- The player has been validated by the server process and is currently connected.\nCOMPLETED -- The player connection has been dropped.\nTIMEDOUT -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).\n\n

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. If a player session ID is specified, this parameter is ignored.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored.

    :rtype: dict

ReturnsResponse Syntax
{
    'PlayerSessions': [
        {
            'PlayerSessionId': 'string',
            'PlayerId': 'string',
            'GameSessionId': 'string',
            'FleetId': 'string',
            'FleetArn': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'TerminationTime': datetime(2015, 1, 1),
            'Status': 'RESERVED'|'ACTIVE'|'COMPLETED'|'TIMEDOUT',
            'IpAddress': 'string',
            'DnsName': 'string',
            'Port': 123,
            'PlayerData': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

PlayerSessions (list) --
A collection of objects containing properties for each player session that matches the request.

(dict) --
Properties describing a player session. Player session objects are created either by creating a player session for a specific game session, or as part of a game session placement. A player session represents either a player reservation for a game session (status RESERVED ) or actual player activity in a game session (status ACTIVE ). A player session object (including player data) is automatically passed to a game session when the player connects to the game session and is validated.
When a player disconnects, the player session status changes to COMPLETED . Once the session ends, the player session object is retained for 30 days and then removed.

CreatePlayerSession
CreatePlayerSessions
DescribePlayerSessions
Game session placements
StartGameSessionPlacement
DescribeGameSessionPlacement
StopGameSessionPlacement




PlayerSessionId (string) --
A unique identifier for a player session.

PlayerId (string) --
A unique identifier for a player that is associated with this player session.

GameSessionId (string) --
A unique identifier for the game session that the player session is connected to.

FleetId (string) --
A unique identifier for a fleet that the player\'s game session is running on.

FleetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift fleet that the player\'s game session is running on.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

TerminationTime (datetime) --
Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

Status (string) --
Current status of the player session.
Possible player session statuses include the following:

RESERVED -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.
ACTIVE -- The player has been validated by the server process and is currently connected.
COMPLETED -- The player connection has been dropped.
TIMEDOUT -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).


IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift server process, an app needs both the IP address and port number.

PlayerData (string) --
Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.





NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'PlayerSessions': [
            {
                'PlayerSessionId': 'string',
                'PlayerId': 'string',
                'GameSessionId': 'string',
                'FleetId': 'string',
                'FleetArn': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'TerminationTime': datetime(2015, 1, 1),
                'Status': 'RESERVED'|'ACTIVE'|'COMPLETED'|'TIMEDOUT',
                'IpAddress': 'string',
                'DnsName': 'string',
                'Port': 123,
                'PlayerData': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    GameSessionId (string) -- A unique identifier for the game session to retrieve player sessions for.
    PlayerId (string) -- A unique identifier for a player to retrieve player sessions for.
    PlayerSessionId (string) -- A unique identifier for a player session to retrieve.
    PlayerSessionStatusFilter (string) -- Player session status to filter results on.
    Possible player session statuses include the following:
    
    RESERVED -- The player session request has been received, but the player has not yet connected to the server process and/or been validated.
    ACTIVE -- The player has been validated by the server process and is currently connected.
    COMPLETED -- The player connection has been dropped.
    TIMEDOUT -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).
    
    
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. If a player session ID is specified, this parameter is ignored.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored.
    
    """
    pass

def describe_runtime_configuration(FleetId=None):
    """
    Retrieves a fleet\'s runtime configuration settings. The runtime configuration tells Amazon GameLift which server processes to run (and how) on each instance in the fleet.
    To get a runtime configuration, specify the fleet\'s unique identifier. If successful, a  RuntimeConfiguration object is returned for the requested fleet. If the requested fleet has been deleted, the result set is empty.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_runtime_configuration(
        FleetId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to get the runtime configuration for. You can use either the fleet ID or ARN value.\n

    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --Represents the returned data in response to a request action.

RuntimeConfiguration (dict) --Instructions describing how server processes should be launched and maintained on each instance in the fleet.

ServerProcesses (list) --A collection of server process configurations that describe which server processes to run on each instance in a fleet.

(dict) --A set of instructions for launching server processes on each instance in a fleet. Server processes run either a custom game build executable or a Realtime Servers script. Each instruction set identifies the location of the custom game build executable or Realtime launch script, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet\'s ``  RuntimeConfiguration `` .

LaunchPath (string) --The location of the server executable in a custom game build or the name of the Realtime script file that contains the Init() function. Game builds and Realtime scripts are installed on instances at the root:

Windows (for custom game builds only): C:\\game . Example: "C:\\game\\MyGame\\server.exe "
Linux: /local/game . Examples: "/local/game/MyGame/server.exe " or "/local/game/MyRealtimeScript.js "


Parameters (string) --An optional list of parameters to pass to the server executable or Realtime script on launch.

ConcurrentExecutions (integer) --The number of server processes that use this configuration to run concurrently on an instance.





MaxConcurrentGameSessionActivations (integer) --The maximum number of game sessions with status ACTIVATING to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.

GameSessionActivationTimeoutSeconds (integer) --The maximum amount of time (in seconds) that a game session can remain in status ACTIVATING . If the game session is not active before the timeout, activation is terminated and the game session status is changed to TERMINATED .








Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException


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
    Windows (for custom game builds only): C:\\game . Example: "C:\\game\\MyGame\\server.exe "
    Linux: /local/game . Examples: "/local/game/MyGame/server.exe " or "/local/game/MyRealtimeScript.js "
    
    """
    pass

def describe_scaling_policies(FleetId=None, StatusFilter=None, Limit=None, NextToken=None):
    """
    Retrieves all scaling policies applied to a fleet.
    To get a fleet\'s scaling policies, specify the fleet ID. You can filter this request by policy status, such as to retrieve only active scaling policies. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, set of  ScalingPolicy objects is returned for the fleet.
    A fleet may have all of its scaling policies suspended ( StopFleetActions ). This action does not affect the status of the scaling policies, which remains ACTIVE. To see whether a fleet\'s scaling policies are in force or suspended, call  DescribeFleetAttributes and check the stopped actions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_scaling_policies(
        FleetId='string',
        StatusFilter='ACTIVE'|'UPDATE_REQUESTED'|'UPDATING'|'DELETE_REQUESTED'|'DELETING'|'DELETED'|'ERROR',
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to retrieve scaling policies for. You can use either the fleet ID or ARN value.\n

    :type StatusFilter: string
    :param StatusFilter: Scaling policy status to filter results on. A scaling policy is only in force when in an ACTIVE status.\n\nACTIVE -- The scaling policy is currently in force.\nUPDATEREQUESTED -- A request to update the scaling policy has been received.\nUPDATING -- A change is being made to the scaling policy.\nDELETEREQUESTED -- A request to delete the scaling policy has been received.\nDELETING -- The scaling policy is being deleted.\nDELETED -- The scaling policy has been deleted.\nERROR -- An error occurred in creating the policy. It should be removed and recreated.\n\n

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
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
            'MetricName': 'ActivatingGameSessions'|'ActiveGameSessions'|'ActiveInstances'|'AvailableGameSessions'|'AvailablePlayerSessions'|'CurrentPlayerSessions'|'IdleInstances'|'PercentAvailableGameSessions'|'PercentIdleInstances'|'QueueDepth'|'WaitTime',
            'PolicyType': 'RuleBased'|'TargetBased',
            'TargetConfiguration': {
                'TargetValue': 123.0
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

ScalingPolicies (list) --
A collection of objects containing the scaling policies matching the request.

(dict) --
Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.

DescribeFleetCapacity
UpdateFleetCapacity
DescribeEC2InstanceLimits
Manage scaling policies:
PutScalingPolicy (auto-scaling)
DescribeScalingPolicies (auto-scaling)
DeleteScalingPolicy (auto-scaling)


Manage fleet actions:
StartFleetActions
StopFleetActions




FleetId (string) --
A unique identifier for a fleet that is associated with this scaling policy.

Name (string) --
A descriptive label that is associated with a scaling policy. Policy names do not need to be unique.

Status (string) --
Current status of the scaling policy. The scaling policy can be in force only when in an ACTIVE status. Scaling policies can be suspended for individual fleets (see  StopFleetActions ; if suspended for a fleet, the policy status does not change. View a fleet\'s stopped actions by calling  DescribeFleetCapacity .

ACTIVE -- The scaling policy can be used for auto-scaling a fleet.
UPDATE_REQUESTED -- A request to update the scaling policy has been received.
UPDATING -- A change is being made to the scaling policy.
DELETE_REQUESTED -- A request to delete the scaling policy has been received.
DELETING -- The scaling policy is being deleted.
DELETED -- The scaling policy has been deleted.
ERROR -- An error occurred in creating the policy. It should be removed and recreated.


ScalingAdjustment (integer) --
Amount of adjustment to make, based on the scaling adjustment type.

ScalingAdjustmentType (string) --
The type of adjustment to make to a fleet\'s instance count (see  FleetCapacity ):

ChangeInCapacity -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
ExactCapacity -- set the instance count to the scaling adjustment value.
PercentChangeInCapacity -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.


ComparisonOperator (string) --
Comparison operator to use when measuring a metric against the threshold value.

Threshold (float) --
Metric value used to trigger a scaling event.

EvaluationPeriods (integer) --
Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.

MetricName (string) --
Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see Monitor Amazon GameLift with Amazon CloudWatch .

ActivatingGameSessions -- Game sessions in the process of being created.
ActiveGameSessions -- Game sessions that are currently running.
ActiveInstances -- Fleet instances that are currently running at least one game session.
AvailableGameSessions -- Additional game sessions that fleet could host simultaneously, given current capacity.
AvailablePlayerSessions -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
CurrentPlayerSessions -- Player slots in active game sessions that are being used by a player or are reserved for a player.
IdleInstances -- Active instances that are currently hosting zero game sessions.
PercentAvailableGameSessions -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
PercentIdleInstances -- Percentage of the total number of active instances that are hosting zero game sessions.
QueueDepth -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
WaitTime -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.


PolicyType (string) --
The type of scaling policy to create. For a target-based policy, set the parameter MetricName to \'PercentAvailableGameSessions\' and specify a TargetConfiguration . For a rule-based policy set the following parameters: MetricName , ComparisonOperator , Threshold , EvaluationPeriods , ScalingAdjustmentType , and ScalingAdjustment .

TargetConfiguration (dict) --
The settings for a target-based scaling policy.

TargetValue (float) --
Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet\'s buffer (the percent of capacity that should be idle and ready for new game sessions).







NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.NotFoundException


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
                'MetricName': 'ActivatingGameSessions'|'ActiveGameSessions'|'ActiveInstances'|'AvailableGameSessions'|'AvailablePlayerSessions'|'CurrentPlayerSessions'|'IdleInstances'|'PercentAvailableGameSessions'|'PercentIdleInstances'|'QueueDepth'|'WaitTime',
                'PolicyType': 'RuleBased'|'TargetBased',
                'TargetConfiguration': {
                    'TargetValue': 123.0
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet to retrieve scaling policies for. You can use either the fleet ID or ARN value.
    
    StatusFilter (string) -- Scaling policy status to filter results on. A scaling policy is only in force when in an ACTIVE status.
    
    ACTIVE -- The scaling policy is currently in force.
    UPDATEREQUESTED -- A request to update the scaling policy has been received.
    UPDATING -- A change is being made to the scaling policy.
    DELETEREQUESTED -- A request to delete the scaling policy has been received.
    DELETING -- The scaling policy is being deleted.
    DELETED -- The scaling policy has been deleted.
    ERROR -- An error occurred in creating the policy. It should be removed and recreated.
    
    
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def describe_script(ScriptId=None):
    """
    Retrieves properties for a Realtime script.
    To request a script record, specify the script ID. If successful, an object containing the script properties is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_script(
        ScriptId='string'
    )
    
    
    :type ScriptId: string
    :param ScriptId: [REQUIRED]\nA unique identifier for a Realtime script to retrieve properties for. You can use either the script ID or ARN value.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Script': {
        'ScriptId': 'string',
        'ScriptArn': 'string',
        'Name': 'string',
        'Version': 'string',
        'SizeOnDisk': 123,
        'CreationTime': datetime(2015, 1, 1),
        'StorageLocation': {
            'Bucket': 'string',
            'Key': 'string',
            'RoleArn': 'string',
            'ObjectVersion': 'string'
        }
    }
}


Response Structure

(dict) --
Script (dict) --A set of properties describing the requested script.

ScriptId (string) --A unique identifier for a Realtime script

ScriptArn (string) --Amazon Resource Name (ARN ) that is assigned to a GameLift script resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift script ARN, the resource ID matches the ScriptId value.

Name (string) --A descriptive label that is associated with a script. Script names do not need to be unique.

Version (string) --The version that is associated with a build or script. Version strings do not need to be unique.

SizeOnDisk (integer) --The file size of the uploaded Realtime script, expressed in bytes. When files are uploaded from an S3 location, this value remains at "0".

CreationTime (datetime) --A time stamp indicating when this data object was created. The format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

StorageLocation (dict) --The location in S3 where build or script files are stored for access by Amazon GameLift. This location is specified in  CreateBuild ,  CreateScript , and  UpdateScript requests.

Bucket (string) --An S3 bucket identifier. This is the name of the S3 bucket.

Key (string) --The name of the zip file that contains the build files or script files.

RoleArn (string) --The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access the S3 bucket.

ObjectVersion (string) --The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.










Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException


    :return: {
        'Script': {
            'ScriptId': 'string',
            'ScriptArn': 'string',
            'Name': 'string',
            'Version': 'string',
            'SizeOnDisk': 123,
            'CreationTime': datetime(2015, 1, 1),
            'StorageLocation': {
                'Bucket': 'string',
                'Key': 'string',
                'RoleArn': 'string',
                'ObjectVersion': 'string'
            }
        }
    }
    
    
    :returns: 
    GameLift.Client.exceptions.UnauthorizedException
    GameLift.Client.exceptions.InvalidRequestException
    GameLift.Client.exceptions.InternalServiceException
    GameLift.Client.exceptions.NotFoundException
    
    """
    pass

def describe_vpc_peering_authorizations():
    """
    Retrieves valid VPC peering authorizations that are pending for the AWS account. This operation returns all VPC peering authorizations and requests for peering. This includes those initiated and received by this account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_vpc_peering_authorizations()
    
    
    :rtype: dict
ReturnsResponse Syntax{
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


Response Structure

(dict) --
VpcPeeringAuthorizations (list) --A collection of objects that describe all valid VPC peering operations for the current AWS account.

(dict) --Represents an authorization for a VPC peering connection between the VPC for an Amazon GameLift fleet and another VPC on an account you have access to. This authorization must exist and be valid for the peering connection to be established. Authorizations are valid for 24 hours after they are issued.

CreateVpcPeeringAuthorization
DescribeVpcPeeringAuthorizations
DeleteVpcPeeringAuthorization
CreateVpcPeeringConnection
DescribeVpcPeeringConnections
DeleteVpcPeeringConnection


GameLiftAwsAccountId (string) --A unique identifier for the AWS account that you use to manage your Amazon GameLift fleet. You can find your Account ID in the AWS Management Console under account settings.

PeerVpcAwsAccountId (string) --
PeerVpcId (string) --A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .

CreationTime (datetime) --Time stamp indicating when this authorization was issued. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

ExpirationTime (datetime) --Time stamp indicating when this authorization expires (24 hours after issuance). Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").










Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException


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
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_vpc_peering_connections(
        FleetId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: A unique identifier for a fleet. You can use either the fleet ID or ARN value.

    :rtype: dict
ReturnsResponse Syntax{
    'VpcPeeringConnections': [
        {
            'FleetId': 'string',
            'FleetArn': 'string',
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


Response Structure

(dict) --Represents the returned data in response to a request action.

VpcPeeringConnections (list) --A collection of VPC peering connection records that match the request.

(dict) --Represents a peering connection between a VPC on one of your AWS accounts and the VPC for your Amazon GameLift fleets. This record may be for an active peering connection or a pending connection that has not yet been established.

CreateVpcPeeringAuthorization
DescribeVpcPeeringAuthorizations
DeleteVpcPeeringAuthorization
CreateVpcPeeringConnection
DescribeVpcPeeringConnections
DeleteVpcPeeringConnection


FleetId (string) --A unique identifier for a fleet. This ID determines the ID of the Amazon GameLift VPC for your fleet.

FleetArn (string) --The Amazon Resource Name (ARN ) associated with the GameLift fleet resource for this connection.

IpV4CidrBlock (string) --CIDR block of IPv4 addresses assigned to the VPC peering connection for the GameLift VPC. The peered VPC also has an IPv4 CIDR block associated with it; these blocks cannot overlap or the peering connection cannot be created.

VpcPeeringConnectionId (string) --A unique identifier that is automatically assigned to the connection record. This ID is referenced in VPC peering connection events, and is used when deleting a connection with  DeleteVpcPeeringConnection .

Status (dict) --The status information about the connection. Status indicates if a connection is pending, successful, or failed.

Code (string) --Code indicating the status of a VPC peering connection.

Message (string) --Additional messaging associated with the connection status.



PeerVpcId (string) --A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region where your fleet is deployed. Look up a VPC ID using the VPC Dashboard in the AWS Management Console. Learn more about VPC peering in VPC Peering with Amazon GameLift Fleets .

GameLiftVpcId (string) --A unique identifier for the VPC that contains the Amazon GameLift fleet for this connection. This VPC is managed by Amazon GameLift and does not appear in your AWS account.










Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'VpcPeeringConnections': [
            {
                'FleetId': 'string',
                'FleetArn': 'string',
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
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_game_session_log_url(GameSessionId=None):
    """
    Retrieves the location of stored game session logs for a specified game session. When a game session is terminated, Amazon GameLift automatically stores the logs in Amazon S3 and retains them for 14 days. Use this URL to download the logs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_game_session_log_url(
        GameSessionId='string'
    )
    
    
    :type GameSessionId: string
    :param GameSessionId: [REQUIRED]\nA unique identifier for the game session to get logs for.\n

    :rtype: dict
ReturnsResponse Syntax{
    'PreSignedUrl': 'string'
}


Response Structure

(dict) --Represents the returned data in response to a request action.

PreSignedUrl (string) --Location of the requested game session logs, available for download. This URL is valid for 15 minutes, after which S3 will reject any download request using this URL. You can request a new URL any time within the 14-day period that the logs are retained.






Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException


    :return: {
        'PreSignedUrl': 'string'
    }
    
    
    :returns: 
    GameLift.Client.exceptions.InternalServiceException
    GameLift.Client.exceptions.NotFoundException
    GameLift.Client.exceptions.UnauthorizedException
    GameLift.Client.exceptions.InvalidRequestException
    
    """
    pass

def get_instance_access(FleetId=None, InstanceId=None):
    """
    Requests remote access to a fleet instance. Remote access is useful for debugging, gathering benchmarking data, or observing activity in real time.
    To remotely access an instance, you need credentials that match the operating system of the instance. For a Windows instance, Amazon GameLift returns a user name and password as strings for use with a Windows Remote Desktop client. For a Linux instance, Amazon GameLift returns a user name and RSA private key, also as strings, for use with an SSH client. The private key must be saved in the proper format to a .pem file before using. If you\'re making this request using the AWS CLI, saving the secret can be handled as part of the GetInstanceAccess request, as shown in one of the examples for this action.
    To request access to a specific instance, specify the IDs of both the instance and the fleet it belongs to. You can retrieve a fleet\'s instance IDs by calling  DescribeInstances . If successful, an  InstanceAccess object is returned that contains the instance\'s IP address and a set of credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_instance_access(
        FleetId='string',
        InstanceId='string'
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet that contains the instance you want access to. You can use either the fleet ID or ARN value. The fleet can be in any of the following statuses: ACTIVATING , ACTIVE , or ERROR . Fleets with an ERROR status may be accessible for a short time before they are deleted.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nA unique identifier for an instance you want to get access to. You can access an instance in any status.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'InstanceAccess': {
        'FleetId': 'string',
        'InstanceId': 'string',
        'IpAddress': 'string',
        'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
        'Credentials': {
            'UserName': 'string',
            'Secret': 'string'
        }
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

InstanceAccess (dict) --
The connection information for a fleet instance, including IP address and access credentials.

FleetId (string) --
A unique identifier for a fleet containing the instance being accessed.

InstanceId (string) --
A unique identifier for an instance being accessed.

IpAddress (string) --
IP address that is assigned to the instance.

OperatingSystem (string) --
Operating system that is running on the instance.

Credentials (dict) --
Credentials required to access the instance.

UserName (string) --
User login string.

Secret (string) --
Secret string. For Windows instances, the secret is a password for use with Windows Remote Desktop. For Linux instances, it is a private key (which must be saved as a .pem file) for use with SSH.











Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'InstanceAccess': {
            'FleetId': 'string',
            'InstanceId': 'string',
            'IpAddress': 'string',
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
            'Credentials': {
                'UserName': 'string',
                'Secret': 'string'
            }
        }
    }
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet that contains the instance you want access to. You can use either the fleet ID or ARN value. The fleet can be in any of the following statuses: ACTIVATING , ACTIVE , or ERROR . Fleets with an ERROR status may be accessible for a short time before they are deleted.
    
    InstanceId (string) -- [REQUIRED]
    A unique identifier for an instance you want to get access to. You can access an instance in any status.
    
    
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

def list_aliases(RoutingStrategyType=None, Name=None, Limit=None, NextToken=None):
    """
    Retrieves all aliases for this AWS account. You can filter the result set by alias name and/or routing strategy type. Use the pagination parameters to retrieve results in sequential pages.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_aliases(
        RoutingStrategyType='SIMPLE'|'TERMINAL',
        Name='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type RoutingStrategyType: string
    :param RoutingStrategyType: The routing type to filter results on. Use this parameter to retrieve only aliases with a certain routing type. To retrieve all aliases, leave this parameter empty.\nPossible routing types include the following:\n\nSIMPLE -- The alias resolves to one specific fleet. Use this type when routing to active fleets.\nTERMINAL -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.\n\n

    :type Name: string
    :param Name: A descriptive label that is associated with an alias. Alias names do not need to be unique.

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

Aliases (list) --
A collection of alias resources that match the request parameters.

(dict) --
Properties that describe an alias resource.

CreateAlias
ListAliases
DescribeAlias
UpdateAlias
DeleteAlias
ResolveAlias


AliasId (string) --
A unique identifier for an alias. Alias IDs are unique within a Region.

Name (string) --
A descriptive label that is associated with an alias. Alias names do not need to be unique.

AliasArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift alias resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift alias ARN, the resource ID matches the alias ID value.

Description (string) --
A human-readable description of an alias.

RoutingStrategy (dict) --
The routing configuration, including routing type and fleet target, for the alias.

Type (string) --
The type of routing strategy for the alias.
Possible routing types include the following:

SIMPLE - The alias resolves to one specific fleet. Use this type when routing to active fleets.
TERMINAL - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.


FleetId (string) --
The unique identifier for a fleet that the alias points to. This value is the fleet ID, not the fleet ARN.

Message (string) --
The message text to be used with a terminal routing strategy.



CreationTime (datetime) --
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --
The time that this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").





NextToken (string) --
A token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException


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
    RoutingStrategyType (string) -- The routing type to filter results on. Use this parameter to retrieve only aliases with a certain routing type. To retrieve all aliases, leave this parameter empty.
    Possible routing types include the following:
    
    SIMPLE -- The alias resolves to one specific fleet. Use this type when routing to active fleets.
    TERMINAL -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
    
    
    Name (string) -- A descriptive label that is associated with an alias. Alias names do not need to be unique.
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def list_builds(Status=None, Limit=None, NextToken=None):
    """
    Retrieves build resources for all builds associated with the AWS account in use. You can limit results to builds that are in a specific status by using the Status parameter. Use the pagination parameters to retrieve results in a set of sequential pages.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_builds(
        Status='INITIALIZED'|'READY'|'FAILED',
        Limit=123,
        NextToken='string'
    )
    
    
    :type Status: string
    :param Status: Build status to filter results by. To retrieve all builds, leave this parameter empty.\nPossible build statuses include the following:\n\nINITIALIZED -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.\nREADY -- The game build has been successfully uploaded. You can now create new fleets for this build.\nFAILED -- The game build upload failed. You cannot create new fleets for this build.\n\n

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'Builds': [
        {
            'BuildId': 'string',
            'BuildArn': 'string',
            'Name': 'string',
            'Version': 'string',
            'Status': 'INITIALIZED'|'READY'|'FAILED',
            'SizeOnDisk': 123,
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
            'CreationTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

Builds (list) --
A collection of build resources that match the request.

(dict) --
Properties describing a custom game build.

Related operations


CreateBuild
ListBuilds
DescribeBuild
UpdateBuild
DeleteBuild


BuildId (string) --
A unique identifier for a build.

BuildArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift build resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift build ARN, the resource ID matches the BuildId value.

Name (string) --
A descriptive label that is associated with a build. Build names do not need to be unique. It can be set using  CreateBuild or  UpdateBuild .

Version (string) --
Version information that is associated with a build or script. Version strings do not need to be unique. This value can be set using  CreateBuild or  UpdateBuild .

Status (string) --
Current status of the build.
Possible build statuses include the following:

INITIALIZED -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
READY -- The game build has been successfully uploaded. You can now create new fleets for this build.
FAILED -- The game build upload failed. You cannot create new fleets for this build.


SizeOnDisk (integer) --
File size of the uploaded game build, expressed in bytes. When the build status is INITIALIZED , this value is 0.

OperatingSystem (string) --
Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").





NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'Builds': [
            {
                'BuildId': 'string',
                'BuildArn': 'string',
                'Name': 'string',
                'Version': 'string',
                'Status': 'INITIALIZED'|'READY'|'FAILED',
                'SizeOnDisk': 123,
                'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
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
    
    
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def list_fleets(BuildId=None, ScriptId=None, Limit=None, NextToken=None):
    """
    Retrieves a collection of fleet resources for this AWS account. You can filter the result set to find only those fleets that are deployed with a specific build or script. Use the pagination parameters to retrieve results in sequential pages.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_fleets(
        BuildId='string',
        ScriptId='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type BuildId: string
    :param BuildId: A unique identifier for a build to return fleets for. Use this parameter to return only fleets using a specified build. Use either the build ID or ARN value. To retrieve all fleets, do not include either a BuildId and ScriptID parameter.

    :type ScriptId: string
    :param ScriptId: A unique identifier for a Realtime script to return fleets for. Use this parameter to return only fleets using a specified script. Use either the script ID or ARN value. To retrieve all fleets, leave this parameter empty.

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'FleetIds': [
        'string',
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

FleetIds (list) --
Set of fleet IDs matching the list request. You can retrieve additional information about all returned fleets by passing this result set to a call to  DescribeFleetAttributes ,  DescribeFleetCapacity , or  DescribeFleetUtilization .

(string) --


NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'FleetIds': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    BuildId (string) -- A unique identifier for a build to return fleets for. Use this parameter to return only fleets using a specified build. Use either the build ID or ARN value. To retrieve all fleets, do not include either a BuildId and ScriptID parameter.
    ScriptId (string) -- A unique identifier for a Realtime script to return fleets for. Use this parameter to return only fleets using a specified script. Use either the script ID or ARN value. To retrieve all fleets, leave this parameter empty.
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def list_game_server_groups(Limit=None, NextToken=None):
    """
    Retrieves information on all game servers groups that exist in the current AWS account for the selected region. Use the pagination parameters to retrieve results in a set of sequential pages.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_game_server_groups(
        Limit=123,
        NextToken='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServerGroups': [
        {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'RoleArn': 'string',
            'InstanceDefinitions': [
                {
                    'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                    'WeightedCapacity': 'string'
                },
            ],
            'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
            'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
            'AutoScalingGroupArn': 'string',
            'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
            'StatusReason': 'string',
            'SuspendedActions': [
                'REPLACE_INSTANCE_TYPES',
            ],
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

GameServerGroups (list) --
A collection of game server group objects that match the request.

(dict) --

This data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.

Properties describing a game server group resource. A game server group manages certain properties of a corresponding EC2 Auto Scaling group.
A game server group is created by a successful call to  CreateGameServerGroup and deleted by calling  DeleteGameServerGroup . Game server group activity can be temporarily suspended and resumed by calling  SuspendGameServerGroup and  ResumeGameServerGroup .

GameServerGroupName (string) --
A developer-defined identifier for the game server group. The name is unique per Region per AWS account.

GameServerGroupArn (string) --
A generated unique ID for the game server group.

RoleArn (string) --
The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups. The submitted role is validated to ensure that it contains the necessary permissions for game server groups.

InstanceDefinitions (list) --
The set of EC2 instance types that GameLift FleetIQ can use when rebalancing and autoscaling instances in the group.

(dict) --

This data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.

An allowed instance type for your game server group. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

InstanceType (string) --
An EC2 instance type designation.

WeightedCapacity (string) --
Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by GameLift FleetIQ to calculate the instance type\'s cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see Instance Weighting in the Amazon EC2 Auto Scaling User Guide . Default value is "1".





BalancingStrategy (string) --
The fallback balancing method to use for the game server group when Spot instances in a Region become unavailable or are not viable for game hosting. Once triggered, this method remains active until Spot instances can once again be used. Method options include:

SPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.
SPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.


GameServerProtectionPolicy (string) --
A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running may be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see  DeleteGameServerGroup ). An exception to this is Spot Instances, which may be terminated by AWS regardless of protection status.

AutoScalingGroupArn (string) --
A generated unique ID for the EC2 Auto Scaling group with is associated with this game server group.

Status (string) --
The current status of the game server group. Possible statuses include:

NEW - GameLift FleetIQ has validated the CreateGameServerGroup() request.
ACTIVATING - GameLift FleetIQ is setting up a game server group, which includes creating an autoscaling group in your AWS account.
ACTIVE - The game server group has been successfully created.
DELETE_SCHEDULED - A request to delete the game server group has been received.
DELETING - GameLift FleetIQ has received a valid DeleteGameServerGroup() request and is processing it. GameLift FleetIQ must first complete and release hosts before it deletes the autoscaling group and the game server group.
DELETED - The game server group has been successfully deleted.
ERROR - The asynchronous processes of activating or deleting a game server group has failed, resulting in an error state.


StatusReason (string) --
Additional information about the current game server group status. This information may provide additional insight on groups that in ERROR status.

SuspendedActions (list) --
A list of activities that are currently suspended for this game server group. If this property is empty, all activities are occurring.

(string) --


CreationTime (datetime) --
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --
A time stamp indicating when this game server group was last updated.





NextToken (string) --
A token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'GameServerGroups': [
            {
                'GameServerGroupName': 'string',
                'GameServerGroupArn': 'string',
                'RoleArn': 'string',
                'InstanceDefinitions': [
                    {
                        'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                        'WeightedCapacity': 'string'
                    },
                ],
                'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
                'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
                'AutoScalingGroupArn': 'string',
                'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
                'StatusReason': 'string',
                'SuspendedActions': [
                    'REPLACE_INSTANCE_TYPES',
                ],
                'CreationTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def list_game_servers(GameServerGroupName=None, SortOrder=None, Limit=None, NextToken=None):
    """
    Retrieves information on all game servers that are currently running in a specified game server group. If there are custom key sort values for your game servers, you can opt to have the returned list sorted based on these values. Use the pagination parameters to retrieve results in a set of sequential pages.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_game_servers(
        GameServerGroupName='string',
        SortOrder='ASCENDING'|'DESCENDING',
        Limit=123,
        NextToken='string'
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nAn identifier for the game server group for the game server you want to list. Use either the GameServerGroup name or ARN value.\n

    :type SortOrder: string
    :param SortOrder: Indicates how to sort the returned data based on the game servers\' custom key sort value. If this parameter is left empty, the list of game servers is returned in no particular order.

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServers': [
        {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'GameServerId': 'string',
            'InstanceId': 'string',
            'ConnectionInfo': 'string',
            'GameServerData': 'string',
            'CustomSortKey': 'string',
            'ClaimStatus': 'CLAIMED',
            'UtilizationStatus': 'AVAILABLE'|'UTILIZED',
            'RegistrationTime': datetime(2015, 1, 1),
            'LastClaimTime': datetime(2015, 1, 1),
            'LastHealthCheckTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

GameServers (list) --
A collection of game server objects that match the request.

(dict) --

This data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.

Properties describing a game server resource.
A game server resource is created by a successful call to  RegisterGameServer and deleted by calling  DeregisterGameServer .

GameServerGroupName (string) --
The name identifier for the game server group where the game server is located.

GameServerGroupArn (string) --
The ARN identifier for the game server group where the game server is located.

GameServerId (string) --
A custom string that uniquely identifies the game server. Game server IDs are developer-defined and are unique across all game server groups in an AWS account.

InstanceId (string) --
The unique identifier for the instance where the game server is located.

ConnectionInfo (string) --
The port and IP address that must be used to establish a client connection to the game server.

GameServerData (string) --
A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service in response to requests  ListGameServers or  ClaimGameServer . This property can be updated using  UpdateGameServer .

CustomSortKey (string) --
A game server tag that can be used to request sorted lists of game servers when calling  ListGameServers . Custom sort keys are developer-defined. This property can be updated using  UpdateGameServer .

ClaimStatus (string) --
Indicates when an available game server has been reserved but has not yet started hosting a game. Once it is claimed, game server remains in CLAIMED status for a maximum of one minute. During this time, game clients must connect to the game server and start the game, which triggers the game server to update its utilization status. After one minute, the game server claim status reverts to null.

UtilizationStatus (string) --
Indicates whether the game server is currently available for new games or is busy. Possible statuses include:

AVAILABLE - The game server is available to be claimed. A game server that has been claimed remains in this status until it reports game hosting activity.
IN_USE - The game server is currently hosting a game session with players.


RegistrationTime (datetime) --
Time stamp indicating when the game server resource was created with a  RegisterGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastClaimTime (datetime) --
Time stamp indicating the last time the game server was claimed with a  ClaimGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057"). This value is used to calculate when the game server\'s claim status.

LastHealthCheckTime (datetime) --
Time stamp indicating the last time the game server was updated with health status using an  UpdateGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057"). After game server registration, this property is only changed when a game server update specifies a health check value.





NextToken (string) --
A token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'GameServers': [
            {
                'GameServerGroupName': 'string',
                'GameServerGroupArn': 'string',
                'GameServerId': 'string',
                'InstanceId': 'string',
                'ConnectionInfo': 'string',
                'GameServerData': 'string',
                'CustomSortKey': 'string',
                'ClaimStatus': 'CLAIMED',
                'UtilizationStatus': 'AVAILABLE'|'UTILIZED',
                'RegistrationTime': datetime(2015, 1, 1),
                'LastClaimTime': datetime(2015, 1, 1),
                'LastHealthCheckTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    GameServerGroupName (string) -- [REQUIRED]
    An identifier for the game server group for the game server you want to list. Use either the  GameServerGroup name or ARN value.
    
    SortOrder (string) -- Indicates how to sort the returned data based on the game servers\' custom key sort value. If this parameter is left empty, the list of game servers is returned in no particular order.
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def list_scripts(Limit=None, NextToken=None):
    """
    Retrieves script records for all Realtime scripts that are associated with the AWS account in use.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_scripts(
        Limit=123,
        NextToken='string'
    )
    
    
    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.

    :type NextToken: string
    :param NextToken: A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'Scripts': [
        {
            'ScriptId': 'string',
            'ScriptArn': 'string',
            'Name': 'string',
            'Version': 'string',
            'SizeOnDisk': 123,
            'CreationTime': datetime(2015, 1, 1),
            'StorageLocation': {
                'Bucket': 'string',
                'Key': 'string',
                'RoleArn': 'string',
                'ObjectVersion': 'string'
            }
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Scripts (list) --
A set of properties describing the requested script.

(dict) --
Properties describing a Realtime script.

Related operations


CreateScript
ListScripts
DescribeScript
UpdateScript
DeleteScript


ScriptId (string) --
A unique identifier for a Realtime script

ScriptArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift script resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift script ARN, the resource ID matches the ScriptId value.

Name (string) --
A descriptive label that is associated with a script. Script names do not need to be unique.

Version (string) --
The version that is associated with a build or script. Version strings do not need to be unique.

SizeOnDisk (integer) --
The file size of the uploaded Realtime script, expressed in bytes. When files are uploaded from an S3 location, this value remains at "0".

CreationTime (datetime) --
A time stamp indicating when this data object was created. The format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

StorageLocation (dict) --
The location in S3 where build or script files are stored for access by Amazon GameLift. This location is specified in  CreateBuild ,  CreateScript , and  UpdateScript requests.

Bucket (string) --
An S3 bucket identifier. This is the name of the S3 bucket.

Key (string) --
The name of the zip file that contains the build files or script files.

RoleArn (string) --
The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access the S3 bucket.

ObjectVersion (string) --
The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.







NextToken (string) --
A token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'Scripts': [
            {
                'ScriptId': 'string',
                'ScriptArn': 'string',
                'Name': 'string',
                'Version': 'string',
                'SizeOnDisk': 123,
                'CreationTime': datetime(2015, 1, 1),
                'StorageLocation': {
                    'Bucket': 'string',
                    'Key': 'string',
                    'RoleArn': 'string',
                    'ObjectVersion': 'string'
                }
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    Limit (integer) -- The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages.
    NextToken (string) -- A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.
    
    """
    pass

def list_tags_for_resource(ResourceARN=None):
    """
    Retrieves all tags that are assigned to a GameLift resource. Resource tags are used to organize AWS resources for a range of purposes. This action handles the permissions necessary to manage tags for the following GameLift resource types:
    To list tags for a resource, specify the unique ARN value for the resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceARN='string'
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN ) that is assigned to and uniquely identifies the GameLift resource that you want to retrieve tags for. GameLift resource ARNs are included in the data object for the resource, which can be retrieved by calling a List or Describe action for the resource type.\n

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
Tags (list) --The collection of tags that have been assigned to the specified resource.

(dict) --A label that can be assigned to a GameLift resource.

Learn moreTagging AWS Resources in the AWS General Reference
AWS Tagging Strategies
Related operations


TagResource
UntagResource
ListTagsForResource


Key (string) --The key for a developer-defined key:value pair for tagging an AWS resource.

Value (string) --The value for a developer-defined key:value pair for tagging an AWS resource.










Exceptions

GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.TaggingFailedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'Tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    :returns: 
    TagResource
    UntagResource
    ListTagsForResource
    
    """
    pass

def put_scaling_policy(Name=None, FleetId=None, ScalingAdjustment=None, ScalingAdjustmentType=None, Threshold=None, ComparisonOperator=None, EvaluationPeriods=None, MetricName=None, PolicyType=None, TargetConfiguration=None):
    """
    Creates or updates a scaling policy for a fleet. Scaling policies are used to automatically scale a fleet\'s hosting capacity to meet player demand. An active scaling policy instructs Amazon GameLift to track a fleet metric and automatically change the fleet\'s capacity when a certain threshold is reached. There are two types of scaling policies: target-based and rule-based. Use a target-based policy to quickly and efficiently manage fleet scaling; this option is the most commonly used. Use rule-based policies when you need to exert fine-grained control over auto-scaling.
    Fleets can have multiple scaling policies of each type in force at the same time; you can have one target-based policy, one or multiple rule-based scaling policies, or both. We recommend caution, however, because multiple auto-scaling policies can have unintended consequences.
    You can temporarily suspend all scaling policies for a fleet by calling  StopFleetActions with the fleet action AUTO_SCALING. To resume scaling policies, call  StartFleetActions with the same fleet action. To stop just one scaling policy--or to permanently remove it, you must delete the policy with  DeleteScalingPolicy .
    Learn more about how to work with auto-scaling in Set Up Fleet Automatic Scaling .
    A target-based policy tracks a single metric: PercentAvailableGameSessions. This metric tells us how much of a fleet\'s hosting capacity is ready to host game sessions but is not currently in use. This is the fleet\'s buffer; it measures the additional player demand that the fleet could handle at current capacity. With a target-based policy, you set your ideal buffer size and leave it to Amazon GameLift to take whatever action is needed to maintain that target.
    For example, you might choose to maintain a 10% buffer for a fleet that has the capacity to host 100 simultaneous game sessions. This policy tells Amazon GameLift to take action whenever the fleet\'s available capacity falls below or rises above 10 game sessions. Amazon GameLift will start new instances or stop unused instances in order to return to the 10% buffer.
    To create or update a target-based policy, specify a fleet ID and name, and set the policy type to "TargetBased". Specify the metric to track (PercentAvailableGameSessions) and reference a  TargetConfiguration object with your desired buffer value. Exclude all other parameters. On a successful request, the policy name is returned. The scaling policy is automatically in force as soon as it\'s successfully created. If the fleet\'s auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.
    A rule-based policy tracks specified fleet metric, sets a threshold value, and specifies the type of action to initiate when triggered. With a rule-based policy, you can select from several available fleet metrics. Each policy specifies whether to scale up or scale down (and by how much), so you need one policy for each type of action.
    For example, a policy may make the following statement: "If the percentage of idle instances is greater than 20% for more than 15 minutes, then reduce the fleet capacity by 10%."
    A policy\'s rule statement has the following structure:
    If [MetricName] is [ComparisonOperator] [Threshold] for [EvaluationPeriods] minutes, then [ScalingAdjustmentType] to/by [ScalingAdjustment] .
    To implement the example, the rule statement would look like this:
    If [PercentIdleInstances] is [GreaterThanThreshold] [20] for [15] minutes, then [PercentChangeInCapacity] to/by [10] .
    To create or update a scaling policy, specify a unique combination of name and fleet ID, and set the policy type to "RuleBased". Specify the parameter values for a policy rule statement. On a successful request, the policy name is returned. Scaling policies are automatically in force as soon as they\'re successfully created. If the fleet\'s auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_scaling_policy(
        Name='string',
        FleetId='string',
        ScalingAdjustment=123,
        ScalingAdjustmentType='ChangeInCapacity'|'ExactCapacity'|'PercentChangeInCapacity',
        Threshold=123.0,
        ComparisonOperator='GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold',
        EvaluationPeriods=123,
        MetricName='ActivatingGameSessions'|'ActiveGameSessions'|'ActiveInstances'|'AvailableGameSessions'|'AvailablePlayerSessions'|'CurrentPlayerSessions'|'IdleInstances'|'PercentAvailableGameSessions'|'PercentIdleInstances'|'QueueDepth'|'WaitTime',
        PolicyType='RuleBased'|'TargetBased',
        TargetConfiguration={
            'TargetValue': 123.0
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA descriptive label that is associated with a scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.\n

    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to apply this policy to. You can use either the fleet ID or ARN value. The fleet cannot be in any of the following statuses: ERROR or DELETING.\n

    :type ScalingAdjustment: integer
    :param ScalingAdjustment: Amount of adjustment to make, based on the scaling adjustment type.

    :type ScalingAdjustmentType: string
    :param ScalingAdjustmentType: The type of adjustment to make to a fleet\'s instance count (see FleetCapacity ):\n\nChangeInCapacity -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.\nExactCapacity -- set the instance count to the scaling adjustment value.\nPercentChangeInCapacity -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of '-10' scales the fleet down by 10%.\n\n

    :type Threshold: float
    :param Threshold: Metric value used to trigger a scaling event.

    :type ComparisonOperator: string
    :param ComparisonOperator: Comparison operator to use when measuring the metric against the threshold value.

    :type EvaluationPeriods: integer
    :param EvaluationPeriods: Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.

    :type MetricName: string
    :param MetricName: [REQUIRED]\nName of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see Monitor Amazon GameLift with Amazon CloudWatch .\n\nActivatingGameSessions -- Game sessions in the process of being created.\nActiveGameSessions -- Game sessions that are currently running.\nActiveInstances -- Fleet instances that are currently running at least one game session.\nAvailableGameSessions -- Additional game sessions that fleet could host simultaneously, given current capacity.\nAvailablePlayerSessions -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.\nCurrentPlayerSessions -- Player slots in active game sessions that are being used by a player or are reserved for a player.\nIdleInstances -- Active instances that are currently hosting zero game sessions.\nPercentAvailableGameSessions -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.\nPercentIdleInstances -- Percentage of the total number of active instances that are hosting zero game sessions.\nQueueDepth -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.\nWaitTime -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.\n\n

    :type PolicyType: string
    :param PolicyType: The type of scaling policy to create. For a target-based policy, set the parameter MetricName to \'PercentAvailableGameSessions\' and specify a TargetConfiguration . For a rule-based policy set the following parameters: MetricName , ComparisonOperator , Threshold , EvaluationPeriods , ScalingAdjustmentType , and ScalingAdjustment .

    :type TargetConfiguration: dict
    :param TargetConfiguration: The settings for a target-based scaling policy.\n\nTargetValue (float) -- [REQUIRED]Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet\'s buffer (the percent of capacity that should be idle and ready for new game sessions).\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

Name (string) --
A descriptive label that is associated with a scaling policy. Policy names do not need to be unique.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.NotFoundException


    :return: {
        'Name': 'string'
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A descriptive label that is associated with a scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.
    
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet to apply this policy to. You can use either the fleet ID or ARN value. The fleet cannot be in any of the following statuses: ERROR or DELETING.
    
    ScalingAdjustment (integer) -- Amount of adjustment to make, based on the scaling adjustment type.
    ScalingAdjustmentType (string) -- The type of adjustment to make to a fleet\'s instance count (see  FleetCapacity ):
    
    ChangeInCapacity -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
    ExactCapacity -- set the instance count to the scaling adjustment value.
    PercentChangeInCapacity -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of "-10" scales the fleet down by 10%.
    
    
    Threshold (float) -- Metric value used to trigger a scaling event.
    ComparisonOperator (string) -- Comparison operator to use when measuring the metric against the threshold value.
    EvaluationPeriods (integer) -- Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
    MetricName (string) -- [REQUIRED]
    Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see Monitor Amazon GameLift with Amazon CloudWatch .
    
    ActivatingGameSessions -- Game sessions in the process of being created.
    ActiveGameSessions -- Game sessions that are currently running.
    ActiveInstances -- Fleet instances that are currently running at least one game session.
    AvailableGameSessions -- Additional game sessions that fleet could host simultaneously, given current capacity.
    AvailablePlayerSessions -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
    CurrentPlayerSessions -- Player slots in active game sessions that are being used by a player or are reserved for a player.
    IdleInstances -- Active instances that are currently hosting zero game sessions.
    PercentAvailableGameSessions -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
    PercentIdleInstances -- Percentage of the total number of active instances that are hosting zero game sessions.
    QueueDepth -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
    WaitTime -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
    
    
    PolicyType (string) -- The type of scaling policy to create. For a target-based policy, set the parameter MetricName to \'PercentAvailableGameSessions\' and specify a TargetConfiguration . For a rule-based policy set the following parameters: MetricName , ComparisonOperator , Threshold , EvaluationPeriods , ScalingAdjustmentType , and ScalingAdjustment .
    TargetConfiguration (dict) -- The settings for a target-based scaling policy.
    
    TargetValue (float) -- [REQUIRED]Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet\'s buffer (the percent of capacity that should be idle and ready for new game sessions).
    
    
    
    
    """
    pass

def register_game_server(GameServerGroupName=None, GameServerId=None, InstanceId=None, ConnectionInfo=None, GameServerData=None, CustomSortKey=None, Tags=None):
    """
    Creates a new game server resource and notifies GameLift FleetIQ that the game server is ready to host gameplay and players. This action is called by a game server process that is running on an instance in a game server group. Registering game servers enables GameLift FleetIQ to track available game servers and enables game clients and services to claim a game server for a new game session.
    To register a game server, identify the game server group and instance where the game server is running, and provide a unique identifier for the game server. You can also include connection and game server data; when a game client or service requests a game server by calling  ClaimGameServer , this information is returned in response.
    Once a game server is successfully registered, it is put in status AVAILABLE. A request to register a game server may fail if the instance it is in the process of shutting down as part of instance rebalancing or scale-down activity.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_game_server(
        GameServerGroupName='string',
        GameServerId='string',
        InstanceId='string',
        ConnectionInfo='string',
        GameServerData='string',
        CustomSortKey='string',
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nAn identifier for the game server group where the game server is running. You can use either the GameServerGroup name or ARN value.\n

    :type GameServerId: string
    :param GameServerId: [REQUIRED]\nA custom string that uniquely identifies the new game server. Game server IDs are developer-defined and must be unique across all game server groups in your AWS account.\n

    :type InstanceId: string
    :param InstanceId: [REQUIRED]\nThe unique identifier for the instance where the game server is running. This ID is available in the instance metadata.\n

    :type ConnectionInfo: string
    :param ConnectionInfo: Information needed to make inbound client connections to the game server. This might include IP address and port, DNS name, etc.

    :type GameServerData: string
    :param GameServerData: A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on a game servers using ListGameServers or ClaimGameServer .

    :type CustomSortKey: string
    :param CustomSortKey: A game server tag that can be used to request sorted lists of game servers using ListGameServers . Custom sort keys are developer-defined based on how you want to organize the retrieved game server information.

    :type Tags: list
    :param Tags: A list of labels to assign to the new game server resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management, and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use TagResource , UntagResource , and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.\n\n(dict) --A label that can be assigned to a GameLift resource.\n\nLearn moreTagging AWS Resources in the AWS General Reference\nAWS Tagging Strategies\nRelated operations\n\n\nTagResource\nUntagResource\nListTagsForResource\n\n\nKey (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.\n\nValue (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServer': {
        'GameServerGroupName': 'string',
        'GameServerGroupArn': 'string',
        'GameServerId': 'string',
        'InstanceId': 'string',
        'ConnectionInfo': 'string',
        'GameServerData': 'string',
        'CustomSortKey': 'string',
        'ClaimStatus': 'CLAIMED',
        'UtilizationStatus': 'AVAILABLE'|'UTILIZED',
        'RegistrationTime': datetime(2015, 1, 1),
        'LastClaimTime': datetime(2015, 1, 1),
        'LastHealthCheckTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

GameServer (dict) --
Object that describes the newly created game server resource.

GameServerGroupName (string) --
The name identifier for the game server group where the game server is located.

GameServerGroupArn (string) --
The ARN identifier for the game server group where the game server is located.

GameServerId (string) --
A custom string that uniquely identifies the game server. Game server IDs are developer-defined and are unique across all game server groups in an AWS account.

InstanceId (string) --
The unique identifier for the instance where the game server is located.

ConnectionInfo (string) --
The port and IP address that must be used to establish a client connection to the game server.

GameServerData (string) --
A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service in response to requests  ListGameServers or  ClaimGameServer . This property can be updated using  UpdateGameServer .

CustomSortKey (string) --
A game server tag that can be used to request sorted lists of game servers when calling  ListGameServers . Custom sort keys are developer-defined. This property can be updated using  UpdateGameServer .

ClaimStatus (string) --
Indicates when an available game server has been reserved but has not yet started hosting a game. Once it is claimed, game server remains in CLAIMED status for a maximum of one minute. During this time, game clients must connect to the game server and start the game, which triggers the game server to update its utilization status. After one minute, the game server claim status reverts to null.

UtilizationStatus (string) --
Indicates whether the game server is currently available for new games or is busy. Possible statuses include:

AVAILABLE - The game server is available to be claimed. A game server that has been claimed remains in this status until it reports game hosting activity.
IN_USE - The game server is currently hosting a game session with players.


RegistrationTime (datetime) --
Time stamp indicating when the game server resource was created with a  RegisterGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastClaimTime (datetime) --
Time stamp indicating the last time the game server was claimed with a  ClaimGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057"). This value is used to calculate when the game server\'s claim status.

LastHealthCheckTime (datetime) --
Time stamp indicating the last time the game server was updated with health status using an  UpdateGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057"). After game server registration, this property is only changed when a game server update specifies a health check value.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.LimitExceededException


    :return: {
        'GameServer': {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'GameServerId': 'string',
            'InstanceId': 'string',
            'ConnectionInfo': 'string',
            'GameServerData': 'string',
            'CustomSortKey': 'string',
            'ClaimStatus': 'CLAIMED',
            'UtilizationStatus': 'AVAILABLE'|'UTILIZED',
            'RegistrationTime': datetime(2015, 1, 1),
            'LastClaimTime': datetime(2015, 1, 1),
            'LastHealthCheckTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    GameServerGroupName (string) -- [REQUIRED]
    An identifier for the game server group where the game server is running. You can use either the  GameServerGroup name or ARN value.
    
    GameServerId (string) -- [REQUIRED]
    A custom string that uniquely identifies the new game server. Game server IDs are developer-defined and must be unique across all game server groups in your AWS account.
    
    InstanceId (string) -- [REQUIRED]
    The unique identifier for the instance where the game server is running. This ID is available in the instance metadata.
    
    ConnectionInfo (string) -- Information needed to make inbound client connections to the game server. This might include IP address and port, DNS name, etc.
    GameServerData (string) -- A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on a game servers using  ListGameServers or  ClaimGameServer .
    CustomSortKey (string) -- A game server tag that can be used to request sorted lists of game servers using  ListGameServers . Custom sort keys are developer-defined based on how you want to organize the retrieved game server information.
    Tags (list) -- A list of labels to assign to the new game server resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management, and cost allocation. For more information, see Tagging AWS Resources in the AWS General Reference . Once the resource is created, you can use  TagResource ,  UntagResource , and  ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
    
    (dict) --A label that can be assigned to a GameLift resource.
    
    Learn moreTagging AWS Resources in the AWS General Reference
    AWS Tagging Strategies
    Related operations
    
    
    TagResource
    UntagResource
    ListTagsForResource
    
    
    Key (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.
    
    Value (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.
    
    
    
    
    
    
    """
    pass

def request_upload_credentials(BuildId=None):
    """
    Retrieves a fresh set of credentials for use when uploading a new set of game build files to Amazon GameLift\'s Amazon S3. This is done as part of the build creation process; see  CreateBuild .
    To request new credentials, specify the build ID as returned with an initial CreateBuild request. If successful, a new set of credentials are returned, along with the S3 storage location associated with the build ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.request_upload_credentials(
        BuildId='string'
    )
    
    
    :type BuildId: string
    :param BuildId: [REQUIRED]\nA unique identifier for a build to get credentials for. You can use either the build ID or ARN value.\n

    :rtype: dict
ReturnsResponse Syntax{
    'UploadCredentials': {
        'AccessKeyId': 'string',
        'SecretAccessKey': 'string',
        'SessionToken': 'string'
    },
    'StorageLocation': {
        'Bucket': 'string',
        'Key': 'string',
        'RoleArn': 'string',
        'ObjectVersion': 'string'
    }
}


Response Structure

(dict) --Represents the returned data in response to a request action.

UploadCredentials (dict) --AWS credentials required when uploading a game build to the storage location. These credentials have a limited lifespan and are valid only for the build they were issued for.

AccessKeyId (string) --Temporary key allowing access to the Amazon GameLift S3 account.

SecretAccessKey (string) --Temporary secret key allowing access to the Amazon GameLift S3 account.

SessionToken (string) --Token used to associate a specific build ID with the files uploaded using these credentials.



StorageLocation (dict) --Amazon S3 path and key, identifying where the game build files are stored.

Bucket (string) --An S3 bucket identifier. This is the name of the S3 bucket.

Key (string) --The name of the zip file that contains the build files or script files.

RoleArn (string) --The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access the S3 bucket.

ObjectVersion (string) --The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.








Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'UploadCredentials': {
            'AccessKeyId': 'string',
            'SecretAccessKey': 'string',
            'SessionToken': 'string'
        },
        'StorageLocation': {
            'Bucket': 'string',
            'Key': 'string',
            'RoleArn': 'string',
            'ObjectVersion': 'string'
        }
    }
    
    
    :returns: 
    GameLift.Client.exceptions.UnauthorizedException
    GameLift.Client.exceptions.InvalidRequestException
    GameLift.Client.exceptions.NotFoundException
    GameLift.Client.exceptions.InternalServiceException
    
    """
    pass

def resolve_alias(AliasId=None):
    """
    Retrieves the fleet ID that an alias is currently pointing to.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resolve_alias(
        AliasId='string'
    )
    
    
    :type AliasId: string
    :param AliasId: [REQUIRED]\nThe unique identifier of the alias that you want to retrieve a fleet ID for. You can use either the alias ID or ARN value.\n

    :rtype: dict
ReturnsResponse Syntax{
    'FleetId': 'string',
    'FleetArn': 'string'
}


Response Structure

(dict) --Represents the returned data in response to a request action.

FleetId (string) --The fleet identifier that the alias is pointing to.

FleetArn (string) --The Amazon Resource Name (ARN ) associated with the GameLift fleet resource that this alias points to.






Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.TerminalRoutingStrategyException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'FleetId': 'string',
        'FleetArn': 'string'
    }
    
    
    :returns: 
    GameLift.Client.exceptions.UnauthorizedException
    GameLift.Client.exceptions.InvalidRequestException
    GameLift.Client.exceptions.NotFoundException
    GameLift.Client.exceptions.TerminalRoutingStrategyException
    GameLift.Client.exceptions.InternalServiceException
    
    """
    pass

def resume_game_server_group(GameServerGroupName=None, ResumeActions=None):
    """
    Reinstates activity on a game server group after it has been suspended. A game server group may be suspended by calling  SuspendGameServerGroup , or it may have been involuntarily suspended due to a configuration problem. You can manually resume activity on the group once the configuration problem has been resolved. Refer to the game server group status and status reason for more information on why group activity is suspended.
    To resume activity, specify a game server group ARN and the type of activity to be resumed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.resume_game_server_group(
        GameServerGroupName='string',
        ResumeActions=[
            'REPLACE_INSTANCE_TYPES',
        ]
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nThe unique identifier of the game server group to resume activity on. Use either the GameServerGroup name or ARN value.\n

    :type ResumeActions: list
    :param ResumeActions: [REQUIRED]\nThe action to resume for this game server group.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServerGroup': {
        'GameServerGroupName': 'string',
        'GameServerGroupArn': 'string',
        'RoleArn': 'string',
        'InstanceDefinitions': [
            {
                'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'WeightedCapacity': 'string'
            },
        ],
        'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
        'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
        'AutoScalingGroupArn': 'string',
        'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
        'StatusReason': 'string',
        'SuspendedActions': [
            'REPLACE_INSTANCE_TYPES',
        ],
        'CreationTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

GameServerGroup (dict) --
An object that describes the game server group resource, with the SuspendedActions property updated to reflect the resumed activity.

GameServerGroupName (string) --
A developer-defined identifier for the game server group. The name is unique per Region per AWS account.

GameServerGroupArn (string) --
A generated unique ID for the game server group.

RoleArn (string) --
The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups. The submitted role is validated to ensure that it contains the necessary permissions for game server groups.

InstanceDefinitions (list) --
The set of EC2 instance types that GameLift FleetIQ can use when rebalancing and autoscaling instances in the group.

(dict) --

This data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.

An allowed instance type for your game server group. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

InstanceType (string) --
An EC2 instance type designation.

WeightedCapacity (string) --
Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by GameLift FleetIQ to calculate the instance type\'s cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see Instance Weighting in the Amazon EC2 Auto Scaling User Guide . Default value is "1".





BalancingStrategy (string) --
The fallback balancing method to use for the game server group when Spot instances in a Region become unavailable or are not viable for game hosting. Once triggered, this method remains active until Spot instances can once again be used. Method options include:

SPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.
SPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.


GameServerProtectionPolicy (string) --
A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running may be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see  DeleteGameServerGroup ). An exception to this is Spot Instances, which may be terminated by AWS regardless of protection status.

AutoScalingGroupArn (string) --
A generated unique ID for the EC2 Auto Scaling group with is associated with this game server group.

Status (string) --
The current status of the game server group. Possible statuses include:

NEW - GameLift FleetIQ has validated the CreateGameServerGroup() request.
ACTIVATING - GameLift FleetIQ is setting up a game server group, which includes creating an autoscaling group in your AWS account.
ACTIVE - The game server group has been successfully created.
DELETE_SCHEDULED - A request to delete the game server group has been received.
DELETING - GameLift FleetIQ has received a valid DeleteGameServerGroup() request and is processing it. GameLift FleetIQ must first complete and release hosts before it deletes the autoscaling group and the game server group.
DELETED - The game server group has been successfully deleted.
ERROR - The asynchronous processes of activating or deleting a game server group has failed, resulting in an error state.


StatusReason (string) --
Additional information about the current game server group status. This information may provide additional insight on groups that in ERROR status.

SuspendedActions (list) --
A list of activities that are currently suspended for this game server group. If this property is empty, all activities are occurring.

(string) --


CreationTime (datetime) --
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --
A time stamp indicating when this game server group was last updated.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'GameServerGroup': {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'RoleArn': 'string',
            'InstanceDefinitions': [
                {
                    'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                    'WeightedCapacity': 'string'
                },
            ],
            'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
            'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
            'AutoScalingGroupArn': 'string',
            'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
            'StatusReason': 'string',
            'SuspendedActions': [
                'REPLACE_INSTANCE_TYPES',
            ],
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    GameServerGroupName (string) -- [REQUIRED]
    The unique identifier of the game server group to resume activity on. Use either the  GameServerGroup name or ARN value.
    
    ResumeActions (list) -- [REQUIRED]
    The action to resume for this game server group.
    
    (string) --
    
    
    
    """
    pass

def search_game_sessions(FleetId=None, AliasId=None, FilterExpression=None, SortExpression=None, Limit=None, NextToken=None):
    """
    Retrieves all active game sessions that match a set of search criteria and sorts them in a specified order. You can search or sort by the following game session attributes:
    To search or sort, specify either a fleet ID or an alias ID, and provide a search filter expression, a sort expression, or both. If successful, a collection of  GameSession objects matching the request is returned. Use the pagination parameters to retrieve results as a set of sequential pages.
    You can search for game sessions one fleet at a time only. To find game sessions across multiple fleets, you must search each fleet separately and combine the results. This search feature finds only game sessions that are in ACTIVE status. To locate games in statuses other than active, use  DescribeGameSessionDetails .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_game_sessions(
        FleetId='string',
        AliasId='string',
        FilterExpression='string',
        SortExpression='string',
        Limit=123,
        NextToken='string'
    )
    
    
    :type FleetId: string
    :param FleetId: A unique identifier for a fleet to search for active game sessions. You can use either the fleet ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.

    :type AliasId: string
    :param AliasId: A unique identifier for an alias associated with the fleet to search for active game sessions. You can use either the alias ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.

    :type FilterExpression: string
    :param FilterExpression: String containing the search criteria for the session search. If no filter expression is included, the request returns results for all game sessions in the fleet that are in ACTIVE status.\nA filter expression can contain one or multiple conditions. Each condition consists of the following:\n\nOperand -- Name of a game session attribute. Valid values are gameSessionName , gameSessionId , gameSessionProperties , maximumSessions , creationTimeMillis , playerSessionCount , hasAvailablePlayerSessions .\nComparator -- Valid comparators are: = , <> , < , > , <= , >= .\nValue -- Value to be searched for. Values may be numbers, boolean values (true/false) or strings depending on the operand. String values are case sensitive and must be enclosed in single quotes. Special characters must be escaped. Boolean and string values can only be used with the comparators = and <> . For example, the following filter expression searches on gameSessionName : 'FilterExpression': 'gameSessionName = \'Matt\\\\\'s Awesome Game 1\'' .\n\nTo chain multiple conditions in a single expression, use the logical keywords AND , OR , and NOT and parentheses as needed. For example: x AND y AND NOT z , NOT (x OR y) .\nSession search evaluates conditions from left to right using the following precedence rules:\n\n= , <> , < , > , <= , >=\nParentheses\nNOT\nAND\nOR\n\nFor example, this filter expression retrieves game sessions hosting at least ten players that have an open player slot: 'maximumSessions>=10 AND hasAvailablePlayerSessions=true' .\n

    :type SortExpression: string
    :param SortExpression: Instructions on how to sort the search results. If no sort expression is included, the request returns results in random order. A sort expression consists of the following elements:\n\nOperand -- Name of a game session attribute. Valid values are gameSessionName , gameSessionId , gameSessionProperties , maximumSessions , creationTimeMillis , playerSessionCount , hasAvailablePlayerSessions .\nOrder -- Valid sort orders are ASC (ascending) and DESC (descending).\n\nFor example, this sort expression returns the oldest active sessions first: 'SortExpression': 'creationTimeMillis ASC' . Results with a null value for the sort operand are returned at the end of the list.\n

    :type Limit: integer
    :param Limit: The maximum number of results to return. Use this parameter with NextToken to get results as a set of sequential pages. The maximum number of results returned is 20, even if this value is not set or is set higher than 20.

    :type NextToken: string
    :param NextToken: Token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this action. To start at the beginning of the result set, do not specify a value.

    :rtype: dict

ReturnsResponse Syntax
{
    'GameSessions': [
        {
            'GameSessionId': 'string',
            'Name': 'string',
            'FleetId': 'string',
            'FleetArn': 'string',
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
            'DnsName': 'string',
            'Port': 123,
            'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
            'CreatorId': 'string',
            'GameSessionData': 'string',
            'MatchmakerData': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

GameSessions (list) --
A collection of objects containing game session properties for each session matching the request.

(dict) --
Properties describing a game session.
A game session in ACTIVE status can host players. When a game session ends, its status is set to TERMINATED .
Once the session ends, the game session object is retained for 30 days. This means you can reuse idempotency token values after this time. Game session logs are retained for 14 days.

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




GameSessionId (string) --
A unique identifier for the game session. A game session ARN has the following format: arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token> .

Name (string) --
A descriptive label that is associated with a game session. Session names do not need to be unique.

FleetId (string) --
A unique identifier for a fleet that the game session is running on.

FleetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift fleet that this game session is running on.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

TerminationTime (datetime) --
Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

CurrentPlayerSessionCount (integer) --
Number of players currently in the game session.

MaximumPlayerSessionCount (integer) --
The maximum number of players that can be connected simultaneously to the game session.

Status (string) --
Current status of the game session. A game session must have an ACTIVE status to have player sessions.

StatusReason (string) --
Provides additional information about game session status. INTERRUPTED indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.

GameProperties (list) --
Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). You can search for active game sessions based on this custom data with  SearchGameSessions .

(dict) --
Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --
The game property identifier.

Value (string) --
The game property value.





IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

PlayerSessionCreationPolicy (string) --
Indicates whether or not the game session is accepting new players.

CreatorId (string) --
A unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.

GameSessionData (string) --
Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

MatchmakerData (string) --
Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see Match Data . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ).





NextToken (string) --
Token that indicates where to resume retrieving results on the next call to this action. If no token is returned, these results represent the end of the list.







Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.TerminalRoutingStrategyException


    :return: {
        'GameSessions': [
            {
                'GameSessionId': 'string',
                'Name': 'string',
                'FleetId': 'string',
                'FleetArn': 'string',
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
                'DnsName': 'string',
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

def start_fleet_actions(FleetId=None, Actions=None):
    """
    Resumes activity on a fleet that was suspended with  StopFleetActions . Currently, this operation is used to restart a fleet\'s auto-scaling activity.
    To start fleet actions, specify the fleet ID and the type of actions to restart. When auto-scaling fleet actions are restarted, Amazon GameLift once again initiates scaling events as triggered by the fleet\'s scaling policies. If actions on the fleet were never stopped, this operation will have no effect. You can view a fleet\'s stopped actions using  DescribeFleetAttributes .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_fleet_actions(
        FleetId='string',
        Actions=[
            'AUTO_SCALING',
        ]
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to start actions on. You can use either the fleet ID or ARN value.\n

    :type Actions: list
    :param Actions: [REQUIRED]\nList of actions to restart on the fleet.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet to start actions on. You can use either the fleet ID or ARN value.
    
    Actions (list) -- [REQUIRED]
    List of actions to restart on the fleet.
    
    (string) --
    
    
    
    """
    pass

def start_game_session_placement(PlacementId=None, GameSessionQueueName=None, GameProperties=None, MaximumPlayerSessionCount=None, GameSessionName=None, PlayerLatencies=None, DesiredPlayerSessions=None, GameSessionData=None):
    """
    Places a request for a new game session in a queue (see  CreateGameSessionQueue ). When processing a placement request, Amazon GameLift searches for available resources on the queue\'s destinations, scanning each until it finds resources or the placement request times out.
    A game session placement request can also request player sessions. When a new game session is successfully created, Amazon GameLift creates a player session for each player included in the request.
    When placing a game session, by default Amazon GameLift tries each fleet in the order they are listed in the queue configuration. Ideally, a queue\'s destinations are listed in preference order.
    Alternatively, when requesting a game session with players, you can also provide latency data for each player in relevant Regions. Latency data indicates the performance lag a player experiences when connected to a fleet in the Region. Amazon GameLift uses latency data to reorder the list of destinations to place the game session in a Region with minimal lag. If latency data is provided for multiple players, Amazon GameLift calculates each Region\'s average lag for all players and reorders to get the best game play across all players.
    To place a new game session request, specify the following:
    If successful, a new game session placement is created.
    To track the status of a placement request, call  DescribeGameSessionPlacement and check the request\'s status. If the status is FULFILLED , a new game session has been created and a game session ARN and Region are referenced. If the placement request times out, you can resubmit the request or retry it with a different queue.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param PlacementId: [REQUIRED]\nA unique identifier to assign to the new game session placement. This value is developer-defined. The value must be unique across all Regions and cannot be reused unless you are resubmitting a canceled or timed-out placement request.\n

    :type GameSessionQueueName: string
    :param GameSessionQueueName: [REQUIRED]\nName of the queue to use to place the new game session. You can use either the queue name or ARN value.\n

    :type GameProperties: list
    :param GameProperties: Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ).\n\n(dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .\n\nKey (string) -- [REQUIRED]The game property identifier.\n\nValue (string) -- [REQUIRED]The game property value.\n\n\n\n\n

    :type MaximumPlayerSessionCount: integer
    :param MaximumPlayerSessionCount: [REQUIRED]\nThe maximum number of players that can be connected simultaneously to the game session.\n

    :type GameSessionName: string
    :param GameSessionName: A descriptive label that is associated with a game session. Session names do not need to be unique.

    :type PlayerLatencies: list
    :param PlayerLatencies: Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions. This information is used to try to place the new game session where it can offer the best possible gameplay experience for the players.\n\n(dict) --Regional latency information for a player, used when requesting a new game session with StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified Region. The relative difference between a player\'s latency values for multiple Regions are used to determine which fleets are best suited to place a new game session for the player.\n\nPlayerId (string) --A unique identifier for a player associated with the latency data.\n\nRegionIdentifier (string) --Name of the Region that is associated with the latency value.\n\nLatencyInMilliseconds (float) --Amount of time that represents the time lag experienced by the player when connected to the specified Region.\n\n\n\n\n

    :type DesiredPlayerSessions: list
    :param DesiredPlayerSessions: Set of information on each player to create a player session for.\n\n(dict) --Player information for use when creating player sessions using a game session placement request with StartGameSessionPlacement .\n\nPlayerId (string) --A unique identifier for a player to associate with the player session.\n\nPlayerData (string) --Developer-defined information related to a player. Amazon GameLift does not use this data, so it can be formatted as needed for use in the game.\n\n\n\n\n

    :type GameSessionData: string
    :param GameSessionData: Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ).

    :rtype: dict

ReturnsResponse Syntax
{
    'GameSessionPlacement': {
        'PlacementId': 'string',
        'GameSessionQueueName': 'string',
        'Status': 'PENDING'|'FULFILLED'|'CANCELLED'|'TIMED_OUT'|'FAILED',
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
        'DnsName': 'string',
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

GameSessionPlacement (dict) --
Object that describes the newly created game session placement. This object includes all the information provided in the request, as well as start/end time stamps and placement status.

PlacementId (string) --
A unique identifier for a game session placement.

GameSessionQueueName (string) --
A descriptive label that is associated with game session queue. Queue names must be unique within each Region.

Status (string) --
Current status of the game session placement request.

PENDING -- The placement request is currently in the queue waiting to be processed.
FULFILLED -- A new game session and player sessions (if requested) have been successfully created. Values for GameSessionArn and GameSessionRegion are available.
CANCELLED -- The placement request was canceled with a call to  StopGameSessionPlacement .
TIMED_OUT -- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed.
FAILED -- GameLift is not able to complete the process of placing the game session. Common reasons are the game session terminated before the placement process was completed, or an unexpected internal error.


GameProperties (list) --
Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

(dict) --
Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --
The game property identifier.

Value (string) --
The game property value.





MaximumPlayerSessionCount (integer) --
The maximum number of players that can be connected simultaneously to the game session.

GameSessionName (string) --
A descriptive label that is associated with a game session. Session names do not need to be unique.

GameSessionId (string) --
A unique identifier for the game session. This value is set once the new game session is placed (placement status is FULFILLED ).

GameSessionArn (string) --
Identifier for the game session created by this placement request. This value is set once the new game session is placed (placement status is FULFILLED ). This identifier is unique across all Regions. You can use this value as a GameSessionId value as needed.

GameSessionRegion (string) --
Name of the Region where the game session created by this placement request is running. This value is set once the new game session is placed (placement status is FULFILLED ).

PlayerLatencies (list) --
Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions.

(dict) --
Regional latency information for a player, used when requesting a new game session with  StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified Region. The relative difference between a player\'s latency values for multiple Regions are used to determine which fleets are best suited to place a new game session for the player.

PlayerId (string) --
A unique identifier for a player associated with the latency data.

RegionIdentifier (string) --
Name of the Region that is associated with the latency value.

LatencyInMilliseconds (float) --
Amount of time that represents the time lag experienced by the player when connected to the specified Region.





StartTime (datetime) --
Time stamp indicating when this request was placed in the queue. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

EndTime (datetime) --
Time stamp indicating when this request was completed, canceled, or timed out.

IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number. This value is set once the new game session is placed (placement status is FULFILLED ).

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value is set once the new game session is placed (placement status is FULFILLED ).

PlacedPlayerSessions (list) --
A collection of information on player sessions created in response to the game session placement request. These player sessions are created only once a new game session is successfully placed (placement status is FULFILLED ). This information includes the player ID (as provided in the placement request) and the corresponding player session ID. Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.

(dict) --
Information about a player session that was created as part of a  StartGameSessionPlacement request. This object contains only the player ID and player session ID. To retrieve full details on a player session, call  DescribePlayerSessions with the player session ID.

CreatePlayerSession
CreatePlayerSessions
DescribePlayerSessions
Game session placements
StartGameSessionPlacement
DescribeGameSessionPlacement
StopGameSessionPlacement




PlayerId (string) --
A unique identifier for a player that is associated with this player session.

PlayerSessionId (string) --
A unique identifier for a player session.





GameSessionData (string) --
Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

MatchmakerData (string) --
Information on the matchmaking process for this game. Data is in JSON syntax, formatted as a string. It identifies the matchmaking configuration used to create the match, and contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see Match Data .









Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'GameSessionPlacement': {
            'PlacementId': 'string',
            'GameSessionQueueName': 'string',
            'Status': 'PENDING'|'FULFILLED'|'CANCELLED'|'TIMED_OUT'|'FAILED',
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
            'DnsName': 'string',
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
    To request a match backfill, specify a unique ticket ID, the existing game session\'s ARN, a matchmaking configuration, and a set of data that describes all current players in the game session. If successful, a match backfill ticket is created and returned with status set to QUEUED. The ticket is placed in the matchmaker\'s ticket pool and processed. Track the status of the ticket to respond as needed.
    The process of finding backfill matches is essentially identical to the initial matchmaking process. The matchmaker searches the pool and groups tickets together to form potential matches, allowing only one backfill ticket per potential match. Once the a match is formed, the matchmaker creates player sessions for the new players. All tickets in the match are updated with the game session\'s connection information, and the  GameSession object is updated to include matchmaker data on the new players. For more detail on how match backfill requests are processed, see How Amazon GameLift FlexMatch Works .
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param TicketId: A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift will generate one in the form of a UUID. Use this identifier to track the match backfill ticket status and retrieve match results.

    :type ConfigurationName: string
    :param ConfigurationName: [REQUIRED]\nName of the matchmaker to use for this request. You can use either the configuration name or ARN value. The ARN of the matchmaker that was used with the original game session is listed in the GameSession object, MatchmakerData property.\n

    :type GameSessionArn: string
    :param GameSessionArn: [REQUIRED]\nAmazon Resource Name (ARN ) that is assigned to a game session and uniquely identifies it. This is the same as the game session ID.\n

    :type Players: list
    :param Players: [REQUIRED]\nMatch information on all players that are currently assigned to the game session. This information is used by the matchmaker to find new players and add them to the existing game.\n\nPlayerID, PlayerAttributes, Team -\\- This information is maintained in the GameSession object, MatchmakerData property, for all players who are currently assigned to the game session. The matchmaker data is in JSON syntax, formatted as a string. For more details, see Match Data .\nLatencyInMs -\\- If the matchmaker uses player latency, include a latency value, in milliseconds, for the Region that the game session is currently in. Do not include latency values for any other Region.\n\n\n(dict) --Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.\n\nPlayerId (string) --A unique identifier for a player\n\nPlayerAttributes (dict) --A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the playerAttributes used in a matchmaking rule set. Example: 'PlayerAttributes': {'skill': {'N': '23'}, 'gameMode': {'S': 'deathmatch'}} .\n\n(string) --\n(dict) --Values for use in Player attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each AttributeValue object can use only one of the available properties.\n\nS (string) --For single string values. Maximum string length is 100 characters.\n\nN (float) --For number values, expressed as double.\n\nSL (list) --For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.\n\n(string) --\n\n\nSDM (dict) --For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.\n\n(string) --\n(float) --\n\n\n\n\n\n\n\n\n\n\nTeam (string) --Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.\n\nLatencyInMs (dict) --Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions. If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported.\nIf a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable.\n\n(string) --\n(integer) --\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'MatchmakingTicket': {
        'TicketId': 'string',
        'ConfigurationName': 'string',
        'ConfigurationArn': 'string',
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
            'DnsName': 'string',
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

MatchmakingTicket (dict) --
Ticket representing the backfill matchmaking request. This object includes the information in the request, ticket status, and match results as generated during the matchmaking process.

TicketId (string) --
A unique identifier for a matchmaking ticket.

ConfigurationName (string) --
Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking configurations determine how players are grouped into a match and how a new game session is created for the match.

ConfigurationArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift matchmaking configuration resource that is used with this ticket.

Status (string) --
Current status of the matchmaking request.

QUEUED -- The matchmaking request has been received and is currently waiting to be processed.
SEARCHING -- The matchmaking request is currently being processed.
REQUIRES_ACCEPTANCE -- A match has been proposed and the players must accept the match (see  AcceptMatch ). This status is used only with requests that use a matchmaking configuration with a player acceptance requirement.
PLACING -- The FlexMatch engine has matched players and is in the process of placing a new game session for the match.
COMPLETED -- Players have been matched and a game session is ready to host the players. A ticket in this state contains the necessary connection information for players.
FAILED -- The matchmaking request was not completed.
CANCELLED -- The matchmaking request was canceled. This may be the result of a call to  StopMatchmaking or a proposed match that one or more players failed to accept.
TIMED_OUT -- The matchmaking request was not successful within the duration specified in the matchmaking configuration.


Note
Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED, TIMED_OUT) can be resubmitted as new requests with new ticket IDs.


StatusReason (string) --
Code to explain the current status. For example, a status reason may indicate when a ticket has returned to SEARCHING status after a proposed match fails to receive player acceptances.

StatusMessage (string) --
Additional information about the current status.

StartTime (datetime) --
Time stamp indicating when this matchmaking request was received. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

EndTime (datetime) --
Time stamp indicating when this matchmaking request stopped being processed due to success, failure, or cancellation. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

Players (list) --
A set of Player objects, each representing a player to find matches for. Players are identified by a unique player ID and may include latency data for use during matchmaking. If the ticket is in status COMPLETED , the Player objects include the team the players were assigned to in the resulting match.

(dict) --
Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.

PlayerId (string) --
A unique identifier for a player

PlayerAttributes (dict) --
A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the playerAttributes used in a matchmaking rule set. Example: "PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}} .

(string) --

(dict) --
Values for use in  Player attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each AttributeValue object can use only one of the available properties.

S (string) --
For single string values. Maximum string length is 100 characters.

N (float) --
For number values, expressed as double.

SL (list) --
For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.

(string) --


SDM (dict) --
For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.

(string) --
(float) --










Team (string) --
Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.

LatencyInMs (dict) --
Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions. If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported.
If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable.

(string) --
(integer) --








GameSessionConnectionInfo (dict) --
Identifier and connection information of the game session created for the match. This information is added to the ticket only after the matchmaking request has been successfully completed.

GameSessionArn (string) --
Amazon Resource Name (ARN ) that is assigned to a game session and uniquely identifies it.

IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

MatchedPlayerSessions (list) --
A collection of player session IDs, one for each player ID that was included in the original matchmaking request.

(dict) --
Represents a new player session that is created as a result of a successful FlexMatch match. A successful match automatically creates new player sessions for every player ID in the original matchmaking request.
When players connect to the match\'s game session, they must include both player ID and player session ID in order to claim their assigned player slot.

PlayerId (string) --
A unique identifier for a player

PlayerSessionId (string) --
A unique identifier for a player session







EstimatedWaitTime (integer) --
Average amount of time (in seconds) that players are currently waiting for a match. If there is not enough recent data, this property may be empty.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException


    :return: {
        'MatchmakingTicket': {
            'TicketId': 'string',
            'ConfigurationName': 'string',
            'ConfigurationArn': 'string',
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
                'DnsName': 'string',
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
    TicketId (string) -- A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift will generate one in the form of a UUID. Use this identifier to track the match backfill ticket status and retrieve match results.
    ConfigurationName (string) -- [REQUIRED]
    Name of the matchmaker to use for this request. You can use either the configuration name or ARN value. The ARN of the matchmaker that was used with the original game session is listed in the  GameSession object, MatchmakerData property.
    
    GameSessionArn (string) -- [REQUIRED]
    Amazon Resource Name (ARN ) that is assigned to a game session and uniquely identifies it. This is the same as the game session ID.
    
    Players (list) -- [REQUIRED]
    Match information on all players that are currently assigned to the game session. This information is used by the matchmaker to find new players and add them to the existing game.
    
    PlayerID, PlayerAttributes, Team -\\- This information is maintained in the  GameSession object, MatchmakerData property, for all players who are currently assigned to the game session. The matchmaker data is in JSON syntax, formatted as a string. For more details, see Match Data .
    LatencyInMs -\\- If the matchmaker uses player latency, include a latency value, in milliseconds, for the Region that the game session is currently in. Do not include latency values for any other Region.
    
    
    (dict) --Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.
    
    PlayerId (string) --A unique identifier for a player
    
    PlayerAttributes (dict) --A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the playerAttributes used in a matchmaking rule set. Example: "PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}} .
    
    (string) --
    (dict) --Values for use in  Player attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each AttributeValue object can use only one of the available properties.
    
    S (string) --For single string values. Maximum string length is 100 characters.
    
    N (float) --For number values, expressed as double.
    
    SL (list) --For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.
    
    (string) --
    
    
    SDM (dict) --For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.
    
    (string) --
    (float) --
    
    
    
    
    
    
    
    
    
    
    Team (string) --Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.
    
    LatencyInMs (dict) --Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions. If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported.
    If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable.
    
    (string) --
    (integer) --
    
    
    
    
    
    
    
    
    
    """
    pass

def start_matchmaking(TicketId=None, ConfigurationName=None, Players=None):
    """
    Uses FlexMatch to create a game match for a group of players based on custom matchmaking rules, and starts a new game for the matched players. Each matchmaking request specifies the type of match to build (team configuration, rules for an acceptable match, etc.). The request also specifies the players to find a match for and where to host the new game session for optimal performance. A matchmaking request might start with a single player or a group of players who want to play together. FlexMatch finds additional players as needed to fill the match. Match type, rules, and the queue used to place a new game session are defined in a MatchmakingConfiguration .
    To start matchmaking, provide a unique ticket ID, specify a matchmaking configuration, and include the players to be matched. You must also include a set of player attributes relevant for the matchmaking configuration. If successful, a matchmaking ticket is returned with status set to QUEUED . Track the status of the ticket to respond as needed and acquire game session connection information for successfully completed matches.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param TicketId: A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift will generate one in the form of a UUID. Use this identifier to track the matchmaking ticket status and retrieve match results.

    :type ConfigurationName: string
    :param ConfigurationName: [REQUIRED]\nName of the matchmaking configuration to use for this request. Matchmaking configurations must exist in the same Region as this request. You can use either the configuration name or ARN value.\n

    :type Players: list
    :param Players: [REQUIRED]\nInformation on each player to be matched. This information must include a player ID, and may contain player attributes and latency data to be used in the matchmaking process. After a successful match, Player objects contain the name of the team the player is assigned to.\n\n(dict) --Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.\n\nPlayerId (string) --A unique identifier for a player\n\nPlayerAttributes (dict) --A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the playerAttributes used in a matchmaking rule set. Example: 'PlayerAttributes': {'skill': {'N': '23'}, 'gameMode': {'S': 'deathmatch'}} .\n\n(string) --\n(dict) --Values for use in Player attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each AttributeValue object can use only one of the available properties.\n\nS (string) --For single string values. Maximum string length is 100 characters.\n\nN (float) --For number values, expressed as double.\n\nSL (list) --For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.\n\n(string) --\n\n\nSDM (dict) --For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.\n\n(string) --\n(float) --\n\n\n\n\n\n\n\n\n\n\nTeam (string) --Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.\n\nLatencyInMs (dict) --Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions. If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported.\nIf a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable.\n\n(string) --\n(integer) --\n\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'MatchmakingTicket': {
        'TicketId': 'string',
        'ConfigurationName': 'string',
        'ConfigurationArn': 'string',
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
            'DnsName': 'string',
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

MatchmakingTicket (dict) --
Ticket representing the matchmaking request. This object include the information included in the request, ticket status, and match results as generated during the matchmaking process.

TicketId (string) --
A unique identifier for a matchmaking ticket.

ConfigurationName (string) --
Name of the  MatchmakingConfiguration that is used with this ticket. Matchmaking configurations determine how players are grouped into a match and how a new game session is created for the match.

ConfigurationArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift matchmaking configuration resource that is used with this ticket.

Status (string) --
Current status of the matchmaking request.

QUEUED -- The matchmaking request has been received and is currently waiting to be processed.
SEARCHING -- The matchmaking request is currently being processed.
REQUIRES_ACCEPTANCE -- A match has been proposed and the players must accept the match (see  AcceptMatch ). This status is used only with requests that use a matchmaking configuration with a player acceptance requirement.
PLACING -- The FlexMatch engine has matched players and is in the process of placing a new game session for the match.
COMPLETED -- Players have been matched and a game session is ready to host the players. A ticket in this state contains the necessary connection information for players.
FAILED -- The matchmaking request was not completed.
CANCELLED -- The matchmaking request was canceled. This may be the result of a call to  StopMatchmaking or a proposed match that one or more players failed to accept.
TIMED_OUT -- The matchmaking request was not successful within the duration specified in the matchmaking configuration.


Note
Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED, TIMED_OUT) can be resubmitted as new requests with new ticket IDs.


StatusReason (string) --
Code to explain the current status. For example, a status reason may indicate when a ticket has returned to SEARCHING status after a proposed match fails to receive player acceptances.

StatusMessage (string) --
Additional information about the current status.

StartTime (datetime) --
Time stamp indicating when this matchmaking request was received. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

EndTime (datetime) --
Time stamp indicating when this matchmaking request stopped being processed due to success, failure, or cancellation. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

Players (list) --
A set of Player objects, each representing a player to find matches for. Players are identified by a unique player ID and may include latency data for use during matchmaking. If the ticket is in status COMPLETED , the Player objects include the team the players were assigned to in the resulting match.

(dict) --
Represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and may have latency data. Team information is added after a match has been successfully completed.

PlayerId (string) --
A unique identifier for a player

PlayerAttributes (dict) --
A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the playerAttributes used in a matchmaking rule set. Example: "PlayerAttributes": {"skill": {"N": "23"}, "gameMode": {"S": "deathmatch"}} .

(string) --

(dict) --
Values for use in  Player attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each AttributeValue object can use only one of the available properties.

S (string) --
For single string values. Maximum string length is 100 characters.

N (float) --
For number values, expressed as double.

SL (list) --
For a list of up to 10 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.

(string) --


SDM (dict) --
For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters.

(string) --
(float) --










Team (string) --
Name of the team that the player is assigned to in a match. Team names are defined in a matchmaking rule set.

LatencyInMs (dict) --
Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions. If this property is present, FlexMatch considers placing the match only in Regions for which latency is reported.
If a matchmaker has a rule that evaluates player latency, players must report latency in order to be matched. If no latency is reported in this scenario, FlexMatch assumes that no Regions are available to the player and the ticket is not matchable.

(string) --
(integer) --








GameSessionConnectionInfo (dict) --
Identifier and connection information of the game session created for the match. This information is added to the ticket only after the matchmaking request has been successfully completed.

GameSessionArn (string) --
Amazon Resource Name (ARN ) that is assigned to a game session and uniquely identifies it.

IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

MatchedPlayerSessions (list) --
A collection of player session IDs, one for each player ID that was included in the original matchmaking request.

(dict) --
Represents a new player session that is created as a result of a successful FlexMatch match. A successful match automatically creates new player sessions for every player ID in the original matchmaking request.
When players connect to the match\'s game session, they must include both player ID and player session ID in order to claim their assigned player slot.

PlayerId (string) --
A unique identifier for a player

PlayerSessionId (string) --
A unique identifier for a player session







EstimatedWaitTime (integer) --
Average amount of time (in seconds) that players are currently waiting for a match. If there is not enough recent data, this property may be empty.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException


    :return: {
        'MatchmakingTicket': {
            'TicketId': 'string',
            'ConfigurationName': 'string',
            'ConfigurationArn': 'string',
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
                'DnsName': 'string',
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

def stop_fleet_actions(FleetId=None, Actions=None):
    """
    Suspends activity on a fleet. Currently, this operation is used to stop a fleet\'s auto-scaling activity. It is used to temporarily stop triggering scaling events. The policies can be retained and auto-scaling activity can be restarted using  StartFleetActions . You can view a fleet\'s stopped actions using  DescribeFleetAttributes .
    To stop fleet actions, specify the fleet ID and the type of actions to suspend. When auto-scaling fleet actions are stopped, Amazon GameLift no longer initiates scaling events except in response to manual changes using  UpdateFleetCapacity .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_fleet_actions(
        FleetId='string',
        Actions=[
            'AUTO_SCALING',
        ]
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to stop actions on. You can use either the fleet ID or ARN value.\n

    :type Actions: list
    :param Actions: [REQUIRED]\nList of actions to suspend on the fleet.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.NotFoundException


    :return: {}
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet to stop actions on. You can use either the fleet ID or ARN value.
    
    Actions (list) -- [REQUIRED]
    List of actions to suspend on the fleet.
    
    (string) --
    
    
    
    """
    pass

def stop_game_session_placement(PlacementId=None):
    """
    Cancels a game session placement that is in PENDING status. To stop a placement, provide the placement ID values. If successful, the placement is moved to CANCELLED status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_game_session_placement(
        PlacementId='string'
    )
    
    
    :type PlacementId: string
    :param PlacementId: [REQUIRED]\nA unique identifier for a game session placement to cancel.\n

    :rtype: dict
ReturnsResponse Syntax{
    'GameSessionPlacement': {
        'PlacementId': 'string',
        'GameSessionQueueName': 'string',
        'Status': 'PENDING'|'FULFILLED'|'CANCELLED'|'TIMED_OUT'|'FAILED',
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
        'DnsName': 'string',
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


Response Structure

(dict) --Represents the returned data in response to a request action.

GameSessionPlacement (dict) --Object that describes the canceled game session placement, with CANCELLED status and an end time stamp.

PlacementId (string) --A unique identifier for a game session placement.

GameSessionQueueName (string) --A descriptive label that is associated with game session queue. Queue names must be unique within each Region.

Status (string) --Current status of the game session placement request.

PENDING -- The placement request is currently in the queue waiting to be processed.
FULFILLED -- A new game session and player sessions (if requested) have been successfully created. Values for GameSessionArn and GameSessionRegion are available.
CANCELLED -- The placement request was canceled with a call to  StopGameSessionPlacement .
TIMED_OUT -- A new game session was not successfully created before the time limit expired. You can resubmit the placement request as needed.
FAILED -- GameLift is not able to complete the process of placing the game session. Common reasons are the game session terminated before the placement process was completed, or an unexpected internal error.


GameProperties (list) --Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

(dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --The game property identifier.

Value (string) --The game property value.





MaximumPlayerSessionCount (integer) --The maximum number of players that can be connected simultaneously to the game session.

GameSessionName (string) --A descriptive label that is associated with a game session. Session names do not need to be unique.

GameSessionId (string) --A unique identifier for the game session. This value is set once the new game session is placed (placement status is FULFILLED ).

GameSessionArn (string) --Identifier for the game session created by this placement request. This value is set once the new game session is placed (placement status is FULFILLED ). This identifier is unique across all Regions. You can use this value as a GameSessionId value as needed.

GameSessionRegion (string) --Name of the Region where the game session created by this placement request is running. This value is set once the new game session is placed (placement status is FULFILLED ).

PlayerLatencies (list) --Set of values, expressed in milliseconds, indicating the amount of latency that a player experiences when connected to AWS Regions.

(dict) --Regional latency information for a player, used when requesting a new game session with  StartGameSessionPlacement . This value indicates the amount of time lag that exists when the player is connected to a fleet in the specified Region. The relative difference between a player\'s latency values for multiple Regions are used to determine which fleets are best suited to place a new game session for the player.

PlayerId (string) --A unique identifier for a player associated with the latency data.

RegionIdentifier (string) --Name of the Region that is associated with the latency value.

LatencyInMilliseconds (float) --Amount of time that represents the time lag experienced by the player when connected to the specified Region.





StartTime (datetime) --Time stamp indicating when this request was placed in the queue. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

EndTime (datetime) --Time stamp indicating when this request was completed, canceled, or timed out.

IpAddress (string) --IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number. This value is set once the new game session is placed (placement status is FULFILLED ).

DnsName (string) --DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number. This value is set once the new game session is placed (placement status is FULFILLED ).

PlacedPlayerSessions (list) --A collection of information on player sessions created in response to the game session placement request. These player sessions are created only once a new game session is successfully placed (placement status is FULFILLED ). This information includes the player ID (as provided in the placement request) and the corresponding player session ID. Retrieve full player sessions by calling  DescribePlayerSessions with the player session ID.

(dict) --Information about a player session that was created as part of a  StartGameSessionPlacement request. This object contains only the player ID and player session ID. To retrieve full details on a player session, call  DescribePlayerSessions with the player session ID.

CreatePlayerSession
CreatePlayerSessions
DescribePlayerSessions
Game session placements
StartGameSessionPlacement
DescribeGameSessionPlacement
StopGameSessionPlacement




PlayerId (string) --A unique identifier for a player that is associated with this player session.

PlayerSessionId (string) --A unique identifier for a player session.





GameSessionData (string) --Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

MatchmakerData (string) --Information on the matchmaking process for this game. Data is in JSON syntax, formatted as a string. It identifies the matchmaking configuration used to create the match, and contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see Match Data .








Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'GameSessionPlacement': {
            'PlacementId': 'string',
            'GameSessionQueueName': 'string',
            'Status': 'PENDING'|'FULFILLED'|'CANCELLED'|'TIMED_OUT'|'FAILED',
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
            'DnsName': 'string',
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
    FAILED -- GameLift is not able to complete the process of placing the game session. Common reasons are the game session terminated before the placement process was completed, or an unexpected internal error.
    
    """
    pass

def stop_matchmaking(TicketId=None):
    """
    Cancels a matchmaking ticket or match backfill ticket that is currently being processed. To stop the matchmaking operation, specify the ticket ID. If successful, work on the ticket is stopped, and the ticket status is changed to CANCELLED .
    This call is also used to turn off automatic backfill for an individual game session. This is for game sessions that are created with a matchmaking configuration that has automatic backfill enabled. The ticket ID is included in the MatchmakerData of an updated game session object, which is provided to the game server.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_matchmaking(
        TicketId='string'
    )
    
    
    :type TicketId: string
    :param TicketId: [REQUIRED]\nA unique identifier for a matchmaking ticket.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def suspend_game_server_group(GameServerGroupName=None, SuspendActions=None):
    """
    Temporarily stops activity on a game server group without terminating instances or the game server group. Activity can be restarted by calling  ResumeGameServerGroup . Activities that can suspended are:
    To suspend activity, specify a game server group ARN and the type of activity to be suspended.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.suspend_game_server_group(
        GameServerGroupName='string',
        SuspendActions=[
            'REPLACE_INSTANCE_TYPES',
        ]
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nThe unique identifier of the game server group to stop activity on. Use either the GameServerGroup name or ARN value.\n

    :type SuspendActions: list
    :param SuspendActions: [REQUIRED]\nThe action to suspend for this game server group.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServerGroup': {
        'GameServerGroupName': 'string',
        'GameServerGroupArn': 'string',
        'RoleArn': 'string',
        'InstanceDefinitions': [
            {
                'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'WeightedCapacity': 'string'
            },
        ],
        'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
        'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
        'AutoScalingGroupArn': 'string',
        'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
        'StatusReason': 'string',
        'SuspendedActions': [
            'REPLACE_INSTANCE_TYPES',
        ],
        'CreationTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

GameServerGroup (dict) --
An object that describes the game server group resource, with the SuspendedActions property updated to reflect the suspended activity.

GameServerGroupName (string) --
A developer-defined identifier for the game server group. The name is unique per Region per AWS account.

GameServerGroupArn (string) --
A generated unique ID for the game server group.

RoleArn (string) --
The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups. The submitted role is validated to ensure that it contains the necessary permissions for game server groups.

InstanceDefinitions (list) --
The set of EC2 instance types that GameLift FleetIQ can use when rebalancing and autoscaling instances in the group.

(dict) --

This data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.

An allowed instance type for your game server group. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

InstanceType (string) --
An EC2 instance type designation.

WeightedCapacity (string) --
Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by GameLift FleetIQ to calculate the instance type\'s cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see Instance Weighting in the Amazon EC2 Auto Scaling User Guide . Default value is "1".





BalancingStrategy (string) --
The fallback balancing method to use for the game server group when Spot instances in a Region become unavailable or are not viable for game hosting. Once triggered, this method remains active until Spot instances can once again be used. Method options include:

SPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.
SPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.


GameServerProtectionPolicy (string) --
A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running may be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see  DeleteGameServerGroup ). An exception to this is Spot Instances, which may be terminated by AWS regardless of protection status.

AutoScalingGroupArn (string) --
A generated unique ID for the EC2 Auto Scaling group with is associated with this game server group.

Status (string) --
The current status of the game server group. Possible statuses include:

NEW - GameLift FleetIQ has validated the CreateGameServerGroup() request.
ACTIVATING - GameLift FleetIQ is setting up a game server group, which includes creating an autoscaling group in your AWS account.
ACTIVE - The game server group has been successfully created.
DELETE_SCHEDULED - A request to delete the game server group has been received.
DELETING - GameLift FleetIQ has received a valid DeleteGameServerGroup() request and is processing it. GameLift FleetIQ must first complete and release hosts before it deletes the autoscaling group and the game server group.
DELETED - The game server group has been successfully deleted.
ERROR - The asynchronous processes of activating or deleting a game server group has failed, resulting in an error state.


StatusReason (string) --
Additional information about the current game server group status. This information may provide additional insight on groups that in ERROR status.

SuspendedActions (list) --
A list of activities that are currently suspended for this game server group. If this property is empty, all activities are occurring.

(string) --


CreationTime (datetime) --
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --
A time stamp indicating when this game server group was last updated.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'GameServerGroup': {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'RoleArn': 'string',
            'InstanceDefinitions': [
                {
                    'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                    'WeightedCapacity': 'string'
                },
            ],
            'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
            'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
            'AutoScalingGroupArn': 'string',
            'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
            'StatusReason': 'string',
            'SuspendedActions': [
                'REPLACE_INSTANCE_TYPES',
            ],
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CreateGameServerGroup
    ListGameServerGroups
    DescribeGameServerGroup
    UpdateGameServerGroup
    DeleteGameServerGroup
    ResumeGameServerGroup
    SuspendGameServerGroup
    
    """
    pass

def tag_resource(ResourceARN=None, Tags=None):
    """
    Assigns a tag to a GameLift resource. AWS resource tags provide an additional management tool set. You can use tags to organize resources, create IAM permissions policies to manage access to groups of resources, customize AWS cost breakdowns, etc. This action handles the permissions necessary to manage tags for the following GameLift resource types:
    To add a tag to a resource, specify the unique ARN value for the resource and provide a tag list containing one or more tags. The operation succeeds even if the list includes tags that are already assigned to the specified resource.
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
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN ) that is assigned to and uniquely identifies the GameLift resource that you want to assign tags to. GameLift resource ARNs are included in the data object for the resource, which can be retrieved by calling a List or Describe action for the resource type.\n

    :type Tags: list
    :param Tags: [REQUIRED]\nA list of one or more tags to assign to the specified GameLift resource. Tags are developer-defined and structured as key-value pairs. The maximum tag limit may be lower than stated. See Tagging AWS Resources for actual tagging limits.\n\n(dict) --A label that can be assigned to a GameLift resource.\n\nLearn moreTagging AWS Resources in the AWS General Reference\nAWS Tagging Strategies\nRelated operations\n\n\nTagResource\nUntagResource\nListTagsForResource\n\n\nKey (string) -- [REQUIRED]The key for a developer-defined key:value pair for tagging an AWS resource.\n\nValue (string) -- [REQUIRED]The value for a developer-defined key:value pair for tagging an AWS resource.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.TaggingFailedException
GameLift.Client.exceptions.InternalServiceException


    :return: {}
    
    
    :returns: 
    TagResource
    UntagResource
    ListTagsForResource
    
    """
    pass

def untag_resource(ResourceARN=None, TagKeys=None):
    """
    Removes a tag that is assigned to a GameLift resource. Resource tags are used to organize AWS resources for a range of purposes. This action handles the permissions necessary to manage tags for the following GameLift resource types:
    To remove a tag from a resource, specify the unique ARN value for the resource and provide a string list containing one or more tags to be removed. This action succeeds even if the list includes tags that are not currently assigned to the specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceARN='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceARN: string
    :param ResourceARN: [REQUIRED]\nThe Amazon Resource Name (ARN ) that is assigned to and uniquely identifies the GameLift resource that you want to remove tags from. GameLift resource ARNs are included in the data object for the resource, which can be retrieved by calling a List or Describe action for the resource type.\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nA list of one or more tag keys to remove from the specified GameLift resource. An AWS resource can have only one tag with a specific tag key, so specifying the tag key identifies which tag to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.TaggingFailedException
GameLift.Client.exceptions.InternalServiceException


    :return: {}
    
    
    :returns: 
    TagResource
    UntagResource
    ListTagsForResource
    
    """
    pass

def update_alias(AliasId=None, Name=None, Description=None, RoutingStrategy=None):
    """
    Updates properties for an alias. To update properties, specify the alias ID to be updated and provide the information to be changed. To reassign an alias to another fleet, provide an updated routing strategy. If successful, the updated alias record is returned.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param AliasId: [REQUIRED]\nA unique identifier for the alias that you want to update. You can use either the alias ID or ARN value.\n

    :type Name: string
    :param Name: A descriptive label that is associated with an alias. Alias names do not need to be unique.

    :type Description: string
    :param Description: A human-readable description of the alias.

    :type RoutingStrategy: dict
    :param RoutingStrategy: The routing configuration, including routing type and fleet target, for the alias.\n\nType (string) --The type of routing strategy for the alias.\nPossible routing types include the following:\n\nSIMPLE - The alias resolves to one specific fleet. Use this type when routing to active fleets.\nTERMINAL - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the RoutingStrategy message embedded.\n\n\nFleetId (string) --The unique identifier for a fleet that the alias points to. This value is the fleet ID, not the fleet ARN.\n\nMessage (string) --The message text to be used with a terminal routing strategy.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

Alias (dict) --
The updated alias resource.

AliasId (string) --
A unique identifier for an alias. Alias IDs are unique within a Region.

Name (string) --
A descriptive label that is associated with an alias. Alias names do not need to be unique.

AliasArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift alias resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift alias ARN, the resource ID matches the alias ID value.

Description (string) --
A human-readable description of an alias.

RoutingStrategy (dict) --
The routing configuration, including routing type and fleet target, for the alias.

Type (string) --
The type of routing strategy for the alias.
Possible routing types include the following:

SIMPLE - The alias resolves to one specific fleet. Use this type when routing to active fleets.
TERMINAL - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.


FleetId (string) --
The unique identifier for a fleet that the alias points to. This value is the fleet ID, not the fleet ARN.

Message (string) --
The message text to be used with a terminal routing strategy.



CreationTime (datetime) --
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --
The time that this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").









Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


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
    A unique identifier for the alias that you want to update. You can use either the alias ID or ARN value.
    
    Name (string) -- A descriptive label that is associated with an alias. Alias names do not need to be unique.
    Description (string) -- A human-readable description of the alias.
    RoutingStrategy (dict) -- The routing configuration, including routing type and fleet target, for the alias.
    
    Type (string) --The type of routing strategy for the alias.
    Possible routing types include the following:
    
    SIMPLE - The alias resolves to one specific fleet. Use this type when routing to active fleets.
    TERMINAL - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the  RoutingStrategy message embedded.
    
    
    FleetId (string) --The unique identifier for a fleet that the alias points to. This value is the fleet ID, not the fleet ARN.
    
    Message (string) --The message text to be used with a terminal routing strategy.
    
    
    
    
    """
    pass

def update_build(BuildId=None, Name=None, Version=None):
    """
    Updates metadata in a build resource, including the build name and version. To update the metadata, specify the build ID to update and provide the new values. If successful, a build object containing the updated metadata is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_build(
        BuildId='string',
        Name='string',
        Version='string'
    )
    
    
    :type BuildId: string
    :param BuildId: [REQUIRED]\nA unique identifier for a build to update. You can use either the build ID or ARN value.\n

    :type Name: string
    :param Name: A descriptive label that is associated with a build. Build names do not need to be unique.

    :type Version: string
    :param Version: Version information that is associated with a build or script. Version strings do not need to be unique.

    :rtype: dict

ReturnsResponse Syntax
{
    'Build': {
        'BuildId': 'string',
        'BuildArn': 'string',
        'Name': 'string',
        'Version': 'string',
        'Status': 'INITIALIZED'|'READY'|'FAILED',
        'SizeOnDisk': 123,
        'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
        'CreationTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

Build (dict) --
The updated build resource.

BuildId (string) --
A unique identifier for a build.

BuildArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift build resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift build ARN, the resource ID matches the BuildId value.

Name (string) --
A descriptive label that is associated with a build. Build names do not need to be unique. It can be set using  CreateBuild or  UpdateBuild .

Version (string) --
Version information that is associated with a build or script. Version strings do not need to be unique. This value can be set using  CreateBuild or  UpdateBuild .

Status (string) --
Current status of the build.
Possible build statuses include the following:

INITIALIZED -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
READY -- The game build has been successfully uploaded. You can now create new fleets for this build.
FAILED -- The game build upload failed. You cannot create new fleets for this build.


SizeOnDisk (integer) --
File size of the uploaded game build, expressed in bytes. When the build status is INITIALIZED , this value is 0.

OperatingSystem (string) --
Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").









Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'Build': {
            'BuildId': 'string',
            'BuildArn': 'string',
            'Name': 'string',
            'Version': 'string',
            'Status': 'INITIALIZED'|'READY'|'FAILED',
            'SizeOnDisk': 123,
            'OperatingSystem': 'WINDOWS_2012'|'AMAZON_LINUX'|'AMAZON_LINUX_2',
            'CreationTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    BuildId (string) -- [REQUIRED]
    A unique identifier for a build to update. You can use either the build ID or ARN value.
    
    Name (string) -- A descriptive label that is associated with a build. Build names do not need to be unique.
    Version (string) -- Version information that is associated with a build or script. Version strings do not need to be unique.
    
    """
    pass

def update_fleet_attributes(FleetId=None, Name=None, Description=None, NewGameSessionProtectionPolicy=None, ResourceCreationLimitPolicy=None, MetricGroups=None):
    """
    Updates fleet properties, including name and description, for a fleet. To update metadata, specify the fleet ID and the property values that you want to change. If successful, the fleet ID for the updated fleet is returned.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to update attribute metadata for. You can use either the fleet ID or ARN value.\n

    :type Name: string
    :param Name: A descriptive label that is associated with a fleet. Fleet names do not need to be unique.

    :type Description: string
    :param Description: Human-readable description of a fleet.

    :type NewGameSessionProtectionPolicy: string
    :param NewGameSessionProtectionPolicy: Game session protection policy to apply to all new instances created in this fleet. Instances that already exist are not affected. You can set protection for individual instances using UpdateGameSession .\n\nNoProtection -- The game session can be terminated during a scale-down event.\nFullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.\n\n

    :type ResourceCreationLimitPolicy: dict
    :param ResourceCreationLimitPolicy: Policy that limits the number of game sessions an individual player can create over a span of time.\n\nNewGameSessionsPerCreator (integer) --The maximum number of game sessions that an individual can create during the policy period.\n\nPolicyPeriodInMinutes (integer) --The time span used in evaluating the resource creation limit policy.\n\n\n

    :type MetricGroups: list
    :param MetricGroups: Names of metric groups to include this fleet in. Amazon CloudWatch uses a fleet metric group is to aggregate metrics from multiple fleets. Use an existing metric group name to add this fleet to the group. Or use a new name to create a new metric group. A fleet can only be included in one metric group at a time.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FleetId': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

FleetId (string) --
A unique identifier for a fleet that was updated. Use either the fleet ID or ARN value.







Exceptions

GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.InvalidFleetStatusException
GameLift.Client.exceptions.LimitExceededException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'FleetId': 'string'
    }
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet to update attribute metadata for. You can use either the fleet ID or ARN value.
    
    Name (string) -- A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
    Description (string) -- Human-readable description of a fleet.
    NewGameSessionProtectionPolicy (string) -- Game session protection policy to apply to all new instances created in this fleet. Instances that already exist are not affected. You can set protection for individual instances using  UpdateGameSession .
    
    NoProtection -- The game session can be terminated during a scale-down event.
    FullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
    
    
    ResourceCreationLimitPolicy (dict) -- Policy that limits the number of game sessions an individual player can create over a span of time.
    
    NewGameSessionsPerCreator (integer) --The maximum number of game sessions that an individual can create during the policy period.
    
    PolicyPeriodInMinutes (integer) --The time span used in evaluating the resource creation limit policy.
    
    
    
    MetricGroups (list) -- Names of metric groups to include this fleet in. Amazon CloudWatch uses a fleet metric group is to aggregate metrics from multiple fleets. Use an existing metric group name to add this fleet to the group. Or use a new name to create a new metric group. A fleet can only be included in one metric group at a time.
    
    (string) --
    
    
    
    """
    pass

def update_fleet_capacity(FleetId=None, DesiredInstances=None, MinSize=None, MaxSize=None):
    """
    Updates capacity settings for a fleet. Use this action to specify the number of EC2 instances (hosts) that you want this fleet to contain. Before calling this action, you may want to call  DescribeEC2InstanceLimits to get the maximum capacity based on the fleet\'s EC2 instance type.
    Specify minimum and maximum number of instances. Amazon GameLift will not change fleet capacity to values fall outside of this range. This is particularly important when using auto-scaling (see  PutScalingPolicy ) to allow capacity to adjust based on player demand while imposing limits on automatic adjustments.
    To update fleet capacity, specify the fleet ID and the number of instances you want the fleet to host. If successful, Amazon GameLift starts or terminates instances so that the fleet\'s active instance count matches the desired instance count. You can view a fleet\'s current capacity information by calling  DescribeFleetCapacity . If the desired instance count is higher than the instance type\'s limit, the "Limit Exceeded" exception occurs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_fleet_capacity(
        FleetId='string',
        DesiredInstances=123,
        MinSize=123,
        MaxSize=123
    )
    
    
    :type FleetId: string
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to update capacity for. You can use either the fleet ID or ARN value.\n

    :type DesiredInstances: integer
    :param DesiredInstances: Number of EC2 instances you want this fleet to host.

    :type MinSize: integer
    :param MinSize: The minimum value allowed for the fleet\'s instance count. Default if not set is 0.

    :type MaxSize: integer
    :param MaxSize: The maximum value allowed for the fleet\'s instance count. Default if not set is 1.

    :rtype: dict

ReturnsResponse Syntax
{
    'FleetId': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

FleetId (string) --
A unique identifier for a fleet that was updated.







Exceptions

GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.LimitExceededException
GameLift.Client.exceptions.InvalidFleetStatusException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'FleetId': 'string'
    }
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet to update capacity for. You can use either the fleet ID or ARN value.
    
    DesiredInstances (integer) -- Number of EC2 instances you want this fleet to host.
    MinSize (integer) -- The minimum value allowed for the fleet\'s instance count. Default if not set is 0.
    MaxSize (integer) -- The maximum value allowed for the fleet\'s instance count. Default if not set is 1.
    
    """
    pass

def update_fleet_port_settings(FleetId=None, InboundPermissionAuthorizations=None, InboundPermissionRevocations=None):
    """
    Updates port settings for a fleet. To update settings, specify the fleet ID to be updated and list the permissions you want to update. List the permissions you want to add in InboundPermissionAuthorizations , and permissions you want to remove in InboundPermissionRevocations . Permissions to be removed must match existing fleet permissions. If successful, the fleet ID for the updated fleet is returned.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to update port settings for. You can use either the fleet ID or ARN value.\n

    :type InboundPermissionAuthorizations: list
    :param InboundPermissionAuthorizations: A collection of port settings to be added to the fleet resource.\n\n(dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift hosting resource. New game sessions that are started on the fleet are assigned an IP address/port number combination, which must fall into the fleet\'s allowed ranges. For fleets created with a custom game server, the ranges reflect the server\'s game session assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP for use by the Realtime servers.\n\nFromPort (integer) -- [REQUIRED]A starting value for a range of allowed port numbers.\n\nToPort (integer) -- [REQUIRED]An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .\n\nIpRange (string) -- [REQUIRED]A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: '000.000.000.000/[subnet mask] ' or optionally the shortened version '0.0.0.0/[subnet mask] '.\n\nProtocol (string) -- [REQUIRED]The network communication protocol used by the fleet.\n\n\n\n\n

    :type InboundPermissionRevocations: list
    :param InboundPermissionRevocations: A collection of port settings to be removed from the fleet resource.\n\n(dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift hosting resource. New game sessions that are started on the fleet are assigned an IP address/port number combination, which must fall into the fleet\'s allowed ranges. For fleets created with a custom game server, the ranges reflect the server\'s game session assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP for use by the Realtime servers.\n\nFromPort (integer) -- [REQUIRED]A starting value for a range of allowed port numbers.\n\nToPort (integer) -- [REQUIRED]An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .\n\nIpRange (string) -- [REQUIRED]A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: '000.000.000.000/[subnet mask] ' or optionally the shortened version '0.0.0.0/[subnet mask] '.\n\nProtocol (string) -- [REQUIRED]The network communication protocol used by the fleet.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FleetId': 'string'
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

FleetId (string) --
A unique identifier for a fleet that was updated.







Exceptions

GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.InvalidFleetStatusException
GameLift.Client.exceptions.LimitExceededException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.UnauthorizedException


    :return: {
        'FleetId': 'string'
    }
    
    
    :returns: 
    FleetId (string) -- [REQUIRED]
    A unique identifier for a fleet to update port settings for. You can use either the fleet ID or ARN value.
    
    InboundPermissionAuthorizations (list) -- A collection of port settings to be added to the fleet resource.
    
    (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift hosting resource. New game sessions that are started on the fleet are assigned an IP address/port number combination, which must fall into the fleet\'s allowed ranges. For fleets created with a custom game server, the ranges reflect the server\'s game session assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP for use by the Realtime servers.
    
    FromPort (integer) -- [REQUIRED]A starting value for a range of allowed port numbers.
    
    ToPort (integer) -- [REQUIRED]An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
    
    IpRange (string) -- [REQUIRED]A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: "000.000.000.000/[subnet mask] " or optionally the shortened version "0.0.0.0/[subnet mask] ".
    
    Protocol (string) -- [REQUIRED]The network communication protocol used by the fleet.
    
    
    
    
    
    InboundPermissionRevocations (list) -- A collection of port settings to be removed from the fleet resource.
    
    (dict) --A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift hosting resource. New game sessions that are started on the fleet are assigned an IP address/port number combination, which must fall into the fleet\'s allowed ranges. For fleets created with a custom game server, the ranges reflect the server\'s game session assignments. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP for use by the Realtime servers.
    
    FromPort (integer) -- [REQUIRED]A starting value for a range of allowed port numbers.
    
    ToPort (integer) -- [REQUIRED]An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than FromPort .
    
    IpRange (string) -- [REQUIRED]A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: "000.000.000.000/[subnet mask] " or optionally the shortened version "0.0.0.0/[subnet mask] ".
    
    Protocol (string) -- [REQUIRED]The network communication protocol used by the fleet.
    
    
    
    
    
    
    """
    pass

def update_game_server(GameServerGroupName=None, GameServerId=None, GameServerData=None, CustomSortKey=None, UtilizationStatus=None, HealthCheck=None):
    """
    Updates information about a registered game server. This action is called by a game server process that is running on an instance in a game server group. There are three reasons to update game server information: (1) to change the utilization status of the game server, (2) to report game server health status, and (3) to change game server metadata. A registered game server should regularly report health and should update utilization status when it is supporting gameplay so that GameLift FleetIQ can accurately track game server availability. You can make all three types of updates in the same request.
    Once a game server is successfully updated, the relevant statuses and timestamps are updated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_game_server(
        GameServerGroupName='string',
        GameServerId='string',
        GameServerData='string',
        CustomSortKey='string',
        UtilizationStatus='AVAILABLE'|'UTILIZED',
        HealthCheck='HEALTHY'
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nAn identifier for the game server group where the game server is running. Use either the GameServerGroup name or ARN value.\n

    :type GameServerId: string
    :param GameServerId: [REQUIRED]\nThe identifier for the game server to be updated.\n

    :type GameServerData: string
    :param GameServerData: A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on a game servers using DescribeGameServer or ClaimGameServer .

    :type CustomSortKey: string
    :param CustomSortKey: A game server tag that can be used to request sorted lists of game servers using ListGameServers . Custom sort keys are developer-defined based on how you want to organize the retrieved game server information.

    :type UtilizationStatus: string
    :param UtilizationStatus: Indicates whether the game server is available or is currently hosting gameplay.

    :type HealthCheck: string
    :param HealthCheck: Indicates health status of the game server. An update that explicitly includes this parameter updates the game server\'s LastHealthCheckTime time stamp.

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServer': {
        'GameServerGroupName': 'string',
        'GameServerGroupArn': 'string',
        'GameServerId': 'string',
        'InstanceId': 'string',
        'ConnectionInfo': 'string',
        'GameServerData': 'string',
        'CustomSortKey': 'string',
        'ClaimStatus': 'CLAIMED',
        'UtilizationStatus': 'AVAILABLE'|'UTILIZED',
        'RegistrationTime': datetime(2015, 1, 1),
        'LastClaimTime': datetime(2015, 1, 1),
        'LastHealthCheckTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

GameServer (dict) --
Object that describes the newly updated game server resource.

GameServerGroupName (string) --
The name identifier for the game server group where the game server is located.

GameServerGroupArn (string) --
The ARN identifier for the game server group where the game server is located.

GameServerId (string) --
A custom string that uniquely identifies the game server. Game server IDs are developer-defined and are unique across all game server groups in an AWS account.

InstanceId (string) --
The unique identifier for the instance where the game server is located.

ConnectionInfo (string) --
The port and IP address that must be used to establish a client connection to the game server.

GameServerData (string) --
A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service in response to requests  ListGameServers or  ClaimGameServer . This property can be updated using  UpdateGameServer .

CustomSortKey (string) --
A game server tag that can be used to request sorted lists of game servers when calling  ListGameServers . Custom sort keys are developer-defined. This property can be updated using  UpdateGameServer .

ClaimStatus (string) --
Indicates when an available game server has been reserved but has not yet started hosting a game. Once it is claimed, game server remains in CLAIMED status for a maximum of one minute. During this time, game clients must connect to the game server and start the game, which triggers the game server to update its utilization status. After one minute, the game server claim status reverts to null.

UtilizationStatus (string) --
Indicates whether the game server is currently available for new games or is busy. Possible statuses include:

AVAILABLE - The game server is available to be claimed. A game server that has been claimed remains in this status until it reports game hosting activity.
IN_USE - The game server is currently hosting a game session with players.


RegistrationTime (datetime) --
Time stamp indicating when the game server resource was created with a  RegisterGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastClaimTime (datetime) --
Time stamp indicating the last time the game server was claimed with a  ClaimGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057"). This value is used to calculate when the game server\'s claim status.

LastHealthCheckTime (datetime) --
Time stamp indicating the last time the game server was updated with health status using an  UpdateGameServer request. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057"). After game server registration, this property is only changed when a game server update specifies a health check value.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'GameServer': {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'GameServerId': 'string',
            'InstanceId': 'string',
            'ConnectionInfo': 'string',
            'GameServerData': 'string',
            'CustomSortKey': 'string',
            'ClaimStatus': 'CLAIMED',
            'UtilizationStatus': 'AVAILABLE'|'UTILIZED',
            'RegistrationTime': datetime(2015, 1, 1),
            'LastClaimTime': datetime(2015, 1, 1),
            'LastHealthCheckTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    RegisterGameServer
    ListGameServers
    ClaimGameServer
    DescribeGameServer
    UpdateGameServer
    DeregisterGameServer
    
    """
    pass

def update_game_server_group(GameServerGroupName=None, RoleArn=None, InstanceDefinitions=None, GameServerProtectionPolicy=None, BalancingStrategy=None):
    """
    Updates GameLift FleetIQ-specific properties for a game server group. These properties include instance rebalancing and game server protection. Many Auto Scaling group properties are updated directly. These include autoscaling policies, minimum/maximum/desired instance counts, and launch template.
    To update the game server group, specify the game server group ID and provide the updated values.
    Updated properties are validated to ensure that GameLift FleetIQ can continue to perform its core instance rebalancing activity. When you change Auto Scaling group properties directly and the changes cause errors with GameLift FleetIQ activities, an alert is sent.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_game_server_group(
        GameServerGroupName='string',
        RoleArn='string',
        InstanceDefinitions=[
            {
                'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'WeightedCapacity': 'string'
            },
        ],
        GameServerProtectionPolicy='NO_PROTECTION'|'FULL_PROTECTION',
        BalancingStrategy='SPOT_ONLY'|'SPOT_PREFERRED'
    )
    
    
    :type GameServerGroupName: string
    :param GameServerGroupName: [REQUIRED]\nThe unique identifier of the game server group to update. Use either the GameServerGroup name or ARN value.\n

    :type RoleArn: string
    :param RoleArn: The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups. The submitted role is validated to ensure that it contains the necessary permissions for game server groups.

    :type InstanceDefinitions: list
    :param InstanceDefinitions: An updated list of EC2 instance types to use when creating instances in the group. The instance definition must specify instance types that are supported by GameLift FleetIQ, and must include at least two instance types. This updated list replaces the entire current list of instance definitions for the game server group. For more information on instance types, see EC2 Instance Types in the Amazon EC2 User Guide ..\n\n(dict) --\nThis data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.\nAn allowed instance type for your game server group. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.\n\nInstanceType (string) -- [REQUIRED]An EC2 instance type designation.\n\nWeightedCapacity (string) --Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by GameLift FleetIQ to calculate the instance type\'s cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see Instance Weighting in the Amazon EC2 Auto Scaling User Guide . Default value is '1'.\n\n\n\n\n

    :type GameServerProtectionPolicy: string
    :param GameServerProtectionPolicy: A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running may by terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running. An exception to this is Spot Instances, which may be terminated by AWS regardless of protection status. This property is set to NO_PROTECTION by default.

    :type BalancingStrategy: string
    :param BalancingStrategy: The fallback balancing method to use for the game server group when Spot instances in a Region become unavailable or are not viable for game hosting. Once triggered, this method remains active until Spot instances can once again be used. Method options include:\n\nSPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.\nSPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GameServerGroup': {
        'GameServerGroupName': 'string',
        'GameServerGroupArn': 'string',
        'RoleArn': 'string',
        'InstanceDefinitions': [
            {
                'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                'WeightedCapacity': 'string'
            },
        ],
        'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
        'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
        'AutoScalingGroupArn': 'string',
        'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
        'StatusReason': 'string',
        'SuspendedActions': [
            'REPLACE_INSTANCE_TYPES',
        ],
        'CreationTime': datetime(2015, 1, 1),
        'LastUpdatedTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

GameServerGroup (dict) --
An object that describes the game server group resource with updated properties.

GameServerGroupName (string) --
A developer-defined identifier for the game server group. The name is unique per Region per AWS account.

GameServerGroupArn (string) --
A generated unique ID for the game server group.

RoleArn (string) --
The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups. The submitted role is validated to ensure that it contains the necessary permissions for game server groups.

InstanceDefinitions (list) --
The set of EC2 instance types that GameLift FleetIQ can use when rebalancing and autoscaling instances in the group.

(dict) --

This data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.

An allowed instance type for your game server group. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

InstanceType (string) --
An EC2 instance type designation.

WeightedCapacity (string) --
Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by GameLift FleetIQ to calculate the instance type\'s cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see Instance Weighting in the Amazon EC2 Auto Scaling User Guide . Default value is "1".





BalancingStrategy (string) --
The fallback balancing method to use for the game server group when Spot instances in a Region become unavailable or are not viable for game hosting. Once triggered, this method remains active until Spot instances can once again be used. Method options include:

SPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.
SPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.


GameServerProtectionPolicy (string) --
A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running may be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see  DeleteGameServerGroup ). An exception to this is Spot Instances, which may be terminated by AWS regardless of protection status.

AutoScalingGroupArn (string) --
A generated unique ID for the EC2 Auto Scaling group with is associated with this game server group.

Status (string) --
The current status of the game server group. Possible statuses include:

NEW - GameLift FleetIQ has validated the CreateGameServerGroup() request.
ACTIVATING - GameLift FleetIQ is setting up a game server group, which includes creating an autoscaling group in your AWS account.
ACTIVE - The game server group has been successfully created.
DELETE_SCHEDULED - A request to delete the game server group has been received.
DELETING - GameLift FleetIQ has received a valid DeleteGameServerGroup() request and is processing it. GameLift FleetIQ must first complete and release hosts before it deletes the autoscaling group and the game server group.
DELETED - The game server group has been successfully deleted.
ERROR - The asynchronous processes of activating or deleting a game server group has failed, resulting in an error state.


StatusReason (string) --
Additional information about the current game server group status. This information may provide additional insight on groups that in ERROR status.

SuspendedActions (list) --
A list of activities that are currently suspended for this game server group. If this property is empty, all activities are occurring.

(string) --


CreationTime (datetime) --
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

LastUpdatedTime (datetime) --
A time stamp indicating when this game server group was last updated.









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'GameServerGroup': {
            'GameServerGroupName': 'string',
            'GameServerGroupArn': 'string',
            'RoleArn': 'string',
            'InstanceDefinitions': [
                {
                    'InstanceType': 'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'c5.large'|'c5.xlarge'|'c5.2xlarge'|'c5.4xlarge'|'c5.9xlarge'|'c5.12xlarge'|'c5.18xlarge'|'c5.24xlarge'|'r4.large'|'r4.xlarge'|'r4.2xlarge'|'r4.4xlarge'|'r4.8xlarge'|'r4.16xlarge'|'r5.large'|'r5.xlarge'|'r5.2xlarge'|'r5.4xlarge'|'r5.8xlarge'|'r5.12xlarge'|'r5.16xlarge'|'r5.24xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m5.large'|'m5.xlarge'|'m5.2xlarge'|'m5.4xlarge'|'m5.8xlarge'|'m5.12xlarge'|'m5.16xlarge'|'m5.24xlarge',
                    'WeightedCapacity': 'string'
                },
            ],
            'BalancingStrategy': 'SPOT_ONLY'|'SPOT_PREFERRED',
            'GameServerProtectionPolicy': 'NO_PROTECTION'|'FULL_PROTECTION',
            'AutoScalingGroupArn': 'string',
            'Status': 'NEW'|'ACTIVATING'|'ACTIVE'|'DELETE_SCHEDULED'|'DELETING'|'DELETED'|'ERROR',
            'StatusReason': 'string',
            'SuspendedActions': [
                'REPLACE_INSTANCE_TYPES',
            ],
            'CreationTime': datetime(2015, 1, 1),
            'LastUpdatedTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    GameServerGroupName (string) -- [REQUIRED]
    The unique identifier of the game server group to update. Use either the  GameServerGroup name or ARN value.
    
    RoleArn (string) -- The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups. The submitted role is validated to ensure that it contains the necessary permissions for game server groups.
    InstanceDefinitions (list) -- An updated list of EC2 instance types to use when creating instances in the group. The instance definition must specify instance types that are supported by GameLift FleetIQ, and must include at least two instance types. This updated list replaces the entire current list of instance definitions for the game server group. For more information on instance types, see EC2 Instance Types in the Amazon EC2 User Guide ..
    
    (dict) --
    This data type is part of Amazon GameLift FleetIQ with game server groups, which is in preview release and is subject to change.
    An allowed instance type for your game server group. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.
    
    InstanceType (string) -- [REQUIRED]An EC2 instance type designation.
    
    WeightedCapacity (string) --Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by GameLift FleetIQ to calculate the instance type\'s cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see Instance Weighting in the Amazon EC2 Auto Scaling User Guide . Default value is "1".
    
    
    
    
    
    GameServerProtectionPolicy (string) -- A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running may by terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running. An exception to this is Spot Instances, which may be terminated by AWS regardless of protection status. This property is set to NO_PROTECTION by default.
    BalancingStrategy (string) -- The fallback balancing method to use for the game server group when Spot instances in a Region become unavailable or are not viable for game hosting. Once triggered, this method remains active until Spot instances can once again be used. Method options include:
    
    SPOT_ONLY -- If Spot instances are unavailable, the game server group provides no hosting capacity. No new instances are started, and the existing nonviable Spot instances are terminated (once current gameplay ends) and not replaced.
    SPOT_PREFERRED -- If Spot instances are unavailable, the game server group continues to provide hosting capacity by using On-Demand instances. Existing nonviable Spot instances are terminated (once current gameplay ends) and replaced with new On-Demand instances.
    
    
    
    """
    pass

def update_game_session(GameSessionId=None, MaximumPlayerSessionCount=None, Name=None, PlayerSessionCreationPolicy=None, ProtectionPolicy=None):
    """
    Updates game session properties. This includes the session name, maximum player count, protection policy, which controls whether or not an active game session can be terminated during a scale-down event, and the player session creation policy, which controls whether or not new players can join the session. To update a game session, specify the game session ID and the values you want to change. If successful, an updated  GameSession object is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_game_session(
        GameSessionId='string',
        MaximumPlayerSessionCount=123,
        Name='string',
        PlayerSessionCreationPolicy='ACCEPT_ALL'|'DENY_ALL',
        ProtectionPolicy='NoProtection'|'FullProtection'
    )
    
    
    :type GameSessionId: string
    :param GameSessionId: [REQUIRED]\nA unique identifier for the game session to update.\n

    :type MaximumPlayerSessionCount: integer
    :param MaximumPlayerSessionCount: The maximum number of players that can be connected simultaneously to the game session.

    :type Name: string
    :param Name: A descriptive label that is associated with a game session. Session names do not need to be unique.

    :type PlayerSessionCreationPolicy: string
    :param PlayerSessionCreationPolicy: Policy determining whether or not the game session accepts new players.

    :type ProtectionPolicy: string
    :param ProtectionPolicy: Game session protection policy to apply to this game session only.\n\nNoProtection -- The game session can be terminated during a scale-down event.\nFullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'GameSession': {
        'GameSessionId': 'string',
        'Name': 'string',
        'FleetId': 'string',
        'FleetArn': 'string',
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
        'DnsName': 'string',
        'Port': 123,
        'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
        'CreatorId': 'string',
        'GameSessionData': 'string',
        'MatchmakerData': 'string'
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

GameSession (dict) --
The updated game session metadata.

GameSessionId (string) --
A unique identifier for the game session. A game session ARN has the following format: arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token> .

Name (string) --
A descriptive label that is associated with a game session. Session names do not need to be unique.

FleetId (string) --
A unique identifier for a fleet that the game session is running on.

FleetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift fleet that this game session is running on.

CreationTime (datetime) --
Time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

TerminationTime (datetime) --
Time stamp indicating when this data object was terminated. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

CurrentPlayerSessionCount (integer) --
Number of players currently in the game session.

MaximumPlayerSessionCount (integer) --
The maximum number of players that can be connected simultaneously to the game session.

Status (string) --
Current status of the game session. A game session must have an ACTIVE status to have player sessions.

StatusReason (string) --
Provides additional information about game session status. INTERRUPTED indicates that the game session was hosted on a spot instance that was reclaimed, causing the active game session to be terminated.

GameProperties (list) --
Set of custom properties for a game session, formatted as key:value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). You can search for active game sessions based on this custom data with  SearchGameSessions .

(dict) --
Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --
The game property identifier.

Value (string) --
The game property value.





IpAddress (string) --
IP address of the instance that is running the game session. When connecting to a Amazon GameLift game server, a client needs to reference an IP address (or DNS name) and port number.

DnsName (string) --
DNS identifier assigned to the instance that is running the game session. Values have the following format:

TLS-enabled fleets: <unique identifier>.<region identifier>.amazongamelift.com .
Non-TLS-enabled fleets: ec2-<unique identifier>.compute.amazonaws.com . (See Amazon EC2 Instance IP Addressing .)

When connecting to a game session that is running on a TLS-enabled fleet, you must use the DNS name, not the IP address.

Port (integer) --
Port number for the game session. To connect to a Amazon GameLift game server, an app needs both the IP address and port number.

PlayerSessionCreationPolicy (string) --
Indicates whether or not the game session is accepting new players.

CreatorId (string) --
A unique identifier for a player. This ID is used to enforce a resource protection policy (if one exists), that limits the number of game sessions a player can create.

GameSessionData (string) --
Set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ).

MatchmakerData (string) --
Information about the matchmaking process that was used to create the game session. It is in JSON syntax, formatted as a string. In addition the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments. For more details on matchmaker data, see Match Data . Matchmaker data is useful when requesting match backfills, and is updated whenever new players are added during a successful backfill (see  StartMatchBackfill ).









Exceptions

GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.ConflictException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidGameSessionStatusException
GameLift.Client.exceptions.InvalidRequestException


    :return: {
        'GameSession': {
            'GameSessionId': 'string',
            'Name': 'string',
            'FleetId': 'string',
            'FleetArn': 'string',
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
            'DnsName': 'string',
            'Port': 123,
            'PlayerSessionCreationPolicy': 'ACCEPT_ALL'|'DENY_ALL',
            'CreatorId': 'string',
            'GameSessionData': 'string',
            'MatchmakerData': 'string'
        }
    }
    
    
    :returns: 
    GameSessionId (string) -- [REQUIRED]
    A unique identifier for the game session to update.
    
    MaximumPlayerSessionCount (integer) -- The maximum number of players that can be connected simultaneously to the game session.
    Name (string) -- A descriptive label that is associated with a game session. Session names do not need to be unique.
    PlayerSessionCreationPolicy (string) -- Policy determining whether or not the game session accepts new players.
    ProtectionPolicy (string) -- Game session protection policy to apply to this game session only.
    
    NoProtection -- The game session can be terminated during a scale-down event.
    FullProtection -- If the game session is in an ACTIVE status, it cannot be terminated during a scale-down event.
    
    
    
    """
    pass

def update_game_session_queue(Name=None, TimeoutInSeconds=None, PlayerLatencyPolicies=None, Destinations=None):
    """
    Updates settings for a game session queue, which determines how new game session requests in the queue are processed. To update settings, specify the queue name to be updated and provide the new settings. When updating destinations, provide a complete list of destinations.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param Name: [REQUIRED]\nA descriptive label that is associated with game session queue. Queue names must be unique within each Region. You can use either the queue ID or ARN value.\n

    :type TimeoutInSeconds: integer
    :param TimeoutInSeconds: The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.

    :type PlayerLatencyPolicies: list
    :param PlayerLatencyPolicies: A collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, the policy is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. When updating policies, provide a complete collection of policies.\n\n(dict) --Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed with any fleet in a Region where a player reports latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.\n\nCreateGameSessionQueue\nDescribeGameSessionQueues\nUpdateGameSessionQueue\nDeleteGameSessionQueue\n\n\nMaximumIndividualPlayerLatencyMilliseconds (integer) --The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.\n\nPolicyDurationSeconds (integer) --The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.\n\n\n\n\n

    :type Destinations: list
    :param Destinations: A list of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order. When updating this list, provide a complete list of destinations.\n\n(dict) --Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination that is configured for a queue.\n\nCreateGameSessionQueue\nDescribeGameSessionQueues\nUpdateGameSessionQueue\nDeleteGameSessionQueue\n\n\nDestinationArn (string) --The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

GameSessionQueue (dict) --
An object that describes the newly updated game session queue.

Name (string) --
A descriptive label that is associated with game session queue. Queue names must be unique within each Region.

GameSessionQueueArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift game session queue ARN, the resource ID matches the Name value.

TimeoutInSeconds (integer) --
The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.

PlayerLatencyPolicies (list) --
A collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, the policy is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement.

(dict) --
Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed with any fleet in a Region where a player reports latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.

CreateGameSessionQueue
DescribeGameSessionQueues
UpdateGameSessionQueue
DeleteGameSessionQueue


MaximumIndividualPlayerLatencyMilliseconds (integer) --
The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.

PolicyDurationSeconds (integer) --
The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.





Destinations (list) --
A list of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order.

(dict) --
Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination that is configured for a queue.

CreateGameSessionQueue
DescribeGameSessionQueues
UpdateGameSessionQueue
DeleteGameSessionQueue


DestinationArn (string) --
The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.













Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.UnauthorizedException


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
    A descriptive label that is associated with game session queue. Queue names must be unique within each Region. You can use either the queue ID or ARN value.
    
    TimeoutInSeconds (integer) -- The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a TIMED_OUT status.
    PlayerLatencyPolicies (list) -- A collection of latency policies to apply when processing game sessions placement requests with player latency information. Multiple policies are evaluated in order of the maximum latency value, starting with the lowest latency values. With just one policy, the policy is enforced at the start of the game session placement for the duration period. With multiple policies, each policy is enforced consecutively for its duration period. For example, a queue might enforce a 60-second policy followed by a 120-second policy, and then no policy for the remainder of the placement. When updating policies, provide a complete collection of policies.
    
    (dict) --Queue setting that determines the highest latency allowed for individual players when placing a game session. When a latency policy is in force, a game session cannot be placed with any fleet in a Region where a player reports latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.
    
    CreateGameSessionQueue
    DescribeGameSessionQueues
    UpdateGameSessionQueue
    DeleteGameSessionQueue
    
    
    MaximumIndividualPlayerLatencyMilliseconds (integer) --The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
    
    PolicyDurationSeconds (integer) --The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.
    
    
    
    
    
    Destinations (list) -- A list of fleets that can be used to fulfill game session placement requests in the queue. Fleets are identified by either a fleet ARN or a fleet alias ARN. Destinations are listed in default preference order. When updating this list, provide a complete list of destinations.
    
    (dict) --Fleet designated in a game session queue. Requests for new game sessions in the queue are fulfilled by starting a new game session on any destination that is configured for a queue.
    
    CreateGameSessionQueue
    DescribeGameSessionQueues
    UpdateGameSessionQueue
    DeleteGameSessionQueue
    
    
    DestinationArn (string) --The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.
    
    
    
    
    
    
    """
    pass

def update_matchmaking_configuration(Name=None, Description=None, GameSessionQueueArns=None, RequestTimeoutSeconds=None, AcceptanceTimeoutSeconds=None, AcceptanceRequired=None, RuleSetName=None, NotificationTarget=None, AdditionalPlayerCount=None, CustomEventData=None, GameProperties=None, GameSessionData=None, BackfillMode=None):
    """
    Updates settings for a FlexMatch matchmaking configuration. These changes affect all matches and game sessions that are created after the update. To update settings, specify the configuration name to be updated and provide the new settings.
    See also: AWS API Documentation
    
    Exceptions
    
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
        GameSessionData='string',
        BackfillMode='AUTOMATIC'|'MANUAL'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nA unique identifier for a matchmaking configuration to update. You can use either the configuration name or ARN value.\n

    :type Description: string
    :param Description: A descriptive label that is associated with matchmaking configuration.

    :type GameSessionQueueArns: list
    :param GameSessionQueueArns: Amazon Resource Name (ARN ) that is assigned to a GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any Region.\n\n(string) --\n\n

    :type RequestTimeoutSeconds: integer
    :param RequestTimeoutSeconds: The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.

    :type AcceptanceTimeoutSeconds: integer
    :param AcceptanceTimeoutSeconds: The length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.

    :type AcceptanceRequired: boolean
    :param AcceptanceRequired: A flag that indicates whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.

    :type RuleSetName: string
    :param RuleSetName: A unique identifier for a matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.

    :type NotificationTarget: string
    :param NotificationTarget: An SNS topic ARN that is set up to receive matchmaking notifications. See Setting up Notifications for Matchmaking for more information.

    :type AdditionalPlayerCount: integer
    :param AdditionalPlayerCount: The number of player slots in a match to keep open for future players. For example, assume that the configuration\'s rule set specifies a match for a single 12-person team. If the additional player count is set to 2, only 10 players are initially selected for the match.

    :type CustomEventData: string
    :param CustomEventData: Information to add to all events related to the matchmaking configuration.

    :type GameProperties: list
    :param GameProperties: A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new GameSession object that is created for a successful match.\n\n(dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .\n\nKey (string) -- [REQUIRED]The game property identifier.\n\nValue (string) -- [REQUIRED]The game property value.\n\n\n\n\n

    :type GameSessionData: string
    :param GameSessionData: A set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new GameSession object that is created for a successful match.

    :type BackfillMode: string
    :param BackfillMode: The method that is used to backfill game sessions created with this matchmaking configuration. Specify MANUAL when your game manages backfill requests manually or does not use the match backfill feature. Specify AUTOMATIC to have GameLift create a StartMatchBackfill request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in Backfill Existing Games with FlexMatch .

    :rtype: dict

ReturnsResponse Syntax
{
    'Configuration': {
        'Name': 'string',
        'ConfigurationArn': 'string',
        'Description': 'string',
        'GameSessionQueueArns': [
            'string',
        ],
        'RequestTimeoutSeconds': 123,
        'AcceptanceTimeoutSeconds': 123,
        'AcceptanceRequired': True|False,
        'RuleSetName': 'string',
        'RuleSetArn': 'string',
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
        'GameSessionData': 'string',
        'BackfillMode': 'AUTOMATIC'|'MANUAL'
    }
}


Response Structure

(dict) --
Represents the returned data in response to a request action.

Configuration (dict) --
The updated matchmaking configuration.

Name (string) --
A unique identifier for a matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.

ConfigurationArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift matchmaking configuration resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift configuration ARN, the resource ID matches the Name value.

Description (string) --
A descriptive label that is associated with matchmaking configuration.

GameSessionQueueArns (list) --
Amazon Resource Name (ARN ) that is assigned to a GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. GameLift uses the listed queues when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any Region.

(string) --


RequestTimeoutSeconds (integer) --
The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.

AcceptanceTimeoutSeconds (integer) --
The length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.

AcceptanceRequired (boolean) --
A flag that indicates whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.

RuleSetName (string) --
A unique identifier for a matchmaking rule set to use with this configuration. A matchmaking configuration can only use rule sets that are defined in the same Region.

RuleSetArn (string) --
The Amazon Resource Name (ARN ) associated with the GameLift matchmaking rule set resource that this configuration uses.

NotificationTarget (string) --
An SNS topic ARN that is set up to receive matchmaking notifications.

AdditionalPlayerCount (integer) --
The number of player slots in a match to keep open for future players. For example, assume that the configuration\'s rule set specifies a match for a single 12-person team. If the additional player count is set to 2, only 10 players are initially selected for the match.

CustomEventData (string) --
Information to attach to all events related to the matchmaking configuration.

CreationTime (datetime) --
The time stamp indicating when this data object was created. The format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

GameProperties (list) --
A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.

(dict) --
Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .

Key (string) --
The game property identifier.

Value (string) --
The game property value.





GameSessionData (string) --
A set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.

BackfillMode (string) --
The method used to backfill game sessions created with this matchmaking configuration. MANUAL indicates that the game makes backfill requests or does not use the match backfill feature. AUTOMATIC indicates that GameLift creates  StartMatchBackfill requests whenever a game session has one or more open slots. Learn more about manual and automatic backfill in Backfill Existing Games with FlexMatch .









Exceptions

GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException


    :return: {
        'Configuration': {
            'Name': 'string',
            'ConfigurationArn': 'string',
            'Description': 'string',
            'GameSessionQueueArns': [
                'string',
            ],
            'RequestTimeoutSeconds': 123,
            'AcceptanceTimeoutSeconds': 123,
            'AcceptanceRequired': True|False,
            'RuleSetName': 'string',
            'RuleSetArn': 'string',
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
            'GameSessionData': 'string',
            'BackfillMode': 'AUTOMATIC'|'MANUAL'
        }
    }
    
    
    :returns: 
    Name (string) -- [REQUIRED]
    A unique identifier for a matchmaking configuration to update. You can use either the configuration name or ARN value.
    
    Description (string) -- A descriptive label that is associated with matchmaking configuration.
    GameSessionQueueArns (list) -- Amazon Resource Name (ARN ) that is assigned to a GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. These queues are used when placing game sessions for matches that are created with this matchmaking configuration. Queues can be located in any Region.
    
    (string) --
    
    
    RequestTimeoutSeconds (integer) -- The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.
    AcceptanceTimeoutSeconds (integer) -- The length of time (in seconds) to wait for players to accept a proposed match. If any player rejects the match or fails to accept before the timeout, the ticket continues to look for an acceptable match.
    AcceptanceRequired (boolean) -- A flag that indicates whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE.
    RuleSetName (string) -- A unique identifier for a matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.
    NotificationTarget (string) -- An SNS topic ARN that is set up to receive matchmaking notifications. See Setting up Notifications for Matchmaking for more information.
    AdditionalPlayerCount (integer) -- The number of player slots in a match to keep open for future players. For example, assume that the configuration\'s rule set specifies a match for a single 12-person team. If the additional player count is set to 2, only 10 players are initially selected for the match.
    CustomEventData (string) -- Information to add to all events related to the matchmaking configuration.
    GameProperties (list) -- A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.
    
    (dict) --Set of key-value pairs that contain information about a game session. When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the Amazon GameLift Developer Guide .
    
    Key (string) -- [REQUIRED]The game property identifier.
    
    Value (string) -- [REQUIRED]The game property value.
    
    
    
    
    
    GameSessionData (string) -- A set of custom game session properties, formatted as a single string value. This data is passed to a game server process in the  GameSession object with a request to start a new game session (see Start a Game Session ). This information is added to the new  GameSession object that is created for a successful match.
    BackfillMode (string) -- The method that is used to backfill game sessions created with this matchmaking configuration. Specify MANUAL when your game manages backfill requests manually or does not use the match backfill feature. Specify AUTOMATIC to have GameLift create a  StartMatchBackfill request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in Backfill Existing Games with FlexMatch .
    
    """
    pass

def update_runtime_configuration(FleetId=None, RuntimeConfiguration=None):
    """
    Updates the current runtime configuration for the specified fleet, which tells Amazon GameLift how to launch server processes on instances in the fleet. You can update a fleet\'s runtime configuration at any time after the fleet is created; it does not need to be in an ACTIVE status.
    To update runtime configuration, specify the fleet ID and provide a RuntimeConfiguration object with an updated set of server process configurations.
    Each instance in a Amazon GameLift fleet checks regularly for an updated runtime configuration and changes how it launches server processes to comply with the latest version. Existing server processes are not affected by the update; runtime configuration changes are applied gradually as existing processes shut down and new processes are launched during Amazon GameLift\'s normal process recycling activity.
    See also: AWS API Documentation
    
    Exceptions
    
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
    :param FleetId: [REQUIRED]\nA unique identifier for a fleet to update runtime configuration for. You can use either the fleet ID or ARN value.\n

    :type RuntimeConfiguration: dict
    :param RuntimeConfiguration: [REQUIRED]\nInstructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime Servers script. The runtime configuration lists the types of server processes to run on an instance and includes the following configuration settings: the server executable or launch script file, launch parameters, and the number of processes to run concurrently on each instance. A CreateFleet request must include a runtime configuration with at least one server process configuration.\n\nServerProcesses (list) --A collection of server process configurations that describe which server processes to run on each instance in a fleet.\n\n(dict) --A set of instructions for launching server processes on each instance in a fleet. Server processes run either a custom game build executable or a Realtime Servers script. Each instruction set identifies the location of the custom game build executable or Realtime launch script, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet\'s `` RuntimeConfiguration `` .\n\nLaunchPath (string) -- [REQUIRED]The location of the server executable in a custom game build or the name of the Realtime script file that contains the Init() function. Game builds and Realtime scripts are installed on instances at the root:\n\nWindows (for custom game builds only): C:\\game . Example: 'C:\\game\\MyGame\\server.exe '\nLinux: /local/game . Examples: '/local/game/MyGame/server.exe ' or '/local/game/MyRealtimeScript.js '\n\n\nParameters (string) --An optional list of parameters to pass to the server executable or Realtime script on launch.\n\nConcurrentExecutions (integer) -- [REQUIRED]The number of server processes that use this configuration to run concurrently on an instance.\n\n\n\n\n\nMaxConcurrentGameSessionActivations (integer) --The maximum number of game sessions with status ACTIVATING to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.\n\nGameSessionActivationTimeoutSeconds (integer) --The maximum amount of time (in seconds) that a game session can remain in status ACTIVATING . If the game session is not active before the timeout, activation is terminated and the game session status is changed to TERMINATED .\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Represents the returned data in response to a request action.

RuntimeConfiguration (dict) --
The runtime configuration currently in force. If the update was successful, this object matches the one in the request.

ServerProcesses (list) --
A collection of server process configurations that describe which server processes to run on each instance in a fleet.

(dict) --
A set of instructions for launching server processes on each instance in a fleet. Server processes run either a custom game build executable or a Realtime Servers script. Each instruction set identifies the location of the custom game build executable or Realtime launch script, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet\'s ``  RuntimeConfiguration `` .

LaunchPath (string) --
The location of the server executable in a custom game build or the name of the Realtime script file that contains the Init() function. Game builds and Realtime scripts are installed on instances at the root:

Windows (for custom game builds only): C:\\game . Example: "C:\\game\\MyGame\\server.exe "
Linux: /local/game . Examples: "/local/game/MyGame/server.exe " or "/local/game/MyRealtimeScript.js "


Parameters (string) --
An optional list of parameters to pass to the server executable or Realtime script on launch.

ConcurrentExecutions (integer) --
The number of server processes that use this configuration to run concurrently on an instance.





MaxConcurrentGameSessionActivations (integer) --
The maximum number of game sessions with status ACTIVATING to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.

GameSessionActivationTimeoutSeconds (integer) --
The maximum amount of time (in seconds) that a game session can remain in status ACTIVATING . If the game session is not active before the timeout, activation is terminated and the game session status is changed to TERMINATED .









Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.InvalidFleetStatusException


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
    A unique identifier for a fleet to update runtime configuration for. You can use either the fleet ID or ARN value.
    
    RuntimeConfiguration (dict) -- [REQUIRED]
    Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime Servers script. The runtime configuration lists the types of server processes to run on an instance and includes the following configuration settings: the server executable or launch script file, launch parameters, and the number of processes to run concurrently on each instance. A CreateFleet request must include a runtime configuration with at least one server process configuration.
    
    ServerProcesses (list) --A collection of server process configurations that describe which server processes to run on each instance in a fleet.
    
    (dict) --A set of instructions for launching server processes on each instance in a fleet. Server processes run either a custom game build executable or a Realtime Servers script. Each instruction set identifies the location of the custom game build executable or Realtime launch script, optional launch parameters, and the number of server processes with this configuration to maintain concurrently on the instance. Server process configurations make up a fleet\'s ``  RuntimeConfiguration `` .
    
    LaunchPath (string) -- [REQUIRED]The location of the server executable in a custom game build or the name of the Realtime script file that contains the Init() function. Game builds and Realtime scripts are installed on instances at the root:
    
    Windows (for custom game builds only): C:\\game . Example: "C:\\game\\MyGame\\server.exe "
    Linux: /local/game . Examples: "/local/game/MyGame/server.exe " or "/local/game/MyRealtimeScript.js "
    
    
    Parameters (string) --An optional list of parameters to pass to the server executable or Realtime script on launch.
    
    ConcurrentExecutions (integer) -- [REQUIRED]The number of server processes that use this configuration to run concurrently on an instance.
    
    
    
    
    
    MaxConcurrentGameSessionActivations (integer) --The maximum number of game sessions with status ACTIVATING to allow on an instance simultaneously. This setting limits the amount of instance resources that can be used for new game activations at any one time.
    
    GameSessionActivationTimeoutSeconds (integer) --The maximum amount of time (in seconds) that a game session can remain in status ACTIVATING . If the game session is not active before the timeout, activation is terminated and the game session status is changed to TERMINATED .
    
    
    
    
    """
    pass

def update_script(ScriptId=None, Name=None, Version=None, StorageLocation=None, ZipFile=None):
    """
    Updates Realtime script metadata and content.
    To update script metadata, specify the script ID and provide updated name and/or version values.
    To update script content, provide an updated zip file by pointing to either a local file or an Amazon S3 bucket location. You can use either method regardless of how the original script was uploaded. Use the Version parameter to track updates to the script.
    If the call is successful, the updated metadata is stored in the script record and a revised script is uploaded to the Amazon GameLift service. Once the script is updated and acquired by a fleet instance, the new version is used for all new game sessions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_script(
        ScriptId='string',
        Name='string',
        Version='string',
        StorageLocation={
            'Bucket': 'string',
            'Key': 'string',
            'RoleArn': 'string',
            'ObjectVersion': 'string'
        },
        ZipFile=b'bytes'
    )
    
    
    :type ScriptId: string
    :param ScriptId: [REQUIRED]\nA unique identifier for a Realtime script to update. You can use either the script ID or ARN value.\n

    :type Name: string
    :param Name: A descriptive label that is associated with a script. Script names do not need to be unique.

    :type Version: string
    :param Version: The version that is associated with a build or script. Version strings do not need to be unique.

    :type StorageLocation: dict
    :param StorageLocation: The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the 'key'), and a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ObjectVersion parameter to specify an earlier version.\n\nBucket (string) --An S3 bucket identifier. This is the name of the S3 bucket.\n\nKey (string) --The name of the zip file that contains the build files or script files.\n\nRoleArn (string) --The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access the S3 bucket.\n\nObjectVersion (string) --The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.\n\n\n

    :type ZipFile: bytes
    :param ZipFile: A data object containing your Realtime scripts and dependencies as a zip file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.\nWhen using the AWS CLI tool to create a script, this parameter is set to the zip file name. It must be prepended with the string 'fileb://' to indicate that the file data is a binary object. For example: --zip-file fileb://myRealtimeScript.zip .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Script': {
        'ScriptId': 'string',
        'ScriptArn': 'string',
        'Name': 'string',
        'Version': 'string',
        'SizeOnDisk': 123,
        'CreationTime': datetime(2015, 1, 1),
        'StorageLocation': {
            'Bucket': 'string',
            'Key': 'string',
            'RoleArn': 'string',
            'ObjectVersion': 'string'
        }
    }
}


Response Structure

(dict) --

Script (dict) --
The newly created script record with a unique script ID. The new script\'s storage location reflects an Amazon S3 location: (1) If the script was uploaded from an S3 bucket under your account, the storage location reflects the information that was provided in the CreateScript request; (2) If the script file was uploaded from a local zip file, the storage location reflects an S3 location controls by the Amazon GameLift service.

ScriptId (string) --
A unique identifier for a Realtime script

ScriptArn (string) --
Amazon Resource Name (ARN ) that is assigned to a GameLift script resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift script ARN, the resource ID matches the ScriptId value.

Name (string) --
A descriptive label that is associated with a script. Script names do not need to be unique.

Version (string) --
The version that is associated with a build or script. Version strings do not need to be unique.

SizeOnDisk (integer) --
The file size of the uploaded Realtime script, expressed in bytes. When files are uploaded from an S3 location, this value remains at "0".

CreationTime (datetime) --
A time stamp indicating when this data object was created. The format is a number expressed in Unix time as milliseconds (for example "1469498468.057").

StorageLocation (dict) --
The location in S3 where build or script files are stored for access by Amazon GameLift. This location is specified in  CreateBuild ,  CreateScript , and  UpdateScript requests.

Bucket (string) --
An S3 bucket identifier. This is the name of the S3 bucket.

Key (string) --
The name of the zip file that contains the build files or script files.

RoleArn (string) --
The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access the S3 bucket.

ObjectVersion (string) --
The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.











Exceptions

GameLift.Client.exceptions.UnauthorizedException
GameLift.Client.exceptions.InvalidRequestException
GameLift.Client.exceptions.NotFoundException
GameLift.Client.exceptions.InternalServiceException


    :return: {
        'Script': {
            'ScriptId': 'string',
            'ScriptArn': 'string',
            'Name': 'string',
            'Version': 'string',
            'SizeOnDisk': 123,
            'CreationTime': datetime(2015, 1, 1),
            'StorageLocation': {
                'Bucket': 'string',
                'Key': 'string',
                'RoleArn': 'string',
                'ObjectVersion': 'string'
            }
        }
    }
    
    
    :returns: 
    ScriptId (string) -- [REQUIRED]
    A unique identifier for a Realtime script to update. You can use either the script ID or ARN value.
    
    Name (string) -- A descriptive label that is associated with a script. Script names do not need to be unique.
    Version (string) -- The version that is associated with a build or script. Version strings do not need to be unique.
    StorageLocation (dict) -- The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ObjectVersion parameter to specify an earlier version.
    
    Bucket (string) --An S3 bucket identifier. This is the name of the S3 bucket.
    
    Key (string) --The name of the zip file that contains the build files or script files.
    
    RoleArn (string) --The Amazon Resource Name (ARN ) for an IAM role that allows Amazon GameLift to access the S3 bucket.
    
    ObjectVersion (string) --The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.
    
    
    
    ZipFile (bytes) -- A data object containing your Realtime scripts and dependencies as a zip file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.
    When using the AWS CLI tool to create a script, this parameter is set to the zip file name. It must be prepended with the string "fileb://" to indicate that the file data is a binary object. For example: --zip-file fileb://myRealtimeScript.zip .
    
    
    """
    pass

def validate_matchmaking_rule_set(RuleSetBody=None):
    """
    Validates the syntax of a matchmaking rule or rule set. This operation checks that the rule set is using syntactically correct JSON and that it conforms to allowed property expressions. To validate syntax, provide a rule set JSON string.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.validate_matchmaking_rule_set(
        RuleSetBody='string'
    )
    
    
    :type RuleSetBody: string
    :param RuleSetBody: [REQUIRED]\nA collection of matchmaking rules to validate, formatted as a JSON string.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Valid': True|False
}


Response Structure

(dict) --Represents the returned data in response to a request action.

Valid (boolean) --A response indicating whether the rule set is valid.






Exceptions

GameLift.Client.exceptions.InternalServiceException
GameLift.Client.exceptions.UnsupportedRegionException
GameLift.Client.exceptions.InvalidRequestException


    :return: {
        'Valid': True|False
    }
    
    
    :returns: 
    CreateMatchmakingConfiguration
    DescribeMatchmakingConfigurations
    UpdateMatchmakingConfiguration
    DeleteMatchmakingConfiguration
    CreateMatchmakingRuleSet
    DescribeMatchmakingRuleSets
    ValidateMatchmakingRuleSet
    DeleteMatchmakingRuleSet
    
    """
    pass

