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


def create_api_key(name=None, description=None, enabled=None, generateDistinctId=None, value=None, stageKeys=None):
    """
    :param name: The name of the ApiKey .
    :type name: string
    :param description: The description of the ApiKey .
    :type description: string
    :param enabled: Specifies whether the ApiKey can be used by callers.
    :type enabled: boolean
    :param generateDistinctId: Specifies whether (true ) or not (false ) the key identifier is distinct from the created API key value.
    :type generateDistinctId: boolean
    :param value: Specifies a value of the API key.
    :type value: string
    :param stageKeys: DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.
            (dict) --A reference to a unique stage identified in the format {restApiId}/{stage} .
            restApiId (string) --A list of Stage resources that are associated with the ApiKey resource.
            stageName (string) --The stage name in the RestApi that the stage key references.
            
            
    :type stageKeys: list
    """
    pass


def create_authorizer(restApiId=None, name=None, type=None, providerARNs=None, authType=None, authorizerUri=None,
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
    :param providerARNs: A list of the Cognito Your User Pool authorizer's provider ARNs.
            (string) --
            
    :type providerARNs: list
    :param authType: Optional customer-defined field, used in Swagger imports/exports. Has no functional impact.
    :type authType: string
    :param authorizerUri: [Required] Specifies the authorizer's Uniform Resource Identifier (URI).
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
    pass


def create_base_path_mapping(domainName=None, basePath=None, restApiId=None, stage=None):
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
    pass


def create_deployment(restApiId=None, stageName=None, stageDescription=None, description=None, cacheClusterEnabled=None,
                      cacheClusterSize=None, variables=None):
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
    :param variables: A map that defines the stage variables for the Stage resource that is associated with the new deployment. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#=,]+ .
            (string) --
            (string) --
            
    :type variables: dict
    """
    pass


def create_domain_name(domainName=None, certificateName=None, certificateBody=None, certificatePrivateKey=None,
                       certificateChain=None):
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
    pass


def create_model(restApiId=None, name=None, description=None, schema=None, contentType=None):
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
    pass


def create_resource(restApiId=None, parentId=None, pathPart=None):
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
    pass


def create_rest_api(name=None, description=None, cloneFrom=None):
    """
    :param name: [REQUIRED]
            The name of the RestApi .
            
    :type name: string
    :param description: The description of the RestApi .
    :type description: string
    :param cloneFrom: The ID of the RestApi that you want to clone from.
    :type cloneFrom: string
    """
    pass


def create_stage(restApiId=None, stageName=None, deploymentId=None, description=None, cacheClusterEnabled=None,
                 cacheClusterSize=None, variables=None):
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
    :param variables: A map that defines the stage variables for the new Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#=,]+ .
            (string) --
            (string) --
            
    :type variables: dict
    """
    pass


def create_usage_plan(name=None, description=None, apiStages=None, throttle=None, quota=None):
    """
    :param name: [REQUIRED]
            The name of the usage plan.
            
    :type name: string
    :param description: The description of the usage plan.
    :type description: string
    :param apiStages: The associated API stages of the usage plan.
            (dict) --API stage name of the associated API stage in a usage plan.
            apiId (string) --API Id of the associated API stage in a usage plan.
            stage (string) --API stage name of the associated API stage in a usage plan.
            
            
    :type apiStages: list
    :param throttle: The throttling limits of the usage plan.
            burstLimit (integer) --The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
            rateLimit (float) --The API request steady-state rate limit.
            
    :type throttle: dict
    :param quota: The quota of the usage plan.
            limit (integer) --The maximum number of requests that can be made in a given time period.
            offset (integer) --The number of requests subtracted from the given limit in the initial time period.
            period (string) --The time period in which the limit applies. Valid values are 'DAY', 'WEEK' or 'MONTH'.
            
    :type quota: dict
    """
    pass


def create_usage_plan_key(usagePlanId=None, keyId=None, keyType=None):
    """
    :param usagePlanId: [REQUIRED]
            The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer.
            
    :type usagePlanId: string
    :param keyId: [REQUIRED]
            The identifier of a UsagePlanKey resource for a plan customer.
            
    :type keyId: string
    :param keyType: [REQUIRED]
            The type of a UsagePlanKey resource for a plan customer.
            
    :type keyType: string
    """
    pass


def delete_api_key(apiKey=None):
    """
    :param apiKey: [REQUIRED]
            The identifier of the ApiKey resource to be deleted.
            ReturnsNone
            
    :type apiKey: string
    """
    pass


def delete_authorizer(restApiId=None, authorizerId=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Authorizer resource.
            
    :type restApiId: string
    :param authorizerId: [REQUIRED]
            The identifier of the Authorizer resource.
            
    :type authorizerId: string
    """
    pass


def delete_base_path_mapping(domainName=None, basePath=None):
    """
    :param domainName: [REQUIRED]
            The domain name of the BasePathMapping resource to delete.
            
    :type domainName: string
    :param basePath: [REQUIRED]
            The base path name of the BasePathMapping resource to delete.
            
    :type basePath: string
    """
    pass


def delete_client_certificate(clientCertificateId=None):
    """
    :param clientCertificateId: [REQUIRED]
            The identifier of the ClientCertificate resource to be deleted.
            ReturnsNone
            
    :type clientCertificateId: string
    """
    pass


def delete_deployment(restApiId=None, deploymentId=None):
    """
    :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Deployment resource to delete.
            
    :type restApiId: string
    :param deploymentId: [REQUIRED]
            The identifier of the Deployment resource to delete.
            
    :type deploymentId: string
    """
    pass


def delete_domain_name(domainName=None):
    """
    :param domainName: [REQUIRED]
            The name of the DomainName resource to be deleted.
            ReturnsNone
            
    :type domainName: string
    """
    pass


def delete_integration(restApiId=None, resourceId=None, httpMethod=None):
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
    pass


def delete_integration_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
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
    pass


def delete_method(restApiId=None, resourceId=None, httpMethod=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Method resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            
    :type resourceId: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            
    :type httpMethod: string
    """
    pass


def delete_method_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the MethodResponse resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the MethodResponse resource.
            
    :type resourceId: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            
    :type httpMethod: string
    :param statusCode: [REQUIRED]
            The status code identifier for the MethodResponse resource.
            
    :type statusCode: string
    """
    pass


def delete_model(restApiId=None, modelName=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi under which the model will be deleted.
            
    :type restApiId: string
    :param modelName: [REQUIRED]
            The name of the model to delete.
            
    :type modelName: string
    """
    pass


def delete_resource(restApiId=None, resourceId=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Resource resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The identifier of the Resource resource.
            
    :type resourceId: string
    """
    pass


def delete_rest_api(restApiId=None):
    """
    :param restApiId: [REQUIRED]
            The ID of the RestApi you want to delete.
            ReturnsNone
            
    :type restApiId: string
    """
    pass


def delete_stage(restApiId=None, stageName=None):
    """
    :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Stage resource to delete.
            
    :type restApiId: string
    :param stageName: [REQUIRED]
            The name of the Stage resource to delete.
            
    :type stageName: string
    """
    pass


def delete_usage_plan(usagePlanId=None):
    """
    :param usagePlanId: [REQUIRED]
            The Id of the to-be-deleted usage plan.
            ReturnsNone
            
    :type usagePlanId: string
    """
    pass


def delete_usage_plan_key(usagePlanId=None, keyId=None):
    """
    :param usagePlanId: [REQUIRED]
            The Id of the UsagePlan resource representing the usage plan containing the to-be-deleted UsagePlanKey resource representing a plan customer.
            
    :type usagePlanId: string
    :param keyId: [REQUIRED]
            The Id of the UsagePlanKey resource to be deleted.
            
    :type keyId: string
    """
    pass


def flush_stage_authorizers_cache(restApiId=None, stageName=None):
    """
    :param restApiId: [REQUIRED]
            The API identifier of the stage to flush.
            
    :type restApiId: string
    :param stageName: [REQUIRED]
            The name of the stage to flush.
            
    :type stageName: string
    """
    pass


def flush_stage_cache(restApiId=None, stageName=None):
    """
    :param restApiId: [REQUIRED]
            The API identifier of the stage to flush its cache.
            
    :type restApiId: string
    :param stageName: [REQUIRED]
            The name of the stage to flush its cache.
            
    :type stageName: string
    """
    pass


def generate_client_certificate(description=None):
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
            (dict) --Represents a client certificate used to configure client-side SSL authentication while sending requests to the integration endpoint.
            Client certificates are used authenticate an API by the back-end server. To authenticate an API client (or user), use a custom Authorizer . Use Client-Side Certificate
            clientCertificateId (string) --The identifier of the client certificate.
            description (string) --The description of the client certificate.
            pemEncodedCertificate (string) --The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .
            createdDate (datetime) --The date when the client certificate was created, in ISO 8601 format .
            expirationDate (datetime) --The date when the client certificate will expire, in ISO 8601 format .
            
            
    :type description: string
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


def get_account():
    """
    """
    pass


def get_api_key(apiKey=None, includeValue=None):
    """
    :param apiKey: [REQUIRED]
            The identifier of the ApiKey resource.
            
    :type apiKey: string
    :param includeValue: A boolean flag to specify whether (true ) or not (false ) the result contains the key value.
    :type includeValue: boolean
    """
    pass


def get_api_keys(position=None, limit=None, nameQuery=None, includeValues=None):
    """
    :param position: The position of the current ApiKeys resource to get information about.
    :type position: string
    :param limit: The maximum number of ApiKeys to get information about.
    :type limit: integer
    :param nameQuery: The name of queried API keys.
    :type nameQuery: string
    :param includeValues: A boolean flag to specify whether (true ) or not (false ) the result contains key values.
    :type includeValues: boolean
    """
    pass


def get_authorizer(restApiId=None, authorizerId=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Authorizer resource.
            
    :type restApiId: string
    :param authorizerId: [REQUIRED]
            The identifier of the Authorizer resource.
            
    :type authorizerId: string
    """
    pass


def get_authorizers(restApiId=None, position=None, limit=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Authorizers resource.
            
    :type restApiId: string
    :param position: If not all Authorizer resources in the response were present, the position will specify where to start the next page of results.
    :type position: string
    :param limit: Limit the number of Authorizer resources in the response.
    :type limit: integer
    """
    pass


def get_base_path_mapping(domainName=None, basePath=None):
    """
    :param domainName: [REQUIRED]
            The domain name of the BasePathMapping resource to be described.
            
    :type domainName: string
    :param basePath: [REQUIRED]
            The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Leave this blank if you do not want callers to specify any base path name after the domain name.
            
    :type basePath: string
    """
    pass


def get_base_path_mappings(domainName=None, position=None, limit=None):
    """
    :param domainName: [REQUIRED]
            The domain name of a BasePathMapping resource.
            
    :type domainName: string
    :param position: The position of the current BasePathMapping resource in the collection to get information about.
    :type position: string
    :param limit: The maximum number of BasePathMapping resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
    :type limit: integer
    """
    pass


def get_client_certificate(clientCertificateId=None):
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
            (dict) --Represents a client certificate used to configure client-side SSL authentication while sending requests to the integration endpoint.
            Client certificates are used authenticate an API by the back-end server. To authenticate an API client (or user), use a custom Authorizer . Use Client-Side Certificate
            clientCertificateId (string) --The identifier of the client certificate.
            description (string) --The description of the client certificate.
            pemEncodedCertificate (string) --The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint .
            createdDate (datetime) --The date when the client certificate was created, in ISO 8601 format .
            expirationDate (datetime) --The date when the client certificate will expire, in ISO 8601 format .
            
            
    :type clientCertificateId: string
    """
    pass


def get_client_certificates(position=None, limit=None):
    """
    :param position: The position of the current ClientCertificate resource in the collection to get information about.
    :type position: string
    :param limit: The maximum number of ClientCertificate resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
    :type limit: integer
    """
    pass


def get_deployment(restApiId=None, deploymentId=None):
    """
    :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Deployment resource to get information about.
            
    :type restApiId: string
    :param deploymentId: [REQUIRED]
            The identifier of the Deployment resource to get information about.
            
    :type deploymentId: string
    """
    pass


def get_deployments(restApiId=None, position=None, limit=None):
    """
    :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the collection of Deployment resources to get information about.
            
    :type restApiId: string
    :param position: The position of the current Deployment resource in the collection to get information about.
    :type position: string
    :param limit: The maximum number of Deployment resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
    :type limit: integer
    """
    pass


def get_domain_name(domainName=None):
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
            Use Client-Side Certificate
            domainName (string) --The name of the DomainName resource.
            certificateName (string) --The name of the certificate.
            certificateUploadDate (datetime) --The date when the certificate was uploaded, in ISO 8601 format .
            distributionDomainName (string) --The domain name of the Amazon CloudFront distribution. For more information, see the Amazon CloudFront documentation .
            
            
    :type domainName: string
    """
    pass


def get_domain_names(position=None, limit=None):
    """
    :param position: The position of the current domain names to get information about.
    :type position: string
    :param limit: The maximum number of DomainName resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
    :type limit: integer
    """
    pass


def get_export(restApiId=None, stageName=None, exportType=None, parameters=None, accepts=None):
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
    :param parameters: A key-value map of query string parameters that specify properties of the export, depending on the requested exportType . For exportType swagger , any combination of the following parameters are supported: integrations will export the API with x-amazon-apigateway-integration extensions. authorizers will export the API with x-amazon-apigateway-authorizer extensions. postman will export the API with Postman extensions, allowing for import to the Postman tool
            (string) --
            (string) --
            
    :type parameters: dict
    :param accepts: The content-type of the export, for example application/json . Currently application/json and application/yaml are supported for exportType of swagger . This should be specified in the Accept header for direct API requests.
    :type accepts: string
    """
    pass


def get_integration(restApiId=None, resourceId=None, httpMethod=None):
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
    pass


def get_integration_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
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
    pass


def get_method(restApiId=None, resourceId=None, httpMethod=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Method resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            
    :type resourceId: string
    :param httpMethod: [REQUIRED]
            Specifies the method request's HTTP method type.
            
    :type httpMethod: string
    """
    pass


def get_method_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the MethodResponse resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the MethodResponse resource.
            
    :type resourceId: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            
    :type httpMethod: string
    :param statusCode: [REQUIRED]
            The status code for the MethodResponse resource.
            
    :type statusCode: string
    """
    pass


def get_model(restApiId=None, modelName=None, flatten=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier under which the Model exists.
            
    :type restApiId: string
    :param modelName: [REQUIRED]
            The name of the model as an identifier.
            
    :type modelName: string
    :param flatten: A query parameter of a Boolean value to resolve (true ) all external model references and returns a flattened model schema or not (false ) The default is false .
    :type flatten: boolean
    """
    pass


def get_model_template(restApiId=None, modelName=None):
    """
    :param restApiId: [REQUIRED]
            The ID of the RestApi under which the model exists.
            
    :type restApiId: string
    :param modelName: [REQUIRED]
            The name of the model for which to generate a template.
            
    :type modelName: string
    """
    pass


def get_models(restApiId=None, position=None, limit=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier.
            
    :type restApiId: string
    :param position: The position of the next set of results in the Models resource to get information about.
    :type position: string
    :param limit: The maximum number of models in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
    :type limit: integer
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


def get_resource(restApiId=None, resourceId=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The identifier for the Resource resource.
            
    :type resourceId: string
    """
    pass


def get_resources(restApiId=None, position=None, limit=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Resource.
            
    :type restApiId: string
    :param position: The position of the next set of results in the current Resources resource to get information about.
    :type position: string
    :param limit: The maximum number of Resource resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
    :type limit: integer
    """
    pass


def get_rest_api(restApiId=None):
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
            Create an API
            id (string) --The API's identifier. This identifier is unique across all of your APIs in Amazon API Gateway.
            name (string) --The API's name.
            description (string) --The API's description.
            createdDate (datetime) --The date when the API was created, in ISO 8601 format .
            warnings (list) --The warning messages reported when failonwarnings is turned on during API import.
            (string) --
            
            
    :type restApiId: string
    """
    pass


def get_rest_apis(position=None, limit=None):
    """
    :param position: The position of the current RestApis resource in the collection to get information about.
    :type position: string
    :param limit: The maximum number of RestApi resources in the collection to get information about. The default limit is 25. It should be an integer between 1 - 500.
    :type limit: integer
    """
    pass


def get_sdk(restApiId=None, stageName=None, sdkType=None, parameters=None):
    """
    :param restApiId: [REQUIRED]
            The identifier of the RestApi that the SDK will use.
            
    :type restApiId: string
    :param stageName: [REQUIRED]
            The name of the Stage that the SDK will use.
            
    :type stageName: string
    :param sdkType: [REQUIRED]
            The language for the generated SDK. Currently javascript , android , and objectivec (for iOS) are supported.
            
    :type sdkType: string
    :param parameters: A key-value map of query string parameters that specify properties of the SDK, depending on the requested sdkType . For sdkType of objectivec , a parameter named classPrefix is required. For sdkType of android , parameters named groupId , artifactId , artifactVersion , and invokerPackage are required.
            (string) --
            (string) --
            
    :type parameters: dict
    """
    pass


def get_stage(restApiId=None, stageName=None):
    """
    :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Stage resource to get information about.
            
    :type restApiId: string
    :param stageName: [REQUIRED]
            The name of the Stage resource to get information about.
            
    :type stageName: string
    """
    pass


def get_stages(restApiId=None, deploymentId=None):
    """
    :param restApiId: [REQUIRED]
            The stages' API identifiers.
            
    :type restApiId: string
    :param deploymentId: The stages' deployment identifiers.
    :type deploymentId: string
    """
    pass


def get_usage(usagePlanId=None, keyId=None, startDate=None, endDate=None, position=None, limit=None):
    """
    :param usagePlanId: [REQUIRED]
            The Id of the usage plan associated with the usage data.
            
    :type usagePlanId: string
    :param keyId: The Id of the API key associated with the resultant usage data.
    :type keyId: string
    :param startDate: [REQUIRED]
            The starting date (e.g., 2016-01-01) of the usage data.
            
    :type startDate: string
    :param endDate: [REQUIRED]
            The ending date (e.g., 2016-12-31) of the usage data.
            
    :type endDate: string
    :param position: Position
    :type position: string
    :param limit: The maximum number of results to be returned.
    :type limit: integer
    """
    pass


def get_usage_plan(usagePlanId=None):
    """
    :param usagePlanId: [REQUIRED]
            The identifier of the UsagePlan resource to be retrieved.
            Return typedict
            ReturnsResponse Syntax{
              'id': 'string',
              'name': 'string',
              'description': 'string',
              'apiStages': [
                {
                  'apiId': 'string',
                  'stage': 'string'
                },
              ],
              'throttle': {
                'burstLimit': 123,
                'rateLimit': 123.0
              },
              'quota': {
                'limit': 123,
                'offset': 123,
                'period': 'DAY'|'WEEK'|'MONTH'
              }
            }
            Response Structure
            (dict) --Represents a usage plan than can specify who can assess associated API stages with specified request limits and quotas.
            In a usage plan, you associate an API by specifying the API's Id and a stage name of the specified API. You add plan customers by adding API keys to the plan.
            Create and Use Usage Plans
            id (string) --The identifier of a UsagePlan resource.
            name (string) --The name of a usage plan.
            description (string) --The description of a usage plan.
            apiStages (list) --The associated API stages of a usage plan.
            (dict) --API stage name of the associated API stage in a usage plan.
            apiId (string) --API Id of the associated API stage in a usage plan.
            stage (string) --API stage name of the associated API stage in a usage plan.
            
            throttle (dict) --The request throttle limits of a usage plan.
            burstLimit (integer) --The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
            rateLimit (float) --The API request steady-state rate limit.
            quota (dict) --The maximum number of permitted requests per a given unit time interval.
            limit (integer) --The maximum number of requests that can be made in a given time period.
            offset (integer) --The number of requests subtracted from the given limit in the initial time period.
            period (string) --The time period in which the limit applies. Valid values are 'DAY', 'WEEK' or 'MONTH'.
            
            
            
    :type usagePlanId: string
    """
    pass


def get_usage_plan_key(usagePlanId=None, keyId=None):
    """
    :param usagePlanId: [REQUIRED]
            The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
            
    :type usagePlanId: string
    :param keyId: [REQUIRED]
            The key Id of the to-be-retrieved UsagePlanKey resource representing a plan customer.
            
    :type keyId: string
    """
    pass


def get_usage_plan_keys(usagePlanId=None, position=None, limit=None, nameQuery=None):
    """
    :param usagePlanId: [REQUIRED]
            The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer.
            
    :type usagePlanId: string
    :param position: A query parameter specifying the zero-based index specifying the position of a usage plan key.
    :type position: string
    :param limit: A query parameter specifying the maximum number usage plan keys returned by the GET request.
    :type limit: integer
    :param nameQuery: A query parameter specifying the name of the to-be-returned usage plan keys.
    :type nameQuery: string
    """
    pass


def get_usage_plans(position=None, keyId=None, limit=None):
    """
    :param position: The zero-based array index specifying the position of the to-be-retrieved UsagePlan resource.
    :type position: string
    :param keyId: The identifier of the API key associated with the usage plans.
    :type keyId: string
    :param limit: The number of UsagePlan resources to be returned as the result.
    :type limit: integer
    """
    pass


def get_waiter():
    """
    """
    pass


def import_api_keys(body=None, format=None, failOnWarnings=None):
    """
    :param body: [REQUIRED]
            The payload of the POST request to import API keys. For the payload format, see API Key File Format .
            
    :type body: bytes or seekable file-like object
    :param format: [REQUIRED]
            A query parameter to specify the input format to imported API keys. Currently, only the csv format is supported.
            
    :type format: string
    :param failOnWarnings: A query parameter to indicate whether to rollback ApiKey importation (true ) or not (false ) when error is encountered.
    :type failOnWarnings: boolean
    """
    pass


def import_rest_api(failOnWarnings=None, parameters=None, body=None):
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
    pass


def put_integration(restApiId=None, resourceId=None, httpMethod=None, type=None, integrationHttpMethod=None, uri=None,
                    credentials=None, requestParameters=None, requestTemplates=None, passthroughBehavior=None,
                    cacheNamespace=None, cacheKeyParameters=None):
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
    :param requestParameters: A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the back end. The method request parameter value must match the pattern of method.request.{location}.{name} , where location is querystring , path , or header and name must be a valid and unique method request parameter name.
            (string) --
            (string) --
            
    :type requestParameters: dict
    :param requestTemplates: Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value.
            (string) --
            (string) --
            
    :type requestTemplates: dict
    :param passthroughBehavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH , WHEN_NO_TEMPLATES , and NEVER .
            WHEN_NO_MATCH passes the request body for unmapped content types through to the integration back end without transformation.
            NEVER rejects unmapped content types with an HTTP 415 'Unsupported Media Type' response.
            WHEN_NO_TEMPLATES allows pass-through when the integration has NO content types mapped to templates. However if there is at least one content type defined, unmapped content types will be rejected with the same 415 response.
            
    :type passthroughBehavior: string
    :param cacheNamespace: Specifies a put integration input's cache namespace.
    :type cacheNamespace: string
    :param cacheKeyParameters: Specifies a put integration input's cache key parameters.
            (string) --
            
    :type cacheKeyParameters: list
    """
    pass


def put_integration_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None, selectionPattern=None,
                             responseParameters=None, responseTemplates=None):
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
    :param responseParameters: A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name} , where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression} , where name must be a valid and unique response header name and JSON-expression a valid JSON expression without the $ prefix.
            (string) --
            (string) --
            
    :type responseParameters: dict
    :param responseTemplates: Specifies a put integration response's templates.
            (string) --
            (string) --
            
    :type responseTemplates: dict
    """
    pass


def put_method(restApiId=None, resourceId=None, httpMethod=None, authorizationType=None, authorizerId=None,
               apiKeyRequired=None, requestParameters=None, requestModels=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the new Method resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the new Method resource.
            
    :type resourceId: string
    :param httpMethod: [REQUIRED]
            Specifies the method request's HTTP method type.
            
    :type httpMethod: string
    :param authorizationType: [REQUIRED]
            Specifies the type of authorization used for the method.
            
    :type authorizationType: string
    :param authorizerId: Specifies the identifier of an Authorizer to use on this Method, if the type is CUSTOM.
    :type authorizerId: string
    :param apiKeyRequired: Specifies whether the method required a valid ApiKey .
    :type apiKeyRequired: boolean
    :param requestParameters: A key-value map defining required or optional method request parameters that can be accepted by Amazon API Gateway. A key defines a method request parameter name matching the pattern of method.request.{location}.{name} , where location is querystring , path , or header and name is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (true ) or optional (false ). The method request parameter names defined here are available in Integration to be mapped to integration request parameters or body-mapping templates.
            (string) --
            (boolean) --
            
    :type requestParameters: dict
    :param requestModels: Specifies the Model resources used for the request's content type. Request models are represented as a key/value map, with a content type as the key and a Model name as the value.
            (string) --
            (string) --
            
    :type requestModels: dict
    """
    pass


def put_method_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None, responseParameters=None,
                        responseModels=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Method resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            
    :type resourceId: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            
    :type httpMethod: string
    :param statusCode: [REQUIRED]
            The method response's status code.
            
    :type statusCode: string
    :param responseParameters: A key-value map specifying required or optional response parameters that Amazon API Gateway can send back to the caller. A key defines a method response header name and the associated value is a Boolean flag indicating whether the method response parameter is required or not. The method response header names must match the pattern of method.response.header.{name} , where name is a valid and unique header name. The response parameter names defined here are available in the integration response to be mapped from an integration response header expressed in integration.response.header.{name} , a static value enclosed within a pair of single quotes (e.g., 'application/json' ), or a JSON expression from the back-end response payload in the form of integration.response.body.{JSON-expression} , where JSON-expression is a valid JSON expression without the $ prefix.)
            (string) --
            (boolean) --
            
    :type responseParameters: dict
    :param responseModels: Specifies the Model resources used for the response's content type. Response models are represented as a key/value map, with a content type as the key and a Model name as the value.
            (string) --
            (string) --
            
    :type responseModels: dict
    """
    pass


def put_rest_api(restApiId=None, mode=None, failOnWarnings=None, parameters=None, body=None):
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
    pass


def test_invoke_authorizer(restApiId=None, authorizerId=None, headers=None, pathWithQueryString=None, body=None,
                           stageVariables=None, additionalContext=None):
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
    pass


def test_invoke_method(restApiId=None, resourceId=None, httpMethod=None, pathWithQueryString=None, body=None,
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
    :param clientCertificateId: A ClientCertificate identifier to use in the test invocation. API Gateway will use the certificate when making the HTTPS request to the defined back-end endpoint.
    :type clientCertificateId: string
    :param stageVariables: A key-value map of stage variables to simulate an invocation on a deployed Stage .
            (string) --
            (string) --
            
    :type stageVariables: dict
    """
    pass


def update_account(patchOperations=None):
    """
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            Return typedict
            ReturnsResponse Syntax{
              'cloudwatchRoleArn': 'string',
              'throttleSettings': {
                'burstLimit': 123,
                'rateLimit': 123.0
              },
              'features': [
                'string',
              ],
              'apiKeyVersion': 'string'
            }
            Response Structure
            (dict) --Represents an AWS account that is associated with Amazon API Gateway.
            To view the account info, call GET on this resource.
            Error Codes
            The following exception may be thrown when the request fails.
            UnauthorizedException
            NotFoundException
            TooManyRequestsException
            For detailed error code information, including the corresponding HTTP Status Codes, see API Gateway Error Codes
            Example: Get the information about an account. Request GET /account HTTP/1.1 Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160531T184618Z Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash} Response
            The successful response returns a 200 OK status code and a payload similar to the following:
            { '_links': { 'curies': { 'href': 'http://docs.aws.amazon.com/apigateway/latest/developerguide/account-apigateway-{rel}.html', 'name': 'account', 'templated': true }, 'self': { 'href': '/account' }, 'account:update': { 'href': '/account' } }, 'cloudwatchRoleArn': 'arn:aws:iam::123456789012:role/apigAwsProxyRole', 'throttleSettings': { 'rateLimit': 500, 'burstLimit': 1000 } }
            In addition to making the REST API call directly, you can use the AWS CLI and an AWS SDK to access this resource.
            API Gateway Limits Developer Guide , AWS CLI
            cloudwatchRoleArn (string) --The ARN of an Amazon CloudWatch role for the current Account .
            throttleSettings (dict) --Specifies the API request limits configured for the current Account .
            burstLimit (integer) --The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
            rateLimit (float) --The API request steady-state rate limit.
            features (list) --A list of features supported for the account. When usage plans are enabled, the features list will include an entry of 'UsagePlans' .
            (string) --
            apiKeyVersion (string) --The version of the API keys used for the account.
            
            
    :type patchOperations: list
    """
    pass


def update_api_key(apiKey=None, patchOperations=None):
    """
    :param apiKey: [REQUIRED]
            The identifier of the ApiKey resource to be updated.
            
    :type apiKey: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_authorizer(restApiId=None, authorizerId=None, patchOperations=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Authorizer resource.
            
    :type restApiId: string
    :param authorizerId: [REQUIRED]
            The identifier of the Authorizer resource.
            
    :type authorizerId: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_base_path_mapping(domainName=None, basePath=None, patchOperations=None):
    """
    :param domainName: [REQUIRED]
            The domain name of the BasePathMapping resource to change.
            
    :type domainName: string
    :param basePath: [REQUIRED]
            The base path of the BasePathMapping resource to change.
            
    :type basePath: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_client_certificate(clientCertificateId=None, patchOperations=None):
    """
    :param clientCertificateId: [REQUIRED]
            The identifier of the ClientCertificate resource to be updated.
            
    :type clientCertificateId: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_deployment(restApiId=None, deploymentId=None, patchOperations=None):
    """
    :param restApiId: [REQUIRED]
            The replacement identifier of the RestApi resource for the Deployment resource to change information about.
            
    :type restApiId: string
    :param deploymentId: [REQUIRED]
            The replacement identifier for the Deployment resource to change information about.
            
    :type deploymentId: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_domain_name(domainName=None, patchOperations=None):
    """
    :param domainName: [REQUIRED]
            The name of the DomainName resource to be changed.
            
    :type domainName: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_integration(restApiId=None, resourceId=None, httpMethod=None, patchOperations=None):
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
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_integration_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None,
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
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_method(restApiId=None, resourceId=None, httpMethod=None, patchOperations=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Method resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the Method resource.
            
    :type resourceId: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            
    :type httpMethod: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_method_response(restApiId=None, resourceId=None, httpMethod=None, statusCode=None, patchOperations=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the MethodResponse resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The Resource identifier for the MethodResponse resource.
            
    :type resourceId: string
    :param httpMethod: [REQUIRED]
            The HTTP verb of the Method resource.
            
    :type httpMethod: string
    :param statusCode: [REQUIRED]
            The status code for the MethodResponse resource.
            
    :type statusCode: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_model(restApiId=None, modelName=None, patchOperations=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier under which the model exists.
            
    :type restApiId: string
    :param modelName: [REQUIRED]
            The name of the model to update.
            
    :type modelName: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_resource(restApiId=None, resourceId=None, patchOperations=None):
    """
    :param restApiId: [REQUIRED]
            The RestApi identifier for the Resource resource.
            
    :type restApiId: string
    :param resourceId: [REQUIRED]
            The identifier of the Resource resource.
            
    :type resourceId: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_rest_api(restApiId=None, patchOperations=None):
    """
    :param restApiId: [REQUIRED]
            The ID of the RestApi you want to update.
            
    :type restApiId: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_stage(restApiId=None, stageName=None, patchOperations=None):
    """
    :param restApiId: [REQUIRED]
            The identifier of the RestApi resource for the Stage resource to change information about.
            
    :type restApiId: string
    :param stageName: [REQUIRED]
            The name of the Stage resource to change information about.
            
    :type stageName: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_usage(usagePlanId=None, keyId=None, patchOperations=None):
    """
    :param usagePlanId: [REQUIRED]
            The Id of the usage plan associated with the usage data.
            
    :type usagePlanId: string
    :param keyId: [REQUIRED]
            The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota.
            
    :type keyId: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass


def update_usage_plan(usagePlanId=None, patchOperations=None):
    """
    :param usagePlanId: [REQUIRED]
            The Id of the to-be-updated usage plan.
            
    :type usagePlanId: string
    :param patchOperations: A list of update operations to be applied to the specified resource and in the order specified in this list.
            (dict) -- A single patch operation to apply to the specified resource. Please refer to http://tools.ietf.org/html/rfc6902#section-4 for an explanation of how each operation is used.
            op (string) --An update operation to be performed with this PATCH request. The valid value can be 'add', 'remove', or 'replace'. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message.
            path (string) --The op operation's target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {'name':'value'} , the path for this property is /name . If the name property value is a JSON object (e.g., {'name': {'child/name': 'child-value'}} ), the path for the child/name property will be /name/child~1name . Any slash ('/') character appearing in path names must be escaped with '~1', as shown in the example above. Each op operation can have only one path associated with it.
            value (string) --The new target value of the update operation.
            from (string) --Not supported.
            
            
    :type patchOperations: list
    """
    pass
