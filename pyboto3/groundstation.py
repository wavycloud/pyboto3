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

def cancel_contact(contactId=None):
    """
    Cancels a contact with a specified contact ID.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.cancel_contact(
        contactId='string'
    )
    
    
    :type contactId: string
    :param contactId: [REQUIRED]\nUUID of a contact.\n

    :rtype: dict
ReturnsResponse Syntax{
    'contactId': 'string'
}


Response Structure

(dict) --
contactId (string) --UUID of a contact.






Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'contactId': 'string'
    }
    
    
    """
    pass

def create_config(configData=None, name=None, tags=None):
    """
    Creates a Config with the specified configData parameters.
    Only one type of configData can be specified.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_config(
        configData={
            'antennaDownlinkConfig': {
                'spectrumConfig': {
                    'bandwidth': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'centerFrequency': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                }
            },
            'antennaDownlinkDemodDecodeConfig': {
                'decodeConfig': {
                    'unvalidatedJSON': 'string'
                },
                'demodulationConfig': {
                    'unvalidatedJSON': 'string'
                },
                'spectrumConfig': {
                    'bandwidth': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'centerFrequency': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                }
            },
            'antennaUplinkConfig': {
                'spectrumConfig': {
                    'centerFrequency': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                },
                'targetEirp': {
                    'units': 'dBW',
                    'value': 123.0
                }
            },
            'dataflowEndpointConfig': {
                'dataflowEndpointName': 'string',
                'dataflowEndpointRegion': 'string'
            },
            'trackingConfig': {
                'autotrack': 'PREFERRED'|'REMOVED'|'REQUIRED'
            },
            'uplinkEchoConfig': {
                'antennaUplinkConfigArn': 'string',
                'enabled': True|False
            }
        },
        name='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type configData: dict
    :param configData: [REQUIRED]\nParameters of a Config .\n\nantennaDownlinkConfig (dict) --Information about how AWS Ground Station should configure an antenna for downlink during a contact.\n\nspectrumConfig (dict) -- [REQUIRED]Object that describes a spectral Config .\n\nbandwidth (dict) -- [REQUIRED]Bandwidth of a spectral Config .\n\nunits (string) -- [REQUIRED]Frequency bandwidth units.\n\nvalue (float) -- [REQUIRED]Frequency bandwidth value.\n\n\n\ncenterFrequency (dict) -- [REQUIRED]Center frequency of a spectral Config .\n\nunits (string) -- [REQUIRED]Frequency units.\n\nvalue (float) -- [REQUIRED]Frequency value.\n\n\n\npolarization (string) --Polarization of a spectral Config .\n\n\n\n\n\nantennaDownlinkDemodDecodeConfig (dict) --Information about how AWS Ground Station should con\xef\xac\x81gure an antenna for downlink demod decode during a contact.\n\ndecodeConfig (dict) -- [REQUIRED]Information about the decode Config .\n\nunvalidatedJSON (string) -- [REQUIRED]Unvalidated JSON of a decode Config .\n\n\n\ndemodulationConfig (dict) -- [REQUIRED]Information about the demodulation Config .\n\nunvalidatedJSON (string) -- [REQUIRED]Unvalidated JSON of a demodulation Config .\n\n\n\nspectrumConfig (dict) -- [REQUIRED]Information about the spectral Config .\n\nbandwidth (dict) -- [REQUIRED]Bandwidth of a spectral Config .\n\nunits (string) -- [REQUIRED]Frequency bandwidth units.\n\nvalue (float) -- [REQUIRED]Frequency bandwidth value.\n\n\n\ncenterFrequency (dict) -- [REQUIRED]Center frequency of a spectral Config .\n\nunits (string) -- [REQUIRED]Frequency units.\n\nvalue (float) -- [REQUIRED]Frequency value.\n\n\n\npolarization (string) --Polarization of a spectral Config .\n\n\n\n\n\nantennaUplinkConfig (dict) --Information about how AWS Ground Station should con\xef\xac\x81gure an antenna for uplink during a contact.\n\nspectrumConfig (dict) -- [REQUIRED]Information about the uplink spectral Config .\n\ncenterFrequency (dict) -- [REQUIRED]Center frequency of an uplink spectral Config .\n\nunits (string) -- [REQUIRED]Frequency units.\n\nvalue (float) -- [REQUIRED]Frequency value.\n\n\n\npolarization (string) --Polarization of an uplink spectral Config .\n\n\n\ntargetEirp (dict) -- [REQUIRED]EIRP of the target.\n\nunits (string) -- [REQUIRED]Units of an EIRP.\n\nvalue (float) -- [REQUIRED]Value of an EIRP.\n\n\n\n\n\ndataflowEndpointConfig (dict) --Information about the dataflow endpoint Config .\n\ndataflowEndpointName (string) -- [REQUIRED]Name of a dataflow endpoint.\n\ndataflowEndpointRegion (string) --Region of a dataflow endpoint.\n\n\n\ntrackingConfig (dict) --Object that determines whether tracking should be used during a contact executed with this Config in the mission profile.\n\nautotrack (string) -- [REQUIRED]Current setting for autotrack.\n\n\n\nuplinkEchoConfig (dict) --Information about an uplink echo Config .\nParameters from the AntennaUplinkConfig , corresponding to the specified AntennaUplinkConfigArn , are used when this UplinkEchoConfig is used in a contact.\n\nantennaUplinkConfigArn (string) -- [REQUIRED]ARN of an uplink Config .\n\nenabled (boolean) -- [REQUIRED]Whether or not an uplink Config is enabled.\n\n\n\n\n

    :type name: string
    :param name: [REQUIRED]\nName of a Config .\n

    :type tags: dict
    :param tags: Tags assigned to a Config .\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'configArn': 'string',
    'configId': 'string',
    'configType': 'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo'
}


Response Structure

(dict) --

configArn (string) --
ARN of a Config .

configId (string) --
UUID of a Config .

configType (string) --
Type of a Config .







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceLimitExceededException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'configArn': 'string',
        'configId': 'string',
        'configType': 'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceLimitExceededException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_dataflow_endpoint_group(endpointDetails=None, tags=None):
    """
    Creates a DataflowEndpoint group containing the specified list of DataflowEndpoint objects.
    The name field in each endpoint is used in your mission profile DataflowEndpointConfig to specify which endpoints to use during a contact.
    When a contact uses multiple DataflowEndpointConfig objects, each Config must match a DataflowEndpoint in the same group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_dataflow_endpoint_group(
        endpointDetails=[
            {
                'endpoint': {
                    'address': {
                        'name': 'string',
                        'port': 123
                    },
                    'name': 'string',
                    'status': 'created'|'creating'|'deleted'|'deleting'|'failed'
                },
                'securityDetails': {
                    'roleArn': 'string',
                    'securityGroupIds': [
                        'string',
                    ],
                    'subnetIds': [
                        'string',
                    ]
                }
            },
        ],
        tags={
            'string': 'string'
        }
    )
    
    
    :type endpointDetails: list
    :param endpointDetails: [REQUIRED]\nEndpoint details of each endpoint in the dataflow endpoint group.\n\n(dict) --Information about the endpoint details.\n\nendpoint (dict) --A dataflow endpoint.\n\naddress (dict) --Socket address of a dataflow endpoint.\n\nname (string) -- [REQUIRED]Name of a socket address.\n\nport (integer) -- [REQUIRED]Port of a socket address.\n\n\n\nname (string) --Name of a dataflow endpoint.\n\nstatus (string) --Status of a dataflow endpoint.\n\n\n\nsecurityDetails (dict) --Endpoint security details.\n\nroleArn (string) -- [REQUIRED]ARN to a role needed for connecting streams to your instances.\n\nsecurityGroupIds (list) -- [REQUIRED]The security groups to attach to the elastic network interfaces.\n\n(string) --\n\n\nsubnetIds (list) -- [REQUIRED]A list of subnets where AWS Ground Station places elastic network interfaces to send streams to your instances.\n\n(string) --\n\n\n\n\n\n\n\n

    :type tags: dict
    :param tags: Tags of a dataflow endpoint group.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'dataflowEndpointGroupId': 'string'
}


