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

def associate_approval_rule_template_with_repository(approvalRuleTemplateName=None, repositoryName=None):
    """
    Creates an association between an approval rule template and a specified repository. Then, the next time a pull request is created in the repository where the destination reference (if specified) matches the destination reference (branch) for the pull request, an approval rule that matches the template conditions is automatically created for that pull request. If no destination references are specified in the template, an approval rule that matches the template contents is created for all pull requests in that repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_approval_rule_template_with_repository(
        approvalRuleTemplateName='string',
        repositoryName='string'
    )
    
    
    :type approvalRuleTemplateName: string
    :param approvalRuleTemplateName: [REQUIRED]\nThe name for the approval rule template.\n

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that you want to associate with the template.\n

    :returns: 
    CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
    CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
    CodeCommit.Client.exceptions.MaximumRuleTemplatesAssociatedWithRepositoryException
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def batch_associate_approval_rule_template_with_repositories(approvalRuleTemplateName=None, repositoryNames=None):
    """
    Creates an association between an approval rule template and one or more specified repositories.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_associate_approval_rule_template_with_repositories(
        approvalRuleTemplateName='string',
        repositoryNames=[
            'string',
        ]
    )
    
    
    :type approvalRuleTemplateName: string
    :param approvalRuleTemplateName: [REQUIRED]\nThe name of the template you want to associate with one or more repositories.\n

    :type repositoryNames: list
    :param repositoryNames: [REQUIRED]\nThe names of the repositories you want to associate with the template.\n\nNote\nThe length constraint limit is for each string in the array. The array itself can be empty.\n\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'associatedRepositoryNames': [
        'string',
    ],
    'errors': [
        {
            'repositoryName': 'string',
            'errorCode': 'string',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

associatedRepositoryNames (list) --
A list of names of the repositories that have been associated with the template.

(string) --


errors (list) --
A list of any errors that might have occurred while attempting to create the association between the template and the repositories.

(dict) --
Returns information about errors in a BatchAssociateApprovalRuleTemplateWithRepositories operation.

repositoryName (string) --
The name of the repository where the association was not made.

errorCode (string) --
An error code that specifies whether the repository name was not valid or not found.

errorMessage (string) --
An error message that provides details about why the repository name was not found or not valid.











Exceptions

CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
CodeCommit.Client.exceptions.RepositoryNamesRequiredException
CodeCommit.Client.exceptions.MaximumRepositoryNamesExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'associatedRepositoryNames': [
            'string',
        ],
        'errors': [
            {
                'repositoryName': 'string',
                'errorCode': 'string',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_describe_merge_conflicts(repositoryName=None, destinationCommitSpecifier=None, sourceCommitSpecifier=None, mergeOption=None, maxMergeHunks=None, maxConflictFiles=None, filePaths=None, conflictDetailLevel=None, conflictResolutionStrategy=None, nextToken=None):
    """
    Returns information about one or more merge conflicts in the attempted merge of two commit specifiers using the squash or three-way merge strategy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_describe_merge_conflicts(
        repositoryName='string',
        destinationCommitSpecifier='string',
        sourceCommitSpecifier='string',
        mergeOption='FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
        maxMergeHunks=123,
        maxConflictFiles=123,
        filePaths=[
            'string',
        ],
        conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
        conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
        nextToken='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that contains the merge conflicts you want to review.\n

    :type destinationCommitSpecifier: string
    :param destinationCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type sourceCommitSpecifier: string
    :param sourceCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type mergeOption: string
    :param mergeOption: [REQUIRED]\nThe merge option or strategy you want to use to merge the code.\n

    :type maxMergeHunks: integer
    :param maxMergeHunks: The maximum number of merge hunks to include in the output.

    :type maxConflictFiles: integer
    :param maxConflictFiles: The maximum number of files to include in the output.

    :type filePaths: list
    :param filePaths: The path of the target files used to describe the conflicts. If not specified, the default is all conflict files.\n\n(string) --\n\n

    :type conflictDetailLevel: string
    :param conflictDetailLevel: The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

    :type conflictResolutionStrategy: string
    :param conflictResolutionStrategy: Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

    :type nextToken: string
    :param nextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'conflicts': [
        {
            'conflictMetadata': {
                'filePath': 'string',
                'fileSizes': {
                    'source': 123,
                    'destination': 123,
                    'base': 123
                },
                'fileModes': {
                    'source': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                    'destination': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                    'base': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
                'objectTypes': {
                    'source': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                    'destination': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                    'base': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK'
                },
                'numberOfConflicts': 123,
                'isBinaryFile': {
                    'source': True|False,
                    'destination': True|False,
                    'base': True|False
                },
                'contentConflict': True|False,
                'fileModeConflict': True|False,
                'objectTypeConflict': True|False,
                'mergeOperations': {
                    'source': 'A'|'M'|'D',
                    'destination': 'A'|'M'|'D'
                }
            },
            'mergeHunks': [
                {
                    'isConflict': True|False,
                    'source': {
                        'startLine': 123,
                        'endLine': 123,
                        'hunkContent': 'string'
                    },
                    'destination': {
                        'startLine': 123,
                        'endLine': 123,
                        'hunkContent': 'string'
                    },
                    'base': {
                        'startLine': 123,
                        'endLine': 123,
                        'hunkContent': 'string'
                    }
                },
            ]
        },
    ],
    'nextToken': 'string',
    'errors': [
        {
            'filePath': 'string',
            'exceptionName': 'string',
            'message': 'string'
        },
    ],
    'destinationCommitId': 'string',
    'sourceCommitId': 'string',
    'baseCommitId': 'string'
}


Response Structure

(dict) --

conflicts (list) --
A list of conflicts for each file, including the conflict metadata and the hunks of the differences between the files.

(dict) --
Information about conflicts in a merge operation.

conflictMetadata (dict) --
Metadata about a conflict in a merge operation.

filePath (string) --
The path of the file that contains conflicts.

fileSizes (dict) --
The file sizes of the file in the source, destination, and base of the merge.

source (integer) --
The size of a file in the source of a merge or pull request.

destination (integer) --
The size of a file in the destination of a merge or pull request.

base (integer) --
The size of a file in the base of a merge or pull request.



fileModes (dict) --
The file modes of the file in the source, destination, and base of the merge.

source (string) --
The file mode of a file in the source of a merge or pull request.

destination (string) --
The file mode of a file in the destination of a merge or pull request.

base (string) --
The file mode of a file in the base of a merge or pull request.



objectTypes (dict) --
Information about any object type conflicts in a merge operation.

source (string) --
The type of the object in the source branch.

destination (string) --
The type of the object in the destination branch.

base (string) --
The type of the object in the base commit of the merge.



numberOfConflicts (integer) --
The number of conflicts, including both hunk conflicts and metadata conflicts.

isBinaryFile (dict) --
A boolean value (true or false) indicating whether the file is binary or textual in the source, destination, and base of the merge.

source (boolean) --
The binary or non-binary status of file in the source of a merge or pull request.

destination (boolean) --
The binary or non-binary status of a file in the destination of a merge or pull request.

base (boolean) --
The binary or non-binary status of a file in the base of a merge or pull request.



contentConflict (boolean) --
A boolean value indicating whether there are conflicts in the content of a file.

fileModeConflict (boolean) --
A boolean value indicating whether there are conflicts in the file mode of a file.

objectTypeConflict (boolean) --
A boolean value (true or false) indicating whether there are conflicts between the branches in the object type of a file, folder, or submodule.

mergeOperations (dict) --
Whether an add, modify, or delete operation caused the conflict between the source and destination of the merge.

source (string) --
The operation (add, modify, or delete) on a file in the source of a merge or pull request.

destination (string) --
The operation on a file in the destination of a merge or pull request.





mergeHunks (list) --
A list of hunks that contain the differences between files or lines causing the conflict.

(dict) --
Information about merge hunks in a merge or pull request operation.

isConflict (boolean) --
A Boolean value indicating whether a combination of hunks contains a conflict. Conflicts occur when the same file or the same lines in a file were modified in both the source and destination of a merge or pull request. Valid values include true, false, and null. True when the hunk represents a conflict and one or more files contains a line conflict. File mode conflicts in a merge do not set this to true.

source (dict) --
Information about the merge hunk in the source of a merge or pull request.

startLine (integer) --
The start position of the hunk in the merge result.

endLine (integer) --
The end position of the hunk in the merge result.

hunkContent (string) --
The base-64 encoded content of the hunk merged region that might contain a conflict.



destination (dict) --
Information about the merge hunk in the destination of a merge or pull request.

startLine (integer) --
The start position of the hunk in the merge result.

endLine (integer) --
The end position of the hunk in the merge result.

hunkContent (string) --
The base-64 encoded content of the hunk merged region that might contain a conflict.



base (dict) --
Information about the merge hunk in the base of a merge or pull request.

startLine (integer) --
The start position of the hunk in the merge result.

endLine (integer) --
The end position of the hunk in the merge result.

hunkContent (string) --
The base-64 encoded content of the hunk merged region that might contain a conflict.











nextToken (string) --
An enumeration token that can be used in a request to return the next batch of the results.

errors (list) --
A list of any errors returned while describing the merge conflicts for each file.

(dict) --
Returns information about errors in a BatchDescribeMergeConflicts operation.

filePath (string) --
The path to the file.

exceptionName (string) --
The name of the exception.

message (string) --
The message provided by the exception.





destinationCommitId (string) --
The commit ID of the destination commit specifier that was used in the merge evaluation.

sourceCommitId (string) --
The commit ID of the source commit specifier that was used in the merge evaluation.

baseCommitId (string) --
The commit ID of the merge base.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.MergeOptionRequiredException
CodeCommit.Client.exceptions.InvalidMergeOptionException
CodeCommit.Client.exceptions.InvalidContinuationTokenException
CodeCommit.Client.exceptions.CommitRequiredException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.TipsDivergenceExceededException
CodeCommit.Client.exceptions.InvalidMaxConflictFilesException
CodeCommit.Client.exceptions.InvalidMaxMergeHunksException
CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'conflicts': [
            {
                'conflictMetadata': {
                    'filePath': 'string',
                    'fileSizes': {
                        'source': 123,
                        'destination': 123,
                        'base': 123
                    },
                    'fileModes': {
                        'source': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                        'destination': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                        'base': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                    },
                    'objectTypes': {
                        'source': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                        'destination': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                        'base': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK'
                    },
                    'numberOfConflicts': 123,
                    'isBinaryFile': {
                        'source': True|False,
                        'destination': True|False,
                        'base': True|False
                    },
                    'contentConflict': True|False,
                    'fileModeConflict': True|False,
                    'objectTypeConflict': True|False,
                    'mergeOperations': {
                        'source': 'A'|'M'|'D',
                        'destination': 'A'|'M'|'D'
                    }
                },
                'mergeHunks': [
                    {
                        'isConflict': True|False,
                        'source': {
                            'startLine': 123,
                            'endLine': 123,
                            'hunkContent': 'string'
                        },
                        'destination': {
                            'startLine': 123,
                            'endLine': 123,
                            'hunkContent': 'string'
                        },
                        'base': {
                            'startLine': 123,
                            'endLine': 123,
                            'hunkContent': 'string'
                        }
                    },
                ]
            },
        ],
        'nextToken': 'string',
        'errors': [
            {
                'filePath': 'string',
                'exceptionName': 'string',
                'message': 'string'
            },
        ],
        'destinationCommitId': 'string',
        'sourceCommitId': 'string',
        'baseCommitId': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.MergeOptionRequiredException
    CodeCommit.Client.exceptions.InvalidMergeOptionException
    CodeCommit.Client.exceptions.InvalidContinuationTokenException
    CodeCommit.Client.exceptions.CommitRequiredException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidCommitException
    CodeCommit.Client.exceptions.TipsDivergenceExceededException
    CodeCommit.Client.exceptions.InvalidMaxConflictFilesException
    CodeCommit.Client.exceptions.InvalidMaxMergeHunksException
    CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
    CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
    CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
    CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def batch_disassociate_approval_rule_template_from_repositories(approvalRuleTemplateName=None, repositoryNames=None):
    """
    Removes the association between an approval rule template and one or more specified repositories.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_disassociate_approval_rule_template_from_repositories(
        approvalRuleTemplateName='string',
        repositoryNames=[
            'string',
        ]
    )
    
    
    :type approvalRuleTemplateName: string
    :param approvalRuleTemplateName: [REQUIRED]\nThe name of the template that you want to disassociate from one or more repositories.\n

    :type repositoryNames: list
    :param repositoryNames: [REQUIRED]\nThe repository names that you want to disassociate from the approval rule template.\n\nNote\nThe length constraint limit is for each string in the array. The array itself can be empty.\n\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'disassociatedRepositoryNames': [
        'string',
    ],
    'errors': [
        {
            'repositoryName': 'string',
            'errorCode': 'string',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

disassociatedRepositoryNames (list) --
A list of repository names that have had their association with the template removed.

(string) --


errors (list) --
A list of any errors that might have occurred while attempting to remove the association between the template and the repositories.

(dict) --
Returns information about errors in a BatchDisassociateApprovalRuleTemplateFromRepositories operation.

repositoryName (string) --
The name of the repository where the association with the template was not able to be removed.

errorCode (string) --
An error code that specifies whether the repository name was not valid or not found.

errorMessage (string) --
An error message that provides details about why the repository name was either not found or not valid.











Exceptions

CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
CodeCommit.Client.exceptions.RepositoryNamesRequiredException
CodeCommit.Client.exceptions.MaximumRepositoryNamesExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'disassociatedRepositoryNames': [
            'string',
        ],
        'errors': [
            {
                'repositoryName': 'string',
                'errorCode': 'string',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_get_commits(commitIds=None, repositoryName=None):
    """
    Returns information about the contents of one or more commits in a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_commits(
        commitIds=[
            'string',
        ],
        repositoryName='string'
    )
    
    
    :type commitIds: list
    :param commitIds: [REQUIRED]\nThe full commit IDs of the commits to get information about.\n\nNote\nYou must supply the full SHA IDs of each commit. You cannot use shortened SHA IDs.\n\n\n(string) --\n\n

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that contains the commits.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'commits': [
        {
            'commitId': 'string',
            'treeId': 'string',
            'parents': [
                'string',
            ],
            'message': 'string',
            'author': {
                'name': 'string',
                'email': 'string',
                'date': 'string'
            },
            'committer': {
                'name': 'string',
                'email': 'string',
                'date': 'string'
            },
            'additionalData': 'string'
        },
    ],
    'errors': [
        {
            'commitId': 'string',
            'errorCode': 'string',
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --

commits (list) --
An array of commit data type objects, each of which contains information about a specified commit.

(dict) --
Returns information about a specific commit.

commitId (string) --
The full SHA ID of the specified commit.

treeId (string) --
Tree information for the specified commit.

parents (list) --
A list of parent commits for the specified commit. Each parent commit ID is the full commit ID.

(string) --


message (string) --
The commit message associated with the specified commit.

author (dict) --
Information about the author of the specified commit. Information includes the date in timestamp format with GMT offset, the name of the author, and the email address for the author, as configured in Git.

name (string) --
The name of the user who made the specified commit.

email (string) --
The email address associated with the user who made the commit, if any.

date (string) --
The date when the specified commit was commited, in timestamp format with GMT offset.



committer (dict) --
Information about the person who committed the specified commit, also known as the committer. Information includes the date in timestamp format with GMT offset, the name of the committer, and the email address for the committer, as configured in Git.
For more information about the difference between an author and a committer in Git, see Viewing the Commit History in Pro Git by Scott Chacon and Ben Straub.

name (string) --
The name of the user who made the specified commit.

email (string) --
The email address associated with the user who made the commit, if any.

date (string) --
The date when the specified commit was commited, in timestamp format with GMT offset.



additionalData (string) --
Any other data associated with the specified commit.





errors (list) --
Returns any commit IDs for which information could not be found. For example, if one of the commit IDs was a shortened SHA ID or that commit was not found in the specified repository, the ID returns an error object with more information.

(dict) --
Returns information about errors in a BatchGetCommits operation.

commitId (string) --
A commit ID that either could not be found or was not in a valid format.

errorCode (string) --
An error code that specifies whether the commit ID was not valid or not found.

errorMessage (string) --
An error message that provides detail about why the commit ID either was not found or was not valid.











Exceptions

CodeCommit.Client.exceptions.CommitIdsListRequiredException
CodeCommit.Client.exceptions.CommitIdsLimitExceededException
CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'commits': [
            {
                'commitId': 'string',
                'treeId': 'string',
                'parents': [
                    'string',
                ],
                'message': 'string',
                'author': {
                    'name': 'string',
                    'email': 'string',
                    'date': 'string'
                },
                'committer': {
                    'name': 'string',
                    'email': 'string',
                    'date': 'string'
                },
                'additionalData': 'string'
            },
        ],
        'errors': [
            {
                'commitId': 'string',
                'errorCode': 'string',
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def batch_get_repositories(repositoryNames=None):
    """
    Returns information about one or more repositories.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.batch_get_repositories(
        repositoryNames=[
            'string',
        ]
    )
    
    
    :type repositoryNames: list
    :param repositoryNames: [REQUIRED]\nThe names of the repositories to get information about.\n\nNote\nThe length constraint limit is for each string in the array. The array itself can be empty.\n\n\n(string) --\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'repositories': [
        {
            'accountId': 'string',
            'repositoryId': 'string',
            'repositoryName': 'string',
            'repositoryDescription': 'string',
            'defaultBranch': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'cloneUrlHttp': 'string',
            'cloneUrlSsh': 'string',
            'Arn': 'string'
        },
    ],
    'repositoriesNotFound': [
        'string',
    ]
}


Response Structure

(dict) --Represents the output of a batch get repositories operation.

repositories (list) --A list of repositories returned by the batch get repositories operation.

(dict) --Information about a repository.

accountId (string) --The ID of the AWS account associated with the repository.

repositoryId (string) --The ID of the repository.

repositoryName (string) --The repository\'s name.

repositoryDescription (string) --A comment or description about the repository.

defaultBranch (string) --The repository\'s default branch name.

lastModifiedDate (datetime) --The date and time the repository was last modified, in timestamp format.

creationDate (datetime) --The date and time the repository was created, in timestamp format.

cloneUrlHttp (string) --The URL to use for cloning the repository over HTTPS.

cloneUrlSsh (string) --The URL to use for cloning the repository over SSH.

Arn (string) --The Amazon Resource Name (ARN) of the repository.





repositoriesNotFound (list) --Returns a list of repository names for which information could not be found.

(string) --







Exceptions

CodeCommit.Client.exceptions.RepositoryNamesRequiredException
CodeCommit.Client.exceptions.MaximumRepositoryNamesExceededException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'repositories': [
            {
                'accountId': 'string',
                'repositoryId': 'string',
                'repositoryName': 'string',
                'repositoryDescription': 'string',
                'defaultBranch': 'string',
                'lastModifiedDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1),
                'cloneUrlHttp': 'string',
                'cloneUrlSsh': 'string',
                'Arn': 'string'
            },
        ],
        'repositoriesNotFound': [
            'string',
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_approval_rule_template(approvalRuleTemplateName=None, approvalRuleTemplateContent=None, approvalRuleTemplateDescription=None):
    """
    Creates a template for approval rules that can then be associated with one or more repositories in your AWS account. When you associate a template with a repository, AWS CodeCommit creates an approval rule that matches the conditions of the template for all pull requests that meet the conditions of the template. For more information, see  AssociateApprovalRuleTemplateWithRepository .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_approval_rule_template(
        approvalRuleTemplateName='string',
        approvalRuleTemplateContent='string',
        approvalRuleTemplateDescription='string'
    )
    
    
    :type approvalRuleTemplateName: string
    :param approvalRuleTemplateName: [REQUIRED]\nThe name of the approval rule template. Provide descriptive names, because this name is applied to the approval rules created automatically in associated repositories.\n

    :type approvalRuleTemplateContent: string
    :param approvalRuleTemplateContent: [REQUIRED]\nThe content of the approval rule that is created on pull requests in associated repositories. If you specify one or more destination references (branches), approval rules are created in an associated repository only if their destination references (branches) match those specified in the template.\n\nNote\nWhen you create the content of the approval rule template, you can specify approvers in an approval pool in one of two ways:\n\nCodeCommitApprovers : This option only requires an AWS account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the AWS account 123456789012 and Mary_Major , all of the following are counted as approvals coming from that user:\nAn IAM user in the account (arn:aws:iam::123456789012 :user/Mary_Major )\nA federated user identified in IAM as Mary_Major (arn:aws:sts::123456789012 :federated-user/Mary_Major )\n\n\n\nThis option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of Mary_Major (arn:aws:sts::123456789012 :assumed-role/CodeCommitReview/Mary_Major ) unless you include a wildcard (*Mary_Major).\n\nFully qualified ARN : This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role.\n\nFor more information about IAM ARNs, wildcards, and formats, see IAM Identifiers in the IAM User Guide .\n\n

    :type approvalRuleTemplateDescription: string
    :param approvalRuleTemplateDescription: The description of the approval rule template. Consider providing a description that explains what this template does and when it might be appropriate to associate it with repositories.

    :rtype: dict

ReturnsResponse Syntax
{
    'approvalRuleTemplate': {
        'approvalRuleTemplateId': 'string',
        'approvalRuleTemplateName': 'string',
        'approvalRuleTemplateDescription': 'string',
        'approvalRuleTemplateContent': 'string',
        'ruleContentSha256': 'string',
        'lastModifiedDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedUser': 'string'
    }
}


Response Structure

(dict) --

approvalRuleTemplate (dict) --
The content and structure of the created approval rule template.

approvalRuleTemplateId (string) --
The system-generated ID of the approval rule template.

approvalRuleTemplateName (string) --
The name of the approval rule template.

approvalRuleTemplateDescription (string) --
The description of the approval rule template.

approvalRuleTemplateContent (string) --
The content of the approval rule template.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule template.

lastModifiedDate (datetime) --
The date the approval rule template was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule template was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule template.









Exceptions

CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
CodeCommit.Client.exceptions.ApprovalRuleTemplateNameAlreadyExistsException
CodeCommit.Client.exceptions.ApprovalRuleTemplateContentRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateContentException
CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateDescriptionException
CodeCommit.Client.exceptions.NumberOfRuleTemplatesExceededException


    :return: {
        'approvalRuleTemplate': {
            'approvalRuleTemplateId': 'string',
            'approvalRuleTemplateName': 'string',
            'approvalRuleTemplateDescription': 'string',
            'approvalRuleTemplateContent': 'string',
            'ruleContentSha256': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedUser': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
    CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateNameAlreadyExistsException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateContentRequiredException
    CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateContentException
    CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateDescriptionException
    CodeCommit.Client.exceptions.NumberOfRuleTemplatesExceededException
    
    """
    pass

def create_branch(repositoryName=None, branchName=None, commitId=None):
    """
    Creates a branch in a repository and points the branch to a commit.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_branch(
        repositoryName='string',
        branchName='string',
        commitId='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository in which you want to create the new branch.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nThe name of the new branch to create.\n

    :type commitId: string
    :param commitId: [REQUIRED]\nThe ID of the commit to point the new branch to.\n

    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.BranchNameRequiredException
    CodeCommit.Client.exceptions.BranchNameExistsException
    CodeCommit.Client.exceptions.InvalidBranchNameException
    CodeCommit.Client.exceptions.CommitIdRequiredException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidCommitIdException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def create_commit(repositoryName=None, branchName=None, parentCommitId=None, authorName=None, email=None, commitMessage=None, keepEmptyFolders=None, putFiles=None, deleteFiles=None, setFileModes=None):
    """
    Creates a commit for a repository on the tip of a specified branch.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_commit(
        repositoryName='string',
        branchName='string',
        parentCommitId='string',
        authorName='string',
        email='string',
        commitMessage='string',
        keepEmptyFolders=True|False,
        putFiles=[
            {
                'filePath': 'string',
                'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                'fileContent': b'bytes',
                'sourceFile': {
                    'filePath': 'string',
                    'isMove': True|False
                }
            },
        ],
        deleteFiles=[
            {
                'filePath': 'string'
            },
        ],
        setFileModes=[
            {
                'filePath': 'string',
                'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
            },
        ]
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you create the commit.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nThe name of the branch where you create the commit.\n

    :type parentCommitId: string
    :param parentCommitId: The ID of the commit that is the parent of the commit you create. Not required if this is an empty repository.

    :type authorName: string
    :param authorName: The name of the author who created the commit. This information is used as both the author and committer for the commit.

    :type email: string
    :param email: The email address of the person who created the commit.

    :type commitMessage: string
    :param commitMessage: The commit message you want to include in the commit. Commit messages are limited to 256 KB. If no message is specified, a default message is used.

    :type keepEmptyFolders: boolean
    :param keepEmptyFolders: If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a ..gitkeep file is created for empty folders. The default is false.

    :type putFiles: list
    :param putFiles: The files to add or update in this commit.\n\n(dict) --Information about a file added or updated as part of a commit.\n\nfilePath (string) -- [REQUIRED]The full path to the file in the repository, including the name of the file.\n\nfileMode (string) --The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.\n\nfileContent (bytes) --The content of the file, if a source file is not specified.\n\nsourceFile (dict) --The name and full path of the file that contains the changes you want to make as part of the commit, if you are not providing the file content directly.\n\nfilePath (string) -- [REQUIRED]The full path to the file, including the name of the file.\n\nisMove (boolean) --Whether to remove the source file from the parent commit.\n\n\n\n\n\n\n

    :type deleteFiles: list
    :param deleteFiles: The files to delete in this commit. These files still exist in earlier commits.\n\n(dict) --A file that is deleted as part of a commit.\n\nfilePath (string) -- [REQUIRED]The full path of the file to be deleted, including the name of the file.\n\n\n\n\n

    :type setFileModes: list
    :param setFileModes: The file modes to update for files in this commit.\n\n(dict) --Information about the file mode changes.\n\nfilePath (string) -- [REQUIRED]The full path to the file, including the name of the file.\n\nfileMode (string) -- [REQUIRED]The file mode for the file.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'commitId': 'string',
    'treeId': 'string',
    'filesAdded': [
        {
            'absolutePath': 'string',
            'blobId': 'string',
            'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
        },
    ],
    'filesUpdated': [
        {
            'absolutePath': 'string',
            'blobId': 'string',
            'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
        },
    ],
    'filesDeleted': [
        {
            'absolutePath': 'string',
            'blobId': 'string',
            'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
        },
    ]
}


Response Structure

(dict) --

commitId (string) --
The full commit ID of the commit that contains your committed file changes.

treeId (string) --
The full SHA-1 pointer of the tree information for the commit that contains the commited file changes.

filesAdded (list) --
The files added as part of the committed file changes.

(dict) --
A file to be added, updated, or deleted as part of a commit.

absolutePath (string) --
The full path to the file to be added or updated, including the name of the file.

blobId (string) --
The blob ID that contains the file information.

fileMode (string) --
The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.





filesUpdated (list) --
The files updated as part of the commited file changes.

(dict) --
A file to be added, updated, or deleted as part of a commit.

absolutePath (string) --
The full path to the file to be added or updated, including the name of the file.

blobId (string) --
The blob ID that contains the file information.

fileMode (string) --
The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.





filesDeleted (list) --
The files deleted as part of the committed file changes.

(dict) --
A file to be added, updated, or deleted as part of a commit.

absolutePath (string) --
The full path to the file to be added or updated, including the name of the file.

blobId (string) --
The blob ID that contains the file information.

fileMode (string) --
The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.











Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.ParentCommitIdRequiredException
CodeCommit.Client.exceptions.InvalidParentCommitIdException
CodeCommit.Client.exceptions.ParentCommitDoesNotExistException
CodeCommit.Client.exceptions.ParentCommitIdOutdatedException
CodeCommit.Client.exceptions.BranchNameRequiredException
CodeCommit.Client.exceptions.InvalidBranchNameException
CodeCommit.Client.exceptions.BranchDoesNotExistException
CodeCommit.Client.exceptions.BranchNameIsTagNameException
CodeCommit.Client.exceptions.FileEntryRequiredException
CodeCommit.Client.exceptions.MaximumFileEntriesExceededException
CodeCommit.Client.exceptions.PutFileEntryConflictException
CodeCommit.Client.exceptions.SourceFileOrContentRequiredException
CodeCommit.Client.exceptions.FileContentAndSourceFileSpecifiedException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.SamePathRequestException
CodeCommit.Client.exceptions.FileDoesNotExistException
CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
CodeCommit.Client.exceptions.InvalidDeletionParameterException
CodeCommit.Client.exceptions.RestrictedSourceFileException
CodeCommit.Client.exceptions.FileModeRequiredException
CodeCommit.Client.exceptions.InvalidFileModeException
CodeCommit.Client.exceptions.NameLengthExceededException
CodeCommit.Client.exceptions.InvalidEmailException
CodeCommit.Client.exceptions.CommitMessageLengthExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
CodeCommit.Client.exceptions.NoChangeException
CodeCommit.Client.exceptions.FileNameConflictsWithDirectoryNameException
CodeCommit.Client.exceptions.DirectoryNameConflictsWithFileNameException
CodeCommit.Client.exceptions.FilePathConflictsWithSubmodulePathException


    :return: {
        'commitId': 'string',
        'treeId': 'string',
        'filesAdded': [
            {
                'absolutePath': 'string',
                'blobId': 'string',
                'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
            },
        ],
        'filesUpdated': [
            {
                'absolutePath': 'string',
                'blobId': 'string',
                'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
            },
        ],
        'filesDeleted': [
            {
                'absolutePath': 'string',
                'blobId': 'string',
                'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
            },
        ]
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.ParentCommitIdRequiredException
    CodeCommit.Client.exceptions.InvalidParentCommitIdException
    CodeCommit.Client.exceptions.ParentCommitDoesNotExistException
    CodeCommit.Client.exceptions.ParentCommitIdOutdatedException
    CodeCommit.Client.exceptions.BranchNameRequiredException
    CodeCommit.Client.exceptions.InvalidBranchNameException
    CodeCommit.Client.exceptions.BranchDoesNotExistException
    CodeCommit.Client.exceptions.BranchNameIsTagNameException
    CodeCommit.Client.exceptions.FileEntryRequiredException
    CodeCommit.Client.exceptions.MaximumFileEntriesExceededException
    CodeCommit.Client.exceptions.PutFileEntryConflictException
    CodeCommit.Client.exceptions.SourceFileOrContentRequiredException
    CodeCommit.Client.exceptions.FileContentAndSourceFileSpecifiedException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.SamePathRequestException
    CodeCommit.Client.exceptions.FileDoesNotExistException
    CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
    CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
    CodeCommit.Client.exceptions.InvalidDeletionParameterException
    CodeCommit.Client.exceptions.RestrictedSourceFileException
    CodeCommit.Client.exceptions.FileModeRequiredException
    CodeCommit.Client.exceptions.InvalidFileModeException
    CodeCommit.Client.exceptions.NameLengthExceededException
    CodeCommit.Client.exceptions.InvalidEmailException
    CodeCommit.Client.exceptions.CommitMessageLengthExceededException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    CodeCommit.Client.exceptions.NoChangeException
    CodeCommit.Client.exceptions.FileNameConflictsWithDirectoryNameException
    CodeCommit.Client.exceptions.DirectoryNameConflictsWithFileNameException
    CodeCommit.Client.exceptions.FilePathConflictsWithSubmodulePathException
    
    """
    pass

def create_pull_request(title=None, description=None, targets=None, clientRequestToken=None):
    """
    Creates a pull request in the specified repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_pull_request(
        title='string',
        description='string',
        targets=[
            {
                'repositoryName': 'string',
                'sourceReference': 'string',
                'destinationReference': 'string'
            },
        ],
        clientRequestToken='string'
    )
    
    
    :type title: string
    :param title: [REQUIRED]\nThe title of the pull request. This title is used to identify the pull request to other users in the repository.\n

    :type description: string
    :param description: A description of the pull request.

    :type targets: list
    :param targets: [REQUIRED]\nThe targets for the pull request, including the source of the code to be reviewed (the source branch) and the destination where the creator of the pull request intends the code to be merged after the pull request is closed (the destination branch).\n\n(dict) --Returns information about a target for a pull request.\n\nrepositoryName (string) -- [REQUIRED]The name of the repository that contains the pull request.\n\nsourceReference (string) -- [REQUIRED]The branch of the repository that contains the changes for the pull request. Also known as the source branch.\n\ndestinationReference (string) --The branch of the repository where the pull request changes are merged. Also known as the destination branch.\n\n\n\n\n

    :type clientRequestToken: string
    :param clientRequestToken: A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.\n\nNote\nThe AWS SDKs prepopulate client request tokens. If you are using an AWS SDK, an idempotency token is created for you.\n\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'pullRequest': {
        'pullRequestId': 'string',
        'title': 'string',
        'description': 'string',
        'lastActivityDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'pullRequestStatus': 'OPEN'|'CLOSED',
        'authorArn': 'string',
        'pullRequestTargets': [
            {
                'repositoryName': 'string',
                'sourceReference': 'string',
                'destinationReference': 'string',
                'destinationCommit': 'string',
                'sourceCommit': 'string',
                'mergeBase': 'string',
                'mergeMetadata': {
                    'isMerged': True|False,
                    'mergedBy': 'string',
                    'mergeCommitId': 'string',
                    'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                }
            },
        ],
        'clientRequestToken': 'string',
        'revisionId': 'string',
        'approvalRules': [
            {
                'approvalRuleId': 'string',
                'approvalRuleName': 'string',
                'approvalRuleContent': 'string',
                'ruleContentSha256': 'string',
                'lastModifiedDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedUser': 'string',
                'originApprovalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --

pullRequest (dict) --
Information about the newly created pull request.

pullRequestId (string) --
The system-generated ID of the pull request.

title (string) --
The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.

description (string) --
The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.

lastActivityDate (datetime) --
The day and time of the last user or system activity on the pull request, in timestamp format.

creationDate (datetime) --
The date and time the pull request was originally created, in timestamp format.

pullRequestStatus (string) --
The status of the pull request. Pull request status can only change from OPEN to CLOSED .

authorArn (string) --
The Amazon Resource Name (ARN) of the user who created the pull request.

pullRequestTargets (list) --
The targets of the pull request, including the source branch and destination branch for the pull request.

(dict) --
Returns information about a pull request target.

repositoryName (string) --
The name of the repository that contains the pull request source and destination branches.

sourceReference (string) --
The branch of the repository that contains the changes for the pull request. Also known as the source branch.

destinationReference (string) --
The branch of the repository where the pull request changes are merged. Also known as the destination branch.

destinationCommit (string) --
The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.

sourceCommit (string) --
The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.

mergeBase (string) --
The commit ID of the most recent commit that the source branch and the destination branch have in common.

mergeMetadata (dict) --
Returns metadata about the state of the merge, including whether the merge has been made.

isMerged (boolean) --
A Boolean value indicating whether the merge has been made.

mergedBy (string) --
The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId (string) --
The commit ID for the merge commit, if any.

mergeOption (string) --
The merge strategy used in the merge.







clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

revisionId (string) --
The system-generated revision ID for the pull request.

approvalRules (list) --
The approval rules applied to the pull request.

(dict) --
Returns information about an approval rule.

approvalRuleId (string) --
The system-generated ID of the approval rule.

approvalRuleName (string) --
The name of the approval rule.

approvalRuleContent (string) --
The content of the approval rule.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate (datetime) --
The date the approval rule was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate (dict) --
The approval rule template used to create the rule.

approvalRuleTemplateId (string) --
The ID of the template that created the approval rule.

approvalRuleTemplateName (string) --
The name of the template that created the approval rule.















Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
CodeCommit.Client.exceptions.ClientRequestTokenRequiredException
CodeCommit.Client.exceptions.InvalidClientRequestTokenException
CodeCommit.Client.exceptions.IdempotencyParameterMismatchException
CodeCommit.Client.exceptions.ReferenceNameRequiredException
CodeCommit.Client.exceptions.InvalidReferenceNameException
CodeCommit.Client.exceptions.ReferenceDoesNotExistException
CodeCommit.Client.exceptions.ReferenceTypeNotSupportedException
CodeCommit.Client.exceptions.TitleRequiredException
CodeCommit.Client.exceptions.InvalidTitleException
CodeCommit.Client.exceptions.InvalidDescriptionException
CodeCommit.Client.exceptions.TargetsRequiredException
CodeCommit.Client.exceptions.InvalidTargetsException
CodeCommit.Client.exceptions.TargetRequiredException
CodeCommit.Client.exceptions.InvalidTargetException
CodeCommit.Client.exceptions.MultipleRepositoriesInPullRequestException
CodeCommit.Client.exceptions.MaximumOpenPullRequestsExceededException
CodeCommit.Client.exceptions.SourceAndDestinationAreSameException


    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeBase': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string',
                        'mergeCommitId': 'string',
                        'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                    }
                },
            ],
            'clientRequestToken': 'string',
            'revisionId': 'string',
            'approvalRules': [
                {
                    'approvalRuleId': 'string',
                    'approvalRuleName': 'string',
                    'approvalRuleContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string',
                    'originApprovalRuleTemplate': {
                        'approvalRuleTemplateId': 'string',
                        'approvalRuleTemplateName': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    CodeCommit.Client.exceptions.ClientRequestTokenRequiredException
    CodeCommit.Client.exceptions.InvalidClientRequestTokenException
    CodeCommit.Client.exceptions.IdempotencyParameterMismatchException
    CodeCommit.Client.exceptions.ReferenceNameRequiredException
    CodeCommit.Client.exceptions.InvalidReferenceNameException
    CodeCommit.Client.exceptions.ReferenceDoesNotExistException
    CodeCommit.Client.exceptions.ReferenceTypeNotSupportedException
    CodeCommit.Client.exceptions.TitleRequiredException
    CodeCommit.Client.exceptions.InvalidTitleException
    CodeCommit.Client.exceptions.InvalidDescriptionException
    CodeCommit.Client.exceptions.TargetsRequiredException
    CodeCommit.Client.exceptions.InvalidTargetsException
    CodeCommit.Client.exceptions.TargetRequiredException
    CodeCommit.Client.exceptions.InvalidTargetException
    CodeCommit.Client.exceptions.MultipleRepositoriesInPullRequestException
    CodeCommit.Client.exceptions.MaximumOpenPullRequestsExceededException
    CodeCommit.Client.exceptions.SourceAndDestinationAreSameException
    
    """
    pass

def create_pull_request_approval_rule(pullRequestId=None, approvalRuleName=None, approvalRuleContent=None):
    """
    Creates an approval rule for a pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_pull_request_approval_rule(
        pullRequestId='string',
        approvalRuleName='string',
        approvalRuleContent='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request for which you want to create the approval rule.\n

    :type approvalRuleName: string
    :param approvalRuleName: [REQUIRED]\nThe name for the approval rule.\n

    :type approvalRuleContent: string
    :param approvalRuleContent: [REQUIRED]\nThe content of the approval rule, including the number of approvals needed and the structure of an approval pool defined for approvals, if any. For more information about approval pools, see the AWS CodeCommit User Guide.\n\nNote\nWhen you create the content of the approval rule, you can specify approvers in an approval pool in one of two ways:\n\nCodeCommitApprovers : This option only requires an AWS account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the AWS account 123456789012 and Mary_Major , all of the following would be counted as approvals coming from that user:\nAn IAM user in the account (arn:aws:iam::123456789012 :user/Mary_Major )\nA federated user identified in IAM as Mary_Major (arn:aws:sts::123456789012 :federated-user/Mary_Major )\n\n\n\nThis option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of Mary_Major (arn:aws:sts::123456789012 :assumed-role/CodeCommitReview/Mary_Major ) unless you include a wildcard (*Mary_Major).\n\nFully qualified ARN : This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role.\n\nFor more information about IAM ARNs, wildcards, and formats, see IAM Identifiers in the IAM User Guide .\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'approvalRule': {
        'approvalRuleId': 'string',
        'approvalRuleName': 'string',
        'approvalRuleContent': 'string',
        'ruleContentSha256': 'string',
        'lastModifiedDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedUser': 'string',
        'originApprovalRuleTemplate': {
            'approvalRuleTemplateId': 'string',
            'approvalRuleTemplateName': 'string'
        }
    }
}


Response Structure

(dict) --

approvalRule (dict) --
Information about the created approval rule.

approvalRuleId (string) --
The system-generated ID of the approval rule.

approvalRuleName (string) --
The name of the approval rule.

approvalRuleContent (string) --
The content of the approval rule.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate (datetime) --
The date the approval rule was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate (dict) --
The approval rule template used to create the rule.

approvalRuleTemplateId (string) --
The ID of the template that created the approval rule.

approvalRuleTemplateName (string) --
The name of the template that created the approval rule.











Exceptions

CodeCommit.Client.exceptions.ApprovalRuleNameRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleNameException
CodeCommit.Client.exceptions.ApprovalRuleNameAlreadyExistsException
CodeCommit.Client.exceptions.ApprovalRuleContentRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleContentException
CodeCommit.Client.exceptions.NumberOfRulesExceededException
CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'approvalRule': {
            'approvalRuleId': 'string',
            'approvalRuleName': 'string',
            'approvalRuleContent': 'string',
            'ruleContentSha256': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedUser': 'string',
            'originApprovalRuleTemplate': {
                'approvalRuleTemplateId': 'string',
                'approvalRuleTemplateName': 'string'
            }
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.ApprovalRuleNameRequiredException
    CodeCommit.Client.exceptions.InvalidApprovalRuleNameException
    CodeCommit.Client.exceptions.ApprovalRuleNameAlreadyExistsException
    CodeCommit.Client.exceptions.ApprovalRuleContentRequiredException
    CodeCommit.Client.exceptions.InvalidApprovalRuleContentException
    CodeCommit.Client.exceptions.NumberOfRulesExceededException
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def create_repository(repositoryName=None, repositoryDescription=None, tags=None):
    """
    Creates a new, empty repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_repository(
        repositoryName='string',
        repositoryDescription='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the new repository to be created.\n\nNote\nThe repository name must be unique across the calling AWS account. Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. For more information about the limits on repository names, see Limits in the AWS CodeCommit User Guide . The suffix .git is prohibited.\n\n

    :type repositoryDescription: string
    :param repositoryDescription: A comment or description about the new repository.\n\nNote\nThe description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.\n\n

    :type tags: dict
    :param tags: One or more tag key-value pairs to use when tagging this repository.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'repositoryMetadata': {
        'accountId': 'string',
        'repositoryId': 'string',
        'repositoryName': 'string',
        'repositoryDescription': 'string',
        'defaultBranch': 'string',
        'lastModifiedDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'cloneUrlHttp': 'string',
        'cloneUrlSsh': 'string',
        'Arn': 'string'
    }
}


Response Structure

(dict) --
Represents the output of a create repository operation.

repositoryMetadata (dict) --
Information about the newly created repository.

accountId (string) --
The ID of the AWS account associated with the repository.

repositoryId (string) --
The ID of the repository.

repositoryName (string) --
The repository\'s name.

repositoryDescription (string) --
A comment or description about the repository.

defaultBranch (string) --
The repository\'s default branch name.

lastModifiedDate (datetime) --
The date and time the repository was last modified, in timestamp format.

creationDate (datetime) --
The date and time the repository was created, in timestamp format.

cloneUrlHttp (string) --
The URL to use for cloning the repository over HTTPS.

cloneUrlSsh (string) --
The URL to use for cloning the repository over SSH.

Arn (string) --
The Amazon Resource Name (ARN) of the repository.









Exceptions

CodeCommit.Client.exceptions.RepositoryNameExistsException
CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.InvalidRepositoryDescriptionException
CodeCommit.Client.exceptions.RepositoryLimitExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
CodeCommit.Client.exceptions.InvalidTagsMapException
CodeCommit.Client.exceptions.TooManyTagsException
CodeCommit.Client.exceptions.InvalidSystemTagUsageException
CodeCommit.Client.exceptions.TagPolicyException


    :return: {
        'repositoryMetadata': {
            'accountId': 'string',
            'repositoryId': 'string',
            'repositoryName': 'string',
            'repositoryDescription': 'string',
            'defaultBranch': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'cloneUrlHttp': 'string',
            'cloneUrlSsh': 'string',
            'Arn': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameExistsException
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.InvalidRepositoryDescriptionException
    CodeCommit.Client.exceptions.RepositoryLimitExceededException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    CodeCommit.Client.exceptions.InvalidTagsMapException
    CodeCommit.Client.exceptions.TooManyTagsException
    CodeCommit.Client.exceptions.InvalidSystemTagUsageException
    CodeCommit.Client.exceptions.TagPolicyException
    
    """
    pass

def create_unreferenced_merge_commit(repositoryName=None, sourceCommitSpecifier=None, destinationCommitSpecifier=None, mergeOption=None, conflictDetailLevel=None, conflictResolutionStrategy=None, authorName=None, email=None, commitMessage=None, keepEmptyFolders=None, conflictResolution=None):
    """
    Creates an unreferenced commit that represents the result of merging two branches using a specified merge strategy. This can help you determine the outcome of a potential merge. This API cannot be used with the fast-forward merge strategy because that strategy does not create a merge commit.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_unreferenced_merge_commit(
        repositoryName='string',
        sourceCommitSpecifier='string',
        destinationCommitSpecifier='string',
        mergeOption='FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
        conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
        conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
        authorName='string',
        email='string',
        commitMessage='string',
        keepEmptyFolders=True|False,
        conflictResolution={
            'replaceContents': [
                {
                    'filePath': 'string',
                    'replacementType': 'KEEP_BASE'|'KEEP_SOURCE'|'KEEP_DESTINATION'|'USE_NEW_CONTENT',
                    'content': b'bytes',
                    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
            ],
            'deleteFiles': [
                {
                    'filePath': 'string'
                },
            ],
            'setFileModes': [
                {
                    'filePath': 'string',
                    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
            ]
        }
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to create the unreferenced merge commit.\n

    :type sourceCommitSpecifier: string
    :param sourceCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type destinationCommitSpecifier: string
    :param destinationCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type mergeOption: string
    :param mergeOption: [REQUIRED]\nThe merge option or strategy you want to use to merge the code.\n

    :type conflictDetailLevel: string
    :param conflictDetailLevel: The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

    :type conflictResolutionStrategy: string
    :param conflictResolutionStrategy: Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

    :type authorName: string
    :param authorName: The name of the author who created the unreferenced commit. This information is used as both the author and committer for the commit.

    :type email: string
    :param email: The email address for the person who created the unreferenced commit.

    :type commitMessage: string
    :param commitMessage: The commit message for the unreferenced commit.

    :type keepEmptyFolders: boolean
    :param keepEmptyFolders: If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If this is specified as true, a .gitkeep file is created for empty folders. The default is false.

    :type conflictResolution: dict
    :param conflictResolution: If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.\n\nreplaceContents (list) --Files to have content replaced as part of the merge conflict resolution.\n\n(dict) --Information about a replacement content entry in the conflict of a merge or pull request operation.\n\nfilePath (string) -- [REQUIRED]The path of the conflicting file.\n\nreplacementType (string) -- [REQUIRED]The replacement type to use when determining how to resolve the conflict.\n\ncontent (bytes) --The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.\n\nfileMode (string) --The file mode to apply during conflict resoltion.\n\n\n\n\n\ndeleteFiles (list) --Files to be deleted as part of the merge conflict resolution.\n\n(dict) --A file that is deleted as part of a commit.\n\nfilePath (string) -- [REQUIRED]The full path of the file to be deleted, including the name of the file.\n\n\n\n\n\nsetFileModes (list) --File modes that are set as part of the merge conflict resolution.\n\n(dict) --Information about the file mode changes.\n\nfilePath (string) -- [REQUIRED]The full path to the file, including the name of the file.\n\nfileMode (string) -- [REQUIRED]The file mode for the file.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'commitId': 'string',
    'treeId': 'string'
}


Response Structure

(dict) --

commitId (string) --
The full commit ID of the commit that contains your merge results.

treeId (string) --
The full SHA-1 pointer of the tree information for the commit that contains the merge results.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.TipsDivergenceExceededException
CodeCommit.Client.exceptions.CommitRequiredException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.MergeOptionRequiredException
CodeCommit.Client.exceptions.InvalidMergeOptionException
CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
CodeCommit.Client.exceptions.InvalidConflictResolutionException
CodeCommit.Client.exceptions.ManualMergeRequiredException
CodeCommit.Client.exceptions.MaximumConflictResolutionEntriesExceededException
CodeCommit.Client.exceptions.MultipleConflictResolutionEntriesException
CodeCommit.Client.exceptions.ReplacementTypeRequiredException
CodeCommit.Client.exceptions.InvalidReplacementTypeException
CodeCommit.Client.exceptions.ReplacementContentRequiredException
CodeCommit.Client.exceptions.InvalidReplacementContentException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
CodeCommit.Client.exceptions.FileModeRequiredException
CodeCommit.Client.exceptions.InvalidFileModeException
CodeCommit.Client.exceptions.NameLengthExceededException
CodeCommit.Client.exceptions.InvalidEmailException
CodeCommit.Client.exceptions.CommitMessageLengthExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'commitId': 'string',
        'treeId': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.TipsDivergenceExceededException
    CodeCommit.Client.exceptions.CommitRequiredException
    CodeCommit.Client.exceptions.InvalidCommitException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.MergeOptionRequiredException
    CodeCommit.Client.exceptions.InvalidMergeOptionException
    CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
    CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
    CodeCommit.Client.exceptions.InvalidConflictResolutionException
    CodeCommit.Client.exceptions.ManualMergeRequiredException
    CodeCommit.Client.exceptions.MaximumConflictResolutionEntriesExceededException
    CodeCommit.Client.exceptions.MultipleConflictResolutionEntriesException
    CodeCommit.Client.exceptions.ReplacementTypeRequiredException
    CodeCommit.Client.exceptions.InvalidReplacementTypeException
    CodeCommit.Client.exceptions.ReplacementContentRequiredException
    CodeCommit.Client.exceptions.InvalidReplacementContentException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
    CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
    CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
    CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
    CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
    CodeCommit.Client.exceptions.FileModeRequiredException
    CodeCommit.Client.exceptions.InvalidFileModeException
    CodeCommit.Client.exceptions.NameLengthExceededException
    CodeCommit.Client.exceptions.InvalidEmailException
    CodeCommit.Client.exceptions.CommitMessageLengthExceededException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def delete_approval_rule_template(approvalRuleTemplateName=None):
    """
    Deletes a specified approval rule template. Deleting a template does not remove approval rules on pull requests already created with the template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_approval_rule_template(
        approvalRuleTemplateName='string'
    )
    
    
    :type approvalRuleTemplateName: string
    :param approvalRuleTemplateName: [REQUIRED]\nThe name of the approval rule template to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'approvalRuleTemplateId': 'string'
}


Response Structure

(dict) --
approvalRuleTemplateId (string) --The system-generated ID of the deleted approval rule template. If the template has been previously deleted, the only response is a 200 OK.






Exceptions

CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
CodeCommit.Client.exceptions.ApprovalRuleTemplateInUseException


    :return: {
        'approvalRuleTemplateId': 'string'
    }
    
    
    """
    pass

def delete_branch(repositoryName=None, branchName=None):
    """
    Deletes a branch from a repository, unless that branch is the default branch for the repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_branch(
        repositoryName='string',
        branchName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that contains the branch to be deleted.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nThe name of the branch to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'deletedBranch': {
        'branchName': 'string',
        'commitId': 'string'
    }
}


Response Structure

(dict) --
Represents the output of a delete branch operation.

deletedBranch (dict) --
Information about the branch deleted by the operation, including the branch name and the commit ID that was the tip of the branch.

branchName (string) --
The name of the branch.

commitId (string) --
The ID of the last commit made to the branch.









Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.BranchNameRequiredException
CodeCommit.Client.exceptions.InvalidBranchNameException
CodeCommit.Client.exceptions.DefaultBranchCannotBeDeletedException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'deletedBranch': {
            'branchName': 'string',
            'commitId': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.BranchNameRequiredException
    CodeCommit.Client.exceptions.InvalidBranchNameException
    CodeCommit.Client.exceptions.DefaultBranchCannotBeDeletedException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def delete_comment_content(commentId=None):
    """
    Deletes the content of a comment made on a change, file, or commit in a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_comment_content(
        commentId='string'
    )
    
    
    :type commentId: string
    :param commentId: [REQUIRED]\nThe unique, system-generated ID of the comment. To get this ID, use GetCommentsForComparedCommit or GetCommentsForPullRequest .\n

    :rtype: dict
ReturnsResponse Syntax{
    'comment': {
        'commentId': 'string',
        'content': 'string',
        'inReplyTo': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'authorArn': 'string',
        'deleted': True|False,
        'clientRequestToken': 'string'
    }
}


Response Structure

(dict) --
comment (dict) --Information about the comment you just deleted.

commentId (string) --The system-generated comment ID.

content (string) --The content of the comment.

inReplyTo (string) --The ID of the comment for which this comment is a reply, if any.

creationDate (datetime) --The date and time the comment was created, in timestamp format.

lastModifiedDate (datetime) --The date and time the comment was most recently modified, in timestamp format.

authorArn (string) --The Amazon Resource Name (ARN) of the person who posted the comment.

deleted (boolean) --A Boolean value indicating whether the comment has been deleted.

clientRequestToken (string) --A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.








Exceptions

CodeCommit.Client.exceptions.CommentDoesNotExistException
CodeCommit.Client.exceptions.CommentIdRequiredException
CodeCommit.Client.exceptions.InvalidCommentIdException
CodeCommit.Client.exceptions.CommentDeletedException


    :return: {
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def delete_file(repositoryName=None, branchName=None, filePath=None, parentCommitId=None, keepEmptyFolders=None, commitMessage=None, name=None, email=None):
    """
    Deletes a specified file from a specified branch. A commit is created on the branch that contains the revision. The file still exists in the commits earlier to the commit that contains the deletion.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_file(
        repositoryName='string',
        branchName='string',
        filePath='string',
        parentCommitId='string',
        keepEmptyFolders=True|False,
        commitMessage='string',
        name='string',
        email='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that contains the file to delete.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nThe name of the branch where the commit that deletes the file is made.\n

    :type filePath: string
    :param filePath: [REQUIRED]\nThe fully qualified path to the file that to be deleted, including the full name and extension of that file. For example, /examples/file.md is a fully qualified path to a file named file.md in a folder named examples.\n

    :type parentCommitId: string
    :param parentCommitId: [REQUIRED]\nThe ID of the commit that is the tip of the branch where you want to create the commit that deletes the file. This must be the HEAD commit for the branch. The commit that deletes the file is created from this commit ID.\n

    :type keepEmptyFolders: boolean
    :param keepEmptyFolders: If a file is the only object in the folder or directory, specifies whether to delete the folder or directory that contains the file. By default, empty folders are deleted. This includes empty folders that are part of the directory structure. For example, if the path to a file is dir1/dir2/dir3/dir4, and dir2 and dir3 are empty, deleting the last file in dir4 also deletes the empty folders dir4, dir3, and dir2.

    :type commitMessage: string
    :param commitMessage: The commit message you want to include as part of deleting the file. Commit messages are limited to 256 KB. If no message is specified, a default message is used.

    :type name: string
    :param name: The name of the author of the commit that deletes the file. If no name is specified, the user\'s ARN is used as the author name and committer name.

    :type email: string
    :param email: The email address for the commit that deletes the file. If no email address is specified, the email address is left blank.

    :rtype: dict

ReturnsResponse Syntax
{
    'commitId': 'string',
    'blobId': 'string',
    'treeId': 'string',
    'filePath': 'string'
}


Response Structure

(dict) --

commitId (string) --
The full commit ID of the commit that contains the change that deletes the file.

blobId (string) --
The blob ID removed from the tree as part of deleting the file.

treeId (string) --
The full SHA-1 pointer of the tree information for the commit that contains the delete file change.

filePath (string) --
The fully qualified path to the file to be deleted, including the full name and extension of that file.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.ParentCommitIdRequiredException
CodeCommit.Client.exceptions.InvalidParentCommitIdException
CodeCommit.Client.exceptions.ParentCommitDoesNotExistException
CodeCommit.Client.exceptions.ParentCommitIdOutdatedException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.FileDoesNotExistException
CodeCommit.Client.exceptions.BranchNameRequiredException
CodeCommit.Client.exceptions.InvalidBranchNameException
CodeCommit.Client.exceptions.BranchDoesNotExistException
CodeCommit.Client.exceptions.BranchNameIsTagNameException
CodeCommit.Client.exceptions.NameLengthExceededException
CodeCommit.Client.exceptions.InvalidEmailException
CodeCommit.Client.exceptions.CommitMessageLengthExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'commitId': 'string',
        'blobId': 'string',
        'treeId': 'string',
        'filePath': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.ParentCommitIdRequiredException
    CodeCommit.Client.exceptions.InvalidParentCommitIdException
    CodeCommit.Client.exceptions.ParentCommitDoesNotExistException
    CodeCommit.Client.exceptions.ParentCommitIdOutdatedException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.FileDoesNotExistException
    CodeCommit.Client.exceptions.BranchNameRequiredException
    CodeCommit.Client.exceptions.InvalidBranchNameException
    CodeCommit.Client.exceptions.BranchDoesNotExistException
    CodeCommit.Client.exceptions.BranchNameIsTagNameException
    CodeCommit.Client.exceptions.NameLengthExceededException
    CodeCommit.Client.exceptions.InvalidEmailException
    CodeCommit.Client.exceptions.CommitMessageLengthExceededException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def delete_pull_request_approval_rule(pullRequestId=None, approvalRuleName=None):
    """
    Deletes an approval rule from a specified pull request. Approval rules can be deleted from a pull request only if the pull request is open, and if the approval rule was created specifically for a pull request and not generated from an approval rule template associated with the repository where the pull request was created. You cannot delete an approval rule from a merged or closed pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_pull_request_approval_rule(
        pullRequestId='string',
        approvalRuleName='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request that contains the approval rule you want to delete.\n

    :type approvalRuleName: string
    :param approvalRuleName: [REQUIRED]\nThe name of the approval rule you want to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'approvalRuleId': 'string'
}


Response Structure

(dict) --

approvalRuleId (string) --
The ID of the deleted approval rule.

Note
If the approval rule was deleted in an earlier API call, the response is 200 OK without content.








Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
CodeCommit.Client.exceptions.ApprovalRuleNameRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleNameException
CodeCommit.Client.exceptions.CannotDeleteApprovalRuleFromTemplateException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'approvalRuleId': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
    CodeCommit.Client.exceptions.ApprovalRuleNameRequiredException
    CodeCommit.Client.exceptions.InvalidApprovalRuleNameException
    CodeCommit.Client.exceptions.CannotDeleteApprovalRuleFromTemplateException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def delete_repository(repositoryName=None):
    """
    Deletes a repository. If a specified repository was already deleted, a null repository ID is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_repository(
        repositoryName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to delete.\n

    :rtype: dict
ReturnsResponse Syntax{
    'repositoryId': 'string'
}


Response Structure

(dict) --Represents the output of a delete repository operation.

repositoryId (string) --The ID of the repository that was deleted.






Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'repositoryId': 'string'
    }
    
    
    """
    pass

def describe_merge_conflicts(repositoryName=None, destinationCommitSpecifier=None, sourceCommitSpecifier=None, mergeOption=None, maxMergeHunks=None, filePath=None, conflictDetailLevel=None, conflictResolutionStrategy=None, nextToken=None):
    """
    Returns information about one or more merge conflicts in the attempted merge of two commit specifiers using the squash or three-way merge strategy. If the merge option for the attempted merge is specified as FAST_FORWARD_MERGE, an exception is thrown.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_merge_conflicts(
        repositoryName='string',
        destinationCommitSpecifier='string',
        sourceCommitSpecifier='string',
        mergeOption='FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
        maxMergeHunks=123,
        filePath='string',
        conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
        conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
        nextToken='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to get information about a merge conflict.\n

    :type destinationCommitSpecifier: string
    :param destinationCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type sourceCommitSpecifier: string
    :param sourceCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type mergeOption: string
    :param mergeOption: [REQUIRED]\nThe merge option or strategy you want to use to merge the code.\n

    :type maxMergeHunks: integer
    :param maxMergeHunks: The maximum number of merge hunks to include in the output.

    :type filePath: string
    :param filePath: [REQUIRED]\nThe path of the target files used to describe the conflicts.\n

    :type conflictDetailLevel: string
    :param conflictDetailLevel: The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

    :type conflictResolutionStrategy: string
    :param conflictResolutionStrategy: Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

    :type nextToken: string
    :param nextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'conflictMetadata': {
        'filePath': 'string',
        'fileSizes': {
            'source': 123,
            'destination': 123,
            'base': 123
        },
        'fileModes': {
            'source': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
            'destination': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
            'base': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
        },
        'objectTypes': {
            'source': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
            'destination': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
            'base': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK'
        },
        'numberOfConflicts': 123,
        'isBinaryFile': {
            'source': True|False,
            'destination': True|False,
            'base': True|False
        },
        'contentConflict': True|False,
        'fileModeConflict': True|False,
        'objectTypeConflict': True|False,
        'mergeOperations': {
            'source': 'A'|'M'|'D',
            'destination': 'A'|'M'|'D'
        }
    },
    'mergeHunks': [
        {
            'isConflict': True|False,
            'source': {
                'startLine': 123,
                'endLine': 123,
                'hunkContent': 'string'
            },
            'destination': {
                'startLine': 123,
                'endLine': 123,
                'hunkContent': 'string'
            },
            'base': {
                'startLine': 123,
                'endLine': 123,
                'hunkContent': 'string'
            }
        },
    ],
    'nextToken': 'string',
    'destinationCommitId': 'string',
    'sourceCommitId': 'string',
    'baseCommitId': 'string'
}


Response Structure

(dict) --

conflictMetadata (dict) --
Contains metadata about the conflicts found in the merge.

filePath (string) --
The path of the file that contains conflicts.

fileSizes (dict) --
The file sizes of the file in the source, destination, and base of the merge.

source (integer) --
The size of a file in the source of a merge or pull request.

destination (integer) --
The size of a file in the destination of a merge or pull request.

base (integer) --
The size of a file in the base of a merge or pull request.



fileModes (dict) --
The file modes of the file in the source, destination, and base of the merge.

source (string) --
The file mode of a file in the source of a merge or pull request.

destination (string) --
The file mode of a file in the destination of a merge or pull request.

base (string) --
The file mode of a file in the base of a merge or pull request.



objectTypes (dict) --
Information about any object type conflicts in a merge operation.

source (string) --
The type of the object in the source branch.

destination (string) --
The type of the object in the destination branch.

base (string) --
The type of the object in the base commit of the merge.



numberOfConflicts (integer) --
The number of conflicts, including both hunk conflicts and metadata conflicts.

isBinaryFile (dict) --
A boolean value (true or false) indicating whether the file is binary or textual in the source, destination, and base of the merge.

source (boolean) --
The binary or non-binary status of file in the source of a merge or pull request.

destination (boolean) --
The binary or non-binary status of a file in the destination of a merge or pull request.

base (boolean) --
The binary or non-binary status of a file in the base of a merge or pull request.



contentConflict (boolean) --
A boolean value indicating whether there are conflicts in the content of a file.

fileModeConflict (boolean) --
A boolean value indicating whether there are conflicts in the file mode of a file.

objectTypeConflict (boolean) --
A boolean value (true or false) indicating whether there are conflicts between the branches in the object type of a file, folder, or submodule.

mergeOperations (dict) --
Whether an add, modify, or delete operation caused the conflict between the source and destination of the merge.

source (string) --
The operation (add, modify, or delete) on a file in the source of a merge or pull request.

destination (string) --
The operation on a file in the destination of a merge or pull request.





mergeHunks (list) --
A list of merge hunks of the differences between the files or lines.

(dict) --
Information about merge hunks in a merge or pull request operation.

isConflict (boolean) --
A Boolean value indicating whether a combination of hunks contains a conflict. Conflicts occur when the same file or the same lines in a file were modified in both the source and destination of a merge or pull request. Valid values include true, false, and null. True when the hunk represents a conflict and one or more files contains a line conflict. File mode conflicts in a merge do not set this to true.

source (dict) --
Information about the merge hunk in the source of a merge or pull request.

startLine (integer) --
The start position of the hunk in the merge result.

endLine (integer) --
The end position of the hunk in the merge result.

hunkContent (string) --
The base-64 encoded content of the hunk merged region that might contain a conflict.



destination (dict) --
Information about the merge hunk in the destination of a merge or pull request.

startLine (integer) --
The start position of the hunk in the merge result.

endLine (integer) --
The end position of the hunk in the merge result.

hunkContent (string) --
The base-64 encoded content of the hunk merged region that might contain a conflict.



base (dict) --
Information about the merge hunk in the base of a merge or pull request.

startLine (integer) --
The start position of the hunk in the merge result.

endLine (integer) --
The end position of the hunk in the merge result.

hunkContent (string) --
The base-64 encoded content of the hunk merged region that might contain a conflict.







nextToken (string) --
An enumeration token that can be used in a request to return the next batch of the results.

destinationCommitId (string) --
The commit ID of the destination commit specifier that was used in the merge evaluation.

sourceCommitId (string) --
The commit ID of the source commit specifier that was used in the merge evaluation.

baseCommitId (string) --
The commit ID of the merge base.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.MergeOptionRequiredException
CodeCommit.Client.exceptions.InvalidMergeOptionException
CodeCommit.Client.exceptions.InvalidContinuationTokenException
CodeCommit.Client.exceptions.CommitRequiredException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.TipsDivergenceExceededException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.FileDoesNotExistException
CodeCommit.Client.exceptions.InvalidMaxMergeHunksException
CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'conflictMetadata': {
            'filePath': 'string',
            'fileSizes': {
                'source': 123,
                'destination': 123,
                'base': 123
            },
            'fileModes': {
                'source': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                'destination': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                'base': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
            },
            'objectTypes': {
                'source': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                'destination': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                'base': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK'
            },
            'numberOfConflicts': 123,
            'isBinaryFile': {
                'source': True|False,
                'destination': True|False,
                'base': True|False
            },
            'contentConflict': True|False,
            'fileModeConflict': True|False,
            'objectTypeConflict': True|False,
            'mergeOperations': {
                'source': 'A'|'M'|'D',
                'destination': 'A'|'M'|'D'
            }
        },
        'mergeHunks': [
            {
                'isConflict': True|False,
                'source': {
                    'startLine': 123,
                    'endLine': 123,
                    'hunkContent': 'string'
                },
                'destination': {
                    'startLine': 123,
                    'endLine': 123,
                    'hunkContent': 'string'
                },
                'base': {
                    'startLine': 123,
                    'endLine': 123,
                    'hunkContent': 'string'
                }
            },
        ],
        'nextToken': 'string',
        'destinationCommitId': 'string',
        'sourceCommitId': 'string',
        'baseCommitId': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.MergeOptionRequiredException
    CodeCommit.Client.exceptions.InvalidMergeOptionException
    CodeCommit.Client.exceptions.InvalidContinuationTokenException
    CodeCommit.Client.exceptions.CommitRequiredException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidCommitException
    CodeCommit.Client.exceptions.TipsDivergenceExceededException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.FileDoesNotExistException
    CodeCommit.Client.exceptions.InvalidMaxMergeHunksException
    CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
    CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
    CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
    CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def describe_pull_request_events(pullRequestId=None, pullRequestEventType=None, actorArn=None, nextToken=None, maxResults=None):
    """
    Returns information about one or more pull request events.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_pull_request_events(
        pullRequestId='string',
        pullRequestEventType='PULL_REQUEST_CREATED'|'PULL_REQUEST_STATUS_CHANGED'|'PULL_REQUEST_SOURCE_REFERENCE_UPDATED'|'PULL_REQUEST_MERGE_STATE_CHANGED'|'PULL_REQUEST_APPROVAL_RULE_CREATED'|'PULL_REQUEST_APPROVAL_RULE_UPDATED'|'PULL_REQUEST_APPROVAL_RULE_DELETED'|'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN'|'PULL_REQUEST_APPROVAL_STATE_CHANGED',
        actorArn='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request. To get this ID, use ListPullRequests .\n

    :type pullRequestEventType: string
    :param pullRequestEventType: Optional. The pull request event type about which you want to return information.

    :type actorArn: string
    :param actorArn: The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with more commits or changing the status of a pull request.

    :type nextToken: string
    :param nextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-zero, non-negative integer used to limit the number of returned results. The default is 100 events, which is also the maximum number of events that can be returned in a result.

    :rtype: dict

ReturnsResponse Syntax
{
    'pullRequestEvents': [
        {
            'pullRequestId': 'string',
            'eventDate': datetime(2015, 1, 1),
            'pullRequestEventType': 'PULL_REQUEST_CREATED'|'PULL_REQUEST_STATUS_CHANGED'|'PULL_REQUEST_SOURCE_REFERENCE_UPDATED'|'PULL_REQUEST_MERGE_STATE_CHANGED'|'PULL_REQUEST_APPROVAL_RULE_CREATED'|'PULL_REQUEST_APPROVAL_RULE_UPDATED'|'PULL_REQUEST_APPROVAL_RULE_DELETED'|'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN'|'PULL_REQUEST_APPROVAL_STATE_CHANGED',
            'actorArn': 'string',
            'pullRequestCreatedEventMetadata': {
                'repositoryName': 'string',
                'sourceCommitId': 'string',
                'destinationCommitId': 'string',
                'mergeBase': 'string'
            },
            'pullRequestStatusChangedEventMetadata': {
                'pullRequestStatus': 'OPEN'|'CLOSED'
            },
            'pullRequestSourceReferenceUpdatedEventMetadata': {
                'repositoryName': 'string',
                'beforeCommitId': 'string',
                'afterCommitId': 'string',
                'mergeBase': 'string'
            },
            'pullRequestMergedStateChangedEventMetadata': {
                'repositoryName': 'string',
                'destinationReference': 'string',
                'mergeMetadata': {
                    'isMerged': True|False,
                    'mergedBy': 'string',
                    'mergeCommitId': 'string',
                    'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                }
            },
            'approvalRuleEventMetadata': {
                'approvalRuleName': 'string',
                'approvalRuleId': 'string',
                'approvalRuleContent': 'string'
            },
            'approvalStateChangedEventMetadata': {
                'revisionId': 'string',
                'approvalStatus': 'APPROVE'|'REVOKE'
            },
            'approvalRuleOverriddenEventMetadata': {
                'revisionId': 'string',
                'overrideStatus': 'OVERRIDE'|'REVOKE'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

pullRequestEvents (list) --
Information about the pull request events.

(dict) --
Returns information about a pull request event.

pullRequestId (string) --
The system-generated ID of the pull request.

eventDate (datetime) --
The day and time of the pull request event, in timestamp format.

pullRequestEventType (string) --
The type of the pull request event (for example, a status change event (PULL_REQUEST_STATUS_CHANGED) or update event (PULL_REQUEST_SOURCE_REFERENCE_UPDATED)).

actorArn (string) --
The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with more commits or changing the status of a pull request.

pullRequestCreatedEventMetadata (dict) --
Information about the source and destination branches for the pull request.

repositoryName (string) --
The name of the repository where the pull request was created.

sourceCommitId (string) --
The commit ID on the source branch used when the pull request was created.

destinationCommitId (string) --
The commit ID of the tip of the branch specified as the destination branch when the pull request was created.

mergeBase (string) --
The commit ID of the most recent commit that the source branch and the destination branch have in common.



pullRequestStatusChangedEventMetadata (dict) --
Information about the change in status for the pull request event.

pullRequestStatus (string) --
The changed status of the pull request.



pullRequestSourceReferenceUpdatedEventMetadata (dict) --
Information about the updated source branch for the pull request event.

repositoryName (string) --
The name of the repository where the pull request was updated.

beforeCommitId (string) --
The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was updated.

afterCommitId (string) --
The full commit ID of the commit in the source branch that was the tip of the branch at the time the pull request was updated.

mergeBase (string) --
The commit ID of the most recent commit that the source branch and the destination branch have in common.



pullRequestMergedStateChangedEventMetadata (dict) --
Information about the change in mergability state for the pull request event.

repositoryName (string) --
The name of the repository where the pull request was created.

destinationReference (string) --
The name of the branch that the pull request is merged into.

mergeMetadata (dict) --
Information about the merge state change event.

isMerged (boolean) --
A Boolean value indicating whether the merge has been made.

mergedBy (string) --
The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId (string) --
The commit ID for the merge commit, if any.

mergeOption (string) --
The merge strategy used in the merge.





approvalRuleEventMetadata (dict) --
Information about a pull request event.

approvalRuleName (string) --
The name of the approval rule.

approvalRuleId (string) --
The system-generated ID of the approval rule.

approvalRuleContent (string) --
The content of the approval rule.



approvalStateChangedEventMetadata (dict) --
Information about an approval state change for a pull request.

revisionId (string) --
The revision ID of the pull request when the approval state changed.

approvalStatus (string) --
The approval status for the pull request.



approvalRuleOverriddenEventMetadata (dict) --
Information about an approval rule override event for a pull request.

revisionId (string) --
The revision ID of the pull request when the override event occurred.

overrideStatus (string) --
The status of the override event.







nextToken (string) --
An enumeration token that can be used in a request to return the next batch of the results.







Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.InvalidPullRequestEventTypeException
CodeCommit.Client.exceptions.InvalidActorArnException
CodeCommit.Client.exceptions.ActorDoesNotExistException
CodeCommit.Client.exceptions.InvalidMaxResultsException
CodeCommit.Client.exceptions.InvalidContinuationTokenException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'pullRequestEvents': [
            {
                'pullRequestId': 'string',
                'eventDate': datetime(2015, 1, 1),
                'pullRequestEventType': 'PULL_REQUEST_CREATED'|'PULL_REQUEST_STATUS_CHANGED'|'PULL_REQUEST_SOURCE_REFERENCE_UPDATED'|'PULL_REQUEST_MERGE_STATE_CHANGED'|'PULL_REQUEST_APPROVAL_RULE_CREATED'|'PULL_REQUEST_APPROVAL_RULE_UPDATED'|'PULL_REQUEST_APPROVAL_RULE_DELETED'|'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN'|'PULL_REQUEST_APPROVAL_STATE_CHANGED',
                'actorArn': 'string',
                'pullRequestCreatedEventMetadata': {
                    'repositoryName': 'string',
                    'sourceCommitId': 'string',
                    'destinationCommitId': 'string',
                    'mergeBase': 'string'
                },
                'pullRequestStatusChangedEventMetadata': {
                    'pullRequestStatus': 'OPEN'|'CLOSED'
                },
                'pullRequestSourceReferenceUpdatedEventMetadata': {
                    'repositoryName': 'string',
                    'beforeCommitId': 'string',
                    'afterCommitId': 'string',
                    'mergeBase': 'string'
                },
                'pullRequestMergedStateChangedEventMetadata': {
                    'repositoryName': 'string',
                    'destinationReference': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string',
                        'mergeCommitId': 'string',
                        'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                    }
                },
                'approvalRuleEventMetadata': {
                    'approvalRuleName': 'string',
                    'approvalRuleId': 'string',
                    'approvalRuleContent': 'string'
                },
                'approvalStateChangedEventMetadata': {
                    'revisionId': 'string',
                    'approvalStatus': 'APPROVE'|'REVOKE'
                },
                'approvalRuleOverriddenEventMetadata': {
                    'revisionId': 'string',
                    'overrideStatus': 'OVERRIDE'|'REVOKE'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.InvalidPullRequestEventTypeException
    CodeCommit.Client.exceptions.InvalidActorArnException
    CodeCommit.Client.exceptions.ActorDoesNotExistException
    CodeCommit.Client.exceptions.InvalidMaxResultsException
    CodeCommit.Client.exceptions.InvalidContinuationTokenException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def disassociate_approval_rule_template_from_repository(approvalRuleTemplateName=None, repositoryName=None):
    """
    Removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository. This does not delete any approval rules previously created for pull requests through the template association.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disassociate_approval_rule_template_from_repository(
        approvalRuleTemplateName='string',
        repositoryName='string'
    )
    
    
    :type approvalRuleTemplateName: string
    :param approvalRuleTemplateName: [REQUIRED]\nThe name of the approval rule template to disassociate from a specified repository.\n

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository you want to disassociate from the template.\n

    :returns: 
    CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
    CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def evaluate_pull_request_approval_rules(pullRequestId=None, revisionId=None):
    """
    Evaluates whether a pull request has met all the conditions specified in its associated approval rules.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.evaluate_pull_request_approval_rules(
        pullRequestId='string',
        revisionId='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request you want to evaluate.\n

    :type revisionId: string
    :param revisionId: [REQUIRED]\nThe system-generated ID for the pull request revision. To retrieve the most recent revision ID for a pull request, use GetPullRequest .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'evaluation': {
        'approved': True|False,
        'overridden': True|False,
        'approvalRulesSatisfied': [
            'string',
        ],
        'approvalRulesNotSatisfied': [
            'string',
        ]
    }
}


Response Structure

(dict) --

evaluation (dict) --
The result of the evaluation, including the names of the rules whose conditions have been met (if any), the names of the rules whose conditions have not been met (if any), whether the pull request is in the approved state, and whether the pull request approval rule has been set aside by an override.

approved (boolean) --
Whether the state of the pull request is approved.

overridden (boolean) --
Whether the approval rule requirements for the pull request have been overridden and no longer need to be met.

approvalRulesSatisfied (list) --
The names of the approval rules that have had their conditions met.

(string) --


approvalRulesNotSatisfied (list) --
The names of the approval rules that have not had their conditions met.

(string) --










Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.InvalidRevisionIdException
CodeCommit.Client.exceptions.RevisionIdRequiredException
CodeCommit.Client.exceptions.RevisionNotCurrentException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'evaluation': {
            'approved': True|False,
            'overridden': True|False,
            'approvalRulesSatisfied': [
                'string',
            ],
            'approvalRulesNotSatisfied': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    (string) --
    
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

def get_approval_rule_template(approvalRuleTemplateName=None):
    """
    Returns information about a specified approval rule template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_approval_rule_template(
        approvalRuleTemplateName='string'
    )
    
    
    :type approvalRuleTemplateName: string
    :param approvalRuleTemplateName: [REQUIRED]\nThe name of the approval rule template for which you want to get information.\n

    :rtype: dict
ReturnsResponse Syntax{
    'approvalRuleTemplate': {
        'approvalRuleTemplateId': 'string',
        'approvalRuleTemplateName': 'string',
        'approvalRuleTemplateDescription': 'string',
        'approvalRuleTemplateContent': 'string',
        'ruleContentSha256': 'string',
        'lastModifiedDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedUser': 'string'
    }
}


Response Structure

(dict) --
approvalRuleTemplate (dict) --The content and structure of the approval rule template.

approvalRuleTemplateId (string) --The system-generated ID of the approval rule template.

approvalRuleTemplateName (string) --The name of the approval rule template.

approvalRuleTemplateDescription (string) --The description of the approval rule template.

approvalRuleTemplateContent (string) --The content of the approval rule template.

ruleContentSha256 (string) --The SHA-256 hash signature for the content of the approval rule template.

lastModifiedDate (datetime) --The date the approval rule template was most recently changed, in timestamp format.

creationDate (datetime) --The date the approval rule template was created, in timestamp format.

lastModifiedUser (string) --The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule template.








Exceptions

CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException


    :return: {
        'approvalRuleTemplate': {
            'approvalRuleTemplateId': 'string',
            'approvalRuleTemplateName': 'string',
            'approvalRuleTemplateDescription': 'string',
            'approvalRuleTemplateContent': 'string',
            'ruleContentSha256': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedUser': 'string'
        }
    }
    
    
    """
    pass

def get_blob(repositoryName=None, blobId=None):
    """
    Returns the base-64 encoded content of an individual blob in a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_blob(
        repositoryName='string',
        blobId='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that contains the blob.\n

    :type blobId: string
    :param blobId: [REQUIRED]\nThe ID of the blob, which is its SHA-1 pointer.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'content': b'bytes'
}


Response Structure

(dict) --
Represents the output of a get blob operation.

content (bytes) --
The content of the blob, usually a file.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.BlobIdRequiredException
CodeCommit.Client.exceptions.InvalidBlobIdException
CodeCommit.Client.exceptions.BlobIdDoesNotExistException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
CodeCommit.Client.exceptions.FileTooLargeException


    :return: {
        'content': b'bytes'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.BlobIdRequiredException
    CodeCommit.Client.exceptions.InvalidBlobIdException
    CodeCommit.Client.exceptions.BlobIdDoesNotExistException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    CodeCommit.Client.exceptions.FileTooLargeException
    
    """
    pass

def get_branch(repositoryName=None, branchName=None):
    """
    Returns information about a repository branch, including its name and the last commit ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_branch(
        repositoryName='string',
        branchName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: The name of the repository that contains the branch for which you want to retrieve information.

    :type branchName: string
    :param branchName: The name of the branch for which you want to retrieve information.

    :rtype: dict

ReturnsResponse Syntax
{
    'branch': {
        'branchName': 'string',
        'commitId': 'string'
    }
}


Response Structure

(dict) --
Represents the output of a get branch operation.

branch (dict) --
The name of the branch.

branchName (string) --
The name of the branch.

commitId (string) --
The ID of the last commit made to the branch.









Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.BranchNameRequiredException
CodeCommit.Client.exceptions.InvalidBranchNameException
CodeCommit.Client.exceptions.BranchDoesNotExistException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'branch': {
            'branchName': 'string',
            'commitId': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.BranchNameRequiredException
    CodeCommit.Client.exceptions.InvalidBranchNameException
    CodeCommit.Client.exceptions.BranchDoesNotExistException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def get_comment(commentId=None):
    """
    Returns the content of a comment made on a change, file, or commit in a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_comment(
        commentId='string'
    )
    
    
    :type commentId: string
    :param commentId: [REQUIRED]\nThe unique, system-generated ID of the comment. To get this ID, use GetCommentsForComparedCommit or GetCommentsForPullRequest .\n

    :rtype: dict
ReturnsResponse Syntax{
    'comment': {
        'commentId': 'string',
        'content': 'string',
        'inReplyTo': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'authorArn': 'string',
        'deleted': True|False,
        'clientRequestToken': 'string'
    }
}


Response Structure

(dict) --
comment (dict) --The contents of the comment.

commentId (string) --The system-generated comment ID.

content (string) --The content of the comment.

inReplyTo (string) --The ID of the comment for which this comment is a reply, if any.

creationDate (datetime) --The date and time the comment was created, in timestamp format.

lastModifiedDate (datetime) --The date and time the comment was most recently modified, in timestamp format.

authorArn (string) --The Amazon Resource Name (ARN) of the person who posted the comment.

deleted (boolean) --A Boolean value indicating whether the comment has been deleted.

clientRequestToken (string) --A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.








Exceptions

CodeCommit.Client.exceptions.CommentDoesNotExistException
CodeCommit.Client.exceptions.CommentIdRequiredException
CodeCommit.Client.exceptions.InvalidCommentIdException
CodeCommit.Client.exceptions.CommentDeletedException


    :return: {
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    """
    pass

def get_comments_for_compared_commit(repositoryName=None, beforeCommitId=None, afterCommitId=None, nextToken=None, maxResults=None):
    """
    Returns information about comments made on the comparison between two commits.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_comments_for_compared_commit(
        repositoryName='string',
        beforeCommitId='string',
        afterCommitId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to compare commits.\n

    :type beforeCommitId: string
    :param beforeCommitId: To establish the directionality of the comparison, the full commit ID of the before commit.

    :type afterCommitId: string
    :param afterCommitId: [REQUIRED]\nTo establish the directionality of the comparison, the full commit ID of the after commit.\n

    :type nextToken: string
    :param nextToken: An enumeration token that when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-zero, non-negative integer used to limit the number of returned results. The default is 100 comments, but you can configure up to 500.

    :rtype: dict

ReturnsResponse Syntax
{
    'commentsForComparedCommitData': [
        {
            'repositoryName': 'string',
            'beforeCommitId': 'string',
            'afterCommitId': 'string',
            'beforeBlobId': 'string',
            'afterBlobId': 'string',
            'location': {
                'filePath': 'string',
                'filePosition': 123,
                'relativeFileVersion': 'BEFORE'|'AFTER'
            },
            'comments': [
                {
                    'commentId': 'string',
                    'content': 'string',
                    'inReplyTo': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'authorArn': 'string',
                    'deleted': True|False,
                    'clientRequestToken': 'string'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

commentsForComparedCommitData (list) --
A list of comment objects on the compared commit.

(dict) --
Returns information about comments on the comparison between two commits.

repositoryName (string) --
The name of the repository that contains the compared commits.

beforeCommitId (string) --
The full commit ID of the commit used to establish the before of the comparison.

afterCommitId (string) --
The full commit ID of the commit used to establish the after of the comparison.

beforeBlobId (string) --
The full blob ID of the commit used to establish the before of the comparison.

afterBlobId (string) --
The full blob ID of the commit used to establish the after of the comparison.

location (dict) --
Location information about the comment on the comparison, including the file name, line number, and whether the version of the file where the comment was made is BEFORE or AFTER.

filePath (string) --
The name of the file being compared, including its extension and subdirectory, if any.

filePosition (integer) --
The position of a change in a compared file, in line number format.

relativeFileVersion (string) --
In a comparison of commits or a pull request, whether the change is in the before or after of that comparison.



comments (list) --
An array of comment objects. Each comment object contains information about a comment on the comparison between commits.

(dict) --
Returns information about a specific comment.

commentId (string) --
The system-generated comment ID.

content (string) --
The content of the comment.

inReplyTo (string) --
The ID of the comment for which this comment is a reply, if any.

creationDate (datetime) --
The date and time the comment was created, in timestamp format.

lastModifiedDate (datetime) --
The date and time the comment was most recently modified, in timestamp format.

authorArn (string) --
The Amazon Resource Name (ARN) of the person who posted the comment.

deleted (boolean) --
A Boolean value indicating whether the comment has been deleted.

clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.









nextToken (string) --
An enumeration token that can be used in a request to return the next batch of the results.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.CommitIdRequiredException
CodeCommit.Client.exceptions.InvalidCommitIdException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidMaxResultsException
CodeCommit.Client.exceptions.InvalidContinuationTokenException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'commentsForComparedCommitData': [
            {
                'repositoryName': 'string',
                'beforeCommitId': 'string',
                'afterCommitId': 'string',
                'beforeBlobId': 'string',
                'afterBlobId': 'string',
                'location': {
                    'filePath': 'string',
                    'filePosition': 123,
                    'relativeFileVersion': 'BEFORE'|'AFTER'
                },
                'comments': [
                    {
                        'commentId': 'string',
                        'content': 'string',
                        'inReplyTo': 'string',
                        'creationDate': datetime(2015, 1, 1),
                        'lastModifiedDate': datetime(2015, 1, 1),
                        'authorArn': 'string',
                        'deleted': True|False,
                        'clientRequestToken': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.CommitIdRequiredException
    CodeCommit.Client.exceptions.InvalidCommitIdException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidMaxResultsException
    CodeCommit.Client.exceptions.InvalidContinuationTokenException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def get_comments_for_pull_request(pullRequestId=None, repositoryName=None, beforeCommitId=None, afterCommitId=None, nextToken=None, maxResults=None):
    """
    Returns comments made on a pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_comments_for_pull_request(
        pullRequestId='string',
        repositoryName='string',
        beforeCommitId='string',
        afterCommitId='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request. To get this ID, use ListPullRequests .\n

    :type repositoryName: string
    :param repositoryName: The name of the repository that contains the pull request.

    :type beforeCommitId: string
    :param beforeCommitId: The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created.

    :type afterCommitId: string
    :param afterCommitId: The full commit ID of the commit in the source branch that was the tip of the branch at the time the comment was made.

    :type nextToken: string
    :param nextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-zero, non-negative integer used to limit the number of returned results. The default is 100 comments. You can return up to 500 comments with a single request.

    :rtype: dict

ReturnsResponse Syntax
{
    'commentsForPullRequestData': [
        {
            'pullRequestId': 'string',
            'repositoryName': 'string',
            'beforeCommitId': 'string',
            'afterCommitId': 'string',
            'beforeBlobId': 'string',
            'afterBlobId': 'string',
            'location': {
                'filePath': 'string',
                'filePosition': 123,
                'relativeFileVersion': 'BEFORE'|'AFTER'
            },
            'comments': [
                {
                    'commentId': 'string',
                    'content': 'string',
                    'inReplyTo': 'string',
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'authorArn': 'string',
                    'deleted': True|False,
                    'clientRequestToken': 'string'
                },
            ]
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

commentsForPullRequestData (list) --
An array of comment objects on the pull request.

(dict) --
Returns information about comments on a pull request.

pullRequestId (string) --
The system-generated ID of the pull request.

repositoryName (string) --
The name of the repository that contains the pull request.

beforeCommitId (string) --
The full commit ID of the commit that was the tip of the destination branch when the pull request was created. This commit is superceded by the after commit in the source branch when and if you merge the source branch into the destination branch.

afterCommitId (string) --
The full commit ID of the commit that was the tip of the source branch at the time the comment was made.

beforeBlobId (string) --
The full blob ID of the file on which you want to comment on the destination commit.

afterBlobId (string) --
The full blob ID of the file on which you want to comment on the source commit.

location (dict) --
Location information about the comment on the pull request, including the file name, line number, and whether the version of the file where the comment was made is BEFORE (destination branch) or AFTER (source branch).

filePath (string) --
The name of the file being compared, including its extension and subdirectory, if any.

filePosition (integer) --
The position of a change in a compared file, in line number format.

relativeFileVersion (string) --
In a comparison of commits or a pull request, whether the change is in the before or after of that comparison.



comments (list) --
An array of comment objects. Each comment object contains information about a comment on the pull request.

(dict) --
Returns information about a specific comment.

commentId (string) --
The system-generated comment ID.

content (string) --
The content of the comment.

inReplyTo (string) --
The ID of the comment for which this comment is a reply, if any.

creationDate (datetime) --
The date and time the comment was created, in timestamp format.

lastModifiedDate (datetime) --
The date and time the comment was most recently modified, in timestamp format.

authorArn (string) --
The Amazon Resource Name (ARN) of the person who posted the comment.

deleted (boolean) --
A Boolean value indicating whether the comment has been deleted.

clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.









nextToken (string) --
An enumeration token that can be used in a request to return the next batch of the results.







Exceptions

CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.CommitIdRequiredException
CodeCommit.Client.exceptions.InvalidCommitIdException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidMaxResultsException
CodeCommit.Client.exceptions.InvalidContinuationTokenException
CodeCommit.Client.exceptions.RepositoryNotAssociatedWithPullRequestException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'commentsForPullRequestData': [
            {
                'pullRequestId': 'string',
                'repositoryName': 'string',
                'beforeCommitId': 'string',
                'afterCommitId': 'string',
                'beforeBlobId': 'string',
                'afterBlobId': 'string',
                'location': {
                    'filePath': 'string',
                    'filePosition': 123,
                    'relativeFileVersion': 'BEFORE'|'AFTER'
                },
                'comments': [
                    {
                        'commentId': 'string',
                        'content': 'string',
                        'inReplyTo': 'string',
                        'creationDate': datetime(2015, 1, 1),
                        'lastModifiedDate': datetime(2015, 1, 1),
                        'authorArn': 'string',
                        'deleted': True|False,
                        'clientRequestToken': 'string'
                    },
                ]
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.CommitIdRequiredException
    CodeCommit.Client.exceptions.InvalidCommitIdException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidMaxResultsException
    CodeCommit.Client.exceptions.InvalidContinuationTokenException
    CodeCommit.Client.exceptions.RepositoryNotAssociatedWithPullRequestException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def get_commit(repositoryName=None, commitId=None):
    """
    Returns information about a commit, including commit message and committer information.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_commit(
        repositoryName='string',
        commitId='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to which the commit was made.\n

    :type commitId: string
    :param commitId: [REQUIRED]\nThe commit ID. Commit IDs are the full SHA ID of the commit.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'commit': {
        'commitId': 'string',
        'treeId': 'string',
        'parents': [
            'string',
        ],
        'message': 'string',
        'author': {
            'name': 'string',
            'email': 'string',
            'date': 'string'
        },
        'committer': {
            'name': 'string',
            'email': 'string',
            'date': 'string'
        },
        'additionalData': 'string'
    }
}


Response Structure

(dict) --
Represents the output of a get commit operation.

commit (dict) --
A commit data type object that contains information about the specified commit.

commitId (string) --
The full SHA ID of the specified commit.

treeId (string) --
Tree information for the specified commit.

parents (list) --
A list of parent commits for the specified commit. Each parent commit ID is the full commit ID.

(string) --


message (string) --
The commit message associated with the specified commit.

author (dict) --
Information about the author of the specified commit. Information includes the date in timestamp format with GMT offset, the name of the author, and the email address for the author, as configured in Git.

name (string) --
The name of the user who made the specified commit.

email (string) --
The email address associated with the user who made the commit, if any.

date (string) --
The date when the specified commit was commited, in timestamp format with GMT offset.



committer (dict) --
Information about the person who committed the specified commit, also known as the committer. Information includes the date in timestamp format with GMT offset, the name of the committer, and the email address for the committer, as configured in Git.
For more information about the difference between an author and a committer in Git, see Viewing the Commit History in Pro Git by Scott Chacon and Ben Straub.

name (string) --
The name of the user who made the specified commit.

email (string) --
The email address associated with the user who made the commit, if any.

date (string) --
The date when the specified commit was commited, in timestamp format with GMT offset.



additionalData (string) --
Any other data associated with the specified commit.









Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.CommitIdRequiredException
CodeCommit.Client.exceptions.InvalidCommitIdException
CodeCommit.Client.exceptions.CommitIdDoesNotExistException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'commit': {
            'commitId': 'string',
            'treeId': 'string',
            'parents': [
                'string',
            ],
            'message': 'string',
            'author': {
                'name': 'string',
                'email': 'string',
                'date': 'string'
            },
            'committer': {
                'name': 'string',
                'email': 'string',
                'date': 'string'
            },
            'additionalData': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_differences(repositoryName=None, beforeCommitSpecifier=None, afterCommitSpecifier=None, beforePath=None, afterPath=None, MaxResults=None, NextToken=None):
    """
    Returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference). Results can be limited to a specified path.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_differences(
        repositoryName='string',
        beforeCommitSpecifier='string',
        afterCommitSpecifier='string',
        beforePath='string',
        afterPath='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to get differences.\n

    :type beforeCommitSpecifier: string
    :param beforeCommitSpecifier: The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, the full commit ID). Optional. If not specified, all changes before the afterCommitSpecifier value are shown. If you do not use beforeCommitSpecifier in your request, consider limiting the results with maxResults .

    :type afterCommitSpecifier: string
    :param afterCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit.\n

    :type beforePath: string
    :param beforePath: The file path in which to check for differences. Limits the results to this path. Can also be used to specify the previous name of a directory or folder. If beforePath and afterPath are not specified, differences are shown for all paths.

    :type afterPath: string
    :param afterPath: The file path in which to check differences. Limits the results to this path. Can also be used to specify the changed name of a directory or folder, if it has changed. If not specified, differences are shown for all paths.

    :type MaxResults: integer
    :param MaxResults: A non-zero, non-negative integer used to limit the number of returned results.

    :type NextToken: string
    :param NextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'differences': [
        {
            'beforeBlob': {
                'blobId': 'string',
                'path': 'string',
                'mode': 'string'
            },
            'afterBlob': {
                'blobId': 'string',
                'path': 'string',
                'mode': 'string'
            },
            'changeType': 'A'|'M'|'D'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

differences (list) --
A data type object that contains information about the differences, including whether the difference is added, modified, or deleted (A, D, M).

(dict) --
Returns information about a set of differences for a commit specifier.

beforeBlob (dict) --
Information about a beforeBlob data type object, including the ID, the file mode permission code, and the path.

blobId (string) --
The full ID of the blob.

path (string) --
The path to the blob and associated file name, if any.

mode (string) --
The file mode permissions of the blob. File mode permission codes include:

100644 indicates read/write
100755 indicates read/write/execute
160000 indicates a submodule
120000 indicates a symlink




afterBlob (dict) --
Information about an afterBlob data type object, including the ID, the file mode permission code, and the path.

blobId (string) --
The full ID of the blob.

path (string) --
The path to the blob and associated file name, if any.

mode (string) --
The file mode permissions of the blob. File mode permission codes include:

100644 indicates read/write
100755 indicates read/write/execute
160000 indicates a submodule
120000 indicates a symlink




changeType (string) --
Whether the change type of the difference is an addition (A), deletion (D), or modification (M).





NextToken (string) --
An enumeration token that can be used in a request to return the next batch of the results.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.InvalidContinuationTokenException
CodeCommit.Client.exceptions.InvalidMaxResultsException
CodeCommit.Client.exceptions.InvalidCommitIdException
CodeCommit.Client.exceptions.CommitRequiredException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.PathDoesNotExistException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'differences': [
            {
                'beforeBlob': {
                    'blobId': 'string',
                    'path': 'string',
                    'mode': 'string'
                },
                'afterBlob': {
                    'blobId': 'string',
                    'path': 'string',
                    'mode': 'string'
                },
                'changeType': 'A'|'M'|'D'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    100644 indicates read/write
    100755 indicates read/write/execute
    160000 indicates a submodule
    120000 indicates a symlink
    
    """
    pass

def get_file(repositoryName=None, commitSpecifier=None, filePath=None):
    """
    Returns the base-64 encoded contents of a specified file and its metadata.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_file(
        repositoryName='string',
        commitSpecifier='string',
        filePath='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that contains the file.\n

    :type commitSpecifier: string
    :param commitSpecifier: The fully quaified reference that identifies the commit that contains the file. For example, you can specify a full commit ID, a tag, a branch name, or a reference such as refs/heads/master. If none is provided, the head commit is used.

    :type filePath: string
    :param filePath: [REQUIRED]\nThe fully qualified path to the file, including the full name and extension of the file. For example, /examples/file.md is the fully qualified path to a file named file.md in a folder named examples.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'commitId': 'string',
    'blobId': 'string',
    'filePath': 'string',
    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
    'fileSize': 123,
    'fileContent': b'bytes'
}


Response Structure

(dict) --

commitId (string) --
The full commit ID of the commit that contains the content returned by GetFile.

blobId (string) --
The blob ID of the object that represents the file content.

filePath (string) --
The fully qualified path to the specified file. Returns the name and extension of the file.

fileMode (string) --
The extrapolated file mode permissions of the blob. Valid values include strings such as EXECUTABLE and not numeric values.

Note
The file mode permissions returned by this API are not the standard file mode permission values, such as 100644, but rather extrapolated values. See the supported return values.


fileSize (integer) --
The size of the contents of the file, in bytes.

fileContent (bytes) --
The base-64 encoded binary data object that represents the content of the file.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.FileDoesNotExistException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
CodeCommit.Client.exceptions.FileTooLargeException


    :return: {
        'commitId': 'string',
        'blobId': 'string',
        'filePath': 'string',
        'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
        'fileSize': 123,
        'fileContent': b'bytes'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidCommitException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.FileDoesNotExistException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    CodeCommit.Client.exceptions.FileTooLargeException
    
    """
    pass

def get_folder(repositoryName=None, commitSpecifier=None, folderPath=None):
    """
    Returns the contents of a specified folder in a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_folder(
        repositoryName='string',
        commitSpecifier='string',
        folderPath='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository.\n

    :type commitSpecifier: string
    :param commitSpecifier: A fully qualified reference used to identify a commit that contains the version of the folder\'s content to return. A fully qualified reference can be a commit ID, branch name, tag, or reference such as HEAD. If no specifier is provided, the folder content is returned as it exists in the HEAD commit.

    :type folderPath: string
    :param folderPath: [REQUIRED]\nThe fully qualified path to the folder whose contents are returned, including the folder name. For example, /examples is a fully-qualified path to a folder named examples that was created off of the root directory (/) of a repository.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'commitId': 'string',
    'folderPath': 'string',
    'treeId': 'string',
    'subFolders': [
        {
            'treeId': 'string',
            'absolutePath': 'string',
            'relativePath': 'string'
        },
    ],
    'files': [
        {
            'blobId': 'string',
            'absolutePath': 'string',
            'relativePath': 'string',
            'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
        },
    ],
    'symbolicLinks': [
        {
            'blobId': 'string',
            'absolutePath': 'string',
            'relativePath': 'string',
            'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
        },
    ],
    'subModules': [
        {
            'commitId': 'string',
            'absolutePath': 'string',
            'relativePath': 'string'
        },
    ]
}


Response Structure

(dict) --

commitId (string) --
The full commit ID used as a reference for the returned version of the folder content.

folderPath (string) --
The fully qualified path of the folder whose contents are returned.

treeId (string) --
The full SHA-1 pointer of the tree information for the commit that contains the folder.

subFolders (list) --
The list of folders that exist under the specified folder, if any.

(dict) --
Returns information about a folder in a repository.

treeId (string) --
The full SHA-1 pointer of the tree information for the commit that contains the folder.

absolutePath (string) --
The fully qualified path of the folder in the repository.

relativePath (string) --
The relative path of the specified folder from the folder where the query originated.





files (list) --
The list of files in the specified folder, if any.

(dict) --
Returns information about a file in a repository.

blobId (string) --
The blob ID that contains the file information.

absolutePath (string) --
The fully qualified path to the file in the repository.

relativePath (string) --
The relative path of the file from the folder where the query originated.

fileMode (string) --
The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.





symbolicLinks (list) --
The list of symbolic links to other files and folders in the specified folder, if any.

(dict) --
Returns information about a symbolic link in a repository folder.

blobId (string) --
The blob ID that contains the information about the symbolic link.

absolutePath (string) --
The fully qualified path to the folder that contains the symbolic link.

relativePath (string) --
The relative path of the symbolic link from the folder where the query originated.

fileMode (string) --
The file mode permissions of the blob that cotains information about the symbolic link.





subModules (list) --
The list of submodules in the specified folder, if any.

(dict) --
Returns information about a submodule reference in a repository folder.

commitId (string) --
The commit ID that contains the reference to the submodule.

absolutePath (string) --
The fully qualified path to the folder that contains the reference to the submodule.

relativePath (string) --
The relative path of the submodule from the folder where the query originated.











Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.FolderDoesNotExistException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'commitId': 'string',
        'folderPath': 'string',
        'treeId': 'string',
        'subFolders': [
            {
                'treeId': 'string',
                'absolutePath': 'string',
                'relativePath': 'string'
            },
        ],
        'files': [
            {
                'blobId': 'string',
                'absolutePath': 'string',
                'relativePath': 'string',
                'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
            },
        ],
        'symbolicLinks': [
            {
                'blobId': 'string',
                'absolutePath': 'string',
                'relativePath': 'string',
                'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
            },
        ],
        'subModules': [
            {
                'commitId': 'string',
                'absolutePath': 'string',
                'relativePath': 'string'
            },
        ]
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidCommitException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.FolderDoesNotExistException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def get_merge_commit(repositoryName=None, sourceCommitSpecifier=None, destinationCommitSpecifier=None, conflictDetailLevel=None, conflictResolutionStrategy=None):
    """
    Returns information about a specified merge commit.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_merge_commit(
        repositoryName='string',
        sourceCommitSpecifier='string',
        destinationCommitSpecifier='string',
        conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
        conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that contains the merge commit about which you want to get information.\n

    :type sourceCommitSpecifier: string
    :param sourceCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type destinationCommitSpecifier: string
    :param destinationCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type conflictDetailLevel: string
    :param conflictDetailLevel: The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

    :type conflictResolutionStrategy: string
    :param conflictResolutionStrategy: Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

    :rtype: dict

ReturnsResponse Syntax
{
    'sourceCommitId': 'string',
    'destinationCommitId': 'string',
    'baseCommitId': 'string',
    'mergedCommitId': 'string'
}


Response Structure

(dict) --

sourceCommitId (string) --
The commit ID of the source commit specifier that was used in the merge evaluation.

destinationCommitId (string) --
The commit ID of the destination commit specifier that was used in the merge evaluation.

baseCommitId (string) --
The commit ID of the merge base.

mergedCommitId (string) --
The commit ID for the merge commit created when the source branch was merged into the destination branch. If the fast-forward merge strategy was used, there is no merge commit.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.CommitRequiredException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'sourceCommitId': 'string',
        'destinationCommitId': 'string',
        'baseCommitId': 'string',
        'mergedCommitId': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.CommitRequiredException
    CodeCommit.Client.exceptions.InvalidCommitException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
    CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def get_merge_conflicts(repositoryName=None, destinationCommitSpecifier=None, sourceCommitSpecifier=None, mergeOption=None, conflictDetailLevel=None, maxConflictFiles=None, conflictResolutionStrategy=None, nextToken=None):
    """
    Returns information about merge conflicts between the before and after commit IDs for a pull request in a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_merge_conflicts(
        repositoryName='string',
        destinationCommitSpecifier='string',
        sourceCommitSpecifier='string',
        mergeOption='FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
        conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
        maxConflictFiles=123,
        conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
        nextToken='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where the pull request was created.\n

    :type destinationCommitSpecifier: string
    :param destinationCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type sourceCommitSpecifier: string
    :param sourceCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type mergeOption: string
    :param mergeOption: [REQUIRED]\nThe merge option or strategy you want to use to merge the code.\n

    :type conflictDetailLevel: string
    :param conflictDetailLevel: The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

    :type maxConflictFiles: integer
    :param maxConflictFiles: The maximum number of files to include in the output.

    :type conflictResolutionStrategy: string
    :param conflictResolutionStrategy: Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

    :type nextToken: string
    :param nextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'mergeable': True|False,
    'destinationCommitId': 'string',
    'sourceCommitId': 'string',
    'baseCommitId': 'string',
    'conflictMetadataList': [
        {
            'filePath': 'string',
            'fileSizes': {
                'source': 123,
                'destination': 123,
                'base': 123
            },
            'fileModes': {
                'source': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                'destination': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                'base': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
            },
            'objectTypes': {
                'source': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                'destination': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                'base': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK'
            },
            'numberOfConflicts': 123,
            'isBinaryFile': {
                'source': True|False,
                'destination': True|False,
                'base': True|False
            },
            'contentConflict': True|False,
            'fileModeConflict': True|False,
            'objectTypeConflict': True|False,
            'mergeOperations': {
                'source': 'A'|'M'|'D',
                'destination': 'A'|'M'|'D'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

mergeable (boolean) --
A Boolean value that indicates whether the code is mergeable by the specified merge option.

destinationCommitId (string) --
The commit ID of the destination commit specifier that was used in the merge evaluation.

sourceCommitId (string) --
The commit ID of the source commit specifier that was used in the merge evaluation.

baseCommitId (string) --
The commit ID of the merge base.

conflictMetadataList (list) --
A list of metadata for any conflicting files. If the specified merge strategy is FAST_FORWARD_MERGE, this list is always empty.

(dict) --
Information about the metadata for a conflict in a merge operation.

filePath (string) --
The path of the file that contains conflicts.

fileSizes (dict) --
The file sizes of the file in the source, destination, and base of the merge.

source (integer) --
The size of a file in the source of a merge or pull request.

destination (integer) --
The size of a file in the destination of a merge or pull request.

base (integer) --
The size of a file in the base of a merge or pull request.



fileModes (dict) --
The file modes of the file in the source, destination, and base of the merge.

source (string) --
The file mode of a file in the source of a merge or pull request.

destination (string) --
The file mode of a file in the destination of a merge or pull request.

base (string) --
The file mode of a file in the base of a merge or pull request.



objectTypes (dict) --
Information about any object type conflicts in a merge operation.

source (string) --
The type of the object in the source branch.

destination (string) --
The type of the object in the destination branch.

base (string) --
The type of the object in the base commit of the merge.



numberOfConflicts (integer) --
The number of conflicts, including both hunk conflicts and metadata conflicts.

isBinaryFile (dict) --
A boolean value (true or false) indicating whether the file is binary or textual in the source, destination, and base of the merge.

source (boolean) --
The binary or non-binary status of file in the source of a merge or pull request.

destination (boolean) --
The binary or non-binary status of a file in the destination of a merge or pull request.

base (boolean) --
The binary or non-binary status of a file in the base of a merge or pull request.



contentConflict (boolean) --
A boolean value indicating whether there are conflicts in the content of a file.

fileModeConflict (boolean) --
A boolean value indicating whether there are conflicts in the file mode of a file.

objectTypeConflict (boolean) --
A boolean value (true or false) indicating whether there are conflicts between the branches in the object type of a file, folder, or submodule.

mergeOperations (dict) --
Whether an add, modify, or delete operation caused the conflict between the source and destination of the merge.

source (string) --
The operation (add, modify, or delete) on a file in the source of a merge or pull request.

destination (string) --
The operation on a file in the destination of a merge or pull request.







nextToken (string) --
An enumeration token that can be used in a request to return the next batch of the results.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.MergeOptionRequiredException
CodeCommit.Client.exceptions.InvalidMergeOptionException
CodeCommit.Client.exceptions.InvalidContinuationTokenException
CodeCommit.Client.exceptions.CommitRequiredException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.TipsDivergenceExceededException
CodeCommit.Client.exceptions.InvalidMaxConflictFilesException
CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
CodeCommit.Client.exceptions.InvalidDestinationCommitSpecifierException
CodeCommit.Client.exceptions.InvalidSourceCommitSpecifierException
CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'mergeable': True|False,
        'destinationCommitId': 'string',
        'sourceCommitId': 'string',
        'baseCommitId': 'string',
        'conflictMetadataList': [
            {
                'filePath': 'string',
                'fileSizes': {
                    'source': 123,
                    'destination': 123,
                    'base': 123
                },
                'fileModes': {
                    'source': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                    'destination': 'EXECUTABLE'|'NORMAL'|'SYMLINK',
                    'base': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
                'objectTypes': {
                    'source': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                    'destination': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK',
                    'base': 'FILE'|'DIRECTORY'|'GIT_LINK'|'SYMBOLIC_LINK'
                },
                'numberOfConflicts': 123,
                'isBinaryFile': {
                    'source': True|False,
                    'destination': True|False,
                    'base': True|False
                },
                'contentConflict': True|False,
                'fileModeConflict': True|False,
                'objectTypeConflict': True|False,
                'mergeOperations': {
                    'source': 'A'|'M'|'D',
                    'destination': 'A'|'M'|'D'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.MergeOptionRequiredException
    CodeCommit.Client.exceptions.InvalidMergeOptionException
    CodeCommit.Client.exceptions.InvalidContinuationTokenException
    CodeCommit.Client.exceptions.CommitRequiredException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidCommitException
    CodeCommit.Client.exceptions.TipsDivergenceExceededException
    CodeCommit.Client.exceptions.InvalidMaxConflictFilesException
    CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
    CodeCommit.Client.exceptions.InvalidDestinationCommitSpecifierException
    CodeCommit.Client.exceptions.InvalidSourceCommitSpecifierException
    CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
    CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
    CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def get_merge_options(repositoryName=None, sourceCommitSpecifier=None, destinationCommitSpecifier=None, conflictDetailLevel=None, conflictResolutionStrategy=None):
    """
    Returns information about the merge options available for merging two specified branches. For details about why a merge option is not available, use GetMergeConflicts or DescribeMergeConflicts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_merge_options(
        repositoryName='string',
        sourceCommitSpecifier='string',
        destinationCommitSpecifier='string',
        conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
        conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that contains the commits about which you want to get merge options.\n

    :type sourceCommitSpecifier: string
    :param sourceCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type destinationCommitSpecifier: string
    :param destinationCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type conflictDetailLevel: string
    :param conflictDetailLevel: The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

    :type conflictResolutionStrategy: string
    :param conflictResolutionStrategy: Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

    :rtype: dict

ReturnsResponse Syntax
{
    'mergeOptions': [
        'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
    ],
    'sourceCommitId': 'string',
    'destinationCommitId': 'string',
    'baseCommitId': 'string'
}


Response Structure

(dict) --

mergeOptions (list) --
The merge option or strategy used to merge the code.

(string) --


sourceCommitId (string) --
The commit ID of the source commit specifier that was used in the merge evaluation.

destinationCommitId (string) --
The commit ID of the destination commit specifier that was used in the merge evaluation.

baseCommitId (string) --
The commit ID of the merge base.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.CommitRequiredException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.TipsDivergenceExceededException
CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'mergeOptions': [
            'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE',
        ],
        'sourceCommitId': 'string',
        'destinationCommitId': 'string',
        'baseCommitId': 'string'
    }
    
    
    :returns: 
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

def get_pull_request(pullRequestId=None):
    """
    Gets information about a pull request in a specified repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_pull_request(
        pullRequestId='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request. To get this ID, use ListPullRequests .\n

    :rtype: dict
ReturnsResponse Syntax{
    'pullRequest': {
        'pullRequestId': 'string',
        'title': 'string',
        'description': 'string',
        'lastActivityDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'pullRequestStatus': 'OPEN'|'CLOSED',
        'authorArn': 'string',
        'pullRequestTargets': [
            {
                'repositoryName': 'string',
                'sourceReference': 'string',
                'destinationReference': 'string',
                'destinationCommit': 'string',
                'sourceCommit': 'string',
                'mergeBase': 'string',
                'mergeMetadata': {
                    'isMerged': True|False,
                    'mergedBy': 'string',
                    'mergeCommitId': 'string',
                    'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                }
            },
        ],
        'clientRequestToken': 'string',
        'revisionId': 'string',
        'approvalRules': [
            {
                'approvalRuleId': 'string',
                'approvalRuleName': 'string',
                'approvalRuleContent': 'string',
                'ruleContentSha256': 'string',
                'lastModifiedDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedUser': 'string',
                'originApprovalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --
pullRequest (dict) --Information about the specified pull request.

pullRequestId (string) --The system-generated ID of the pull request.

title (string) --The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.

description (string) --The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.

lastActivityDate (datetime) --The day and time of the last user or system activity on the pull request, in timestamp format.

creationDate (datetime) --The date and time the pull request was originally created, in timestamp format.

pullRequestStatus (string) --The status of the pull request. Pull request status can only change from OPEN to CLOSED .

authorArn (string) --The Amazon Resource Name (ARN) of the user who created the pull request.

pullRequestTargets (list) --The targets of the pull request, including the source branch and destination branch for the pull request.

(dict) --Returns information about a pull request target.

repositoryName (string) --The name of the repository that contains the pull request source and destination branches.

sourceReference (string) --The branch of the repository that contains the changes for the pull request. Also known as the source branch.

destinationReference (string) --The branch of the repository where the pull request changes are merged. Also known as the destination branch.

destinationCommit (string) --The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.

sourceCommit (string) --The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.

mergeBase (string) --The commit ID of the most recent commit that the source branch and the destination branch have in common.

mergeMetadata (dict) --Returns metadata about the state of the merge, including whether the merge has been made.

isMerged (boolean) --A Boolean value indicating whether the merge has been made.

mergedBy (string) --The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId (string) --The commit ID for the merge commit, if any.

mergeOption (string) --The merge strategy used in the merge.







clientRequestToken (string) --A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

revisionId (string) --The system-generated revision ID for the pull request.

approvalRules (list) --The approval rules applied to the pull request.

(dict) --Returns information about an approval rule.

approvalRuleId (string) --The system-generated ID of the approval rule.

approvalRuleName (string) --The name of the approval rule.

approvalRuleContent (string) --The content of the approval rule.

ruleContentSha256 (string) --The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate (datetime) --The date the approval rule was most recently changed, in timestamp format.

creationDate (datetime) --The date the approval rule was created, in timestamp format.

lastModifiedUser (string) --The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate (dict) --The approval rule template used to create the rule.

approvalRuleTemplateId (string) --The ID of the template that created the approval rule.

approvalRuleTemplateName (string) --The name of the template that created the approval rule.














Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeBase': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string',
                        'mergeCommitId': 'string',
                        'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                    }
                },
            ],
            'clientRequestToken': 'string',
            'revisionId': 'string',
            'approvalRules': [
                {
                    'approvalRuleId': 'string',
                    'approvalRuleName': 'string',
                    'approvalRuleContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string',
                    'originApprovalRuleTemplate': {
                        'approvalRuleTemplateId': 'string',
                        'approvalRuleTemplateName': 'string'
                    }
                },
            ]
        }
    }
    
    
    """
    pass

def get_pull_request_approval_states(pullRequestId=None, revisionId=None):
    """
    Gets information about the approval states for a specified pull request. Approval states only apply to pull requests that have one or more approval rules applied to them.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_pull_request_approval_states(
        pullRequestId='string',
        revisionId='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID for the pull request.\n

    :type revisionId: string
    :param revisionId: [REQUIRED]\nThe system-generated ID for the pull request revision.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'approvals': [
        {
            'userArn': 'string',
            'approvalState': 'APPROVE'|'REVOKE'
        },
    ]
}


Response Structure

(dict) --

approvals (list) --
Information about users who have approved the pull request.

(dict) --
Returns information about a specific approval on a pull request.

userArn (string) --
The Amazon Resource Name (ARN) of the user.

approvalState (string) --
The state of the approval, APPROVE or REVOKE. REVOKE states are not stored.











Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.InvalidRevisionIdException
CodeCommit.Client.exceptions.RevisionIdRequiredException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'approvals': [
            {
                'userArn': 'string',
                'approvalState': 'APPROVE'|'REVOKE'
            },
        ]
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.InvalidRevisionIdException
    CodeCommit.Client.exceptions.RevisionIdRequiredException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def get_pull_request_override_state(pullRequestId=None, revisionId=None):
    """
    Returns information about whether approval rules have been set aside (overridden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_pull_request_override_state(
        pullRequestId='string',
        revisionId='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe ID of the pull request for which you want to get information about whether approval rules have been set aside (overridden).\n

    :type revisionId: string
    :param revisionId: [REQUIRED]\nThe system-generated ID of the revision for the pull request. To retrieve the most recent revision ID, use GetPullRequest .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'overridden': True|False,
    'overrider': 'string'
}


Response Structure

(dict) --

overridden (boolean) --
A Boolean value that indicates whether a pull request has had its rules set aside (TRUE) or whether all approval rules still apply (FALSE).

overrider (string) --
The Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.







Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.InvalidRevisionIdException
CodeCommit.Client.exceptions.RevisionIdRequiredException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'overridden': True|False,
        'overrider': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.InvalidRevisionIdException
    CodeCommit.Client.exceptions.RevisionIdRequiredException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def get_repository(repositoryName=None):
    """
    Returns information about a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_repository(
        repositoryName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to get information about.\n

    :rtype: dict
ReturnsResponse Syntax{
    'repositoryMetadata': {
        'accountId': 'string',
        'repositoryId': 'string',
        'repositoryName': 'string',
        'repositoryDescription': 'string',
        'defaultBranch': 'string',
        'lastModifiedDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'cloneUrlHttp': 'string',
        'cloneUrlSsh': 'string',
        'Arn': 'string'
    }
}


Response Structure

(dict) --Represents the output of a get repository operation.

repositoryMetadata (dict) --Information about the repository.

accountId (string) --The ID of the AWS account associated with the repository.

repositoryId (string) --The ID of the repository.

repositoryName (string) --The repository\'s name.

repositoryDescription (string) --A comment or description about the repository.

defaultBranch (string) --The repository\'s default branch name.

lastModifiedDate (datetime) --The date and time the repository was last modified, in timestamp format.

creationDate (datetime) --The date and time the repository was created, in timestamp format.

cloneUrlHttp (string) --The URL to use for cloning the repository over HTTPS.

cloneUrlSsh (string) --The URL to use for cloning the repository over SSH.

Arn (string) --The Amazon Resource Name (ARN) of the repository.








Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'repositoryMetadata': {
            'accountId': 'string',
            'repositoryId': 'string',
            'repositoryName': 'string',
            'repositoryDescription': 'string',
            'defaultBranch': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'cloneUrlHttp': 'string',
            'cloneUrlSsh': 'string',
            'Arn': 'string'
        }
    }
    
    
    """
    pass

def get_repository_triggers(repositoryName=None):
    """
    Gets information about triggers configured for a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_repository_triggers(
        repositoryName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository for which the trigger is configured.\n

    :rtype: dict
ReturnsResponse Syntax{
    'configurationId': 'string',
    'triggers': [
        {
            'name': 'string',
            'destinationArn': 'string',
            'customData': 'string',
            'branches': [
                'string',
            ],
            'events': [
                'all'|'updateReference'|'createReference'|'deleteReference',
            ]
        },
    ]
}


Response Structure

(dict) --Represents the output of a get repository triggers operation.

configurationId (string) --The system-generated unique ID for the trigger.

triggers (list) --The JSON block of configuration information for each trigger.

(dict) --Information about a trigger for a repository.

name (string) --The name of the trigger.

destinationArn (string) --The ARN of the resource that is the target for a trigger (for example, the ARN of a topic in Amazon SNS).

customData (string) --Any custom data associated with the trigger to be included in the information sent to the target of the trigger.

branches (list) --The branches to be included in the trigger configuration. If you specify an empty array, the trigger applies to all branches.

Note
Although no content is required in the array, you must include the array itself.


(string) --


events (list) --The repository events that cause the trigger to run actions in another service, such as sending a notification through Amazon SNS.

Note
The valid value "all" cannot be used with any other values.


(string) --











Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'configurationId': 'string',
        'triggers': [
            {
                'name': 'string',
                'destinationArn': 'string',
                'customData': 'string',
                'branches': [
                    'string',
                ],
                'events': [
                    'all'|'updateReference'|'createReference'|'deleteReference',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
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

def list_approval_rule_templates(nextToken=None, maxResults=None):
    """
    Lists all approval rule templates in the specified AWS Region in your AWS account. If an AWS Region is not specified, the AWS Region where you are signed in is used.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_approval_rule_templates(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-zero, non-negative integer used to limit the number of returned results.

    :rtype: dict

ReturnsResponse Syntax
{
    'approvalRuleTemplateNames': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

approvalRuleTemplateNames (list) --
The names of all the approval rule templates found in the AWS Region for your AWS account.

(string) --


nextToken (string) --
An enumeration token that allows the operation to batch the next results of the operation.







Exceptions

CodeCommit.Client.exceptions.InvalidMaxResultsException
CodeCommit.Client.exceptions.InvalidContinuationTokenException


    :return: {
        'approvalRuleTemplateNames': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_associated_approval_rule_templates_for_repository(repositoryName=None, nextToken=None, maxResults=None):
    """
    Lists all approval rule templates that are associated with a specified repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_associated_approval_rule_templates_for_repository(
        repositoryName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository for which you want to list all associated approval rule templates.\n

    :type nextToken: string
    :param nextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-zero, non-negative integer used to limit the number of returned results.

    :rtype: dict

ReturnsResponse Syntax
{
    'approvalRuleTemplateNames': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

approvalRuleTemplateNames (list) --
The names of all approval rule templates associated with the repository.

(string) --


nextToken (string) --
An enumeration token that allows the operation to batch the next results of the operation.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidMaxResultsException
CodeCommit.Client.exceptions.InvalidContinuationTokenException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'approvalRuleTemplateNames': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_branches(repositoryName=None, nextToken=None):
    """
    Gets information about one or more branches in a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_branches(
        repositoryName='string',
        nextToken='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository that contains the branches.\n

    :type nextToken: string
    :param nextToken: An enumeration token that allows the operation to batch the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'branches': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the output of a list branches operation.

branches (list) --
The list of branch names.

(string) --


nextToken (string) --
An enumeration token that returns the batch of the results.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
CodeCommit.Client.exceptions.InvalidContinuationTokenException


    :return: {
        'branches': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_pull_requests(repositoryName=None, authorArn=None, pullRequestStatus=None, nextToken=None, maxResults=None):
    """
    Returns a list of pull requests for a specified repository. The return list can be refined by pull request status or pull request author ARN.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_pull_requests(
        repositoryName='string',
        authorArn='string',
        pullRequestStatus='OPEN'|'CLOSED',
        nextToken='string',
        maxResults=123
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository for which you want to list pull requests.\n

    :type authorArn: string
    :param authorArn: Optional. The Amazon Resource Name (ARN) of the user who created the pull request. If used, this filters the results to pull requests created by that user.

    :type pullRequestStatus: string
    :param pullRequestStatus: Optional. The status of the pull request. If used, this refines the results to the pull requests that match the specified status.

    :type nextToken: string
    :param nextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-zero, non-negative integer used to limit the number of returned results.

    :rtype: dict

ReturnsResponse Syntax
{
    'pullRequestIds': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

pullRequestIds (list) --
The system-generated IDs of the pull requests.

(string) --


nextToken (string) --
An enumeration token that allows the operation to batch the next results of the operation.







Exceptions

CodeCommit.Client.exceptions.InvalidPullRequestStatusException
CodeCommit.Client.exceptions.InvalidAuthorArnException
CodeCommit.Client.exceptions.AuthorDoesNotExistException
CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidMaxResultsException
CodeCommit.Client.exceptions.InvalidContinuationTokenException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'pullRequestIds': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_repositories(nextToken=None, sortBy=None, order=None):
    """
    Gets information about one or more repositories.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_repositories(
        nextToken='string',
        sortBy='repositoryName'|'lastModifiedDate',
        order='ascending'|'descending'
    )
    
    
    :type nextToken: string
    :param nextToken: An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to AWS CodeCommit, another page of 1,000 records is retrieved.

    :type sortBy: string
    :param sortBy: The criteria used to sort the results of a list repositories operation.

    :type order: string
    :param order: The order in which to sort the results of a list repositories operation.

    :rtype: dict

ReturnsResponse Syntax
{
    'repositories': [
        {
            'repositoryName': 'string',
            'repositoryId': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
Represents the output of a list repositories operation.

repositories (list) --
Lists the repositories called by the list repositories operation.

(dict) --
Information about a repository name and ID.

repositoryName (string) --
The name associated with the repository.

repositoryId (string) --
The ID associated with the repository.





nextToken (string) --
An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to AWS CodeCommit, another page of 1,000 records is retrieved.







Exceptions

CodeCommit.Client.exceptions.InvalidSortByException
CodeCommit.Client.exceptions.InvalidOrderException
CodeCommit.Client.exceptions.InvalidContinuationTokenException


    :return: {
        'repositories': [
            {
                'repositoryName': 'string',
                'repositoryId': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.InvalidSortByException
    CodeCommit.Client.exceptions.InvalidOrderException
    CodeCommit.Client.exceptions.InvalidContinuationTokenException
    
    """
    pass

def list_repositories_for_approval_rule_template(approvalRuleTemplateName=None, nextToken=None, maxResults=None):
    """
    Lists all repositories associated with the specified approval rule template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_repositories_for_approval_rule_template(
        approvalRuleTemplateName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type approvalRuleTemplateName: string
    :param approvalRuleTemplateName: [REQUIRED]\nThe name of the approval rule template for which you want to list repositories that are associated with that template.\n

    :type nextToken: string
    :param nextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :type maxResults: integer
    :param maxResults: A non-zero, non-negative integer used to limit the number of returned results.

    :rtype: dict

ReturnsResponse Syntax
{
    'repositoryNames': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

repositoryNames (list) --
A list of repository names that are associated with the specified approval rule template.

(string) --


nextToken (string) --
An enumeration token that allows the operation to batch the next results of the operation.







Exceptions

CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
CodeCommit.Client.exceptions.InvalidMaxResultsException
CodeCommit.Client.exceptions.InvalidContinuationTokenException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'repositoryNames': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(resourceArn=None, nextToken=None):
    """
    Gets information about AWS tags for a specified Amazon Resource Name (ARN) in AWS CodeCommit. For a list of valid resources in AWS CodeCommit, see CodeCommit Resources and Operations in the*AWS CodeCommit User Guide* .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string',
        nextToken='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource for which you want to get information about tags, if any.\n

    :type nextToken: string
    :param nextToken: An enumeration token that, when provided in a request, returns the next batch of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'tags': {
        'string': 'string'
    },
    'nextToken': 'string'
}


Response Structure

(dict) --

tags (dict) --
A list of tag key and value pairs associated with the specified resource.

(string) --
(string) --




nextToken (string) --
An enumeration token that allows the operation to batch the next results of the operation.







Exceptions

CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.ResourceArnRequiredException
CodeCommit.Client.exceptions.InvalidResourceArnException


    :return: {
        'tags': {
            'string': 'string'
        },
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def merge_branches_by_fast_forward(repositoryName=None, sourceCommitSpecifier=None, destinationCommitSpecifier=None, targetBranch=None):
    """
    Merges two branches using the fast-forward merge strategy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.merge_branches_by_fast_forward(
        repositoryName='string',
        sourceCommitSpecifier='string',
        destinationCommitSpecifier='string',
        targetBranch='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to merge two branches.\n

    :type sourceCommitSpecifier: string
    :param sourceCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type destinationCommitSpecifier: string
    :param destinationCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type targetBranch: string
    :param targetBranch: The branch where the merge is applied.

    :rtype: dict

ReturnsResponse Syntax
{
    'commitId': 'string',
    'treeId': 'string'
}


Response Structure

(dict) --

commitId (string) --
The commit ID of the merge in the destination or target branch.

treeId (string) --
The tree ID of the merge in the destination or target branch.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.TipsDivergenceExceededException
CodeCommit.Client.exceptions.CommitRequiredException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidTargetBranchException
CodeCommit.Client.exceptions.InvalidBranchNameException
CodeCommit.Client.exceptions.BranchNameRequiredException
CodeCommit.Client.exceptions.BranchNameIsTagNameException
CodeCommit.Client.exceptions.BranchDoesNotExistException
CodeCommit.Client.exceptions.ManualMergeRequiredException
CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'commitId': 'string',
        'treeId': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.TipsDivergenceExceededException
    CodeCommit.Client.exceptions.CommitRequiredException
    CodeCommit.Client.exceptions.InvalidCommitException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidTargetBranchException
    CodeCommit.Client.exceptions.InvalidBranchNameException
    CodeCommit.Client.exceptions.BranchNameRequiredException
    CodeCommit.Client.exceptions.BranchNameIsTagNameException
    CodeCommit.Client.exceptions.BranchDoesNotExistException
    CodeCommit.Client.exceptions.ManualMergeRequiredException
    CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def merge_branches_by_squash(repositoryName=None, sourceCommitSpecifier=None, destinationCommitSpecifier=None, targetBranch=None, conflictDetailLevel=None, conflictResolutionStrategy=None, authorName=None, email=None, commitMessage=None, keepEmptyFolders=None, conflictResolution=None):
    """
    Merges two branches using the squash merge strategy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.merge_branches_by_squash(
        repositoryName='string',
        sourceCommitSpecifier='string',
        destinationCommitSpecifier='string',
        targetBranch='string',
        conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
        conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
        authorName='string',
        email='string',
        commitMessage='string',
        keepEmptyFolders=True|False,
        conflictResolution={
            'replaceContents': [
                {
                    'filePath': 'string',
                    'replacementType': 'KEEP_BASE'|'KEEP_SOURCE'|'KEEP_DESTINATION'|'USE_NEW_CONTENT',
                    'content': b'bytes',
                    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
            ],
            'deleteFiles': [
                {
                    'filePath': 'string'
                },
            ],
            'setFileModes': [
                {
                    'filePath': 'string',
                    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
            ]
        }
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to merge two branches.\n

    :type sourceCommitSpecifier: string
    :param sourceCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type destinationCommitSpecifier: string
    :param destinationCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type targetBranch: string
    :param targetBranch: The branch where the merge is applied.

    :type conflictDetailLevel: string
    :param conflictDetailLevel: The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

    :type conflictResolutionStrategy: string
    :param conflictResolutionStrategy: Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

    :type authorName: string
    :param authorName: The name of the author who created the commit. This information is used as both the author and committer for the commit.

    :type email: string
    :param email: The email address of the person merging the branches. This information is used in the commit information for the merge.

    :type commitMessage: string
    :param commitMessage: The commit message for the merge.

    :type keepEmptyFolders: boolean
    :param keepEmptyFolders: If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If this is specified as true, a .gitkeep file is created for empty folders. The default is false.

    :type conflictResolution: dict
    :param conflictResolution: If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.\n\nreplaceContents (list) --Files to have content replaced as part of the merge conflict resolution.\n\n(dict) --Information about a replacement content entry in the conflict of a merge or pull request operation.\n\nfilePath (string) -- [REQUIRED]The path of the conflicting file.\n\nreplacementType (string) -- [REQUIRED]The replacement type to use when determining how to resolve the conflict.\n\ncontent (bytes) --The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.\n\nfileMode (string) --The file mode to apply during conflict resoltion.\n\n\n\n\n\ndeleteFiles (list) --Files to be deleted as part of the merge conflict resolution.\n\n(dict) --A file that is deleted as part of a commit.\n\nfilePath (string) -- [REQUIRED]The full path of the file to be deleted, including the name of the file.\n\n\n\n\n\nsetFileModes (list) --File modes that are set as part of the merge conflict resolution.\n\n(dict) --Information about the file mode changes.\n\nfilePath (string) -- [REQUIRED]The full path to the file, including the name of the file.\n\nfileMode (string) -- [REQUIRED]The file mode for the file.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'commitId': 'string',
    'treeId': 'string'
}


Response Structure

(dict) --

commitId (string) --
The commit ID of the merge in the destination or target branch.

treeId (string) --
The tree ID of the merge in the destination or target branch.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.TipsDivergenceExceededException
CodeCommit.Client.exceptions.CommitRequiredException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidTargetBranchException
CodeCommit.Client.exceptions.InvalidBranchNameException
CodeCommit.Client.exceptions.BranchNameRequiredException
CodeCommit.Client.exceptions.BranchNameIsTagNameException
CodeCommit.Client.exceptions.BranchDoesNotExistException
CodeCommit.Client.exceptions.ManualMergeRequiredException
CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
CodeCommit.Client.exceptions.InvalidConflictResolutionException
CodeCommit.Client.exceptions.MaximumConflictResolutionEntriesExceededException
CodeCommit.Client.exceptions.MultipleConflictResolutionEntriesException
CodeCommit.Client.exceptions.ReplacementTypeRequiredException
CodeCommit.Client.exceptions.InvalidReplacementTypeException
CodeCommit.Client.exceptions.ReplacementContentRequiredException
CodeCommit.Client.exceptions.InvalidReplacementContentException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
CodeCommit.Client.exceptions.FileModeRequiredException
CodeCommit.Client.exceptions.InvalidFileModeException
CodeCommit.Client.exceptions.NameLengthExceededException
CodeCommit.Client.exceptions.InvalidEmailException
CodeCommit.Client.exceptions.CommitMessageLengthExceededException
CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'commitId': 'string',
        'treeId': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.TipsDivergenceExceededException
    CodeCommit.Client.exceptions.CommitRequiredException
    CodeCommit.Client.exceptions.InvalidCommitException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidTargetBranchException
    CodeCommit.Client.exceptions.InvalidBranchNameException
    CodeCommit.Client.exceptions.BranchNameRequiredException
    CodeCommit.Client.exceptions.BranchNameIsTagNameException
    CodeCommit.Client.exceptions.BranchDoesNotExistException
    CodeCommit.Client.exceptions.ManualMergeRequiredException
    CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
    CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
    CodeCommit.Client.exceptions.InvalidConflictResolutionException
    CodeCommit.Client.exceptions.MaximumConflictResolutionEntriesExceededException
    CodeCommit.Client.exceptions.MultipleConflictResolutionEntriesException
    CodeCommit.Client.exceptions.ReplacementTypeRequiredException
    CodeCommit.Client.exceptions.InvalidReplacementTypeException
    CodeCommit.Client.exceptions.ReplacementContentRequiredException
    CodeCommit.Client.exceptions.InvalidReplacementContentException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
    CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
    CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
    CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
    CodeCommit.Client.exceptions.FileModeRequiredException
    CodeCommit.Client.exceptions.InvalidFileModeException
    CodeCommit.Client.exceptions.NameLengthExceededException
    CodeCommit.Client.exceptions.InvalidEmailException
    CodeCommit.Client.exceptions.CommitMessageLengthExceededException
    CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def merge_branches_by_three_way(repositoryName=None, sourceCommitSpecifier=None, destinationCommitSpecifier=None, targetBranch=None, conflictDetailLevel=None, conflictResolutionStrategy=None, authorName=None, email=None, commitMessage=None, keepEmptyFolders=None, conflictResolution=None):
    """
    Merges two specified branches using the three-way merge strategy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.merge_branches_by_three_way(
        repositoryName='string',
        sourceCommitSpecifier='string',
        destinationCommitSpecifier='string',
        targetBranch='string',
        conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
        conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
        authorName='string',
        email='string',
        commitMessage='string',
        keepEmptyFolders=True|False,
        conflictResolution={
            'replaceContents': [
                {
                    'filePath': 'string',
                    'replacementType': 'KEEP_BASE'|'KEEP_SOURCE'|'KEEP_DESTINATION'|'USE_NEW_CONTENT',
                    'content': b'bytes',
                    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
            ],
            'deleteFiles': [
                {
                    'filePath': 'string'
                },
            ],
            'setFileModes': [
                {
                    'filePath': 'string',
                    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
            ]
        }
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to merge two branches.\n

    :type sourceCommitSpecifier: string
    :param sourceCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type destinationCommitSpecifier: string
    :param destinationCommitSpecifier: [REQUIRED]\nThe branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).\n

    :type targetBranch: string
    :param targetBranch: The branch where the merge is applied.

    :type conflictDetailLevel: string
    :param conflictDetailLevel: The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

    :type conflictResolutionStrategy: string
    :param conflictResolutionStrategy: Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

    :type authorName: string
    :param authorName: The name of the author who created the commit. This information is used as both the author and committer for the commit.

    :type email: string
    :param email: The email address of the person merging the branches. This information is used in the commit information for the merge.

    :type commitMessage: string
    :param commitMessage: The commit message to include in the commit information for the merge.

    :type keepEmptyFolders: boolean
    :param keepEmptyFolders: If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a .gitkeep file is created for empty folders. The default is false.

    :type conflictResolution: dict
    :param conflictResolution: If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.\n\nreplaceContents (list) --Files to have content replaced as part of the merge conflict resolution.\n\n(dict) --Information about a replacement content entry in the conflict of a merge or pull request operation.\n\nfilePath (string) -- [REQUIRED]The path of the conflicting file.\n\nreplacementType (string) -- [REQUIRED]The replacement type to use when determining how to resolve the conflict.\n\ncontent (bytes) --The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.\n\nfileMode (string) --The file mode to apply during conflict resoltion.\n\n\n\n\n\ndeleteFiles (list) --Files to be deleted as part of the merge conflict resolution.\n\n(dict) --A file that is deleted as part of a commit.\n\nfilePath (string) -- [REQUIRED]The full path of the file to be deleted, including the name of the file.\n\n\n\n\n\nsetFileModes (list) --File modes that are set as part of the merge conflict resolution.\n\n(dict) --Information about the file mode changes.\n\nfilePath (string) -- [REQUIRED]The full path to the file, including the name of the file.\n\nfileMode (string) -- [REQUIRED]The file mode for the file.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'commitId': 'string',
    'treeId': 'string'
}


Response Structure

(dict) --

commitId (string) --
The commit ID of the merge in the destination or target branch.

treeId (string) --
The tree ID of the merge in the destination or target branch.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.TipsDivergenceExceededException
CodeCommit.Client.exceptions.CommitRequiredException
CodeCommit.Client.exceptions.InvalidCommitException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidTargetBranchException
CodeCommit.Client.exceptions.InvalidBranchNameException
CodeCommit.Client.exceptions.BranchNameRequiredException
CodeCommit.Client.exceptions.BranchNameIsTagNameException
CodeCommit.Client.exceptions.BranchDoesNotExistException
CodeCommit.Client.exceptions.ManualMergeRequiredException
CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
CodeCommit.Client.exceptions.InvalidConflictResolutionException
CodeCommit.Client.exceptions.MaximumConflictResolutionEntriesExceededException
CodeCommit.Client.exceptions.MultipleConflictResolutionEntriesException
CodeCommit.Client.exceptions.ReplacementTypeRequiredException
CodeCommit.Client.exceptions.InvalidReplacementTypeException
CodeCommit.Client.exceptions.ReplacementContentRequiredException
CodeCommit.Client.exceptions.InvalidReplacementContentException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
CodeCommit.Client.exceptions.FileModeRequiredException
CodeCommit.Client.exceptions.InvalidFileModeException
CodeCommit.Client.exceptions.NameLengthExceededException
CodeCommit.Client.exceptions.InvalidEmailException
CodeCommit.Client.exceptions.CommitMessageLengthExceededException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'commitId': 'string',
        'treeId': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.TipsDivergenceExceededException
    CodeCommit.Client.exceptions.CommitRequiredException
    CodeCommit.Client.exceptions.InvalidCommitException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidTargetBranchException
    CodeCommit.Client.exceptions.InvalidBranchNameException
    CodeCommit.Client.exceptions.BranchNameRequiredException
    CodeCommit.Client.exceptions.BranchNameIsTagNameException
    CodeCommit.Client.exceptions.BranchDoesNotExistException
    CodeCommit.Client.exceptions.ManualMergeRequiredException
    CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
    CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
    CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
    CodeCommit.Client.exceptions.InvalidConflictResolutionException
    CodeCommit.Client.exceptions.MaximumConflictResolutionEntriesExceededException
    CodeCommit.Client.exceptions.MultipleConflictResolutionEntriesException
    CodeCommit.Client.exceptions.ReplacementTypeRequiredException
    CodeCommit.Client.exceptions.InvalidReplacementTypeException
    CodeCommit.Client.exceptions.ReplacementContentRequiredException
    CodeCommit.Client.exceptions.InvalidReplacementContentException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
    CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
    CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
    CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
    CodeCommit.Client.exceptions.FileModeRequiredException
    CodeCommit.Client.exceptions.InvalidFileModeException
    CodeCommit.Client.exceptions.NameLengthExceededException
    CodeCommit.Client.exceptions.InvalidEmailException
    CodeCommit.Client.exceptions.CommitMessageLengthExceededException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def merge_pull_request_by_fast_forward(pullRequestId=None, repositoryName=None, sourceCommitId=None):
    """
    Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the fast-forward merge strategy. If the merge is successful, it closes the pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.merge_pull_request_by_fast_forward(
        pullRequestId='string',
        repositoryName='string',
        sourceCommitId='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request. To get this ID, use ListPullRequests .\n

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where the pull request was created.\n

    :type sourceCommitId: string
    :param sourceCommitId: The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.

    :rtype: dict

ReturnsResponse Syntax
{
    'pullRequest': {
        'pullRequestId': 'string',
        'title': 'string',
        'description': 'string',
        'lastActivityDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'pullRequestStatus': 'OPEN'|'CLOSED',
        'authorArn': 'string',
        'pullRequestTargets': [
            {
                'repositoryName': 'string',
                'sourceReference': 'string',
                'destinationReference': 'string',
                'destinationCommit': 'string',
                'sourceCommit': 'string',
                'mergeBase': 'string',
                'mergeMetadata': {
                    'isMerged': True|False,
                    'mergedBy': 'string',
                    'mergeCommitId': 'string',
                    'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                }
            },
        ],
        'clientRequestToken': 'string',
        'revisionId': 'string',
        'approvalRules': [
            {
                'approvalRuleId': 'string',
                'approvalRuleName': 'string',
                'approvalRuleContent': 'string',
                'ruleContentSha256': 'string',
                'lastModifiedDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedUser': 'string',
                'originApprovalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --

pullRequest (dict) --
Information about the specified pull request, including the merge.

pullRequestId (string) --
The system-generated ID of the pull request.

title (string) --
The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.

description (string) --
The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.

lastActivityDate (datetime) --
The day and time of the last user or system activity on the pull request, in timestamp format.

creationDate (datetime) --
The date and time the pull request was originally created, in timestamp format.

pullRequestStatus (string) --
The status of the pull request. Pull request status can only change from OPEN to CLOSED .

authorArn (string) --
The Amazon Resource Name (ARN) of the user who created the pull request.

pullRequestTargets (list) --
The targets of the pull request, including the source branch and destination branch for the pull request.

(dict) --
Returns information about a pull request target.

repositoryName (string) --
The name of the repository that contains the pull request source and destination branches.

sourceReference (string) --
The branch of the repository that contains the changes for the pull request. Also known as the source branch.

destinationReference (string) --
The branch of the repository where the pull request changes are merged. Also known as the destination branch.

destinationCommit (string) --
The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.

sourceCommit (string) --
The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.

mergeBase (string) --
The commit ID of the most recent commit that the source branch and the destination branch have in common.

mergeMetadata (dict) --
Returns metadata about the state of the merge, including whether the merge has been made.

isMerged (boolean) --
A Boolean value indicating whether the merge has been made.

mergedBy (string) --
The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId (string) --
The commit ID for the merge commit, if any.

mergeOption (string) --
The merge strategy used in the merge.







clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

revisionId (string) --
The system-generated revision ID for the pull request.

approvalRules (list) --
The approval rules applied to the pull request.

(dict) --
Returns information about an approval rule.

approvalRuleId (string) --
The system-generated ID of the approval rule.

approvalRuleName (string) --
The name of the approval rule.

approvalRuleContent (string) --
The content of the approval rule.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate (datetime) --
The date the approval rule was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate (dict) --
The approval rule template used to create the rule.

approvalRuleTemplateId (string) --
The ID of the template that created the approval rule.

approvalRuleTemplateName (string) --
The name of the template that created the approval rule.















Exceptions

CodeCommit.Client.exceptions.ManualMergeRequiredException
CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.TipOfSourceReferenceIsDifferentException
CodeCommit.Client.exceptions.ReferenceDoesNotExistException
CodeCommit.Client.exceptions.InvalidCommitIdException
CodeCommit.Client.exceptions.RepositoryNotAssociatedWithPullRequestException
CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
CodeCommit.Client.exceptions.PullRequestApprovalRulesNotSatisfiedException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeBase': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string',
                        'mergeCommitId': 'string',
                        'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                    }
                },
            ],
            'clientRequestToken': 'string',
            'revisionId': 'string',
            'approvalRules': [
                {
                    'approvalRuleId': 'string',
                    'approvalRuleName': 'string',
                    'approvalRuleContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string',
                    'originApprovalRuleTemplate': {
                        'approvalRuleTemplateId': 'string',
                        'approvalRuleTemplateName': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.ManualMergeRequiredException
    CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.TipOfSourceReferenceIsDifferentException
    CodeCommit.Client.exceptions.ReferenceDoesNotExistException
    CodeCommit.Client.exceptions.InvalidCommitIdException
    CodeCommit.Client.exceptions.RepositoryNotAssociatedWithPullRequestException
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
    CodeCommit.Client.exceptions.PullRequestApprovalRulesNotSatisfiedException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def merge_pull_request_by_squash(pullRequestId=None, repositoryName=None, sourceCommitId=None, conflictDetailLevel=None, conflictResolutionStrategy=None, commitMessage=None, authorName=None, email=None, keepEmptyFolders=None, conflictResolution=None):
    """
    Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the squash merge strategy. If the merge is successful, it closes the pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.merge_pull_request_by_squash(
        pullRequestId='string',
        repositoryName='string',
        sourceCommitId='string',
        conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
        conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
        commitMessage='string',
        authorName='string',
        email='string',
        keepEmptyFolders=True|False,
        conflictResolution={
            'replaceContents': [
                {
                    'filePath': 'string',
                    'replacementType': 'KEEP_BASE'|'KEEP_SOURCE'|'KEEP_DESTINATION'|'USE_NEW_CONTENT',
                    'content': b'bytes',
                    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
            ],
            'deleteFiles': [
                {
                    'filePath': 'string'
                },
            ],
            'setFileModes': [
                {
                    'filePath': 'string',
                    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
            ]
        }
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request. To get this ID, use ListPullRequests .\n

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where the pull request was created.\n

    :type sourceCommitId: string
    :param sourceCommitId: The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.

    :type conflictDetailLevel: string
    :param conflictDetailLevel: The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

    :type conflictResolutionStrategy: string
    :param conflictResolutionStrategy: Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

    :type commitMessage: string
    :param commitMessage: The commit message to include in the commit information for the merge.

    :type authorName: string
    :param authorName: The name of the author who created the commit. This information is used as both the author and committer for the commit.

    :type email: string
    :param email: The email address of the person merging the branches. This information is used in the commit information for the merge.

    :type keepEmptyFolders: boolean
    :param keepEmptyFolders: If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a .gitkeep file is created for empty folders. The default is false.

    :type conflictResolution: dict
    :param conflictResolution: If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.\n\nreplaceContents (list) --Files to have content replaced as part of the merge conflict resolution.\n\n(dict) --Information about a replacement content entry in the conflict of a merge or pull request operation.\n\nfilePath (string) -- [REQUIRED]The path of the conflicting file.\n\nreplacementType (string) -- [REQUIRED]The replacement type to use when determining how to resolve the conflict.\n\ncontent (bytes) --The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.\n\nfileMode (string) --The file mode to apply during conflict resoltion.\n\n\n\n\n\ndeleteFiles (list) --Files to be deleted as part of the merge conflict resolution.\n\n(dict) --A file that is deleted as part of a commit.\n\nfilePath (string) -- [REQUIRED]The full path of the file to be deleted, including the name of the file.\n\n\n\n\n\nsetFileModes (list) --File modes that are set as part of the merge conflict resolution.\n\n(dict) --Information about the file mode changes.\n\nfilePath (string) -- [REQUIRED]The full path to the file, including the name of the file.\n\nfileMode (string) -- [REQUIRED]The file mode for the file.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'pullRequest': {
        'pullRequestId': 'string',
        'title': 'string',
        'description': 'string',
        'lastActivityDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'pullRequestStatus': 'OPEN'|'CLOSED',
        'authorArn': 'string',
        'pullRequestTargets': [
            {
                'repositoryName': 'string',
                'sourceReference': 'string',
                'destinationReference': 'string',
                'destinationCommit': 'string',
                'sourceCommit': 'string',
                'mergeBase': 'string',
                'mergeMetadata': {
                    'isMerged': True|False,
                    'mergedBy': 'string',
                    'mergeCommitId': 'string',
                    'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                }
            },
        ],
        'clientRequestToken': 'string',
        'revisionId': 'string',
        'approvalRules': [
            {
                'approvalRuleId': 'string',
                'approvalRuleName': 'string',
                'approvalRuleContent': 'string',
                'ruleContentSha256': 'string',
                'lastModifiedDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedUser': 'string',
                'originApprovalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --

pullRequest (dict) --
Returns information about a pull request.

pullRequestId (string) --
The system-generated ID of the pull request.

title (string) --
The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.

description (string) --
The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.

lastActivityDate (datetime) --
The day and time of the last user or system activity on the pull request, in timestamp format.

creationDate (datetime) --
The date and time the pull request was originally created, in timestamp format.

pullRequestStatus (string) --
The status of the pull request. Pull request status can only change from OPEN to CLOSED .

authorArn (string) --
The Amazon Resource Name (ARN) of the user who created the pull request.

pullRequestTargets (list) --
The targets of the pull request, including the source branch and destination branch for the pull request.

(dict) --
Returns information about a pull request target.

repositoryName (string) --
The name of the repository that contains the pull request source and destination branches.

sourceReference (string) --
The branch of the repository that contains the changes for the pull request. Also known as the source branch.

destinationReference (string) --
The branch of the repository where the pull request changes are merged. Also known as the destination branch.

destinationCommit (string) --
The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.

sourceCommit (string) --
The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.

mergeBase (string) --
The commit ID of the most recent commit that the source branch and the destination branch have in common.

mergeMetadata (dict) --
Returns metadata about the state of the merge, including whether the merge has been made.

isMerged (boolean) --
A Boolean value indicating whether the merge has been made.

mergedBy (string) --
The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId (string) --
The commit ID for the merge commit, if any.

mergeOption (string) --
The merge strategy used in the merge.







clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

revisionId (string) --
The system-generated revision ID for the pull request.

approvalRules (list) --
The approval rules applied to the pull request.

(dict) --
Returns information about an approval rule.

approvalRuleId (string) --
The system-generated ID of the approval rule.

approvalRuleName (string) --
The name of the approval rule.

approvalRuleContent (string) --
The content of the approval rule.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate (datetime) --
The date the approval rule was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate (dict) --
The approval rule template used to create the rule.

approvalRuleTemplateId (string) --
The ID of the template that created the approval rule.

approvalRuleTemplateName (string) --
The name of the template that created the approval rule.















Exceptions

CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.InvalidCommitIdException
CodeCommit.Client.exceptions.ManualMergeRequiredException
CodeCommit.Client.exceptions.TipOfSourceReferenceIsDifferentException
CodeCommit.Client.exceptions.TipsDivergenceExceededException
CodeCommit.Client.exceptions.NameLengthExceededException
CodeCommit.Client.exceptions.InvalidEmailException
CodeCommit.Client.exceptions.CommitMessageLengthExceededException
CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
CodeCommit.Client.exceptions.InvalidConflictResolutionException
CodeCommit.Client.exceptions.ReplacementTypeRequiredException
CodeCommit.Client.exceptions.InvalidReplacementTypeException
CodeCommit.Client.exceptions.MultipleConflictResolutionEntriesException
CodeCommit.Client.exceptions.ReplacementContentRequiredException
CodeCommit.Client.exceptions.MaximumConflictResolutionEntriesExceededException
CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.InvalidFileModeException
CodeCommit.Client.exceptions.InvalidReplacementContentException
CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.RepositoryNotAssociatedWithPullRequestException
CodeCommit.Client.exceptions.PullRequestApprovalRulesNotSatisfiedException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeBase': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string',
                        'mergeCommitId': 'string',
                        'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                    }
                },
            ],
            'clientRequestToken': 'string',
            'revisionId': 'string',
            'approvalRules': [
                {
                    'approvalRuleId': 'string',
                    'approvalRuleName': 'string',
                    'approvalRuleContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string',
                    'originApprovalRuleTemplate': {
                        'approvalRuleTemplateId': 'string',
                        'approvalRuleTemplateName': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.InvalidCommitIdException
    CodeCommit.Client.exceptions.ManualMergeRequiredException
    CodeCommit.Client.exceptions.TipOfSourceReferenceIsDifferentException
    CodeCommit.Client.exceptions.TipsDivergenceExceededException
    CodeCommit.Client.exceptions.NameLengthExceededException
    CodeCommit.Client.exceptions.InvalidEmailException
    CodeCommit.Client.exceptions.CommitMessageLengthExceededException
    CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
    CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
    CodeCommit.Client.exceptions.InvalidConflictResolutionException
    CodeCommit.Client.exceptions.ReplacementTypeRequiredException
    CodeCommit.Client.exceptions.InvalidReplacementTypeException
    CodeCommit.Client.exceptions.MultipleConflictResolutionEntriesException
    CodeCommit.Client.exceptions.ReplacementContentRequiredException
    CodeCommit.Client.exceptions.MaximumConflictResolutionEntriesExceededException
    CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.InvalidFileModeException
    CodeCommit.Client.exceptions.InvalidReplacementContentException
    CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
    CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
    CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
    CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.RepositoryNotAssociatedWithPullRequestException
    CodeCommit.Client.exceptions.PullRequestApprovalRulesNotSatisfiedException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def merge_pull_request_by_three_way(pullRequestId=None, repositoryName=None, sourceCommitId=None, conflictDetailLevel=None, conflictResolutionStrategy=None, commitMessage=None, authorName=None, email=None, keepEmptyFolders=None, conflictResolution=None):
    """
    Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the three-way merge strategy. If the merge is successful, it closes the pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.merge_pull_request_by_three_way(
        pullRequestId='string',
        repositoryName='string',
        sourceCommitId='string',
        conflictDetailLevel='FILE_LEVEL'|'LINE_LEVEL',
        conflictResolutionStrategy='NONE'|'ACCEPT_SOURCE'|'ACCEPT_DESTINATION'|'AUTOMERGE',
        commitMessage='string',
        authorName='string',
        email='string',
        keepEmptyFolders=True|False,
        conflictResolution={
            'replaceContents': [
                {
                    'filePath': 'string',
                    'replacementType': 'KEEP_BASE'|'KEEP_SOURCE'|'KEEP_DESTINATION'|'USE_NEW_CONTENT',
                    'content': b'bytes',
                    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
            ],
            'deleteFiles': [
                {
                    'filePath': 'string'
                },
            ],
            'setFileModes': [
                {
                    'filePath': 'string',
                    'fileMode': 'EXECUTABLE'|'NORMAL'|'SYMLINK'
                },
            ]
        }
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request. To get this ID, use ListPullRequests .\n

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where the pull request was created.\n

    :type sourceCommitId: string
    :param sourceCommitId: The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.

    :type conflictDetailLevel: string
    :param conflictDetailLevel: The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

    :type conflictResolutionStrategy: string
    :param conflictResolutionStrategy: Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

    :type commitMessage: string
    :param commitMessage: The commit message to include in the commit information for the merge.

    :type authorName: string
    :param authorName: The name of the author who created the commit. This information is used as both the author and committer for the commit.

    :type email: string
    :param email: The email address of the person merging the branches. This information is used in the commit information for the merge.

    :type keepEmptyFolders: boolean
    :param keepEmptyFolders: If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a .gitkeep file is created for empty folders. The default is false.

    :type conflictResolution: dict
    :param conflictResolution: If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.\n\nreplaceContents (list) --Files to have content replaced as part of the merge conflict resolution.\n\n(dict) --Information about a replacement content entry in the conflict of a merge or pull request operation.\n\nfilePath (string) -- [REQUIRED]The path of the conflicting file.\n\nreplacementType (string) -- [REQUIRED]The replacement type to use when determining how to resolve the conflict.\n\ncontent (bytes) --The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.\n\nfileMode (string) --The file mode to apply during conflict resoltion.\n\n\n\n\n\ndeleteFiles (list) --Files to be deleted as part of the merge conflict resolution.\n\n(dict) --A file that is deleted as part of a commit.\n\nfilePath (string) -- [REQUIRED]The full path of the file to be deleted, including the name of the file.\n\n\n\n\n\nsetFileModes (list) --File modes that are set as part of the merge conflict resolution.\n\n(dict) --Information about the file mode changes.\n\nfilePath (string) -- [REQUIRED]The full path to the file, including the name of the file.\n\nfileMode (string) -- [REQUIRED]The file mode for the file.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'pullRequest': {
        'pullRequestId': 'string',
        'title': 'string',
        'description': 'string',
        'lastActivityDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'pullRequestStatus': 'OPEN'|'CLOSED',
        'authorArn': 'string',
        'pullRequestTargets': [
            {
                'repositoryName': 'string',
                'sourceReference': 'string',
                'destinationReference': 'string',
                'destinationCommit': 'string',
                'sourceCommit': 'string',
                'mergeBase': 'string',
                'mergeMetadata': {
                    'isMerged': True|False,
                    'mergedBy': 'string',
                    'mergeCommitId': 'string',
                    'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                }
            },
        ],
        'clientRequestToken': 'string',
        'revisionId': 'string',
        'approvalRules': [
            {
                'approvalRuleId': 'string',
                'approvalRuleName': 'string',
                'approvalRuleContent': 'string',
                'ruleContentSha256': 'string',
                'lastModifiedDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedUser': 'string',
                'originApprovalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --

pullRequest (dict) --
Returns information about a pull request.

pullRequestId (string) --
The system-generated ID of the pull request.

title (string) --
The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.

description (string) --
The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.

lastActivityDate (datetime) --
The day and time of the last user or system activity on the pull request, in timestamp format.

creationDate (datetime) --
The date and time the pull request was originally created, in timestamp format.

pullRequestStatus (string) --
The status of the pull request. Pull request status can only change from OPEN to CLOSED .

authorArn (string) --
The Amazon Resource Name (ARN) of the user who created the pull request.

pullRequestTargets (list) --
The targets of the pull request, including the source branch and destination branch for the pull request.

(dict) --
Returns information about a pull request target.

repositoryName (string) --
The name of the repository that contains the pull request source and destination branches.

sourceReference (string) --
The branch of the repository that contains the changes for the pull request. Also known as the source branch.

destinationReference (string) --
The branch of the repository where the pull request changes are merged. Also known as the destination branch.

destinationCommit (string) --
The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.

sourceCommit (string) --
The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.

mergeBase (string) --
The commit ID of the most recent commit that the source branch and the destination branch have in common.

mergeMetadata (dict) --
Returns metadata about the state of the merge, including whether the merge has been made.

isMerged (boolean) --
A Boolean value indicating whether the merge has been made.

mergedBy (string) --
The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId (string) --
The commit ID for the merge commit, if any.

mergeOption (string) --
The merge strategy used in the merge.







clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

revisionId (string) --
The system-generated revision ID for the pull request.

approvalRules (list) --
The approval rules applied to the pull request.

(dict) --
Returns information about an approval rule.

approvalRuleId (string) --
The system-generated ID of the approval rule.

approvalRuleName (string) --
The name of the approval rule.

approvalRuleContent (string) --
The content of the approval rule.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate (datetime) --
The date the approval rule was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate (dict) --
The approval rule template used to create the rule.

approvalRuleTemplateId (string) --
The ID of the template that created the approval rule.

approvalRuleTemplateName (string) --
The name of the template that created the approval rule.















Exceptions

CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.InvalidCommitIdException
CodeCommit.Client.exceptions.ManualMergeRequiredException
CodeCommit.Client.exceptions.TipOfSourceReferenceIsDifferentException
CodeCommit.Client.exceptions.TipsDivergenceExceededException
CodeCommit.Client.exceptions.NameLengthExceededException
CodeCommit.Client.exceptions.InvalidEmailException
CodeCommit.Client.exceptions.CommitMessageLengthExceededException
CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
CodeCommit.Client.exceptions.InvalidConflictResolutionException
CodeCommit.Client.exceptions.ReplacementTypeRequiredException
CodeCommit.Client.exceptions.InvalidReplacementTypeException
CodeCommit.Client.exceptions.MultipleConflictResolutionEntriesException
CodeCommit.Client.exceptions.ReplacementContentRequiredException
CodeCommit.Client.exceptions.MaximumConflictResolutionEntriesExceededException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.InvalidFileModeException
CodeCommit.Client.exceptions.InvalidReplacementContentException
CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.RepositoryNotAssociatedWithPullRequestException
CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
CodeCommit.Client.exceptions.PullRequestApprovalRulesNotSatisfiedException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeBase': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string',
                        'mergeCommitId': 'string',
                        'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                    }
                },
            ],
            'clientRequestToken': 'string',
            'revisionId': 'string',
            'approvalRules': [
                {
                    'approvalRuleId': 'string',
                    'approvalRuleName': 'string',
                    'approvalRuleContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string',
                    'originApprovalRuleTemplate': {
                        'approvalRuleTemplateId': 'string',
                        'approvalRuleTemplateName': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.InvalidCommitIdException
    CodeCommit.Client.exceptions.ManualMergeRequiredException
    CodeCommit.Client.exceptions.TipOfSourceReferenceIsDifferentException
    CodeCommit.Client.exceptions.TipsDivergenceExceededException
    CodeCommit.Client.exceptions.NameLengthExceededException
    CodeCommit.Client.exceptions.InvalidEmailException
    CodeCommit.Client.exceptions.CommitMessageLengthExceededException
    CodeCommit.Client.exceptions.InvalidConflictDetailLevelException
    CodeCommit.Client.exceptions.InvalidConflictResolutionStrategyException
    CodeCommit.Client.exceptions.InvalidConflictResolutionException
    CodeCommit.Client.exceptions.ReplacementTypeRequiredException
    CodeCommit.Client.exceptions.InvalidReplacementTypeException
    CodeCommit.Client.exceptions.MultipleConflictResolutionEntriesException
    CodeCommit.Client.exceptions.ReplacementContentRequiredException
    CodeCommit.Client.exceptions.MaximumConflictResolutionEntriesExceededException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.InvalidFileModeException
    CodeCommit.Client.exceptions.InvalidReplacementContentException
    CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
    CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
    CodeCommit.Client.exceptions.MaximumFileContentToLoadExceededException
    CodeCommit.Client.exceptions.MaximumItemsToCompareExceededException
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.RepositoryNotAssociatedWithPullRequestException
    CodeCommit.Client.exceptions.ConcurrentReferenceUpdateException
    CodeCommit.Client.exceptions.PullRequestApprovalRulesNotSatisfiedException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def override_pull_request_approval_rules(pullRequestId=None, revisionId=None, overrideStatus=None):
    """
    Sets aside (overrides) all approval rule requirements for a specified pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.override_pull_request_approval_rules(
        pullRequestId='string',
        revisionId='string',
        overrideStatus='OVERRIDE'|'REVOKE'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request for which you want to override all approval rule requirements. To get this information, use GetPullRequest .\n

    :type revisionId: string
    :param revisionId: [REQUIRED]\nThe system-generated ID of the most recent revision of the pull request. You cannot override approval rules for anything but the most recent revision of a pull request. To get the revision ID, use GetPullRequest.\n

    :type overrideStatus: string
    :param overrideStatus: [REQUIRED]\nWhether you want to set aside approval rule requirements for the pull request (OVERRIDE) or revoke a previous override and apply approval rule requirements (REVOKE). REVOKE status is not stored.\n

    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.InvalidRevisionIdException
    CodeCommit.Client.exceptions.RevisionIdRequiredException
    CodeCommit.Client.exceptions.InvalidOverrideStatusException
    CodeCommit.Client.exceptions.OverrideStatusRequiredException
    CodeCommit.Client.exceptions.OverrideAlreadySetException
    CodeCommit.Client.exceptions.RevisionNotCurrentException
    CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def post_comment_for_compared_commit(repositoryName=None, beforeCommitId=None, afterCommitId=None, location=None, content=None, clientRequestToken=None):
    """
    Posts a comment on the comparison between two commits.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.post_comment_for_compared_commit(
        repositoryName='string',
        beforeCommitId='string',
        afterCommitId='string',
        location={
            'filePath': 'string',
            'filePosition': 123,
            'relativeFileVersion': 'BEFORE'|'AFTER'
        },
        content='string',
        clientRequestToken='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to post a comment on the comparison between commits.\n

    :type beforeCommitId: string
    :param beforeCommitId: To establish the directionality of the comparison, the full commit ID of the before commit. Required for commenting on any commit unless that commit is the initial commit.

    :type afterCommitId: string
    :param afterCommitId: [REQUIRED]\nTo establish the directionality of the comparison, the full commit ID of the after commit.\n

    :type location: dict
    :param location: The location of the comparison where you want to comment.\n\nfilePath (string) --The name of the file being compared, including its extension and subdirectory, if any.\n\nfilePosition (integer) --The position of a change in a compared file, in line number format.\n\nrelativeFileVersion (string) --In a comparison of commits or a pull request, whether the change is in the before or after of that comparison.\n\n\n

    :type content: string
    :param content: [REQUIRED]\nThe content of the comment you want to make.\n

    :type clientRequestToken: string
    :param clientRequestToken: A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'repositoryName': 'string',
    'beforeCommitId': 'string',
    'afterCommitId': 'string',
    'beforeBlobId': 'string',
    'afterBlobId': 'string',
    'location': {
        'filePath': 'string',
        'filePosition': 123,
        'relativeFileVersion': 'BEFORE'|'AFTER'
    },
    'comment': {
        'commentId': 'string',
        'content': 'string',
        'inReplyTo': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'authorArn': 'string',
        'deleted': True|False,
        'clientRequestToken': 'string'
    }
}


Response Structure

(dict) --

repositoryName (string) --
The name of the repository where you posted a comment on the comparison between commits.

beforeCommitId (string) --
In the directionality you established, the full commit ID of the before commit.

afterCommitId (string) --
In the directionality you established, the full commit ID of the after commit.

beforeBlobId (string) --
In the directionality you established, the blob ID of the before blob.

afterBlobId (string) --
In the directionality you established, the blob ID of the after blob.

location (dict) --
The location of the comment in the comparison between the two commits.

filePath (string) --
The name of the file being compared, including its extension and subdirectory, if any.

filePosition (integer) --
The position of a change in a compared file, in line number format.

relativeFileVersion (string) --
In a comparison of commits or a pull request, whether the change is in the before or after of that comparison.



comment (dict) --
The content of the comment you posted.

commentId (string) --
The system-generated comment ID.

content (string) --
The content of the comment.

inReplyTo (string) --
The ID of the comment for which this comment is a reply, if any.

creationDate (datetime) --
The date and time the comment was created, in timestamp format.

lastModifiedDate (datetime) --
The date and time the comment was most recently modified, in timestamp format.

authorArn (string) --
The Amazon Resource Name (ARN) of the person who posted the comment.

deleted (boolean) --
A Boolean value indicating whether the comment has been deleted.

clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.









Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.ClientRequestTokenRequiredException
CodeCommit.Client.exceptions.InvalidClientRequestTokenException
CodeCommit.Client.exceptions.IdempotencyParameterMismatchException
CodeCommit.Client.exceptions.CommentContentRequiredException
CodeCommit.Client.exceptions.CommentContentSizeLimitExceededException
CodeCommit.Client.exceptions.InvalidFileLocationException
CodeCommit.Client.exceptions.InvalidRelativeFileVersionEnumException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidFilePositionException
CodeCommit.Client.exceptions.CommitIdRequiredException
CodeCommit.Client.exceptions.InvalidCommitIdException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
CodeCommit.Client.exceptions.BeforeCommitIdAndAfterCommitIdAreSameException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.PathDoesNotExistException


    :return: {
        'repositoryName': 'string',
        'beforeCommitId': 'string',
        'afterCommitId': 'string',
        'beforeBlobId': 'string',
        'afterBlobId': 'string',
        'location': {
            'filePath': 'string',
            'filePosition': 123,
            'relativeFileVersion': 'BEFORE'|'AFTER'
        },
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.ClientRequestTokenRequiredException
    CodeCommit.Client.exceptions.InvalidClientRequestTokenException
    CodeCommit.Client.exceptions.IdempotencyParameterMismatchException
    CodeCommit.Client.exceptions.CommentContentRequiredException
    CodeCommit.Client.exceptions.CommentContentSizeLimitExceededException
    CodeCommit.Client.exceptions.InvalidFileLocationException
    CodeCommit.Client.exceptions.InvalidRelativeFileVersionEnumException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidFilePositionException
    CodeCommit.Client.exceptions.CommitIdRequiredException
    CodeCommit.Client.exceptions.InvalidCommitIdException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    CodeCommit.Client.exceptions.BeforeCommitIdAndAfterCommitIdAreSameException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.PathDoesNotExistException
    
    """
    pass

def post_comment_for_pull_request(pullRequestId=None, repositoryName=None, beforeCommitId=None, afterCommitId=None, location=None, content=None, clientRequestToken=None):
    """
    Posts a comment on a pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.post_comment_for_pull_request(
        pullRequestId='string',
        repositoryName='string',
        beforeCommitId='string',
        afterCommitId='string',
        location={
            'filePath': 'string',
            'filePosition': 123,
            'relativeFileVersion': 'BEFORE'|'AFTER'
        },
        content='string',
        clientRequestToken='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request. To get this ID, use ListPullRequests .\n

    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to post a comment on a pull request.\n

    :type beforeCommitId: string
    :param beforeCommitId: [REQUIRED]\nThe full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created.\n

    :type afterCommitId: string
    :param afterCommitId: [REQUIRED]\nThe full commit ID of the commit in the source branch that is the current tip of the branch for the pull request when you post the comment.\n

    :type location: dict
    :param location: The location of the change where you want to post your comment. If no location is provided, the comment is posted as a general comment on the pull request difference between the before commit ID and the after commit ID.\n\nfilePath (string) --The name of the file being compared, including its extension and subdirectory, if any.\n\nfilePosition (integer) --The position of a change in a compared file, in line number format.\n\nrelativeFileVersion (string) --In a comparison of commits or a pull request, whether the change is in the before or after of that comparison.\n\n\n

    :type content: string
    :param content: [REQUIRED]\nThe content of your comment on the change.\n

    :type clientRequestToken: string
    :param clientRequestToken: A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'repositoryName': 'string',
    'pullRequestId': 'string',
    'beforeCommitId': 'string',
    'afterCommitId': 'string',
    'beforeBlobId': 'string',
    'afterBlobId': 'string',
    'location': {
        'filePath': 'string',
        'filePosition': 123,
        'relativeFileVersion': 'BEFORE'|'AFTER'
    },
    'comment': {
        'commentId': 'string',
        'content': 'string',
        'inReplyTo': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'authorArn': 'string',
        'deleted': True|False,
        'clientRequestToken': 'string'
    }
}


Response Structure

(dict) --

repositoryName (string) --
The name of the repository where you posted a comment on a pull request.

pullRequestId (string) --
The system-generated ID of the pull request.

beforeCommitId (string) --
The full commit ID of the commit in the source branch used to create the pull request, or in the case of an updated pull request, the full commit ID of the commit used to update the pull request.

afterCommitId (string) --
The full commit ID of the commit in the destination branch where the pull request is merged.

beforeBlobId (string) --
In the directionality of the pull request, the blob ID of the before blob.

afterBlobId (string) --
In the directionality of the pull request, the blob ID of the after blob.

location (dict) --
The location of the change where you posted your comment.

filePath (string) --
The name of the file being compared, including its extension and subdirectory, if any.

filePosition (integer) --
The position of a change in a compared file, in line number format.

relativeFileVersion (string) --
In a comparison of commits or a pull request, whether the change is in the before or after of that comparison.



comment (dict) --
The content of the comment you posted.

commentId (string) --
The system-generated comment ID.

content (string) --
The content of the comment.

inReplyTo (string) --
The ID of the comment for which this comment is a reply, if any.

creationDate (datetime) --
The date and time the comment was created, in timestamp format.

lastModifiedDate (datetime) --
The date and time the comment was most recently modified, in timestamp format.

authorArn (string) --
The Amazon Resource Name (ARN) of the person who posted the comment.

deleted (boolean) --
A Boolean value indicating whether the comment has been deleted.

clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.









Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.RepositoryNotAssociatedWithPullRequestException
CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.ClientRequestTokenRequiredException
CodeCommit.Client.exceptions.InvalidClientRequestTokenException
CodeCommit.Client.exceptions.IdempotencyParameterMismatchException
CodeCommit.Client.exceptions.CommentContentRequiredException
CodeCommit.Client.exceptions.CommentContentSizeLimitExceededException
CodeCommit.Client.exceptions.InvalidFileLocationException
CodeCommit.Client.exceptions.InvalidRelativeFileVersionEnumException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidFilePositionException
CodeCommit.Client.exceptions.CommitIdRequiredException
CodeCommit.Client.exceptions.InvalidCommitIdException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
CodeCommit.Client.exceptions.CommitDoesNotExistException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.PathDoesNotExistException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.BeforeCommitIdAndAfterCommitIdAreSameException


    :return: {
        'repositoryName': 'string',
        'pullRequestId': 'string',
        'beforeCommitId': 'string',
        'afterCommitId': 'string',
        'beforeBlobId': 'string',
        'afterBlobId': 'string',
        'location': {
            'filePath': 'string',
            'filePosition': 123,
            'relativeFileVersion': 'BEFORE'|'AFTER'
        },
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.RepositoryNotAssociatedWithPullRequestException
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.ClientRequestTokenRequiredException
    CodeCommit.Client.exceptions.InvalidClientRequestTokenException
    CodeCommit.Client.exceptions.IdempotencyParameterMismatchException
    CodeCommit.Client.exceptions.CommentContentRequiredException
    CodeCommit.Client.exceptions.CommentContentSizeLimitExceededException
    CodeCommit.Client.exceptions.InvalidFileLocationException
    CodeCommit.Client.exceptions.InvalidRelativeFileVersionEnumException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidFilePositionException
    CodeCommit.Client.exceptions.CommitIdRequiredException
    CodeCommit.Client.exceptions.InvalidCommitIdException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    CodeCommit.Client.exceptions.CommitDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.PathDoesNotExistException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.BeforeCommitIdAndAfterCommitIdAreSameException
    
    """
    pass

def post_comment_reply(inReplyTo=None, clientRequestToken=None, content=None):
    """
    Posts a comment in reply to an existing comment on a comparison between commits or a pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.post_comment_reply(
        inReplyTo='string',
        clientRequestToken='string',
        content='string'
    )
    
    
    :type inReplyTo: string
    :param inReplyTo: [REQUIRED]\nThe system-generated ID of the comment to which you want to reply. To get this ID, use GetCommentsForComparedCommit or GetCommentsForPullRequest .\n

    :type clientRequestToken: string
    :param clientRequestToken: A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.\nThis field is autopopulated if not provided.\n

    :type content: string
    :param content: [REQUIRED]\nThe contents of your reply to a comment.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'comment': {
        'commentId': 'string',
        'content': 'string',
        'inReplyTo': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'authorArn': 'string',
        'deleted': True|False,
        'clientRequestToken': 'string'
    }
}


Response Structure

(dict) --

comment (dict) --
Information about the reply to a comment.

commentId (string) --
The system-generated comment ID.

content (string) --
The content of the comment.

inReplyTo (string) --
The ID of the comment for which this comment is a reply, if any.

creationDate (datetime) --
The date and time the comment was created, in timestamp format.

lastModifiedDate (datetime) --
The date and time the comment was most recently modified, in timestamp format.

authorArn (string) --
The Amazon Resource Name (ARN) of the person who posted the comment.

deleted (boolean) --
A Boolean value indicating whether the comment has been deleted.

clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.









Exceptions

CodeCommit.Client.exceptions.ClientRequestTokenRequiredException
CodeCommit.Client.exceptions.InvalidClientRequestTokenException
CodeCommit.Client.exceptions.IdempotencyParameterMismatchException
CodeCommit.Client.exceptions.CommentContentRequiredException
CodeCommit.Client.exceptions.CommentContentSizeLimitExceededException
CodeCommit.Client.exceptions.CommentDoesNotExistException
CodeCommit.Client.exceptions.CommentIdRequiredException
CodeCommit.Client.exceptions.InvalidCommentIdException


    :return: {
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.ClientRequestTokenRequiredException
    CodeCommit.Client.exceptions.InvalidClientRequestTokenException
    CodeCommit.Client.exceptions.IdempotencyParameterMismatchException
    CodeCommit.Client.exceptions.CommentContentRequiredException
    CodeCommit.Client.exceptions.CommentContentSizeLimitExceededException
    CodeCommit.Client.exceptions.CommentDoesNotExistException
    CodeCommit.Client.exceptions.CommentIdRequiredException
    CodeCommit.Client.exceptions.InvalidCommentIdException
    
    """
    pass

def put_file(repositoryName=None, branchName=None, fileContent=None, filePath=None, fileMode=None, parentCommitId=None, commitMessage=None, name=None, email=None):
    """
    Adds or updates a file in a branch in an AWS CodeCommit repository, and generates a commit for the addition in the specified branch.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_file(
        repositoryName='string',
        branchName='string',
        fileContent=b'bytes',
        filePath='string',
        fileMode='EXECUTABLE'|'NORMAL'|'SYMLINK',
        parentCommitId='string',
        commitMessage='string',
        name='string',
        email='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to add or update the file.\n

    :type branchName: string
    :param branchName: [REQUIRED]\nThe name of the branch where you want to add or update the file. If this is an empty repository, this branch is created.\n

    :type fileContent: bytes
    :param fileContent: [REQUIRED]\nThe content of the file, in binary object format.\n

    :type filePath: string
    :param filePath: [REQUIRED]\nThe name of the file you want to add or update, including the relative path to the file in the repository.\n\nNote\nIf the path does not currently exist in the repository, the path is created as part of adding the file.\n\n

    :type fileMode: string
    :param fileMode: The file mode permissions of the blob. Valid file mode permissions are listed here.

    :type parentCommitId: string
    :param parentCommitId: The full commit ID of the head commit in the branch where you want to add or update the file. If this is an empty repository, no commit ID is required. If this is not an empty repository, a commit ID is required.\nThe commit ID must match the ID of the head commit at the time of the operation. Otherwise, an error occurs, and the file is not added or updated.\n

    :type commitMessage: string
    :param commitMessage: A message about why this file was added or updated. Although it is optional, a message makes the commit history for your repository more useful.

    :type name: string
    :param name: The name of the person adding or updating the file. Although it is optional, a name makes the commit history for your repository more useful.

    :type email: string
    :param email: An email address for the person adding or updating the file.

    :rtype: dict

ReturnsResponse Syntax
{
    'commitId': 'string',
    'blobId': 'string',
    'treeId': 'string'
}


Response Structure

(dict) --

commitId (string) --
The full SHA ID of the commit that contains this file change.

blobId (string) --
The ID of the blob, which is its SHA-1 pointer.

treeId (string) --
The full SHA-1 pointer of the tree information for the commit that contains this file change.







Exceptions

CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.ParentCommitIdRequiredException
CodeCommit.Client.exceptions.InvalidParentCommitIdException
CodeCommit.Client.exceptions.ParentCommitDoesNotExistException
CodeCommit.Client.exceptions.ParentCommitIdOutdatedException
CodeCommit.Client.exceptions.FileContentRequiredException
CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
CodeCommit.Client.exceptions.PathRequiredException
CodeCommit.Client.exceptions.InvalidPathException
CodeCommit.Client.exceptions.BranchNameRequiredException
CodeCommit.Client.exceptions.InvalidBranchNameException
CodeCommit.Client.exceptions.BranchDoesNotExistException
CodeCommit.Client.exceptions.BranchNameIsTagNameException
CodeCommit.Client.exceptions.InvalidFileModeException
CodeCommit.Client.exceptions.NameLengthExceededException
CodeCommit.Client.exceptions.InvalidEmailException
CodeCommit.Client.exceptions.CommitMessageLengthExceededException
CodeCommit.Client.exceptions.InvalidDeletionParameterException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
CodeCommit.Client.exceptions.SameFileContentException
CodeCommit.Client.exceptions.FileNameConflictsWithDirectoryNameException
CodeCommit.Client.exceptions.DirectoryNameConflictsWithFileNameException
CodeCommit.Client.exceptions.FilePathConflictsWithSubmodulePathException


    :return: {
        'commitId': 'string',
        'blobId': 'string',
        'treeId': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.ParentCommitIdRequiredException
    CodeCommit.Client.exceptions.InvalidParentCommitIdException
    CodeCommit.Client.exceptions.ParentCommitDoesNotExistException
    CodeCommit.Client.exceptions.ParentCommitIdOutdatedException
    CodeCommit.Client.exceptions.FileContentRequiredException
    CodeCommit.Client.exceptions.FileContentSizeLimitExceededException
    CodeCommit.Client.exceptions.FolderContentSizeLimitExceededException
    CodeCommit.Client.exceptions.PathRequiredException
    CodeCommit.Client.exceptions.InvalidPathException
    CodeCommit.Client.exceptions.BranchNameRequiredException
    CodeCommit.Client.exceptions.InvalidBranchNameException
    CodeCommit.Client.exceptions.BranchDoesNotExistException
    CodeCommit.Client.exceptions.BranchNameIsTagNameException
    CodeCommit.Client.exceptions.InvalidFileModeException
    CodeCommit.Client.exceptions.NameLengthExceededException
    CodeCommit.Client.exceptions.InvalidEmailException
    CodeCommit.Client.exceptions.CommitMessageLengthExceededException
    CodeCommit.Client.exceptions.InvalidDeletionParameterException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    CodeCommit.Client.exceptions.SameFileContentException
    CodeCommit.Client.exceptions.FileNameConflictsWithDirectoryNameException
    CodeCommit.Client.exceptions.DirectoryNameConflictsWithFileNameException
    CodeCommit.Client.exceptions.FilePathConflictsWithSubmodulePathException
    
    """
    pass

def put_repository_triggers(repositoryName=None, triggers=None):
    """
    Replaces all triggers for a repository. Used to create or delete triggers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_repository_triggers(
        repositoryName='string',
        triggers=[
            {
                'name': 'string',
                'destinationArn': 'string',
                'customData': 'string',
                'branches': [
                    'string',
                ],
                'events': [
                    'all'|'updateReference'|'createReference'|'deleteReference',
                ]
            },
        ]
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository where you want to create or update the trigger.\n

    :type triggers: list
    :param triggers: [REQUIRED]\nThe JSON block of configuration information for each trigger.\n\n(dict) --Information about a trigger for a repository.\n\nname (string) -- [REQUIRED]The name of the trigger.\n\ndestinationArn (string) -- [REQUIRED]The ARN of the resource that is the target for a trigger (for example, the ARN of a topic in Amazon SNS).\n\ncustomData (string) --Any custom data associated with the trigger to be included in the information sent to the target of the trigger.\n\nbranches (list) --The branches to be included in the trigger configuration. If you specify an empty array, the trigger applies to all branches.\n\nNote\nAlthough no content is required in the array, you must include the array itself.\n\n\n(string) --\n\n\nevents (list) -- [REQUIRED]The repository events that cause the trigger to run actions in another service, such as sending a notification through Amazon SNS.\n\nNote\nThe valid value 'all' cannot be used with any other values.\n\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'configurationId': 'string'
}


Response Structure

(dict) --
Represents the output of a put repository triggers operation.

configurationId (string) --
The system-generated unique ID for the create or update operation.







Exceptions

CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryTriggersListRequiredException
CodeCommit.Client.exceptions.MaximumRepositoryTriggersExceededException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerNameException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerDestinationArnException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerRegionException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerCustomDataException
CodeCommit.Client.exceptions.MaximumBranchesExceededException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerBranchNameException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerEventsException
CodeCommit.Client.exceptions.RepositoryTriggerNameRequiredException
CodeCommit.Client.exceptions.RepositoryTriggerDestinationArnRequiredException
CodeCommit.Client.exceptions.RepositoryTriggerBranchNameListRequiredException
CodeCommit.Client.exceptions.RepositoryTriggerEventsListRequiredException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'configurationId': 'string'
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.RepositoryTriggersListRequiredException
    CodeCommit.Client.exceptions.MaximumRepositoryTriggersExceededException
    CodeCommit.Client.exceptions.InvalidRepositoryTriggerNameException
    CodeCommit.Client.exceptions.InvalidRepositoryTriggerDestinationArnException
    CodeCommit.Client.exceptions.InvalidRepositoryTriggerRegionException
    CodeCommit.Client.exceptions.InvalidRepositoryTriggerCustomDataException
    CodeCommit.Client.exceptions.MaximumBranchesExceededException
    CodeCommit.Client.exceptions.InvalidRepositoryTriggerBranchNameException
    CodeCommit.Client.exceptions.InvalidRepositoryTriggerEventsException
    CodeCommit.Client.exceptions.RepositoryTriggerNameRequiredException
    CodeCommit.Client.exceptions.RepositoryTriggerDestinationArnRequiredException
    CodeCommit.Client.exceptions.RepositoryTriggerBranchNameListRequiredException
    CodeCommit.Client.exceptions.RepositoryTriggerEventsListRequiredException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds or updates tags for a resource in AWS CodeCommit. For a list of valid resources in AWS CodeCommit, see CodeCommit Resources and Operations in the AWS CodeCommit User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to which you want to add or update tags.\n

    :type tags: dict
    :param tags: [REQUIRED]\nThe key-value pair to use when tagging this repository.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.ResourceArnRequiredException
    CodeCommit.Client.exceptions.InvalidResourceArnException
    CodeCommit.Client.exceptions.TagsMapRequiredException
    CodeCommit.Client.exceptions.InvalidTagsMapException
    CodeCommit.Client.exceptions.TooManyTagsException
    CodeCommit.Client.exceptions.InvalidSystemTagUsageException
    CodeCommit.Client.exceptions.TagPolicyException
    
    """
    pass

def test_repository_triggers(repositoryName=None, triggers=None):
    """
    Tests the functionality of repository triggers by sending information to the trigger target. If real data is available in the repository, the test sends data from the last commit. If no data is available, sample data is generated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.test_repository_triggers(
        repositoryName='string',
        triggers=[
            {
                'name': 'string',
                'destinationArn': 'string',
                'customData': 'string',
                'branches': [
                    'string',
                ],
                'events': [
                    'all'|'updateReference'|'createReference'|'deleteReference',
                ]
            },
        ]
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository in which to test the triggers.\n

    :type triggers: list
    :param triggers: [REQUIRED]\nThe list of triggers to test.\n\n(dict) --Information about a trigger for a repository.\n\nname (string) -- [REQUIRED]The name of the trigger.\n\ndestinationArn (string) -- [REQUIRED]The ARN of the resource that is the target for a trigger (for example, the ARN of a topic in Amazon SNS).\n\ncustomData (string) --Any custom data associated with the trigger to be included in the information sent to the target of the trigger.\n\nbranches (list) --The branches to be included in the trigger configuration. If you specify an empty array, the trigger applies to all branches.\n\nNote\nAlthough no content is required in the array, you must include the array itself.\n\n\n(string) --\n\n\nevents (list) -- [REQUIRED]The repository events that cause the trigger to run actions in another service, such as sending a notification through Amazon SNS.\n\nNote\nThe valid value 'all' cannot be used with any other values.\n\n\n(string) --\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'successfulExecutions': [
        'string',
    ],
    'failedExecutions': [
        {
            'trigger': 'string',
            'failureMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
Represents the output of a test repository triggers operation.

successfulExecutions (list) --
The list of triggers that were successfully tested. This list provides the names of the triggers that were successfully tested, separated by commas.

(string) --


failedExecutions (list) --
The list of triggers that were not tested. This list provides the names of the triggers that could not be tested, separated by commas.

(dict) --
A trigger failed to run.

trigger (string) --
The name of the trigger that did not run.

failureMessage (string) --
Message information about the trigger that did not run.











Exceptions

CodeCommit.Client.exceptions.RepositoryDoesNotExistException
CodeCommit.Client.exceptions.RepositoryNameRequiredException
CodeCommit.Client.exceptions.InvalidRepositoryNameException
CodeCommit.Client.exceptions.RepositoryTriggersListRequiredException
CodeCommit.Client.exceptions.MaximumRepositoryTriggersExceededException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerNameException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerDestinationArnException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerRegionException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerCustomDataException
CodeCommit.Client.exceptions.MaximumBranchesExceededException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerBranchNameException
CodeCommit.Client.exceptions.InvalidRepositoryTriggerEventsException
CodeCommit.Client.exceptions.RepositoryTriggerNameRequiredException
CodeCommit.Client.exceptions.RepositoryTriggerDestinationArnRequiredException
CodeCommit.Client.exceptions.RepositoryTriggerBranchNameListRequiredException
CodeCommit.Client.exceptions.RepositoryTriggerEventsListRequiredException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'successfulExecutions': [
            'string',
        ],
        'failedExecutions': [
            {
                'trigger': 'string',
                'failureMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes tags for a resource in AWS CodeCommit. For a list of valid resources in AWS CodeCommit, see CodeCommit Resources and Operations in the AWS CodeCommit User Guide .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the resource to which you want to remove tags.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nThe tag key for each tag that you want to remove from the resource.\n\n(string) --\n\n

    :returns: 
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.ResourceArnRequiredException
    CodeCommit.Client.exceptions.InvalidResourceArnException
    CodeCommit.Client.exceptions.TagKeysListRequiredException
    CodeCommit.Client.exceptions.InvalidTagKeysListException
    CodeCommit.Client.exceptions.TooManyTagsException
    CodeCommit.Client.exceptions.InvalidSystemTagUsageException
    CodeCommit.Client.exceptions.TagPolicyException
    
    """
    pass

def update_approval_rule_template_content(approvalRuleTemplateName=None, newRuleContent=None, existingRuleContentSha256=None):
    """
    Updates the content of an approval rule template. You can change the number of required approvals, the membership of the approval rule, and whether an approval pool is defined.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_approval_rule_template_content(
        approvalRuleTemplateName='string',
        newRuleContent='string',
        existingRuleContentSha256='string'
    )
    
    
    :type approvalRuleTemplateName: string
    :param approvalRuleTemplateName: [REQUIRED]\nThe name of the approval rule template where you want to update the content of the rule.\n

    :type newRuleContent: string
    :param newRuleContent: [REQUIRED]\nThe content that replaces the existing content of the rule. Content statements must be complete. You cannot provide only the changes.\n

    :type existingRuleContentSha256: string
    :param existingRuleContentSha256: The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using GetPullRequest .

    :rtype: dict

ReturnsResponse Syntax
{
    'approvalRuleTemplate': {
        'approvalRuleTemplateId': 'string',
        'approvalRuleTemplateName': 'string',
        'approvalRuleTemplateDescription': 'string',
        'approvalRuleTemplateContent': 'string',
        'ruleContentSha256': 'string',
        'lastModifiedDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedUser': 'string'
    }
}


Response Structure

(dict) --

approvalRuleTemplate (dict) --
Returns information about an approval rule template.

approvalRuleTemplateId (string) --
The system-generated ID of the approval rule template.

approvalRuleTemplateName (string) --
The name of the approval rule template.

approvalRuleTemplateDescription (string) --
The description of the approval rule template.

approvalRuleTemplateContent (string) --
The content of the approval rule template.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule template.

lastModifiedDate (datetime) --
The date the approval rule template was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule template was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule template.









Exceptions

CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateContentException
CodeCommit.Client.exceptions.InvalidRuleContentSha256Exception
CodeCommit.Client.exceptions.ApprovalRuleTemplateContentRequiredException


    :return: {
        'approvalRuleTemplate': {
            'approvalRuleTemplateId': 'string',
            'approvalRuleTemplateName': 'string',
            'approvalRuleTemplateDescription': 'string',
            'approvalRuleTemplateContent': 'string',
            'ruleContentSha256': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedUser': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
    CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateContentException
    CodeCommit.Client.exceptions.InvalidRuleContentSha256Exception
    CodeCommit.Client.exceptions.ApprovalRuleTemplateContentRequiredException
    
    """
    pass

def update_approval_rule_template_description(approvalRuleTemplateName=None, approvalRuleTemplateDescription=None):
    """
    Updates the description for a specified approval rule template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_approval_rule_template_description(
        approvalRuleTemplateName='string',
        approvalRuleTemplateDescription='string'
    )
    
    
    :type approvalRuleTemplateName: string
    :param approvalRuleTemplateName: [REQUIRED]\nThe name of the template for which you want to update the description.\n

    :type approvalRuleTemplateDescription: string
    :param approvalRuleTemplateDescription: [REQUIRED]\nThe updated description of the approval rule template.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'approvalRuleTemplate': {
        'approvalRuleTemplateId': 'string',
        'approvalRuleTemplateName': 'string',
        'approvalRuleTemplateDescription': 'string',
        'approvalRuleTemplateContent': 'string',
        'ruleContentSha256': 'string',
        'lastModifiedDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedUser': 'string'
    }
}


Response Structure

(dict) --

approvalRuleTemplate (dict) --
The structure and content of the updated approval rule template.

approvalRuleTemplateId (string) --
The system-generated ID of the approval rule template.

approvalRuleTemplateName (string) --
The name of the approval rule template.

approvalRuleTemplateDescription (string) --
The description of the approval rule template.

approvalRuleTemplateContent (string) --
The content of the approval rule template.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule template.

lastModifiedDate (datetime) --
The date the approval rule template was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule template was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule template.









Exceptions

CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateDescriptionException


    :return: {
        'approvalRuleTemplate': {
            'approvalRuleTemplateId': 'string',
            'approvalRuleTemplateName': 'string',
            'approvalRuleTemplateDescription': 'string',
            'approvalRuleTemplateContent': 'string',
            'ruleContentSha256': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedUser': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
    CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateDescriptionException
    
    """
    pass

def update_approval_rule_template_name(oldApprovalRuleTemplateName=None, newApprovalRuleTemplateName=None):
    """
    Updates the name of a specified approval rule template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_approval_rule_template_name(
        oldApprovalRuleTemplateName='string',
        newApprovalRuleTemplateName='string'
    )
    
    
    :type oldApprovalRuleTemplateName: string
    :param oldApprovalRuleTemplateName: [REQUIRED]\nThe current name of the approval rule template.\n

    :type newApprovalRuleTemplateName: string
    :param newApprovalRuleTemplateName: [REQUIRED]\nThe new name you want to apply to the approval rule template.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'approvalRuleTemplate': {
        'approvalRuleTemplateId': 'string',
        'approvalRuleTemplateName': 'string',
        'approvalRuleTemplateDescription': 'string',
        'approvalRuleTemplateContent': 'string',
        'ruleContentSha256': 'string',
        'lastModifiedDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedUser': 'string'
    }
}


Response Structure

(dict) --

approvalRuleTemplate (dict) --
The structure and content of the updated approval rule template.

approvalRuleTemplateId (string) --
The system-generated ID of the approval rule template.

approvalRuleTemplateName (string) --
The name of the approval rule template.

approvalRuleTemplateDescription (string) --
The description of the approval rule template.

approvalRuleTemplateContent (string) --
The content of the approval rule template.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule template.

lastModifiedDate (datetime) --
The date the approval rule template was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule template was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule template.









Exceptions

CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
CodeCommit.Client.exceptions.ApprovalRuleTemplateNameAlreadyExistsException


    :return: {
        'approvalRuleTemplate': {
            'approvalRuleTemplateId': 'string',
            'approvalRuleTemplateName': 'string',
            'approvalRuleTemplateDescription': 'string',
            'approvalRuleTemplateContent': 'string',
            'ruleContentSha256': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedUser': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.InvalidApprovalRuleTemplateNameException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateNameRequiredException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateDoesNotExistException
    CodeCommit.Client.exceptions.ApprovalRuleTemplateNameAlreadyExistsException
    
    """
    pass

def update_comment(commentId=None, content=None):
    """
    Replaces the contents of a comment.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_comment(
        commentId='string',
        content='string'
    )
    
    
    :type commentId: string
    :param commentId: [REQUIRED]\nThe system-generated ID of the comment you want to update. To get this ID, use GetCommentsForComparedCommit or GetCommentsForPullRequest .\n

    :type content: string
    :param content: [REQUIRED]\nThe updated content to replace the existing content of the comment.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'comment': {
        'commentId': 'string',
        'content': 'string',
        'inReplyTo': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'authorArn': 'string',
        'deleted': True|False,
        'clientRequestToken': 'string'
    }
}


Response Structure

(dict) --

comment (dict) --
Information about the updated comment.

commentId (string) --
The system-generated comment ID.

content (string) --
The content of the comment.

inReplyTo (string) --
The ID of the comment for which this comment is a reply, if any.

creationDate (datetime) --
The date and time the comment was created, in timestamp format.

lastModifiedDate (datetime) --
The date and time the comment was most recently modified, in timestamp format.

authorArn (string) --
The Amazon Resource Name (ARN) of the person who posted the comment.

deleted (boolean) --
A Boolean value indicating whether the comment has been deleted.

clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.









Exceptions

CodeCommit.Client.exceptions.CommentContentRequiredException
CodeCommit.Client.exceptions.CommentContentSizeLimitExceededException
CodeCommit.Client.exceptions.CommentDoesNotExistException
CodeCommit.Client.exceptions.CommentIdRequiredException
CodeCommit.Client.exceptions.InvalidCommentIdException
CodeCommit.Client.exceptions.CommentNotCreatedByCallerException
CodeCommit.Client.exceptions.CommentDeletedException


    :return: {
        'comment': {
            'commentId': 'string',
            'content': 'string',
            'inReplyTo': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'authorArn': 'string',
            'deleted': True|False,
            'clientRequestToken': 'string'
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.CommentContentRequiredException
    CodeCommit.Client.exceptions.CommentContentSizeLimitExceededException
    CodeCommit.Client.exceptions.CommentDoesNotExistException
    CodeCommit.Client.exceptions.CommentIdRequiredException
    CodeCommit.Client.exceptions.InvalidCommentIdException
    CodeCommit.Client.exceptions.CommentNotCreatedByCallerException
    CodeCommit.Client.exceptions.CommentDeletedException
    
    """
    pass

def update_default_branch(repositoryName=None, defaultBranchName=None):
    """
    Sets or changes the default branch name for the specified repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_default_branch(
        repositoryName='string',
        defaultBranchName='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to set or change the default branch for.\n

    :type defaultBranchName: string
    :param defaultBranchName: [REQUIRED]\nThe name of the branch to set as the default.\n

    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.BranchNameRequiredException
    CodeCommit.Client.exceptions.InvalidBranchNameException
    CodeCommit.Client.exceptions.BranchDoesNotExistException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def update_pull_request_approval_rule_content(pullRequestId=None, approvalRuleName=None, existingRuleContentSha256=None, newRuleContent=None):
    """
    Updates the structure of an approval rule created specifically for a pull request. For example, you can change the number of required approvers and the approval pool for approvers.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_pull_request_approval_rule_content(
        pullRequestId='string',
        approvalRuleName='string',
        existingRuleContentSha256='string',
        newRuleContent='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request.\n

    :type approvalRuleName: string
    :param approvalRuleName: [REQUIRED]\nThe name of the approval rule you want to update.\n

    :type existingRuleContentSha256: string
    :param existingRuleContentSha256: The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using GetPullRequest .

    :type newRuleContent: string
    :param newRuleContent: [REQUIRED]\nThe updated content for the approval rule.\n\nNote\nWhen you update the content of the approval rule, you can specify approvers in an approval pool in one of two ways:\n\nCodeCommitApprovers : This option only requires an AWS account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the AWS account 123456789012 and Mary_Major , all of the following are counted as approvals coming from that user:\nAn IAM user in the account (arn:aws:iam::123456789012 :user/Mary_Major )\nA federated user identified in IAM as Mary_Major (arn:aws:sts::123456789012 :federated-user/Mary_Major )\n\n\n\nThis option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of Mary_Major (arn:aws:sts::123456789012 :assumed-role/CodeCommitReview/Mary_Major ) unless you include a wildcard (*Mary_Major).\n\nFully qualified ARN : This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role.\n\nFor more information about IAM ARNs, wildcards, and formats, see IAM Identifiers in the IAM User Guide .\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'approvalRule': {
        'approvalRuleId': 'string',
        'approvalRuleName': 'string',
        'approvalRuleContent': 'string',
        'ruleContentSha256': 'string',
        'lastModifiedDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedUser': 'string',
        'originApprovalRuleTemplate': {
            'approvalRuleTemplateId': 'string',
            'approvalRuleTemplateName': 'string'
        }
    }
}


Response Structure

(dict) --

approvalRule (dict) --
Information about the updated approval rule.

approvalRuleId (string) --
The system-generated ID of the approval rule.

approvalRuleName (string) --
The name of the approval rule.

approvalRuleContent (string) --
The content of the approval rule.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate (datetime) --
The date the approval rule was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate (dict) --
The approval rule template used to create the rule.

approvalRuleTemplateId (string) --
The ID of the template that created the approval rule.

approvalRuleTemplateName (string) --
The name of the template that created the approval rule.











Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
CodeCommit.Client.exceptions.ApprovalRuleNameRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleNameException
CodeCommit.Client.exceptions.ApprovalRuleDoesNotExistException
CodeCommit.Client.exceptions.InvalidRuleContentSha256Exception
CodeCommit.Client.exceptions.ApprovalRuleContentRequiredException
CodeCommit.Client.exceptions.InvalidApprovalRuleContentException
CodeCommit.Client.exceptions.CannotModifyApprovalRuleFromTemplateException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'approvalRule': {
            'approvalRuleId': 'string',
            'approvalRuleName': 'string',
            'approvalRuleContent': 'string',
            'ruleContentSha256': 'string',
            'lastModifiedDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedUser': 'string',
            'originApprovalRuleTemplate': {
                'approvalRuleTemplateId': 'string',
                'approvalRuleTemplateName': 'string'
            }
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
    CodeCommit.Client.exceptions.ApprovalRuleNameRequiredException
    CodeCommit.Client.exceptions.InvalidApprovalRuleNameException
    CodeCommit.Client.exceptions.ApprovalRuleDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRuleContentSha256Exception
    CodeCommit.Client.exceptions.ApprovalRuleContentRequiredException
    CodeCommit.Client.exceptions.InvalidApprovalRuleContentException
    CodeCommit.Client.exceptions.CannotModifyApprovalRuleFromTemplateException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def update_pull_request_approval_state(pullRequestId=None, revisionId=None, approvalState=None):
    """
    Updates the state of a user\'s approval on a pull request. The user is derived from the signed-in account when the request is made.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_pull_request_approval_state(
        pullRequestId='string',
        revisionId='string',
        approvalState='APPROVE'|'REVOKE'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request.\n

    :type revisionId: string
    :param revisionId: [REQUIRED]\nThe system-generated ID of the revision.\n

    :type approvalState: string
    :param approvalState: [REQUIRED]\nThe approval state to associate with the user on the pull request.\n

    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.InvalidRevisionIdException
    CodeCommit.Client.exceptions.RevisionIdRequiredException
    CodeCommit.Client.exceptions.InvalidApprovalStateException
    CodeCommit.Client.exceptions.ApprovalStateRequiredException
    CodeCommit.Client.exceptions.PullRequestCannotBeApprovedByAuthorException
    CodeCommit.Client.exceptions.RevisionNotCurrentException
    CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
    CodeCommit.Client.exceptions.MaximumNumberOfApprovalsExceededException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def update_pull_request_description(pullRequestId=None, description=None):
    """
    Replaces the contents of the description of a pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_pull_request_description(
        pullRequestId='string',
        description='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request. To get this ID, use ListPullRequests .\n

    :type description: string
    :param description: [REQUIRED]\nThe updated content of the description for the pull request. This content replaces the existing description.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'pullRequest': {
        'pullRequestId': 'string',
        'title': 'string',
        'description': 'string',
        'lastActivityDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'pullRequestStatus': 'OPEN'|'CLOSED',
        'authorArn': 'string',
        'pullRequestTargets': [
            {
                'repositoryName': 'string',
                'sourceReference': 'string',
                'destinationReference': 'string',
                'destinationCommit': 'string',
                'sourceCommit': 'string',
                'mergeBase': 'string',
                'mergeMetadata': {
                    'isMerged': True|False,
                    'mergedBy': 'string',
                    'mergeCommitId': 'string',
                    'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                }
            },
        ],
        'clientRequestToken': 'string',
        'revisionId': 'string',
        'approvalRules': [
            {
                'approvalRuleId': 'string',
                'approvalRuleName': 'string',
                'approvalRuleContent': 'string',
                'ruleContentSha256': 'string',
                'lastModifiedDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedUser': 'string',
                'originApprovalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --

pullRequest (dict) --
Information about the updated pull request.

pullRequestId (string) --
The system-generated ID of the pull request.

title (string) --
The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.

description (string) --
The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.

lastActivityDate (datetime) --
The day and time of the last user or system activity on the pull request, in timestamp format.

creationDate (datetime) --
The date and time the pull request was originally created, in timestamp format.

pullRequestStatus (string) --
The status of the pull request. Pull request status can only change from OPEN to CLOSED .

authorArn (string) --
The Amazon Resource Name (ARN) of the user who created the pull request.

pullRequestTargets (list) --
The targets of the pull request, including the source branch and destination branch for the pull request.

(dict) --
Returns information about a pull request target.

repositoryName (string) --
The name of the repository that contains the pull request source and destination branches.

sourceReference (string) --
The branch of the repository that contains the changes for the pull request. Also known as the source branch.

destinationReference (string) --
The branch of the repository where the pull request changes are merged. Also known as the destination branch.

destinationCommit (string) --
The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.

sourceCommit (string) --
The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.

mergeBase (string) --
The commit ID of the most recent commit that the source branch and the destination branch have in common.

mergeMetadata (dict) --
Returns metadata about the state of the merge, including whether the merge has been made.

isMerged (boolean) --
A Boolean value indicating whether the merge has been made.

mergedBy (string) --
The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId (string) --
The commit ID for the merge commit, if any.

mergeOption (string) --
The merge strategy used in the merge.







clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

revisionId (string) --
The system-generated revision ID for the pull request.

approvalRules (list) --
The approval rules applied to the pull request.

(dict) --
Returns information about an approval rule.

approvalRuleId (string) --
The system-generated ID of the approval rule.

approvalRuleName (string) --
The name of the approval rule.

approvalRuleContent (string) --
The content of the approval rule.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate (datetime) --
The date the approval rule was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate (dict) --
The approval rule template used to create the rule.

approvalRuleTemplateId (string) --
The ID of the template that created the approval rule.

approvalRuleTemplateName (string) --
The name of the template that created the approval rule.















Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.InvalidDescriptionException
CodeCommit.Client.exceptions.PullRequestAlreadyClosedException


    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeBase': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string',
                        'mergeCommitId': 'string',
                        'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                    }
                },
            ],
            'clientRequestToken': 'string',
            'revisionId': 'string',
            'approvalRules': [
                {
                    'approvalRuleId': 'string',
                    'approvalRuleName': 'string',
                    'approvalRuleContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string',
                    'originApprovalRuleTemplate': {
                        'approvalRuleTemplateId': 'string',
                        'approvalRuleTemplateName': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.InvalidDescriptionException
    CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
    
    """
    pass

def update_pull_request_status(pullRequestId=None, pullRequestStatus=None):
    """
    Updates the status of a pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_pull_request_status(
        pullRequestId='string',
        pullRequestStatus='OPEN'|'CLOSED'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request. To get this ID, use ListPullRequests .\n

    :type pullRequestStatus: string
    :param pullRequestStatus: [REQUIRED]\nThe status of the pull request. The only valid operations are to update the status from OPEN to OPEN , OPEN to CLOSED or from CLOSED to CLOSED .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'pullRequest': {
        'pullRequestId': 'string',
        'title': 'string',
        'description': 'string',
        'lastActivityDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'pullRequestStatus': 'OPEN'|'CLOSED',
        'authorArn': 'string',
        'pullRequestTargets': [
            {
                'repositoryName': 'string',
                'sourceReference': 'string',
                'destinationReference': 'string',
                'destinationCommit': 'string',
                'sourceCommit': 'string',
                'mergeBase': 'string',
                'mergeMetadata': {
                    'isMerged': True|False,
                    'mergedBy': 'string',
                    'mergeCommitId': 'string',
                    'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                }
            },
        ],
        'clientRequestToken': 'string',
        'revisionId': 'string',
        'approvalRules': [
            {
                'approvalRuleId': 'string',
                'approvalRuleName': 'string',
                'approvalRuleContent': 'string',
                'ruleContentSha256': 'string',
                'lastModifiedDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedUser': 'string',
                'originApprovalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --

pullRequest (dict) --
Information about the pull request.

pullRequestId (string) --
The system-generated ID of the pull request.

title (string) --
The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.

description (string) --
The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.

lastActivityDate (datetime) --
The day and time of the last user or system activity on the pull request, in timestamp format.

creationDate (datetime) --
The date and time the pull request was originally created, in timestamp format.

pullRequestStatus (string) --
The status of the pull request. Pull request status can only change from OPEN to CLOSED .

authorArn (string) --
The Amazon Resource Name (ARN) of the user who created the pull request.

pullRequestTargets (list) --
The targets of the pull request, including the source branch and destination branch for the pull request.

(dict) --
Returns information about a pull request target.

repositoryName (string) --
The name of the repository that contains the pull request source and destination branches.

sourceReference (string) --
The branch of the repository that contains the changes for the pull request. Also known as the source branch.

destinationReference (string) --
The branch of the repository where the pull request changes are merged. Also known as the destination branch.

destinationCommit (string) --
The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.

sourceCommit (string) --
The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.

mergeBase (string) --
The commit ID of the most recent commit that the source branch and the destination branch have in common.

mergeMetadata (dict) --
Returns metadata about the state of the merge, including whether the merge has been made.

isMerged (boolean) --
A Boolean value indicating whether the merge has been made.

mergedBy (string) --
The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId (string) --
The commit ID for the merge commit, if any.

mergeOption (string) --
The merge strategy used in the merge.







clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

revisionId (string) --
The system-generated revision ID for the pull request.

approvalRules (list) --
The approval rules applied to the pull request.

(dict) --
Returns information about an approval rule.

approvalRuleId (string) --
The system-generated ID of the approval rule.

approvalRuleName (string) --
The name of the approval rule.

approvalRuleContent (string) --
The content of the approval rule.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate (datetime) --
The date the approval rule was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate (dict) --
The approval rule template used to create the rule.

approvalRuleTemplateId (string) --
The ID of the template that created the approval rule.

approvalRuleTemplateName (string) --
The name of the template that created the approval rule.















Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.InvalidPullRequestStatusUpdateException
CodeCommit.Client.exceptions.InvalidPullRequestStatusException
CodeCommit.Client.exceptions.PullRequestStatusRequiredException
CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
CodeCommit.Client.exceptions.EncryptionKeyDisabledException
CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
CodeCommit.Client.exceptions.EncryptionKeyUnavailableException


    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeBase': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string',
                        'mergeCommitId': 'string',
                        'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                    }
                },
            ],
            'clientRequestToken': 'string',
            'revisionId': 'string',
            'approvalRules': [
                {
                    'approvalRuleId': 'string',
                    'approvalRuleName': 'string',
                    'approvalRuleContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string',
                    'originApprovalRuleTemplate': {
                        'approvalRuleTemplateId': 'string',
                        'approvalRuleTemplateName': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.InvalidPullRequestStatusUpdateException
    CodeCommit.Client.exceptions.InvalidPullRequestStatusException
    CodeCommit.Client.exceptions.PullRequestStatusRequiredException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def update_pull_request_title(pullRequestId=None, title=None):
    """
    Replaces the title of a pull request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_pull_request_title(
        pullRequestId='string',
        title='string'
    )
    
    
    :type pullRequestId: string
    :param pullRequestId: [REQUIRED]\nThe system-generated ID of the pull request. To get this ID, use ListPullRequests .\n

    :type title: string
    :param title: [REQUIRED]\nThe updated title of the pull request. This replaces the existing title.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'pullRequest': {
        'pullRequestId': 'string',
        'title': 'string',
        'description': 'string',
        'lastActivityDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1),
        'pullRequestStatus': 'OPEN'|'CLOSED',
        'authorArn': 'string',
        'pullRequestTargets': [
            {
                'repositoryName': 'string',
                'sourceReference': 'string',
                'destinationReference': 'string',
                'destinationCommit': 'string',
                'sourceCommit': 'string',
                'mergeBase': 'string',
                'mergeMetadata': {
                    'isMerged': True|False,
                    'mergedBy': 'string',
                    'mergeCommitId': 'string',
                    'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                }
            },
        ],
        'clientRequestToken': 'string',
        'revisionId': 'string',
        'approvalRules': [
            {
                'approvalRuleId': 'string',
                'approvalRuleName': 'string',
                'approvalRuleContent': 'string',
                'ruleContentSha256': 'string',
                'lastModifiedDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedUser': 'string',
                'originApprovalRuleTemplate': {
                    'approvalRuleTemplateId': 'string',
                    'approvalRuleTemplateName': 'string'
                }
            },
        ]
    }
}


Response Structure

(dict) --

pullRequest (dict) --
Information about the updated pull request.

pullRequestId (string) --
The system-generated ID of the pull request.

title (string) --
The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.

description (string) --
The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.

lastActivityDate (datetime) --
The day and time of the last user or system activity on the pull request, in timestamp format.

creationDate (datetime) --
The date and time the pull request was originally created, in timestamp format.

pullRequestStatus (string) --
The status of the pull request. Pull request status can only change from OPEN to CLOSED .

authorArn (string) --
The Amazon Resource Name (ARN) of the user who created the pull request.

pullRequestTargets (list) --
The targets of the pull request, including the source branch and destination branch for the pull request.

(dict) --
Returns information about a pull request target.

repositoryName (string) --
The name of the repository that contains the pull request source and destination branches.

sourceReference (string) --
The branch of the repository that contains the changes for the pull request. Also known as the source branch.

destinationReference (string) --
The branch of the repository where the pull request changes are merged. Also known as the destination branch.

destinationCommit (string) --
The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.

sourceCommit (string) --
The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.

mergeBase (string) --
The commit ID of the most recent commit that the source branch and the destination branch have in common.

mergeMetadata (dict) --
Returns metadata about the state of the merge, including whether the merge has been made.

isMerged (boolean) --
A Boolean value indicating whether the merge has been made.

mergedBy (string) --
The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId (string) --
The commit ID for the merge commit, if any.

mergeOption (string) --
The merge strategy used in the merge.







clientRequestToken (string) --
A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

revisionId (string) --
The system-generated revision ID for the pull request.

approvalRules (list) --
The approval rules applied to the pull request.

(dict) --
Returns information about an approval rule.

approvalRuleId (string) --
The system-generated ID of the approval rule.

approvalRuleName (string) --
The name of the approval rule.

approvalRuleContent (string) --
The content of the approval rule.

ruleContentSha256 (string) --
The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate (datetime) --
The date the approval rule was most recently changed, in timestamp format.

creationDate (datetime) --
The date the approval rule was created, in timestamp format.

lastModifiedUser (string) --
The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate (dict) --
The approval rule template used to create the rule.

approvalRuleTemplateId (string) --
The ID of the template that created the approval rule.

approvalRuleTemplateName (string) --
The name of the template that created the approval rule.















Exceptions

CodeCommit.Client.exceptions.PullRequestDoesNotExistException
CodeCommit.Client.exceptions.InvalidPullRequestIdException
CodeCommit.Client.exceptions.PullRequestIdRequiredException
CodeCommit.Client.exceptions.TitleRequiredException
CodeCommit.Client.exceptions.InvalidTitleException
CodeCommit.Client.exceptions.PullRequestAlreadyClosedException


    :return: {
        'pullRequest': {
            'pullRequestId': 'string',
            'title': 'string',
            'description': 'string',
            'lastActivityDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1),
            'pullRequestStatus': 'OPEN'|'CLOSED',
            'authorArn': 'string',
            'pullRequestTargets': [
                {
                    'repositoryName': 'string',
                    'sourceReference': 'string',
                    'destinationReference': 'string',
                    'destinationCommit': 'string',
                    'sourceCommit': 'string',
                    'mergeBase': 'string',
                    'mergeMetadata': {
                        'isMerged': True|False,
                        'mergedBy': 'string',
                        'mergeCommitId': 'string',
                        'mergeOption': 'FAST_FORWARD_MERGE'|'SQUASH_MERGE'|'THREE_WAY_MERGE'
                    }
                },
            ],
            'clientRequestToken': 'string',
            'revisionId': 'string',
            'approvalRules': [
                {
                    'approvalRuleId': 'string',
                    'approvalRuleName': 'string',
                    'approvalRuleContent': 'string',
                    'ruleContentSha256': 'string',
                    'lastModifiedDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1),
                    'lastModifiedUser': 'string',
                    'originApprovalRuleTemplate': {
                        'approvalRuleTemplateId': 'string',
                        'approvalRuleTemplateName': 'string'
                    }
                },
            ]
        }
    }
    
    
    :returns: 
    CodeCommit.Client.exceptions.PullRequestDoesNotExistException
    CodeCommit.Client.exceptions.InvalidPullRequestIdException
    CodeCommit.Client.exceptions.PullRequestIdRequiredException
    CodeCommit.Client.exceptions.TitleRequiredException
    CodeCommit.Client.exceptions.InvalidTitleException
    CodeCommit.Client.exceptions.PullRequestAlreadyClosedException
    
    """
    pass

def update_repository_description(repositoryName=None, repositoryDescription=None):
    """
    Sets or changes the comment or description for a repository.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_repository_description(
        repositoryName='string',
        repositoryDescription='string'
    )
    
    
    :type repositoryName: string
    :param repositoryName: [REQUIRED]\nThe name of the repository to set or change the comment or description for.\n

    :type repositoryDescription: string
    :param repositoryDescription: The new comment or description for the specified repository. Repository descriptions are limited to 1,000 characters.

    :returns: 
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    CodeCommit.Client.exceptions.InvalidRepositoryDescriptionException
    CodeCommit.Client.exceptions.EncryptionIntegrityChecksFailedException
    CodeCommit.Client.exceptions.EncryptionKeyAccessDeniedException
    CodeCommit.Client.exceptions.EncryptionKeyDisabledException
    CodeCommit.Client.exceptions.EncryptionKeyNotFoundException
    CodeCommit.Client.exceptions.EncryptionKeyUnavailableException
    
    """
    pass

def update_repository_name(oldName=None, newName=None):
    """
    Renames a repository. The repository name must be unique across the calling AWS account. Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. The suffix .git is prohibited. For more information about the limits on repository names, see Limits in the AWS CodeCommit User Guide.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_repository_name(
        oldName='string',
        newName='string'
    )
    
    
    :type oldName: string
    :param oldName: [REQUIRED]\nThe current name of the repository.\n

    :type newName: string
    :param newName: [REQUIRED]\nThe new name for the repository.\n

    :returns: 
    CodeCommit.Client.exceptions.RepositoryDoesNotExistException
    CodeCommit.Client.exceptions.RepositoryNameExistsException
    CodeCommit.Client.exceptions.RepositoryNameRequiredException
    CodeCommit.Client.exceptions.InvalidRepositoryNameException
    
    """
    pass

