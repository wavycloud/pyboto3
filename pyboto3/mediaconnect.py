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

def add_flow_outputs(FlowArn=None, Outputs=None):
    """
    Adds outputs to an existing flow. You can create up to 50 outputs per flow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_flow_outputs(
        FlowArn='string',
        Outputs=[
            {
                'CidrAllowList': [
                    'string',
                ],
                'Description': 'string',
                'Destination': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'MaxLatency': 123,
                'Name': 'string',
                'Port': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'RemoteId': 'string',
                'SmoothingLatency': 123,
                'StreamId': 'string',
                'VpcInterfaceAttachment': {
                    'VpcInterfaceName': 'string'
                }
            },
        ]
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to add outputs to.

    :type Outputs: list
    :param Outputs: [REQUIRED] A list of outputs that you want to add.\n\n(dict) -- The output that you want to add to this flow.\nCidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.\n(string) --\n\n\nDescription (string) -- A description of the output. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the end user.\nDestination (string) -- The IP address from which video will be sent to output destinations.\nEncryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nAlgorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).\nConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.\nDeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nKeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nRegion (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nRoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).\nSecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.\nUrl (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.\n\n\nMaxLatency (integer) -- The maximum latency in milliseconds for Zixi-based streams.\nName (string) -- The name of the output. This value must be unique within the current flow.\nPort (integer) -- The port to use when content is distributed to this output.\nProtocol (string) -- [REQUIRED] The protocol to use for the output.\nRemoteId (string) -- The remote ID for the Zixi-pull output stream.\nSmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.\nStreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.\nVpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.\nVpcInterfaceName (string) -- The name of the VPC interface to use for this output.\n\n\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FlowArn': 'string',
    'Outputs': [
        {
            'DataTransferSubscriberFeePercent': 123,
            'Description': 'string',
            'Destination': 'string',
            'Encryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'ConstantInitializationVector': 'string',
                'DeviceId': 'string',
                'KeyType': 'speke'|'static-key',
                'Region': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SecretArn': 'string',
                'Url': 'string'
            },
            'EntitlementArn': 'string',
            'MediaLiveInputArn': 'string',
            'Name': 'string',
            'OutputArn': 'string',
            'Port': 123,
            'Transport': {
                'CidrAllowList': [
                    'string',
                ],
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'RemoteId': 'string',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            },
            'VpcInterfaceAttachment': {
                'VpcInterfaceName': 'string'
            }
        },
    ]
}


Response Structure

(dict) -- AWS Elemental MediaConnect added the outputs successfully.
FlowArn (string) -- The ARN of the flow that these outputs were added to.
Outputs (list) -- The details of the newly added outputs.
(dict) -- The settings for an output.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Description (string) -- A description of the output.
Destination (string) -- The address where you want to send the output.
Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementArn (string) -- The ARN of the entitlement on the originator\'\'s flow. This value is relevant only on entitled flows.
MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
Name (string) -- The name of the output. This value must be unique within the current flow.
OutputArn (string) -- The ARN of the output.
Port (integer) -- The port to use when content is distributed to this output.
Transport (dict) -- Attributes related to the transport stream that are used in the output.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.
VpcInterfaceName (string) -- The name of the VPC interface to use for this output.












Exceptions

MediaConnect.Client.exceptions.AddFlowOutputs420Exception
MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'Outputs': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Description': 'string',
                'Destination': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'EntitlementArn': 'string',
                'MediaLiveInputArn': 'string',
                'Name': 'string',
                'OutputArn': 'string',
                'Port': 123,
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceAttachment': {
                    'VpcInterfaceName': 'string'
                }
            },
        ]
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect added the outputs successfully.
    FlowArn (string) -- The ARN of the flow that these outputs were added to.
    Outputs (list) -- The details of the newly added outputs.
    (dict) -- The settings for an output.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Description (string) -- A description of the output.
    Destination (string) -- The address where you want to send the output.
    Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    EntitlementArn (string) -- The ARN of the entitlement on the originator\'\'s flow. This value is relevant only on entitled flows.
    MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
    Name (string) -- The name of the output. This value must be unique within the current flow.
    OutputArn (string) -- The ARN of the output.
    Port (integer) -- The port to use when content is distributed to this output.
    Transport (dict) -- Attributes related to the transport stream that are used in the output.
    CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    (string) --
    
    
    MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    RemoteId (string) -- The remote ID for the Zixi-pull stream.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    VpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.
    VpcInterfaceName (string) -- The name of the VPC interface to use for this output.
    
    
    
    
    
    
    
    
    
    """
    pass

def add_flow_sources(FlowArn=None, Sources=None):
    """
    Adds Sources to flow
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_flow_sources(
        FlowArn='string',
        Sources=[
            {
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestPort': 123,
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Name': 'string',
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'StreamId': 'string',
                'VpcInterfaceName': 'string',
                'WhitelistCidr': 'string'
            },
        ]
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to mutate.

    :type Sources: list
    :param Sources: [REQUIRED] A list of sources that you want to add.\n\n(dict) -- The settings for the source of the flow.\nDecryption (dict) -- The type of encryption that is used on the content ingested from this source.\nAlgorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).\nConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.\nDeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nKeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nRegion (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nRoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).\nSecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.\nUrl (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.\n\n\nDescription (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.\nEntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator\'s flow.\nIngestPort (integer) -- The port that the flow will be listening on for incoming content.\nMaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.\nMaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.\nName (string) -- The name of the source.\nProtocol (string) -- The protocol that is used by the source.\nStreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.\nVpcInterfaceName (string) -- The name of the VPC interface to use for this source.\nWhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FlowArn': 'string',
    'Sources': [
        {
            'DataTransferSubscriberFeePercent': 123,
            'Decryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'ConstantInitializationVector': 'string',
                'DeviceId': 'string',
                'KeyType': 'speke'|'static-key',
                'Region': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SecretArn': 'string',
                'Url': 'string'
            },
            'Description': 'string',
            'EntitlementArn': 'string',
            'IngestIp': 'string',
            'IngestPort': 123,
            'Name': 'string',
            'SourceArn': 'string',
            'Transport': {
                'CidrAllowList': [
                    'string',
                ],
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'RemoteId': 'string',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            },
            'VpcInterfaceName': 'string',
            'WhitelistCidr': 'string'
        },
    ]
}


Response Structure

(dict) -- AWS Elemental MediaConnect added sources to the flow successfully.
FlowArn (string) -- The ARN of the flow that these sources were added to.
Sources (list) -- The details of the newly added sources.
(dict) -- The settings for the source of the flow.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
IngestPort (integer) -- The port that the flow will be listening on for incoming content.
Name (string) -- The name of the source.
SourceArn (string) -- The ARN of the source.
Transport (dict) -- Attributes related to the transport stream that are used in the source.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.










Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'Sources': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestIp': 'string',
                'IngestPort': 123,
                'Name': 'string',
                'SourceArn': 'string',
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceName': 'string',
                'WhitelistCidr': 'string'
            },
        ]
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect added sources to the flow successfully.
    FlowArn (string) -- The ARN of the flow that these sources were added to.
    Sources (list) -- The details of the newly added sources.
    (dict) -- The settings for the source of the flow.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
    IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
    IngestPort (integer) -- The port that the flow will be listening on for incoming content.
    Name (string) -- The name of the source.
    SourceArn (string) -- The ARN of the source.
    Transport (dict) -- Attributes related to the transport stream that are used in the source.
    CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    (string) --
    
    
    MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    RemoteId (string) -- The remote ID for the Zixi-pull stream.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
    WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    
    
    
    
    
    
    
    """
    pass