Response Structure

(dict) --

dataflowEndpointGroupId (string) --
UUID of a dataflow endpoint group.







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'dataflowEndpointGroupId': 'string'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def create_mission_profile(contactPostPassDurationSeconds=None, contactPrePassDurationSeconds=None, dataflowEdges=None, minimumViableContactDurationSeconds=None, name=None, tags=None, trackingConfigArn=None):
    """
    Creates a mission profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_mission_profile(
        contactPostPassDurationSeconds=123,
        contactPrePassDurationSeconds=123,
        dataflowEdges=[
            [
                'string',
            ],
        ],
        minimumViableContactDurationSeconds=123,
        name='string',
        tags={
            'string': 'string'
        },
        trackingConfigArn='string'
    )
    
    
    :type contactPostPassDurationSeconds: integer
    :param contactPostPassDurationSeconds: Amount of time after a contact ends that you\xe2\x80\x99d like to receive a CloudWatch event indicating the pass has finished.

    :type contactPrePassDurationSeconds: integer
    :param contactPrePassDurationSeconds: Amount of time prior to contact start you\xe2\x80\x99d like to receive a CloudWatch event indicating an upcoming pass.

    :type dataflowEdges: list
    :param dataflowEdges: [REQUIRED]\nA list of lists of ARNs. Each list of ARNs is an edge, with a from Config and a to Config .\n\n(list) --\n(string) --\n\n\n\n

    :type minimumViableContactDurationSeconds: integer
    :param minimumViableContactDurationSeconds: [REQUIRED]\nSmallest amount of time in seconds that you\xe2\x80\x99d like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.\n

    :type name: string
    :param name: [REQUIRED]\nName of a mission profile.\n

    :type tags: dict
    :param tags: Tags assigned to a mission profile.\n\n(string) --\n(string) --\n\n\n\n

    :type trackingConfigArn: string
    :param trackingConfigArn: [REQUIRED]\nARN of a tracking Config .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'missionProfileId': 'string'
}


Response Structure

(dict) --

missionProfileId (string) --
UUID of a mission profile.







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'missionProfileId': 'string'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def delete_config(configId=None, configType=None):
    """
    Deletes a Config .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_config(
        configId='string',
        configType='antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo'
    )
    
    
    :type configId: string
    :param configId: [REQUIRED]\nUUID of a Config .\n

    :type configType: string
    :param configType: [REQUIRED]\nType of a Config .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'configArn': 'string',
    'configId': 'string',
    'configType': 'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo'
}


Response Structure

(dict) --

configArn (string) --
ARN of a Config .

configId (string) --
UUID of a Config .

configType (string) --
Type of a Config .







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'configArn': 'string',
        'configId': 'string',
        'configType': 'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def delete_dataflow_endpoint_group(dataflowEndpointGroupId=None):
    """
    Deletes a dataflow endpoint group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_dataflow_endpoint_group(
        dataflowEndpointGroupId='string'
    )
    
    
    :type dataflowEndpointGroupId: string
    :param dataflowEndpointGroupId: [REQUIRED]\nUUID of a dataflow endpoint group.\n

    :rtype: dict
ReturnsResponse Syntax{
    'dataflowEndpointGroupId': 'string'
}


Response Structure

(dict) --
dataflowEndpointGroupId (string) --UUID of a dataflow endpoint group.






Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'dataflowEndpointGroupId': 'string'
    }
    
    
    """
    pass

def delete_mission_profile(missionProfileId=None):
    """
    Deletes a mission profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_mission_profile(
        missionProfileId='string'
    )
    
    
    :type missionProfileId: string
    :param missionProfileId: [REQUIRED]\nUUID of a mission profile.\n

    :rtype: dict
ReturnsResponse Syntax{
    'missionProfileId': 'string'
}


Response Structure

(dict) --
missionProfileId (string) --UUID of a mission profile.






Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'missionProfileId': 'string'
    }
    
    
    """
    pass

