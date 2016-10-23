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


def cancel_job(JobId=None, APIVersion=None):
    """
    :param JobId: [REQUIRED] A unique identifier which refers to a particular job.
    :type JobId: string
    :param APIVersion: Specifies the version of the client tool.
    :type APIVersion: string
    """
    pass


def create_job(JobType=None, Manifest=None, ManifestAddendum=None, ValidateOnly=None, APIVersion=None):
    """
    :param JobType: [REQUIRED] Specifies whether the job to initiate is an import or export job.
    :type JobType: string
    :param Manifest: [REQUIRED] The UTF-8 encoded text of the manifest file.
    :type Manifest: string
    :param ManifestAddendum: For internal use only.
    :type ManifestAddendum: string
    :param ValidateOnly: [REQUIRED] Validate the manifest and parameter values in the request but do not actually create a job.
    :type ValidateOnly: boolean
    :param APIVersion: Specifies the version of the client tool.
    :type APIVersion: string
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


def get_shipping_label(jobIds=None, name=None, company=None, phoneNumber=None, country=None, stateOrProvince=None,
                       city=None, postalCode=None, street1=None, street2=None, street3=None, APIVersion=None):
    """
    :param jobIds: [REQUIRED]
            (string) --
            
    :type jobIds: list
    :param name: Specifies the name of the person responsible for shipping this package.
    :type name: string
    :param company: Specifies the name of the company that will ship this package.
    :type company: string
    :param phoneNumber: Specifies the phone number of the person responsible for shipping this package.
    :type phoneNumber: string
    :param country: Specifies the name of your country for the return address.
    :type country: string
    :param stateOrProvince: Specifies the name of your state or your province for the return address.
    :type stateOrProvince: string
    :param city: Specifies the name of your city for the return address.
    :type city: string
    :param postalCode: Specifies the postal code for the return address.
    :type postalCode: string
    :param street1: Specifies the first part of the street address for the return address, for example 1234 Main Street.
    :type street1: string
    :param street2: Specifies the optional second part of the street address for the return address, for example Suite 100.
    :type street2: string
    :param street3: Specifies the optional third part of the street address for the return address, for example c/o Jane Doe.
    :type street3: string
    :param APIVersion: Specifies the version of the client tool.
    :type APIVersion: string
    """
    pass


def get_status(JobId=None, APIVersion=None):
    """
    :param JobId: [REQUIRED] A unique identifier which refers to a particular job.
    :type JobId: string
    :param APIVersion: Specifies the version of the client tool.
    :type APIVersion: string
    """
    pass


def get_waiter():
    """
    """
    pass


def list_jobs(MaxJobs=None, Marker=None, APIVersion=None):
    """
    :param MaxJobs: Sets the maximum number of jobs returned in the response. If there are additional jobs that were not returned because MaxJobs was exceeded, the response contains IsTruncatedtrue/IsTruncated. To return the additional jobs, see Marker.
    :type MaxJobs: integer
    :param Marker: Specifies the JOBID to start after when listing the jobs created with your account. AWS Import/Export lists your jobs in reverse chronological order. See MaxJobs.
    :type Marker: string
    :param APIVersion: Specifies the version of the client tool.
    :type APIVersion: string
    """
    pass


def update_job(JobId=None, Manifest=None, JobType=None, ValidateOnly=None, APIVersion=None):
    """
    :param JobId: [REQUIRED] A unique identifier which refers to a particular job.
    :type JobId: string
    :param Manifest: [REQUIRED] The UTF-8 encoded text of the manifest file.
    :type Manifest: string
    :param JobType: [REQUIRED] Specifies whether the job to initiate is an import or export job.
    :type JobType: string
    :param ValidateOnly: [REQUIRED] Validate the manifest and parameter values in the request but do not actually create a job.
    :type ValidateOnly: boolean
    :param APIVersion: Specifies the version of the client tool.
    :type APIVersion: string
    """
    pass