def add_flow_vpc_interfaces(FlowArn=None, VpcInterfaces=None):
    """
    Adds VPC interfaces to flow
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.add_flow_vpc_interfaces(
        FlowArn='string',
        VpcInterfaces=[
            {
                'Name': 'string',
                'RoleArn': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetId': 'string'
            },
        ]
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to mutate.

    :type VpcInterfaces: list
    :param VpcInterfaces: [REQUIRED] A list of VPC interfaces that you want to add.\n\n(dict) -- Desired VPC Interface for a Flow\nName (string) -- [REQUIRED] The name of the VPC Interface. This value must be unique within the current flow.\nRoleArn (string) -- [REQUIRED] Role Arn MediaConnect can assumes to create ENIs in customer\'s account\nSecurityGroupIds (list) -- [REQUIRED] Security Group IDs to be used on ENI.\n(string) --\n\n\nSubnetId (string) -- [REQUIRED] Subnet must be in the AZ of the Flow\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FlowArn': 'string',
    'VpcInterfaces': [
        {
            'Name': 'string',
            'NetworkInterfaceIds': [
                'string',
            ],
            'RoleArn': 'string',
            'SecurityGroupIds': [
                'string',
            ],
            'SubnetId': 'string'
        },
    ]
}


Response Structure

(dict) -- The following VPC interface was added to the Flow configuration.
FlowArn (string) -- The ARN of the flow that these VPC interfaces were added to.
VpcInterfaces (list) -- The details of the newly added VPC interfaces.
(dict) -- The settings for a VPC Source.
Name (string) -- Immutable and has to be a unique against other VpcInterfaces in this Flow
NetworkInterfaceIds (list) -- IDs of the network interfaces created in customer\'s account by MediaConnect.
(string) --


RoleArn (string) -- Role Arn MediaConnect can assumes to create ENIs in customer\'s account
SecurityGroupIds (list) -- Security Group IDs to be used on ENI.
(string) --


SubnetId (string) -- Subnet must be in the AZ of the Flow










Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'VpcInterfaces': [
            {
                'Name': 'string',
                'NetworkInterfaceIds': [
                    'string',
                ],
                'RoleArn': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetId': 'string'
            },
        ]
    }
    
    
    :returns: 
    (dict) -- The following VPC interface was added to the Flow configuration.
    FlowArn (string) -- The ARN of the flow that these VPC interfaces were added to.
    VpcInterfaces (list) -- The details of the newly added VPC interfaces.
    (dict) -- The settings for a VPC Source.
    Name (string) -- Immutable and has to be a unique against other VpcInterfaces in this Flow
    NetworkInterfaceIds (list) -- IDs of the network interfaces created in customer\'s account by MediaConnect.
    (string) --
    
    
    RoleArn (string) -- Role Arn MediaConnect can assumes to create ENIs in customer\'s account
    SecurityGroupIds (list) -- Security Group IDs to be used on ENI.
    (string) --
    
    
    SubnetId (string) -- Subnet must be in the AZ of the Flow
    
    
    
    
    
    
    
    """
    pass

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def create_flow(AvailabilityZone=None, Entitlements=None, Name=None, Outputs=None, Source=None, SourceFailoverConfig=None, Sources=None, VpcInterfaces=None):
    """
    Creates a new flow. The request must include one source. The request optionally can include outputs (up to 50) and entitlements (up to 50).
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.create_flow(
        AvailabilityZone='string',
        Entitlements=[
            {
                'DataTransferSubscriberFeePercent': 123,
                'Description': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Name': 'string',
                'Subscribers': [
                    'string',
                ]
            },
        ],
        Name='string',
        Outputs=[
            {
                'CidrAllowList': [
                    'string',
                ],
                'Description': 'string',
                'Destination': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'MaxLatency': 123,
                'Name': 'string',
                'Port': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'RemoteId': 'string',
                'SmoothingLatency': 123,
                'StreamId': 'string',
                'VpcInterfaceAttachment': {
                    'VpcInterfaceName': 'string'
                }
            },
        ],
        Source={
            'Decryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'ConstantInitializationVector': 'string',
                'DeviceId': 'string',
                'KeyType': 'speke'|'static-key',
                'Region': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SecretArn': 'string',
                'Url': 'string'
            },
            'Description': 'string',
            'EntitlementArn': 'string',
            'IngestPort': 123,
            'MaxBitrate': 123,
            'MaxLatency': 123,
            'Name': 'string',
            'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
            'StreamId': 'string',
            'VpcInterfaceName': 'string',
            'WhitelistCidr': 'string'
        },
        SourceFailoverConfig={
            'RecoveryWindow': 123,
            'State': 'ENABLED'|'DISABLED'
        },
        Sources=[
            {
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestPort': 123,
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Name': 'string',
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'StreamId': 'string',
                'VpcInterfaceName': 'string',
                'WhitelistCidr': 'string'
            },
        ],
        VpcInterfaces=[
            {
                'Name': 'string',
                'RoleArn': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetId': 'string'
            },
        ]
    )
    
    
    :type AvailabilityZone: string
    :param AvailabilityZone: The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS Region.

    :type Entitlements: list
    :param Entitlements: The entitlements that you want to grant on a flow.\n\n(dict) -- The entitlements that you want to grant on a flow.\nDataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.\nDescription (string) -- A description of the entitlement. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.\nEncryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.\nAlgorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).\nConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.\nDeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nKeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nRegion (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nRoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).\nSecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.\nUrl (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.\n\n\nName (string) -- The name of the entitlement. This value must be unique within the current flow.\nSubscribers (list) -- [REQUIRED] The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.\n(string) --\n\n\n\n\n\n

    :type Name: string
    :param Name: [REQUIRED] The name of the flow.

    :type Outputs: list
    :param Outputs: The outputs that you want to add to this flow.\n\n(dict) -- The output that you want to add to this flow.\nCidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.\n(string) --\n\n\nDescription (string) -- A description of the output. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the end user.\nDestination (string) -- The IP address from which video will be sent to output destinations.\nEncryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nAlgorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).\nConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.\nDeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nKeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nRegion (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nRoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).\nSecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.\nUrl (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.\n\n\nMaxLatency (integer) -- The maximum latency in milliseconds for Zixi-based streams.\nName (string) -- The name of the output. This value must be unique within the current flow.\nPort (integer) -- The port to use when content is distributed to this output.\nProtocol (string) -- [REQUIRED] The protocol to use for the output.\nRemoteId (string) -- The remote ID for the Zixi-pull output stream.\nSmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.\nStreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.\nVpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.\nVpcInterfaceName (string) -- The name of the VPC interface to use for this output.\n\n\n\n\n\n

    :type Source: dict
    :param Source: The settings for the source of the flow.\n\nDecryption (dict) -- The type of encryption that is used on the content ingested from this source.\nAlgorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).\nConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.\nDeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nKeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nRegion (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nRoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).\nSecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.\nUrl (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.\n\n\nDescription (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.\nEntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator\'s flow.\nIngestPort (integer) -- The port that the flow will be listening on for incoming content.\nMaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.\nMaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.\nName (string) -- The name of the source.\nProtocol (string) -- The protocol that is used by the source.\nStreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.\nVpcInterfaceName (string) -- The name of the VPC interface to use for this source.\nWhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.\n\n

    :type SourceFailoverConfig: dict
    :param SourceFailoverConfig: The settings for source failover\n\nRecoveryWindow (integer) -- Search window time to look for dash-7 packets\nState (string) --\n\n

    :type Sources: list
    :param Sources: \n(dict) -- The settings for the source of the flow.\nDecryption (dict) -- The type of encryption that is used on the content ingested from this source.\nAlgorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).\nConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.\nDeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nKeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nRegion (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nRoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).\nSecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.\nUrl (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.\n\n\nDescription (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.\nEntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator\'s flow.\nIngestPort (integer) -- The port that the flow will be listening on for incoming content.\nMaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.\nMaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.\nName (string) -- The name of the source.\nProtocol (string) -- The protocol that is used by the source.\nStreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.\nVpcInterfaceName (string) -- The name of the VPC interface to use for this source.\nWhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.\n\n\n\n

    :type VpcInterfaces: list
    :param VpcInterfaces: The VPC interfaces you want on the flow.\n\n(dict) -- Desired VPC Interface for a Flow\nName (string) -- [REQUIRED] The name of the VPC Interface. This value must be unique within the current flow.\nRoleArn (string) -- [REQUIRED] Role Arn MediaConnect can assumes to create ENIs in customer\'s account\nSecurityGroupIds (list) -- [REQUIRED] Security Group IDs to be used on ENI.\n(string) --\n\n\nSubnetId (string) -- [REQUIRED] Subnet must be in the AZ of the Flow\n\n\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Flow': {
        'AvailabilityZone': 'string',
        'Description': 'string',
        'EgressIp': 'string',
        'Entitlements': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Description': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'EntitlementArn': 'string',
                'Name': 'string',
                'Subscribers': [
                    'string',
                ]
            },
        ],
        'FlowArn': 'string',
        'Name': 'string',
        'Outputs': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Description': 'string',
                'Destination': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'EntitlementArn': 'string',
                'MediaLiveInputArn': 'string',
                'Name': 'string',
                'OutputArn': 'string',
                'Port': 123,
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceAttachment': {
                    'VpcInterfaceName': 'string'
                }
            },
        ],
        'Source': {
            'DataTransferSubscriberFeePercent': 123,
            'Decryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'ConstantInitializationVector': 'string',
                'DeviceId': 'string',
                'KeyType': 'speke'|'static-key',
                'Region': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SecretArn': 'string',
                'Url': 'string'
            },
            'Description': 'string',
            'EntitlementArn': 'string',
            'IngestIp': 'string',
            'IngestPort': 123,
            'Name': 'string',
            'SourceArn': 'string',
            'Transport': {
                'CidrAllowList': [
                    'string',
                ],
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'RemoteId': 'string',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            },
            'VpcInterfaceName': 'string',
            'WhitelistCidr': 'string'
        },
        'SourceFailoverConfig': {
            'RecoveryWindow': 123,
            'State': 'ENABLED'|'DISABLED'
        },
        'Sources': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestIp': 'string',
                'IngestPort': 123,
                'Name': 'string',
                'SourceArn': 'string',
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceName': 'string',
                'WhitelistCidr': 'string'
            },
        ],
        'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR',
        'VpcInterfaces': [
            {
                'Name': 'string',
                'NetworkInterfaceIds': [
                    'string',
                ],
                'RoleArn': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetId': 'string'
            },
        ]
    }
}


Response Structure

(dict) -- AWS Elemental MediaConnect created the new flow successfully.
Flow (dict) -- The settings for a flow, including its source, outputs, and entitlements.
AvailabilityZone (string) -- The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
Description (string) -- A description of the flow. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EgressIp (string) -- The IP address from which video will be sent to output destinations.
Entitlements (list) -- The entitlements in this flow.
(dict) -- The settings for a flow entitlement.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Description (string) -- A description of the entitlement.
Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementArn (string) -- The ARN of the entitlement.
Name (string) -- The name of the entitlement.
Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
(string) --






FlowArn (string) -- The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
Name (string) -- The name of the flow.
Outputs (list) -- The outputs in this flow.
(dict) -- The settings for an output.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Description (string) -- A description of the output.
Destination (string) -- The address where you want to send the output.
Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementArn (string) -- The ARN of the entitlement on the originator\'\'s flow. This value is relevant only on entitled flows.
MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
Name (string) -- The name of the output. This value must be unique within the current flow.
OutputArn (string) -- The ARN of the output.
Port (integer) -- The port to use when content is distributed to this output.
Transport (dict) -- Attributes related to the transport stream that are used in the output.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.
VpcInterfaceName (string) -- The name of the VPC interface to use for this output.






Source (dict) -- The settings for the source of the flow.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
IngestPort (integer) -- The port that the flow will be listening on for incoming content.
Name (string) -- The name of the source.
SourceArn (string) -- The ARN of the source.
Transport (dict) -- Attributes related to the transport stream that are used in the source.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.


SourceFailoverConfig (dict) -- The settings for source failover
RecoveryWindow (integer) -- Search window time to look for dash-7 packets
State (string) --


Sources (list) --
(dict) -- The settings for the source of the flow.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
IngestPort (integer) -- The port that the flow will be listening on for incoming content.
Name (string) -- The name of the source.
SourceArn (string) -- The ARN of the source.
Transport (dict) -- Attributes related to the transport stream that are used in the source.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.




Status (string) -- The current status of the flow.
VpcInterfaces (list) -- The VPC Interfaces for this flow.
(dict) -- The settings for a VPC Source.
Name (string) -- Immutable and has to be a unique against other VpcInterfaces in this Flow
NetworkInterfaceIds (list) -- IDs of the network interfaces created in customer\'s account by MediaConnect.
(string) --


RoleArn (string) -- Role Arn MediaConnect can assumes to create ENIs in customer\'s account
SecurityGroupIds (list) -- Security Group IDs to be used on ENI.
(string) --


SubnetId (string) -- Subnet must be in the AZ of the Flow












Exceptions

MediaConnect.Client.exceptions.CreateFlow420Exception
MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'Flow': {
            'AvailabilityZone': 'string',
            'Description': 'string',
            'EgressIp': 'string',
            'Entitlements': [
                {
                    'DataTransferSubscriberFeePercent': 123,
                    'Description': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'EntitlementArn': 'string',
                    'Name': 'string',
                    'Subscribers': [
                        'string',
                    ]
                },
            ],
            'FlowArn': 'string',
            'Name': 'string',
            'Outputs': [
                {
                    'DataTransferSubscriberFeePercent': 123,
                    'Description': 'string',
                    'Destination': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'EntitlementArn': 'string',
                    'MediaLiveInputArn': 'string',
                    'Name': 'string',
                    'OutputArn': 'string',
                    'Port': 123,
                    'Transport': {
                        'CidrAllowList': [
                            'string',
                        ],
                        'MaxBitrate': 123,
                        'MaxLatency': 123,
                        'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                        'RemoteId': 'string',
                        'SmoothingLatency': 123,
                        'StreamId': 'string'
                    },
                    'VpcInterfaceAttachment': {
                        'VpcInterfaceName': 'string'
                    }
                },
            ],
            'Source': {
                'DataTransferSubscriberFeePercent': 123,
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestIp': 'string',
                'IngestPort': 123,
                'Name': 'string',
                'SourceArn': 'string',
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceName': 'string',
                'WhitelistCidr': 'string'
            },
            'SourceFailoverConfig': {
                'RecoveryWindow': 123,
                'State': 'ENABLED'|'DISABLED'
            },
            'Sources': [
                {
                    'DataTransferSubscriberFeePercent': 123,
                    'Decryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'Description': 'string',
                    'EntitlementArn': 'string',
                    'IngestIp': 'string',
                    'IngestPort': 123,
                    'Name': 'string',
                    'SourceArn': 'string',
                    'Transport': {
                        'CidrAllowList': [
                            'string',
                        ],
                        'MaxBitrate': 123,
                        'MaxLatency': 123,
                        'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                        'RemoteId': 'string',
                        'SmoothingLatency': 123,
                        'StreamId': 'string'
                    },
                    'VpcInterfaceName': 'string',
                    'WhitelistCidr': 'string'
                },
            ],
            'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR',
            'VpcInterfaces': [
                {
                    'Name': 'string',
                    'NetworkInterfaceIds': [
                        'string',
                    ],
                    'RoleArn': 'string',
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'SubnetId': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect created the new flow successfully.
    Flow (dict) -- The settings for a flow, including its source, outputs, and entitlements.
    AvailabilityZone (string) -- The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
    Description (string) -- A description of the flow. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EgressIp (string) -- The IP address from which video will be sent to output destinations.
    Entitlements (list) -- The entitlements in this flow.
    (dict) -- The settings for a flow entitlement.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Description (string) -- A description of the entitlement.
    Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    EntitlementArn (string) -- The ARN of the entitlement.
    Name (string) -- The name of the entitlement.
    Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
    (string) --
    
    
    
    
    
    
    FlowArn (string) -- The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
    Name (string) -- The name of the flow.
    Outputs (list) -- The outputs in this flow.
    (dict) -- The settings for an output.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Description (string) -- A description of the output.
    Destination (string) -- The address where you want to send the output.
    Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    EntitlementArn (string) -- The ARN of the entitlement on the originator\'\'s flow. This value is relevant only on entitled flows.
    MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
    Name (string) -- The name of the output. This value must be unique within the current flow.
    OutputArn (string) -- The ARN of the output.
    Port (integer) -- The port to use when content is distributed to this output.
    Transport (dict) -- Attributes related to the transport stream that are used in the output.
    CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    (string) --
    
    
    MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    RemoteId (string) -- The remote ID for the Zixi-pull stream.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    VpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.
    VpcInterfaceName (string) -- The name of the VPC interface to use for this output.
    
    
    
    
    
    
    Source (dict) -- The settings for the source of the flow.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
    IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
    IngestPort (integer) -- The port that the flow will be listening on for incoming content.
    Name (string) -- The name of the source.
    SourceArn (string) -- The ARN of the source.
    Transport (dict) -- Attributes related to the transport stream that are used in the source.
    CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    (string) --
    
    
    MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    RemoteId (string) -- The remote ID for the Zixi-pull stream.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
    WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    
    
    SourceFailoverConfig (dict) -- The settings for source failover
    RecoveryWindow (integer) -- Search window time to look for dash-7 packets
    State (string) --
    
    
    Sources (list) --
    (dict) -- The settings for the source of the flow.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
    IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
    IngestPort (integer) -- The port that the flow will be listening on for incoming content.
    Name (string) -- The name of the source.
    SourceArn (string) -- The ARN of the source.
    Transport (dict) -- Attributes related to the transport stream that are used in the source.
    CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    (string) --
    
    
    MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    RemoteId (string) -- The remote ID for the Zixi-pull stream.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
    WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    
    
    
    
    Status (string) -- The current status of the flow.
    VpcInterfaces (list) -- The VPC Interfaces for this flow.
    (dict) -- The settings for a VPC Source.
    Name (string) -- Immutable and has to be a unique against other VpcInterfaces in this Flow
    NetworkInterfaceIds (list) -- IDs of the network interfaces created in customer\'s account by MediaConnect.
    (string) --
    
    
    RoleArn (string) -- Role Arn MediaConnect can assumes to create ENIs in customer\'s account
    SecurityGroupIds (list) -- Security Group IDs to be used on ENI.
    (string) --
    
    
    SubnetId (string) -- Subnet must be in the AZ of the Flow
    
    
    
    
    
    
    
    
    
    """
    pass

