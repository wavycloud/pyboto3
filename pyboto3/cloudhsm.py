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


def add_tags_to_resource(ResourceArn=None, TagList=None):
    """
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS CloudHSM resource to tag.
            
    :type ResourceArn: string
    :param TagList: [REQUIRED]
            One or more tags.
            (dict) --A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) -- [REQUIRED]The value of the tag.
            
            
    :type TagList: list
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


def create_hapg(Label=None):
    """
    :param Label: [REQUIRED]
            The label of the new high-availability partition group.
            Return typedict
            ReturnsResponse Syntax{
              'HapgArn': 'string'
            }
            Response Structure
            (dict) --Contains the output of the CreateHAPartitionGroup action.
            HapgArn (string) --The ARN of the high-availability partition group.
            
            
    :type Label: string
    """
    pass


def create_hsm(SubnetId=None, SshKey=None, EniIp=None, IamRoleArn=None, ExternalId=None, SubscriptionType=None,
               ClientToken=None, SyslogIp=None):
    """
    :param SubnetId: [REQUIRED]
            The identifier of the subnet in your VPC in which to place the HSM.
            
    :type SubnetId: string
    :param SshKey: [REQUIRED]
            The SSH public key to install on the HSM.
            
    :type SshKey: string
    :param EniIp: The IP address to assign to the HSM's ENI.
            If an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the subnet.
            
    :type EniIp: string
    :param IamRoleArn: [REQUIRED]
            The ARN of an IAM role to enable the AWS CloudHSM service to allocate an ENI on your behalf.
            
    :type IamRoleArn: string
    :param ExternalId: The external ID from IamRoleArn , if present.
    :type ExternalId: string
    :param SubscriptionType: [REQUIRED]
            Specifies the type of subscription for the HSM.
            PRODUCTION - The HSM is being used in a production environment.
            TRIAL - The HSM is being used in a product trial.
            
    :type SubscriptionType: string
    :param ClientToken: A user-defined token to ensure idempotence. Subsequent calls to this operation with the same token will be ignored.
    :type ClientToken: string
    :param SyslogIp: The IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.
    :type SyslogIp: string
    """
    pass


def create_luna_client(Label=None, Certificate=None):
    """
    :param Label: The label for the client.
    :type Label: string
    :param Certificate: [REQUIRED]
            The contents of a Base64-Encoded X.509 v3 certificate to be installed on the HSMs used by this client.
            
    :type Certificate: string
    """
    pass


def delete_hapg(HapgArn=None):
    """
    :param HapgArn: [REQUIRED]
            The ARN of the high-availability partition group to delete.
            Return typedict
            ReturnsResponse Syntax{
              'Status': 'string'
            }
            Response Structure
            (dict) --Contains the output of the DeleteHapg action.
            Status (string) --The status of the action.
            
            
    :type HapgArn: string
    """
    pass


def delete_hsm(HsmArn=None):
    """
    :param HsmArn: [REQUIRED]
            The ARN of the HSM to delete.
            Return typedict
            ReturnsResponse Syntax{
              'Status': 'string'
            }
            Response Structure
            (dict) --Contains the output of the DeleteHsm operation.
            Status (string) --The status of the operation.
            
            
    :type HsmArn: string
    """
    pass


def delete_luna_client(ClientArn=None):
    """
    :param ClientArn: [REQUIRED]
            The ARN of the client to delete.
            Return typedict
            ReturnsResponse Syntax{
              'Status': 'string'
            }
            Response Structure
            (dict) --
            Status (string) --The status of the action.
            
            
    :type ClientArn: string
    """
    pass


def describe_hapg(HapgArn=None):
    """
    :param HapgArn: [REQUIRED]
            The ARN of the high-availability partition group to describe.
            Return typedict
            ReturnsResponse Syntax{
              'HapgArn': 'string',
              'HapgSerial': 'string',
              'HsmsLastActionFailed': [
                'string',
              ],
              'HsmsPendingDeletion': [
                'string',
              ],
              'HsmsPendingRegistration': [
                'string',
              ],
              'Label': 'string',
              'LastModifiedTimestamp': 'string',
              'PartitionSerialList': [
                'string',
              ],
              'State': 'READY'|'UPDATING'|'DEGRADED'
            }
            Response Structure
            (dict) --Contains the output of the DescribeHapg action.
            HapgArn (string) --The ARN of the high-availability partition group.
            HapgSerial (string) --The serial number of the high-availability partition group.
            HsmsLastActionFailed (list) --Contains a list of ARNs that identify the HSMs.
            (string) --An ARN that identifies an HSM.
            HsmsPendingDeletion (list) --Contains a list of ARNs that identify the HSMs.
            (string) --An ARN that identifies an HSM.
            HsmsPendingRegistration (list) --Contains a list of ARNs that identify the HSMs.
            (string) --An ARN that identifies an HSM.
            Label (string) --The label for the high-availability partition group.
            LastModifiedTimestamp (string) --The date and time the high-availability partition group was last modified.
            PartitionSerialList (list) --The list of partition serial numbers that belong to the high-availability partition group.
            (string) --
            State (string) --The state of the high-availability partition group.
            
            
    :type HapgArn: string
    """
    pass


def describe_hsm(HsmArn=None, HsmSerialNumber=None):
    """
    :param HsmArn: The ARN of the HSM. Either the HsmArn or the SerialNumber parameter must be specified.
    :type HsmArn: string
    :param HsmSerialNumber: The serial number of the HSM. Either the HsmArn or the HsmSerialNumber parameter must be specified.
    :type HsmSerialNumber: string
    """
    pass


def describe_luna_client(ClientArn=None, CertificateFingerprint=None):
    """
    :param ClientArn: The ARN of the client.
    :type ClientArn: string
    :param CertificateFingerprint: The certificate fingerprint.
    :type CertificateFingerprint: string
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


