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

def cancel_journal_kinesis_stream(LedgerName=None, StreamId=None):
    """
    Ends a given Amazon QLDB journal stream. Before a stream can be canceled, its current status must be ACTIVE .
    You can\'t restart a stream after you cancel it. Canceled QLDB stream resources are subject to a 7-day retention period, so they are automatically deleted after this limit expires.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_journal_kinesis_stream(
        LedgerName='string',
        StreamId='string'
    )
    
    
    :type LedgerName: string
    :param LedgerName: [REQUIRED]\nThe name of the ledger.\n

    :type StreamId: string
    :param StreamId: [REQUIRED]\nThe unique ID that QLDB assigns to each QLDB journal stream.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamId': 'string'
}


Response Structure

(dict) --

StreamId (string) --
The unique ID that QLDB assigns to each QLDB journal stream.







Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException
QLDB.Client.exceptions.ResourcePreconditionNotMetException


    :return: {
        'StreamId': 'string'
    }
    
    
    :returns: 
    QLDB.Client.exceptions.InvalidParameterException
    QLDB.Client.exceptions.ResourceNotFoundException
    QLDB.Client.exceptions.ResourcePreconditionNotMetException
    
    """
    pass

def create_ledger(Name=None, Tags=None, PermissionsMode=None, DeletionProtection=None):
    """
    Creates a new ledger in your AWS account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_ledger(
        Name='string',
        Tags={
            'string': 'string'
        },
        PermissionsMode='ALLOW_ALL',
        DeletionProtection=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the ledger that you want to create. The name must be unique among all of your ledgers in the current AWS Region.\n

    :type Tags: dict
    :param Tags: The key-value pairs to add as tags to the ledger that you want to create. Tag keys are case sensitive. Tag values are case sensitive and can be null.\n\n(string) --\n(string) --\n\n\n\n

    :type PermissionsMode: string
    :param PermissionsMode: [REQUIRED]\nThe permissions mode to assign to the ledger that you want to create.\n

    :type DeletionProtection: boolean
    :param DeletionProtection: The flag that prevents a ledger from being deleted by any user. If not provided on ledger creation, this feature is enabled (true ) by default.\nIf deletion protection is enabled, you must first disable it before you can delete the ledger using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling the UpdateLedger operation to set the flag to false . The QLDB console disables deletion protection for you when you use it to delete a ledger.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'Arn': 'string',
    'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
    'CreationDateTime': datetime(2015, 1, 1),
    'DeletionProtection': True|False
}


Response Structure

(dict) --

Name (string) --
The name of the ledger.

Arn (string) --
The Amazon Resource Name (ARN) for the ledger.

State (string) --
The current status of the ledger.

CreationDateTime (datetime) --
The date and time, in epoch time format, when the ledger was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

DeletionProtection (boolean) --
The flag that prevents a ledger from being deleted by any user. If not provided on ledger creation, this feature is enabled (true ) by default.
If deletion protection is enabled, you must first disable it before you can delete the ledger using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling the UpdateLedger operation to set the flag to false . The QLDB console disables deletion protection for you when you use it to delete a ledger.







Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceAlreadyExistsException
QLDB.Client.exceptions.LimitExceededException
QLDB.Client.exceptions.ResourceInUseException


    :return: {
        'Name': 'string',
        'Arn': 'string',
        'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
        'CreationDateTime': datetime(2015, 1, 1),
        'DeletionProtection': True|False
    }
    
    
    :returns: 
    QLDB.Client.exceptions.InvalidParameterException
    QLDB.Client.exceptions.ResourceAlreadyExistsException
    QLDB.Client.exceptions.LimitExceededException
    QLDB.Client.exceptions.ResourceInUseException
    
    """
    pass

def delete_ledger(Name=None):
    """
    Deletes a ledger and all of its contents. This action is irreversible.
    If deletion protection is enabled, you must first disable it before you can delete the ledger using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling the UpdateLedger operation to set the flag to false . The QLDB console disables deletion protection for you when you use it to delete a ledger.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_ledger(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the ledger that you want to delete.\n

    """
    pass