def describe_contact(contactId=None):
    """
    Describes an existing contact.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_contact(
        contactId='string'
    )
    
    
    :type contactId: string
    :param contactId: [REQUIRED]\nUUID of a contact.\n

    :rtype: dict
ReturnsResponse Syntax{
    'contactId': 'string',
    'contactStatus': 'AVAILABLE'|'AWS_CANCELLED'|'CANCELLED'|'CANCELLING'|'COMPLETED'|'FAILED'|'FAILED_TO_SCHEDULE'|'PASS'|'POSTPASS'|'PREPASS'|'SCHEDULED'|'SCHEDULING',
    'endTime': datetime(2015, 1, 1),
    'errorMessage': 'string',
    'groundStation': 'string',
    'maximumElevation': {
        'unit': 'DEGREE_ANGLE'|'RADIAN',
        'value': 123.0
    },
    'missionProfileArn': 'string',
    'postPassEndTime': datetime(2015, 1, 1),
    'prePassStartTime': datetime(2015, 1, 1),
    'region': 'string',
    'satelliteArn': 'string',
    'startTime': datetime(2015, 1, 1),
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
contactId (string) --UUID of a contact.

contactStatus (string) --Status of a contact.

endTime (datetime) --End time of a contact.

errorMessage (string) --Error message for a contact.

groundStation (string) --Ground station for a contact.

maximumElevation (dict) --Maximum elevation angle of a contact.

unit (string) --Elevation angle units.

value (float) --Elevation angle value.



missionProfileArn (string) --ARN of a mission profile.

postPassEndTime (datetime) --Amount of time after a contact ends that you\xe2\x80\x99d like to receive a CloudWatch event indicating the pass has finished.

prePassStartTime (datetime) --Amount of time prior to contact start you\xe2\x80\x99d like to receive a CloudWatch event indicating an upcoming pass.

region (string) --Region of a contact.

satelliteArn (string) --ARN of a satellite.

startTime (datetime) --Start time of a contact.

tags (dict) --Tags assigned to a contact.

(string) --
(string) --









Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'contactId': 'string',
        'contactStatus': 'AVAILABLE'|'AWS_CANCELLED'|'CANCELLED'|'CANCELLING'|'COMPLETED'|'FAILED'|'FAILED_TO_SCHEDULE'|'PASS'|'POSTPASS'|'PREPASS'|'SCHEDULED'|'SCHEDULING',
        'endTime': datetime(2015, 1, 1),
        'errorMessage': 'string',
        'groundStation': 'string',
        'maximumElevation': {
            'unit': 'DEGREE_ANGLE'|'RADIAN',
            'value': 123.0
        },
        'missionProfileArn': 'string',
        'postPassEndTime': datetime(2015, 1, 1),
        'prePassStartTime': datetime(2015, 1, 1),
        'region': 'string',
        'satelliteArn': 'string',
        'startTime': datetime(2015, 1, 1),
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
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

def get_config(configId=None, configType=None):
    """
    Returns Config information.
    Only one Config response can be returned.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_config(
        configId='string',
        configType='antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo'
    )
    
    
    :type configId: string
    :param configId: [REQUIRED]\nUUID of a Config .\n

    :type configType: string
    :param configType: [REQUIRED]\nType of a Config .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'configArn': 'string',
    'configData': {
        'antennaDownlinkConfig': {
            'spectrumConfig': {
                'bandwidth': {
                    'units': 'GHz'|'MHz'|'kHz',
                    'value': 123.0
                },
                'centerFrequency': {
                    'units': 'GHz'|'MHz'|'kHz',
                    'value': 123.0
                },
                'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
            }
        },
        'antennaDownlinkDemodDecodeConfig': {
            'decodeConfig': {
                'unvalidatedJSON': 'string'
            },
            'demodulationConfig': {
                'unvalidatedJSON': 'string'
            },
            'spectrumConfig': {
                'bandwidth': {
                    'units': 'GHz'|'MHz'|'kHz',
                    'value': 123.0
                },
                'centerFrequency': {
                    'units': 'GHz'|'MHz'|'kHz',
                    'value': 123.0
                },
                'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
            }
        },
        'antennaUplinkConfig': {
            'spectrumConfig': {
                'centerFrequency': {
                    'units': 'GHz'|'MHz'|'kHz',
                    'value': 123.0
                },
                'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
            },
            'targetEirp': {
                'units': 'dBW',
                'value': 123.0
            }
        },
        'dataflowEndpointConfig': {
            'dataflowEndpointName': 'string',
            'dataflowEndpointRegion': 'string'
        },
        'trackingConfig': {
            'autotrack': 'PREFERRED'|'REMOVED'|'REQUIRED'
        },
        'uplinkEchoConfig': {
            'antennaUplinkConfigArn': 'string',
            'enabled': True|False
        }
    },
    'configId': 'string',
    'configType': 'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo',
    'name': 'string',
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --

configArn (string) --
ARN of a Config

configData (dict) --
Data elements in a Config .

antennaDownlinkConfig (dict) --
Information about how AWS Ground Station should configure an antenna for downlink during a contact.

spectrumConfig (dict) --
Object that describes a spectral Config .

bandwidth (dict) --
Bandwidth of a spectral Config .

units (string) --
Frequency bandwidth units.

value (float) --
Frequency bandwidth value.



centerFrequency (dict) --
Center frequency of a spectral Config .

units (string) --
Frequency units.

value (float) --
Frequency value.



polarization (string) --
Polarization of a spectral Config .





antennaDownlinkDemodDecodeConfig (dict) --
Information about how AWS Ground Station should con\xef\xac\x81gure an antenna for downlink demod decode during a contact.

decodeConfig (dict) --
Information about the decode Config .

unvalidatedJSON (string) --
Unvalidated JSON of a decode Config .



demodulationConfig (dict) --
Information about the demodulation Config .

unvalidatedJSON (string) --
Unvalidated JSON of a demodulation Config .



spectrumConfig (dict) --
Information about the spectral Config .

bandwidth (dict) --
Bandwidth of a spectral Config .

units (string) --
Frequency bandwidth units.

value (float) --
Frequency bandwidth value.



centerFrequency (dict) --
Center frequency of a spectral Config .

units (string) --
Frequency units.

value (float) --
Frequency value.



