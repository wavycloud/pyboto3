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

def accept_certificate_transfer(certificateId=None, setAsActive=None):
    """
    Accepts a pending certificate transfer. The default state of the certificate is INACTIVE.
    To check for pending certificate transfers, call  ListCertificates to enumerate your certificates.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.accept_certificate_transfer(
        certificateId='string',
        setAsActive=True|False
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]\nThe ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)\n

    :type setAsActive: boolean
    :param setAsActive: Specifies whether the certificate is active.

    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.TransferAlreadyCompletedException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def add_thing_to_billing_group(billingGroupName=None, billingGroupArn=None, thingName=None, thingArn=None):
    """
    Adds a thing to a billing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_thing_to_billing_group(
        billingGroupName='string',
        billingGroupArn='string',
        thingName='string',
        thingArn='string'
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: The name of the billing group.

    :type billingGroupArn: string
    :param billingGroupArn: The ARN of the billing group.

    :type thingName: string
    :param thingName: The name of the thing to be added to the billing group.

    :type thingArn: string
    :param thingArn: The ARN of the thing to be added to the billing group.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def add_thing_to_thing_group(thingGroupName=None, thingGroupArn=None, thingName=None, thingArn=None, overrideDynamicGroups=None):
    """
    Adds a thing to a thing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_thing_to_thing_group(
        thingGroupName='string',
        thingGroupArn='string',
        thingName='string',
        thingArn='string',
        overrideDynamicGroups=True|False
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: The name of the group to which you are adding a thing.

    :type thingGroupArn: string
    :param thingGroupArn: The ARN of the group to which you are adding a thing.

    :type thingName: string
    :param thingName: The name of the thing to add to a group.

    :type thingArn: string
    :param thingArn: The ARN of the thing to add to a group.

    :type overrideDynamicGroups: boolean
    :param overrideDynamicGroups: Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def associate_targets_with_job(targets=None, jobId=None, comment=None):
    """
    Associates a group with a continuous job. The following criteria must be met:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.associate_targets_with_job(
        targets=[
            'string',
        ],
        jobId='string',
        comment='string'
    )
    
    
    :type targets: list
    :param targets: [REQUIRED]\nA list of thing group ARNs that define the targets of the job.\n\n(string) --\n\n

    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique identifier you assigned to this job when it was created.\n

    :type comment: string
    :param comment: An optional comment string describing why the job was associated with the targets.

    :rtype: dict

ReturnsResponse Syntax
{
    'jobArn': 'string',
    'jobId': 'string',
    'description': 'string'
}


Response Structure

(dict) --

jobArn (string) --
An ARN identifying the job.

jobId (string) --
The unique identifier you assigned to this job when it was created.

description (string) --
A short text description of the job.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'jobArn': 'string',
        'jobId': 'string',
        'description': 'string'
    }
    
    
    :returns: 
    targets (list) -- [REQUIRED]
    A list of thing group ARNs that define the targets of the job.
    
    (string) --
    
    
    jobId (string) -- [REQUIRED]
    The unique identifier you assigned to this job when it was created.
    
    comment (string) -- An optional comment string describing why the job was associated with the targets.
    
    """
    pass

def attach_policy(policyName=None, target=None):
    """
    Attaches a policy to the specified target.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.attach_policy(
        policyName='string',
        target='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe name of the policy to attach.\n

    :type target: string
    :param target: [REQUIRED]\nThe identity to which the policy is attached.\n

    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.LimitExceededException
    
    """
    pass

def attach_principal_policy(policyName=None, principal=None):
    """
    Attaches the specified policy to the specified principal (certificate or other credential).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.attach_principal_policy(
        policyName='string',
        principal='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe policy name.\n

    :type principal: string
    :param principal: [REQUIRED]\nThe principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.\n

    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.LimitExceededException
    
    """
    pass

def attach_security_profile(securityProfileName=None, securityProfileTargetArn=None):
    """
    Associates a Device Defender security profile with a thing group or this account. Each thing group or account can have up to five security profiles associated with it.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.attach_security_profile(
        securityProfileName='string',
        securityProfileTargetArn='string'
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]\nThe security profile that is attached.\n

    :type securityProfileTargetArn: string
    :param securityProfileTargetArn: [REQUIRED]\nThe ARN of the target (thing group) to which the security profile is attached.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.VersionConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def attach_thing_principal(thingName=None, principal=None):
    """
    Attaches the specified principal to the specified thing. A principal can be X.509 certificates, IAM users, groups, and roles, Amazon Cognito identities or federated identities.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.attach_thing_principal(
        thingName='string',
        principal='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing.\n

    :type principal: string
    :param principal: [REQUIRED]\nThe principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The output from the AttachThingPrincipal operation.





Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def cancel_audit_mitigation_actions_task(taskId=None):
    """
    Cancels a mitigation action task that is in progress. If the task is not in progress, an InvalidRequestException occurs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_audit_mitigation_actions_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]\nThe unique identifier for the task that you want to cancel.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def cancel_audit_task(taskId=None):
    """
    Cancels an audit that is in progress. The audit can be either scheduled or on-demand. If the audit is not in progress, an "InvalidRequestException" occurs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_audit_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]\nThe ID of the audit you want to cancel. You can only cancel an audit that is 'IN_PROGRESS'.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def cancel_certificate_transfer(certificateId=None):
    """
    Cancels a pending transfer for the specified certificate.
    After a certificate transfer is cancelled, the status of the certificate changes from PENDING_TRANSFER to INACTIVE.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_certificate_transfer(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]\nThe ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)\n

    """
    pass

def cancel_job(jobId=None, reasonCode=None, comment=None, force=None):
    """
    Cancels a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_job(
        jobId='string',
        reasonCode='string',
        comment='string',
        force=True|False
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique identifier you assigned to this job when it was created.\n

    :type reasonCode: string
    :param reasonCode: (Optional)A reason code string that explains why the job was canceled.

    :type comment: string
    :param comment: An optional comment string describing why the job was canceled.

    :type force: boolean
    :param force: (Optional) If true job executions with status 'IN_PROGRESS' and 'QUEUED' are canceled, otherwise only job executions with status 'QUEUED' are canceled. The default is false .\nCanceling a job which is 'IN_PROGRESS', will cause a device which is executing the job to be unable to update the job execution status. Use caution and ensure that each device executing a job which is canceled is able to recover to a valid state.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobArn': 'string',
    'jobId': 'string',
    'description': 'string'
}


Response Structure

(dict) --

jobArn (string) --
The job ARN.

jobId (string) --
The unique identifier you assigned to this job when it was created.

description (string) --
A short text description of the job.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'jobArn': 'string',
        'jobId': 'string',
        'description': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def cancel_job_execution(jobId=None, thingName=None, force=None, expectedVersion=None, statusDetails=None):
    """
    Cancels the execution of a job for a given thing.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_job_execution(
        jobId='string',
        thingName='string',
        force=True|False,
        expectedVersion=123,
        statusDetails={
            'string': 'string'
        }
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe ID of the job to be canceled.\n

    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing whose execution of the job will be canceled.\n

    :type force: boolean
    :param force: (Optional) If true the job execution will be canceled if it has status IN_PROGRESS or QUEUED, otherwise the job execution will be canceled only if it has status QUEUED. If you attempt to cancel a job execution that is IN_PROGRESS, and you do not set force to true , then an InvalidStateTransitionException will be thrown. The default is false .\nCanceling a job execution which is 'IN_PROGRESS', will cause the device to be unable to update the job execution status. Use caution and ensure that the device is able to recover to a valid state.\n

    :type expectedVersion: integer
    :param expectedVersion: (Optional) The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)

    :type statusDetails: dict
    :param statusDetails: A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged. You can specify at most 10 name/value pairs.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.InvalidStateTransitionException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.VersionConflictException
    
    """
    pass

def clear_default_authorizer():
    """
    Clears the default authorizer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.clear_default_authorizer()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def confirm_topic_rule_destination(confirmationToken=None):
    """
    Confirms a topic rule destination. When you create a rule requiring a destination, AWS IoT sends a confirmation message to the endpoint or base address you specify. The message includes a token which you pass back when calling ConfirmTopicRuleDestination to confirm that you own or have access to the endpoint.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.confirm_topic_rule_destination(
        confirmationToken='string'
    )
    
    
    :type confirmationToken: string
    :param confirmationToken: [REQUIRED]\nThe token used to confirm ownership or access to the topic rule confirmation URL.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ConflictingResourceUpdateException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.InternalException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ConflictingResourceUpdateException
    
    """
    pass

def create_authorizer(authorizerName=None, authorizerFunctionArn=None, tokenKeyName=None, tokenSigningPublicKeys=None, status=None, tags=None, signingDisabled=None):
    """
    Creates an authorizer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_authorizer(
        authorizerName='string',
        authorizerFunctionArn='string',
        tokenKeyName='string',
        tokenSigningPublicKeys={
            'string': 'string'
        },
        status='ACTIVE'|'INACTIVE',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        signingDisabled=True|False
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]\nThe authorizer name.\n

    :type authorizerFunctionArn: string
    :param authorizerFunctionArn: [REQUIRED]\nThe ARN of the authorizer\'s Lambda function.\n

    :type tokenKeyName: string
    :param tokenKeyName: The name of the token key used to extract the token from the HTTP headers.

    :type tokenSigningPublicKeys: dict
    :param tokenSigningPublicKeys: The public keys used to verify the digital signature returned by your custom authentication service.\n\n(string) --\n(string) --\n\n\n\n

    :type status: string
    :param status: The status of the create authorizer request.

    :type tags: list
    :param tags: Metadata which can be used to manage the custom authorizer.\n\nNote\nFor URI Request parameters use format: ...key1=value1&key2=value2...\nFor the CLI command-line parameter use format: &&tags 'key1=value1&key2=value2...'\nFor the cli-input-json file use format: 'tags': 'key1=value1&key2=value2...'\n\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :type signingDisabled: boolean
    :param signingDisabled: Specifies whether AWS IoT validates the token signature in an authorization request.

    :rtype: dict

ReturnsResponse Syntax
{
    'authorizerName': 'string',
    'authorizerArn': 'string'
}


Response Structure

(dict) --

authorizerName (string) --
The authorizer\'s name.

authorizerArn (string) --
The authorizer ARN.







Exceptions

IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'authorizerName': 'string',
        'authorizerArn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def create_billing_group(billingGroupName=None, billingGroupProperties=None, tags=None):
    """
    Creates a billing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_billing_group(
        billingGroupName='string',
        billingGroupProperties={
            'billingGroupDescription': 'string'
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: [REQUIRED]\nThe name you wish to give to the billing group.\n

    :type billingGroupProperties: dict
    :param billingGroupProperties: The properties of the billing group.\n\nbillingGroupDescription (string) --The description of the billing group.\n\n\n

    :type tags: list
    :param tags: Metadata which can be used to manage the billing group.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'billingGroupName': 'string',
    'billingGroupArn': 'string',
    'billingGroupId': 'string'
}


Response Structure

(dict) --

billingGroupName (string) --
The name you gave to the billing group.

billingGroupArn (string) --
The ARN of the billing group.

billingGroupId (string) --
The ID of the billing group.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'billingGroupName': 'string',
        'billingGroupArn': 'string',
        'billingGroupId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def create_certificate_from_csr(certificateSigningRequest=None, setAsActive=None):
    """
    Creates an X.509 certificate using the specified certificate signing request.
    You can create multiple certificates in a batch by creating a directory, copying multiple .csr files into that directory, and then specifying that directory on the command line. The following commands show how to create a batch of certificates given a batch of CSRs.
    Assuming a set of CSRs are located inside of the directory my-csr-directory:
    On Linux and OS X, the command is:
    $ ls my-csr-directory/ | xargs -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}
    This command lists all of the CSRs in my-csr-directory and pipes each CSR file name to the aws iot create-certificate-from-csr AWS CLI command to create a certificate for the corresponding CSR.
    The aws iot create-certificate-from-csr part of the command can also be run in parallel to speed up the certificate creation process:
    $ ls my-csr-directory/ | xargs -P 10 -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}
    On Windows PowerShell, the command to create certificates for all CSRs in my-csr-directory is:
    > ls -Name my-csr-directory | %{aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/$_}
    On a Windows command prompt, the command to create certificates for all CSRs in my-csr-directory is:
    > forfiles /p my-csr-directory /c "cmd /c aws iot create-certificate-from-csr --certificate-signing-request file://@path"
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_certificate_from_csr(
        certificateSigningRequest='string',
        setAsActive=True|False
    )
    
    
    :type certificateSigningRequest: string
    :param certificateSigningRequest: [REQUIRED]\nThe certificate signing request (CSR).\n

    :type setAsActive: boolean
    :param setAsActive: Specifies whether the certificate is active.

    :rtype: dict

ReturnsResponse Syntax
{
    'certificateArn': 'string',
    'certificateId': 'string',
    'certificatePem': 'string'
}


Response Structure

(dict) --
The output from the CreateCertificateFromCsr operation.

certificateArn (string) --
The Amazon Resource Name (ARN) of the certificate. You can use the ARN as a principal for policy operations.

certificateId (string) --
The ID of the certificate. Certificate management operations only take a certificateId.

certificatePem (string) --
The certificate data, in PEM format.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'certificateArn': 'string',
        'certificateId': 'string',
        'certificatePem': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def create_dimension(name=None, type=None, stringValues=None, tags=None, clientRequestToken=None):
    """
    Create a dimension that you can use to limit the scope of a metric used in a security profile for AWS IoT Device Defender. For example, using a TOPIC_FILTER dimension, you can narrow down the scope of the metric only to MQTT topics whose name match the pattern specified in the dimension.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_dimension(
        name='string',
        type='TOPIC_FILTER',
        stringValues=[
            'string',
        ],
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        clientRequestToken='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nA unique identifier for the dimension. Choose something that describes the type and value to make it easy to remember what it does.\n

    :type type: string
    :param type: [REQUIRED]\nSpecifies the type of dimension. Supported types: TOPIC_FILTER.\n

    :type stringValues: list
    :param stringValues: [REQUIRED]\nSpecifies the value or list of values for the dimension. For TOPIC_FILTER dimensions, this is a pattern used to match the MQTT topic (for example, 'admin/#').\n\n(string) --\n\n

    :type tags: list
    :param tags: Metadata that can be used to manage the dimension.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :type clientRequestToken: string
    :param clientRequestToken: [REQUIRED]\nEach dimension must have a unique client request token. If you try to create a new dimension with the same token as a dimension that already exists, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'arn': 'string'
}


Response Structure

(dict) --

name (string) --
A unique identifier for the dimension.

arn (string) --
The ARN (Amazon resource name) of the created dimension.







Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ThrottlingException


    :return: {
        'name': 'string',
        'arn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ThrottlingException
    
    """
    pass

def create_domain_configuration(domainConfigurationName=None, domainName=None, serverCertificateArns=None, validationCertificateArn=None, authorizerConfig=None, serviceType=None, tags=None):
    """
    Creates a domain configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_domain_configuration(
        domainConfigurationName='string',
        domainName='string',
        serverCertificateArns=[
            'string',
        ],
        validationCertificateArn='string',
        authorizerConfig={
            'defaultAuthorizerName': 'string',
            'allowAuthorizerOverride': True|False
        },
        serviceType='DATA'|'CREDENTIAL_PROVIDER'|'JOBS',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type domainConfigurationName: string
    :param domainConfigurationName: [REQUIRED]\nThe name of the domain configuration. This value must be unique to a region.\n

    :type domainName: string
    :param domainName: The name of the domain.

    :type serverCertificateArns: list
    :param serverCertificateArns: The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake. Currently you can specify only one certificate ARN. This value is not required for AWS-managed domains.\n\n(string) --\n\n

    :type validationCertificateArn: string
    :param validationCertificateArn: The certificate used to validate the server certificate and prove domain name ownership. This certificate must be signed by a public certificate authority. This value is not required for AWS-managed domains.

    :type authorizerConfig: dict
    :param authorizerConfig: An object that specifies the authorization service for a domain.\n\ndefaultAuthorizerName (string) --The name of the authorization service for a domain configuration.\n\nallowAuthorizerOverride (boolean) --A Boolean that specifies whether the domain configuration\'s authorization service can be overridden.\n\n\n

    :type serviceType: string
    :param serviceType: The type of service delivered by the endpoint.\n\nNote\nAWS IoT Core currently supports only the DATA service type.\n\n

    :type tags: list
    :param tags: Metadata which can be used to manage the domain configuration.\n\nNote\nFor URI Request parameters use format: ...key1=value1&key2=value2...\nFor the CLI command-line parameter use format: &&tags 'key1=value1&key2=value2...'\nFor the cli-input-json file use format: 'tags': 'key1=value1&key2=value2...'\n\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'domainConfigurationName': 'string',
    'domainConfigurationArn': 'string'
}


Response Structure

(dict) --

domainConfigurationName (string) --
The name of the domain configuration.

domainConfigurationArn (string) --
The ARN of the domain configuration.







Exceptions

IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.CertificateValidationException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ThrottlingException


    :return: {
        'domainConfigurationName': 'string',
        'domainConfigurationArn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.CertificateValidationException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ThrottlingException
    
    """
    pass

def create_dynamic_thing_group(thingGroupName=None, thingGroupProperties=None, indexName=None, queryString=None, queryVersion=None, tags=None):
    """
    Creates a dynamic thing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_dynamic_thing_group(
        thingGroupName='string',
        thingGroupProperties={
            'thingGroupDescription': 'string',
            'attributePayload': {
                'attributes': {
                    'string': 'string'
                },
                'merge': True|False
            }
        },
        indexName='string',
        queryString='string',
        queryVersion='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]\nThe dynamic thing group name to create.\n

    :type thingGroupProperties: dict
    :param thingGroupProperties: The dynamic thing group properties.\n\nthingGroupDescription (string) --The thing group description.\n\nattributePayload (dict) --The thing group attributes in JSON format.\n\nattributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:\n\n{\\'attributes\\':{\\'string1\\':\\'string2\\'}}\n\n(string) --\n(string) --\n\n\n\n\nmerge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.\nTo remove an attribute, call UpdateThing with an empty attribute value.\n\nNote\nThe merge attribute is only valid when calling UpdateThing or UpdateThingGroup .\n\n\n\n\n\n

    :type indexName: string
    :param indexName: The dynamic thing group index name.\n\nNote\nCurrently one index is supported: 'AWS_Things'.\n\n

    :type queryString: string
    :param queryString: [REQUIRED]\nThe dynamic thing group search query string.\nSee Query Syntax for information about query string syntax.\n

    :type queryVersion: string
    :param queryVersion: The dynamic thing group query version.\n\nNote\nCurrently one query version is supported: '2017-09-30'. If not specified, the query version defaults to this value.\n\n

    :type tags: list
    :param tags: Metadata which can be used to manage the dynamic thing group.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'thingGroupName': 'string',
    'thingGroupArn': 'string',
    'thingGroupId': 'string',
    'indexName': 'string',
    'queryString': 'string',
    'queryVersion': 'string'
}


Response Structure

(dict) --

thingGroupName (string) --
The dynamic thing group name.

thingGroupArn (string) --
The dynamic thing group ARN.

thingGroupId (string) --
The dynamic thing group ID.

indexName (string) --
The dynamic thing group index name.

queryString (string) --
The dynamic thing group search query string.

queryVersion (string) --
The dynamic thing group query version.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidQueryException
IoT.Client.exceptions.LimitExceededException


    :return: {
        'thingGroupName': 'string',
        'thingGroupArn': 'string',
        'thingGroupId': 'string',
        'indexName': 'string',
        'queryString': 'string',
        'queryVersion': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidQueryException
    IoT.Client.exceptions.LimitExceededException
    
    """
    pass

def create_job(jobId=None, targets=None, documentSource=None, document=None, description=None, presignedUrlConfig=None, targetSelection=None, jobExecutionsRolloutConfig=None, abortConfig=None, timeoutConfig=None, tags=None):
    """
    Creates a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_job(
        jobId='string',
        targets=[
            'string',
        ],
        documentSource='string',
        document='string',
        description='string',
        presignedUrlConfig={
            'roleArn': 'string',
            'expiresInSec': 123
        },
        targetSelection='CONTINUOUS'|'SNAPSHOT',
        jobExecutionsRolloutConfig={
            'maximumPerMinute': 123,
            'exponentialRate': {
                'baseRatePerMinute': 123,
                'incrementFactor': 123.0,
                'rateIncreaseCriteria': {
                    'numberOfNotifiedThings': 123,
                    'numberOfSucceededThings': 123
                }
            }
        },
        abortConfig={
            'criteriaList': [
                {
                    'failureType': 'FAILED'|'REJECTED'|'TIMED_OUT'|'ALL',
                    'action': 'CANCEL',
                    'thresholdPercentage': 123.0,
                    'minNumberOfExecutedThings': 123
                },
            ]
        },
        timeoutConfig={
            'inProgressTimeoutInMinutes': 123
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nA job identifier which must be unique for your AWS account. We recommend using a UUID. Alpha-numeric characters, '-' and '_' are valid for use here.\n

    :type targets: list
    :param targets: [REQUIRED]\nA list of things and thing groups to which the job should be sent.\n\n(string) --\n\n

    :type documentSource: string
    :param documentSource: An S3 link to the job document.

    :type document: string
    :param document: The job document.\n\nNote\nIf the job document resides in an S3 bucket, you must use a placeholder link when specifying the document.\nThe placeholder link is of the following form:\n\n${aws:iot:s3-presigned-url:https://s3.amazonaws.com/*bucket* /*key* }\nwhere bucket is your bucket name and key is the object in the bucket to which you are linking.\n\n

    :type description: string
    :param description: A short text description of the job.

    :type presignedUrlConfig: dict
    :param presignedUrlConfig: Configuration information for pre-signed S3 URLs.\n\nroleArn (string) --The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.\n\nexpiresInSec (integer) --How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.\n\n\n

    :type targetSelection: string
    :param targetSelection: Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.

    :type jobExecutionsRolloutConfig: dict
    :param jobExecutionsRolloutConfig: Allows you to create a staged rollout of the job.\n\nmaximumPerMinute (integer) --The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.\n\nexponentialRate (dict) --The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.\n\nbaseRatePerMinute (integer) -- [REQUIRED]The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.\n\nincrementFactor (float) -- [REQUIRED]The exponential factor to increase the rate of rollout for a job.\n\nrateIncreaseCriteria (dict) -- [REQUIRED]The criteria to initiate the increase in rate of rollout for a job.\nAWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).\n\nnumberOfNotifiedThings (integer) --The threshold for number of notified things that will initiate the increase in rate of rollout.\n\nnumberOfSucceededThings (integer) --The threshold for number of succeeded things that will initiate the increase in rate of rollout.\n\n\n\n\n\n\n

    :type abortConfig: dict
    :param abortConfig: Allows you to create criteria to abort a job.\n\ncriteriaList (list) -- [REQUIRED]The list of abort criteria to define rules to abort the job.\n\n(dict) --Details of abort criteria to define rules to abort the job.\n\nfailureType (string) -- [REQUIRED]The type of job execution failure to define a rule to initiate a job abort.\n\naction (string) -- [REQUIRED]The type of abort action to initiate a job abort.\n\nthresholdPercentage (float) -- [REQUIRED]The threshold as a percentage of the total number of executed things that will initiate a job abort.\nAWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).\n\nminNumberOfExecutedThings (integer) -- [REQUIRED]Minimum number of executed things before evaluating an abort rule.\n\n\n\n\n\n\n

    :type timeoutConfig: dict
    :param timeoutConfig: Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to IN_PROGRESS . If the job execution status is not set to another terminal state before the time expires, it will be automatically set to TIMED_OUT .\n\ninProgressTimeoutInMinutes (integer) --Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can\'t be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal TIMED_OUT status.\n\n\n

    :type tags: list
    :param tags: Metadata which can be used to manage the job.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'jobArn': 'string',
    'jobId': 'string',
    'description': 'string'
}


Response Structure

(dict) --

jobArn (string) --
The job ARN.

jobId (string) --
The unique identifier you assigned to this job.

description (string) --
The job description.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'jobArn': 'string',
        'jobId': 'string',
        'description': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def create_keys_and_certificate(setAsActive=None):
    """
    Creates a 2048-bit RSA key pair and issues an X.509 certificate using the issued public key. You can also call CreateKeysAndCertificate over MQTT from a device, for more information, see Provisioning MQTT API .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_keys_and_certificate(
        setAsActive=True|False
    )
    
    
    :type setAsActive: boolean
    :param setAsActive: Specifies whether the certificate is active.

    :rtype: dict
ReturnsResponse Syntax{
    'certificateArn': 'string',
    'certificateId': 'string',
    'certificatePem': 'string',
    'keyPair': {
        'PublicKey': 'string',
        'PrivateKey': 'string'
    }
}


Response Structure

(dict) --The output of the CreateKeysAndCertificate operation.

certificateArn (string) --The ARN of the certificate.

certificateId (string) --The ID of the certificate. AWS IoT issues a default subject name for the certificate (for example, AWS IoT Certificate).

certificatePem (string) --The certificate data, in PEM format.

keyPair (dict) --The generated key pair.

PublicKey (string) --The public key.

PrivateKey (string) --The private key.








Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'certificateArn': 'string',
        'certificateId': 'string',
        'certificatePem': 'string',
        'keyPair': {
            'PublicKey': 'string',
            'PrivateKey': 'string'
        }
    }
    
    
    """
    pass

def create_mitigation_action(actionName=None, roleArn=None, actionParams=None, tags=None):
    """
    Defines an action that can be applied to audit findings by using StartAuditMitigationActionsTask. Each mitigation action can apply only one type of change.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_mitigation_action(
        actionName='string',
        roleArn='string',
        actionParams={
            'updateDeviceCertificateParams': {
                'action': 'DEACTIVATE'
            },
            'updateCACertificateParams': {
                'action': 'DEACTIVATE'
            },
            'addThingsToThingGroupParams': {
                'thingGroupNames': [
                    'string',
                ],
                'overrideDynamicGroups': True|False
            },
            'replaceDefaultPolicyVersionParams': {
                'templateName': 'BLANK_POLICY'
            },
            'enableIoTLoggingParams': {
                'roleArnForLogging': 'string',
                'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
            },
            'publishFindingToSnsParams': {
                'topicArn': 'string'
            }
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type actionName: string
    :param actionName: [REQUIRED]\nA friendly name for the action. Choose a friendly name that accurately describes the action (for example, EnableLoggingAction ).\n

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe ARN of the IAM role that is used to apply the mitigation action.\n

    :type actionParams: dict
    :param actionParams: [REQUIRED]\nDefines the type of action and the parameters for that action.\n\nupdateDeviceCertificateParams (dict) --Parameters to define a mitigation action that changes the state of the device certificate to inactive.\n\naction (string) -- [REQUIRED]The action that you want to apply to the device cerrtificate. The only supported value is DEACTIVATE .\n\n\n\nupdateCACertificateParams (dict) --Parameters to define a mitigation action that changes the state of the CA certificate to inactive.\n\naction (string) -- [REQUIRED]The action that you want to apply to the CA cerrtificate. The only supported value is DEACTIVATE .\n\n\n\naddThingsToThingGroupParams (dict) --Parameters to define a mitigation action that moves devices associated with a certificate to one or more specified thing groups, typically for quarantine.\n\nthingGroupNames (list) -- [REQUIRED]The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to more than one group in the same hierarchy.\n\n(string) --\n\n\noverrideDynamicGroups (boolean) --Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic things groups.\n\n\n\nreplaceDefaultPolicyVersionParams (dict) --Parameters to define a mitigation action that adds a blank policy to restrict permissions.\n\ntemplateName (string) -- [REQUIRED]The name of the template to be applied. The only supported value is BLANK_POLICY .\n\n\n\nenableIoTLoggingParams (dict) --Parameters to define a mitigation action that enables AWS IoT logging at a specified level of detail.\n\nroleArnForLogging (string) -- [REQUIRED]The ARN of the IAM role used for logging.\n\nlogLevel (string) -- [REQUIRED]Specifies the types of information to be logged.\n\n\n\npublishFindingToSnsParams (dict) --Parameters to define a mitigation action that publishes findings to Amazon SNS. You can implement your own custom actions in response to the Amazon SNS messages.\n\ntopicArn (string) -- [REQUIRED]The ARN of the topic to which you want to publish the findings.\n\n\n\n\n

    :type tags: list
    :param tags: Metadata that can be used to manage the mitigation action.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'actionArn': 'string',
    'actionId': 'string'
}


Response Structure

(dict) --

actionArn (string) --
The ARN for the new mitigation action.

actionId (string) --
A unique identifier for the new mitigation action.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'actionArn': 'string',
        'actionId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def create_ota_update(otaUpdateId=None, description=None, targets=None, protocols=None, targetSelection=None, awsJobExecutionsRolloutConfig=None, awsJobPresignedUrlConfig=None, files=None, roleArn=None, additionalParameters=None, tags=None):
    """
    Creates an AWS IoT OTAUpdate on a target group of things or groups.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_ota_update(
        otaUpdateId='string',
        description='string',
        targets=[
            'string',
        ],
        protocols=[
            'MQTT'|'HTTP',
        ],
        targetSelection='CONTINUOUS'|'SNAPSHOT',
        awsJobExecutionsRolloutConfig={
            'maximumPerMinute': 123
        },
        awsJobPresignedUrlConfig={
            'expiresInSec': 123
        },
        files=[
            {
                'fileName': 'string',
                'fileVersion': 'string',
                'fileLocation': {
                    'stream': {
                        'streamId': 'string',
                        'fileId': 123
                    },
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'version': 'string'
                    }
                },
                'codeSigning': {
                    'awsSignerJobId': 'string',
                    'startSigningJobParameter': {
                        'signingProfileParameter': {
                            'certificateArn': 'string',
                            'platform': 'string',
                            'certificatePathOnDevice': 'string'
                        },
                        'signingProfileName': 'string',
                        'destination': {
                            's3Destination': {
                                'bucket': 'string',
                                'prefix': 'string'
                            }
                        }
                    },
                    'customCodeSigning': {
                        'signature': {
                            'inlineDocument': b'bytes'
                        },
                        'certificateChain': {
                            'certificateName': 'string',
                            'inlineDocument': 'string'
                        },
                        'hashAlgorithm': 'string',
                        'signatureAlgorithm': 'string'
                    }
                },
                'attributes': {
                    'string': 'string'
                }
            },
        ],
        roleArn='string',
        additionalParameters={
            'string': 'string'
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type otaUpdateId: string
    :param otaUpdateId: [REQUIRED]\nThe ID of the OTA update to be created.\n

    :type description: string
    :param description: The description of the OTA update.

    :type targets: list
    :param targets: [REQUIRED]\nThe targeted devices to receive OTA updates.\n\n(string) --\n\n

    :type protocols: list
    :param protocols: The protocol used to transfer the OTA update image. Valid values are [HTTP], [MQTT], [HTTP, MQTT]. When both HTTP and MQTT are specified, the target device can choose the protocol.\n\n(string) --\n\n

    :type targetSelection: string
    :param targetSelection: Specifies whether the update will continue to run (CONTINUOUS), or will be complete after all the things specified as targets have completed the update (SNAPSHOT). If continuous, the update may also be run on a thing when a change is detected in a target. For example, an update will run on a thing when the thing is added to a target group, even after the update was completed by all things originally in the group. Valid values: CONTINUOUS | SNAPSHOT.

    :type awsJobExecutionsRolloutConfig: dict
    :param awsJobExecutionsRolloutConfig: Configuration for the rollout of OTA updates.\n\nmaximumPerMinute (integer) --The maximum number of OTA update job executions started per minute.\n\n\n

    :type awsJobPresignedUrlConfig: dict
    :param awsJobPresignedUrlConfig: Configuration information for pre-signed URLs.\n\nexpiresInSec (integer) --How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 1800 seconds. Pre-signed URLs are generated when a request for the job document is received.\n\n\n

    :type files: list
    :param files: [REQUIRED]\nThe files to be streamed by the OTA update.\n\n(dict) --Describes a file to be associated with an OTA update.\n\nfileName (string) --The name of the file.\n\nfileVersion (string) --The file version.\n\nfileLocation (dict) --The location of the updated firmware.\n\nstream (dict) --The stream that contains the OTA update.\n\nstreamId (string) --The stream ID.\n\nfileId (integer) --The ID of a file associated with a stream.\n\n\n\ns3Location (dict) --The location of the updated firmware in S3.\n\nbucket (string) --The S3 bucket.\n\nkey (string) --The S3 key.\n\nversion (string) --The S3 bucket version.\n\n\n\n\n\ncodeSigning (dict) --The code signing method of the file.\n\nawsSignerJobId (string) --The ID of the AWSSignerJob which was created to sign the file.\n\nstartSigningJobParameter (dict) --Describes the code-signing job.\n\nsigningProfileParameter (dict) --Describes the code-signing profile.\n\ncertificateArn (string) --Certificate ARN.\n\nplatform (string) --The hardware platform of your device.\n\ncertificatePathOnDevice (string) --The location of the code-signing certificate on your device.\n\n\n\nsigningProfileName (string) --The code-signing profile name.\n\ndestination (dict) --The location to write the code-signed file.\n\ns3Destination (dict) --Describes the location in S3 of the updated firmware.\n\nbucket (string) --The S3 bucket that contains the updated firmware.\n\nprefix (string) --The S3 prefix.\n\n\n\n\n\n\n\ncustomCodeSigning (dict) --A custom method for code signing a file.\n\nsignature (dict) --The signature for the file.\n\ninlineDocument (bytes) --A base64 encoded binary representation of the code signing signature.\n\n\n\ncertificateChain (dict) --The certificate chain.\n\ncertificateName (string) --The name of the certificate.\n\ninlineDocument (string) --A base64 encoded binary representation of the code signing certificate chain.\n\n\n\nhashAlgorithm (string) --The hash algorithm used to code sign the file.\n\nsignatureAlgorithm (string) --The signature algorithm used to code sign the file.\n\n\n\n\n\nattributes (dict) --A list of name/attribute pairs.\n\n(string) --\n(string) --\n\n\n\n\n\n\n\n

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe IAM role that allows access to the AWS IoT Jobs service.\n

    :type additionalParameters: dict
    :param additionalParameters: A list of additional OTA update parameters which are name-value pairs.\n\n(string) --\n(string) --\n\n\n\n

    :type tags: list
    :param tags: Metadata which can be used to manage updates.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'otaUpdateId': 'string',
    'awsIotJobId': 'string',
    'otaUpdateArn': 'string',
    'awsIotJobArn': 'string',
    'otaUpdateStatus': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
}


Response Structure

(dict) --

otaUpdateId (string) --
The OTA update ID.

awsIotJobId (string) --
The AWS IoT job ID associated with the OTA update.

otaUpdateArn (string) --
The OTA update ARN.

awsIotJobArn (string) --
The AWS IoT job ARN associated with the OTA update.

otaUpdateStatus (string) --
The OTA update status.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'otaUpdateId': 'string',
        'awsIotJobId': 'string',
        'otaUpdateArn': 'string',
        'awsIotJobArn': 'string',
        'otaUpdateStatus': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def create_policy(policyName=None, policyDocument=None, tags=None):
    """
    Creates an AWS IoT policy.
    The created policy is the default version for the policy. This operation creates a policy version with a version identifier of 1 and sets 1 as the policy\'s default version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_policy(
        policyName='string',
        policyDocument='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe policy name.\n

    :type policyDocument: string
    :param policyDocument: [REQUIRED]\nThe JSON document that describes the policy. policyDocument must have a minimum length of 1, with a maximum length of 2048, excluding whitespace.\n

    :type tags: list
    :param tags: Metadata which can be used to manage the policy.\n\nNote\nFor URI Request parameters use format: ...key1=value1&key2=value2...\nFor the CLI command-line parameter use format: &&tags 'key1=value1&key2=value2...'\nFor the cli-input-json file use format: 'tags': 'key1=value1&key2=value2...'\n\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'policyName': 'string',
    'policyArn': 'string',
    'policyDocument': 'string',
    'policyVersionId': 'string'
}


Response Structure

(dict) --
The output from the CreatePolicy operation.

policyName (string) --
The policy name.

policyArn (string) --
The policy ARN.

policyDocument (string) --
The JSON document that describes the policy.

policyVersionId (string) --
The policy version ID.







Exceptions

IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.MalformedPolicyException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'policyName': 'string',
        'policyArn': 'string',
        'policyDocument': 'string',
        'policyVersionId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.MalformedPolicyException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def create_policy_version(policyName=None, policyDocument=None, setAsDefault=None):
    """
    Creates a new version of the specified AWS IoT policy. To update a policy, create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must use  DeletePolicyVersion to delete an existing version before you create a new one.
    Optionally, you can set the new version as the policy\'s default version. The default version is the operative version (that is, the version that is in effect for the certificates to which the policy is attached).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_policy_version(
        policyName='string',
        policyDocument='string',
        setAsDefault=True|False
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe policy name.\n

    :type policyDocument: string
    :param policyDocument: [REQUIRED]\nThe JSON document that describes the policy. Minimum length of 1. Maximum length of 2048, excluding whitespace.\n

    :type setAsDefault: boolean
    :param setAsDefault: Specifies whether the policy version is set as the default. When this parameter is true, the new policy version becomes the operative version (that is, the version that is in effect for the certificates to which the policy is attached).

    :rtype: dict

ReturnsResponse Syntax
{
    'policyArn': 'string',
    'policyDocument': 'string',
    'policyVersionId': 'string',
    'isDefaultVersion': True|False
}


Response Structure

(dict) --
The output of the CreatePolicyVersion operation.

policyArn (string) --
The policy ARN.

policyDocument (string) --
The JSON document that describes the policy.

policyVersionId (string) --
The policy version ID.

isDefaultVersion (boolean) --
Specifies whether the policy version is the default.







Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.MalformedPolicyException
IoT.Client.exceptions.VersionsLimitExceededException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'policyArn': 'string',
        'policyDocument': 'string',
        'policyVersionId': 'string',
        'isDefaultVersion': True|False
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.MalformedPolicyException
    IoT.Client.exceptions.VersionsLimitExceededException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def create_provisioning_claim(templateName=None):
    """
    Creates a provisioning claim.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_provisioning_claim(
        templateName='string'
    )
    
    
    :type templateName: string
    :param templateName: [REQUIRED]\nThe name of the provisioning template to use.\n

    :rtype: dict
ReturnsResponse Syntax{
    'certificateId': 'string',
    'certificatePem': 'string',
    'keyPair': {
        'PublicKey': 'string',
        'PrivateKey': 'string'
    },
    'expiration': datetime(2015, 1, 1)
}


Response Structure

(dict) --
certificateId (string) --The ID of the certificate.

certificatePem (string) --The provisioning claim certificate.

keyPair (dict) --The provisioning claim key pair.

PublicKey (string) --The public key.

PrivateKey (string) --The private key.



expiration (datetime) --The provisioning claim expiration time.






Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'certificateId': 'string',
        'certificatePem': 'string',
        'keyPair': {
            'PublicKey': 'string',
            'PrivateKey': 'string'
        },
        'expiration': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def create_provisioning_template(templateName=None, description=None, templateBody=None, enabled=None, provisioningRoleArn=None, preProvisioningHook=None, tags=None):
    """
    Creates a fleet provisioning template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_provisioning_template(
        templateName='string',
        description='string',
        templateBody='string',
        enabled=True|False,
        provisioningRoleArn='string',
        preProvisioningHook={
            'payloadVersion': 'string',
            'targetArn': 'string'
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type templateName: string
    :param templateName: [REQUIRED]\nThe name of the fleet provisioning template.\n

    :type description: string
    :param description: The description of the fleet provisioning template.

    :type templateBody: string
    :param templateBody: [REQUIRED]\nThe JSON formatted contents of the fleet provisioning template.\n

    :type enabled: boolean
    :param enabled: True to enable the fleet provisioning template, otherwise false.

    :type provisioningRoleArn: string
    :param provisioningRoleArn: [REQUIRED]\nThe role ARN for the role associated with the fleet provisioning template. This IoT role grants permission to provision a device.\n

    :type preProvisioningHook: dict
    :param preProvisioningHook: Creates a pre-provisioning hook template.\n\npayloadVersion (string) --The payload that was sent to the target function.\n\nNote: Only Lambda functions are currently supported.\n\ntargetArn (string) -- [REQUIRED]The ARN of the target function.\n\nNote: Only Lambda functions are currently supported.\n\n\n

    :type tags: list
    :param tags: Metadata which can be used to manage the fleet provisioning template.\n\nNote\nFor URI Request parameters use format: ...key1=value1&key2=value2...\nFor the CLI command-line parameter use format: &&tags 'key1=value1&key2=value2...'\nFor the cli-input-json file use format: 'tags': 'key1=value1&key2=value2...'\n\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'templateArn': 'string',
    'templateName': 'string',
    'defaultVersionId': 123
}


Response Structure

(dict) --

templateArn (string) --
The ARN that identifies the provisioning template.

templateName (string) --
The name of the fleet provisioning template.

defaultVersionId (integer) --
The default version of the fleet provisioning template.







Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ResourceAlreadyExistsException


    :return: {
        'templateArn': 'string',
        'templateName': 'string',
        'defaultVersionId': 123
    }
    
    
    :returns: 
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    
    """
    pass

def create_provisioning_template_version(templateName=None, templateBody=None, setAsDefault=None):
    """
    Creates a new version of a fleet provisioning template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_provisioning_template_version(
        templateName='string',
        templateBody='string',
        setAsDefault=True|False
    )
    
    
    :type templateName: string
    :param templateName: [REQUIRED]\nThe name of the fleet provisioning template.\n

    :type templateBody: string
    :param templateBody: [REQUIRED]\nThe JSON formatted contents of the fleet provisioning template.\n

    :type setAsDefault: boolean
    :param setAsDefault: Sets a fleet provision template version as the default version.

    :rtype: dict

ReturnsResponse Syntax
{
    'templateArn': 'string',
    'templateName': 'string',
    'versionId': 123,
    'isDefaultVersion': True|False
}


Response Structure

(dict) --

templateArn (string) --
The ARN that identifies the provisioning template.

templateName (string) --
The name of the fleet provisioning template.

versionId (integer) --
The version of the fleet provisioning template.

isDefaultVersion (boolean) --
True if the fleet provisioning template version is the default version, otherwise false.







Exceptions

IoT.Client.exceptions.VersionsLimitExceededException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ConflictingResourceUpdateException


    :return: {
        'templateArn': 'string',
        'templateName': 'string',
        'versionId': 123,
        'isDefaultVersion': True|False
    }
    
    
    :returns: 
    IoT.Client.exceptions.VersionsLimitExceededException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ConflictingResourceUpdateException
    
    """
    pass

def create_role_alias(roleAlias=None, roleArn=None, credentialDurationSeconds=None, tags=None):
    """
    Creates a role alias.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_role_alias(
        roleAlias='string',
        roleArn='string',
        credentialDurationSeconds=123,
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type roleAlias: string
    :param roleAlias: [REQUIRED]\nThe role alias that points to a role ARN. This allows you to change the role without having to update the device.\n

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe role ARN.\n

    :type credentialDurationSeconds: integer
    :param credentialDurationSeconds: How long (in seconds) the credentials will be valid.

    :type tags: list
    :param tags: Metadata which can be used to manage the role alias.\n\nNote\nFor URI Request parameters use format: ...key1=value1&key2=value2...\nFor the CLI command-line parameter use format: &&tags 'key1=value1&key2=value2...'\nFor the cli-input-json file use format: 'tags': 'key1=value1&key2=value2...'\n\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'roleAlias': 'string',
    'roleAliasArn': 'string'
}


Response Structure

(dict) --

roleAlias (string) --
The role alias.

roleAliasArn (string) --
The role alias ARN.







Exceptions

IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'roleAlias': 'string',
        'roleAliasArn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def create_scheduled_audit(frequency=None, dayOfMonth=None, dayOfWeek=None, targetCheckNames=None, scheduledAuditName=None, tags=None):
    """
    Creates a scheduled audit that is run at a specified time interval.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_scheduled_audit(
        frequency='DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
        dayOfMonth='string',
        dayOfWeek='SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT',
        targetCheckNames=[
            'string',
        ],
        scheduledAuditName='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type frequency: string
    :param frequency: [REQUIRED]\nHow often the scheduled audit takes place. Can be one of 'DAILY', 'WEEKLY', 'BIWEEKLY' or 'MONTHLY'. The start time of each audit is determined by the system.\n

    :type dayOfMonth: string
    :param dayOfMonth: The day of the month on which the scheduled audit takes place. Can be '1' through '31' or 'LAST'. This field is required if the 'frequency' parameter is set to 'MONTHLY'. If days 29-31 are specified, and the month does not have that many days, the audit takes place on the 'LAST' day of the month.

    :type dayOfWeek: string
    :param dayOfWeek: The day of the week on which the scheduled audit takes place. Can be one of 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', or 'SAT'. This field is required if the 'frequency' parameter is set to 'WEEKLY' or 'BIWEEKLY'.

    :type targetCheckNames: list
    :param targetCheckNames: [REQUIRED]\nWhich checks are performed during the scheduled audit. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)\n\n(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)\n\n\n

    :type scheduledAuditName: string
    :param scheduledAuditName: [REQUIRED]\nThe name you want to give to the scheduled audit. (Max. 128 chars)\n

    :type tags: list
    :param tags: Metadata that can be used to manage the scheduled audit.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'scheduledAuditArn': 'string'
}


Response Structure

(dict) --

scheduledAuditArn (string) --
The ARN of the scheduled audit.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.LimitExceededException


    :return: {
        'scheduledAuditArn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.LimitExceededException
    
    """
    pass

def create_security_profile(securityProfileName=None, securityProfileDescription=None, behaviors=None, alertTargets=None, additionalMetricsToRetain=None, additionalMetricsToRetainV2=None, tags=None):
    """
    Creates a Device Defender security profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_security_profile(
        securityProfileName='string',
        securityProfileDescription='string',
        behaviors=[
            {
                'name': 'string',
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                },
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123,
                    'consecutiveDatapointsToAlarm': 123,
                    'consecutiveDatapointsToClear': 123,
                    'statisticalThreshold': {
                        'statistic': 'string'
                    }
                }
            },
        ],
        alertTargets={
            'string': {
                'alertTargetArn': 'string',
                'roleArn': 'string'
            }
        },
        additionalMetricsToRetain=[
            'string',
        ],
        additionalMetricsToRetainV2=[
            {
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                }
            },
        ],
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]\nThe name you are giving to the security profile.\n

    :type securityProfileDescription: string
    :param securityProfileDescription: A description of the security profile.

    :type behaviors: list
    :param behaviors: Specifies the behaviors that, when violated by a device (thing), cause an alert.\n\n(dict) --A Device Defender security profile behavior.\n\nname (string) -- [REQUIRED]The name you have given to the behavior.\n\nmetric (string) --What is measured by the behavior.\n\nmetricDimension (dict) --The dimension for a metric in your behavior. For example, using a TOPIC_FILTER dimension, you can narrow down the scope of the metric only to MQTT topics whose name match the pattern specified in the dimension.\n\ndimensionName (string) -- [REQUIRED]A unique identifier for the dimension.\n\noperator (string) --Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .\n\n\n\ncriteria (dict) --The criteria that determine if a device is behaving normally in regard to the metric .\n\ncomparisonOperator (string) --The operator that relates the thing measured (metric ) to the criteria (containing a value or statisticalThreshold ).\n\nvalue (dict) --The value to be compared with the metric .\n\ncount (integer) --If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .\n\ncidrs (list) --If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .\n\n(string) --\n\n\nports (list) --If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .\n\n(integer) --\n\n\n\n\ndurationSeconds (integer) --Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ). For a statisticalThreshhold metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.\n\nconsecutiveDatapointsToAlarm (integer) --If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.\n\nconsecutiveDatapointsToClear (integer) --If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.\n\nstatisticalThreshold (dict) --A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.\n\nstatistic (string) --The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (durationSeconds ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (comparisonOperator ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.\n\n\n\n\n\n\n\n\n

    :type alertTargets: dict
    :param alertTargets: Specifies the destinations to which alerts are sent. (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.\n\n(string) --The type of alert target: one of 'SNS'.\n\n(dict) --A structure containing the alert target ARN and the role ARN.\n\nalertTargetArn (string) -- [REQUIRED]The ARN of the notification target to which alerts are sent.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants permission to send alerts to the notification target.\n\n\n\n\n\n\n

    :type additionalMetricsToRetain: list
    :param additionalMetricsToRetain: A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile\'s behaviors , but it is also retained for any metric specified here.\n\nNote: This API field is deprecated. Please use CreateSecurityProfileRequest$additionalMetricsToRetainV2 instead.\n\n(string) --\n\n

    :type additionalMetricsToRetainV2: list
    :param additionalMetricsToRetainV2: A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile\'s behaviors , but it is also retained for any metric specified here.\n\n(dict) --The metric you want to retain. Dimensions are optional.\n\nmetric (string) -- [REQUIRED]What is measured by the behavior.\n\nmetricDimension (dict) --The dimension of a metric.\n\ndimensionName (string) -- [REQUIRED]A unique identifier for the dimension.\n\noperator (string) --Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .\n\n\n\n\n\n\n

    :type tags: list
    :param tags: Metadata that can be used to manage the security profile.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'securityProfileName': 'string',
    'securityProfileArn': 'string'
}


Response Structure

(dict) --

securityProfileName (string) --
The name you gave to the security profile.

securityProfileArn (string) --
The ARN of the security profile.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'securityProfileName': 'string',
        'securityProfileArn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def create_stream(streamId=None, description=None, files=None, roleArn=None, tags=None):
    """
    Creates a stream for delivering one or more large files in chunks over MQTT. A stream transports data bytes in chunks or blocks packaged as MQTT messages from a source like S3. You can have one or more files associated with a stream.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_stream(
        streamId='string',
        description='string',
        files=[
            {
                'fileId': 123,
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'version': 'string'
                }
            },
        ],
        roleArn='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type streamId: string
    :param streamId: [REQUIRED]\nThe stream ID.\n

    :type description: string
    :param description: A description of the stream.

    :type files: list
    :param files: [REQUIRED]\nThe files to stream.\n\n(dict) --Represents a file to stream.\n\nfileId (integer) --The file ID.\n\ns3Location (dict) --The location of the file in S3.\n\nbucket (string) --The S3 bucket.\n\nkey (string) --The S3 key.\n\nversion (string) --The S3 bucket version.\n\n\n\n\n\n\n

    :type roleArn: string
    :param roleArn: [REQUIRED]\nAn IAM role that allows the IoT service principal assumes to access your S3 files.\n

    :type tags: list
    :param tags: Metadata which can be used to manage streams.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'streamId': 'string',
    'streamArn': 'string',
    'description': 'string',
    'streamVersion': 123
}


Response Structure

(dict) --

streamId (string) --
The stream ID.

streamArn (string) --
The stream ARN.

description (string) --
A description of the stream.

streamVersion (integer) --
The version of the stream.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'streamId': 'string',
        'streamArn': 'string',
        'description': 'string',
        'streamVersion': 123
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def create_thing(thingName=None, thingTypeName=None, attributePayload=None, billingGroupName=None):
    """
    Creates a thing record in the registry. If this call is made multiple times using the same thing name and configuration, the call will succeed. If this call is made with the same thing name but different configuration a ResourceAlreadyExistsException is thrown.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_thing(
        thingName='string',
        thingTypeName='string',
        attributePayload={
            'attributes': {
                'string': 'string'
            },
            'merge': True|False
        },
        billingGroupName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing to create.\nYou can\'t change a thing\'s name after you create it. To change a thing\'s name, you must create a new thing, give it the new name, and then delete the old thing.\n

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type associated with the new thing.

    :type attributePayload: dict
    :param attributePayload: The attribute payload, which consists of up to three name/value pairs in a JSON document. For example:\n\n{\\'attributes\\':{\\'string1\\':\\'string2\\'}}\n\nattributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:\n\n{\\'attributes\\':{\\'string1\\':\\'string2\\'}}\n\n(string) --\n(string) --\n\n\n\n\nmerge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.\nTo remove an attribute, call UpdateThing with an empty attribute value.\n\nNote\nThe merge attribute is only valid when calling UpdateThing or UpdateThingGroup .\n\n\n\n

    :type billingGroupName: string
    :param billingGroupName: The name of the billing group the thing will be added to.

    :rtype: dict

ReturnsResponse Syntax
{
    'thingName': 'string',
    'thingArn': 'string',
    'thingId': 'string'
}


Response Structure

(dict) --
The output of the CreateThing operation.

thingName (string) --
The name of the new thing.

thingArn (string) --
The ARN of the new thing.

thingId (string) --
The thing ID.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'thingName': 'string',
        'thingArn': 'string',
        'thingId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_thing_group(thingGroupName=None, parentGroupName=None, thingGroupProperties=None, tags=None):
    """
    Create a thing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_thing_group(
        thingGroupName='string',
        parentGroupName='string',
        thingGroupProperties={
            'thingGroupDescription': 'string',
            'attributePayload': {
                'attributes': {
                    'string': 'string'
                },
                'merge': True|False
            }
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]\nThe thing group name to create.\n

    :type parentGroupName: string
    :param parentGroupName: The name of the parent thing group.

    :type thingGroupProperties: dict
    :param thingGroupProperties: The thing group properties.\n\nthingGroupDescription (string) --The thing group description.\n\nattributePayload (dict) --The thing group attributes in JSON format.\n\nattributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:\n\n{\\'attributes\\':{\\'string1\\':\\'string2\\'}}\n\n(string) --\n(string) --\n\n\n\n\nmerge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.\nTo remove an attribute, call UpdateThing with an empty attribute value.\n\nNote\nThe merge attribute is only valid when calling UpdateThing or UpdateThingGroup .\n\n\n\n\n\n

    :type tags: list
    :param tags: Metadata which can be used to manage the thing group.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'thingGroupName': 'string',
    'thingGroupArn': 'string',
    'thingGroupId': 'string'
}


Response Structure

(dict) --

thingGroupName (string) --
The thing group name.

thingGroupArn (string) --
The thing group ARN.

thingGroupId (string) --
The thing group ID.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'thingGroupName': 'string',
        'thingGroupArn': 'string',
        'thingGroupId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def create_thing_type(thingTypeName=None, thingTypeProperties=None, tags=None):
    """
    Creates a new thing type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_thing_type(
        thingTypeName='string',
        thingTypeProperties={
            'thingTypeDescription': 'string',
            'searchableAttributes': [
                'string',
            ]
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]\nThe name of the thing type.\n

    :type thingTypeProperties: dict
    :param thingTypeProperties: The ThingTypeProperties for the thing type to create. It contains information about the new thing type including a description, and a list of searchable thing attribute names.\n\nthingTypeDescription (string) --The description of the thing type.\n\nsearchableAttributes (list) --A list of searchable thing attribute names.\n\n(string) --\n\n\n\n

    :type tags: list
    :param tags: Metadata which can be used to manage the thing type.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'thingTypeName': 'string',
    'thingTypeArn': 'string',
    'thingTypeId': 'string'
}


Response Structure

(dict) --
The output of the CreateThingType operation.

thingTypeName (string) --
The name of the thing type.

thingTypeArn (string) --
The Amazon Resource Name (ARN) of the thing type.

thingTypeId (string) --
The thing type ID.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceAlreadyExistsException


    :return: {
        'thingTypeName': 'string',
        'thingTypeArn': 'string',
        'thingTypeId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    
    """
    pass

def create_topic_rule(ruleName=None, topicRulePayload=None, tags=None):
    """
    Creates a rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_topic_rule(
        ruleName='string',
        topicRulePayload={
            'sql': 'string',
            'description': 'string',
            'actions': [
                {
                    'dynamoDB': {
                        'tableName': 'string',
                        'roleArn': 'string',
                        'operation': 'string',
                        'hashKeyField': 'string',
                        'hashKeyValue': 'string',
                        'hashKeyType': 'STRING'|'NUMBER',
                        'rangeKeyField': 'string',
                        'rangeKeyValue': 'string',
                        'rangeKeyType': 'STRING'|'NUMBER',
                        'payloadField': 'string'
                    },
                    'dynamoDBv2': {
                        'roleArn': 'string',
                        'putItem': {
                            'tableName': 'string'
                        }
                    },
                    'lambda': {
                        'functionArn': 'string'
                    },
                    'sns': {
                        'targetArn': 'string',
                        'roleArn': 'string',
                        'messageFormat': 'RAW'|'JSON'
                    },
                    'sqs': {
                        'roleArn': 'string',
                        'queueUrl': 'string',
                        'useBase64': True|False
                    },
                    'kinesis': {
                        'roleArn': 'string',
                        'streamName': 'string',
                        'partitionKey': 'string'
                    },
                    'republish': {
                        'roleArn': 'string',
                        'topic': 'string',
                        'qos': 123
                    },
                    's3': {
                        'roleArn': 'string',
                        'bucketName': 'string',
                        'key': 'string',
                        'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                    },
                    'firehose': {
                        'roleArn': 'string',
                        'deliveryStreamName': 'string',
                        'separator': 'string'
                    },
                    'cloudwatchMetric': {
                        'roleArn': 'string',
                        'metricNamespace': 'string',
                        'metricName': 'string',
                        'metricValue': 'string',
                        'metricUnit': 'string',
                        'metricTimestamp': 'string'
                    },
                    'cloudwatchAlarm': {
                        'roleArn': 'string',
                        'alarmName': 'string',
                        'stateReason': 'string',
                        'stateValue': 'string'
                    },
                    'cloudwatchLogs': {
                        'roleArn': 'string',
                        'logGroupName': 'string'
                    },
                    'elasticsearch': {
                        'roleArn': 'string',
                        'endpoint': 'string',
                        'index': 'string',
                        'type': 'string',
                        'id': 'string'
                    },
                    'salesforce': {
                        'token': 'string',
                        'url': 'string'
                    },
                    'iotAnalytics': {
                        'channelArn': 'string',
                        'channelName': 'string',
                        'roleArn': 'string'
                    },
                    'iotEvents': {
                        'inputName': 'string',
                        'messageId': 'string',
                        'roleArn': 'string'
                    },
                    'iotSiteWise': {
                        'putAssetPropertyValueEntries': [
                            {
                                'entryId': 'string',
                                'assetId': 'string',
                                'propertyId': 'string',
                                'propertyAlias': 'string',
                                'propertyValues': [
                                    {
                                        'value': {
                                            'stringValue': 'string',
                                            'integerValue': 'string',
                                            'doubleValue': 'string',
                                            'booleanValue': 'string'
                                        },
                                        'timestamp': {
                                            'timeInSeconds': 'string',
                                            'offsetInNanos': 'string'
                                        },
                                        'quality': 'string'
                                    },
                                ]
                            },
                        ],
                        'roleArn': 'string'
                    },
                    'stepFunctions': {
                        'executionNamePrefix': 'string',
                        'stateMachineName': 'string',
                        'roleArn': 'string'
                    },
                    'http': {
                        'url': 'string',
                        'confirmationUrl': 'string',
                        'headers': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'auth': {
                            'sigv4': {
                                'signingRegion': 'string',
                                'serviceName': 'string',
                                'roleArn': 'string'
                            }
                        }
                    }
                },
            ],
            'ruleDisabled': True|False,
            'awsIotSqlVersion': 'string',
            'errorAction': {
                'dynamoDB': {
                    'tableName': 'string',
                    'roleArn': 'string',
                    'operation': 'string',
                    'hashKeyField': 'string',
                    'hashKeyValue': 'string',
                    'hashKeyType': 'STRING'|'NUMBER',
                    'rangeKeyField': 'string',
                    'rangeKeyValue': 'string',
                    'rangeKeyType': 'STRING'|'NUMBER',
                    'payloadField': 'string'
                },
                'dynamoDBv2': {
                    'roleArn': 'string',
                    'putItem': {
                        'tableName': 'string'
                    }
                },
                'lambda': {
                    'functionArn': 'string'
                },
                'sns': {
                    'targetArn': 'string',
                    'roleArn': 'string',
                    'messageFormat': 'RAW'|'JSON'
                },
                'sqs': {
                    'roleArn': 'string',
                    'queueUrl': 'string',
                    'useBase64': True|False
                },
                'kinesis': {
                    'roleArn': 'string',
                    'streamName': 'string',
                    'partitionKey': 'string'
                },
                'republish': {
                    'roleArn': 'string',
                    'topic': 'string',
                    'qos': 123
                },
                's3': {
                    'roleArn': 'string',
                    'bucketName': 'string',
                    'key': 'string',
                    'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                },
                'firehose': {
                    'roleArn': 'string',
                    'deliveryStreamName': 'string',
                    'separator': 'string'
                },
                'cloudwatchMetric': {
                    'roleArn': 'string',
                    'metricNamespace': 'string',
                    'metricName': 'string',
                    'metricValue': 'string',
                    'metricUnit': 'string',
                    'metricTimestamp': 'string'
                },
                'cloudwatchAlarm': {
                    'roleArn': 'string',
                    'alarmName': 'string',
                    'stateReason': 'string',
                    'stateValue': 'string'
                },
                'cloudwatchLogs': {
                    'roleArn': 'string',
                    'logGroupName': 'string'
                },
                'elasticsearch': {
                    'roleArn': 'string',
                    'endpoint': 'string',
                    'index': 'string',
                    'type': 'string',
                    'id': 'string'
                },
                'salesforce': {
                    'token': 'string',
                    'url': 'string'
                },
                'iotAnalytics': {
                    'channelArn': 'string',
                    'channelName': 'string',
                    'roleArn': 'string'
                },
                'iotEvents': {
                    'inputName': 'string',
                    'messageId': 'string',
                    'roleArn': 'string'
                },
                'iotSiteWise': {
                    'putAssetPropertyValueEntries': [
                        {
                            'entryId': 'string',
                            'assetId': 'string',
                            'propertyId': 'string',
                            'propertyAlias': 'string',
                            'propertyValues': [
                                {
                                    'value': {
                                        'stringValue': 'string',
                                        'integerValue': 'string',
                                        'doubleValue': 'string',
                                        'booleanValue': 'string'
                                    },
                                    'timestamp': {
                                        'timeInSeconds': 'string',
                                        'offsetInNanos': 'string'
                                    },
                                    'quality': 'string'
                                },
                            ]
                        },
                    ],
                    'roleArn': 'string'
                },
                'stepFunctions': {
                    'executionNamePrefix': 'string',
                    'stateMachineName': 'string',
                    'roleArn': 'string'
                },
                'http': {
                    'url': 'string',
                    'confirmationUrl': 'string',
                    'headers': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'auth': {
                        'sigv4': {
                            'signingRegion': 'string',
                            'serviceName': 'string',
                            'roleArn': 'string'
                        }
                    }
                }
            }
        },
        tags='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]\nThe name of the rule.\n

    :type topicRulePayload: dict
    :param topicRulePayload: [REQUIRED]\nThe rule payload.\n\nsql (string) -- [REQUIRED]The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference in the AWS IoT Developer Guide .\n\ndescription (string) --The description of the rule.\n\nactions (list) -- [REQUIRED]The actions associated with the rule.\n\n(dict) --Describes the actions associated with a rule.\n\ndynamoDB (dict) --Write to a DynamoDB table.\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.\n\noperation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .\n\nhashKeyField (string) -- [REQUIRED]The hash key name.\n\nhashKeyValue (string) -- [REQUIRED]The hash key value.\n\nhashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'\n\nrangeKeyField (string) --The range key name.\n\nrangeKeyValue (string) --The range key value.\n\nrangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'\n\npayloadField (string) --The action payload. This name can be customized.\n\n\n\ndynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.\n\nputItem (dict) -- [REQUIRED]Specifies the DynamoDB table to which the message data will be written. For example:\n\n{ 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }\nEach attribute in the message payload will be written to a separate column in the DynamoDB database.\n\ntableName (string) -- [REQUIRED]The table where the message data will be written.\n\n\n\n\n\nlambda (dict) --Invoke a Lambda function.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function.\n\n\n\nsns (dict) --Publish to an Amazon SNS topic.\n\ntargetArn (string) -- [REQUIRED]The ARN of the SNS topic.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nmessageFormat (string) --(Optional) The message format of the message to publish. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see https://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.\n\n\n\nsqs (dict) --Publish to an Amazon SQS queue.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nqueueUrl (string) -- [REQUIRED]The URL of the Amazon SQS queue.\n\nuseBase64 (boolean) --Specifies whether to use Base64 encoding.\n\n\n\nkinesis (dict) --Write data to an Amazon Kinesis stream.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the Amazon Kinesis stream.\n\nstreamName (string) -- [REQUIRED]The name of the Amazon Kinesis stream.\n\npartitionKey (string) --The partition key.\n\n\n\nrepublish (dict) --Publish to another MQTT topic.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\ntopic (string) -- [REQUIRED]The name of the MQTT topic.\n\nqos (integer) --The Quality of Service (QoS) level to use when republishing messages. The default value is 0.\n\n\n\ns3 (dict) --Write to an Amazon S3 bucket.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nbucketName (string) -- [REQUIRED]The Amazon S3 bucket.\n\nkey (string) -- [REQUIRED]The object key.\n\ncannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .\n\n\n\nfirehose (dict) --Write to an Amazon Kinesis Firehose stream.\n\nroleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehose stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The delivery stream name.\n\nseparator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\n\n\ncloudwatchMetric (dict) --Capture a CloudWatch metric.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch metric.\n\nmetricNamespace (string) -- [REQUIRED]The CloudWatch metric namespace name.\n\nmetricName (string) -- [REQUIRED]The CloudWatch metric name.\n\nmetricValue (string) -- [REQUIRED]The CloudWatch metric value.\n\nmetricUnit (string) -- [REQUIRED]The metric unit supported by CloudWatch.\n\nmetricTimestamp (string) --An optional Unix timestamp .\n\n\n\ncloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch alarm.\n\nalarmName (string) -- [REQUIRED]The CloudWatch alarm name.\n\nstateReason (string) -- [REQUIRED]The reason for the alarm change.\n\nstateValue (string) -- [REQUIRED]The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.\n\n\n\ncloudwatchLogs (dict) --Send data to CloudWatch Logs.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch log.\n\nlogGroupName (string) -- [REQUIRED]The CloudWatch log group to which the action sends data.\n\n\n\nelasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.\n\nroleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.\n\nendpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.\n\nindex (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.\n\ntype (string) -- [REQUIRED]The type of document you are storing.\n\nid (string) -- [REQUIRED]The unique identifier for the document you are storing.\n\n\n\nsalesforce (dict) --Send a message to a Salesforce IoT Cloud Input Stream.\n\ntoken (string) -- [REQUIRED]The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.\n\nurl (string) -- [REQUIRED]The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.\n\n\n\niotAnalytics (dict) --Sends message data to an AWS IoT Analytics channel.\n\nchannelArn (string) --(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.\n\nchannelName (string) --The name of the IoT Analytics channel to which message data will be sent.\n\nroleArn (string) --The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).\n\n\n\niotEvents (dict) --Sends an input to an AWS IoT Events detector.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input.\n\nmessageId (string) --[Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ('Action':'iotevents:BatchPutMessage').\n\n\n\niotSiteWise (dict) --Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.\n\nputAssetPropertyValueEntries (list) -- [REQUIRED]A list of asset property value entries.\n\n(dict) --An asset property value entry containing the following information.\n\nentryId (string) --Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.\n\nassetId (string) --The ID of the AWS IoT SiteWise asset. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyId (string) --The ID of the asset\'s property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyAlias (string) --The name of the property alias associated with your asset property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyValues (list) -- [REQUIRED]A list of property values to insert that each contain timestamp, quality, and value (TQV) information.\n\n(dict) --An asset property value entry containing the following information.\n\nvalue (dict) -- [REQUIRED]The value of the asset property.\n\nstringValue (string) --Optional. The string value of the value entry. Accepts substitution templates.\n\nintegerValue (string) --Optional. A string that contains the integer value of the value entry. Accepts substitution templates.\n\ndoubleValue (string) --Optional. A string that contains the double value of the value entry. Accepts substitution templates.\n\nbooleanValue (string) --Optional. A string that contains the boolean value (true or false ) of the value entry. Accepts substitution templates.\n\n\n\ntimestamp (dict) -- [REQUIRED]The asset property value timestamp.\n\ntimeInSeconds (string) -- [REQUIRED]A string that contains the time in seconds since epoch. Accepts substitution templates.\n\noffsetInNanos (string) --Optional. A string that contains the nanosecond time offset. Accepts substitution templates.\n\n\n\nquality (string) --Optional. A string that describes the quality of the value. Accepts substitution templates. Must be GOOD , BAD , or UNCERTAIN .\n\n\n\n\n\n\n\n\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoTSiteWise. ('Action': 'iotsitewise:BatchPutAssetPropertyValue' ). The trust policy can restrict access to specific asset hierarchy paths.\n\n\n\nstepFunctions (dict) --Starts execution of a Step Functions state machine.\n\nexecutionNamePrefix (string) --(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.\n\nstateMachineName (string) -- [REQUIRED]The name of the Step Functions state machine whose execution will be started.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants IoT permission to start execution of a state machine ('Action':'states:StartExecution').\n\n\n\nhttp (dict) --Send data to an HTTPS endpoint.\n\nurl (string) -- [REQUIRED]The endpoint URL. If substitution templates are used in the URL, you must also specify a confirmationUrl . If this is a new destination, a new TopicRuleDestination is created if possible.\n\nconfirmationUrl (string) --The URL to which AWS IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.\n\nheaders (list) --The HTTP headers to send with the message data.\n\n(dict) --The HTTP action header.\n\nkey (string) -- [REQUIRED]The HTTP header key.\n\nvalue (string) -- [REQUIRED]The HTTP header value. Substitution templates are supported.\n\n\n\n\n\nauth (dict) --The authentication method to use when sending data to an HTTPS endpoint.\n\nsigv4 (dict) --Use Sig V4 authorization. For more information, see Signature Version 4 Signing Process .\n\nsigningRegion (string) -- [REQUIRED]The signing region.\n\nserviceName (string) -- [REQUIRED]The service name to use while signing with Sig V4.\n\nroleArn (string) -- [REQUIRED]The ARN of the signing role.\n\n\n\n\n\n\n\n\n\n\n\nruleDisabled (boolean) --Specifies whether the rule is disabled.\n\nawsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.\n\nerrorAction (dict) --The action to take when an error occurs.\n\ndynamoDB (dict) --Write to a DynamoDB table.\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.\n\noperation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .\n\nhashKeyField (string) -- [REQUIRED]The hash key name.\n\nhashKeyValue (string) -- [REQUIRED]The hash key value.\n\nhashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'\n\nrangeKeyField (string) --The range key name.\n\nrangeKeyValue (string) --The range key value.\n\nrangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'\n\npayloadField (string) --The action payload. This name can be customized.\n\n\n\ndynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.\n\nputItem (dict) -- [REQUIRED]Specifies the DynamoDB table to which the message data will be written. For example:\n\n{ 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }\nEach attribute in the message payload will be written to a separate column in the DynamoDB database.\n\ntableName (string) -- [REQUIRED]The table where the message data will be written.\n\n\n\n\n\nlambda (dict) --Invoke a Lambda function.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function.\n\n\n\nsns (dict) --Publish to an Amazon SNS topic.\n\ntargetArn (string) -- [REQUIRED]The ARN of the SNS topic.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nmessageFormat (string) --(Optional) The message format of the message to publish. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see https://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.\n\n\n\nsqs (dict) --Publish to an Amazon SQS queue.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nqueueUrl (string) -- [REQUIRED]The URL of the Amazon SQS queue.\n\nuseBase64 (boolean) --Specifies whether to use Base64 encoding.\n\n\n\nkinesis (dict) --Write data to an Amazon Kinesis stream.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the Amazon Kinesis stream.\n\nstreamName (string) -- [REQUIRED]The name of the Amazon Kinesis stream.\n\npartitionKey (string) --The partition key.\n\n\n\nrepublish (dict) --Publish to another MQTT topic.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\ntopic (string) -- [REQUIRED]The name of the MQTT topic.\n\nqos (integer) --The Quality of Service (QoS) level to use when republishing messages. The default value is 0.\n\n\n\ns3 (dict) --Write to an Amazon S3 bucket.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nbucketName (string) -- [REQUIRED]The Amazon S3 bucket.\n\nkey (string) -- [REQUIRED]The object key.\n\ncannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .\n\n\n\nfirehose (dict) --Write to an Amazon Kinesis Firehose stream.\n\nroleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehose stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The delivery stream name.\n\nseparator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\n\n\ncloudwatchMetric (dict) --Capture a CloudWatch metric.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch metric.\n\nmetricNamespace (string) -- [REQUIRED]The CloudWatch metric namespace name.\n\nmetricName (string) -- [REQUIRED]The CloudWatch metric name.\n\nmetricValue (string) -- [REQUIRED]The CloudWatch metric value.\n\nmetricUnit (string) -- [REQUIRED]The metric unit supported by CloudWatch.\n\nmetricTimestamp (string) --An optional Unix timestamp .\n\n\n\ncloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch alarm.\n\nalarmName (string) -- [REQUIRED]The CloudWatch alarm name.\n\nstateReason (string) -- [REQUIRED]The reason for the alarm change.\n\nstateValue (string) -- [REQUIRED]The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.\n\n\n\ncloudwatchLogs (dict) --Send data to CloudWatch Logs.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch log.\n\nlogGroupName (string) -- [REQUIRED]The CloudWatch log group to which the action sends data.\n\n\n\nelasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.\n\nroleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.\n\nendpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.\n\nindex (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.\n\ntype (string) -- [REQUIRED]The type of document you are storing.\n\nid (string) -- [REQUIRED]The unique identifier for the document you are storing.\n\n\n\nsalesforce (dict) --Send a message to a Salesforce IoT Cloud Input Stream.\n\ntoken (string) -- [REQUIRED]The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.\n\nurl (string) -- [REQUIRED]The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.\n\n\n\niotAnalytics (dict) --Sends message data to an AWS IoT Analytics channel.\n\nchannelArn (string) --(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.\n\nchannelName (string) --The name of the IoT Analytics channel to which message data will be sent.\n\nroleArn (string) --The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).\n\n\n\niotEvents (dict) --Sends an input to an AWS IoT Events detector.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input.\n\nmessageId (string) --[Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ('Action':'iotevents:BatchPutMessage').\n\n\n\niotSiteWise (dict) --Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.\n\nputAssetPropertyValueEntries (list) -- [REQUIRED]A list of asset property value entries.\n\n(dict) --An asset property value entry containing the following information.\n\nentryId (string) --Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.\n\nassetId (string) --The ID of the AWS IoT SiteWise asset. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyId (string) --The ID of the asset\'s property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyAlias (string) --The name of the property alias associated with your asset property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyValues (list) -- [REQUIRED]A list of property values to insert that each contain timestamp, quality, and value (TQV) information.\n\n(dict) --An asset property value entry containing the following information.\n\nvalue (dict) -- [REQUIRED]The value of the asset property.\n\nstringValue (string) --Optional. The string value of the value entry. Accepts substitution templates.\n\nintegerValue (string) --Optional. A string that contains the integer value of the value entry. Accepts substitution templates.\n\ndoubleValue (string) --Optional. A string that contains the double value of the value entry. Accepts substitution templates.\n\nbooleanValue (string) --Optional. A string that contains the boolean value (true or false ) of the value entry. Accepts substitution templates.\n\n\n\ntimestamp (dict) -- [REQUIRED]The asset property value timestamp.\n\ntimeInSeconds (string) -- [REQUIRED]A string that contains the time in seconds since epoch. Accepts substitution templates.\n\noffsetInNanos (string) --Optional. A string that contains the nanosecond time offset. Accepts substitution templates.\n\n\n\nquality (string) --Optional. A string that describes the quality of the value. Accepts substitution templates. Must be GOOD , BAD , or UNCERTAIN .\n\n\n\n\n\n\n\n\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoTSiteWise. ('Action': 'iotsitewise:BatchPutAssetPropertyValue' ). The trust policy can restrict access to specific asset hierarchy paths.\n\n\n\nstepFunctions (dict) --Starts execution of a Step Functions state machine.\n\nexecutionNamePrefix (string) --(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.\n\nstateMachineName (string) -- [REQUIRED]The name of the Step Functions state machine whose execution will be started.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants IoT permission to start execution of a state machine ('Action':'states:StartExecution').\n\n\n\nhttp (dict) --Send data to an HTTPS endpoint.\n\nurl (string) -- [REQUIRED]The endpoint URL. If substitution templates are used in the URL, you must also specify a confirmationUrl . If this is a new destination, a new TopicRuleDestination is created if possible.\n\nconfirmationUrl (string) --The URL to which AWS IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.\n\nheaders (list) --The HTTP headers to send with the message data.\n\n(dict) --The HTTP action header.\n\nkey (string) -- [REQUIRED]The HTTP header key.\n\nvalue (string) -- [REQUIRED]The HTTP header value. Substitution templates are supported.\n\n\n\n\n\nauth (dict) --The authentication method to use when sending data to an HTTPS endpoint.\n\nsigv4 (dict) --Use Sig V4 authorization. For more information, see Signature Version 4 Signing Process .\n\nsigningRegion (string) -- [REQUIRED]The signing region.\n\nserviceName (string) -- [REQUIRED]The service name to use while signing with Sig V4.\n\nroleArn (string) -- [REQUIRED]The ARN of the signing role.\n\n\n\n\n\n\n\n\n\n\n

    :type tags: string
    :param tags: Metadata which can be used to manage the topic rule.\n\nNote\nFor URI Request parameters use format: ...key1=value1&key2=value2...\nFor the CLI command-line parameter use format: --tags 'key1=value1&key2=value2...'\nFor the cli-input-json file use format: 'tags': 'key1=value1&key2=value2...'\n\n

    :returns: 
    IoT.Client.exceptions.SqlParseException
    IoT.Client.exceptions.InternalException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.ConflictingResourceUpdateException
    
    """
    pass

def create_topic_rule_destination(destinationConfiguration=None):
    """
    Creates a topic rule destination. The destination must be confirmed prior to use.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_topic_rule_destination(
        destinationConfiguration={
            'httpUrlConfiguration': {
                'confirmationUrl': 'string'
            }
        }
    )
    
    
    :type destinationConfiguration: dict
    :param destinationConfiguration: [REQUIRED]\nThe topic rule destination configuration.\n\nhttpUrlConfiguration (dict) --Configuration of the HTTP URL.\n\nconfirmationUrl (string) -- [REQUIRED]The URL AWS IoT uses to confirm ownership of or access to the topic rule destination URL.\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'topicRuleDestination': {
        'arn': 'string',
        'status': 'ENABLED'|'IN_PROGRESS'|'DISABLED'|'ERROR',
        'statusReason': 'string',
        'httpUrlProperties': {
            'confirmationUrl': 'string'
        }
    }
}


Response Structure

(dict) --
topicRuleDestination (dict) --The topic rule destination.

arn (string) --The topic rule destination URL.

status (string) --The status of the topic rule destination. Valid values are:

IN_PROGRESS
A topic rule destination was created but has not been confirmed. You can set status to IN_PROGRESS by calling UpdateTopicRuleDestination . Calling UpdateTopicRuleDestination causes a new confirmation challenge to be sent to your confirmation endpoint.

ENABLED
Confirmation was completed, and traffic to this destination is allowed. You can set status to DISABLED by calling UpdateTopicRuleDestination .

DISABLED
Confirmation was completed, and traffic to this destination is not allowed. You can set status to ENABLED by calling UpdateTopicRuleDestination .

ERROR
Confirmation could not be completed, for example if the confirmation timed out. You can call GetTopicRuleDestination for details about the error. You can set status to IN_PROGRESS by calling UpdateTopicRuleDestination . Calling UpdateTopicRuleDestination causes a new confirmation challenge to be sent to your confirmation endpoint.

statusReason (string) --Additional details or reason why the topic rule destination is in the current status.

httpUrlProperties (dict) --Properties of the HTTP URL.

confirmationUrl (string) --The URL used to confirm the HTTP topic rule destination URL.










Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.ConflictingResourceUpdateException


    :return: {
        'topicRuleDestination': {
            'arn': 'string',
            'status': 'ENABLED'|'IN_PROGRESS'|'DISABLED'|'ERROR',
            'statusReason': 'string',
            'httpUrlProperties': {
                'confirmationUrl': 'string'
            }
        }
    }
    
    
    """
    pass

def delete_account_audit_configuration(deleteScheduledAudits=None):
    """
    Restores the default settings for Device Defender audits for this account. Any configuration data you entered is deleted and all audit checks are reset to disabled.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_account_audit_configuration(
        deleteScheduledAudits=True|False
    )
    
    
    :type deleteScheduledAudits: boolean
    :param deleteScheduledAudits: If true, all scheduled audits are deleted.

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_authorizer(authorizerName=None):
    """
    Deletes an authorizer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_authorizer(
        authorizerName='string'
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]\nThe name of the authorizer to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.DeleteConflictException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.DeleteConflictException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_billing_group(billingGroupName=None, expectedVersion=None):
    """
    Deletes the billing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_billing_group(
        billingGroupName='string',
        expectedVersion=123
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: [REQUIRED]\nThe name of the billing group.\n

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the billing group. If the version of the billing group does not match the expected version specified in the request, the DeleteBillingGroup request is rejected with a VersionConflictException .

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.VersionConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_ca_certificate(certificateId=None):
    """
    Deletes a registered CA certificate.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_ca_certificate(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]\nThe ID of the certificate to delete. (The last part of the certificate ARN contains the certificate ID.)\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The output for the DeleteCACertificate operation.




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.CertificateStateException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    """
    pass

def delete_certificate(certificateId=None, forceDelete=None):
    """
    Deletes the specified certificate.
    A certificate cannot be deleted if it has a policy or IoT thing attached to it or if its status is set to ACTIVE. To delete a certificate, first use the  DetachPrincipalPolicy API to detach all policies. Next, use the  UpdateCertificate API to set the certificate to the INACTIVE status.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_certificate(
        certificateId='string',
        forceDelete=True|False
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]\nThe ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)\n

    :type forceDelete: boolean
    :param forceDelete: Forces the deletion of a certificate if it is inactive and is not attached to an IoT thing.

    :returns: 
    IoT.Client.exceptions.CertificateStateException
    IoT.Client.exceptions.DeleteConflictException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def delete_dimension(name=None):
    """
    Removes the specified dimension from your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_dimension(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe unique identifier for the dimension that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    
    """
    pass

def delete_domain_configuration(domainConfigurationName=None):
    """
    Deletes the specified domain configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_domain_configuration(
        domainConfigurationName='string'
    )
    
    
    :type domainConfigurationName: string
    :param domainConfigurationName: [REQUIRED]\nThe name of the domain configuration to be deleted.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    
    """
    pass

def delete_dynamic_thing_group(thingGroupName=None, expectedVersion=None):
    """
    Deletes a dynamic thing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_dynamic_thing_group(
        thingGroupName='string',
        expectedVersion=123
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]\nThe name of the dynamic thing group to delete.\n

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the dynamic thing group to delete.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.VersionConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_job(jobId=None, force=None):
    """
    Deletes a job and its related job executions.
    Deleting a job may take time, depending on the number of job executions created for the job and various other factors. While the job is being deleted, the status of the job will be shown as "DELETION_IN_PROGRESS". Attempting to delete or cancel a job whose status is already "DELETION_IN_PROGRESS" will result in an error.
    Only 10 jobs may have status "DELETION_IN_PROGRESS" at the same time, or a LimitExceededException will occur.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_job(
        jobId='string',
        force=True|False
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe ID of the job to be deleted.\nAfter a job deletion is completed, you may reuse this jobId when you create a new job. However, this is not recommended, and you must ensure that your devices are not using the jobId to refer to the deleted job.\n

    :type force: boolean
    :param force: (Optional) When true, you can delete a job which is 'IN_PROGRESS'. Otherwise, you can only delete a job which is in a terminal state ('COMPLETED' or 'CANCELED') or an exception will occur. The default is false.\n\nNote\nDeleting a job which is 'IN_PROGRESS', will cause a device which is executing the job to be unable to access job information or update the job execution status. Use caution and ensure that each device executing a job which is deleted is able to recover to a valid state.\n\n

    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.InvalidStateTransitionException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_job_execution(jobId=None, thingName=None, executionNumber=None, force=None):
    """
    Deletes a job execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_job_execution(
        jobId='string',
        thingName='string',
        executionNumber=123,
        force=True|False
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe ID of the job whose execution on a particular device will be deleted.\n

    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing whose job execution will be deleted.\n

    :type executionNumber: integer
    :param executionNumber: [REQUIRED]\nThe ID of the job execution to be deleted. The executionNumber refers to the execution of a particular job on a particular device.\nNote that once a job execution is deleted, the executionNumber may be reused by IoT, so be sure you get and use the correct value here.\n

    :type force: boolean
    :param force: (Optional) When true, you can delete a job execution which is 'IN_PROGRESS'. Otherwise, you can only delete a job execution which is in a terminal state ('SUCCEEDED', 'FAILED', 'REJECTED', 'REMOVED' or 'CANCELED') or an exception will occur. The default is false.\n\nNote\nDeleting a job execution which is 'IN_PROGRESS', will cause the device to be unable to access job information or update the job execution status. Use caution and ensure that the device is able to recover to a valid state.\n\n

    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.InvalidStateTransitionException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def delete_mitigation_action(actionName=None):
    """
    Deletes a defined mitigation action from your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_mitigation_action(
        actionName='string'
    )
    
    
    :type actionName: string
    :param actionName: [REQUIRED]\nThe name of the mitigation action that you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_ota_update(otaUpdateId=None, deleteStream=None, forceDeleteAWSJob=None):
    """
    Delete an OTA update.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_ota_update(
        otaUpdateId='string',
        deleteStream=True|False,
        forceDeleteAWSJob=True|False
    )
    
    
    :type otaUpdateId: string
    :param otaUpdateId: [REQUIRED]\nThe OTA update ID to delete.\n

    :type deleteStream: boolean
    :param deleteStream: Specifies if the stream associated with an OTA update should be deleted when the OTA update is deleted.

    :type forceDeleteAWSJob: boolean
    :param forceDeleteAWSJob: Specifies if the AWS Job associated with the OTA update should be deleted with the OTA update is deleted.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.VersionConflictException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_policy(policyName=None):
    """
    Deletes the specified policy.
    A policy cannot be deleted if it has non-default versions or it is attached to any certificate.
    To delete a policy, use the DeletePolicyVersion API to delete all non-default versions of the policy; use the DetachPrincipalPolicy API to detach the policy from any certificate; and then use the DeletePolicy API to delete the policy.
    When a policy is deleted using DeletePolicy, its default version is deleted with it.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_policy(
        policyName='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe name of the policy to delete.\n

    """
    pass

def delete_policy_version(policyName=None, policyVersionId=None):
    """
    Deletes the specified version of the specified policy. You cannot delete the default version of a policy using this API. To delete the default version of a policy, use  DeletePolicy . To find out which version of a policy is marked as the default version, use ListPolicyVersions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_policy_version(
        policyName='string',
        policyVersionId='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe name of the policy.\n

    :type policyVersionId: string
    :param policyVersionId: [REQUIRED]\nThe policy version ID.\n

    :returns: 
    IoT.Client.exceptions.DeleteConflictException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_provisioning_template(templateName=None):
    """
    Deletes a fleet provisioning template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_provisioning_template(
        templateName='string'
    )
    
    
    :type templateName: string
    :param templateName: [REQUIRED]\nThe name of the fleet provision template to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.DeleteConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.DeleteConflictException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    
    """
    pass

def delete_provisioning_template_version(templateName=None, versionId=None):
    """
    Deletes a fleet provisioning template version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_provisioning_template_version(
        templateName='string',
        versionId=123
    )
    
    
    :type templateName: string
    :param templateName: [REQUIRED]\nThe name of the fleet provisioning template version to delete.\n

    :type versionId: integer
    :param versionId: [REQUIRED]\nThe fleet provisioning template version ID to delete.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.DeleteConflictException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_registration_code():
    """
    Deletes a CA certificate registration code.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_registration_code()
    
    
    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The output for the DeleteRegistrationCode operation.




Exceptions

IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    """
    pass

def delete_role_alias(roleAlias=None):
    """
    Deletes a role alias
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_role_alias(
        roleAlias='string'
    )
    
    
    :type roleAlias: string
    :param roleAlias: [REQUIRED]\nThe role alias to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.DeleteConflictException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.DeleteConflictException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def delete_scheduled_audit(scheduledAuditName=None):
    """
    Deletes a scheduled audit.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_scheduled_audit(
        scheduledAuditName='string'
    )
    
    
    :type scheduledAuditName: string
    :param scheduledAuditName: [REQUIRED]\nThe name of the scheduled audit you want to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_security_profile(securityProfileName=None, expectedVersion=None):
    """
    Deletes a Device Defender security profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_security_profile(
        securityProfileName='string',
        expectedVersion=123
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]\nThe name of the security profile to be deleted.\n

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the security profile. A new version is generated whenever the security profile is updated. If you specify a value that is different from the actual version, a VersionConflictException is thrown.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.VersionConflictException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_stream(streamId=None):
    """
    Deletes a stream.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_stream(
        streamId='string'
    )
    
    
    :type streamId: string
    :param streamId: [REQUIRED]\nThe stream ID.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.DeleteConflictException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.DeleteConflictException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_thing(thingName=None, expectedVersion=None):
    """
    Deletes the specified thing. Returns successfully with no error if the deletion is successful or you specify a thing that doesn\'t exist.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_thing(
        thingName='string',
        expectedVersion=123
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing to delete.\n

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the DeleteThing request is rejected with a VersionConflictException .

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The output of the DeleteThing operation.





Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.VersionConflictException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.VersionConflictException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def delete_thing_group(thingGroupName=None, expectedVersion=None):
    """
    Deletes a thing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_thing_group(
        thingGroupName='string',
        expectedVersion=123
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]\nThe name of the thing group to delete.\n

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the thing group to delete.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.VersionConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def delete_thing_type(thingTypeName=None):
    """
    Deletes the specified thing type. You cannot delete a thing type if it has things associated with it. To delete a thing type, first mark it as deprecated by calling  DeprecateThingType , then remove any associated things by calling  UpdateThing to change the thing type on any associated thing, and finally use  DeleteThingType to delete the thing type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_thing_type(
        thingTypeName='string'
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]\nThe name of the thing type.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --The output for the DeleteThingType operation.




Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    """
    pass

def delete_topic_rule(ruleName=None):
    """
    Deletes the rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]\nThe name of the rule.\n

    """
    pass

def delete_topic_rule_destination(arn=None):
    """
    Deletes a topic rule destination.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_topic_rule_destination(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe ARN of the topic rule destination to delete.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ConflictingResourceUpdateException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.InternalException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ConflictingResourceUpdateException
    
    """
    pass

def delete_v2_logging_level(targetType=None, targetName=None):
    """
    Deletes a logging level.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_v2_logging_level(
        targetType='DEFAULT'|'THING_GROUP',
        targetName='string'
    )
    
    
    :type targetType: string
    :param targetType: [REQUIRED]\nThe type of resource for which you are configuring logging. Must be THING_Group .\n

    :type targetName: string
    :param targetName: [REQUIRED]\nThe name of the resource for which you are configuring logging.\n

    :returns: 
    IoT.Client.exceptions.InternalException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def deprecate_thing_type(thingTypeName=None, undoDeprecate=None):
    """
    Deprecates a thing type. You can not associate new things with deprecated thing type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.deprecate_thing_type(
        thingTypeName='string',
        undoDeprecate=True|False
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]\nThe name of the thing type to deprecate.\n

    :type undoDeprecate: boolean
    :param undoDeprecate: Whether to undeprecate a deprecated thing type. If true , the thing type will not be deprecated anymore and you can associate it with things.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The output for the DeprecateThingType operation.





Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def describe_account_audit_configuration():
    """
    Gets information about the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_account_audit_configuration()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'roleArn': 'string',
    'auditNotificationTargetConfigurations': {
        'string': {
            'targetArn': 'string',
            'roleArn': 'string',
            'enabled': True|False
        }
    },
    'auditCheckConfigurations': {
        'string': {
            'enabled': True|False
        }
    }
}


Response Structure

(dict) --
roleArn (string) --The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.
On the first call to UpdateAccountAuditConfiguration , this parameter is required.

auditNotificationTargetConfigurations (dict) --Information about the targets to which audit notifications are sent for this account.

(string) --
(dict) --Information about the targets to which audit notifications are sent.

targetArn (string) --The ARN of the target (SNS topic) to which audit notifications are sent.

roleArn (string) --The ARN of the role that grants permission to send notifications to the target.

enabled (boolean) --True if notifications to the target are enabled.







auditCheckConfigurations (dict) --Which audit checks are enabled and disabled for this account.

(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)

(dict) --Which audit checks are enabled and disabled for this account.

enabled (boolean) --True if this audit check is enabled for this account.












Exceptions

IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'roleArn': 'string',
        'auditNotificationTargetConfigurations': {
            'string': {
                'targetArn': 'string',
                'roleArn': 'string',
                'enabled': True|False
            }
        },
        'auditCheckConfigurations': {
            'string': {
                'enabled': True|False
            }
        }
    }
    
    
    """
    pass

def describe_audit_finding(findingId=None):
    """
    Gets information about a single audit finding. Properties include the reason for noncompliance, the severity of the issue, and when the audit that returned the finding was started.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_audit_finding(
        findingId='string'
    )
    
    
    :type findingId: string
    :param findingId: [REQUIRED]\nA unique identifier for a single audit finding. You can use this identifier to apply mitigation actions to the finding.\n

    :rtype: dict
ReturnsResponse Syntax{
    'finding': {
        'findingId': 'string',
        'taskId': 'string',
        'checkName': 'string',
        'taskStartTime': datetime(2015, 1, 1),
        'findingTime': datetime(2015, 1, 1),
        'severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW',
        'nonCompliantResource': {
            'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS'|'ROLE_ALIAS'|'IAM_ROLE',
            'resourceIdentifier': {
                'deviceCertificateId': 'string',
                'caCertificateId': 'string',
                'cognitoIdentityPoolId': 'string',
                'clientId': 'string',
                'policyVersionIdentifier': {
                    'policyName': 'string',
                    'policyVersionId': 'string'
                },
                'account': 'string',
                'iamRoleArn': 'string',
                'roleAliasArn': 'string'
            },
            'additionalInfo': {
                'string': 'string'
            }
        },
        'relatedResources': [
            {
                'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS'|'ROLE_ALIAS'|'IAM_ROLE',
                'resourceIdentifier': {
                    'deviceCertificateId': 'string',
                    'caCertificateId': 'string',
                    'cognitoIdentityPoolId': 'string',
                    'clientId': 'string',
                    'policyVersionIdentifier': {
                        'policyName': 'string',
                        'policyVersionId': 'string'
                    },
                    'account': 'string',
                    'iamRoleArn': 'string',
                    'roleAliasArn': 'string'
                },
                'additionalInfo': {
                    'string': 'string'
                }
            },
        ],
        'reasonForNonCompliance': 'string',
        'reasonForNonComplianceCode': 'string'
    }
}


Response Structure

(dict) --
finding (dict) --The findings (results) of the audit.

findingId (string) --A unique identifier for this set of audit findings. This identifier is used to apply mitigation tasks to one or more sets of findings.

taskId (string) --The ID of the audit that generated this result (finding).

checkName (string) --The audit check that generated this result.

taskStartTime (datetime) --The time the audit started.

findingTime (datetime) --The time the result (finding) was discovered.

severity (string) --The severity of the result (finding).

nonCompliantResource (dict) --The resource that was found to be noncompliant with the audit check.

resourceType (string) --The type of the noncompliant resource.

resourceIdentifier (dict) --Information that identifies the noncompliant resource.

deviceCertificateId (string) --The ID of the certificate attached to the resource.

caCertificateId (string) --The ID of the CA certificate used to authorize the certificate.

cognitoIdentityPoolId (string) --The ID of the Amazon Cognito identity pool.

clientId (string) --The client ID.

policyVersionIdentifier (dict) --The version of the policy associated with the resource.

policyName (string) --The name of the policy.

policyVersionId (string) --The ID of the version of the policy associated with the resource.



account (string) --The account with which the resource is associated.

iamRoleArn (string) --The ARN of the IAM role that has overly permissive actions.

roleAliasArn (string) --The ARN of the role alias that has overly permissive actions.



additionalInfo (dict) --Other information about the noncompliant resource.

(string) --
(string) --






relatedResources (list) --The list of related resources.

(dict) --Information about a related resource.

resourceType (string) --The type of resource.

resourceIdentifier (dict) --Information that identifies the resource.

deviceCertificateId (string) --The ID of the certificate attached to the resource.

caCertificateId (string) --The ID of the CA certificate used to authorize the certificate.

cognitoIdentityPoolId (string) --The ID of the Amazon Cognito identity pool.

clientId (string) --The client ID.

policyVersionIdentifier (dict) --The version of the policy associated with the resource.

policyName (string) --The name of the policy.

policyVersionId (string) --The ID of the version of the policy associated with the resource.



account (string) --The account with which the resource is associated.

iamRoleArn (string) --The ARN of the IAM role that has overly permissive actions.

roleAliasArn (string) --The ARN of the role alias that has overly permissive actions.



additionalInfo (dict) --Other information about the resource.

(string) --
(string) --








reasonForNonCompliance (string) --The reason the resource was noncompliant.

reasonForNonComplianceCode (string) --A code that indicates the reason that the resource was noncompliant.








Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'finding': {
            'findingId': 'string',
            'taskId': 'string',
            'checkName': 'string',
            'taskStartTime': datetime(2015, 1, 1),
            'findingTime': datetime(2015, 1, 1),
            'severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW',
            'nonCompliantResource': {
                'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS'|'ROLE_ALIAS'|'IAM_ROLE',
                'resourceIdentifier': {
                    'deviceCertificateId': 'string',
                    'caCertificateId': 'string',
                    'cognitoIdentityPoolId': 'string',
                    'clientId': 'string',
                    'policyVersionIdentifier': {
                        'policyName': 'string',
                        'policyVersionId': 'string'
                    },
                    'account': 'string',
                    'iamRoleArn': 'string',
                    'roleAliasArn': 'string'
                },
                'additionalInfo': {
                    'string': 'string'
                }
            },
            'relatedResources': [
                {
                    'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS'|'ROLE_ALIAS'|'IAM_ROLE',
                    'resourceIdentifier': {
                        'deviceCertificateId': 'string',
                        'caCertificateId': 'string',
                        'cognitoIdentityPoolId': 'string',
                        'clientId': 'string',
                        'policyVersionIdentifier': {
                            'policyName': 'string',
                            'policyVersionId': 'string'
                        },
                        'account': 'string',
                        'iamRoleArn': 'string',
                        'roleAliasArn': 'string'
                    },
                    'additionalInfo': {
                        'string': 'string'
                    }
                },
            ],
            'reasonForNonCompliance': 'string',
            'reasonForNonComplianceCode': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_audit_mitigation_actions_task(taskId=None):
    """
    Gets information about an audit mitigation task that is used to apply mitigation actions to a set of audit findings. Properties include the actions being applied, the audit checks to which they\'re being applied, the task status, and aggregated task statistics.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_audit_mitigation_actions_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]\nThe unique identifier for the audit mitigation task.\n

    :rtype: dict
ReturnsResponse Syntax{
    'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
    'startTime': datetime(2015, 1, 1),
    'endTime': datetime(2015, 1, 1),
    'taskStatistics': {
        'string': {
            'totalFindingsCount': 123,
            'failedFindingsCount': 123,
            'succeededFindingsCount': 123,
            'skippedFindingsCount': 123,
            'canceledFindingsCount': 123
        }
    },
    'target': {
        'auditTaskId': 'string',
        'findingIds': [
            'string',
        ],
        'auditCheckToReasonCodeFilter': {
            'string': [
                'string',
            ]
        }
    },
    'auditCheckToActionsMapping': {
        'string': [
            'string',
        ]
    },
    'actionsDefinition': [
        {
            'name': 'string',
            'id': 'string',
            'roleArn': 'string',
            'actionParams': {
                'updateDeviceCertificateParams': {
                    'action': 'DEACTIVATE'
                },
                'updateCACertificateParams': {
                    'action': 'DEACTIVATE'
                },
                'addThingsToThingGroupParams': {
                    'thingGroupNames': [
                        'string',
                    ],
                    'overrideDynamicGroups': True|False
                },
                'replaceDefaultPolicyVersionParams': {
                    'templateName': 'BLANK_POLICY'
                },
                'enableIoTLoggingParams': {
                    'roleArnForLogging': 'string',
                    'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
                },
                'publishFindingToSnsParams': {
                    'topicArn': 'string'
                }
            }
        },
    ]
}


Response Structure

(dict) --
taskStatus (string) --The current status of the task.

startTime (datetime) --The date and time when the task was started.

endTime (datetime) --The date and time when the task was completed or canceled.

taskStatistics (dict) --Aggregate counts of the results when the mitigation tasks were applied to the findings for this audit mitigation actions task.

(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)

(dict) --Provides summary counts of how many tasks for findings are in a particular state. This information is included in the response from DescribeAuditMitigationActionsTask.

totalFindingsCount (integer) --The total number of findings to which a task is being applied.

failedFindingsCount (integer) --The number of findings for which at least one of the actions failed when applied.

succeededFindingsCount (integer) --The number of findings for which all mitigation actions succeeded when applied.

skippedFindingsCount (integer) --The number of findings skipped because of filter conditions provided in the parameters to the command.

canceledFindingsCount (integer) --The number of findings to which the mitigation action task was canceled when applied.







target (dict) --Identifies the findings to which the mitigation actions are applied. This can be by audit checks, by audit task, or a set of findings.

auditTaskId (string) --If the task will apply a mitigation action to findings from a specific audit, this value uniquely identifies the audit.

findingIds (list) --If the task will apply a mitigation action to one or more listed findings, this value uniquely identifies those findings.

(string) --


auditCheckToReasonCodeFilter (dict) --Specifies a filter in the form of an audit check and set of reason codes that identify the findings from the audit to which the audit mitigation actions task apply.

(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)

(list) --
(string) --








auditCheckToActionsMapping (dict) --Specifies the mitigation actions that should be applied to specific audit checks.

(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)

(list) --
(string) --






actionsDefinition (list) --Specifies the mitigation actions and their parameters that are applied as part of this task.

(dict) --Describes which changes should be applied as part of a mitigation action.

name (string) --A user-friendly name for the mitigation action.

id (string) --A unique identifier for the mitigation action.

roleArn (string) --The IAM role ARN used to apply this mitigation action.

actionParams (dict) --The set of parameters for this mitigation action. The parameters vary, depending on the kind of action you apply.

updateDeviceCertificateParams (dict) --Parameters to define a mitigation action that changes the state of the device certificate to inactive.

action (string) --The action that you want to apply to the device cerrtificate. The only supported value is DEACTIVATE .



updateCACertificateParams (dict) --Parameters to define a mitigation action that changes the state of the CA certificate to inactive.

action (string) --The action that you want to apply to the CA cerrtificate. The only supported value is DEACTIVATE .



addThingsToThingGroupParams (dict) --Parameters to define a mitigation action that moves devices associated with a certificate to one or more specified thing groups, typically for quarantine.

thingGroupNames (list) --The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to more than one group in the same hierarchy.

(string) --


overrideDynamicGroups (boolean) --Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic things groups.



replaceDefaultPolicyVersionParams (dict) --Parameters to define a mitigation action that adds a blank policy to restrict permissions.

templateName (string) --The name of the template to be applied. The only supported value is BLANK_POLICY .



enableIoTLoggingParams (dict) --Parameters to define a mitigation action that enables AWS IoT logging at a specified level of detail.

roleArnForLogging (string) --The ARN of the IAM role used for logging.

logLevel (string) --Specifies the types of information to be logged.



publishFindingToSnsParams (dict) --Parameters to define a mitigation action that publishes findings to Amazon SNS. You can implement your own custom actions in response to the Amazon SNS messages.

topicArn (string) --The ARN of the topic to which you want to publish the findings.














Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
        'startTime': datetime(2015, 1, 1),
        'endTime': datetime(2015, 1, 1),
        'taskStatistics': {
            'string': {
                'totalFindingsCount': 123,
                'failedFindingsCount': 123,
                'succeededFindingsCount': 123,
                'skippedFindingsCount': 123,
                'canceledFindingsCount': 123
            }
        },
        'target': {
            'auditTaskId': 'string',
            'findingIds': [
                'string',
            ],
            'auditCheckToReasonCodeFilter': {
                'string': [
                    'string',
                ]
            }
        },
        'auditCheckToActionsMapping': {
            'string': [
                'string',
            ]
        },
        'actionsDefinition': [
            {
                'name': 'string',
                'id': 'string',
                'roleArn': 'string',
                'actionParams': {
                    'updateDeviceCertificateParams': {
                        'action': 'DEACTIVATE'
                    },
                    'updateCACertificateParams': {
                        'action': 'DEACTIVATE'
                    },
                    'addThingsToThingGroupParams': {
                        'thingGroupNames': [
                            'string',
                        ],
                        'overrideDynamicGroups': True|False
                    },
                    'replaceDefaultPolicyVersionParams': {
                        'templateName': 'BLANK_POLICY'
                    },
                    'enableIoTLoggingParams': {
                        'roleArnForLogging': 'string',
                        'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
                    },
                    'publishFindingToSnsParams': {
                        'topicArn': 'string'
                    }
                }
            },
        ]
    }
    
    
    :returns: 
    (list) --
    (string) --
    
    
    
    """
    pass

def describe_audit_task(taskId=None):
    """
    Gets information about a Device Defender audit.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_audit_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]\nThe ID of the audit whose information you want to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
    'taskType': 'ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK',
    'taskStartTime': datetime(2015, 1, 1),
    'taskStatistics': {
        'totalChecks': 123,
        'inProgressChecks': 123,
        'waitingForDataCollectionChecks': 123,
        'compliantChecks': 123,
        'nonCompliantChecks': 123,
        'failedChecks': 123,
        'canceledChecks': 123
    },
    'scheduledAuditName': 'string',
    'auditDetails': {
        'string': {
            'checkRunStatus': 'IN_PROGRESS'|'WAITING_FOR_DATA_COLLECTION'|'CANCELED'|'COMPLETED_COMPLIANT'|'COMPLETED_NON_COMPLIANT'|'FAILED',
            'checkCompliant': True|False,
            'totalResourcesCount': 123,
            'nonCompliantResourcesCount': 123,
            'errorCode': 'string',
            'message': 'string'
        }
    }
}


Response Structure

(dict) --
taskStatus (string) --The status of the audit: one of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".

taskType (string) --The type of audit: "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".

taskStartTime (datetime) --The time the audit started.

taskStatistics (dict) --Statistical information about the audit.

totalChecks (integer) --The number of checks in this audit.

inProgressChecks (integer) --The number of checks in progress.

waitingForDataCollectionChecks (integer) --The number of checks waiting for data collection.

compliantChecks (integer) --The number of checks that found compliant resources.

nonCompliantChecks (integer) --The number of checks that found noncompliant resources.

failedChecks (integer) --The number of checks.

canceledChecks (integer) --The number of checks that did not run because the audit was canceled.



scheduledAuditName (string) --The name of the scheduled audit (only if the audit was a scheduled audit).

auditDetails (dict) --Detailed information about each check performed during this audit.

(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)

(dict) --Information about the audit check.

checkRunStatus (string) --The completion status of this check. One of "IN_PROGRESS", "WAITING_FOR_DATA_COLLECTION", "CANCELED", "COMPLETED_COMPLIANT", "COMPLETED_NON_COMPLIANT", or "FAILED".

checkCompliant (boolean) --True if the check is complete and found all resources compliant.

totalResourcesCount (integer) --The number of resources on which the check was performed.

nonCompliantResourcesCount (integer) --The number of resources that were found noncompliant during the check.

errorCode (string) --The code of any error encountered when this check is performed during this audit. One of "INSUFFICIENT_PERMISSIONS" or "AUDIT_CHECK_DISABLED".

message (string) --The message associated with any error encountered when this check is performed during this audit.












Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
        'taskType': 'ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK',
        'taskStartTime': datetime(2015, 1, 1),
        'taskStatistics': {
            'totalChecks': 123,
            'inProgressChecks': 123,
            'waitingForDataCollectionChecks': 123,
            'compliantChecks': 123,
            'nonCompliantChecks': 123,
            'failedChecks': 123,
            'canceledChecks': 123
        },
        'scheduledAuditName': 'string',
        'auditDetails': {
            'string': {
                'checkRunStatus': 'IN_PROGRESS'|'WAITING_FOR_DATA_COLLECTION'|'CANCELED'|'COMPLETED_COMPLIANT'|'COMPLETED_NON_COMPLIANT'|'FAILED',
                'checkCompliant': True|False,
                'totalResourcesCount': 123,
                'nonCompliantResourcesCount': 123,
                'errorCode': 'string',
                'message': 'string'
            }
        }
    }
    
    
    """
    pass

def describe_authorizer(authorizerName=None):
    """
    Describes an authorizer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_authorizer(
        authorizerName='string'
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]\nThe name of the authorizer to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'authorizerDescription': {
        'authorizerName': 'string',
        'authorizerArn': 'string',
        'authorizerFunctionArn': 'string',
        'tokenKeyName': 'string',
        'tokenSigningPublicKeys': {
            'string': 'string'
        },
        'status': 'ACTIVE'|'INACTIVE',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'signingDisabled': True|False
    }
}


Response Structure

(dict) --
authorizerDescription (dict) --The authorizer description.

authorizerName (string) --The authorizer name.

authorizerArn (string) --The authorizer ARN.

authorizerFunctionArn (string) --The authorizer\'s Lambda function ARN.

tokenKeyName (string) --The key used to extract the token from the HTTP headers.

tokenSigningPublicKeys (dict) --The public keys used to validate the token signature returned by your custom authentication service.

(string) --
(string) --




status (string) --The status of the authorizer.

creationDate (datetime) --The UNIX timestamp of when the authorizer was created.

lastModifiedDate (datetime) --The UNIX timestamp of when the authorizer was last updated.

signingDisabled (boolean) --Specifies whether AWS IoT validates the token signature in an authorization request.








Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'authorizerDescription': {
            'authorizerName': 'string',
            'authorizerArn': 'string',
            'authorizerFunctionArn': 'string',
            'tokenKeyName': 'string',
            'tokenSigningPublicKeys': {
                'string': 'string'
            },
            'status': 'ACTIVE'|'INACTIVE',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'signingDisabled': True|False
        }
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def describe_billing_group(billingGroupName=None):
    """
    Returns information about a billing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_billing_group(
        billingGroupName='string'
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: [REQUIRED]\nThe name of the billing group.\n

    :rtype: dict
ReturnsResponse Syntax{
    'billingGroupName': 'string',
    'billingGroupId': 'string',
    'billingGroupArn': 'string',
    'version': 123,
    'billingGroupProperties': {
        'billingGroupDescription': 'string'
    },
    'billingGroupMetadata': {
        'creationDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
billingGroupName (string) --The name of the billing group.

billingGroupId (string) --The ID of the billing group.

billingGroupArn (string) --The ARN of the billing group.

version (integer) --The version of the billing group.

billingGroupProperties (dict) --The properties of the billing group.

billingGroupDescription (string) --The description of the billing group.



billingGroupMetadata (dict) --Additional information about the billing group.

creationDate (datetime) --The date the billing group was created.








Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'billingGroupName': 'string',
        'billingGroupId': 'string',
        'billingGroupArn': 'string',
        'version': 123,
        'billingGroupProperties': {
            'billingGroupDescription': 'string'
        },
        'billingGroupMetadata': {
            'creationDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def describe_ca_certificate(certificateId=None):
    """
    Describes a registered CA certificate.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_ca_certificate(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]\nThe CA certificate identifier.\n

    :rtype: dict
ReturnsResponse Syntax{
    'certificateDescription': {
        'certificateArn': 'string',
        'certificateId': 'string',
        'status': 'ACTIVE'|'INACTIVE',
        'certificatePem': 'string',
        'ownedBy': 'string',
        'creationDate': datetime(2015, 1, 1),
        'autoRegistrationStatus': 'ENABLE'|'DISABLE',
        'lastModifiedDate': datetime(2015, 1, 1),
        'customerVersion': 123,
        'generationId': 'string',
        'validity': {
            'notBefore': datetime(2015, 1, 1),
            'notAfter': datetime(2015, 1, 1)
        }
    },
    'registrationConfig': {
        'templateBody': 'string',
        'roleArn': 'string'
    }
}


Response Structure

(dict) --The output from the DescribeCACertificate operation.

certificateDescription (dict) --The CA certificate description.

certificateArn (string) --The CA certificate ARN.

certificateId (string) --The CA certificate ID.

status (string) --The status of a CA certificate.

certificatePem (string) --The CA certificate data, in PEM format.

ownedBy (string) --The owner of the CA certificate.

creationDate (datetime) --The date the CA certificate was created.

autoRegistrationStatus (string) --Whether the CA certificate configured for auto registration of device certificates. Valid values are "ENABLE" and "DISABLE"

lastModifiedDate (datetime) --The date the CA certificate was last modified.

customerVersion (integer) --The customer version of the CA certificate.

generationId (string) --The generation ID of the CA certificate.

validity (dict) --When the CA certificate is valid.

notBefore (datetime) --The certificate is not valid before this date.

notAfter (datetime) --The certificate is not valid after this date.





registrationConfig (dict) --Information about the registration configuration.

templateBody (string) --The template body.

roleArn (string) --The ARN of the role.








Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'certificateDescription': {
            'certificateArn': 'string',
            'certificateId': 'string',
            'status': 'ACTIVE'|'INACTIVE',
            'certificatePem': 'string',
            'ownedBy': 'string',
            'creationDate': datetime(2015, 1, 1),
            'autoRegistrationStatus': 'ENABLE'|'DISABLE',
            'lastModifiedDate': datetime(2015, 1, 1),
            'customerVersion': 123,
            'generationId': 'string',
            'validity': {
                'notBefore': datetime(2015, 1, 1),
                'notAfter': datetime(2015, 1, 1)
            }
        },
        'registrationConfig': {
            'templateBody': 'string',
            'roleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_certificate(certificateId=None):
    """
    Gets information about the specified certificate.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_certificate(
        certificateId='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]\nThe ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)\n

    :rtype: dict
ReturnsResponse Syntax{
    'certificateDescription': {
        'certificateArn': 'string',
        'certificateId': 'string',
        'caCertificateId': 'string',
        'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
        'certificatePem': 'string',
        'ownedBy': 'string',
        'previousOwnedBy': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'customerVersion': 123,
        'transferData': {
            'transferMessage': 'string',
            'rejectReason': 'string',
            'transferDate': datetime(2015, 1, 1),
            'acceptDate': datetime(2015, 1, 1),
            'rejectDate': datetime(2015, 1, 1)
        },
        'generationId': 'string',
        'validity': {
            'notBefore': datetime(2015, 1, 1),
            'notAfter': datetime(2015, 1, 1)
        },
        'certificateMode': 'DEFAULT'|'SNI_ONLY'
    }
}


Response Structure

(dict) --The output of the DescribeCertificate operation.

certificateDescription (dict) --The description of the certificate.

certificateArn (string) --The ARN of the certificate.

certificateId (string) --The ID of the certificate.

caCertificateId (string) --The certificate ID of the CA certificate used to sign this certificate.

status (string) --The status of the certificate.

certificatePem (string) --The certificate data, in PEM format.

ownedBy (string) --The ID of the AWS account that owns the certificate.

previousOwnedBy (string) --The ID of the AWS account of the previous owner of the certificate.

creationDate (datetime) --The date and time the certificate was created.

lastModifiedDate (datetime) --The date and time the certificate was last modified.

customerVersion (integer) --The customer version of the certificate.

transferData (dict) --The transfer data.

transferMessage (string) --The transfer message.

rejectReason (string) --The reason why the transfer was rejected.

transferDate (datetime) --The date the transfer took place.

acceptDate (datetime) --The date the transfer was accepted.

rejectDate (datetime) --The date the transfer was rejected.



generationId (string) --The generation ID of the certificate.

validity (dict) --When the certificate is valid.

notBefore (datetime) --The certificate is not valid before this date.

notAfter (datetime) --The certificate is not valid after this date.



certificateMode (string) --The mode of the certificate.








Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'certificateDescription': {
            'certificateArn': 'string',
            'certificateId': 'string',
            'caCertificateId': 'string',
            'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
            'certificatePem': 'string',
            'ownedBy': 'string',
            'previousOwnedBy': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'customerVersion': 123,
            'transferData': {
                'transferMessage': 'string',
                'rejectReason': 'string',
                'transferDate': datetime(2015, 1, 1),
                'acceptDate': datetime(2015, 1, 1),
                'rejectDate': datetime(2015, 1, 1)
            },
            'generationId': 'string',
            'validity': {
                'notBefore': datetime(2015, 1, 1),
                'notAfter': datetime(2015, 1, 1)
            },
            'certificateMode': 'DEFAULT'|'SNI_ONLY'
        }
    }
    
    
    """
    pass

def describe_default_authorizer():
    """
    Describes the default authorizer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_default_authorizer()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'authorizerDescription': {
        'authorizerName': 'string',
        'authorizerArn': 'string',
        'authorizerFunctionArn': 'string',
        'tokenKeyName': 'string',
        'tokenSigningPublicKeys': {
            'string': 'string'
        },
        'status': 'ACTIVE'|'INACTIVE',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'signingDisabled': True|False
    }
}


Response Structure

(dict) --
authorizerDescription (dict) --The default authorizer\'s description.

authorizerName (string) --The authorizer name.

authorizerArn (string) --The authorizer ARN.

authorizerFunctionArn (string) --The authorizer\'s Lambda function ARN.

tokenKeyName (string) --The key used to extract the token from the HTTP headers.

tokenSigningPublicKeys (dict) --The public keys used to validate the token signature returned by your custom authentication service.

(string) --
(string) --




status (string) --The status of the authorizer.

creationDate (datetime) --The UNIX timestamp of when the authorizer was created.

lastModifiedDate (datetime) --The UNIX timestamp of when the authorizer was last updated.

signingDisabled (boolean) --Specifies whether AWS IoT validates the token signature in an authorization request.








Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'authorizerDescription': {
            'authorizerName': 'string',
            'authorizerArn': 'string',
            'authorizerFunctionArn': 'string',
            'tokenKeyName': 'string',
            'tokenSigningPublicKeys': {
                'string': 'string'
            },
            'status': 'ACTIVE'|'INACTIVE',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'signingDisabled': True|False
        }
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def describe_dimension(name=None):
    """
    Provides details about a dimension that is defined in your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_dimension(
        name='string'
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nThe unique identifier for the dimension.\n

    :rtype: dict
ReturnsResponse Syntax{
    'name': 'string',
    'arn': 'string',
    'type': 'TOPIC_FILTER',
    'stringValues': [
        'string',
    ],
    'creationDate': datetime(2015, 1, 1),
    'lastModifiedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
name (string) --The unique identifier for the dimension.

arn (string) --The ARN (Amazon resource name) for the dimension.

type (string) --The type of the dimension.

stringValues (list) --The value or list of values used to scope the dimension. For example, for topic filters, this is the pattern used to match the MQTT topic name.

(string) --


creationDate (datetime) --The date the dimension was created.

lastModifiedDate (datetime) --The date the dimension was last modified.






Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException


    :return: {
        'name': 'string',
        'arn': 'string',
        'type': 'TOPIC_FILTER',
        'stringValues': [
            'string',
        ],
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    
    """
    pass

def describe_domain_configuration(domainConfigurationName=None):
    """
    Gets summary information about a domain configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_domain_configuration(
        domainConfigurationName='string'
    )
    
    
    :type domainConfigurationName: string
    :param domainConfigurationName: [REQUIRED]\nThe name of the domain configuration.\n

    :rtype: dict
ReturnsResponse Syntax{
    'domainConfigurationName': 'string',
    'domainConfigurationArn': 'string',
    'domainName': 'string',
    'serverCertificates': [
        {
            'serverCertificateArn': 'string',
            'serverCertificateStatus': 'INVALID'|'VALID',
            'serverCertificateStatusDetail': 'string'
        },
    ],
    'authorizerConfig': {
        'defaultAuthorizerName': 'string',
        'allowAuthorizerOverride': True|False
    },
    'domainConfigurationStatus': 'ENABLED'|'DISABLED',
    'serviceType': 'DATA'|'CREDENTIAL_PROVIDER'|'JOBS',
    'domainType': 'ENDPOINT'|'AWS_MANAGED'|'CUSTOMER_MANAGED'
}


Response Structure

(dict) --
domainConfigurationName (string) --The name of the domain configuration.

domainConfigurationArn (string) --The ARN of the domain configuration.

domainName (string) --The name of the domain.

serverCertificates (list) --A list containing summary information about the server certificate included in the domain configuration.

(dict) --An object that contains information about a server certificate.

serverCertificateArn (string) --The ARN of the server certificate.

serverCertificateStatus (string) --The status of the server certificate.

serverCertificateStatusDetail (string) --Details that explain the status of the server certificate.





authorizerConfig (dict) --An object that specifies the authorization service for a domain.

defaultAuthorizerName (string) --The name of the authorization service for a domain configuration.

allowAuthorizerOverride (boolean) --A Boolean that specifies whether the domain configuration\'s authorization service can be overridden.



domainConfigurationStatus (string) --A Boolean value that specifies the current state of the domain configuration.

serviceType (string) --The type of service delivered by the endpoint.

domainType (string) --The type of the domain.






Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'domainConfigurationName': 'string',
        'domainConfigurationArn': 'string',
        'domainName': 'string',
        'serverCertificates': [
            {
                'serverCertificateArn': 'string',
                'serverCertificateStatus': 'INVALID'|'VALID',
                'serverCertificateStatusDetail': 'string'
            },
        ],
        'authorizerConfig': {
            'defaultAuthorizerName': 'string',
            'allowAuthorizerOverride': True|False
        },
        'domainConfigurationStatus': 'ENABLED'|'DISABLED',
        'serviceType': 'DATA'|'CREDENTIAL_PROVIDER'|'JOBS',
        'domainType': 'ENDPOINT'|'AWS_MANAGED'|'CUSTOMER_MANAGED'
    }
    
    
    """
    pass

def describe_endpoint(endpointType=None):
    """
    Returns a unique endpoint specific to the AWS account making the call.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_endpoint(
        endpointType='string'
    )
    
    
    :type endpointType: string
    :param endpointType: The endpoint type. Valid endpoint types include:\n\niot:Data - Returns a VeriSign signed data endpoint.\niot:Data-ATS - Returns an ATS signed data endpoint.\niot:CredentialProvider - Returns an AWS IoT credentials provider API endpoint.\niot:Jobs - Returns an AWS IoT device management Jobs API endpoint.\n\nWe strongly recommend that customers use the newer iot:Data-ATS endpoint type to avoid issues related to the widespread distrust of Symantec certificate authorities.\n

    :rtype: dict
ReturnsResponse Syntax{
    'endpointAddress': 'string'
}


Response Structure

(dict) --The output from the DescribeEndpoint operation.

endpointAddress (string) --The endpoint. The format of the endpoint is as follows: identifier .iot.*region* .amazonaws.com.






Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ThrottlingException


    :return: {
        'endpointAddress': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ThrottlingException
    
    """
    pass

def describe_event_configurations():
    """
    Describes event configurations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_event_configurations()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'eventConfigurations': {
        'string': {
            'Enabled': True|False
        }
    },
    'creationDate': datetime(2015, 1, 1),
    'lastModifiedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
eventConfigurations (dict) --The event configurations.

(string) --
(dict) --Configuration.

Enabled (boolean) --True to enable the configuration.







creationDate (datetime) --The creation date of the event configuration.

lastModifiedDate (datetime) --The date the event configurations were last modified.






Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ThrottlingException


    :return: {
        'eventConfigurations': {
            'string': {
                'Enabled': True|False
            }
        },
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    """
    pass

def describe_index(indexName=None):
    """
    Describes a search index.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_index(
        indexName='string'
    )
    
    
    :type indexName: string
    :param indexName: [REQUIRED]\nThe index name.\n

    :rtype: dict
ReturnsResponse Syntax{
    'indexName': 'string',
    'indexStatus': 'ACTIVE'|'BUILDING'|'REBUILDING',
    'schema': 'string'
}


Response Structure

(dict) --
indexName (string) --The index name.

indexStatus (string) --The index status.

schema (string) --Contains a value that specifies the type of indexing performed. Valid values are:

REGISTRY \xe2\x80\x93 Your thing index contains only registry data.
REGISTRY_AND_SHADOW - Your thing index contains registry data and shadow data.
REGISTRY_AND_CONNECTIVITY_STATUS - Your thing index contains registry data and thing connectivity status data.
REGISTRY_AND_SHADOW_AND_CONNECTIVITY_STATUS - Your thing index contains registry data, shadow data, and thing connectivity status data.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'indexName': 'string',
        'indexStatus': 'ACTIVE'|'BUILDING'|'REBUILDING',
        'schema': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_job(jobId=None):
    """
    Describes a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_job(
        jobId='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique identifier you assigned to this job when it was created.\n

    :rtype: dict
ReturnsResponse Syntax{
    'documentSource': 'string',
    'job': {
        'jobArn': 'string',
        'jobId': 'string',
        'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
        'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
        'forceCanceled': True|False,
        'reasonCode': 'string',
        'comment': 'string',
        'targets': [
            'string',
        ],
        'description': 'string',
        'presignedUrlConfig': {
            'roleArn': 'string',
            'expiresInSec': 123
        },
        'jobExecutionsRolloutConfig': {
            'maximumPerMinute': 123,
            'exponentialRate': {
                'baseRatePerMinute': 123,
                'incrementFactor': 123.0,
                'rateIncreaseCriteria': {
                    'numberOfNotifiedThings': 123,
                    'numberOfSucceededThings': 123
                }
            }
        },
        'abortConfig': {
            'criteriaList': [
                {
                    'failureType': 'FAILED'|'REJECTED'|'TIMED_OUT'|'ALL',
                    'action': 'CANCEL',
                    'thresholdPercentage': 123.0,
                    'minNumberOfExecutedThings': 123
                },
            ]
        },
        'createdAt': datetime(2015, 1, 1),
        'lastUpdatedAt': datetime(2015, 1, 1),
        'completedAt': datetime(2015, 1, 1),
        'jobProcessDetails': {
            'processingTargets': [
                'string',
            ],
            'numberOfCanceledThings': 123,
            'numberOfSucceededThings': 123,
            'numberOfFailedThings': 123,
            'numberOfRejectedThings': 123,
            'numberOfQueuedThings': 123,
            'numberOfInProgressThings': 123,
            'numberOfRemovedThings': 123,
            'numberOfTimedOutThings': 123
        },
        'timeoutConfig': {
            'inProgressTimeoutInMinutes': 123
        }
    }
}


Response Structure

(dict) --
documentSource (string) --An S3 link to the job document.

job (dict) --Information about the job.

jobArn (string) --An ARN identifying the job with format "arn:aws:iot:region:account:job/jobId".

jobId (string) --The unique identifier you assigned to this job when it was created.

targetSelection (string) --Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a device when the thing representing the device is added to a target group, even after the job was completed by all things originally in the group.

status (string) --The status of the job, one of IN_PROGRESS , CANCELED , DELETION_IN_PROGRESS or COMPLETED .

forceCanceled (boolean) --Will be true if the job was canceled with the optional force parameter set to true .

reasonCode (string) --If the job was updated, provides the reason code for the update.

comment (string) --If the job was updated, describes the reason for the update.

targets (list) --A list of IoT things and thing groups to which the job should be sent.

(string) --


description (string) --A short text description of the job.

presignedUrlConfig (dict) --Configuration for pre-signed S3 URLs.

roleArn (string) --The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.

expiresInSec (integer) --How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.



jobExecutionsRolloutConfig (dict) --Allows you to create a staged rollout of a job.

maximumPerMinute (integer) --The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.

exponentialRate (dict) --The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.

baseRatePerMinute (integer) --The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.

incrementFactor (float) --The exponential factor to increase the rate of rollout for a job.

rateIncreaseCriteria (dict) --The criteria to initiate the increase in rate of rollout for a job.
AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

numberOfNotifiedThings (integer) --The threshold for number of notified things that will initiate the increase in rate of rollout.

numberOfSucceededThings (integer) --The threshold for number of succeeded things that will initiate the increase in rate of rollout.







abortConfig (dict) --Configuration for criteria to abort the job.

criteriaList (list) --The list of abort criteria to define rules to abort the job.

(dict) --Details of abort criteria to define rules to abort the job.

failureType (string) --The type of job execution failure to define a rule to initiate a job abort.

action (string) --The type of abort action to initiate a job abort.

thresholdPercentage (float) --The threshold as a percentage of the total number of executed things that will initiate a job abort.
AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).

minNumberOfExecutedThings (integer) --Minimum number of executed things before evaluating an abort rule.







createdAt (datetime) --The time, in seconds since the epoch, when the job was created.

lastUpdatedAt (datetime) --The time, in seconds since the epoch, when the job was last updated.

completedAt (datetime) --The time, in seconds since the epoch, when the job was completed.

jobProcessDetails (dict) --Details about the job process.

processingTargets (list) --The target devices to which the job execution is being rolled out. This value will be null after the job execution has finished rolling out to all the target devices.

(string) --


numberOfCanceledThings (integer) --The number of things that cancelled the job.

numberOfSucceededThings (integer) --The number of things which successfully completed the job.

numberOfFailedThings (integer) --The number of things that failed executing the job.

numberOfRejectedThings (integer) --The number of things that rejected the job.

numberOfQueuedThings (integer) --The number of things that are awaiting execution of the job.

numberOfInProgressThings (integer) --The number of things currently executing the job.

numberOfRemovedThings (integer) --The number of things that are no longer scheduled to execute the job because they have been deleted or have been removed from the group that was a target of the job.

numberOfTimedOutThings (integer) --The number of things whose job execution status is TIMED_OUT .



timeoutConfig (dict) --Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to IN_PROGRESS . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to TIMED_OUT .

inProgressTimeoutInMinutes (integer) --Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can\'t be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal TIMED_OUT status.










Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'documentSource': 'string',
        'job': {
            'jobArn': 'string',
            'jobId': 'string',
            'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
            'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
            'forceCanceled': True|False,
            'reasonCode': 'string',
            'comment': 'string',
            'targets': [
                'string',
            ],
            'description': 'string',
            'presignedUrlConfig': {
                'roleArn': 'string',
                'expiresInSec': 123
            },
            'jobExecutionsRolloutConfig': {
                'maximumPerMinute': 123,
                'exponentialRate': {
                    'baseRatePerMinute': 123,
                    'incrementFactor': 123.0,
                    'rateIncreaseCriteria': {
                        'numberOfNotifiedThings': 123,
                        'numberOfSucceededThings': 123
                    }
                }
            },
            'abortConfig': {
                'criteriaList': [
                    {
                        'failureType': 'FAILED'|'REJECTED'|'TIMED_OUT'|'ALL',
                        'action': 'CANCEL',
                        'thresholdPercentage': 123.0,
                        'minNumberOfExecutedThings': 123
                    },
                ]
            },
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'completedAt': datetime(2015, 1, 1),
            'jobProcessDetails': {
                'processingTargets': [
                    'string',
                ],
                'numberOfCanceledThings': 123,
                'numberOfSucceededThings': 123,
                'numberOfFailedThings': 123,
                'numberOfRejectedThings': 123,
                'numberOfQueuedThings': 123,
                'numberOfInProgressThings': 123,
                'numberOfRemovedThings': 123,
                'numberOfTimedOutThings': 123
            },
            'timeoutConfig': {
                'inProgressTimeoutInMinutes': 123
            }
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def describe_job_execution(jobId=None, thingName=None, executionNumber=None):
    """
    Describes a job execution.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_job_execution(
        jobId='string',
        thingName='string',
        executionNumber=123
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique identifier you assigned to this job when it was created.\n

    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing on which the job execution is running.\n

    :type executionNumber: integer
    :param executionNumber: A string (consisting of the digits '0' through '9' which is used to specify a particular job execution on a particular device.

    :rtype: dict

ReturnsResponse Syntax
{
    'execution': {
        'jobId': 'string',
        'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
        'forceCanceled': True|False,
        'statusDetails': {
            'detailsMap': {
                'string': 'string'
            }
        },
        'thingArn': 'string',
        'queuedAt': datetime(2015, 1, 1),
        'startedAt': datetime(2015, 1, 1),
        'lastUpdatedAt': datetime(2015, 1, 1),
        'executionNumber': 123,
        'versionNumber': 123,
        'approximateSecondsBeforeTimedOut': 123
    }
}


Response Structure

(dict) --

execution (dict) --
Information about the job execution.

jobId (string) --
The unique identifier you assigned to the job when it was created.

status (string) --
The status of the job execution (IN_PROGRESS, QUEUED, FAILED, SUCCEEDED, TIMED_OUT, CANCELED, or REJECTED).

forceCanceled (boolean) --
Will be true if the job execution was canceled with the optional force parameter set to true .

statusDetails (dict) --
A collection of name/value pairs that describe the status of the job execution.

detailsMap (dict) --
The job execution status.

(string) --
(string) --






thingArn (string) --
The ARN of the thing on which the job execution is running.

queuedAt (datetime) --
The time, in seconds since the epoch, when the job execution was queued.

startedAt (datetime) --
The time, in seconds since the epoch, when the job execution started.

lastUpdatedAt (datetime) --
The time, in seconds since the epoch, when the job execution was last updated.

executionNumber (integer) --
A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used in commands which return or update job execution information.

versionNumber (integer) --
The version of the job execution. Job execution versions are incremented each time they are updated by a device.

approximateSecondsBeforeTimedOut (integer) --
The estimated number of seconds that remain before the job execution status will be changed to TIMED_OUT . The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The actual job execution timeout can occur up to 60 seconds later than the estimated duration. This value will not be included if the job execution has reached a terminal status.









Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'execution': {
            'jobId': 'string',
            'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
            'forceCanceled': True|False,
            'statusDetails': {
                'detailsMap': {
                    'string': 'string'
                }
            },
            'thingArn': 'string',
            'queuedAt': datetime(2015, 1, 1),
            'startedAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'executionNumber': 123,
            'versionNumber': 123,
            'approximateSecondsBeforeTimedOut': 123
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def describe_mitigation_action(actionName=None):
    """
    Gets information about a mitigation action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_mitigation_action(
        actionName='string'
    )
    
    
    :type actionName: string
    :param actionName: [REQUIRED]\nThe friendly name that uniquely identifies the mitigation action.\n

    :rtype: dict
ReturnsResponse Syntax{
    'actionName': 'string',
    'actionType': 'UPDATE_DEVICE_CERTIFICATE'|'UPDATE_CA_CERTIFICATE'|'ADD_THINGS_TO_THING_GROUP'|'REPLACE_DEFAULT_POLICY_VERSION'|'ENABLE_IOT_LOGGING'|'PUBLISH_FINDING_TO_SNS',
    'actionArn': 'string',
    'actionId': 'string',
    'roleArn': 'string',
    'actionParams': {
        'updateDeviceCertificateParams': {
            'action': 'DEACTIVATE'
        },
        'updateCACertificateParams': {
            'action': 'DEACTIVATE'
        },
        'addThingsToThingGroupParams': {
            'thingGroupNames': [
                'string',
            ],
            'overrideDynamicGroups': True|False
        },
        'replaceDefaultPolicyVersionParams': {
            'templateName': 'BLANK_POLICY'
        },
        'enableIoTLoggingParams': {
            'roleArnForLogging': 'string',
            'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
        },
        'publishFindingToSnsParams': {
            'topicArn': 'string'
        }
    },
    'creationDate': datetime(2015, 1, 1),
    'lastModifiedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
actionName (string) --The friendly name that uniquely identifies the mitigation action.

actionType (string) --The type of mitigation action.

actionArn (string) --The ARN that identifies this migration action.

actionId (string) --A unique identifier for this action.

roleArn (string) --The ARN of the IAM role used to apply this action.

actionParams (dict) --Parameters that control how the mitigation action is applied, specific to the type of mitigation action.

updateDeviceCertificateParams (dict) --Parameters to define a mitigation action that changes the state of the device certificate to inactive.

action (string) --The action that you want to apply to the device cerrtificate. The only supported value is DEACTIVATE .



updateCACertificateParams (dict) --Parameters to define a mitigation action that changes the state of the CA certificate to inactive.

action (string) --The action that you want to apply to the CA cerrtificate. The only supported value is DEACTIVATE .



addThingsToThingGroupParams (dict) --Parameters to define a mitigation action that moves devices associated with a certificate to one or more specified thing groups, typically for quarantine.

thingGroupNames (list) --The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to more than one group in the same hierarchy.

(string) --


overrideDynamicGroups (boolean) --Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic things groups.



replaceDefaultPolicyVersionParams (dict) --Parameters to define a mitigation action that adds a blank policy to restrict permissions.

templateName (string) --The name of the template to be applied. The only supported value is BLANK_POLICY .



enableIoTLoggingParams (dict) --Parameters to define a mitigation action that enables AWS IoT logging at a specified level of detail.

roleArnForLogging (string) --The ARN of the IAM role used for logging.

logLevel (string) --Specifies the types of information to be logged.



publishFindingToSnsParams (dict) --Parameters to define a mitigation action that publishes findings to Amazon SNS. You can implement your own custom actions in response to the Amazon SNS messages.

topicArn (string) --The ARN of the topic to which you want to publish the findings.





creationDate (datetime) --The date and time when the mitigation action was added to your AWS account.

lastModifiedDate (datetime) --The date and time when the mitigation action was last changed.






Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'actionName': 'string',
        'actionType': 'UPDATE_DEVICE_CERTIFICATE'|'UPDATE_CA_CERTIFICATE'|'ADD_THINGS_TO_THING_GROUP'|'REPLACE_DEFAULT_POLICY_VERSION'|'ENABLE_IOT_LOGGING'|'PUBLISH_FINDING_TO_SNS',
        'actionArn': 'string',
        'actionId': 'string',
        'roleArn': 'string',
        'actionParams': {
            'updateDeviceCertificateParams': {
                'action': 'DEACTIVATE'
            },
            'updateCACertificateParams': {
                'action': 'DEACTIVATE'
            },
            'addThingsToThingGroupParams': {
                'thingGroupNames': [
                    'string',
                ],
                'overrideDynamicGroups': True|False
            },
            'replaceDefaultPolicyVersionParams': {
                'templateName': 'BLANK_POLICY'
            },
            'enableIoTLoggingParams': {
                'roleArnForLogging': 'string',
                'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
            },
            'publishFindingToSnsParams': {
                'topicArn': 'string'
            }
        },
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def describe_provisioning_template(templateName=None):
    """
    Returns information about a fleet provisioning template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_provisioning_template(
        templateName='string'
    )
    
    
    :type templateName: string
    :param templateName: [REQUIRED]\nThe name of the fleet provisioning template.\n

    :rtype: dict
ReturnsResponse Syntax{
    'templateArn': 'string',
    'templateName': 'string',
    'description': 'string',
    'creationDate': datetime(2015, 1, 1),
    'lastModifiedDate': datetime(2015, 1, 1),
    'defaultVersionId': 123,
    'templateBody': 'string',
    'enabled': True|False,
    'provisioningRoleArn': 'string',
    'preProvisioningHook': {
        'payloadVersion': 'string',
        'targetArn': 'string'
    }
}


Response Structure

(dict) --
templateArn (string) --The ARN of the fleet provisioning template.

templateName (string) --The name of the fleet provisioning template.

description (string) --The description of the fleet provisioning template.

creationDate (datetime) --The date when the fleet provisioning template was created.

lastModifiedDate (datetime) --The date when the fleet provisioning template was last modified.

defaultVersionId (integer) --The default fleet template version ID.

templateBody (string) --The JSON formatted contents of the fleet provisioning template.

enabled (boolean) --True if the fleet provisioning template is enabled, otherwise false.

provisioningRoleArn (string) --The ARN of the role associated with the provisioning template. This IoT role grants permission to provision a device.

preProvisioningHook (dict) --Gets information about a pre-provisioned hook.

payloadVersion (string) --The payload that was sent to the target function.

Note: Only Lambda functions are currently supported.

targetArn (string) --The ARN of the target function.

Note: Only Lambda functions are currently supported.








Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException


    :return: {
        'templateArn': 'string',
        'templateName': 'string',
        'description': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'defaultVersionId': 123,
        'templateBody': 'string',
        'enabled': True|False,
        'provisioningRoleArn': 'string',
        'preProvisioningHook': {
            'payloadVersion': 'string',
            'targetArn': 'string'
        }
    }
    
    
    """
    pass

def describe_provisioning_template_version(templateName=None, versionId=None):
    """
    Returns information about a fleet provisioning template version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_provisioning_template_version(
        templateName='string',
        versionId=123
    )
    
    
    :type templateName: string
    :param templateName: [REQUIRED]\nThe template name.\n

    :type versionId: integer
    :param versionId: [REQUIRED]\nThe fleet provisioning template version ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'versionId': 123,
    'creationDate': datetime(2015, 1, 1),
    'templateBody': 'string',
    'isDefaultVersion': True|False
}


Response Structure

(dict) --

versionId (integer) --
The fleet provisioning template version ID.

creationDate (datetime) --
The date when the fleet provisioning template version was created.

templateBody (string) --
The JSON formatted contents of the fleet provisioning template version.

isDefaultVersion (boolean) --
True if the fleet provisioning template version is the default version.







Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.UnauthorizedException


    :return: {
        'versionId': 123,
        'creationDate': datetime(2015, 1, 1),
        'templateBody': 'string',
        'isDefaultVersion': True|False
    }
    
    
    :returns: 
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.UnauthorizedException
    
    """
    pass

def describe_role_alias(roleAlias=None):
    """
    Describes a role alias.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_role_alias(
        roleAlias='string'
    )
    
    
    :type roleAlias: string
    :param roleAlias: [REQUIRED]\nThe role alias to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'roleAliasDescription': {
        'roleAlias': 'string',
        'roleAliasArn': 'string',
        'roleArn': 'string',
        'owner': 'string',
        'credentialDurationSeconds': 123,
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
roleAliasDescription (dict) --The role alias description.

roleAlias (string) --The role alias.

roleAliasArn (string) --The ARN of the role alias.

roleArn (string) --The role ARN.

owner (string) --The role alias owner.

credentialDurationSeconds (integer) --The number of seconds for which the credential is valid.

creationDate (datetime) --The UNIX timestamp of when the role alias was created.

lastModifiedDate (datetime) --The UNIX timestamp of when the role alias was last modified.








Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'roleAliasDescription': {
            'roleAlias': 'string',
            'roleAliasArn': 'string',
            'roleArn': 'string',
            'owner': 'string',
            'credentialDurationSeconds': 123,
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1)
        }
    }
    
    
    """
    pass

def describe_scheduled_audit(scheduledAuditName=None):
    """
    Gets information about a scheduled audit.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_scheduled_audit(
        scheduledAuditName='string'
    )
    
    
    :type scheduledAuditName: string
    :param scheduledAuditName: [REQUIRED]\nThe name of the scheduled audit whose information you want to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'frequency': 'DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
    'dayOfMonth': 'string',
    'dayOfWeek': 'SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT',
    'targetCheckNames': [
        'string',
    ],
    'scheduledAuditName': 'string',
    'scheduledAuditArn': 'string'
}


Response Structure

(dict) --
frequency (string) --How often the scheduled audit takes place. One of "DAILY", "WEEKLY", "BIWEEKLY", or "MONTHLY". The start time of each audit is determined by the system.

dayOfMonth (string) --The day of the month on which the scheduled audit takes place. Will be "1" through "31" or "LAST". If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.

dayOfWeek (string) --The day of the week on which the scheduled audit takes place. One of "SUN", "MON", "TUE", "WED", "THU", "FRI", or "SAT".

targetCheckNames (list) --Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)

(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)



scheduledAuditName (string) --The name of the scheduled audit.

scheduledAuditArn (string) --The ARN of the scheduled audit.






Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'frequency': 'DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
        'dayOfMonth': 'string',
        'dayOfWeek': 'SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT',
        'targetCheckNames': [
            'string',
        ],
        'scheduledAuditName': 'string',
        'scheduledAuditArn': 'string'
    }
    
    
    """
    pass

def describe_security_profile(securityProfileName=None):
    """
    Gets information about a Device Defender security profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_security_profile(
        securityProfileName='string'
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]\nThe name of the security profile whose information you want to get.\n

    :rtype: dict
ReturnsResponse Syntax{
    'securityProfileName': 'string',
    'securityProfileArn': 'string',
    'securityProfileDescription': 'string',
    'behaviors': [
        {
            'name': 'string',
            'metric': 'string',
            'metricDimension': {
                'dimensionName': 'string',
                'operator': 'IN'|'NOT_IN'
            },
            'criteria': {
                'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                'value': {
                    'count': 123,
                    'cidrs': [
                        'string',
                    ],
                    'ports': [
                        123,
                    ]
                },
                'durationSeconds': 123,
                'consecutiveDatapointsToAlarm': 123,
                'consecutiveDatapointsToClear': 123,
                'statisticalThreshold': {
                    'statistic': 'string'
                }
            }
        },
    ],
    'alertTargets': {
        'string': {
            'alertTargetArn': 'string',
            'roleArn': 'string'
        }
    },
    'additionalMetricsToRetain': [
        'string',
    ],
    'additionalMetricsToRetainV2': [
        {
            'metric': 'string',
            'metricDimension': {
                'dimensionName': 'string',
                'operator': 'IN'|'NOT_IN'
            }
        },
    ],
    'version': 123,
    'creationDate': datetime(2015, 1, 1),
    'lastModifiedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --
securityProfileName (string) --The name of the security profile.

securityProfileArn (string) --The ARN of the security profile.

securityProfileDescription (string) --A description of the security profile (associated with the security profile when it was created or updated).

behaviors (list) --Specifies the behaviors that, when violated by a device (thing), cause an alert.

(dict) --A Device Defender security profile behavior.

name (string) --The name you have given to the behavior.

metric (string) --What is measured by the behavior.

metricDimension (dict) --The dimension for a metric in your behavior. For example, using a TOPIC_FILTER dimension, you can narrow down the scope of the metric only to MQTT topics whose name match the pattern specified in the dimension.

dimensionName (string) --A unique identifier for the dimension.

operator (string) --Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .



criteria (dict) --The criteria that determine if a device is behaving normally in regard to the metric .

comparisonOperator (string) --The operator that relates the thing measured (metric ) to the criteria (containing a value or statisticalThreshold ).

value (dict) --The value to be compared with the metric .

count (integer) --If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .

cidrs (list) --If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .

(string) --


ports (list) --If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .

(integer) --




durationSeconds (integer) --Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ). For a statisticalThreshhold metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.

consecutiveDatapointsToAlarm (integer) --If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.

consecutiveDatapointsToClear (integer) --If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.

statisticalThreshold (dict) --A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

statistic (string) --The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (durationSeconds ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (comparisonOperator ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.









alertTargets (dict) --Where the alerts are sent. (Alerts are always sent to the console.)

(string) --The type of alert target: one of "SNS".

(dict) --A structure containing the alert target ARN and the role ARN.

alertTargetArn (string) --The ARN of the notification target to which alerts are sent.

roleArn (string) --The ARN of the role that grants permission to send alerts to the notification target.







additionalMetricsToRetain (list) --A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile\'s behaviors , but it is also retained for any metric specified here.

Note: This API field is deprecated. Please use  DescribeSecurityProfileResponse$additionalMetricsToRetainV2 instead.

(string) --


additionalMetricsToRetainV2 (list) --A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile\'s behaviors, but it is also retained for any metric specified here.

(dict) --The metric you want to retain. Dimensions are optional.

metric (string) --What is measured by the behavior.

metricDimension (dict) --The dimension of a metric.

dimensionName (string) --A unique identifier for the dimension.

operator (string) --Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .







version (integer) --The version of the security profile. A new version is generated whenever the security profile is updated.

creationDate (datetime) --The time the security profile was created.

lastModifiedDate (datetime) --The time the security profile was last modified.






Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'securityProfileName': 'string',
        'securityProfileArn': 'string',
        'securityProfileDescription': 'string',
        'behaviors': [
            {
                'name': 'string',
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                },
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123,
                    'consecutiveDatapointsToAlarm': 123,
                    'consecutiveDatapointsToClear': 123,
                    'statisticalThreshold': {
                        'statistic': 'string'
                    }
                }
            },
        ],
        'alertTargets': {
            'string': {
                'alertTargetArn': 'string',
                'roleArn': 'string'
            }
        },
        'additionalMetricsToRetain': [
            'string',
        ],
        'additionalMetricsToRetainV2': [
            {
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                }
            },
        ],
        'version': 123,
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

def describe_stream(streamId=None):
    """
    Gets information about a stream.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_stream(
        streamId='string'
    )
    
    
    :type streamId: string
    :param streamId: [REQUIRED]\nThe stream ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'streamInfo': {
        'streamId': 'string',
        'streamArn': 'string',
        'streamVersion': 123,
        'description': 'string',
        'files': [
            {
                'fileId': 123,
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'version': 'string'
                }
            },
        ],
        'createdAt': datetime(2015, 1, 1),
        'lastUpdatedAt': datetime(2015, 1, 1),
        'roleArn': 'string'
    }
}


Response Structure

(dict) --
streamInfo (dict) --Information about the stream.

streamId (string) --The stream ID.

streamArn (string) --The stream ARN.

streamVersion (integer) --The stream version.

description (string) --The description of the stream.

files (list) --The files to stream.

(dict) --Represents a file to stream.

fileId (integer) --The file ID.

s3Location (dict) --The location of the file in S3.

bucket (string) --The S3 bucket.

key (string) --The S3 key.

version (string) --The S3 bucket version.







createdAt (datetime) --The date when the stream was created.

lastUpdatedAt (datetime) --The date when the stream was last updated.

roleArn (string) --An IAM role AWS IoT assumes to access your S3 files.








Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'streamInfo': {
            'streamId': 'string',
            'streamArn': 'string',
            'streamVersion': 123,
            'description': 'string',
            'files': [
                {
                    'fileId': 123,
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'version': 'string'
                    }
                },
            ],
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'roleArn': 'string'
        }
    }
    
    
    """
    pass

def describe_thing(thingName=None):
    """
    Gets information about the specified thing.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_thing(
        thingName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing.\n

    :rtype: dict
ReturnsResponse Syntax{
    'defaultClientId': 'string',
    'thingName': 'string',
    'thingId': 'string',
    'thingArn': 'string',
    'thingTypeName': 'string',
    'attributes': {
        'string': 'string'
    },
    'version': 123,
    'billingGroupName': 'string'
}


Response Structure

(dict) --The output from the DescribeThing operation.

defaultClientId (string) --The default MQTT client ID. For a typical device, the thing name is also used as the default MQTT client ID. Although we don\xe2\x80\x99t require a mapping between a thing\'s registry name and its use of MQTT client IDs, certificates, or shadow state, we recommend that you choose a thing name and use it as the MQTT client ID for the registry and the Device Shadow service.
This lets you better organize your AWS IoT fleet without removing the flexibility of the underlying device certificate model or shadows.

thingName (string) --The name of the thing.

thingId (string) --The ID of the thing to describe.

thingArn (string) --The ARN of the thing to describe.

thingTypeName (string) --The thing type name.

attributes (dict) --The thing attributes.

(string) --
(string) --




version (integer) --The current version of the thing record in the registry.

Note
To avoid unintentional changes to the information in the registry, you can pass the version information in the expectedVersion parameter of the UpdateThing and DeleteThing calls.


billingGroupName (string) --The name of the billing group the thing belongs to.






Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'defaultClientId': 'string',
        'thingName': 'string',
        'thingId': 'string',
        'thingArn': 'string',
        'thingTypeName': 'string',
        'attributes': {
            'string': 'string'
        },
        'version': 123,
        'billingGroupName': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def describe_thing_group(thingGroupName=None):
    """
    Describe a thing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_thing_group(
        thingGroupName='string'
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]\nThe name of the thing group.\n

    :rtype: dict
ReturnsResponse Syntax{
    'thingGroupName': 'string',
    'thingGroupId': 'string',
    'thingGroupArn': 'string',
    'version': 123,
    'thingGroupProperties': {
        'thingGroupDescription': 'string',
        'attributePayload': {
            'attributes': {
                'string': 'string'
            },
            'merge': True|False
        }
    },
    'thingGroupMetadata': {
        'parentGroupName': 'string',
        'rootToParentThingGroups': [
            {
                'groupName': 'string',
                'groupArn': 'string'
            },
        ],
        'creationDate': datetime(2015, 1, 1)
    },
    'indexName': 'string',
    'queryString': 'string',
    'queryVersion': 'string',
    'status': 'ACTIVE'|'BUILDING'|'REBUILDING'
}


Response Structure

(dict) --
thingGroupName (string) --The name of the thing group.

thingGroupId (string) --The thing group ID.

thingGroupArn (string) --The thing group ARN.

version (integer) --The version of the thing group.

thingGroupProperties (dict) --The thing group properties.

thingGroupDescription (string) --The thing group description.

attributePayload (dict) --The thing group attributes in JSON format.

attributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:

{\\"attributes\\":{\\"string1\\":\\"string2\\"}}

(string) --
(string) --




merge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.
To remove an attribute, call UpdateThing with an empty attribute value.

Note
The merge attribute is only valid when calling UpdateThing or UpdateThingGroup .






thingGroupMetadata (dict) --Thing group metadata.

parentGroupName (string) --The parent thing group name.

rootToParentThingGroups (list) --The root parent thing group.

(dict) --The name and ARN of a group.

groupName (string) --The group name.

groupArn (string) --The group ARN.





creationDate (datetime) --The UNIX timestamp of when the thing group was created.



indexName (string) --The dynamic thing group index name.

queryString (string) --The dynamic thing group search query string.

queryVersion (string) --The dynamic thing group query version.

status (string) --The dynamic thing group status.






Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'thingGroupName': 'string',
        'thingGroupId': 'string',
        'thingGroupArn': 'string',
        'version': 123,
        'thingGroupProperties': {
            'thingGroupDescription': 'string',
            'attributePayload': {
                'attributes': {
                    'string': 'string'
                },
                'merge': True|False
            }
        },
        'thingGroupMetadata': {
            'parentGroupName': 'string',
            'rootToParentThingGroups': [
                {
                    'groupName': 'string',
                    'groupArn': 'string'
                },
            ],
            'creationDate': datetime(2015, 1, 1)
        },
        'indexName': 'string',
        'queryString': 'string',
        'queryVersion': 'string',
        'status': 'ACTIVE'|'BUILDING'|'REBUILDING'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def describe_thing_registration_task(taskId=None):
    """
    Describes a bulk thing provisioning task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_thing_registration_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]\nThe task ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'taskId': 'string',
    'creationDate': datetime(2015, 1, 1),
    'lastModifiedDate': datetime(2015, 1, 1),
    'templateBody': 'string',
    'inputFileBucket': 'string',
    'inputFileKey': 'string',
    'roleArn': 'string',
    'status': 'InProgress'|'Completed'|'Failed'|'Cancelled'|'Cancelling',
    'message': 'string',
    'successCount': 123,
    'failureCount': 123,
    'percentageProgress': 123
}


Response Structure

(dict) --
taskId (string) --The task ID.

creationDate (datetime) --The task creation date.

lastModifiedDate (datetime) --The date when the task was last modified.

templateBody (string) --The task\'s template.

inputFileBucket (string) --The S3 bucket that contains the input file.

inputFileKey (string) --The input file key.

roleArn (string) --The role ARN that grants access to the input file bucket.

status (string) --The status of the bulk thing provisioning task.

message (string) --The message.

successCount (integer) --The number of things successfully provisioned.

failureCount (integer) --The number of things that failed to be provisioned.

percentageProgress (integer) --The progress of the bulk provisioning task expressed as a percentage.






Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'taskId': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'templateBody': 'string',
        'inputFileBucket': 'string',
        'inputFileKey': 'string',
        'roleArn': 'string',
        'status': 'InProgress'|'Completed'|'Failed'|'Cancelled'|'Cancelling',
        'message': 'string',
        'successCount': 123,
        'failureCount': 123,
        'percentageProgress': 123
    }
    
    
    """
    pass

def describe_thing_type(thingTypeName=None):
    """
    Gets information about the specified thing type.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_thing_type(
        thingTypeName='string'
    )
    
    
    :type thingTypeName: string
    :param thingTypeName: [REQUIRED]\nThe name of the thing type.\n

    :rtype: dict
ReturnsResponse Syntax{
    'thingTypeName': 'string',
    'thingTypeId': 'string',
    'thingTypeArn': 'string',
    'thingTypeProperties': {
        'thingTypeDescription': 'string',
        'searchableAttributes': [
            'string',
        ]
    },
    'thingTypeMetadata': {
        'deprecated': True|False,
        'deprecationDate': datetime(2015, 1, 1),
        'creationDate': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --The output for the DescribeThingType operation.

thingTypeName (string) --The name of the thing type.

thingTypeId (string) --The thing type ID.

thingTypeArn (string) --The thing type ARN.

thingTypeProperties (dict) --The ThingTypeProperties contains information about the thing type including description, and a list of searchable thing attribute names.

thingTypeDescription (string) --The description of the thing type.

searchableAttributes (list) --A list of searchable thing attribute names.

(string) --




thingTypeMetadata (dict) --The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.

deprecated (boolean) --Whether the thing type is deprecated. If true , no new things could be associated with this type.

deprecationDate (datetime) --The date and time when the thing type was deprecated.

creationDate (datetime) --The date and time when the thing type was created.








Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'thingTypeName': 'string',
        'thingTypeId': 'string',
        'thingTypeArn': 'string',
        'thingTypeProperties': {
            'thingTypeDescription': 'string',
            'searchableAttributes': [
                'string',
            ]
        },
        'thingTypeMetadata': {
            'deprecated': True|False,
            'deprecationDate': datetime(2015, 1, 1),
            'creationDate': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def detach_policy(policyName=None, target=None):
    """
    Detaches a policy from the specified target.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_policy(
        policyName='string',
        target='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe policy to detach.\n

    :type target: string
    :param target: [REQUIRED]\nThe target from which the policy will be detached.\n

    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.LimitExceededException
    
    """
    pass

def detach_principal_policy(policyName=None, principal=None):
    """
    Removes the specified policy from the specified certificate.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_principal_policy(
        policyName='string',
        principal='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe name of the policy to detach.\n

    :type principal: string
    :param principal: [REQUIRED]\nThe principal.\nIf the principal is a certificate, specify the certificate ARN. If the principal is an Amazon Cognito identity, specify the identity ID.\n

    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def detach_security_profile(securityProfileName=None, securityProfileTargetArn=None):
    """
    Disassociates a Device Defender security profile from a thing group or from this account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_security_profile(
        securityProfileName='string',
        securityProfileTargetArn='string'
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]\nThe security profile that is detached.\n

    :type securityProfileTargetArn: string
    :param securityProfileTargetArn: [REQUIRED]\nThe ARN of the thing group from which the security profile is detached.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def detach_thing_principal(thingName=None, principal=None):
    """
    Detaches the specified principal from the specified thing. A principal can be X.509 certificates, IAM users, groups, and roles, Amazon Cognito identities or federated identities.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.detach_thing_principal(
        thingName='string',
        principal='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing.\n

    :type principal: string
    :param principal: [REQUIRED]\nIf the principal is a certificate, this value must be ARN of the certificate. If the principal is an Amazon Cognito identity, this value must be the ID of the Amazon Cognito identity.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The output from the DetachThingPrincipal operation.





Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def disable_topic_rule(ruleName=None):
    """
    Disables the rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.disable_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]\nThe name of the rule to disable.\n

    """
    pass

def enable_topic_rule(ruleName=None):
    """
    Enables the rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.enable_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]\nThe name of the topic rule to enable.\n

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

def get_cardinality(indexName=None, queryString=None, aggregationField=None, queryVersion=None):
    """
    Returns the approximate count of unique values that match the query.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_cardinality(
        indexName='string',
        queryString='string',
        aggregationField='string',
        queryVersion='string'
    )
    
    
    :type indexName: string
    :param indexName: The name of the index to search.

    :type queryString: string
    :param queryString: [REQUIRED]\nThe search query.\n

    :type aggregationField: string
    :param aggregationField: The field to aggregate.

    :type queryVersion: string
    :param queryVersion: The query version.

    :rtype: dict

ReturnsResponse Syntax
{
    'cardinality': 123
}


Response Structure

(dict) --

cardinality (integer) --
The approximate count of unique values that match the query.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidQueryException
IoT.Client.exceptions.InvalidAggregationException
IoT.Client.exceptions.IndexNotReadyException


    :return: {
        'cardinality': 123
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidQueryException
    IoT.Client.exceptions.InvalidAggregationException
    IoT.Client.exceptions.IndexNotReadyException
    
    """
    pass

def get_effective_policies(principal=None, cognitoIdentityPoolId=None, thingName=None):
    """
    Gets a list of the policies that have an effect on the authorization behavior of the specified device when it connects to the AWS IoT device gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_effective_policies(
        principal='string',
        cognitoIdentityPoolId='string',
        thingName='string'
    )
    
    
    :type principal: string
    :param principal: The principal.

    :type cognitoIdentityPoolId: string
    :param cognitoIdentityPoolId: The Cognito identity pool ID.

    :type thingName: string
    :param thingName: The thing name.

    :rtype: dict

ReturnsResponse Syntax
{
    'effectivePolicies': [
        {
            'policyName': 'string',
            'policyArn': 'string',
            'policyDocument': 'string'
        },
    ]
}


Response Structure

(dict) --

effectivePolicies (list) --
The effective policies.

(dict) --
The policy that has the effect on the authorization results.

policyName (string) --
The policy name.

policyArn (string) --
The policy ARN.

policyDocument (string) --
The IAM policy document.











Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.LimitExceededException


    :return: {
        'effectivePolicies': [
            {
                'policyName': 'string',
                'policyArn': 'string',
                'policyDocument': 'string'
            },
        ]
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.LimitExceededException
    
    """
    pass

def get_indexing_configuration():
    """
    Gets the indexing configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_indexing_configuration()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'thingIndexingConfiguration': {
        'thingIndexingMode': 'OFF'|'REGISTRY'|'REGISTRY_AND_SHADOW',
        'thingConnectivityIndexingMode': 'OFF'|'STATUS',
        'managedFields': [
            {
                'name': 'string',
                'type': 'Number'|'String'|'Boolean'
            },
        ],
        'customFields': [
            {
                'name': 'string',
                'type': 'Number'|'String'|'Boolean'
            },
        ]
    },
    'thingGroupIndexingConfiguration': {
        'thingGroupIndexingMode': 'OFF'|'ON',
        'managedFields': [
            {
                'name': 'string',
                'type': 'Number'|'String'|'Boolean'
            },
        ],
        'customFields': [
            {
                'name': 'string',
                'type': 'Number'|'String'|'Boolean'
            },
        ]
    }
}


Response Structure

(dict) --
thingIndexingConfiguration (dict) --Thing indexing configuration.

thingIndexingMode (string) --Thing indexing mode. Valid values are:

REGISTRY \xe2\x80\x93 Your thing index contains registry data only.
REGISTRY_AND_SHADOW - Your thing index contains registry and shadow data.
OFF - Thing indexing is disabled.


thingConnectivityIndexingMode (string) --Thing connectivity indexing mode. Valid values are:

STATUS \xe2\x80\x93 Your thing index contains connectivity status. To enable thing connectivity indexing, thingIndexMode must not be set to OFF.
OFF - Thing connectivity status indexing is disabled.


managedFields (list) --Contains fields that are indexed and whose types are already known by the Fleet Indexing service.

(dict) --Describes the name and data type at a field.

name (string) --The name of the field.

type (string) --The datatype of the field.





customFields (list) --Contains custom field names and their data type.

(dict) --Describes the name and data type at a field.

name (string) --The name of the field.

type (string) --The datatype of the field.







thingGroupIndexingConfiguration (dict) --The index configuration.

thingGroupIndexingMode (string) --Thing group indexing mode.

managedFields (list) --Contains fields that are indexed and whose types are already known by the Fleet Indexing service.

(dict) --Describes the name and data type at a field.

name (string) --The name of the field.

type (string) --The datatype of the field.





customFields (list) --A list of thing group fields to index. This list cannot contain any managed fields. Use the GetIndexingConfiguration API to get a list of managed fields.
Contains custom field names and their data type.

(dict) --Describes the name and data type at a field.

name (string) --The name of the field.

type (string) --The datatype of the field.












Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'thingIndexingConfiguration': {
            'thingIndexingMode': 'OFF'|'REGISTRY'|'REGISTRY_AND_SHADOW',
            'thingConnectivityIndexingMode': 'OFF'|'STATUS',
            'managedFields': [
                {
                    'name': 'string',
                    'type': 'Number'|'String'|'Boolean'
                },
            ],
            'customFields': [
                {
                    'name': 'string',
                    'type': 'Number'|'String'|'Boolean'
                },
            ]
        },
        'thingGroupIndexingConfiguration': {
            'thingGroupIndexingMode': 'OFF'|'ON',
            'managedFields': [
                {
                    'name': 'string',
                    'type': 'Number'|'String'|'Boolean'
                },
            ],
            'customFields': [
                {
                    'name': 'string',
                    'type': 'Number'|'String'|'Boolean'
                },
            ]
        }
    }
    
    
    :returns: 
    STATUS \xe2\x80\x93 Your thing index contains connectivity status. To enable thing connectivity indexing, thingIndexMode must not be set to OFF.
    OFF - Thing connectivity status indexing is disabled.
    
    """
    pass

def get_job_document(jobId=None):
    """
    Gets a job document.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_job_document(
        jobId='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique identifier you assigned to this job when it was created.\n

    :rtype: dict
ReturnsResponse Syntax{
    'document': 'string'
}


Response Structure

(dict) --
document (string) --The job document content.






Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'document': 'string'
    }
    
    
    """
    pass

def get_logging_options():
    """
    Gets the logging options.
    NOTE: use of this command is not recommended. Use GetV2LoggingOptions instead.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_logging_options()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'roleArn': 'string',
    'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
}


Response Structure

(dict) --The output from the GetLoggingOptions operation.

roleArn (string) --The ARN of the IAM role that grants access.

logLevel (string) --The logging level.






Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'roleArn': 'string',
        'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
    }
    
    
    """
    pass

def get_ota_update(otaUpdateId=None):
    """
    Gets an OTA update.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_ota_update(
        otaUpdateId='string'
    )
    
    
    :type otaUpdateId: string
    :param otaUpdateId: [REQUIRED]\nThe OTA update ID.\n

    :rtype: dict
ReturnsResponse Syntax{
    'otaUpdateInfo': {
        'otaUpdateId': 'string',
        'otaUpdateArn': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'description': 'string',
        'targets': [
            'string',
        ],
        'protocols': [
            'MQTT'|'HTTP',
        ],
        'awsJobExecutionsRolloutConfig': {
            'maximumPerMinute': 123
        },
        'awsJobPresignedUrlConfig': {
            'expiresInSec': 123
        },
        'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
        'otaUpdateFiles': [
            {
                'fileName': 'string',
                'fileVersion': 'string',
                'fileLocation': {
                    'stream': {
                        'streamId': 'string',
                        'fileId': 123
                    },
                    's3Location': {
                        'bucket': 'string',
                        'key': 'string',
                        'version': 'string'
                    }
                },
                'codeSigning': {
                    'awsSignerJobId': 'string',
                    'startSigningJobParameter': {
                        'signingProfileParameter': {
                            'certificateArn': 'string',
                            'platform': 'string',
                            'certificatePathOnDevice': 'string'
                        },
                        'signingProfileName': 'string',
                        'destination': {
                            's3Destination': {
                                'bucket': 'string',
                                'prefix': 'string'
                            }
                        }
                    },
                    'customCodeSigning': {
                        'signature': {
                            'inlineDocument': b'bytes'
                        },
                        'certificateChain': {
                            'certificateName': 'string',
                            'inlineDocument': 'string'
                        },
                        'hashAlgorithm': 'string',
                        'signatureAlgorithm': 'string'
                    }
                },
                'attributes': {
                    'string': 'string'
                }
            },
        ],
        'otaUpdateStatus': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED',
        'awsIotJobId': 'string',
        'awsIotJobArn': 'string',
        'errorInfo': {
            'code': 'string',
            'message': 'string'
        },
        'additionalParameters': {
            'string': 'string'
        }
    }
}


Response Structure

(dict) --
otaUpdateInfo (dict) --The OTA update info.

otaUpdateId (string) --The OTA update ID.

otaUpdateArn (string) --The OTA update ARN.

creationDate (datetime) --The date when the OTA update was created.

lastModifiedDate (datetime) --The date when the OTA update was last updated.

description (string) --A description of the OTA update.

targets (list) --The targets of the OTA update.

(string) --


protocols (list) --The protocol used to transfer the OTA update image. Valid values are [HTTP], [MQTT], [HTTP, MQTT]. When both HTTP and MQTT are specified, the target device can choose the protocol.

(string) --


awsJobExecutionsRolloutConfig (dict) --Configuration for the rollout of OTA updates.

maximumPerMinute (integer) --The maximum number of OTA update job executions started per minute.



awsJobPresignedUrlConfig (dict) --Configuration information for pre-signed URLs. Valid when protocols contains HTTP.

expiresInSec (integer) --How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 1800 seconds. Pre-signed URLs are generated when a request for the job document is received.



targetSelection (string) --Specifies whether the OTA update will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the OTA update (SNAPSHOT). If continuous, the OTA update may also be run on a thing when a change is detected in a target. For example, an OTA update will run on a thing when the thing is added to a target group, even after the OTA update was completed by all things originally in the group.

otaUpdateFiles (list) --A list of files associated with the OTA update.

(dict) --Describes a file to be associated with an OTA update.

fileName (string) --The name of the file.

fileVersion (string) --The file version.

fileLocation (dict) --The location of the updated firmware.

stream (dict) --The stream that contains the OTA update.

streamId (string) --The stream ID.

fileId (integer) --The ID of a file associated with a stream.



s3Location (dict) --The location of the updated firmware in S3.

bucket (string) --The S3 bucket.

key (string) --The S3 key.

version (string) --The S3 bucket version.





codeSigning (dict) --The code signing method of the file.

awsSignerJobId (string) --The ID of the AWSSignerJob which was created to sign the file.

startSigningJobParameter (dict) --Describes the code-signing job.

signingProfileParameter (dict) --Describes the code-signing profile.

certificateArn (string) --Certificate ARN.

platform (string) --The hardware platform of your device.

certificatePathOnDevice (string) --The location of the code-signing certificate on your device.



signingProfileName (string) --The code-signing profile name.

destination (dict) --The location to write the code-signed file.

s3Destination (dict) --Describes the location in S3 of the updated firmware.

bucket (string) --The S3 bucket that contains the updated firmware.

prefix (string) --The S3 prefix.







customCodeSigning (dict) --A custom method for code signing a file.

signature (dict) --The signature for the file.

inlineDocument (bytes) --A base64 encoded binary representation of the code signing signature.



certificateChain (dict) --The certificate chain.

certificateName (string) --The name of the certificate.

inlineDocument (string) --A base64 encoded binary representation of the code signing certificate chain.



hashAlgorithm (string) --The hash algorithm used to code sign the file.

signatureAlgorithm (string) --The signature algorithm used to code sign the file.





attributes (dict) --A list of name/attribute pairs.

(string) --
(string) --








otaUpdateStatus (string) --The status of the OTA update.

awsIotJobId (string) --The AWS IoT job ID associated with the OTA update.

awsIotJobArn (string) --The AWS IoT job ARN associated with the OTA update.

errorInfo (dict) --Error information associated with the OTA update.

code (string) --The error code.

message (string) --The error message.



additionalParameters (dict) --A collection of name/value pairs

(string) --
(string) --











Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'otaUpdateInfo': {
            'otaUpdateId': 'string',
            'otaUpdateArn': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'description': 'string',
            'targets': [
                'string',
            ],
            'protocols': [
                'MQTT'|'HTTP',
            ],
            'awsJobExecutionsRolloutConfig': {
                'maximumPerMinute': 123
            },
            'awsJobPresignedUrlConfig': {
                'expiresInSec': 123
            },
            'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
            'otaUpdateFiles': [
                {
                    'fileName': 'string',
                    'fileVersion': 'string',
                    'fileLocation': {
                        'stream': {
                            'streamId': 'string',
                            'fileId': 123
                        },
                        's3Location': {
                            'bucket': 'string',
                            'key': 'string',
                            'version': 'string'
                        }
                    },
                    'codeSigning': {
                        'awsSignerJobId': 'string',
                        'startSigningJobParameter': {
                            'signingProfileParameter': {
                                'certificateArn': 'string',
                                'platform': 'string',
                                'certificatePathOnDevice': 'string'
                            },
                            'signingProfileName': 'string',
                            'destination': {
                                's3Destination': {
                                    'bucket': 'string',
                                    'prefix': 'string'
                                }
                            }
                        },
                        'customCodeSigning': {
                            'signature': {
                                'inlineDocument': b'bytes'
                            },
                            'certificateChain': {
                                'certificateName': 'string',
                                'inlineDocument': 'string'
                            },
                            'hashAlgorithm': 'string',
                            'signatureAlgorithm': 'string'
                        }
                    },
                    'attributes': {
                        'string': 'string'
                    }
                },
            ],
            'otaUpdateStatus': 'CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED',
            'awsIotJobId': 'string',
            'awsIotJobArn': 'string',
            'errorInfo': {
                'code': 'string',
                'message': 'string'
            },
            'additionalParameters': {
                'string': 'string'
            }
        }
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

def get_percentiles(indexName=None, queryString=None, aggregationField=None, queryVersion=None, percents=None):
    """
    Groups the aggregated values that match the query into percentile groupings. The default percentile groupings are: 1,5,25,50,75,95,99, although you can specify your own when you call GetPercentiles . This function returns a value for each percentile group specified (or the default percentile groupings). The percentile group "1" contains the aggregated field value that occurs in approximately one percent of the values that match the query. The percentile group "5" contains the aggregated field value that occurs in approximately five percent of the values that match the query, and so on. The result is an approximation, the more values that match the query, the more accurate the percentile values.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_percentiles(
        indexName='string',
        queryString='string',
        aggregationField='string',
        queryVersion='string',
        percents=[
            123.0,
        ]
    )
    
    
    :type indexName: string
    :param indexName: The name of the index to search.

    :type queryString: string
    :param queryString: [REQUIRED]\nThe query string.\n

    :type aggregationField: string
    :param aggregationField: The field to aggregate.

    :type queryVersion: string
    :param queryVersion: The query version.

    :type percents: list
    :param percents: The percentile groups returned.\n\n(float) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'percentiles': [
        {
            'percent': 123.0,
            'value': 123.0
        },
    ]
}


Response Structure

(dict) --

percentiles (list) --
The percentile values of the aggregated fields.

(dict) --
Describes the percentile and percentile value.

percent (float) --
The percentile.

value (float) --
The value of the percentile.











Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidQueryException
IoT.Client.exceptions.InvalidAggregationException
IoT.Client.exceptions.IndexNotReadyException


    :return: {
        'percentiles': [
            {
                'percent': 123.0,
                'value': 123.0
            },
        ]
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidQueryException
    IoT.Client.exceptions.InvalidAggregationException
    IoT.Client.exceptions.IndexNotReadyException
    
    """
    pass

def get_policy(policyName=None):
    """
    Gets information about the specified policy with the policy document of the default version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_policy(
        policyName='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe name of the policy.\n

    :rtype: dict
ReturnsResponse Syntax{
    'policyName': 'string',
    'policyArn': 'string',
    'policyDocument': 'string',
    'defaultVersionId': 'string',
    'creationDate': datetime(2015, 1, 1),
    'lastModifiedDate': datetime(2015, 1, 1),
    'generationId': 'string'
}


Response Structure

(dict) --The output from the GetPolicy operation.

policyName (string) --The policy name.

policyArn (string) --The policy ARN.

policyDocument (string) --The JSON document that describes the policy.

defaultVersionId (string) --The default policy version ID.

creationDate (datetime) --The date the policy was created.

lastModifiedDate (datetime) --The date the policy was last modified.

generationId (string) --The generation ID of the policy.






Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'policyName': 'string',
        'policyArn': 'string',
        'policyDocument': 'string',
        'defaultVersionId': 'string',
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'generationId': 'string'
    }
    
    
    """
    pass

def get_policy_version(policyName=None, policyVersionId=None):
    """
    Gets information about the specified policy version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_policy_version(
        policyName='string',
        policyVersionId='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe name of the policy.\n

    :type policyVersionId: string
    :param policyVersionId: [REQUIRED]\nThe policy version ID.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'policyArn': 'string',
    'policyName': 'string',
    'policyDocument': 'string',
    'policyVersionId': 'string',
    'isDefaultVersion': True|False,
    'creationDate': datetime(2015, 1, 1),
    'lastModifiedDate': datetime(2015, 1, 1),
    'generationId': 'string'
}


Response Structure

(dict) --
The output from the GetPolicyVersion operation.

policyArn (string) --
The policy ARN.

policyName (string) --
The policy name.

policyDocument (string) --
The JSON document that describes the policy.

policyVersionId (string) --
The policy version ID.

isDefaultVersion (boolean) --
Specifies whether the policy version is the default.

creationDate (datetime) --
The date the policy was created.

lastModifiedDate (datetime) --
The date the policy was last modified.

generationId (string) --
The generation ID of the policy version.







Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'policyArn': 'string',
        'policyName': 'string',
        'policyDocument': 'string',
        'policyVersionId': 'string',
        'isDefaultVersion': True|False,
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1),
        'generationId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def get_registration_code():
    """
    Gets a registration code used to register a CA certificate with AWS IoT.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_registration_code()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'registrationCode': 'string'
}


Response Structure

(dict) --The output from the GetRegistrationCode operation.

registrationCode (string) --The CA certificate registration code.






Exceptions

IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException


    :return: {
        'registrationCode': 'string'
    }
    
    
    """
    pass

def get_statistics(indexName=None, queryString=None, aggregationField=None, queryVersion=None):
    """
    Returns the count, average, sum, minimum, maximum, sum of squares, variance, and standard deviation for the specified aggregated field. If the aggregation field is of type String , only the count statistic is returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_statistics(
        indexName='string',
        queryString='string',
        aggregationField='string',
        queryVersion='string'
    )
    
    
    :type indexName: string
    :param indexName: The name of the index to search. The default value is AWS_Things .

    :type queryString: string
    :param queryString: [REQUIRED]\nThe query used to search. You can specify '*' for the query string to get the count of all indexed things in your AWS account.\n

    :type aggregationField: string
    :param aggregationField: The aggregation field name.

    :type queryVersion: string
    :param queryVersion: The version of the query used to search.

    :rtype: dict

ReturnsResponse Syntax
{
    'statistics': {
        'count': 123,
        'average': 123.0,
        'sum': 123.0,
        'minimum': 123.0,
        'maximum': 123.0,
        'sumOfSquares': 123.0,
        'variance': 123.0,
        'stdDeviation': 123.0
    }
}


Response Structure

(dict) --

statistics (dict) --
The statistics returned by the Fleet Indexing service based on the query and aggregation field.

count (integer) --
The count of things that match the query.

average (float) --
The average of the aggregated field values.

sum (float) --
The sum of the aggregated field values.

minimum (float) --
The minimum aggregated field value.

maximum (float) --
The maximum aggregated field value.

sumOfSquares (float) --
The sum of the squares of the aggregated field values.

variance (float) --
The variance of the aggregated field values.

stdDeviation (float) --
The standard deviation of the aggregated field values.









Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidQueryException
IoT.Client.exceptions.InvalidAggregationException
IoT.Client.exceptions.IndexNotReadyException


    :return: {
        'statistics': {
            'count': 123,
            'average': 123.0,
            'sum': 123.0,
            'minimum': 123.0,
            'maximum': 123.0,
            'sumOfSquares': 123.0,
            'variance': 123.0,
            'stdDeviation': 123.0
        }
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidQueryException
    IoT.Client.exceptions.InvalidAggregationException
    IoT.Client.exceptions.IndexNotReadyException
    
    """
    pass

def get_topic_rule(ruleName=None):
    """
    Gets information about the rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_topic_rule(
        ruleName='string'
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]\nThe name of the rule.\n

    :rtype: dict
ReturnsResponse Syntax{
    'ruleArn': 'string',
    'rule': {
        'ruleName': 'string',
        'sql': 'string',
        'description': 'string',
        'createdAt': datetime(2015, 1, 1),
        'actions': [
            {
                'dynamoDB': {
                    'tableName': 'string',
                    'roleArn': 'string',
                    'operation': 'string',
                    'hashKeyField': 'string',
                    'hashKeyValue': 'string',
                    'hashKeyType': 'STRING'|'NUMBER',
                    'rangeKeyField': 'string',
                    'rangeKeyValue': 'string',
                    'rangeKeyType': 'STRING'|'NUMBER',
                    'payloadField': 'string'
                },
                'dynamoDBv2': {
                    'roleArn': 'string',
                    'putItem': {
                        'tableName': 'string'
                    }
                },
                'lambda': {
                    'functionArn': 'string'
                },
                'sns': {
                    'targetArn': 'string',
                    'roleArn': 'string',
                    'messageFormat': 'RAW'|'JSON'
                },
                'sqs': {
                    'roleArn': 'string',
                    'queueUrl': 'string',
                    'useBase64': True|False
                },
                'kinesis': {
                    'roleArn': 'string',
                    'streamName': 'string',
                    'partitionKey': 'string'
                },
                'republish': {
                    'roleArn': 'string',
                    'topic': 'string',
                    'qos': 123
                },
                's3': {
                    'roleArn': 'string',
                    'bucketName': 'string',
                    'key': 'string',
                    'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                },
                'firehose': {
                    'roleArn': 'string',
                    'deliveryStreamName': 'string',
                    'separator': 'string'
                },
                'cloudwatchMetric': {
                    'roleArn': 'string',
                    'metricNamespace': 'string',
                    'metricName': 'string',
                    'metricValue': 'string',
                    'metricUnit': 'string',
                    'metricTimestamp': 'string'
                },
                'cloudwatchAlarm': {
                    'roleArn': 'string',
                    'alarmName': 'string',
                    'stateReason': 'string',
                    'stateValue': 'string'
                },
                'cloudwatchLogs': {
                    'roleArn': 'string',
                    'logGroupName': 'string'
                },
                'elasticsearch': {
                    'roleArn': 'string',
                    'endpoint': 'string',
                    'index': 'string',
                    'type': 'string',
                    'id': 'string'
                },
                'salesforce': {
                    'token': 'string',
                    'url': 'string'
                },
                'iotAnalytics': {
                    'channelArn': 'string',
                    'channelName': 'string',
                    'roleArn': 'string'
                },
                'iotEvents': {
                    'inputName': 'string',
                    'messageId': 'string',
                    'roleArn': 'string'
                },
                'iotSiteWise': {
                    'putAssetPropertyValueEntries': [
                        {
                            'entryId': 'string',
                            'assetId': 'string',
                            'propertyId': 'string',
                            'propertyAlias': 'string',
                            'propertyValues': [
                                {
                                    'value': {
                                        'stringValue': 'string',
                                        'integerValue': 'string',
                                        'doubleValue': 'string',
                                        'booleanValue': 'string'
                                    },
                                    'timestamp': {
                                        'timeInSeconds': 'string',
                                        'offsetInNanos': 'string'
                                    },
                                    'quality': 'string'
                                },
                            ]
                        },
                    ],
                    'roleArn': 'string'
                },
                'stepFunctions': {
                    'executionNamePrefix': 'string',
                    'stateMachineName': 'string',
                    'roleArn': 'string'
                },
                'http': {
                    'url': 'string',
                    'confirmationUrl': 'string',
                    'headers': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'auth': {
                        'sigv4': {
                            'signingRegion': 'string',
                            'serviceName': 'string',
                            'roleArn': 'string'
                        }
                    }
                }
            },
        ],
        'ruleDisabled': True|False,
        'awsIotSqlVersion': 'string',
        'errorAction': {
            'dynamoDB': {
                'tableName': 'string',
                'roleArn': 'string',
                'operation': 'string',
                'hashKeyField': 'string',
                'hashKeyValue': 'string',
                'hashKeyType': 'STRING'|'NUMBER',
                'rangeKeyField': 'string',
                'rangeKeyValue': 'string',
                'rangeKeyType': 'STRING'|'NUMBER',
                'payloadField': 'string'
            },
            'dynamoDBv2': {
                'roleArn': 'string',
                'putItem': {
                    'tableName': 'string'
                }
            },
            'lambda': {
                'functionArn': 'string'
            },
            'sns': {
                'targetArn': 'string',
                'roleArn': 'string',
                'messageFormat': 'RAW'|'JSON'
            },
            'sqs': {
                'roleArn': 'string',
                'queueUrl': 'string',
                'useBase64': True|False
            },
            'kinesis': {
                'roleArn': 'string',
                'streamName': 'string',
                'partitionKey': 'string'
            },
            'republish': {
                'roleArn': 'string',
                'topic': 'string',
                'qos': 123
            },
            's3': {
                'roleArn': 'string',
                'bucketName': 'string',
                'key': 'string',
                'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
            },
            'firehose': {
                'roleArn': 'string',
                'deliveryStreamName': 'string',
                'separator': 'string'
            },
            'cloudwatchMetric': {
                'roleArn': 'string',
                'metricNamespace': 'string',
                'metricName': 'string',
                'metricValue': 'string',
                'metricUnit': 'string',
                'metricTimestamp': 'string'
            },
            'cloudwatchAlarm': {
                'roleArn': 'string',
                'alarmName': 'string',
                'stateReason': 'string',
                'stateValue': 'string'
            },
            'cloudwatchLogs': {
                'roleArn': 'string',
                'logGroupName': 'string'
            },
            'elasticsearch': {
                'roleArn': 'string',
                'endpoint': 'string',
                'index': 'string',
                'type': 'string',
                'id': 'string'
            },
            'salesforce': {
                'token': 'string',
                'url': 'string'
            },
            'iotAnalytics': {
                'channelArn': 'string',
                'channelName': 'string',
                'roleArn': 'string'
            },
            'iotEvents': {
                'inputName': 'string',
                'messageId': 'string',
                'roleArn': 'string'
            },
            'iotSiteWise': {
                'putAssetPropertyValueEntries': [
                    {
                        'entryId': 'string',
                        'assetId': 'string',
                        'propertyId': 'string',
                        'propertyAlias': 'string',
                        'propertyValues': [
                            {
                                'value': {
                                    'stringValue': 'string',
                                    'integerValue': 'string',
                                    'doubleValue': 'string',
                                    'booleanValue': 'string'
                                },
                                'timestamp': {
                                    'timeInSeconds': 'string',
                                    'offsetInNanos': 'string'
                                },
                                'quality': 'string'
                            },
                        ]
                    },
                ],
                'roleArn': 'string'
            },
            'stepFunctions': {
                'executionNamePrefix': 'string',
                'stateMachineName': 'string',
                'roleArn': 'string'
            },
            'http': {
                'url': 'string',
                'confirmationUrl': 'string',
                'headers': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'auth': {
                    'sigv4': {
                        'signingRegion': 'string',
                        'serviceName': 'string',
                        'roleArn': 'string'
                    }
                }
            }
        }
    }
}


Response Structure

(dict) --The output from the GetTopicRule operation.

ruleArn (string) --The rule ARN.

rule (dict) --The rule.

ruleName (string) --The name of the rule.

sql (string) --The SQL statement used to query the topic. When using a SQL query with multiple lines, be sure to escape the newline characters.

description (string) --The description of the rule.

createdAt (datetime) --The date and time the rule was created.

actions (list) --The actions associated with the rule.

(dict) --Describes the actions associated with a rule.

dynamoDB (dict) --Write to a DynamoDB table.

tableName (string) --The name of the DynamoDB table.

roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.

operation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .

hashKeyField (string) --The hash key name.

hashKeyValue (string) --The hash key value.

hashKeyType (string) --The hash key type. Valid values are "STRING" or "NUMBER"

rangeKeyField (string) --The range key name.

rangeKeyValue (string) --The range key value.

rangeKeyType (string) --The range key type. Valid values are "STRING" or "NUMBER"

payloadField (string) --The action payload. This name can be customized.



dynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.

putItem (dict) --Specifies the DynamoDB table to which the message data will be written. For example:

{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }
Each attribute in the message payload will be written to a separate column in the DynamoDB database.

tableName (string) --The table where the message data will be written.





lambda (dict) --Invoke a Lambda function.

functionArn (string) --The ARN of the Lambda function.



sns (dict) --Publish to an Amazon SNS topic.

targetArn (string) --The ARN of the SNS topic.

roleArn (string) --The ARN of the IAM role that grants access.

messageFormat (string) --(Optional) The message format of the message to publish. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see https://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.



sqs (dict) --Publish to an Amazon SQS queue.

roleArn (string) --The ARN of the IAM role that grants access.

queueUrl (string) --The URL of the Amazon SQS queue.

useBase64 (boolean) --Specifies whether to use Base64 encoding.



kinesis (dict) --Write data to an Amazon Kinesis stream.

roleArn (string) --The ARN of the IAM role that grants access to the Amazon Kinesis stream.

streamName (string) --The name of the Amazon Kinesis stream.

partitionKey (string) --The partition key.



republish (dict) --Publish to another MQTT topic.

roleArn (string) --The ARN of the IAM role that grants access.

topic (string) --The name of the MQTT topic.

qos (integer) --The Quality of Service (QoS) level to use when republishing messages. The default value is 0.



s3 (dict) --Write to an Amazon S3 bucket.

roleArn (string) --The ARN of the IAM role that grants access.

bucketName (string) --The Amazon S3 bucket.

key (string) --The object key.

cannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .



firehose (dict) --Write to an Amazon Kinesis Firehose stream.

roleArn (string) --The IAM role that grants access to the Amazon Kinesis Firehose stream.

deliveryStreamName (string) --The delivery stream name.

separator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).



cloudwatchMetric (dict) --Capture a CloudWatch metric.

roleArn (string) --The IAM role that allows access to the CloudWatch metric.

metricNamespace (string) --The CloudWatch metric namespace name.

metricName (string) --The CloudWatch metric name.

metricValue (string) --The CloudWatch metric value.

metricUnit (string) --The metric unit supported by CloudWatch.

metricTimestamp (string) --An optional Unix timestamp .



cloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.

roleArn (string) --The IAM role that allows access to the CloudWatch alarm.

alarmName (string) --The CloudWatch alarm name.

stateReason (string) --The reason for the alarm change.

stateValue (string) --The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.



cloudwatchLogs (dict) --Send data to CloudWatch Logs.

roleArn (string) --The IAM role that allows access to the CloudWatch log.

logGroupName (string) --The CloudWatch log group to which the action sends data.



elasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.

roleArn (string) --The IAM role ARN that has access to Elasticsearch.

endpoint (string) --The endpoint of your Elasticsearch domain.

index (string) --The Elasticsearch index where you want to store your data.

type (string) --The type of document you are storing.

id (string) --The unique identifier for the document you are storing.



salesforce (dict) --Send a message to a Salesforce IoT Cloud Input Stream.

token (string) --The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

url (string) --The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.



iotAnalytics (dict) --Sends message data to an AWS IoT Analytics channel.

channelArn (string) --(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

channelName (string) --The name of the IoT Analytics channel to which message data will be sent.

roleArn (string) --The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).



iotEvents (dict) --Sends an input to an AWS IoT Events detector.

inputName (string) --The name of the AWS IoT Events input.

messageId (string) --[Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.

roleArn (string) --The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ("Action":"iotevents:BatchPutMessage").



iotSiteWise (dict) --Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.

putAssetPropertyValueEntries (list) --A list of asset property value entries.

(dict) --An asset property value entry containing the following information.

entryId (string) --Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.

assetId (string) --The ID of the AWS IoT SiteWise asset. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.

propertyId (string) --The ID of the asset\'s property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.

propertyAlias (string) --The name of the property alias associated with your asset property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.

propertyValues (list) --A list of property values to insert that each contain timestamp, quality, and value (TQV) information.

(dict) --An asset property value entry containing the following information.

value (dict) --The value of the asset property.

stringValue (string) --Optional. The string value of the value entry. Accepts substitution templates.

integerValue (string) --Optional. A string that contains the integer value of the value entry. Accepts substitution templates.

doubleValue (string) --Optional. A string that contains the double value of the value entry. Accepts substitution templates.

booleanValue (string) --Optional. A string that contains the boolean value (true or false ) of the value entry. Accepts substitution templates.



timestamp (dict) --The asset property value timestamp.

timeInSeconds (string) --A string that contains the time in seconds since epoch. Accepts substitution templates.

offsetInNanos (string) --Optional. A string that contains the nanosecond time offset. Accepts substitution templates.



quality (string) --Optional. A string that describes the quality of the value. Accepts substitution templates. Must be GOOD , BAD , or UNCERTAIN .









roleArn (string) --The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoTSiteWise. ("Action": "iotsitewise:BatchPutAssetPropertyValue" ). The trust policy can restrict access to specific asset hierarchy paths.



stepFunctions (dict) --Starts execution of a Step Functions state machine.

executionNamePrefix (string) --(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.

stateMachineName (string) --The name of the Step Functions state machine whose execution will be started.

roleArn (string) --The ARN of the role that grants IoT permission to start execution of a state machine ("Action":"states:StartExecution").



http (dict) --Send data to an HTTPS endpoint.

url (string) --The endpoint URL. If substitution templates are used in the URL, you must also specify a confirmationUrl . If this is a new destination, a new TopicRuleDestination is created if possible.

confirmationUrl (string) --The URL to which AWS IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.

headers (list) --The HTTP headers to send with the message data.

(dict) --The HTTP action header.

key (string) --The HTTP header key.

value (string) --The HTTP header value. Substitution templates are supported.





auth (dict) --The authentication method to use when sending data to an HTTPS endpoint.

sigv4 (dict) --Use Sig V4 authorization. For more information, see Signature Version 4 Signing Process .

signingRegion (string) --The signing region.

serviceName (string) --The service name to use while signing with Sig V4.

roleArn (string) --The ARN of the signing role.











ruleDisabled (boolean) --Specifies whether the rule is disabled.

awsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.

errorAction (dict) --The action to perform when an error occurs.

dynamoDB (dict) --Write to a DynamoDB table.

tableName (string) --The name of the DynamoDB table.

roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.

operation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .

hashKeyField (string) --The hash key name.

hashKeyValue (string) --The hash key value.

hashKeyType (string) --The hash key type. Valid values are "STRING" or "NUMBER"

rangeKeyField (string) --The range key name.

rangeKeyValue (string) --The range key value.

rangeKeyType (string) --The range key type. Valid values are "STRING" or "NUMBER"

payloadField (string) --The action payload. This name can be customized.



dynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

roleArn (string) --The ARN of the IAM role that grants access to the DynamoDB table.

putItem (dict) --Specifies the DynamoDB table to which the message data will be written. For example:

{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }
Each attribute in the message payload will be written to a separate column in the DynamoDB database.

tableName (string) --The table where the message data will be written.





lambda (dict) --Invoke a Lambda function.

functionArn (string) --The ARN of the Lambda function.



sns (dict) --Publish to an Amazon SNS topic.

targetArn (string) --The ARN of the SNS topic.

roleArn (string) --The ARN of the IAM role that grants access.

messageFormat (string) --(Optional) The message format of the message to publish. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see https://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.



sqs (dict) --Publish to an Amazon SQS queue.

roleArn (string) --The ARN of the IAM role that grants access.

queueUrl (string) --The URL of the Amazon SQS queue.

useBase64 (boolean) --Specifies whether to use Base64 encoding.



kinesis (dict) --Write data to an Amazon Kinesis stream.

roleArn (string) --The ARN of the IAM role that grants access to the Amazon Kinesis stream.

streamName (string) --The name of the Amazon Kinesis stream.

partitionKey (string) --The partition key.



republish (dict) --Publish to another MQTT topic.

roleArn (string) --The ARN of the IAM role that grants access.

topic (string) --The name of the MQTT topic.

qos (integer) --The Quality of Service (QoS) level to use when republishing messages. The default value is 0.



s3 (dict) --Write to an Amazon S3 bucket.

roleArn (string) --The ARN of the IAM role that grants access.

bucketName (string) --The Amazon S3 bucket.

key (string) --The object key.

cannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .



firehose (dict) --Write to an Amazon Kinesis Firehose stream.

roleArn (string) --The IAM role that grants access to the Amazon Kinesis Firehose stream.

deliveryStreamName (string) --The delivery stream name.

separator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).



cloudwatchMetric (dict) --Capture a CloudWatch metric.

roleArn (string) --The IAM role that allows access to the CloudWatch metric.

metricNamespace (string) --The CloudWatch metric namespace name.

metricName (string) --The CloudWatch metric name.

metricValue (string) --The CloudWatch metric value.

metricUnit (string) --The metric unit supported by CloudWatch.

metricTimestamp (string) --An optional Unix timestamp .



cloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.

roleArn (string) --The IAM role that allows access to the CloudWatch alarm.

alarmName (string) --The CloudWatch alarm name.

stateReason (string) --The reason for the alarm change.

stateValue (string) --The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.



cloudwatchLogs (dict) --Send data to CloudWatch Logs.

roleArn (string) --The IAM role that allows access to the CloudWatch log.

logGroupName (string) --The CloudWatch log group to which the action sends data.



elasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.

roleArn (string) --The IAM role ARN that has access to Elasticsearch.

endpoint (string) --The endpoint of your Elasticsearch domain.

index (string) --The Elasticsearch index where you want to store your data.

type (string) --The type of document you are storing.

id (string) --The unique identifier for the document you are storing.



salesforce (dict) --Send a message to a Salesforce IoT Cloud Input Stream.

token (string) --The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

url (string) --The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.



iotAnalytics (dict) --Sends message data to an AWS IoT Analytics channel.

channelArn (string) --(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

channelName (string) --The name of the IoT Analytics channel to which message data will be sent.

roleArn (string) --The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).



iotEvents (dict) --Sends an input to an AWS IoT Events detector.

inputName (string) --The name of the AWS IoT Events input.

messageId (string) --[Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.

roleArn (string) --The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ("Action":"iotevents:BatchPutMessage").



iotSiteWise (dict) --Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.

putAssetPropertyValueEntries (list) --A list of asset property value entries.

(dict) --An asset property value entry containing the following information.

entryId (string) --Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.

assetId (string) --The ID of the AWS IoT SiteWise asset. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.

propertyId (string) --The ID of the asset\'s property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.

propertyAlias (string) --The name of the property alias associated with your asset property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.

propertyValues (list) --A list of property values to insert that each contain timestamp, quality, and value (TQV) information.

(dict) --An asset property value entry containing the following information.

value (dict) --The value of the asset property.

stringValue (string) --Optional. The string value of the value entry. Accepts substitution templates.

integerValue (string) --Optional. A string that contains the integer value of the value entry. Accepts substitution templates.

doubleValue (string) --Optional. A string that contains the double value of the value entry. Accepts substitution templates.

booleanValue (string) --Optional. A string that contains the boolean value (true or false ) of the value entry. Accepts substitution templates.



timestamp (dict) --The asset property value timestamp.

timeInSeconds (string) --A string that contains the time in seconds since epoch. Accepts substitution templates.

offsetInNanos (string) --Optional. A string that contains the nanosecond time offset. Accepts substitution templates.



quality (string) --Optional. A string that describes the quality of the value. Accepts substitution templates. Must be GOOD , BAD , or UNCERTAIN .









roleArn (string) --The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoTSiteWise. ("Action": "iotsitewise:BatchPutAssetPropertyValue" ). The trust policy can restrict access to specific asset hierarchy paths.



stepFunctions (dict) --Starts execution of a Step Functions state machine.

executionNamePrefix (string) --(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.

stateMachineName (string) --The name of the Step Functions state machine whose execution will be started.

roleArn (string) --The ARN of the role that grants IoT permission to start execution of a state machine ("Action":"states:StartExecution").



http (dict) --Send data to an HTTPS endpoint.

url (string) --The endpoint URL. If substitution templates are used in the URL, you must also specify a confirmationUrl . If this is a new destination, a new TopicRuleDestination is created if possible.

confirmationUrl (string) --The URL to which AWS IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.

headers (list) --The HTTP headers to send with the message data.

(dict) --The HTTP action header.

key (string) --The HTTP header key.

value (string) --The HTTP header value. Substitution templates are supported.





auth (dict) --The authentication method to use when sending data to an HTTPS endpoint.

sigv4 (dict) --Use Sig V4 authorization. For more information, see Signature Version 4 Signing Process .

signingRegion (string) --The signing region.

serviceName (string) --The service name to use while signing with Sig V4.

roleArn (string) --The ARN of the signing role.
















Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.UnauthorizedException


    :return: {
        'ruleArn': 'string',
        'rule': {
            'ruleName': 'string',
            'sql': 'string',
            'description': 'string',
            'createdAt': datetime(2015, 1, 1),
            'actions': [
                {
                    'dynamoDB': {
                        'tableName': 'string',
                        'roleArn': 'string',
                        'operation': 'string',
                        'hashKeyField': 'string',
                        'hashKeyValue': 'string',
                        'hashKeyType': 'STRING'|'NUMBER',
                        'rangeKeyField': 'string',
                        'rangeKeyValue': 'string',
                        'rangeKeyType': 'STRING'|'NUMBER',
                        'payloadField': 'string'
                    },
                    'dynamoDBv2': {
                        'roleArn': 'string',
                        'putItem': {
                            'tableName': 'string'
                        }
                    },
                    'lambda': {
                        'functionArn': 'string'
                    },
                    'sns': {
                        'targetArn': 'string',
                        'roleArn': 'string',
                        'messageFormat': 'RAW'|'JSON'
                    },
                    'sqs': {
                        'roleArn': 'string',
                        'queueUrl': 'string',
                        'useBase64': True|False
                    },
                    'kinesis': {
                        'roleArn': 'string',
                        'streamName': 'string',
                        'partitionKey': 'string'
                    },
                    'republish': {
                        'roleArn': 'string',
                        'topic': 'string',
                        'qos': 123
                    },
                    's3': {
                        'roleArn': 'string',
                        'bucketName': 'string',
                        'key': 'string',
                        'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                    },
                    'firehose': {
                        'roleArn': 'string',
                        'deliveryStreamName': 'string',
                        'separator': 'string'
                    },
                    'cloudwatchMetric': {
                        'roleArn': 'string',
                        'metricNamespace': 'string',
                        'metricName': 'string',
                        'metricValue': 'string',
                        'metricUnit': 'string',
                        'metricTimestamp': 'string'
                    },
                    'cloudwatchAlarm': {
                        'roleArn': 'string',
                        'alarmName': 'string',
                        'stateReason': 'string',
                        'stateValue': 'string'
                    },
                    'cloudwatchLogs': {
                        'roleArn': 'string',
                        'logGroupName': 'string'
                    },
                    'elasticsearch': {
                        'roleArn': 'string',
                        'endpoint': 'string',
                        'index': 'string',
                        'type': 'string',
                        'id': 'string'
                    },
                    'salesforce': {
                        'token': 'string',
                        'url': 'string'
                    },
                    'iotAnalytics': {
                        'channelArn': 'string',
                        'channelName': 'string',
                        'roleArn': 'string'
                    },
                    'iotEvents': {
                        'inputName': 'string',
                        'messageId': 'string',
                        'roleArn': 'string'
                    },
                    'iotSiteWise': {
                        'putAssetPropertyValueEntries': [
                            {
                                'entryId': 'string',
                                'assetId': 'string',
                                'propertyId': 'string',
                                'propertyAlias': 'string',
                                'propertyValues': [
                                    {
                                        'value': {
                                            'stringValue': 'string',
                                            'integerValue': 'string',
                                            'doubleValue': 'string',
                                            'booleanValue': 'string'
                                        },
                                        'timestamp': {
                                            'timeInSeconds': 'string',
                                            'offsetInNanos': 'string'
                                        },
                                        'quality': 'string'
                                    },
                                ]
                            },
                        ],
                        'roleArn': 'string'
                    },
                    'stepFunctions': {
                        'executionNamePrefix': 'string',
                        'stateMachineName': 'string',
                        'roleArn': 'string'
                    },
                    'http': {
                        'url': 'string',
                        'confirmationUrl': 'string',
                        'headers': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'auth': {
                            'sigv4': {
                                'signingRegion': 'string',
                                'serviceName': 'string',
                                'roleArn': 'string'
                            }
                        }
                    }
                },
            ],
            'ruleDisabled': True|False,
            'awsIotSqlVersion': 'string',
            'errorAction': {
                'dynamoDB': {
                    'tableName': 'string',
                    'roleArn': 'string',
                    'operation': 'string',
                    'hashKeyField': 'string',
                    'hashKeyValue': 'string',
                    'hashKeyType': 'STRING'|'NUMBER',
                    'rangeKeyField': 'string',
                    'rangeKeyValue': 'string',
                    'rangeKeyType': 'STRING'|'NUMBER',
                    'payloadField': 'string'
                },
                'dynamoDBv2': {
                    'roleArn': 'string',
                    'putItem': {
                        'tableName': 'string'
                    }
                },
                'lambda': {
                    'functionArn': 'string'
                },
                'sns': {
                    'targetArn': 'string',
                    'roleArn': 'string',
                    'messageFormat': 'RAW'|'JSON'
                },
                'sqs': {
                    'roleArn': 'string',
                    'queueUrl': 'string',
                    'useBase64': True|False
                },
                'kinesis': {
                    'roleArn': 'string',
                    'streamName': 'string',
                    'partitionKey': 'string'
                },
                'republish': {
                    'roleArn': 'string',
                    'topic': 'string',
                    'qos': 123
                },
                's3': {
                    'roleArn': 'string',
                    'bucketName': 'string',
                    'key': 'string',
                    'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                },
                'firehose': {
                    'roleArn': 'string',
                    'deliveryStreamName': 'string',
                    'separator': 'string'
                },
                'cloudwatchMetric': {
                    'roleArn': 'string',
                    'metricNamespace': 'string',
                    'metricName': 'string',
                    'metricValue': 'string',
                    'metricUnit': 'string',
                    'metricTimestamp': 'string'
                },
                'cloudwatchAlarm': {
                    'roleArn': 'string',
                    'alarmName': 'string',
                    'stateReason': 'string',
                    'stateValue': 'string'
                },
                'cloudwatchLogs': {
                    'roleArn': 'string',
                    'logGroupName': 'string'
                },
                'elasticsearch': {
                    'roleArn': 'string',
                    'endpoint': 'string',
                    'index': 'string',
                    'type': 'string',
                    'id': 'string'
                },
                'salesforce': {
                    'token': 'string',
                    'url': 'string'
                },
                'iotAnalytics': {
                    'channelArn': 'string',
                    'channelName': 'string',
                    'roleArn': 'string'
                },
                'iotEvents': {
                    'inputName': 'string',
                    'messageId': 'string',
                    'roleArn': 'string'
                },
                'iotSiteWise': {
                    'putAssetPropertyValueEntries': [
                        {
                            'entryId': 'string',
                            'assetId': 'string',
                            'propertyId': 'string',
                            'propertyAlias': 'string',
                            'propertyValues': [
                                {
                                    'value': {
                                        'stringValue': 'string',
                                        'integerValue': 'string',
                                        'doubleValue': 'string',
                                        'booleanValue': 'string'
                                    },
                                    'timestamp': {
                                        'timeInSeconds': 'string',
                                        'offsetInNanos': 'string'
                                    },
                                    'quality': 'string'
                                },
                            ]
                        },
                    ],
                    'roleArn': 'string'
                },
                'stepFunctions': {
                    'executionNamePrefix': 'string',
                    'stateMachineName': 'string',
                    'roleArn': 'string'
                },
                'http': {
                    'url': 'string',
                    'confirmationUrl': 'string',
                    'headers': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'auth': {
                        'sigv4': {
                            'signingRegion': 'string',
                            'serviceName': 'string',
                            'roleArn': 'string'
                        }
                    }
                }
            }
        }
    }
    
    
    """
    pass

def get_topic_rule_destination(arn=None):
    """
    Gets information about a topic rule destination.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_topic_rule_destination(
        arn='string'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe ARN of the topic rule destination.\n

    :rtype: dict
ReturnsResponse Syntax{
    'topicRuleDestination': {
        'arn': 'string',
        'status': 'ENABLED'|'IN_PROGRESS'|'DISABLED'|'ERROR',
        'statusReason': 'string',
        'httpUrlProperties': {
            'confirmationUrl': 'string'
        }
    }
}


Response Structure

(dict) --
topicRuleDestination (dict) --The topic rule destination.

arn (string) --The topic rule destination URL.

status (string) --The status of the topic rule destination. Valid values are:

IN_PROGRESS
A topic rule destination was created but has not been confirmed. You can set status to IN_PROGRESS by calling UpdateTopicRuleDestination . Calling UpdateTopicRuleDestination causes a new confirmation challenge to be sent to your confirmation endpoint.

ENABLED
Confirmation was completed, and traffic to this destination is allowed. You can set status to DISABLED by calling UpdateTopicRuleDestination .

DISABLED
Confirmation was completed, and traffic to this destination is not allowed. You can set status to ENABLED by calling UpdateTopicRuleDestination .

ERROR
Confirmation could not be completed, for example if the confirmation timed out. You can call GetTopicRuleDestination for details about the error. You can set status to IN_PROGRESS by calling UpdateTopicRuleDestination . Calling UpdateTopicRuleDestination causes a new confirmation challenge to be sent to your confirmation endpoint.

statusReason (string) --Additional details or reason why the topic rule destination is in the current status.

httpUrlProperties (dict) --Properties of the HTTP URL.

confirmationUrl (string) --The URL used to confirm the HTTP topic rule destination URL.










Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.UnauthorizedException


    :return: {
        'topicRuleDestination': {
            'arn': 'string',
            'status': 'ENABLED'|'IN_PROGRESS'|'DISABLED'|'ERROR',
            'statusReason': 'string',
            'httpUrlProperties': {
                'confirmationUrl': 'string'
            }
        }
    }
    
    
    """
    pass

def get_v2_logging_options():
    """
    Gets the fine grained logging options.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_v2_logging_options()
    
    
    :rtype: dict
ReturnsResponse Syntax{
    'roleArn': 'string',
    'defaultLogLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED',
    'disableAllLogs': True|False
}


Response Structure

(dict) --
roleArn (string) --The IAM role ARN AWS IoT uses to write to your CloudWatch logs.

defaultLogLevel (string) --The default log level.

disableAllLogs (boolean) --Disables all logs.






Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.NotConfiguredException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'roleArn': 'string',
        'defaultLogLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED',
        'disableAllLogs': True|False
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

def list_active_violations(thingName=None, securityProfileName=None, nextToken=None, maxResults=None):
    """
    Lists the active violations for a given Device Defender security profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_active_violations(
        thingName='string',
        securityProfileName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type thingName: string
    :param thingName: The name of the thing whose active violations are listed.

    :type securityProfileName: string
    :param securityProfileName: The name of the Device Defender security profile for which violations are listed.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'activeViolations': [
        {
            'violationId': 'string',
            'thingName': 'string',
            'securityProfileName': 'string',
            'behavior': {
                'name': 'string',
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                },
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123,
                    'consecutiveDatapointsToAlarm': 123,
                    'consecutiveDatapointsToClear': 123,
                    'statisticalThreshold': {
                        'statistic': 'string'
                    }
                }
            },
            'lastViolationValue': {
                'count': 123,
                'cidrs': [
                    'string',
                ],
                'ports': [
                    123,
                ]
            },
            'lastViolationTime': datetime(2015, 1, 1),
            'violationStartTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

activeViolations (list) --
The list of active violations.

(dict) --
Information about an active Device Defender security profile behavior violation.

violationId (string) --
The ID of the active violation.

thingName (string) --
The name of the thing responsible for the active violation.

securityProfileName (string) --
The security profile whose behavior is in violation.

behavior (dict) --
The behavior which is being violated.

name (string) --
The name you have given to the behavior.

metric (string) --
What is measured by the behavior.

metricDimension (dict) --
The dimension for a metric in your behavior. For example, using a TOPIC_FILTER dimension, you can narrow down the scope of the metric only to MQTT topics whose name match the pattern specified in the dimension.

dimensionName (string) --
A unique identifier for the dimension.

operator (string) --
Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .



criteria (dict) --
The criteria that determine if a device is behaving normally in regard to the metric .

comparisonOperator (string) --
The operator that relates the thing measured (metric ) to the criteria (containing a value or statisticalThreshold ).

value (dict) --
The value to be compared with the metric .

count (integer) --
If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .

cidrs (list) --
If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .

(string) --


ports (list) --
If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .

(integer) --




durationSeconds (integer) --
Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ). For a statisticalThreshhold metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.

consecutiveDatapointsToAlarm (integer) --
If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.

consecutiveDatapointsToClear (integer) --
If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.

statisticalThreshold (dict) --
A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

statistic (string) --
The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (durationSeconds ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (comparisonOperator ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.







lastViolationValue (dict) --
The value of the metric (the measurement) which caused the most recent violation.

count (integer) --
If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .

cidrs (list) --
If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .

(string) --


ports (list) --
If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .

(integer) --




lastViolationTime (datetime) --
The time the most recent violation occurred.

violationStartTime (datetime) --
The time the violation started.





nextToken (string) --
A token that can be used to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'activeViolations': [
            {
                'violationId': 'string',
                'thingName': 'string',
                'securityProfileName': 'string',
                'behavior': {
                    'name': 'string',
                    'metric': 'string',
                    'metricDimension': {
                        'dimensionName': 'string',
                        'operator': 'IN'|'NOT_IN'
                    },
                    'criteria': {
                        'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                        'value': {
                            'count': 123,
                            'cidrs': [
                                'string',
                            ],
                            'ports': [
                                123,
                            ]
                        },
                        'durationSeconds': 123,
                        'consecutiveDatapointsToAlarm': 123,
                        'consecutiveDatapointsToClear': 123,
                        'statisticalThreshold': {
                            'statistic': 'string'
                        }
                    }
                },
                'lastViolationValue': {
                    'count': 123,
                    'cidrs': [
                        'string',
                    ],
                    'ports': [
                        123,
                    ]
                },
                'lastViolationTime': datetime(2015, 1, 1),
                'violationStartTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_attached_policies(target=None, recursive=None, marker=None, pageSize=None):
    """
    Lists the policies attached to the specified thing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_attached_policies(
        target='string',
        recursive=True|False,
        marker='string',
        pageSize=123
    )
    
    
    :type target: string
    :param target: [REQUIRED]\nThe group or principal for which the policies will be listed.\n

    :type recursive: boolean
    :param recursive: When true, recursively list attached policies.

    :type marker: string
    :param marker: The token to retrieve the next set of results.

    :type pageSize: integer
    :param pageSize: The maximum number of results to be returned per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'policies': [
        {
            'policyName': 'string',
            'policyArn': 'string'
        },
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --

policies (list) --
The policies.

(dict) --
Describes an AWS IoT policy.

policyName (string) --
The policy name.

policyArn (string) --
The policy ARN.





nextMarker (string) --
The token to retrieve the next set of results, or null if there are no more results.







Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.LimitExceededException


    :return: {
        'policies': [
            {
                'policyName': 'string',
                'policyArn': 'string'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.LimitExceededException
    
    """
    pass

def list_audit_findings(taskId=None, checkName=None, resourceIdentifier=None, maxResults=None, nextToken=None, startTime=None, endTime=None):
    """
    Lists the findings (results) of a Device Defender audit or of the audits performed during a specified time period. (Findings are retained for 180 days.)
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_audit_findings(
        taskId='string',
        checkName='string',
        resourceIdentifier={
            'deviceCertificateId': 'string',
            'caCertificateId': 'string',
            'cognitoIdentityPoolId': 'string',
            'clientId': 'string',
            'policyVersionIdentifier': {
                'policyName': 'string',
                'policyVersionId': 'string'
            },
            'account': 'string',
            'iamRoleArn': 'string',
            'roleAliasArn': 'string'
        },
        maxResults=123,
        nextToken='string',
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1)
    )
    
    
    :type taskId: string
    :param taskId: A filter to limit results to the audit with the specified ID. You must specify either the taskId or the startTime and endTime, but not both.

    :type checkName: string
    :param checkName: A filter to limit results to the findings for the specified audit check.

    :type resourceIdentifier: dict
    :param resourceIdentifier: Information identifying the noncompliant resource.\n\ndeviceCertificateId (string) --The ID of the certificate attached to the resource.\n\ncaCertificateId (string) --The ID of the CA certificate used to authorize the certificate.\n\ncognitoIdentityPoolId (string) --The ID of the Amazon Cognito identity pool.\n\nclientId (string) --The client ID.\n\npolicyVersionIdentifier (dict) --The version of the policy associated with the resource.\n\npolicyName (string) --The name of the policy.\n\npolicyVersionId (string) --The ID of the version of the policy associated with the resource.\n\n\n\naccount (string) --The account with which the resource is associated.\n\niamRoleArn (string) --The ARN of the IAM role that has overly permissive actions.\n\nroleAliasArn (string) --The ARN of the role alias that has overly permissive actions.\n\n\n

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time. The default is 25.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type startTime: datetime
    :param startTime: A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both.

    :type endTime: datetime
    :param endTime: A filter to limit results to those found before the specified time. You must specify either the startTime and endTime or the taskId, but not both.

    :rtype: dict

ReturnsResponse Syntax
{
    'findings': [
        {
            'findingId': 'string',
            'taskId': 'string',
            'checkName': 'string',
            'taskStartTime': datetime(2015, 1, 1),
            'findingTime': datetime(2015, 1, 1),
            'severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW',
            'nonCompliantResource': {
                'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS'|'ROLE_ALIAS'|'IAM_ROLE',
                'resourceIdentifier': {
                    'deviceCertificateId': 'string',
                    'caCertificateId': 'string',
                    'cognitoIdentityPoolId': 'string',
                    'clientId': 'string',
                    'policyVersionIdentifier': {
                        'policyName': 'string',
                        'policyVersionId': 'string'
                    },
                    'account': 'string',
                    'iamRoleArn': 'string',
                    'roleAliasArn': 'string'
                },
                'additionalInfo': {
                    'string': 'string'
                }
            },
            'relatedResources': [
                {
                    'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS'|'ROLE_ALIAS'|'IAM_ROLE',
                    'resourceIdentifier': {
                        'deviceCertificateId': 'string',
                        'caCertificateId': 'string',
                        'cognitoIdentityPoolId': 'string',
                        'clientId': 'string',
                        'policyVersionIdentifier': {
                            'policyName': 'string',
                            'policyVersionId': 'string'
                        },
                        'account': 'string',
                        'iamRoleArn': 'string',
                        'roleAliasArn': 'string'
                    },
                    'additionalInfo': {
                        'string': 'string'
                    }
                },
            ],
            'reasonForNonCompliance': 'string',
            'reasonForNonComplianceCode': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

findings (list) --
The findings (results) of the audit.

(dict) --
The findings (results) of the audit.

findingId (string) --
A unique identifier for this set of audit findings. This identifier is used to apply mitigation tasks to one or more sets of findings.

taskId (string) --
The ID of the audit that generated this result (finding).

checkName (string) --
The audit check that generated this result.

taskStartTime (datetime) --
The time the audit started.

findingTime (datetime) --
The time the result (finding) was discovered.

severity (string) --
The severity of the result (finding).

nonCompliantResource (dict) --
The resource that was found to be noncompliant with the audit check.

resourceType (string) --
The type of the noncompliant resource.

resourceIdentifier (dict) --
Information that identifies the noncompliant resource.

deviceCertificateId (string) --
The ID of the certificate attached to the resource.

caCertificateId (string) --
The ID of the CA certificate used to authorize the certificate.

cognitoIdentityPoolId (string) --
The ID of the Amazon Cognito identity pool.

clientId (string) --
The client ID.

policyVersionIdentifier (dict) --
The version of the policy associated with the resource.

policyName (string) --
The name of the policy.

policyVersionId (string) --
The ID of the version of the policy associated with the resource.



account (string) --
The account with which the resource is associated.

iamRoleArn (string) --
The ARN of the IAM role that has overly permissive actions.

roleAliasArn (string) --
The ARN of the role alias that has overly permissive actions.



additionalInfo (dict) --
Other information about the noncompliant resource.

(string) --
(string) --






relatedResources (list) --
The list of related resources.

(dict) --
Information about a related resource.

resourceType (string) --
The type of resource.

resourceIdentifier (dict) --
Information that identifies the resource.

deviceCertificateId (string) --
The ID of the certificate attached to the resource.

caCertificateId (string) --
The ID of the CA certificate used to authorize the certificate.

cognitoIdentityPoolId (string) --
The ID of the Amazon Cognito identity pool.

clientId (string) --
The client ID.

policyVersionIdentifier (dict) --
The version of the policy associated with the resource.

policyName (string) --
The name of the policy.

policyVersionId (string) --
The ID of the version of the policy associated with the resource.



account (string) --
The account with which the resource is associated.

iamRoleArn (string) --
The ARN of the IAM role that has overly permissive actions.

roleAliasArn (string) --
The ARN of the role alias that has overly permissive actions.



additionalInfo (dict) --
Other information about the resource.

(string) --
(string) --








reasonForNonCompliance (string) --
The reason the resource was noncompliant.

reasonForNonComplianceCode (string) --
A code that indicates the reason that the resource was noncompliant.





nextToken (string) --
A token that can be used to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'findings': [
            {
                'findingId': 'string',
                'taskId': 'string',
                'checkName': 'string',
                'taskStartTime': datetime(2015, 1, 1),
                'findingTime': datetime(2015, 1, 1),
                'severity': 'CRITICAL'|'HIGH'|'MEDIUM'|'LOW',
                'nonCompliantResource': {
                    'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS'|'ROLE_ALIAS'|'IAM_ROLE',
                    'resourceIdentifier': {
                        'deviceCertificateId': 'string',
                        'caCertificateId': 'string',
                        'cognitoIdentityPoolId': 'string',
                        'clientId': 'string',
                        'policyVersionIdentifier': {
                            'policyName': 'string',
                            'policyVersionId': 'string'
                        },
                        'account': 'string',
                        'iamRoleArn': 'string',
                        'roleAliasArn': 'string'
                    },
                    'additionalInfo': {
                        'string': 'string'
                    }
                },
                'relatedResources': [
                    {
                        'resourceType': 'DEVICE_CERTIFICATE'|'CA_CERTIFICATE'|'IOT_POLICY'|'COGNITO_IDENTITY_POOL'|'CLIENT_ID'|'ACCOUNT_SETTINGS'|'ROLE_ALIAS'|'IAM_ROLE',
                        'resourceIdentifier': {
                            'deviceCertificateId': 'string',
                            'caCertificateId': 'string',
                            'cognitoIdentityPoolId': 'string',
                            'clientId': 'string',
                            'policyVersionIdentifier': {
                                'policyName': 'string',
                                'policyVersionId': 'string'
                            },
                            'account': 'string',
                            'iamRoleArn': 'string',
                            'roleAliasArn': 'string'
                        },
                        'additionalInfo': {
                            'string': 'string'
                        }
                    },
                ],
                'reasonForNonCompliance': 'string',
                'reasonForNonComplianceCode': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_audit_mitigation_actions_executions(taskId=None, actionStatus=None, findingId=None, maxResults=None, nextToken=None):
    """
    Gets the status of audit mitigation action tasks that were executed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_audit_mitigation_actions_executions(
        taskId='string',
        actionStatus='IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED'|'SKIPPED'|'PENDING',
        findingId='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]\nSpecify this filter to limit results to actions for a specific audit mitigation actions task.\n

    :type actionStatus: string
    :param actionStatus: Specify this filter to limit results to those with a specific status.

    :type findingId: string
    :param findingId: [REQUIRED]\nSpecify this filter to limit results to those that were applied to a specific audit finding.\n

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time. The default is 25.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'actionsExecutions': [
        {
            'taskId': 'string',
            'findingId': 'string',
            'actionName': 'string',
            'actionId': 'string',
            'status': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED'|'SKIPPED'|'PENDING',
            'startTime': datetime(2015, 1, 1),
            'endTime': datetime(2015, 1, 1),
            'errorCode': 'string',
            'message': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

actionsExecutions (list) --
A set of task execution results based on the input parameters. Details include the mitigation action applied, start time, and task status.

(dict) --
Returned by ListAuditMitigationActionsTask, this object contains information that describes a mitigation action that has been started.

taskId (string) --
The unique identifier for the task that applies the mitigation action.

findingId (string) --
The unique identifier for the findings to which the task and associated mitigation action are applied.

actionName (string) --
The friendly name of the mitigation action being applied by the task.

actionId (string) --
The unique identifier for the mitigation action being applied by the task.

status (string) --
The current status of the task being executed.

startTime (datetime) --
The date and time when the task was started.

endTime (datetime) --
The date and time when the task was completed or canceled. Blank if the task is still running.

errorCode (string) --
If an error occurred, the code that indicates which type of error occurred.

message (string) --
If an error occurred, a message that describes the error.





nextToken (string) --
The token for the next set of results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'actionsExecutions': [
            {
                'taskId': 'string',
                'findingId': 'string',
                'actionName': 'string',
                'actionId': 'string',
                'status': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED'|'SKIPPED'|'PENDING',
                'startTime': datetime(2015, 1, 1),
                'endTime': datetime(2015, 1, 1),
                'errorCode': 'string',
                'message': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_audit_mitigation_actions_tasks(auditTaskId=None, findingId=None, taskStatus=None, maxResults=None, nextToken=None, startTime=None, endTime=None):
    """
    Gets a list of audit mitigation action tasks that match the specified filters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_audit_mitigation_actions_tasks(
        auditTaskId='string',
        findingId='string',
        taskStatus='IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
        maxResults=123,
        nextToken='string',
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1)
    )
    
    
    :type auditTaskId: string
    :param auditTaskId: Specify this filter to limit results to tasks that were applied to results for a specific audit.

    :type findingId: string
    :param findingId: Specify this filter to limit results to tasks that were applied to a specific audit finding.

    :type taskStatus: string
    :param taskStatus: Specify this filter to limit results to tasks that are in a specific state.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time. The default is 25.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type startTime: datetime
    :param startTime: [REQUIRED]\nSpecify this filter to limit results to tasks that began on or after a specific date and time.\n

    :type endTime: datetime
    :param endTime: [REQUIRED]\nSpecify this filter to limit results to tasks that were completed or canceled on or before a specific date and time.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'tasks': [
        {
            'taskId': 'string',
            'startTime': datetime(2015, 1, 1),
            'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

tasks (list) --
The collection of audit mitigation tasks that matched the filter criteria.

(dict) --
Information about an audit mitigation actions task that is returned by ListAuditMitigationActionsTasks .

taskId (string) --
The unique identifier for the task.

startTime (datetime) --
The time at which the audit mitigation actions task was started.

taskStatus (string) --
The current state of the audit mitigation actions task.





nextToken (string) --
The token for the next set of results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'tasks': [
            {
                'taskId': 'string',
                'startTime': datetime(2015, 1, 1),
                'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_audit_tasks(startTime=None, endTime=None, taskType=None, taskStatus=None, nextToken=None, maxResults=None):
    """
    Lists the Device Defender audits that have been performed during a given time period.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_audit_tasks(
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        taskType='ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK',
        taskStatus='IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
        nextToken='string',
        maxResults=123
    )
    
    
    :type startTime: datetime
    :param startTime: [REQUIRED]\nThe beginning of the time period. Audit information is retained for a limited time (180 days). Requesting a start time prior to what is retained results in an 'InvalidRequestException'.\n

    :type endTime: datetime
    :param endTime: [REQUIRED]\nThe end of the time period.\n

    :type taskType: string
    :param taskType: A filter to limit the output to the specified type of audit: can be one of 'ON_DEMAND_AUDIT_TASK' or 'SCHEDULED__AUDIT_TASK'.

    :type taskStatus: string
    :param taskStatus: A filter to limit the output to audits with the specified completion status: can be one of 'IN_PROGRESS', 'COMPLETED', 'FAILED', or 'CANCELED'.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time. The default is 25.

    :rtype: dict

ReturnsResponse Syntax
{
    'tasks': [
        {
            'taskId': 'string',
            'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
            'taskType': 'ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

tasks (list) --
The audits that were performed during the specified time period.

(dict) --
The audits that were performed.

taskId (string) --
The ID of this audit.

taskStatus (string) --
The status of this audit. One of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".

taskType (string) --
The type of this audit. One of "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".





nextToken (string) --
A token that can be used to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'tasks': [
            {
                'taskId': 'string',
                'taskStatus': 'IN_PROGRESS'|'COMPLETED'|'FAILED'|'CANCELED',
                'taskType': 'ON_DEMAND_AUDIT_TASK'|'SCHEDULED_AUDIT_TASK'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_authorizers(pageSize=None, marker=None, ascendingOrder=None, status=None):
    """
    Lists the authorizers registered in your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_authorizers(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False,
        status='ACTIVE'|'INACTIVE'
    )
    
    
    :type pageSize: integer
    :param pageSize: The maximum number of results to return at one time.

    :type marker: string
    :param marker: A marker used to get the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Return the list of authorizers in ascending alphabetical order.

    :type status: string
    :param status: The status of the list authorizers request.

    :rtype: dict

ReturnsResponse Syntax
{
    'authorizers': [
        {
            'authorizerName': 'string',
            'authorizerArn': 'string'
        },
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --

authorizers (list) --
The authorizers.

(dict) --
The authorizer summary.

authorizerName (string) --
The authorizer name.

authorizerArn (string) --
The authorizer ARN.





nextMarker (string) --
A marker used to get the next set of results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'authorizers': [
            {
                'authorizerName': 'string',
                'authorizerArn': 'string'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_billing_groups(nextToken=None, maxResults=None, namePrefixFilter=None):
    """
    Lists the billing groups you have created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_billing_groups(
        nextToken='string',
        maxResults=123,
        namePrefixFilter='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return per request.

    :type namePrefixFilter: string
    :param namePrefixFilter: Limit the results to billing groups whose names have the given prefix.

    :rtype: dict

ReturnsResponse Syntax
{
    'billingGroups': [
        {
            'groupName': 'string',
            'groupArn': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

billingGroups (list) --
The list of billing groups.

(dict) --
The name and ARN of a group.

groupName (string) --
The group name.

groupArn (string) --
The group ARN.





nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException


    :return: {
        'billingGroups': [
            {
                'groupName': 'string',
                'groupArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    
    """
    pass

def list_ca_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists the CA certificates registered for your AWS account.
    The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_ca_certificates(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Determines the order of the results.

    :rtype: dict

ReturnsResponse Syntax
{
    'certificates': [
        {
            'certificateArn': 'string',
            'certificateId': 'string',
            'status': 'ACTIVE'|'INACTIVE',
            'creationDate': datetime(2015, 1, 1)
        },
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --
The output from the ListCACertificates operation.

certificates (list) --
The CA certificates registered in your AWS account.

(dict) --
A CA certificate.

certificateArn (string) --
The ARN of the CA certificate.

certificateId (string) --
The ID of the CA certificate.

status (string) --
The status of the CA certificate.
The status value REGISTER_INACTIVE is deprecated and should not be used.

creationDate (datetime) --
The date the CA certificate was created.





nextMarker (string) --
The current position within the list of CA certificates.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'certificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists the certificates registered in your AWS account.
    The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_certificates(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

    :rtype: dict

ReturnsResponse Syntax
{
    'certificates': [
        {
            'certificateArn': 'string',
            'certificateId': 'string',
            'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
            'certificateMode': 'DEFAULT'|'SNI_ONLY',
            'creationDate': datetime(2015, 1, 1)
        },
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --
The output of the ListCertificates operation.

certificates (list) --
The descriptions of the certificates.

(dict) --
Information about a certificate.

certificateArn (string) --
The ARN of the certificate.

certificateId (string) --
The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)

status (string) --
The status of the certificate.
The status value REGISTER_INACTIVE is deprecated and should not be used.

certificateMode (string) --
The mode of the certificate.

creationDate (datetime) --
The date and time the certificate was created.





nextMarker (string) --
The marker for the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'certificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                'certificateMode': 'DEFAULT'|'SNI_ONLY',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_certificates_by_ca(caCertificateId=None, pageSize=None, marker=None, ascendingOrder=None):
    """
    List the device certificates signed by the specified CA certificate.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_certificates_by_ca(
        caCertificateId='string',
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type caCertificateId: string
    :param caCertificateId: [REQUIRED]\nThe ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.\n

    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

    :rtype: dict

ReturnsResponse Syntax
{
    'certificates': [
        {
            'certificateArn': 'string',
            'certificateId': 'string',
            'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
            'certificateMode': 'DEFAULT'|'SNI_ONLY',
            'creationDate': datetime(2015, 1, 1)
        },
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --
The output of the ListCertificatesByCA operation.

certificates (list) --
The device certificates signed by the specified CA certificate.

(dict) --
Information about a certificate.

certificateArn (string) --
The ARN of the certificate.

certificateId (string) --
The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)

status (string) --
The status of the certificate.
The status value REGISTER_INACTIVE is deprecated and should not be used.

certificateMode (string) --
The mode of the certificate.

creationDate (datetime) --
The date and time the certificate was created.





nextMarker (string) --
The marker for the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'certificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                'certificateMode': 'DEFAULT'|'SNI_ONLY',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_dimensions(nextToken=None, maxResults=None):
    """
    List the set of dimensions that are defined for your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_dimensions(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to retrieve at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'dimensionNames': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

dimensionNames (list) --
A list of the names of the defined dimensions. Use DescribeDimension to get details for a dimension.

(string) --


nextToken (string) --
A token that can be used to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException


    :return: {
        'dimensionNames': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_domain_configurations(marker=None, pageSize=None, serviceType=None):
    """
    Gets a list of domain configurations for the user. This list is sorted alphabetically by domain configuration name.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_domain_configurations(
        marker='string',
        pageSize=123,
        serviceType='DATA'|'CREDENTIAL_PROVIDER'|'JOBS'
    )
    
    
    :type marker: string
    :param marker: The marker for the next set of results.

    :type pageSize: integer
    :param pageSize: The result page size.

    :type serviceType: string
    :param serviceType: The type of service delivered by the endpoint.

    :rtype: dict

ReturnsResponse Syntax
{
    'domainConfigurations': [
        {
            'domainConfigurationName': 'string',
            'domainConfigurationArn': 'string',
            'serviceType': 'DATA'|'CREDENTIAL_PROVIDER'|'JOBS'
        },
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --

domainConfigurations (list) --
A list of objects that contain summary information about the user\'s domain configurations.

(dict) --
The summary of a domain configuration. A domain configuration specifies custom IoT-specific information about a domain. A domain configuration can be associated with an AWS-managed domain (for example, dbc123defghijk.iot.us-west-2.amazonaws.com), a customer managed domain, or a default endpoint.

Data
Jobs
CredentialProvider


Note
The domain configuration feature is in public preview and is subject to change.


domainConfigurationName (string) --
The name of the domain configuration. This value must be unique to a region.

domainConfigurationArn (string) --
The ARN of the domain configuration.

serviceType (string) --
The type of service delivered by the endpoint.





nextMarker (string) --
The marker for the next set of results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'domainConfigurations': [
            {
                'domainConfigurationName': 'string',
                'domainConfigurationArn': 'string',
                'serviceType': 'DATA'|'CREDENTIAL_PROVIDER'|'JOBS'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    Data
    Jobs
    CredentialProvider
    
    """
    pass

def list_indices(nextToken=None, maxResults=None):
    """
    Lists the search indices.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_indices(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token used to get the next set of results, or null if there are no additional results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'indexNames': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

indexNames (list) --
The index names.

(string) --


nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'indexNames': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_job_executions_for_job(jobId=None, status=None, maxResults=None, nextToken=None):
    """
    Lists the job executions for a job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_job_executions_for_job(
        jobId='string',
        status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe unique identifier you assigned to this job when it was created.\n

    :type status: string
    :param status: The status of the job.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per request.

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'executionSummaries': [
        {
            'thingArn': 'string',
            'jobExecutionSummary': {
                'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                'queuedAt': datetime(2015, 1, 1),
                'startedAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'executionNumber': 123
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

executionSummaries (list) --
A list of job execution summaries.

(dict) --
Contains a summary of information about job executions for a specific job.

thingArn (string) --
The ARN of the thing on which the job execution is running.

jobExecutionSummary (dict) --
Contains a subset of information about a job execution.

status (string) --
The status of the job execution.

queuedAt (datetime) --
The time, in seconds since the epoch, when the job execution was queued.

startedAt (datetime) --
The time, in seconds since the epoch, when the job execution started.

lastUpdatedAt (datetime) --
The time, in seconds since the epoch, when the job execution was last updated.

executionNumber (integer) --
A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used later in commands which return or update job execution information.







nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'executionSummaries': [
            {
                'thingArn': 'string',
                'jobExecutionSummary': {
                    'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                    'queuedAt': datetime(2015, 1, 1),
                    'startedAt': datetime(2015, 1, 1),
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'executionNumber': 123
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_job_executions_for_thing(thingName=None, status=None, maxResults=None, nextToken=None):
    """
    Lists the job executions for the specified thing.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_job_executions_for_thing(
        thingName='string',
        status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe thing name.\n

    :type status: string
    :param status: An optional filter that lets you search for jobs that have the specified status.

    :type maxResults: integer
    :param maxResults: The maximum number of results to be returned per request.

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'executionSummaries': [
        {
            'jobId': 'string',
            'jobExecutionSummary': {
                'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                'queuedAt': datetime(2015, 1, 1),
                'startedAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'executionNumber': 123
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

executionSummaries (list) --
A list of job execution summaries.

(dict) --
The job execution summary for a thing.

jobId (string) --
The unique identifier you assigned to this job when it was created.

jobExecutionSummary (dict) --
Contains a subset of information about a job execution.

status (string) --
The status of the job execution.

queuedAt (datetime) --
The time, in seconds since the epoch, when the job execution was queued.

startedAt (datetime) --
The time, in seconds since the epoch, when the job execution started.

lastUpdatedAt (datetime) --
The time, in seconds since the epoch, when the job execution was last updated.

executionNumber (integer) --
A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used later in commands which return or update job execution information.







nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'executionSummaries': [
            {
                'jobId': 'string',
                'jobExecutionSummary': {
                    'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'TIMED_OUT'|'REJECTED'|'REMOVED'|'CANCELED',
                    'queuedAt': datetime(2015, 1, 1),
                    'startedAt': datetime(2015, 1, 1),
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'executionNumber': 123
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_jobs(status=None, targetSelection=None, maxResults=None, nextToken=None, thingGroupName=None, thingGroupId=None):
    """
    Lists jobs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_jobs(
        status='IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
        targetSelection='CONTINUOUS'|'SNAPSHOT',
        maxResults=123,
        nextToken='string',
        thingGroupName='string',
        thingGroupId='string'
    )
    
    
    :type status: string
    :param status: An optional filter that lets you search for jobs that have the specified status.

    :type targetSelection: string
    :param targetSelection: Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return per request.

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type thingGroupName: string
    :param thingGroupName: A filter that limits the returned jobs to those for the specified group.

    :type thingGroupId: string
    :param thingGroupId: A filter that limits the returned jobs to those for the specified group.

    :rtype: dict

ReturnsResponse Syntax
{
    'jobs': [
        {
            'jobArn': 'string',
            'jobId': 'string',
            'thingGroupId': 'string',
            'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
            'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
            'createdAt': datetime(2015, 1, 1),
            'lastUpdatedAt': datetime(2015, 1, 1),
            'completedAt': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

jobs (list) --
A list of jobs.

(dict) --
The job summary.

jobArn (string) --
The job ARN.

jobId (string) --
The unique identifier you assigned to this job when it was created.

thingGroupId (string) --
The ID of the thing group.

targetSelection (string) --
Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.

status (string) --
The job summary status.

createdAt (datetime) --
The time, in seconds since the epoch, when the job was created.

lastUpdatedAt (datetime) --
The time, in seconds since the epoch, when the job was last updated.

completedAt (datetime) --
The time, in seconds since the epoch, when the job completed.





nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'jobs': [
            {
                'jobArn': 'string',
                'jobId': 'string',
                'thingGroupId': 'string',
                'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
                'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED'|'DELETION_IN_PROGRESS',
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'completedAt': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_mitigation_actions(actionType=None, maxResults=None, nextToken=None):
    """
    Gets a list of all mitigation actions that match the specified filter criteria.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_mitigation_actions(
        actionType='UPDATE_DEVICE_CERTIFICATE'|'UPDATE_CA_CERTIFICATE'|'ADD_THINGS_TO_THING_GROUP'|'REPLACE_DEFAULT_POLICY_VERSION'|'ENABLE_IOT_LOGGING'|'PUBLISH_FINDING_TO_SNS',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type actionType: string
    :param actionType: Specify a value to limit the result to mitigation actions with a specific action type.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time. The default is 25.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'actionIdentifiers': [
        {
            'actionName': 'string',
            'actionArn': 'string',
            'creationDate': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

actionIdentifiers (list) --
A set of actions that matched the specified filter criteria.

(dict) --
Information that identifies a mitigation action. This information is returned by ListMitigationActions.

actionName (string) --
The friendly name of the mitigation action.

actionArn (string) --
The IAM role ARN used to apply this mitigation action.

creationDate (datetime) --
The date when this mitigation action was created.





nextToken (string) --
The token for the next set of results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'actionIdentifiers': [
            {
                'actionName': 'string',
                'actionArn': 'string',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_ota_updates(maxResults=None, nextToken=None, otaUpdateStatus=None):
    """
    Lists OTA updates.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_ota_updates(
        maxResults=123,
        nextToken='string',
        otaUpdateStatus='CREATE_PENDING'|'CREATE_IN_PROGRESS'|'CREATE_COMPLETE'|'CREATE_FAILED'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type nextToken: string
    :param nextToken: A token used to retrieve the next set of results.

    :type otaUpdateStatus: string
    :param otaUpdateStatus: The OTA update job status.

    :rtype: dict

ReturnsResponse Syntax
{
    'otaUpdates': [
        {
            'otaUpdateId': 'string',
            'otaUpdateArn': 'string',
            'creationDate': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

otaUpdates (list) --
A list of OTA update jobs.

(dict) --
An OTA update summary.

otaUpdateId (string) --
The OTA update ID.

otaUpdateArn (string) --
The OTA update ARN.

creationDate (datetime) --
The date when the OTA update was created.





nextToken (string) --
A token to use to get the next set of results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'otaUpdates': [
            {
                'otaUpdateId': 'string',
                'otaUpdateArn': 'string',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_outgoing_certificates(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists certificates that are being transferred but not yet accepted.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_outgoing_certificates(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The result page size.

    :type marker: string
    :param marker: The marker for the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

    :rtype: dict

ReturnsResponse Syntax
{
    'outgoingCertificates': [
        {
            'certificateArn': 'string',
            'certificateId': 'string',
            'transferredTo': 'string',
            'transferDate': datetime(2015, 1, 1),
            'transferMessage': 'string',
            'creationDate': datetime(2015, 1, 1)
        },
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --
The output from the ListOutgoingCertificates operation.

outgoingCertificates (list) --
The certificates that are being transferred but not yet accepted.

(dict) --
A certificate that has been transferred but not yet accepted.

certificateArn (string) --
The certificate ARN.

certificateId (string) --
The certificate ID.

transferredTo (string) --
The AWS account to which the transfer was made.

transferDate (datetime) --
The date the transfer was initiated.

transferMessage (string) --
The transfer message.

creationDate (datetime) --
The certificate creation date.





nextMarker (string) --
The marker for the next set of results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'outgoingCertificates': [
            {
                'certificateArn': 'string',
                'certificateId': 'string',
                'transferredTo': 'string',
                'transferDate': datetime(2015, 1, 1),
                'transferMessage': 'string',
                'creationDate': datetime(2015, 1, 1)
            },
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_policies(marker=None, pageSize=None, ascendingOrder=None):
    """
    Lists your policies.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_policies(
        marker='string',
        pageSize=123,
        ascendingOrder=True|False
    )
    
    
    :type marker: string
    :param marker: The marker for the next set of results.

    :type pageSize: integer
    :param pageSize: The result page size.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If true, the results are returned in ascending creation order.

    :rtype: dict

ReturnsResponse Syntax
{
    'policies': [
        {
            'policyName': 'string',
            'policyArn': 'string'
        },
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --
The output from the ListPolicies operation.

policies (list) --
The descriptions of the policies.

(dict) --
Describes an AWS IoT policy.

policyName (string) --
The policy name.

policyArn (string) --
The policy ARN.





nextMarker (string) --
The marker for the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'policies': [
            {
                'policyName': 'string',
                'policyArn': 'string'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_policy_principals(policyName=None, marker=None, pageSize=None, ascendingOrder=None):
    """
    Lists the principals associated with the specified policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_policy_principals(
        policyName='string',
        marker='string',
        pageSize=123,
        ascendingOrder=True|False
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe policy name.\n

    :type marker: string
    :param marker: The marker for the next set of results.

    :type pageSize: integer
    :param pageSize: The result page size.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If true, the results are returned in ascending creation order.

    :rtype: dict

ReturnsResponse Syntax
{
    'principals': [
        'string',
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --
The output from the ListPolicyPrincipals operation.

principals (list) --
The descriptions of the principals.

(string) --


nextMarker (string) --
The marker for the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'principals': [
            'string',
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_policy_versions(policyName=None):
    """
    Lists the versions of the specified policy and identifies the default version.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_policy_versions(
        policyName='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe policy name.\n

    :rtype: dict
ReturnsResponse Syntax{
    'policyVersions': [
        {
            'versionId': 'string',
            'isDefaultVersion': True|False,
            'createDate': datetime(2015, 1, 1)
        },
    ]
}


Response Structure

(dict) --The output from the ListPolicyVersions operation.

policyVersions (list) --The policy versions.

(dict) --Describes a policy version.

versionId (string) --The policy version ID.

isDefaultVersion (boolean) --Specifies whether the policy version is the default.

createDate (datetime) --The date and time the policy was created.










Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'policyVersions': [
            {
                'versionId': 'string',
                'isDefaultVersion': True|False,
                'createDate': datetime(2015, 1, 1)
            },
        ]
    }
    
    
    """
    pass

def list_principal_policies(principal=None, marker=None, pageSize=None, ascendingOrder=None):
    """
    Lists the policies attached to the specified principal. If you use an Cognito identity, the ID must be in AmazonCognito Identity format .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_principal_policies(
        principal='string',
        marker='string',
        pageSize=123,
        ascendingOrder=True|False
    )
    
    
    :type principal: string
    :param principal: [REQUIRED]\nThe principal.\n

    :type marker: string
    :param marker: The marker for the next set of results.

    :type pageSize: integer
    :param pageSize: The result page size.

    :type ascendingOrder: boolean
    :param ascendingOrder: Specifies the order for results. If true, results are returned in ascending creation order.

    :rtype: dict

ReturnsResponse Syntax
{
    'policies': [
        {
            'policyName': 'string',
            'policyArn': 'string'
        },
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --
The output from the ListPrincipalPolicies operation.

policies (list) --
The policies.

(dict) --
Describes an AWS IoT policy.

policyName (string) --
The policy name.

policyArn (string) --
The policy ARN.





nextMarker (string) --
The marker for the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'policies': [
            {
                'policyName': 'string',
                'policyArn': 'string'
            },
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_principal_things(nextToken=None, maxResults=None, principal=None):
    """
    Lists the things associated with the specified principal. A principal can be X.509 certificates, IAM users, groups, and roles, Amazon Cognito identities or federated identities.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_principal_things(
        nextToken='string',
        maxResults=123,
        principal='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this operation.

    :type principal: string
    :param principal: [REQUIRED]\nThe principal.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'things': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The output from the ListPrincipalThings operation.

things (list) --
The things.

(string) --


nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'things': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_provisioning_template_versions(templateName=None, maxResults=None, nextToken=None):
    """
    A list of fleet provisioning template versions.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_provisioning_template_versions(
        templateName='string',
        maxResults=123,
        nextToken='string'
    )
    
    
    :type templateName: string
    :param templateName: [REQUIRED]\nThe name of the fleet provisioning template.\n

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type nextToken: string
    :param nextToken: A token to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'versions': [
        {
            'versionId': 123,
            'creationDate': datetime(2015, 1, 1),
            'isDefaultVersion': True|False
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

versions (list) --
The list of fleet provisioning template versions.

(dict) --
A summary of information about a fleet provision template version.

versionId (integer) --
The ID of the fleet privisioning template version.

creationDate (datetime) --
The date when the fleet provisioning template version was created

isDefaultVersion (boolean) --
True if the fleet provisioning template version is the default version, otherwise false.





nextToken (string) --
A token to retrieve the next set of results.







Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.UnauthorizedException


    :return: {
        'versions': [
            {
                'versionId': 123,
                'creationDate': datetime(2015, 1, 1),
                'isDefaultVersion': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.UnauthorizedException
    
    """
    pass

def list_provisioning_templates(maxResults=None, nextToken=None):
    """
    Lists the fleet provisioning templates in your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_provisioning_templates(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type nextToken: string
    :param nextToken: A token to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'templates': [
        {
            'templateArn': 'string',
            'templateName': 'string',
            'description': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'enabled': True|False
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

templates (list) --
A list of fleet provisioning templates

(dict) --
A summary of information about a fleet provisioning template.

templateArn (string) --
The ARN of the fleet provisioning template.

templateName (string) --
The name of the fleet provisioning template.

description (string) --
The description of the fleet provisioning template.

creationDate (datetime) --
The date when the fleet provisioning template summary was created.

lastModifiedDate (datetime) --
The date when the fleet provisioning template summary was last modified.

enabled (boolean) --
True if the fleet provision template is enabled, otherwise false.





nextToken (string) --
A token to retrieve the next set of results.







Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException


    :return: {
        'templates': [
            {
                'templateArn': 'string',
                'templateName': 'string',
                'description': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1),
                'enabled': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    
    """
    pass

def list_role_aliases(pageSize=None, marker=None, ascendingOrder=None):
    """
    Lists the role aliases registered in your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_role_aliases(
        pageSize=123,
        marker='string',
        ascendingOrder=True|False
    )
    
    
    :type pageSize: integer
    :param pageSize: The maximum number of results to return at one time.

    :type marker: string
    :param marker: A marker used to get the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Return the list of role aliases in ascending alphabetical order.

    :rtype: dict

ReturnsResponse Syntax
{
    'roleAliases': [
        'string',
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --

roleAliases (list) --
The role aliases.

(string) --


nextMarker (string) --
A marker used to get the next set of results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'roleAliases': [
            'string',
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_scheduled_audits(nextToken=None, maxResults=None):
    """
    Lists all of your scheduled audits.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_scheduled_audits(
        nextToken='string',
        maxResults=123
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time. The default is 25.

    :rtype: dict

ReturnsResponse Syntax
{
    'scheduledAudits': [
        {
            'scheduledAuditName': 'string',
            'scheduledAuditArn': 'string',
            'frequency': 'DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
            'dayOfMonth': 'string',
            'dayOfWeek': 'SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

scheduledAudits (list) --
The list of scheduled audits.

(dict) --
Information about the scheduled audit.

scheduledAuditName (string) --
The name of the scheduled audit.

scheduledAuditArn (string) --
The ARN of the scheduled audit.

frequency (string) --
How often the scheduled audit occurs.

dayOfMonth (string) --
The day of the month on which the scheduled audit is run (if the frequency is "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.

dayOfWeek (string) --
The day of the week on which the scheduled audit is run (if the frequency is "WEEKLY" or "BIWEEKLY").





nextToken (string) --
A token that can be used to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'scheduledAudits': [
            {
                'scheduledAuditName': 'string',
                'scheduledAuditArn': 'string',
                'frequency': 'DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
                'dayOfMonth': 'string',
                'dayOfWeek': 'SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_security_profiles(nextToken=None, maxResults=None, dimensionName=None):
    """
    Lists the Device Defender security profiles you have created. You can use filters to list only those security profiles associated with a thing group or only those associated with your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_security_profiles(
        nextToken='string',
        maxResults=123,
        dimensionName='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type dimensionName: string
    :param dimensionName: A filter to limit results to the security profiles that use the defined dimension.

    :rtype: dict

ReturnsResponse Syntax
{
    'securityProfileIdentifiers': [
        {
            'name': 'string',
            'arn': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

securityProfileIdentifiers (list) --
A list of security profile identifiers (names and ARNs).

(dict) --
Identifying information for a Device Defender security profile.

name (string) --
The name you have given to the security profile.

arn (string) --
The ARN of the security profile.





nextToken (string) --
A token that can be used to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'securityProfileIdentifiers': [
            {
                'name': 'string',
                'arn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_security_profiles_for_target(nextToken=None, maxResults=None, recursive=None, securityProfileTargetArn=None):
    """
    Lists the Device Defender security profiles attached to a target (thing group).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_security_profiles_for_target(
        nextToken='string',
        maxResults=123,
        recursive=True|False,
        securityProfileTargetArn='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type recursive: boolean
    :param recursive: If true, return child groups too.

    :type securityProfileTargetArn: string
    :param securityProfileTargetArn: [REQUIRED]\nThe ARN of the target (thing group) whose attached security profiles you want to get.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'securityProfileTargetMappings': [
        {
            'securityProfileIdentifier': {
                'name': 'string',
                'arn': 'string'
            },
            'target': {
                'arn': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

securityProfileTargetMappings (list) --
A list of security profiles and their associated targets.

(dict) --
Information about a security profile and the target associated with it.

securityProfileIdentifier (dict) --
Information that identifies the security profile.

name (string) --
The name you have given to the security profile.

arn (string) --
The ARN of the security profile.



target (dict) --
Information about the target (thing group) associated with the security profile.

arn (string) --
The ARN of the security profile.







nextToken (string) --
A token that can be used to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'securityProfileTargetMappings': [
            {
                'securityProfileIdentifier': {
                    'name': 'string',
                    'arn': 'string'
                },
                'target': {
                    'arn': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_streams(maxResults=None, nextToken=None, ascendingOrder=None):
    """
    Lists all of the streams in your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_streams(
        maxResults=123,
        nextToken='string',
        ascendingOrder=True|False
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return at a time.

    :type nextToken: string
    :param nextToken: A token used to get the next set of results.

    :type ascendingOrder: boolean
    :param ascendingOrder: Set to true to return the list of streams in ascending order.

    :rtype: dict

ReturnsResponse Syntax
{
    'streams': [
        {
            'streamId': 'string',
            'streamArn': 'string',
            'streamVersion': 123,
            'description': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

streams (list) --
A list of streams.

(dict) --
A summary of a stream.

streamId (string) --
The stream ID.

streamArn (string) --
The stream ARN.

streamVersion (integer) --
The stream version.

description (string) --
A description of the stream.





nextToken (string) --
A token used to get the next set of results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'streams': [
            {
                'streamId': 'string',
                'streamArn': 'string',
                'streamVersion': 123,
                'description': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_tags_for_resource(resourceArn=None, nextToken=None):
    """
    Lists the tags (metadata) you have assigned to the resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string',
        nextToken='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource.\n

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'tags': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

tags (list) --
The list of tags assigned to the resource.

(dict) --
A set of key/value pairs that are used to manage the resource.

Key (string) --
The tag\'s key.

Value (string) --
The tag\'s value.





nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException


    :return: {
        'tags': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    
    """
    pass

def list_targets_for_policy(policyName=None, marker=None, pageSize=None):
    """
    List targets for the specified policy.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_targets_for_policy(
        policyName='string',
        marker='string',
        pageSize=123
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe policy name.\n

    :type marker: string
    :param marker: A marker used to get the next set of results.

    :type pageSize: integer
    :param pageSize: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'targets': [
        'string',
    ],
    'nextMarker': 'string'
}


Response Structure

(dict) --

targets (list) --
The policy targets.

(string) --


nextMarker (string) --
A marker used to get the next set of results.







Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.LimitExceededException


    :return: {
        'targets': [
            'string',
        ],
        'nextMarker': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_targets_for_security_profile(securityProfileName=None, nextToken=None, maxResults=None):
    """
    Lists the targets (thing groups) associated with a given Device Defender security profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_targets_for_security_profile(
        securityProfileName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]\nThe security profile.\n

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'securityProfileTargets': [
        {
            'arn': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

securityProfileTargets (list) --
The thing groups to which the security profile is attached.

(dict) --
A target to which an alert is sent when a security profile behavior is violated.

arn (string) --
The ARN of the security profile.





nextToken (string) --
A token that can be used to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'securityProfileTargets': [
            {
                'arn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def list_thing_groups(nextToken=None, maxResults=None, parentGroup=None, namePrefixFilter=None, recursive=None):
    """
    List the thing groups in your account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_thing_groups(
        nextToken='string',
        maxResults=123,
        parentGroup='string',
        namePrefixFilter='string',
        recursive=True|False
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type parentGroup: string
    :param parentGroup: A filter that limits the results to those with the specified parent group.

    :type namePrefixFilter: string
    :param namePrefixFilter: A filter that limits the results to those with the specified name prefix.

    :type recursive: boolean
    :param recursive: If true, return child groups as well.

    :rtype: dict

ReturnsResponse Syntax
{
    'thingGroups': [
        {
            'groupName': 'string',
            'groupArn': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

thingGroups (list) --
The thing groups.

(dict) --
The name and ARN of a group.

groupName (string) --
The group name.

groupArn (string) --
The group ARN.





nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'thingGroups': [
            {
                'groupName': 'string',
                'groupArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_thing_groups_for_thing(thingName=None, nextToken=None, maxResults=None):
    """
    List the thing groups to which the specified thing belongs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_thing_groups_for_thing(
        thingName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe thing name.\n

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'thingGroups': [
        {
            'groupName': 'string',
            'groupArn': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

thingGroups (list) --
The thing groups.

(dict) --
The name and ARN of a group.

groupName (string) --
The group name.

groupArn (string) --
The group ARN.





nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'thingGroups': [
            {
                'groupName': 'string',
                'groupArn': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_thing_principals(thingName=None):
    """
    Lists the principals associated with the specified thing. A principal can be X.509 certificates, IAM users, groups, and roles, Amazon Cognito identities or federated identities.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_thing_principals(
        thingName='string'
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing.\n

    :rtype: dict
ReturnsResponse Syntax{
    'principals': [
        'string',
    ]
}


Response Structure

(dict) --The output from the ListThingPrincipals operation.

principals (list) --The principals associated with the thing.

(string) --







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'principals': [
            'string',
        ]
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_thing_registration_task_reports(taskId=None, reportType=None, nextToken=None, maxResults=None):
    """
    Information about the thing registration tasks.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_thing_registration_task_reports(
        taskId='string',
        reportType='ERRORS'|'RESULTS',
        nextToken='string',
        maxResults=123
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]\nThe id of the task.\n

    :type reportType: string
    :param reportType: [REQUIRED]\nThe type of task report.\n

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'resourceLinks': [
        'string',
    ],
    'reportType': 'ERRORS'|'RESULTS',
    'nextToken': 'string'
}


Response Structure

(dict) --

resourceLinks (list) --
Links to the task resources.

(string) --


reportType (string) --
The type of task report.

nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'resourceLinks': [
            'string',
        ],
        'reportType': 'ERRORS'|'RESULTS',
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_thing_registration_tasks(nextToken=None, maxResults=None, status=None):
    """
    List bulk thing provisioning tasks.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_thing_registration_tasks(
        nextToken='string',
        maxResults=123,
        status='InProgress'|'Completed'|'Failed'|'Cancelled'|'Cancelling'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type status: string
    :param status: The status of the bulk thing provisioning task.

    :rtype: dict

ReturnsResponse Syntax
{
    'taskIds': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

taskIds (list) --
A list of bulk thing provisioning task IDs.

(string) --


nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'taskIds': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_thing_types(nextToken=None, maxResults=None, thingTypeName=None):
    """
    Lists the existing thing types.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_thing_types(
        nextToken='string',
        maxResults=123,
        thingTypeName='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this operation.

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type.

    :rtype: dict

ReturnsResponse Syntax
{
    'thingTypes': [
        {
            'thingTypeName': 'string',
            'thingTypeArn': 'string',
            'thingTypeProperties': {
                'thingTypeDescription': 'string',
                'searchableAttributes': [
                    'string',
                ]
            },
            'thingTypeMetadata': {
                'deprecated': True|False,
                'deprecationDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1)
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The output for the ListThingTypes operation.

thingTypes (list) --
The thing types.

(dict) --
The definition of the thing type, including thing type name and description.

thingTypeName (string) --
The name of the thing type.

thingTypeArn (string) --
The thing type ARN.

thingTypeProperties (dict) --
The ThingTypeProperties for the thing type.

thingTypeDescription (string) --
The description of the thing type.

searchableAttributes (list) --
A list of searchable thing attribute names.

(string) --




thingTypeMetadata (dict) --
The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.

deprecated (boolean) --
Whether the thing type is deprecated. If true , no new things could be associated with this type.

deprecationDate (datetime) --
The date and time when the thing type was deprecated.

creationDate (datetime) --
The date and time when the thing type was created.







nextToken (string) --
The token for the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'thingTypes': [
            {
                'thingTypeName': 'string',
                'thingTypeArn': 'string',
                'thingTypeProperties': {
                    'thingTypeDescription': 'string',
                    'searchableAttributes': [
                        'string',
                    ]
                },
                'thingTypeMetadata': {
                    'deprecated': True|False,
                    'deprecationDate': datetime(2015, 1, 1),
                    'creationDate': datetime(2015, 1, 1)
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_things(nextToken=None, maxResults=None, attributeName=None, attributeValue=None, thingTypeName=None):
    """
    Lists your things. Use the attributeName and attributeValue parameters to filter your things. For example, calling ListThings with attributeName=Color and attributeValue=Red retrieves all things in the registry that contain an attribute Color with the value Red .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_things(
        nextToken='string',
        maxResults=123,
        attributeName='string',
        attributeValue='string',
        thingTypeName='string'
    )
    
    
    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return in this operation.

    :type attributeName: string
    :param attributeName: The attribute name used to search for things.

    :type attributeValue: string
    :param attributeValue: The attribute value used to search for things.

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type used to search for things.

    :rtype: dict

ReturnsResponse Syntax
{
    'things': [
        {
            'thingName': 'string',
            'thingTypeName': 'string',
            'thingArn': 'string',
            'attributes': {
                'string': 'string'
            },
            'version': 123
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The output from the ListThings operation.

things (list) --
The things.

(dict) --
The properties of the thing, including thing name, thing type name, and a list of thing attributes.

thingName (string) --
The name of the thing.

thingTypeName (string) --
The name of the thing type, if the thing has been associated with a type.

thingArn (string) --
The thing ARN.

attributes (dict) --
A list of thing attributes which are name-value pairs.

(string) --
(string) --




version (integer) --
The version of the thing record in the registry.





nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'things': [
            {
                'thingName': 'string',
                'thingTypeName': 'string',
                'thingArn': 'string',
                'attributes': {
                    'string': 'string'
                },
                'version': 123
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_things_in_billing_group(billingGroupName=None, nextToken=None, maxResults=None):
    """
    Lists the things you have added to the given billing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_things_in_billing_group(
        billingGroupName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: [REQUIRED]\nThe name of the billing group.\n

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return per request.

    :rtype: dict

ReturnsResponse Syntax
{
    'things': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

things (list) --
A list of things in the billing group.

(string) --


nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException


    :return: {
        'things': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_things_in_thing_group(thingGroupName=None, recursive=None, nextToken=None, maxResults=None):
    """
    Lists the things in the specified group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_things_in_thing_group(
        thingGroupName='string',
        recursive=True|False,
        nextToken='string',
        maxResults=123
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]\nThe thing group name.\n

    :type recursive: boolean
    :param recursive: When true, list things in this thing group and in all child groups as well.

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'things': [
        'string',
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

things (list) --
The things in the specified thing group.

(string) --


nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'things': [
            'string',
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_topic_rule_destinations(maxResults=None, nextToken=None):
    """
    Lists all the topic rule destinations in your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_topic_rule_destinations(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type nextToken: string
    :param nextToken: The token to retrieve the next set of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'destinationSummaries': [
        {
            'arn': 'string',
            'status': 'ENABLED'|'IN_PROGRESS'|'DISABLED'|'ERROR',
            'statusReason': 'string',
            'httpUrlSummary': {
                'confirmationUrl': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

destinationSummaries (list) --
Information about a topic rule destination.

(dict) --
Information about the topic rule destination.

arn (string) --
The topic rule destination ARN.

status (string) --
The status of the topic rule destination. Valid values are:

IN_PROGRESS

A topic rule destination was created but has not been confirmed. You can set status to IN_PROGRESS by calling UpdateTopicRuleDestination . Calling UpdateTopicRuleDestination causes a new confirmation challenge to be sent to your confirmation endpoint.

ENABLED

Confirmation was completed, and traffic to this destination is allowed. You can set status to DISABLED by calling UpdateTopicRuleDestination .

DISABLED

Confirmation was completed, and traffic to this destination is not allowed. You can set status to ENABLED by calling UpdateTopicRuleDestination .

ERROR

Confirmation could not be completed, for example if the confirmation timed out. You can call GetTopicRuleDestination for details about the error. You can set status to IN_PROGRESS by calling UpdateTopicRuleDestination . Calling UpdateTopicRuleDestination causes a new confirmation challenge to be sent to your confirmation endpoint.

statusReason (string) --
The reason the topic rule destination is in the current status.

httpUrlSummary (dict) --
Information about the HTTP URL.

confirmationUrl (string) --
The URL used to confirm ownership of or access to the HTTP topic rule destination URL.







nextToken (string) --
The token to retrieve the next set of results.







Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.UnauthorizedException


    :return: {
        'destinationSummaries': [
            {
                'arn': 'string',
                'status': 'ENABLED'|'IN_PROGRESS'|'DISABLED'|'ERROR',
                'statusReason': 'string',
                'httpUrlSummary': {
                    'confirmationUrl': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InternalException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.UnauthorizedException
    
    """
    pass

def list_topic_rules(topic=None, maxResults=None, nextToken=None, ruleDisabled=None):
    """
    Lists the rules for the specific topic.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_topic_rules(
        topic='string',
        maxResults=123,
        nextToken='string',
        ruleDisabled=True|False
    )
    
    
    :type topic: string
    :param topic: The topic.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return.

    :type nextToken: string
    :param nextToken: A token used to retrieve the next value.

    :type ruleDisabled: boolean
    :param ruleDisabled: Specifies whether the rule is disabled.

    :rtype: dict

ReturnsResponse Syntax
{
    'rules': [
        {
            'ruleArn': 'string',
            'ruleName': 'string',
            'topicPattern': 'string',
            'createdAt': datetime(2015, 1, 1),
            'ruleDisabled': True|False
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --
The output from the ListTopicRules operation.

rules (list) --
The rules.

(dict) --
Describes a rule.

ruleArn (string) --
The rule ARN.

ruleName (string) --
The name of the rule.

topicPattern (string) --
The pattern for the topic names that apply.

createdAt (datetime) --
The date and time the rule was created.

ruleDisabled (boolean) --
Specifies whether the rule is disabled.





nextToken (string) --
A token used to retrieve the next value.







Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'rules': [
            {
                'ruleArn': 'string',
                'ruleName': 'string',
                'topicPattern': 'string',
                'createdAt': datetime(2015, 1, 1),
                'ruleDisabled': True|False
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InternalException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_v2_logging_levels(targetType=None, nextToken=None, maxResults=None):
    """
    Lists logging levels.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_v2_logging_levels(
        targetType='DEFAULT'|'THING_GROUP',
        nextToken='string',
        maxResults=123
    )
    
    
    :type targetType: string
    :param targetType: The type of resource for which you are configuring logging. Must be THING_Group .

    :type nextToken: string
    :param nextToken: The token used to get the next set of results, or null if there are no additional results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'logTargetConfigurations': [
        {
            'logTarget': {
                'targetType': 'DEFAULT'|'THING_GROUP',
                'targetName': 'string'
            },
            'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

logTargetConfigurations (list) --
The logging configuration for a target.

(dict) --
The target configuration.

logTarget (dict) --
A log target

targetType (string) --
The target type.

targetName (string) --
The target name.



logLevel (string) --
The logging level.





nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.NotConfiguredException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ServiceUnavailableException


    :return: {
        'logTargetConfigurations': [
            {
                'logTarget': {
                    'targetType': 'DEFAULT'|'THING_GROUP',
                    'targetName': 'string'
                },
                'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InternalException
    IoT.Client.exceptions.NotConfiguredException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def list_violation_events(startTime=None, endTime=None, thingName=None, securityProfileName=None, nextToken=None, maxResults=None):
    """
    Lists the Device Defender security profile violations discovered during the given time period. You can use filters to limit the results to those alerts issued for a particular security profile, behavior, or thing (device).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_violation_events(
        startTime=datetime(2015, 1, 1),
        endTime=datetime(2015, 1, 1),
        thingName='string',
        securityProfileName='string',
        nextToken='string',
        maxResults=123
    )
    
    
    :type startTime: datetime
    :param startTime: [REQUIRED]\nThe start time for the alerts to be listed.\n

    :type endTime: datetime
    :param endTime: [REQUIRED]\nThe end time for the alerts to be listed.\n

    :type thingName: string
    :param thingName: A filter to limit results to those alerts caused by the specified thing.

    :type securityProfileName: string
    :param securityProfileName: A filter to limit results to those alerts generated by the specified security profile.

    :type nextToken: string
    :param nextToken: The token for the next set of results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :rtype: dict

ReturnsResponse Syntax
{
    'violationEvents': [
        {
            'violationId': 'string',
            'thingName': 'string',
            'securityProfileName': 'string',
            'behavior': {
                'name': 'string',
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                },
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123,
                    'consecutiveDatapointsToAlarm': 123,
                    'consecutiveDatapointsToClear': 123,
                    'statisticalThreshold': {
                        'statistic': 'string'
                    }
                }
            },
            'metricValue': {
                'count': 123,
                'cidrs': [
                    'string',
                ],
                'ports': [
                    123,
                ]
            },
            'violationEventType': 'in-alarm'|'alarm-cleared'|'alarm-invalidated',
            'violationEventTime': datetime(2015, 1, 1)
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

violationEvents (list) --
The security profile violation alerts issued for this account during the given time period, potentially filtered by security profile, behavior violated, or thing (device) violating.

(dict) --
Information about a Device Defender security profile behavior violation.

violationId (string) --
The ID of the violation event.

thingName (string) --
The name of the thing responsible for the violation event.

securityProfileName (string) --
The name of the security profile whose behavior was violated.

behavior (dict) --
The behavior which was violated.

name (string) --
The name you have given to the behavior.

metric (string) --
What is measured by the behavior.

metricDimension (dict) --
The dimension for a metric in your behavior. For example, using a TOPIC_FILTER dimension, you can narrow down the scope of the metric only to MQTT topics whose name match the pattern specified in the dimension.

dimensionName (string) --
A unique identifier for the dimension.

operator (string) --
Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .



criteria (dict) --
The criteria that determine if a device is behaving normally in regard to the metric .

comparisonOperator (string) --
The operator that relates the thing measured (metric ) to the criteria (containing a value or statisticalThreshold ).

value (dict) --
The value to be compared with the metric .

count (integer) --
If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .

cidrs (list) --
If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .

(string) --


ports (list) --
If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .

(integer) --




durationSeconds (integer) --
Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ). For a statisticalThreshhold metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.

consecutiveDatapointsToAlarm (integer) --
If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.

consecutiveDatapointsToClear (integer) --
If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.

statisticalThreshold (dict) --
A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

statistic (string) --
The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (durationSeconds ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (comparisonOperator ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.







metricValue (dict) --
The value of the metric (the measurement).

count (integer) --
If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .

cidrs (list) --
If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .

(string) --


ports (list) --
If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .

(integer) --




violationEventType (string) --
The type of violation event.

violationEventTime (datetime) --
The time the violation event occurred.





nextToken (string) --
A token that can be used to retrieve the next set of results, or null if there are no additional results.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'violationEvents': [
            {
                'violationId': 'string',
                'thingName': 'string',
                'securityProfileName': 'string',
                'behavior': {
                    'name': 'string',
                    'metric': 'string',
                    'metricDimension': {
                        'dimensionName': 'string',
                        'operator': 'IN'|'NOT_IN'
                    },
                    'criteria': {
                        'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                        'value': {
                            'count': 123,
                            'cidrs': [
                                'string',
                            ],
                            'ports': [
                                123,
                            ]
                        },
                        'durationSeconds': 123,
                        'consecutiveDatapointsToAlarm': 123,
                        'consecutiveDatapointsToClear': 123,
                        'statisticalThreshold': {
                            'statistic': 'string'
                        }
                    }
                },
                'metricValue': {
                    'count': 123,
                    'cidrs': [
                        'string',
                    ],
                    'ports': [
                        123,
                    ]
                },
                'violationEventType': 'in-alarm'|'alarm-cleared'|'alarm-invalidated',
                'violationEventTime': datetime(2015, 1, 1)
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def register_ca_certificate(caCertificate=None, verificationCertificate=None, setAsActive=None, allowAutoRegistration=None, registrationConfig=None, tags=None):
    """
    Registers a CA certificate with AWS IoT. This CA certificate can then be used to sign device certificates, which can be then registered with AWS IoT. You can register up to 10 CA certificates per AWS account that have the same subject field. This enables you to have up to 10 certificate authorities sign your device certificates. If you have more than one CA certificate registered, make sure you pass the CA certificate when you register your device certificates with the RegisterCertificate API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_ca_certificate(
        caCertificate='string',
        verificationCertificate='string',
        setAsActive=True|False,
        allowAutoRegistration=True|False,
        registrationConfig={
            'templateBody': 'string',
            'roleArn': 'string'
        },
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type caCertificate: string
    :param caCertificate: [REQUIRED]\nThe CA certificate.\n

    :type verificationCertificate: string
    :param verificationCertificate: [REQUIRED]\nThe private key verification certificate.\n

    :type setAsActive: boolean
    :param setAsActive: A boolean value that specifies if the CA certificate is set to active.

    :type allowAutoRegistration: boolean
    :param allowAutoRegistration: Allows this CA certificate to be used for auto registration of device certificates.

    :type registrationConfig: dict
    :param registrationConfig: Information about the registration configuration.\n\ntemplateBody (string) --The template body.\n\nroleArn (string) --The ARN of the role.\n\n\n

    :type tags: list
    :param tags: Metadata which can be used to manage the CA certificate.\n\nNote\nFor URI Request parameters use format: ...key1=value1&key2=value2...\nFor the CLI command-line parameter use format: &&tags 'key1=value1&key2=value2...'\nFor the cli-input-json file use format: 'tags': 'key1=value1&key2=value2...'\n\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'certificateArn': 'string',
    'certificateId': 'string'
}


Response Structure

(dict) --
The output from the RegisterCACertificateResponse operation.

certificateArn (string) --
The CA certificate ARN.

certificateId (string) --
The CA certificate identifier.







Exceptions

IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.RegistrationCodeValidationException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.CertificateValidationException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'certificateArn': 'string',
        'certificateId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.RegistrationCodeValidationException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.CertificateValidationException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def register_certificate(certificatePem=None, caCertificatePem=None, setAsActive=None, status=None):
    """
    Registers a device certificate with AWS IoT. If you have more than one CA certificate that has the same subject field, you must specify the CA certificate that was used to sign the device certificate being registered.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_certificate(
        certificatePem='string',
        caCertificatePem='string',
        setAsActive=True|False,
        status='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
    )
    
    
    :type certificatePem: string
    :param certificatePem: [REQUIRED]\nThe certificate data, in PEM format.\n

    :type caCertificatePem: string
    :param caCertificatePem: The CA certificate used to sign the device certificate being registered.

    :type setAsActive: boolean
    :param setAsActive: A boolean value that specifies if the certificate is set to active.

    :type status: string
    :param status: The status of the register certificate request.

    :rtype: dict

ReturnsResponse Syntax
{
    'certificateArn': 'string',
    'certificateId': 'string'
}


Response Structure

(dict) --
The output from the RegisterCertificate operation.

certificateArn (string) --
The certificate ARN.

certificateId (string) --
The certificate identifier.







Exceptions

IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.CertificateValidationException
IoT.Client.exceptions.CertificateStateException
IoT.Client.exceptions.CertificateConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'certificateArn': 'string',
        'certificateId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.CertificateValidationException
    IoT.Client.exceptions.CertificateStateException
    IoT.Client.exceptions.CertificateConflictException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def register_certificate_without_ca(certificatePem=None, status=None):
    """
    Register a certificate that does not have a certificate authority (CA).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_certificate_without_ca(
        certificatePem='string',
        status='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
    )
    
    
    :type certificatePem: string
    :param certificatePem: [REQUIRED]\nThe certificate data, in PEM format.\n

    :type status: string
    :param status: The status of the register certificate request.

    :rtype: dict

ReturnsResponse Syntax
{
    'certificateArn': 'string',
    'certificateId': 'string'
}


Response Structure

(dict) --

certificateArn (string) --
The Amazon Resource Name (ARN) of the registered certificate.

certificateId (string) --
The ID of the registered certificate. (The last part of the certificate ARN contains the certificate ID.







Exceptions

IoT.Client.exceptions.ResourceAlreadyExistsException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.CertificateStateException
IoT.Client.exceptions.CertificateValidationException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'certificateArn': 'string',
        'certificateId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceAlreadyExistsException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.CertificateStateException
    IoT.Client.exceptions.CertificateValidationException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def register_thing(templateBody=None, parameters=None):
    """
    Provisions a thing in the device registry. RegisterThing calls other AWS IoT control plane APIs. These calls might exceed your account level AWS IoT Throttling Limits and cause throttle errors. Please contact AWS Customer Support to raise your throttling limits if necessary.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.register_thing(
        templateBody='string',
        parameters={
            'string': 'string'
        }
    )
    
    
    :type templateBody: string
    :param templateBody: [REQUIRED]\nThe provisioning template. See Provisioning Devices That Have Device Certificates for more information.\n

    :type parameters: dict
    :param parameters: The parameters for provisioning a thing. See Provisioning Templates for more information.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'certificatePem': 'string',
    'resourceArns': {
        'string': 'string'
    }
}


Response Structure

(dict) --

certificatePem (string) --
The certificate data, in PEM format.

resourceArns (dict) --
ARNs for the generated resources.

(string) --
(string) --










Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.ConflictingResourceUpdateException
IoT.Client.exceptions.ResourceRegistrationFailureException


    :return: {
        'certificatePem': 'string',
        'resourceArns': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def reject_certificate_transfer(certificateId=None, rejectReason=None):
    """
    Rejects a pending certificate transfer. After AWS IoT rejects a certificate transfer, the certificate status changes from PENDING_TRANSFER to INACTIVE .
    To check for pending certificate transfers, call  ListCertificates to enumerate your certificates.
    This operation can only be called by the transfer destination. After it is called, the certificate will be returned to the source\'s account in the INACTIVE state.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reject_certificate_transfer(
        certificateId='string',
        rejectReason='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]\nThe ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)\n

    :type rejectReason: string
    :param rejectReason: The reason the certificate transfer was rejected.

    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.TransferAlreadyCompletedException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def remove_thing_from_billing_group(billingGroupName=None, billingGroupArn=None, thingName=None, thingArn=None):
    """
    Removes the given thing from the billing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_thing_from_billing_group(
        billingGroupName='string',
        billingGroupArn='string',
        thingName='string',
        thingArn='string'
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: The name of the billing group.

    :type billingGroupArn: string
    :param billingGroupArn: The ARN of the billing group.

    :type thingName: string
    :param thingName: The name of the thing to be removed from the billing group.

    :type thingArn: string
    :param thingArn: The ARN of the thing to be removed from the billing group.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def remove_thing_from_thing_group(thingGroupName=None, thingGroupArn=None, thingName=None, thingArn=None):
    """
    Remove the specified thing from the specified group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_thing_from_thing_group(
        thingGroupName='string',
        thingGroupArn='string',
        thingName='string',
        thingArn='string'
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: The group name.

    :type thingGroupArn: string
    :param thingGroupArn: The group ARN.

    :type thingName: string
    :param thingName: The name of the thing to remove from the group.

    :type thingArn: string
    :param thingArn: The ARN of the thing to remove from the group.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def replace_topic_rule(ruleName=None, topicRulePayload=None):
    """
    Replaces the rule. You must specify all parameters for the new rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.replace_topic_rule(
        ruleName='string',
        topicRulePayload={
            'sql': 'string',
            'description': 'string',
            'actions': [
                {
                    'dynamoDB': {
                        'tableName': 'string',
                        'roleArn': 'string',
                        'operation': 'string',
                        'hashKeyField': 'string',
                        'hashKeyValue': 'string',
                        'hashKeyType': 'STRING'|'NUMBER',
                        'rangeKeyField': 'string',
                        'rangeKeyValue': 'string',
                        'rangeKeyType': 'STRING'|'NUMBER',
                        'payloadField': 'string'
                    },
                    'dynamoDBv2': {
                        'roleArn': 'string',
                        'putItem': {
                            'tableName': 'string'
                        }
                    },
                    'lambda': {
                        'functionArn': 'string'
                    },
                    'sns': {
                        'targetArn': 'string',
                        'roleArn': 'string',
                        'messageFormat': 'RAW'|'JSON'
                    },
                    'sqs': {
                        'roleArn': 'string',
                        'queueUrl': 'string',
                        'useBase64': True|False
                    },
                    'kinesis': {
                        'roleArn': 'string',
                        'streamName': 'string',
                        'partitionKey': 'string'
                    },
                    'republish': {
                        'roleArn': 'string',
                        'topic': 'string',
                        'qos': 123
                    },
                    's3': {
                        'roleArn': 'string',
                        'bucketName': 'string',
                        'key': 'string',
                        'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                    },
                    'firehose': {
                        'roleArn': 'string',
                        'deliveryStreamName': 'string',
                        'separator': 'string'
                    },
                    'cloudwatchMetric': {
                        'roleArn': 'string',
                        'metricNamespace': 'string',
                        'metricName': 'string',
                        'metricValue': 'string',
                        'metricUnit': 'string',
                        'metricTimestamp': 'string'
                    },
                    'cloudwatchAlarm': {
                        'roleArn': 'string',
                        'alarmName': 'string',
                        'stateReason': 'string',
                        'stateValue': 'string'
                    },
                    'cloudwatchLogs': {
                        'roleArn': 'string',
                        'logGroupName': 'string'
                    },
                    'elasticsearch': {
                        'roleArn': 'string',
                        'endpoint': 'string',
                        'index': 'string',
                        'type': 'string',
                        'id': 'string'
                    },
                    'salesforce': {
                        'token': 'string',
                        'url': 'string'
                    },
                    'iotAnalytics': {
                        'channelArn': 'string',
                        'channelName': 'string',
                        'roleArn': 'string'
                    },
                    'iotEvents': {
                        'inputName': 'string',
                        'messageId': 'string',
                        'roleArn': 'string'
                    },
                    'iotSiteWise': {
                        'putAssetPropertyValueEntries': [
                            {
                                'entryId': 'string',
                                'assetId': 'string',
                                'propertyId': 'string',
                                'propertyAlias': 'string',
                                'propertyValues': [
                                    {
                                        'value': {
                                            'stringValue': 'string',
                                            'integerValue': 'string',
                                            'doubleValue': 'string',
                                            'booleanValue': 'string'
                                        },
                                        'timestamp': {
                                            'timeInSeconds': 'string',
                                            'offsetInNanos': 'string'
                                        },
                                        'quality': 'string'
                                    },
                                ]
                            },
                        ],
                        'roleArn': 'string'
                    },
                    'stepFunctions': {
                        'executionNamePrefix': 'string',
                        'stateMachineName': 'string',
                        'roleArn': 'string'
                    },
                    'http': {
                        'url': 'string',
                        'confirmationUrl': 'string',
                        'headers': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'auth': {
                            'sigv4': {
                                'signingRegion': 'string',
                                'serviceName': 'string',
                                'roleArn': 'string'
                            }
                        }
                    }
                },
            ],
            'ruleDisabled': True|False,
            'awsIotSqlVersion': 'string',
            'errorAction': {
                'dynamoDB': {
                    'tableName': 'string',
                    'roleArn': 'string',
                    'operation': 'string',
                    'hashKeyField': 'string',
                    'hashKeyValue': 'string',
                    'hashKeyType': 'STRING'|'NUMBER',
                    'rangeKeyField': 'string',
                    'rangeKeyValue': 'string',
                    'rangeKeyType': 'STRING'|'NUMBER',
                    'payloadField': 'string'
                },
                'dynamoDBv2': {
                    'roleArn': 'string',
                    'putItem': {
                        'tableName': 'string'
                    }
                },
                'lambda': {
                    'functionArn': 'string'
                },
                'sns': {
                    'targetArn': 'string',
                    'roleArn': 'string',
                    'messageFormat': 'RAW'|'JSON'
                },
                'sqs': {
                    'roleArn': 'string',
                    'queueUrl': 'string',
                    'useBase64': True|False
                },
                'kinesis': {
                    'roleArn': 'string',
                    'streamName': 'string',
                    'partitionKey': 'string'
                },
                'republish': {
                    'roleArn': 'string',
                    'topic': 'string',
                    'qos': 123
                },
                's3': {
                    'roleArn': 'string',
                    'bucketName': 'string',
                    'key': 'string',
                    'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                },
                'firehose': {
                    'roleArn': 'string',
                    'deliveryStreamName': 'string',
                    'separator': 'string'
                },
                'cloudwatchMetric': {
                    'roleArn': 'string',
                    'metricNamespace': 'string',
                    'metricName': 'string',
                    'metricValue': 'string',
                    'metricUnit': 'string',
                    'metricTimestamp': 'string'
                },
                'cloudwatchAlarm': {
                    'roleArn': 'string',
                    'alarmName': 'string',
                    'stateReason': 'string',
                    'stateValue': 'string'
                },
                'cloudwatchLogs': {
                    'roleArn': 'string',
                    'logGroupName': 'string'
                },
                'elasticsearch': {
                    'roleArn': 'string',
                    'endpoint': 'string',
                    'index': 'string',
                    'type': 'string',
                    'id': 'string'
                },
                'salesforce': {
                    'token': 'string',
                    'url': 'string'
                },
                'iotAnalytics': {
                    'channelArn': 'string',
                    'channelName': 'string',
                    'roleArn': 'string'
                },
                'iotEvents': {
                    'inputName': 'string',
                    'messageId': 'string',
                    'roleArn': 'string'
                },
                'iotSiteWise': {
                    'putAssetPropertyValueEntries': [
                        {
                            'entryId': 'string',
                            'assetId': 'string',
                            'propertyId': 'string',
                            'propertyAlias': 'string',
                            'propertyValues': [
                                {
                                    'value': {
                                        'stringValue': 'string',
                                        'integerValue': 'string',
                                        'doubleValue': 'string',
                                        'booleanValue': 'string'
                                    },
                                    'timestamp': {
                                        'timeInSeconds': 'string',
                                        'offsetInNanos': 'string'
                                    },
                                    'quality': 'string'
                                },
                            ]
                        },
                    ],
                    'roleArn': 'string'
                },
                'stepFunctions': {
                    'executionNamePrefix': 'string',
                    'stateMachineName': 'string',
                    'roleArn': 'string'
                },
                'http': {
                    'url': 'string',
                    'confirmationUrl': 'string',
                    'headers': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'auth': {
                        'sigv4': {
                            'signingRegion': 'string',
                            'serviceName': 'string',
                            'roleArn': 'string'
                        }
                    }
                }
            }
        }
    )
    
    
    :type ruleName: string
    :param ruleName: [REQUIRED]\nThe name of the rule.\n

    :type topicRulePayload: dict
    :param topicRulePayload: [REQUIRED]\nThe rule payload.\n\nsql (string) -- [REQUIRED]The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference in the AWS IoT Developer Guide .\n\ndescription (string) --The description of the rule.\n\nactions (list) -- [REQUIRED]The actions associated with the rule.\n\n(dict) --Describes the actions associated with a rule.\n\ndynamoDB (dict) --Write to a DynamoDB table.\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.\n\noperation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .\n\nhashKeyField (string) -- [REQUIRED]The hash key name.\n\nhashKeyValue (string) -- [REQUIRED]The hash key value.\n\nhashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'\n\nrangeKeyField (string) --The range key name.\n\nrangeKeyValue (string) --The range key value.\n\nrangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'\n\npayloadField (string) --The action payload. This name can be customized.\n\n\n\ndynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.\n\nputItem (dict) -- [REQUIRED]Specifies the DynamoDB table to which the message data will be written. For example:\n\n{ 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }\nEach attribute in the message payload will be written to a separate column in the DynamoDB database.\n\ntableName (string) -- [REQUIRED]The table where the message data will be written.\n\n\n\n\n\nlambda (dict) --Invoke a Lambda function.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function.\n\n\n\nsns (dict) --Publish to an Amazon SNS topic.\n\ntargetArn (string) -- [REQUIRED]The ARN of the SNS topic.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nmessageFormat (string) --(Optional) The message format of the message to publish. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see https://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.\n\n\n\nsqs (dict) --Publish to an Amazon SQS queue.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nqueueUrl (string) -- [REQUIRED]The URL of the Amazon SQS queue.\n\nuseBase64 (boolean) --Specifies whether to use Base64 encoding.\n\n\n\nkinesis (dict) --Write data to an Amazon Kinesis stream.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the Amazon Kinesis stream.\n\nstreamName (string) -- [REQUIRED]The name of the Amazon Kinesis stream.\n\npartitionKey (string) --The partition key.\n\n\n\nrepublish (dict) --Publish to another MQTT topic.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\ntopic (string) -- [REQUIRED]The name of the MQTT topic.\n\nqos (integer) --The Quality of Service (QoS) level to use when republishing messages. The default value is 0.\n\n\n\ns3 (dict) --Write to an Amazon S3 bucket.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nbucketName (string) -- [REQUIRED]The Amazon S3 bucket.\n\nkey (string) -- [REQUIRED]The object key.\n\ncannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .\n\n\n\nfirehose (dict) --Write to an Amazon Kinesis Firehose stream.\n\nroleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehose stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The delivery stream name.\n\nseparator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\n\n\ncloudwatchMetric (dict) --Capture a CloudWatch metric.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch metric.\n\nmetricNamespace (string) -- [REQUIRED]The CloudWatch metric namespace name.\n\nmetricName (string) -- [REQUIRED]The CloudWatch metric name.\n\nmetricValue (string) -- [REQUIRED]The CloudWatch metric value.\n\nmetricUnit (string) -- [REQUIRED]The metric unit supported by CloudWatch.\n\nmetricTimestamp (string) --An optional Unix timestamp .\n\n\n\ncloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch alarm.\n\nalarmName (string) -- [REQUIRED]The CloudWatch alarm name.\n\nstateReason (string) -- [REQUIRED]The reason for the alarm change.\n\nstateValue (string) -- [REQUIRED]The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.\n\n\n\ncloudwatchLogs (dict) --Send data to CloudWatch Logs.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch log.\n\nlogGroupName (string) -- [REQUIRED]The CloudWatch log group to which the action sends data.\n\n\n\nelasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.\n\nroleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.\n\nendpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.\n\nindex (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.\n\ntype (string) -- [REQUIRED]The type of document you are storing.\n\nid (string) -- [REQUIRED]The unique identifier for the document you are storing.\n\n\n\nsalesforce (dict) --Send a message to a Salesforce IoT Cloud Input Stream.\n\ntoken (string) -- [REQUIRED]The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.\n\nurl (string) -- [REQUIRED]The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.\n\n\n\niotAnalytics (dict) --Sends message data to an AWS IoT Analytics channel.\n\nchannelArn (string) --(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.\n\nchannelName (string) --The name of the IoT Analytics channel to which message data will be sent.\n\nroleArn (string) --The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).\n\n\n\niotEvents (dict) --Sends an input to an AWS IoT Events detector.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input.\n\nmessageId (string) --[Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ('Action':'iotevents:BatchPutMessage').\n\n\n\niotSiteWise (dict) --Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.\n\nputAssetPropertyValueEntries (list) -- [REQUIRED]A list of asset property value entries.\n\n(dict) --An asset property value entry containing the following information.\n\nentryId (string) --Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.\n\nassetId (string) --The ID of the AWS IoT SiteWise asset. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyId (string) --The ID of the asset\'s property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyAlias (string) --The name of the property alias associated with your asset property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyValues (list) -- [REQUIRED]A list of property values to insert that each contain timestamp, quality, and value (TQV) information.\n\n(dict) --An asset property value entry containing the following information.\n\nvalue (dict) -- [REQUIRED]The value of the asset property.\n\nstringValue (string) --Optional. The string value of the value entry. Accepts substitution templates.\n\nintegerValue (string) --Optional. A string that contains the integer value of the value entry. Accepts substitution templates.\n\ndoubleValue (string) --Optional. A string that contains the double value of the value entry. Accepts substitution templates.\n\nbooleanValue (string) --Optional. A string that contains the boolean value (true or false ) of the value entry. Accepts substitution templates.\n\n\n\ntimestamp (dict) -- [REQUIRED]The asset property value timestamp.\n\ntimeInSeconds (string) -- [REQUIRED]A string that contains the time in seconds since epoch. Accepts substitution templates.\n\noffsetInNanos (string) --Optional. A string that contains the nanosecond time offset. Accepts substitution templates.\n\n\n\nquality (string) --Optional. A string that describes the quality of the value. Accepts substitution templates. Must be GOOD , BAD , or UNCERTAIN .\n\n\n\n\n\n\n\n\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoTSiteWise. ('Action': 'iotsitewise:BatchPutAssetPropertyValue' ). The trust policy can restrict access to specific asset hierarchy paths.\n\n\n\nstepFunctions (dict) --Starts execution of a Step Functions state machine.\n\nexecutionNamePrefix (string) --(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.\n\nstateMachineName (string) -- [REQUIRED]The name of the Step Functions state machine whose execution will be started.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants IoT permission to start execution of a state machine ('Action':'states:StartExecution').\n\n\n\nhttp (dict) --Send data to an HTTPS endpoint.\n\nurl (string) -- [REQUIRED]The endpoint URL. If substitution templates are used in the URL, you must also specify a confirmationUrl . If this is a new destination, a new TopicRuleDestination is created if possible.\n\nconfirmationUrl (string) --The URL to which AWS IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.\n\nheaders (list) --The HTTP headers to send with the message data.\n\n(dict) --The HTTP action header.\n\nkey (string) -- [REQUIRED]The HTTP header key.\n\nvalue (string) -- [REQUIRED]The HTTP header value. Substitution templates are supported.\n\n\n\n\n\nauth (dict) --The authentication method to use when sending data to an HTTPS endpoint.\n\nsigv4 (dict) --Use Sig V4 authorization. For more information, see Signature Version 4 Signing Process .\n\nsigningRegion (string) -- [REQUIRED]The signing region.\n\nserviceName (string) -- [REQUIRED]The service name to use while signing with Sig V4.\n\nroleArn (string) -- [REQUIRED]The ARN of the signing role.\n\n\n\n\n\n\n\n\n\n\n\nruleDisabled (boolean) --Specifies whether the rule is disabled.\n\nawsIotSqlVersion (string) --The version of the SQL rules engine to use when evaluating the rule.\n\nerrorAction (dict) --The action to take when an error occurs.\n\ndynamoDB (dict) --Write to a DynamoDB table.\n\ntableName (string) -- [REQUIRED]The name of the DynamoDB table.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.\n\noperation (string) --The type of operation to be performed. This follows the substitution template, so it can be ${operation} , but the substitution must result in one of the following: INSERT , UPDATE , or DELETE .\n\nhashKeyField (string) -- [REQUIRED]The hash key name.\n\nhashKeyValue (string) -- [REQUIRED]The hash key value.\n\nhashKeyType (string) --The hash key type. Valid values are 'STRING' or 'NUMBER'\n\nrangeKeyField (string) --The range key name.\n\nrangeKeyValue (string) --The range key value.\n\nrangeKeyType (string) --The range key type. Valid values are 'STRING' or 'NUMBER'\n\npayloadField (string) --The action payload. This name can be customized.\n\n\n\ndynamoDBv2 (dict) --Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the DynamoDB table.\n\nputItem (dict) -- [REQUIRED]Specifies the DynamoDB table to which the message data will be written. For example:\n\n{ 'dynamoDBv2': { 'roleArn': 'aws:iam:12341251:my-role' 'putItem': { 'tableName': 'my-table' } } }\nEach attribute in the message payload will be written to a separate column in the DynamoDB database.\n\ntableName (string) -- [REQUIRED]The table where the message data will be written.\n\n\n\n\n\nlambda (dict) --Invoke a Lambda function.\n\nfunctionArn (string) -- [REQUIRED]The ARN of the Lambda function.\n\n\n\nsns (dict) --Publish to an Amazon SNS topic.\n\ntargetArn (string) -- [REQUIRED]The ARN of the SNS topic.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nmessageFormat (string) --(Optional) The message format of the message to publish. Accepted values are 'JSON' and 'RAW'. The default value of the attribute is 'RAW'. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see https://docs.aws.amazon.com/sns/latest/dg/json-formats.html refer to their official documentation.\n\n\n\nsqs (dict) --Publish to an Amazon SQS queue.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nqueueUrl (string) -- [REQUIRED]The URL of the Amazon SQS queue.\n\nuseBase64 (boolean) --Specifies whether to use Base64 encoding.\n\n\n\nkinesis (dict) --Write data to an Amazon Kinesis stream.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access to the Amazon Kinesis stream.\n\nstreamName (string) -- [REQUIRED]The name of the Amazon Kinesis stream.\n\npartitionKey (string) --The partition key.\n\n\n\nrepublish (dict) --Publish to another MQTT topic.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\ntopic (string) -- [REQUIRED]The name of the MQTT topic.\n\nqos (integer) --The Quality of Service (QoS) level to use when republishing messages. The default value is 0.\n\n\n\ns3 (dict) --Write to an Amazon S3 bucket.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nbucketName (string) -- [REQUIRED]The Amazon S3 bucket.\n\nkey (string) -- [REQUIRED]The object key.\n\ncannedAcl (string) --The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see S3 canned ACLs .\n\n\n\nfirehose (dict) --Write to an Amazon Kinesis Firehose stream.\n\nroleArn (string) -- [REQUIRED]The IAM role that grants access to the Amazon Kinesis Firehose stream.\n\ndeliveryStreamName (string) -- [REQUIRED]The delivery stream name.\n\nseparator (string) --A character separator that will be used to separate records written to the Firehose stream. Valid values are: \'n\' (newline), \'t\' (tab), \'rn\' (Windows newline), \',\' (comma).\n\n\n\ncloudwatchMetric (dict) --Capture a CloudWatch metric.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch metric.\n\nmetricNamespace (string) -- [REQUIRED]The CloudWatch metric namespace name.\n\nmetricName (string) -- [REQUIRED]The CloudWatch metric name.\n\nmetricValue (string) -- [REQUIRED]The CloudWatch metric value.\n\nmetricUnit (string) -- [REQUIRED]The metric unit supported by CloudWatch.\n\nmetricTimestamp (string) --An optional Unix timestamp .\n\n\n\ncloudwatchAlarm (dict) --Change the state of a CloudWatch alarm.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch alarm.\n\nalarmName (string) -- [REQUIRED]The CloudWatch alarm name.\n\nstateReason (string) -- [REQUIRED]The reason for the alarm change.\n\nstateValue (string) -- [REQUIRED]The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.\n\n\n\ncloudwatchLogs (dict) --Send data to CloudWatch Logs.\n\nroleArn (string) -- [REQUIRED]The IAM role that allows access to the CloudWatch log.\n\nlogGroupName (string) -- [REQUIRED]The CloudWatch log group to which the action sends data.\n\n\n\nelasticsearch (dict) --Write data to an Amazon Elasticsearch Service domain.\n\nroleArn (string) -- [REQUIRED]The IAM role ARN that has access to Elasticsearch.\n\nendpoint (string) -- [REQUIRED]The endpoint of your Elasticsearch domain.\n\nindex (string) -- [REQUIRED]The Elasticsearch index where you want to store your data.\n\ntype (string) -- [REQUIRED]The type of document you are storing.\n\nid (string) -- [REQUIRED]The unique identifier for the document you are storing.\n\n\n\nsalesforce (dict) --Send a message to a Salesforce IoT Cloud Input Stream.\n\ntoken (string) -- [REQUIRED]The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.\n\nurl (string) -- [REQUIRED]The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.\n\n\n\niotAnalytics (dict) --Sends message data to an AWS IoT Analytics channel.\n\nchannelArn (string) --(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.\n\nchannelName (string) --The name of the IoT Analytics channel to which message data will be sent.\n\nroleArn (string) --The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).\n\n\n\niotEvents (dict) --Sends an input to an AWS IoT Events detector.\n\ninputName (string) -- [REQUIRED]The name of the AWS IoT Events input.\n\nmessageId (string) --[Optional] Use this to ensure that only one input (message) with a given messageId will be processed by an AWS IoT Events detector.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ('Action':'iotevents:BatchPutMessage').\n\n\n\niotSiteWise (dict) --Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.\n\nputAssetPropertyValueEntries (list) -- [REQUIRED]A list of asset property value entries.\n\n(dict) --An asset property value entry containing the following information.\n\nentryId (string) --Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.\n\nassetId (string) --The ID of the AWS IoT SiteWise asset. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyId (string) --The ID of the asset\'s property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyAlias (string) --The name of the property alias associated with your asset property. You must specify either a propertyAlias or both an aliasId and a propertyId . Accepts substitution templates.\n\npropertyValues (list) -- [REQUIRED]A list of property values to insert that each contain timestamp, quality, and value (TQV) information.\n\n(dict) --An asset property value entry containing the following information.\n\nvalue (dict) -- [REQUIRED]The value of the asset property.\n\nstringValue (string) --Optional. The string value of the value entry. Accepts substitution templates.\n\nintegerValue (string) --Optional. A string that contains the integer value of the value entry. Accepts substitution templates.\n\ndoubleValue (string) --Optional. A string that contains the double value of the value entry. Accepts substitution templates.\n\nbooleanValue (string) --Optional. A string that contains the boolean value (true or false ) of the value entry. Accepts substitution templates.\n\n\n\ntimestamp (dict) -- [REQUIRED]The asset property value timestamp.\n\ntimeInSeconds (string) -- [REQUIRED]A string that contains the time in seconds since epoch. Accepts substitution templates.\n\noffsetInNanos (string) --Optional. A string that contains the nanosecond time offset. Accepts substitution templates.\n\n\n\nquality (string) --Optional. A string that describes the quality of the value. Accepts substitution templates. Must be GOOD , BAD , or UNCERTAIN .\n\n\n\n\n\n\n\n\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoTSiteWise. ('Action': 'iotsitewise:BatchPutAssetPropertyValue' ). The trust policy can restrict access to specific asset hierarchy paths.\n\n\n\nstepFunctions (dict) --Starts execution of a Step Functions state machine.\n\nexecutionNamePrefix (string) --(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.\n\nstateMachineName (string) -- [REQUIRED]The name of the Step Functions state machine whose execution will be started.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants IoT permission to start execution of a state machine ('Action':'states:StartExecution').\n\n\n\nhttp (dict) --Send data to an HTTPS endpoint.\n\nurl (string) -- [REQUIRED]The endpoint URL. If substitution templates are used in the URL, you must also specify a confirmationUrl . If this is a new destination, a new TopicRuleDestination is created if possible.\n\nconfirmationUrl (string) --The URL to which AWS IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.\n\nheaders (list) --The HTTP headers to send with the message data.\n\n(dict) --The HTTP action header.\n\nkey (string) -- [REQUIRED]The HTTP header key.\n\nvalue (string) -- [REQUIRED]The HTTP header value. Substitution templates are supported.\n\n\n\n\n\nauth (dict) --The authentication method to use when sending data to an HTTPS endpoint.\n\nsigv4 (dict) --Use Sig V4 authorization. For more information, see Signature Version 4 Signing Process .\n\nsigningRegion (string) -- [REQUIRED]The signing region.\n\nserviceName (string) -- [REQUIRED]The service name to use while signing with Sig V4.\n\nroleArn (string) -- [REQUIRED]The ARN of the signing role.\n\n\n\n\n\n\n\n\n\n\n

    :returns: 
    IoT.Client.exceptions.SqlParseException
    IoT.Client.exceptions.InternalException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ConflictingResourceUpdateException
    
    """
    pass

def search_index(indexName=None, queryString=None, nextToken=None, maxResults=None, queryVersion=None):
    """
    The query search index.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.search_index(
        indexName='string',
        queryString='string',
        nextToken='string',
        maxResults=123,
        queryVersion='string'
    )
    
    
    :type indexName: string
    :param indexName: The search index name.

    :type queryString: string
    :param queryString: [REQUIRED]\nThe search query string.\n

    :type nextToken: string
    :param nextToken: The token used to get the next set of results, or null if there are no additional results.

    :type maxResults: integer
    :param maxResults: The maximum number of results to return at one time.

    :type queryVersion: string
    :param queryVersion: The query version.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'things': [
        {
            'thingName': 'string',
            'thingId': 'string',
            'thingTypeName': 'string',
            'thingGroupNames': [
                'string',
            ],
            'attributes': {
                'string': 'string'
            },
            'shadow': 'string',
            'connectivity': {
                'connected': True|False,
                'timestamp': 123
            }
        },
    ],
    'thingGroups': [
        {
            'thingGroupName': 'string',
            'thingGroupId': 'string',
            'thingGroupDescription': 'string',
            'attributes': {
                'string': 'string'
            },
            'parentGroupNames': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
The token used to get the next set of results, or null if there are no additional results.

things (list) --
The things that match the search query.

(dict) --
The thing search index document.

thingName (string) --
The thing name.

thingId (string) --
The thing ID.

thingTypeName (string) --
The thing type name.

thingGroupNames (list) --
Thing group names.

(string) --


attributes (dict) --
The attributes.

(string) --
(string) --




shadow (string) --
The shadow.

connectivity (dict) --
Indicates whether the thing is connected to the AWS IoT service.

connected (boolean) --
True if the thing is connected to the AWS IoT service; false if it is not connected.

timestamp (integer) --
The epoch time (in milliseconds) when the thing last connected or disconnected. If the thing has been disconnected for more than a few weeks, the time value might be missing.







thingGroups (list) --
The thing groups that match the search query.

(dict) --
The thing group search index document.

thingGroupName (string) --
The thing group name.

thingGroupId (string) --
The thing group ID.

thingGroupDescription (string) --
The thing group description.

attributes (dict) --
The thing group attributes.

(string) --
(string) --




parentGroupNames (list) --
Parent group names.

(string) --












Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidQueryException
IoT.Client.exceptions.IndexNotReadyException


    :return: {
        'nextToken': 'string',
        'things': [
            {
                'thingName': 'string',
                'thingId': 'string',
                'thingTypeName': 'string',
                'thingGroupNames': [
                    'string',
                ],
                'attributes': {
                    'string': 'string'
                },
                'shadow': 'string',
                'connectivity': {
                    'connected': True|False,
                    'timestamp': 123
                }
            },
        ],
        'thingGroups': [
            {
                'thingGroupName': 'string',
                'thingGroupId': 'string',
                'thingGroupDescription': 'string',
                'attributes': {
                    'string': 'string'
                },
                'parentGroupNames': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def set_default_authorizer(authorizerName=None):
    """
    Sets the default authorizer. This will be used if a websocket connection is made without specifying an authorizer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_default_authorizer(
        authorizerName='string'
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]\nThe authorizer name.\n

    :rtype: dict
ReturnsResponse Syntax{
    'authorizerName': 'string',
    'authorizerArn': 'string'
}


Response Structure

(dict) --
authorizerName (string) --The authorizer name.

authorizerArn (string) --The authorizer ARN.






Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceAlreadyExistsException


    :return: {
        'authorizerName': 'string',
        'authorizerArn': 'string'
    }
    
    
    """
    pass

def set_default_policy_version(policyName=None, policyVersionId=None):
    """
    Sets the specified version of the specified policy as the policy\'s default (operative) version. This action affects all certificates to which the policy is attached. To list the principals the policy is attached to, use the ListPrincipalPolicy API.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_default_policy_version(
        policyName='string',
        policyVersionId='string'
    )
    
    
    :type policyName: string
    :param policyName: [REQUIRED]\nThe policy name.\n

    :type policyVersionId: string
    :param policyVersionId: [REQUIRED]\nThe policy version ID.\n

    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def set_logging_options(loggingOptionsPayload=None):
    """
    Sets the logging options.
    NOTE: use of this command is not recommended. Use SetV2LoggingOptions instead.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_logging_options(
        loggingOptionsPayload={
            'roleArn': 'string',
            'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
        }
    )
    
    
    :type loggingOptionsPayload: dict
    :param loggingOptionsPayload: [REQUIRED]\nThe logging options payload.\n\nroleArn (string) -- [REQUIRED]The ARN of the IAM role that grants access.\n\nlogLevel (string) --The log level.\n\n\n

    """
    pass

def set_v2_logging_level(logTarget=None, logLevel=None):
    """
    Sets the logging level.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_v2_logging_level(
        logTarget={
            'targetType': 'DEFAULT'|'THING_GROUP',
            'targetName': 'string'
        },
        logLevel='DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
    )
    
    
    :type logTarget: dict
    :param logTarget: [REQUIRED]\nThe log target.\n\ntargetType (string) -- [REQUIRED]The target type.\n\ntargetName (string) --The target name.\n\n\n

    :type logLevel: string
    :param logLevel: [REQUIRED]\nThe log level.\n

    :returns: 
    IoT.Client.exceptions.InternalException
    IoT.Client.exceptions.NotConfiguredException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def set_v2_logging_options(roleArn=None, defaultLogLevel=None, disableAllLogs=None):
    """
    Sets the logging options for the V2 logging service.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.set_v2_logging_options(
        roleArn='string',
        defaultLogLevel='DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED',
        disableAllLogs=True|False
    )
    
    
    :type roleArn: string
    :param roleArn: The ARN of the role that allows IoT to write to Cloudwatch logs.

    :type defaultLogLevel: string
    :param defaultLogLevel: The default logging level.

    :type disableAllLogs: boolean
    :param disableAllLogs: If true all logs are disabled. The default is false.

    :returns: 
    IoT.Client.exceptions.InternalException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def start_audit_mitigation_actions_task(taskId=None, target=None, auditCheckToActionsMapping=None, clientRequestToken=None):
    """
    Starts a task that applies a set of mitigation actions to the specified target.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_audit_mitigation_actions_task(
        taskId='string',
        target={
            'auditTaskId': 'string',
            'findingIds': [
                'string',
            ],
            'auditCheckToReasonCodeFilter': {
                'string': [
                    'string',
                ]
            }
        },
        auditCheckToActionsMapping={
            'string': [
                'string',
            ]
        },
        clientRequestToken='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]\nA unique identifier for the task. You can use this identifier to check the status of the task or to cancel it.\n

    :type target: dict
    :param target: [REQUIRED]\nSpecifies the audit findings to which the mitigation actions are applied. You can apply them to a type of audit check, to all findings from an audit, or to a speecific set of findings.\n\nauditTaskId (string) --If the task will apply a mitigation action to findings from a specific audit, this value uniquely identifies the audit.\n\nfindingIds (list) --If the task will apply a mitigation action to one or more listed findings, this value uniquely identifies those findings.\n\n(string) --\n\n\nauditCheckToReasonCodeFilter (dict) --Specifies a filter in the form of an audit check and set of reason codes that identify the findings from the audit to which the audit mitigation actions task apply.\n\n(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)\n\n(list) --\n(string) --\n\n\n\n\n\n\n\n

    :type auditCheckToActionsMapping: dict
    :param auditCheckToActionsMapping: [REQUIRED]\nFor an audit check, specifies which mitigation actions to apply. Those actions must be defined in your AWS account.\n\n(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)\n\n(list) --\n(string) --\n\n\n\n\n\n

    :type clientRequestToken: string
    :param clientRequestToken: [REQUIRED]\nEach audit mitigation task must have a unique client request token. If you try to start a new task with the same token as a task that already exists, an exception occurs. If you omit this value, a unique client request token is generated automatically.\nThis field is autopopulated if not provided.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'taskId': 'string'
}


Response Structure

(dict) --

taskId (string) --
The unique identifier for the audit mitigation task. This matches the taskId that you specified in the request.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.TaskAlreadyExistsException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'taskId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.TaskAlreadyExistsException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def start_on_demand_audit_task(targetCheckNames=None):
    """
    Starts an on-demand Device Defender audit.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_on_demand_audit_task(
        targetCheckNames=[
            'string',
        ]
    )
    
    
    :type targetCheckNames: list
    :param targetCheckNames: [REQUIRED]\nWhich checks are performed during the audit. The checks you specify must be enabled for your account or an exception occurs. Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or UpdateAccountAuditConfiguration to select which checks are enabled.\n\n(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'taskId': 'string'
}


Response Structure

(dict) --
taskId (string) --The ID of the on-demand audit you started.






Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.LimitExceededException


    :return: {
        'taskId': 'string'
    }
    
    
    """
    pass

def start_thing_registration_task(templateBody=None, inputFileBucket=None, inputFileKey=None, roleArn=None):
    """
    Creates a bulk thing provisioning task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_thing_registration_task(
        templateBody='string',
        inputFileBucket='string',
        inputFileKey='string',
        roleArn='string'
    )
    
    
    :type templateBody: string
    :param templateBody: [REQUIRED]\nThe provisioning template.\n

    :type inputFileBucket: string
    :param inputFileBucket: [REQUIRED]\nThe S3 bucket that contains the input file.\n

    :type inputFileKey: string
    :param inputFileKey: [REQUIRED]\nThe name of input file within the S3 bucket. This file contains a newline delimited JSON file. Each line contains the parameter values to provision one device (thing).\n

    :type roleArn: string
    :param roleArn: [REQUIRED]\nThe IAM role ARN that grants permission the input file.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'taskId': 'string'
}


Response Structure

(dict) --

taskId (string) --
The bulk thing provisioning task ID.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'taskId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def stop_thing_registration_task(taskId=None):
    """
    Cancels a bulk thing provisioning task.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_thing_registration_task(
        taskId='string'
    )
    
    
    :type taskId: string
    :param taskId: [REQUIRED]\nThe bulk thing provisioning task ID.\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource.\n

    :type tags: list
    :param tags: [REQUIRED]\nThe new or modified tags for the resource.\n\n(dict) --A set of key/value pairs that are used to manage the resource.\n\nKey (string) -- [REQUIRED]The tag\'s key.\n\nValue (string) --The tag\'s value.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.LimitExceededException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def test_authorization(principal=None, cognitoIdentityPoolId=None, authInfos=None, clientId=None, policyNamesToAdd=None, policyNamesToSkip=None):
    """
    Tests if a specified principal is authorized to perform an AWS IoT action on a specified resource. Use this to test and debug the authorization behavior of devices that connect to the AWS IoT device gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.test_authorization(
        principal='string',
        cognitoIdentityPoolId='string',
        authInfos=[
            {
                'actionType': 'PUBLISH'|'SUBSCRIBE'|'RECEIVE'|'CONNECT',
                'resources': [
                    'string',
                ]
            },
        ],
        clientId='string',
        policyNamesToAdd=[
            'string',
        ],
        policyNamesToSkip=[
            'string',
        ]
    )
    
    
    :type principal: string
    :param principal: The principal.

    :type cognitoIdentityPoolId: string
    :param cognitoIdentityPoolId: The Cognito identity pool ID.

    :type authInfos: list
    :param authInfos: [REQUIRED]\nA list of authorization info objects. Simulating authorization will create a response for each authInfo object in the list.\n\n(dict) --A collection of authorization information.\n\nactionType (string) --The type of action for which the principal is being authorized.\n\nresources (list) -- [REQUIRED]The resources for which the principal is being authorized to perform the specified action.\n\n(string) --\n\n\n\n\n\n

    :type clientId: string
    :param clientId: The MQTT client ID.

    :type policyNamesToAdd: list
    :param policyNamesToAdd: When testing custom authorization, the policies specified here are treated as if they are attached to the principal being authorized.\n\n(string) --\n\n

    :type policyNamesToSkip: list
    :param policyNamesToSkip: When testing custom authorization, the policies specified here are treated as if they are not attached to the principal being authorized.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'authResults': [
        {
            'authInfo': {
                'actionType': 'PUBLISH'|'SUBSCRIBE'|'RECEIVE'|'CONNECT',
                'resources': [
                    'string',
                ]
            },
            'allowed': {
                'policies': [
                    {
                        'policyName': 'string',
                        'policyArn': 'string'
                    },
                ]
            },
            'denied': {
                'implicitDeny': {
                    'policies': [
                        {
                            'policyName': 'string',
                            'policyArn': 'string'
                        },
                    ]
                },
                'explicitDeny': {
                    'policies': [
                        {
                            'policyName': 'string',
                            'policyArn': 'string'
                        },
                    ]
                }
            },
            'authDecision': 'ALLOWED'|'EXPLICIT_DENY'|'IMPLICIT_DENY',
            'missingContextValues': [
                'string',
            ]
        },
    ]
}


Response Structure

(dict) --

authResults (list) --
The authentication results.

(dict) --
The authorizer result.

authInfo (dict) --
Authorization information.

actionType (string) --
The type of action for which the principal is being authorized.

resources (list) --
The resources for which the principal is being authorized to perform the specified action.

(string) --




allowed (dict) --
The policies and statements that allowed the specified action.

policies (list) --
A list of policies that allowed the authentication.

(dict) --
Describes an AWS IoT policy.

policyName (string) --
The policy name.

policyArn (string) --
The policy ARN.







denied (dict) --
The policies and statements that denied the specified action.

implicitDeny (dict) --
Information that implicitly denies the authorization. When a policy doesn\'t explicitly deny or allow an action on a resource it is considered an implicit deny.

policies (list) --
Policies that don\'t contain a matching allow or deny statement for the specified action on the specified resource.

(dict) --
Describes an AWS IoT policy.

policyName (string) --
The policy name.

policyArn (string) --
The policy ARN.







explicitDeny (dict) --
Information that explicitly denies the authorization.

policies (list) --
The policies that denied the authorization.

(dict) --
Describes an AWS IoT policy.

policyName (string) --
The policy name.

policyArn (string) --
The policy ARN.









authDecision (string) --
The final authorization decision of this scenario. Multiple statements are taken into account when determining the authorization decision. An explicit deny statement can override multiple allow statements.

missingContextValues (list) --
Contains any missing context values found while evaluating policy.

(string) --












Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.LimitExceededException


    :return: {
        'authResults': [
            {
                'authInfo': {
                    'actionType': 'PUBLISH'|'SUBSCRIBE'|'RECEIVE'|'CONNECT',
                    'resources': [
                        'string',
                    ]
                },
                'allowed': {
                    'policies': [
                        {
                            'policyName': 'string',
                            'policyArn': 'string'
                        },
                    ]
                },
                'denied': {
                    'implicitDeny': {
                        'policies': [
                            {
                                'policyName': 'string',
                                'policyArn': 'string'
                            },
                        ]
                    },
                    'explicitDeny': {
                        'policies': [
                            {
                                'policyName': 'string',
                                'policyArn': 'string'
                            },
                        ]
                    }
                },
                'authDecision': 'ALLOWED'|'EXPLICIT_DENY'|'IMPLICIT_DENY',
                'missingContextValues': [
                    'string',
                ]
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def test_invoke_authorizer(authorizerName=None, token=None, tokenSignature=None, httpContext=None, mqttContext=None, tlsContext=None):
    """
    Tests a custom authorization behavior by invoking a specified custom authorizer. Use this to test and debug the custom authorization behavior of devices that connect to the AWS IoT device gateway.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.test_invoke_authorizer(
        authorizerName='string',
        token='string',
        tokenSignature='string',
        httpContext={
            'headers': {
                'string': 'string'
            },
            'queryString': 'string'
        },
        mqttContext={
            'username': 'string',
            'password': b'bytes',
            'clientId': 'string'
        },
        tlsContext={
            'serverName': 'string'
        }
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]\nThe custom authorizer name.\n

    :type token: string
    :param token: The token returned by your custom authentication service.

    :type tokenSignature: string
    :param tokenSignature: The signature made with the token and your custom authentication service\'s private key. This value must be Base-64-encoded.

    :type httpContext: dict
    :param httpContext: Specifies a test HTTP authorization request.\n\nheaders (dict) --The header keys and values in an HTTP authorization request.\n\n(string) --\n(string) --\n\n\n\n\nqueryString (string) --The query string keys and values in an HTTP authorization request.\n\n\n

    :type mqttContext: dict
    :param mqttContext: Specifies a test MQTT authorization request.\n\nusername (string) --The value of the username key in an MQTT authorization request.\n\npassword (bytes) --The value of the password key in an MQTT authorization request.\n\nclientId (string) --The value of the clientId key in an MQTT authorization request.\n\n\n

    :type tlsContext: dict
    :param tlsContext: Specifies a test TLS authorization request.\n\nserverName (string) --The value of the serverName key in a TLS authorization request.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'isAuthenticated': True|False,
    'principalId': 'string',
    'policyDocuments': [
        'string',
    ],
    'refreshAfterInSeconds': 123,
    'disconnectAfterInSeconds': 123
}


Response Structure

(dict) --

isAuthenticated (boolean) --
True if the token is authenticated, otherwise false.

principalId (string) --
The principal ID.

policyDocuments (list) --
IAM policy documents.

(string) --


refreshAfterInSeconds (integer) --
The number of seconds after which the temporary credentials are refreshed.

disconnectAfterInSeconds (integer) --
The number of seconds after which the connection is terminated.







Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidResponseException


    :return: {
        'isAuthenticated': True|False,
        'principalId': 'string',
        'policyDocuments': [
            'string',
        ],
        'refreshAfterInSeconds': 123,
        'disconnectAfterInSeconds': 123
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def transfer_certificate(certificateId=None, targetAwsAccount=None, transferMessage=None):
    """
    Transfers the specified certificate to the specified AWS account.
    You can cancel the transfer until it is acknowledged by the recipient.
    No notification is sent to the transfer destination\'s account. It is up to the caller to notify the transfer target.
    The certificate being transferred must not be in the ACTIVE state. You can use the UpdateCertificate API to deactivate it.
    The certificate must not have any policies attached to it. You can use the DetachPrincipalPolicy API to detach them.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.transfer_certificate(
        certificateId='string',
        targetAwsAccount='string',
        transferMessage='string'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]\nThe ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)\n

    :type targetAwsAccount: string
    :param targetAwsAccount: [REQUIRED]\nThe AWS account.\n

    :type transferMessage: string
    :param transferMessage: The transfer message.

    :rtype: dict

ReturnsResponse Syntax
{
    'transferredCertificateArn': 'string'
}


Response Structure

(dict) --
The output from the TransferCertificate operation.

transferredCertificateArn (string) --
The ARN of the certificate.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.CertificateStateException
IoT.Client.exceptions.TransferConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'transferredCertificateArn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.CertificateStateException
    IoT.Client.exceptions.TransferConflictException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Removes the given tags (metadata) from the resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nThe ARN of the resource.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nA list of the keys of the tags to be removed from the resource.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_account_audit_configuration(roleArn=None, auditNotificationTargetConfigurations=None, auditCheckConfigurations=None):
    """
    Configures or reconfigures the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_account_audit_configuration(
        roleArn='string',
        auditNotificationTargetConfigurations={
            'string': {
                'targetArn': 'string',
                'roleArn': 'string',
                'enabled': True|False
            }
        },
        auditCheckConfigurations={
            'string': {
                'enabled': True|False
            }
        }
    )
    
    
    :type roleArn: string
    :param roleArn: The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as required when performing an audit.

    :type auditNotificationTargetConfigurations: dict
    :param auditNotificationTargetConfigurations: Information about the targets to which audit notifications are sent.\n\n(string) --\n(dict) --Information about the targets to which audit notifications are sent.\n\ntargetArn (string) --The ARN of the target (SNS topic) to which audit notifications are sent.\n\nroleArn (string) --The ARN of the role that grants permission to send notifications to the target.\n\nenabled (boolean) --True if notifications to the target are enabled.\n\n\n\n\n\n\n

    :type auditCheckConfigurations: dict
    :param auditCheckConfigurations: Specifies which audit checks are enabled and disabled for this account. Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are currently enabled.\nSome data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted.\nYou cannot disable a check if it is used by any scheduled audit. You must first delete the check from the scheduled audit or delete the scheduled audit itself.\nOn the first call to UpdateAccountAuditConfiguration , this parameter is required and must specify at least one enabled check.\n\n(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)\n\n(dict) --Which audit checks are enabled and disabled for this account.\n\nenabled (boolean) --True if this audit check is enabled for this account.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_authorizer(authorizerName=None, authorizerFunctionArn=None, tokenKeyName=None, tokenSigningPublicKeys=None, status=None):
    """
    Updates an authorizer.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_authorizer(
        authorizerName='string',
        authorizerFunctionArn='string',
        tokenKeyName='string',
        tokenSigningPublicKeys={
            'string': 'string'
        },
        status='ACTIVE'|'INACTIVE'
    )
    
    
    :type authorizerName: string
    :param authorizerName: [REQUIRED]\nThe authorizer name.\n

    :type authorizerFunctionArn: string
    :param authorizerFunctionArn: The ARN of the authorizer\'s Lambda function.

    :type tokenKeyName: string
    :param tokenKeyName: The key used to extract the token from the HTTP headers.

    :type tokenSigningPublicKeys: dict
    :param tokenSigningPublicKeys: The public keys used to verify the token signature.\n\n(string) --\n(string) --\n\n\n\n

    :type status: string
    :param status: The status of the update authorizer request.

    :rtype: dict

ReturnsResponse Syntax
{
    'authorizerName': 'string',
    'authorizerArn': 'string'
}


Response Structure

(dict) --

authorizerName (string) --
The authorizer name.

authorizerArn (string) --
The authorizer ARN.







Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.LimitExceededException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'authorizerName': 'string',
        'authorizerArn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.LimitExceededException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def update_billing_group(billingGroupName=None, billingGroupProperties=None, expectedVersion=None):
    """
    Updates information about the billing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_billing_group(
        billingGroupName='string',
        billingGroupProperties={
            'billingGroupDescription': 'string'
        },
        expectedVersion=123
    )
    
    
    :type billingGroupName: string
    :param billingGroupName: [REQUIRED]\nThe name of the billing group.\n

    :type billingGroupProperties: dict
    :param billingGroupProperties: [REQUIRED]\nThe properties of the billing group.\n\nbillingGroupDescription (string) --The description of the billing group.\n\n\n

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the billing group. If the version of the billing group does not match the expected version specified in the request, the UpdateBillingGroup request is rejected with a VersionConflictException .

    :rtype: dict

ReturnsResponse Syntax
{
    'version': 123
}


Response Structure

(dict) --

version (integer) --
The latest version of the billing group.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.VersionConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'version': 123
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.VersionConflictException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_ca_certificate(certificateId=None, newStatus=None, newAutoRegistrationStatus=None, registrationConfig=None, removeAutoRegistration=None):
    """
    Updates a registered CA certificate.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_ca_certificate(
        certificateId='string',
        newStatus='ACTIVE'|'INACTIVE',
        newAutoRegistrationStatus='ENABLE'|'DISABLE',
        registrationConfig={
            'templateBody': 'string',
            'roleArn': 'string'
        },
        removeAutoRegistration=True|False
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]\nThe CA certificate identifier.\n

    :type newStatus: string
    :param newStatus: The updated status of the CA certificate.\n\nNote: The status value REGISTER_INACTIVE is deprecated and should not be used.\n

    :type newAutoRegistrationStatus: string
    :param newAutoRegistrationStatus: The new value for the auto registration status. Valid values are: 'ENABLE' or 'DISABLE'.

    :type registrationConfig: dict
    :param registrationConfig: Information about the registration configuration.\n\ntemplateBody (string) --The template body.\n\nroleArn (string) --The ARN of the role.\n\n\n

    :type removeAutoRegistration: boolean
    :param removeAutoRegistration: If true, removes auto registration.

    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def update_certificate(certificateId=None, newStatus=None):
    """
    Updates the status of the specified certificate. This operation is idempotent.
    Moving a certificate from the ACTIVE state (including REVOKED) will not disconnect currently connected devices, but these devices will be unable to reconnect.
    The ACTIVE state is required to authenticate devices connecting to AWS IoT using a certificate.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_certificate(
        certificateId='string',
        newStatus='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
    )
    
    
    :type certificateId: string
    :param certificateId: [REQUIRED]\nThe ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)\n

    :type newStatus: string
    :param newStatus: [REQUIRED]\nThe new status.\n\nNote: Setting the status to PENDING_TRANSFER or PENDING_ACTIVATION will result in an exception being thrown. PENDING_TRANSFER and PENDING_ACTIVATION are statuses used internally by AWS IoT. They are not intended for developer use.Note: The status value REGISTER_INACTIVE is deprecated and should not be used.\n\n

    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.CertificateStateException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def update_dimension(name=None, stringValues=None):
    """
    Updates the definition for a dimension. You cannot change the type of a dimension after it is created (you can delete it and re-create it).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_dimension(
        name='string',
        stringValues=[
            'string',
        ]
    )
    
    
    :type name: string
    :param name: [REQUIRED]\nA unique identifier for the dimension. Choose something that describes the type and value to make it easy to remember what it does.\n

    :type stringValues: list
    :param stringValues: [REQUIRED]\nSpecifies the value or list of values for the dimension. For TOPIC_FILTER dimensions, this is a pattern used to match the MQTT topic (for example, 'admin/#').\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'name': 'string',
    'arn': 'string',
    'type': 'TOPIC_FILTER',
    'stringValues': [
        'string',
    ],
    'creationDate': datetime(2015, 1, 1),
    'lastModifiedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

name (string) --
A unique identifier for the dimension.

arn (string) --
The ARN (Amazon resource name) of the created dimension.

type (string) --
The type of the dimension.

stringValues (list) --
The value or list of values used to scope the dimension. For example, for topic filters, this is the pattern used to match the MQTT topic name.

(string) --


creationDate (datetime) --
The date and time, in milliseconds since epoch, when the dimension was initially created.

lastModifiedDate (datetime) --
The date and time, in milliseconds since epoch, when the dimension was most recently updated.







Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException


    :return: {
        'name': 'string',
        'arn': 'string',
        'type': 'TOPIC_FILTER',
        'stringValues': [
            'string',
        ],
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_domain_configuration(domainConfigurationName=None, authorizerConfig=None, domainConfigurationStatus=None, removeAuthorizerConfig=None):
    """
    Updates values stored in the domain configuration. Domain configurations for default endpoints can\'t be updated.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_domain_configuration(
        domainConfigurationName='string',
        authorizerConfig={
            'defaultAuthorizerName': 'string',
            'allowAuthorizerOverride': True|False
        },
        domainConfigurationStatus='ENABLED'|'DISABLED',
        removeAuthorizerConfig=True|False
    )
    
    
    :type domainConfigurationName: string
    :param domainConfigurationName: [REQUIRED]\nThe name of the domain configuration to be updated.\n

    :type authorizerConfig: dict
    :param authorizerConfig: An object that specifies the authorization service for a domain.\n\ndefaultAuthorizerName (string) --The name of the authorization service for a domain configuration.\n\nallowAuthorizerOverride (boolean) --A Boolean that specifies whether the domain configuration\'s authorization service can be overridden.\n\n\n

    :type domainConfigurationStatus: string
    :param domainConfigurationStatus: The status to which the domain configuration should be updated.

    :type removeAuthorizerConfig: boolean
    :param removeAuthorizerConfig: Removes the authorization configuration from a domain.

    :rtype: dict

ReturnsResponse Syntax
{
    'domainConfigurationName': 'string',
    'domainConfigurationArn': 'string'
}


Response Structure

(dict) --

domainConfigurationName (string) --
The name of the domain configuration that was updated.

domainConfigurationArn (string) --
The ARN of the domain configuration that was updated.







Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.CertificateValidationException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'domainConfigurationName': 'string',
        'domainConfigurationArn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.CertificateValidationException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def update_dynamic_thing_group(thingGroupName=None, thingGroupProperties=None, expectedVersion=None, indexName=None, queryString=None, queryVersion=None):
    """
    Updates a dynamic thing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_dynamic_thing_group(
        thingGroupName='string',
        thingGroupProperties={
            'thingGroupDescription': 'string',
            'attributePayload': {
                'attributes': {
                    'string': 'string'
                },
                'merge': True|False
            }
        },
        expectedVersion=123,
        indexName='string',
        queryString='string',
        queryVersion='string'
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]\nThe name of the dynamic thing group to update.\n

    :type thingGroupProperties: dict
    :param thingGroupProperties: [REQUIRED]\nThe dynamic thing group properties to update.\n\nthingGroupDescription (string) --The thing group description.\n\nattributePayload (dict) --The thing group attributes in JSON format.\n\nattributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:\n\n{\\'attributes\\':{\\'string1\\':\\'string2\\'}}\n\n(string) --\n(string) --\n\n\n\n\nmerge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.\nTo remove an attribute, call UpdateThing with an empty attribute value.\n\nNote\nThe merge attribute is only valid when calling UpdateThing or UpdateThingGroup .\n\n\n\n\n\n

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the dynamic thing group to update.

    :type indexName: string
    :param indexName: The dynamic thing group index to update.\n\nNote\nCurrently one index is supported: \'AWS_Things\'.\n\n

    :type queryString: string
    :param queryString: The dynamic thing group search query string to update.

    :type queryVersion: string
    :param queryVersion: The dynamic thing group query version to update.\n\nNote\nCurrently one query version is supported: '2017-09-30'. If not specified, the query version defaults to this value.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'version': 123
}


Response Structure

(dict) --

version (integer) --
The dynamic thing group version.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.VersionConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidQueryException


    :return: {
        'version': 123
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.VersionConflictException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidQueryException
    
    """
    pass

def update_event_configurations(eventConfigurations=None):
    """
    Updates the event configurations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_event_configurations(
        eventConfigurations={
            'string': {
                'Enabled': True|False
            }
        }
    )
    
    
    :type eventConfigurations: dict
    :param eventConfigurations: The new event configuration values.\n\n(string) --\n(dict) --Configuration.\n\nEnabled (boolean) --True to enable the configuration.\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{}


Response Structure

(dict) --



Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ThrottlingException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ThrottlingException
    
    """
    pass

def update_indexing_configuration(thingIndexingConfiguration=None, thingGroupIndexingConfiguration=None):
    """
    Updates the search configuration.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_indexing_configuration(
        thingIndexingConfiguration={
            'thingIndexingMode': 'OFF'|'REGISTRY'|'REGISTRY_AND_SHADOW',
            'thingConnectivityIndexingMode': 'OFF'|'STATUS',
            'managedFields': [
                {
                    'name': 'string',
                    'type': 'Number'|'String'|'Boolean'
                },
            ],
            'customFields': [
                {
                    'name': 'string',
                    'type': 'Number'|'String'|'Boolean'
                },
            ]
        },
        thingGroupIndexingConfiguration={
            'thingGroupIndexingMode': 'OFF'|'ON',
            'managedFields': [
                {
                    'name': 'string',
                    'type': 'Number'|'String'|'Boolean'
                },
            ],
            'customFields': [
                {
                    'name': 'string',
                    'type': 'Number'|'String'|'Boolean'
                },
            ]
        }
    )
    
    
    :type thingIndexingConfiguration: dict
    :param thingIndexingConfiguration: Thing indexing configuration.\n\nthingIndexingMode (string) -- [REQUIRED]Thing indexing mode. Valid values are:\n\nREGISTRY \xe2\x80\x93 Your thing index contains registry data only.\nREGISTRY_AND_SHADOW - Your thing index contains registry and shadow data.\nOFF - Thing indexing is disabled.\n\n\nthingConnectivityIndexingMode (string) --Thing connectivity indexing mode. Valid values are:\n\nSTATUS \xe2\x80\x93 Your thing index contains connectivity status. To enable thing connectivity indexing, thingIndexMode must not be set to OFF.\nOFF - Thing connectivity status indexing is disabled.\n\n\nmanagedFields (list) --Contains fields that are indexed and whose types are already known by the Fleet Indexing service.\n\n(dict) --Describes the name and data type at a field.\n\nname (string) --The name of the field.\n\ntype (string) --The datatype of the field.\n\n\n\n\n\ncustomFields (list) --Contains custom field names and their data type.\n\n(dict) --Describes the name and data type at a field.\n\nname (string) --The name of the field.\n\ntype (string) --The datatype of the field.\n\n\n\n\n\n\n

    :type thingGroupIndexingConfiguration: dict
    :param thingGroupIndexingConfiguration: Thing group indexing configuration.\n\nthingGroupIndexingMode (string) -- [REQUIRED]Thing group indexing mode.\n\nmanagedFields (list) --Contains fields that are indexed and whose types are already known by the Fleet Indexing service.\n\n(dict) --Describes the name and data type at a field.\n\nname (string) --The name of the field.\n\ntype (string) --The datatype of the field.\n\n\n\n\n\ncustomFields (list) --A list of thing group fields to index. This list cannot contain any managed fields. Use the GetIndexingConfiguration API to get a list of managed fields.\nContains custom field names and their data type.\n\n(dict) --Describes the name and data type at a field.\n\nname (string) --The name of the field.\n\ntype (string) --The datatype of the field.\n\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_job(jobId=None, description=None, presignedUrlConfig=None, jobExecutionsRolloutConfig=None, abortConfig=None, timeoutConfig=None):
    """
    Updates supported fields of the specified job.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_job(
        jobId='string',
        description='string',
        presignedUrlConfig={
            'roleArn': 'string',
            'expiresInSec': 123
        },
        jobExecutionsRolloutConfig={
            'maximumPerMinute': 123,
            'exponentialRate': {
                'baseRatePerMinute': 123,
                'incrementFactor': 123.0,
                'rateIncreaseCriteria': {
                    'numberOfNotifiedThings': 123,
                    'numberOfSucceededThings': 123
                }
            }
        },
        abortConfig={
            'criteriaList': [
                {
                    'failureType': 'FAILED'|'REJECTED'|'TIMED_OUT'|'ALL',
                    'action': 'CANCEL',
                    'thresholdPercentage': 123.0,
                    'minNumberOfExecutedThings': 123
                },
            ]
        },
        timeoutConfig={
            'inProgressTimeoutInMinutes': 123
        }
    )
    
    
    :type jobId: string
    :param jobId: [REQUIRED]\nThe ID of the job to be updated.\n

    :type description: string
    :param description: A short text description of the job.

    :type presignedUrlConfig: dict
    :param presignedUrlConfig: Configuration information for pre-signed S3 URLs.\n\nroleArn (string) --The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.\n\nexpiresInSec (integer) --How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.\n\n\n

    :type jobExecutionsRolloutConfig: dict
    :param jobExecutionsRolloutConfig: Allows you to create a staged rollout of the job.\n\nmaximumPerMinute (integer) --The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.\n\nexponentialRate (dict) --The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.\n\nbaseRatePerMinute (integer) -- [REQUIRED]The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.\n\nincrementFactor (float) -- [REQUIRED]The exponential factor to increase the rate of rollout for a job.\n\nrateIncreaseCriteria (dict) -- [REQUIRED]The criteria to initiate the increase in rate of rollout for a job.\nAWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).\n\nnumberOfNotifiedThings (integer) --The threshold for number of notified things that will initiate the increase in rate of rollout.\n\nnumberOfSucceededThings (integer) --The threshold for number of succeeded things that will initiate the increase in rate of rollout.\n\n\n\n\n\n\n

    :type abortConfig: dict
    :param abortConfig: Allows you to create criteria to abort a job.\n\ncriteriaList (list) -- [REQUIRED]The list of abort criteria to define rules to abort the job.\n\n(dict) --Details of abort criteria to define rules to abort the job.\n\nfailureType (string) -- [REQUIRED]The type of job execution failure to define a rule to initiate a job abort.\n\naction (string) -- [REQUIRED]The type of abort action to initiate a job abort.\n\nthresholdPercentage (float) -- [REQUIRED]The threshold as a percentage of the total number of executed things that will initiate a job abort.\nAWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).\n\nminNumberOfExecutedThings (integer) -- [REQUIRED]Minimum number of executed things before evaluating an abort rule.\n\n\n\n\n\n\n

    :type timeoutConfig: dict
    :param timeoutConfig: Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to IN_PROGRESS . If the job execution status is not set to another terminal state before the time expires, it will be automatically set to TIMED_OUT .\n\ninProgressTimeoutInMinutes (integer) --Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can\'t be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal TIMED_OUT status.\n\n\n

    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.ServiceUnavailableException
    
    """
    pass

def update_mitigation_action(actionName=None, roleArn=None, actionParams=None):
    """
    Updates the definition for the specified mitigation action.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_mitigation_action(
        actionName='string',
        roleArn='string',
        actionParams={
            'updateDeviceCertificateParams': {
                'action': 'DEACTIVATE'
            },
            'updateCACertificateParams': {
                'action': 'DEACTIVATE'
            },
            'addThingsToThingGroupParams': {
                'thingGroupNames': [
                    'string',
                ],
                'overrideDynamicGroups': True|False
            },
            'replaceDefaultPolicyVersionParams': {
                'templateName': 'BLANK_POLICY'
            },
            'enableIoTLoggingParams': {
                'roleArnForLogging': 'string',
                'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
            },
            'publishFindingToSnsParams': {
                'topicArn': 'string'
            }
        }
    )
    
    
    :type actionName: string
    :param actionName: [REQUIRED]\nThe friendly name for the mitigation action. You can\'t change the name by using UpdateMitigationAction . Instead, you must delete and re-create the mitigation action with the new name.\n

    :type roleArn: string
    :param roleArn: The ARN of the IAM role that is used to apply the mitigation action.

    :type actionParams: dict
    :param actionParams: Defines the type of action and the parameters for that action.\n\nupdateDeviceCertificateParams (dict) --Parameters to define a mitigation action that changes the state of the device certificate to inactive.\n\naction (string) -- [REQUIRED]The action that you want to apply to the device cerrtificate. The only supported value is DEACTIVATE .\n\n\n\nupdateCACertificateParams (dict) --Parameters to define a mitigation action that changes the state of the CA certificate to inactive.\n\naction (string) -- [REQUIRED]The action that you want to apply to the CA cerrtificate. The only supported value is DEACTIVATE .\n\n\n\naddThingsToThingGroupParams (dict) --Parameters to define a mitigation action that moves devices associated with a certificate to one or more specified thing groups, typically for quarantine.\n\nthingGroupNames (list) -- [REQUIRED]The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to more than one group in the same hierarchy.\n\n(string) --\n\n\noverrideDynamicGroups (boolean) --Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic things groups.\n\n\n\nreplaceDefaultPolicyVersionParams (dict) --Parameters to define a mitigation action that adds a blank policy to restrict permissions.\n\ntemplateName (string) -- [REQUIRED]The name of the template to be applied. The only supported value is BLANK_POLICY .\n\n\n\nenableIoTLoggingParams (dict) --Parameters to define a mitigation action that enables AWS IoT logging at a specified level of detail.\n\nroleArnForLogging (string) -- [REQUIRED]The ARN of the IAM role used for logging.\n\nlogLevel (string) -- [REQUIRED]Specifies the types of information to be logged.\n\n\n\npublishFindingToSnsParams (dict) --Parameters to define a mitigation action that publishes findings to Amazon SNS. You can implement your own custom actions in response to the Amazon SNS messages.\n\ntopicArn (string) -- [REQUIRED]The ARN of the topic to which you want to publish the findings.\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'actionArn': 'string',
    'actionId': 'string'
}


Response Structure

(dict) --

actionArn (string) --
The ARN for the new mitigation action.

actionId (string) --
A unique identifier for the mitigation action.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'actionArn': 'string',
        'actionId': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def update_provisioning_template(templateName=None, description=None, enabled=None, defaultVersionId=None, provisioningRoleArn=None, preProvisioningHook=None, removePreProvisioningHook=None):
    """
    Updates a fleet provisioning template.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_provisioning_template(
        templateName='string',
        description='string',
        enabled=True|False,
        defaultVersionId=123,
        provisioningRoleArn='string',
        preProvisioningHook={
            'payloadVersion': 'string',
            'targetArn': 'string'
        },
        removePreProvisioningHook=True|False
    )
    
    
    :type templateName: string
    :param templateName: [REQUIRED]\nThe name of the fleet provisioning template.\n

    :type description: string
    :param description: The description of the fleet provisioning template.

    :type enabled: boolean
    :param enabled: True to enable the fleet provisioning template, otherwise false.

    :type defaultVersionId: integer
    :param defaultVersionId: The ID of the default provisioning template version.

    :type provisioningRoleArn: string
    :param provisioningRoleArn: The ARN of the role associated with the provisioning template. This IoT role grants permission to provision a device.

    :type preProvisioningHook: dict
    :param preProvisioningHook: Updates the pre-provisioning hook template.\n\npayloadVersion (string) --The payload that was sent to the target function.\n\nNote: Only Lambda functions are currently supported.\n\ntargetArn (string) -- [REQUIRED]The ARN of the target function.\n\nNote: Only Lambda functions are currently supported.\n\n\n

    :type removePreProvisioningHook: boolean
    :param removePreProvisioningHook: Removes pre-provisioning hook template.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ConflictingResourceUpdateException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_role_alias(roleAlias=None, roleArn=None, credentialDurationSeconds=None):
    """
    Updates a role alias.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_role_alias(
        roleAlias='string',
        roleArn='string',
        credentialDurationSeconds=123
    )
    
    
    :type roleAlias: string
    :param roleAlias: [REQUIRED]\nThe role alias to update.\n

    :type roleArn: string
    :param roleArn: The role ARN.

    :type credentialDurationSeconds: integer
    :param credentialDurationSeconds: The number of seconds the credential will be valid.

    :rtype: dict

ReturnsResponse Syntax
{
    'roleAlias': 'string',
    'roleAliasArn': 'string'
}


Response Structure

(dict) --

roleAlias (string) --
The role alias.

roleAliasArn (string) --
The role alias ARN.







Exceptions

IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'roleAlias': 'string',
        'roleAliasArn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def update_scheduled_audit(frequency=None, dayOfMonth=None, dayOfWeek=None, targetCheckNames=None, scheduledAuditName=None):
    """
    Updates a scheduled audit, including which checks are performed and how often the audit takes place.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_scheduled_audit(
        frequency='DAILY'|'WEEKLY'|'BIWEEKLY'|'MONTHLY',
        dayOfMonth='string',
        dayOfWeek='SUN'|'MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT',
        targetCheckNames=[
            'string',
        ],
        scheduledAuditName='string'
    )
    
    
    :type frequency: string
    :param frequency: How often the scheduled audit takes place. Can be one of 'DAILY', 'WEEKLY', 'BIWEEKLY', or 'MONTHLY'. The start time of each audit is determined by the system.

    :type dayOfMonth: string
    :param dayOfMonth: The day of the month on which the scheduled audit takes place. Can be '1' through '31' or 'LAST'. This field is required if the 'frequency' parameter is set to 'MONTHLY'. If days 29-31 are specified, and the month does not have that many days, the audit takes place on the 'LAST' day of the month.

    :type dayOfWeek: string
    :param dayOfWeek: The day of the week on which the scheduled audit takes place. Can be one of 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', or 'SAT'. This field is required if the 'frequency' parameter is set to 'WEEKLY' or 'BIWEEKLY'.

    :type targetCheckNames: list
    :param targetCheckNames: Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)\n\n(string) --An audit check name. Checks must be enabled for your account. (Use DescribeAccountAuditConfiguration to see the list of all checks, including those that are enabled or use UpdateAccountAuditConfiguration to select which checks are enabled.)\n\n\n

    :type scheduledAuditName: string
    :param scheduledAuditName: [REQUIRED]\nThe name of the scheduled audit. (Max. 128 chars)\n

    :rtype: dict

ReturnsResponse Syntax
{
    'scheduledAuditArn': 'string'
}


Response Structure

(dict) --

scheduledAuditArn (string) --
The ARN of the scheduled audit.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'scheduledAuditArn': 'string'
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def update_security_profile(securityProfileName=None, securityProfileDescription=None, behaviors=None, alertTargets=None, additionalMetricsToRetain=None, additionalMetricsToRetainV2=None, deleteBehaviors=None, deleteAlertTargets=None, deleteAdditionalMetricsToRetain=None, expectedVersion=None):
    """
    Updates a Device Defender security profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_security_profile(
        securityProfileName='string',
        securityProfileDescription='string',
        behaviors=[
            {
                'name': 'string',
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                },
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123,
                    'consecutiveDatapointsToAlarm': 123,
                    'consecutiveDatapointsToClear': 123,
                    'statisticalThreshold': {
                        'statistic': 'string'
                    }
                }
            },
        ],
        alertTargets={
            'string': {
                'alertTargetArn': 'string',
                'roleArn': 'string'
            }
        },
        additionalMetricsToRetain=[
            'string',
        ],
        additionalMetricsToRetainV2=[
            {
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                }
            },
        ],
        deleteBehaviors=True|False,
        deleteAlertTargets=True|False,
        deleteAdditionalMetricsToRetain=True|False,
        expectedVersion=123
    )
    
    
    :type securityProfileName: string
    :param securityProfileName: [REQUIRED]\nThe name of the security profile you want to update.\n

    :type securityProfileDescription: string
    :param securityProfileDescription: A description of the security profile.

    :type behaviors: list
    :param behaviors: Specifies the behaviors that, when violated by a device (thing), cause an alert.\n\n(dict) --A Device Defender security profile behavior.\n\nname (string) -- [REQUIRED]The name you have given to the behavior.\n\nmetric (string) --What is measured by the behavior.\n\nmetricDimension (dict) --The dimension for a metric in your behavior. For example, using a TOPIC_FILTER dimension, you can narrow down the scope of the metric only to MQTT topics whose name match the pattern specified in the dimension.\n\ndimensionName (string) -- [REQUIRED]A unique identifier for the dimension.\n\noperator (string) --Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .\n\n\n\ncriteria (dict) --The criteria that determine if a device is behaving normally in regard to the metric .\n\ncomparisonOperator (string) --The operator that relates the thing measured (metric ) to the criteria (containing a value or statisticalThreshold ).\n\nvalue (dict) --The value to be compared with the metric .\n\ncount (integer) --If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .\n\ncidrs (list) --If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .\n\n(string) --\n\n\nports (list) --If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .\n\n(integer) --\n\n\n\n\ndurationSeconds (integer) --Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ). For a statisticalThreshhold metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.\n\nconsecutiveDatapointsToAlarm (integer) --If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.\n\nconsecutiveDatapointsToClear (integer) --If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.\n\nstatisticalThreshold (dict) --A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.\n\nstatistic (string) --The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (durationSeconds ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (comparisonOperator ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.\n\n\n\n\n\n\n\n\n

    :type alertTargets: dict
    :param alertTargets: Where the alerts are sent. (Alerts are always sent to the console.)\n\n(string) --The type of alert target: one of 'SNS'.\n\n(dict) --A structure containing the alert target ARN and the role ARN.\n\nalertTargetArn (string) -- [REQUIRED]The ARN of the notification target to which alerts are sent.\n\nroleArn (string) -- [REQUIRED]The ARN of the role that grants permission to send alerts to the notification target.\n\n\n\n\n\n\n

    :type additionalMetricsToRetain: list
    :param additionalMetricsToRetain: A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile\'s behaviors , but it is also retained for any metric specified here.\n\nNote: This API field is deprecated. Please use UpdateSecurityProfileRequest$additionalMetricsToRetainV2 instead.\n\n(string) --\n\n

    :type additionalMetricsToRetainV2: list
    :param additionalMetricsToRetainV2: A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile\'s behaviors, but it is also retained for any metric specified here.\n\n(dict) --The metric you want to retain. Dimensions are optional.\n\nmetric (string) -- [REQUIRED]What is measured by the behavior.\n\nmetricDimension (dict) --The dimension of a metric.\n\ndimensionName (string) -- [REQUIRED]A unique identifier for the dimension.\n\noperator (string) --Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .\n\n\n\n\n\n\n

    :type deleteBehaviors: boolean
    :param deleteBehaviors: If true, delete all behaviors defined for this security profile. If any behaviors are defined in the current invocation, an exception occurs.

    :type deleteAlertTargets: boolean
    :param deleteAlertTargets: If true, delete all alertTargets defined for this security profile. If any alertTargets are defined in the current invocation, an exception occurs.

    :type deleteAdditionalMetricsToRetain: boolean
    :param deleteAdditionalMetricsToRetain: If true, delete all additionalMetricsToRetain defined for this security profile. If any additionalMetricsToRetain are defined in the current invocation, an exception occurs.

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the security profile. A new version is generated whenever the security profile is updated. If you specify a value that is different from the actual version, a VersionConflictException is thrown.

    :rtype: dict

ReturnsResponse Syntax
{
    'securityProfileName': 'string',
    'securityProfileArn': 'string',
    'securityProfileDescription': 'string',
    'behaviors': [
        {
            'name': 'string',
            'metric': 'string',
            'metricDimension': {
                'dimensionName': 'string',
                'operator': 'IN'|'NOT_IN'
            },
            'criteria': {
                'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                'value': {
                    'count': 123,
                    'cidrs': [
                        'string',
                    ],
                    'ports': [
                        123,
                    ]
                },
                'durationSeconds': 123,
                'consecutiveDatapointsToAlarm': 123,
                'consecutiveDatapointsToClear': 123,
                'statisticalThreshold': {
                    'statistic': 'string'
                }
            }
        },
    ],
    'alertTargets': {
        'string': {
            'alertTargetArn': 'string',
            'roleArn': 'string'
        }
    },
    'additionalMetricsToRetain': [
        'string',
    ],
    'additionalMetricsToRetainV2': [
        {
            'metric': 'string',
            'metricDimension': {
                'dimensionName': 'string',
                'operator': 'IN'|'NOT_IN'
            }
        },
    ],
    'version': 123,
    'creationDate': datetime(2015, 1, 1),
    'lastModifiedDate': datetime(2015, 1, 1)
}


Response Structure

(dict) --

securityProfileName (string) --
The name of the security profile that was updated.

securityProfileArn (string) --
The ARN of the security profile that was updated.

securityProfileDescription (string) --
The description of the security profile.

behaviors (list) --
Specifies the behaviors that, when violated by a device (thing), cause an alert.

(dict) --
A Device Defender security profile behavior.

name (string) --
The name you have given to the behavior.

metric (string) --
What is measured by the behavior.

metricDimension (dict) --
The dimension for a metric in your behavior. For example, using a TOPIC_FILTER dimension, you can narrow down the scope of the metric only to MQTT topics whose name match the pattern specified in the dimension.

dimensionName (string) --
A unique identifier for the dimension.

operator (string) --
Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .



criteria (dict) --
The criteria that determine if a device is behaving normally in regard to the metric .

comparisonOperator (string) --
The operator that relates the thing measured (metric ) to the criteria (containing a value or statisticalThreshold ).

value (dict) --
The value to be compared with the metric .

count (integer) --
If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .

cidrs (list) --
If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .

(string) --


ports (list) --
If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .

(integer) --




durationSeconds (integer) --
Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ). For a statisticalThreshhold metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.

consecutiveDatapointsToAlarm (integer) --
If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.

consecutiveDatapointsToClear (integer) --
If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.

statisticalThreshold (dict) --
A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

statistic (string) --
The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (durationSeconds ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (comparisonOperator ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.









alertTargets (dict) --
Where the alerts are sent. (Alerts are always sent to the console.)

(string) --
The type of alert target: one of "SNS".

(dict) --
A structure containing the alert target ARN and the role ARN.

alertTargetArn (string) --
The ARN of the notification target to which alerts are sent.

roleArn (string) --
The ARN of the role that grants permission to send alerts to the notification target.







additionalMetricsToRetain (list) --
A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the security profile\'s behaviors , but it is also retained for any metric specified here.

Note: This API field is deprecated. Please use  UpdateSecurityProfileResponse$additionalMetricsToRetainV2 instead.


(string) --


additionalMetricsToRetainV2 (list) --
A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile\'s behaviors, but it is also retained for any metric specified here.

(dict) --
The metric you want to retain. Dimensions are optional.

metric (string) --
What is measured by the behavior.

metricDimension (dict) --
The dimension of a metric.

dimensionName (string) --
A unique identifier for the dimension.

operator (string) --
Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .







version (integer) --
The updated version of the security profile.

creationDate (datetime) --
The time the security profile was created.

lastModifiedDate (datetime) --
The time the security profile was last modified.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.VersionConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'securityProfileName': 'string',
        'securityProfileArn': 'string',
        'securityProfileDescription': 'string',
        'behaviors': [
            {
                'name': 'string',
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                },
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123,
                    'consecutiveDatapointsToAlarm': 123,
                    'consecutiveDatapointsToClear': 123,
                    'statisticalThreshold': {
                        'statistic': 'string'
                    }
                }
            },
        ],
        'alertTargets': {
            'string': {
                'alertTargetArn': 'string',
                'roleArn': 'string'
            }
        },
        'additionalMetricsToRetain': [
            'string',
        ],
        'additionalMetricsToRetainV2': [
            {
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                }
            },
        ],
        'version': 123,
        'creationDate': datetime(2015, 1, 1),
        'lastModifiedDate': datetime(2015, 1, 1)
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def update_stream(streamId=None, description=None, files=None, roleArn=None):
    """
    Updates an existing stream. The stream version will be incremented by one.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_stream(
        streamId='string',
        description='string',
        files=[
            {
                'fileId': 123,
                's3Location': {
                    'bucket': 'string',
                    'key': 'string',
                    'version': 'string'
                }
            },
        ],
        roleArn='string'
    )
    
    
    :type streamId: string
    :param streamId: [REQUIRED]\nThe stream ID.\n

    :type description: string
    :param description: The description of the stream.

    :type files: list
    :param files: The files associated with the stream.\n\n(dict) --Represents a file to stream.\n\nfileId (integer) --The file ID.\n\ns3Location (dict) --The location of the file in S3.\n\nbucket (string) --The S3 bucket.\n\nkey (string) --The S3 key.\n\nversion (string) --The S3 bucket version.\n\n\n\n\n\n\n

    :type roleArn: string
    :param roleArn: An IAM role that allows the IoT service principal assumes to access your S3 files.

    :rtype: dict

ReturnsResponse Syntax
{
    'streamId': 'string',
    'streamArn': 'string',
    'description': 'string',
    'streamVersion': 123
}


Response Structure

(dict) --

streamId (string) --
The stream ID.

streamArn (string) --
The stream ARN.

description (string) --
A description of the stream.

streamVersion (integer) --
The stream version.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ResourceNotFoundException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'streamId': 'string',
        'streamArn': 'string',
        'description': 'string',
        'streamVersion': 123
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.ResourceNotFoundException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    
    """
    pass

def update_thing(thingName=None, thingTypeName=None, attributePayload=None, expectedVersion=None, removeThingType=None):
    """
    Updates the data for a thing.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_thing(
        thingName='string',
        thingTypeName='string',
        attributePayload={
            'attributes': {
                'string': 'string'
            },
            'merge': True|False
        },
        expectedVersion=123,
        removeThingType=True|False
    )
    
    
    :type thingName: string
    :param thingName: [REQUIRED]\nThe name of the thing to update.\nYou can\'t change a thing\'s name. To change a thing\'s name, you must create a new thing, give it the new name, and then delete the old thing.\n

    :type thingTypeName: string
    :param thingTypeName: The name of the thing type.

    :type attributePayload: dict
    :param attributePayload: A list of thing attributes, a JSON string containing name-value pairs. For example:\n\n{\\'attributes\\':{\\'name1\\':\\'value2\\'}}\nThis data is used to add new attributes or update existing attributes.\n\nattributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:\n\n{\\'attributes\\':{\\'string1\\':\\'string2\\'}}\n\n(string) --\n(string) --\n\n\n\n\nmerge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.\nTo remove an attribute, call UpdateThing with an empty attribute value.\n\nNote\nThe merge attribute is only valid when calling UpdateThing or UpdateThingGroup .\n\n\n\n

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the UpdateThing request is rejected with a VersionConflictException .

    :type removeThingType: boolean
    :param removeThingType: Remove a thing type association. If true , the association is removed.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --
The output from the UpdateThing operation.





Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.VersionConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.VersionConflictException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.UnauthorizedException
    IoT.Client.exceptions.ServiceUnavailableException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_thing_group(thingGroupName=None, thingGroupProperties=None, expectedVersion=None):
    """
    Update a thing group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_thing_group(
        thingGroupName='string',
        thingGroupProperties={
            'thingGroupDescription': 'string',
            'attributePayload': {
                'attributes': {
                    'string': 'string'
                },
                'merge': True|False
            }
        },
        expectedVersion=123
    )
    
    
    :type thingGroupName: string
    :param thingGroupName: [REQUIRED]\nThe thing group to update.\n

    :type thingGroupProperties: dict
    :param thingGroupProperties: [REQUIRED]\nThe thing group properties.\n\nthingGroupDescription (string) --The thing group description.\n\nattributePayload (dict) --The thing group attributes in JSON format.\n\nattributes (dict) --A JSON string containing up to three key-value pair in JSON format. For example:\n\n{\\'attributes\\':{\\'string1\\':\\'string2\\'}}\n\n(string) --\n(string) --\n\n\n\n\nmerge (boolean) --Specifies whether the list of attributes provided in the AttributePayload is merged with the attributes stored in the registry, instead of overwriting them.\nTo remove an attribute, call UpdateThing with an empty attribute value.\n\nNote\nThe merge attribute is only valid when calling UpdateThing or UpdateThingGroup .\n\n\n\n\n\n

    :type expectedVersion: integer
    :param expectedVersion: The expected version of the thing group. If this does not match the version of the thing group being updated, the update will fail.

    :rtype: dict

ReturnsResponse Syntax
{
    'version': 123
}


Response Structure

(dict) --

version (integer) --
The version of the updated thing group.







Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.VersionConflictException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {
        'version': 123
    }
    
    
    :returns: 
    IoT.Client.exceptions.InvalidRequestException
    IoT.Client.exceptions.VersionConflictException
    IoT.Client.exceptions.ThrottlingException
    IoT.Client.exceptions.InternalFailureException
    IoT.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_thing_groups_for_thing(thingName=None, thingGroupsToAdd=None, thingGroupsToRemove=None, overrideDynamicGroups=None):
    """
    Updates the groups to which the thing belongs.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_thing_groups_for_thing(
        thingName='string',
        thingGroupsToAdd=[
            'string',
        ],
        thingGroupsToRemove=[
            'string',
        ],
        overrideDynamicGroups=True|False
    )
    
    
    :type thingName: string
    :param thingName: The thing whose group memberships will be updated.

    :type thingGroupsToAdd: list
    :param thingGroupsToAdd: The groups to which the thing will be added.\n\n(string) --\n\n

    :type thingGroupsToRemove: list
    :param thingGroupsToRemove: The groups from which the thing will be removed.\n\n(string) --\n\n

    :type overrideDynamicGroups: boolean
    :param overrideDynamicGroups: Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException
IoT.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_topic_rule_destination(arn=None, status=None):
    """
    Updates a topic rule destination. You use this to change the status, endpoint URL, or confirmation URL of the destination.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_topic_rule_destination(
        arn='string',
        status='ENABLED'|'IN_PROGRESS'|'DISABLED'|'ERROR'
    )
    
    
    :type arn: string
    :param arn: [REQUIRED]\nThe ARN of the topic rule destination.\n

    :type status: string
    :param status: [REQUIRED]\nThe status of the topic rule destination. Valid values are:\n\nIN_PROGRESS\nA topic rule destination was created but has not been confirmed. You can set status to IN_PROGRESS by calling UpdateTopicRuleDestination . Calling UpdateTopicRuleDestination causes a new confirmation challenge to be sent to your confirmation endpoint.\n\nENABLED\nConfirmation was completed, and traffic to this destination is allowed. You can set status to DISABLED by calling UpdateTopicRuleDestination .\n\nDISABLED\nConfirmation was completed, and traffic to this destination is not allowed. You can set status to ENABLED by calling UpdateTopicRuleDestination .\n\nERROR\nConfirmation could not be completed, for example if the confirmation timed out. You can call GetTopicRuleDestination for details about the error. You can set status to IN_PROGRESS by calling UpdateTopicRuleDestination . Calling UpdateTopicRuleDestination causes a new confirmation challenge to be sent to your confirmation endpoint.\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

IoT.Client.exceptions.InternalException
IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ServiceUnavailableException
IoT.Client.exceptions.UnauthorizedException
IoT.Client.exceptions.ConflictingResourceUpdateException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def validate_security_profile_behaviors(behaviors=None):
    """
    Validates a Device Defender security profile behaviors specification.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.validate_security_profile_behaviors(
        behaviors=[
            {
                'name': 'string',
                'metric': 'string',
                'metricDimension': {
                    'dimensionName': 'string',
                    'operator': 'IN'|'NOT_IN'
                },
                'criteria': {
                    'comparisonOperator': 'less-than'|'less-than-equals'|'greater-than'|'greater-than-equals'|'in-cidr-set'|'not-in-cidr-set'|'in-port-set'|'not-in-port-set',
                    'value': {
                        'count': 123,
                        'cidrs': [
                            'string',
                        ],
                        'ports': [
                            123,
                        ]
                    },
                    'durationSeconds': 123,
                    'consecutiveDatapointsToAlarm': 123,
                    'consecutiveDatapointsToClear': 123,
                    'statisticalThreshold': {
                        'statistic': 'string'
                    }
                }
            },
        ]
    )
    
    
    :type behaviors: list
    :param behaviors: [REQUIRED]\nSpecifies the behaviors that, when violated by a device (thing), cause an alert.\n\n(dict) --A Device Defender security profile behavior.\n\nname (string) -- [REQUIRED]The name you have given to the behavior.\n\nmetric (string) --What is measured by the behavior.\n\nmetricDimension (dict) --The dimension for a metric in your behavior. For example, using a TOPIC_FILTER dimension, you can narrow down the scope of the metric only to MQTT topics whose name match the pattern specified in the dimension.\n\ndimensionName (string) -- [REQUIRED]A unique identifier for the dimension.\n\noperator (string) --Defines how the dimensionValues of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the IN operator, a message will be counted only if its topic matches one of the topic filters. With NOT_IN operator, a message will be counted only if it doesn\'t match any of the topic filters. The operator is optional: if it\'s not provided (is null ), it will be interpreted as IN .\n\n\n\ncriteria (dict) --The criteria that determine if a device is behaving normally in regard to the metric .\n\ncomparisonOperator (string) --The operator that relates the thing measured (metric ) to the criteria (containing a value or statisticalThreshold ).\n\nvalue (dict) --The value to be compared with the metric .\n\ncount (integer) --If the comparisonOperator calls for a numeric value, use this to specify that numeric value to be compared with the metric .\n\ncidrs (list) --If the comparisonOperator calls for a set of CIDRs, use this to specify that set to be compared with the metric .\n\n(string) --\n\n\nports (list) --If the comparisonOperator calls for a set of ports, use this to specify that set to be compared with the metric .\n\n(integer) --\n\n\n\n\ndurationSeconds (integer) --Use this to specify the time duration over which the behavior is evaluated, for those criteria which have a time dimension (for example, NUM_MESSAGES_SENT ). For a statisticalThreshhold metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank.\n\nconsecutiveDatapointsToAlarm (integer) --If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.\n\nconsecutiveDatapointsToClear (integer) --If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.\n\nstatisticalThreshold (dict) --A statistical ranking (percentile) which indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.\n\nstatistic (string) --The percentile which resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (durationSeconds ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (comparisonOperator ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.\n\n\n\n\n\n\n\n\n

    :rtype: dict
ReturnsResponse Syntax{
    'valid': True|False,
    'validationErrors': [
        {
            'errorMessage': 'string'
        },
    ]
}


Response Structure

(dict) --
valid (boolean) --True if the behaviors were valid.

validationErrors (list) --The list of any errors found in the behaviors.

(dict) --Information about an error found in a behavior specification.

errorMessage (string) --The description of an error found in the behaviors.










Exceptions

IoT.Client.exceptions.InvalidRequestException
IoT.Client.exceptions.ThrottlingException
IoT.Client.exceptions.InternalFailureException


    :return: {
        'valid': True|False,
        'validationErrors': [
            {
                'errorMessage': 'string'
            },
        ]
    }
    
    
    :returns: 
    (integer) --
    
    """
    pass

