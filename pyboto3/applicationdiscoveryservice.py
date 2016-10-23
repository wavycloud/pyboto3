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


def create_tags(configurationIds=None, tags=None):
    """
    :param configurationIds: [REQUIRED]
            A list of configuration items that you want to tag.
            (string) --
            
    :type configurationIds: list
    :param tags: [REQUIRED]
            Tags that you want to associate with one or more configuration items. Specify the tags that you want to create in a key -value format. For example:
            {'key': 'serverType', 'value': 'webServer'}
            (dict) --Metadata that help you categorize IT assets.
            key (string) -- [REQUIRED]A type of tag to filter on.
            value (string) -- [REQUIRED]A value for a tag key to filter on.
            
            
    :type tags: list
    """
    pass


def delete_tags(configurationIds=None, tags=None):
    """
    :param configurationIds: [REQUIRED]
            A list of configuration items with tags that you want to delete.
            (string) --
            
    :type configurationIds: list
    :param tags: Tags that you want to delete from one or more configuration items. Specify the tags that you want to delete in a key -value format. For example:
            {'key': 'serverType', 'value': 'webServer'}
            (dict) --Metadata that help you categorize IT assets.
            key (string) -- [REQUIRED]A type of tag to filter on.
            value (string) -- [REQUIRED]A value for a tag key to filter on.
            
            
    :type tags: list
    """
    pass


def describe_agents(agentIds=None, maxResults=None, nextToken=None):
    """
    :param agentIds: The agent IDs for which you want information. If you specify no IDs, the system returns information about all agents associated with your AWS user account.
            (string) --
            
    :type agentIds: list
    :param maxResults: The total number of agents to return. The maximum value is 100.
    :type maxResults: integer
    :param nextToken: A token to start the list. Use this token to get the next set of results.
    :type nextToken: string
    """
    pass


def describe_configurations(configurationIds=None):
    """
    :param configurationIds: [REQUIRED]
            One or more configuration IDs.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'configurations': [
                {
                  'string': 'string'
                },
              ]
            }
            Response Structure
            (dict) --
            configurations (list) --A key in the response map. The value is an array of data.
            (dict) --
            (string) --
            (string) --
            
            
            
    :type configurationIds: list
    """
    pass


def describe_export_configurations(exportIds=None, maxResults=None, nextToken=None):
    """
    :param exportIds: A unique identifier that you can use to query the export status.
            (string) --
            
    :type exportIds: list
    :param maxResults: The maximum number of results that you want to display as a part of the query.
    :type maxResults: integer
    :param nextToken: A token to get the next set of results. For example, if you specified 100 IDs for DescribeConfigurationsRequest$configurationIds but set DescribeExportConfigurationsRequest$maxResults to 10, you will get results in a set of 10. Use the token in the query to get the next set of 10.
    :type nextToken: string
    """
    pass


def describe_tags(filters=None, maxResults=None, nextToken=None):
    """
    :param filters: You can filter the list using a key -value format. You can separate these items by using logical operators. Allowed filters include tagKey , tagValue , and configurationId .
            (dict) --The name of a tag filter. Valid names are: tagKey , tagValue , configurationId .
            name (string) -- [REQUIRED]A name of a tag filter.
            values (list) -- [REQUIRED]Values of a tag filter.
            (string) --
            
            
    :type filters: list
    :param maxResults: The total number of items to return. The maximum value is 100.
    :type maxResults: integer
    :param nextToken: A token to start the list. Use this token to get the next set of results.
    :type nextToken: string
    """
    pass