def describe_journal_kinesis_stream(LedgerName=None, StreamId=None):
    """
    Returns detailed information about a given Amazon QLDB journal stream. The output includes the Amazon Resource Name (ARN), stream name, current status, creation time, and the parameters of your original stream creation request.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_journal_kinesis_stream(
        LedgerName='string',
        StreamId='string'
    )
    
    
    :type LedgerName: string
    :param LedgerName: [REQUIRED]\nThe name of the ledger.\n

    :type StreamId: string
    :param StreamId: [REQUIRED]\nThe unique ID that QLDB assigns to each QLDB journal stream.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Stream': {
        'LedgerName': 'string',
        'CreationTime': datetime(2015, 1, 1),
        'InclusiveStartTime': datetime(2015, 1, 1),
        'ExclusiveEndTime': datetime(2015, 1, 1),
        'RoleArn': 'string',
        'StreamId': 'string',
        'Arn': 'string',
        'Status': 'ACTIVE'|'COMPLETED'|'CANCELED'|'FAILED'|'IMPAIRED',
        'KinesisConfiguration': {
            'StreamArn': 'string',
            'AggregationEnabled': True|False
        },
        'ErrorCause': 'KINESIS_STREAM_NOT_FOUND'|'IAM_PERMISSION_REVOKED',
        'StreamName': 'string'
    }
}


Response Structure

(dict) --

Stream (dict) --
Information about the QLDB journal stream returned by a DescribeJournalS3Export request.

LedgerName (string) --
The name of the ledger.

CreationTime (datetime) --
The date and time, in epoch time format, when the QLDB journal stream was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

InclusiveStartTime (datetime) --
The inclusive start date and time from which to start streaming journal data.

ExclusiveEndTime (datetime) --
The exclusive date and time that specifies when the stream ends. If this parameter is blank, the stream runs indefinitely until you cancel it.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal stream to write data records to a Kinesis Data Streams resource.

StreamId (string) --
The unique ID that QLDB assigns to each QLDB journal stream.

Arn (string) --
The Amazon Resource Name (ARN) of the QLDB journal stream.

Status (string) --
The current state of the QLDB journal stream.

KinesisConfiguration (dict) --
The configuration settings of the Amazon Kinesis Data Streams destination for your QLDB journal stream.

StreamArn (string) --
The Amazon Resource Name (ARN) of the Kinesis data stream resource.

AggregationEnabled (boolean) --
Enables QLDB to publish multiple stream records in a single Kinesis Data Streams record. To learn more, see KPL Key Concepts in the Amazon Kinesis Data Streams Developer Guide .



ErrorCause (string) --
The error message that describes the reason that a stream has a status of IMPAIRED or FAILED . This is not applicable to streams that have other status values.

StreamName (string) --
The user-defined name of the QLDB journal stream.









Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException
QLDB.Client.exceptions.ResourcePreconditionNotMetException


    :return: {
        'Stream': {
            'LedgerName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'InclusiveStartTime': datetime(2015, 1, 1),
            'ExclusiveEndTime': datetime(2015, 1, 1),
            'RoleArn': 'string',
            'StreamId': 'string',
            'Arn': 'string',
            'Status': 'ACTIVE'|'COMPLETED'|'CANCELED'|'FAILED'|'IMPAIRED',
            'KinesisConfiguration': {
                'StreamArn': 'string',
                'AggregationEnabled': True|False
            },
            'ErrorCause': 'KINESIS_STREAM_NOT_FOUND'|'IAM_PERMISSION_REVOKED',
            'StreamName': 'string'
        }
    }
    
    
    :returns: 
    QLDB.Client.exceptions.InvalidParameterException
    QLDB.Client.exceptions.ResourceNotFoundException
    QLDB.Client.exceptions.ResourcePreconditionNotMetException
    
    """
    pass

def describe_journal_s3_export(Name=None, ExportId=None):
    """
    Returns information about a journal export job, including the ledger name, export ID, when it was created, current status, and its start and end time export parameters.
    This action does not return any expired export jobs. For more information, see Export Job Expiration in the Amazon QLDB Developer Guide .
    If the export job with the given ExportId doesn\'t exist, then throws ResourceNotFoundException .
    If the ledger with the given Name doesn\'t exist, then throws ResourceNotFoundException .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_journal_s3_export(
        Name='string',
        ExportId='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the ledger.\n

    :type ExportId: string
    :param ExportId: [REQUIRED]\nThe unique ID of the journal export job that you want to describe.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ExportDescription': {
        'LedgerName': 'string',
        'ExportId': 'string',
        'ExportCreationTime': datetime(2015, 1, 1),
        'Status': 'IN_PROGRESS'|'COMPLETED'|'CANCELLED',
        'InclusiveStartTime': datetime(2015, 1, 1),
        'ExclusiveEndTime': datetime(2015, 1, 1),
        'S3ExportConfiguration': {
            'Bucket': 'string',
            'Prefix': 'string',
            'EncryptionConfiguration': {
                'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                'KmsKeyArn': 'string'
            }
        },
        'RoleArn': 'string'
    }
}


Response Structure

(dict) --

ExportDescription (dict) --
Information about the journal export job returned by a DescribeJournalS3Export request.

LedgerName (string) --
The name of the ledger.

ExportId (string) --
The unique ID of the journal export job.

ExportCreationTime (datetime) --
The date and time, in epoch time format, when the export job was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

Status (string) --
The current state of the journal export job.

InclusiveStartTime (datetime) --
The inclusive start date and time for the range of journal contents that are specified in the original export request.

ExclusiveEndTime (datetime) --
The exclusive end date and time for the range of journal contents that are specified in the original export request.

S3ExportConfiguration (dict) --
The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export job writes the journal contents.

Bucket (string) --
The Amazon S3 bucket name in which a journal export job writes the journal contents.
The bucket name must comply with the Amazon S3 bucket naming conventions. For more information, see Bucket Restrictions and Limitations in the Amazon S3 Developer Guide .

Prefix (string) --
The prefix for the Amazon S3 bucket in which a journal export job writes the journal contents.
The prefix must comply with Amazon S3 key naming rules and restrictions. For more information, see Object Key and Metadata in the Amazon S3 Developer Guide .
The following are examples of valid Prefix values:

JournalExports-ForMyLedger/Testing/
JournalExports
My:Tests/


EncryptionConfiguration (dict) --
The encryption settings that are used by a journal export job to write data in an Amazon S3 bucket.

ObjectEncryptionType (string) --
The Amazon S3 object encryption type.
To learn more about server-side encryption options in Amazon S3, see Protecting Data Using Server-Side Encryption in the Amazon S3 Developer Guide .

KmsKeyArn (string) --
The Amazon Resource Name (ARN) for a symmetric customer master key (CMK) in AWS Key Management Service (AWS KMS). Amazon QLDB does not support asymmetric CMKs.
You must provide a KmsKeyArn if you specify SSE_KMS as the ObjectEncryptionType .

KmsKeyArn is not required if you specify SSE_S3 as the ObjectEncryptionType .






RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal export job to do the following:

Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.
(Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS) for server-side encryption of your exported data.










Exceptions

QLDB.Client.exceptions.ResourceNotFoundException


    :return: {
        'ExportDescription': {
            'LedgerName': 'string',
            'ExportId': 'string',
            'ExportCreationTime': datetime(2015, 1, 1),
            'Status': 'IN_PROGRESS'|'COMPLETED'|'CANCELLED',
            'InclusiveStartTime': datetime(2015, 1, 1),
            'ExclusiveEndTime': datetime(2015, 1, 1),
            'S3ExportConfiguration': {
                'Bucket': 'string',
                'Prefix': 'string',
                'EncryptionConfiguration': {
                    'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                    'KmsKeyArn': 'string'
                }
            },
            'RoleArn': 'string'
        }
    }
    
    
    :returns: 
    JournalExports-ForMyLedger/Testing/
    JournalExports
    My:Tests/
    
    """
    pass