def get_config(ClientArn=None, ClientVersion=None, HapgList=None):
    """
    :param ClientArn: [REQUIRED]
            The ARN of the client.
            
    :type ClientArn: string
    :param ClientVersion: [REQUIRED]
            The client version.
            
    :type ClientVersion: string
    :param HapgList: [REQUIRED]
            A list of ARNs that identify the high-availability partition groups that are associated with the client.
            (string) --
            
    :type HapgList: list
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


def list_available_zones():
    """
    """
    pass


def list_hapgs(NextToken=None):
    """
    :param NextToken: The NextToken value from a previous call to ListHapgs . Pass null if this is the first call.
            Return typedict
            ReturnsResponse Syntax{
              'HapgList': [
                'string',
              ],
              'NextToken': 'string'
            }
            Response Structure
            (dict) --
            HapgList (list) --The list of high-availability partition groups.
            (string) --
            NextToken (string) --If not null, more results are available. Pass this value to ListHapgs to retrieve the next set of items.
            
            
    :type NextToken: string
    """
    pass


def list_hsms(NextToken=None):
    """
    :param NextToken: The NextToken value from a previous call to ListHsms . Pass null if this is the first call.
            Return typedict
            ReturnsResponse Syntax{
              'HsmList': [
                'string',
              ],
              'NextToken': 'string'
            }
            Response Structure
            (dict) --Contains the output of the ListHsms operation.
            HsmList (list) --The list of ARNs that identify the HSMs.
            (string) --An ARN that identifies an HSM.
            NextToken (string) --If not null, more results are available. Pass this value to ListHsms to retrieve the next set of items.
            
            
    :type NextToken: string
    """
    pass


def list_luna_clients(NextToken=None):
    """
    :param NextToken: The NextToken value from a previous call to ListLunaClients . Pass null if this is the first call.
            Return typedict
            ReturnsResponse Syntax{
              'ClientList': [
                'string',
              ],
              'NextToken': 'string'
            }
            Response Structure
            (dict) --
            ClientList (list) --The list of clients.
            (string) --
            NextToken (string) --If not null, more results are available. Pass this to ListLunaClients to retrieve the next set of items.
            
            
    :type NextToken: string
    """
    pass


def list_tags_for_resource(ResourceArn=None):
    """
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
            Return typedict
            ReturnsResponse Syntax{
              'TagList': [
                {
                  'Key': 'string',
                  'Value': 'string'
                },
              ]
            }
            Response Structure
            (dict) --
            TagList (list) --One or more tags.
            (dict) --A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.
            Key (string) --The key of the tag.
            Value (string) --The value of the tag.
            
            
            
    :type ResourceArn: string
    """
    pass


def modify_hapg(HapgArn=None, Label=None, PartitionSerialList=None):
    """
    :param HapgArn: [REQUIRED]
            The ARN of the high-availability partition group to modify.
            
    :type HapgArn: string
    :param Label: The new label for the high-availability partition group.
    :type Label: string
    :param PartitionSerialList: The list of partition serial numbers to make members of the high-availability partition group.
            (string) --
            
    :type PartitionSerialList: list
    """
    pass


def modify_hsm(HsmArn=None, SubnetId=None, EniIp=None, IamRoleArn=None, ExternalId=None, SyslogIp=None):
    """
    :param HsmArn: [REQUIRED]
            The ARN of the HSM to modify.
            
    :type HsmArn: string
    :param SubnetId: The new identifier of the subnet that the HSM is in. The new subnet must be in the same Availability Zone as the current subnet.
    :type SubnetId: string
    :param EniIp: The new IP address for the elastic network interface (ENI) attached to the HSM.
            If the HSM is moved to a different subnet, and an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the new subnet.
            
    :type EniIp: string
    :param IamRoleArn: The new IAM role ARN.
    :type IamRoleArn: string
    :param ExternalId: The new external ID.
    :type ExternalId: string
    :param SyslogIp: The new IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.
    :type SyslogIp: string
    """
    pass


def modify_luna_client(ClientArn=None, Certificate=None):
    """
    :param ClientArn: [REQUIRED]
            The ARN of the client.
            
    :type ClientArn: string
    :param Certificate: [REQUIRED]
            The new certificate for the client.
            
    :type Certificate: string
    """
    pass


def remove_tags_from_resource(ResourceArn=None, TagKeyList=None):
    """
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
            
    :type ResourceArn: string
    :param TagKeyList: [REQUIRED]
            The tag key or keys to remove.
            Specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use AddTagsToResource .
            (string) --
            
    :type TagKeyList: list
    """
    pass
