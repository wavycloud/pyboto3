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

def assume_role(RoleArn=None, RoleSessionName=None, PolicyArns=None, Policy=None, DurationSeconds=None, Tags=None, TransitiveTagKeys=None, ExternalId=None, SerialNumber=None, TokenCode=None):
    """
    Returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to. These temporary credentials consist of an access key ID, a secret access key, and a security token. Typically, you use AssumeRole within your account or for cross-account access. For a comparison of AssumeRole with other API operations that produce temporary credentials, see Requesting Temporary Security Credentials and Comparing the AWS STS API operations in the IAM User Guide .
    For cross-account access, imagine that you own multiple accounts and need to access resources in each account. You could create long-term credentials in each account to access those resources. However, managing all those credentials and remembering which one can access which account can be time consuming. Instead, you can create one set of long-term credentials in one account. Then use temporary security credentials to access all the other accounts by assuming roles in those accounts. For more information about roles, see IAM Roles in the IAM User Guide .
    By default, the temporary security credentials created by AssumeRole last for one hour. However, you can use the optional DurationSeconds parameter to specify the duration of your session. You can provide a value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. To learn how to view the maximum value for your role, see View the Maximum Session Duration Setting for a Role in the IAM User Guide . The maximum session duration limit applies when you use the AssumeRole* API operations or the assume-role* CLI commands. However the limit does not apply when you use those operations to create a console URL. For more information, see Using IAM Roles in the IAM User Guide .
    The temporary security credentials created by AssumeRole can be used to make API calls to any AWS service with the following exception: You cannot call the AWS STS GetFederationToken or GetSessionToken API operations.
    (Optional) You can pass inline or managed session policies to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policies to use as managed session policies. The plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .
    To assume a role from a different account, your AWS account must be trusted by the role. The trust relationship is defined in the role\'s trust policy when the role is created. That trust policy states which accounts are allowed to delegate that access to users in the account.
    A user who wants to access a role in a different account must also have permissions that are delegated from the user account administrator. The administrator must attach a policy that allows the user to call AssumeRole for the ARN of the role in the other account. If the user is in the same account as the role, then you can do either of the following:
    In this case, the trust policy acts as an IAM resource-based policy. Users in the same account as the role do not need explicit permission to assume the role. For more information about trust policies and resource-based policies, see IAM Policies in the IAM User Guide .
    (Optional) You can pass tag key-value pairs to your session. These tags are called session tags. For more information about session tags, see Passing Session Tags in STS in the IAM User Guide .
    An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see Tutorial: Using Tags for Attribute-Based Access Control in the IAM User Guide .
    You can set the session tags as transitive. Transitive tags persist during role chaining. For more information, see Chaining Roles with Session Tags in the IAM User Guide .
    (Optional) You can include multi-factor authentication (MFA) information when you call AssumeRole . This is useful for cross-account scenarios to ensure that the user that assumes the role has been authenticated with an AWS MFA device. In that scenario, the trust policy of the role being assumed includes a condition that tests for MFA authentication. If the caller does not include valid MFA information, the request to assume the role is denied. The condition in a trust policy that tests for MFA authentication might look like the following example.
    For more information, see Configuring MFA-Protected API Access in the IAM User Guide guide.
    To use MFA with AssumeRole , you pass values for the SerialNumber and TokenCode parameters. The SerialNumber value identifies the user\'s hardware or virtual MFA device. The TokenCode is the time-based one-time password (TOTP) that the MFA device produces.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.assume_role(
        RoleArn='string',
        RoleSessionName='string',
        PolicyArns=[
            {
                'arn': 'string'
            },
        ],
        Policy='string',
        DurationSeconds=123,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        TransitiveTagKeys=[
            'string',
        ],
        ExternalId='string',
        SerialNumber='string',
        TokenCode='string'
    )
    
    
    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the role to assume.\n

    :type RoleSessionName: string
    :param RoleSessionName: [REQUIRED]\nAn identifier for the assumed role session.\nUse the role session name to uniquely identify a session when the same role is assumed by different principals or for different reasons. In cross-account scenarios, the role session name is visible to, and can be logged by the account that owns the role. The role session name is also used in the ARN of the assumed role principal. This means that subsequent cross-account API requests that use the temporary security credentials will expose the role session name to the external account in their AWS CloudTrail logs.\nThe regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-\n

    :type PolicyArns: list
    :param PolicyArns: The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.\nThis parameter is optional. You can provide up to 10 managed policy ARNs. However, the plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference.\n\nNote\nAn AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.\n\nPassing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .\n\n(dict) --A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.\n\narn (string) --The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n\n\n\n\n

    :type Policy: string
    :param Policy: An IAM policy in JSON format that you want to use as an inline session policy.\nThis parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .\nThe plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (u0020 through u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.\n\nNote\nAn AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.\n\n

    :type DurationSeconds: integer
    :param DurationSeconds: The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting, the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. To learn how to view the maximum value for your role, see View the Maximum Session Duration Setting for a Role in the IAM User Guide .\nBy default, the value is set to 3600 seconds.\n\nNote\nThe DurationSeconds parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .\n\n

    :type Tags: list
    :param Tags: A list of session tags that you want to pass. Each session tag consists of a key name and an associated value. For more information about session tags, see Tagging AWS STS Sessions in the IAM User Guide .\nThis parameter is optional. You can pass up to 50 session tags. The plain text session tag keys can\xe2\x80\x99t exceed 128 characters, and the values can\xe2\x80\x99t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .\n\nNote\nAn AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.\n\nYou can pass a session tag with the same key as a tag that is already attached to the role. When you do, session tags override a role tag with the same key.\nTag key\xe2\x80\x93value pairs are not case sensitive, but case is preserved. This means that you cannot have separate Department and department tag keys. Assume that the role has the Department =``Marketing`` tag and you pass the department =``engineering`` session tag. Department and department are not saved as separate tags, and the session tag passed in the request takes precedence over the role tag.\nAdditionally, if you used temporary credentials to perform this operation, the new session inherits any transitive session tags from the calling session. If you pass a session tag with the same key as an inherited tag, the operation fails. To view the inherited tags for a session, see the AWS CloudTrail logs. For more information, see Viewing Session Tags in CloudTrail in the IAM User Guide .\n\n(dict) --You can pass custom key-value pair attributes when you assume a role or federate a user. These are called session tags. You can then use the session tags to control access to resources. For more information, see Tagging AWS STS Sessions in the IAM User Guide .\n\nKey (string) -- [REQUIRED]The key for a session tag.\nYou can pass up to 50 session tags. The plain text session tag keys can\xe2\x80\x99t exceed 128 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .\n\nValue (string) -- [REQUIRED]The value for a session tag.\nYou can pass up to 50 session tags. The plain text session tag values can\xe2\x80\x99t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .\n\n\n\n\n

    :type TransitiveTagKeys: list
    :param TransitiveTagKeys: A list of keys for session tags that you want to set as transitive. If you set a tag key as transitive, the corresponding key and value passes to subsequent sessions in a role chain. For more information, see Chaining Roles with Session Tags in the IAM User Guide .\nThis parameter is optional. When you set session tags as transitive, the session policy and session tags packed binary limit is not affected.\nIf you choose not to specify a transitive tag key, then no tags are passed from this session to any subsequent sessions.\n\n(string) --\n\n

    :type ExternalId: string
    :param ExternalId: A unique identifier that might be required when you assume a role in another account. If the administrator of the account to which the role belongs provided you with an external ID, then provide that value in the ExternalId parameter. This value can be any string, such as a passphrase or account number. A cross-account role is usually set up to trust everyone in an account. Therefore, the administrator of the trusting account might send an external ID to the administrator of the trusted account. That way, only someone with the ID can assume the role, rather than everyone in the account. For more information about the external ID, see How to Use an External ID When Granting Access to Your AWS Resources to a Third Party in the IAM User Guide .\nThe regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-\n

    :type SerialNumber: string
    :param SerialNumber: The identification number of the MFA device that is associated with the user who is making the AssumeRole call. Specify this value if the trust policy of the role being assumed includes a condition that requires MFA authentication. The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user ).\nThe regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-\n

    :type TokenCode: string
    :param TokenCode: The value provided by the MFA device, if the trust policy of the role being assumed requires MFA (that is, if the policy includes a condition that tests for MFA). If the role being assumed requires MFA and if the TokenCode value is missing or expired, the AssumeRole call returns an 'access denied' error.\nThe format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  AssumeRole request, including temporary AWS credentials that can be used to make AWS requests.

Credentials (dict) --
The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.

Note
The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.


AccessKeyId (string) --
The access key ID that identifies the temporary security credentials.

SecretAccessKey (string) --
The secret access key that can be used to sign requests.

SessionToken (string) --
The token that users must pass to the service API to use the temporary credentials.

Expiration (datetime) --
The date on which the current credentials expire.



AssumedRoleUser (dict) --
The Amazon Resource Name (ARN) and the assumed role ID, which are identifiers that you can use to refer to the resulting temporary security credentials. For example, you can reference these credentials as a principal in a resource-based policy by using the ARN or assumed role ID. The ARN and ID include the RoleSessionName that you specified when you called AssumeRole .

AssumedRoleId (string) --
A unique identifier that contains the role ID and the role session name of the role that is being assumed. The role ID is generated by AWS when the role is created.

Arn (string) --
The ARN of the temporary security credentials that are returned from the  AssumeRole action. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .



PackedPolicySize (integer) --
A percentage value that indicates the packed size of the session policies and session tags combined passed in the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.







Exceptions

STS.Client.exceptions.MalformedPolicyDocumentException
STS.Client.exceptions.PackedPolicyTooLargeException
STS.Client.exceptions.RegionDisabledException

Examples
response = client.assume_role(
    DurationSeconds=3600,
    ExternalId='123ABC',
    Policy='{"Version":"2012-10-17","Statement":[{"Sid":"Stmt1","Effect":"Allow","Action":"s3:*","Resource":"*"}]}',
    RoleArn='arn:aws:iam::123456789012:role/demo',
    RoleSessionName='Bob',
)

print(response)


Expected Output:
{
    'AssumedRoleUser': {
        'Arn': 'arn:aws:sts::123456789012:assumed-role/demo/Bob',
        'AssumedRoleId': 'ARO123EXAMPLE123:Bob',
    },
    'Credentials': {
        'AccessKeyId': 'AKIAIOSFODNN7EXAMPLE',
        'Expiration': datetime(2011, 7, 15, 23, 28, 33, 4, 196, 0),
        'SecretAccessKey': 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY',
        'SessionToken': 'AQoDYXdzEPT//////////wEXAMPLEtc764bNrC9SAPBSM22wDOk4x4HIZ8j4FZTwdQWLWsKWHGBuFqwAeMicRXmxfpSPfIeoIYRqTflfKD8YUuwthAx7mSEI/qkPpKPi/kMcGdQrmGdeehM4IC1NtBmUpp2wUE8phUZampKsburEDy0KPkyQDYwT7WZ0wq5VSXDvp75YU9HFvlRd8Tx6q6fE8YQcHNVXAkiY9q6d+xo0rKwT38xVqr7ZD0u0iPPkUL64lIZbqBAz+scqKmlzm8FDrypNC9Yjc8fPOLn9FX9KSYvKTr4rvx3iSIlTJabIQwj2ICCR/oLxBA==',
    },
    'PackedPolicySize': 6,
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    
    :returns: 
    RoleArn (string) -- [REQUIRED]
    The Amazon Resource Name (ARN) of the role to assume.
    
    RoleSessionName (string) -- [REQUIRED]
    An identifier for the assumed role session.
    Use the role session name to uniquely identify a session when the same role is assumed by different principals or for different reasons. In cross-account scenarios, the role session name is visible to, and can be logged by the account that owns the role. The role session name is also used in the ARN of the assumed role principal. This means that subsequent cross-account API requests that use the temporary security credentials will expose the role session name to the external account in their AWS CloudTrail logs.
    The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
    
    PolicyArns (list) -- The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.
    This parameter is optional. You can provide up to 10 managed policy ARNs. However, the plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference.
    
    Note
    An AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.
    
    Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .
    
    (dict) --A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.
    
    arn (string) --The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    
    
    
    
    
    Policy (string) -- An IAM policy in JSON format that you want to use as an inline session policy.
    This parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .
    The plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (u0020 through u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
    
    Note
    An AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.
    
    
    DurationSeconds (integer) -- The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting, the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. To learn how to view the maximum value for your role, see View the Maximum Session Duration Setting for a Role in the IAM User Guide .
    By default, the value is set to 3600 seconds.
    
    Note
    The DurationSeconds parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .
    
    
    Tags (list) -- A list of session tags that you want to pass. Each session tag consists of a key name and an associated value. For more information about session tags, see Tagging AWS STS Sessions in the IAM User Guide .
    This parameter is optional. You can pass up to 50 session tags. The plain text session tag keys can\xe2\x80\x99t exceed 128 characters, and the values can\xe2\x80\x99t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .
    
    Note
    An AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.
    
    You can pass a session tag with the same key as a tag that is already attached to the role. When you do, session tags override a role tag with the same key.
    Tag key\xe2\x80\x93value pairs are not case sensitive, but case is preserved. This means that you cannot have separate Department and department tag keys. Assume that the role has the Department =``Marketing`` tag and you pass the department =``engineering`` session tag. Department and department are not saved as separate tags, and the session tag passed in the request takes precedence over the role tag.
    Additionally, if you used temporary credentials to perform this operation, the new session inherits any transitive session tags from the calling session. If you pass a session tag with the same key as an inherited tag, the operation fails. To view the inherited tags for a session, see the AWS CloudTrail logs. For more information, see Viewing Session Tags in CloudTrail in the IAM User Guide .
    
    (dict) --You can pass custom key-value pair attributes when you assume a role or federate a user. These are called session tags. You can then use the session tags to control access to resources. For more information, see Tagging AWS STS Sessions in the IAM User Guide .
    
    Key (string) -- [REQUIRED]The key for a session tag.
    You can pass up to 50 session tags. The plain text session tag keys can\xe2\x80\x99t exceed 128 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .
    
    Value (string) -- [REQUIRED]The value for a session tag.
    You can pass up to 50 session tags. The plain text session tag values can\xe2\x80\x99t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .
    
    
    
    
    
    TransitiveTagKeys (list) -- A list of keys for session tags that you want to set as transitive. If you set a tag key as transitive, the corresponding key and value passes to subsequent sessions in a role chain. For more information, see Chaining Roles with Session Tags in the IAM User Guide .
    This parameter is optional. When you set session tags as transitive, the session policy and session tags packed binary limit is not affected.
    If you choose not to specify a transitive tag key, then no tags are passed from this session to any subsequent sessions.
    
    (string) --
    
    
    ExternalId (string) -- A unique identifier that might be required when you assume a role in another account. If the administrator of the account to which the role belongs provided you with an external ID, then provide that value in the ExternalId parameter. This value can be any string, such as a passphrase or account number. A cross-account role is usually set up to trust everyone in an account. Therefore, the administrator of the trusting account might send an external ID to the administrator of the trusted account. That way, only someone with the ID can assume the role, rather than everyone in the account. For more information about the external ID, see How to Use an External ID When Granting Access to Your AWS Resources to a Third Party in the IAM User Guide .
    The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-
    
    SerialNumber (string) -- The identification number of the MFA device that is associated with the user who is making the AssumeRole call. Specify this value if the trust policy of the role being assumed includes a condition that requires MFA authentication. The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user ).
    The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
    
    TokenCode (string) -- The value provided by the MFA device, if the trust policy of the role being assumed requires MFA (that is, if the policy includes a condition that tests for MFA). If the role being assumed requires MFA and if the TokenCode value is missing or expired, the AssumeRole call returns an "access denied" error.
    The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.
    
    
    """
    pass

