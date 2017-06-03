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

def assume_role(RoleArn=None, RoleSessionName=None, Policy=None, DurationSeconds=None, ExternalId=None, SerialNumber=None, TokenCode=None):
    """
    Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) that you can use to access AWS resources that you might not normally have access to. Typically, you use AssumeRole for cross-account access or federation. For a comparison of AssumeRole with the other APIs that produce temporary credentials, see Requesting Temporary Security Credentials and Comparing the AWS STS APIs in the IAM User Guide .
    For cross-account access, imagine that you own multiple accounts and need to access resources in each account. You could create long-term credentials in each account to access those resources. However, managing all those credentials and remembering which one can access which account can be time consuming. Instead, you can create one set of long-term credentials in one account and then use temporary security credentials to access all the other accounts by assuming roles in those accounts. For more information about roles, see IAM Roles (Delegation and Federation) in the IAM User Guide .
    For federation, you can, for example, grant single sign-on access to the AWS Management Console. If you already have an identity and authentication system in your corporate network, you don't have to recreate user identities in AWS in order to grant those user identities access to AWS. Instead, after a user has been authenticated, you call AssumeRole (and specify the role with the appropriate permissions) to get temporary security credentials for that user. With those temporary security credentials, you construct a sign-in URL that users can use to access the console. For more information, see Common Scenarios for Temporary Credentials in the IAM User Guide .
    The temporary security credentials are valid for the duration that you specified when calling AssumeRole , which can be from 900 seconds (15 minutes) to a maximum of 3600 seconds (1 hour). The default is 1 hour.
    The temporary security credentials created by AssumeRole can be used to make API calls to any AWS service with the following exception: you cannot call the STS service's GetFederationToken or GetSessionToken APIs.
    Optionally, you can pass an IAM access policy to this operation. If you choose not to pass a policy, the temporary security credentials that are returned by the operation have the permissions that are defined in the access policy of the role that is being assumed. If you pass a policy to this operation, the temporary security credentials that are returned by the operation have the permissions that are allowed by both the access policy of the role that is being assumed, * and * the policy that you pass. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, see Permissions for AssumeRole, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity in the IAM User Guide .
    To assume a role, your AWS account must be trusted by the role. The trust relationship is defined in the role's trust policy when the role is created. That trust policy states which accounts are allowed to delegate access to this account's role.
    The user who wants to access the role must also have permissions delegated from the role's administrator. If the user is in a different account than the role, then the user's administrator must attach a policy that allows the user to call AssumeRole on the ARN of the role in the other account. If the user is in the same account as the role, then you can either attach a policy to the user (identical to the previous different account user), or you can add the user as a principal directly in the role's trust policy
    You can optionally include multi-factor authentication (MFA) information when you call AssumeRole . This is useful for cross-account scenarios in which you want to make sure that the user who is assuming the role has been authenticated using an AWS MFA device. In that scenario, the trust policy of the role being assumed includes a condition that tests for MFA authentication; if the caller does not include valid MFA information, the request to assume the role is denied. The condition in a trust policy that tests for MFA authentication might look like the following example.
    For more information, see Configuring MFA-Protected API Access in the IAM User Guide guide.
    To use MFA with AssumeRole , you pass values for the SerialNumber and TokenCode parameters. The SerialNumber value identifies the user's hardware or virtual MFA device. The TokenCode is the time-based one-time password (TOTP) that the MFA devices produces.
    See also: AWS API Documentation
    
    Examples
    Expected Output:
    
    :example: response = client.assume_role(
        RoleArn='string',
        RoleSessionName='string',
        Policy='string',
        DurationSeconds=123,
        ExternalId='string',
        SerialNumber='string',
        TokenCode='string'
    )
    
    
    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the role to assume.
            

    :type RoleSessionName: string
    :param RoleSessionName: [REQUIRED]
            An identifier for the assumed role session.
            Use the role session name to uniquely identify a session when the same role is assumed by different principals or for different reasons. In cross-account scenarios, the role session name is visible to, and can be logged by the account that owns the role. The role session name is also used in the ARN of the assumed role principal. This means that subsequent cross-account API requests using the temporary security credentials will expose the role session name to the external account in their CloudTrail logs.
            The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
            

    :type Policy: string
    :param Policy: An IAM policy in JSON format.
            This parameter is optional. If you pass a policy, the temporary security credentials that are returned by the operation have the permissions that are allowed by both (the intersection of) the access policy of the role that is being assumed, and the policy that you pass. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, see Permissions for AssumeRole, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity in the IAM User Guide .
            The format for this parameter, as described by its regex pattern, is a string of characters up to 2048 characters in length. The characters can be any ASCII character from the space character to the end of the valid character list (u0020-u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
            Note
            The policy plain text must be 2048 bytes or shorter. However, an internal conversion compresses it into a packed binary format with a separate limit. The PackedPolicySize response element indicates by percentage how close to the upper size limit the policy is, with 100% equaling the maximum allowed size.
            

    :type DurationSeconds: integer
    :param DurationSeconds: The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 3600 seconds (1 hour). By default, the value is set to 3600 seconds.
            Note
            This is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session, separately from the DurationSeconds parameter on this API. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .
            

    :type ExternalId: string
    :param ExternalId: A unique identifier that is used by third parties when assuming roles in their customers' accounts. For each role that the third party can assume, they should instruct their customers to ensure the role's trust policy checks for the external ID that the third party generated. Each time the third party assumes the role, they should pass the customer's external ID. The external ID is useful in order to help third parties bind a role to the customer who created it. For more information about the external ID, see How to Use an External ID When Granting Access to Your AWS Resources to a Third Party in the IAM User Guide .
            The regex used to validated this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-
            

    :type SerialNumber: string
    :param SerialNumber: The identification number of the MFA device that is associated with the user who is making the AssumeRole call. Specify this value if the trust policy of the role being assumed includes a condition that requires MFA authentication. The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user ).
            The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
            

    :type TokenCode: string
    :param TokenCode: The value provided by the MFA device, if the trust policy of the role being assumed requires MFA (that is, if the policy includes a condition that tests for MFA). If the role being assumed requires MFA and if the TokenCode value is missing or expired, the AssumeRole call returns an 'access denied' error.
            The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.
            

    :rtype: dict
    :return: {
        'Credentials': {
            'AccessKeyId': 'string',
            'SecretAccessKey': 'string',
            'SessionToken': 'string',
            'Expiration': datetime(2015, 1, 1)
        },
        'AssumedRoleUser': {
            'AssumedRoleId': 'string',
            'Arn': 'string'
        },
        'PackedPolicySize': 123
    }
    
    
    """
    pass