def export_configurations():
    """
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


def list_configurations(configurationType=None, filters=None, maxResults=None, nextToken=None):
    """
    :param configurationType: [REQUIRED]
            A valid configuration identified by the Discovery Service.
            
    :type configurationType: string
    :param filters: You can filter the list using a key -value format. For example:
            {'key': 'serverType', 'value': 'webServer'}
            You can separate these items by using logical operators.
            (dict) --A filter that can use conditional operators.
            name (string) -- [REQUIRED]The name of the filter. The following filter names are allowed for SERVER configuration items.
            Server
            server.hostName
            server.osName
            server.osVersion
            server.configurationid
            server.agentid
            The name of the filter. The following filter names are allowed for PROCESS configuration items.
            Process
            process.configurationid
            process.name
            process.commandLine
            server.configurationid
            server.hostName
            server.osName
            server.osVersion
            server.agentId
            The name of the filter. The following filter names are allowed for CONNECTION configuration items.
            Connection
            connection.sourceIp
            connection.destinationIp
            connection.destinationPort
            sourceProcess.configurationId
            sourceProcess.name
            sourceProcess.commandLine
            destinationProcess.configurationId
            destinationProcess.name
            destinationProcess.commandLine
            sourceServer.configurationId
            sourceServer.hostName
            sourceServer.osName
            sourceServer.osVersion
            sourceServer.agentId
            destinationServer.configurationId
            destinationServer.hostName
            destinationServer.osName
            destinationServer.osVersion
            destinationServer.agentId
            values (list) -- [REQUIRED]A string value that you want to filter on. For example, if you choose the destinationServer.osVersion filter name, you could specify Ubuntu for the value.
            (string) --
            condition (string) -- [REQUIRED]A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by AND . If you specify multiple values for a particular filter, the system differentiates the values using OR . Calling either DescribeConfigurations or ListConfigurations returns attributes of matching configuration items.
            
            
    :type filters: list
    :param maxResults: The total number of items to return. The maximum value is 100.
    :type maxResults: integer
    :param nextToken: A token to start the list. Use this token to get the next set of results.
    :type nextToken: string
    """
    pass


def start_data_collection_by_agent_ids(agentIds=None):
    """
    :param agentIds: [REQUIRED]
            The IDs of the agents that you want to start collecting data. If you send a request to an AWS agent ID that you do not have permission to contact, according to your AWS account, the service does not throw an exception. Instead, it returns the error in the Description field. If you send a request to multiple agents and you do not have permission to contact some of those agents, the system does not throw an exception. Instead, the system shows Failed in the Description field.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'agentsConfigurationStatus': [
                {
                  'agentId': 'string',
                  'operationSucceeded': True|False,
                  'description': 'string'
                },
              ]
            }
            Response Structure
            (dict) --
            agentsConfigurationStatus (list) --Information about agents that were instructed to start collecting data. Information includes the agent ID, a description of the operation performed, and whether or not the agent configuration was updated.
            (dict) --Information about agents that were instructed to start collecting data. Information includes the agent ID, a description of the operation, and whether or not the agent configuration was updated.
            agentId (string) --The agent ID.
            operationSucceeded (boolean) --Information about the status of the StartDataCollection and StopDataCollection operations. The system has recorded the data collection operation. The agent receives this command the next time it polls for a new command.
            description (string) --A description of the operation performed.
            
            
            
    :type agentIds: list
    """
    pass


def stop_data_collection_by_agent_ids(agentIds=None):
    """
    :param agentIds: [REQUIRED]
            The IDs of the agents that you want to stop collecting data.
            (string) --
            Return typedict
            ReturnsResponse Syntax{
              'agentsConfigurationStatus': [
                {
                  'agentId': 'string',
                  'operationSucceeded': True|False,
                  'description': 'string'
                },
              ]
            }
            Response Structure
            (dict) --
            agentsConfigurationStatus (list) --Information about agents that were instructed to stop collecting data. Information includes the agent ID, a description of the operation performed, and whether or not the agent configuration was updated.
            (dict) --Information about agents that were instructed to start collecting data. Information includes the agent ID, a description of the operation, and whether or not the agent configuration was updated.
            agentId (string) --The agent ID.
            operationSucceeded (boolean) --Information about the status of the StartDataCollection and StopDataCollection operations. The system has recorded the data collection operation. The agent receives this command the next time it polls for a new command.
            description (string) --A description of the operation performed.
            
            
            
    :type agentIds: list
    """
    pass