polarization (string) --
Polarization of a spectral Config .





antennaUplinkConfig (dict) --
Information about how AWS Ground Station should con\xef\xac\x81gure an antenna for uplink during a contact.

spectrumConfig (dict) --
Information about the uplink spectral Config .

centerFrequency (dict) --
Center frequency of an uplink spectral Config .

units (string) --
Frequency units.

value (float) --
Frequency value.



polarization (string) --
Polarization of an uplink spectral Config .



targetEirp (dict) --
EIRP of the target.

units (string) --
Units of an EIRP.

value (float) --
Value of an EIRP.





dataflowEndpointConfig (dict) --
Information about the dataflow endpoint Config .

dataflowEndpointName (string) --
Name of a dataflow endpoint.

dataflowEndpointRegion (string) --
Region of a dataflow endpoint.



trackingConfig (dict) --
Object that determines whether tracking should be used during a contact executed with this Config in the mission profile.

autotrack (string) --
Current setting for autotrack.



uplinkEchoConfig (dict) --
Information about an uplink echo Config .
Parameters from the AntennaUplinkConfig , corresponding to the specified AntennaUplinkConfigArn , are used when this UplinkEchoConfig is used in a contact.

antennaUplinkConfigArn (string) --
ARN of an uplink Config .

enabled (boolean) --
Whether or not an uplink Config is enabled.





configId (string) --
UUID of a Config .

configType (string) --
Type of a Config .

name (string) --
Name of a Config .

tags (dict) --
Tags assigned to a Config .

(string) --
(string) --










Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'configArn': 'string',
        'configData': {
            'antennaDownlinkConfig': {
                'spectrumConfig': {
                    'bandwidth': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'centerFrequency': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                }
            },
            'antennaDownlinkDemodDecodeConfig': {
                'decodeConfig': {
                    'unvalidatedJSON': 'string'
                },
                'demodulationConfig': {
                    'unvalidatedJSON': 'string'
                },
                'spectrumConfig': {
                    'bandwidth': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'centerFrequency': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                }
            },
            'antennaUplinkConfig': {
                'spectrumConfig': {
                    'centerFrequency': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                },
                'targetEirp': {
                    'units': 'dBW',
                    'value': 123.0
                }
            },
            'dataflowEndpointConfig': {
                'dataflowEndpointName': 'string',
                'dataflowEndpointRegion': 'string'
            },
            'trackingConfig': {
                'autotrack': 'PREFERRED'|'REMOVED'|'REQUIRED'
            },
            'uplinkEchoConfig': {
                'antennaUplinkConfigArn': 'string',
                'enabled': True|False
            }
        },
        'configId': 'string',
        'configType': 'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo',
        'name': 'string',
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def get_dataflow_endpoint_group(dataflowEndpointGroupId=None):
    """
    Returns the dataflow endpoint group.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_dataflow_endpoint_group(
        dataflowEndpointGroupId='string'
    )
    
    
    :type dataflowEndpointGroupId: string
    :param dataflowEndpointGroupId: [REQUIRED]\nUUID of a dataflow endpoint group.\n

    :rtype: dict
ReturnsResponse Syntax{
    'dataflowEndpointGroupArn': 'string',
    'dataflowEndpointGroupId': 'string',
    'endpointsDetails': [
        {
            'endpoint': {
                'address': {
                    'name': 'string',
                    'port': 123
                },
                'name': 'string',
                'status': 'created'|'creating'|'deleted'|'deleting'|'failed'
            },
            'securityDetails': {
                'roleArn': 'string',
                'securityGroupIds': [
                    'string',
                ],
                'subnetIds': [
                    'string',
                ]
            }
        },
    ],
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
dataflowEndpointGroupArn (string) --ARN of a dataflow endpoint group.

dataflowEndpointGroupId (string) --UUID of a dataflow endpoint group.

endpointsDetails (list) --Details of a dataflow endpoint.

(dict) --Information about the endpoint details.

endpoint (dict) --A dataflow endpoint.

address (dict) --Socket address of a dataflow endpoint.

name (string) --Name of a socket address.

port (integer) --Port of a socket address.



name (string) --Name of a dataflow endpoint.

status (string) --Status of a dataflow endpoint.



securityDetails (dict) --Endpoint security details.

roleArn (string) --ARN to a role needed for connecting streams to your instances.

securityGroupIds (list) --The security groups to attach to the elastic network interfaces.

(string) --


subnetIds (list) --A list of subnets where AWS Ground Station places elastic network interfaces to send streams to your instances.

(string) --








tags (dict) --Tags assigned to a dataflow endpoint group.

(string) --
(string) --









Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'dataflowEndpointGroupArn': 'string',
        'dataflowEndpointGroupId': 'string',
        'endpointsDetails': [
            {
                'endpoint': {
                    'address': {
                        'name': 'string',
                        'port': 123
                    },
                    'name': 'string',
                    'status': 'created'|'creating'|'deleted'|'deleting'|'failed'
                },
                'securityDetails': {
                    'roleArn': 'string',
                    'securityGroupIds': [
                        'string',
                    ],
                    'subnetIds': [
                        'string',
                    ]
                }
            },
        ],
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def get_minute_usage(month=None, year=None):
    """
    Returns the number of minutes used by account.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_minute_usage(
        month=123,
        year=123
    )
    
    
    :type month: integer
    :param month: [REQUIRED]\nThe month being requested, with a value of 1-12.\n

    :type year: integer
    :param year: [REQUIRED]\nThe year being requested, in the format of YYYY.\n

    :rtype: dict

ReturnsResponse Syntax
{
    'estimatedMinutesRemaining': 123,
    'isReservedMinutesCustomer': True|False,
    'totalReservedMinuteAllocation': 123,
    'totalScheduledMinutes': 123,
    'upcomingMinutesScheduled': 123
}


Response Structure

(dict) --

estimatedMinutesRemaining (integer) --
Estimated number of minutes remaining for an account, specific to the month being requested.

isReservedMinutesCustomer (boolean) --
Returns whether or not an account has signed up for the reserved minutes pricing plan, specific to the month being requested.