def assume_role_with_saml(RoleArn=None, PrincipalArn=None, SAMLAssertion=None, PolicyArns=None, Policy=None, DurationSeconds=None):
    """
    Returns a set of temporary security credentials for users who have been authenticated via a SAML authentication response. This operation provides a mechanism for tying an enterprise identity store or directory to role-based AWS access without user-specific credentials or configuration. For a comparison of AssumeRoleWithSAML with the other API operations that produce temporary credentials, see Requesting Temporary Security Credentials and Comparing the AWS STS API operations in the IAM User Guide .
    The temporary security credentials returned by this operation consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to AWS services.
    By default, the temporary security credentials created by AssumeRoleWithSAML last for one hour. However, you can use the optional DurationSeconds parameter to specify the duration of your session. Your role session lasts for the duration that you specify, or until the time specified in the SAML authentication response\'s SessionNotOnOrAfter value, whichever is shorter. You can provide a DurationSeconds value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. To learn how to view the maximum value for your role, see View the Maximum Session Duration Setting for a Role in the IAM User Guide . The maximum session duration limit applies when you use the AssumeRole* API operations or the assume-role* CLI commands. However the limit does not apply when you use those operations to create a console URL. For more information, see Using IAM Roles in the IAM User Guide .
    The temporary security credentials created by AssumeRoleWithSAML can be used to make API calls to any AWS service with the following exception: you cannot call the STS GetFederationToken or GetSessionToken API operations.
    (Optional) You can pass inline or managed session policies to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policies to use as managed session policies. The plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .
    Calling AssumeRoleWithSAML does not require the use of AWS security credentials. The identity of the caller is validated by using keys in the metadata document that is uploaded for the SAML provider entity for your identity provider.
    (Optional) You can configure your IdP to pass attributes into your SAML assertion as session tags. Each session tag consists of a key name and an associated value. For more information about session tags, see Passing Session Tags in STS in the IAM User Guide .
    You can pass up to 50 session tags. The plain text session tag keys can\xe2\x80\x99t exceed 128 characters and the values can\xe2\x80\x99t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .
    You can pass a session tag with the same key as a tag that is attached to the role. When you do, session tags override the role\'s tags with the same key.
    An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see Tutorial: Using Tags for Attribute-Based Access Control in the IAM User Guide .
    You can set the session tags as transitive. Transitive tags persist during role chaining. For more information, see Chaining Roles with Session Tags in the IAM User Guide .
    Before your application can call AssumeRoleWithSAML , you must configure your SAML identity provider (IdP) to issue the claims required by AWS. Additionally, you must use AWS Identity and Access Management (IAM) to create a SAML provider entity in your AWS account that represents your identity provider. You must also create an IAM role that specifies this SAML provider in its trust policy.
    For more information, see the following resources:
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.assume_role_with_saml(
        RoleArn='string',
        PrincipalArn='string',
        SAMLAssertion='string',
        PolicyArns=[
            {
                'arn': 'string'
            },
        ],
        Policy='string',
        DurationSeconds=123
    )
    
    
    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the role that the caller is assuming.\n

    :type PrincipalArn: string
    :param PrincipalArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.\n

    :type SAMLAssertion: string
    :param SAMLAssertion: [REQUIRED]\nThe base-64 encoded SAML authentication response provided by the IdP.\nFor more information, see Configuring a Relying Party and Adding Claims in the IAM User Guide .\n

    :type PolicyArns: list
    :param PolicyArns: The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.\nThis parameter is optional. You can provide up to 10 managed policy ARNs. However, the plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference.\n\nNote\nAn AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.\n\nPassing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .\n\n(dict) --A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.\n\narn (string) --The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n\n\n\n\n

    :type Policy: string
    :param Policy: An IAM policy in JSON format that you want to use as an inline session policy.\nThis parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .\nThe plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (u0020 through u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.\n\nNote\nAn AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.\n\n

    :type DurationSeconds: integer
    :param DurationSeconds: The duration, in seconds, of the role session. Your role session lasts for the duration that you specify for the DurationSeconds parameter, or until the time specified in the SAML authentication response\'s SessionNotOnOrAfter value, whichever is shorter. You can provide a DurationSeconds value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting, the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. To learn how to view the maximum value for your role, see View the Maximum Session Duration Setting for a Role in the IAM User Guide .\nBy default, the value is set to 3600 seconds.\n\nNote\nThe DurationSeconds parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  AssumeRoleWithSAML request, including temporary AWS credentials that can be used to make AWS requests.

Credentials (dict) --
The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.

Note
The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.


AccessKeyId (string) --
The access key ID that identifies the temporary security credentials.

SecretAccessKey (string) --
The secret access key that can be used to sign requests.

SessionToken (string) --
The token that users must pass to the service API to use the temporary credentials.

Expiration (datetime) --
The date on which the current credentials expire.



AssumedRoleUser (dict) --
The identifiers for the temporary security credentials that the operation returns.

AssumedRoleId (string) --
A unique identifier that contains the role ID and the role session name of the role that is being assumed. The role ID is generated by AWS when the role is created.

Arn (string) --
The ARN of the temporary security credentials that are returned from the  AssumeRole action. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .



PackedPolicySize (integer) --
A percentage value that indicates the packed size of the session policies and session tags combined passed in the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.

Subject (string) --
The value of the NameID element in the Subject element of the SAML assertion.

SubjectType (string) --
The format of the name ID, as defined by the Format attribute in the NameID element of the SAML assertion. Typical examples of the format are transient or persistent .
If the format includes the prefix urn:oasis:names:tc:SAML:2.0:nameid-format , that prefix is removed. For example, urn:oasis:names:tc:SAML:2.0:nameid-format:transient is returned as transient . If the format includes any other prefix, the format is returned with no modifications.

Issuer (string) --
The value of the Issuer element of the SAML assertion.

Audience (string) --
The value of the Recipient attribute of the SubjectConfirmationData element of the SAML assertion.

NameQualifier (string) --
A hash value based on the concatenation of the Issuer response value, the AWS account ID, and the friendly name (the last part of the ARN) of the SAML provider in IAM. The combination of NameQualifier and Subject can be used to uniquely identify a federated user.
The following pseudocode shows how the hash value is calculated:

BASE64 ( SHA1 ( "https://example.com/saml" + "123456789012" + "/MySAMLIdP" ) )








Exceptions

STS.Client.exceptions.MalformedPolicyDocumentException
STS.Client.exceptions.PackedPolicyTooLargeException
STS.Client.exceptions.IDPRejectedClaimException
STS.Client.exceptions.InvalidIdentityTokenException
STS.Client.exceptions.ExpiredTokenException
STS.Client.exceptions.RegionDisabledException


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
    For more information, see Configuring a Relying Party and Adding Claims in the IAM User Guide .
    
    PolicyArns (list) -- The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.
    This parameter is optional. You can provide up to 10 managed policy ARNs. However, the plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference.
    
    Note
    An AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.
    
    Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .
    
    (dict) --A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.
    
    arn (string) --The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    
    
    
    
    
    Policy (string) -- An IAM policy in JSON format that you want to use as an inline session policy.
    This parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .
    The plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (u0020 through u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
    
    Note
    An AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.
    
    
    DurationSeconds (integer) -- The duration, in seconds, of the role session. Your role session lasts for the duration that you specify for the DurationSeconds parameter, or until the time specified in the SAML authentication response\'s SessionNotOnOrAfter value, whichever is shorter. You can provide a DurationSeconds value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting, the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. To learn how to view the maximum value for your role, see View the Maximum Session Duration Setting for a Role in the IAM User Guide .
    By default, the value is set to 3600 seconds.
    
    Note
    The DurationSeconds parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .
    
    
    
    """
    pass

