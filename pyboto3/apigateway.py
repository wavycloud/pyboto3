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

import boto3


class Apigateway(object):
    def __init__(self):
        self.client = boto3.client('Apigateway')

    def can_paginate(self, operation_name=None):
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
        self.client.can_paginate(operation_name=operation_name)

    def create_api_key(self, name=None, description=None, enabled=None, stageKeys=None):
        """
        :param name: The name of the ApiKey .
        :type name: string
        :param description: The description of the ApiKey .
        :type description: string
        :param enabled: Specifies whether the ApiKey can be used by callers.
        :type enabled: boolean
        :param stageKeys: Specifies whether the ApiKey can be used by callers.
            (dict) --A reference to a unique stage identified in the format {restApiId}/{stage} .
            restApiId (string) --A list of Stage resources that are associated with the ApiKey resource.
            stageName (string) --The stage name in the RestApi that the stage key references.
            
            
        :type stageKeys: list
        """
        self.client.create_api_key(name=name, description=description, enabled=enabled, stageKeys=stageKeys)

    def create_authorizer(self, restApiId=None, name=None, type=None, authType=None, authorizerUri=None,
                          authorizerCredentials=None, identitySource=None, identityValidationExpression=None,
                          authorizerResultTtlInSeconds=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier under which the Authorizer will be created.
            
        :type restApiId: string
        :param name: [REQUIRED]
            [Required] The name of the authorizer.
            
        :type name: string
        :param type: [REQUIRED]
            [Required] The type of the authorizer.
            
        :type type: string
        :param authType: Optional customer-defined field, used in Swagger imports/exports. Has no functional impact.
        :type authType: string
        :param authorizerUri: [REQUIRED]
            [Required] Specifies the authorizer's Uniform Resource Identifier (URI).
            
        :type authorizerUri: string
        :param authorizerCredentials: Specifies the credentials required for the authorizer, if any.
        :type authorizerCredentials: string
        :param identitySource: [REQUIRED]
            [Required] The source of the identity in an incoming request.
            
        :type identitySource: string
        :param identityValidationExpression: A validation expression for the incoming identity.
        :type identityValidationExpression: string
        :param authorizerResultTtlInSeconds: The TTL of cached authorizer results.
        :type authorizerResultTtlInSeconds: integer
        """
        self.client.create_authorizer(restApiId=restApiId, name=name, type=type, authType=authType,
                                      authorizerUri=authorizerUri, authorizerCredentials=authorizerCredentials,
                                      identitySource=identitySource,
                                      identityValidationExpression=identityValidationExpression,
                                      authorizerResultTtlInSeconds=authorizerResultTtlInSeconds)

    def create_base_path_mapping(self, domainName=None, basePath=None, restApiId=None, stage=None):
        """
        :param domainName: [REQUIRED]
            The domain name of the BasePathMapping resource to create.
            
        :type domainName: string
        :param basePath: The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Leave this blank if you do not want callers to specify a base path name after the domain name.
        :type basePath: string
        :param restApiId: [REQUIRED]
            The name of the API that you want to apply this mapping to.
            
        :type restApiId: string
        :param stage: The name of the API's stage that you want to use for this mapping. Leave this blank if you do not want callers to explicitly specify the stage name after any base path name.
        :type stage: string
        """
        self.client.create_base_path_mapping(domainName=domainName, basePath=basePath, restApiId=restApiId, stage=stage)

    def create_deployment(self, restApiId=None, stageName=None, stageDescription=None, description=None,
                          cacheClusterEnabled=None, cacheClusterSize=None, variables=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi resource identifier for the Deployment resource to create.
            
        :type restApiId: string
        :param stageName: [REQUIRED]
            The name of the Stage resource for the Deployment resource to create.
            
        :type stageName: string
        :param stageDescription: The description of the Stage resource for the Deployment resource to create.
        :type stageDescription: string
        :param description: The description for the Deployment resource to create.
        :type description: string
        :param cacheClusterEnabled: Enables a cache cluster for the Stage resource specified in the input.
        :type cacheClusterEnabled: boolean
        :param cacheClusterSize: Specifies the cache cluster size for the Stage resource specified in the input, if a cache cluster is enabled.
        :type cacheClusterSize: string
        :param variables: A map that defines the stage variables for the Stage resource that is associated with the new deployment. Variable names can have alphanumeric characters, and the values must match [A-Za-z0-9-._~:/?#=,]+ .
            (string) --
            (string) --
            
        :type variables: dict
        """
        self.client.create_deployment(restApiId=restApiId, stageName=stageName, stageDescription=stageDescription,
                                      description=description, cacheClusterEnabled=cacheClusterEnabled,
                                      cacheClusterSize=cacheClusterSize, variables=variables)

    def create_domain_name(self, domainName=None, certificateName=None, certificateBody=None,
                           certificatePrivateKey=None, certificateChain=None):
        """
        :param domainName: [REQUIRED]
            The name of the DomainName resource.
            
        :type domainName: string
        :param certificateName: [REQUIRED]
            The name of the certificate.
            
        :type certificateName: string
        :param certificateBody: [REQUIRED]
            The body of the server certificate provided by your certificate authority.
            
        :type certificateBody: string
        :param certificatePrivateKey: [REQUIRED]
            Your certificate's private key.
            
        :type certificatePrivateKey: string
        :param certificateChain: [REQUIRED]
            The intermediate certificates and optionally the root certificate, one after the other without any blank lines. If you include the root certificate, your certificate chain must start with intermediate certificates and end with the root certificate. Use the intermediate certificates that were provided by your certificate authority. Do not include any intermediaries that are not in the chain of trust path.
            
        :type certificateChain: string
        """
        self.client.create_domain_name(domainName=domainName, certificateName=certificateName,
                                       certificateBody=certificateBody, certificatePrivateKey=certificatePrivateKey,
                                       certificateChain=certificateChain)

    def create_model(self, restApiId=None, name=None, description=None, schema=None, contentType=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier under which the Model will be created.
            
        :type restApiId: string
        :param name: [REQUIRED]
            The name of the model.
            
        :type name: string
        :param description: The description of the model.
        :type description: string
        :param schema: The schema for the model. For application/json models, this should be JSON-schema draft v4 model.
        :type schema: string
        :param contentType: [REQUIRED]
            The content-type for the model.
            
        :type contentType: string
        """
        self.client.create_model(restApiId=restApiId, name=name, description=description, schema=schema,
                                 contentType=contentType)

    def create_resource(self, restApiId=None, parentId=None, pathPart=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi for the resource.
            
        :type restApiId: string
        :param parentId: [REQUIRED]
            The parent resource's identifier.
            
        :type parentId: string
        :param pathPart: [REQUIRED]
            The last path segment for this resource.
            
        :type pathPart: string
        """
        self.client.create_resource(restApiId=restApiId, parentId=parentId, pathPart=pathPart)

    def create_rest_api(self, name=None, description=None, cloneFrom=None):
        """
        :param name: [REQUIRED]
            The name of the RestApi .
            
        :type name: string
        :param description: The description of the RestApi .
        :type description: string
        :param cloneFrom: The Id of the RestApi that you want to clone from.
        :type cloneFrom: string
        """
        self.client.create_rest_api(name=name, description=description, cloneFrom=cloneFrom)

    def create_stage(self, restApiId=None, stageName=None, deploymentId=None, description=None,
                     cacheClusterEnabled=None, cacheClusterSize=None, variables=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Stage resource to create.
            
        :type restApiId: string
        :param stageName: [REQUIRED]
            The name for the Stage resource.
            
        :type stageName: string
        :param deploymentId: [REQUIRED]
            The identifier of the Deployment resource for the Stage resource.
            
        :type deploymentId: string
        :param description: The description of the Stage resource.
        :type description: string
        :param cacheClusterEnabled: Whether cache clustering is enabled for the stage.
        :type cacheClusterEnabled: boolean
        :param cacheClusterSize: The stage's cache cluster size.
        :type cacheClusterSize: string
        :param variables: A map that defines the stage variables for the new Stage resource. Variable names can have alphanumeric characters, and the values must match [A-Za-z0-9-._~:/?#=,]+ .
            (string) --
            (string) --
            
        :type variables: dict
        """
        self.client.create_stage(restApiId=restApiId, stageName=stageName, deploymentId=deploymentId,
                                 description=description, cacheClusterEnabled=cacheClusterEnabled,
                                 cacheClusterSize=cacheClusterSize, variables=variables)

    def delete_api_key(self, apiKey=None):
        """
        :param apiKey: [REQUIRED]
            The identifier of the ApiKey resource to be deleted.
            ReturnsNone
            
        :type apiKey: string
        """
        self.client.delete_api_key(apiKey=apiKey)

    def delete_authorizer(self, restApiId=None, authorizerId=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Authorizer resource.
            
        :type restApiId: string
        :param authorizerId: [REQUIRED]
            The identifier of the Authorizer resource.
            
        :type authorizerId: string
        """
        self.client.delete_authorizer(restApiId=restApiId, authorizerId=authorizerId)

    def delete_base_path_mapping(self, domainName=None, basePath=None):
        """
        :param domainName: [REQUIRED]
            The domain name of the BasePathMapping resource to delete.
            
        :type domainName: string
        :param basePath: [REQUIRED]
            The base path name of the BasePathMapping resource to delete.
            
        :type basePath: string
        """
        self.client.delete_base_path_mapping(domainName=domainName, basePath=basePath)

    def delete_client_certificate(self, clientCertificateId=None):
        """
        :param clientCertificateId: [REQUIRED]
            The identifier of the ClientCertificate resource to be deleted.
            ReturnsNone
            
        :type clientCertificateId: string
        """
        self.client.delete_client_certificate(clientCertificateId=clientCertificateId)

    def delete_deployment(self, restApiId=None, deploymentId=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Deployment resource to delete.
            
        :type restApiId: string
        :param deploymentId: [REQUIRED]
            The identifier of the Deployment resource to delete.
            
        :type deploymentId: string
        """
        self.client.delete_deployment(restApiId=restApiId, deploymentId=deploymentId)

    def delete_domain_name(self, domainName=None):
        """
        :param domainName: [REQUIRED]
            The name of the DomainName resource to be deleted.
            ReturnsNone
            
        :type domainName: string
        """
        self.client.delete_domain_name(domainName=domainName)

    def delete_integration(self, restApiId=None, resourceId=None, httpMethod=None):
        """
        :param restApiId: [REQUIRED]
            Specifies a delete integration request's API identifier.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            Specifies a delete integration request's resource identifier.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Specifies a delete integration request's HTTP method.
            
        :type httpMethod: string
        """
        self.client.delete_integration(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod)

    def delete_integration_response(self, restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
        """
        :param restApiId: [REQUIRED]
            Specifies a delete integration response request's API identifier.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            Specifies a delete integration response request's resource identifier.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Specifies a delete integration response request's HTTP method.
            
        :type httpMethod: string
        :param statusCode: [REQUIRED]
            Specifies a delete integration response request's status code.
            
        :type statusCode: string
        """
        self.client.delete_integration_response(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                                statusCode=statusCode)

    def delete_method(self, restApiId=None, resourceId=None, httpMethod=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Method resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            The HTTP verb that identifies the Method resource.
            
        :type httpMethod: string
        """
        self.client.delete_method(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod)

    def delete_method_response(self, restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the MethodResponse resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The Resource identifier for the MethodResponse resource.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            The HTTP verb identifier for the parent Method resource.
            
        :type httpMethod: string
        :param statusCode: [REQUIRED]
            The status code identifier for the MethodResponse resource.
            
        :type statusCode: string
        """
        self.client.delete_method_response(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                           statusCode=statusCode)

    def delete_model(self, restApiId=None, modelName=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi under which the model will be deleted.
            
        :type restApiId: string
        :param modelName: [REQUIRED]
            The name of the model to delete.
            
        :type modelName: string
        """
        self.client.delete_model(restApiId=restApiId, modelName=modelName)

    def delete_resource(self, restApiId=None, resourceId=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Resource resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The identifier of the Resource resource.
            
        :type resourceId: string
        """
        self.client.delete_resource(restApiId=restApiId, resourceId=resourceId)

    def delete_rest_api(self, restApiId=None):
        """
        :param restApiId: [REQUIRED]
            The ID of the RestApi you want to delete.
            ReturnsNone
            
        :type restApiId: string
        """
        self.client.delete_rest_api(restApiId=restApiId)

    def delete_stage(self, restApiId=None, stageName=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Stage resource to delete.
            
        :type restApiId: string
        :param stageName: [REQUIRED]
            The name of the Stage resource to delete.
            
        :type stageName: string
        """
        self.client.delete_stage(restApiId=restApiId, stageName=stageName)

    def flush_stage_authorizers_cache(self, restApiId=None, stageName=None):
        """
        :param restApiId: [REQUIRED]
            The API identifier of the stage to flush.
            
        :type restApiId: string
        :param stageName: [REQUIRED]
            The name of the stage to flush.
            
        :type stageName: string
        """
        self.client.flush_stage_authorizers_cache(restApiId=restApiId, stageName=stageName)

    def flush_stage_cache(self, restApiId=None, stageName=None):
        """
        :param restApiId: [REQUIRED]
            The API identifier of the stage to flush its cache.
            
        :type restApiId: string
        :param stageName: [REQUIRED]
            The name of the stage to flush its cache.
            
        :type stageName: string
        """
        self.client.flush_stage_cache(restApiId=restApiId, stageName=stageName)

    def generate_client_certificate(self, description=None):
        """
        :param description: The description of the ClientCertificate .
            Return typedict
            ReturnsResponse Syntax{
              'clientCertificateId': 'string',
              'description': 'string',
              'pemEncodedCertificate': 'string',
              'createdDate': datetime(2015, 1, 1),
              'expirationDate': datetime(2015, 1, 1)
            }
            Response Structure
            (dict) --Represents a Client Certificate used to configure client-side SSL authentication while sending requests to the integration endpoint.
            clientCertificateId (string) --The identifier of the Client Certificate.
            description (string) --The description of the Client Certificate.
            pemEncodedCertificate (string) --The PEM-encoded public key of the Client Certificate, that can be used to configure certificate authentication in the integration endpoint .
            createdDate (datetime) --The date when the Client Certificate was created, in ISO 8601 format .
            expirationDate (datetime) --The date when the Client Certificate will expire, in ISO 8601 format .
            
            
        :type description: string
        """
        self.client.generate_client_certificate(description=description)

    def generate_presigned_url(self, ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
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
        self.client.generate_presigned_url(ClientMethod=ClientMethod, Params=Params, ExpiresIn=ExpiresIn,
                                           HttpMethod=HttpMethod)

    def get_account(self):
        """
        """
        self.client.get_account()

    def get_api_key(self, apiKey=None):
        """
        :param apiKey: [REQUIRED]
            The identifier of the ApiKey resource.
            Return typedict
            ReturnsResponse Syntax{
              'id': 'string',
              'name': 'string',
              'description': 'string',
              'enabled': True|False,
              'stageKeys': [
                'string',
              ],
              'createdDate': datetime(2015, 1, 1),
              'lastUpdatedDate': datetime(2015, 1, 1)
            }
            Response Structure
            (dict) --A resource that can be distributed to callers for executing Method resources that require an API key. API keys can be mapped to any Stage on any RestApi , which indicates that the callers with the API key can make requests to that stage.
            id (string) --The identifier of the API Key.
            name (string) --The name of the API Key.
            description (string) --The description of the API Key.
            enabled (boolean) --Specifies whether the API Key can be used by callers.
            stageKeys (list) --A list of Stage resources that are associated with the ApiKey resource.
            (string) --
            createdDate (datetime) --The date when the API Key was created, in ISO 8601 format .
            lastUpdatedDate (datetime) --When the API Key was last updated, in ISO 8601 format.
            
            
        :type apiKey: string
        """
        self.client.get_api_key(apiKey=apiKey)

    def get_api_keys(self, position=None, limit=None):
        """
        :param position: The position of the current ApiKeys resource to get information about.
        :type position: string
        :param limit: The maximum number of ApiKeys to get information about.
        :type limit: integer
        """
        self.client.get_api_keys(position=position, limit=limit)

    def get_authorizer(self, restApiId=None, authorizerId=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Authorizer resource.
            
        :type restApiId: string
        :param authorizerId: [REQUIRED]
            The identifier of the Authorizer resource.
            
        :type authorizerId: string
        """
        self.client.get_authorizer(restApiId=restApiId, authorizerId=authorizerId)

    def get_authorizers(self, restApiId=None, position=None, limit=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Authorizers resource.
            
        :type restApiId: string
        :param position: If not all Authorizer resources in the response were present, the position will specificy where to start the next page of results.
        :type position: string
        :param limit: Limit the number of Authorizer resources in the response.
        :type limit: integer
        """
        self.client.get_authorizers(restApiId=restApiId, position=position, limit=limit)

    def get_base_path_mapping(self, domainName=None, basePath=None):
        """
        :param domainName: [REQUIRED]
            The domain name of the BasePathMapping resource to be described.
            
        :type domainName: string
        :param basePath: [REQUIRED]
            The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Leave this blank if you do not want callers to specify any base path name after the domain name.
            
        :type basePath: string
        """
        self.client.get_base_path_mapping(domainName=domainName, basePath=basePath)

    def get_base_path_mappings(self, domainName=None, position=None, limit=None):
        """
        :param domainName: [REQUIRED]
            The domain name of a BasePathMapping resource.
            
        :type domainName: string
        :param position: The position of the current BasePathMapping resource in the collection to get information about.
        :type position: string
        :param limit: The maximum number of BasePathMapping resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
        :type limit: integer
        """
        self.client.get_base_path_mappings(domainName=domainName, position=position, limit=limit)

    def get_client_certificate(self, clientCertificateId=None):
        """
        :param clientCertificateId: [REQUIRED]
            The identifier of the ClientCertificate resource to be described.
            Return typedict
            ReturnsResponse Syntax{
              'clientCertificateId': 'string',
              'description': 'string',
              'pemEncodedCertificate': 'string',
              'createdDate': datetime(2015, 1, 1),
              'expirationDate': datetime(2015, 1, 1)
            }
            Response Structure
            (dict) --Represents a Client Certificate used to configure client-side SSL authentication while sending requests to the integration endpoint.
            clientCertificateId (string) --The identifier of the Client Certificate.
            description (string) --The description of the Client Certificate.
            pemEncodedCertificate (string) --The PEM-encoded public key of the Client Certificate, that can be used to configure certificate authentication in the integration endpoint .
            createdDate (datetime) --The date when the Client Certificate was created, in ISO 8601 format .
            expirationDate (datetime) --The date when the Client Certificate will expire, in ISO 8601 format .
            
            
        :type clientCertificateId: string
        """
        self.client.get_client_certificate(clientCertificateId=clientCertificateId)

    def get_client_certificates(self, position=None, limit=None):
        """
        :param position: The position of the current ClientCertificate resource in the collection to get information about.
        :type position: string
        :param limit: The maximum number of ClientCertificate resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
        :type limit: integer
        """
        self.client.get_client_certificates(position=position, limit=limit)

    def get_deployment(self, restApiId=None, deploymentId=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Deployment resource to get information about.
            
        :type restApiId: string
        :param deploymentId: [REQUIRED]
            The identifier of the Deployment resource to get information about.
            
        :type deploymentId: string
        """
        self.client.get_deployment(restApiId=restApiId, deploymentId=deploymentId)

    def get_deployments(self, restApiId=None, position=None, limit=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the collection of Deployment resources to get information about.
            
        :type restApiId: string
        :param position: The position of the current Deployment resource in the collection to get information about.
        :type position: string
        :param limit: The maximum number of Deployment resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
        :type limit: integer
        """
        self.client.get_deployments(restApiId=restApiId, position=position, limit=limit)

    def get_domain_name(self, domainName=None):
        """
        :param domainName: [REQUIRED]
            The name of the DomainName resource.
            Return typedict
            ReturnsResponse Syntax{
              'domainName': 'string',
              'certificateName': 'string',
              'certificateUploadDate': datetime(2015, 1, 1),
              'distributionDomainName': 'string'
            }
            Response Structure
            (dict) --Represents a domain name that is contained in a simpler, more intuitive URL that can be called.
            domainName (string) --The name of the DomainName resource.
            certificateName (string) --The name of the certificate.
            certificateUploadDate (datetime) --The date when the certificate was uploaded, in ISO 8601 format .
            distributionDomainName (string) --The domain name of the Amazon CloudFront distribution. For more information, see the Amazon CloudFront documentation .
            
            
        :type domainName: string
        """
        self.client.get_domain_name(domainName=domainName)

    def get_domain_names(self, position=None, limit=None):
        """
        :param position: The position of the current domain names to get information about.
        :type position: string
        :param limit: The maximum number of DomainName resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
        :type limit: integer
        """
        self.client.get_domain_names(position=position, limit=limit)

    def get_export(self, restApiId=None, stageName=None, exportType=None, parameters=None, accepts=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi to be exported.
            
        :type restApiId: string
        :param stageName: [REQUIRED]
            The name of the Stage that will be exported.
            
        :type stageName: string
        :param exportType: [REQUIRED]
            The type of export. Currently only 'swagger' is supported.
            
        :type exportType: string
        :param parameters: A key-value map of query string parameters that specify properties of the export, depending on the requested exportType. For exportType 'swagger', any combination of the following parameters are supported: 'integrations' will export x-amazon-apigateway-integration extensions 'authorizers' will export x-amazon-apigateway-authorizer extensions 'postman' will export with Postman extensions, allowing for import to the Postman tool
            (string) --
            (string) --
            
        :type parameters: dict
        :param accepts: The content-type of the export, for example 'application/json'. Currently 'application/json' and 'application/yaml' are supported for exportType 'swagger'. Should be specifed in the 'Accept' header for direct API requests.
        :type accepts: string
        """
        self.client.get_export(restApiId=restApiId, stageName=stageName, exportType=exportType, parameters=parameters,
                               accepts=accepts)

    def get_integration(self, restApiId=None, resourceId=None, httpMethod=None):
        """
        :param restApiId: [REQUIRED]
            Specifies a get integration request's API identifier.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            Specifies a get integration request's resource identifier
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Specifies a get integration request's HTTP method.
            
        :type httpMethod: string
        """
        self.client.get_integration(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod)

    def get_integration_response(self, restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
        """
        :param restApiId: [REQUIRED]
            Specifies a get integration response request's API identifier.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            Specifies a get integration response request's resource identifier.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Specifies a get integration response request's HTTP method.
            
        :type httpMethod: string
        :param statusCode: [REQUIRED]
            Specifies a get integration response request's status code.
            
        :type statusCode: string
        """
        self.client.get_integration_response(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                             statusCode=statusCode)

    def get_method(self, restApiId=None, resourceId=None, httpMethod=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Method resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Specifies the put method request's HTTP method type.
            
        :type httpMethod: string
        """
        self.client.get_method(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod)

    def get_method_response(self, restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the MethodResponse resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The Resource identifier for the MethodResponse resource.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            The HTTP verb identifier for the parent Method resource.
            
        :type httpMethod: string
        :param statusCode: [REQUIRED]
            The status code identifier for the MethodResponse resource.
            
        :type statusCode: string
        """
        self.client.get_method_response(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                        statusCode=statusCode)

    def get_model(self, restApiId=None, modelName=None, flatten=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier under which the Model exists.
            
        :type restApiId: string
        :param modelName: [REQUIRED]
            The name of the model as an identifier.
            
        :type modelName: string
        :param flatten: Resolves all external model references and returns a flattened model schema.
        :type flatten: boolean
        """
        self.client.get_model(restApiId=restApiId, modelName=modelName, flatten=flatten)

    def get_model_template(self, restApiId=None, modelName=None):
        """
        :param restApiId: [REQUIRED]
            The ID of the RestApi under which the model exists.
            
        :type restApiId: string
        :param modelName: [REQUIRED]
            The name of the model for which to generate a template.
            
        :type modelName: string
        """
        self.client.get_model_template(restApiId=restApiId, modelName=modelName)

    def get_models(self, restApiId=None, position=None, limit=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier.
            
        :type restApiId: string
        :param position: The position of the next set of results in the Models resource to get information about.
        :type position: string
        :param limit: The maximum number of models in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
        :type limit: integer
        """
        self.client.get_models(restApiId=restApiId, position=position, limit=limit)

    def get_paginator(self, operation_name=None):
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
        self.client.get_paginator(operation_name=operation_name)

    def get_resource(self, restApiId=None, resourceId=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The identifier for the Resource resource.
            
        :type resourceId: string
        """
        self.client.get_resource(restApiId=restApiId, resourceId=resourceId)

    def get_resources(self, restApiId=None, position=None, limit=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Resource.
            
        :type restApiId: string
        :param position: The position of the next set of results in the current Resources resource to get information about.
        :type position: string
        :param limit: The maximum number of Resource resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
        :type limit: integer
        """
        self.client.get_resources(restApiId=restApiId, position=position, limit=limit)

    def get_rest_api(self, restApiId=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi resource.
            Return typedict
            ReturnsResponse Syntax{
              'id': 'string',
              'name': 'string',
              'description': 'string',
              'createdDate': datetime(2015, 1, 1),
              'warnings': [
                'string',
              ]
            }
            Response Structure
            (dict) --Represents a REST API.
            id (string) --The API's identifier. This identifier is unique across all of your APIs in Amazon API Gateway.
            name (string) --The API's name.
            description (string) --The API's description.
            createdDate (datetime) --The date when the API was created, in ISO 8601 format .
            warnings (list) --
            (string) --
            
            
        :type restApiId: string
        """
        self.client.get_rest_api(restApiId=restApiId)

    def get_rest_apis(self, position=None, limit=None):
        """
        :param position: The position of the current RestApis resource in the collection to get information about.
        :type position: string
        :param limit: The maximum number of RestApi resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
        :type limit: integer
        """
        self.client.get_rest_apis(position=position, limit=limit)

    def get_sdk(self, restApiId=None, stageName=None, sdkType=None, parameters=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi that the SDK will use.
            
        :type restApiId: string
        :param stageName: [REQUIRED]
            The name of the Stage that the SDK will use.
            
        :type stageName: string
        :param sdkType: [REQUIRED]
            The language for the generated SDK. Currently javascript, android, and objectivec (for iOS) are supported.
            
        :type sdkType: string
        :param parameters: A key-value map of query string parameters that specify properties of the SDK, depending on the requested sdkType. For sdkType 'objectivec', a parameter named 'classPrefix' is required. For sdkType 'android', parameters named 'groupId', 'artifactId', 'artifactVersion', and 'invokerPackage' are required.
            (string) --
            (string) --
            
        :type parameters: dict
        """
        self.client.get_sdk(restApiId=restApiId, stageName=stageName, sdkType=sdkType, parameters=parameters)

    def get_stage(self, restApiId=None, stageName=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Stage resource to get information about.
            
        :type restApiId: string
        :param stageName: [REQUIRED]
            The name of the Stage resource to get information about.
            
        :type stageName: string
        """
        self.client.get_stage(restApiId=restApiId, stageName=stageName)

    def get_stages(self, restApiId=None, deploymentId=None):
        """
        :param restApiId: [REQUIRED]
            The stages' API identifiers.
            
        :type restApiId: string
        :param deploymentId: The stages' deployment identifiers.
        :type deploymentId: string
        """
        self.client.get_stages(restApiId=restApiId, deploymentId=deploymentId)

    def get_waiter(self):
        """
        """
        self.client.get_waiter()

    def import_rest_api(self, failOnWarnings=None, parameters=None, body=None):
        """
        :param failOnWarnings: A query parameter to indicate whether to rollback the API creation (true ) or not (false ) when a warning is encountered. The default value is false .
        :type failOnWarnings: boolean
        :param parameters: Custom header parameters as part of the request.
            (string) --
            (string) --
            
        :type parameters: dict
        :param body: [REQUIRED]
            The POST request body containing external API definitions. Currently, only Swagger definition JSON files are supported.
            
        :type body: bytes or seekable file-like object
        """
        self.client.import_rest_api(failOnWarnings=failOnWarnings, parameters=parameters, body=body)

    def put_integration(self, restApiId=None, resourceId=None, httpMethod=None, type=None, integrationHttpMethod=None,
                        uri=None, credentials=None, requestParameters=None, requestTemplates=None,
                        passthroughBehavior=None, cacheNamespace=None, cacheKeyParameters=None):
        """
        :param restApiId: [REQUIRED]
            Specifies a put integration request's API identifier.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            Specifies a put integration request's resource ID.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Specifies a put integration request's HTTP method.
            
        :type httpMethod: string
        :param type: [REQUIRED]
            Specifies a put integration input's type.
            
        :type type: string
        :param integrationHttpMethod: Specifies a put integration HTTP method. When the integration type is HTTP or AWS, this field is required.
        :type integrationHttpMethod: string
        :param uri: Specifies a put integration input's Uniform Resource Identifier (URI). When the integration type is HTTP or AWS, this field is required. For integration with Lambda as an AWS service proxy, this value is of the 'arn:aws:apigateway:region:lambda:path/2015-03-31/functions/functionArn/invocations' format.
        :type uri: string
        :param credentials: Specifies whether credentials are required for a put integration.
        :type credentials: string
        :param requestParameters: Represents request parameters that are sent with the backend request. Request parameters are represented as a key/value map, with a destination as the key and a source as the value. A source must match an existing method request parameter, or a static value. Static values must be enclosed with single quotes, and be pre-encoded based on their destination in the request. The destination must match the pattern integration.request.{location}.{name} , where location is either querystring, path, or header. name must be a valid, unique parameter name.
            (string) --
            (string) --
            
        :type requestParameters: dict
        :param requestTemplates: Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.
            (string) --
            (string) --
            
        :type requestTemplates: dict
        :param passthroughBehavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available requestTemplates defined on the Integration. There are three valid values: WHEN_NO_MATCH , WHEN_NO_TEMPLATES , and NEVER .
            WHEN_NO_MATCH passes the request body for unmapped content types through to the Integration backend without transformation.
            NEVER rejects unmapped content types with an HTTP 415 'Unsupported Media Type' response.
            WHEN_NO_TEMPLATES will allow pass-through when the Integration has NO content types mapped to templates. However if there is at least one content type defined, unmapped content types will be rejected with the same 415 response.
            
        :type passthroughBehavior: string
        :param cacheNamespace: Specifies a put integration input's cache namespace.
        :type cacheNamespace: string
        :param cacheKeyParameters: Specifies a put integration input's cache key parameters.
            (string) --
            
        :type cacheKeyParameters: list
        """
        self.client.put_integration(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod, type=type,
                                    integrationHttpMethod=integrationHttpMethod, uri=uri, credentials=credentials,
                                    requestParameters=requestParameters, requestTemplates=requestTemplates,
                                    passthroughBehavior=passthroughBehavior, cacheNamespace=cacheNamespace,
                                    cacheKeyParameters=cacheKeyParameters)

    def put_integration_response(self, restApiId=None, resourceId=None, httpMethod=None, statusCode=None,
                                 selectionPattern=None, responseParameters=None, responseTemplates=None):
        """
        :param restApiId: [REQUIRED]
            Specifies a put integration response request's API identifier.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            Specifies a put integration response request's resource identifier.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Specifies a put integration response request's HTTP method.
            
        :type httpMethod: string
        :param statusCode: [REQUIRED]
            Specifies the status code that is used to map the integration response to an existing MethodResponse .
            
        :type statusCode: string
        :param selectionPattern: Specifies the selection pattern of a put integration response.
        :type selectionPattern: string
        :param responseParameters: Represents response parameters that can be read from the backend response. Response parameters are represented as a key/value map, with a destination as the key and a source as the value. A destination must match an existing response parameter in the Method . The source can be a header from the backend response, or a static value. Static values are specified using enclosing single quotes, and backend response headers can be read using the pattern integration.response.header.{name} .
            (string) --
            (string) --
            
        :type responseParameters: dict
        :param responseTemplates: Specifies a put integration response's templates.
            (string) --
            (string) --
            
        :type responseTemplates: dict
        """
        self.client.put_integration_response(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                             statusCode=statusCode, selectionPattern=selectionPattern,
                                             responseParameters=responseParameters, responseTemplates=responseTemplates)

    def put_method(self, restApiId=None, resourceId=None, httpMethod=None, authorizationType=None, authorizerId=None,
                   apiKeyRequired=None, requestParameters=None, requestModels=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the new Method resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The Resource identifier for the new Method resource.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Specifies the put method request's HTTP method type.
            
        :type httpMethod: string
        :param authorizationType: [REQUIRED]
            Specifies the type of authorization used for the method.
            
        :type authorizationType: string
        :param authorizerId: Specifies the identifier of an Authorizer to use on this Method, if the type is CUSTOM.
        :type authorizerId: string
        :param apiKeyRequired: Specifies whether the method required a valid ApiKey .
        :type apiKeyRequired: boolean
        :param requestParameters: Represents requests parameters that are sent with the backend request. Request parameters are represented as a key/value map, with a destination as the key and a source as the value. A source must match an existing method request parameter, or a static value. Static values must be enclosed with single quotes, and be pre-encoded based on their destination in the request. The destination must match the pattern integration.request.{location}.{name} , where location is either querystring, path, or header. name must be a valid, unique parameter name.
            (string) --
            (boolean) --
            
        :type requestParameters: dict
        :param requestModels: Specifies the Model resources used for the request's content type. Request models are represented as a key/value map, with a content type as the key and a Model name as the value.
            (string) --
            (string) --
            
        :type requestModels: dict
        """
        self.client.put_method(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                               authorizationType=authorizationType, authorizerId=authorizerId,
                               apiKeyRequired=apiKeyRequired, requestParameters=requestParameters,
                               requestModels=requestModels)

    def put_method_response(self, restApiId=None, resourceId=None, httpMethod=None, statusCode=None,
                            responseParameters=None, responseModels=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Method resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            The HTTP verb that identifies the Method resource.
            
        :type httpMethod: string
        :param statusCode: [REQUIRED]
            The method response's status code.
            
        :type statusCode: string
        :param responseParameters: Represents response parameters that can be sent back to the caller by Amazon API Gateway. Response parameters are represented as a key/value map, with a destination as the key and a Boolean flag as the value. The Boolean flag is used to specify whether the parameter is required. A destination must match the pattern method.response.header.{name} , where name is a valid, unique header name. Destinations specified here are available to the integration for mapping from integration response parameters.
            (string) --
            (boolean) --
            
        :type responseParameters: dict
        :param responseModels: Specifies the Model resources used for the response's content type. Response models are represented as a key/value map, with a content type as the key and a Model name as the value.
            (string) --
            (string) --
            
        :type responseModels: dict
        """
        self.client.put_method_response(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                        statusCode=statusCode, responseParameters=responseParameters,
                                        responseModels=responseModels)

    def put_rest_api(self, restApiId=None, mode=None, failOnWarnings=None, parameters=None, body=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi to be updated.
            
        :type restApiId: string
        :param mode: The mode query parameter to specify the update mode. Valid values are 'merge' and 'overwrite'. By default, the update mode is 'merge'.
        :type mode: string
        :param failOnWarnings: A query parameter to indicate whether to rollback the API update (true ) or not (false ) when a warning is encountered. The default value is false .
        :type failOnWarnings: boolean
        :param parameters: Custom headers supplied as part of the request.
            (string) --
            (string) --
            
        :type parameters: dict
        :param body: [REQUIRED]
            The PUT request body containing external API definitions. Currently, only Swagger definition JSON files are supported.
            
        :type body: bytes or seekable file-like object
        """
        self.client.put_rest_api(restApiId=restApiId, mode=mode, failOnWarnings=failOnWarnings, parameters=parameters,
                                 body=body)

    def test_invoke_authorizer(self, restApiId=None, authorizerId=None, headers=None, pathWithQueryString=None,
                               body=None, stageVariables=None, additionalContext=None):
        """
        :param restApiId: [REQUIRED]
            Specifies a test invoke authorizer request's RestApi identifier.
            
        :type restApiId: string
        :param authorizerId: [REQUIRED]
            Specifies a test invoke authorizer request's Authorizer ID.
            
        :type authorizerId: string
        :param headers: [Required] A key-value map of headers to simulate an incoming invocation request. This is where the incoming authorization token, or identity source, should be specified.
            (string) --
            (string) --
            
        :type headers: dict
        :param pathWithQueryString: [Optional] The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters.
        :type pathWithQueryString: string
        :param body: [Optional] The simulated request body of an incoming invocation request.
        :type body: string
        :param stageVariables: A key-value map of stage variables to simulate an invocation on a deployed Stage .
            (string) --
            (string) --
            
        :type stageVariables: dict
        :param additionalContext: [Optional] A key-value map of additional context variables.
            (string) --
            (string) --
            
        :type additionalContext: dict
        """
        self.client.test_invoke_authorizer(restApiId=restApiId, authorizerId=authorizerId, headers=headers,
                                           pathWithQueryString=pathWithQueryString, body=body,
                                           stageVariables=stageVariables, additionalContext=additionalContext)

    def test_invoke_method(self, restApiId=None, resourceId=None, httpMethod=None, pathWithQueryString=None, body=None,
                           headers=None, clientCertificateId=None, stageVariables=None):
        """
        :param restApiId: [REQUIRED]
            Specifies a test invoke method request's API identifier.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            Specifies a test invoke method request's resource ID.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Specifies a test invoke method request's HTTP method.
            
        :type httpMethod: string
        :param pathWithQueryString: The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters.
        :type pathWithQueryString: string
        :param body: The simulated request body of an incoming invocation request.
        :type body: string
        :param headers: A key-value map of headers to simulate an incoming invocation request.
            (string) --
            (string) --
            
        :type headers: dict
        :param clientCertificateId: A ClientCertificate identifier to use in the test invocation. API Gateway will use use the certificate when making the HTTPS request to the defined backend endpoint.
        :type clientCertificateId: string
        :param stageVariables: A key-value map of stage variables to simulate an invocation on a deployed Stage .
            (string) --
            (string) --
            
        :type stageVariables: dict
        """
        self.client.test_invoke_method(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                       pathWithQueryString=pathWithQueryString, body=body, headers=headers,
                                       clientCertificateId=clientCertificateId, stageVariables=stageVariables)

    def update_account(self, patchOperations=None):
        """
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            Return typedict
            ReturnsResponse Syntax{
              'cloudwatchRoleArn': 'string',
              'throttleSettings': {
                'burstLimit': 123,
                'rateLimit': 123.0
              }
            }
            Response Structure
            (dict) --Represents an AWS account that is associated with Amazon API Gateway.
            cloudwatchRoleArn (string) --Specifies the Amazon resource name (ARN) of an Amazon CloudWatch role for the current Account resource.
            throttleSettings (dict) --Specifies the application programming interface (API) throttle settings for the current Account resource.
            burstLimit (integer) --Returns the burstLimit when ThrottleSettings is called.
            rateLimit (float) --Returns the rateLimit when ThrottleSettings is called.
            
            
            
        :type patchOperations: list
        """
        self.client.update_account(patchOperations=patchOperations)

    def update_api_key(self, apiKey=None, patchOperations=None):
        """
        :param apiKey: [REQUIRED]
            The identifier of the ApiKey resource to be updated.
            
        :type apiKey: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_api_key(apiKey=apiKey, patchOperations=patchOperations)

    def update_authorizer(self, restApiId=None, authorizerId=None, patchOperations=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Authorizer resource.
            
        :type restApiId: string
        :param authorizerId: [REQUIRED]
            The identifier of the Authorizer resource.
            
        :type authorizerId: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_authorizer(restApiId=restApiId, authorizerId=authorizerId, patchOperations=patchOperations)

    def update_base_path_mapping(self, domainName=None, basePath=None, patchOperations=None):
        """
        :param domainName: [REQUIRED]
            The domain name of the BasePathMapping resource to change.
            
        :type domainName: string
        :param basePath: [REQUIRED]
            The base path of the BasePathMapping resource to change.
            
        :type basePath: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_base_path_mapping(domainName=domainName, basePath=basePath, patchOperations=patchOperations)

    def update_client_certificate(self, clientCertificateId=None, patchOperations=None):
        """
        :param clientCertificateId: [REQUIRED]
            The identifier of the ClientCertificate resource to be updated.
            
        :type clientCertificateId: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_client_certificate(clientCertificateId=clientCertificateId, patchOperations=patchOperations)

    def update_deployment(self, restApiId=None, deploymentId=None, patchOperations=None):
        """
        :param restApiId: [REQUIRED]
            The replacement identifier of the RestApi resource for the Deployment resource to change information about.
            
        :type restApiId: string
        :param deploymentId: [REQUIRED]
            The replacment identifier for the Deployment resource to change information about.
            
        :type deploymentId: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_deployment(restApiId=restApiId, deploymentId=deploymentId, patchOperations=patchOperations)

    def update_domain_name(self, domainName=None, patchOperations=None):
        """
        :param domainName: [REQUIRED]
            The name of the DomainName resource to be changed.
            
        :type domainName: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_domain_name(domainName=domainName, patchOperations=patchOperations)

    def update_integration(self, restApiId=None, resourceId=None, httpMethod=None, patchOperations=None):
        """
        :param restApiId: [REQUIRED]
            Represents an update integration request's API identifier.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            Represents an update integration request's resource identifier.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Represents an update integration request's HTTP method.
            
        :type httpMethod: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_integration(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                       patchOperations=patchOperations)

    def update_integration_response(self, restApiId=None, resourceId=None, httpMethod=None, statusCode=None,
                                    patchOperations=None):
        """
        :param restApiId: [REQUIRED]
            Specifies an update integration response request's API identifier.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            Specifies an update integration response request's resource identifier.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            Specifies an update integration response request's HTTP method.
            
        :type httpMethod: string
        :param statusCode: [REQUIRED]
            Specifies an update integration response request's status code.
            
        :type statusCode: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_integration_response(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                                statusCode=statusCode, patchOperations=patchOperations)

    def update_method(self, restApiId=None, resourceId=None, httpMethod=None, patchOperations=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Method resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            The HTTP verb that identifies the Method resource.
            
        :type httpMethod: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_method(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                  patchOperations=patchOperations)

    def update_method_response(self, restApiId=None, resourceId=None, httpMethod=None, statusCode=None,
                               patchOperations=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the MethodResponse resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The Resource identifier for the MethodResponse resource.
            
        :type resourceId: string
        :param httpMethod: [REQUIRED]
            The HTTP verb identifier for the parent Method resource.
            
        :type httpMethod: string
        :param statusCode: [REQUIRED]
            The status code identifier for the MethodResponse resource.
            
        :type statusCode: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_method_response(restApiId=restApiId, resourceId=resourceId, httpMethod=httpMethod,
                                           statusCode=statusCode, patchOperations=patchOperations)

    def update_model(self, restApiId=None, modelName=None, patchOperations=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier under which the model exists.
            
        :type restApiId: string
        :param modelName: [REQUIRED]
            The name of the model to update.
            
        :type modelName: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_model(restApiId=restApiId, modelName=modelName, patchOperations=patchOperations)

    def update_resource(self, restApiId=None, resourceId=None, patchOperations=None):
        """
        :param restApiId: [REQUIRED]
            The RestApi identifier for the Resource resource.
            
        :type restApiId: string
        :param resourceId: [REQUIRED]
            The identifier of the Resource resource.
            
        :type resourceId: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_resource(restApiId=restApiId, resourceId=resourceId, patchOperations=patchOperations)

    def update_rest_api(self, restApiId=None, patchOperations=None):
        """
        :param restApiId: [REQUIRED]
            The ID of the RestApi you want to update.
            
        :type restApiId: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_rest_api(restApiId=restApiId, patchOperations=patchOperations)

    def update_stage(self, restApiId=None, stageName=None, patchOperations=None):
        """
        :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Stage resource to change information about.
            
        :type restApiId: string
        :param stageName: [REQUIRED]
            The name of the Stage resource to change information about.
            
        :type stageName: string
        :param patchOperations: A list of operations describing the updates to apply to the specified resource. The patches are applied in the order specified in the list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --A patch operation whose value indicates the operation to perform. Its value MUST be one of 'add', 'remove', 'replace', 'move', 'copy', or 'test'; other values are errors.
            path (string) --Operation objects MUST have exactly one 'path' member. That member's value is a string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.
            value (string) --The actual value content.
            from (string) --The 'move' and 'copy' operation object MUST contain a 'from' member, which is a string containing a JSON Pointer value that references the location in the target document to move the value from.
            
            
        :type patchOperations: list
        """
        self.client.update_stage(restApiId=restApiId, stageName=stageName, patchOperations=patchOperations)