def assume_role_with_saml(RoleArn=None, PrincipalArn=None, SAMLAssertion=None, Policy=None, DurationSeconds=None):
    """
    Returns a set of temporary security credentials for users who have been authenticated via a SAML authentication response. This operation provides a mechanism for tying an enterprise identity store or directory to role-based AWS access without user-specific credentials or configuration. For a comparison of AssumeRoleWithSAML with the other APIs that produce temporary credentials, see Requesting Temporary Security Credentials and Comparing the AWS STS APIs in the IAM User Guide .
    The temporary security credentials returned by this operation consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to AWS services.
    The temporary security credentials are valid for the duration that you specified when calling AssumeRole , or until the time specified in the SAML authentication response's SessionNotOnOrAfter value, whichever is shorter. The duration can be from 900 seconds (15 minutes) to a maximum of 3600 seconds (1 hour). The default is 1 hour.
    The temporary security credentials created by AssumeRoleWithSAML can be used to make API calls to any AWS service with the following exception: you cannot call the STS service's GetFederationToken or GetSessionToken APIs.
    Optionally, you can pass an IAM access policy to this operation. If you choose not to pass a policy, the temporary security credentials that are returned by the operation have the permissions that are defined in the access policy of the role that is being assumed. If you pass a policy to this operation, the temporary security credentials that are returned by the operation have the permissions that are allowed by the intersection of both the access policy of the role that is being assumed, * and * the policy that you pass. This means that both policies must grant the permission for the action to be allowed. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, see Permissions for AssumeRole, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity in the IAM User Guide .
    Before your application can call AssumeRoleWithSAML , you must configure your SAML identity provider (IdP) to issue the claims required by AWS. Additionally, you must use AWS Identity and Access Management (IAM) to create a SAML provider entity in your AWS account that represents your identity provider, and create an IAM role that specifies this SAML provider in its trust policy.
    Calling AssumeRoleWithSAML does not require the use of AWS security credentials. The identity of the caller is validated by using keys in the metadata document that is uploaded for the SAML provider entity for your identity provider.
    For more information, see the following resources:
    See also: AWS API Documentation
    
    
    :example: response = client.assume_role_with_saml(
        RoleArn='string',
        PrincipalArn='string',
        SAMLAssertion='string',
        Policy='string',
        DurationSeconds=123
    )
    
    
    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the role that the caller is assuming.
            

    :type PrincipalArn: string
    :param PrincipalArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.
            

    :type SAMLAssertion: string
    :param SAMLAssertion: [REQUIRED]
            The base-64 encoded SAML authentication response provided by the IdP.
            For more information, see Configuring a Relying Party and Adding Claims in the Using IAM guide.
            

    :type Policy: string
    :param Policy: An IAM policy in JSON format.
            The policy parameter is optional. If you pass a policy, the temporary security credentials that are returned by the operation have the permissions that are allowed by both the access policy of the role that is being assumed, * and * the policy that you pass. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, Permissions for AssumeRole, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity in the IAM User Guide .
            The format for this parameter, as described by its regex pattern, is a string of characters up to 2048 characters in length. The characters can be any ASCII character from the space character to the end of the valid character list (u0020-u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
            Note
            The policy plain text must be 2048 bytes or shorter. However, an internal conversion compresses it into a packed binary format with a separate limit. The PackedPolicySize response element indicates by percentage how close to the upper size limit the policy is, with 100% equaling the maximum allowed size.
            

    :type DurationSeconds: integer
    :param DurationSeconds: The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 3600 seconds (1 hour). By default, the value is set to 3600 seconds. An expiration can also be specified in the SAML authentication response's SessionNotOnOrAfter value. The actual expiration time is whichever value is shorter.
            Note
            This is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session, separately from the DurationSeconds parameter on this API. For more information, see Enabling SAML 2.0 Federated Users to Access the AWS Management Console in the IAM User Guide .
            

    :rtype: dict
    :return: {
        'Credentials': {
            'AccessKeyId': 'string',
            'SecretAccessKey': 'string',
            'SessionToken': 'string',
            'Expiration': datetime(2015, 1, 1)
        },
        'AssumedRoleUser': {
            'AssumedRoleId': 'string',
            'Arn': 'string'
        },
        'PackedPolicySize': 123,
        'Subject': 'string',
        'SubjectType': 'string',
        'Issuer': 'string',
        'Audience': 'string',
        'NameQualifier': 'string'
    }
    
    
    :returns: 
    RoleArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the role that the caller is assuming.
    
    PrincipalArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.
    
    SAMLAssertion (string) -- [REQUIRED]
    The base-64 encoded SAML authentication response provided by the IdP.
    For more information, see Configuring a Relying Party and Adding Claims in the Using IAM guide.
    
    Policy (string) -- An IAM policy in JSON format.
    The policy parameter is optional. If you pass a policy, the temporary security credentials that are returned by the operation have the permissions that are allowed by both the access policy of the role that is being assumed, * and * the policy that you pass. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, Permissions for AssumeRole, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity in the IAM User Guide .
    The format for this parameter, as described by its regex pattern, is a string of characters up to 2048 characters in length. The characters can be any ASCII character from the space character to the end of the valid character list (u0020-u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
    
    Note
    The policy plain text must be 2048 bytes or shorter. However, an internal conversion compresses it into a packed binary format with a separate limit. The PackedPolicySize response element indicates by percentage how close to the upper size limit the policy is, with 100% equaling the maximum allowed size.
    
    
    DurationSeconds (integer) -- The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 3600 seconds (1 hour). By default, the value is set to 3600 seconds. An expiration can also be specified in the SAML authentication response's SessionNotOnOrAfter value. The actual expiration time is whichever value is shorter.
    
    Note
    This is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session, separately from the DurationSeconds parameter on this API. For more information, see Enabling SAML 2.0 Federated Users to Access the AWS Management Console in the IAM User Guide .
    
    
    
    """
    pass

