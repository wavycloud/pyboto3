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

def batch_delete_builds(ids=None):
    """
    Deletes one or more builds.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_delete_builds(
        ids=[
            'string',
        ]
    )
    
    
    :type ids: list
    :param ids: [REQUIRED]\nThe IDs of the builds to delete.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'buildsDeleted': [
        'string',
    ],
    'buildsNotDeleted': [
        {
            'id': 'string',
            'statusCode': 'string'
        },
    ]
}


Response Structure

(dict) --
buildsDeleted (list) --The IDs of the builds that were successfully deleted.

(string) --


buildsNotDeleted (list) --Information about any builds that could not be successfully deleted.

(dict) --Information about a build that could not be successfully deleted.

id (string) --The ID of the build that could not be successfully deleted.

statusCode (string) --Additional information about the build that could not be successfully deleted.










Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'buildsDeleted': [
            'string',
        ],
        'buildsNotDeleted': [
            {
                'id': 'string',
                'statusCode': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_get_builds(ids=None):
    """
    Gets information about one or more builds.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    The following example gets information about builds with the specified build IDs.
    Expected Output:
    
    :example: response = client.batch_get_builds(
        ids=[
            'string',
        ]
    )
    
    
    :type ids: list
    :param ids: [REQUIRED]\nThe IDs of the builds.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'builds': [
        {
            'id': 'string',
            'arn': 'string',
            'buildNumber': 123,
            'startTime': datetime(2015, 1, 1),
            'endTime': datetime(2015, 1, 1),
            'currentPhase': 'string',
            'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
            'sourceVersion': 'string',
            'resolvedSourceVersion': 'string',
            'projectName': 'string',
            'phases': [
                {
                    'phaseType': 'SUBMITTED'|'QUEUED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                    'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'durationInSeconds': 123,
                    'contexts': [
                        {
                            'statusCode': 'string',
                            'message': 'string'
                        },
                    ]
                },
            ],
            'source': {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
            'secondarySources': [
                {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'gitSubmodulesConfig': {
                        'fetchSubmodules': True|False
                    },
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
            ],
            'secondarySourceVersions': [
                {
                    'sourceIdentifier': 'string',
                    'sourceVersion': 'string'
                },
            ],
            'artifacts': {
                'location': 'string',
                'sha256sum': 'string',
                'md5sum': 'string',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
            'secondaryArtifacts': [
                {
                    'location': 'string',
                    'sha256sum': 'string',
                    'md5sum': 'string',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
            ],
            'cache': {
                'type': 'NO_CACHE'|'S3'|'LOCAL',
                'location': 'string',
                'modes': [
                    'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                ]
            },
            'environment': {
                'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
                'image': 'string',
                'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                'environmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                    },
                ],
                'privilegedMode': True|False,
                'certificate': 'string',
                'registryCredential': {
                    'credential': 'string',
                    'credentialProvider': 'SECRETS_MANAGER'
                },
                'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
            },
            'serviceRole': 'string',
            'logs': {
                'groupName': 'string',
                'streamName': 'string',
                'deepLink': 'string',
                's3DeepLink': 'string',
                'cloudWatchLogsArn': 'string',
                's3LogsArn': 'string',
                'cloudWatchLogs': {
                    'status': 'ENABLED'|'DISABLED',
                    'groupName': 'string',
                    'streamName': 'string'
                },
                's3Logs': {
                    'status': 'ENABLED'|'DISABLED',
                    'location': 'string',
                    'encryptionDisabled': True|False
                }
            },
            'timeoutInMinutes': 123,
            'queuedTimeoutInMinutes': 123,
            'buildComplete': True|False,
            'initiator': 'string',
            'vpcConfig': {
                'vpcId': 'string',
                'subnets': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ]
            },
            'networkInterface': {
                'subnetId': 'string',
                'networkInterfaceId': 'string'
            },
            'encryptionKey': 'string',
            'exportedEnvironmentVariables': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ],
            'reportArns': [
                'string',
            ],
            'fileSystemLocations': [
                {
                    'type': 'EFS',
                    'location': 'string',
                    'mountPoint': 'string',
                    'identifier': 'string',
                    'mountOptions': 'string'
                },
            ]
        },
    ],
    'buildsNotFound': [
        'string',
    ]
}


Response Structure

(dict) --
builds (list) --Information about the requested builds.

(dict) --Information about a build.

id (string) --The unique ID for the build.

arn (string) --The Amazon Resource Name (ARN) of the build.

buildNumber (integer) --The number of the build. For each project, the buildNumber of its first build is 1 . The buildNumber of each subsequent build is incremented by 1 . If a build is deleted, the buildNumber of other builds does not change.

startTime (datetime) --When the build process started, expressed in Unix time format.

endTime (datetime) --When the build process ended, expressed in Unix time format.

currentPhase (string) --The current build phase.

buildStatus (string) --The current status of the build. Valid values include:

FAILED : The build failed.
FAULT : The build faulted.
IN_PROGRESS : The build is still in progress.
STOPPED : The build stopped.
SUCCEEDED : The build succeeded.
TIMED_OUT : The build timed out.


sourceVersion (string) --Any version identifier for the version of the source code to be built. If sourceVersion is specified at the project level, then this sourceVersion (at the build level) takes precedence.
For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .

resolvedSourceVersion (string) --An identifier for the version of this build\'s source code.

For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.
For AWS CodePipeline, the source revision provided by AWS CodePipeline.
For Amazon Simple Storage Service (Amazon S3), this does not apply.


projectName (string) --The name of the AWS CodeBuild project.

phases (list) --Information about all previous build phases that are complete and information about any current build phase that is not yet complete.

(dict) --Information about a stage for a build.

phaseType (string) --The name of the build phase. Valid values include:

BUILD : Core build activities typically occur in this build phase.
COMPLETED : The build has been completed.
DOWNLOAD_SOURCE : Source code is being downloaded in this build phase.
FINALIZING : The build process is completing in this build phase.
INSTALL : Installation activities typically occur in this build phase.
POST_BUILD : Post-build activities typically occur in this build phase.
PRE_BUILD : Pre-build activities typically occur in this build phase.
PROVISIONING : The build environment is being set up.
QUEUED : The build has been submitted and is queued behind other submitted builds.
SUBMITTED : The build has been submitted.
UPLOAD_ARTIFACTS : Build output artifacts are being uploaded to the output location.


phaseStatus (string) --The current status of the build phase. Valid values include:

FAILED : The build phase failed.
FAULT : The build phase faulted.
IN_PROGRESS : The build phase is still in progress.
QUEUED : The build has been submitted and is queued behind other submitted builds.
STOPPED : The build phase stopped.
SUCCEEDED : The build phase succeeded.
TIMED_OUT : The build phase timed out.


startTime (datetime) --When the build phase started, expressed in Unix time format.

endTime (datetime) --When the build phase ended, expressed in Unix time format.

durationInSeconds (integer) --How long, in seconds, between the starting and ending times of the build\'s phase.

contexts (list) --Additional information about a build phase, especially to help troubleshoot a failed build.

(dict) --Additional information about a build phase that has an error. You can use this information for troubleshooting.

statusCode (string) --The status code for the context of the build phase.

message (string) --An explanation of the build phase\'s context. This might include a command ID and an exit code.









source (dict) --Information about the source code to be built.

type (string) --The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --
Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --An identifier for this project source.



secondarySources (list) --An array of ProjectSource objects.

(dict) --Information about the build input source code for the build project.

type (string) --The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --
Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --An identifier for this project source.





secondarySourceVersions (list) --An array of ProjectSourceVersion objects. Each ProjectSourceVersion must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.


(dict) --A source identifier and its corresponding version.

sourceIdentifier (string) --An identifier for a source in the build project.

sourceVersion (string) --The source version for the corresponding source identifier. If specified, must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.

For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .





artifacts (dict) --Information about the output artifacts for the build.

location (string) --Information about the location of the build artifacts.

sha256sum (string) --The SHA-256 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


md5sum (string) --The MD5 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


overrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --Information that tells you if encryption for build artifacts is disabled.

artifactIdentifier (string) --An identifier for this artifact definition.



secondaryArtifacts (list) --An array of ProjectArtifacts objects.

(dict) --Information about build output artifacts.

location (string) --Information about the location of the build artifacts.

sha256sum (string) --The SHA-256 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


md5sum (string) --The MD5 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


overrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --Information that tells you if encryption for build artifacts is disabled.

artifactIdentifier (string) --An identifier for this artifact definition.





cache (dict) --Information about the cache for the build.

type (string) --The type of cache used by the build project. Valid values include:

NO_CACHE : The build project does not use any cache.
S3 : The build project reads and writes from and to S3.
LOCAL : The build project stores a cache locally on a build host that is only available to that build host.


location (string) --Information about the cache location:

NO_CACHE or LOCAL : This value is ignored.
S3 : This is the S3 bucket name/prefix.


modes (list) --If you use a LOCAL cache, the local cache mode. You can use one or more local cache modes at the same time.

LOCAL_SOURCE_CACHE mode caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.
LOCAL_DOCKER_LAYER_CACHE mode caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.


Note

You can use a Docker layer cache in the Linux environment only.
The privileged flag must be set so that your project has the required Docker permissions.
You should consider the security implications before you use a Docker layer cache.



LOCAL_CUSTOM_CACHE mode caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:
Only directories can be specified for caching. You cannot specify individual files.
Symlinks are used to reference cached directories.
Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.




(string) --




environment (dict) --Information about the build environment for this build.

type (string) --The type of build environment to use for related builds.

The environment type ARM_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).
The environment type LINUX_CONTAINER with compute type build.general1.2xlarge is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).
The environment type LINUX_GPU_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).


image (string) --The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:

For an image tag: registry/repository:tag . For example, to specify an image with the tag "latest," use registry/repository:latest .
For an image digest: registry/repository@digest . For example, to specify an image with the digest "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf .


computeType (string) --Information about the compute resources the build project uses. Available values include:

BUILD_GENERAL1_SMALL : Use up to 3 GB memory and 2 vCPUs for builds.
BUILD_GENERAL1_MEDIUM : Use up to 7 GB memory and 4 vCPUs for builds.
BUILD_GENERAL1_LARGE : Use up to 16 GB memory and 8 vCPUs for builds, depending on your environment type.
BUILD_GENERAL1_2XLARGE : Use up to 145 GB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.

If you use BUILD_GENERAL1_LARGE :

For environment type LINUX_CONTAINER , you can use up to 15 GB memory and 8 vCPUs for builds.
For environment type LINUX_GPU_CONTAINER , you can use up to 255 GB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.
For environment type ARM_CONTAINER , you can use up to 16 GB memory and 8 vCPUs on ARM-based processors for builds.

For more information, see Build Environment Compute Types in the AWS CodeBuild User Guide.

environmentVariables (list) --A set of environment variables to make available to builds for this build project.

(dict) --Information about an environment variable for a build project or a build.

name (string) --The name or key of the environment variable.

value (string) --The value of the environment variable.

Warning
We strongly discourage the use of PLAINTEXT environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. PLAINTEXT environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI). For sensitive values, we recommend you use an environment variable of type PARAMETER_STORE or SECRETS_MANAGER .


type (string) --The type of environment variable. Valid values include:

PARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. To learn how to specify a parameter store environment variable, see parameter store reference-key in the buildspec file .
PLAINTEXT : An environment variable in plain text format. This is the default value.
SECRETS_MANAGER : An environment variable stored in AWS Secrets Manager. To learn how to specify a secrets manager environment variable, see secrets manager reference-key in the buildspec file .






privilegedMode (boolean) --Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is false .
You can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:
If the operating system\'s base image is Ubuntu Linux:

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"

If the operating system\'s base image is Alpine Linux and the previous command does not work, add the -t argument to timeout :

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"


certificate (string) --The certificate to use with this build project.

registryCredential (dict) --The credentials for access to a private registry.

credential (string) --The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

Note
The credential can use the name of the credentials only if they exist in your current AWS Region.


credentialProvider (string) --The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.



imagePullCredentialsType (string) --The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid values:

CODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild\'s service principal.
SERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.

When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.



serviceRole (string) --The name of a service role used for this build.

logs (dict) --Information about the build\'s logs in Amazon CloudWatch Logs.

groupName (string) --The name of the Amazon CloudWatch Logs group for the build logs.

streamName (string) --The name of the Amazon CloudWatch Logs stream for the build logs.

deepLink (string) --The URL to an individual build log in Amazon CloudWatch Logs.

s3DeepLink (string) --The URL to a build log in an S3 bucket.

cloudWatchLogsArn (string) --The ARN of Amazon CloudWatch Logs for a build project. Its format is arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName} . For more information, see Resources Defined by Amazon CloudWatch Logs .

s3LogsArn (string) --The ARN of S3 logs for a build project. Its format is arn:${Partition}:s3:::${BucketName}/${ObjectName} . For more information, see Resources Defined by Amazon S3 .

cloudWatchLogs (dict) --Information about Amazon CloudWatch Logs for a build project.

status (string) --The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:

ENABLED : Amazon CloudWatch Logs are enabled for this build project.
DISABLED : Amazon CloudWatch Logs are not enabled for this build project.


groupName (string) --The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .

streamName (string) --The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .



s3Logs (dict) --Information about S3 logs for a build project.

status (string) --The current status of the S3 build logs. Valid values are:

ENABLED : S3 build logs are enabled for this build project.
DISABLED : S3 build logs are not enabled for this build project.


location (string) --The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .

encryptionDisabled (boolean) --Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.





timeoutInMinutes (integer) --How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.

queuedTimeoutInMinutes (integer) --The number of minutes a build is allowed to be queued before it times out.

buildComplete (boolean) --Whether the build is complete. True if complete; otherwise, false.

initiator (string) --The entity that started the build. Valid values include:

If AWS CodePipeline started the build, the pipeline\'s name (for example, codepipeline/my-demo-pipeline ).
If an AWS Identity and Access Management (IAM) user started the build, the user\'s name (for example, MyUserName ).
If the Jenkins plugin for AWS CodeBuild started the build, the string CodeBuild-Jenkins-Plugin .


vpcConfig (dict) --If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.

vpcId (string) --The ID of the Amazon VPC.

subnets (list) --A list of one or more subnet IDs in your Amazon VPC.

(string) --


securityGroupIds (list) --A list of one or more security groups IDs in your Amazon VPC.

(string) --




networkInterface (dict) --Describes a network interface.

subnetId (string) --The ID of the subnet.

networkInterfaceId (string) --The ID of the network interface.



encryptionKey (string) --The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

Note
You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK\'s alias (using the format ``alias/alias-name `` ).

exportedEnvironmentVariables (list) --A list of exported environment variables for this build.

(dict) --Information about an exported environment variable.

name (string) --The name of this exported environment variable.

value (string) --The value assigned to this exported environment variable.

Note
During a build, the value of a variable is available starting with the install phase. It can be updated between the start of the install phase and the end of the post_build phase. After the post_build phase ends, the value of exported variables cannot change.






reportArns (list) --An array of the ARNs associated with this build\'s reports.

(string) --


fileSystemLocations (list) --An array of ProjectFileSystemLocation objects for a CodeBuild build project. A ProjectFileSystemLocation object specifies the identifier , location , mountOptions , mountPoint , and type of a file system created using Amazon Elastic File System.

(dict) --Information about a file system created by Amazon Elastic File System (EFS). For more information, see What Is Amazon Elastic File System?

type (string) --The type of the file system. The one supported type is EFS .

location (string) --A string that specifies the location of the file system created by Amazon EFS. Its format is efs-dns-name:/directory-path . You can find the DNS name of file system when you view it in the AWS EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is fs-abcd1234.efs.us-west-2.amazonaws.com , and its mount directory is my-efs-mount-directory , then the location is fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory .
The directory path in the format efs-dns-name:/directory-path is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.

mountPoint (string) --The location in the container where you mount the file system.

identifier (string) --The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the identifier in all capital letters to CODEBUILD_ . For example, if you specify my-efs for identifier , a new environment variable is create named CODEBUILD_MY-EFS .
The identifier is used to mount your file system.

mountOptions (string) --The mount options for a file system created by AWS EFS. The default mount options used by CodeBuild are nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 . For more information, see Recommended NFS Mount Options .









buildsNotFound (list) --The IDs of builds for which information could not be found.

(string) --







Exceptions

CodeBuild.Client.exceptions.InvalidInputException

Examples
The following example gets information about builds with the specified build IDs.
response = client.batch_get_builds(
    ids=[
        'codebuild-demo-project:9b0ac37f-d19e-4254-9079-f47e9a389eEX',
        'codebuild-demo-project:b79a46f7-1473-4636-a23f-da9c45c208EX',
    ],
)

print(response)


