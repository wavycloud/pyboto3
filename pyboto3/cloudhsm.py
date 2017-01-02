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

def add_tags_to_resource(ResourceArn=None, TagList=None):
    """
    Adds or overwrites one or more tags for the specified AWS CloudHSM resource.
    Each tag consists of a key and a value. Tag keys must be unique to each resource.
    See also: AWS API Documentation
    
    
    :example: response = client.add_tags_to_resource(
        ResourceArn='string',
        TagList=[
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS CloudHSM resource to tag.
            

    :type TagList: list
    :param TagList: [REQUIRED]
            One or more tags.
            (dict) --A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.
            Key (string) -- [REQUIRED]The key of the tag.
            Value (string) -- [REQUIRED]The value of the tag.
            
            

    :rtype: dict
    :return: {
        'Status': 'string'
    }
    
    
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

def create_hapg(Label=None):
    """
    Creates a high-availability partition group. A high-availability partition group is a group of partitions that spans multiple physical HSMs.
    See also: AWS API Documentation
    
    
    :example: response = client.create_hapg(
        Label='string'
    )
    
    
    :type Label: string
    :param Label: [REQUIRED]
            The label of the new high-availability partition group.
            

    :rtype: dict
    :return: {
        'HapgArn': 'string'
    }
    
    
    """
    pass

def create_hsm(SubnetId=None, SshKey=None, EniIp=None, IamRoleArn=None, ExternalId=None, SubscriptionType=None, ClientToken=None, SyslogIp=None):
    """
    Creates an uninitialized HSM instance.
    There is an upfront fee charged for each HSM instance that you create with the  CreateHsm operation. If you accidentally provision an HSM and want to request a refund, delete the instance using the  DeleteHsm operation, go to the AWS Support Center , create a new case, and select Account and Billing Support .
    See also: AWS API Documentation
    
    
    :example: response = client.create_hsm(
        SubnetId='string',
        SshKey='string',
        EniIp='string',
        IamRoleArn='string',
        ExternalId='string',
        SubscriptionType='PRODUCTION',
        ClientToken='string',
        SyslogIp='string'
    )
    
    
    :type SubnetId: string
    :param SubnetId: [REQUIRED]
            The identifier of the subnet in your VPC in which to place the HSM.
            

    :type SshKey: string
    :param SshKey: [REQUIRED]
            The SSH public key to install on the HSM.
            

    :type EniIp: string
    :param EniIp: The IP address to assign to the HSM's ENI.
            If an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the subnet.
            

    :type IamRoleArn: string
    :param IamRoleArn: [REQUIRED]
            The ARN of an IAM role to enable the AWS CloudHSM service to allocate an ENI on your behalf.
            

    :type ExternalId: string
    :param ExternalId: The external ID from IamRoleArn , if present.

    :type SubscriptionType: string
    :param SubscriptionType: [REQUIRED]
            Specifies the type of subscription for the HSM.
            PRODUCTION - The HSM is being used in a production environment.
            TRIAL - The HSM is being used in a product trial.
            

    :type ClientToken: string
    :param ClientToken: A user-defined token to ensure idempotence. Subsequent calls to this operation with the same token will be ignored.

    :type SyslogIp: string
    :param SyslogIp: The IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.

    :rtype: dict
    :return: {
        'HsmArn': 'string'
    }
    
    
    """
    pass

def create_luna_client(Label=None, Certificate=None):
    """
    Creates an HSM client.
    See also: AWS API Documentation
    
    
    :example: response = client.create_luna_client(
        Label='string',
        Certificate='string'
    )
    
    
    :type Label: string
    :param Label: The label for the client.

    :type Certificate: string
    :param Certificate: [REQUIRED]
            The contents of a Base64-Encoded X.509 v3 certificate to be installed on the HSMs used by this client.
            

    :rtype: dict
    :return: {
        'ClientArn': 'string'
    }
    
    
    """
    pass

def delete_hapg(HapgArn=None):
    """
    Deletes a high-availability partition group.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_hapg(
        HapgArn='string'
    )
    
    
    :type HapgArn: string
    :param HapgArn: [REQUIRED]
            The ARN of the high-availability partition group to delete.
            

    :rtype: dict
    :return: {
        'Status': 'string'
    }
    
    
    """
    pass

def delete_hsm(HsmArn=None):
    """
    Deletes an HSM. After completion, this operation cannot be undone and your key material cannot be recovered.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_hsm(
        HsmArn='string'
    )
    
    
    :type HsmArn: string
    :param HsmArn: [REQUIRED]
            The ARN of the HSM to delete.
            

    :rtype: dict
    :return: {
        'Status': 'string'
    }
    
    
    """
    pass

def delete_luna_client(ClientArn=None):
    """
    Deletes a client.
    See also: AWS API Documentation
    
    
    :example: response = client.delete_luna_client(
        ClientArn='string'
    )
    
    
    :type ClientArn: string
    :param ClientArn: [REQUIRED]
            The ARN of the client to delete.
            

    :rtype: dict
    :return: {
        'Status': 'string'
    }
    
    
    """
    pass

def describe_hapg(HapgArn=None):
    """
    Retrieves information about a high-availability partition group.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_hapg(
        HapgArn='string'
    )
    
    
    :type HapgArn: string
    :param HapgArn: [REQUIRED]
            The ARN of the high-availability partition group to describe.
            

    :rtype: dict
    :return: {
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
    
    
    """
    pass

def describe_hsm(HsmArn=None, HsmSerialNumber=None):
    """
    Retrieves information about an HSM. You can identify the HSM by its ARN or its serial number.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_hsm(
        HsmArn='string',
        HsmSerialNumber='string'
    )
    
    
    :type HsmArn: string
    :param HsmArn: The ARN of the HSM. Either the HsmArn or the SerialNumber parameter must be specified.

    :type HsmSerialNumber: string
    :param HsmSerialNumber: The serial number of the HSM. Either the HsmArn or the HsmSerialNumber parameter must be specified.

    :rtype: dict
    :return: {
        'HsmArn': 'string',
        'Status': 'PENDING'|'RUNNING'|'UPDATING'|'SUSPENDED'|'TERMINATING'|'TERMINATED'|'DEGRADED',
        'StatusDetails': 'string',
        'AvailabilityZone': 'string',
        'EniId': 'string',
        'EniIp': 'string',
        'SubscriptionType': 'PRODUCTION',
        'SubscriptionStartDate': 'string',
        'SubscriptionEndDate': 'string',
        'VpcId': 'string',
        'SubnetId': 'string',
        'IamRoleArn': 'string',
        'SerialNumber': 'string',
        'VendorName': 'string',
        'HsmType': 'string',
        'SoftwareVersion': 'string',
        'SshPublicKey': 'string',
        'SshKeyLastUpdated': 'string',
        'ServerCertUri': 'string',
        'ServerCertLastUpdated': 'string',
        'Partitions': [
            'string',
        ]
    }
    
    
    :returns: 
    PRODUCTION - The HSM is being used in a production environment.
    TRIAL - The HSM is being used in a product trial.
    
    """
    pass

def describe_luna_client(ClientArn=None, CertificateFingerprint=None):
    """
    Retrieves information about an HSM client.
    See also: AWS API Documentation
    
    
    :example: response = client.describe_luna_client(
        ClientArn='string',
        CertificateFingerprint='string'
    )
    
    
    :type ClientArn: string
    :param ClientArn: The ARN of the client.

    :type CertificateFingerprint: string
    :param CertificateFingerprint: The certificate fingerprint.

    :rtype: dict
    :return: {
        'ClientArn': 'string',
        'Certificate': 'string',
        'CertificateFingerprint': 'string',
        'LastModifiedTimestamp': 'string',
        'Label': 'string'
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

def get_config(ClientArn=None, ClientVersion=None, HapgList=None):
    """
    Gets the configuration files necessary to connect to all high availability partition groups the client is associated with.
    See also: AWS API Documentation
    
    
    :example: response = client.get_config(
        ClientArn='string',
        ClientVersion='5.1'|'5.3',
        HapgList=[
            'string',
        ]
    )
    
    
    :type ClientArn: string
    :param ClientArn: [REQUIRED]
            The ARN of the client.
            

    :type ClientVersion: string
    :param ClientVersion: [REQUIRED]
            The client version.
            

    :type HapgList: list
    :param HapgList: [REQUIRED]
            A list of ARNs that identify the high-availability partition groups that are associated with the client.
            (string) --
            

    :rtype: dict
    :return: {
        'ConfigType': 'string',
        'ConfigFile': 'string',
        'ConfigCred': 'string'
    }
    
    
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

def get_waiter():
    """
    
    """
    pass

def list_available_zones():
    """
    Lists the Availability Zones that have available AWS CloudHSM capacity.
    See also: AWS API Documentation
    
    
    :example: response = client.list_available_zones()
    
    
    :rtype: dict
    :return: {
        'AZList': [
            'string',
        ]
    }
    
    
    """
    pass

def list_hapgs(NextToken=None):
    """
    Lists the high-availability partition groups for the account.
    This operation supports pagination with the use of the NextToken member. If more results are available, the NextToken member of the response contains a token that you pass in the next call to  ListHapgs to retrieve the next set of items.
    See also: AWS API Documentation
    
    
    :example: response = client.list_hapgs(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The NextToken value from a previous call to ListHapgs . Pass null if this is the first call.

    :rtype: dict
    :return: {
        'HapgList': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_hsms(NextToken=None):
    """
    Retrieves the identifiers of all of the HSMs provisioned for the current customer.
    This operation supports pagination with the use of the NextToken member. If more results are available, the NextToken member of the response contains a token that you pass in the next call to  ListHsms to retrieve the next set of items.
    See also: AWS API Documentation
    
    
    :example: response = client.list_hsms(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The NextToken value from a previous call to ListHsms . Pass null if this is the first call.

    :rtype: dict
    :return: {
        'HsmList': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_luna_clients(NextToken=None):
    """
    Lists all of the clients.
    This operation supports pagination with the use of the NextToken member. If more results are available, the NextToken member of the response contains a token that you pass in the next call to  ListLunaClients to retrieve the next set of items.
    See also: AWS API Documentation
    
    
    :example: response = client.list_luna_clients(
        NextToken='string'
    )
    
    
    :type NextToken: string
    :param NextToken: The NextToken value from a previous call to ListLunaClients . Pass null if this is the first call.

    :rtype: dict
    :return: {
        'ClientList': [
            'string',
        ],
        'NextToken': 'string'
    }
    
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Returns a list of all tags for the specified AWS CloudHSM resource.
    See also: AWS API Documentation
    
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
            

    :rtype: dict
    :return: {
        'TagList': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ]
    }
    
    
    """
    pass

def modify_hapg(HapgArn=None, Label=None, PartitionSerialList=None):
    """
    Modifies an existing high-availability partition group.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_hapg(
        HapgArn='string',
        Label='string',
        PartitionSerialList=[
            'string',
        ]
    )
    
    
    :type HapgArn: string
    :param HapgArn: [REQUIRED]
            The ARN of the high-availability partition group to modify.
            

    :type Label: string
    :param Label: The new label for the high-availability partition group.

    :type PartitionSerialList: list
    :param PartitionSerialList: The list of partition serial numbers to make members of the high-availability partition group.
            (string) --
            

    :rtype: dict
    :return: {
        'HapgArn': 'string'
    }
    
    
    """
    pass

def modify_hsm(HsmArn=None, SubnetId=None, EniIp=None, IamRoleArn=None, ExternalId=None, SyslogIp=None):
    """
    Modifies an HSM.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_hsm(
        HsmArn='string',
        SubnetId='string',
        EniIp='string',
        IamRoleArn='string',
        ExternalId='string',
        SyslogIp='string'
    )
    
    
    :type HsmArn: string
    :param HsmArn: [REQUIRED]
            The ARN of the HSM to modify.
            

    :type SubnetId: string
    :param SubnetId: The new identifier of the subnet that the HSM is in. The new subnet must be in the same Availability Zone as the current subnet.

    :type EniIp: string
    :param EniIp: The new IP address for the elastic network interface (ENI) attached to the HSM.
            If the HSM is moved to a different subnet, and an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the new subnet.
            

    :type IamRoleArn: string
    :param IamRoleArn: The new IAM role ARN.

    :type ExternalId: string
    :param ExternalId: The new external ID.

    :type SyslogIp: string
    :param SyslogIp: The new IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.

    :rtype: dict
    :return: {
        'HsmArn': 'string'
    }
    
    
    """
    pass

def modify_luna_client(ClientArn=None, Certificate=None):
    """
    Modifies the certificate used by the client.
    This action can potentially start a workflow to install the new certificate on the client's HSMs.
    See also: AWS API Documentation
    
    
    :example: response = client.modify_luna_client(
        ClientArn='string',
        Certificate='string'
    )
    
    
    :type ClientArn: string
    :param ClientArn: [REQUIRED]
            The ARN of the client.
            

    :type Certificate: string
    :param Certificate: [REQUIRED]
            The new certificate for the client.
            

    :rtype: dict
    :return: {
        'ClientArn': 'string'
    }
    
    
    """
    pass

def remove_tags_from_resource(ResourceArn=None, TagKeyList=None):
    """
    Removes one or more tags from the specified AWS CloudHSM resource.
    To remove a tag, specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use  AddTagsToResource .
    See also: AWS API Documentation
    
    
    :example: response = client.remove_tags_from_resource(
        ResourceArn='string',
        TagKeyList=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]
            The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
            

    :type TagKeyList: list
    :param TagKeyList: [REQUIRED]
            The tag key or keys to remove.
            Specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use AddTagsToResource .
            (string) --
            

    :rtype: dict
    :return: {
        'Status': 'string'
    }
    
    
    """
    pass