def delete_flow(FlowArn=None):
    """
    Deletes a flow. Before you can delete a flow, you must stop the flow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.delete_flow(
        FlowArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The ARN of the flow that you want to delete.

    :rtype: dict
ReturnsResponse Syntax{
    'FlowArn': 'string',
    'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
}


Response Structure

(dict) -- AWS Elemental MediaConnect is deleting the flow.
FlowArn (string) -- The ARN of the flow that was deleted.
Status (string) -- The status of the flow when the DeleteFlow process begins.





Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
    }
    
    
    :returns: 
    MediaConnect.Client.exceptions.BadRequestException
    MediaConnect.Client.exceptions.InternalServerErrorException
    MediaConnect.Client.exceptions.ForbiddenException
    MediaConnect.Client.exceptions.NotFoundException
    MediaConnect.Client.exceptions.ServiceUnavailableException
    MediaConnect.Client.exceptions.TooManyRequestsException
    
    """
    pass

def describe_flow(FlowArn=None):
    """
    Displays the details of a flow. The response includes the flow ARN, name, and Availability Zone, as well as details about the source, outputs, and entitlements.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.describe_flow(
        FlowArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The ARN of the flow that you want to describe.

    :rtype: dict
ReturnsResponse Syntax{
    'Flow': {
        'AvailabilityZone': 'string',
        'Description': 'string',
        'EgressIp': 'string',
        'Entitlements': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Description': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'EntitlementArn': 'string',
                'Name': 'string',
                'Subscribers': [
                    'string',
                ]
            },
        ],
        'FlowArn': 'string',
        'Name': 'string',
        'Outputs': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Description': 'string',
                'Destination': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'EntitlementArn': 'string',
                'MediaLiveInputArn': 'string',
                'Name': 'string',
                'OutputArn': 'string',
                'Port': 123,
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceAttachment': {
                    'VpcInterfaceName': 'string'
                }
            },
        ],
        'Source': {
            'DataTransferSubscriberFeePercent': 123,
            'Decryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'ConstantInitializationVector': 'string',
                'DeviceId': 'string',
                'KeyType': 'speke'|'static-key',
                'Region': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SecretArn': 'string',
                'Url': 'string'
            },
            'Description': 'string',
            'EntitlementArn': 'string',
            'IngestIp': 'string',
            'IngestPort': 123,
            'Name': 'string',
            'SourceArn': 'string',
            'Transport': {
                'CidrAllowList': [
                    'string',
                ],
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'RemoteId': 'string',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            },
            'VpcInterfaceName': 'string',
            'WhitelistCidr': 'string'
        },
        'SourceFailoverConfig': {
            'RecoveryWindow': 123,
            'State': 'ENABLED'|'DISABLED'
        },
        'Sources': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestIp': 'string',
                'IngestPort': 123,
                'Name': 'string',
                'SourceArn': 'string',
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceName': 'string',
                'WhitelistCidr': 'string'
            },
        ],
        'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR',
        'VpcInterfaces': [
            {
                'Name': 'string',
                'NetworkInterfaceIds': [
                    'string',
                ],
                'RoleArn': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetId': 'string'
            },
        ]
    },
    'Messages': {
        'Errors': [
            'string',
        ]
    }
}


Response Structure

(dict) -- AWS Elemental MediaConnect returned the flow details successfully.
Flow (dict) -- The settings for a flow, including its source, outputs, and entitlements.
AvailabilityZone (string) -- The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
Description (string) -- A description of the flow. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EgressIp (string) -- The IP address from which video will be sent to output destinations.
Entitlements (list) -- The entitlements in this flow.
(dict) -- The settings for a flow entitlement.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Description (string) -- A description of the entitlement.
Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementArn (string) -- The ARN of the entitlement.
Name (string) -- The name of the entitlement.
Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
(string) --






FlowArn (string) -- The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
Name (string) -- The name of the flow.
Outputs (list) -- The outputs in this flow.
(dict) -- The settings for an output.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Description (string) -- A description of the output.
Destination (string) -- The address where you want to send the output.
Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementArn (string) -- The ARN of the entitlement on the originator\'\'s flow. This value is relevant only on entitled flows.
MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
Name (string) -- The name of the output. This value must be unique within the current flow.
OutputArn (string) -- The ARN of the output.
Port (integer) -- The port to use when content is distributed to this output.
Transport (dict) -- Attributes related to the transport stream that are used in the output.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.
VpcInterfaceName (string) -- The name of the VPC interface to use for this output.






Source (dict) -- The settings for the source of the flow.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
IngestPort (integer) -- The port that the flow will be listening on for incoming content.
Name (string) -- The name of the source.
SourceArn (string) -- The ARN of the source.
Transport (dict) -- Attributes related to the transport stream that are used in the source.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.


SourceFailoverConfig (dict) -- The settings for source failover
RecoveryWindow (integer) -- Search window time to look for dash-7 packets
State (string) --


Sources (list) --
(dict) -- The settings for the source of the flow.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
IngestPort (integer) -- The port that the flow will be listening on for incoming content.
Name (string) -- The name of the source.
SourceArn (string) -- The ARN of the source.
Transport (dict) -- Attributes related to the transport stream that are used in the source.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.




Status (string) -- The current status of the flow.
VpcInterfaces (list) -- The VPC Interfaces for this flow.
(dict) -- The settings for a VPC Source.
Name (string) -- Immutable and has to be a unique against other VpcInterfaces in this Flow
NetworkInterfaceIds (list) -- IDs of the network interfaces created in customer\'s account by MediaConnect.
(string) --


RoleArn (string) -- Role Arn MediaConnect can assumes to create ENIs in customer\'s account
SecurityGroupIds (list) -- Security Group IDs to be used on ENI.
(string) --


SubnetId (string) -- Subnet must be in the AZ of the Flow






Messages (dict) -- Messages that provide the state of the flow.
Errors (list) -- A list of errors that might have been generated from processes on this flow.
(string) --









Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'Flow': {
            'AvailabilityZone': 'string',
            'Description': 'string',
            'EgressIp': 'string',
            'Entitlements': [
                {
                    'DataTransferSubscriberFeePercent': 123,
                    'Description': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'EntitlementArn': 'string',
                    'Name': 'string',
                    'Subscribers': [
                        'string',
                    ]
                },
            ],
            'FlowArn': 'string',
            'Name': 'string',
            'Outputs': [
                {
                    'DataTransferSubscriberFeePercent': 123,
                    'Description': 'string',
                    'Destination': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'EntitlementArn': 'string',
                    'MediaLiveInputArn': 'string',
                    'Name': 'string',
                    'OutputArn': 'string',
                    'Port': 123,
                    'Transport': {
                        'CidrAllowList': [
                            'string',
                        ],
                        'MaxBitrate': 123,
                        'MaxLatency': 123,
                        'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                        'RemoteId': 'string',
                        'SmoothingLatency': 123,
                        'StreamId': 'string'
                    },
                    'VpcInterfaceAttachment': {
                        'VpcInterfaceName': 'string'
                    }
                },
            ],
            'Source': {
                'DataTransferSubscriberFeePercent': 123,
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestIp': 'string',
                'IngestPort': 123,
                'Name': 'string',
                'SourceArn': 'string',
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceName': 'string',
                'WhitelistCidr': 'string'
            },
            'SourceFailoverConfig': {
                'RecoveryWindow': 123,
                'State': 'ENABLED'|'DISABLED'
            },
            'Sources': [
                {
                    'DataTransferSubscriberFeePercent': 123,
                    'Decryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'Description': 'string',
                    'EntitlementArn': 'string',
                    'IngestIp': 'string',
                    'IngestPort': 123,
                    'Name': 'string',
                    'SourceArn': 'string',
                    'Transport': {
                        'CidrAllowList': [
                            'string',
                        ],
                        'MaxBitrate': 123,
                        'MaxLatency': 123,
                        'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                        'RemoteId': 'string',
                        'SmoothingLatency': 123,
                        'StreamId': 'string'
                    },
                    'VpcInterfaceName': 'string',
                    'WhitelistCidr': 'string'
                },
            ],
            'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR',
            'VpcInterfaces': [
                {
                    'Name': 'string',
                    'NetworkInterfaceIds': [
                        'string',
                    ],
                    'RoleArn': 'string',
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'SubnetId': 'string'
                },
            ]
        },
        'Messages': {
            'Errors': [
                'string',
            ]
        }
    }
    
    
    :returns: 
    MediaConnect.Client.exceptions.BadRequestException
    MediaConnect.Client.exceptions.InternalServerErrorException
    MediaConnect.Client.exceptions.ForbiddenException
    MediaConnect.Client.exceptions.NotFoundException
    MediaConnect.Client.exceptions.ServiceUnavailableException
    MediaConnect.Client.exceptions.TooManyRequestsException
    
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

def grant_flow_entitlements(Entitlements=None, FlowArn=None):
    """
    Grants entitlements to an existing flow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.grant_flow_entitlements(
        Entitlements=[
            {
                'DataTransferSubscriberFeePercent': 123,
                'Description': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Name': 'string',
                'Subscribers': [
                    'string',
                ]
            },
        ],
        FlowArn='string'
    )
    
    
    :type Entitlements: list
    :param Entitlements: [REQUIRED] The list of entitlements that you want to grant.\n\n(dict) -- The entitlements that you want to grant on a flow.\nDataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.\nDescription (string) -- A description of the entitlement. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.\nEncryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.\nAlgorithm (string) -- [REQUIRED] The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).\nConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.\nDeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nKeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nRegion (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nRoleArn (string) -- [REQUIRED] The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).\nSecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.\nUrl (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.\n\n\nName (string) -- The name of the entitlement. This value must be unique within the current flow.\nSubscribers (list) -- [REQUIRED] The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.\n(string) --\n\n\n\n\n\n

    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to grant entitlements on.

    :rtype: dict

ReturnsResponse Syntax
{
    'Entitlements': [
        {
            'DataTransferSubscriberFeePercent': 123,
            'Description': 'string',
            'Encryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'ConstantInitializationVector': 'string',
                'DeviceId': 'string',
                'KeyType': 'speke'|'static-key',
                'Region': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SecretArn': 'string',
                'Url': 'string'
            },
            'EntitlementArn': 'string',
            'Name': 'string',
            'Subscribers': [
                'string',
            ]
        },
    ],
    'FlowArn': 'string'
}