def assume_role_with_web_identity(RoleArn=None, RoleSessionName=None, WebIdentityToken=None, ProviderId=None, PolicyArns=None, Policy=None, DurationSeconds=None):
    """
    Returns a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider. Example providers include Amazon Cognito, Login with Amazon, Facebook, Google, or any OpenID Connect-compatible identity provider.
    Calling AssumeRoleWithWebIdentity does not require the use of AWS security credentials. Therefore, you can distribute an application (for example, on mobile devices) that requests temporary security credentials without including long-term AWS credentials in the application. You also don\'t need to deploy server-based proxy services that use long-term AWS credentials. Instead, the identity of the caller is validated by using a token from the web identity provider. For a comparison of AssumeRoleWithWebIdentity with the other API operations that produce temporary credentials, see Requesting Temporary Security Credentials and Comparing the AWS STS API operations in the IAM User Guide .
    The temporary security credentials returned by this API consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to AWS service API operations.
    By default, the temporary security credentials created by AssumeRoleWithWebIdentity last for one hour. However, you can use the optional DurationSeconds parameter to specify the duration of your session. You can provide a value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. To learn how to view the maximum value for your role, see View the Maximum Session Duration Setting for a Role in the IAM User Guide . The maximum session duration limit applies when you use the AssumeRole* API operations or the assume-role* CLI commands. However the limit does not apply when you use those operations to create a console URL. For more information, see Using IAM Roles in the IAM User Guide .
    The temporary security credentials created by AssumeRoleWithWebIdentity can be used to make API calls to any AWS service with the following exception: you cannot call the STS GetFederationToken or GetSessionToken API operations.
    (Optional) You can pass inline or managed session policies to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policies to use as managed session policies. The plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .
    (Optional) You can configure your IdP to pass attributes into your web identity token as session tags. Each session tag consists of a key name and an associated value. For more information about session tags, see Passing Session Tags in STS in the IAM User Guide .
    You can pass up to 50 session tags. The plain text session tag keys can\xe2\x80\x99t exceed 128 characters and the values can\xe2\x80\x99t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .
    You can pass a session tag with the same key as a tag that is attached to the role. When you do, the session tag overrides the role tag with the same key.
    An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see Tutorial: Using Tags for Attribute-Based Access Control in the IAM User Guide .
    You can set the session tags as transitive. Transitive tags persist during role chaining. For more information, see Chaining Roles with Session Tags in the IAM User Guide .
    Before your application can call AssumeRoleWithWebIdentity , you must have an identity token from a supported identity provider and create a role that the application can assume. The role that your application assumes must trust the identity provider that is associated with the identity token. In other words, the identity provider must be specified in the role\'s trust policy.
    For more information about how to use web identity federation and the AssumeRoleWithWebIdentity API, see the following resources:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.assume_role_with_web_identity(
        RoleArn='string',
        RoleSessionName='string',
        WebIdentityToken='string',
        ProviderId='string',
        PolicyArns=[
            {
                'arn': 'string'
            },
        ],
        Policy='string',
        DurationSeconds=123
    )
    
    
    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the role that the caller is assuming.\n

    :type RoleSessionName: string
    :param RoleSessionName: [REQUIRED]\nAn identifier for the assumed role session. Typically, you pass the name or identifier that is associated with the user who is using your application. That way, the temporary security credentials that your application will use are associated with that user. This session name is included as part of the ARN and assumed role ID in the AssumedRoleUser response element.\nThe regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-\n

    :type WebIdentityToken: string
    :param WebIdentityToken: [REQUIRED]\nThe OAuth 2.0 access token or OpenID Connect ID token that is provided by the identity provider. Your application must get this token by authenticating the user who is using your application with a web identity provider before the application makes an AssumeRoleWithWebIdentity call.\n

    :type ProviderId: string
    :param ProviderId: The fully qualified host component of the domain name of the identity provider.\nSpecify this value only for OAuth 2.0 access tokens. Currently www.amazon.com and graph.facebook.com are the only supported identity providers for OAuth 2.0 access tokens. Do not include URL schemes and port numbers.\nDo not specify this value for OpenID Connect ID tokens.\n

    :type PolicyArns: list
    :param PolicyArns: The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.\nThis parameter is optional. You can provide up to 10 managed policy ARNs. However, the plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference.\n\nNote\nAn AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.\n\nPassing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .\n\n(dict) --A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.\n\narn (string) --The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n\n\n\n\n

    :type Policy: string
    :param Policy: An IAM policy in JSON format that you want to use as an inline session policy.\nThis parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .\nThe plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (u0020 through u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.\n\nNote\nAn AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.\n\n

    :type DurationSeconds: integer
    :param DurationSeconds: The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting, the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. To learn how to view the maximum value for your role, see View the Maximum Session Duration Setting for a Role in the IAM User Guide .\nBy default, the value is set to 3600 seconds.\n\nNote\nThe DurationSeconds parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  AssumeRoleWithWebIdentity request, including temporary AWS credentials that can be used to make AWS requests.

Credentials (dict) --
The temporary security credentials, which include an access key ID, a secret access key, and a security token.

Note
The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.


AccessKeyId (string) --
The access key ID that identifies the temporary security credentials.

SecretAccessKey (string) --
The secret access key that can be used to sign requests.

SessionToken (string) --
The token that users must pass to the service API to use the temporary credentials.

Expiration (datetime) --
The date on which the current credentials expire.



SubjectFromWebIdentityToken (string) --
The unique user identifier that is returned by the identity provider. This identifier is associated with the WebIdentityToken that was submitted with the AssumeRoleWithWebIdentity call. The identifier is typically unique to the user and the application that acquired the WebIdentityToken (pairwise identifier). For OpenID Connect ID tokens, this field contains the value returned by the identity provider as the token\'s sub (Subject) claim.

AssumedRoleUser (dict) --
The Amazon Resource Name (ARN) and the assumed role ID, which are identifiers that you can use to refer to the resulting temporary security credentials. For example, you can reference these credentials as a principal in a resource-based policy by using the ARN or assumed role ID. The ARN and ID include the RoleSessionName that you specified when you called AssumeRole .

AssumedRoleId (string) --
A unique identifier that contains the role ID and the role session name of the role that is being assumed. The role ID is generated by AWS when the role is created.

Arn (string) --
The ARN of the temporary security credentials that are returned from the  AssumeRole action. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .



PackedPolicySize (integer) --
A percentage value that indicates the packed size of the session policies and session tags combined passed in the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.

Provider (string) --
The issuing authority of the web identity token presented. For OpenID Connect ID tokens, this contains the value of the iss field. For OAuth 2.0 access tokens, this contains the value of the ProviderId parameter that was passed in the AssumeRoleWithWebIdentity request.

Audience (string) --
The intended audience (also known as client ID) of the web identity token. This is traditionally the client identifier issued to the application that requested the web identity token.







Exceptions

STS.Client.exceptions.MalformedPolicyDocumentException
STS.Client.exceptions.PackedPolicyTooLargeException
STS.Client.exceptions.IDPRejectedClaimException
STS.Client.exceptions.IDPCommunicationErrorException
STS.Client.exceptions.InvalidIdentityTokenException
STS.Client.exceptions.ExpiredTokenException
STS.Client.exceptions.RegionDisabledException

Examples
response = client.assume_role_with_web_identity(
    DurationSeconds=3600,
    ProviderId='www.amazon.com',
    RoleArn='arn:aws:iam::123456789012:role/FederatedWebIdentityRole',
    RoleSessionName='app1',
    WebIdentityToken='Atza%7CIQEBLjAsAhRFiXuWpUXuRvQ9PZL3GMFcYevydwIUFAHZwXZXXXXXXXXJnrulxKDHwy87oGKPznh0D6bEQZTSCzyoCtL_8S07pLpr0zMbn6w1lfVZKNTBdDansFBmtGnIsIapjI6xKR02Yc_2bQ8LZbUXSGm6Ry6_BG7PrtLZtj_dfCTj92xNGed-CrKqjG7nPBjNIL016GGvuS5gSvPRUxWES3VYfm1wl7WTI7jn-Pcb6M-buCgHhFOzTQxod27L9CqnOLio7N3gZAGpsp6n1-AJBOCJckcyXe2c6uD0srOJeZlKUm2eTDVMf8IehDVI0r1QOnTV6KzzAI3OY87Vd_cVMQ',
)

print(response)


Expected Output:
{
    'AssumedRoleUser': {
        'Arn': 'arn:aws:sts::123456789012:assumed-role/FederatedWebIdentityRole/app1',
        'AssumedRoleId': 'AROACLKWSDQRAOEXAMPLE:app1',
    },
    'Audience': 'client.5498841531868486423.1548@apps.example.com',
    'Credentials': {
        'AccessKeyId': 'AKIAIOSFODNN7EXAMPLE',
        'Expiration': datetime(2014, 10, 24, 23, 0, 23, 4, 297, 0),
        'SecretAccessKey': 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY',
        'SessionToken': 'AQoDYXdzEE0a8ANXXXXXXXXNO1ewxE5TijQyp+IEXAMPLE',
    },
    'PackedPolicySize': 123,
    'Provider': 'www.amazon.com',
    'SubjectFromWebIdentityToken': 'amzn1.account.AF6RHO7KZU5XRVQJGXK6HEXAMPLE',
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    
    PolicyArns (list) -- The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role.
    This parameter is optional. You can provide up to 10 managed policy ARNs. However, the plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference.
    
    Note
    An AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.
    
    Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .
    
    (dict) --A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.
    
    arn (string) --The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    
    
    
    
    
    Policy (string) -- An IAM policy in JSON format that you want to use as an inline session policy.
    This parameter is optional. Passing policies to this operation returns new temporary credentials. The resulting session\'s permissions are the intersection of the role\'s identity-based policy and the session policies. You can use the role\'s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide .
    The plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (u0020 through u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
    
    Note
    An AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.
    
    
    DurationSeconds (integer) -- The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. If you specify a value higher than this setting, the operation fails. For example, if you specify a session duration of 12 hours, but your administrator set the maximum session duration to 6 hours, your operation fails. To learn how to view the maximum value for your role, see View the Maximum Session Duration Setting for a Role in the IAM User Guide .
    By default, the value is set to 3600 seconds.
    
    Note
    The DurationSeconds parameter is separate from the duration of a console session that you might request using the returned credentials. The request to the federation endpoint for a console sign-in token takes a SessionDuration parameter that specifies the maximum length of the console session. For more information, see Creating a URL that Enables Federated Users to Access the AWS Management Console in the IAM User Guide .
    
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def decode_authorization_message(EncodedMessage=None):
    """
    Decodes additional information about the authorization status of a request from an encoded message returned in response to an AWS request.
    For example, if a user is not authorized to perform an operation that he or she has requested, the request returns a Client.UnauthorizedOperation response (an HTTP 403 response). Some AWS operations additionally return an encoded message that can provide details about this authorization failure.
    The message is encoded because the details of the authorization status can constitute privileged information that the user who requested the operation should not see. To decode an authorization status message, a user must be granted permissions via an IAM policy to request the DecodeAuthorizationMessage (sts:DecodeAuthorizationMessage ) action.
    The decoded message includes the following type of information:
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.decode_authorization_message(
        EncodedMessage='string'
    )
    
    
    :type EncodedMessage: string
    :param EncodedMessage: [REQUIRED]\nThe encoded message that was returned with the response.\n

    :rtype: dict