totalReservedMinuteAllocation (integer) --
Total number of reserved minutes allocated, specific to the month being requested.

totalScheduledMinutes (integer) --
Total scheduled minutes for an account, specific to the month being requested.

upcomingMinutesScheduled (integer) --
Upcoming minutes scheduled for an account, specific to the month being requested.







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'estimatedMinutesRemaining': 123,
        'isReservedMinutesCustomer': True|False,
        'totalReservedMinuteAllocation': 123,
        'totalScheduledMinutes': 123,
        'upcomingMinutesScheduled': 123
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def get_mission_profile(missionProfileId=None):
    """
    Returns a mission profile.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_mission_profile(
        missionProfileId='string'
    )
    
    
    :type missionProfileId: string
    :param missionProfileId: [REQUIRED]\nUUID of a mission profile.\n

    :rtype: dict
ReturnsResponse Syntax{
    'contactPostPassDurationSeconds': 123,
    'contactPrePassDurationSeconds': 123,
    'dataflowEdges': [
        [
            'string',
        ],
    ],
    'minimumViableContactDurationSeconds': 123,
    'missionProfileArn': 'string',
    'missionProfileId': 'string',
    'name': 'string',
    'region': 'string',
    'tags': {
        'string': 'string'
    },
    'trackingConfigArn': 'string'
}


Response Structure

(dict) --
contactPostPassDurationSeconds (integer) --Amount of time after a contact ends that you\xe2\x80\x99d like to receive a CloudWatch event indicating the pass has finished.

contactPrePassDurationSeconds (integer) --Amount of time prior to contact start you\xe2\x80\x99d like to receive a CloudWatch event indicating an upcoming pass.

dataflowEdges (list) --A list of lists of ARNs. Each list of ARNs is an edge, with a from Config and a to Config .

(list) --
(string) --




minimumViableContactDurationSeconds (integer) --Smallest amount of time in seconds that you\xe2\x80\x99d like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.

missionProfileArn (string) --ARN of a mission profile.

missionProfileId (string) --UUID of a mission profile.

name (string) --Name of a mission profile.

region (string) --Region of a mission profile.

tags (dict) --Tags assigned to a mission profile.

(string) --
(string) --




trackingConfigArn (string) --ARN of a tracking Config .






Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'contactPostPassDurationSeconds': 123,
        'contactPrePassDurationSeconds': 123,
        'dataflowEdges': [
            [
                'string',
            ],
        ],
        'minimumViableContactDurationSeconds': 123,
        'missionProfileArn': 'string',
        'missionProfileId': 'string',
        'name': 'string',
        'region': 'string',
        'tags': {
            'string': 'string'
        },
        'trackingConfigArn': 'string'
    }
    
    
    :returns: 
    (string) --
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

def get_satellite(satelliteId=None):
    """
    Returns a satellite.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.get_satellite(
        satelliteId='string'
    )
    
    
    :type satelliteId: string
    :param satelliteId: [REQUIRED]\nUUID of a satellite.\n

    :rtype: dict
ReturnsResponse Syntax{
    'groundStations': [
        'string',
    ],
    'noradSatelliteID': 123,
    'satelliteArn': 'string',
    'satelliteId': 'string'
}


Response Structure

(dict) --
groundStations (list) --A list of ground stations to which the satellite is on-boarded.

(string) --


noradSatelliteID (integer) --NORAD satellite ID number.

satelliteArn (string) --ARN of a satellite.

satelliteId (string) --UUID of a satellite.






Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'groundStations': [
            'string',
        ],
        'noradSatelliteID': 123,
        'satelliteArn': 'string',
        'satelliteId': 'string'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
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

