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


def assume_role(RoleArn=None, RoleSessionName=None, Policy=None, DurationSeconds=None, ExternalId=None,
                SerialNumber=None, TokenCode=None):
    """
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the role to assume.
            
    :type RoleArn: string
    :param RoleSessionName: [REQUIRED]
            An identifier for the assumed role session.
            Use the role session name to uniquely identify a session when the same role is assumed by different principals or for different reasons. In cross-account scenarios, the role session name is visible to, and can be logged by the account that owns the role. The role session name is also used in the ARN of the assumed role principal. This means that subsequent cross-account API requests using the temporary security credentials will expose the role session name to the external account in their CloudTrail logs.
            The format for this parameter, as described by its regex pattern, is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
            
    :type RoleSessionName: string
    :param Policy: An IAM policy in JSON format.
            This parameter is optional. If you pass a policy, the temporary security credentials that are returned by the operation have the permissions that are allowed by both (the intersection of) the access policy of the role that is being assumed, and the policy that you pass. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, see Permissions for AssumeRole, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity in the IAM User Guide .
            The format for this parameter, as described by its regex pattern, is a string of characters up to 2048 characters in length. The characters can be any ASCII character from the space character to the end of the valid character list (u0020-u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
            Note
            The policy plain text must be 2048 bytes or shorter. However, an internal conversion compresses it into a packed binary format with a separate limit. The PackedPolicySize response element indicates by percentage how close to the upper size limit the policy is, with 100% equaling the maximum allowed size.
            
    :type Policy: string
    :param DurationSeconds: The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 3600 seconds (1 hour). By default, the value is set to 3600 seconds.
            Note
            This is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session, separately from the DurationSeconds parameter on this API. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .
            
    :type DurationSeconds: integer
    :param ExternalId: A unique identifier that is used by third parties when assuming roles in their customers' accounts. For each role that the third party can assume, they should instruct their customers to ensure the role's trust policy checks for the external ID that the third party generated. Each time the third party assumes the role, they should pass the customer's external ID. The external ID is useful in order to help third parties bind a role to the customer who created it. For more information about the external ID, see How to Use an External ID When Granting Access to Your AWS Resources to a Third Party in the IAM User Guide .
            The format for this parameter, as described by its regex pattern, is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-
            
    :type ExternalId: string
    :param SerialNumber: The identification number of the MFA device that is associated with the user who is making the AssumeRole call. Specify this value if the trust policy of the role being assumed includes a condition that requires MFA authentication. The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user ).
            The format for this parameter, as described by its regex pattern, is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
            
    :type SerialNumber: string
    :param TokenCode: The value provided by the MFA device, if the trust policy of the role being assumed requires MFA (that is, if the policy includes a condition that tests for MFA). If the role being assumed requires MFA and if the TokenCode value is missing or expired, the AssumeRole call returns an 'access denied' error.
            The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.
            
    :type TokenCode: string
    """
    pass


def assume_role_with_saml(RoleArn=None, PrincipalArn=None, SAMLAssertion=None, Policy=None, DurationSeconds=None):
    """
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the role that the caller is assuming.
            
    :type RoleArn: string
    :param PrincipalArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.
            
    :type PrincipalArn: string
    :param SAMLAssertion: [REQUIRED]
            The base-64 encoded SAML authentication response provided by the IdP.
            For more information, see Configuring a Relying Party and Adding Claims in the Using IAM guide.
            
    :type SAMLAssertion: string
    :param Policy: An IAM policy in JSON format.
            The policy parameter is optional. If you pass a policy, the temporary security credentials that are returned by the operation have the permissions that are allowed by both the access policy of the role that is being assumed, * and * the policy that you pass. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, Permissions for AssumeRole, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity in the IAM User Guide .
            The format for this parameter, as described by its regex pattern, is a string of characters up to 2048 characters in length. The characters can be any ASCII character from the space character to the end of the valid character list (u0020-u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
            Note
            The policy plain text must be 2048 bytes or shorter. However, an internal conversion compresses it into a packed binary format with a separate limit. The PackedPolicySize response element indicates by percentage how close to the upper size limit the policy is, with 100% equaling the maximum allowed size.
            
    :type Policy: string
    :param DurationSeconds: The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 3600 seconds (1 hour). By default, the value is set to 3600 seconds. An expiration can also be specified in the SAML authentication response's SessionNotOnOrAfter value. The actual expiration time is whichever value is shorter.
            Note
            This is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session, separately from the DurationSeconds parameter on this API. For more information, see Enabling SAML 2.0 Federated Users to Access the AWS Management Console in the IAM User Guide .
            
    :type DurationSeconds: integer
    """
    pass