ReturnsResponse Syntax{
    'DecodedMessage': 'string'
}


Response Structure

(dict) --A document that contains additional information about the authorization status of a request from an encoded message that is returned in response to an AWS request.

DecodedMessage (string) --An XML document that contains the decoded message.






Exceptions

STS.Client.exceptions.InvalidAuthorizationMessageException

Examples
response = client.decode_authorization_message(
    EncodedMessage='<encoded-message>',
)

print(response)


Expected Output:
{
    'DecodedMessage': '{"allowed": "false","explicitDeny": "false","matchedStatements": "","failures": "","context": {"principal": {"id": "AIDACKCEVSQ6C2EXAMPLE","name": "Bob","arn": "arn:aws:iam::123456789012:user/Bob"},"action": "ec2:StopInstances","resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-dd01c9bd","conditions": [{"item": {"key": "ec2:Tenancy","values": ["default"]},{"item": {"key": "ec2:ResourceTag/elasticbeanstalk:environment-name","values": ["Default-Environment"]}},(Additional items ...)]}}',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'DecodedMessage': 'string'
    }
    
    
    :returns: 
    STS.Client.exceptions.InvalidAuthorizationMessageException
    
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

def get_access_key_info(AccessKeyId=None):
    """
    Returns the account identifier for the specified access key ID.
    Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE ) and a secret access key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY ). For more information about access keys, see Managing Access Keys for IAM Users in the IAM User Guide .
    When you pass an access key ID to this operation, it returns the ID of the AWS account to which the keys belong. Access key IDs beginning with AKIA are long-term credentials for an IAM user or the AWS account root user. Access key IDs beginning with ASIA are temporary credentials that are created using STS operations. If the account in the response belongs to you, you can sign in as the root user and review your root user access keys. Then, you can pull a credentials report to learn which IAM user owns the keys. To learn who requested the temporary credentials for an ASIA access key, view the STS events in your CloudTrail logs in the IAM User Guide .
    This operation does not indicate the state of the access key. The key might be active, inactive, or deleted. Active keys might not have permissions to perform an operation. Providing a deleted access key might return an error that the key doesn\'t exist.
    See also: AWS API Documentation
    
    
    :example: response = client.get_access_key_info(
        AccessKeyId='string'
    )
    
    
    :type AccessKeyId: string
    :param AccessKeyId: [REQUIRED]\nThe identifier of an access key.\nThis parameter allows (through its regex pattern) a string of characters that can consist of any upper- or lowercase letter or digit.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Account': 'string'
}


Response Structure

(dict) --
Account (string) --The number used to identify the AWS account.







    :return: {
        'Account': 'string'
    }
    
    
    """
    pass