Response Structure

(dict) -- AWS Elemental MediaConnect granted the entitlements successfully.
Entitlements (list) -- The entitlements that were just granted.
(dict) -- The settings for a flow entitlement.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Description (string) -- A description of the entitlement.
Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementArn (string) -- The ARN of the entitlement.
Name (string) -- The name of the entitlement.
Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
(string) --






FlowArn (string) -- The ARN of the flow that these entitlements were granted to.






Exceptions

MediaConnect.Client.exceptions.GrantFlowEntitlements420Exception
MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'Entitlements': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Description': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'EntitlementArn': 'string',
                'Name': 'string',
                'Subscribers': [
                    'string',
                ]
            },
        ],
        'FlowArn': 'string'
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect granted the entitlements successfully.
    Entitlements (list) -- The entitlements that were just granted.
    (dict) -- The settings for a flow entitlement.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Description (string) -- A description of the entitlement.
    Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    EntitlementArn (string) -- The ARN of the entitlement.
    Name (string) -- The name of the entitlement.
    Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
    (string) --
    
    
    
    
    
    
    FlowArn (string) -- The ARN of the flow that these entitlements were granted to.
    
    
    
    """
    pass

def list_entitlements(MaxResults=None, NextToken=None):
    """
    Displays a list of all entitlements that have been granted to this account. This request returns 20 results per page.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_entitlements(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per API request. For example, you submit a ListEntitlements request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 20 results per page.

    :type NextToken: string
    :param NextToken: The token that identifies which batch of results that you want to see. For example, you submit a ListEntitlements request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListEntitlements request a second time and specify the NextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'Entitlements': [
        {
            'DataTransferSubscriberFeePercent': 123,
            'EntitlementArn': 'string',
            'EntitlementName': 'string'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) -- AWS Elemental MediaConnect returned the list of entitlements successfully.
Entitlements (list) -- A list of entitlements that have been granted to you from other AWS accounts.
(dict) -- An entitlement that has been granted to you from other AWS accounts.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
EntitlementArn (string) -- The ARN of the entitlement.
EntitlementName (string) -- The name of the entitlement.




NextToken (string) -- The token that identifies which batch of results that you want to see. For example, you submit a ListEntitlements request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListEntitlements request a second time and specify the NextToken value.






Exceptions

MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException
MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException


    :return: {
        'Entitlements': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'EntitlementArn': 'string',
                'EntitlementName': 'string'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect returned the list of entitlements successfully.
    Entitlements (list) -- A list of entitlements that have been granted to you from other AWS accounts.
    (dict) -- An entitlement that has been granted to you from other AWS accounts.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    EntitlementArn (string) -- The ARN of the entitlement.
    EntitlementName (string) -- The name of the entitlement.
    
    
    
    
    NextToken (string) -- The token that identifies which batch of results that you want to see. For example, you submit a ListEntitlements request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListEntitlements request a second time and specify the NextToken value.
    
    
    
    """
    pass

def list_flows(MaxResults=None, NextToken=None):
    """
    Displays a list of flows that are associated with this account. This request returns a paginated result.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_flows(
        MaxResults=123,
        NextToken='string'
    )
    
    
    :type MaxResults: integer
    :param MaxResults: The maximum number of results to return per API request. For example, you submit a ListFlows request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 10 results per page.

    :type NextToken: string
    :param NextToken: The token that identifies which batch of results that you want to see. For example, you submit a ListFlows request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFlows request a second time and specify the NextToken value.

    :rtype: dict

ReturnsResponse Syntax
{
    'Flows': [
        {
            'AvailabilityZone': 'string',
            'Description': 'string',
            'FlowArn': 'string',
            'Name': 'string',
            'SourceType': 'OWNED'|'ENTITLED',
            'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
        },
    ],
    'NextToken': 'string'
}


Response Structure

(dict) -- AWS Elemental MediaConnect returned the list of flows successfully.
Flows (list) -- A list of flow summaries.
(dict) -- Provides a summary of a flow, including its ARN, Availability Zone, and source type.
AvailabilityZone (string) -- The Availability Zone that the flow was created in.
Description (string) -- A description of the flow.
FlowArn (string) -- The ARN of the flow.
Name (string) -- The name of the flow.
SourceType (string) -- The type of source. This value is either owned (originated somewhere other than an AWS Elemental MediaConnect flow owned by another AWS account) or entitled (originated at an AWS Elemental MediaConnect flow owned by another AWS account).
Status (string) -- The current status of the flow.




NextToken (string) -- The token that identifies which batch of results that you want to see. For example, you submit a ListFlows request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFlows request a second time and specify the NextToken value.






Exceptions

MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException
MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException


    :return: {
        'Flows': [
            {
                'AvailabilityZone': 'string',
                'Description': 'string',
                'FlowArn': 'string',
                'Name': 'string',
                'SourceType': 'OWNED'|'ENTITLED',
                'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
            },
        ],
        'NextToken': 'string'
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect returned the list of flows successfully.
    Flows (list) -- A list of flow summaries.
    (dict) -- Provides a summary of a flow, including its ARN, Availability Zone, and source type.
    AvailabilityZone (string) -- The Availability Zone that the flow was created in.
    Description (string) -- A description of the flow.
    FlowArn (string) -- The ARN of the flow.
    Name (string) -- The name of the flow.
    SourceType (string) -- The type of source. This value is either owned (originated somewhere other than an AWS Elemental MediaConnect flow owned by another AWS account) or entitled (originated at an AWS Elemental MediaConnect flow owned by another AWS account).
    Status (string) -- The current status of the flow.
    
    
    
    
    NextToken (string) -- The token that identifies which batch of results that you want to see. For example, you submit a ListFlows request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFlows request a second time and specify the NextToken value.
    
    
    
    """
    pass

def list_tags_for_resource(ResourceArn=None):
    """
    List all tags on an AWS Elemental MediaConnect resource
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.list_tags_for_resource(
        ResourceArn='string'
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED] The Amazon Resource Name (ARN) that identifies the AWS Elemental MediaConnect resource for which to list the tags.

    :rtype: dict
ReturnsResponse Syntax{
    'Tags': {
        'string': 'string'
    }
}


Response Structure

(dict) -- The tags for the resource
Tags (dict) -- A map from tag keys to values. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
(string) --
(string) --









Exceptions

MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException


    :return: {
        'Tags': {
            'string': 'string'
        }
    }
    
    
    :returns: 
    MediaConnect.Client.exceptions.NotFoundException
    MediaConnect.Client.exceptions.BadRequestException
    MediaConnect.Client.exceptions.InternalServerErrorException
    
    """
    pass

def remove_flow_output(FlowArn=None, OutputArn=None):
    """
    Removes an output from an existing flow. This request can be made only on an output that does not have an entitlement associated with it. If the output has an entitlement, you must revoke the entitlement instead. When an entitlement is revoked from a flow, the service automatically removes the associated output.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_flow_output(
        FlowArn='string',
        OutputArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to remove an output from.

    :type OutputArn: string
    :param OutputArn: [REQUIRED] The ARN of the output that you want to remove.

    :rtype: dict

ReturnsResponse Syntax
{
    'FlowArn': 'string',
    'OutputArn': 'string'
}


Response Structure

(dict) -- output successfully removed from flow configuration.
FlowArn (string) -- The ARN of the flow that is associated with the output you removed.
OutputArn (string) -- The ARN of the output that was removed.






Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'OutputArn': 'string'
    }
    
    
    :returns: 
    (dict) -- output successfully removed from flow configuration.
    FlowArn (string) -- The ARN of the flow that is associated with the output you removed.
    OutputArn (string) -- The ARN of the output that was removed.
    
    
    
    """
    pass

def remove_flow_source(FlowArn=None, SourceArn=None):
    """
    Removes a source from an existing flow. This request can be made only if there is more than one source on the flow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_flow_source(
        FlowArn='string',
        SourceArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to remove a source from.

    :type SourceArn: string
    :param SourceArn: [REQUIRED] The ARN of the source that you want to remove.

    :rtype: dict

ReturnsResponse Syntax
{
    'FlowArn': 'string',
    'SourceArn': 'string'
}


Response Structure

(dict) -- source successfully removed from flow configuration.
FlowArn (string) -- The ARN of the flow that is associated with the source you removed.
SourceArn (string) -- The ARN of the source that was removed.






Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'SourceArn': 'string'
    }
    
    
    :returns: 
    (dict) -- source successfully removed from flow configuration.
    FlowArn (string) -- The ARN of the flow that is associated with the source you removed.
    SourceArn (string) -- The ARN of the source that was removed.
    
    
    
    """
    pass

def remove_flow_vpc_interface(FlowArn=None, VpcInterfaceName=None):
    """
    Removes a VPC Interface from an existing flow. This request can be made only on a VPC interface that does not have a Source or Output associated with it. If the VPC interface is referenced by a Source or Output, you must first delete or update the Source or Output to no longer reference the VPC interface.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.remove_flow_vpc_interface(
        FlowArn='string',
        VpcInterfaceName='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to remove a VPC interface from.

    :type VpcInterfaceName: string
    :param VpcInterfaceName: [REQUIRED] The name of the VPC interface that you want to remove.

    :rtype: dict

ReturnsResponse Syntax
{
    'FlowArn': 'string',
    'NonDeletedNetworkInterfaceIds': [
        'string',
    ],
    'VpcInterfaceName': 'string'
}


Response Structure

(dict) -- VPC interface successfully removed from flow configuration.
FlowArn (string) -- The ARN of the flow that is associated with the VPC interface you removed.
NonDeletedNetworkInterfaceIds (list) -- IDs of network interfaces associated with the removed VPC interface that Media Connect was unable to remove.
(string) --


VpcInterfaceName (string) -- The name of the VPC interface that was removed.






Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'NonDeletedNetworkInterfaceIds': [
            'string',
        ],
        'VpcInterfaceName': 'string'
    }
    
    
    :returns: 
    (dict) -- VPC interface successfully removed from flow configuration.
    FlowArn (string) -- The ARN of the flow that is associated with the VPC interface you removed.
    NonDeletedNetworkInterfaceIds (list) -- IDs of network interfaces associated with the removed VPC interface that Media Connect was unable to remove.
    (string) --
    
    
    VpcInterfaceName (string) -- The name of the VPC interface that was removed.
    
    
    
    """
    pass

def revoke_flow_entitlement(EntitlementArn=None, FlowArn=None):
    """
    Revokes an entitlement from a flow. Once an entitlement is revoked, the content becomes unavailable to the subscriber and the associated output is removed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.revoke_flow_entitlement(
        EntitlementArn='string',
        FlowArn='string'
    )
    
    
    :type EntitlementArn: string
    :param EntitlementArn: [REQUIRED] The ARN of the entitlement that you want to revoke.

    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to revoke an entitlement from.

    :rtype: dict

ReturnsResponse Syntax
{
    'EntitlementArn': 'string',
    'FlowArn': 'string'
}


Response Structure

(dict) -- AWS Elemental MediaConnect revoked the entitlement successfully.
EntitlementArn (string) -- The ARN of the entitlement that was revoked.
FlowArn (string) -- The ARN of the flow that the entitlement was revoked from.






Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'EntitlementArn': 'string',
        'FlowArn': 'string'
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect revoked the entitlement successfully.
    EntitlementArn (string) -- The ARN of the entitlement that was revoked.
    FlowArn (string) -- The ARN of the flow that the entitlement was revoked from.
    
    
    
    """
    pass

def start_flow(FlowArn=None):
    """
    Starts a flow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.start_flow(
        FlowArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The ARN of the flow that you want to start.

    :rtype: dict
ReturnsResponse Syntax{
    'FlowArn': 'string',
    'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
}


Response Structure

(dict) -- AWS Elemental MediaConnect is starting the flow.
FlowArn (string) -- The ARN of the flow that you started.
Status (string) -- The status of the flow when the StartFlow process begins.





Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
    }
    
    
    :returns: 
    MediaConnect.Client.exceptions.BadRequestException
    MediaConnect.Client.exceptions.InternalServerErrorException
    MediaConnect.Client.exceptions.ForbiddenException
    MediaConnect.Client.exceptions.NotFoundException
    MediaConnect.Client.exceptions.ServiceUnavailableException
    MediaConnect.Client.exceptions.TooManyRequestsException
    
    """
    pass

def stop_flow(FlowArn=None):
    """
    Stops a flow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.stop_flow(
        FlowArn='string'
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The ARN of the flow that you want to stop.

    :rtype: dict
ReturnsResponse Syntax{
    'FlowArn': 'string',
    'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
}


Response Structure

(dict) -- AWS Elemental MediaConnect is stopping the flow.
FlowArn (string) -- The ARN of the flow that you stopped.
Status (string) -- The status of the flow when the StopFlow process begins.





Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR'
    }
    
    
    :returns: 
    MediaConnect.Client.exceptions.BadRequestException
    MediaConnect.Client.exceptions.InternalServerErrorException
    MediaConnect.Client.exceptions.ForbiddenException
    MediaConnect.Client.exceptions.NotFoundException
    MediaConnect.Client.exceptions.ServiceUnavailableException
    MediaConnect.Client.exceptions.TooManyRequestsException
    
    """
    pass

def tag_resource(ResourceArn=None, Tags=None):
    """
    Associates the specified tags to a resource with the specified resourceArn. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.tag_resource(
        ResourceArn='string',
        Tags={
            'string': 'string'
        }
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED] The Amazon Resource Name (ARN) that identifies the AWS Elemental MediaConnect resource to which to add tags.

    :type Tags: dict
    :param Tags: [REQUIRED] A map from tag keys to values. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.\n\n(string) --\n(string) --\n\n\n\n

    :returns: 
    MediaConnect.Client.exceptions.NotFoundException
    MediaConnect.Client.exceptions.BadRequestException
    MediaConnect.Client.exceptions.InternalServerErrorException
    
    """
    pass

def untag_resource(ResourceArn=None, TagKeys=None):
    """
    Deletes specified tags from a resource.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.untag_resource(
        ResourceArn='string',
        TagKeys=[
            'string',
        ]
    )
    
    
    :type ResourceArn: string
    :param ResourceArn: [REQUIRED] The Amazon Resource Name (ARN) that identifies the AWS Elemental MediaConnect resource from which to delete tags.

    :type TagKeys: list
    :param TagKeys: [REQUIRED] The keys of the tags to be removed.\n\n(string) --\n\n

    :returns: 
    MediaConnect.Client.exceptions.NotFoundException
    MediaConnect.Client.exceptions.BadRequestException
    MediaConnect.Client.exceptions.InternalServerErrorException
    
    """
    pass

def update_flow(FlowArn=None, SourceFailoverConfig=None):
    """
    Updates flow
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_flow(
        FlowArn='string',
        SourceFailoverConfig={
            'RecoveryWindow': 123,
            'State': 'ENABLED'|'DISABLED'
        }
    )
    
    
    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that you want to update.

    :type SourceFailoverConfig: dict
    :param SourceFailoverConfig: The settings for source failover\n\nRecoveryWindow (integer) -- Recovery window time to look for dash-7 packets\nState (string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Flow': {
        'AvailabilityZone': 'string',
        'Description': 'string',
        'EgressIp': 'string',
        'Entitlements': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Description': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'EntitlementArn': 'string',
                'Name': 'string',
                'Subscribers': [
                    'string',
                ]
            },
        ],
        'FlowArn': 'string',
        'Name': 'string',
        'Outputs': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Description': 'string',
                'Destination': 'string',
                'Encryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'EntitlementArn': 'string',
                'MediaLiveInputArn': 'string',
                'Name': 'string',
                'OutputArn': 'string',
                'Port': 123,
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceAttachment': {
                    'VpcInterfaceName': 'string'
                }
            },
        ],
        'Source': {
            'DataTransferSubscriberFeePercent': 123,
            'Decryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'ConstantInitializationVector': 'string',
                'DeviceId': 'string',
                'KeyType': 'speke'|'static-key',
                'Region': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SecretArn': 'string',
                'Url': 'string'
            },
            'Description': 'string',
            'EntitlementArn': 'string',
            'IngestIp': 'string',
            'IngestPort': 123,
            'Name': 'string',
            'SourceArn': 'string',
            'Transport': {
                'CidrAllowList': [
                    'string',
                ],
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'RemoteId': 'string',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            },
            'VpcInterfaceName': 'string',
            'WhitelistCidr': 'string'
        },
        'SourceFailoverConfig': {
            'RecoveryWindow': 123,
            'State': 'ENABLED'|'DISABLED'
        },
        'Sources': [
            {
                'DataTransferSubscriberFeePercent': 123,
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestIp': 'string',
                'IngestPort': 123,
                'Name': 'string',
                'SourceArn': 'string',
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceName': 'string',
                'WhitelistCidr': 'string'
            },
        ],
        'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR',
        'VpcInterfaces': [
            {
                'Name': 'string',
                'NetworkInterfaceIds': [
                    'string',
                ],
                'RoleArn': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'SubnetId': 'string'
            },
        ]
    }
}