def list_configs(maxResults=None, nextToken=None):
    """
    Returns a list of Config objects.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_configs(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: Maximum number of Configs returned.

    :type nextToken: string
    :param nextToken: Next token returned in the request of a previous ListConfigs call. Used to get the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'configList': [
        {
            'configArn': 'string',
            'configId': 'string',
            'configType': 'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo',
            'name': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

configList (list) --
List of Config items.

(dict) --
An item in a list of Config objects.

configArn (string) --
ARN of a Config .

configId (string) --
UUID of a Config .

configType (string) --
Type of a Config .

name (string) --
Name of a Config .





nextToken (string) --
Next token returned in the response of a previous ListConfigs call. Used to get the next page of results.







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'configList': [
            {
                'configArn': 'string',
                'configId': 'string',
                'configType': 'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo',
                'name': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_contacts(endTime=None, groundStation=None, maxResults=None, missionProfileArn=None, nextToken=None, satelliteArn=None, startTime=None, statusList=None):
    """
    Returns a list of contacts.
    If statusList contains AVAILABLE, the request must include groundStation , missionprofileArn , and satelliteArn .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_contacts(
        endTime=datetime(2015, 1, 1),
        groundStation='string',
        maxResults=123,
        missionProfileArn='string',
        nextToken='string',
        satelliteArn='string',
        startTime=datetime(2015, 1, 1),
        statusList=[
            'AVAILABLE'|'AWS_CANCELLED'|'CANCELLED'|'CANCELLING'|'COMPLETED'|'FAILED'|'FAILED_TO_SCHEDULE'|'PASS'|'POSTPASS'|'PREPASS'|'SCHEDULED'|'SCHEDULING',
        ]
    )
    
    
    :type endTime: datetime
    :param endTime: [REQUIRED]\nEnd time of a contact.\n

    :type groundStation: string
    :param groundStation: Name of a ground station.

    :type maxResults: integer
    :param maxResults: Maximum number of contacts returned.

    :type missionProfileArn: string
    :param missionProfileArn: ARN of a mission profile.

    :type nextToken: string
    :param nextToken: Next token returned in the request of a previous ListContacts call. Used to get the next page of results.

    :type satelliteArn: string
    :param satelliteArn: ARN of a satellite.

    :type startTime: datetime
    :param startTime: [REQUIRED]\nStart time of a contact.\n

    :type statusList: list
    :param statusList: [REQUIRED]\nStatus of a contact reservation.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'contactList': [
        {
            'contactId': 'string',
            'contactStatus': 'AVAILABLE'|'AWS_CANCELLED'|'CANCELLED'|'CANCELLING'|'COMPLETED'|'FAILED'|'FAILED_TO_SCHEDULE'|'PASS'|'POSTPASS'|'PREPASS'|'SCHEDULED'|'SCHEDULING',
            'endTime': datetime(2015, 1, 1),
            'errorMessage': 'string',
            'groundStation': 'string',
            'maximumElevation': {
                'unit': 'DEGREE_ANGLE'|'RADIAN',
                'value': 123.0
            },
            'missionProfileArn': 'string',
            'postPassEndTime': datetime(2015, 1, 1),
            'prePassStartTime': datetime(2015, 1, 1),
            'region': 'string',
            'satelliteArn': 'string',
            'startTime': datetime(2015, 1, 1),
            'tags': {
                'string': 'string'
            }
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

contactList (list) --
List of contacts.

(dict) --
Data describing a contact.

contactId (string) --
UUID of a contact.

contactStatus (string) --
Status of a contact.

endTime (datetime) --
End time of a contact.

errorMessage (string) --
Error message of a contact.

groundStation (string) --
Name of a ground station.

maximumElevation (dict) --
Maximum elevation angle of a contact.

unit (string) --
Elevation angle units.

value (float) --
Elevation angle value.



missionProfileArn (string) --
ARN of a mission profile.

postPassEndTime (datetime) --
Amount of time after a contact ends that you\xe2\x80\x99d like to receive a CloudWatch event indicating the pass has finished.

prePassStartTime (datetime) --
Amount of time prior to contact start you\xe2\x80\x99d like to receive a CloudWatch event indicating an upcoming pass.

region (string) --
Region of a contact.

satelliteArn (string) --
ARN of a satellite.

startTime (datetime) --
Start time of a contact.

tags (dict) --
Tags assigned to a contact.

(string) --
(string) --








nextToken (string) --
Next token returned in the response of a previous ListContacts call. Used to get the next page of results.







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'contactList': [
            {
                'contactId': 'string',
                'contactStatus': 'AVAILABLE'|'AWS_CANCELLED'|'CANCELLED'|'CANCELLING'|'COMPLETED'|'FAILED'|'FAILED_TO_SCHEDULE'|'PASS'|'POSTPASS'|'PREPASS'|'SCHEDULED'|'SCHEDULING',
                'endTime': datetime(2015, 1, 1),
                'errorMessage': 'string',
                'groundStation': 'string',
                'maximumElevation': {
                    'unit': 'DEGREE_ANGLE'|'RADIAN',
                    'value': 123.0
                },
                'missionProfileArn': 'string',
                'postPassEndTime': datetime(2015, 1, 1),
                'prePassStartTime': datetime(2015, 1, 1),
                'region': 'string',
                'satelliteArn': 'string',
                'startTime': datetime(2015, 1, 1),
                'tags': {
                    'string': 'string'
                }
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    (string) --
    (string) --
    
    
    
    """
    pass

def list_dataflow_endpoint_groups(maxResults=None, nextToken=None):
    """
    Returns a list of DataflowEndpoint groups.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_dataflow_endpoint_groups(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: Maximum number of dataflow endpoint groups returned.

    :type nextToken: string
    :param nextToken: Next token returned in the request of a previous ListDataflowEndpointGroups call. Used to get the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'dataflowEndpointGroupList': [
        {
            'dataflowEndpointGroupArn': 'string',
            'dataflowEndpointGroupId': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

dataflowEndpointGroupList (list) --
A list of dataflow endpoint groups.

(dict) --
Item in a list of DataflowEndpoint groups.

dataflowEndpointGroupArn (string) --
ARN of a dataflow endpoint group.

dataflowEndpointGroupId (string) --
UUID of a dataflow endpoint group.





nextToken (string) --
Next token returned in the response of a previous ListDataflowEndpointGroups call. Used to get the next page of results.







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'dataflowEndpointGroupList': [
            {
                'dataflowEndpointGroupArn': 'string',
                'dataflowEndpointGroupId': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_ground_stations(maxResults=None, nextToken=None, satelliteId=None):
    """
    Returns a list of ground stations.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_ground_stations(
        maxResults=123,
        nextToken='string',
        satelliteId='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: Maximum number of ground stations returned.

    :type nextToken: string
    :param nextToken: Next token that can be supplied in the next call to get the next page of ground stations.

    :type satelliteId: string
    :param satelliteId: Satellite ID to retrieve on-boarded ground stations.

    :rtype: dict

ReturnsResponse Syntax
{
    'groundStationList': [
        {
            'groundStationId': 'string',
            'groundStationName': 'string',
            'region': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

groundStationList (list) --
List of ground stations.

(dict) --
Information about the ground station data.

groundStationId (string) --
UUID of a ground station.

groundStationName (string) --
Name of a ground station.

region (string) --
Ground station Region.





nextToken (string) --
Next token that can be supplied in the next call to get the next page of ground stations.







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'groundStationList': [
            {
                'groundStationId': 'string',
                'groundStationName': 'string',
                'region': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_mission_profiles(maxResults=None, nextToken=None):
    """
    Returns a list of mission profiles.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_mission_profiles(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: Maximum number of mission profiles returned.

    :type nextToken: string
    :param nextToken: Next token returned in the request of a previous ListMissionProfiles call. Used to get the next page of results.

    :rtype: dict

ReturnsResponse Syntax
{
    'missionProfileList': [
        {
            'missionProfileArn': 'string',
            'missionProfileId': 'string',
            'name': 'string',
            'region': 'string'
        },
    ],
    'nextToken': 'string'
}


Response Structure

(dict) --

missionProfileList (list) --
List of mission profiles.

(dict) --
Item in a list of mission profiles.

missionProfileArn (string) --
ARN of a mission profile.

missionProfileId (string) --
UUID of a mission profile.

name (string) --
Name of a mission profile.

region (string) --
Region of a mission profile.





nextToken (string) --
Next token returned in the response of a previous ListMissionProfiles call. Used to get the next page of results.







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'missionProfileList': [
            {
                'missionProfileArn': 'string',
                'missionProfileId': 'string',
                'name': 'string',
                'region': 'string'
            },
        ],
        'nextToken': 'string'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def list_satellites(maxResults=None, nextToken=None):
    """
    Returns a list of satellites.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_satellites(
        maxResults=123,
        nextToken='string'
    )
    
    
    :type maxResults: integer
    :param maxResults: Maximum number of satellites returned.

    :type nextToken: string
    :param nextToken: Next token that can be supplied in the next call to get the next page of satellites.

    :rtype: dict

ReturnsResponse Syntax
{
    'nextToken': 'string',
    'satellites': [
        {
            'groundStations': [
                'string',
            ],
            'noradSatelliteID': 123,
            'satelliteArn': 'string',
            'satelliteId': 'string'
        },
    ]
}


Response Structure

(dict) --

nextToken (string) --
Next token that can be supplied in the next call to get the next page of satellites.

satellites (list) --
List of satellites.

(dict) --
Item in a list of satellites.

groundStations (list) --
A list of ground stations to which the satellite is on-boarded.

(string) --


noradSatelliteID (integer) --
NORAD satellite ID number.

satelliteArn (string) --
ARN of a satellite.

satelliteId (string) --
UUID of a satellite.











Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'nextToken': 'string',
        'satellites': [
            {
                'groundStations': [
                    'string',
                ],
                'noradSatelliteID': 123,
                'satelliteArn': 'string',
                'satelliteId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (string) --
    
    """
    pass

def list_tags_for_resource(resourceArn=None):
    """
    Returns a list of tags for a specified resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        resourceArn='string'
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nARN of a resource.\n

    :rtype: dict
ReturnsResponse Syntax{
    'tags': {
        'string': 'string'
    }
}


Response Structure

(dict) --
tags (dict) --Tags assigned to a resource.

(string) --
(string) --









Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def reserve_contact(endTime=None, groundStation=None, missionProfileArn=None, satelliteArn=None, startTime=None, tags=None):
    """
    Reserves a contact using specified parameters.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.reserve_contact(
        endTime=datetime(2015, 1, 1),
        groundStation='string',
        missionProfileArn='string',
        satelliteArn='string',
        startTime=datetime(2015, 1, 1),
        tags={
            'string': 'string'
        }
    )
    
    
    :type endTime: datetime
    :param endTime: [REQUIRED]\nEnd time of a contact.\n

    :type groundStation: string
    :param groundStation: [REQUIRED]\nName of a ground station.\n

    :type missionProfileArn: string
    :param missionProfileArn: [REQUIRED]\nARN of a mission profile.\n

    :type satelliteArn: string
    :param satelliteArn: [REQUIRED]\nARN of a satellite\n

    :type startTime: datetime
    :param startTime: [REQUIRED]\nStart time of a contact.\n

    :type tags: dict
    :param tags: Tags assigned to a contact.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'contactId': 'string'
}


Response Structure

(dict) --

contactId (string) --
UUID of a contact.







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'contactId': 'string'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def tag_resource(resourceArn=None, tags=None):
    """
    Assigns a tag to a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        resourceArn='string',
        tags={
            'string': 'string'
        }
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nARN of a resource tag.\n

    :type tags: dict
    :param tags: [REQUIRED]\nTags assigned to a resource.\n\n(string) --\n(string) --\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def untag_resource(resourceArn=None, tagKeys=None):
    """
    Deassigns a resource tag.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        resourceArn='string',
        tagKeys=[
            'string',
        ]
    )
    
    
    :type resourceArn: string
    :param resourceArn: [REQUIRED]\nARN of a resource.\n

    :type tagKeys: list
    :param tagKeys: [REQUIRED]\nKeys of a resource tag.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{}


Response Structure

(dict) --




Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {}
    
    
    :returns: 
    (dict) --
    
    """
    pass

def update_config(configData=None, configId=None, configType=None, name=None):
    """
    Updates the Config used when scheduling contacts.
    Updating a Config will not update the execution parameters for existing future contacts scheduled with this Config .
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_config(
        configData={
            'antennaDownlinkConfig': {
                'spectrumConfig': {
                    'bandwidth': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'centerFrequency': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                }
            },
            'antennaDownlinkDemodDecodeConfig': {
                'decodeConfig': {
                    'unvalidatedJSON': 'string'
                },
                'demodulationConfig': {
                    'unvalidatedJSON': 'string'
                },
                'spectrumConfig': {
                    'bandwidth': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'centerFrequency': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                }
            },
            'antennaUplinkConfig': {
                'spectrumConfig': {
                    'centerFrequency': {
                        'units': 'GHz'|'MHz'|'kHz',
                        'value': 123.0
                    },
                    'polarization': 'LEFT_HAND'|'NONE'|'RIGHT_HAND'
                },
                'targetEirp': {
                    'units': 'dBW',
                    'value': 123.0
                }
            },
            'dataflowEndpointConfig': {
                'dataflowEndpointName': 'string',
                'dataflowEndpointRegion': 'string'
            },
            'trackingConfig': {
                'autotrack': 'PREFERRED'|'REMOVED'|'REQUIRED'
            },
            'uplinkEchoConfig': {
                'antennaUplinkConfigArn': 'string',
                'enabled': True|False
            }
        },
        configId='string',
        configType='antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo',
        name='string'
    )
    
    
    :type configData: dict
    :param configData: [REQUIRED]\nParameters of a Config .\n\nantennaDownlinkConfig (dict) --Information about how AWS Ground Station should configure an antenna for downlink during a contact.\n\nspectrumConfig (dict) -- [REQUIRED]Object that describes a spectral Config .\n\nbandwidth (dict) -- [REQUIRED]Bandwidth of a spectral Config .\n\nunits (string) -- [REQUIRED]Frequency bandwidth units.\n\nvalue (float) -- [REQUIRED]Frequency bandwidth value.\n\n\n\ncenterFrequency (dict) -- [REQUIRED]Center frequency of a spectral Config .\n\nunits (string) -- [REQUIRED]Frequency units.\n\nvalue (float) -- [REQUIRED]Frequency value.\n\n\n\npolarization (string) --Polarization of a spectral Config .\n\n\n\n\n\nantennaDownlinkDemodDecodeConfig (dict) --Information about how AWS Ground Station should con\xef\xac\x81gure an antenna for downlink demod decode during a contact.\n\ndecodeConfig (dict) -- [REQUIRED]Information about the decode Config .\n\nunvalidatedJSON (string) -- [REQUIRED]Unvalidated JSON of a decode Config .\n\n\n\ndemodulationConfig (dict) -- [REQUIRED]Information about the demodulation Config .\n\nunvalidatedJSON (string) -- [REQUIRED]Unvalidated JSON of a demodulation Config .\n\n\n\nspectrumConfig (dict) -- [REQUIRED]Information about the spectral Config .\n\nbandwidth (dict) -- [REQUIRED]Bandwidth of a spectral Config .\n\nunits (string) -- [REQUIRED]Frequency bandwidth units.\n\nvalue (float) -- [REQUIRED]Frequency bandwidth value.\n\n\n\ncenterFrequency (dict) -- [REQUIRED]Center frequency of a spectral Config .\n\nunits (string) -- [REQUIRED]Frequency units.\n\nvalue (float) -- [REQUIRED]Frequency value.\n\n\n\npolarization (string) --Polarization of a spectral Config .\n\n\n\n\n\nantennaUplinkConfig (dict) --Information about how AWS Ground Station should con\xef\xac\x81gure an antenna for uplink during a contact.\n\nspectrumConfig (dict) -- [REQUIRED]Information about the uplink spectral Config .\n\ncenterFrequency (dict) -- [REQUIRED]Center frequency of an uplink spectral Config .\n\nunits (string) -- [REQUIRED]Frequency units.\n\nvalue (float) -- [REQUIRED]Frequency value.\n\n\n\npolarization (string) --Polarization of an uplink spectral Config .\n\n\n\ntargetEirp (dict) -- [REQUIRED]EIRP of the target.\n\nunits (string) -- [REQUIRED]Units of an EIRP.\n\nvalue (float) -- [REQUIRED]Value of an EIRP.\n\n\n\n\n\ndataflowEndpointConfig (dict) --Information about the dataflow endpoint Config .\n\ndataflowEndpointName (string) -- [REQUIRED]Name of a dataflow endpoint.\n\ndataflowEndpointRegion (string) --Region of a dataflow endpoint.\n\n\n\ntrackingConfig (dict) --Object that determines whether tracking should be used during a contact executed with this Config in the mission profile.\n\nautotrack (string) -- [REQUIRED]Current setting for autotrack.\n\n\n\nuplinkEchoConfig (dict) --Information about an uplink echo Config .\nParameters from the AntennaUplinkConfig , corresponding to the specified AntennaUplinkConfigArn , are used when this UplinkEchoConfig is used in a contact.\n\nantennaUplinkConfigArn (string) -- [REQUIRED]ARN of an uplink Config .\n\nenabled (boolean) -- [REQUIRED]Whether or not an uplink Config is enabled.\n\n\n\n\n

    :type configId: string
    :param configId: [REQUIRED]\nUUID of a Config .\n

    :type configType: string
    :param configType: [REQUIRED]\nType of a Config .\n

    :type name: string
    :param name: [REQUIRED]\nName of a Config .\n

    :rtype: dict

ReturnsResponse Syntax
{
    'configArn': 'string',
    'configId': 'string',
    'configType': 'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo'
}


Response Structure

(dict) --

configArn (string) --
ARN of a Config .

configId (string) --
UUID of a Config .

configType (string) --
Type of a Config .







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'configArn': 'string',
        'configId': 'string',
        'configType': 'antenna-downlink'|'antenna-downlink-demod-decode'|'antenna-uplink'|'dataflow-endpoint'|'tracking'|'uplink-echo'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

def update_mission_profile(contactPostPassDurationSeconds=None, contactPrePassDurationSeconds=None, dataflowEdges=None, minimumViableContactDurationSeconds=None, missionProfileId=None, name=None, trackingConfigArn=None):
    """
    Updates a mission profile.
    Updating a mission profile will not update the execution parameters for existing future contacts.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_mission_profile(
        contactPostPassDurationSeconds=123,
        contactPrePassDurationSeconds=123,
        dataflowEdges=[
            [
                'string',
            ],
        ],
        minimumViableContactDurationSeconds=123,
        missionProfileId='string',
        name='string',
        trackingConfigArn='string'
    )
    
    
    :type contactPostPassDurationSeconds: integer
    :param contactPostPassDurationSeconds: Amount of time after a contact ends that you\xe2\x80\x99d like to receive a CloudWatch event indicating the pass has finished.

    :type contactPrePassDurationSeconds: integer
    :param contactPrePassDurationSeconds: Amount of time after a contact ends that you\xe2\x80\x99d like to receive a CloudWatch event indicating the pass has finished.

    :type dataflowEdges: list
    :param dataflowEdges: A list of lists of ARNs. Each list of ARNs is an edge, with a from Config and a to Config .\n\n(list) --\n(string) --\n\n\n\n

    :type minimumViableContactDurationSeconds: integer
    :param minimumViableContactDurationSeconds: Smallest amount of time in seconds that you\xe2\x80\x99d like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.

    :type missionProfileId: string
    :param missionProfileId: [REQUIRED]\nUUID of a mission profile.\n

    :type name: string
    :param name: Name of a mission profile.

    :type trackingConfigArn: string
    :param trackingConfigArn: ARN of a tracking Config .

    :rtype: dict

ReturnsResponse Syntax
{
    'missionProfileId': 'string'
}


Response Structure

(dict) --

missionProfileId (string) --
UUID of a mission profile.







Exceptions

GroundStation.Client.exceptions.InvalidParameterException
GroundStation.Client.exceptions.DependencyException
GroundStation.Client.exceptions.ResourceNotFoundException


    :return: {
        'missionProfileId': 'string'
    }
    
    
    :returns: 
    GroundStation.Client.exceptions.InvalidParameterException
    GroundStation.Client.exceptions.DependencyException
    GroundStation.Client.exceptions.ResourceNotFoundException
    
    """
    pass