def get_caller_identity():
    """
    Returns details about the IAM user or role whose credentials are used to call the operation.
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
ReturnsResponse Syntax{
    'UserId': 'string',
    'Account': 'string',
    'Arn': 'string'
}


Response Structure

(dict) --Contains the response to a successful  GetCallerIdentity request, including information about the entity making the request.

UserId (string) --The unique identifier of the calling entity. The exact value depends on the type of entity that is making the call. The values returned are those listed in the aws:userid column in the Principal table found on the Policy Variables reference page in the IAM User Guide .

Account (string) --The AWS account ID number of the account that owns or contains the calling entity.

Arn (string) --The AWS ARN associated with the calling entity.






Examples
This example shows a request and response made with the credentials for a user named Alice in the AWS account 123456789012.
response = client.get_caller_identity(
)

print(response)


Expected Output:
{
    'Account': '123456789012',
    'Arn': 'arn:aws:iam::123456789012:user/Alice',
    'UserId': 'AKIAI44QH8DHBEXAMPLE',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example shows a request and response made with temporary credentials created by AssumeRole. The name of the assumed role is my-role-name, and the RoleSessionName is set to my-role-session-name.
response = client.get_caller_identity(
)

print(response)


Expected Output:
{
    'Account': '123456789012',
    'Arn': 'arn:aws:sts::123456789012:assumed-role/my-role-name/my-role-session-name',
    'UserId': 'AKIAI44QH8DHBEXAMPLE:my-role-session-name',
    'ResponseMetadata': {
        '...': '...',
    },
}


This example shows a request and response made with temporary credentials created by using GetFederationToken. The Name parameter is set to my-federated-user-name.
response = client.get_caller_identity(
)

print(response)


Expected Output:
{
    'Account': '123456789012',
    'Arn': 'arn:aws:sts::123456789012:federated-user/my-federated-user-name',
    'UserId': '123456789012:my-federated-user-name',
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'UserId': 'string',
        'Account': 'string',
        'Arn': 'string'
    }
    
    
    """
    pass

