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


def create_file_system(CreationToken=None, PerformanceMode=None):
    """
    :param CreationToken: [REQUIRED]
            String of up to 64 ASCII characters. Amazon EFS uses this to ensure idempotent creation.
            
    :type CreationToken: string
    :param PerformanceMode: The PerformanceMode of the file system. We recommend generalPurpose performance mode for most file systems. File systems using the maxIO performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. This can't be changed after the file system has been created.
    :type PerformanceMode: string
    """
    pass


def create_mount_target(FileSystemId=None, SubnetId=None, IpAddress=None, SecurityGroups=None):
    """
    :param FileSystemId: [REQUIRED]
            ID of the file system for which to create the mount target.
            
    :type FileSystemId: string
    :param SubnetId: [REQUIRED]
            ID of the subnet to add the mount target in.
            
    :type SubnetId: string
    :param IpAddress: Valid IPv4 address within the address range of the specified subnet.
    :type IpAddress: string
    :param SecurityGroups: Up to five VPC security group IDs, of the form sg-xxxxxxxx . These must be for the same VPC as subnet specified.
            (string) --
            
    :type SecurityGroups: list
    """
    pass


def create_tags(FileSystemId=None, Tags=None):
    """
    :param FileSystemId: [REQUIRED]
            ID of the file system whose tags you want to modify (String). This operation modifies the tags only, not the file system.
            
    :type FileSystemId: string
    :param Tags: [REQUIRED]
            Array of Tag objects to add. Each Tag object is a key-value pair.
            (dict) --A tag is a key-value pair. Allowed characters: letters, whitespace, and numbers, representable in UTF-8, and the following characters:+ - = . _ : /
            Key (string) -- [REQUIRED]Tag key (String). The key can't start with aws: .
            Value (string) -- [REQUIRED]Value of the tag key.
            
            
    :type Tags: list
    """
    pass


def delete_file_system(FileSystemId=None):
    """
    :param FileSystemId: [REQUIRED]
            ID of the file system you want to delete.
            ReturnsNone
            
    :type FileSystemId: string
    """
    pass


def delete_mount_target(MountTargetId=None):
    """
    :param MountTargetId: [REQUIRED]
            ID of the mount target to delete (String).
            ReturnsNone
            
    :type MountTargetId: string
    """
    pass


def delete_tags(FileSystemId=None, TagKeys=None):
    """
    :param FileSystemId: [REQUIRED]
            ID of the file system whose tags you want to delete (String).
            
    :type FileSystemId: string
    :param TagKeys: [REQUIRED]
            List of tag keys to delete.
            (string) --
            
    :type TagKeys: list
    """
    pass


def describe_file_systems(MaxItems=None, Marker=None, CreationToken=None, FileSystemId=None):
    """
    :param MaxItems: (Optional) Specifies the maximum number of file systems to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon EFS returns is the minimum of the MaxItems parameter specified in the request and the service's internal maximum number of items per page.
    :type MaxItems: integer
    :param Marker: (Optional) Opaque pagination token returned from a previous DescribeFileSystems operation (String). If present, specifies to continue the list from where the returning call had left off.
    :type Marker: string
    :param CreationToken: (Optional) Restricts the list to the file system with this creation token (String). You specify a creation token when you create an Amazon EFS file system.
    :type CreationToken: string
    :param FileSystemId: (Optional) ID of the file system whose description you want to retrieve (String).
    :type FileSystemId: string
    """
    pass


def describe_mount_target_security_groups(MountTargetId=None):
    """
    :param MountTargetId: [REQUIRED]
            ID of the mount target whose security groups you want to retrieve.
            Return typedict
            ReturnsResponse Syntax{
              'SecurityGroups': [
                'string',
              ]
            }
            Response Structure
            (dict) --
            SecurityGroups (list) --Array of security groups.
            (string) --
            
            
    :type MountTargetId: string
    """
    pass


def describe_mount_targets(MaxItems=None, Marker=None, FileSystemId=None, MountTargetId=None):
    """
    :param MaxItems: (Optional) Maximum number of mount targets to return in the response. It must be an integer with a value greater than zero.
    :type MaxItems: integer
    :param Marker: (Optional) Opaque pagination token returned from a previous DescribeMountTargets operation (String). If present, it specifies to continue the list from where the previous returning call left off.
    :type Marker: string
    :param FileSystemId: (Optional) ID of the file system whose mount targets you want to list (String). It must be included in your request if MountTargetId is not included.
    :type FileSystemId: string
    :param MountTargetId: (Optional) ID of the mount target that you want to have described (String). It must be included in your request if FileSystemId is not included.
    :type MountTargetId: string
    """
    pass


def describe_tags(MaxItems=None, Marker=None, FileSystemId=None):
    """
    :param MaxItems: (Optional) Maximum number of file system tags to return in the response. It must be an integer with a value greater than zero.
    :type MaxItems: integer
    :param Marker: (Optional) Opaque pagination token returned from a previous DescribeTags operation (String). If present, it specifies to continue the list from where the previous call left off.
    :type Marker: string
    :param FileSystemId: [REQUIRED]
            ID of the file system whose tag set you want to retrieve.
            
    :type FileSystemId: string
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


def modify_mount_target_security_groups(MountTargetId=None, SecurityGroups=None):
    """
    :param MountTargetId: [REQUIRED]
            ID of the mount target whose security groups you want to modify.
            
    :type MountTargetId: string
    :param SecurityGroups: Array of up to five VPC security group IDs.
            (string) --
            
    :type SecurityGroups: list
    """
    pass
