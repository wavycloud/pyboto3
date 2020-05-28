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

def create_app(name=None, description=None, repository=None, platform=None, iamServiceRoleArn=None, oauthToken=None, accessToken=None, environmentVariables=None, enableBranchAutoBuild=None, enableBasicAuth=None, basicAuthCredentials=None, customRules=None, tags=None, buildSpec=None, enableAutoBranchCreation=None, autoBranchCreationPatterns=None, autoBranchCreationConfig=None):
    """
    Creates a new Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_app(
        name='string',
        description='string',
        repository='string',
        platform='WEB',
        iamServiceRoleArn='string',
        oauthToken='string',
        accessToken='string',
        environmentVariables={
            'string': 'string'
        },
        enableBranchAutoBuild=True|False,
        enableBasicAuth=True|False,
        basicAuthCredentials='string',
        customRules=[
            {
                'source': 'string',
                'target': 'string',
                'status': 'string',
                'condition': 'string'
            },
        ],
        tags={
            'string': 'string'
        },
        buildSpec='string',
        enableAutoBranchCreation=True|False,
        autoBranchCreationPatterns=[
            'string',
        ],
        autoBranchCreationConfig={
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'framework': 'string',
            'enableAutoBuild': True|False,
            'environmentVariables': {
                'string': 'string'
            },
            'basicAuthCredentials': 'string',
            'enableBasicAuth': True|False,
            'buildSpec': 'string',
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string'
        }
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nName for the Amplify App\n

    :type description: string
    :param description: Description for an Amplify App

    :type repository: string
    :param repository: Repository for an Amplify App

    :type platform: string
    :param platform: Platform / framework for an Amplify App

    :type iamServiceRoleArn: string
    :param iamServiceRoleArn: AWS IAM service role for an Amplify App

    :type oauthToken: string
    :param oauthToken: OAuth token for 3rd party source control system for an Amplify App, used to create webhook and read-only deploy key. OAuth token is not stored.

    :type accessToken: string
    :param accessToken: Personal Access token for 3rd party source control system for an Amplify App, used to create webhook and read-only deploy key. Token is not stored.

    :type environmentVariables: dict
    :param environmentVariables: Environment variables map for an Amplify App.\n\n(string) --\n(string) --\n\n\n\n

    :type enableBranchAutoBuild: boolean
    :param enableBranchAutoBuild: Enable the auto building of branches for an Amplify App.

    :type enableBasicAuth: boolean
    :param enableBasicAuth: Enable Basic Authorization for an Amplify App, this will apply to all branches part of this App.

    :type basicAuthCredentials: string
    :param basicAuthCredentials: Credentials for Basic Authorization for an Amplify App.

    :type customRules: list
    :param customRules: Custom rewrite / redirect rules for an Amplify App.\n\n(dict) --Custom rewrite / redirect rule.\n\nsource (string) -- [REQUIRED]The source pattern for a URL rewrite or redirect rule.\n\ntarget (string) -- [REQUIRED]The target pattern for a URL rewrite or redirect rule.\n\nstatus (string) --The status code for a URL rewrite or redirect rule.\n\ncondition (string) --The condition for a URL rewrite or redirect rule, e.g. country code.\n\n\n\n\n

    :type tags: dict
    :param tags: Tag for an Amplify App\n\n(string) --\n(string) --\n\n\n\n

    :type buildSpec: string
    :param buildSpec: BuildSpec for an Amplify App

    :type enableAutoBranchCreation: boolean
    :param enableAutoBranchCreation: Enables automated branch creation for the Amplify App.

    :type autoBranchCreationPatterns: list
    :param autoBranchCreationPatterns: Automated branch creation glob patterns for the Amplify App.\n\n(string) --\n\n

    :type autoBranchCreationConfig: dict
    :param autoBranchCreationConfig: Automated branch creation config for the Amplify App.\n\nstage (string) --Stage for the auto created branch.\n\nframework (string) --Framework for the auto created branch.\n\nenableAutoBuild (boolean) --Enables auto building for the auto created branch.\n\nenvironmentVariables (dict) --Environment Variables for the auto created branch.\n\n(string) --\n(string) --\n\n\n\n\nbasicAuthCredentials (string) --Basic Authorization credentials for the auto created branch.\n\nenableBasicAuth (boolean) --Enables Basic Auth for the auto created branch.\n\nbuildSpec (string) --BuildSpec for the auto created branch.\n\nenablePullRequestPreview (boolean) --Enables Pull Request Preview for auto created branch.\n\npullRequestEnvironmentName (string) --The Amplify Environment name for the pull request.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'app': {
        'appId': 'string',
        'appArn': 'string',
        'name': 'string',
        'tags': {
            'string': 'string'
        },
        'description': 'string',
        'repository': 'string',
        'platform': 'WEB',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1),
        'iamServiceRoleArn': 'string',
        'environmentVariables': {
            'string': 'string'
        },
        'defaultDomain': 'string',
        'enableBranchAutoBuild': True|False,
        'enableBasicAuth': True|False,
        'basicAuthCredentials': 'string',
        'customRules': [
            {
                'source': 'string',
                'target': 'string',
                'status': 'string',
                'condition': 'string'
            },
        ],
        'productionBranch': {
            'lastDeployTime': datetime(2015, 1, 1),
            'status': 'string',
            'thumbnailUrl': 'string',
            'branchName': 'string'
        },
        'buildSpec': 'string',
        'enableAutoBranchCreation': True|False,
        'autoBranchCreationPatterns': [
            'string',
        ],
        'autoBranchCreationConfig': {
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'framework': 'string',
            'enableAutoBuild': True|False,
            'environmentVariables': {
                'string': 'string'
            },
            'basicAuthCredentials': 'string',
            'enableBasicAuth': True|False,
            'buildSpec': 'string',
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string'
        }
    }
}


Response Structure

(dict) --

app (dict) --
Amplify App represents different branches of a repository for building, deploying, and hosting.

appId (string) --
Unique Id for the Amplify App.

appArn (string) --
ARN for the Amplify App.

name (string) --
Name for the Amplify App.

tags (dict) --
Tag for Amplify App.

(string) --
(string) --




description (string) --
Description for the Amplify App.

repository (string) --
Repository for the Amplify App.

platform (string) --
Platform for the Amplify App.

createTime (datetime) --
Create date / time for the Amplify App.

updateTime (datetime) --
Update date / time for the Amplify App.

iamServiceRoleArn (string) --
IAM service role ARN for the Amplify App.

environmentVariables (dict) --
Environment Variables for the Amplify App.

(string) --
(string) --




defaultDomain (string) --
Default domain for the Amplify App.

enableBranchAutoBuild (boolean) --
Enables auto-building of branches for the Amplify App.

enableBasicAuth (boolean) --
Enables Basic Authorization for branches for the Amplify App.

basicAuthCredentials (string) --
Basic Authorization credentials for branches for the Amplify App.

customRules (list) --
Custom redirect / rewrite rules for the Amplify App.

(dict) --
Custom rewrite / redirect rule.

source (string) --
The source pattern for a URL rewrite or redirect rule.

target (string) --
The target pattern for a URL rewrite or redirect rule.

status (string) --
The status code for a URL rewrite or redirect rule.

condition (string) --
The condition for a URL rewrite or redirect rule, e.g. country code.





productionBranch (dict) --
Structure with Production Branch information.

lastDeployTime (datetime) --
Last Deploy Time of Production Branch.

status (string) --
Status of Production Branch.

thumbnailUrl (string) --
Thumbnail URL for Production Branch.

branchName (string) --
Branch Name for Production Branch.



buildSpec (string) --
BuildSpec content for Amplify App.

enableAutoBranchCreation (boolean) --
Enables automated branch creation for the Amplify App.

autoBranchCreationPatterns (list) --
Automated branch creation glob patterns for the Amplify App.

(string) --


autoBranchCreationConfig (dict) --
Automated branch creation config for the Amplify App.

stage (string) --
Stage for the auto created branch.

framework (string) --
Framework for the auto created branch.

enableAutoBuild (boolean) --
Enables auto building for the auto created branch.

environmentVariables (dict) --
Environment Variables for the auto created branch.

(string) --
(string) --




basicAuthCredentials (string) --
Basic Authorization credentials for the auto created branch.

enableBasicAuth (boolean) --
Enables Basic Auth for the auto created branch.

buildSpec (string) --
BuildSpec for the auto created branch.

enablePullRequestPreview (boolean) --
Enables Pull Request Preview for auto created branch.

pullRequestEnvironmentName (string) --
The Amplify Environment name for the pull request.











Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.LimitExceededException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'app': {
            'appId': 'string',
            'appArn': 'string',
            'name': 'string',
            'tags': {
                'string': 'string'
            },
            'description': 'string',
            'repository': 'string',
            'platform': 'WEB',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'iamServiceRoleArn': 'string',
            'environmentVariables': {
                'string': 'string'
            },
            'defaultDomain': 'string',
            'enableBranchAutoBuild': True|False,
            'enableBasicAuth': True|False,
            'basicAuthCredentials': 'string',
            'customRules': [
                {
                    'source': 'string',
                    'target': 'string',
                    'status': 'string',
                    'condition': 'string'
                },
            ],
            'productionBranch': {
                'lastDeployTime': datetime(2015, 1, 1),
                'status': 'string',
                'thumbnailUrl': 'string',
                'branchName': 'string'
            },
            'buildSpec': 'string',
            'enableAutoBranchCreation': True|False,
            'autoBranchCreationPatterns': [
                'string',
            ],
            'autoBranchCreationConfig': {
                'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
                'framework': 'string',
                'enableAutoBuild': True|False,
                'environmentVariables': {
                    'string': 'string'
                },
                'basicAuthCredentials': 'string',
                'enableBasicAuth': True|False,
                'buildSpec': 'string',
                'enablePullRequestPreview': True|False,
                'pullRequestEnvironmentName': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_backend_environment(appId=None, environmentName=None, stackName=None, deploymentArtifacts=None):
    """
    Creates a new backend environment for an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_backend_environment(
        appId='string',
        environmentName='string',
        stackName='string',
        deploymentArtifacts='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type environmentName: string
    :param environmentName: [REQUIRED]\nName for the backend environment.\n

    :type stackName: string
    :param stackName: CloudFormation stack name of backend environment.

    :type deploymentArtifacts: string
    :param deploymentArtifacts: Name of deployment artifacts.

    :rtype: dict

ReturnsResponse Syntax
{
    'backendEnvironment': {
        'backendEnvironmentArn': 'string',
        'environmentName': 'string',
        'stackName': 'string',
        'deploymentArtifacts': 'string',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Result structure for create backend environment.

backendEnvironment (dict) --
Backend environment structure for an amplify App.

backendEnvironmentArn (string) --
Arn for a backend environment, part of an Amplify App.

environmentName (string) --
Name for a backend environment, part of an Amplify App.

stackName (string) --
CloudFormation stack name of backend environment.

deploymentArtifacts (string) --
Name of deployment artifacts.

createTime (datetime) --
Creation date and time for a backend environment, part of an Amplify App.

updateTime (datetime) --
Last updated date and time for a backend environment, part of an Amplify App.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'backendEnvironment': {
            'backendEnvironmentArn': 'string',
            'environmentName': 'string',
            'stackName': 'string',
            'deploymentArtifacts': 'string',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.LimitExceededException
    
    """
    pass

def create_branch(appId=None, branchName=None, description=None, stage=None, framework=None, enableNotification=None, enableAutoBuild=None, environmentVariables=None, basicAuthCredentials=None, enableBasicAuth=None, tags=None, buildSpec=None, ttl=None, displayName=None, enablePullRequestPreview=None, pullRequestEnvironmentName=None, backendEnvironmentArn=None):
    """
    Creates a new Branch for an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_branch(
        appId='string',
        branchName='string',
        description='string',
        stage='PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
        framework='string',
        enableNotification=True|False,
        enableAutoBuild=True|False,
        environmentVariables={
            'string': 'string'
        },
        basicAuthCredentials='string',
        enableBasicAuth=True|False,
        tags={
            'string': 'string'
        },
        buildSpec='string',
        ttl='string',
        displayName='string',
        enablePullRequestPreview=True|False,
        pullRequestEnvironmentName='string',
        backendEnvironmentArn='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for the branch.\n

    :type description: string
    :param description: Description for the branch.

    :type stage: string
    :param stage: Stage for the branch.

    :type framework: string
    :param framework: Framework for the branch.

    :type enableNotification: boolean
    :param enableNotification: Enables notifications for the branch.

    :type enableAutoBuild: boolean
    :param enableAutoBuild: Enables auto building for the branch.

    :type environmentVariables: dict
    :param environmentVariables: Environment Variables for the branch.\n\n(string) --\n(string) --\n\n\n\n

    :type basicAuthCredentials: string
    :param basicAuthCredentials: Basic Authorization credentials for the branch.

    :type enableBasicAuth: boolean
    :param enableBasicAuth: Enables Basic Auth for the branch.

    :type tags: dict
    :param tags: Tag for the branch.\n\n(string) --\n(string) --\n\n\n\n

    :type buildSpec: string
    :param buildSpec: BuildSpec for the branch.

    :type ttl: string
    :param ttl: The content TTL for the website in seconds.

    :type displayName: string
    :param displayName: Display name for a branch, will use as the default domain prefix.

    :type enablePullRequestPreview: boolean
    :param enablePullRequestPreview: Enables Pull Request Preview for this branch.

    :type pullRequestEnvironmentName: string
    :param pullRequestEnvironmentName: The Amplify Environment name for the pull request.

    :type backendEnvironmentArn: string
    :param backendEnvironmentArn: ARN for a Backend Environment, part of an Amplify App.

    :rtype: dict

ReturnsResponse Syntax
{
    'branch': {
        'branchArn': 'string',
        'branchName': 'string',
        'description': 'string',
        'tags': {
            'string': 'string'
        },
        'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
        'displayName': 'string',
        'enableNotification': True|False,
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1),
        'environmentVariables': {
            'string': 'string'
        },
        'enableAutoBuild': True|False,
        'customDomains': [
            'string',
        ],
        'framework': 'string',
        'activeJobId': 'string',
        'totalNumberOfJobs': 'string',
        'enableBasicAuth': True|False,
        'thumbnailUrl': 'string',
        'basicAuthCredentials': 'string',
        'buildSpec': 'string',
        'ttl': 'string',
        'associatedResources': [
            'string',
        ],
        'enablePullRequestPreview': True|False,
        'pullRequestEnvironmentName': 'string',
        'destinationBranch': 'string',
        'sourceBranch': 'string',
        'backendEnvironmentArn': 'string'
    }
}


Response Structure

(dict) --
Result structure for create branch request.

branch (dict) --
Branch structure for an Amplify App.

branchArn (string) --
ARN for a branch, part of an Amplify App.

branchName (string) --
Name for a branch, part of an Amplify App.

description (string) --
Description for a branch, part of an Amplify App.

tags (dict) --
Tag for branch for Amplify App.

(string) --
(string) --




stage (string) --
Stage for a branch, part of an Amplify App.

displayName (string) --
Display name for a branch, will use as the default domain prefix.

enableNotification (boolean) --
Enables notifications for a branch, part of an Amplify App.

createTime (datetime) --
Creation date and time for a branch, part of an Amplify App.

updateTime (datetime) --
Last updated date and time for a branch, part of an Amplify App.

environmentVariables (dict) --
Environment Variables specific to a branch, part of an Amplify App.

(string) --
(string) --




enableAutoBuild (boolean) --
Enables auto-building on push for a branch, part of an Amplify App.

customDomains (list) --
Custom domains for a branch, part of an Amplify App.

(string) --


framework (string) --
Framework for a branch, part of an Amplify App.

activeJobId (string) --
Id of the active job for a branch, part of an Amplify App.

totalNumberOfJobs (string) --
Total number of Jobs part of an Amplify App.

enableBasicAuth (boolean) --
Enables Basic Authorization for a branch, part of an Amplify App.

thumbnailUrl (string) --
Thumbnail URL for the branch.

basicAuthCredentials (string) --
Basic Authorization credentials for a branch, part of an Amplify App.

buildSpec (string) --
BuildSpec content for branch for Amplify App.

ttl (string) --
The content TTL for the website in seconds.

associatedResources (list) --
List of custom resources that are linked to this branch.

(string) --


enablePullRequestPreview (boolean) --
Enables Pull Request Preview for this branch.

pullRequestEnvironmentName (string) --
The Amplify Environment name for the pull request.

destinationBranch (string) --
The destination branch if the branch is a pull request branch.

sourceBranch (string) --
The source branch if the branch is a pull request branch.

backendEnvironmentArn (string) --
ARN for a Backend Environment, part of an Amplify App.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.LimitExceededException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'branch': {
            'branchArn': 'string',
            'branchName': 'string',
            'description': 'string',
            'tags': {
                'string': 'string'
            },
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'displayName': 'string',
            'enableNotification': True|False,
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'environmentVariables': {
                'string': 'string'
            },
            'enableAutoBuild': True|False,
            'customDomains': [
                'string',
            ],
            'framework': 'string',
            'activeJobId': 'string',
            'totalNumberOfJobs': 'string',
            'enableBasicAuth': True|False,
            'thumbnailUrl': 'string',
            'basicAuthCredentials': 'string',
            'buildSpec': 'string',
            'ttl': 'string',
            'associatedResources': [
                'string',
            ],
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string',
            'destinationBranch': 'string',
            'sourceBranch': 'string',
            'backendEnvironmentArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_deployment(appId=None, branchName=None, fileMap=None):
    """
    Create a deployment for manual deploy apps. (Apps are not connected to repository)
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_deployment(
        appId='string',
        branchName='string',
        fileMap={
            'string': 'string'
        }
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for the branch, for the Job.\n

    :type fileMap: dict
    :param fileMap: Optional file map that contains file name as the key and file content md5 hash as the value. If this argument is provided, the service will generate different upload url per file. Otherwise, the service will only generate a single upload url for the zipped files.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobId': 'string',
    'fileUploadUrls': {
        'string': 'string'
    },
    'zipUploadUrl': 'string'
}


Response Structure

(dict) --
Result structure for create a new deployment.

jobId (string) --
The jobId for this deployment, will supply to start deployment api.

fileUploadUrls (dict) --
When the fileMap argument is provided in the request, the fileUploadUrls will contain a map of file names to upload url.

(string) --
(string) --




zipUploadUrl (string) --
When the fileMap argument is NOT provided. This zipUploadUrl will be returned.







Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'jobId': 'string',
        'fileUploadUrls': {
            'string': 'string'
        },
        'zipUploadUrl': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def create_domain_association(appId=None, domainName=None, enableAutoSubDomain=None, subDomainSettings=None):
    """
    Create a new DomainAssociation on an App
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_domain_association(
        appId='string',
        domainName='string',
        enableAutoSubDomain=True|False,
        subDomainSettings=[
            {
                'prefix': 'string',
                'branchName': 'string'
            },
        ]
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type domainName: string
    :param domainName: [REQUIRED]\nDomain name for the Domain Association.\n

    :type enableAutoSubDomain: boolean
    :param enableAutoSubDomain: Enables automated creation of Subdomains for branches. (Currently not supported)

    :type subDomainSettings: list
    :param subDomainSettings: [REQUIRED]\nSetting structure for the Subdomain.\n\n(dict) --Setting for the Subdomain.\n\nprefix (string) -- [REQUIRED]Prefix setting for the Subdomain.\n\nbranchName (string) -- [REQUIRED]Branch name setting for the Subdomain.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'domainAssociation': {
        'domainAssociationArn': 'string',
        'domainName': 'string',
        'enableAutoSubDomain': True|False,
        'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'|'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
        'statusReason': 'string',
        'certificateVerificationDNSRecord': 'string',
        'subDomains': [
            {
                'subDomainSetting': {
                    'prefix': 'string',
                    'branchName': 'string'
                },
                'verified': True|False,
                'dnsRecord': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Result structure for the create Domain Association request.

domainAssociation (dict) --
Domain Association structure.

domainAssociationArn (string) --
ARN for the Domain Association.

domainName (string) --
Name of the domain.

enableAutoSubDomain (boolean) --
Enables automated creation of Subdomains for branches. (Currently not supported)

domainStatus (string) --
Status fo the Domain Association.

statusReason (string) --
Reason for the current status of the Domain Association.

certificateVerificationDNSRecord (string) --
DNS Record for certificate verification.

subDomains (list) --
Subdomains for the Domain Association.

(dict) --
Subdomain for the Domain Association.

subDomainSetting (dict) --
Setting structure for the Subdomain.

prefix (string) --
Prefix setting for the Subdomain.

branchName (string) --
Branch name setting for the Subdomain.



verified (boolean) --
Verified status of the Subdomain

dnsRecord (string) --
DNS record for the Subdomain.













Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.LimitExceededException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'domainAssociation': {
            'domainAssociationArn': 'string',
            'domainName': 'string',
            'enableAutoSubDomain': True|False,
            'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'|'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
            'statusReason': 'string',
            'certificateVerificationDNSRecord': 'string',
            'subDomains': [
                {
                    'subDomainSetting': {
                        'prefix': 'string',
                        'branchName': 'string'
                    },
                    'verified': True|False,
                    'dnsRecord': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.LimitExceededException
    Amplify.Client.exceptions.DependentServiceFailureException
    
    """
    pass

def create_webhook(appId=None, branchName=None, description=None):
    """
    Create a new webhook on an App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_webhook(
        appId='string',
        branchName='string',
        description='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for a branch, part of an Amplify App.\n

    :type description: string
    :param description: Description for a webhook.

    :rtype: dict

ReturnsResponse Syntax
{
    'webhook': {
        'webhookArn': 'string',
        'webhookId': 'string',
        'webhookUrl': 'string',
        'branchName': 'string',
        'description': 'string',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Result structure for the create webhook request.

webhook (dict) --
Webhook structure.

webhookArn (string) --
ARN for the webhook.

webhookId (string) --
Id of the webhook.

webhookUrl (string) --
Url of the webhook.

branchName (string) --
Name for a branch, part of an Amplify App.

description (string) --
Description for a webhook.

createTime (datetime) --
Create date / time for a webhook.

updateTime (datetime) --
Update date / time for a webhook.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.LimitExceededException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'webhook': {
            'webhookArn': 'string',
            'webhookId': 'string',
            'webhookUrl': 'string',
            'branchName': 'string',
            'description': 'string',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.LimitExceededException
    Amplify.Client.exceptions.DependentServiceFailureException
    
    """
    pass

def delete_app(appId=None):
    """
    Delete an existing Amplify App by appId.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_app(
        appId='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :rtype: dict
ReturnsResponse Syntax{
    'app': {
        'appId': 'string',
        'appArn': 'string',
        'name': 'string',
        'tags': {
            'string': 'string'
        },
        'description': 'string',
        'repository': 'string',
        'platform': 'WEB',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1),
        'iamServiceRoleArn': 'string',
        'environmentVariables': {
            'string': 'string'
        },
        'defaultDomain': 'string',
        'enableBranchAutoBuild': True|False,
        'enableBasicAuth': True|False,
        'basicAuthCredentials': 'string',
        'customRules': [
            {
                'source': 'string',
                'target': 'string',
                'status': 'string',
                'condition': 'string'
            },
        ],
        'productionBranch': {
            'lastDeployTime': datetime(2015, 1, 1),
            'status': 'string',
            'thumbnailUrl': 'string',
            'branchName': 'string'
        },
        'buildSpec': 'string',
        'enableAutoBranchCreation': True|False,
        'autoBranchCreationPatterns': [
            'string',
        ],
        'autoBranchCreationConfig': {
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'framework': 'string',
            'enableAutoBuild': True|False,
            'environmentVariables': {
                'string': 'string'
            },
            'basicAuthCredentials': 'string',
            'enableBasicAuth': True|False,
            'buildSpec': 'string',
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string'
        }
    }
}


Response Structure

(dict) --Result structure for an Amplify App delete request.

app (dict) --Amplify App represents different branches of a repository for building, deploying, and hosting.

appId (string) --Unique Id for the Amplify App.

appArn (string) --ARN for the Amplify App.

name (string) --Name for the Amplify App.

tags (dict) --Tag for Amplify App.

(string) --
(string) --




description (string) --Description for the Amplify App.

repository (string) --Repository for the Amplify App.

platform (string) --Platform for the Amplify App.

createTime (datetime) --Create date / time for the Amplify App.

updateTime (datetime) --Update date / time for the Amplify App.

iamServiceRoleArn (string) --IAM service role ARN for the Amplify App.

environmentVariables (dict) --Environment Variables for the Amplify App.

(string) --
(string) --




defaultDomain (string) --Default domain for the Amplify App.

enableBranchAutoBuild (boolean) --Enables auto-building of branches for the Amplify App.

enableBasicAuth (boolean) --Enables Basic Authorization for branches for the Amplify App.

basicAuthCredentials (string) --Basic Authorization credentials for branches for the Amplify App.

customRules (list) --Custom redirect / rewrite rules for the Amplify App.

(dict) --Custom rewrite / redirect rule.

source (string) --The source pattern for a URL rewrite or redirect rule.

target (string) --The target pattern for a URL rewrite or redirect rule.

status (string) --The status code for a URL rewrite or redirect rule.

condition (string) --The condition for a URL rewrite or redirect rule, e.g. country code.





productionBranch (dict) --Structure with Production Branch information.

lastDeployTime (datetime) --Last Deploy Time of Production Branch.

status (string) --Status of Production Branch.

thumbnailUrl (string) --Thumbnail URL for Production Branch.

branchName (string) --Branch Name for Production Branch.



buildSpec (string) --BuildSpec content for Amplify App.

enableAutoBranchCreation (boolean) --Enables automated branch creation for the Amplify App.

autoBranchCreationPatterns (list) --Automated branch creation glob patterns for the Amplify App.

(string) --


autoBranchCreationConfig (dict) --Automated branch creation config for the Amplify App.

stage (string) --Stage for the auto created branch.

framework (string) --Framework for the auto created branch.

enableAutoBuild (boolean) --Enables auto building for the auto created branch.

environmentVariables (dict) --Environment Variables for the auto created branch.

(string) --
(string) --




basicAuthCredentials (string) --Basic Authorization credentials for the auto created branch.

enableBasicAuth (boolean) --Enables Basic Auth for the auto created branch.

buildSpec (string) --BuildSpec for the auto created branch.

enablePullRequestPreview (boolean) --Enables Pull Request Preview for auto created branch.

pullRequestEnvironmentName (string) --The Amplify Environment name for the pull request.










Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'app': {
            'appId': 'string',
            'appArn': 'string',
            'name': 'string',
            'tags': {
                'string': 'string'
            },
            'description': 'string',
            'repository': 'string',
            'platform': 'WEB',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'iamServiceRoleArn': 'string',
            'environmentVariables': {
                'string': 'string'
            },
            'defaultDomain': 'string',
            'enableBranchAutoBuild': True|False,
            'enableBasicAuth': True|False,
            'basicAuthCredentials': 'string',
            'customRules': [
                {
                    'source': 'string',
                    'target': 'string',
                    'status': 'string',
                    'condition': 'string'
                },
            ],
            'productionBranch': {
                'lastDeployTime': datetime(2015, 1, 1),
                'status': 'string',
                'thumbnailUrl': 'string',
                'branchName': 'string'
            },
            'buildSpec': 'string',
            'enableAutoBranchCreation': True|False,
            'autoBranchCreationPatterns': [
                'string',
            ],
            'autoBranchCreationConfig': {
                'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
                'framework': 'string',
                'enableAutoBuild': True|False,
                'environmentVariables': {
                    'string': 'string'
                },
                'basicAuthCredentials': 'string',
                'enableBasicAuth': True|False,
                'buildSpec': 'string',
                'enablePullRequestPreview': True|False,
                'pullRequestEnvironmentName': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_backend_environment(appId=None, environmentName=None):
    """
    Delete backend environment for an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_backend_environment(
        appId='string',
        environmentName='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id of an Amplify App.\n

    :type environmentName: string
    :param environmentName: [REQUIRED]\nName of a backend environment of an Amplify App.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'backendEnvironment': {
        'backendEnvironmentArn': 'string',
        'environmentName': 'string',
        'stackName': 'string',
        'deploymentArtifacts': 'string',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Result structure of a delete backend environment result.

backendEnvironment (dict) --
Backend environment structure for an Amplify App.

backendEnvironmentArn (string) --
Arn for a backend environment, part of an Amplify App.

environmentName (string) --
Name for a backend environment, part of an Amplify App.

stackName (string) --
CloudFormation stack name of backend environment.

deploymentArtifacts (string) --
Name of deployment artifacts.

createTime (datetime) --
Creation date and time for a backend environment, part of an Amplify App.

updateTime (datetime) --
Last updated date and time for a backend environment, part of an Amplify App.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'backendEnvironment': {
            'backendEnvironmentArn': 'string',
            'environmentName': 'string',
            'stackName': 'string',
            'deploymentArtifacts': 'string',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.DependentServiceFailureException
    
    """
    pass

def delete_branch(appId=None, branchName=None):
    """
    Deletes a branch for an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_branch(
        appId='string',
        branchName='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for the branch.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'branch': {
        'branchArn': 'string',
        'branchName': 'string',
        'description': 'string',
        'tags': {
            'string': 'string'
        },
        'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
        'displayName': 'string',
        'enableNotification': True|False,
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1),
        'environmentVariables': {
            'string': 'string'
        },
        'enableAutoBuild': True|False,
        'customDomains': [
            'string',
        ],
        'framework': 'string',
        'activeJobId': 'string',
        'totalNumberOfJobs': 'string',
        'enableBasicAuth': True|False,
        'thumbnailUrl': 'string',
        'basicAuthCredentials': 'string',
        'buildSpec': 'string',
        'ttl': 'string',
        'associatedResources': [
            'string',
        ],
        'enablePullRequestPreview': True|False,
        'pullRequestEnvironmentName': 'string',
        'destinationBranch': 'string',
        'sourceBranch': 'string',
        'backendEnvironmentArn': 'string'
    }
}


Response Structure

(dict) --
Result structure for delete branch request.

branch (dict) --
Branch structure for an Amplify App.

branchArn (string) --
ARN for a branch, part of an Amplify App.

branchName (string) --
Name for a branch, part of an Amplify App.

description (string) --
Description for a branch, part of an Amplify App.

tags (dict) --
Tag for branch for Amplify App.

(string) --
(string) --




stage (string) --
Stage for a branch, part of an Amplify App.

displayName (string) --
Display name for a branch, will use as the default domain prefix.

enableNotification (boolean) --
Enables notifications for a branch, part of an Amplify App.

createTime (datetime) --
Creation date and time for a branch, part of an Amplify App.

updateTime (datetime) --
Last updated date and time for a branch, part of an Amplify App.

environmentVariables (dict) --
Environment Variables specific to a branch, part of an Amplify App.

(string) --
(string) --




enableAutoBuild (boolean) --
Enables auto-building on push for a branch, part of an Amplify App.

customDomains (list) --
Custom domains for a branch, part of an Amplify App.

(string) --


framework (string) --
Framework for a branch, part of an Amplify App.

activeJobId (string) --
Id of the active job for a branch, part of an Amplify App.

totalNumberOfJobs (string) --
Total number of Jobs part of an Amplify App.

enableBasicAuth (boolean) --
Enables Basic Authorization for a branch, part of an Amplify App.

thumbnailUrl (string) --
Thumbnail URL for the branch.

basicAuthCredentials (string) --
Basic Authorization credentials for a branch, part of an Amplify App.

buildSpec (string) --
BuildSpec content for branch for Amplify App.

ttl (string) --
The content TTL for the website in seconds.

associatedResources (list) --
List of custom resources that are linked to this branch.

(string) --


enablePullRequestPreview (boolean) --
Enables Pull Request Preview for this branch.

pullRequestEnvironmentName (string) --
The Amplify Environment name for the pull request.

destinationBranch (string) --
The destination branch if the branch is a pull request branch.

sourceBranch (string) --
The source branch if the branch is a pull request branch.

backendEnvironmentArn (string) --
ARN for a Backend Environment, part of an Amplify App.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'branch': {
            'branchArn': 'string',
            'branchName': 'string',
            'description': 'string',
            'tags': {
                'string': 'string'
            },
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'displayName': 'string',
            'enableNotification': True|False,
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'environmentVariables': {
                'string': 'string'
            },
            'enableAutoBuild': True|False,
            'customDomains': [
                'string',
            ],
            'framework': 'string',
            'activeJobId': 'string',
            'totalNumberOfJobs': 'string',
            'enableBasicAuth': True|False,
            'thumbnailUrl': 'string',
            'basicAuthCredentials': 'string',
            'buildSpec': 'string',
            'ttl': 'string',
            'associatedResources': [
                'string',
            ],
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string',
            'destinationBranch': 'string',
            'sourceBranch': 'string',
            'backendEnvironmentArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def delete_domain_association(appId=None, domainName=None):
    """
    Deletes a DomainAssociation.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_domain_association(
        appId='string',
        domainName='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type domainName: string
    :param domainName: [REQUIRED]\nName of the domain.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'domainAssociation': {
        'domainAssociationArn': 'string',
        'domainName': 'string',
        'enableAutoSubDomain': True|False,
        'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'|'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
        'statusReason': 'string',
        'certificateVerificationDNSRecord': 'string',
        'subDomains': [
            {
                'subDomainSetting': {
                    'prefix': 'string',
                    'branchName': 'string'
                },
                'verified': True|False,
                'dnsRecord': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

domainAssociation (dict) --
Structure for Domain Association, which associates a custom domain with an Amplify App.

domainAssociationArn (string) --
ARN for the Domain Association.

domainName (string) --
Name of the domain.

enableAutoSubDomain (boolean) --
Enables automated creation of Subdomains for branches. (Currently not supported)

domainStatus (string) --
Status fo the Domain Association.

statusReason (string) --
Reason for the current status of the Domain Association.

certificateVerificationDNSRecord (string) --
DNS Record for certificate verification.

subDomains (list) --
Subdomains for the Domain Association.

(dict) --
Subdomain for the Domain Association.

subDomainSetting (dict) --
Setting structure for the Subdomain.

prefix (string) --
Prefix setting for the Subdomain.

branchName (string) --
Branch name setting for the Subdomain.



verified (boolean) --
Verified status of the Subdomain

dnsRecord (string) --
DNS record for the Subdomain.













Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'domainAssociation': {
            'domainAssociationArn': 'string',
            'domainName': 'string',
            'enableAutoSubDomain': True|False,
            'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'|'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
            'statusReason': 'string',
            'certificateVerificationDNSRecord': 'string',
            'subDomains': [
                {
                    'subDomainSetting': {
                        'prefix': 'string',
                        'branchName': 'string'
                    },
                    'verified': True|False,
                    'dnsRecord': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.DependentServiceFailureException
    
    """
    pass

def delete_job(appId=None, branchName=None, jobId=None):
    """
    Delete a job, for an Amplify branch, part of Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_job(
        appId='string',
        branchName='string',
        jobId='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for the branch, for the Job.\n

    :type jobId: string
    :param jobId: [REQUIRED]\nUnique Id for the Job.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobSummary': {
        'jobArn': 'string',
        'jobId': 'string',
        'commitId': 'string',
        'commitMessage': 'string',
        'commitTime': datetime(2015, 1, 1),
        'startTime': datetime(2015, 1, 1),
        'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
        'endTime': datetime(2015, 1, 1),
        'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
    }
}


Response Structure

(dict) --
Result structure for the delete job request.

jobSummary (dict) --
Structure for the summary of a Job.

jobArn (string) --
Arn for the Job.

jobId (string) --
Unique Id for the Job.

commitId (string) --
Commit Id from 3rd party repository provider for the Job.

commitMessage (string) --
Commit message from 3rd party repository provider for the Job.

commitTime (datetime) --
Commit date / time for the Job.

startTime (datetime) --
Start date / time for the Job.

status (string) --
Status for the Job.

endTime (datetime) --
End date / time for the Job.

jobType (string) --
Type for the Job. n "RELEASE": Manually released from source by using StartJob API. "RETRY": Manually retried by using StartJob API. "WEB_HOOK": Automatically triggered by WebHooks.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'jobSummary': {
            'jobArn': 'string',
            'jobId': 'string',
            'commitId': 'string',
            'commitMessage': 'string',
            'commitTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
            'endTime': datetime(2015, 1, 1),
            'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.LimitExceededException
    
    """
    pass

def delete_webhook(webhookId=None):
    """
    Deletes a webhook.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_webhook(
        webhookId='string'
    )
    
    
    :type webhookId: string
    :param webhookId: [REQUIRED]\nUnique Id for a webhook.\n

    :rtype: dict
ReturnsResponse Syntax{
    'webhook': {
        'webhookArn': 'string',
        'webhookId': 'string',
        'webhookUrl': 'string',
        'branchName': 'string',
        'description': 'string',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --Result structure for the delete webhook request.

webhook (dict) --Webhook structure.

webhookArn (string) --ARN for the webhook.

webhookId (string) --Id of the webhook.

webhookUrl (string) --Url of the webhook.

branchName (string) --Name for a branch, part of an Amplify App.

description (string) --Description for a webhook.

createTime (datetime) --Create date / time for a webhook.

updateTime (datetime) --Update date / time for a webhook.








Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'webhook': {
            'webhookArn': 'string',
            'webhookId': 'string',
            'webhookUrl': 'string',
            'branchName': 'string',
            'description': 'string',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def generate_access_logs(startTime=None, endTime=None, domainName=None, appId=None):
    """
    Retrieve website access logs for a specific time range via a pre-signed URL.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.generate_access_logs(
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        domainName='string',
        appId='string'
    )
    
    
    :type startTime: datetime
    :param startTime: The time at which the logs should start, inclusive.

    :type endTime: datetime
    :param endTime: The time at which the logs should end, inclusive.

    :type domainName: string
    :param domainName: [REQUIRED]\nName of the domain.\n

    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'logUrl': 'string'
}


Response Structure

(dict) --
Result structure for the generate access logs request.

logUrl (string) --
Pre-signed URL for the requested access logs.







Exceptions

Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException


    :return: {
        'logUrl': 'string'
    }
    
    
    :returns: 
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.InternalFailureException
    
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

def get_app(appId=None):
    """
    Retrieves an existing Amplify App by appId.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_app(
        appId='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :rtype: dict
ReturnsResponse Syntax{
    'app': {
        'appId': 'string',
        'appArn': 'string',
        'name': 'string',
        'tags': {
            'string': 'string'
        },
        'description': 'string',
        'repository': 'string',
        'platform': 'WEB',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1),
        'iamServiceRoleArn': 'string',
        'environmentVariables': {
            'string': 'string'
        },
        'defaultDomain': 'string',
        'enableBranchAutoBuild': True|False,
        'enableBasicAuth': True|False,
        'basicAuthCredentials': 'string',
        'customRules': [
            {
                'source': 'string',
                'target': 'string',
                'status': 'string',
                'condition': 'string'
            },
        ],
        'productionBranch': {
            'lastDeployTime': datetime(2015, 1, 1),
            'status': 'string',
            'thumbnailUrl': 'string',
            'branchName': 'string'
        },
        'buildSpec': 'string',
        'enableAutoBranchCreation': True|False,
        'autoBranchCreationPatterns': [
            'string',
        ],
        'autoBranchCreationConfig': {
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'framework': 'string',
            'enableAutoBuild': True|False,
            'environmentVariables': {
                'string': 'string'
            },
            'basicAuthCredentials': 'string',
            'enableBasicAuth': True|False,
            'buildSpec': 'string',
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string'
        }
    }
}


Response Structure

(dict) --
app (dict) --Amplify App represents different branches of a repository for building, deploying, and hosting.

appId (string) --Unique Id for the Amplify App.

appArn (string) --ARN for the Amplify App.

name (string) --Name for the Amplify App.

tags (dict) --Tag for Amplify App.

(string) --
(string) --




description (string) --Description for the Amplify App.

repository (string) --Repository for the Amplify App.

platform (string) --Platform for the Amplify App.

createTime (datetime) --Create date / time for the Amplify App.

updateTime (datetime) --Update date / time for the Amplify App.

iamServiceRoleArn (string) --IAM service role ARN for the Amplify App.

environmentVariables (dict) --Environment Variables for the Amplify App.

(string) --
(string) --




defaultDomain (string) --Default domain for the Amplify App.

enableBranchAutoBuild (boolean) --Enables auto-building of branches for the Amplify App.

enableBasicAuth (boolean) --Enables Basic Authorization for branches for the Amplify App.

basicAuthCredentials (string) --Basic Authorization credentials for branches for the Amplify App.

customRules (list) --Custom redirect / rewrite rules for the Amplify App.

(dict) --Custom rewrite / redirect rule.

source (string) --The source pattern for a URL rewrite or redirect rule.

target (string) --The target pattern for a URL rewrite or redirect rule.

status (string) --The status code for a URL rewrite or redirect rule.

condition (string) --The condition for a URL rewrite or redirect rule, e.g. country code.





productionBranch (dict) --Structure with Production Branch information.

lastDeployTime (datetime) --Last Deploy Time of Production Branch.

status (string) --Status of Production Branch.

thumbnailUrl (string) --Thumbnail URL for Production Branch.

branchName (string) --Branch Name for Production Branch.



buildSpec (string) --BuildSpec content for Amplify App.

enableAutoBranchCreation (boolean) --Enables automated branch creation for the Amplify App.

autoBranchCreationPatterns (list) --Automated branch creation glob patterns for the Amplify App.

(string) --


autoBranchCreationConfig (dict) --Automated branch creation config for the Amplify App.

stage (string) --Stage for the auto created branch.

framework (string) --Framework for the auto created branch.

enableAutoBuild (boolean) --Enables auto building for the auto created branch.

environmentVariables (dict) --Environment Variables for the auto created branch.

(string) --
(string) --




basicAuthCredentials (string) --Basic Authorization credentials for the auto created branch.

enableBasicAuth (boolean) --Enables Basic Auth for the auto created branch.

buildSpec (string) --BuildSpec for the auto created branch.

enablePullRequestPreview (boolean) --Enables Pull Request Preview for auto created branch.

pullRequestEnvironmentName (string) --The Amplify Environment name for the pull request.










Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException


    :return: {
        'app': {
            'appId': 'string',
            'appArn': 'string',
            'name': 'string',
            'tags': {
                'string': 'string'
            },
            'description': 'string',
            'repository': 'string',
            'platform': 'WEB',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'iamServiceRoleArn': 'string',
            'environmentVariables': {
                'string': 'string'
            },
            'defaultDomain': 'string',
            'enableBranchAutoBuild': True|False,
            'enableBasicAuth': True|False,
            'basicAuthCredentials': 'string',
            'customRules': [
                {
                    'source': 'string',
                    'target': 'string',
                    'status': 'string',
                    'condition': 'string'
                },
            ],
            'productionBranch': {
                'lastDeployTime': datetime(2015, 1, 1),
                'status': 'string',
                'thumbnailUrl': 'string',
                'branchName': 'string'
            },
            'buildSpec': 'string',
            'enableAutoBranchCreation': True|False,
            'autoBranchCreationPatterns': [
                'string',
            ],
            'autoBranchCreationConfig': {
                'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
                'framework': 'string',
                'enableAutoBuild': True|False,
                'environmentVariables': {
                    'string': 'string'
                },
                'basicAuthCredentials': 'string',
                'enableBasicAuth': True|False,
                'buildSpec': 'string',
                'enablePullRequestPreview': True|False,
                'pullRequestEnvironmentName': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_artifact_url(artifactId=None):
    """
    Retrieves artifact info that corresponds to a artifactId.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_artifact_url(
        artifactId='string'
    )
    
    
    :type artifactId: string
    :param artifactId: [REQUIRED]\nUnique Id for a artifact.\n

    :rtype: dict
ReturnsResponse Syntax{
    'artifactId': 'string',
    'artifactUrl': 'string'
}


Response Structure

(dict) --Result structure for the get artifact request.

artifactId (string) --Unique Id for a artifact.

artifactUrl (string) --Presigned url for the artifact.






Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'artifactId': 'string',
        'artifactUrl': 'string'
    }
    
    
    """
    pass

def get_backend_environment(appId=None, environmentName=None):
    """
    Retrieves a backend environment for an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_backend_environment(
        appId='string',
        environmentName='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type environmentName: string
    :param environmentName: [REQUIRED]\nName for the backend environment.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'backendEnvironment': {
        'backendEnvironmentArn': 'string',
        'environmentName': 'string',
        'stackName': 'string',
        'deploymentArtifacts': 'string',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Result structure for get backend environment result.

backendEnvironment (dict) --
Backend environment structure for an an Amplify App.

backendEnvironmentArn (string) --
Arn for a backend environment, part of an Amplify App.

environmentName (string) --
Name for a backend environment, part of an Amplify App.

stackName (string) --
CloudFormation stack name of backend environment.

deploymentArtifacts (string) --
Name of deployment artifacts.

createTime (datetime) --
Creation date and time for a backend environment, part of an Amplify App.

updateTime (datetime) --
Last updated date and time for a backend environment, part of an Amplify App.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException


    :return: {
        'backendEnvironment': {
            'backendEnvironmentArn': 'string',
            'environmentName': 'string',
            'stackName': 'string',
            'deploymentArtifacts': 'string',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.InternalFailureException
    
    """
    pass

def get_branch(appId=None, branchName=None):
    """
    Retrieves a branch for an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_branch(
        appId='string',
        branchName='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for the branch.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'branch': {
        'branchArn': 'string',
        'branchName': 'string',
        'description': 'string',
        'tags': {
            'string': 'string'
        },
        'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
        'displayName': 'string',
        'enableNotification': True|False,
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1),
        'environmentVariables': {
            'string': 'string'
        },
        'enableAutoBuild': True|False,
        'customDomains': [
            'string',
        ],
        'framework': 'string',
        'activeJobId': 'string',
        'totalNumberOfJobs': 'string',
        'enableBasicAuth': True|False,
        'thumbnailUrl': 'string',
        'basicAuthCredentials': 'string',
        'buildSpec': 'string',
        'ttl': 'string',
        'associatedResources': [
            'string',
        ],
        'enablePullRequestPreview': True|False,
        'pullRequestEnvironmentName': 'string',
        'destinationBranch': 'string',
        'sourceBranch': 'string',
        'backendEnvironmentArn': 'string'
    }
}


Response Structure

(dict) --

branch (dict) --
Branch for an Amplify App, which maps to a 3rd party repository branch.

branchArn (string) --
ARN for a branch, part of an Amplify App.

branchName (string) --
Name for a branch, part of an Amplify App.

description (string) --
Description for a branch, part of an Amplify App.

tags (dict) --
Tag for branch for Amplify App.

(string) --
(string) --




stage (string) --
Stage for a branch, part of an Amplify App.

displayName (string) --
Display name for a branch, will use as the default domain prefix.

enableNotification (boolean) --
Enables notifications for a branch, part of an Amplify App.

createTime (datetime) --
Creation date and time for a branch, part of an Amplify App.

updateTime (datetime) --
Last updated date and time for a branch, part of an Amplify App.

environmentVariables (dict) --
Environment Variables specific to a branch, part of an Amplify App.

(string) --
(string) --




enableAutoBuild (boolean) --
Enables auto-building on push for a branch, part of an Amplify App.

customDomains (list) --
Custom domains for a branch, part of an Amplify App.

(string) --


framework (string) --
Framework for a branch, part of an Amplify App.

activeJobId (string) --
Id of the active job for a branch, part of an Amplify App.

totalNumberOfJobs (string) --
Total number of Jobs part of an Amplify App.

enableBasicAuth (boolean) --
Enables Basic Authorization for a branch, part of an Amplify App.

thumbnailUrl (string) --
Thumbnail URL for the branch.

basicAuthCredentials (string) --
Basic Authorization credentials for a branch, part of an Amplify App.

buildSpec (string) --
BuildSpec content for branch for Amplify App.

ttl (string) --
The content TTL for the website in seconds.

associatedResources (list) --
List of custom resources that are linked to this branch.

(string) --


enablePullRequestPreview (boolean) --
Enables Pull Request Preview for this branch.

pullRequestEnvironmentName (string) --
The Amplify Environment name for the pull request.

destinationBranch (string) --
The destination branch if the branch is a pull request branch.

sourceBranch (string) --
The source branch if the branch is a pull request branch.

backendEnvironmentArn (string) --
ARN for a Backend Environment, part of an Amplify App.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException


    :return: {
        'branch': {
            'branchArn': 'string',
            'branchName': 'string',
            'description': 'string',
            'tags': {
                'string': 'string'
            },
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'displayName': 'string',
            'enableNotification': True|False,
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'environmentVariables': {
                'string': 'string'
            },
            'enableAutoBuild': True|False,
            'customDomains': [
                'string',
            ],
            'framework': 'string',
            'activeJobId': 'string',
            'totalNumberOfJobs': 'string',
            'enableBasicAuth': True|False,
            'thumbnailUrl': 'string',
            'basicAuthCredentials': 'string',
            'buildSpec': 'string',
            'ttl': 'string',
            'associatedResources': [
                'string',
            ],
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string',
            'destinationBranch': 'string',
            'sourceBranch': 'string',
            'backendEnvironmentArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_domain_association(appId=None, domainName=None):
    """
    Retrieves domain info that corresponds to an appId and domainName.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_domain_association(
        appId='string',
        domainName='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type domainName: string
    :param domainName: [REQUIRED]\nName of the domain.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'domainAssociation': {
        'domainAssociationArn': 'string',
        'domainName': 'string',
        'enableAutoSubDomain': True|False,
        'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'|'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
        'statusReason': 'string',
        'certificateVerificationDNSRecord': 'string',
        'subDomains': [
            {
                'subDomainSetting': {
                    'prefix': 'string',
                    'branchName': 'string'
                },
                'verified': True|False,
                'dnsRecord': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Result structure for the get Domain Association request.

domainAssociation (dict) --
Domain Association structure.

domainAssociationArn (string) --
ARN for the Domain Association.

domainName (string) --
Name of the domain.

enableAutoSubDomain (boolean) --
Enables automated creation of Subdomains for branches. (Currently not supported)

domainStatus (string) --
Status fo the Domain Association.

statusReason (string) --
Reason for the current status of the Domain Association.

certificateVerificationDNSRecord (string) --
DNS Record for certificate verification.

subDomains (list) --
Subdomains for the Domain Association.

(dict) --
Subdomain for the Domain Association.

subDomainSetting (dict) --
Setting structure for the Subdomain.

prefix (string) --
Prefix setting for the Subdomain.

branchName (string) --
Branch name setting for the Subdomain.



verified (boolean) --
Verified status of the Subdomain

dnsRecord (string) --
DNS record for the Subdomain.













Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException


    :return: {
        'domainAssociation': {
            'domainAssociationArn': 'string',
            'domainName': 'string',
            'enableAutoSubDomain': True|False,
            'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'|'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
            'statusReason': 'string',
            'certificateVerificationDNSRecord': 'string',
            'subDomains': [
                {
                    'subDomainSetting': {
                        'prefix': 'string',
                        'branchName': 'string'
                    },
                    'verified': True|False,
                    'dnsRecord': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.InternalFailureException
    
    """
    pass

def get_job(appId=None, branchName=None, jobId=None):
    """
    Get a job for a branch, part of an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_job(
        appId='string',
        branchName='string',
        jobId='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for the branch, for the Job.\n

    :type jobId: string
    :param jobId: [REQUIRED]\nUnique Id for the Job.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'job': {
        'summary': {
            'jobArn': 'string',
            'jobId': 'string',
            'commitId': 'string',
            'commitMessage': 'string',
            'commitTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
            'endTime': datetime(2015, 1, 1),
            'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
        },
        'steps': [
            {
                'stepName': 'string',
                'startTime': datetime(2015, 1, 1),
                'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                'endTime': datetime(2015, 1, 1),
                'logUrl': 'string',
                'artifactsUrl': 'string',
                'testArtifactsUrl': 'string',
                'testConfigUrl': 'string',
                'screenshots': {
                    'string': 'string'
                },
                'statusReason': 'string',
                'context': 'string'
            },
        ]
    }
}


Response Structure

(dict) --

job (dict) --
Structure for an execution job for an Amplify App.

summary (dict) --
Summary for an execution job for an Amplify App.

jobArn (string) --
Arn for the Job.

jobId (string) --
Unique Id for the Job.

commitId (string) --
Commit Id from 3rd party repository provider for the Job.

commitMessage (string) --
Commit message from 3rd party repository provider for the Job.

commitTime (datetime) --
Commit date / time for the Job.

startTime (datetime) --
Start date / time for the Job.

status (string) --
Status for the Job.

endTime (datetime) --
End date / time for the Job.

jobType (string) --
Type for the Job. n "RELEASE": Manually released from source by using StartJob API. "RETRY": Manually retried by using StartJob API. "WEB_HOOK": Automatically triggered by WebHooks.



steps (list) --
Execution steps for an execution job, for an Amplify App.

(dict) --
Structure for an execution step for an execution job, for an Amplify App.

stepName (string) --
Name of the execution step.

startTime (datetime) --
Start date/ time of the execution step.

status (string) --
Status of the execution step.

endTime (datetime) --
End date/ time of the execution step.

logUrl (string) --
URL to the logs for the execution step.

artifactsUrl (string) --
URL to the artifact for the execution step.

testArtifactsUrl (string) --
URL to the test artifact for the execution step.

testConfigUrl (string) --
URL to the test config for the execution step.

screenshots (dict) --
List of screenshot URLs for the execution step, if relevant.

(string) --
(string) --




statusReason (string) --
The reason for current step status.

context (string) --
The context for current step, will include build image if step is build.













Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'job': {
            'summary': {
                'jobArn': 'string',
                'jobId': 'string',
                'commitId': 'string',
                'commitMessage': 'string',
                'commitTime': datetime(2015, 1, 1),
                'startTime': datetime(2015, 1, 1),
                'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                'endTime': datetime(2015, 1, 1),
                'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
            },
            'steps': [
                {
                    'stepName': 'string',
                    'startTime': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                    'endTime': datetime(2015, 1, 1),
                    'logUrl': 'string',
                    'artifactsUrl': 'string',
                    'testArtifactsUrl': 'string',
                    'testConfigUrl': 'string',
                    'screenshots': {
                        'string': 'string'
                    },
                    'statusReason': 'string',
                    'context': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
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

def get_webhook(webhookId=None):
    """
    Retrieves webhook info that corresponds to a webhookId.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_webhook(
        webhookId='string'
    )
    
    
    :type webhookId: string
    :param webhookId: [REQUIRED]\nUnique Id for a webhook.\n

    :rtype: dict
ReturnsResponse Syntax{
    'webhook': {
        'webhookArn': 'string',
        'webhookId': 'string',
        'webhookUrl': 'string',
        'branchName': 'string',
        'description': 'string',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --Result structure for the get webhook request.

webhook (dict) --Webhook structure.

webhookArn (string) --ARN for the webhook.

webhookId (string) --Id of the webhook.

webhookUrl (string) --Url of the webhook.

branchName (string) --Name for a branch, part of an Amplify App.

description (string) --Description for a webhook.

createTime (datetime) --Create date / time for a webhook.

updateTime (datetime) --Update date / time for a webhook.








Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'webhook': {
            'webhookArn': 'string',
            'webhookId': 'string',
            'webhookUrl': 'string',
            'branchName': 'string',
            'description': 'string',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def list_apps(nextToken=None, maxResults=None):
    """
    Lists existing Amplify Apps.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_apps(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict

ReturnsResponse Syntax
{
    'apps': [
        {
            'appId': 'string',
            'appArn': 'string',
            'name': 'string',
            'tags': {
                'string': 'string'
            },
            'description': 'string',
            'repository': 'string',
            'platform': 'WEB',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'iamServiceRoleArn': 'string',
            'environmentVariables': {
                'string': 'string'
            },
            'defaultDomain': 'string',
            'enableBranchAutoBuild': True|False,
            'enableBasicAuth': True|False,
            'basicAuthCredentials': 'string',
            'customRules': [
                {
                    'source': 'string',
                    'target': 'string',
                    'status': 'string',
                    'condition': 'string'
                },
            ],
            'productionBranch': {
                'lastDeployTime': datetime(2015, 1, 1),
                'status': 'string',
                'thumbnailUrl': 'string',
                'branchName': 'string'
            },
            'buildSpec': 'string',
            'enableAutoBranchCreation': True|False,
            'autoBranchCreationPatterns': [
                'string',
            ],
            'autoBranchCreationConfig': {
                'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
                'framework': 'string',
                'enableAutoBuild': True|False,
                'environmentVariables': {
                    'string': 'string'
                },
                'basicAuthCredentials': 'string',
                'enableBasicAuth': True|False,
                'buildSpec': 'string',
                'enablePullRequestPreview': True|False,
                'pullRequestEnvironmentName': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Result structure for an Amplify App list request.

apps (list) --
List of Amplify Apps.

(dict) --
Amplify App represents different branches of a repository for building, deploying, and hosting.

appId (string) --
Unique Id for the Amplify App.

appArn (string) --
ARN for the Amplify App.

name (string) --
Name for the Amplify App.

tags (dict) --
Tag for Amplify App.

(string) --
(string) --




description (string) --
Description for the Amplify App.

repository (string) --
Repository for the Amplify App.

platform (string) --
Platform for the Amplify App.

createTime (datetime) --
Create date / time for the Amplify App.

updateTime (datetime) --
Update date / time for the Amplify App.

iamServiceRoleArn (string) --
IAM service role ARN for the Amplify App.

environmentVariables (dict) --
Environment Variables for the Amplify App.

(string) --
(string) --




defaultDomain (string) --
Default domain for the Amplify App.

enableBranchAutoBuild (boolean) --
Enables auto-building of branches for the Amplify App.

enableBasicAuth (boolean) --
Enables Basic Authorization for branches for the Amplify App.

basicAuthCredentials (string) --
Basic Authorization credentials for branches for the Amplify App.

customRules (list) --
Custom redirect / rewrite rules for the Amplify App.

(dict) --
Custom rewrite / redirect rule.

source (string) --
The source pattern for a URL rewrite or redirect rule.

target (string) --
The target pattern for a URL rewrite or redirect rule.

status (string) --
The status code for a URL rewrite or redirect rule.

condition (string) --
The condition for a URL rewrite or redirect rule, e.g. country code.





productionBranch (dict) --
Structure with Production Branch information.

lastDeployTime (datetime) --
Last Deploy Time of Production Branch.

status (string) --
Status of Production Branch.

thumbnailUrl (string) --
Thumbnail URL for Production Branch.

branchName (string) --
Branch Name for Production Branch.



buildSpec (string) --
BuildSpec content for Amplify App.

enableAutoBranchCreation (boolean) --
Enables automated branch creation for the Amplify App.

autoBranchCreationPatterns (list) --
Automated branch creation glob patterns for the Amplify App.

(string) --


autoBranchCreationConfig (dict) --
Automated branch creation config for the Amplify App.

stage (string) --
Stage for the auto created branch.

framework (string) --
Framework for the auto created branch.

enableAutoBuild (boolean) --
Enables auto building for the auto created branch.

environmentVariables (dict) --
Environment Variables for the auto created branch.

(string) --
(string) --




basicAuthCredentials (string) --
Basic Authorization credentials for the auto created branch.

enableBasicAuth (boolean) --
Enables Basic Auth for the auto created branch.

buildSpec (string) --
BuildSpec for the auto created branch.

enablePullRequestPreview (boolean) --
Enables Pull Request Preview for auto created branch.

pullRequestEnvironmentName (string) --
The Amplify Environment name for the pull request.







nextToken (string) --
Pagination token. Set to null to start listing Apps from start. If non-null pagination token is returned in a result, then pass its value in here to list more projects.







Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException


    :return: {
        'apps': [
            {
                'appId': 'string',
                'appArn': 'string',
                'name': 'string',
                'tags': {
                    'string': 'string'
                },
                'description': 'string',
                'repository': 'string',
                'platform': 'WEB',
                'createTime': datetime(2015, 1, 1),
                'updateTime': datetime(2015, 1, 1),
                'iamServiceRoleArn': 'string',
                'environmentVariables': {
                    'string': 'string'
                },
                'defaultDomain': 'string',
                'enableBranchAutoBuild': True|False,
                'enableBasicAuth': True|False,
                'basicAuthCredentials': 'string',
                'customRules': [
                    {
                        'source': 'string',
                        'target': 'string',
                        'status': 'string',
                        'condition': 'string'
                    },
                ],
                'productionBranch': {
                    'lastDeployTime': datetime(2015, 1, 1),
                    'status': 'string',
                    'thumbnailUrl': 'string',
                    'branchName': 'string'
                },
                'buildSpec': 'string',
                'enableAutoBranchCreation': True|False,
                'autoBranchCreationPatterns': [
                    'string',
                ],
                'autoBranchCreationConfig': {
                    'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
                    'framework': 'string',
                    'enableAutoBuild': True|False,
                    'environmentVariables': {
                        'string': 'string'
                    },
                    'basicAuthCredentials': 'string',
                    'enableBasicAuth': True|False,
                    'buildSpec': 'string',
                    'enablePullRequestPreview': True|False,
                    'pullRequestEnvironmentName': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_artifacts(appId=None, branchName=None, jobId=None, nextToken=None, maxResults=None):
    """
    List artifacts with an app, a branch, a job and an artifact type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_artifacts(
        appId='string',
        branchName='string',
        jobId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for a branch, part of an Amplify App.\n

    :type jobId: string
    :param jobId: [REQUIRED]\nUnique Id for an Job.\n

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing artifacts from start. If non-null pagination token is returned in a result, then pass its value in here to list more artifacts.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict

ReturnsResponse Syntax
{
    'artifacts': [
        {
            'artifactFileName': 'string',
            'artifactId': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Result structure for the list artifacts request.

artifacts (list) --
List of artifacts.

(dict) --
Structure for artifact.

artifactFileName (string) --
File name for the artifact.

artifactId (string) --
Unique Id for a artifact.





nextToken (string) --
Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries.







Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'artifacts': [
            {
                'artifactFileName': 'string',
                'artifactId': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.LimitExceededException
    
    """
    pass

def list_backend_environments(appId=None, environmentName=None, nextToken=None, maxResults=None):
    """
    Lists backend environments for an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_backend_environments(
        appId='string',
        environmentName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an amplify App.\n

    :type environmentName: string
    :param environmentName: Name of the backend environment

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing backen environments from start. If a non-null pagination token is returned in a result, then pass its value in here to list more backend environments.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict

ReturnsResponse Syntax
{
    'backendEnvironments': [
        {
            'backendEnvironmentArn': 'string',
            'environmentName': 'string',
            'stackName': 'string',
            'deploymentArtifacts': 'string',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Result structure for list backend environments result.

backendEnvironments (list) --
List of backend environments for an Amplify App.

(dict) --
Backend environment for an Amplify App.

backendEnvironmentArn (string) --
Arn for a backend environment, part of an Amplify App.

environmentName (string) --
Name for a backend environment, part of an Amplify App.

stackName (string) --
CloudFormation stack name of backend environment.

deploymentArtifacts (string) --
Name of deployment artifacts.

createTime (datetime) --
Creation date and time for a backend environment, part of an Amplify App.

updateTime (datetime) --
Last updated date and time for a backend environment, part of an Amplify App.





nextToken (string) --
Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries.







Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException


    :return: {
        'backendEnvironments': [
            {
                'backendEnvironmentArn': 'string',
                'environmentName': 'string',
                'stackName': 'string',
                'deploymentArtifacts': 'string',
                'createTime': datetime(2015, 1, 1),
                'updateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.InternalFailureException
    
    """
    pass

def list_branches(appId=None, nextToken=None, maxResults=None):
    """
    Lists branches for an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_branches(
        appId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing branches from start. If a non-null pagination token is returned in a result, then pass its value in here to list more branches.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict

ReturnsResponse Syntax
{
    'branches': [
        {
            'branchArn': 'string',
            'branchName': 'string',
            'description': 'string',
            'tags': {
                'string': 'string'
            },
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'displayName': 'string',
            'enableNotification': True|False,
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'environmentVariables': {
                'string': 'string'
            },
            'enableAutoBuild': True|False,
            'customDomains': [
                'string',
            ],
            'framework': 'string',
            'activeJobId': 'string',
            'totalNumberOfJobs': 'string',
            'enableBasicAuth': True|False,
            'thumbnailUrl': 'string',
            'basicAuthCredentials': 'string',
            'buildSpec': 'string',
            'ttl': 'string',
            'associatedResources': [
                'string',
            ],
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string',
            'destinationBranch': 'string',
            'sourceBranch': 'string',
            'backendEnvironmentArn': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Result structure for list branches request.

branches (list) --
List of branches for an Amplify App.

(dict) --
Branch for an Amplify App, which maps to a 3rd party repository branch.

branchArn (string) --
ARN for a branch, part of an Amplify App.

branchName (string) --
Name for a branch, part of an Amplify App.

description (string) --
Description for a branch, part of an Amplify App.

tags (dict) --
Tag for branch for Amplify App.

(string) --
(string) --




stage (string) --
Stage for a branch, part of an Amplify App.

displayName (string) --
Display name for a branch, will use as the default domain prefix.

enableNotification (boolean) --
Enables notifications for a branch, part of an Amplify App.

createTime (datetime) --
Creation date and time for a branch, part of an Amplify App.

updateTime (datetime) --
Last updated date and time for a branch, part of an Amplify App.

environmentVariables (dict) --
Environment Variables specific to a branch, part of an Amplify App.

(string) --
(string) --




enableAutoBuild (boolean) --
Enables auto-building on push for a branch, part of an Amplify App.

customDomains (list) --
Custom domains for a branch, part of an Amplify App.

(string) --


framework (string) --
Framework for a branch, part of an Amplify App.

activeJobId (string) --
Id of the active job for a branch, part of an Amplify App.

totalNumberOfJobs (string) --
Total number of Jobs part of an Amplify App.

enableBasicAuth (boolean) --
Enables Basic Authorization for a branch, part of an Amplify App.

thumbnailUrl (string) --
Thumbnail URL for the branch.

basicAuthCredentials (string) --
Basic Authorization credentials for a branch, part of an Amplify App.

buildSpec (string) --
BuildSpec content for branch for Amplify App.

ttl (string) --
The content TTL for the website in seconds.

associatedResources (list) --
List of custom resources that are linked to this branch.

(string) --


enablePullRequestPreview (boolean) --
Enables Pull Request Preview for this branch.

pullRequestEnvironmentName (string) --
The Amplify Environment name for the pull request.

destinationBranch (string) --
The destination branch if the branch is a pull request branch.

sourceBranch (string) --
The source branch if the branch is a pull request branch.

backendEnvironmentArn (string) --
ARN for a Backend Environment, part of an Amplify App.





nextToken (string) --
Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries.







Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException


    :return: {
        'branches': [
            {
                'branchArn': 'string',
                'branchName': 'string',
                'description': 'string',
                'tags': {
                    'string': 'string'
                },
                'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
                'displayName': 'string',
                'enableNotification': True|False,
                'createTime': datetime(2015, 1, 1),
                'updateTime': datetime(2015, 1, 1),
                'environmentVariables': {
                    'string': 'string'
                },
                'enableAutoBuild': True|False,
                'customDomains': [
                    'string',
                ],
                'framework': 'string',
                'activeJobId': 'string',
                'totalNumberOfJobs': 'string',
                'enableBasicAuth': True|False,
                'thumbnailUrl': 'string',
                'basicAuthCredentials': 'string',
                'buildSpec': 'string',
                'ttl': 'string',
                'associatedResources': [
                    'string',
                ],
                'enablePullRequestPreview': True|False,
                'pullRequestEnvironmentName': 'string',
                'destinationBranch': 'string',
                'sourceBranch': 'string',
                'backendEnvironmentArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_domain_associations(appId=None, nextToken=None, maxResults=None):
    """
    List domains with an app
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_domain_associations(
        appId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing Apps from start. If non-null pagination token is returned in a result, then pass its value in here to list more projects.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict

ReturnsResponse Syntax
{
    'domainAssociations': [
        {
            'domainAssociationArn': 'string',
            'domainName': 'string',
            'enableAutoSubDomain': True|False,
            'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'|'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
            'statusReason': 'string',
            'certificateVerificationDNSRecord': 'string',
            'subDomains': [
                {
                    'subDomainSetting': {
                        'prefix': 'string',
                        'branchName': 'string'
                    },
                    'verified': True|False,
                    'dnsRecord': 'string'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Result structure for the list Domain Association request.

domainAssociations (list) --
List of Domain Associations.

(dict) --
Structure for Domain Association, which associates a custom domain with an Amplify App.

domainAssociationArn (string) --
ARN for the Domain Association.

domainName (string) --
Name of the domain.

enableAutoSubDomain (boolean) --
Enables automated creation of Subdomains for branches. (Currently not supported)

domainStatus (string) --
Status fo the Domain Association.

statusReason (string) --
Reason for the current status of the Domain Association.

certificateVerificationDNSRecord (string) --
DNS Record for certificate verification.

subDomains (list) --
Subdomains for the Domain Association.

(dict) --
Subdomain for the Domain Association.

subDomainSetting (dict) --
Setting structure for the Subdomain.

prefix (string) --
Prefix setting for the Subdomain.

branchName (string) --
Branch name setting for the Subdomain.



verified (boolean) --
Verified status of the Subdomain

dnsRecord (string) --
DNS record for the Subdomain.









nextToken (string) --
Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries.







Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException


    :return: {
        'domainAssociations': [
            {
                'domainAssociationArn': 'string',
                'domainName': 'string',
                'enableAutoSubDomain': True|False,
                'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'|'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
                'statusReason': 'string',
                'certificateVerificationDNSRecord': 'string',
                'subDomains': [
                    {
                        'subDomainSetting': {
                            'prefix': 'string',
                            'branchName': 'string'
                        },
                        'verified': True|False,
                        'dnsRecord': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.InternalFailureException
    
    """
    pass

def list_jobs(appId=None, branchName=None, nextToken=None, maxResults=None):
    """
    List Jobs for a branch, part of an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_jobs(
        appId='string',
        branchName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for a branch.\n

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing steps from start. If a non-null pagination token is returned in a result, then pass its value in here to list more steps.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict

ReturnsResponse Syntax
{
    'jobSummaries': [
        {
            'jobArn': 'string',
            'jobId': 'string',
            'commitId': 'string',
            'commitMessage': 'string',
            'commitTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
            'endTime': datetime(2015, 1, 1),
            'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Maximum number of records to list in a single response.

jobSummaries (list) --
Result structure for list job result request.

(dict) --
Structure for the summary of a Job.

jobArn (string) --
Arn for the Job.

jobId (string) --
Unique Id for the Job.

commitId (string) --
Commit Id from 3rd party repository provider for the Job.

commitMessage (string) --
Commit message from 3rd party repository provider for the Job.

commitTime (datetime) --
Commit date / time for the Job.

startTime (datetime) --
Start date / time for the Job.

status (string) --
Status for the Job.

endTime (datetime) --
End date / time for the Job.

jobType (string) --
Type for the Job. n "RELEASE": Manually released from source by using StartJob API. "RETRY": Manually retried by using StartJob API. "WEB_HOOK": Automatically triggered by WebHooks.





nextToken (string) --
Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries.







Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'jobSummaries': [
            {
                'jobArn': 'string',
                'jobId': 'string',
                'commitId': 'string',
                'commitMessage': 'string',
                'commitTime': datetime(2015, 1, 1),
                'startTime': datetime(2015, 1, 1),
                'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
                'endTime': datetime(2015, 1, 1),
                'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.LimitExceededException
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    List tags for resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nResource arn used to list tags.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --Response for list tags.

tags (dict) --Tags result for response.

(string) --
(string) --









Exceptions

Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.ResourceNotFoundException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_webhooks(appId=None, nextToken=None, maxResults=None):
    """
    List webhooks with an app.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_webhooks(
        appId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type nextToken: string
    :param nextToken: Pagination token. Set to null to start listing webhooks from start. If non-null pagination token is returned in a result, then pass its value in here to list more webhooks.

    :type maxResults: integer
    :param maxResults: Maximum number of records to list in a single response.

    :rtype: dict

ReturnsResponse Syntax
{
    'webhooks': [
        {
            'webhookArn': 'string',
            'webhookId': 'string',
            'webhookUrl': 'string',
            'branchName': 'string',
            'description': 'string',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Result structure for the list webhooks request.

webhooks (list) --
List of webhooks.

(dict) --
Structure for webhook, which associates a webhook with an Amplify App.

webhookArn (string) --
ARN for the webhook.

webhookId (string) --
Id of the webhook.

webhookUrl (string) --
Url of the webhook.

branchName (string) --
Name for a branch, part of an Amplify App.

description (string) --
Description for a webhook.

createTime (datetime) --
Create date / time for a webhook.

updateTime (datetime) --
Update date / time for a webhook.





nextToken (string) --
Pagination token. If non-null pagination token is returned in a result, then pass its value in another request to fetch more entries.







Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'webhooks': [
            {
                'webhookArn': 'string',
                'webhookId': 'string',
                'webhookUrl': 'string',
                'branchName': 'string',
                'description': 'string',
                'createTime': datetime(2015, 1, 1),
                'updateTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.LimitExceededException
    
    """
    pass

def start_deployment(appId=None, branchName=None, jobId=None, sourceUrl=None):
    """
    Start a deployment for manual deploy apps. (Apps are not connected to repository)
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_deployment(
        appId='string',
        branchName='string',
        jobId='string',
        sourceUrl='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for the branch, for the Job.\n

    :type jobId: string
    :param jobId: The job id for this deployment, generated by create deployment request.

    :type sourceUrl: string
    :param sourceUrl: The sourceUrl for this deployment, used when calling start deployment without create deployment. SourceUrl can be any HTTP GET url that is public accessible and downloads a single zip.

    :rtype: dict

ReturnsResponse Syntax
{
    'jobSummary': {
        'jobArn': 'string',
        'jobId': 'string',
        'commitId': 'string',
        'commitMessage': 'string',
        'commitTime': datetime(2015, 1, 1),
        'startTime': datetime(2015, 1, 1),
        'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
        'endTime': datetime(2015, 1, 1),
        'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
    }
}


Response Structure

(dict) --
Result structure for start a deployment.

jobSummary (dict) --
Summary for the Job.

jobArn (string) --
Arn for the Job.

jobId (string) --
Unique Id for the Job.

commitId (string) --
Commit Id from 3rd party repository provider for the Job.

commitMessage (string) --
Commit message from 3rd party repository provider for the Job.

commitTime (datetime) --
Commit date / time for the Job.

startTime (datetime) --
Start date / time for the Job.

status (string) --
Status for the Job.

endTime (datetime) --
End date / time for the Job.

jobType (string) --
Type for the Job. n "RELEASE": Manually released from source by using StartJob API. "RETRY": Manually retried by using StartJob API. "WEB_HOOK": Automatically triggered by WebHooks.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'jobSummary': {
            'jobArn': 'string',
            'jobId': 'string',
            'commitId': 'string',
            'commitMessage': 'string',
            'commitTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
            'endTime': datetime(2015, 1, 1),
            'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.LimitExceededException
    
    """
    pass

def start_job(appId=None, branchName=None, jobId=None, jobType=None, jobReason=None, commitId=None, commitMessage=None, commitTime=None):
    """
    Starts a new job for a branch, part of an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_job(
        appId='string',
        branchName='string',
        jobId='string',
        jobType='RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK',
        jobReason='string',
        commitId='string',
        commitMessage='string',
        commitTime=datetime(2015, 1, 1)
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for the branch, for the Job.\n

    :type jobId: string
    :param jobId: Unique Id for an existing job. Required for 'RETRY' JobType.

    :type jobType: string
    :param jobType: [REQUIRED]\nType for the Job. Available JobTypes are: n 'RELEASE': Start a new job with the latest change from the specified branch. Only available for apps that have connected to a repository. 'RETRY': Retry an existing job. JobId is required for this type of job.\n

    :type jobReason: string
    :param jobReason: Descriptive reason for starting this job.

    :type commitId: string
    :param commitId: Commit Id from 3rd party repository provider for the Job.

    :type commitMessage: string
    :param commitMessage: Commit message from 3rd party repository provider for the Job.

    :type commitTime: datetime
    :param commitTime: Commit date / time for the Job.

    :rtype: dict

ReturnsResponse Syntax
{
    'jobSummary': {
        'jobArn': 'string',
        'jobId': 'string',
        'commitId': 'string',
        'commitMessage': 'string',
        'commitTime': datetime(2015, 1, 1),
        'startTime': datetime(2015, 1, 1),
        'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
        'endTime': datetime(2015, 1, 1),
        'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
    }
}


Response Structure

(dict) --
Result structure for run job request.

jobSummary (dict) --
Summary for the Job.

jobArn (string) --
Arn for the Job.

jobId (string) --
Unique Id for the Job.

commitId (string) --
Commit Id from 3rd party repository provider for the Job.

commitMessage (string) --
Commit message from 3rd party repository provider for the Job.

commitTime (datetime) --
Commit date / time for the Job.

startTime (datetime) --
Start date / time for the Job.

status (string) --
Status for the Job.

endTime (datetime) --
End date / time for the Job.

jobType (string) --
Type for the Job. n "RELEASE": Manually released from source by using StartJob API. "RETRY": Manually retried by using StartJob API. "WEB_HOOK": Automatically triggered by WebHooks.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'jobSummary': {
            'jobArn': 'string',
            'jobId': 'string',
            'commitId': 'string',
            'commitMessage': 'string',
            'commitTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
            'endTime': datetime(2015, 1, 1),
            'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.LimitExceededException
    
    """
    pass

def stop_job(appId=None, branchName=None, jobId=None):
    """
    Stop a job that is in progress, for an Amplify branch, part of Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_job(
        appId='string',
        branchName='string',
        jobId='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for the branch, for the Job.\n

    :type jobId: string
    :param jobId: [REQUIRED]\nUnique Id for the Job.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobSummary': {
        'jobArn': 'string',
        'jobId': 'string',
        'commitId': 'string',
        'commitMessage': 'string',
        'commitTime': datetime(2015, 1, 1),
        'startTime': datetime(2015, 1, 1),
        'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
        'endTime': datetime(2015, 1, 1),
        'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
    }
}


Response Structure

(dict) --
Result structure for the stop job request.

jobSummary (dict) --
Summary for the Job.

jobArn (string) --
Arn for the Job.

jobId (string) --
Unique Id for the Job.

commitId (string) --
Commit Id from 3rd party repository provider for the Job.

commitMessage (string) --
Commit message from 3rd party repository provider for the Job.

commitTime (datetime) --
Commit date / time for the Job.

startTime (datetime) --
Start date / time for the Job.

status (string) --
Status for the Job.

endTime (datetime) --
End date / time for the Job.

jobType (string) --
Type for the Job. n "RELEASE": Manually released from source by using StartJob API. "RETRY": Manually retried by using StartJob API. "WEB_HOOK": Automatically triggered by WebHooks.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.LimitExceededException


    :return: {
        'jobSummary': {
            'jobArn': 'string',
            'jobId': 'string',
            'commitId': 'string',
            'commitMessage': 'string',
            'commitTime': datetime(2015, 1, 1),
            'startTime': datetime(2015, 1, 1),
            'status': 'PENDING'|'PROVISIONING'|'RUNNING'|'FAILED'|'SUCCEED'|'CANCELLING'|'CANCELLED',
            'endTime': datetime(2015, 1, 1),
            'jobType': 'RELEASE'|'RETRY'|'MANUAL'|'WEB_HOOK'
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.LimitExceededException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Tag resource with tag key and value.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nResource arn used to tag resource.\n

    :type tags: dict
    :param tags: [REQUIRED]\nTags used to tag resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response for tag resource.





Exceptions

Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Untag resource with resourceArn.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nResource arn used to untag resource.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nTag keys used to untag resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
Response for untag resource.





Exceptions

Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_app(appId=None, name=None, description=None, platform=None, iamServiceRoleArn=None, environmentVariables=None, enableBranchAutoBuild=None, enableBasicAuth=None, basicAuthCredentials=None, customRules=None, buildSpec=None, enableAutoBranchCreation=None, autoBranchCreationPatterns=None, autoBranchCreationConfig=None, repository=None, oauthToken=None, accessToken=None):
    """
    Updates an existing Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_app(
        appId='string',
        name='string',
        description='string',
        platform='WEB',
        iamServiceRoleArn='string',
        environmentVariables={
            'string': 'string'
        },
        enableBranchAutoBuild=True|False,
        enableBasicAuth=True|False,
        basicAuthCredentials='string',
        customRules=[
            {
                'source': 'string',
                'target': 'string',
                'status': 'string',
                'condition': 'string'
            },
        ],
        buildSpec='string',
        enableAutoBranchCreation=True|False,
        autoBranchCreationPatterns=[
            'string',
        ],
        autoBranchCreationConfig={
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'framework': 'string',
            'enableAutoBuild': True|False,
            'environmentVariables': {
                'string': 'string'
            },
            'basicAuthCredentials': 'string',
            'enableBasicAuth': True|False,
            'buildSpec': 'string',
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string'
        },
        repository='string',
        oauthToken='string',
        accessToken='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type name: string
    :param name: Name for an Amplify App.

    :type description: string
    :param description: Description for an Amplify App.

    :type platform: string
    :param platform: Platform for an Amplify App.

    :type iamServiceRoleArn: string
    :param iamServiceRoleArn: IAM service role for an Amplify App.

    :type environmentVariables: dict
    :param environmentVariables: Environment Variables for an Amplify App.\n\n(string) --\n(string) --\n\n\n\n

    :type enableBranchAutoBuild: boolean
    :param enableBranchAutoBuild: Enables branch auto-building for an Amplify App.

    :type enableBasicAuth: boolean
    :param enableBasicAuth: Enables Basic Authorization for an Amplify App.

    :type basicAuthCredentials: string
    :param basicAuthCredentials: Basic Authorization credentials for an Amplify App.

    :type customRules: list
    :param customRules: Custom redirect / rewrite rules for an Amplify App.\n\n(dict) --Custom rewrite / redirect rule.\n\nsource (string) -- [REQUIRED]The source pattern for a URL rewrite or redirect rule.\n\ntarget (string) -- [REQUIRED]The target pattern for a URL rewrite or redirect rule.\n\nstatus (string) --The status code for a URL rewrite or redirect rule.\n\ncondition (string) --The condition for a URL rewrite or redirect rule, e.g. country code.\n\n\n\n\n

    :type buildSpec: string
    :param buildSpec: BuildSpec for an Amplify App.

    :type enableAutoBranchCreation: boolean
    :param enableAutoBranchCreation: Enables automated branch creation for the Amplify App.

    :type autoBranchCreationPatterns: list
    :param autoBranchCreationPatterns: Automated branch creation glob patterns for the Amplify App.\n\n(string) --\n\n

    :type autoBranchCreationConfig: dict
    :param autoBranchCreationConfig: Automated branch creation branchConfig for the Amplify App.\n\nstage (string) --Stage for the auto created branch.\n\nframework (string) --Framework for the auto created branch.\n\nenableAutoBuild (boolean) --Enables auto building for the auto created branch.\n\nenvironmentVariables (dict) --Environment Variables for the auto created branch.\n\n(string) --\n(string) --\n\n\n\n\nbasicAuthCredentials (string) --Basic Authorization credentials for the auto created branch.\n\nenableBasicAuth (boolean) --Enables Basic Auth for the auto created branch.\n\nbuildSpec (string) --BuildSpec for the auto created branch.\n\nenablePullRequestPreview (boolean) --Enables Pull Request Preview for auto created branch.\n\npullRequestEnvironmentName (string) --The Amplify Environment name for the pull request.\n\n\n

    :type repository: string
    :param repository: Repository for an Amplify App

    :type oauthToken: string
    :param oauthToken: OAuth token for 3rd party source control system for an Amplify App, used to create webhook and read-only deploy key. OAuth token is not stored.

    :type accessToken: string
    :param accessToken: Personal Access token for 3rd party source control system for an Amplify App, used to create webhook and read-only deploy key. Token is not stored.

    :rtype: dict

ReturnsResponse Syntax
{
    'app': {
        'appId': 'string',
        'appArn': 'string',
        'name': 'string',
        'tags': {
            'string': 'string'
        },
        'description': 'string',
        'repository': 'string',
        'platform': 'WEB',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1),
        'iamServiceRoleArn': 'string',
        'environmentVariables': {
            'string': 'string'
        },
        'defaultDomain': 'string',
        'enableBranchAutoBuild': True|False,
        'enableBasicAuth': True|False,
        'basicAuthCredentials': 'string',
        'customRules': [
            {
                'source': 'string',
                'target': 'string',
                'status': 'string',
                'condition': 'string'
            },
        ],
        'productionBranch': {
            'lastDeployTime': datetime(2015, 1, 1),
            'status': 'string',
            'thumbnailUrl': 'string',
            'branchName': 'string'
        },
        'buildSpec': 'string',
        'enableAutoBranchCreation': True|False,
        'autoBranchCreationPatterns': [
            'string',
        ],
        'autoBranchCreationConfig': {
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'framework': 'string',
            'enableAutoBuild': True|False,
            'environmentVariables': {
                'string': 'string'
            },
            'basicAuthCredentials': 'string',
            'enableBasicAuth': True|False,
            'buildSpec': 'string',
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string'
        }
    }
}


Response Structure

(dict) --
Result structure for an Amplify App update request.

app (dict) --
App structure for the updated App.

appId (string) --
Unique Id for the Amplify App.

appArn (string) --
ARN for the Amplify App.

name (string) --
Name for the Amplify App.

tags (dict) --
Tag for Amplify App.

(string) --
(string) --




description (string) --
Description for the Amplify App.

repository (string) --
Repository for the Amplify App.

platform (string) --
Platform for the Amplify App.

createTime (datetime) --
Create date / time for the Amplify App.

updateTime (datetime) --
Update date / time for the Amplify App.

iamServiceRoleArn (string) --
IAM service role ARN for the Amplify App.

environmentVariables (dict) --
Environment Variables for the Amplify App.

(string) --
(string) --




defaultDomain (string) --
Default domain for the Amplify App.

enableBranchAutoBuild (boolean) --
Enables auto-building of branches for the Amplify App.

enableBasicAuth (boolean) --
Enables Basic Authorization for branches for the Amplify App.

basicAuthCredentials (string) --
Basic Authorization credentials for branches for the Amplify App.

customRules (list) --
Custom redirect / rewrite rules for the Amplify App.

(dict) --
Custom rewrite / redirect rule.

source (string) --
The source pattern for a URL rewrite or redirect rule.

target (string) --
The target pattern for a URL rewrite or redirect rule.

status (string) --
The status code for a URL rewrite or redirect rule.

condition (string) --
The condition for a URL rewrite or redirect rule, e.g. country code.





productionBranch (dict) --
Structure with Production Branch information.

lastDeployTime (datetime) --
Last Deploy Time of Production Branch.

status (string) --
Status of Production Branch.

thumbnailUrl (string) --
Thumbnail URL for Production Branch.

branchName (string) --
Branch Name for Production Branch.



buildSpec (string) --
BuildSpec content for Amplify App.

enableAutoBranchCreation (boolean) --
Enables automated branch creation for the Amplify App.

autoBranchCreationPatterns (list) --
Automated branch creation glob patterns for the Amplify App.

(string) --


autoBranchCreationConfig (dict) --
Automated branch creation config for the Amplify App.

stage (string) --
Stage for the auto created branch.

framework (string) --
Framework for the auto created branch.

enableAutoBuild (boolean) --
Enables auto building for the auto created branch.

environmentVariables (dict) --
Environment Variables for the auto created branch.

(string) --
(string) --




basicAuthCredentials (string) --
Basic Authorization credentials for the auto created branch.

enableBasicAuth (boolean) --
Enables Basic Auth for the auto created branch.

buildSpec (string) --
BuildSpec for the auto created branch.

enablePullRequestPreview (boolean) --
Enables Pull Request Preview for auto created branch.

pullRequestEnvironmentName (string) --
The Amplify Environment name for the pull request.











Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.InternalFailureException


    :return: {
        'app': {
            'appId': 'string',
            'appArn': 'string',
            'name': 'string',
            'tags': {
                'string': 'string'
            },
            'description': 'string',
            'repository': 'string',
            'platform': 'WEB',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'iamServiceRoleArn': 'string',
            'environmentVariables': {
                'string': 'string'
            },
            'defaultDomain': 'string',
            'enableBranchAutoBuild': True|False,
            'enableBasicAuth': True|False,
            'basicAuthCredentials': 'string',
            'customRules': [
                {
                    'source': 'string',
                    'target': 'string',
                    'status': 'string',
                    'condition': 'string'
                },
            ],
            'productionBranch': {
                'lastDeployTime': datetime(2015, 1, 1),
                'status': 'string',
                'thumbnailUrl': 'string',
                'branchName': 'string'
            },
            'buildSpec': 'string',
            'enableAutoBranchCreation': True|False,
            'autoBranchCreationPatterns': [
                'string',
            ],
            'autoBranchCreationConfig': {
                'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
                'framework': 'string',
                'enableAutoBuild': True|False,
                'environmentVariables': {
                    'string': 'string'
                },
                'basicAuthCredentials': 'string',
                'enableBasicAuth': True|False,
                'buildSpec': 'string',
                'enablePullRequestPreview': True|False,
                'pullRequestEnvironmentName': 'string'
            }
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_branch(appId=None, branchName=None, description=None, framework=None, stage=None, enableNotification=None, enableAutoBuild=None, environmentVariables=None, basicAuthCredentials=None, enableBasicAuth=None, buildSpec=None, ttl=None, displayName=None, enablePullRequestPreview=None, pullRequestEnvironmentName=None, backendEnvironmentArn=None):
    """
    Updates a branch for an Amplify App.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_branch(
        appId='string',
        branchName='string',
        description='string',
        framework='string',
        stage='PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
        enableNotification=True|False,
        enableAutoBuild=True|False,
        environmentVariables={
            'string': 'string'
        },
        basicAuthCredentials='string',
        enableBasicAuth=True|False,
        buildSpec='string',
        ttl='string',
        displayName='string',
        enablePullRequestPreview=True|False,
        pullRequestEnvironmentName='string',
        backendEnvironmentArn='string'
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nName for the branch.\n

    :type description: string
    :param description: Description for the branch.

    :type framework: string
    :param framework: Framework for the branch.

    :type stage: string
    :param stage: Stage for the branch.

    :type enableNotification: boolean
    :param enableNotification: Enables notifications for the branch.

    :type enableAutoBuild: boolean
    :param enableAutoBuild: Enables auto building for the branch.

    :type environmentVariables: dict
    :param environmentVariables: Environment Variables for the branch.\n\n(string) --\n(string) --\n\n\n\n

    :type basicAuthCredentials: string
    :param basicAuthCredentials: Basic Authorization credentials for the branch.

    :type enableBasicAuth: boolean
    :param enableBasicAuth: Enables Basic Auth for the branch.

    :type buildSpec: string
    :param buildSpec: BuildSpec for the branch.

    :type ttl: string
    :param ttl: The content TTL for the website in seconds.

    :type displayName: string
    :param displayName: Display name for a branch, will use as the default domain prefix.

    :type enablePullRequestPreview: boolean
    :param enablePullRequestPreview: Enables Pull Request Preview for this branch.

    :type pullRequestEnvironmentName: string
    :param pullRequestEnvironmentName: The Amplify Environment name for the pull request.

    :type backendEnvironmentArn: string
    :param backendEnvironmentArn: ARN for a Backend Environment, part of an Amplify App.

    :rtype: dict

ReturnsResponse Syntax
{
    'branch': {
        'branchArn': 'string',
        'branchName': 'string',
        'description': 'string',
        'tags': {
            'string': 'string'
        },
        'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
        'displayName': 'string',
        'enableNotification': True|False,
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1),
        'environmentVariables': {
            'string': 'string'
        },
        'enableAutoBuild': True|False,
        'customDomains': [
            'string',
        ],
        'framework': 'string',
        'activeJobId': 'string',
        'totalNumberOfJobs': 'string',
        'enableBasicAuth': True|False,
        'thumbnailUrl': 'string',
        'basicAuthCredentials': 'string',
        'buildSpec': 'string',
        'ttl': 'string',
        'associatedResources': [
            'string',
        ],
        'enablePullRequestPreview': True|False,
        'pullRequestEnvironmentName': 'string',
        'destinationBranch': 'string',
        'sourceBranch': 'string',
        'backendEnvironmentArn': 'string'
    }
}


Response Structure

(dict) --
Result structure for update branch request.

branch (dict) --
Branch structure for an Amplify App.

branchArn (string) --
ARN for a branch, part of an Amplify App.

branchName (string) --
Name for a branch, part of an Amplify App.

description (string) --
Description for a branch, part of an Amplify App.

tags (dict) --
Tag for branch for Amplify App.

(string) --
(string) --




stage (string) --
Stage for a branch, part of an Amplify App.

displayName (string) --
Display name for a branch, will use as the default domain prefix.

enableNotification (boolean) --
Enables notifications for a branch, part of an Amplify App.

createTime (datetime) --
Creation date and time for a branch, part of an Amplify App.

updateTime (datetime) --
Last updated date and time for a branch, part of an Amplify App.

environmentVariables (dict) --
Environment Variables specific to a branch, part of an Amplify App.

(string) --
(string) --




enableAutoBuild (boolean) --
Enables auto-building on push for a branch, part of an Amplify App.

customDomains (list) --
Custom domains for a branch, part of an Amplify App.

(string) --


framework (string) --
Framework for a branch, part of an Amplify App.

activeJobId (string) --
Id of the active job for a branch, part of an Amplify App.

totalNumberOfJobs (string) --
Total number of Jobs part of an Amplify App.

enableBasicAuth (boolean) --
Enables Basic Authorization for a branch, part of an Amplify App.

thumbnailUrl (string) --
Thumbnail URL for the branch.

basicAuthCredentials (string) --
Basic Authorization credentials for a branch, part of an Amplify App.

buildSpec (string) --
BuildSpec content for branch for Amplify App.

ttl (string) --
The content TTL for the website in seconds.

associatedResources (list) --
List of custom resources that are linked to this branch.

(string) --


enablePullRequestPreview (boolean) --
Enables Pull Request Preview for this branch.

pullRequestEnvironmentName (string) --
The Amplify Environment name for the pull request.

destinationBranch (string) --
The destination branch if the branch is a pull request branch.

sourceBranch (string) --
The source branch if the branch is a pull request branch.

backendEnvironmentArn (string) --
ARN for a Backend Environment, part of an Amplify App.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'branch': {
            'branchArn': 'string',
            'branchName': 'string',
            'description': 'string',
            'tags': {
                'string': 'string'
            },
            'stage': 'PRODUCTION'|'BETA'|'DEVELOPMENT'|'EXPERIMENTAL'|'PULL_REQUEST',
            'displayName': 'string',
            'enableNotification': True|False,
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1),
            'environmentVariables': {
                'string': 'string'
            },
            'enableAutoBuild': True|False,
            'customDomains': [
                'string',
            ],
            'framework': 'string',
            'activeJobId': 'string',
            'totalNumberOfJobs': 'string',
            'enableBasicAuth': True|False,
            'thumbnailUrl': 'string',
            'basicAuthCredentials': 'string',
            'buildSpec': 'string',
            'ttl': 'string',
            'associatedResources': [
                'string',
            ],
            'enablePullRequestPreview': True|False,
            'pullRequestEnvironmentName': 'string',
            'destinationBranch': 'string',
            'sourceBranch': 'string',
            'backendEnvironmentArn': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def update_domain_association(appId=None, domainName=None, enableAutoSubDomain=None, subDomainSettings=None):
    """
    Create a new DomainAssociation on an App
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_domain_association(
        appId='string',
        domainName='string',
        enableAutoSubDomain=True|False,
        subDomainSettings=[
            {
                'prefix': 'string',
                'branchName': 'string'
            },
        ]
    )
    
    
    :type appId: string
    :param appId: [REQUIRED]\nUnique Id for an Amplify App.\n

    :type domainName: string
    :param domainName: [REQUIRED]\nName of the domain.\n

    :type enableAutoSubDomain: boolean
    :param enableAutoSubDomain: Enables automated creation of Subdomains for branches. (Currently not supported)

    :type subDomainSettings: list
    :param subDomainSettings: [REQUIRED]\nSetting structure for the Subdomain.\n\n(dict) --Setting for the Subdomain.\n\nprefix (string) -- [REQUIRED]Prefix setting for the Subdomain.\n\nbranchName (string) -- [REQUIRED]Branch name setting for the Subdomain.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'domainAssociation': {
        'domainAssociationArn': 'string',
        'domainName': 'string',
        'enableAutoSubDomain': True|False,
        'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'|'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
        'statusReason': 'string',
        'certificateVerificationDNSRecord': 'string',
        'subDomains': [
            {
                'subDomainSetting': {
                    'prefix': 'string',
                    'branchName': 'string'
                },
                'verified': True|False,
                'dnsRecord': 'string'
            },
        ]
    }
}


Response Structure

(dict) --
Result structure for the update Domain Association request.

domainAssociation (dict) --
Domain Association structure.

domainAssociationArn (string) --
ARN for the Domain Association.

domainName (string) --
Name of the domain.

enableAutoSubDomain (boolean) --
Enables automated creation of Subdomains for branches. (Currently not supported)

domainStatus (string) --
Status fo the Domain Association.

statusReason (string) --
Reason for the current status of the Domain Association.

certificateVerificationDNSRecord (string) --
DNS Record for certificate verification.

subDomains (list) --
Subdomains for the Domain Association.

(dict) --
Subdomain for the Domain Association.

subDomainSetting (dict) --
Setting structure for the Subdomain.

prefix (string) --
Prefix setting for the Subdomain.

branchName (string) --
Branch name setting for the Subdomain.



verified (boolean) --
Verified status of the Subdomain

dnsRecord (string) --
DNS record for the Subdomain.













Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'domainAssociation': {
            'domainAssociationArn': 'string',
            'domainName': 'string',
            'enableAutoSubDomain': True|False,
            'domainStatus': 'PENDING_VERIFICATION'|'IN_PROGRESS'|'AVAILABLE'|'PENDING_DEPLOYMENT'|'FAILED'|'CREATING'|'REQUESTING_CERTIFICATE'|'UPDATING',
            'statusReason': 'string',
            'certificateVerificationDNSRecord': 'string',
            'subDomains': [
                {
                    'subDomainSetting': {
                        'prefix': 'string',
                        'branchName': 'string'
                    },
                    'verified': True|False,
                    'dnsRecord': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.DependentServiceFailureException
    
    """
    pass

def update_webhook(webhookId=None, branchName=None, description=None):
    """
    Update a webhook.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_webhook(
        webhookId='string',
        branchName='string',
        description='string'
    )
    
    
    :type webhookId: string
    :param webhookId: [REQUIRED]\nUnique Id for a webhook.\n

    :type branchName: string
    :param branchName: Name for a branch, part of an Amplify App.

    :type description: string
    :param description: Description for a webhook.

    :rtype: dict

ReturnsResponse Syntax
{
    'webhook': {
        'webhookArn': 'string',
        'webhookId': 'string',
        'webhookUrl': 'string',
        'branchName': 'string',
        'description': 'string',
        'createTime': datetime(2015, 1, 1),
        'updateTime': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Result structure for the update webhook request.

webhook (dict) --
Webhook structure.

webhookArn (string) --
ARN for the webhook.

webhookId (string) --
Id of the webhook.

webhookUrl (string) --
Url of the webhook.

branchName (string) --
Name for a branch, part of an Amplify App.

description (string) --
Description for a webhook.

createTime (datetime) --
Create date / time for a webhook.

updateTime (datetime) --
Update date / time for a webhook.









Exceptions

Amplify.Client.exceptions.BadRequestException
Amplify.Client.exceptions.UnauthorizedException
Amplify.Client.exceptions.NotFoundException
Amplify.Client.exceptions.InternalFailureException
Amplify.Client.exceptions.DependentServiceFailureException


    :return: {
        'webhook': {
            'webhookArn': 'string',
            'webhookId': 'string',
            'webhookUrl': 'string',
            'branchName': 'string',
            'description': 'string',
            'createTime': datetime(2015, 1, 1),
            'updateTime': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    Amplify.Client.exceptions.BadRequestException
    Amplify.Client.exceptions.UnauthorizedException
    Amplify.Client.exceptions.NotFoundException
    Amplify.Client.exceptions.InternalFailureException
    Amplify.Client.exceptions.DependentServiceFailureException
    
    """
    pass