def get_federation_token(Name=None, Policy=None, PolicyArns=None, DurationSeconds=None, Tags=None):
    """
    Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a federated user. A typical use is in a proxy application that gets temporary security credentials on behalf of distributed applications inside a corporate network. You must call the GetFederationToken operation using the long-term security credentials of an IAM user. As a result, this call is appropriate in contexts where those credentials can be safely stored, usually in a server-based application. For a comparison of GetFederationToken with the other API operations that produce temporary credentials, see Requesting Temporary Security Credentials and Comparing the AWS STS API operations in the IAM User Guide .
    You can also call GetFederationToken using the security credentials of an AWS account root user, but we do not recommend it. Instead, we recommend that you create an IAM user for the purpose of the proxy application. Then attach a policy to the IAM user that limits federated users to only the actions and resources that they need to access. For more information, see IAM Best Practices in the IAM User Guide .
    The temporary credentials are valid for the specified duration, from 900 seconds (15 minutes) up to a maximum of 129,600 seconds (36 hours). The default session duration is 43,200 seconds (12 hours). Temporary credentials that are obtained by using AWS account root user credentials have a maximum duration of 3,600 seconds (1 hour).
    You can use the temporary credentials created by GetFederationToken in any AWS service except the following:
    You must pass an inline or managed session policy to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policies to use as managed session policies. The plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters.
    Though the session policy parameters are optional, if you do not pass a policy, then the resulting federated user session has no permissions. When you pass session policies, the session permissions are the intersection of the IAM user policies and the session policies that you pass. This gives you a way to further restrict the permissions for a federated user. You cannot use session policies to grant more permissions than those that are defined in the permissions policy of the IAM user. For more information, see Session Policies in the IAM User Guide . For information about using GetFederationToken to create temporary security credentials, see GetFederationToken\xe2\x80\x94Federation Through a Custom Identity Broker .
    You can use the credentials to access a resource that has a resource-based policy. If that policy specifically references the federated user session in the Principal element of the policy, the session has the permissions allowed by the policy. These permissions are granted in addition to the permissions granted by the session policies.
    (Optional) You can pass tag key-value pairs to your session. These are called session tags. For more information about session tags, see Passing Session Tags in STS in the IAM User Guide .
    An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see Tutorial: Using Tags for Attribute-Based Access Control in the IAM User Guide .
    Tag key\xe2\x80\x93value pairs are not case sensitive, but case is preserved. This means that you cannot have separate Department and department tag keys. Assume that the user that you are federating has the Department =``Marketing`` tag and you pass the department =``engineering`` session tag. Department and department are not saved as separate tags, and the session tag passed in the request takes precedence over the user tag.
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.get_federation_token(
        Name='string',
        Policy='string',
        PolicyArns=[
            {
                'arn': 'string'
            },
        ],
        DurationSeconds=123,
        Tags=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the federated user. The name is used as an identifier for the temporary security credentials (such as Bob ). For example, you can reference the federated user name in a resource-based policy, such as in an Amazon S3 bucket policy.\nThe regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-\n

    :type Policy: string
    :param Policy: An IAM policy in JSON format that you want to use as an inline session policy.\nYou must pass an inline or managed session policy to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policies to use as managed session policies.\nThis parameter is optional. However, if you do not pass any session policies, then the resulting federated user session has no permissions.\nWhen you pass session policies, the session permissions are the intersection of the IAM user policies and the session policies that you pass. This gives you a way to further restrict the permissions for a federated user. You cannot use session policies to grant more permissions than those that are defined in the permissions policy of the IAM user. For more information, see Session Policies in the IAM User Guide .\nThe resulting credentials can be used to access a resource that has a resource-based policy. If that policy specifically references the federated user session in the Principal element of the policy, the session has the permissions allowed by the policy. These permissions are granted in addition to the permissions that are granted by the session policies.\nThe plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (u0020 through u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.\n\nNote\nAn AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.\n\n

    :type PolicyArns: list
    :param PolicyArns: The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as a managed session policy. The policies must exist in the same account as the IAM user that is requesting federated access.\nYou must pass an inline or managed session policy to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policies to use as managed session policies. The plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. You can provide up to 10 managed policy ARNs. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference.\nThis parameter is optional. However, if you do not pass any session policies, then the resulting federated user session has no permissions.\nWhen you pass session policies, the session permissions are the intersection of the IAM user policies and the session policies that you pass. This gives you a way to further restrict the permissions for a federated user. You cannot use session policies to grant more permissions than those that are defined in the permissions policy of the IAM user. For more information, see Session Policies in the IAM User Guide .\nThe resulting credentials can be used to access a resource that has a resource-based policy. If that policy specifically references the federated user session in the Principal element of the policy, the session has the permissions allowed by the policy. These permissions are granted in addition to the permissions that are granted by the session policies.\n\nNote\nAn AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.\n\n\n(dict) --A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.\n\narn (string) --The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .\n\n\n\n\n

    :type DurationSeconds: integer
    :param DurationSeconds: The duration, in seconds, that the session should last. Acceptable durations for federation sessions range from 900 seconds (15 minutes) to 129,600 seconds (36 hours), with 43,200 seconds (12 hours) as the default. Sessions obtained using AWS account root user credentials are restricted to a maximum of 3,600 seconds (one hour). If the specified duration is longer than one hour, the session obtained by using root user credentials defaults to one hour.

    :type Tags: list
    :param Tags: A list of session tags. Each session tag consists of a key name and an associated value. For more information about session tags, see Passing Session Tags in STS in the IAM User Guide .\nThis parameter is optional. You can pass up to 50 session tags. The plain text session tag keys can\xe2\x80\x99t exceed 128 characters and the values can\xe2\x80\x99t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .\n\nNote\nAn AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.\n\nYou can pass a session tag with the same key as a tag that is already attached to the user you are federating. When you do, session tags override a user tag with the same key.\nTag key\xe2\x80\x93value pairs are not case sensitive, but case is preserved. This means that you cannot have separate Department and department tag keys. Assume that the role has the Department =``Marketing`` tag and you pass the department =``engineering`` session tag. Department and department are not saved as separate tags, and the session tag passed in the request takes precedence over the role tag.\n\n(dict) --You can pass custom key-value pair attributes when you assume a role or federate a user. These are called session tags. You can then use the session tags to control access to resources. For more information, see Tagging AWS STS Sessions in the IAM User Guide .\n\nKey (string) -- [REQUIRED]The key for a session tag.\nYou can pass up to 50 session tags. The plain text session tag keys can\xe2\x80\x99t exceed 128 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .\n\nValue (string) -- [REQUIRED]The value for a session tag.\nYou can pass up to 50 session tags. The plain text session tag values can\xe2\x80\x99t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
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


Response Structure

(dict) --
Contains the response to a successful  GetFederationToken request, including temporary AWS credentials that can be used to make AWS requests.

Credentials (dict) --
The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.

Note
The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.


AccessKeyId (string) --
The access key ID that identifies the temporary security credentials.

SecretAccessKey (string) --
The secret access key that can be used to sign requests.

SessionToken (string) --
The token that users must pass to the service API to use the temporary credentials.

Expiration (datetime) --
The date on which the current credentials expire.



FederatedUser (dict) --
Identifiers for the federated user associated with the credentials (such as arn:aws:sts::123456789012:federated-user/Bob or 123456789012:Bob ). You can use the federated user\'s ARN in your resource-based policies, such as an Amazon S3 bucket policy.

FederatedUserId (string) --
The string that identifies the federated user associated with the credentials, similar to the unique ID of an IAM user.

Arn (string) --
The ARN that specifies the federated user that is associated with the credentials. For more information about ARNs and how to use them in policies, see IAM Identifiers in the IAM User Guide .



PackedPolicySize (integer) --
A percentage value that indicates the packed size of the session policies and session tags combined passed in the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.







Exceptions

STS.Client.exceptions.MalformedPolicyDocumentException
STS.Client.exceptions.PackedPolicyTooLargeException
STS.Client.exceptions.RegionDisabledException

Examples
response = client.get_federation_token(
    DurationSeconds=3600,
    Name='Bob',
    Policy='{"Version":"2012-10-17","Statement":[{"Sid":"Stmt1","Effect":"Allow","Action":"s3:*","Resource":"*"}]}',
)

print(response)


Expected Output:
{
    'Credentials': {
        'AccessKeyId': 'AKIAIOSFODNN7EXAMPLE',
        'Expiration': datetime(2011, 7, 15, 23, 28, 33, 4, 196, 0),
        'SecretAccessKey': 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY',
        'SessionToken': 'AQoDYXdzEPT//////////wEXAMPLEtc764bNrC9SAPBSM22wDOk4x4HIZ8j4FZTwdQWLWsKWHGBuFqwAeMicRXmxfpSPfIeoIYRqTflfKD8YUuwthAx7mSEI/qkPpKPi/kMcGdQrmGdeehM4IC1NtBmUpp2wUE8phUZampKsburEDy0KPkyQDYwT7WZ0wq5VSXDvp75YU9HFvlRd8Tx6q6fE8YQcHNVXAkiY9q6d+xo0rKwT38xVqr7ZD0u0iPPkUL64lIZbqBAz+scqKmlzm8FDrypNC9Yjc8fPOLn9FX9KSYvKTr4rvx3iSIlTJabIQwj2ICCR/oLxBA==',
    },
    'FederatedUser': {
        'Arn': 'arn:aws:sts::123456789012:federated-user/Bob',
        'FederatedUserId': '123456789012:Bob',
    },
    'PackedPolicySize': 6,
    'ResponseMetadata': {
        '...': '...',
    },
}



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
    Name (string) -- [REQUIRED]
    The name of the federated user. The name is used as an identifier for the temporary security credentials (such as Bob ). For example, you can reference the federated user name in a resource-based policy, such as in an Amazon S3 bucket policy.
    The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
    
    Policy (string) -- An IAM policy in JSON format that you want to use as an inline session policy.
    You must pass an inline or managed session policy to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policies to use as managed session policies.
    This parameter is optional. However, if you do not pass any session policies, then the resulting federated user session has no permissions.
    When you pass session policies, the session permissions are the intersection of the IAM user policies and the session policies that you pass. This gives you a way to further restrict the permissions for a federated user. You cannot use session policies to grant more permissions than those that are defined in the permissions policy of the IAM user. For more information, see Session Policies in the IAM User Guide .
    The resulting credentials can be used to access a resource that has a resource-based policy. If that policy specifically references the federated user session in the Principal element of the policy, the session has the permissions allowed by the policy. These permissions are granted in addition to the permissions that are granted by the session policies.
    The plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. The JSON policy characters can be any ASCII character from the space character to the end of the valid character list (u0020 through u00FF). It can also include the tab (u0009), linefeed (u000A), and carriage return (u000D) characters.
    
    Note
    An AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.
    
    
    PolicyArns (list) -- The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as a managed session policy. The policies must exist in the same account as the IAM user that is requesting federated access.
    You must pass an inline or managed session policy to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policies to use as managed session policies. The plain text that you use for both inline and managed session policies can\'t exceed 2,048 characters. You can provide up to 10 managed policy ARNs. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference.
    This parameter is optional. However, if you do not pass any session policies, then the resulting federated user session has no permissions.
    When you pass session policies, the session permissions are the intersection of the IAM user policies and the session policies that you pass. This gives you a way to further restrict the permissions for a federated user. You cannot use session policies to grant more permissions than those that are defined in the permissions policy of the IAM user. For more information, see Session Policies in the IAM User Guide .
    The resulting credentials can be used to access a resource that has a resource-based policy. If that policy specifically references the federated user session in the Principal element of the policy, the session has the permissions allowed by the policy. These permissions are granted in addition to the permissions that are granted by the session policies.
    
    Note
    An AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.
    
    
    (dict) --A reference to the IAM managed policy that is passed as a session policy for a role session or a federated user session.
    
    arn (string) --The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    
    
    
    
    
    DurationSeconds (integer) -- The duration, in seconds, that the session should last. Acceptable durations for federation sessions range from 900 seconds (15 minutes) to 129,600 seconds (36 hours), with 43,200 seconds (12 hours) as the default. Sessions obtained using AWS account root user credentials are restricted to a maximum of 3,600 seconds (one hour). If the specified duration is longer than one hour, the session obtained by using root user credentials defaults to one hour.
    Tags (list) -- A list of session tags. Each session tag consists of a key name and an associated value. For more information about session tags, see Passing Session Tags in STS in the IAM User Guide .
    This parameter is optional. You can pass up to 50 session tags. The plain text session tag keys can\xe2\x80\x99t exceed 128 characters and the values can\xe2\x80\x99t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .
    
    Note
    An AWS conversion compresses the passed session policies and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plain text meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit.
    
    You can pass a session tag with the same key as a tag that is already attached to the user you are federating. When you do, session tags override a user tag with the same key.
    Tag key\xe2\x80\x93value pairs are not case sensitive, but case is preserved. This means that you cannot have separate Department and department tag keys. Assume that the role has the Department =``Marketing`` tag and you pass the department =``engineering`` session tag. Department and department are not saved as separate tags, and the session tag passed in the request takes precedence over the role tag.
    
    (dict) --You can pass custom key-value pair attributes when you assume a role or federate a user. These are called session tags. You can then use the session tags to control access to resources. For more information, see Tagging AWS STS Sessions in the IAM User Guide .
    
    Key (string) -- [REQUIRED]The key for a session tag.
    You can pass up to 50 session tags. The plain text session tag keys can\xe2\x80\x99t exceed 128 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .
    
    Value (string) -- [REQUIRED]The value for a session tag.
    You can pass up to 50 session tags. The plain text session tag values can\xe2\x80\x99t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide .
    
    
    
    
    
    
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

def get_session_token(DurationSeconds=None, SerialNumber=None, TokenCode=None):
    """
    Returns a set of temporary credentials for an AWS account or IAM user. The credentials consist of an access key ID, a secret access key, and a security token. Typically, you use GetSessionToken if you want to use MFA to protect programmatic calls to specific AWS API operations like Amazon EC2 StopInstances . MFA-enabled IAM users would need to call GetSessionToken and submit an MFA code that is associated with their MFA device. Using the temporary security credentials that are returned from the call, IAM users can then make programmatic calls to API operations that require MFA authentication. If you do not supply a correct MFA code, then the API returns an access denied error. For a comparison of GetSessionToken with the other API operations that produce temporary credentials, see Requesting Temporary Security Credentials and Comparing the AWS STS API operations in the IAM User Guide .
    The GetSessionToken operation must be called by using the long-term AWS security credentials of the AWS account root user or an IAM user. Credentials that are created by IAM users are valid for the duration that you specify. This duration can range from 900 seconds (15 minutes) up to a maximum of 129,600 seconds (36 hours), with a default of 43,200 seconds (12 hours). Credentials based on account credentials can range from 900 seconds (15 minutes) up to 3,600 seconds (1 hour), with a default of 1 hour.
    The temporary security credentials created by GetSessionToken can be used to make API calls to any AWS service with the following exceptions:
    The credentials that are returned by GetSessionToken are based on permissions associated with the user whose credentials were used to call the operation. If GetSessionToken is called using AWS account root user credentials, the temporary credentials have root user permissions. Similarly, if GetSessionToken is called using the credentials of an IAM user, the temporary credentials have the same permissions as the IAM user.
    For more information about using GetSessionToken to create temporary credentials, go to Temporary Credentials for Users in Untrusted Environments in the IAM User Guide .
    See also: AWS API Documentation
    
    Exceptions
    Examples
    Expected Output:
    
    :example: response = client.get_session_token(
        DurationSeconds=123,
        SerialNumber='string',
        TokenCode='string'
    )
    
    
    :type DurationSeconds: integer
    :param DurationSeconds: The duration, in seconds, that the credentials should remain valid. Acceptable durations for IAM user sessions range from 900 seconds (15 minutes) to 129,600 seconds (36 hours), with 43,200 seconds (12 hours) as the default. Sessions for AWS account owners are restricted to a maximum of 3,600 seconds (one hour). If the duration is longer than one hour, the session for AWS account owners defaults to one hour.

    :type SerialNumber: string
    :param SerialNumber: The identification number of the MFA device that is associated with the IAM user who is making the GetSessionToken call. Specify this value if the IAM user has a policy that requires MFA authentication. The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user ). You can find the device for an IAM user by going to the AWS Management Console and viewing the user\'s security credentials.\nThe regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-\n

    :type TokenCode: string
    :param TokenCode: The value provided by the MFA device, if MFA is required. If any policy requires the IAM user to submit an MFA code, specify this value. If MFA authentication is required, the user must provide a code when requesting a set of temporary security credentials. A user who fails to provide the code receives an 'access denied' response when requesting resources that require MFA authentication.\nThe format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Credentials': {
        'AccessKeyId': 'string',
        'SecretAccessKey': 'string',
        'SessionToken': 'string',
        'Expiration': datetime(2015, 1, 1)
    }
}