def describe_ledger(Name=None):
    """
    Returns information about a ledger, including its state and when it was created.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_ledger(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the ledger that you want to describe.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Name': 'string',
    'Arn': 'string',
    'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
    'CreationDateTime': datetime(2015, 1, 1),
    'DeletionProtection': True|False
}


Response Structure

(dict) --
Name (string) --The name of the ledger.

Arn (string) --The Amazon Resource Name (ARN) for the ledger.

State (string) --The current status of the ledger.

CreationDateTime (datetime) --The date and time, in epoch time format, when the ledger was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

DeletionProtection (boolean) --The flag that prevents a ledger from being deleted by any user. If not provided on ledger creation, this feature is enabled (true ) by default.
If deletion protection is enabled, you must first disable it before you can delete the ledger using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling the UpdateLedger operation to set the flag to false . The QLDB console disables deletion protection for you when you use it to delete a ledger.






Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException


    :return: {
        'Name': 'string',
        'Arn': 'string',
        'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
        'CreationDateTime': datetime(2015, 1, 1),
        'DeletionProtection': True|False
    }
    
    
    """
    pass

def export_journal_to_s3(Name=None, InclusiveStartTime=None, ExclusiveEndTime=None, S3ExportConfiguration=None, RoleArn=None):
    """
    Exports journal contents within a date and time range from a ledger into a specified Amazon Simple Storage Service (Amazon S3) bucket. The data is written as files in Amazon Ion format.
    If the ledger with the given Name doesn\'t exist, then throws ResourceNotFoundException .
    If the ledger with the given Name is in CREATING status, then throws ResourcePreconditionNotMetException .
    You can initiate up to two concurrent journal export requests for each ledger. Beyond this limit, journal export requests throw LimitExceededException .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.export_journal_to_s3(
        Name='string',
        InclusiveStartTime=datetime(2015, 1, 1),
        ExclusiveEndTime=datetime(2015, 1, 1),
        S3ExportConfiguration={
            'Bucket': 'string',
            'Prefix': 'string',
            'EncryptionConfiguration': {
                'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                'KmsKeyArn': 'string'
            }
        },
        RoleArn='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the ledger.\n

    :type InclusiveStartTime: datetime
    :param InclusiveStartTime: [REQUIRED]\nThe inclusive start date and time for the range of journal contents that you want to export.\nThe InclusiveStartTime must be in ISO 8601 date and time format and in Universal Coordinated Time (UTC). For example: 2019-06-13T21:36:34Z\nThe InclusiveStartTime must be before ExclusiveEndTime .\nIf you provide an InclusiveStartTime that is before the ledger\'s CreationDateTime , Amazon QLDB defaults it to the ledger\'s CreationDateTime .\n

    :type ExclusiveEndTime: datetime
    :param ExclusiveEndTime: [REQUIRED]\nThe exclusive end date and time for the range of journal contents that you want to export.\nThe ExclusiveEndTime must be in ISO 8601 date and time format and in Universal Coordinated Time (UTC). For example: 2019-06-13T21:36:34Z\nThe ExclusiveEndTime must be less than or equal to the current UTC date and time.\n

    :type S3ExportConfiguration: dict
    :param S3ExportConfiguration: [REQUIRED]\nThe configuration settings of the Amazon S3 bucket destination for your export request.\n\nBucket (string) -- [REQUIRED]The Amazon S3 bucket name in which a journal export job writes the journal contents.\nThe bucket name must comply with the Amazon S3 bucket naming conventions. For more information, see Bucket Restrictions and Limitations in the Amazon S3 Developer Guide .\n\nPrefix (string) -- [REQUIRED]The prefix for the Amazon S3 bucket in which a journal export job writes the journal contents.\nThe prefix must comply with Amazon S3 key naming rules and restrictions. For more information, see Object Key and Metadata in the Amazon S3 Developer Guide .\nThe following are examples of valid Prefix values:\n\nJournalExports-ForMyLedger/Testing/\nJournalExports\nMy:Tests/\n\n\nEncryptionConfiguration (dict) -- [REQUIRED]The encryption settings that are used by a journal export job to write data in an Amazon S3 bucket.\n\nObjectEncryptionType (string) -- [REQUIRED]The Amazon S3 object encryption type.\nTo learn more about server-side encryption options in Amazon S3, see Protecting Data Using Server-Side Encryption in the Amazon S3 Developer Guide .\n\nKmsKeyArn (string) --The Amazon Resource Name (ARN) for a symmetric customer master key (CMK) in AWS Key Management Service (AWS KMS). Amazon QLDB does not support asymmetric CMKs.\nYou must provide a KmsKeyArn if you specify SSE_KMS as the ObjectEncryptionType .\n\nKmsKeyArn is not required if you specify SSE_S3 as the ObjectEncryptionType .\n\n\n\n\n

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal export job to do the following:\n\nWrite objects into your Amazon Simple Storage Service (Amazon S3) bucket.\n(Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS) for server-side encryption of your exported data.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'ExportId': 'string'
}


Response Structure

(dict) --

ExportId (string) --
The unique ID that QLDB assigns to each journal export job.
To describe your export request and check the status of the job, you can use ExportId to call DescribeJournalS3Export .







Exceptions

QLDB.Client.exceptions.ResourceNotFoundException
QLDB.Client.exceptions.ResourcePreconditionNotMetException


    :return: {
        'ExportId': 'string'
    }
    
    
    :returns: 
    QLDB.Client.exceptions.ResourceNotFoundException
    QLDB.Client.exceptions.ResourcePreconditionNotMetException
    
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

def get_block(Name=None, BlockAddress=None, DigestTipAddress=None):
    """
    Returns a journal block object at a specified address in a ledger. Also returns a proof of the specified block for verification if DigestTipAddress is provided.
    If the specified ledger doesn\'t exist or is in DELETING status, then throws ResourceNotFoundException .
    If the specified ledger is in CREATING status, then throws ResourcePreconditionNotMetException .
    If no block exists with the specified address, then throws InvalidParameterException .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_block(
        Name='string',
        BlockAddress={
            'IonText': 'string'
        },
        DigestTipAddress={
            'IonText': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the ledger.\n

    :type BlockAddress: dict
    :param BlockAddress: [REQUIRED]\nThe location of the block that you want to request. An address is an Amazon Ion structure that has two fields: strandId and sequenceNo .\nFor example: {strandId:'BlFTjlSXze9BIh1KOszcE3',sequenceNo:14}\n\nIonText (string) --An Amazon Ion plaintext value contained in a ValueHolder structure.\n\n\n

    :type DigestTipAddress: dict
    :param DigestTipAddress: The latest block location covered by the digest for which to request a proof. An address is an Amazon Ion structure that has two fields: strandId and sequenceNo .\nFor example: {strandId:'BlFTjlSXze9BIh1KOszcE3',sequenceNo:49}\n\nIonText (string) --An Amazon Ion plaintext value contained in a ValueHolder structure.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Block': {
        'IonText': 'string'
    },
    'Proof': {
        'IonText': 'string'
    }
}