def assume_role_with_web_identity(RoleArn=None, RoleSessionName=None, WebIdentityToken=None, ProviderId=None,
                                  Policy=None, DurationSeconds=None):
    """
    :param RoleArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the role that the caller is assuming.
            
    :type RoleArn: string
    :param RoleSessionName: [REQUIRED]
            An identifier for the assumed role session. Typically, you pass the name or identifier that is associated with the user who is using your application. That way, the temporary security credentials that your application will use are associated with that user. This session name is included as part of the ARN and assumed role ID in the AssumedRoleUser response element.
            The format for this parameter, as described by its regex pattern, is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
            
    :type RoleSessionName: string
    :param WebIdentityToken: [REQUIRED]
            The OAuth 2.0 access token or OpenID Connect ID token that is provided by the identity provider. Your application must get this token by authenticating the user who is using your application with a web identity provider before the application makes an AssumeRoleWithWebIdentity call.
            
    :type WebIdentityToken: string
    :param ProviderId: The fully qualified host component of the domain name of the identity provider.
            Specify this value only for OAuth 2.0 access tokens. Currently www.amazon.com and graph.facebook.com are the only supported identity providers for OAuth 2.0 access tokens. Do not include URL schemes and port numbers.
            Do not specify this value for OpenID Connect ID tokens.
            
    :type ProviderId: string
    :param Policy: An IAM policy in JSON format.
            The policy parameter is optional. If you pass a policy, the temporary security credentials that are returned by the operation have the permissions that are allowed by both the access policy of the role that is being assumed, * and * the policy that you pass. This gives you a way to further restrict the permissions for the resulting temporary security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed. For more information, see Permissions for AssumeRoleWithWebIdentity in the IAM User Guide .
            The format for this parameter, as described by its regex pattern, is a string of characters up to 2048 characters in length. The characters can be any ASCII character from the space character to the end of the valid character list (u0020-u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
            Note
            The policy plain text must be 2048 bytes or shorter. However, an internal conversion compresses it into a packed binary format with a separate limit. The PackedPolicySize response element indicates by percentage how close to the upper size limit the policy is, with 100% equaling the maximum allowed size.
            
    :type Policy: string
    :param DurationSeconds: The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) to 3600 seconds (1 hour). By default, the value is set to 3600 seconds.
            Note
            This is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session, separately from the DurationSeconds parameter on this API. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .
            
    :type DurationSeconds: integer
    """
    pass


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


def decode_authorization_message(EncodedMessage=None):
    """
    :param EncodedMessage: [REQUIRED]
            The encoded message that was returned with the response.
            Return typedict
            ReturnsResponse Syntax{
              'DecodedMessage': 'string'
            }
            Response Structure
            (dict) --A document that contains additional information about the authorization status of a request from an encoded message that is returned in response to an AWS request.
            DecodedMessage (string) --An XML document that contains the decoded message.
            
            
    :type EncodedMessage: string
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


def get_caller_identity():
    """
    """
    pass


def get_federation_token(Name=None, Policy=None, DurationSeconds=None):
    """
    :param Name: [REQUIRED]
            The name of the federated user. The name is used as an identifier for the temporary security credentials (such as Bob ). For example, you can reference the federated user name in a resource-based policy, such as in an Amazon S3 bucket policy.
            The format for this parameter, as described by its regex pattern, is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
            
    :type Name: string
    :param Policy: An IAM policy in JSON format that is passed with the GetFederationToken call and evaluated along with the policy or policies that are attached to the IAM user whose credentials are used to call GetFederationToken . The passed policy is used to scope down the permissions that are available to the IAM user, by allowing only a subset of the permissions that are granted to the IAM user. The passed policy cannot grant more permissions than those granted to the IAM user. The final permissions for the federated user are the most restrictive set based on the intersection of the passed policy and the IAM user policy.
            If you do not pass a policy, the resulting temporary security credentials have no effective permissions. The only exception is when the temporary security credentials are used to access a resource that has a resource-based policy that specifically allows the federated user to access the resource.
            The format for this parameter, as described by its regex pattern, is a string of characters up to 2048 characters in length. The characters can be any ASCII character from the space character to the end of the valid character list (u0020-u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
            Note
            The policy plain text must be 2048 bytes or shorter. However, an internal conversion compresses it into a packed binary format with a separate limit. The PackedPolicySize response element indicates by percentage how close to the upper size limit the policy is, with 100% equaling the maximum allowed size.
            For more information about how permissions work, see Permissions for GetFederationToken .
            
    :type Policy: string
    :param DurationSeconds: The duration, in seconds, that the session should last. Acceptable durations for federation sessions range from 900 seconds (15 minutes) to 129600 seconds (36 hours), with 43200 seconds (12 hours) as the default. Sessions obtained using AWS account (root) credentials are restricted to a maximum of 3600 seconds (one hour). If the specified duration is longer than one hour, the session obtained by using AWS account (root) credentials defaults to one hour.
    :type DurationSeconds: integer
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


def get_session_token(DurationSeconds=None, SerialNumber=None, TokenCode=None):
    """
    :param DurationSeconds: The duration, in seconds, that the credentials should remain valid. Acceptable durations for IAM user sessions range from 900 seconds (15 minutes) to 129600 seconds (36 hours), with 43200 seconds (12 hours) as the default. Sessions for AWS account owners are restricted to a maximum of 3600 seconds (one hour). If the duration is longer than one hour, the session for AWS account owners defaults to one hour.
    :type DurationSeconds: integer
    :param SerialNumber: The identification number of the MFA device that is associated with the IAM user who is making the GetSessionToken call. Specify this value if the IAM user has a policy that requires MFA authentication. The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user ). You can find the device for an IAM user by going to the AWS Management Console and viewing the user's security credentials.
            The format for this parameter, as described by its regex pattern, is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
            
    :type SerialNumber: string
    :param TokenCode: The value provided by the MFA device, if MFA is required. If any policy requires the IAM user to submit an MFA code, specify this value. If MFA authentication is required, and the user does not provide a code when requesting a set of temporary security credentials, the user will receive an 'access denied' response when requesting resources that require MFA authentication.
            The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.
            
    :type TokenCode: string
    """
    pass


def get_waiter():
    """
    """
    pass