Response Structure

(dict) -- AWS Elemental MediaConnect updated the flow successfully.
Flow (dict) -- The settings for a flow, including its source, outputs, and entitlements.
AvailabilityZone (string) -- The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
Description (string) -- A description of the flow. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EgressIp (string) -- The IP address from which video will be sent to output destinations.
Entitlements (list) -- The entitlements in this flow.
(dict) -- The settings for a flow entitlement.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Description (string) -- A description of the entitlement.
Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementArn (string) -- The ARN of the entitlement.
Name (string) -- The name of the entitlement.
Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
(string) --






FlowArn (string) -- The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
Name (string) -- The name of the flow.
Outputs (list) -- The outputs in this flow.
(dict) -- The settings for an output.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Description (string) -- A description of the output.
Destination (string) -- The address where you want to send the output.
Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementArn (string) -- The ARN of the entitlement on the originator\'\'s flow. This value is relevant only on entitled flows.
MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
Name (string) -- The name of the output. This value must be unique within the current flow.
OutputArn (string) -- The ARN of the output.
Port (integer) -- The port to use when content is distributed to this output.
Transport (dict) -- Attributes related to the transport stream that are used in the output.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.
VpcInterfaceName (string) -- The name of the VPC interface to use for this output.






Source (dict) -- The settings for the source of the flow.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
IngestPort (integer) -- The port that the flow will be listening on for incoming content.
Name (string) -- The name of the source.
SourceArn (string) -- The ARN of the source.
Transport (dict) -- Attributes related to the transport stream that are used in the source.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.