Expected Output:
{
    'builds': [
        {
            'arn': 'arn:aws:codebuild:us-east-1:123456789012:build/codebuild-demo-project:9b0ac37f-d19e-4254-9079-f47e9a389eEX',
            'artifacts': {
                'location': 'arn:aws:s3:::codebuild-123456789012-output-bucket/codebuild-demo-project',
            },
            'buildComplete': True,
            'buildStatus': 'SUCCEEDED',
            'currentPhase': 'COMPLETED',
            'endTime': 1479832474.764,
            'environment': {
                'type': 'LINUX_CONTAINER',
                'computeType': 'BUILD_GENERAL1_SMALL',
                'environmentVariables': [
                ],
                'image': 'aws/codebuild/java:openjdk-8',
                'privilegedMode': False,
            },
            'id': 'codebuild-demo-project:9b0ac37f-d19e-4254-9079-f47e9a389eEX',
            'initiator': 'MyDemoUser',
            'logs': {
                'deepLink': 'https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logEvent:group=/aws/codebuild/codebuild-demo-project;stream=9b0ac37f-d19e-4254-9079-f47e9a389eEX',
                'groupName': '/aws/codebuild/codebuild-demo-project',
                'streamName': '9b0ac37f-d19e-4254-9079-f47e9a389eEX',
            },
            'phases': [
                {
                    'durationInSeconds': 0,
                    'endTime': 1479832342.23,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'SUBMITTED',
                    'startTime': 1479832341.854,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 72,
                    'endTime': 1479832415.064,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'PROVISIONING',
                    'startTime': 1479832342.23,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 46,
                    'endTime': 1479832461.261,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'DOWNLOAD_SOURCE',
                    'startTime': 1479832415.064,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 0,
                    'endTime': 1479832461.354,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'INSTALL',
                    'startTime': 1479832461.261,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 0,
                    'endTime': 1479832461.448,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'PRE_BUILD',
                    'startTime': 1479832461.354,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 9,
                    'endTime': 1479832471.115,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'BUILD',
                    'startTime': 1479832461.448,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 0,
                    'endTime': 1479832471.224,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'POST_BUILD',
                    'startTime': 1479832471.115,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 0,
                    'endTime': 1479832471.791,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'UPLOAD_ARTIFACTS',
                    'startTime': 1479832471.224,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 2,
                    'endTime': 1479832474.764,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'FINALIZING',
                    'startTime': 1479832471.791,
                },
                {
                    'phaseType': 'COMPLETED',
                    'startTime': 1479832474.764,
                },
            ],
            'projectName': 'codebuild-demo-project',
            'source': {
                'type': 'S3',
                'buildspec': '',
                'location': 'arn:aws:s3:::codebuild-123456789012-input-bucket/MessageUtil.zip',
            },
            'startTime': 1479832341.854,
            'timeoutInMinutes': 60,
        },
        {
            'arn': 'arn:aws:codebuild:us-east-1:123456789012:build/codebuild-demo-project:b79a46f7-1473-4636-a23f-da9c45c208EX',
            'artifacts': {
                'location': 'arn:aws:s3:::codebuild-123456789012-output-bucket/codebuild-demo-project',
            },
            'buildComplete': True,
            'buildStatus': 'SUCCEEDED',
            'currentPhase': 'COMPLETED',
            'endTime': 1479401214.239,
            'environment': {
                'type': 'LINUX_CONTAINER',
                'computeType': 'BUILD_GENERAL1_SMALL',
                'environmentVariables': [
                ],
                'image': 'aws/codebuild/java:openjdk-8',
                'privilegedMode': False,
            },
            'id': 'codebuild-demo-project:b79a46f7-1473-4636-a23f-da9c45c208EX',
            'initiator': 'MyDemoUser',
            'logs': {
                'deepLink': 'https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logEvent:group=/aws/codebuild/codebuild-demo-project;stream=b79a46f7-1473-4636-a23f-da9c45c208EX',
                'groupName': '/aws/codebuild/codebuild-demo-project',
                'streamName': 'b79a46f7-1473-4636-a23f-da9c45c208EX',
            },
            'phases': [
                {
                    'durationInSeconds': 0,
                    'endTime': 1479401082.342,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'SUBMITTED',
                    'startTime': 1479401081.869,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 71,
                    'endTime': 1479401154.129,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'PROVISIONING',
                    'startTime': 1479401082.342,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 45,
                    'endTime': 1479401199.136,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'DOWNLOAD_SOURCE',
                    'startTime': 1479401154.129,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 0,
                    'endTime': 1479401199.236,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'INSTALL',
                    'startTime': 1479401199.136,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 0,
                    'endTime': 1479401199.345,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'PRE_BUILD',
                    'startTime': 1479401199.236,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 9,
                    'endTime': 1479401208.68,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'BUILD',
                    'startTime': 1479401199.345,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 0,
                    'endTime': 1479401208.783,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'POST_BUILD',
                    'startTime': 1479401208.68,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 0,
                    'endTime': 1479401209.463,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'UPLOAD_ARTIFACTS',
                    'startTime': 1479401208.783,
                },
                {
                    'contexts': [
                    ],
                    'durationInSeconds': 4,
                    'endTime': 1479401214.239,
                    'phaseStatus': 'SUCCEEDED',
                    'phaseType': 'FINALIZING',
                    'startTime': 1479401209.463,
                },
                {
                    'phaseType': 'COMPLETED',
                    'startTime': 1479401214.239,
                },
            ],
            'projectName': 'codebuild-demo-project',
            'source': {
                'type': 'S3',
                'location': 'arn:aws:s3:::codebuild-123456789012-input-bucket/MessageUtil.zip',
            },
            'startTime': 1479401081.869,
            'timeoutInMinutes': 60,
        },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'builds': [
            {
                'id': 'string',
                'arn': 'string',
                'buildNumber': 123,
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'currentPhase': 'string',
                'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                'sourceVersion': 'string',
                'resolvedSourceVersion': 'string',
                'projectName': 'string',
                'phases': [
                    {
                        'phaseType': 'SUBMITTED'|'QUEUED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                        'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                        'startTime': datetime(2015, 1, 1),
                        'endTime': datetime(2015, 1, 1),
                        'durationInSeconds': 123,
                        'contexts': [
                            {
                                'statusCode': 'string',
                                'message': 'string'
                            },
                        ]
                    },
                ],
                'source': {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'gitSubmodulesConfig': {
                        'fetchSubmodules': True|False
                    },
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
                'secondarySources': [
                    {
                        'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                        'location': 'string',
                        'gitCloneDepth': 123,
                        'gitSubmodulesConfig': {
                            'fetchSubmodules': True|False
                        },
                        'buildspec': 'string',
                        'auth': {
                            'type': 'OAUTH',
                            'resource': 'string'
                        },
                        'reportBuildStatus': True|False,
                        'insecureSsl': True|False,
                        'sourceIdentifier': 'string'
                    },
                ],
                'secondarySourceVersions': [
                    {
                        'sourceIdentifier': 'string',
                        'sourceVersion': 'string'
                    },
                ],
                'artifacts': {
                    'location': 'string',
                    'sha256sum': 'string',
                    'md5sum': 'string',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
                'secondaryArtifacts': [
                    {
                        'location': 'string',
                        'sha256sum': 'string',
                        'md5sum': 'string',
                        'overrideArtifactName': True|False,
                        'encryptionDisabled': True|False,
                        'artifactIdentifier': 'string'
                    },
                ],
                'cache': {
                    'type': 'NO_CACHE'|'S3'|'LOCAL',
                    'location': 'string',
                    'modes': [
                        'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                    ]
                },
                'environment': {
                    'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
                    'image': 'string',
                    'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                    'environmentVariables': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                        },
                    ],
                    'privilegedMode': True|False,
                    'certificate': 'string',
                    'registryCredential': {
                        'credential': 'string',
                        'credentialProvider': 'SECRETS_MANAGER'
                    },
                    'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
                },
                'serviceRole': 'string',
                'logs': {
                    'groupName': 'string',
                    'streamName': 'string',
                    'deepLink': 'string',
                    's3DeepLink': 'string',
                    'cloudWatchLogsArn': 'string',
                    's3LogsArn': 'string',
                    'cloudWatchLogs': {
                        'status': 'ENABLED'|'DISABLED',
                        'groupName': 'string',
                        'streamName': 'string'
                    },
                    's3Logs': {
                        'status': 'ENABLED'|'DISABLED',
                        'location': 'string',
                        'encryptionDisabled': True|False
                    }
                },
                'timeoutInMinutes': 123,
                'queuedTimeoutInMinutes': 123,
                'buildComplete': True|False,
                'initiator': 'string',
                'vpcConfig': {
                    'vpcId': 'string',
                    'subnets': [
                        'string',
                    ],
                    'securityGroupIds': [
                        'string',
                    ]
                },
                'networkInterface': {
                    'subnetId': 'string',
                    'networkInterfaceId': 'string'
                },
                'encryptionKey': 'string',
                'exportedEnvironmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string'
                    },
                ],
                'reportArns': [
                    'string',
                ],
                'fileSystemLocations': [
                    {
                        'type': 'EFS',
                        'location': 'string',
                        'mountPoint': 'string',
                        'identifier': 'string',
                        'mountOptions': 'string'
                    },
                ]
            },
        ],
        'buildsNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    FAILED : The build failed.
    FAULT : The build faulted.
    IN_PROGRESS : The build is still in progress.
    STOPPED : The build stopped.
    SUCCEEDED : The build succeeded.
    TIMED_OUT : The build timed out.
    
    """
    pass

def batch_get_projects(names=None):
    """
    Gets information about one or more build projects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_projects(
        names=[
            'string',
        ]
    )
    
    
    :type names: list
    :param names: [REQUIRED]\nThe names or ARNs of the build projects. To get information about a project shared with your AWS account, its ARN must be specified. You cannot specify a shared project using its name.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'projects': [
        {
            'name': 'string',
            'arn': 'string',
            'description': 'string',
            'source': {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
            'secondarySources': [
                {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'gitSubmodulesConfig': {
                        'fetchSubmodules': True|False
                    },
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
            ],
            'sourceVersion': 'string',
            'secondarySourceVersions': [
                {
                    'sourceIdentifier': 'string',
                    'sourceVersion': 'string'
                },
            ],
            'artifacts': {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
            'secondaryArtifacts': [
                {
                    'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                    'location': 'string',
                    'path': 'string',
                    'namespaceType': 'NONE'|'BUILD_ID',
                    'name': 'string',
                    'packaging': 'NONE'|'ZIP',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
            ],
            'cache': {
                'type': 'NO_CACHE'|'S3'|'LOCAL',
                'location': 'string',
                'modes': [
                    'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                ]
            },
            'environment': {
                'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
                'image': 'string',
                'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                'environmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                    },
                ],
                'privilegedMode': True|False,
                'certificate': 'string',
                'registryCredential': {
                    'credential': 'string',
                    'credentialProvider': 'SECRETS_MANAGER'
                },
                'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
            },
            'serviceRole': 'string',
            'timeoutInMinutes': 123,
            'queuedTimeoutInMinutes': 123,
            'encryptionKey': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'created': datetime(2015, 1, 1),
            'lastModified': datetime(2015, 1, 1),
            'webhook': {
                'url': 'string',
                'payloadUrl': 'string',
                'secret': 'string',
                'branchFilter': 'string',
                'filterGroups': [
                    [
                        {
                            'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                            'pattern': 'string',
                            'excludeMatchedPattern': True|False
                        },
                    ],
                ],
                'lastModifiedSecret': datetime(2015, 1, 1)
            },
            'vpcConfig': {
                'vpcId': 'string',
                'subnets': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ]
            },
            'badge': {
                'badgeEnabled': True|False,
                'badgeRequestUrl': 'string'
            },
            'logsConfig': {
                'cloudWatchLogs': {
                    'status': 'ENABLED'|'DISABLED',
                    'groupName': 'string',
                    'streamName': 'string'
                },
                's3Logs': {
                    'status': 'ENABLED'|'DISABLED',
                    'location': 'string',
                    'encryptionDisabled': True|False
                }
            },
            'fileSystemLocations': [
                {
                    'type': 'EFS',
                    'location': 'string',
                    'mountPoint': 'string',
                    'identifier': 'string',
                    'mountOptions': 'string'
                },
            ]
        },
    ],
    'projectsNotFound': [
        'string',
    ]
}


Response Structure

(dict) --
projects (list) --Information about the requested build projects.

(dict) --Information about a build project.

name (string) --The name of the build project.

arn (string) --The Amazon Resource Name (ARN) of the build project.

description (string) --A description that makes the build project easy to identify.

source (dict) --Information about the build input source code for this build project.

type (string) --The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --
Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --An identifier for this project source.



secondarySources (list) --An array of ProjectSource objects.

(dict) --Information about the build input source code for the build project.

type (string) --The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --
Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --An identifier for this project source.





sourceVersion (string) --A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.

If sourceVersion is specified at the build level, then that version takes precedence over this sourceVersion (at the project level).
For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .

secondarySourceVersions (list) --An array of ProjectSourceVersion objects. If secondarySourceVersions is specified at the build level, then they take over these secondarySourceVersions (at the project level).

(dict) --A source identifier and its corresponding version.

sourceIdentifier (string) --An identifier for a source in the build project.

sourceVersion (string) --The source version for the corresponding source identifier. If specified, must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.

For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .





artifacts (dict) --Information about the build output artifacts for the build project.

type (string) --The type of build output artifact. Valid values include:

CODEPIPELINE : The build project has build output generated through AWS CodePipeline.


Note
The CODEPIPELINE type is not supported for secondaryArtifacts .


NO_ARTIFACTS : The build project does not produce any build output.
S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).


location (string) --Information about the build output artifact location:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output bucket.


path (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.

For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .

namespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
BUILD_ID : Include the build ID in the location of the build output artifact.
NONE : Do not include the build ID. This is the default if namespaceType is not specified.



For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .

name (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

For example:

If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
If path is empty, namespaceType is set to NONE , and name is set to "/ ", the output artifact is stored in the root of the output bucket.
If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to "/ ", the output artifact is stored in ``MyArtifacts/build-ID `` .


packaging (string) --The type of build output artifact to create:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.




overrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.

artifactIdentifier (string) --An identifier for this artifact definition.



secondaryArtifacts (list) --An array of ProjectArtifacts objects.

(dict) --Information about the build output artifacts for the build project.

type (string) --The type of build output artifact. Valid values include:

CODEPIPELINE : The build project has build output generated through AWS CodePipeline.


Note
The CODEPIPELINE type is not supported for secondaryArtifacts .


NO_ARTIFACTS : The build project does not produce any build output.
S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).


location (string) --Information about the build output artifact location:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output bucket.


path (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.

For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .

namespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
BUILD_ID : Include the build ID in the location of the build output artifact.
NONE : Do not include the build ID. This is the default if namespaceType is not specified.



For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .

name (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

For example:

If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
If path is empty, namespaceType is set to NONE , and name is set to "/ ", the output artifact is stored in the root of the output bucket.
If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to "/ ", the output artifact is stored in ``MyArtifacts/build-ID `` .


packaging (string) --The type of build output artifact to create:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.




overrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.

artifactIdentifier (string) --An identifier for this artifact definition.





cache (dict) --Information about the cache for the build project.

type (string) --The type of cache used by the build project. Valid values include:

NO_CACHE : The build project does not use any cache.
S3 : The build project reads and writes from and to S3.
LOCAL : The build project stores a cache locally on a build host that is only available to that build host.


location (string) --Information about the cache location:

NO_CACHE or LOCAL : This value is ignored.
S3 : This is the S3 bucket name/prefix.


modes (list) --If you use a LOCAL cache, the local cache mode. You can use one or more local cache modes at the same time.

LOCAL_SOURCE_CACHE mode caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.
LOCAL_DOCKER_LAYER_CACHE mode caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.


Note

You can use a Docker layer cache in the Linux environment only.
The privileged flag must be set so that your project has the required Docker permissions.
You should consider the security implications before you use a Docker layer cache.



LOCAL_CUSTOM_CACHE mode caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:
Only directories can be specified for caching. You cannot specify individual files.
Symlinks are used to reference cached directories.
Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.




(string) --




environment (dict) --Information about the build environment for this build project.

type (string) --The type of build environment to use for related builds.

The environment type ARM_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).
The environment type LINUX_CONTAINER with compute type build.general1.2xlarge is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).
The environment type LINUX_GPU_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).


image (string) --The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:

For an image tag: registry/repository:tag . For example, to specify an image with the tag "latest," use registry/repository:latest .
For an image digest: registry/repository@digest . For example, to specify an image with the digest "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf .


computeType (string) --Information about the compute resources the build project uses. Available values include:

BUILD_GENERAL1_SMALL : Use up to 3 GB memory and 2 vCPUs for builds.
BUILD_GENERAL1_MEDIUM : Use up to 7 GB memory and 4 vCPUs for builds.
BUILD_GENERAL1_LARGE : Use up to 16 GB memory and 8 vCPUs for builds, depending on your environment type.
BUILD_GENERAL1_2XLARGE : Use up to 145 GB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.

If you use BUILD_GENERAL1_LARGE :

For environment type LINUX_CONTAINER , you can use up to 15 GB memory and 8 vCPUs for builds.
For environment type LINUX_GPU_CONTAINER , you can use up to 255 GB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.
For environment type ARM_CONTAINER , you can use up to 16 GB memory and 8 vCPUs on ARM-based processors for builds.

For more information, see Build Environment Compute Types in the AWS CodeBuild User Guide.

environmentVariables (list) --A set of environment variables to make available to builds for this build project.

(dict) --Information about an environment variable for a build project or a build.

name (string) --The name or key of the environment variable.

value (string) --The value of the environment variable.

Warning
We strongly discourage the use of PLAINTEXT environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. PLAINTEXT environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI). For sensitive values, we recommend you use an environment variable of type PARAMETER_STORE or SECRETS_MANAGER .


type (string) --The type of environment variable. Valid values include:

PARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. To learn how to specify a parameter store environment variable, see parameter store reference-key in the buildspec file .
PLAINTEXT : An environment variable in plain text format. This is the default value.
SECRETS_MANAGER : An environment variable stored in AWS Secrets Manager. To learn how to specify a secrets manager environment variable, see secrets manager reference-key in the buildspec file .






privilegedMode (boolean) --Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is false .
You can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:
If the operating system\'s base image is Ubuntu Linux:

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"

If the operating system\'s base image is Alpine Linux and the previous command does not work, add the -t argument to timeout :

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"


certificate (string) --The certificate to use with this build project.

registryCredential (dict) --The credentials for access to a private registry.

credential (string) --The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

Note
The credential can use the name of the credentials only if they exist in your current AWS Region.


credentialProvider (string) --The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.



imagePullCredentialsType (string) --The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid values:

CODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild\'s service principal.
SERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.

When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.



serviceRole (string) --The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

timeoutInMinutes (integer) --How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.

queuedTimeoutInMinutes (integer) --The number of minutes a build is allowed to be queued before it times out.

encryptionKey (string) --The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

Note
You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK\'s alias (using the format ``alias/alias-name `` ).

tags (list) --A list of tag key and value pairs associated with this build project.
These tags are available for use by AWS services that support AWS CodeBuild build project tags.

(dict) --A tag, consisting of a key and a value.
This tag is available for use by AWS services that support tags in AWS CodeBuild.

key (string) --The tag\'s key.

value (string) --The tag\'s value.





created (datetime) --When the build project was created, expressed in Unix time format.

lastModified (datetime) --When the build project\'s settings were last modified, expressed in Unix time format.

webhook (dict) --Information about a webhook that connects repository events to a build project in AWS CodeBuild.

url (string) --The URL to the webhook.

payloadUrl (string) --The AWS CodeBuild endpoint where webhook events are sent.

secret (string) --The secret token of the associated repository.

Note
A Bitbucket webhook does not support secret .


branchFilter (string) --A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If branchFilter is empty, then all branches are built.

Note
It is recommended that you use filterGroups instead of branchFilter .


filterGroups (list) --An array of arrays of WebhookFilter objects used to determine which webhooks are triggered. At least one WebhookFilter in the array must specify EVENT as its type .
For a build to be triggered, at least one filter group in the filterGroups array must pass. For a filter group to pass, each of its filters must pass.

(list) --
(dict) --A filter used to determine which webhooks trigger a build.

type (string) --The type of webhook filter. There are five webhook filter types: EVENT , ACTOR_ACCOUNT_ID , HEAD_REF , BASE_REF , and FILE_PATH .

EVENT
A webhook event triggers a build when the provided pattern matches one of five event types: PUSH , PULL_REQUEST_CREATED , PULL_REQUEST_UPDATED , PULL_REQUEST_REOPENED , and PULL_REQUEST_MERGED . The EVENT patterns are specified as a comma-separated string. For example, PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED filters all push, pull request created, and pull request updated events.

Note
The PULL_REQUEST_REOPENED works with GitHub and GitHub Enterprise only.
ACTOR_ACCOUNT_ID

A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression pattern .

HEAD_REF
A webhook event triggers a build when the head reference matches the regular expression pattern . For example, refs/heads/branch-name and refs/tags/tag-name .
Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.

BASE_REF
A webhook event triggers a build when the base reference matches the regular expression pattern . For example, refs/heads/branch-name .

Note
Works with pull request events only.
FILE_PATH

A webhook triggers a build when the path of a changed file matches the regular expression pattern .

Note
Works with GitHub and GitHub Enterprise push events only.


pattern (string) --For a WebHookFilter that uses EVENT type, a comma-separated string that specifies one or more events. For example, the webhook filter PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED allows all push, pull request created, and pull request updated events to trigger a build.
For a WebHookFilter that uses any of the other filter types, a regular expression pattern. For example, a WebHookFilter that uses HEAD_REF for its type and the pattern ^refs/heads/ triggers a build when the head reference is a branch with a reference name refs/heads/branch-name .

excludeMatchedPattern (boolean) --Used to indicate that the pattern determines which webhook events do not trigger a build. If true, then a webhook event that does not match the pattern triggers a build. If false, then a webhook event that matches the pattern triggers a build.







lastModifiedSecret (datetime) --A timestamp that indicates the last time a repository\'s secret token was modified.



vpcConfig (dict) --Information about the VPC configuration that AWS CodeBuild accesses.

vpcId (string) --The ID of the Amazon VPC.

subnets (list) --A list of one or more subnet IDs in your Amazon VPC.

(string) --


securityGroupIds (list) --A list of one or more security groups IDs in your Amazon VPC.

(string) --




badge (dict) --Information about the build badge for the build project.

badgeEnabled (boolean) --Set this to true to generate a publicly accessible URL for your project\'s build badge.

badgeRequestUrl (string) --The publicly-accessible URL through which you can access the build badge for your project.
The publicly accessible URL through which you can access the build badge for your project.



logsConfig (dict) --Information about logs for the build project. A project can create logs in Amazon CloudWatch Logs, an S3 bucket, or both.

cloudWatchLogs (dict) --Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default.

status (string) --The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:

ENABLED : Amazon CloudWatch Logs are enabled for this build project.
DISABLED : Amazon CloudWatch Logs are not enabled for this build project.


groupName (string) --The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .

streamName (string) --The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .



s3Logs (dict) --Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.

status (string) --The current status of the S3 build logs. Valid values are:

ENABLED : S3 build logs are enabled for this build project.
DISABLED : S3 build logs are not enabled for this build project.


location (string) --The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .

encryptionDisabled (boolean) --Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.





fileSystemLocations (list) --An array of ProjectFileSystemLocation objects for a CodeBuild build project. A ProjectFileSystemLocation object specifies the identifier , location , mountOptions , mountPoint , and type of a file system created using Amazon Elastic File System.

(dict) --Information about a file system created by Amazon Elastic File System (EFS). For more information, see What Is Amazon Elastic File System?

type (string) --The type of the file system. The one supported type is EFS .

location (string) --A string that specifies the location of the file system created by Amazon EFS. Its format is efs-dns-name:/directory-path . You can find the DNS name of file system when you view it in the AWS EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is fs-abcd1234.efs.us-west-2.amazonaws.com , and its mount directory is my-efs-mount-directory , then the location is fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory .
The directory path in the format efs-dns-name:/directory-path is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.

mountPoint (string) --The location in the container where you mount the file system.

identifier (string) --The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the identifier in all capital letters to CODEBUILD_ . For example, if you specify my-efs for identifier , a new environment variable is create named CODEBUILD_MY-EFS .
The identifier is used to mount your file system.

mountOptions (string) --The mount options for a file system created by AWS EFS. The default mount options used by CodeBuild are nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 . For more information, see Recommended NFS Mount Options .









projectsNotFound (list) --The names of build projects for which information could not be found.

(string) --







Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'projects': [
            {
                'name': 'string',
                'arn': 'string',
                'description': 'string',
                'source': {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'gitSubmodulesConfig': {
                        'fetchSubmodules': True|False
                    },
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
                'secondarySources': [
                    {
                        'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                        'location': 'string',
                        'gitCloneDepth': 123,
                        'gitSubmodulesConfig': {
                            'fetchSubmodules': True|False
                        },
                        'buildspec': 'string',
                        'auth': {
                            'type': 'OAUTH',
                            'resource': 'string'
                        },
                        'reportBuildStatus': True|False,
                        'insecureSsl': True|False,
                        'sourceIdentifier': 'string'
                    },
                ],
                'sourceVersion': 'string',
                'secondarySourceVersions': [
                    {
                        'sourceIdentifier': 'string',
                        'sourceVersion': 'string'
                    },
                ],
                'artifacts': {
                    'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                    'location': 'string',
                    'path': 'string',
                    'namespaceType': 'NONE'|'BUILD_ID',
                    'name': 'string',
                    'packaging': 'NONE'|'ZIP',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
                'secondaryArtifacts': [
                    {
                        'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                        'location': 'string',
                        'path': 'string',
                        'namespaceType': 'NONE'|'BUILD_ID',
                        'name': 'string',
                        'packaging': 'NONE'|'ZIP',
                        'overrideArtifactName': True|False,
                        'encryptionDisabled': True|False,
                        'artifactIdentifier': 'string'
                    },
                ],
                'cache': {
                    'type': 'NO_CACHE'|'S3'|'LOCAL',
                    'location': 'string',
                    'modes': [
                        'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                    ]
                },
                'environment': {
                    'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
                    'image': 'string',
                    'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                    'environmentVariables': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                        },
                    ],
                    'privilegedMode': True|False,
                    'certificate': 'string',
                    'registryCredential': {
                        'credential': 'string',
                        'credentialProvider': 'SECRETS_MANAGER'
                    },
                    'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
                },
                'serviceRole': 'string',
                'timeoutInMinutes': 123,
                'queuedTimeoutInMinutes': 123,
                'encryptionKey': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'created': datetime(2015, 1, 1),
                'lastModified': datetime(2015, 1, 1),
                'webhook': {
                    'url': 'string',
                    'payloadUrl': 'string',
                    'secret': 'string',
                    'branchFilter': 'string',
                    'filterGroups': [
                        [
                            {
                                'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                                'pattern': 'string',
                                'excludeMatchedPattern': True|False
                            },
                        ],
                    ],
                    'lastModifiedSecret': datetime(2015, 1, 1)
                },
                'vpcConfig': {
                    'vpcId': 'string',
                    'subnets': [
                        'string',
                    ],
                    'securityGroupIds': [
                        'string',
                    ]
                },
                'badge': {
                    'badgeEnabled': True|False,
                    'badgeRequestUrl': 'string'
                },
                'logsConfig': {
                    'cloudWatchLogs': {
                        'status': 'ENABLED'|'DISABLED',
                        'groupName': 'string',
                        'streamName': 'string'
                    },
                    's3Logs': {
                        'status': 'ENABLED'|'DISABLED',
                        'location': 'string',
                        'encryptionDisabled': True|False
                    }
                },
                'fileSystemLocations': [
                    {
                        'type': 'EFS',
                        'location': 'string',
                        'mountPoint': 'string',
                        'identifier': 'string',
                        'mountOptions': 'string'
                    },
                ]
            },
        ],
        'projectsNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    BITBUCKET : The source code is in a Bitbucket repository.
    CODECOMMIT : The source code is in an AWS CodeCommit repository.
    CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
    GITHUB : The source code is in a GitHub repository.
    GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
    NO_SOURCE : The project does not have input source code.
    S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    
    """
    pass

def batch_get_report_groups(reportGroupArns=None):
    """
    Returns an array of report groups.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_report_groups(
        reportGroupArns=[
            'string',
        ]
    )
    
    
    :type reportGroupArns: list
    :param reportGroupArns: [REQUIRED]\nAn array of report group ARNs that identify the report groups to return.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'reportGroups': [
        {
            'arn': 'string',
            'name': 'string',
            'type': 'TEST',
            'exportConfig': {
                'exportConfigType': 'S3'|'NO_EXPORT',
                's3Destination': {
                    'bucket': 'string',
                    'path': 'string',
                    'packaging': 'ZIP'|'NONE',
                    'encryptionKey': 'string',
                    'encryptionDisabled': True|False
                }
            },
            'created': datetime(2015, 1, 1),
            'lastModified': datetime(2015, 1, 1),
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        },
    ],
    'reportGroupsNotFound': [
        'string',
    ]
}


Response Structure

(dict) --
reportGroups (list) --The array of report groups returned by BatchGetReportGroups .

(dict) --A series of reports. Each report contains information about the results from running a series of test cases. You specify the test cases for a report group in the buildspec for a build project using one or more paths to the test case files.

arn (string) --The ARN of a ReportGroup .

name (string) --The name of a ReportGroup .

type (string) --The type of the ReportGroup . The one valid value is TEST .

exportConfig (dict) --Information about the destination where the raw data of this ReportGroup is exported.

exportConfigType (string) --The export configuration type. Valid values are:

S3 : The report results are exported to an S3 bucket.
NO_EXPORT : The report results are not exported.


s3Destination (dict) --A S3ReportExportConfig object that contains information about the S3 bucket where the run of a report is exported.

bucket (string) --The name of the S3 bucket where the raw data of a report are exported.

path (string) --The path to the exported report\'s raw data results.

packaging (string) --The type of build output artifact to create. Valid values include:

NONE : AWS CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified.
ZIP : AWS CodeBuild creates a ZIP file with the raw data in the output bucket.


encryptionKey (string) --The encryption key for the report\'s encrypted raw data.

encryptionDisabled (boolean) --A boolean value that specifies if the results of a report are encrypted.





created (datetime) --The date and time this ReportGroup was created.

lastModified (datetime) --The date and time this ReportGroup was last modified.

tags (list) --A list of tag key and value pairs associated with this report group.
These tags are available for use by AWS services that support AWS CodeBuild report group tags.

(dict) --A tag, consisting of a key and a value.
This tag is available for use by AWS services that support tags in AWS CodeBuild.

key (string) --The tag\'s key.

value (string) --The tag\'s value.









reportGroupsNotFound (list) --An array of ARNs passed to BatchGetReportGroups that are not associated with a ReportGroup .

(string) --







Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'reportGroups': [
            {
                'arn': 'string',
                'name': 'string',
                'type': 'TEST',
                'exportConfig': {
                    'exportConfigType': 'S3'|'NO_EXPORT',
                    's3Destination': {
                        'bucket': 'string',
                        'path': 'string',
                        'packaging': 'ZIP'|'NONE',
                        'encryptionKey': 'string',
                        'encryptionDisabled': True|False
                    }
                },
                'created': datetime(2015, 1, 1),
                'lastModified': datetime(2015, 1, 1),
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            },
        ],
        'reportGroupsNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    S3 : The report results are exported to an S3 bucket.
    NO_EXPORT : The report results are not exported.
    
    """
    pass

def batch_get_reports(reportArns=None):
    """
    Returns an array of reports.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_reports(
        reportArns=[
            'string',
        ]
    )
    
    
    :type reportArns: list
    :param reportArns: [REQUIRED]\nAn array of ARNs that identify the Report objects to return.\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'reports': [
        {
            'arn': 'string',
            'type': 'TEST',
            'name': 'string',
            'reportGroupArn': 'string',
            'executionId': 'string',
            'status': 'GENERATING'|'SUCCEEDED'|'FAILED'|'INCOMPLETE'|'DELETING',
            'created': datetime(2015, 1, 1),
            'expired': datetime(2015, 1, 1),
            'exportConfig': {
                'exportConfigType': 'S3'|'NO_EXPORT',
                's3Destination': {
                    'bucket': 'string',
                    'path': 'string',
                    'packaging': 'ZIP'|'NONE',
                    'encryptionKey': 'string',
                    'encryptionDisabled': True|False
                }
            },
            'truncated': True|False,
            'testSummary': {
                'total': 123,
                'statusCounts': {
                    'string': 123
                },
                'durationInNanoSeconds': 123
            }
        },
    ],
    'reportsNotFound': [
        'string',
    ]
}


Response Structure

(dict) --
reports (list) --The array of Report objects returned by BatchGetReports .

(dict) --Information about the results from running a series of test cases during the run of a build project. The test cases are specified in the buildspec for the build project using one or more paths to the test case files. You can specify any type of tests you want, such as unit tests, integration tests, and functional tests.

arn (string) --The ARN of the report run.

type (string) --The type of the report that was run.

name (string) --The name of the report that was run.

reportGroupArn (string) --The ARN of the report group associated with this report.

executionId (string) --The ARN of the build run that generated this report.

status (string) --The status of this report.

created (datetime) --The date and time this report run occurred.

expired (datetime) --The date and time a report expires. A report expires 30 days after it is created. An expired report is not available to view in CodeBuild.

exportConfig (dict) --Information about where the raw data used to generate this report was exported.

exportConfigType (string) --The export configuration type. Valid values are:

S3 : The report results are exported to an S3 bucket.
NO_EXPORT : The report results are not exported.


s3Destination (dict) --A S3ReportExportConfig object that contains information about the S3 bucket where the run of a report is exported.

bucket (string) --The name of the S3 bucket where the raw data of a report are exported.

path (string) --The path to the exported report\'s raw data results.

packaging (string) --The type of build output artifact to create. Valid values include:

NONE : AWS CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified.
ZIP : AWS CodeBuild creates a ZIP file with the raw data in the output bucket.


encryptionKey (string) --The encryption key for the report\'s encrypted raw data.

encryptionDisabled (boolean) --A boolean value that specifies if the results of a report are encrypted.





truncated (boolean) --A boolean that specifies if this report run is truncated. The list of test cases is truncated after the maximum number of test cases is reached.

testSummary (dict) --A TestReportSummary object that contains information about this test report.

total (integer) --The number of test cases in this TestReportSummary . The total includes truncated test cases.

statusCounts (dict) --A map that contains the number of each type of status returned by the test results in this TestReportSummary .

(string) --
(integer) --




durationInNanoSeconds (integer) --The number of nanoseconds it took to run all of the test cases in this report.







reportsNotFound (list) --An array of ARNs passed to BatchGetReportGroups that are not associated with a Report .

(string) --







Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'reports': [
            {
                'arn': 'string',
                'type': 'TEST',
                'name': 'string',
                'reportGroupArn': 'string',
                'executionId': 'string',
                'status': 'GENERATING'|'SUCCEEDED'|'FAILED'|'INCOMPLETE'|'DELETING',
                'created': datetime(2015, 1, 1),
                'expired': datetime(2015, 1, 1),
                'exportConfig': {
                    'exportConfigType': 'S3'|'NO_EXPORT',
                    's3Destination': {
                        'bucket': 'string',
                        'path': 'string',
                        'packaging': 'ZIP'|'NONE',
                        'encryptionKey': 'string',
                        'encryptionDisabled': True|False
                    }
                },
                'truncated': True|False,
                'testSummary': {
                    'total': 123,
                    'statusCounts': {
                        'string': 123
                    },
                    'durationInNanoSeconds': 123
                }
            },
        ],
        'reportsNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    S3 : The report results are exported to an S3 bucket.
    NO_EXPORT : The report results are not exported.
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_project(name=None, description=None, source=None, secondarySources=None, sourceVersion=None, secondarySourceVersions=None, artifacts=None, secondaryArtifacts=None, cache=None, environment=None, serviceRole=None, timeoutInMinutes=None, queuedTimeoutInMinutes=None, encryptionKey=None, tags=None, vpcConfig=None, badgeEnabled=None, logsConfig=None, fileSystemLocations=None):
    """
    Creates a build project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_project(
        name='string',
        description='string',
        source={
            'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
            'location': 'string',
            'gitCloneDepth': 123,
            'gitSubmodulesConfig': {
                'fetchSubmodules': True|False
            },
            'buildspec': 'string',
            'auth': {
                'type': 'OAUTH',
                'resource': 'string'
            },
            'reportBuildStatus': True|False,
            'insecureSsl': True|False,
            'sourceIdentifier': 'string'
        },
        secondarySources=[
            {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
        ],
        sourceVersion='string',
        secondarySourceVersions=[
            {
                'sourceIdentifier': 'string',
                'sourceVersion': 'string'
            },
        ],
        artifacts={
            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
            'location': 'string',
            'path': 'string',
            'namespaceType': 'NONE'|'BUILD_ID',
            'name': 'string',
            'packaging': 'NONE'|'ZIP',
            'overrideArtifactName': True|False,
            'encryptionDisabled': True|False,
            'artifactIdentifier': 'string'
        },
        secondaryArtifacts=[
            {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
        ],
        cache={
            'type': 'NO_CACHE'|'S3'|'LOCAL',
            'location': 'string',
            'modes': [
                'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
            ]
        },
        environment={
            'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
            'image': 'string',
            'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
            'environmentVariables': [
                {
                    'name': 'string',
                    'value': 'string',
                    'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                },
            ],
            'privilegedMode': True|False,
            'certificate': 'string',
            'registryCredential': {
                'credential': 'string',
                'credentialProvider': 'SECRETS_MANAGER'
            },
            'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
        },
        serviceRole='string',
        timeoutInMinutes=123,
        queuedTimeoutInMinutes=123,
        encryptionKey='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        vpcConfig={
            'vpcId': 'string',
            'subnets': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ]
        },
        badgeEnabled=True|False,
        logsConfig={
            'cloudWatchLogs': {
                'status': 'ENABLED'|'DISABLED',
                'groupName': 'string',
                'streamName': 'string'
            },
            's3Logs': {
                'status': 'ENABLED'|'DISABLED',
                'location': 'string',
                'encryptionDisabled': True|False
            }
        },
        fileSystemLocations=[
            {
                'type': 'EFS',
                'location': 'string',
                'mountPoint': 'string',
                'identifier': 'string',
                'mountOptions': 'string'
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the build project.\n

    :type description: string
    :param description: A description that makes the build project easy to identify.

    :type source: dict
    :param source: [REQUIRED]\nInformation about the build input source code for the build project.\n\ntype (string) -- [REQUIRED]The type of repository that contains the source code to be built. Valid values include:\n\nBITBUCKET : The source code is in a Bitbucket repository.\nCODECOMMIT : The source code is in an AWS CodeCommit repository.\nCODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.\nGITHUB : The source code is in a GitHub repository.\nGITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.\nNO_SOURCE : The project does not have input source code.\nS3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.\n\n\nlocation (string) --Information about the location of the source code to be built. Valid values include:\n\nFor source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.\nFor source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).\nFor source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.\nThe path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).\nThe path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).\n\n\nFor source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .\nFor source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .\n\n\ngitCloneDepth (integer) --Information about the Git clone depth for the build project.\n\ngitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.\n\nfetchSubmodules (boolean) -- [REQUIRED]Set to true to fetch Git submodules for your AWS CodeBuild build project.\n\n\n\nbuildspec (string) --The buildspec file declaration to use for the builds in this build project.\nIf this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .\n\nauth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.\nThis information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.\n\ntype (string) -- [REQUIRED]\nNote\nThis data type is deprecated and is no longer accurate or used.\n\nThe authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.\n\nresource (string) --The resource value that applies to the specified authorization type.\n\n\n\nreportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.\n\nNote\nThe status of a build triggered by a webhook is always reported to your source provider.\n\n\ninsecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.\n\nsourceIdentifier (string) --An identifier for this project source.\n\n\n

    :type secondarySources: list
    :param secondarySources: An array of ProjectSource objects.\n\n(dict) --Information about the build input source code for the build project.\n\ntype (string) -- [REQUIRED]The type of repository that contains the source code to be built. Valid values include:\n\nBITBUCKET : The source code is in a Bitbucket repository.\nCODECOMMIT : The source code is in an AWS CodeCommit repository.\nCODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.\nGITHUB : The source code is in a GitHub repository.\nGITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.\nNO_SOURCE : The project does not have input source code.\nS3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.\n\n\nlocation (string) --Information about the location of the source code to be built. Valid values include:\n\nFor source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.\nFor source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).\nFor source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.\nThe path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).\nThe path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).\n\n\nFor source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .\nFor source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .\n\n\ngitCloneDepth (integer) --Information about the Git clone depth for the build project.\n\ngitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.\n\nfetchSubmodules (boolean) -- [REQUIRED]Set to true to fetch Git submodules for your AWS CodeBuild build project.\n\n\n\nbuildspec (string) --The buildspec file declaration to use for the builds in this build project.\nIf this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .\n\nauth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.\nThis information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.\n\ntype (string) -- [REQUIRED]\nNote\nThis data type is deprecated and is no longer accurate or used.\n\nThe authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.\n\nresource (string) --The resource value that applies to the specified authorization type.\n\n\n\nreportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.\n\nNote\nThe status of a build triggered by a webhook is always reported to your source provider.\n\n\ninsecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.\n\nsourceIdentifier (string) --An identifier for this project source.\n\n\n\n\n

    :type sourceVersion: string
    :param sourceVersion: A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of:\n\nFor AWS CodeCommit: the commit ID, branch, or Git tag to use.\nFor GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.\n\nIf sourceVersion is specified at the build level, then that version takes precedence over this sourceVersion (at the project level).\nFor more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .\n

    :type secondarySourceVersions: list
    :param secondarySourceVersions: An array of ProjectSourceVersion objects. If secondarySourceVersions is specified at the build level, then they take precedence over these secondarySourceVersions (at the project level).\n\n(dict) --A source identifier and its corresponding version.\n\nsourceIdentifier (string) -- [REQUIRED]An identifier for a source in the build project.\n\nsourceVersion (string) -- [REQUIRED]The source version for the corresponding source identifier. If specified, must be one of:\n\nFor AWS CodeCommit: the commit ID, branch, or Git tag to use.\nFor GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.\n\nFor more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .\n\n\n\n\n

    :type artifacts: dict
    :param artifacts: [REQUIRED]\nInformation about the build output artifacts for the build project.\n\ntype (string) -- [REQUIRED]The type of build output artifact. Valid values include:\n\nCODEPIPELINE : The build project has build output generated through AWS CodePipeline.\n\n\nNote\nThe CODEPIPELINE type is not supported for secondaryArtifacts .\n\n\nNO_ARTIFACTS : The build project does not produce any build output.\nS3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).\n\n\nlocation (string) --Information about the build output artifact location:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output bucket.\n\n\npath (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.\n\nFor example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .\n\nnamespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nBUILD_ID : Include the build ID in the location of the build output artifact.\nNONE : Do not include the build ID. This is the default if namespaceType is not specified.\n\n\n\nFor example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\n\nname (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.\n\nFor example:\n\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\nIf path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .\n\n\npackaging (string) --The type of build output artifact to create:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nNONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.\nZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.\n\n\n\n\noverrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.\n\nencryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.\n\nartifactIdentifier (string) --An identifier for this artifact definition.\n\n\n

    :type secondaryArtifacts: list
    :param secondaryArtifacts: An array of ProjectArtifacts objects.\n\n(dict) --Information about the build output artifacts for the build project.\n\ntype (string) -- [REQUIRED]The type of build output artifact. Valid values include:\n\nCODEPIPELINE : The build project has build output generated through AWS CodePipeline.\n\n\nNote\nThe CODEPIPELINE type is not supported for secondaryArtifacts .\n\n\nNO_ARTIFACTS : The build project does not produce any build output.\nS3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).\n\n\nlocation (string) --Information about the build output artifact location:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output bucket.\n\n\npath (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.\n\nFor example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .\n\nnamespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nBUILD_ID : Include the build ID in the location of the build output artifact.\nNONE : Do not include the build ID. This is the default if namespaceType is not specified.\n\n\n\nFor example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\n\nname (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.\n\nFor example:\n\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\nIf path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .\n\n\npackaging (string) --The type of build output artifact to create:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nNONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.\nZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.\n\n\n\n\noverrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.\n\nencryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.\n\nartifactIdentifier (string) --An identifier for this artifact definition.\n\n\n\n\n

    :type cache: dict
    :param cache: Stores recently used information so that it can be quickly accessed at a later time.\n\ntype (string) -- [REQUIRED]The type of cache used by the build project. Valid values include:\n\nNO_CACHE : The build project does not use any cache.\nS3 : The build project reads and writes from and to S3.\nLOCAL : The build project stores a cache locally on a build host that is only available to that build host.\n\n\nlocation (string) --Information about the cache location:\n\nNO_CACHE or LOCAL : This value is ignored.\nS3 : This is the S3 bucket name/prefix.\n\n\nmodes (list) --If you use a LOCAL cache, the local cache mode. You can use one or more local cache modes at the same time.\n\nLOCAL_SOURCE_CACHE mode caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.\nLOCAL_DOCKER_LAYER_CACHE mode caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.\n\n\nNote\n\nYou can use a Docker layer cache in the Linux environment only.\nThe privileged flag must be set so that your project has the required Docker permissions.\nYou should consider the security implications before you use a Docker layer cache.\n\n\n\nLOCAL_CUSTOM_CACHE mode caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:\nOnly directories can be specified for caching. You cannot specify individual files.\nSymlinks are used to reference cached directories.\nCached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.\n\n\n\n\n(string) --\n\n\n\n

    :type environment: dict
    :param environment: [REQUIRED]\nInformation about the build environment for the build project.\n\ntype (string) -- [REQUIRED]The type of build environment to use for related builds.\n\nThe environment type ARM_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).\nThe environment type LINUX_CONTAINER with compute type build.general1.2xlarge is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).\nThe environment type LINUX_GPU_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).\n\n\nimage (string) -- [REQUIRED]The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:\n\nFor an image tag: registry/repository:tag . For example, to specify an image with the tag 'latest,' use registry/repository:latest .\nFor an image digest: registry/repository@digest . For example, to specify an image with the digest 'sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf,' use registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf .\n\n\ncomputeType (string) -- [REQUIRED]Information about the compute resources the build project uses. Available values include:\n\nBUILD_GENERAL1_SMALL : Use up to 3 GB memory and 2 vCPUs for builds.\nBUILD_GENERAL1_MEDIUM : Use up to 7 GB memory and 4 vCPUs for builds.\nBUILD_GENERAL1_LARGE : Use up to 16 GB memory and 8 vCPUs for builds, depending on your environment type.\nBUILD_GENERAL1_2XLARGE : Use up to 145 GB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.\n\nIf you use BUILD_GENERAL1_LARGE :\n\nFor environment type LINUX_CONTAINER , you can use up to 15 GB memory and 8 vCPUs for builds.\nFor environment type LINUX_GPU_CONTAINER , you can use up to 255 GB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.\nFor environment type ARM_CONTAINER , you can use up to 16 GB memory and 8 vCPUs on ARM-based processors for builds.\n\nFor more information, see Build Environment Compute Types in the AWS CodeBuild User Guide.\n\nenvironmentVariables (list) --A set of environment variables to make available to builds for this build project.\n\n(dict) --Information about an environment variable for a build project or a build.\n\nname (string) -- [REQUIRED]The name or key of the environment variable.\n\nvalue (string) -- [REQUIRED]The value of the environment variable.\n\nWarning\nWe strongly discourage the use of PLAINTEXT environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. PLAINTEXT environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI). For sensitive values, we recommend you use an environment variable of type PARAMETER_STORE or SECRETS_MANAGER .\n\n\ntype (string) --The type of environment variable. Valid values include:\n\nPARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. To learn how to specify a parameter store environment variable, see parameter store reference-key in the buildspec file .\nPLAINTEXT : An environment variable in plain text format. This is the default value.\nSECRETS_MANAGER : An environment variable stored in AWS Secrets Manager. To learn how to specify a secrets manager environment variable, see secrets manager reference-key in the buildspec file .\n\n\n\n\n\n\nprivilegedMode (boolean) --Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is false .\nYou can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:\nIf the operating system\'s base image is Ubuntu Linux:\n\n- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&- timeout 15 sh -c 'until docker info; do echo .; sleep 1; done'\n\nIf the operating system\'s base image is Alpine Linux and the previous command does not work, add the -t argument to timeout :\n\n- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&- timeout -t 15 sh -c 'until docker info; do echo .; sleep 1; done'\n\n\ncertificate (string) --The certificate to use with this build project.\n\nregistryCredential (dict) --The credentials for access to a private registry.\n\ncredential (string) -- [REQUIRED]The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.\n\nNote\nThe credential can use the name of the credentials only if they exist in your current AWS Region.\n\n\ncredentialProvider (string) -- [REQUIRED]The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.\n\n\n\nimagePullCredentialsType (string) --The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid values:\n\nCODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild\'s service principal.\nSERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.\n\nWhen you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.\n\n\n

    :type serviceRole: string
    :param serviceRole: [REQUIRED]\nThe ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.\n

    :type timeoutInMinutes: integer
    :param timeoutInMinutes: How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before it times out any build that has not been marked as completed. The default is 60 minutes.

    :type queuedTimeoutInMinutes: integer
    :param queuedTimeoutInMinutes: The number of minutes a build is allowed to be queued before it times out.

    :type encryptionKey: string
    :param encryptionKey: The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.\n\nNote\nYou can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.\n\nYou can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK\'s alias (using the format ``alias/alias-name `` ).\n

    :type tags: list
    :param tags: A list of tag key and value pairs associated with this build project.\nThese tags are available for use by AWS services that support AWS CodeBuild build project tags.\n\n(dict) --A tag, consisting of a key and a value.\nThis tag is available for use by AWS services that support tags in AWS CodeBuild.\n\nkey (string) --The tag\'s key.\n\nvalue (string) --The tag\'s value.\n\n\n\n\n

    :type vpcConfig: dict
    :param vpcConfig: VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.\n\nvpcId (string) --The ID of the Amazon VPC.\n\nsubnets (list) --A list of one or more subnet IDs in your Amazon VPC.\n\n(string) --\n\n\nsecurityGroupIds (list) --A list of one or more security groups IDs in your Amazon VPC.\n\n(string) --\n\n\n\n

    :type badgeEnabled: boolean
    :param badgeEnabled: Set this to true to generate a publicly accessible URL for your project\'s build badge.

    :type logsConfig: dict
    :param logsConfig: Information about logs for the build project. These can be logs in Amazon CloudWatch Logs, logs uploaded to a specified S3 bucket, or both.\n\ncloudWatchLogs (dict) --Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default.\n\nstatus (string) -- [REQUIRED]The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:\n\nENABLED : Amazon CloudWatch Logs are enabled for this build project.\nDISABLED : Amazon CloudWatch Logs are not enabled for this build project.\n\n\ngroupName (string) --The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .\n\nstreamName (string) --The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .\n\n\n\ns3Logs (dict) --Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.\n\nstatus (string) -- [REQUIRED]The current status of the S3 build logs. Valid values are:\n\nENABLED : S3 build logs are enabled for this build project.\nDISABLED : S3 build logs are not enabled for this build project.\n\n\nlocation (string) --The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .\n\nencryptionDisabled (boolean) --Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.\n\n\n\n\n

    :type fileSystemLocations: list
    :param fileSystemLocations: An array of ProjectFileSystemLocation objects for a CodeBuild build project. A ProjectFileSystemLocation object specifies the identifier , location , mountOptions , mountPoint , and type of a file system created using Amazon Elastic File System.\n\n(dict) --Information about a file system created by Amazon Elastic File System (EFS). For more information, see What Is Amazon Elastic File System?\n\ntype (string) --The type of the file system. The one supported type is EFS .\n\nlocation (string) --A string that specifies the location of the file system created by Amazon EFS. Its format is efs-dns-name:/directory-path . You can find the DNS name of file system when you view it in the AWS EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is fs-abcd1234.efs.us-west-2.amazonaws.com , and its mount directory is my-efs-mount-directory , then the location is fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory .\nThe directory path in the format efs-dns-name:/directory-path is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.\n\nmountPoint (string) --The location in the container where you mount the file system.\n\nidentifier (string) --The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the identifier in all capital letters to CODEBUILD_ . For example, if you specify my-efs for identifier , a new environment variable is create named CODEBUILD_MY-EFS .\nThe identifier is used to mount your file system.\n\nmountOptions (string) --The mount options for a file system created by AWS EFS. The default mount options used by CodeBuild are nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 . For more information, see Recommended NFS Mount Options .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'project': {
        'name': 'string',
        'arn': 'string',
        'description': 'string',
        'source': {
            'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
            'location': 'string',
            'gitCloneDepth': 123,
            'gitSubmodulesConfig': {
                'fetchSubmodules': True|False
            },
            'buildspec': 'string',
            'auth': {
                'type': 'OAUTH',
                'resource': 'string'
            },
            'reportBuildStatus': True|False,
            'insecureSsl': True|False,
            'sourceIdentifier': 'string'
        },
        'secondarySources': [
            {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
        ],
        'sourceVersion': 'string',
        'secondarySourceVersions': [
            {
                'sourceIdentifier': 'string',
                'sourceVersion': 'string'
            },
        ],
        'artifacts': {
            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
            'location': 'string',
            'path': 'string',
            'namespaceType': 'NONE'|'BUILD_ID',
            'name': 'string',
            'packaging': 'NONE'|'ZIP',
            'overrideArtifactName': True|False,
            'encryptionDisabled': True|False,
            'artifactIdentifier': 'string'
        },
        'secondaryArtifacts': [
            {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
        ],
        'cache': {
            'type': 'NO_CACHE'|'S3'|'LOCAL',
            'location': 'string',
            'modes': [
                'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
            ]
        },
        'environment': {
            'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
            'image': 'string',
            'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
            'environmentVariables': [
                {
                    'name': 'string',
                    'value': 'string',
                    'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                },
            ],
            'privilegedMode': True|False,
            'certificate': 'string',
            'registryCredential': {
                'credential': 'string',
                'credentialProvider': 'SECRETS_MANAGER'
            },
            'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
        },
        'serviceRole': 'string',
        'timeoutInMinutes': 123,
        'queuedTimeoutInMinutes': 123,
        'encryptionKey': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'created': datetime(2015, 1, 1),
        'lastModified': datetime(2015, 1, 1),
        'webhook': {
            'url': 'string',
            'payloadUrl': 'string',
            'secret': 'string',
            'branchFilter': 'string',
            'filterGroups': [
                [
                    {
                        'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                        'pattern': 'string',
                        'excludeMatchedPattern': True|False
                    },
                ],
            ],
            'lastModifiedSecret': datetime(2015, 1, 1)
        },
        'vpcConfig': {
            'vpcId': 'string',
            'subnets': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ]
        },
        'badge': {
            'badgeEnabled': True|False,
            'badgeRequestUrl': 'string'
        },
        'logsConfig': {
            'cloudWatchLogs': {
                'status': 'ENABLED'|'DISABLED',
                'groupName': 'string',
                'streamName': 'string'
            },
            's3Logs': {
                'status': 'ENABLED'|'DISABLED',
                'location': 'string',
                'encryptionDisabled': True|False
            }
        },
        'fileSystemLocations': [
            {
                'type': 'EFS',
                'location': 'string',
                'mountPoint': 'string',
                'identifier': 'string',
                'mountOptions': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

project (dict) --
Information about the build project that was created.

name (string) --
The name of the build project.

arn (string) --
The Amazon Resource Name (ARN) of the build project.

description (string) --
A description that makes the build project easy to identify.

source (dict) --
Information about the build input source code for this build project.

type (string) --
The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --
Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --
Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --
Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --
Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --
The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --
Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --

Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --
The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --
Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --
Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --
An identifier for this project source.



secondarySources (list) --
An array of ProjectSource objects.

(dict) --
Information about the build input source code for the build project.

type (string) --
The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --
Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --
Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --
Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --
Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --
The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --
Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --

Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --
The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --
Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --
Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --
An identifier for this project source.





sourceVersion (string) --
A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.

If sourceVersion is specified at the build level, then that version takes precedence over this sourceVersion (at the project level).
For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .

secondarySourceVersions (list) --
An array of ProjectSourceVersion objects. If secondarySourceVersions is specified at the build level, then they take over these secondarySourceVersions (at the project level).

(dict) --
A source identifier and its corresponding version.

sourceIdentifier (string) --
An identifier for a source in the build project.

sourceVersion (string) --
The source version for the corresponding source identifier. If specified, must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.

For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .





artifacts (dict) --
Information about the build output artifacts for the build project.

type (string) --
The type of build output artifact. Valid values include:

CODEPIPELINE : The build project has build output generated through AWS CodePipeline.


Note
The CODEPIPELINE type is not supported for secondaryArtifacts .


NO_ARTIFACTS : The build project does not produce any build output.
S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).


location (string) --
Information about the build output artifact location:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output bucket.


path (string) --
Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.

For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .

namespaceType (string) --
Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
BUILD_ID : Include the build ID in the location of the build output artifact.
NONE : Do not include the build ID. This is the default if namespaceType is not specified.



For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .

name (string) --
Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

For example:

If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
If path is empty, namespaceType is set to NONE , and name is set to "/ ", the output artifact is stored in the root of the output bucket.
If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to "/ ", the output artifact is stored in ``MyArtifacts/build-ID `` .


packaging (string) --
The type of build output artifact to create:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.




overrideArtifactName (boolean) --
If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --
Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.

artifactIdentifier (string) --
An identifier for this artifact definition.



secondaryArtifacts (list) --
An array of ProjectArtifacts objects.

(dict) --
Information about the build output artifacts for the build project.

type (string) --
The type of build output artifact. Valid values include:

CODEPIPELINE : The build project has build output generated through AWS CodePipeline.


Note
The CODEPIPELINE type is not supported for secondaryArtifacts .


NO_ARTIFACTS : The build project does not produce any build output.
S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).


location (string) --
Information about the build output artifact location:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output bucket.


path (string) --
Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.

For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .

namespaceType (string) --
Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
BUILD_ID : Include the build ID in the location of the build output artifact.
NONE : Do not include the build ID. This is the default if namespaceType is not specified.



For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .

name (string) --
Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

For example:

If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
If path is empty, namespaceType is set to NONE , and name is set to "/ ", the output artifact is stored in the root of the output bucket.
If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to "/ ", the output artifact is stored in ``MyArtifacts/build-ID `` .


packaging (string) --
The type of build output artifact to create:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.




overrideArtifactName (boolean) --
If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --
Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.

artifactIdentifier (string) --
An identifier for this artifact definition.





cache (dict) --
Information about the cache for the build project.

type (string) --
The type of cache used by the build project. Valid values include:

NO_CACHE : The build project does not use any cache.
S3 : The build project reads and writes from and to S3.
LOCAL : The build project stores a cache locally on a build host that is only available to that build host.


location (string) --
Information about the cache location:

NO_CACHE or LOCAL : This value is ignored.
S3 : This is the S3 bucket name/prefix.


modes (list) --
If you use a LOCAL cache, the local cache mode. You can use one or more local cache modes at the same time.

LOCAL_SOURCE_CACHE mode caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.
LOCAL_DOCKER_LAYER_CACHE mode caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.


Note

You can use a Docker layer cache in the Linux environment only.
The privileged flag must be set so that your project has the required Docker permissions.
You should consider the security implications before you use a Docker layer cache.



LOCAL_CUSTOM_CACHE mode caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:
Only directories can be specified for caching. You cannot specify individual files.
Symlinks are used to reference cached directories.
Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.




(string) --




environment (dict) --
Information about the build environment for this build project.

type (string) --
The type of build environment to use for related builds.

The environment type ARM_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).
The environment type LINUX_CONTAINER with compute type build.general1.2xlarge is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).
The environment type LINUX_GPU_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).


image (string) --
The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:

For an image tag: registry/repository:tag . For example, to specify an image with the tag "latest," use registry/repository:latest .
For an image digest: registry/repository@digest . For example, to specify an image with the digest "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf .


computeType (string) --
Information about the compute resources the build project uses. Available values include:

BUILD_GENERAL1_SMALL : Use up to 3 GB memory and 2 vCPUs for builds.
BUILD_GENERAL1_MEDIUM : Use up to 7 GB memory and 4 vCPUs for builds.
BUILD_GENERAL1_LARGE : Use up to 16 GB memory and 8 vCPUs for builds, depending on your environment type.
BUILD_GENERAL1_2XLARGE : Use up to 145 GB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.

If you use BUILD_GENERAL1_LARGE :

For environment type LINUX_CONTAINER , you can use up to 15 GB memory and 8 vCPUs for builds.
For environment type LINUX_GPU_CONTAINER , you can use up to 255 GB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.
For environment type ARM_CONTAINER , you can use up to 16 GB memory and 8 vCPUs on ARM-based processors for builds.

For more information, see Build Environment Compute Types in the AWS CodeBuild User Guide.

environmentVariables (list) --
A set of environment variables to make available to builds for this build project.

(dict) --
Information about an environment variable for a build project or a build.

name (string) --
The name or key of the environment variable.

value (string) --
The value of the environment variable.

Warning
We strongly discourage the use of PLAINTEXT environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. PLAINTEXT environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI). For sensitive values, we recommend you use an environment variable of type PARAMETER_STORE or SECRETS_MANAGER .


type (string) --
The type of environment variable. Valid values include:

PARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. To learn how to specify a parameter store environment variable, see parameter store reference-key in the buildspec file .
PLAINTEXT : An environment variable in plain text format. This is the default value.
SECRETS_MANAGER : An environment variable stored in AWS Secrets Manager. To learn how to specify a secrets manager environment variable, see secrets manager reference-key in the buildspec file .






privilegedMode (boolean) --
Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is false .
You can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:
If the operating system\'s base image is Ubuntu Linux:

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&
- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"

If the operating system\'s base image is Alpine Linux and the previous command does not work, add the -t argument to timeout :

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&
- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"


certificate (string) --
The certificate to use with this build project.

registryCredential (dict) --
The credentials for access to a private registry.

credential (string) --
The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

Note
The credential can use the name of the credentials only if they exist in your current AWS Region.


credentialProvider (string) --
The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.



imagePullCredentialsType (string) --
The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid values:

CODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild\'s service principal.
SERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.

When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.



serviceRole (string) --
The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

timeoutInMinutes (integer) --
How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.

queuedTimeoutInMinutes (integer) --
The number of minutes a build is allowed to be queued before it times out.

encryptionKey (string) --
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

Note
You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK\'s alias (using the format ``alias/alias-name `` ).

tags (list) --
A list of tag key and value pairs associated with this build project.
These tags are available for use by AWS services that support AWS CodeBuild build project tags.

(dict) --
A tag, consisting of a key and a value.
This tag is available for use by AWS services that support tags in AWS CodeBuild.

key (string) --
The tag\'s key.

value (string) --
The tag\'s value.





created (datetime) --
When the build project was created, expressed in Unix time format.

lastModified (datetime) --
When the build project\'s settings were last modified, expressed in Unix time format.

webhook (dict) --
Information about a webhook that connects repository events to a build project in AWS CodeBuild.

url (string) --
The URL to the webhook.

payloadUrl (string) --
The AWS CodeBuild endpoint where webhook events are sent.

secret (string) --
The secret token of the associated repository.

Note
A Bitbucket webhook does not support secret .


branchFilter (string) --
A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If branchFilter is empty, then all branches are built.

Note
It is recommended that you use filterGroups instead of branchFilter .


filterGroups (list) --
An array of arrays of WebhookFilter objects used to determine which webhooks are triggered. At least one WebhookFilter in the array must specify EVENT as its type .
For a build to be triggered, at least one filter group in the filterGroups array must pass. For a filter group to pass, each of its filters must pass.

(list) --

(dict) --
A filter used to determine which webhooks trigger a build.

type (string) --
The type of webhook filter. There are five webhook filter types: EVENT , ACTOR_ACCOUNT_ID , HEAD_REF , BASE_REF , and FILE_PATH .

EVENT

A webhook event triggers a build when the provided pattern matches one of five event types: PUSH , PULL_REQUEST_CREATED , PULL_REQUEST_UPDATED , PULL_REQUEST_REOPENED , and PULL_REQUEST_MERGED . The EVENT patterns are specified as a comma-separated string. For example, PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED filters all push, pull request created, and pull request updated events.

Note
The PULL_REQUEST_REOPENED works with GitHub and GitHub Enterprise only.
ACTOR_ACCOUNT_ID

A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression pattern .

HEAD_REF

A webhook event triggers a build when the head reference matches the regular expression pattern . For example, refs/heads/branch-name and refs/tags/tag-name .
Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.

BASE_REF

A webhook event triggers a build when the base reference matches the regular expression pattern . For example, refs/heads/branch-name .

Note
Works with pull request events only.
FILE_PATH

A webhook triggers a build when the path of a changed file matches the regular expression pattern .

Note
Works with GitHub and GitHub Enterprise push events only.


pattern (string) --
For a WebHookFilter that uses EVENT type, a comma-separated string that specifies one or more events. For example, the webhook filter PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED allows all push, pull request created, and pull request updated events to trigger a build.
For a WebHookFilter that uses any of the other filter types, a regular expression pattern. For example, a WebHookFilter that uses HEAD_REF for its type and the pattern ^refs/heads/ triggers a build when the head reference is a branch with a reference name refs/heads/branch-name .

excludeMatchedPattern (boolean) --
Used to indicate that the pattern determines which webhook events do not trigger a build. If true, then a webhook event that does not match the pattern triggers a build. If false, then a webhook event that matches the pattern triggers a build.







lastModifiedSecret (datetime) --
A timestamp that indicates the last time a repository\'s secret token was modified.



vpcConfig (dict) --
Information about the VPC configuration that AWS CodeBuild accesses.

vpcId (string) --
The ID of the Amazon VPC.

subnets (list) --
A list of one or more subnet IDs in your Amazon VPC.

(string) --


securityGroupIds (list) --
A list of one or more security groups IDs in your Amazon VPC.

(string) --




badge (dict) --
Information about the build badge for the build project.

badgeEnabled (boolean) --
Set this to true to generate a publicly accessible URL for your project\'s build badge.

badgeRequestUrl (string) --
The publicly-accessible URL through which you can access the build badge for your project.
The publicly accessible URL through which you can access the build badge for your project.



logsConfig (dict) --
Information about logs for the build project. A project can create logs in Amazon CloudWatch Logs, an S3 bucket, or both.

cloudWatchLogs (dict) --
Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default.

status (string) --
The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:

ENABLED : Amazon CloudWatch Logs are enabled for this build project.
DISABLED : Amazon CloudWatch Logs are not enabled for this build project.


groupName (string) --
The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .

streamName (string) --
The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .



s3Logs (dict) --
Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.

status (string) --
The current status of the S3 build logs. Valid values are:

ENABLED : S3 build logs are enabled for this build project.
DISABLED : S3 build logs are not enabled for this build project.


location (string) --
The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .

encryptionDisabled (boolean) --
Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.





fileSystemLocations (list) --
An array of ProjectFileSystemLocation objects for a CodeBuild build project. A ProjectFileSystemLocation object specifies the identifier , location , mountOptions , mountPoint , and type of a file system created using Amazon Elastic File System.

(dict) --
Information about a file system created by Amazon Elastic File System (EFS). For more information, see What Is Amazon Elastic File System?

type (string) --
The type of the file system. The one supported type is EFS .

location (string) --
A string that specifies the location of the file system created by Amazon EFS. Its format is efs-dns-name:/directory-path . You can find the DNS name of file system when you view it in the AWS EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is fs-abcd1234.efs.us-west-2.amazonaws.com , and its mount directory is my-efs-mount-directory , then the location is fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory .
The directory path in the format efs-dns-name:/directory-path is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.

mountPoint (string) --
The location in the container where you mount the file system.

identifier (string) --
The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the identifier in all capital letters to CODEBUILD_ . For example, if you specify my-efs for identifier , a new environment variable is create named CODEBUILD_MY-EFS .
The identifier is used to mount your file system.

mountOptions (string) --
The mount options for a file system created by AWS EFS. The default mount options used by CodeBuild are nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 . For more information, see Recommended NFS Mount Options .













Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceAlreadyExistsException
CodeBuild.Client.exceptions.AccountLimitExceededException


    :return: {
        'project': {
            'name': 'string',
            'arn': 'string',
            'description': 'string',
            'source': {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
            'secondarySources': [
                {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'gitSubmodulesConfig': {
                        'fetchSubmodules': True|False
                    },
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
            ],
            'sourceVersion': 'string',
            'secondarySourceVersions': [
                {
                    'sourceIdentifier': 'string',
                    'sourceVersion': 'string'
                },
            ],
            'artifacts': {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
            'secondaryArtifacts': [
                {
                    'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                    'location': 'string',
                    'path': 'string',
                    'namespaceType': 'NONE'|'BUILD_ID',
                    'name': 'string',
                    'packaging': 'NONE'|'ZIP',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
            ],
            'cache': {
                'type': 'NO_CACHE'|'S3'|'LOCAL',
                'location': 'string',
                'modes': [
                    'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                ]
            },
            'environment': {
                'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
                'image': 'string',
                'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                'environmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                    },
                ],
                'privilegedMode': True|False,
                'certificate': 'string',
                'registryCredential': {
                    'credential': 'string',
                    'credentialProvider': 'SECRETS_MANAGER'
                },
                'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
            },
            'serviceRole': 'string',
            'timeoutInMinutes': 123,
            'queuedTimeoutInMinutes': 123,
            'encryptionKey': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'created': datetime(2015, 1, 1),
            'lastModified': datetime(2015, 1, 1),
            'webhook': {
                'url': 'string',
                'payloadUrl': 'string',
                'secret': 'string',
                'branchFilter': 'string',
                'filterGroups': [
                    [
                        {
                            'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                            'pattern': 'string',
                            'excludeMatchedPattern': True|False
                        },
                    ],
                ],
                'lastModifiedSecret': datetime(2015, 1, 1)
            },
            'vpcConfig': {
                'vpcId': 'string',
                'subnets': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ]
            },
            'badge': {
                'badgeEnabled': True|False,
                'badgeRequestUrl': 'string'
            },
            'logsConfig': {
                'cloudWatchLogs': {
                    'status': 'ENABLED'|'DISABLED',
                    'groupName': 'string',
                    'streamName': 'string'
                },
                's3Logs': {
                    'status': 'ENABLED'|'DISABLED',
                    'location': 'string',
                    'encryptionDisabled': True|False
                }
            },
            'fileSystemLocations': [
                {
                    'type': 'EFS',
                    'location': 'string',
                    'mountPoint': 'string',
                    'identifier': 'string',
                    'mountOptions': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    BITBUCKET : The source code is in a Bitbucket repository.
    CODECOMMIT : The source code is in an AWS CodeCommit repository.
    CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
    GITHUB : The source code is in a GitHub repository.
    GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
    NO_SOURCE : The project does not have input source code.
    S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    
    """
    pass

def create_report_group(name=None, type=None, exportConfig=None, tags=None):
    """
    Creates a report group. A report group contains a collection of reports.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_report_group(
        name='string',
        type='TEST',
        exportConfig={
            'exportConfigType': 'S3'|'NO_EXPORT',
            's3Destination': {
                'bucket': 'string',
                'path': 'string',
                'packaging': 'ZIP'|'NONE',
                'encryptionKey': 'string',
                'encryptionDisabled': True|False
            }
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the report group.\n

    :type type: string
    :param type: [REQUIRED]\nThe type of report group.\n

    :type exportConfig: dict
    :param exportConfig: [REQUIRED]\nA ReportExportConfig object that contains information about where the report group test results are exported.\n\nexportConfigType (string) --The export configuration type. Valid values are:\n\nS3 : The report results are exported to an S3 bucket.\nNO_EXPORT : The report results are not exported.\n\n\ns3Destination (dict) --A S3ReportExportConfig object that contains information about the S3 bucket where the run of a report is exported.\n\nbucket (string) --The name of the S3 bucket where the raw data of a report are exported.\n\npath (string) --The path to the exported report\'s raw data results.\n\npackaging (string) --The type of build output artifact to create. Valid values include:\n\nNONE : AWS CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified.\nZIP : AWS CodeBuild creates a ZIP file with the raw data in the output bucket.\n\n\nencryptionKey (string) --The encryption key for the report\'s encrypted raw data.\n\nencryptionDisabled (boolean) --A boolean value that specifies if the results of a report are encrypted.\n\n\n\n\n

    :type tags: list
    :param tags: A list of tag key and value pairs associated with this report group.\nThese tags are available for use by AWS services that support AWS CodeBuild report group tags.\n\n(dict) --A tag, consisting of a key and a value.\nThis tag is available for use by AWS services that support tags in AWS CodeBuild.\n\nkey (string) --The tag\'s key.\n\nvalue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'reportGroup': {
        'arn': 'string',
        'name': 'string',
        'type': 'TEST',
        'exportConfig': {
            'exportConfigType': 'S3'|'NO_EXPORT',
            's3Destination': {
                'bucket': 'string',
                'path': 'string',
                'packaging': 'ZIP'|'NONE',
                'encryptionKey': 'string',
                'encryptionDisabled': True|False
            }
        },
        'created': datetime(2015, 1, 1),
        'lastModified': datetime(2015, 1, 1),
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

reportGroup (dict) --
Information about the report group that was created.

arn (string) --
The ARN of a ReportGroup .

name (string) --
The name of a ReportGroup .

type (string) --
The type of the ReportGroup . The one valid value is TEST .

exportConfig (dict) --
Information about the destination where the raw data of this ReportGroup is exported.

exportConfigType (string) --
The export configuration type. Valid values are:

S3 : The report results are exported to an S3 bucket.
NO_EXPORT : The report results are not exported.


s3Destination (dict) --
A S3ReportExportConfig object that contains information about the S3 bucket where the run of a report is exported.

bucket (string) --
The name of the S3 bucket where the raw data of a report are exported.

path (string) --
The path to the exported report\'s raw data results.

packaging (string) --
The type of build output artifact to create. Valid values include:

NONE : AWS CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified.
ZIP : AWS CodeBuild creates a ZIP file with the raw data in the output bucket.


encryptionKey (string) --
The encryption key for the report\'s encrypted raw data.

encryptionDisabled (boolean) --
A boolean value that specifies if the results of a report are encrypted.





created (datetime) --
The date and time this ReportGroup was created.

lastModified (datetime) --
The date and time this ReportGroup was last modified.

tags (list) --
A list of tag key and value pairs associated with this report group.
These tags are available for use by AWS services that support AWS CodeBuild report group tags.

(dict) --
A tag, consisting of a key and a value.
This tag is available for use by AWS services that support tags in AWS CodeBuild.

key (string) --
The tag\'s key.

value (string) --
The tag\'s value.













Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceAlreadyExistsException
CodeBuild.Client.exceptions.AccountLimitExceededException


    :return: {
        'reportGroup': {
            'arn': 'string',
            'name': 'string',
            'type': 'TEST',
            'exportConfig': {
                'exportConfigType': 'S3'|'NO_EXPORT',
                's3Destination': {
                    'bucket': 'string',
                    'path': 'string',
                    'packaging': 'ZIP'|'NONE',
                    'encryptionKey': 'string',
                    'encryptionDisabled': True|False
                }
            },
            'created': datetime(2015, 1, 1),
            'lastModified': datetime(2015, 1, 1),
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    S3 : The report results are exported to an S3 bucket.
    NO_EXPORT : The report results are not exported.
    
    """
    pass

def create_webhook(projectName=None, branchFilter=None, filterGroups=None):
    """
    For an existing AWS CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, enables AWS CodeBuild to start rebuilding the source code every time a code change is pushed to the repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_webhook(
        projectName='string',
        branchFilter='string',
        filterGroups=[
            [
                {
                    'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                    'pattern': 'string',
                    'excludeMatchedPattern': True|False
                },
            ],
        ]
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]\nThe name of the AWS CodeBuild project.\n

    :type branchFilter: string
    :param branchFilter: A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If branchFilter is empty, then all branches are built.\n\nNote\nIt is recommended that you use filterGroups instead of branchFilter .\n\n

    :type filterGroups: list
    :param filterGroups: An array of arrays of WebhookFilter objects used to determine which webhooks are triggered. At least one WebhookFilter in the array must specify EVENT as its type .\nFor a build to be triggered, at least one filter group in the filterGroups array must pass. For a filter group to pass, each of its filters must pass.\n\n(list) --\n(dict) --A filter used to determine which webhooks trigger a build.\n\ntype (string) -- [REQUIRED]The type of webhook filter. There are five webhook filter types: EVENT , ACTOR_ACCOUNT_ID , HEAD_REF , BASE_REF , and FILE_PATH .\n\nEVENT\nA webhook event triggers a build when the provided pattern matches one of five event types: PUSH , PULL_REQUEST_CREATED , PULL_REQUEST_UPDATED , PULL_REQUEST_REOPENED , and PULL_REQUEST_MERGED . The EVENT patterns are specified as a comma-separated string. For example, PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED filters all push, pull request created, and pull request updated events.\n\nNote\nThe PULL_REQUEST_REOPENED works with GitHub and GitHub Enterprise only.\nACTOR_ACCOUNT_ID\n\nA webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression pattern .\n\nHEAD_REF\nA webhook event triggers a build when the head reference matches the regular expression pattern . For example, refs/heads/branch-name and refs/tags/tag-name .\nWorks with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.\n\nBASE_REF\nA webhook event triggers a build when the base reference matches the regular expression pattern . For example, refs/heads/branch-name .\n\nNote\nWorks with pull request events only.\nFILE_PATH\n\nA webhook triggers a build when the path of a changed file matches the regular expression pattern .\n\nNote\nWorks with GitHub and GitHub Enterprise push events only.\n\n\npattern (string) -- [REQUIRED]For a WebHookFilter that uses EVENT type, a comma-separated string that specifies one or more events. For example, the webhook filter PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED allows all push, pull request created, and pull request updated events to trigger a build.\nFor a WebHookFilter that uses any of the other filter types, a regular expression pattern. For example, a WebHookFilter that uses HEAD_REF for its type and the pattern ^refs/heads/ triggers a build when the head reference is a branch with a reference name refs/heads/branch-name .\n\nexcludeMatchedPattern (boolean) --Used to indicate that the pattern determines which webhook events do not trigger a build. If true, then a webhook event that does not match the pattern triggers a build. If false, then a webhook event that matches the pattern triggers a build.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'webhook': {
        'url': 'string',
        'payloadUrl': 'string',
        'secret': 'string',
        'branchFilter': 'string',
        'filterGroups': [
            [
                {
                    'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                    'pattern': 'string',
                    'excludeMatchedPattern': True|False
                },
            ],
        ],
        'lastModifiedSecret': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

webhook (dict) --
Information about a webhook that connects repository events to a build project in AWS CodeBuild.

url (string) --
The URL to the webhook.

payloadUrl (string) --
The AWS CodeBuild endpoint where webhook events are sent.

secret (string) --
The secret token of the associated repository.

Note
A Bitbucket webhook does not support secret .


branchFilter (string) --
A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If branchFilter is empty, then all branches are built.

Note
It is recommended that you use filterGroups instead of branchFilter .


filterGroups (list) --
An array of arrays of WebhookFilter objects used to determine which webhooks are triggered. At least one WebhookFilter in the array must specify EVENT as its type .
For a build to be triggered, at least one filter group in the filterGroups array must pass. For a filter group to pass, each of its filters must pass.

(list) --

(dict) --
A filter used to determine which webhooks trigger a build.

type (string) --
The type of webhook filter. There are five webhook filter types: EVENT , ACTOR_ACCOUNT_ID , HEAD_REF , BASE_REF , and FILE_PATH .

EVENT

A webhook event triggers a build when the provided pattern matches one of five event types: PUSH , PULL_REQUEST_CREATED , PULL_REQUEST_UPDATED , PULL_REQUEST_REOPENED , and PULL_REQUEST_MERGED . The EVENT patterns are specified as a comma-separated string. For example, PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED filters all push, pull request created, and pull request updated events.

Note
The PULL_REQUEST_REOPENED works with GitHub and GitHub Enterprise only.
ACTOR_ACCOUNT_ID

A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression pattern .

HEAD_REF

A webhook event triggers a build when the head reference matches the regular expression pattern . For example, refs/heads/branch-name and refs/tags/tag-name .
Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.

BASE_REF

A webhook event triggers a build when the base reference matches the regular expression pattern . For example, refs/heads/branch-name .

Note
Works with pull request events only.
FILE_PATH

A webhook triggers a build when the path of a changed file matches the regular expression pattern .

Note
Works with GitHub and GitHub Enterprise push events only.


pattern (string) --
For a WebHookFilter that uses EVENT type, a comma-separated string that specifies one or more events. For example, the webhook filter PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED allows all push, pull request created, and pull request updated events to trigger a build.
For a WebHookFilter that uses any of the other filter types, a regular expression pattern. For example, a WebHookFilter that uses HEAD_REF for its type and the pattern ^refs/heads/ triggers a build when the head reference is a branch with a reference name refs/heads/branch-name .

excludeMatchedPattern (boolean) --
Used to indicate that the pattern determines which webhook events do not trigger a build. If true, then a webhook event that does not match the pattern triggers a build. If false, then a webhook event that matches the pattern triggers a build.







lastModifiedSecret (datetime) --
A timestamp that indicates the last time a repository\'s secret token was modified.









Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.OAuthProviderException
CodeBuild.Client.exceptions.ResourceAlreadyExistsException
CodeBuild.Client.exceptions.ResourceNotFoundException


    :return: {
        'webhook': {
            'url': 'string',
            'payloadUrl': 'string',
            'secret': 'string',
            'branchFilter': 'string',
            'filterGroups': [
                [
                    {
                        'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                        'pattern': 'string',
                        'excludeMatchedPattern': True|False
                    },
                ],
            ],
            'lastModifiedSecret': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CodeBuild.Client.exceptions.InvalidInputException
    CodeBuild.Client.exceptions.OAuthProviderException
    CodeBuild.Client.exceptions.ResourceAlreadyExistsException
    CodeBuild.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def delete_project(name=None):
    """
    Deletes a build project. When you delete a project, its builds are not deleted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_project(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the build project.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {}
    
    
    :returns: 
    CodeBuild.Client.exceptions.InvalidInputException
    
    """
    pass

def delete_report(arn=None):
    """
    Deletes a report.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_report(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe ARN of the report to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {}
    
    
    :returns: 
    CodeBuild.Client.exceptions.InvalidInputException
    
    """
    pass

def delete_report_group(arn=None):
    """
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_report_group(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe ARN of the report group to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {}
    
    
    :returns: 
    CodeBuild.Client.exceptions.InvalidInputException
    
    """
    pass

def delete_resource_policy(resourceArn=None):
    """
    Deletes a resource policy that is identified by its resource ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_resource_policy(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource that is associated with the resource policy.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {}
    
    
    :returns: 
    CodeBuild.Client.exceptions.InvalidInputException
    
    """
    pass

def delete_source_credentials(arn=None):
    """
    Deletes a set of GitHub, GitHub Enterprise, or Bitbucket source credentials.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_source_credentials(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the token.\n

    :rtype: dict
ReturnsResponse Syntax{
    'arn': 'string'
}


Response Structure

(dict) --
arn (string) --The Amazon Resource Name (ARN) of the token.






Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException


    :return: {
        'arn': 'string'
    }
    
    
    """
    pass

def delete_webhook(projectName=None):
    """
    For an existing AWS CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, stops AWS CodeBuild from rebuilding the source code every time a code change is pushed to the repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_webhook(
        projectName='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]\nThe name of the AWS CodeBuild project.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException
CodeBuild.Client.exceptions.OAuthProviderException


    :return: {}
    
    
    :returns: 
    CodeBuild.Client.exceptions.InvalidInputException
    CodeBuild.Client.exceptions.ResourceNotFoundException
    CodeBuild.Client.exceptions.OAuthProviderException
    
    """
    pass

def describe_test_cases(reportArn=None, nextToken=None, maxResults=None, filter=None):
    """
    Returns a list of details about test cases for a report.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_test_cases(
        reportArn='string',
        nextToken='string',
        maxResults=123,
        filter={
            'status': 'string'
        }
    )
    
    
    :type reportArn: string
    :param reportArn: [REQUIRED]\nThe ARN of the report for which test cases are returned.\n

    :type nextToken: string
    :param nextToken: During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :type maxResults: integer
    :param maxResults: The maximum number of paginated test cases returned per response. Use nextToken to iterate pages in the list of returned TestCase objects. The default value is 100.

    :type filter: dict
    :param filter: A TestCaseFilter object used to filter the returned reports.\n\nstatus (string) --The status used to filter test cases. Valid statuses are SUCCEEDED , FAILED , ERROR , SKIPPED , and UNKNOWN . A TestCaseFilter can have one status.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'testCases': [
        {
            'reportArn': 'string',
            'testRawDataPath': 'string',
            'prefix': 'string',
            'name': 'string',
            'status': 'string',
            'durationInNanoSeconds': 123,
            'message': 'string',
            'expired': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

testCases (list) --
The returned list of test cases.

(dict) --
Information about a test case created using a framework such as NUnit or Cucumber. A test case might be a unit test or a configuration test.

reportArn (string) --
The ARN of the report to which the test case belongs.

testRawDataPath (string) --
The path to the raw data file that contains the test result.

prefix (string) --
A string that is applied to a series of related test cases. CodeBuild generates the prefix. The prefix depends on the framework used to generate the tests.

name (string) --
The name of the test case.

status (string) --
The status returned by the test case after it was run. Valid statuses are SUCCEEDED , FAILED , ERROR , SKIPPED , and UNKNOWN .

durationInNanoSeconds (integer) --
The number of nanoseconds it took to run this test case.

message (string) --
A message associated with a test case. For example, an error message or stack trace.

expired (datetime) --
The date and time a test case expires. A test case expires 30 days after it is created. An expired test case is not available to view in CodeBuild.











Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException


    :return: {
        'nextToken': 'string',
        'testCases': [
            {
                'reportArn': 'string',
                'testRawDataPath': 'string',
                'prefix': 'string',
                'name': 'string',
                'status': 'string',
                'durationInNanoSeconds': 123,
                'message': 'string',
                'expired': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    :returns: 
    CodeBuild.Client.exceptions.InvalidInputException
    CodeBuild.Client.exceptions.ResourceNotFoundException
    
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

def get_resource_policy(resourceArn=None):
    """
    Gets a resource policy that is identified by its resource ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_resource_policy(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource that is associated with the resource policy.\n

    :rtype: dict
ReturnsResponse Syntax{
    'policy': 'string'
}


Response Structure

(dict) --
policy (string) --The resource policy for the resource identified by the input ARN parameter.






Exceptions

CodeBuild.Client.exceptions.ResourceNotFoundException
CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'policy': 'string'
    }
    
    
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

def import_source_credentials(username=None, token=None, serverType=None, authType=None, shouldOverwrite=None):
    """
    Imports the source repository credentials for an AWS CodeBuild project that has its source code stored in a GitHub, GitHub Enterprise, or Bitbucket repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.import_source_credentials(
        username='string',
        token='string',
        serverType='GITHUB'|'BITBUCKET'|'GITHUB_ENTERPRISE',
        authType='OAUTH'|'BASIC_AUTH'|'PERSONAL_ACCESS_TOKEN',
        shouldOverwrite=True|False
    )
    
    
    :type username: string
    :param username: The Bitbucket username when the authType is BASIC_AUTH. This parameter is not valid for other types of source providers or connections.

    :type token: string
    :param token: [REQUIRED]\nFor GitHub or GitHub Enterprise, this is the personal access token. For Bitbucket, this is the app password.\n

    :type serverType: string
    :param serverType: [REQUIRED]\nThe source provider used for this project.\n

    :type authType: string
    :param authType: [REQUIRED]\nThe type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API and must be created using the AWS CodeBuild console.\n

    :type shouldOverwrite: boolean
    :param shouldOverwrite: Set to false to prevent overwriting the repository source credentials. Set to true to overwrite the repository source credentials. The default value is true .

    :rtype: dict

ReturnsResponse Syntax
{
    'arn': 'string'
}


Response Structure

(dict) --

arn (string) --
The Amazon Resource Name (ARN) of the token.







Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.AccountLimitExceededException
CodeBuild.Client.exceptions.ResourceAlreadyExistsException


    :return: {
        'arn': 'string'
    }
    
    
    :returns: 
    CodeBuild.Client.exceptions.InvalidInputException
    CodeBuild.Client.exceptions.AccountLimitExceededException
    CodeBuild.Client.exceptions.ResourceAlreadyExistsException
    
    """
    pass

def invalidate_project_cache(projectName=None):
    """
    Resets the cache for a project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.invalidate_project_cache(
        projectName='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]\nThe name of the AWS CodeBuild build project that the cache is reset for.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    CodeBuild.Client.exceptions.InvalidInputException
    CodeBuild.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_builds(sortOrder=None, nextToken=None):
    """
    Gets a list of build IDs, with each build ID representing a single build.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_builds(
        sortOrder='ASCENDING'|'DESCENDING',
        nextToken='string'
    )
    
    
    :type sortOrder: string
    :param sortOrder: The order to list build IDs. Valid values include:\n\nASCENDING : List the build IDs in ascending order by build ID.\nDESCENDING : List the build IDs in descending order by build ID.\n\n

    :type nextToken: string
    :param nextToken: During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a nextToken . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'ids': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

ids (list) --
A list of build IDs, with each build ID representing a single build.

(string) --


nextToken (string) --
If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a nextToken . To get the next batch of items in the list, call this operation again, adding the next token to the call.







Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'ids': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_builds_for_project(projectName=None, sortOrder=None, nextToken=None):
    """
    Gets a list of build IDs for the specified build project, with each build ID representing a single build.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_builds_for_project(
        projectName='string',
        sortOrder='ASCENDING'|'DESCENDING',
        nextToken='string'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]\nThe name of the AWS CodeBuild project.\n

    :type sortOrder: string
    :param sortOrder: The order to list build IDs. Valid values include:\n\nASCENDING : List the build IDs in ascending order by build ID.\nDESCENDING : List the build IDs in descending order by build ID.\n\n

    :type nextToken: string
    :param nextToken: During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a nextToken . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'ids': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

ids (list) --
A list of build IDs for the specified build project, with each build ID representing a single build.

(string) --


nextToken (string) --
If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a nextToken . To get the next batch of items in the list, call this operation again, adding the next token to the call.







Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException


    :return: {
        'ids': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_curated_environment_images():
    """
    Gets information about Docker images that are managed by AWS CodeBuild.
    See also: AWS API Documentation
    
    
    :example: response = client.list_curated_environment_images()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'platforms': [
        {
            'platform': 'DEBIAN'|'AMAZON_LINUX'|'UBUNTU'|'WINDOWS_SERVER',
            'languages': [
                {
                    'language': 'JAVA'|'PYTHON'|'NODE_JS'|'RUBY'|'GOLANG'|'DOCKER'|'ANDROID'|'DOTNET'|'BASE'|'PHP',
                    'images': [
                        {
                            'name': 'string',
                            'description': 'string',
                            'versions': [
                                'string',
                            ]
                        },
                    ]
                },
            ]
        },
    ]
}


Response Structure

(dict) --
platforms (list) --Information about supported platforms for Docker images that are managed by AWS CodeBuild.

(dict) --A set of Docker images that are related by platform and are managed by AWS CodeBuild.

platform (string) --The platform\'s name.

languages (list) --The list of programming languages that are available for the specified platform.

(dict) --A set of Docker images that are related by programming language and are managed by AWS CodeBuild.

language (string) --The programming language for the Docker images.

images (list) --The list of Docker images that are related by the specified programming language.

(dict) --Information about a Docker image that is managed by AWS CodeBuild.

name (string) --The name of the Docker image.

description (string) --The description of the Docker image.

versions (list) --A list of environment image versions.

(string) --




















    :return: {
        'platforms': [
            {
                'platform': 'DEBIAN'|'AMAZON_LINUX'|'UBUNTU'|'WINDOWS_SERVER',
                'languages': [
                    {
                        'language': 'JAVA'|'PYTHON'|'NODE_JS'|'RUBY'|'GOLANG'|'DOCKER'|'ANDROID'|'DOTNET'|'BASE'|'PHP',
                        'images': [
                            {
                                'name': 'string',
                                'description': 'string',
                                'versions': [
                                    'string',
                                ]
                            },
                        ]
                    },
                ]
            },
        ]
    }
    
    
    """
    pass

def list_projects(sortBy=None, sortOrder=None, nextToken=None):
    """
    Gets a list of build project names, with each build project name representing a single build project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_projects(
        sortBy='NAME'|'CREATED_TIME'|'LAST_MODIFIED_TIME',
        sortOrder='ASCENDING'|'DESCENDING',
        nextToken='string'
    )
    
    
    :type sortBy: string
    :param sortBy: The criterion to be used to list build project names. Valid values include:\n\nCREATED_TIME : List based on when each build project was created.\nLAST_MODIFIED_TIME : List based on when information about each build project was last changed.\nNAME : List based on each build project\'s name.\n\nUse sortOrder to specify in what order to list the build project names based on the preceding criteria.\n

    :type sortOrder: string
    :param sortOrder: The order in which to list build projects. Valid values include:\n\nASCENDING : List in ascending order.\nDESCENDING : List in descending order.\n\nUse sortBy to specify the criterion to be used to list build project names.\n

    :type nextToken: string
    :param nextToken: During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a nextToken . To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'projects': [
        'string',
    ]
}


Response Structure

(dict) --

nextToken (string) --
If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a nextToken . To get the next batch of items in the list, call this operation again, adding the next token to the call.

projects (list) --
The list of build project names, with each build project name representing a single build project.

(string) --








Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'nextToken': 'string',
        'projects': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_report_groups(sortOrder=None, sortBy=None, nextToken=None, maxResults=None):
    """
    Gets a list ARNs for the report groups in the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_report_groups(
        sortOrder='ASCENDING'|'DESCENDING',
        sortBy='NAME'|'CREATED_TIME'|'LAST_MODIFIED_TIME',
        nextToken='string',
        maxResults=123
    )
    
    
    :type sortOrder: string
    :param sortOrder: Used to specify the order to sort the list of returned report groups. Valid values are ASCENDING and DESCENDING .

    :type sortBy: string
    :param sortBy: The criterion to be used to list build report groups. Valid values include:\n\nCREATED_TIME : List based on when each report group was created.\nLAST_MODIFIED_TIME : List based on when each report group was last changed.\nNAME : List based on each report group\'s name.\n\n

    :type nextToken: string
    :param nextToken: During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :type maxResults: integer
    :param maxResults: The maximum number of paginated report groups returned per response. Use nextToken to iterate pages in the list of returned ReportGroup objects. The default value is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'reportGroups': [
        'string',
    ]
}


Response Structure

(dict) --

nextToken (string) --
During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

reportGroups (list) --
The list of ARNs for the report groups in the current AWS account.

(string) --








Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'nextToken': 'string',
        'reportGroups': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_reports(sortOrder=None, nextToken=None, maxResults=None, filter=None):
    """
    Returns a list of ARNs for the reports in the current AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_reports(
        sortOrder='ASCENDING'|'DESCENDING',
        nextToken='string',
        maxResults=123,
        filter={
            'status': 'GENERATING'|'SUCCEEDED'|'FAILED'|'INCOMPLETE'|'DELETING'
        }
    )
    
    
    :type sortOrder: string
    :param sortOrder: Specifies the sort order for the list of returned reports. Valid values are:\n\nASCENDING : return reports in chronological order based on their creation date.\nDESCENDING : return reports in the reverse chronological order based on their creation date.\n\n

    :type nextToken: string
    :param nextToken: During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :type maxResults: integer
    :param maxResults: The maximum number of paginated reports returned per response. Use nextToken to iterate pages in the list of returned Report objects. The default value is 100.

    :type filter: dict
    :param filter: A ReportFilter object used to filter the returned reports.\n\nstatus (string) --The status used to filter reports. You can filter using one status only.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'reports': [
        'string',
    ]
}


Response Structure

(dict) --

nextToken (string) --
During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

reports (list) --
The list of returned ARNs for the reports in the current AWS account.

(string) --








Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'nextToken': 'string',
        'reports': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_reports_for_report_group(reportGroupArn=None, nextToken=None, sortOrder=None, maxResults=None, filter=None):
    """
    Returns a list of ARNs for the reports that belong to a ReportGroup .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_reports_for_report_group(
        reportGroupArn='string',
        nextToken='string',
        sortOrder='ASCENDING'|'DESCENDING',
        maxResults=123,
        filter={
            'status': 'GENERATING'|'SUCCEEDED'|'FAILED'|'INCOMPLETE'|'DELETING'
        }
    )
    
    
    :type reportGroupArn: string
    :param reportGroupArn: [REQUIRED]\nThe ARN of the report group for which you want to return report ARNs.\n

    :type nextToken: string
    :param nextToken: During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :type sortOrder: string
    :param sortOrder: Use to specify whether the results are returned in ascending or descending order.

    :type maxResults: integer
    :param maxResults: The maximum number of paginated reports in this report group returned per response. Use nextToken to iterate pages in the list of returned Report objects. The default value is 100.

    :type filter: dict
    :param filter: A ReportFilter object used to filter the returned reports.\n\nstatus (string) --The status used to filter reports. You can filter using one status only.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'reports': [
        'string',
    ]
}


Response Structure

(dict) --

nextToken (string) --
During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

reports (list) --
The list of returned report group ARNs.

(string) --








Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException


    :return: {
        'nextToken': 'string',
        'reports': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_shared_projects(sortBy=None, sortOrder=None, maxResults=None, nextToken=None):
    """
    Gets a list of projects that are shared with other AWS accounts or users.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_shared_projects(
        sortBy='ARN'|'MODIFIED_TIME',
        sortOrder='ASCENDING'|'DESCENDING',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type sortBy: string
    :param sortBy: The criterion to be used to list build projects shared with the current AWS account or user. Valid values include:\n\nARN : List based on the ARN.\nMODIFIED_TIME : List based on when information about the shared project was last changed.\n\n

    :type sortOrder: string
    :param sortOrder: The order in which to list shared build projects. Valid values include:\n\nASCENDING : List in ascending order.\nDESCENDING : List in descending order.\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of paginated shared build projects returned per response. Use nextToken to iterate pages in the list of returned Project objects. The default value is 100.

    :type nextToken: string
    :param nextToken: During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'projects': [
        'string',
    ]
}


Response Structure

(dict) --

nextToken (string) --
During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

projects (list) --
The list of ARNs for the build projects shared with the current AWS account or user.

(string) --








Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'nextToken': 'string',
        'projects': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_shared_report_groups(sortOrder=None, sortBy=None, nextToken=None, maxResults=None):
    """
    Gets a list of report groups that are shared with other AWS accounts or users.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_shared_report_groups(
        sortOrder='ASCENDING'|'DESCENDING',
        sortBy='ARN'|'MODIFIED_TIME',
        nextToken='string',
        maxResults=123
    )
    
    
    :type sortOrder: string
    :param sortOrder: The order in which to list shared report groups. Valid values include:\n\nASCENDING : List in ascending order.\nDESCENDING : List in descending order.\n\n

    :type sortBy: string
    :param sortBy: The criterion to be used to list report groups shared with the current AWS account or user. Valid values include:\n\nARN : List based on the ARN.\nMODIFIED_TIME : List based on when information about the shared report group was last changed.\n\n

    :type nextToken: string
    :param nextToken: During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

    :type maxResults: integer
    :param maxResults: The maximum number of paginated shared report groups per response. Use nextToken to iterate pages in the list of returned ReportGroup objects. The default value is 100.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'reportGroups': [
        'string',
    ]
}


Response Structure

(dict) --

nextToken (string) --
During a previous call, the maximum number of items that can be returned is the value specified in maxResults . If there more items in the list, then a unique string called a nextToken is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.

reportGroups (list) --
The list of ARNs for the report groups shared with the current AWS account or user.

(string) --








Exceptions

CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'nextToken': 'string',
        'reportGroups': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_source_credentials():
    """
    Returns a list of SourceCredentialsInfo objects.
    See also: AWS API Documentation
    
    
    :example: response = client.list_source_credentials()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'sourceCredentialsInfos': [
        {
            'arn': 'string',
            'serverType': 'GITHUB'|'BITBUCKET'|'GITHUB_ENTERPRISE',
            'authType': 'OAUTH'|'BASIC_AUTH'|'PERSONAL_ACCESS_TOKEN'
        },
    ]
}


Response Structure

(dict) --
sourceCredentialsInfos (list) --A list of SourceCredentialsInfo objects. Each SourceCredentialsInfo object includes the authentication type, token ARN, and type of source provider for one set of credentials.

(dict) --Information about the credentials for a GitHub, GitHub Enterprise, or Bitbucket repository.

arn (string) --The Amazon Resource Name (ARN) of the token.

serverType (string) --The type of source provider. The valid options are GITHUB, GITHUB_ENTERPRISE, or BITBUCKET.

authType (string) --The type of authentication used by the credentials. Valid options are OAUTH, BASIC_AUTH, or PERSONAL_ACCESS_TOKEN.











    :return: {
        'sourceCredentialsInfos': [
            {
                'arn': 'string',
                'serverType': 'GITHUB'|'BITBUCKET'|'GITHUB_ENTERPRISE',
                'authType': 'OAUTH'|'BASIC_AUTH'|'PERSONAL_ACCESS_TOKEN'
            },
        ]
    }
    
    
    """
    pass

def put_resource_policy(policy=None, resourceArn=None):
    """
    Stores a resource policy for the ARN of a Project or ReportGroup object.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_resource_policy(
        policy='string',
        resourceArn='string'
    )
    
    
    :type policy: string
    :param policy: [REQUIRED]\nA JSON-formatted resource policy. For more information, see Sharing a Project and Sharing a Report Group in the AWS CodeBuild User Guide .\n

    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the Project or ReportGroup resource you want to associate with a resource policy.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceArn': 'string'
}


Response Structure

(dict) --

resourceArn (string) --
The ARN of the Project or ReportGroup resource that is associated with a resource policy.







Exceptions

CodeBuild.Client.exceptions.ResourceNotFoundException
CodeBuild.Client.exceptions.InvalidInputException


    :return: {
        'resourceArn': 'string'
    }
    
    
    :returns: 
    CodeBuild.Client.exceptions.ResourceNotFoundException
    CodeBuild.Client.exceptions.InvalidInputException
    
    """
    pass

def start_build(projectName=None, secondarySourcesOverride=None, secondarySourcesVersionOverride=None, sourceVersion=None, artifactsOverride=None, secondaryArtifactsOverride=None, environmentVariablesOverride=None, sourceTypeOverride=None, sourceLocationOverride=None, sourceAuthOverride=None, gitCloneDepthOverride=None, gitSubmodulesConfigOverride=None, buildspecOverride=None, insecureSslOverride=None, reportBuildStatusOverride=None, environmentTypeOverride=None, imageOverride=None, computeTypeOverride=None, certificateOverride=None, cacheOverride=None, serviceRoleOverride=None, privilegedModeOverride=None, timeoutInMinutesOverride=None, queuedTimeoutInMinutesOverride=None, encryptionKeyOverride=None, idempotencyToken=None, logsConfigOverride=None, registryCredentialOverride=None, imagePullCredentialsTypeOverride=None):
    """
    Starts running a build.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_build(
        projectName='string',
        secondarySourcesOverride=[
            {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
        ],
        secondarySourcesVersionOverride=[
            {
                'sourceIdentifier': 'string',
                'sourceVersion': 'string'
            },
        ],
        sourceVersion='string',
        artifactsOverride={
            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
            'location': 'string',
            'path': 'string',
            'namespaceType': 'NONE'|'BUILD_ID',
            'name': 'string',
            'packaging': 'NONE'|'ZIP',
            'overrideArtifactName': True|False,
            'encryptionDisabled': True|False,
            'artifactIdentifier': 'string'
        },
        secondaryArtifactsOverride=[
            {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
        ],
        environmentVariablesOverride=[
            {
                'name': 'string',
                'value': 'string',
                'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
            },
        ],
        sourceTypeOverride='CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
        sourceLocationOverride='string',
        sourceAuthOverride={
            'type': 'OAUTH',
            'resource': 'string'
        },
        gitCloneDepthOverride=123,
        gitSubmodulesConfigOverride={
            'fetchSubmodules': True|False
        },
        buildspecOverride='string',
        insecureSslOverride=True|False,
        reportBuildStatusOverride=True|False,
        environmentTypeOverride='WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
        imageOverride='string',
        computeTypeOverride='BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
        certificateOverride='string',
        cacheOverride={
            'type': 'NO_CACHE'|'S3'|'LOCAL',
            'location': 'string',
            'modes': [
                'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
            ]
        },
        serviceRoleOverride='string',
        privilegedModeOverride=True|False,
        timeoutInMinutesOverride=123,
        queuedTimeoutInMinutesOverride=123,
        encryptionKeyOverride='string',
        idempotencyToken='string',
        logsConfigOverride={
            'cloudWatchLogs': {
                'status': 'ENABLED'|'DISABLED',
                'groupName': 'string',
                'streamName': 'string'
            },
            's3Logs': {
                'status': 'ENABLED'|'DISABLED',
                'location': 'string',
                'encryptionDisabled': True|False
            }
        },
        registryCredentialOverride={
            'credential': 'string',
            'credentialProvider': 'SECRETS_MANAGER'
        },
        imagePullCredentialsTypeOverride='CODEBUILD'|'SERVICE_ROLE'
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]\nThe name of the AWS CodeBuild build project to start running a build.\n

    :type secondarySourcesOverride: list
    :param secondarySourcesOverride: An array of ProjectSource objects.\n\n(dict) --Information about the build input source code for the build project.\n\ntype (string) -- [REQUIRED]The type of repository that contains the source code to be built. Valid values include:\n\nBITBUCKET : The source code is in a Bitbucket repository.\nCODECOMMIT : The source code is in an AWS CodeCommit repository.\nCODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.\nGITHUB : The source code is in a GitHub repository.\nGITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.\nNO_SOURCE : The project does not have input source code.\nS3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.\n\n\nlocation (string) --Information about the location of the source code to be built. Valid values include:\n\nFor source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.\nFor source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).\nFor source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.\nThe path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).\nThe path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).\n\n\nFor source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .\nFor source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .\n\n\ngitCloneDepth (integer) --Information about the Git clone depth for the build project.\n\ngitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.\n\nfetchSubmodules (boolean) -- [REQUIRED]Set to true to fetch Git submodules for your AWS CodeBuild build project.\n\n\n\nbuildspec (string) --The buildspec file declaration to use for the builds in this build project.\nIf this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .\n\nauth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.\nThis information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.\n\ntype (string) -- [REQUIRED]\nNote\nThis data type is deprecated and is no longer accurate or used.\n\nThe authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.\n\nresource (string) --The resource value that applies to the specified authorization type.\n\n\n\nreportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.\n\nNote\nThe status of a build triggered by a webhook is always reported to your source provider.\n\n\ninsecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.\n\nsourceIdentifier (string) --An identifier for this project source.\n\n\n\n\n

    :type secondarySourcesVersionOverride: list
    :param secondarySourcesVersionOverride: An array of ProjectSourceVersion objects that specify one or more versions of the project\'s secondary sources to be used for this build only.\n\n(dict) --A source identifier and its corresponding version.\n\nsourceIdentifier (string) -- [REQUIRED]An identifier for a source in the build project.\n\nsourceVersion (string) -- [REQUIRED]The source version for the corresponding source identifier. If specified, must be one of:\n\nFor AWS CodeCommit: the commit ID, branch, or Git tag to use.\nFor GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.\n\nFor more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .\n\n\n\n\n

    :type sourceVersion: string
    :param sourceVersion: A version of the build input to be built, for this build only. If not specified, the latest version is used. If specified, must be one of:\n\nFor AWS CodeCommit: the commit ID, branch, or Git tag to use.\nFor GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.\n\nIf sourceVersion is specified at the project level, then this sourceVersion (at the build level) takes precedence.\nFor more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .\n

    :type artifactsOverride: dict
    :param artifactsOverride: Build output artifact settings that override, for this build only, the latest ones already defined in the build project.\n\ntype (string) -- [REQUIRED]The type of build output artifact. Valid values include:\n\nCODEPIPELINE : The build project has build output generated through AWS CodePipeline.\n\n\nNote\nThe CODEPIPELINE type is not supported for secondaryArtifacts .\n\n\nNO_ARTIFACTS : The build project does not produce any build output.\nS3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).\n\n\nlocation (string) --Information about the build output artifact location:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output bucket.\n\n\npath (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.\n\nFor example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .\n\nnamespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nBUILD_ID : Include the build ID in the location of the build output artifact.\nNONE : Do not include the build ID. This is the default if namespaceType is not specified.\n\n\n\nFor example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\n\nname (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.\n\nFor example:\n\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\nIf path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .\n\n\npackaging (string) --The type of build output artifact to create:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nNONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.\nZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.\n\n\n\n\noverrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.\n\nencryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.\n\nartifactIdentifier (string) --An identifier for this artifact definition.\n\n\n

    :type secondaryArtifactsOverride: list
    :param secondaryArtifactsOverride: An array of ProjectArtifacts objects.\n\n(dict) --Information about the build output artifacts for the build project.\n\ntype (string) -- [REQUIRED]The type of build output artifact. Valid values include:\n\nCODEPIPELINE : The build project has build output generated through AWS CodePipeline.\n\n\nNote\nThe CODEPIPELINE type is not supported for secondaryArtifacts .\n\n\nNO_ARTIFACTS : The build project does not produce any build output.\nS3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).\n\n\nlocation (string) --Information about the build output artifact location:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output bucket.\n\n\npath (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.\n\nFor example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .\n\nnamespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nBUILD_ID : Include the build ID in the location of the build output artifact.\nNONE : Do not include the build ID. This is the default if namespaceType is not specified.\n\n\n\nFor example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\n\nname (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.\n\nFor example:\n\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\nIf path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .\n\n\npackaging (string) --The type of build output artifact to create:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nNONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.\nZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.\n\n\n\n\noverrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.\n\nencryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.\n\nartifactIdentifier (string) --An identifier for this artifact definition.\n\n\n\n\n

    :type environmentVariablesOverride: list
    :param environmentVariablesOverride: A set of environment variables that overrides, for this build only, the latest ones already defined in the build project.\n\n(dict) --Information about an environment variable for a build project or a build.\n\nname (string) -- [REQUIRED]The name or key of the environment variable.\n\nvalue (string) -- [REQUIRED]The value of the environment variable.\n\nWarning\nWe strongly discourage the use of PLAINTEXT environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. PLAINTEXT environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI). For sensitive values, we recommend you use an environment variable of type PARAMETER_STORE or SECRETS_MANAGER .\n\n\ntype (string) --The type of environment variable. Valid values include:\n\nPARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. To learn how to specify a parameter store environment variable, see parameter store reference-key in the buildspec file .\nPLAINTEXT : An environment variable in plain text format. This is the default value.\nSECRETS_MANAGER : An environment variable stored in AWS Secrets Manager. To learn how to specify a secrets manager environment variable, see secrets manager reference-key in the buildspec file .\n\n\n\n\n\n

    :type sourceTypeOverride: string
    :param sourceTypeOverride: A source input type, for this build, that overrides the source input defined in the build project.

    :type sourceLocationOverride: string
    :param sourceLocationOverride: A location that overrides, for this build, the source location for the one defined in the build project.

    :type sourceAuthOverride: dict
    :param sourceAuthOverride: An authorization type for this build that overrides the one defined in the build project. This override applies only if the build project\'s source is BitBucket or GitHub.\n\ntype (string) -- [REQUIRED]\nNote\nThis data type is deprecated and is no longer accurate or used.\n\nThe authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.\n\nresource (string) --The resource value that applies to the specified authorization type.\n\n\n

    :type gitCloneDepthOverride: integer
    :param gitCloneDepthOverride: The user-defined depth of history, with a minimum value of 0, that overrides, for this build only, any previous depth of history defined in the build project.

    :type gitSubmodulesConfigOverride: dict
    :param gitSubmodulesConfigOverride: Information about the Git submodules configuration for this build of an AWS CodeBuild build project.\n\nfetchSubmodules (boolean) -- [REQUIRED]Set to true to fetch Git submodules for your AWS CodeBuild build project.\n\n\n

    :type buildspecOverride: string
    :param buildspecOverride: A buildspec file declaration that overrides, for this build only, the latest one already defined in the build project.\nIf this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .\n

    :type insecureSslOverride: boolean
    :param insecureSslOverride: Enable this flag to override the insecure SSL setting that is specified in the build project. The insecure SSL setting determines whether to ignore SSL warnings while connecting to the project source code. This override applies only if the build\'s source is GitHub Enterprise.

    :type reportBuildStatusOverride: boolean
    :param reportBuildStatusOverride: Set to true to report to your source provider the status of a build\'s start and completion. If you use this option with a source provider other than GitHub, GitHub Enterprise, or Bitbucket, an invalidInputException is thrown.\n\nNote\nThe status of a build triggered by a webhook is always reported to your source provider.\n\n

    :type environmentTypeOverride: string
    :param environmentTypeOverride: A container type for this build that overrides the one specified in the build project.

    :type imageOverride: string
    :param imageOverride: The name of an image for this build that overrides the one specified in the build project.

    :type computeTypeOverride: string
    :param computeTypeOverride: The name of a compute type for this build that overrides the one specified in the build project.

    :type certificateOverride: string
    :param certificateOverride: The name of a certificate for this build that overrides the one specified in the build project.

    :type cacheOverride: dict
    :param cacheOverride: A ProjectCache object specified for this build that overrides the one defined in the build project.\n\ntype (string) -- [REQUIRED]The type of cache used by the build project. Valid values include:\n\nNO_CACHE : The build project does not use any cache.\nS3 : The build project reads and writes from and to S3.\nLOCAL : The build project stores a cache locally on a build host that is only available to that build host.\n\n\nlocation (string) --Information about the cache location:\n\nNO_CACHE or LOCAL : This value is ignored.\nS3 : This is the S3 bucket name/prefix.\n\n\nmodes (list) --If you use a LOCAL cache, the local cache mode. You can use one or more local cache modes at the same time.\n\nLOCAL_SOURCE_CACHE mode caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.\nLOCAL_DOCKER_LAYER_CACHE mode caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.\n\n\nNote\n\nYou can use a Docker layer cache in the Linux environment only.\nThe privileged flag must be set so that your project has the required Docker permissions.\nYou should consider the security implications before you use a Docker layer cache.\n\n\n\nLOCAL_CUSTOM_CACHE mode caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:\nOnly directories can be specified for caching. You cannot specify individual files.\nSymlinks are used to reference cached directories.\nCached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.\n\n\n\n\n(string) --\n\n\n\n

    :type serviceRoleOverride: string
    :param serviceRoleOverride: The name of a service role for this build that overrides the one specified in the build project.

    :type privilegedModeOverride: boolean
    :param privilegedModeOverride: Enable this flag to override privileged mode in the build project.

    :type timeoutInMinutesOverride: integer
    :param timeoutInMinutesOverride: The number of build timeout minutes, from 5 to 480 (8 hours), that overrides, for this build only, the latest setting already defined in the build project.

    :type queuedTimeoutInMinutesOverride: integer
    :param queuedTimeoutInMinutesOverride: The number of minutes a build is allowed to be queued before it times out.

    :type encryptionKeyOverride: string
    :param encryptionKeyOverride: The AWS Key Management Service (AWS KMS) customer master key (CMK) that overrides the one specified in the build project. The CMK key encrypts the build output artifacts.\n\nNote\nYou can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.\n\nYou can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK\'s alias (using the format ``alias/alias-name `` ).\n

    :type idempotencyToken: string
    :param idempotencyToken: A unique, case sensitive identifier you provide to ensure the idempotency of the StartBuild request. The token is included in the StartBuild request and is valid for 12 hours. If you repeat the StartBuild request with the same token, but change a parameter, AWS CodeBuild returns a parameter mismatch error.

    :type logsConfigOverride: dict
    :param logsConfigOverride: Log settings for this build that override the log settings defined in the build project.\n\ncloudWatchLogs (dict) --Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default.\n\nstatus (string) -- [REQUIRED]The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:\n\nENABLED : Amazon CloudWatch Logs are enabled for this build project.\nDISABLED : Amazon CloudWatch Logs are not enabled for this build project.\n\n\ngroupName (string) --The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .\n\nstreamName (string) --The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .\n\n\n\ns3Logs (dict) --Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.\n\nstatus (string) -- [REQUIRED]The current status of the S3 build logs. Valid values are:\n\nENABLED : S3 build logs are enabled for this build project.\nDISABLED : S3 build logs are not enabled for this build project.\n\n\nlocation (string) --The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .\n\nencryptionDisabled (boolean) --Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.\n\n\n\n\n

    :type registryCredentialOverride: dict
    :param registryCredentialOverride: The credentials for access to a private registry.\n\ncredential (string) -- [REQUIRED]The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.\n\nNote\nThe credential can use the name of the credentials only if they exist in your current AWS Region.\n\n\ncredentialProvider (string) -- [REQUIRED]The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.\n\n\n

    :type imagePullCredentialsTypeOverride: string
    :param imagePullCredentialsTypeOverride: The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid values:\n\nCODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild\'s service principal.\nSERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.\n\nWhen using a cross-account or private registry image, you must use SERVICE_ROLE credentials. When using an AWS CodeBuild curated image, you must use CODEBUILD credentials.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'build': {
        'id': 'string',
        'arn': 'string',
        'buildNumber': 123,
        'startTime': datetime(2015, 1, 1),
        'endTime': datetime(2015, 1, 1),
        'currentPhase': 'string',
        'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
        'sourceVersion': 'string',
        'resolvedSourceVersion': 'string',
        'projectName': 'string',
        'phases': [
            {
                'phaseType': 'SUBMITTED'|'QUEUED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'durationInSeconds': 123,
                'contexts': [
                    {
                        'statusCode': 'string',
                        'message': 'string'
                    },
                ]
            },
        ],
        'source': {
            'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
            'location': 'string',
            'gitCloneDepth': 123,
            'gitSubmodulesConfig': {
                'fetchSubmodules': True|False
            },
            'buildspec': 'string',
            'auth': {
                'type': 'OAUTH',
                'resource': 'string'
            },
            'reportBuildStatus': True|False,
            'insecureSsl': True|False,
            'sourceIdentifier': 'string'
        },
        'secondarySources': [
            {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
        ],
        'secondarySourceVersions': [
            {
                'sourceIdentifier': 'string',
                'sourceVersion': 'string'
            },
        ],
        'artifacts': {
            'location': 'string',
            'sha256sum': 'string',
            'md5sum': 'string',
            'overrideArtifactName': True|False,
            'encryptionDisabled': True|False,
            'artifactIdentifier': 'string'
        },
        'secondaryArtifacts': [
            {
                'location': 'string',
                'sha256sum': 'string',
                'md5sum': 'string',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
        ],
        'cache': {
            'type': 'NO_CACHE'|'S3'|'LOCAL',
            'location': 'string',
            'modes': [
                'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
            ]
        },
        'environment': {
            'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
            'image': 'string',
            'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
            'environmentVariables': [
                {
                    'name': 'string',
                    'value': 'string',
                    'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                },
            ],
            'privilegedMode': True|False,
            'certificate': 'string',
            'registryCredential': {
                'credential': 'string',
                'credentialProvider': 'SECRETS_MANAGER'
            },
            'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
        },
        'serviceRole': 'string',
        'logs': {
            'groupName': 'string',
            'streamName': 'string',
            'deepLink': 'string',
            's3DeepLink': 'string',
            'cloudWatchLogsArn': 'string',
            's3LogsArn': 'string',
            'cloudWatchLogs': {
                'status': 'ENABLED'|'DISABLED',
                'groupName': 'string',
                'streamName': 'string'
            },
            's3Logs': {
                'status': 'ENABLED'|'DISABLED',
                'location': 'string',
                'encryptionDisabled': True|False
            }
        },
        'timeoutInMinutes': 123,
        'queuedTimeoutInMinutes': 123,
        'buildComplete': True|False,
        'initiator': 'string',
        'vpcConfig': {
            'vpcId': 'string',
            'subnets': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ]
        },
        'networkInterface': {
            'subnetId': 'string',
            'networkInterfaceId': 'string'
        },
        'encryptionKey': 'string',
        'exportedEnvironmentVariables': [
            {
                'name': 'string',
                'value': 'string'
            },
        ],
        'reportArns': [
            'string',
        ],
        'fileSystemLocations': [
            {
                'type': 'EFS',
                'location': 'string',
                'mountPoint': 'string',
                'identifier': 'string',
                'mountOptions': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

build (dict) --
Information about the build to be run.

id (string) --
The unique ID for the build.

arn (string) --
The Amazon Resource Name (ARN) of the build.

buildNumber (integer) --
The number of the build. For each project, the buildNumber of its first build is 1 . The buildNumber of each subsequent build is incremented by 1 . If a build is deleted, the buildNumber of other builds does not change.

startTime (datetime) --
When the build process started, expressed in Unix time format.

endTime (datetime) --
When the build process ended, expressed in Unix time format.

currentPhase (string) --
The current build phase.

buildStatus (string) --
The current status of the build. Valid values include:

FAILED : The build failed.
FAULT : The build faulted.
IN_PROGRESS : The build is still in progress.
STOPPED : The build stopped.
SUCCEEDED : The build succeeded.
TIMED_OUT : The build timed out.


sourceVersion (string) --
Any version identifier for the version of the source code to be built. If sourceVersion is specified at the project level, then this sourceVersion (at the build level) takes precedence.
For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .

resolvedSourceVersion (string) --
An identifier for the version of this build\'s source code.

For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.
For AWS CodePipeline, the source revision provided by AWS CodePipeline.
For Amazon Simple Storage Service (Amazon S3), this does not apply.


projectName (string) --
The name of the AWS CodeBuild project.

phases (list) --
Information about all previous build phases that are complete and information about any current build phase that is not yet complete.

(dict) --
Information about a stage for a build.

phaseType (string) --
The name of the build phase. Valid values include:

BUILD : Core build activities typically occur in this build phase.
COMPLETED : The build has been completed.
DOWNLOAD_SOURCE : Source code is being downloaded in this build phase.
FINALIZING : The build process is completing in this build phase.
INSTALL : Installation activities typically occur in this build phase.
POST_BUILD : Post-build activities typically occur in this build phase.
PRE_BUILD : Pre-build activities typically occur in this build phase.
PROVISIONING : The build environment is being set up.
QUEUED : The build has been submitted and is queued behind other submitted builds.
SUBMITTED : The build has been submitted.
UPLOAD_ARTIFACTS : Build output artifacts are being uploaded to the output location.


phaseStatus (string) --
The current status of the build phase. Valid values include:

FAILED : The build phase failed.
FAULT : The build phase faulted.
IN_PROGRESS : The build phase is still in progress.
QUEUED : The build has been submitted and is queued behind other submitted builds.
STOPPED : The build phase stopped.
SUCCEEDED : The build phase succeeded.
TIMED_OUT : The build phase timed out.


startTime (datetime) --
When the build phase started, expressed in Unix time format.

endTime (datetime) --
When the build phase ended, expressed in Unix time format.

durationInSeconds (integer) --
How long, in seconds, between the starting and ending times of the build\'s phase.

contexts (list) --
Additional information about a build phase, especially to help troubleshoot a failed build.

(dict) --
Additional information about a build phase that has an error. You can use this information for troubleshooting.

statusCode (string) --
The status code for the context of the build phase.

message (string) --
An explanation of the build phase\'s context. This might include a command ID and an exit code.









source (dict) --
Information about the source code to be built.

type (string) --
The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --
Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --
Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --
Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --
Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --
The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --
Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --

Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --
The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --
Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --
Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --
An identifier for this project source.



secondarySources (list) --
An array of ProjectSource objects.

(dict) --
Information about the build input source code for the build project.

type (string) --
The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --
Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --
Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --
Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --
Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --
The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --
Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --

Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --
The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --
Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --
Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --
An identifier for this project source.





secondarySourceVersions (list) --
An array of ProjectSourceVersion objects. Each ProjectSourceVersion must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.


(dict) --
A source identifier and its corresponding version.

sourceIdentifier (string) --
An identifier for a source in the build project.

sourceVersion (string) --
The source version for the corresponding source identifier. If specified, must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.

For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .





artifacts (dict) --
Information about the output artifacts for the build.

location (string) --
Information about the location of the build artifacts.

sha256sum (string) --
The SHA-256 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


md5sum (string) --
The MD5 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


overrideArtifactName (boolean) --
If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --
Information that tells you if encryption for build artifacts is disabled.

artifactIdentifier (string) --
An identifier for this artifact definition.



secondaryArtifacts (list) --
An array of ProjectArtifacts objects.

(dict) --
Information about build output artifacts.

location (string) --
Information about the location of the build artifacts.

sha256sum (string) --
The SHA-256 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


md5sum (string) --
The MD5 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


overrideArtifactName (boolean) --
If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --
Information that tells you if encryption for build artifacts is disabled.

artifactIdentifier (string) --
An identifier for this artifact definition.





cache (dict) --
Information about the cache for the build.

type (string) --
The type of cache used by the build project. Valid values include:

NO_CACHE : The build project does not use any cache.
S3 : The build project reads and writes from and to S3.
LOCAL : The build project stores a cache locally on a build host that is only available to that build host.


location (string) --
Information about the cache location:

NO_CACHE or LOCAL : This value is ignored.
S3 : This is the S3 bucket name/prefix.


modes (list) --
If you use a LOCAL cache, the local cache mode. You can use one or more local cache modes at the same time.

LOCAL_SOURCE_CACHE mode caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.
LOCAL_DOCKER_LAYER_CACHE mode caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.


Note

You can use a Docker layer cache in the Linux environment only.
The privileged flag must be set so that your project has the required Docker permissions.
You should consider the security implications before you use a Docker layer cache.



LOCAL_CUSTOM_CACHE mode caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:
Only directories can be specified for caching. You cannot specify individual files.
Symlinks are used to reference cached directories.
Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.




(string) --




environment (dict) --
Information about the build environment for this build.

type (string) --
The type of build environment to use for related builds.

The environment type ARM_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).
The environment type LINUX_CONTAINER with compute type build.general1.2xlarge is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).
The environment type LINUX_GPU_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).


image (string) --
The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:

For an image tag: registry/repository:tag . For example, to specify an image with the tag "latest," use registry/repository:latest .
For an image digest: registry/repository@digest . For example, to specify an image with the digest "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf .


computeType (string) --
Information about the compute resources the build project uses. Available values include:

BUILD_GENERAL1_SMALL : Use up to 3 GB memory and 2 vCPUs for builds.
BUILD_GENERAL1_MEDIUM : Use up to 7 GB memory and 4 vCPUs for builds.
BUILD_GENERAL1_LARGE : Use up to 16 GB memory and 8 vCPUs for builds, depending on your environment type.
BUILD_GENERAL1_2XLARGE : Use up to 145 GB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.

If you use BUILD_GENERAL1_LARGE :

For environment type LINUX_CONTAINER , you can use up to 15 GB memory and 8 vCPUs for builds.
For environment type LINUX_GPU_CONTAINER , you can use up to 255 GB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.
For environment type ARM_CONTAINER , you can use up to 16 GB memory and 8 vCPUs on ARM-based processors for builds.

For more information, see Build Environment Compute Types in the AWS CodeBuild User Guide.

environmentVariables (list) --
A set of environment variables to make available to builds for this build project.

(dict) --
Information about an environment variable for a build project or a build.

name (string) --
The name or key of the environment variable.

value (string) --
The value of the environment variable.

Warning
We strongly discourage the use of PLAINTEXT environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. PLAINTEXT environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI). For sensitive values, we recommend you use an environment variable of type PARAMETER_STORE or SECRETS_MANAGER .


type (string) --
The type of environment variable. Valid values include:

PARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. To learn how to specify a parameter store environment variable, see parameter store reference-key in the buildspec file .
PLAINTEXT : An environment variable in plain text format. This is the default value.
SECRETS_MANAGER : An environment variable stored in AWS Secrets Manager. To learn how to specify a secrets manager environment variable, see secrets manager reference-key in the buildspec file .






privilegedMode (boolean) --
Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is false .
You can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:
If the operating system\'s base image is Ubuntu Linux:

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&
- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"

If the operating system\'s base image is Alpine Linux and the previous command does not work, add the -t argument to timeout :

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&
- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"


certificate (string) --
The certificate to use with this build project.

registryCredential (dict) --
The credentials for access to a private registry.

credential (string) --
The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

Note
The credential can use the name of the credentials only if they exist in your current AWS Region.


credentialProvider (string) --
The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.



imagePullCredentialsType (string) --
The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid values:

CODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild\'s service principal.
SERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.

When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.



serviceRole (string) --
The name of a service role used for this build.

logs (dict) --
Information about the build\'s logs in Amazon CloudWatch Logs.

groupName (string) --
The name of the Amazon CloudWatch Logs group for the build logs.

streamName (string) --
The name of the Amazon CloudWatch Logs stream for the build logs.

deepLink (string) --
The URL to an individual build log in Amazon CloudWatch Logs.

s3DeepLink (string) --
The URL to a build log in an S3 bucket.

cloudWatchLogsArn (string) --
The ARN of Amazon CloudWatch Logs for a build project. Its format is arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName} . For more information, see Resources Defined by Amazon CloudWatch Logs .

s3LogsArn (string) --
The ARN of S3 logs for a build project. Its format is arn:${Partition}:s3:::${BucketName}/${ObjectName} . For more information, see Resources Defined by Amazon S3 .

cloudWatchLogs (dict) --
Information about Amazon CloudWatch Logs for a build project.

status (string) --
The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:

ENABLED : Amazon CloudWatch Logs are enabled for this build project.
DISABLED : Amazon CloudWatch Logs are not enabled for this build project.


groupName (string) --
The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .

streamName (string) --
The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .



s3Logs (dict) --
Information about S3 logs for a build project.

status (string) --
The current status of the S3 build logs. Valid values are:

ENABLED : S3 build logs are enabled for this build project.
DISABLED : S3 build logs are not enabled for this build project.


location (string) --
The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .

encryptionDisabled (boolean) --
Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.





timeoutInMinutes (integer) --
How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.

queuedTimeoutInMinutes (integer) --
The number of minutes a build is allowed to be queued before it times out.

buildComplete (boolean) --
Whether the build is complete. True if complete; otherwise, false.

initiator (string) --
The entity that started the build. Valid values include:

If AWS CodePipeline started the build, the pipeline\'s name (for example, codepipeline/my-demo-pipeline ).
If an AWS Identity and Access Management (IAM) user started the build, the user\'s name (for example, MyUserName ).
If the Jenkins plugin for AWS CodeBuild started the build, the string CodeBuild-Jenkins-Plugin .


vpcConfig (dict) --
If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.

vpcId (string) --
The ID of the Amazon VPC.

subnets (list) --
A list of one or more subnet IDs in your Amazon VPC.

(string) --


securityGroupIds (list) --
A list of one or more security groups IDs in your Amazon VPC.

(string) --




networkInterface (dict) --
Describes a network interface.

subnetId (string) --
The ID of the subnet.

networkInterfaceId (string) --
The ID of the network interface.



encryptionKey (string) --
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

Note
You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK\'s alias (using the format ``alias/alias-name `` ).

exportedEnvironmentVariables (list) --
A list of exported environment variables for this build.

(dict) --
Information about an exported environment variable.

name (string) --
The name of this exported environment variable.

value (string) --
The value assigned to this exported environment variable.

Note
During a build, the value of a variable is available starting with the install phase. It can be updated between the start of the install phase and the end of the post_build phase. After the post_build phase ends, the value of exported variables cannot change.






reportArns (list) --
An array of the ARNs associated with this build\'s reports.

(string) --


fileSystemLocations (list) --
An array of ProjectFileSystemLocation objects for a CodeBuild build project. A ProjectFileSystemLocation object specifies the identifier , location , mountOptions , mountPoint , and type of a file system created using Amazon Elastic File System.

(dict) --
Information about a file system created by Amazon Elastic File System (EFS). For more information, see What Is Amazon Elastic File System?

type (string) --
The type of the file system. The one supported type is EFS .

location (string) --
A string that specifies the location of the file system created by Amazon EFS. Its format is efs-dns-name:/directory-path . You can find the DNS name of file system when you view it in the AWS EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is fs-abcd1234.efs.us-west-2.amazonaws.com , and its mount directory is my-efs-mount-directory , then the location is fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory .
The directory path in the format efs-dns-name:/directory-path is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.

mountPoint (string) --
The location in the container where you mount the file system.

identifier (string) --
The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the identifier in all capital letters to CODEBUILD_ . For example, if you specify my-efs for identifier , a new environment variable is create named CODEBUILD_MY-EFS .
The identifier is used to mount your file system.

mountOptions (string) --
The mount options for a file system created by AWS EFS. The default mount options used by CodeBuild are nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 . For more information, see Recommended NFS Mount Options .













Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException
CodeBuild.Client.exceptions.AccountLimitExceededException


    :return: {
        'build': {
            'id': 'string',
            'arn': 'string',
            'buildNumber': 123,
            'startTime': datetime(2015, 1, 1),
            'endTime': datetime(2015, 1, 1),
            'currentPhase': 'string',
            'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
            'sourceVersion': 'string',
            'resolvedSourceVersion': 'string',
            'projectName': 'string',
            'phases': [
                {
                    'phaseType': 'SUBMITTED'|'QUEUED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                    'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'durationInSeconds': 123,
                    'contexts': [
                        {
                            'statusCode': 'string',
                            'message': 'string'
                        },
                    ]
                },
            ],
            'source': {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
            'secondarySources': [
                {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'gitSubmodulesConfig': {
                        'fetchSubmodules': True|False
                    },
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
            ],
            'secondarySourceVersions': [
                {
                    'sourceIdentifier': 'string',
                    'sourceVersion': 'string'
                },
            ],
            'artifacts': {
                'location': 'string',
                'sha256sum': 'string',
                'md5sum': 'string',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
            'secondaryArtifacts': [
                {
                    'location': 'string',
                    'sha256sum': 'string',
                    'md5sum': 'string',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
            ],
            'cache': {
                'type': 'NO_CACHE'|'S3'|'LOCAL',
                'location': 'string',
                'modes': [
                    'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                ]
            },
            'environment': {
                'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
                'image': 'string',
                'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                'environmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                    },
                ],
                'privilegedMode': True|False,
                'certificate': 'string',
                'registryCredential': {
                    'credential': 'string',
                    'credentialProvider': 'SECRETS_MANAGER'
                },
                'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
            },
            'serviceRole': 'string',
            'logs': {
                'groupName': 'string',
                'streamName': 'string',
                'deepLink': 'string',
                's3DeepLink': 'string',
                'cloudWatchLogsArn': 'string',
                's3LogsArn': 'string',
                'cloudWatchLogs': {
                    'status': 'ENABLED'|'DISABLED',
                    'groupName': 'string',
                    'streamName': 'string'
                },
                's3Logs': {
                    'status': 'ENABLED'|'DISABLED',
                    'location': 'string',
                    'encryptionDisabled': True|False
                }
            },
            'timeoutInMinutes': 123,
            'queuedTimeoutInMinutes': 123,
            'buildComplete': True|False,
            'initiator': 'string',
            'vpcConfig': {
                'vpcId': 'string',
                'subnets': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ]
            },
            'networkInterface': {
                'subnetId': 'string',
                'networkInterfaceId': 'string'
            },
            'encryptionKey': 'string',
            'exportedEnvironmentVariables': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ],
            'reportArns': [
                'string',
            ],
            'fileSystemLocations': [
                {
                    'type': 'EFS',
                    'location': 'string',
                    'mountPoint': 'string',
                    'identifier': 'string',
                    'mountOptions': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    FAILED : The build failed.
    FAULT : The build faulted.
    IN_PROGRESS : The build is still in progress.
    STOPPED : The build stopped.
    SUCCEEDED : The build succeeded.
    TIMED_OUT : The build timed out.
    
    """
    pass

def stop_build(id=None):
    """
    Attempts to stop running a build.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_build(
        id='string'
    )
    
    
    :type id: string
    :param id: [REQUIRED]\nThe ID of the build.\n

    :rtype: dict
ReturnsResponse Syntax{
    'build': {
        'id': 'string',
        'arn': 'string',
        'buildNumber': 123,
        'startTime': datetime(2015, 1, 1),
        'endTime': datetime(2015, 1, 1),
        'currentPhase': 'string',
        'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
        'sourceVersion': 'string',
        'resolvedSourceVersion': 'string',
        'projectName': 'string',
        'phases': [
            {
                'phaseType': 'SUBMITTED'|'QUEUED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'durationInSeconds': 123,
                'contexts': [
                    {
                        'statusCode': 'string',
                        'message': 'string'
                    },
                ]
            },
        ],
        'source': {
            'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
            'location': 'string',
            'gitCloneDepth': 123,
            'gitSubmodulesConfig': {
                'fetchSubmodules': True|False
            },
            'buildspec': 'string',
            'auth': {
                'type': 'OAUTH',
                'resource': 'string'
            },
            'reportBuildStatus': True|False,
            'insecureSsl': True|False,
            'sourceIdentifier': 'string'
        },
        'secondarySources': [
            {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
        ],
        'secondarySourceVersions': [
            {
                'sourceIdentifier': 'string',
                'sourceVersion': 'string'
            },
        ],
        'artifacts': {
            'location': 'string',
            'sha256sum': 'string',
            'md5sum': 'string',
            'overrideArtifactName': True|False,
            'encryptionDisabled': True|False,
            'artifactIdentifier': 'string'
        },
        'secondaryArtifacts': [
            {
                'location': 'string',
                'sha256sum': 'string',
                'md5sum': 'string',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
        ],
        'cache': {
            'type': 'NO_CACHE'|'S3'|'LOCAL',
            'location': 'string',
            'modes': [
                'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
            ]
        },
        'environment': {
            'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
            'image': 'string',
            'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
            'environmentVariables': [
                {
                    'name': 'string',
                    'value': 'string',
                    'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                },
            ],
            'privilegedMode': True|False,
            'certificate': 'string',
            'registryCredential': {
                'credential': 'string',
                'credentialProvider': 'SECRETS_MANAGER'
            },
            'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
        },
        'serviceRole': 'string',
        'logs': {
            'groupName': 'string',
            'streamName': 'string',
            'deepLink': 'string',
            's3DeepLink': 'string',
            'cloudWatchLogsArn': 'string',
            's3LogsArn': 'string',
            'cloudWatchLogs': {
                'status': 'ENABLED'|'DISABLED',
                'groupName': 'string',
                'streamName': 'string'
            },
            's3Logs': {
                'status': 'ENABLED'|'DISABLED',
                'location': 'string',
                'encryptionDisabled': True|False
            }
        },
        'timeoutInMinutes': 123,
        'queuedTimeoutInMinutes': 123,
        'buildComplete': True|False,
        'initiator': 'string',
        'vpcConfig': {
            'vpcId': 'string',
            'subnets': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ]
        },
        'networkInterface': {
            'subnetId': 'string',
            'networkInterfaceId': 'string'
        },
        'encryptionKey': 'string',
        'exportedEnvironmentVariables': [
            {
                'name': 'string',
                'value': 'string'
            },
        ],
        'reportArns': [
            'string',
        ],
        'fileSystemLocations': [
            {
                'type': 'EFS',
                'location': 'string',
                'mountPoint': 'string',
                'identifier': 'string',
                'mountOptions': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
build (dict) --Information about the build.

id (string) --The unique ID for the build.

arn (string) --The Amazon Resource Name (ARN) of the build.

buildNumber (integer) --The number of the build. For each project, the buildNumber of its first build is 1 . The buildNumber of each subsequent build is incremented by 1 . If a build is deleted, the buildNumber of other builds does not change.

startTime (datetime) --When the build process started, expressed in Unix time format.

endTime (datetime) --When the build process ended, expressed in Unix time format.

currentPhase (string) --The current build phase.

buildStatus (string) --The current status of the build. Valid values include:

FAILED : The build failed.
FAULT : The build faulted.
IN_PROGRESS : The build is still in progress.
STOPPED : The build stopped.
SUCCEEDED : The build succeeded.
TIMED_OUT : The build timed out.


sourceVersion (string) --Any version identifier for the version of the source code to be built. If sourceVersion is specified at the project level, then this sourceVersion (at the build level) takes precedence.
For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .

resolvedSourceVersion (string) --An identifier for the version of this build\'s source code.

For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.
For AWS CodePipeline, the source revision provided by AWS CodePipeline.
For Amazon Simple Storage Service (Amazon S3), this does not apply.


projectName (string) --The name of the AWS CodeBuild project.

phases (list) --Information about all previous build phases that are complete and information about any current build phase that is not yet complete.

(dict) --Information about a stage for a build.

phaseType (string) --The name of the build phase. Valid values include:

BUILD : Core build activities typically occur in this build phase.
COMPLETED : The build has been completed.
DOWNLOAD_SOURCE : Source code is being downloaded in this build phase.
FINALIZING : The build process is completing in this build phase.
INSTALL : Installation activities typically occur in this build phase.
POST_BUILD : Post-build activities typically occur in this build phase.
PRE_BUILD : Pre-build activities typically occur in this build phase.
PROVISIONING : The build environment is being set up.
QUEUED : The build has been submitted and is queued behind other submitted builds.
SUBMITTED : The build has been submitted.
UPLOAD_ARTIFACTS : Build output artifacts are being uploaded to the output location.


phaseStatus (string) --The current status of the build phase. Valid values include:

FAILED : The build phase failed.
FAULT : The build phase faulted.
IN_PROGRESS : The build phase is still in progress.
QUEUED : The build has been submitted and is queued behind other submitted builds.
STOPPED : The build phase stopped.
SUCCEEDED : The build phase succeeded.
TIMED_OUT : The build phase timed out.


startTime (datetime) --When the build phase started, expressed in Unix time format.

endTime (datetime) --When the build phase ended, expressed in Unix time format.

durationInSeconds (integer) --How long, in seconds, between the starting and ending times of the build\'s phase.

contexts (list) --Additional information about a build phase, especially to help troubleshoot a failed build.

(dict) --Additional information about a build phase that has an error. You can use this information for troubleshooting.

statusCode (string) --The status code for the context of the build phase.

message (string) --An explanation of the build phase\'s context. This might include a command ID and an exit code.









source (dict) --Information about the source code to be built.

type (string) --The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --
Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --An identifier for this project source.



secondarySources (list) --An array of ProjectSource objects.

(dict) --Information about the build input source code for the build project.

type (string) --The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --
Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --An identifier for this project source.





secondarySourceVersions (list) --An array of ProjectSourceVersion objects. Each ProjectSourceVersion must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.


(dict) --A source identifier and its corresponding version.

sourceIdentifier (string) --An identifier for a source in the build project.

sourceVersion (string) --The source version for the corresponding source identifier. If specified, must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.

For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .





artifacts (dict) --Information about the output artifacts for the build.

location (string) --Information about the location of the build artifacts.

sha256sum (string) --The SHA-256 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


md5sum (string) --The MD5 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


overrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --Information that tells you if encryption for build artifacts is disabled.

artifactIdentifier (string) --An identifier for this artifact definition.



secondaryArtifacts (list) --An array of ProjectArtifacts objects.

(dict) --Information about build output artifacts.

location (string) --Information about the location of the build artifacts.

sha256sum (string) --The SHA-256 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


md5sum (string) --The MD5 hash of the build artifact.
You can use this hash along with a checksum tool to confirm file integrity and authenticity.

Note
This value is available only if the build project\'s packaging value is set to ZIP .


overrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --Information that tells you if encryption for build artifacts is disabled.

artifactIdentifier (string) --An identifier for this artifact definition.





cache (dict) --Information about the cache for the build.

type (string) --The type of cache used by the build project. Valid values include:

NO_CACHE : The build project does not use any cache.
S3 : The build project reads and writes from and to S3.
LOCAL : The build project stores a cache locally on a build host that is only available to that build host.


location (string) --Information about the cache location:

NO_CACHE or LOCAL : This value is ignored.
S3 : This is the S3 bucket name/prefix.


modes (list) --If you use a LOCAL cache, the local cache mode. You can use one or more local cache modes at the same time.

LOCAL_SOURCE_CACHE mode caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.
LOCAL_DOCKER_LAYER_CACHE mode caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.


Note

You can use a Docker layer cache in the Linux environment only.
The privileged flag must be set so that your project has the required Docker permissions.
You should consider the security implications before you use a Docker layer cache.



LOCAL_CUSTOM_CACHE mode caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:
Only directories can be specified for caching. You cannot specify individual files.
Symlinks are used to reference cached directories.
Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.




(string) --




environment (dict) --Information about the build environment for this build.

type (string) --The type of build environment to use for related builds.

The environment type ARM_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).
The environment type LINUX_CONTAINER with compute type build.general1.2xlarge is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).
The environment type LINUX_GPU_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).


image (string) --The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:

For an image tag: registry/repository:tag . For example, to specify an image with the tag "latest," use registry/repository:latest .
For an image digest: registry/repository@digest . For example, to specify an image with the digest "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf .


computeType (string) --Information about the compute resources the build project uses. Available values include:

BUILD_GENERAL1_SMALL : Use up to 3 GB memory and 2 vCPUs for builds.
BUILD_GENERAL1_MEDIUM : Use up to 7 GB memory and 4 vCPUs for builds.
BUILD_GENERAL1_LARGE : Use up to 16 GB memory and 8 vCPUs for builds, depending on your environment type.
BUILD_GENERAL1_2XLARGE : Use up to 145 GB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.

If you use BUILD_GENERAL1_LARGE :

For environment type LINUX_CONTAINER , you can use up to 15 GB memory and 8 vCPUs for builds.
For environment type LINUX_GPU_CONTAINER , you can use up to 255 GB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.
For environment type ARM_CONTAINER , you can use up to 16 GB memory and 8 vCPUs on ARM-based processors for builds.

For more information, see Build Environment Compute Types in the AWS CodeBuild User Guide.

environmentVariables (list) --A set of environment variables to make available to builds for this build project.

(dict) --Information about an environment variable for a build project or a build.

name (string) --The name or key of the environment variable.

value (string) --The value of the environment variable.

Warning
We strongly discourage the use of PLAINTEXT environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. PLAINTEXT environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI). For sensitive values, we recommend you use an environment variable of type PARAMETER_STORE or SECRETS_MANAGER .


type (string) --The type of environment variable. Valid values include:

PARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. To learn how to specify a parameter store environment variable, see parameter store reference-key in the buildspec file .
PLAINTEXT : An environment variable in plain text format. This is the default value.
SECRETS_MANAGER : An environment variable stored in AWS Secrets Manager. To learn how to specify a secrets manager environment variable, see secrets manager reference-key in the buildspec file .






privilegedMode (boolean) --Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is false .
You can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:
If the operating system\'s base image is Ubuntu Linux:

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"

If the operating system\'s base image is Alpine Linux and the previous command does not work, add the -t argument to timeout :

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"


certificate (string) --The certificate to use with this build project.

registryCredential (dict) --The credentials for access to a private registry.

credential (string) --The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

Note
The credential can use the name of the credentials only if they exist in your current AWS Region.


credentialProvider (string) --The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.



imagePullCredentialsType (string) --The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid values:

CODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild\'s service principal.
SERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.

When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.



serviceRole (string) --The name of a service role used for this build.

logs (dict) --Information about the build\'s logs in Amazon CloudWatch Logs.

groupName (string) --The name of the Amazon CloudWatch Logs group for the build logs.

streamName (string) --The name of the Amazon CloudWatch Logs stream for the build logs.

deepLink (string) --The URL to an individual build log in Amazon CloudWatch Logs.

s3DeepLink (string) --The URL to a build log in an S3 bucket.

cloudWatchLogsArn (string) --The ARN of Amazon CloudWatch Logs for a build project. Its format is arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName} . For more information, see Resources Defined by Amazon CloudWatch Logs .

s3LogsArn (string) --The ARN of S3 logs for a build project. Its format is arn:${Partition}:s3:::${BucketName}/${ObjectName} . For more information, see Resources Defined by Amazon S3 .

cloudWatchLogs (dict) --Information about Amazon CloudWatch Logs for a build project.

status (string) --The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:

ENABLED : Amazon CloudWatch Logs are enabled for this build project.
DISABLED : Amazon CloudWatch Logs are not enabled for this build project.


groupName (string) --The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .

streamName (string) --The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .



s3Logs (dict) --Information about S3 logs for a build project.

status (string) --The current status of the S3 build logs. Valid values are:

ENABLED : S3 build logs are enabled for this build project.
DISABLED : S3 build logs are not enabled for this build project.


location (string) --The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .

encryptionDisabled (boolean) --Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.





timeoutInMinutes (integer) --How long, in minutes, for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.

queuedTimeoutInMinutes (integer) --The number of minutes a build is allowed to be queued before it times out.

buildComplete (boolean) --Whether the build is complete. True if complete; otherwise, false.

initiator (string) --The entity that started the build. Valid values include:

If AWS CodePipeline started the build, the pipeline\'s name (for example, codepipeline/my-demo-pipeline ).
If an AWS Identity and Access Management (IAM) user started the build, the user\'s name (for example, MyUserName ).
If the Jenkins plugin for AWS CodeBuild started the build, the string CodeBuild-Jenkins-Plugin .


vpcConfig (dict) --If your AWS CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.

vpcId (string) --The ID of the Amazon VPC.

subnets (list) --A list of one or more subnet IDs in your Amazon VPC.

(string) --


securityGroupIds (list) --A list of one or more security groups IDs in your Amazon VPC.

(string) --




networkInterface (dict) --Describes a network interface.

subnetId (string) --The ID of the subnet.

networkInterfaceId (string) --The ID of the network interface.



encryptionKey (string) --The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

Note
You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK\'s alias (using the format ``alias/alias-name `` ).

exportedEnvironmentVariables (list) --A list of exported environment variables for this build.

(dict) --Information about an exported environment variable.

name (string) --The name of this exported environment variable.

value (string) --The value assigned to this exported environment variable.

Note
During a build, the value of a variable is available starting with the install phase. It can be updated between the start of the install phase and the end of the post_build phase. After the post_build phase ends, the value of exported variables cannot change.






reportArns (list) --An array of the ARNs associated with this build\'s reports.

(string) --


fileSystemLocations (list) --An array of ProjectFileSystemLocation objects for a CodeBuild build project. A ProjectFileSystemLocation object specifies the identifier , location , mountOptions , mountPoint , and type of a file system created using Amazon Elastic File System.

(dict) --Information about a file system created by Amazon Elastic File System (EFS). For more information, see What Is Amazon Elastic File System?

type (string) --The type of the file system. The one supported type is EFS .

location (string) --A string that specifies the location of the file system created by Amazon EFS. Its format is efs-dns-name:/directory-path . You can find the DNS name of file system when you view it in the AWS EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is fs-abcd1234.efs.us-west-2.amazonaws.com , and its mount directory is my-efs-mount-directory , then the location is fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory .
The directory path in the format efs-dns-name:/directory-path is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.

mountPoint (string) --The location in the container where you mount the file system.

identifier (string) --The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the identifier in all capital letters to CODEBUILD_ . For example, if you specify my-efs for identifier , a new environment variable is create named CODEBUILD_MY-EFS .
The identifier is used to mount your file system.

mountOptions (string) --The mount options for a file system created by AWS EFS. The default mount options used by CodeBuild are nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 . For more information, see Recommended NFS Mount Options .












Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException


    :return: {
        'build': {
            'id': 'string',
            'arn': 'string',
            'buildNumber': 123,
            'startTime': datetime(2015, 1, 1),
            'endTime': datetime(2015, 1, 1),
            'currentPhase': 'string',
            'buildStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
            'sourceVersion': 'string',
            'resolvedSourceVersion': 'string',
            'projectName': 'string',
            'phases': [
                {
                    'phaseType': 'SUBMITTED'|'QUEUED'|'PROVISIONING'|'DOWNLOAD_SOURCE'|'INSTALL'|'PRE_BUILD'|'BUILD'|'POST_BUILD'|'UPLOAD_ARTIFACTS'|'FINALIZING'|'COMPLETED',
                    'phaseStatus': 'SUCCEEDED'|'FAILED'|'FAULT'|'TIMED_OUT'|'IN_PROGRESS'|'STOPPED',
                    'startTime': datetime(2015, 1, 1),
                    'endTime': datetime(2015, 1, 1),
                    'durationInSeconds': 123,
                    'contexts': [
                        {
                            'statusCode': 'string',
                            'message': 'string'
                        },
                    ]
                },
            ],
            'source': {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
            'secondarySources': [
                {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'gitSubmodulesConfig': {
                        'fetchSubmodules': True|False
                    },
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
            ],
            'secondarySourceVersions': [
                {
                    'sourceIdentifier': 'string',
                    'sourceVersion': 'string'
                },
            ],
            'artifacts': {
                'location': 'string',
                'sha256sum': 'string',
                'md5sum': 'string',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
            'secondaryArtifacts': [
                {
                    'location': 'string',
                    'sha256sum': 'string',
                    'md5sum': 'string',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
            ],
            'cache': {
                'type': 'NO_CACHE'|'S3'|'LOCAL',
                'location': 'string',
                'modes': [
                    'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                ]
            },
            'environment': {
                'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
                'image': 'string',
                'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                'environmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                    },
                ],
                'privilegedMode': True|False,
                'certificate': 'string',
                'registryCredential': {
                    'credential': 'string',
                    'credentialProvider': 'SECRETS_MANAGER'
                },
                'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
            },
            'serviceRole': 'string',
            'logs': {
                'groupName': 'string',
                'streamName': 'string',
                'deepLink': 'string',
                's3DeepLink': 'string',
                'cloudWatchLogsArn': 'string',
                's3LogsArn': 'string',
                'cloudWatchLogs': {
                    'status': 'ENABLED'|'DISABLED',
                    'groupName': 'string',
                    'streamName': 'string'
                },
                's3Logs': {
                    'status': 'ENABLED'|'DISABLED',
                    'location': 'string',
                    'encryptionDisabled': True|False
                }
            },
            'timeoutInMinutes': 123,
            'queuedTimeoutInMinutes': 123,
            'buildComplete': True|False,
            'initiator': 'string',
            'vpcConfig': {
                'vpcId': 'string',
                'subnets': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ]
            },
            'networkInterface': {
                'subnetId': 'string',
                'networkInterfaceId': 'string'
            },
            'encryptionKey': 'string',
            'exportedEnvironmentVariables': [
                {
                    'name': 'string',
                    'value': 'string'
                },
            ],
            'reportArns': [
                'string',
            ],
            'fileSystemLocations': [
                {
                    'type': 'EFS',
                    'location': 'string',
                    'mountPoint': 'string',
                    'identifier': 'string',
                    'mountOptions': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    For AWS CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.
    For AWS CodePipeline, the source revision provided by AWS CodePipeline.
    For Amazon Simple Storage Service (Amazon S3), this does not apply.
    
    """
    pass

def update_project(name=None, description=None, source=None, secondarySources=None, sourceVersion=None, secondarySourceVersions=None, artifacts=None, secondaryArtifacts=None, cache=None, environment=None, serviceRole=None, timeoutInMinutes=None, queuedTimeoutInMinutes=None, encryptionKey=None, tags=None, vpcConfig=None, badgeEnabled=None, logsConfig=None, fileSystemLocations=None):
    """
    Changes the settings of a build project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_project(
        name='string',
        description='string',
        source={
            'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
            'location': 'string',
            'gitCloneDepth': 123,
            'gitSubmodulesConfig': {
                'fetchSubmodules': True|False
            },
            'buildspec': 'string',
            'auth': {
                'type': 'OAUTH',
                'resource': 'string'
            },
            'reportBuildStatus': True|False,
            'insecureSsl': True|False,
            'sourceIdentifier': 'string'
        },
        secondarySources=[
            {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
        ],
        sourceVersion='string',
        secondarySourceVersions=[
            {
                'sourceIdentifier': 'string',
                'sourceVersion': 'string'
            },
        ],
        artifacts={
            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
            'location': 'string',
            'path': 'string',
            'namespaceType': 'NONE'|'BUILD_ID',
            'name': 'string',
            'packaging': 'NONE'|'ZIP',
            'overrideArtifactName': True|False,
            'encryptionDisabled': True|False,
            'artifactIdentifier': 'string'
        },
        secondaryArtifacts=[
            {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
        ],
        cache={
            'type': 'NO_CACHE'|'S3'|'LOCAL',
            'location': 'string',
            'modes': [
                'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
            ]
        },
        environment={
            'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
            'image': 'string',
            'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
            'environmentVariables': [
                {
                    'name': 'string',
                    'value': 'string',
                    'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                },
            ],
            'privilegedMode': True|False,
            'certificate': 'string',
            'registryCredential': {
                'credential': 'string',
                'credentialProvider': 'SECRETS_MANAGER'
            },
            'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
        },
        serviceRole='string',
        timeoutInMinutes=123,
        queuedTimeoutInMinutes=123,
        encryptionKey='string',
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        vpcConfig={
            'vpcId': 'string',
            'subnets': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ]
        },
        badgeEnabled=True|False,
        logsConfig={
            'cloudWatchLogs': {
                'status': 'ENABLED'|'DISABLED',
                'groupName': 'string',
                'streamName': 'string'
            },
            's3Logs': {
                'status': 'ENABLED'|'DISABLED',
                'location': 'string',
                'encryptionDisabled': True|False
            }
        },
        fileSystemLocations=[
            {
                'type': 'EFS',
                'location': 'string',
                'mountPoint': 'string',
                'identifier': 'string',
                'mountOptions': 'string'
            },
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe name of the build project.\n\nNote\nYou cannot change a build project\'s name.\n\n

    :type description: string
    :param description: A new or replacement description of the build project.

    :type source: dict
    :param source: Information to be changed about the build input source code for the build project.\n\ntype (string) -- [REQUIRED]The type of repository that contains the source code to be built. Valid values include:\n\nBITBUCKET : The source code is in a Bitbucket repository.\nCODECOMMIT : The source code is in an AWS CodeCommit repository.\nCODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.\nGITHUB : The source code is in a GitHub repository.\nGITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.\nNO_SOURCE : The project does not have input source code.\nS3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.\n\n\nlocation (string) --Information about the location of the source code to be built. Valid values include:\n\nFor source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.\nFor source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).\nFor source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.\nThe path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).\nThe path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).\n\n\nFor source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .\nFor source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .\n\n\ngitCloneDepth (integer) --Information about the Git clone depth for the build project.\n\ngitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.\n\nfetchSubmodules (boolean) -- [REQUIRED]Set to true to fetch Git submodules for your AWS CodeBuild build project.\n\n\n\nbuildspec (string) --The buildspec file declaration to use for the builds in this build project.\nIf this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .\n\nauth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.\nThis information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.\n\ntype (string) -- [REQUIRED]\nNote\nThis data type is deprecated and is no longer accurate or used.\n\nThe authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.\n\nresource (string) --The resource value that applies to the specified authorization type.\n\n\n\nreportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.\n\nNote\nThe status of a build triggered by a webhook is always reported to your source provider.\n\n\ninsecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.\n\nsourceIdentifier (string) --An identifier for this project source.\n\n\n

    :type secondarySources: list
    :param secondarySources: An array of ProjectSource objects.\n\n(dict) --Information about the build input source code for the build project.\n\ntype (string) -- [REQUIRED]The type of repository that contains the source code to be built. Valid values include:\n\nBITBUCKET : The source code is in a Bitbucket repository.\nCODECOMMIT : The source code is in an AWS CodeCommit repository.\nCODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.\nGITHUB : The source code is in a GitHub repository.\nGITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.\nNO_SOURCE : The project does not have input source code.\nS3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.\n\n\nlocation (string) --Information about the location of the source code to be built. Valid values include:\n\nFor source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.\nFor source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).\nFor source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.\nThe path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).\nThe path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).\n\n\nFor source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .\nFor source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .\n\n\ngitCloneDepth (integer) --Information about the Git clone depth for the build project.\n\ngitSubmodulesConfig (dict) --Information about the Git submodules configuration for the build project.\n\nfetchSubmodules (boolean) -- [REQUIRED]Set to true to fetch Git submodules for your AWS CodeBuild build project.\n\n\n\nbuildspec (string) --The buildspec file declaration to use for the builds in this build project.\nIf this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .\n\nauth (dict) --Information about the authorization settings for AWS CodeBuild to access the source code to be built.\nThis information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.\n\ntype (string) -- [REQUIRED]\nNote\nThis data type is deprecated and is no longer accurate or used.\n\nThe authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.\n\nresource (string) --The resource value that applies to the specified authorization type.\n\n\n\nreportBuildStatus (boolean) --Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.\n\nNote\nThe status of a build triggered by a webhook is always reported to your source provider.\n\n\ninsecureSsl (boolean) --Enable this flag to ignore SSL warnings while connecting to the project source code.\n\nsourceIdentifier (string) --An identifier for this project source.\n\n\n\n\n

    :type sourceVersion: string
    :param sourceVersion: A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of:\n\nFor AWS CodeCommit: the commit ID, branch, or Git tag to use.\nFor GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.\n\nIf sourceVersion is specified at the build level, then that version takes precedence over this sourceVersion (at the project level).\nFor more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .\n

    :type secondarySourceVersions: list
    :param secondarySourceVersions: An array of ProjectSourceVersion objects. If secondarySourceVersions is specified at the build level, then they take over these secondarySourceVersions (at the project level).\n\n(dict) --A source identifier and its corresponding version.\n\nsourceIdentifier (string) -- [REQUIRED]An identifier for a source in the build project.\n\nsourceVersion (string) -- [REQUIRED]The source version for the corresponding source identifier. If specified, must be one of:\n\nFor AWS CodeCommit: the commit ID, branch, or Git tag to use.\nFor GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.\nFor Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.\n\nFor more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .\n\n\n\n\n

    :type artifacts: dict
    :param artifacts: Information to be changed about the build output artifacts for the build project.\n\ntype (string) -- [REQUIRED]The type of build output artifact. Valid values include:\n\nCODEPIPELINE : The build project has build output generated through AWS CodePipeline.\n\n\nNote\nThe CODEPIPELINE type is not supported for secondaryArtifacts .\n\n\nNO_ARTIFACTS : The build project does not produce any build output.\nS3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).\n\n\nlocation (string) --Information about the build output artifact location:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output bucket.\n\n\npath (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.\n\nFor example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .\n\nnamespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nBUILD_ID : Include the build ID in the location of the build output artifact.\nNONE : Do not include the build ID. This is the default if namespaceType is not specified.\n\n\n\nFor example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\n\nname (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.\n\nFor example:\n\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\nIf path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .\n\n\npackaging (string) --The type of build output artifact to create:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nNONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.\nZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.\n\n\n\n\noverrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.\n\nencryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.\n\nartifactIdentifier (string) --An identifier for this artifact definition.\n\n\n

    :type secondaryArtifacts: list
    :param secondaryArtifacts: An array of ProjectSource objects.\n\n(dict) --Information about the build output artifacts for the build project.\n\ntype (string) -- [REQUIRED]The type of build output artifact. Valid values include:\n\nCODEPIPELINE : The build project has build output generated through AWS CodePipeline.\n\n\nNote\nThe CODEPIPELINE type is not supported for secondaryArtifacts .\n\n\nNO_ARTIFACTS : The build project does not produce any build output.\nS3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).\n\n\nlocation (string) --Information about the build output artifact location:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output bucket.\n\n\npath (string) --Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.\n\nFor example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .\n\nnamespaceType (string) --Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nBUILD_ID : Include the build ID in the location of the build output artifact.\nNONE : Do not include the build ID. This is the default if namespaceType is not specified.\n\n\n\nFor example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\n\nname (string) --Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ('/'), the artifact is stored in the root of the output bucket.\n\nFor example:\n\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .\nIf path is empty, namespaceType is set to NONE , and name is set to '/ ', the output artifact is stored in the root of the output bucket.\nIf path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to '/ ', the output artifact is stored in ``MyArtifacts/build-ID `` .\n\n\npackaging (string) --The type of build output artifact to create:\n\nIf type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.\nIf type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.\nIf type is set to S3 , valid values include:\nNONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.\nZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.\n\n\n\n\noverrideArtifactName (boolean) --If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.\n\nencryptionDisabled (boolean) --Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.\n\nartifactIdentifier (string) --An identifier for this artifact definition.\n\n\n\n\n

    :type cache: dict
    :param cache: Stores recently used information so that it can be quickly accessed at a later time.\n\ntype (string) -- [REQUIRED]The type of cache used by the build project. Valid values include:\n\nNO_CACHE : The build project does not use any cache.\nS3 : The build project reads and writes from and to S3.\nLOCAL : The build project stores a cache locally on a build host that is only available to that build host.\n\n\nlocation (string) --Information about the cache location:\n\nNO_CACHE or LOCAL : This value is ignored.\nS3 : This is the S3 bucket name/prefix.\n\n\nmodes (list) --If you use a LOCAL cache, the local cache mode. You can use one or more local cache modes at the same time.\n\nLOCAL_SOURCE_CACHE mode caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.\nLOCAL_DOCKER_LAYER_CACHE mode caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.\n\n\nNote\n\nYou can use a Docker layer cache in the Linux environment only.\nThe privileged flag must be set so that your project has the required Docker permissions.\nYou should consider the security implications before you use a Docker layer cache.\n\n\n\nLOCAL_CUSTOM_CACHE mode caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:\nOnly directories can be specified for caching. You cannot specify individual files.\nSymlinks are used to reference cached directories.\nCached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.\n\n\n\n\n(string) --\n\n\n\n

    :type environment: dict
    :param environment: Information to be changed about the build environment for the build project.\n\ntype (string) -- [REQUIRED]The type of build environment to use for related builds.\n\nThe environment type ARM_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).\nThe environment type LINUX_CONTAINER with compute type build.general1.2xlarge is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).\nThe environment type LINUX_GPU_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).\n\n\nimage (string) -- [REQUIRED]The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:\n\nFor an image tag: registry/repository:tag . For example, to specify an image with the tag 'latest,' use registry/repository:latest .\nFor an image digest: registry/repository@digest . For example, to specify an image with the digest 'sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf,' use registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf .\n\n\ncomputeType (string) -- [REQUIRED]Information about the compute resources the build project uses. Available values include:\n\nBUILD_GENERAL1_SMALL : Use up to 3 GB memory and 2 vCPUs for builds.\nBUILD_GENERAL1_MEDIUM : Use up to 7 GB memory and 4 vCPUs for builds.\nBUILD_GENERAL1_LARGE : Use up to 16 GB memory and 8 vCPUs for builds, depending on your environment type.\nBUILD_GENERAL1_2XLARGE : Use up to 145 GB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.\n\nIf you use BUILD_GENERAL1_LARGE :\n\nFor environment type LINUX_CONTAINER , you can use up to 15 GB memory and 8 vCPUs for builds.\nFor environment type LINUX_GPU_CONTAINER , you can use up to 255 GB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.\nFor environment type ARM_CONTAINER , you can use up to 16 GB memory and 8 vCPUs on ARM-based processors for builds.\n\nFor more information, see Build Environment Compute Types in the AWS CodeBuild User Guide.\n\nenvironmentVariables (list) --A set of environment variables to make available to builds for this build project.\n\n(dict) --Information about an environment variable for a build project or a build.\n\nname (string) -- [REQUIRED]The name or key of the environment variable.\n\nvalue (string) -- [REQUIRED]The value of the environment variable.\n\nWarning\nWe strongly discourage the use of PLAINTEXT environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. PLAINTEXT environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI). For sensitive values, we recommend you use an environment variable of type PARAMETER_STORE or SECRETS_MANAGER .\n\n\ntype (string) --The type of environment variable. Valid values include:\n\nPARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. To learn how to specify a parameter store environment variable, see parameter store reference-key in the buildspec file .\nPLAINTEXT : An environment variable in plain text format. This is the default value.\nSECRETS_MANAGER : An environment variable stored in AWS Secrets Manager. To learn how to specify a secrets manager environment variable, see secrets manager reference-key in the buildspec file .\n\n\n\n\n\n\nprivilegedMode (boolean) --Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is false .\nYou can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:\nIf the operating system\'s base image is Ubuntu Linux:\n\n- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&- timeout 15 sh -c 'until docker info; do echo .; sleep 1; done'\n\nIf the operating system\'s base image is Alpine Linux and the previous command does not work, add the -t argument to timeout :\n\n- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&- timeout -t 15 sh -c 'until docker info; do echo .; sleep 1; done'\n\n\ncertificate (string) --The certificate to use with this build project.\n\nregistryCredential (dict) --The credentials for access to a private registry.\n\ncredential (string) -- [REQUIRED]The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.\n\nNote\nThe credential can use the name of the credentials only if they exist in your current AWS Region.\n\n\ncredentialProvider (string) -- [REQUIRED]The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.\n\n\n\nimagePullCredentialsType (string) --The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid values:\n\nCODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild\'s service principal.\nSERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.\n\nWhen you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.\n\n\n

    :type serviceRole: string
    :param serviceRole: The replacement ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

    :type timeoutInMinutes: integer
    :param timeoutInMinutes: The replacement value in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed.

    :type queuedTimeoutInMinutes: integer
    :param queuedTimeoutInMinutes: The number of minutes a build is allowed to be queued before it times out.

    :type encryptionKey: string
    :param encryptionKey: The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.\n\nNote\nYou can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.\n\nYou can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK\'s alias (using the format ``alias/alias-name `` ).\n

    :type tags: list
    :param tags: An updated list of tag key and value pairs associated with this build project.\nThese tags are available for use by AWS services that support AWS CodeBuild build project tags.\n\n(dict) --A tag, consisting of a key and a value.\nThis tag is available for use by AWS services that support tags in AWS CodeBuild.\n\nkey (string) --The tag\'s key.\n\nvalue (string) --The tag\'s value.\n\n\n\n\n

    :type vpcConfig: dict
    :param vpcConfig: VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.\n\nvpcId (string) --The ID of the Amazon VPC.\n\nsubnets (list) --A list of one or more subnet IDs in your Amazon VPC.\n\n(string) --\n\n\nsecurityGroupIds (list) --A list of one or more security groups IDs in your Amazon VPC.\n\n(string) --\n\n\n\n

    :type badgeEnabled: boolean
    :param badgeEnabled: Set this to true to generate a publicly accessible URL for your project\'s build badge.

    :type logsConfig: dict
    :param logsConfig: Information about logs for the build project. A project can create logs in Amazon CloudWatch Logs, logs in an S3 bucket, or both.\n\ncloudWatchLogs (dict) --Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default.\n\nstatus (string) -- [REQUIRED]The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:\n\nENABLED : Amazon CloudWatch Logs are enabled for this build project.\nDISABLED : Amazon CloudWatch Logs are not enabled for this build project.\n\n\ngroupName (string) --The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .\n\nstreamName (string) --The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .\n\n\n\ns3Logs (dict) --Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.\n\nstatus (string) -- [REQUIRED]The current status of the S3 build logs. Valid values are:\n\nENABLED : S3 build logs are enabled for this build project.\nDISABLED : S3 build logs are not enabled for this build project.\n\n\nlocation (string) --The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .\n\nencryptionDisabled (boolean) --Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.\n\n\n\n\n

    :type fileSystemLocations: list
    :param fileSystemLocations: An array of ProjectFileSystemLocation objects for a CodeBuild build project. A ProjectFileSystemLocation object specifies the identifier , location , mountOptions , mountPoint , and type of a file system created using Amazon Elastic File System.\n\n(dict) --Information about a file system created by Amazon Elastic File System (EFS). For more information, see What Is Amazon Elastic File System?\n\ntype (string) --The type of the file system. The one supported type is EFS .\n\nlocation (string) --A string that specifies the location of the file system created by Amazon EFS. Its format is efs-dns-name:/directory-path . You can find the DNS name of file system when you view it in the AWS EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is fs-abcd1234.efs.us-west-2.amazonaws.com , and its mount directory is my-efs-mount-directory , then the location is fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory .\nThe directory path in the format efs-dns-name:/directory-path is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.\n\nmountPoint (string) --The location in the container where you mount the file system.\n\nidentifier (string) --The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the identifier in all capital letters to CODEBUILD_ . For example, if you specify my-efs for identifier , a new environment variable is create named CODEBUILD_MY-EFS .\nThe identifier is used to mount your file system.\n\nmountOptions (string) --The mount options for a file system created by AWS EFS. The default mount options used by CodeBuild are nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 . For more information, see Recommended NFS Mount Options .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'project': {
        'name': 'string',
        'arn': 'string',
        'description': 'string',
        'source': {
            'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
            'location': 'string',
            'gitCloneDepth': 123,
            'gitSubmodulesConfig': {
                'fetchSubmodules': True|False
            },
            'buildspec': 'string',
            'auth': {
                'type': 'OAUTH',
                'resource': 'string'
            },
            'reportBuildStatus': True|False,
            'insecureSsl': True|False,
            'sourceIdentifier': 'string'
        },
        'secondarySources': [
            {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
        ],
        'sourceVersion': 'string',
        'secondarySourceVersions': [
            {
                'sourceIdentifier': 'string',
                'sourceVersion': 'string'
            },
        ],
        'artifacts': {
            'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
            'location': 'string',
            'path': 'string',
            'namespaceType': 'NONE'|'BUILD_ID',
            'name': 'string',
            'packaging': 'NONE'|'ZIP',
            'overrideArtifactName': True|False,
            'encryptionDisabled': True|False,
            'artifactIdentifier': 'string'
        },
        'secondaryArtifacts': [
            {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
        ],
        'cache': {
            'type': 'NO_CACHE'|'S3'|'LOCAL',
            'location': 'string',
            'modes': [
                'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
            ]
        },
        'environment': {
            'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
            'image': 'string',
            'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
            'environmentVariables': [
                {
                    'name': 'string',
                    'value': 'string',
                    'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                },
            ],
            'privilegedMode': True|False,
            'certificate': 'string',
            'registryCredential': {
                'credential': 'string',
                'credentialProvider': 'SECRETS_MANAGER'
            },
            'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
        },
        'serviceRole': 'string',
        'timeoutInMinutes': 123,
        'queuedTimeoutInMinutes': 123,
        'encryptionKey': 'string',
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ],
        'created': datetime(2015, 1, 1),
        'lastModified': datetime(2015, 1, 1),
        'webhook': {
            'url': 'string',
            'payloadUrl': 'string',
            'secret': 'string',
            'branchFilter': 'string',
            'filterGroups': [
                [
                    {
                        'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                        'pattern': 'string',
                        'excludeMatchedPattern': True|False
                    },
                ],
            ],
            'lastModifiedSecret': datetime(2015, 1, 1)
        },
        'vpcConfig': {
            'vpcId': 'string',
            'subnets': [
                'string',
            ],
            'securityGroupIds': [
                'string',
            ]
        },
        'badge': {
            'badgeEnabled': True|False,
            'badgeRequestUrl': 'string'
        },
        'logsConfig': {
            'cloudWatchLogs': {
                'status': 'ENABLED'|'DISABLED',
                'groupName': 'string',
                'streamName': 'string'
            },
            's3Logs': {
                'status': 'ENABLED'|'DISABLED',
                'location': 'string',
                'encryptionDisabled': True|False
            }
        },
        'fileSystemLocations': [
            {
                'type': 'EFS',
                'location': 'string',
                'mountPoint': 'string',
                'identifier': 'string',
                'mountOptions': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

project (dict) --
Information about the build project that was changed.

name (string) --
The name of the build project.

arn (string) --
The Amazon Resource Name (ARN) of the build project.

description (string) --
A description that makes the build project easy to identify.

source (dict) --
Information about the build input source code for this build project.

type (string) --
The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --
Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --
Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --
Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --
Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --
The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --
Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --

Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --
The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --
Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --
Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --
An identifier for this project source.



secondarySources (list) --
An array of ProjectSource objects.

(dict) --
Information about the build input source code for the build project.

type (string) --
The type of repository that contains the source code to be built. Valid values include:

BITBUCKET : The source code is in a Bitbucket repository.
CODECOMMIT : The source code is in an AWS CodeCommit repository.
CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
GITHUB : The source code is in a GitHub repository.
GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
NO_SOURCE : The project does not have input source code.
S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.


location (string) --
Information about the location of the source code to be built. Valid values include:

For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline\'s source action instead of this value.
For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, ``https://git-codecommit.*region-ID* .amazonaws.com/v1/repos/repo-name `` ).
For source code in an Amazon Simple Storage Service (Amazon S3) input bucket, one of the following.
The path to the ZIP file that contains the source code (for example, `` bucket-name /path /to /object-name .zip`` ).
The path to the folder that contains the source code (for example, `` bucket-name /path /to /source-code /folder /`` ).


For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your GitHub account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub Authorize application page, for Organization access , choose Request access next to each repository you want to allow AWS CodeBuild to have access to, and then choose Authorize application . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .
For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your AWS account to your Bitbucket account. Use the AWS CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket Confirm access to your account page, choose Grant access . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the AWS CodeBuild console.) To instruct AWS CodeBuild to use this connection, in the source object, set the auth object\'s type value to OAUTH .


gitCloneDepth (integer) --
Information about the Git clone depth for the build project.

gitSubmodulesConfig (dict) --
Information about the Git submodules configuration for the build project.

fetchSubmodules (boolean) --
Set to true to fetch Git submodules for your AWS CodeBuild build project.



buildspec (string) --
The buildspec file declaration to use for the builds in this build project.
If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in CODEBUILD_SRC_DIR environment variable, or the path to an S3 bucket. The bucket must be in the same AWS Region as the build project. Specify the buildspec file using its ARN (for example, arn:aws:s3:::my-codebuild-sample2/buildspec.yml ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see Buildspec File Name and Storage Location .

auth (dict) --
Information about the authorization settings for AWS CodeBuild to access the source code to be built.
This information is for the AWS CodeBuild console\'s use only. Your code should not get or set this information directly.

type (string) --

Note
This data type is deprecated and is no longer accurate or used.

The authorization type to use. The only valid value is OAUTH , which represents the OAuth authorization type.

resource (string) --
The resource value that applies to the specified authorization type.



reportBuildStatus (boolean) --
Set to true to report the status of a build\'s start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, or Bitbucket. If this is set and you use a different source provider, an invalidInputException is thrown.

Note
The status of a build triggered by a webhook is always reported to your source provider.


insecureSsl (boolean) --
Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier (string) --
An identifier for this project source.





sourceVersion (string) --
A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.

If sourceVersion is specified at the build level, then that version takes precedence over this sourceVersion (at the project level).
For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .

secondarySourceVersions (list) --
An array of ProjectSourceVersion objects. If secondarySourceVersions is specified at the build level, then they take over these secondarySourceVersions (at the project level).

(dict) --
A source identifier and its corresponding version.

sourceIdentifier (string) --
An identifier for a source in the build project.

sourceVersion (string) --
The source version for the corresponding source identifier. If specified, must be one of:

For AWS CodeCommit: the commit ID, branch, or Git tag to use.
For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format pr/pull-request-ID (for example, pr/25 ). If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch\'s HEAD commit ID is used. If not specified, the default branch\'s HEAD commit ID is used.
For Amazon Simple Storage Service (Amazon S3): the version ID of the object that represents the build input ZIP file to use.

For more information, see Source Version Sample with CodeBuild in the AWS CodeBuild User Guide .





artifacts (dict) --
Information about the build output artifacts for the build project.

type (string) --
The type of build output artifact. Valid values include:

CODEPIPELINE : The build project has build output generated through AWS CodePipeline.


Note
The CODEPIPELINE type is not supported for secondaryArtifacts .


NO_ARTIFACTS : The build project does not produce any build output.
S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).


location (string) --
Information about the build output artifact location:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output bucket.


path (string) --
Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.

For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .

namespaceType (string) --
Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
BUILD_ID : Include the build ID in the location of the build output artifact.
NONE : Do not include the build ID. This is the default if namespaceType is not specified.



For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .

name (string) --
Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

For example:

If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
If path is empty, namespaceType is set to NONE , and name is set to "/ ", the output artifact is stored in the root of the output bucket.
If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to "/ ", the output artifact is stored in ``MyArtifacts/build-ID `` .


packaging (string) --
The type of build output artifact to create:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.




overrideArtifactName (boolean) --
If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --
Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.

artifactIdentifier (string) --
An identifier for this artifact definition.



secondaryArtifacts (list) --
An array of ProjectArtifacts objects.

(dict) --
Information about the build output artifacts for the build project.

type (string) --
The type of build output artifact. Valid values include:

CODEPIPELINE : The build project has build output generated through AWS CodePipeline.


Note
The CODEPIPELINE type is not supported for secondaryArtifacts .


NO_ARTIFACTS : The build project does not produce any build output.
S3 : The build project stores build output in Amazon Simple Storage Service (Amazon S3).


location (string) --
Information about the build output artifact location:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output locations instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output bucket.


path (string) --
Along with namespaceType and name , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the path to the output artifact. If path is not specified, path is not used.

For example, if path is set to MyArtifacts , namespaceType is set to NONE , and name is set to MyArtifact.zip , the output artifact is stored in the output bucket at MyArtifacts/MyArtifact.zip .

namespaceType (string) --
Along with path and name , the pattern that AWS CodeBuild uses to determine the name and location to store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
BUILD_ID : Include the build ID in the location of the build output artifact.
NONE : Do not include the build ID. This is the default if namespaceType is not specified.



For example, if path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .

name (string) --
Along with path and namespaceType , the pattern that AWS CodeBuild uses to name and store the output artifact:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output names instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , this is the name of the output artifact object. If you set the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.

For example:

If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to MyArtifact.zip , then the output artifact is stored in MyArtifacts/*build-ID* /MyArtifact.zip .
If path is empty, namespaceType is set to NONE , and name is set to "/ ", the output artifact is stored in the root of the output bucket.
If path is set to MyArtifacts , namespaceType is set to BUILD_ID , and name is set to "/ ", the output artifact is stored in ``MyArtifacts/build-ID `` .


packaging (string) --
The type of build output artifact to create:

If type is set to CODEPIPELINE , AWS CodePipeline ignores this value if specified. This is because AWS CodePipeline manages its build output artifacts instead of AWS CodeBuild.
If type is set to NO_ARTIFACTS , this value is ignored if specified, because no build output is produced.
If type is set to S3 , valid values include:
NONE : AWS CodeBuild creates in the output bucket a folder that contains the build output. This is the default if packaging is not specified.
ZIP : AWS CodeBuild creates in the output bucket a ZIP file that contains the build output.




overrideArtifactName (boolean) --
If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled (boolean) --
Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon Simple Storage Service (Amazon S3). If this is set with another artifacts type, an invalidInputException is thrown.

artifactIdentifier (string) --
An identifier for this artifact definition.





cache (dict) --
Information about the cache for the build project.

type (string) --
The type of cache used by the build project. Valid values include:

NO_CACHE : The build project does not use any cache.
S3 : The build project reads and writes from and to S3.
LOCAL : The build project stores a cache locally on a build host that is only available to that build host.


location (string) --
Information about the cache location:

NO_CACHE or LOCAL : This value is ignored.
S3 : This is the S3 bucket name/prefix.


modes (list) --
If you use a LOCAL cache, the local cache mode. You can use one or more local cache modes at the same time.

LOCAL_SOURCE_CACHE mode caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.
LOCAL_DOCKER_LAYER_CACHE mode caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.


Note

You can use a Docker layer cache in the Linux environment only.
The privileged flag must be set so that your project has the required Docker permissions.
You should consider the security implications before you use a Docker layer cache.



LOCAL_CUSTOM_CACHE mode caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:
Only directories can be specified for caching. You cannot specify individual files.
Symlinks are used to reference cached directories.
Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.




(string) --




environment (dict) --
Information about the build environment for this build project.

type (string) --
The type of build environment to use for related builds.

The environment type ARM_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Sydney), and EU (Frankfurt).
The environment type LINUX_CONTAINER with compute type build.general1.2xlarge is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China (Ningxia).
The environment type LINUX_GPU_CONTAINER is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).


image (string) --
The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:

For an image tag: registry/repository:tag . For example, to specify an image with the tag "latest," use registry/repository:latest .
For an image digest: registry/repository@digest . For example, to specify an image with the digest "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use registry/repository@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf .


computeType (string) --
Information about the compute resources the build project uses. Available values include:

BUILD_GENERAL1_SMALL : Use up to 3 GB memory and 2 vCPUs for builds.
BUILD_GENERAL1_MEDIUM : Use up to 7 GB memory and 4 vCPUs for builds.
BUILD_GENERAL1_LARGE : Use up to 16 GB memory and 8 vCPUs for builds, depending on your environment type.
BUILD_GENERAL1_2XLARGE : Use up to 145 GB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.

If you use BUILD_GENERAL1_LARGE :

For environment type LINUX_CONTAINER , you can use up to 15 GB memory and 8 vCPUs for builds.
For environment type LINUX_GPU_CONTAINER , you can use up to 255 GB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.
For environment type ARM_CONTAINER , you can use up to 16 GB memory and 8 vCPUs on ARM-based processors for builds.

For more information, see Build Environment Compute Types in the AWS CodeBuild User Guide.

environmentVariables (list) --
A set of environment variables to make available to builds for this build project.

(dict) --
Information about an environment variable for a build project or a build.

name (string) --
The name or key of the environment variable.

value (string) --
The value of the environment variable.

Warning
We strongly discourage the use of PLAINTEXT environment variables to store sensitive values, especially AWS secret key IDs and secret access keys. PLAINTEXT environment variables can be displayed in plain text using the AWS CodeBuild console and the AWS Command Line Interface (AWS CLI). For sensitive values, we recommend you use an environment variable of type PARAMETER_STORE or SECRETS_MANAGER .


type (string) --
The type of environment variable. Valid values include:

PARAMETER_STORE : An environment variable stored in Amazon EC2 Systems Manager Parameter Store. To learn how to specify a parameter store environment variable, see parameter store reference-key in the buildspec file .
PLAINTEXT : An environment variable in plain text format. This is the default value.
SECRETS_MANAGER : An environment variable stored in AWS Secrets Manager. To learn how to specify a secrets manager environment variable, see secrets manager reference-key in the buildspec file .






privilegedMode (boolean) --
Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is false .
You can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:
If the operating system\'s base image is Ubuntu Linux:

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&
- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"

If the operating system\'s base image is Alpine Linux and the previous command does not work, add the -t argument to timeout :

- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&
- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"


certificate (string) --
The certificate to use with this build project.

registryCredential (dict) --
The credentials for access to a private registry.

credential (string) --
The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.

Note
The credential can use the name of the credentials only if they exist in your current AWS Region.


credentialProvider (string) --
The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.



imagePullCredentialsType (string) --
The type of credentials AWS CodeBuild uses to pull images in your build. There are two valid values:

CODEBUILD specifies that AWS CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust AWS CodeBuild\'s service principal.
SERVICE_ROLE specifies that AWS CodeBuild uses your build project\'s service role.

When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials.



serviceRole (string) --
The ARN of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

timeoutInMinutes (integer) --
How long, in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.

queuedTimeoutInMinutes (integer) --
The number of minutes a build is allowed to be queued before it times out.

encryptionKey (string) --
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts.

Note
You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK\'s alias (using the format ``alias/alias-name `` ).

tags (list) --
A list of tag key and value pairs associated with this build project.
These tags are available for use by AWS services that support AWS CodeBuild build project tags.

(dict) --
A tag, consisting of a key and a value.
This tag is available for use by AWS services that support tags in AWS CodeBuild.

key (string) --
The tag\'s key.

value (string) --
The tag\'s value.





created (datetime) --
When the build project was created, expressed in Unix time format.

lastModified (datetime) --
When the build project\'s settings were last modified, expressed in Unix time format.

webhook (dict) --
Information about a webhook that connects repository events to a build project in AWS CodeBuild.

url (string) --
The URL to the webhook.

payloadUrl (string) --
The AWS CodeBuild endpoint where webhook events are sent.

secret (string) --
The secret token of the associated repository.

Note
A Bitbucket webhook does not support secret .


branchFilter (string) --
A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If branchFilter is empty, then all branches are built.

Note
It is recommended that you use filterGroups instead of branchFilter .


filterGroups (list) --
An array of arrays of WebhookFilter objects used to determine which webhooks are triggered. At least one WebhookFilter in the array must specify EVENT as its type .
For a build to be triggered, at least one filter group in the filterGroups array must pass. For a filter group to pass, each of its filters must pass.

(list) --

(dict) --
A filter used to determine which webhooks trigger a build.

type (string) --
The type of webhook filter. There are five webhook filter types: EVENT , ACTOR_ACCOUNT_ID , HEAD_REF , BASE_REF , and FILE_PATH .

EVENT

A webhook event triggers a build when the provided pattern matches one of five event types: PUSH , PULL_REQUEST_CREATED , PULL_REQUEST_UPDATED , PULL_REQUEST_REOPENED , and PULL_REQUEST_MERGED . The EVENT patterns are specified as a comma-separated string. For example, PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED filters all push, pull request created, and pull request updated events.

Note
The PULL_REQUEST_REOPENED works with GitHub and GitHub Enterprise only.
ACTOR_ACCOUNT_ID

A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression pattern .

HEAD_REF

A webhook event triggers a build when the head reference matches the regular expression pattern . For example, refs/heads/branch-name and refs/tags/tag-name .
Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.

BASE_REF

A webhook event triggers a build when the base reference matches the regular expression pattern . For example, refs/heads/branch-name .

Note
Works with pull request events only.
FILE_PATH

A webhook triggers a build when the path of a changed file matches the regular expression pattern .

Note
Works with GitHub and GitHub Enterprise push events only.


pattern (string) --
For a WebHookFilter that uses EVENT type, a comma-separated string that specifies one or more events. For example, the webhook filter PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED allows all push, pull request created, and pull request updated events to trigger a build.
For a WebHookFilter that uses any of the other filter types, a regular expression pattern. For example, a WebHookFilter that uses HEAD_REF for its type and the pattern ^refs/heads/ triggers a build when the head reference is a branch with a reference name refs/heads/branch-name .

excludeMatchedPattern (boolean) --
Used to indicate that the pattern determines which webhook events do not trigger a build. If true, then a webhook event that does not match the pattern triggers a build. If false, then a webhook event that matches the pattern triggers a build.







lastModifiedSecret (datetime) --
A timestamp that indicates the last time a repository\'s secret token was modified.



vpcConfig (dict) --
Information about the VPC configuration that AWS CodeBuild accesses.

vpcId (string) --
The ID of the Amazon VPC.

subnets (list) --
A list of one or more subnet IDs in your Amazon VPC.

(string) --


securityGroupIds (list) --
A list of one or more security groups IDs in your Amazon VPC.

(string) --




badge (dict) --
Information about the build badge for the build project.

badgeEnabled (boolean) --
Set this to true to generate a publicly accessible URL for your project\'s build badge.

badgeRequestUrl (string) --
The publicly-accessible URL through which you can access the build badge for your project.
The publicly accessible URL through which you can access the build badge for your project.



logsConfig (dict) --
Information about logs for the build project. A project can create logs in Amazon CloudWatch Logs, an S3 bucket, or both.

cloudWatchLogs (dict) --
Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are enabled by default.

status (string) --
The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values are:

ENABLED : Amazon CloudWatch Logs are enabled for this build project.
DISABLED : Amazon CloudWatch Logs are not enabled for this build project.


groupName (string) --
The group name of the logs in Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .

streamName (string) --
The prefix of the stream name of the Amazon CloudWatch Logs. For more information, see Working with Log Groups and Log Streams .



s3Logs (dict) --
Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.

status (string) --
The current status of the S3 build logs. Valid values are:

ENABLED : S3 build logs are enabled for this build project.
DISABLED : S3 build logs are not enabled for this build project.


location (string) --
The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is my-bucket , and your path prefix is build-log , then acceptable formats are my-bucket/build-log or arn:aws:s3:::my-bucket/build-log .

encryptionDisabled (boolean) --
Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.





fileSystemLocations (list) --
An array of ProjectFileSystemLocation objects for a CodeBuild build project. A ProjectFileSystemLocation object specifies the identifier , location , mountOptions , mountPoint , and type of a file system created using Amazon Elastic File System.

(dict) --
Information about a file system created by Amazon Elastic File System (EFS). For more information, see What Is Amazon Elastic File System?

type (string) --
The type of the file system. The one supported type is EFS .

location (string) --
A string that specifies the location of the file system created by Amazon EFS. Its format is efs-dns-name:/directory-path . You can find the DNS name of file system when you view it in the AWS EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is fs-abcd1234.efs.us-west-2.amazonaws.com , and its mount directory is my-efs-mount-directory , then the location is fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory .
The directory path in the format efs-dns-name:/directory-path is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.

mountPoint (string) --
The location in the container where you mount the file system.

identifier (string) --
The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the identifier in all capital letters to CODEBUILD_ . For example, if you specify my-efs for identifier , a new environment variable is create named CODEBUILD_MY-EFS .
The identifier is used to mount your file system.

mountOptions (string) --
The mount options for a file system created by AWS EFS. The default mount options used by CodeBuild are nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 . For more information, see Recommended NFS Mount Options .













Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException


    :return: {
        'project': {
            'name': 'string',
            'arn': 'string',
            'description': 'string',
            'source': {
                'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                'location': 'string',
                'gitCloneDepth': 123,
                'gitSubmodulesConfig': {
                    'fetchSubmodules': True|False
                },
                'buildspec': 'string',
                'auth': {
                    'type': 'OAUTH',
                    'resource': 'string'
                },
                'reportBuildStatus': True|False,
                'insecureSsl': True|False,
                'sourceIdentifier': 'string'
            },
            'secondarySources': [
                {
                    'type': 'CODECOMMIT'|'CODEPIPELINE'|'GITHUB'|'S3'|'BITBUCKET'|'GITHUB_ENTERPRISE'|'NO_SOURCE',
                    'location': 'string',
                    'gitCloneDepth': 123,
                    'gitSubmodulesConfig': {
                        'fetchSubmodules': True|False
                    },
                    'buildspec': 'string',
                    'auth': {
                        'type': 'OAUTH',
                        'resource': 'string'
                    },
                    'reportBuildStatus': True|False,
                    'insecureSsl': True|False,
                    'sourceIdentifier': 'string'
                },
            ],
            'sourceVersion': 'string',
            'secondarySourceVersions': [
                {
                    'sourceIdentifier': 'string',
                    'sourceVersion': 'string'
                },
            ],
            'artifacts': {
                'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                'location': 'string',
                'path': 'string',
                'namespaceType': 'NONE'|'BUILD_ID',
                'name': 'string',
                'packaging': 'NONE'|'ZIP',
                'overrideArtifactName': True|False,
                'encryptionDisabled': True|False,
                'artifactIdentifier': 'string'
            },
            'secondaryArtifacts': [
                {
                    'type': 'CODEPIPELINE'|'S3'|'NO_ARTIFACTS',
                    'location': 'string',
                    'path': 'string',
                    'namespaceType': 'NONE'|'BUILD_ID',
                    'name': 'string',
                    'packaging': 'NONE'|'ZIP',
                    'overrideArtifactName': True|False,
                    'encryptionDisabled': True|False,
                    'artifactIdentifier': 'string'
                },
            ],
            'cache': {
                'type': 'NO_CACHE'|'S3'|'LOCAL',
                'location': 'string',
                'modes': [
                    'LOCAL_DOCKER_LAYER_CACHE'|'LOCAL_SOURCE_CACHE'|'LOCAL_CUSTOM_CACHE',
                ]
            },
            'environment': {
                'type': 'WINDOWS_CONTAINER'|'LINUX_CONTAINER'|'LINUX_GPU_CONTAINER'|'ARM_CONTAINER',
                'image': 'string',
                'computeType': 'BUILD_GENERAL1_SMALL'|'BUILD_GENERAL1_MEDIUM'|'BUILD_GENERAL1_LARGE'|'BUILD_GENERAL1_2XLARGE',
                'environmentVariables': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'type': 'PLAINTEXT'|'PARAMETER_STORE'|'SECRETS_MANAGER'
                    },
                ],
                'privilegedMode': True|False,
                'certificate': 'string',
                'registryCredential': {
                    'credential': 'string',
                    'credentialProvider': 'SECRETS_MANAGER'
                },
                'imagePullCredentialsType': 'CODEBUILD'|'SERVICE_ROLE'
            },
            'serviceRole': 'string',
            'timeoutInMinutes': 123,
            'queuedTimeoutInMinutes': 123,
            'encryptionKey': 'string',
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ],
            'created': datetime(2015, 1, 1),
            'lastModified': datetime(2015, 1, 1),
            'webhook': {
                'url': 'string',
                'payloadUrl': 'string',
                'secret': 'string',
                'branchFilter': 'string',
                'filterGroups': [
                    [
                        {
                            'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                            'pattern': 'string',
                            'excludeMatchedPattern': True|False
                        },
                    ],
                ],
                'lastModifiedSecret': datetime(2015, 1, 1)
            },
            'vpcConfig': {
                'vpcId': 'string',
                'subnets': [
                    'string',
                ],
                'securityGroupIds': [
                    'string',
                ]
            },
            'badge': {
                'badgeEnabled': True|False,
                'badgeRequestUrl': 'string'
            },
            'logsConfig': {
                'cloudWatchLogs': {
                    'status': 'ENABLED'|'DISABLED',
                    'groupName': 'string',
                    'streamName': 'string'
                },
                's3Logs': {
                    'status': 'ENABLED'|'DISABLED',
                    'location': 'string',
                    'encryptionDisabled': True|False
                }
            },
            'fileSystemLocations': [
                {
                    'type': 'EFS',
                    'location': 'string',
                    'mountPoint': 'string',
                    'identifier': 'string',
                    'mountOptions': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    BITBUCKET : The source code is in a Bitbucket repository.
    CODECOMMIT : The source code is in an AWS CodeCommit repository.
    CODEPIPELINE : The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
    GITHUB : The source code is in a GitHub repository.
    GITHUB_ENTERPRISE : The source code is in a GitHub Enterprise repository.
    NO_SOURCE : The project does not have input source code.
    S3 : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    
    """
    pass

def update_report_group(arn=None, exportConfig=None, tags=None):
    """
    Updates a report group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_report_group(
        arn='string',
        exportConfig={
            'exportConfigType': 'S3'|'NO_EXPORT',
            's3Destination': {
                'bucket': 'string',
                'path': 'string',
                'packaging': 'ZIP'|'NONE',
                'encryptionKey': 'string',
                'encryptionDisabled': True|False
            }
        },
        tags=[
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe ARN of the report group to update.\n

    :type exportConfig: dict
    :param exportConfig: Used to specify an updated export type. Valid values are:\n\nS3 : The report results are exported to an S3 bucket.\nNO_EXPORT : The report results are not exported.\n\n\nexportConfigType (string) --The export configuration type. Valid values are:\n\nS3 : The report results are exported to an S3 bucket.\nNO_EXPORT : The report results are not exported.\n\n\ns3Destination (dict) --A S3ReportExportConfig object that contains information about the S3 bucket where the run of a report is exported.\n\nbucket (string) --The name of the S3 bucket where the raw data of a report are exported.\n\npath (string) --The path to the exported report\'s raw data results.\n\npackaging (string) --The type of build output artifact to create. Valid values include:\n\nNONE : AWS CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified.\nZIP : AWS CodeBuild creates a ZIP file with the raw data in the output bucket.\n\n\nencryptionKey (string) --The encryption key for the report\'s encrypted raw data.\n\nencryptionDisabled (boolean) --A boolean value that specifies if the results of a report are encrypted.\n\n\n\n\n

    :type tags: list
    :param tags: An updated list of tag key and value pairs associated with this report group.\nThese tags are available for use by AWS services that support AWS CodeBuild report group tags.\n\n(dict) --A tag, consisting of a key and a value.\nThis tag is available for use by AWS services that support tags in AWS CodeBuild.\n\nkey (string) --The tag\'s key.\n\nvalue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'reportGroup': {
        'arn': 'string',
        'name': 'string',
        'type': 'TEST',
        'exportConfig': {
            'exportConfigType': 'S3'|'NO_EXPORT',
            's3Destination': {
                'bucket': 'string',
                'path': 'string',
                'packaging': 'ZIP'|'NONE',
                'encryptionKey': 'string',
                'encryptionDisabled': True|False
            }
        },
        'created': datetime(2015, 1, 1),
        'lastModified': datetime(2015, 1, 1),
        'tags': [
            {
                'key': 'string',
                'value': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

reportGroup (dict) --
Information about the updated report group.

arn (string) --
The ARN of a ReportGroup .

name (string) --
The name of a ReportGroup .

type (string) --
The type of the ReportGroup . The one valid value is TEST .

exportConfig (dict) --
Information about the destination where the raw data of this ReportGroup is exported.

exportConfigType (string) --
The export configuration type. Valid values are:

S3 : The report results are exported to an S3 bucket.
NO_EXPORT : The report results are not exported.


s3Destination (dict) --
A S3ReportExportConfig object that contains information about the S3 bucket where the run of a report is exported.

bucket (string) --
The name of the S3 bucket where the raw data of a report are exported.

path (string) --
The path to the exported report\'s raw data results.

packaging (string) --
The type of build output artifact to create. Valid values include:

NONE : AWS CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified.
ZIP : AWS CodeBuild creates a ZIP file with the raw data in the output bucket.


encryptionKey (string) --
The encryption key for the report\'s encrypted raw data.

encryptionDisabled (boolean) --
A boolean value that specifies if the results of a report are encrypted.





created (datetime) --
The date and time this ReportGroup was created.

lastModified (datetime) --
The date and time this ReportGroup was last modified.

tags (list) --
A list of tag key and value pairs associated with this report group.
These tags are available for use by AWS services that support AWS CodeBuild report group tags.

(dict) --
A tag, consisting of a key and a value.
This tag is available for use by AWS services that support tags in AWS CodeBuild.

key (string) --
The tag\'s key.

value (string) --
The tag\'s value.













Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException


    :return: {
        'reportGroup': {
            'arn': 'string',
            'name': 'string',
            'type': 'TEST',
            'exportConfig': {
                'exportConfigType': 'S3'|'NO_EXPORT',
                's3Destination': {
                    'bucket': 'string',
                    'path': 'string',
                    'packaging': 'ZIP'|'NONE',
                    'encryptionKey': 'string',
                    'encryptionDisabled': True|False
                }
            },
            'created': datetime(2015, 1, 1),
            'lastModified': datetime(2015, 1, 1),
            'tags': [
                {
                    'key': 'string',
                    'value': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    S3 : The report results are exported to an S3 bucket.
    NO_EXPORT : The report results are not exported.
    
    """
    pass

def update_webhook(projectName=None, branchFilter=None, rotateSecret=None, filterGroups=None):
    """
    Updates the webhook associated with an AWS CodeBuild build project.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_webhook(
        projectName='string',
        branchFilter='string',
        rotateSecret=True|False,
        filterGroups=[
            [
                {
                    'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                    'pattern': 'string',
                    'excludeMatchedPattern': True|False
                },
            ],
        ]
    )
    
    
    :type projectName: string
    :param projectName: [REQUIRED]\nThe name of the AWS CodeBuild project.\n

    :type branchFilter: string
    :param branchFilter: A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If branchFilter is empty, then all branches are built.\n\nNote\nIt is recommended that you use filterGroups instead of branchFilter .\n\n

    :type rotateSecret: boolean
    :param rotateSecret: A boolean value that specifies whether the associated GitHub repository\'s secret token should be updated. If you use Bitbucket for your repository, rotateSecret is ignored.

    :type filterGroups: list
    :param filterGroups: An array of arrays of WebhookFilter objects used to determine if a webhook event can trigger a build. A filter group must contain at least one EVENT WebhookFilter .\n\n(list) --\n(dict) --A filter used to determine which webhooks trigger a build.\n\ntype (string) -- [REQUIRED]The type of webhook filter. There are five webhook filter types: EVENT , ACTOR_ACCOUNT_ID , HEAD_REF , BASE_REF , and FILE_PATH .\n\nEVENT\nA webhook event triggers a build when the provided pattern matches one of five event types: PUSH , PULL_REQUEST_CREATED , PULL_REQUEST_UPDATED , PULL_REQUEST_REOPENED , and PULL_REQUEST_MERGED . The EVENT patterns are specified as a comma-separated string. For example, PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED filters all push, pull request created, and pull request updated events.\n\nNote\nThe PULL_REQUEST_REOPENED works with GitHub and GitHub Enterprise only.\nACTOR_ACCOUNT_ID\n\nA webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression pattern .\n\nHEAD_REF\nA webhook event triggers a build when the head reference matches the regular expression pattern . For example, refs/heads/branch-name and refs/tags/tag-name .\nWorks with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.\n\nBASE_REF\nA webhook event triggers a build when the base reference matches the regular expression pattern . For example, refs/heads/branch-name .\n\nNote\nWorks with pull request events only.\nFILE_PATH\n\nA webhook triggers a build when the path of a changed file matches the regular expression pattern .\n\nNote\nWorks with GitHub and GitHub Enterprise push events only.\n\n\npattern (string) -- [REQUIRED]For a WebHookFilter that uses EVENT type, a comma-separated string that specifies one or more events. For example, the webhook filter PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED allows all push, pull request created, and pull request updated events to trigger a build.\nFor a WebHookFilter that uses any of the other filter types, a regular expression pattern. For example, a WebHookFilter that uses HEAD_REF for its type and the pattern ^refs/heads/ triggers a build when the head reference is a branch with a reference name refs/heads/branch-name .\n\nexcludeMatchedPattern (boolean) --Used to indicate that the pattern determines which webhook events do not trigger a build. If true, then a webhook event that does not match the pattern triggers a build. If false, then a webhook event that matches the pattern triggers a build.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'webhook': {
        'url': 'string',
        'payloadUrl': 'string',
        'secret': 'string',
        'branchFilter': 'string',
        'filterGroups': [
            [
                {
                    'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                    'pattern': 'string',
                    'excludeMatchedPattern': True|False
                },
            ],
        ],
        'lastModifiedSecret': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --

webhook (dict) --
Information about a repository\'s webhook that is associated with a project in AWS CodeBuild.

url (string) --
The URL to the webhook.

payloadUrl (string) --
The AWS CodeBuild endpoint where webhook events are sent.

secret (string) --
The secret token of the associated repository.

Note
A Bitbucket webhook does not support secret .


branchFilter (string) --
A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If branchFilter is empty, then all branches are built.

Note
It is recommended that you use filterGroups instead of branchFilter .


filterGroups (list) --
An array of arrays of WebhookFilter objects used to determine which webhooks are triggered. At least one WebhookFilter in the array must specify EVENT as its type .
For a build to be triggered, at least one filter group in the filterGroups array must pass. For a filter group to pass, each of its filters must pass.

(list) --

(dict) --
A filter used to determine which webhooks trigger a build.

type (string) --
The type of webhook filter. There are five webhook filter types: EVENT , ACTOR_ACCOUNT_ID , HEAD_REF , BASE_REF , and FILE_PATH .

EVENT

A webhook event triggers a build when the provided pattern matches one of five event types: PUSH , PULL_REQUEST_CREATED , PULL_REQUEST_UPDATED , PULL_REQUEST_REOPENED , and PULL_REQUEST_MERGED . The EVENT patterns are specified as a comma-separated string. For example, PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED filters all push, pull request created, and pull request updated events.

Note
The PULL_REQUEST_REOPENED works with GitHub and GitHub Enterprise only.
ACTOR_ACCOUNT_ID

A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression pattern .

HEAD_REF

A webhook event triggers a build when the head reference matches the regular expression pattern . For example, refs/heads/branch-name and refs/tags/tag-name .
Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.

BASE_REF

A webhook event triggers a build when the base reference matches the regular expression pattern . For example, refs/heads/branch-name .

Note
Works with pull request events only.
FILE_PATH

A webhook triggers a build when the path of a changed file matches the regular expression pattern .

Note
Works with GitHub and GitHub Enterprise push events only.


pattern (string) --
For a WebHookFilter that uses EVENT type, a comma-separated string that specifies one or more events. For example, the webhook filter PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED allows all push, pull request created, and pull request updated events to trigger a build.
For a WebHookFilter that uses any of the other filter types, a regular expression pattern. For example, a WebHookFilter that uses HEAD_REF for its type and the pattern ^refs/heads/ triggers a build when the head reference is a branch with a reference name refs/heads/branch-name .

excludeMatchedPattern (boolean) --
Used to indicate that the pattern determines which webhook events do not trigger a build. If true, then a webhook event that does not match the pattern triggers a build. If false, then a webhook event that matches the pattern triggers a build.







lastModifiedSecret (datetime) --
A timestamp that indicates the last time a repository\'s secret token was modified.









Exceptions

CodeBuild.Client.exceptions.InvalidInputException
CodeBuild.Client.exceptions.ResourceNotFoundException
CodeBuild.Client.exceptions.OAuthProviderException


    :return: {
        'webhook': {
            'url': 'string',
            'payloadUrl': 'string',
            'secret': 'string',
            'branchFilter': 'string',
            'filterGroups': [
                [
                    {
                        'type': 'EVENT'|'BASE_REF'|'HEAD_REF'|'ACTOR_ACCOUNT_ID'|'FILE_PATH'|'COMMIT_MESSAGE',
                        'pattern': 'string',
                        'excludeMatchedPattern': True|False
                    },
                ],
            ],
            'lastModifiedSecret': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    CodeBuild.Client.exceptions.InvalidInputException
    CodeBuild.Client.exceptions.ResourceNotFoundException
    CodeBuild.Client.exceptions.OAuthProviderException
    
    """
    pass