Response Structure

(dict) --

Block (dict) --
The block data object in Amazon Ion format.

IonText (string) --
An Amazon Ion plaintext value contained in a ValueHolder structure.



Proof (dict) --
The proof object in Amazon Ion format returned by a GetBlock request. A proof contains the list of hash values required to recalculate the specified digest using a Merkle tree, starting with the specified block.

IonText (string) --
An Amazon Ion plaintext value contained in a ValueHolder structure.









Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException
QLDB.Client.exceptions.ResourcePreconditionNotMetException


    :return: {
        'Block': {
            'IonText': 'string'
        },
        'Proof': {
            'IonText': 'string'
        }
    }
    
    
    :returns: 
    QLDB.Client.exceptions.InvalidParameterException
    QLDB.Client.exceptions.ResourceNotFoundException
    QLDB.Client.exceptions.ResourcePreconditionNotMetException
    
    """
    pass

def get_digest(Name=None):
    """
    Returns the digest of a ledger at the latest committed block in the journal. The response includes a 256-bit hash value and a block address.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_digest(
        Name='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the ledger.\n

    :rtype: dict
ReturnsResponse Syntax{
    'Digest': b'bytes',
    'DigestTipAddress': {
        'IonText': 'string'
    }
}


Response Structure

(dict) --
Digest (bytes) --The 256-bit hash value representing the digest returned by a GetDigest request.

DigestTipAddress (dict) --The latest block location covered by the digest that you requested. An address is an Amazon Ion structure that has two fields: strandId and sequenceNo .

IonText (string) --An Amazon Ion plaintext value contained in a ValueHolder structure.








Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException
QLDB.Client.exceptions.ResourcePreconditionNotMetException


    :return: {
        'Digest': b'bytes',
        'DigestTipAddress': {
            'IonText': 'string'
        }
    }
    
    
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

def get_revision(Name=None, BlockAddress=None, DocumentId=None, DigestTipAddress=None):
    """
    Returns a revision data object for a specified document ID and block address. Also returns a proof of the specified revision for verification if DigestTipAddress is provided.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_revision(
        Name='string',
        BlockAddress={
            'IonText': 'string'
        },
        DocumentId='string',
        DigestTipAddress={
            'IonText': 'string'
        }
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the ledger.\n

    :type BlockAddress: dict
    :param BlockAddress: [REQUIRED]\nThe block location of the document revision to be verified. An address is an Amazon Ion structure that has two fields: strandId and sequenceNo .\nFor example: {strandId:'BlFTjlSXze9BIh1KOszcE3',sequenceNo:14}\n\nIonText (string) --An Amazon Ion plaintext value contained in a ValueHolder structure.\n\n\n

    :type DocumentId: string
    :param DocumentId: [REQUIRED]\nThe unique ID of the document to be verified.\n

    :type DigestTipAddress: dict
    :param DigestTipAddress: The latest block location covered by the digest for which to request a proof. An address is an Amazon Ion structure that has two fields: strandId and sequenceNo .\nFor example: {strandId:'BlFTjlSXze9BIh1KOszcE3',sequenceNo:49}\n\nIonText (string) --An Amazon Ion plaintext value contained in a ValueHolder structure.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Proof': {
        'IonText': 'string'
    },
    'Revision': {
        'IonText': 'string'
    }
}


Response Structure

(dict) --

Proof (dict) --
The proof object in Amazon Ion format returned by a GetRevision request. A proof contains the list of hash values that are required to recalculate the specified digest using a Merkle tree, starting with the specified document revision.

IonText (string) --
An Amazon Ion plaintext value contained in a ValueHolder structure.



Revision (dict) --
The document revision data object in Amazon Ion format.

IonText (string) --
An Amazon Ion plaintext value contained in a ValueHolder structure.









Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException
QLDB.Client.exceptions.ResourcePreconditionNotMetException


    :return: {
        'Proof': {
            'IonText': 'string'
        },
        'Revision': {
            'IonText': 'string'
        }
    }
    
    
    :returns: 
    QLDB.Client.exceptions.InvalidParameterException
    QLDB.Client.exceptions.ResourceNotFoundException
    QLDB.Client.exceptions.ResourcePreconditionNotMetException
    
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

def list_journal_kinesis_streams_for_ledger(LedgerName=None, MaxResults=None, NextToken=None):
    """
    Returns an array of all Amazon QLDB journal stream descriptors for a given ledger. The output of each stream descriptor includes the same details that are returned by DescribeJournalKinesisStream .
    This action returns a maximum of MaxResults items. It is paginated so that you can retrieve all the items by calling ListJournalKinesisStreamsForLedger multiple times.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_journal_kinesis_streams_for_ledger(
        LedgerName='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type LedgerName: string
    :param LedgerName: [REQUIRED]\nThe name of the ledger.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single ListJournalKinesisStreamsForLedger request. (The actual number of results returned might be fewer.)

    :type NextToken: string
    :param NextToken: A pagination token, indicating that you want to retrieve the next page of results. If you received a value for NextToken in the response from a previous ListJournalKinesisStreamsForLedger call, you should use that value as input here.

    :rtype: dict

ReturnsResponse Syntax
{
    'Streams': [
        {
            'LedgerName': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'InclusiveStartTime': datetime(2015, 1, 1),
            'ExclusiveEndTime': datetime(2015, 1, 1),
            'RoleArn': 'string',
            'StreamId': 'string',
            'Arn': 'string',
            'Status': 'ACTIVE'|'COMPLETED'|'CANCELED'|'FAILED'|'IMPAIRED',
            'KinesisConfiguration': {
                'StreamArn': 'string',
                'AggregationEnabled': True|False
            },
            'ErrorCause': 'KINESIS_STREAM_NOT_FOUND'|'IAM_PERMISSION_REVOKED',
            'StreamName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Streams (list) --
The array of QLDB journal stream descriptors that are associated with the given ledger.

(dict) --
The information about an Amazon QLDB journal stream, including the Amazon Resource Name (ARN), stream name, creation time, current status, and the parameters of your original stream creation request.

LedgerName (string) --
The name of the ledger.

CreationTime (datetime) --
The date and time, in epoch time format, when the QLDB journal stream was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

InclusiveStartTime (datetime) --
The inclusive start date and time from which to start streaming journal data.

ExclusiveEndTime (datetime) --
The exclusive date and time that specifies when the stream ends. If this parameter is blank, the stream runs indefinitely until you cancel it.

RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal stream to write data records to a Kinesis Data Streams resource.

StreamId (string) --
The unique ID that QLDB assigns to each QLDB journal stream.

Arn (string) --
The Amazon Resource Name (ARN) of the QLDB journal stream.

Status (string) --
The current state of the QLDB journal stream.

KinesisConfiguration (dict) --
The configuration settings of the Amazon Kinesis Data Streams destination for your QLDB journal stream.

StreamArn (string) --
The Amazon Resource Name (ARN) of the Kinesis data stream resource.

AggregationEnabled (boolean) --
Enables QLDB to publish multiple stream records in a single Kinesis Data Streams record. To learn more, see KPL Key Concepts in the Amazon Kinesis Data Streams Developer Guide .



ErrorCause (string) --
The error message that describes the reason that a stream has a status of IMPAIRED or FAILED . This is not applicable to streams that have other status values.

StreamName (string) --
The user-defined name of the QLDB journal stream.





NextToken (string) --

If NextToken is empty, the last page of results has been processed and there are no more results to be retrieved.
If NextToken is not empty, more results are available. To retrieve the next page of results, use the value of NextToken in a subsequent ListJournalKinesisStreamsForLedger call.








Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException
QLDB.Client.exceptions.ResourcePreconditionNotMetException


    :return: {
        'Streams': [
            {
                'LedgerName': 'string',
                'CreationTime': datetime(2015, 1, 1),
                'InclusiveStartTime': datetime(2015, 1, 1),
                'ExclusiveEndTime': datetime(2015, 1, 1),
                'RoleArn': 'string',
                'StreamId': 'string',
                'Arn': 'string',
                'Status': 'ACTIVE'|'COMPLETED'|'CANCELED'|'FAILED'|'IMPAIRED',
                'KinesisConfiguration': {
                    'StreamArn': 'string',
                    'AggregationEnabled': True|False
                },
                'ErrorCause': 'KINESIS_STREAM_NOT_FOUND'|'IAM_PERMISSION_REVOKED',
                'StreamName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    If NextToken is empty, the last page of results has been processed and there are no more results to be retrieved.
    If NextToken is not empty, more results are available. To retrieve the next page of results, use the value of NextToken in a subsequent ListJournalKinesisStreamsForLedger call.
    
    """
    pass

def list_journal_s3_exports(MaxResults=None, NextToken=None):
    """
    Returns an array of journal export job descriptions for all ledgers that are associated with the current AWS account and Region.
    This action returns a maximum of MaxResults items, and is paginated so that you can retrieve all the items by calling ListJournalS3Exports multiple times.
    This action does not return any expired export jobs. For more information, see Export Job Expiration in the Amazon QLDB Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.list_journal_s3_exports(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single ListJournalS3Exports request. (The actual number of results returned might be fewer.)

    :type NextToken: string
    :param NextToken: A pagination token, indicating that you want to retrieve the next page of results. If you received a value for NextToken in the response from a previous ListJournalS3Exports call, then you should use that value as input here.

    :rtype: dict

ReturnsResponse Syntax
{
    'JournalS3Exports': [
        {
            'LedgerName': 'string',
            'ExportId': 'string',
            'ExportCreationTime': datetime(2015, 1, 1),
            'Status': 'IN_PROGRESS'|'COMPLETED'|'CANCELLED',
            'InclusiveStartTime': datetime(2015, 1, 1),
            'ExclusiveEndTime': datetime(2015, 1, 1),
            'S3ExportConfiguration': {
                'Bucket': 'string',
                'Prefix': 'string',
                'EncryptionConfiguration': {
                    'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                    'KmsKeyArn': 'string'
                }
            },
            'RoleArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

JournalS3Exports (list) --
The array of journal export job descriptions for all ledgers that are associated with the current AWS account and Region.

(dict) --
The information about a journal export job, including the ledger name, export ID, when it was created, current status, and its start and end time export parameters.

LedgerName (string) --
The name of the ledger.

ExportId (string) --
The unique ID of the journal export job.

ExportCreationTime (datetime) --
The date and time, in epoch time format, when the export job was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

Status (string) --
The current state of the journal export job.

InclusiveStartTime (datetime) --
The inclusive start date and time for the range of journal contents that are specified in the original export request.

ExclusiveEndTime (datetime) --
The exclusive end date and time for the range of journal contents that are specified in the original export request.

S3ExportConfiguration (dict) --
The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export job writes the journal contents.

Bucket (string) --
The Amazon S3 bucket name in which a journal export job writes the journal contents.
The bucket name must comply with the Amazon S3 bucket naming conventions. For more information, see Bucket Restrictions and Limitations in the Amazon S3 Developer Guide .

Prefix (string) --
The prefix for the Amazon S3 bucket in which a journal export job writes the journal contents.
The prefix must comply with Amazon S3 key naming rules and restrictions. For more information, see Object Key and Metadata in the Amazon S3 Developer Guide .
The following are examples of valid Prefix values:

JournalExports-ForMyLedger/Testing/
JournalExports
My:Tests/


EncryptionConfiguration (dict) --
The encryption settings that are used by a journal export job to write data in an Amazon S3 bucket.

ObjectEncryptionType (string) --
The Amazon S3 object encryption type.
To learn more about server-side encryption options in Amazon S3, see Protecting Data Using Server-Side Encryption in the Amazon S3 Developer Guide .

KmsKeyArn (string) --
The Amazon Resource Name (ARN) for a symmetric customer master key (CMK) in AWS Key Management Service (AWS KMS). Amazon QLDB does not support asymmetric CMKs.
You must provide a KmsKeyArn if you specify SSE_KMS as the ObjectEncryptionType .

KmsKeyArn is not required if you specify SSE_S3 as the ObjectEncryptionType .






RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal export job to do the following:

Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.
(Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS) for server-side encryption of your exported data.






NextToken (string) --

If NextToken is empty, then the last page of results has been processed and there are no more results to be retrieved.
If NextToken is not empty, then there are more results available. To retrieve the next page of results, use the value of NextToken in a subsequent ListJournalS3Exports call.









    :return: {
        'JournalS3Exports': [
            {
                'LedgerName': 'string',
                'ExportId': 'string',
                'ExportCreationTime': datetime(2015, 1, 1),
                'Status': 'IN_PROGRESS'|'COMPLETED'|'CANCELLED',
                'InclusiveStartTime': datetime(2015, 1, 1),
                'ExclusiveEndTime': datetime(2015, 1, 1),
                'S3ExportConfiguration': {
                    'Bucket': 'string',
                    'Prefix': 'string',
                    'EncryptionConfiguration': {
                        'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                        'KmsKeyArn': 'string'
                    }
                },
                'RoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    JournalExports-ForMyLedger/Testing/
    JournalExports
    My:Tests/
    
    """
    pass

def list_journal_s3_exports_for_ledger(Name=None, MaxResults=None, NextToken=None):
    """
    Returns an array of journal export job descriptions for a specified ledger.
    This action returns a maximum of MaxResults items, and is paginated so that you can retrieve all the items by calling ListJournalS3ExportsForLedger multiple times.
    This action does not return any expired export jobs. For more information, see Export Job Expiration in the Amazon QLDB Developer Guide .
    See also: AWS API Documentation
    
    
    :example: response = client.list_journal_s3_exports_for_ledger(
        Name='string',
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the ledger.\n

    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single ListJournalS3ExportsForLedger request. (The actual number of results returned might be fewer.)

    :type NextToken: string
    :param NextToken: A pagination token, indicating that you want to retrieve the next page of results. If you received a value for NextToken in the response from a previous ListJournalS3ExportsForLedger call, then you should use that value as input here.

    :rtype: dict

ReturnsResponse Syntax
{
    'JournalS3Exports': [
        {
            'LedgerName': 'string',
            'ExportId': 'string',
            'ExportCreationTime': datetime(2015, 1, 1),
            'Status': 'IN_PROGRESS'|'COMPLETED'|'CANCELLED',
            'InclusiveStartTime': datetime(2015, 1, 1),
            'ExclusiveEndTime': datetime(2015, 1, 1),
            'S3ExportConfiguration': {
                'Bucket': 'string',
                'Prefix': 'string',
                'EncryptionConfiguration': {
                    'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                    'KmsKeyArn': 'string'
                }
            },
            'RoleArn': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

JournalS3Exports (list) --
The array of journal export job descriptions that are associated with the specified ledger.

(dict) --
The information about a journal export job, including the ledger name, export ID, when it was created, current status, and its start and end time export parameters.

LedgerName (string) --
The name of the ledger.

ExportId (string) --
The unique ID of the journal export job.

ExportCreationTime (datetime) --
The date and time, in epoch time format, when the export job was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

Status (string) --
The current state of the journal export job.

InclusiveStartTime (datetime) --
The inclusive start date and time for the range of journal contents that are specified in the original export request.

ExclusiveEndTime (datetime) --
The exclusive end date and time for the range of journal contents that are specified in the original export request.

S3ExportConfiguration (dict) --
The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export job writes the journal contents.

Bucket (string) --
The Amazon S3 bucket name in which a journal export job writes the journal contents.
The bucket name must comply with the Amazon S3 bucket naming conventions. For more information, see Bucket Restrictions and Limitations in the Amazon S3 Developer Guide .

Prefix (string) --
The prefix for the Amazon S3 bucket in which a journal export job writes the journal contents.
The prefix must comply with Amazon S3 key naming rules and restrictions. For more information, see Object Key and Metadata in the Amazon S3 Developer Guide .
The following are examples of valid Prefix values:

JournalExports-ForMyLedger/Testing/
JournalExports
My:Tests/


EncryptionConfiguration (dict) --
The encryption settings that are used by a journal export job to write data in an Amazon S3 bucket.

ObjectEncryptionType (string) --
The Amazon S3 object encryption type.
To learn more about server-side encryption options in Amazon S3, see Protecting Data Using Server-Side Encryption in the Amazon S3 Developer Guide .

KmsKeyArn (string) --
The Amazon Resource Name (ARN) for a symmetric customer master key (CMK) in AWS Key Management Service (AWS KMS). Amazon QLDB does not support asymmetric CMKs.
You must provide a KmsKeyArn if you specify SSE_KMS as the ObjectEncryptionType .

KmsKeyArn is not required if you specify SSE_S3 as the ObjectEncryptionType .






RoleArn (string) --
The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal export job to do the following:

Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.
(Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS) for server-side encryption of your exported data.






NextToken (string) --

If NextToken is empty, then the last page of results has been processed and there are no more results to be retrieved.
If NextToken is not empty, then there are more results available. To retrieve the next page of results, use the value of NextToken in a subsequent ListJournalS3ExportsForLedger call.









    :return: {
        'JournalS3Exports': [
            {
                'LedgerName': 'string',
                'ExportId': 'string',
                'ExportCreationTime': datetime(2015, 1, 1),
                'Status': 'IN_PROGRESS'|'COMPLETED'|'CANCELLED',
                'InclusiveStartTime': datetime(2015, 1, 1),
                'ExclusiveEndTime': datetime(2015, 1, 1),
                'S3ExportConfiguration': {
                    'Bucket': 'string',
                    'Prefix': 'string',
                    'EncryptionConfiguration': {
                        'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                        'KmsKeyArn': 'string'
                    }
                },
                'RoleArn': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    JournalExports-ForMyLedger/Testing/
    JournalExports
    My:Tests/
    
    """
    pass

def list_ledgers(MaxResults=None, NextToken=None):
    """
    Returns an array of ledger summaries that are associated with the current AWS account and Region.
    This action returns a maximum of 100 items and is paginated so that you can retrieve all the items by calling ListLedgers multiple times.
    See also: AWS API Documentation
    
    
    :example: response = client.list_ledgers(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return in a single ListLedgers request. (The actual number of results returned might be fewer.)

    :type NextToken: string
    :param NextToken: A pagination token, indicating that you want to retrieve the next page of results. If you received a value for NextToken in the response from a previous ListLedgers call, then you should use that value as input here.

    :rtype: dict

ReturnsResponse Syntax
{
    'Ledgers': [
        {
            'Name': 'string',
            'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
            'CreationDateTime': datetime(2015, 1, 1)
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) --

Ledgers (list) --
The array of ledger summaries that are associated with the current AWS account and Region.

(dict) --
Information about a ledger, including its name, state, and when it was created.

Name (string) --
The name of the ledger.

State (string) --
The current status of the ledger.

CreationDateTime (datetime) --
The date and time, in epoch time format, when the ledger was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)





NextToken (string) --
A pagination token, indicating whether there are more results available:

If NextToken is empty, then the last page of results has been processed and there are no more results to be retrieved.
If NextToken is not empty, then there are more results available. To retrieve the next page of results, use the value of NextToken in a subsequent ListLedgers call.









    :return: {
        'Ledgers': [
            {
                'Name': 'string',
                'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
                'CreationDateTime': datetime(2015, 1, 1)
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    If NextToken is empty, then the last page of results has been processed and there are no more results to be retrieved.
    If NextToken is not empty, then there are more results available. To retrieve the next page of results, use the value of NextToken in a subsequent ListLedgers call.
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    Returns all tags for a specified Amazon QLDB resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) for which you want to list the tags. For example:\n\narn:aws:qldb:us-east-1:123456789012:ledger/exampleLedger\n

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
Tags (dict) --The tags that are currently associated with the specified Amazon QLDB resource.

(string) --
(string) --









Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    QLDB.Client.exceptions.InvalidParameterException
    QLDB.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def stream_journal_to_kinesis(LedgerName=None, RoleArn=None, Tags=None, InclusiveStartTime=None, ExclusiveEndTime=None, KinesisConfiguration=None, StreamName=None):
    """
    Creates a stream for a given Amazon QLDB ledger that delivers the journal data to a specified Amazon Kinesis Data Streams resource. The stream captures every document revision that is committed to your journal and sends it to the Kinesis data stream.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stream_journal_to_kinesis(
        LedgerName='string',
        RoleArn='string',
        Tags={
            'string': 'string'
        },
        InclusiveStartTime=datetime(2015, 1, 1),
        ExclusiveEndTime=datetime(2015, 1, 1),
        KinesisConfiguration={
            'StreamArn': 'string',
            'AggregationEnabled': True|False
        },
        StreamName='string'
    )
    
    
    :type LedgerName: string
    :param LedgerName: [REQUIRED]\nThe name of the ledger.\n

    :type RoleArn: string
    :param RoleArn: [REQUIRED]\nThe Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal stream to write data records to a Kinesis Data Streams resource.\n

    :type Tags: dict
    :param Tags: The key-value pairs to add as tags to the stream that you want to create. Tag keys are case sensitive. Tag values are case sensitive and can be null.\n\n(string) --\n(string) --\n\n\n\n

    :type InclusiveStartTime: datetime
    :param InclusiveStartTime: [REQUIRED]\nThe inclusive start date and time from which to start streaming journal data. This parameter must be in ISO 8601 date and time format and in Universal Coordinated Time (UTC). For example: 2019-06-13T21:36:34Z\nThe InclusiveStartTime cannot be in the future and must be before ExclusiveEndTime .\nIf you provide an InclusiveStartTime that is before the ledger\'s CreationDateTime , QLDB effectively defaults it to the ledger\'s CreationDateTime .\n

    :type ExclusiveEndTime: datetime
    :param ExclusiveEndTime: The exclusive date and time that specifies when the stream ends. If you keep this parameter blank, the stream runs indefinitely until you cancel it.\nThe ExclusiveEndTime must be in ISO 8601 date and time format and in Universal Coordinated Time (UTC). For example: 2019-06-13T21:36:34Z\n

    :type KinesisConfiguration: dict
    :param KinesisConfiguration: [REQUIRED]\nThe configuration settings of the Kinesis Data Streams destination for your stream request.\n\nStreamArn (string) -- [REQUIRED]The Amazon Resource Name (ARN) of the Kinesis data stream resource.\n\nAggregationEnabled (boolean) --Enables QLDB to publish multiple stream records in a single Kinesis Data Streams record. To learn more, see KPL Key Concepts in the Amazon Kinesis Data Streams Developer Guide .\n\n\n

    :type StreamName: string
    :param StreamName: [REQUIRED]\nThe name that you want to assign to the QLDB journal stream. User-defined names can help identify and indicate the purpose of a stream.\nYour stream name must be unique among other active streams for a given ledger. If you try to create a stream with the same name and configuration of an active, existing stream for the same ledger, QLDB simply returns the existing stream. Stream names have the same naming constraints as ledger names, as defined in Quotas in Amazon QLDB in the Amazon QLDB Developer Guide .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StreamId': 'string'
}


Response Structure

(dict) --

StreamId (string) --
The unique ID that QLDB assigns to each QLDB journal stream.







Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException
QLDB.Client.exceptions.ResourcePreconditionNotMetException


    :return: {
        'StreamId': 'string'
    }
    
    
    :returns: 
    QLDB.Client.exceptions.InvalidParameterException
    QLDB.Client.exceptions.ResourceNotFoundException
    QLDB.Client.exceptions.ResourcePreconditionNotMetException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Adds one or more tags to a specified Amazon QLDB resource.
    A resource can have up to 50 tags. If you try to create more than 50 tags for a resource, your request fails and returns an error.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) to which you want to add the tags. For example:\n\narn:aws:qldb:us-east-1:123456789012:ledger/exampleLedger\n

    :type Tags: dict
    :param Tags: [REQUIRED]\nThe key-value pairs to add as tags to the specified QLDB resource. Tag keys are case sensitive. If you specify a key that already exists for the resource, your request fails and returns an error. Tag values are case sensitive and can be null.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Removes one or more tags from a specified Amazon QLDB resource. You can specify up to 50 tag keys to remove.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED]\nThe Amazon Resource Name (ARN) from which you want to remove the tags. For example:\n\narn:aws:qldb:us-east-1:123456789012:ledger/exampleLedger\n

    :type TagKeys: list
    :param TagKeys: [REQUIRED]\nThe list of tag keys that you want to remove.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_ledger(Name=None, DeletionProtection=None):
    """
    Updates properties on a ledger.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_ledger(
        Name='string',
        DeletionProtection=True|False
    )
    
    
    :type Name: string
    :param Name: [REQUIRED]\nThe name of the ledger.\n

    :type DeletionProtection: boolean
    :param DeletionProtection: The flag that prevents a ledger from being deleted by any user. If not provided on ledger creation, this feature is enabled (true ) by default.\nIf deletion protection is enabled, you must first disable it before you can delete the ledger using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling the UpdateLedger operation to set the flag to false . The QLDB console disables deletion protection for you when you use it to delete a ledger.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Name': 'string',
    'Arn': 'string',
    'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
    'CreationDateTime': datetime(2015, 1, 1),
    'DeletionProtection': True|False
}


Response Structure

(dict) --

Name (string) --
The name of the ledger.

Arn (string) --
The Amazon Resource Name (ARN) for the ledger.

State (string) --
The current status of the ledger.

CreationDateTime (datetime) --
The date and time, in epoch time format, when the ledger was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

DeletionProtection (boolean) --
The flag that prevents a ledger from being deleted by any user. If not provided on ledger creation, this feature is enabled (true ) by default.
If deletion protection is enabled, you must first disable it before you can delete the ledger using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling the UpdateLedger operation to set the flag to false . The QLDB console disables deletion protection for you when you use it to delete a ledger.







Exceptions

QLDB.Client.exceptions.InvalidParameterException
QLDB.Client.exceptions.ResourceNotFoundException


    :return: {
        'Name': 'string',
        'Arn': 'string',
        'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
        'CreationDateTime': datetime(2015, 1, 1),
        'DeletionProtection': True|False
    }
    
    
    :returns: 
    QLDB.Client.exceptions.InvalidParameterException
    QLDB.Client.exceptions.ResourceNotFoundException
    
    """
    pass