def assume_role_with_web_identity(RoleArn=None, RoleSessionName=None, WebIdentityToken=None, ProviderId=None, Policy=None, DurationSeconds=None):
    """
    Returns a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider, such as Amazon Cognito, Login with Amazon, Facebook, Google, or any OpenID Connect-compatible identity provider.
    Calling AssumeRoleWithWebIdentity does not require the use of AWS security credentials. Therefore, you can distribute an application (for example, on mobile devices) that requests temporary security credentials without including long-term AWS credentials in the application, and without deploying server-based proxy services that use long-term AWS credentials. Instead, the identity of the caller is validated by using a token from the web identity provider. For a comparison of AssumeRoleWithWebIdentity with the other APIs that produce temporary credentials, see Requesting Temporary Security Credentials and Comparing the AWS STS APIs in the IAM User Guide .
    The temporary security credentials returned by this API consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to AWS service APIs.
    The credentials are valid for the duration that you specified when calling AssumeRoleWithWebIdentity , which can be from 900 seconds (15 minutes) to a maximum of 3600 seconds (1 hour). The default is 1 hour.
    The temporary security credentials created by AssumeRoleWithWebIdentity can be used to make API calls to any AWS service with the following exception: you cannot call the STS service's GetFederationToken or GetSessionToken APIs.
    Optionally, you can pass an IAM access policy to this operation. If you choose not to pass a policy, the temporary security credentials that are returned by the operation have the permissions that are defined in the access policy of the role that is being assumed. If you pass a policy to this operation, the temporary security credentials that are returned by the operation have the permissions that are allowed by both the access policy of the role that is being assumed, * and * the policy that you pass. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, see Permissions for AssumeRole, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity in the IAM User Guide .
    Before your application can call AssumeRoleWithWebIdentity , you must have an identity token from a supported identity provider and create a role that the application can assume. The role that your application assumes must trust the identity provider that is associated with the identity token. In other words, the identity provider must be specified in the role's trust policy.
    For more information about how to use web identity federation and the AssumeRoleWithWebIdentity API, see the following resources:
    See also: AWS API Documentation
    
    Examples
    Expected Output:
    
    :example: response = client.assume_role_with_web_identity(
        RoleArn='string',
        RoleSessionName='string',
        WebIdentityToken='string',
        ProviderId='string',
        Policy='string',
        DurationSeconds=123
    )
    
    
    :type RoleArn: string
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the role that the caller is assuming.
            

    :type RoleSessionName: string
    :param RoleSessionName: [REQUIRED]
            An identifier for the assumed role session. Typically, you pass the name or identifier that is associated with the user who is using your application. That way, the temporary security credentials that your application will use are associated with that user. This session name is included as part of the ARN and assumed role ID in the AssumedRoleUser response element.
            The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
            

    :type WebIdentityToken: string
    :param WebIdentityToken: [REQUIRED]
            The OAuth 2.0 access token or OpenID Connect ID token that is provided by the identity provider. Your application must get this token by authenticating the user who is using your application with a web identity provider before the application makes an AssumeRoleWithWebIdentity call.
            

    :type ProviderId: string
    :param ProviderId: The fully qualified host component of the domain name of the identity provider.
            Specify this value only for OAuth 2.0 access tokens. Currently www.amazon.com and graph.facebook.com are the only supported identity providers for OAuth 2.0 access tokens. Do not include URL schemes and port numbers.
            Do not specify this value for OpenID Connect ID tokens.
            

    :type Policy: string
    :param Policy: An IAM policy in JSON format.
            The policy parameter is optional. If you pass a policy, the temporary security credentials that are returned by the operation have the permissions that are allowed by both the access policy of the role that is being assumed, * and * the policy that you pass. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, see Permissions for AssumeRoleWithWebIdentity in the IAM User Guide .
            The format for this parameter, as described by its regex pattern, is a string of characters up to 2048 characters in length. The characters can be any ASCII character from the space character to the end of the valid character list (u0020-u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
            Note
            The policy plain text must be 2048 bytes or shorter. However, an internal conversion compresses it into a packed binary format with a separate limit. The PackedPolicySize response element indicates by percentage how close to the upper size limit the policy is, with 100% equaling the maximum allowed size.
            

    :type DurationSeconds: integer
    :param DurationSeconds: The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 3600 seconds (1 hour). By default, the value is set to 3600 seconds.
            Note
            This is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session, separately from the DurationSeconds parameter on this API. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .
            

    :rtype: dict
    :return: {
        'Credentials': {
            'AccessKeyId': 'string',
            'SecretAccessKey': 'string',
            'SessionToken': 'string',
            'Expiration': datetime(2015, 1, 1)
        },
        'SubjectFromWebIdentityToken': 'string',
        'AssumedRoleUser': {
            'AssumedRoleId': 'string',
            'Arn': 'string'
        },
        'PackedPolicySize': 123,
        'Provider': 'string',
        'Audience': 'string'
    }
    
    
    :returns: 
    RoleArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the role that the caller is assuming.
    
    RoleSessionName (string) -- [REQUIRED]
    An identifier for the assumed role session. Typically, you pass the name or identifier that is associated with the user who is using your application. That way, the temporary security credentials that your application will use are associated with that user. This session name is included as part of the ARN and assumed role ID in the AssumedRoleUser response element.
    The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
    
    WebIdentityToken (string) -- [REQUIRED]
    The OAuth 2.0 access token or OpenID Connect ID token that is provided by the identity provider. Your application must get this token by authenticating the user who is using your application with a web identity provider before the application makes an AssumeRoleWithWebIdentity call.
    
    ProviderId (string) -- The fully qualified host component of the domain name of the identity provider.
    Specify this value only for OAuth 2.0 access tokens. Currently www.amazon.com and graph.facebook.com are the only supported identity providers for OAuth 2.0 access tokens. Do not include URL schemes and port numbers.
    Do not specify this value for OpenID Connect ID tokens.
    
    Policy (string) -- An IAM policy in JSON format.
    The policy parameter is optional. If you pass a policy, the temporary security credentials that are returned by the operation have the permissions that are allowed by both the access policy of the role that is being assumed, * and * the policy that you pass. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, see Permissions for AssumeRoleWithWebIdentity in the IAM User Guide .
    The format for this parameter, as described by its regex pattern, is a string of characters up to 2048 characters in length. The characters can be any ASCII character from the space character to the end of the valid character list (u0020-u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
    
    Note
    The policy plain text must be 2048 bytes or shorter. However, an internal conversion compresses it into a packed binary format with a separate limit. The PackedPolicySize response element indicates by percentage how close to the upper size limit the policy is, with 100% equaling the maximum allowed size.
    
    
    DurationSeconds (integer) -- The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 3600 seconds (1 hour). By default, the value is set to 3600 seconds.
    
    Note
    This is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session, separately from the DurationSeconds parameter on this API. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .
    
    
    
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

def decode_authorization_message(EncodedMessage=None):
    """
    Decodes additional information about the authorization status of a request from an encoded message returned in response to an AWS request.
    For example, if a user is not authorized to perform an action that he or she has requested, the request returns a Client.UnauthorizedOperation response (an HTTP 403 response). Some AWS actions additionally return an encoded message that can provide details about this authorization failure.
    The message is encoded because the details of the authorization status can constitute privileged information that the user who requested the action should not see. To decode an authorization status message, a user must be granted permissions via an IAM policy to request the DecodeAuthorizationMessage (sts:DecodeAuthorizationMessage ) action.
    The decoded message includes the following type of information:
    See also: AWS API Documentation
    
    Examples
    Expected Output:
    
    :example: response = client.decode_authorization_message(
        EncodedMessage='string'
    )
    
    
    :type EncodedMessage: string
    :param EncodedMessage: [REQUIRED]
            The encoded message that was returned with the response.
            

    :rtype: dict
    :return: {
        'DecodedMessage': 'string'
    }
    
    
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