Response Structure

(dict) --
Contains the response to a successful  GetSessionToken request, including temporary AWS credentials that can be used to make AWS requests.

Credentials (dict) --
The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.

Note
The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.


AccessKeyId (string) --
The access key ID that identifies the temporary security credentials.

SecretAccessKey (string) --
The secret access key that can be used to sign requests.

SessionToken (string) --
The token that users must pass to the service API to use the temporary credentials.

Expiration (datetime) --
The date on which the current credentials expire.









Exceptions

STS.Client.exceptions.RegionDisabledException

Examples
response = client.get_session_token(
    DurationSeconds=3600,
    SerialNumber='YourMFASerialNumber',
    TokenCode='123456',
)

print(response)


Expected Output:
{
    'Credentials': {
        'AccessKeyId': 'AKIAIOSFODNN7EXAMPLE',
        'Expiration': datetime(2011, 7, 11, 19, 55, 29, 0, 192, 0),
        'SecretAccessKey': 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY',
        'SessionToken': 'AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/LTo6UDdyJwOOvEVPvLXCrrrUtdnniCEXAMPLE/IvU1dYUg2RVAJBanLiHb4IgRmpRV3zrkuWJOgQs8IZZaIv2BXIa2R4OlgkBN9bkUDNCJiBeb/AXlzBBko7b15fjrBs2+cTQtpZ3CYWFXG8C5zqx37wnOE49mRl/+OtkIKGO7fAE',
    },
    'ResponseMetadata': {
        '...': '...',
    },
}



    :return: {
        'Credentials': {
            'AccessKeyId': 'string',
            'SecretAccessKey': 'string',
            'SessionToken': 'string',
            'Expiration': datetime(2015, 1, 1)
        }
    }
    
    
    :returns: 
    DurationSeconds (integer) -- The duration, in seconds, that the credentials should remain valid. Acceptable durations for IAM user sessions range from 900 seconds (15 minutes) to 129,600 seconds (36 hours), with 43,200 seconds (12 hours) as the default. Sessions for AWS account owners are restricted to a maximum of 3,600 seconds (one hour). If the duration is longer than one hour, the session for AWS account owners defaults to one hour.
    SerialNumber (string) -- The identification number of the MFA device that is associated with the IAM user who is making the GetSessionToken call. Specify this value if the IAM user has a policy that requires MFA authentication. The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user ). You can find the device for an IAM user by going to the AWS Management Console and viewing the user\'s security credentials.
    The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-
    
    TokenCode (string) -- The value provided by the MFA device, if MFA is required. If any policy requires the IAM user to submit an MFA code, specify this value. If MFA authentication is required, the user must provide a code when requesting a set of temporary security credentials. A user who fails to provide the code receives an "access denied" response when requesting resources that require MFA authentication.
    The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.
    
    
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