SourceFailoverConfig (dict) -- The settings for source failover
RecoveryWindow (integer) -- Search window time to look for dash-7 packets
State (string) --


Sources (list) --
(dict) -- The settings for the source of the flow.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
IngestPort (integer) -- The port that the flow will be listening on for incoming content.
Name (string) -- The name of the source.
SourceArn (string) -- The ARN of the source.
Transport (dict) -- Attributes related to the transport stream that are used in the source.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.




Status (string) -- The current status of the flow.
VpcInterfaces (list) -- The VPC Interfaces for this flow.
(dict) -- The settings for a VPC Source.
Name (string) -- Immutable and has to be a unique against other VpcInterfaces in this Flow
NetworkInterfaceIds (list) -- IDs of the network interfaces created in customer\'s account by MediaConnect.
(string) --


RoleArn (string) -- Role Arn MediaConnect can assumes to create ENIs in customer\'s account
SecurityGroupIds (list) -- Security Group IDs to be used on ENI.
(string) --


SubnetId (string) -- Subnet must be in the AZ of the Flow












Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'Flow': {
            'AvailabilityZone': 'string',
            'Description': 'string',
            'EgressIp': 'string',
            'Entitlements': [
                {
                    'DataTransferSubscriberFeePercent': 123,
                    'Description': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'EntitlementArn': 'string',
                    'Name': 'string',
                    'Subscribers': [
                        'string',
                    ]
                },
            ],
            'FlowArn': 'string',
            'Name': 'string',
            'Outputs': [
                {
                    'DataTransferSubscriberFeePercent': 123,
                    'Description': 'string',
                    'Destination': 'string',
                    'Encryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'EntitlementArn': 'string',
                    'MediaLiveInputArn': 'string',
                    'Name': 'string',
                    'OutputArn': 'string',
                    'Port': 123,
                    'Transport': {
                        'CidrAllowList': [
                            'string',
                        ],
                        'MaxBitrate': 123,
                        'MaxLatency': 123,
                        'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                        'RemoteId': 'string',
                        'SmoothingLatency': 123,
                        'StreamId': 'string'
                    },
                    'VpcInterfaceAttachment': {
                        'VpcInterfaceName': 'string'
                    }
                },
            ],
            'Source': {
                'DataTransferSubscriberFeePercent': 123,
                'Decryption': {
                    'Algorithm': 'aes128'|'aes192'|'aes256',
                    'ConstantInitializationVector': 'string',
                    'DeviceId': 'string',
                    'KeyType': 'speke'|'static-key',
                    'Region': 'string',
                    'ResourceId': 'string',
                    'RoleArn': 'string',
                    'SecretArn': 'string',
                    'Url': 'string'
                },
                'Description': 'string',
                'EntitlementArn': 'string',
                'IngestIp': 'string',
                'IngestPort': 123,
                'Name': 'string',
                'SourceArn': 'string',
                'Transport': {
                    'CidrAllowList': [
                        'string',
                    ],
                    'MaxBitrate': 123,
                    'MaxLatency': 123,
                    'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                    'RemoteId': 'string',
                    'SmoothingLatency': 123,
                    'StreamId': 'string'
                },
                'VpcInterfaceName': 'string',
                'WhitelistCidr': 'string'
            },
            'SourceFailoverConfig': {
                'RecoveryWindow': 123,
                'State': 'ENABLED'|'DISABLED'
            },
            'Sources': [
                {
                    'DataTransferSubscriberFeePercent': 123,
                    'Decryption': {
                        'Algorithm': 'aes128'|'aes192'|'aes256',
                        'ConstantInitializationVector': 'string',
                        'DeviceId': 'string',
                        'KeyType': 'speke'|'static-key',
                        'Region': 'string',
                        'ResourceId': 'string',
                        'RoleArn': 'string',
                        'SecretArn': 'string',
                        'Url': 'string'
                    },
                    'Description': 'string',
                    'EntitlementArn': 'string',
                    'IngestIp': 'string',
                    'IngestPort': 123,
                    'Name': 'string',
                    'SourceArn': 'string',
                    'Transport': {
                        'CidrAllowList': [
                            'string',
                        ],
                        'MaxBitrate': 123,
                        'MaxLatency': 123,
                        'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                        'RemoteId': 'string',
                        'SmoothingLatency': 123,
                        'StreamId': 'string'
                    },
                    'VpcInterfaceName': 'string',
                    'WhitelistCidr': 'string'
                },
            ],
            'Status': 'STANDBY'|'ACTIVE'|'UPDATING'|'DELETING'|'STARTING'|'STOPPING'|'ERROR',
            'VpcInterfaces': [
                {
                    'Name': 'string',
                    'NetworkInterfaceIds': [
                        'string',
                    ],
                    'RoleArn': 'string',
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'SubnetId': 'string'
                },
            ]
        }
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect updated the flow successfully.
    Flow (dict) -- The settings for a flow, including its source, outputs, and entitlements.
    AvailabilityZone (string) -- The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
    Description (string) -- A description of the flow. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EgressIp (string) -- The IP address from which video will be sent to output destinations.
    Entitlements (list) -- The entitlements in this flow.
    (dict) -- The settings for a flow entitlement.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Description (string) -- A description of the entitlement.
    Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    EntitlementArn (string) -- The ARN of the entitlement.
    Name (string) -- The name of the entitlement.
    Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
    (string) --
    
    
    
    
    
    
    FlowArn (string) -- The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
    Name (string) -- The name of the flow.
    Outputs (list) -- The outputs in this flow.
    (dict) -- The settings for an output.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Description (string) -- A description of the output.
    Destination (string) -- The address where you want to send the output.
    Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    EntitlementArn (string) -- The ARN of the entitlement on the originator\'\'s flow. This value is relevant only on entitled flows.
    MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
    Name (string) -- The name of the output. This value must be unique within the current flow.
    OutputArn (string) -- The ARN of the output.
    Port (integer) -- The port to use when content is distributed to this output.
    Transport (dict) -- Attributes related to the transport stream that are used in the output.
    CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    (string) --
    
    
    MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    RemoteId (string) -- The remote ID for the Zixi-pull stream.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    VpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.
    VpcInterfaceName (string) -- The name of the VPC interface to use for this output.
    
    
    
    
    
    
    Source (dict) -- The settings for the source of the flow.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
    IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
    IngestPort (integer) -- The port that the flow will be listening on for incoming content.
    Name (string) -- The name of the source.
    SourceArn (string) -- The ARN of the source.
    Transport (dict) -- Attributes related to the transport stream that are used in the source.
    CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    (string) --
    
    
    MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    RemoteId (string) -- The remote ID for the Zixi-pull stream.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
    WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    
    
    SourceFailoverConfig (dict) -- The settings for source failover
    RecoveryWindow (integer) -- Search window time to look for dash-7 packets
    State (string) --
    
    
    Sources (list) --
    (dict) -- The settings for the source of the flow.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
    IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
    IngestPort (integer) -- The port that the flow will be listening on for incoming content.
    Name (string) -- The name of the source.
    SourceArn (string) -- The ARN of the source.
    Transport (dict) -- Attributes related to the transport stream that are used in the source.
    CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    (string) --
    
    
    MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    RemoteId (string) -- The remote ID for the Zixi-pull stream.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
    WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    
    
    
    
    Status (string) -- The current status of the flow.
    VpcInterfaces (list) -- The VPC Interfaces for this flow.
    (dict) -- The settings for a VPC Source.
    Name (string) -- Immutable and has to be a unique against other VpcInterfaces in this Flow
    NetworkInterfaceIds (list) -- IDs of the network interfaces created in customer\'s account by MediaConnect.
    (string) --
    
    
    RoleArn (string) -- Role Arn MediaConnect can assumes to create ENIs in customer\'s account
    SecurityGroupIds (list) -- Security Group IDs to be used on ENI.
    (string) --
    
    
    SubnetId (string) -- Subnet must be in the AZ of the Flow
    
    
    
    
    
    
    
    
    
    """
    pass

def update_flow_entitlement(Description=None, Encryption=None, EntitlementArn=None, FlowArn=None, Subscribers=None):
    """
    You can change an entitlement\'s description, subscribers, and encryption. If you change the subscribers, the service will remove the outputs that are are used by the subscribers that are removed.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_flow_entitlement(
        Description='string',
        Encryption={
            'Algorithm': 'aes128'|'aes192'|'aes256',
            'ConstantInitializationVector': 'string',
            'DeviceId': 'string',
            'KeyType': 'speke'|'static-key',
            'Region': 'string',
            'ResourceId': 'string',
            'RoleArn': 'string',
            'SecretArn': 'string',
            'Url': 'string'
        },
        EntitlementArn='string',
        FlowArn='string',
        Subscribers=[
            'string',
        ]
    )
    
    
    :type Description: string
    :param Description: A description of the entitlement. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.

    :type Encryption: dict
    :param Encryption: The type of encryption that will be used on the output associated with this entitlement.\n\nAlgorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).\nConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.\nDeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nKeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nRegion (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nRoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).\nSecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.\nUrl (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.\n\n

    :type EntitlementArn: string
    :param EntitlementArn: [REQUIRED] The ARN of the entitlement that you want to update.

    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that is associated with the entitlement that you want to update.

    :type Subscribers: list
    :param Subscribers: The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.\n\n(string) --\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'Entitlement': {
        'DataTransferSubscriberFeePercent': 123,
        'Description': 'string',
        'Encryption': {
            'Algorithm': 'aes128'|'aes192'|'aes256',
            'ConstantInitializationVector': 'string',
            'DeviceId': 'string',
            'KeyType': 'speke'|'static-key',
            'Region': 'string',
            'ResourceId': 'string',
            'RoleArn': 'string',
            'SecretArn': 'string',
            'Url': 'string'
        },
        'EntitlementArn': 'string',
        'Name': 'string',
        'Subscribers': [
            'string',
        ]
    },
    'FlowArn': 'string'
}