def get_caller_identity():
    """
    Returns details about the IAM identity whose credentials are used to call the API.
    See also: AWS API Documentation
    
    Examples
    This example shows a request and response made with the credentials for a user named Alice in the AWS account 123456789012.
    Expected Output:
    This example shows a request and response made with temporary credentials created by AssumeRole. The name of the assumed role is my-role-name, and the RoleSessionName is set to my-role-session-name.
    Expected Output:
    This example shows a request and response made with temporary credentials created by using GetFederationToken. The Name parameter is set to my-federated-user-name.
    Expected Output:
    
    :example: response = client.get_caller_identity()
    
    
    :rtype: dict
    :return: {
        'UserId': 'string',
        'Account': 'string',
        'Arn': 'string'
    }
    
    
    """
    pass

def get_federation_token(Name=None, Policy=None, DurationSeconds=None):
    """
    Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a federated user. A typical use is in a proxy application that gets temporary security credentials on behalf of distributed applications inside a corporate network. Because you must call the GetFederationToken action using the long-term security credentials of an IAM user, this call is appropriate in contexts where those credentials can be safely stored, usually in a server-based application. For a comparison of GetFederationToken with the other APIs that produce temporary credentials, see Requesting Temporary Security Credentials and Comparing the AWS STS APIs in the IAM User Guide .
    The GetFederationToken action must be called by using the long-term AWS security credentials of an IAM user. You can also call GetFederationToken using the security credentials of an AWS root account, but we do not recommended it. Instead, we recommend that you create an IAM user for the purpose of the proxy application and then attach a policy to the IAM user that limits federated users to only the actions and resources that they need access to. For more information, see IAM Best Practices in the IAM User Guide .
    The temporary security credentials that are obtained by using the long-term credentials of an IAM user are valid for the specified duration, from 900 seconds (15 minutes) up to a maximium of 129600 seconds (36 hours). The default is 43200 seconds (12 hours). Temporary credentials that are obtained by using AWS root account credentials have a maximum duration of 3600 seconds (1 hour).
    The temporary security credentials created by GetFederationToken can be used to make API calls to any AWS service with the following exceptions:
    The permissions for the temporary security credentials returned by GetFederationToken are determined by a combination of the following:
    The passed policy is attached to the temporary security credentials that result from the GetFederationToken API call--that is, to the federated user . When the federated user makes an AWS request, AWS evaluates the policy attached to the federated user in combination with the policy or policies attached to the IAM user whose credentials were used to call GetFederationToken . AWS allows the federated user's request only when both the federated user * and * the IAM user are explicitly allowed to perform the requested action. The passed policy cannot grant more permissions than those that are defined in the IAM user policy.
    A typical use case is that the permissions of the IAM user whose credentials are used to call GetFederationToken are designed to allow access to all the actions and resources that any federated user will need. Then, for individual users, you pass a policy to the operation that scopes down the permissions to a level that's appropriate to that individual user, using a policy that allows only a subset of permissions that are granted to the IAM user.
    If you do not pass a policy, the resulting temporary security credentials have no effective permissions. The only exception is when the temporary security credentials are used to access a resource that has a resource-based policy that specifically allows the federated user to access the resource.
    For more information about how permissions work, see Permissions for GetFederationToken . For information about using GetFederationToken to create temporary security credentials, see GetFederationTokenFederation Through a Custom Identity Broker .
    See also: AWS API Documentation
    
    Examples
    Expected Output:
    
    :example: response = client.get_federation_token(
        Name='string',
        Policy='string',
        DurationSeconds=123
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]
            The name of the federated user. The name is used as an identifier for the temporary security credentials (such as Bob ). For example, you can reference the federated user name in a resource-based policy, such as in an Amazon S3 bucket policy.
            The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
            

    :type Policy: string
    :param Policy: An IAM policy in JSON format that is passed with the GetFederationToken call and evaluated along with the policy or policies that are attached to the IAM user whose credentials are used to call GetFederationToken . The passed policy is used to scope down the permissions that are available to the IAM user, by allowing only a subset of the permissions that are granted to the IAM user. The passed policy cannot grant more permissions than those granted to the IAM user. The final permissions for the federated user are the most restrictive set based on the intersection of the passed policy and the IAM user policy.
            If you do not pass a policy, the resulting temporary security credentials have no effective permissions. The only exception is when the temporary security credentials are used to access a resource that has a resource-based policy that specifically allows the federated user to access the resource.
            The format for this parameter, as described by its regex pattern, is a string of characters up to 2048 characters in length. The characters can be any ASCII character from the space character to the end of the valid character list (u0020-u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
            Note
            The policy plain text must be 2048 bytes or shorter. However, an internal conversion compresses it into a packed binary format with a separate limit. The PackedPolicySize response element indicates by percentage how close to the upper size limit the policy is, with 100% equaling the maximum allowed size.
            For more information about how permissions work, see Permissions for GetFederationToken .
            

    :type DurationSeconds: integer
    :param DurationSeconds: The duration, in seconds, that the session should last. Acceptable durations for federation sessions range from 900 seconds (15 minutes) to 129600 seconds (36 hours), with 43200 seconds (12 hours) as the default. Sessions obtained using AWS account (root) credentials are restricted to a maximum of 3600 seconds (one hour). If the specified duration is longer than one hour, the session obtained by using AWS account (root) credentials defaults to one hour.

    :rtype: dict
    :return: {
        'Credentials': {
            'AccessKeyId': 'string',
            'SecretAccessKey': 'string',
            'SessionToken': 'string',
            'Expiration': datetime(2015, 1, 1)
        },
        'FederatedUser': {
            'FederatedUserId': 'string',
            'Arn': 'string'
        },
        'PackedPolicySize': 123
    }
    
    
    :returns: 
    The policy or policies that are attached to the IAM user whose credentials are used to call GetFederationToken .
    The policy that is passed as a parameter in the call.
    
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

def get_session_token(DurationSeconds=None, SerialNumber=None, TokenCode=None):
    """
    Returns a set of temporary credentials for an AWS account or IAM user. The credentials consist of an access key ID, a secret access key, and a security token. Typically, you use GetSessionToken if you want to use MFA to protect programmatic calls to specific AWS APIs like Amazon EC2 StopInstances . MFA-enabled IAM users would need to call GetSessionToken and submit an MFA code that is associated with their MFA device. Using the temporary security credentials that are returned from the call, IAM users can then make programmatic calls to APIs that require MFA authentication. If you do not supply a correct MFA code, then the API returns an access denied error. For a comparison of GetSessionToken with the other APIs that produce temporary credentials, see Requesting Temporary Security Credentials and Comparing the AWS STS APIs in the IAM User Guide .
    The GetSessionToken action must be called by using the long-term AWS security credentials of the AWS account or an IAM user. Credentials that are created by IAM users are valid for the duration that you specify, from 900 seconds (15 minutes) up to a maximum of 129600 seconds (36 hours), with a default of 43200 seconds (12 hours); credentials that are created by using account credentials can range from 900 seconds (15 minutes) up to a maximum of 3600 seconds (1 hour), with a default of 1 hour.
    The temporary security credentials created by GetSessionToken can be used to make API calls to any AWS service with the following exceptions:
    The permissions associated with the temporary security credentials returned by GetSessionToken are based on the permissions associated with account or IAM user whose credentials are used to call the action. If GetSessionToken is called using root account credentials, the temporary credentials have root account permissions. Similarly, if GetSessionToken is called using the credentials of an IAM user, the temporary credentials have the same permissions as the IAM user.
    For more information about using GetSessionToken to create temporary credentials, go to Temporary Credentials for Users in Untrusted Environments in the IAM User Guide .
    See also: AWS API Documentation
    
    Examples
    Expected Output:
    
    :example: response = client.get_session_token(
        DurationSeconds=123,
        SerialNumber='string',
        TokenCode='string'
    )
    
    
    :type DurationSeconds: integer
    :param DurationSeconds: The duration, in seconds, that the credentials should remain valid. Acceptable durations for IAM user sessions range from 900 seconds (15 minutes) to 129600 seconds (36 hours), with 43200 seconds (12 hours) as the default. Sessions for AWS account owners are restricted to a maximum of 3600 seconds (one hour). If the duration is longer than one hour, the session for AWS account owners defaults to one hour.

    :type SerialNumber: string
    :param SerialNumber: The identification number of the MFA device that is associated with the IAM user who is making the GetSessionToken call. Specify this value if the IAM user has a policy that requires MFA authentication. The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user ). You can find the device for an IAM user by going to the AWS Management Console and viewing the user's security credentials.
            The regex used to validated this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-
            

    :type TokenCode: string
    :param TokenCode: The value provided by the MFA device, if MFA is required. If any policy requires the IAM user to submit an MFA code, specify this value. If MFA authentication is required, and the user does not provide a code when requesting a set of temporary security credentials, the user will receive an 'access denied' response when requesting resources that require MFA authentication.
            The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.
            

    :rtype: dict
    :return: {
        'Credentials': {
            'AccessKeyId': 'string',
            'SecretAccessKey': 'string',
            'SessionToken': 'string',
            'Expiration': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    DurationSeconds (integer) -- The duration, in seconds, that the credentials should remain valid. Acceptable durations for IAM user sessions range from 900 seconds (15 minutes) to 129600 seconds (36 hours), with 43200 seconds (12 hours) as the default. Sessions for AWS account owners are restricted to a maximum of 3600 seconds (one hour). If the duration is longer than one hour, the session for AWS account owners defaults to one hour.
    SerialNumber (string) -- The identification number of the MFA device that is associated with the IAM user who is making the GetSessionToken call. Specify this value if the IAM user has a policy that requires MFA authentication. The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user ). You can find the device for an IAM user by going to the AWS Management Console and viewing the user's security credentials.
    The regex used to validated this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-
    
    TokenCode (string) -- The value provided by the MFA device, if MFA is required. If any policy requires the IAM user to submit an MFA code, specify this value. If MFA authentication is required, and the user does not provide a code when requesting a set of temporary security credentials, the user will receive an "access denied" response when requesting resources that require MFA authentication.
    The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.
    
    
    """
    pass

def get_waiter():
    """
    
    """
    pass

