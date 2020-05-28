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

def send_command(SessionToken=None, StartSession=None, StartTransaction=None, EndSession=None, CommitTransaction=None, AbortTransaction=None, ExecuteStatement=None, FetchPage=None):
    """
    Sends a command to an Amazon QLDB ledger.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.send_command(
        SessionToken='string',
        StartSession={
            'LedgerName': 'string'
        },
        StartTransaction={}
        ,
        EndSession={}
        ,
        CommitTransaction={
            'TransactionId': 'string',
            'CommitDigest': b'bytes'
        },
        AbortTransaction={}
        ,
        ExecuteStatement={
            'TransactionId': 'string',
            'Statement': 'string',
            'Parameters': [
                {
                    'IonBinary': b'bytes',
                    'IonText': 'string'
                },
            ]
        },
        FetchPage={
            'TransactionId': 'string',
            'NextPageToken': 'string'
        }
    )
    
    
    :type SessionToken: string
    :param SessionToken: Specifies the session token for the current command. A session token is constant throughout the life of the session.\nTo obtain a session token, run the StartSession command. This SessionToken is required for every subsequent command that is issued during the current session.\n

    :type StartSession: dict
    :param StartSession: Command to start a new session. A session token is obtained as part of the response.\n\nLedgerName (string) -- [REQUIRED]The name of the ledger to start a new session against.\n\n\n

    :type StartTransaction: dict
    :param StartTransaction: Command to start a new transaction.

    :type EndSession: dict
    :param EndSession: Command to end the current session.

    :type CommitTransaction: dict
    :param CommitTransaction: Command to commit the specified transaction.\n\nTransactionId (string) -- [REQUIRED]Specifies the transaction id of the transaction to commit.\n\nCommitDigest (bytes) -- [REQUIRED]Specifies the commit digest for the transaction to commit. For every active transaction, the commit digest must be passed. QLDB validates CommitDigest and rejects the commit with an error if the digest computed on the client does not match the digest computed by QLDB.\n\n\n

    :type AbortTransaction: dict
    :param AbortTransaction: Command to abort the current transaction.

    :type ExecuteStatement: dict
    :param ExecuteStatement: Command to execute a statement in the specified transaction.\n\nTransactionId (string) -- [REQUIRED]Specifies the transaction id of the request.\n\nStatement (string) -- [REQUIRED]Specifies the statement of the request.\n\nParameters (list) --Specifies the parameters for the parameterized statement in the request.\n\n(dict) --A structure that can contains values in multiple encoding formats.\n\nIonBinary (bytes) --An Amazon Ion binary value contained in a ValueHolder structure.\n\nIonText (string) --An Amazon Ion plaintext value contained in a ValueHolder structure.\n\n\n\n\n\n\n

    :type FetchPage: dict
    :param FetchPage: Command to fetch a page.\n\nTransactionId (string) -- [REQUIRED]Specifies the transaction id of the page to be fetched.\n\nNextPageToken (string) -- [REQUIRED]Specifies the next page token of the page to be fetched.\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'StartSession': {
        'SessionToken': 'string'
    },
    'StartTransaction': {
        'TransactionId': 'string'
    },
    'EndSession': {},
    'CommitTransaction': {
        'TransactionId': 'string',
        'CommitDigest': b'bytes'
    },
    'AbortTransaction': {},
    'ExecuteStatement': {
        'FirstPage': {
            'Values': [
                {
                    'IonBinary': b'bytes',
                    'IonText': 'string'
                },
            ],
            'NextPageToken': 'string'
        }
    },
    'FetchPage': {
        'Page': {
            'Values': [
                {
                    'IonBinary': b'bytes',
                    'IonText': 'string'
                },
            ],
            'NextPageToken': 'string'
        }
    }
}


Response Structure

(dict) --

StartSession (dict) --
Contains the details of the started session that includes a session token. This SessionToken is required for every subsequent command that is issued during the current session.

SessionToken (string) --
Session token of the started session. This SessionToken is required for every subsequent command that is issued during the current session.



StartTransaction (dict) --
Contains the details of the started transaction.

TransactionId (string) --
The transaction id of the started transaction.



EndSession (dict) --
Contains the details of the ended session.

CommitTransaction (dict) --
Contains the details of the committed transaction.

TransactionId (string) --
The transaction id of the committed transaction.

CommitDigest (bytes) --
The commit digest of the committed transaction.



AbortTransaction (dict) --
Contains the details of the aborted transaction.

ExecuteStatement (dict) --
Contains the details of the executed statement.

FirstPage (dict) --
Contains the details of the first fetched page.

Values (list) --
A structure that contains values in multiple encoding formats.

(dict) --
A structure that can contains values in multiple encoding formats.

IonBinary (bytes) --
An Amazon Ion binary value contained in a ValueHolder structure.

IonText (string) --
An Amazon Ion plaintext value contained in a ValueHolder structure.





NextPageToken (string) --
The token of the next page.





FetchPage (dict) --
Contains the details of the fetched page.

Page (dict) --
Contains details of the fetched page.

Values (list) --
A structure that contains values in multiple encoding formats.

(dict) --
A structure that can contains values in multiple encoding formats.

IonBinary (bytes) --
An Amazon Ion binary value contained in a ValueHolder structure.

IonText (string) --
An Amazon Ion plaintext value contained in a ValueHolder structure.





NextPageToken (string) --
The token of the next page.











Exceptions

QLDBSession.Client.exceptions.BadRequestException
QLDBSession.Client.exceptions.InvalidSessionException
QLDBSession.Client.exceptions.OccConflictException
QLDBSession.Client.exceptions.RateExceededException
QLDBSession.Client.exceptions.LimitExceededException


    :return: {
        'StartSession': {
            'SessionToken': 'string'
        },
        'StartTransaction': {
            'TransactionId': 'string'
        },
        'EndSession': {},
        'CommitTransaction': {
            'TransactionId': 'string',
            'CommitDigest': b'bytes'
        },
        'AbortTransaction': {},
        'ExecuteStatement': {
            'FirstPage': {
                'Values': [
                    {
                        'IonBinary': b'bytes',
                        'IonText': 'string'
                    },
                ],
                'NextPageToken': 'string'
            }
        },
        'FetchPage': {
            'Page': {
                'Values': [
                    {
                        'IonBinary': b'bytes',
                        'IonText': 'string'
                    },
                ],
                'NextPageToken': 'string'
            }
        }
    }
    
    
    :returns: 
    QLDBSession.Client.exceptions.BadRequestException
    QLDBSession.Client.exceptions.InvalidSessionException
    QLDBSession.Client.exceptions.OccConflictException
    QLDBSession.Client.exceptions.RateExceededException
    QLDBSession.Client.exceptions.LimitExceededException
    
    """
    pass