Response Structure

(dict) -- AWS Elemental MediaConnect updated the entitlement successfully.
Entitlement (dict) -- The settings for a flow entitlement.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Description (string) -- A description of the entitlement.
Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementArn (string) -- The ARN of the entitlement.
Name (string) -- The name of the entitlement.
Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
(string) --




FlowArn (string) -- The ARN of the flow that this entitlement was granted on.






Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'Entitlement': {
            'DataTransferSubscriberFeePercent': 123,
            'Description': 'string',
            'Encryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'ConstantInitializationVector': 'string',
                'DeviceId': 'string',
                'KeyType': 'speke'|'static-key',
                'Region': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SecretArn': 'string',
                'Url': 'string'
            },
            'EntitlementArn': 'string',
            'Name': 'string',
            'Subscribers': [
                'string',
            ]
        },
        'FlowArn': 'string'
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect updated the entitlement successfully.
    Entitlement (dict) -- The settings for a flow entitlement.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Description (string) -- A description of the entitlement.
    Encryption (dict) -- The type of encryption that will be used on the output that is associated with this entitlement.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    EntitlementArn (string) -- The ARN of the entitlement.
    Name (string) -- The name of the entitlement.
    Subscribers (list) -- The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
    (string) --
    
    
    
    
    FlowArn (string) -- The ARN of the flow that this entitlement was granted on.
    
    
    
    """
    pass

def update_flow_output(CidrAllowList=None, Description=None, Destination=None, Encryption=None, FlowArn=None, MaxLatency=None, OutputArn=None, Port=None, Protocol=None, RemoteId=None, SmoothingLatency=None, StreamId=None, VpcInterfaceAttachment=None):
    """
    Updates an existing flow output.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_flow_output(
        CidrAllowList=[
            'string',
        ],
        Description='string',
        Destination='string',
        Encryption={
            'Algorithm': 'aes128'|'aes192'|'aes256',
            'ConstantInitializationVector': 'string',
            'DeviceId': 'string',
            'KeyType': 'speke'|'static-key',
            'Region': 'string',
            'ResourceId': 'string',
            'RoleArn': 'string',
            'SecretArn': 'string',
            'Url': 'string'
        },
        FlowArn='string',
        MaxLatency=123,
        OutputArn='string',
        Port=123,
        Protocol='zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
        RemoteId='string',
        SmoothingLatency=123,
        StreamId='string',
        VpcInterfaceAttachment={
            'VpcInterfaceName': 'string'
        }
    )
    
    
    :type CidrAllowList: list
    :param CidrAllowList: The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.\n\n(string) --\n\n

    :type Description: string
    :param Description: A description of the output. This description appears only on the AWS Elemental MediaConnect console and will not be seen by the end user.

    :type Destination: string
    :param Destination: The IP address where you want to send the output.

    :type Encryption: dict
    :param Encryption: The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\n\nAlgorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).\nConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.\nDeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nKeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nRegion (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nRoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).\nSecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.\nUrl (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.\n\n

    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that is associated with the output that you want to update.

    :type MaxLatency: integer
    :param MaxLatency: The maximum latency in milliseconds for Zixi-based streams.

    :type OutputArn: string
    :param OutputArn: [REQUIRED] The ARN of the output that you want to update.

    :type Port: integer
    :param Port: The port to use when content is distributed to this output.

    :type Protocol: string
    :param Protocol: The protocol to use for the output.

    :type RemoteId: string
    :param RemoteId: The remote ID for the Zixi-pull stream.

    :type SmoothingLatency: integer
    :param SmoothingLatency: The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.

    :type StreamId: string
    :param StreamId: The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.

    :type VpcInterfaceAttachment: dict
    :param VpcInterfaceAttachment: The name of the VPC interface attachment to use for this output.\n\nVpcInterfaceName (string) -- The name of the VPC interface to use for this output.\n\n

    :rtype: dict

ReturnsResponse Syntax
{
    'FlowArn': 'string',
    'Output': {
        'DataTransferSubscriberFeePercent': 123,
        'Description': 'string',
        'Destination': 'string',
        'Encryption': {
            'Algorithm': 'aes128'|'aes192'|'aes256',
            'ConstantInitializationVector': 'string',
            'DeviceId': 'string',
            'KeyType': 'speke'|'static-key',
            'Region': 'string',
            'ResourceId': 'string',
            'RoleArn': 'string',
            'SecretArn': 'string',
            'Url': 'string'
        },
        'EntitlementArn': 'string',
        'MediaLiveInputArn': 'string',
        'Name': 'string',
        'OutputArn': 'string',
        'Port': 123,
        'Transport': {
            'CidrAllowList': [
                'string',
            ],
            'MaxBitrate': 123,
            'MaxLatency': 123,
            'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
            'RemoteId': 'string',
            'SmoothingLatency': 123,
            'StreamId': 'string'
        },
        'VpcInterfaceAttachment': {
            'VpcInterfaceName': 'string'
        }
    }
}


Response Structure

(dict) -- AWS Elemental MediaConnect updated the output successfully.
FlowArn (string) -- The ARN of the flow that is associated with the updated output.
Output (dict) -- The settings for an output.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Description (string) -- A description of the output.
Destination (string) -- The address where you want to send the output.
Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


EntitlementArn (string) -- The ARN of the entitlement on the originator\'\'s flow. This value is relevant only on entitled flows.
MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
Name (string) -- The name of the output. This value must be unique within the current flow.
OutputArn (string) -- The ARN of the output.
Port (integer) -- The port to use when content is distributed to this output.
Transport (dict) -- Attributes related to the transport stream that are used in the output.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.
VpcInterfaceName (string) -- The name of the VPC interface to use for this output.










Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'Output': {
            'DataTransferSubscriberFeePercent': 123,
            'Description': 'string',
            'Destination': 'string',
            'Encryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'ConstantInitializationVector': 'string',
                'DeviceId': 'string',
                'KeyType': 'speke'|'static-key',
                'Region': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SecretArn': 'string',
                'Url': 'string'
            },
            'EntitlementArn': 'string',
            'MediaLiveInputArn': 'string',
            'Name': 'string',
            'OutputArn': 'string',
            'Port': 123,
            'Transport': {
                'CidrAllowList': [
                    'string',
                ],
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'RemoteId': 'string',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            },
            'VpcInterfaceAttachment': {
                'VpcInterfaceName': 'string'
            }
        }
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect updated the output successfully.
    FlowArn (string) -- The ARN of the flow that is associated with the updated output.
    Output (dict) -- The settings for an output.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Description (string) -- A description of the output.
    Destination (string) -- The address where you want to send the output.
    Encryption (dict) -- The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    EntitlementArn (string) -- The ARN of the entitlement on the originator\'\'s flow. This value is relevant only on entitled flows.
    MediaLiveInputArn (string) -- The input ARN of the AWS Elemental MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.
    Name (string) -- The name of the output. This value must be unique within the current flow.
    OutputArn (string) -- The ARN of the output.
    Port (integer) -- The port to use when content is distributed to this output.
    Transport (dict) -- Attributes related to the transport stream that are used in the output.
    CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    (string) --
    
    
    MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    RemoteId (string) -- The remote ID for the Zixi-pull stream.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    VpcInterfaceAttachment (dict) -- The name of the VPC interface attachment to use for this output.
    VpcInterfaceName (string) -- The name of the VPC interface to use for this output.
    
    
    
    
    
    
    
    """
    pass

def update_flow_source(Decryption=None, Description=None, EntitlementArn=None, FlowArn=None, IngestPort=None, MaxBitrate=None, MaxLatency=None, Protocol=None, SourceArn=None, StreamId=None, VpcInterfaceName=None, WhitelistCidr=None):
    """
    Updates the source of a flow.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.update_flow_source(
        Decryption={
            'Algorithm': 'aes128'|'aes192'|'aes256',
            'ConstantInitializationVector': 'string',
            'DeviceId': 'string',
            'KeyType': 'speke'|'static-key',
            'Region': 'string',
            'ResourceId': 'string',
            'RoleArn': 'string',
            'SecretArn': 'string',
            'Url': 'string'
        },
        Description='string',
        EntitlementArn='string',
        FlowArn='string',
        IngestPort=123,
        MaxBitrate=123,
        MaxLatency=123,
        Protocol='zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
        SourceArn='string',
        StreamId='string',
        VpcInterfaceName='string',
        WhitelistCidr='string'
    )
    
    
    :type Decryption: dict
    :param Decryption: The type of encryption used on the content ingested from this source.\n\nAlgorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).\nConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.\nDeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nKeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).\nRegion (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.\nRoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).\nSecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.\nUrl (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.\n\n

    :type Description: string
    :param Description: A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.

    :type EntitlementArn: string
    :param EntitlementArn: The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator\'s flow.

    :type FlowArn: string
    :param FlowArn: [REQUIRED] The flow that is associated with the source that you want to update.

    :type IngestPort: integer
    :param IngestPort: The port that the flow will be listening on for incoming content.

    :type MaxBitrate: integer
    :param MaxBitrate: The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.

    :type MaxLatency: integer
    :param MaxLatency: The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.

    :type Protocol: string
    :param Protocol: The protocol that is used by the source.

    :type SourceArn: string
    :param SourceArn: [REQUIRED] The ARN of the source that you want to update.

    :type StreamId: string
    :param StreamId: The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.

    :type VpcInterfaceName: string
    :param VpcInterfaceName: The name of the VPC Interface to configure this Source with.

    :type WhitelistCidr: string
    :param WhitelistCidr: The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

    :rtype: dict

ReturnsResponse Syntax
{
    'FlowArn': 'string',
    'Source': {
        'DataTransferSubscriberFeePercent': 123,
        'Decryption': {
            'Algorithm': 'aes128'|'aes192'|'aes256',
            'ConstantInitializationVector': 'string',
            'DeviceId': 'string',
            'KeyType': 'speke'|'static-key',
            'Region': 'string',
            'ResourceId': 'string',
            'RoleArn': 'string',
            'SecretArn': 'string',
            'Url': 'string'
        },
        'Description': 'string',
        'EntitlementArn': 'string',
        'IngestIp': 'string',
        'IngestPort': 123,
        'Name': 'string',
        'SourceArn': 'string',
        'Transport': {
            'CidrAllowList': [
                'string',
            ],
            'MaxBitrate': 123,
            'MaxLatency': 123,
            'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
            'RemoteId': 'string',
            'SmoothingLatency': 123,
            'StreamId': 'string'
        },
        'VpcInterfaceName': 'string',
        'WhitelistCidr': 'string'
    }
}


Response Structure

(dict) -- AWS Elemental MediaConnect updated the flow successfully.
FlowArn (string) -- The ARN of the flow that you want to update.
Source (dict) -- The settings for the source of the flow.
DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.


Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
IngestPort (integer) -- The port that the flow will be listening on for incoming content.
Name (string) -- The name of the source.
SourceArn (string) -- The ARN of the source.
Transport (dict) -- Attributes related to the transport stream that are used in the source.
CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
(string) --


MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
Protocol (string) -- The protocol that is used by the source or output.
RemoteId (string) -- The remote ID for the Zixi-pull stream.
SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.


VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.








Exceptions

MediaConnect.Client.exceptions.BadRequestException
MediaConnect.Client.exceptions.InternalServerErrorException
MediaConnect.Client.exceptions.ForbiddenException
MediaConnect.Client.exceptions.NotFoundException
MediaConnect.Client.exceptions.ServiceUnavailableException
MediaConnect.Client.exceptions.TooManyRequestsException


    :return: {
        'FlowArn': 'string',
        'Source': {
            'DataTransferSubscriberFeePercent': 123,
            'Decryption': {
                'Algorithm': 'aes128'|'aes192'|'aes256',
                'ConstantInitializationVector': 'string',
                'DeviceId': 'string',
                'KeyType': 'speke'|'static-key',
                'Region': 'string',
                'ResourceId': 'string',
                'RoleArn': 'string',
                'SecretArn': 'string',
                'Url': 'string'
            },
            'Description': 'string',
            'EntitlementArn': 'string',
            'IngestIp': 'string',
            'IngestPort': 123,
            'Name': 'string',
            'SourceArn': 'string',
            'Transport': {
                'CidrAllowList': [
                    'string',
                ],
                'MaxBitrate': 123,
                'MaxLatency': 123,
                'Protocol': 'zixi-push'|'rtp-fec'|'rtp'|'zixi-pull'|'rist',
                'RemoteId': 'string',
                'SmoothingLatency': 123,
                'StreamId': 'string'
            },
            'VpcInterfaceName': 'string',
            'WhitelistCidr': 'string'
        }
    }
    
    
    :returns: 
    (dict) -- AWS Elemental MediaConnect updated the flow successfully.
    FlowArn (string) -- The ARN of the flow that you want to update.
    Source (dict) -- The settings for the source of the flow.
    DataTransferSubscriberFeePercent (integer) -- Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
    Decryption (dict) -- The type of encryption that is used on the content ingested from this source.
    Algorithm (string) -- The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    ConstantInitializationVector (string) -- A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
    DeviceId (string) -- The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    KeyType (string) -- The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    Region (string) -- The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    ResourceId (string) -- An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    RoleArn (string) -- The ARN of the role that you created during setup (when you set up AWS Elemental MediaConnect as a trusted entity).
    SecretArn (string) -- The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
    Url (string) -- The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.
    
    
    Description (string) -- A description for the source. This value is not used or seen outside of the current AWS Elemental MediaConnect account.
    EntitlementArn (string) -- The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator\'s flow.
    IngestIp (string) -- The IP address that the flow will be listening on for incoming content.
    IngestPort (integer) -- The port that the flow will be listening on for incoming content.
    Name (string) -- The name of the source.
    SourceArn (string) -- The ARN of the source.
    Transport (dict) -- Attributes related to the transport stream that are used in the source.
    CidrAllowList (list) -- The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    (string) --
    
    
    MaxBitrate (integer) -- The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.
    MaxLatency (integer) -- The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
    Protocol (string) -- The protocol that is used by the source or output.
    RemoteId (string) -- The remote ID for the Zixi-pull stream.
    SmoothingLatency (integer) -- The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
    StreamId (string) -- The stream ID that you want to use for this transport. This parameter applies only to Zixi-based streams.
    
    
    VpcInterfaceName (string) -- The name of the VPC Interface this Source is configured with.
    WhitelistCidr (string) -- The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    
    
    
    
    
    """
    pass

