import os

from bs4 import BeautifulSoup
import requests

from pyboto3 import boto3_interface_generator

from pyboto3.boto3_interface_generator import iter_params, iter_methods, get_method_description, get_param_description, \
    iter_code_lines, generate_all_services_code, iter_all_services, generate_service_code


def test_iter_methods_api_gateway():
    response = requests.get('https://boto3.readthedocs.io/en/latest/reference/services/apigateway.html')
    soup = BeautifulSoup(response._content, 'html.parser')
    methods = {'can_paginate', 'create_api_key', 'create_authorizer', 'create_base_path_mapping', 'create_deployment',
               'create_domain_name', 'create_model', 'create_resource', 'create_rest_api', 'create_stage',
               'delete_api_key', 'delete_authorizer', 'delete_base_path_mapping', 'delete_client_certificate',
               'delete_deployment', 'delete_domain_name', 'delete_integration', 'delete_integration_response',
               'delete_method', 'delete_method_response', 'delete_model', 'delete_resource', 'delete_rest_api',
               'delete_stage', 'flush_stage_authorizers_cache', 'flush_stage_cache', 'generate_client_certificate',
               'generate_presigned_url', 'get_account', 'get_api_key', 'get_api_keys', 'get_authorizer',
               'get_authorizers', 'get_base_path_mapping', 'get_base_path_mappings', 'get_client_certificate',
               'get_client_certificates', 'get_deployment', 'get_deployments', 'get_domain_name', 'get_domain_names',
               'get_export', 'get_integration', 'get_integration_response', 'get_method', 'get_method_response',
               'get_model', 'get_model_template', 'get_models', 'get_paginator', 'get_resource', 'get_resources',
               'get_rest_api', 'get_rest_apis', 'get_sdk', 'get_stage', 'get_stages', 'get_waiter', 'import_rest_api',
               'put_integration', 'put_integration_response', 'put_method', 'put_method_response', 'put_rest_api',
               'test_invoke_authorizer', 'test_invoke_method', 'update_account', 'update_api_key', 'update_authorizer',
               'update_base_path_mapping', 'update_client_certificate', 'update_deployment', 'update_domain_name',
               'update_integration', 'update_integration_response', 'update_method', 'update_method_response',
               'update_model', 'update_resource', 'update_rest_api', 'update_stage'}
    method_soup_dict = {name: html for name, html in iter_methods(soup.find(id='client'))}
    assert methods == set([str(x) for x in method_soup_dict.keys()])

    can_paginate_params = [('operation_name', 'string')]
    assert can_paginate_params == list(
        (name, type) for name, type, desc in iter_params(method_soup_dict['can_paginate']))
    create_api_key_params = [('name', 'string', 'The name of the ApiKey .'),
                             ('description', 'string', 'The description of the ApiKey .'),
                             ('enabled', 'boolean', 'Specifies whether the ApiKey can be used by callers.'),
                             ('stageKeys', 'list', 'Specifies whether the ApiKey can be used by callers.'
                                                   '\n(dict) --A reference to a unique stage identified in the format {restApiId}/{stage} .'
                                                   '\nrestApiId (string) --A list of Stage resources that are associated with the ApiKey resource.'
                                                   '\nstageName (string) --The stage name in the RestApi that the stage key references.\n\n\n')]
    assert create_api_key_params == list(
        (str(name), str(type), str(desc)) for name, type, desc in iter_params(method_soup_dict['create_api_key']))
    assert [('restApiId', 'string'), ('resourceId', 'string')] == list(
        (name, type) for name, type, desc in iter_params(method_soup_dict['get_resource']))

    for method, html in method_soup_dict.iteritems():
        param_dict = {param: type for param, type, description in iter_params(html)}
        print method, param_dict.keys()


def test_description():
    response = requests.get('https://boto3.readthedocs.io/en/latest/reference/services/apigateway.html')
    soup = BeautifulSoup(response._content, 'html.parser')
    method_soup_dict = {name: html for name, html in iter_methods(soup.find(id='client'))}
    can_paginate_description = 'Check if an operation can be paginated.'
    assert can_paginate_description == get_method_description(method_soup_dict.get('can_paginate'))


def test_signle_param_description():
    soup = BeautifulSoup(
        """<dd class="field-body"><strong>operation_name</strong> (<em>string</em>) -- The operation name.  This is the same name as the method name on the client.  For example, if the method name is <tt class="docutils literal"><span class="pre">create_foo</span></tt>, and you'd normally invoke the operation as <tt class="docutils literal"><span class="pre">client.create_foo(**kwargs)</span></tt>, if the <tt class="docutils literal"><span class="pre">create_foo</span></tt> operation can be paginated, you can use the call <tt class="docutils literal"><span class="pre">client.get_paginator("create_foo")</span></tt>.</dd>""",
        'html.parser')
    result = get_param_description(soup)
    print result
    assert result == """The operation name. This is the same name as the method name on the client. For example, if the method name is create_foo, and you'd normally invoke the operation as client.create_foo(**kwargs), if the create_foo operation can be paginated, you can use the call client.get_paginator("create_foo")."""


def test_multiple_param_description():
    soup = BeautifulSoup(
        """<dd class="field-body"><ul class="first simple"> <li><strong>restApiId</strong> (<em>string</em>) -- <p><strong>[REQUIRED]</strong></p> <p>The RestApi identifier under which the Authorizer will be created.</p> </li> <li><strong>name</strong> (<em>string</em>) -- <p><strong>[REQUIRED]</strong></p> <p>[Required] The name of the authorizer.</p> </li> <li><strong>type</strong> (<em>string</em>) -- <p><strong>[REQUIRED]</strong></p> <p>[Required] The type of the authorizer.</p> </li> <li><strong>authType</strong> (<em>string</em>) -- Optional customer-defined field, used in Swagger imports/exports. Has no functional impact.</li> <li><strong>authorizerUri</strong> (<em>string</em>) -- <p><strong>[REQUIRED]</strong></p> <p>[Required] Specifies the authorizer's Uniform Resource Identifier (URI).</p> </li> <li><strong>authorizerCredentials</strong> (<em>string</em>) -- Specifies the credentials required for the authorizer, if any.</li> <li><strong>identitySource</strong> (<em>string</em>) -- <p><strong>[REQUIRED]</strong></p> <p>[Required] The source of the identity in an incoming request.</p> </li> <li><strong>identityValidationExpression</strong> (<em>string</em>) -- A validation expression for the incoming identity.</li> <li><strong>authorizerResultTtlInSeconds</strong> (<em>integer</em>) -- The TTL of cached authorizer results.</li> </ul> </dd>""")
    result = get_param_description(soup)


def test_cloudformation():
    response = requests.get('https://boto3.readthedocs.io/en/latest/reference/services/cloudformation.html')
    soup = BeautifulSoup(response._content, 'html.parser')
    method_soup_dict = {name: html for name, html in iter_methods(soup.find(id='client'))}
    get_template_params = [('StackName', 'string')]
    assert get_template_params == list(
        (name, type) for name, type, desc in iter_params(method_soup_dict['get_template']))


def test_iter_methods_s3():
    response = requests.get('https://boto3.readthedocs.io/en/latest/reference/services/s3.html')
    soup = BeautifulSoup(response._content, 'html.parser')
    s3_methods = {'abort_multipart_upload', 'can_paginate', 'complete_multipart_upload', 'copy_object', 'create_bucket',
                  'create_multipart_upload', 'delete_bucket', 'delete_bucket_cors', 'delete_bucket_lifecycle',
                  'delete_bucket_policy', 'delete_bucket_replication', 'delete_bucket_tagging', 'delete_bucket_website',
                  'delete_object', 'delete_objects', 'download_file', 'generate_presigned_post',
                  'generate_presigned_url', 'get_bucket_accelerate_configuration', 'get_bucket_acl', 'get_bucket_cors',
                  'get_bucket_lifecycle', 'get_bucket_lifecycle_configuration', 'get_bucket_location',
                  'get_bucket_logging', 'get_bucket_notification', 'get_bucket_notification_configuration',
                  'get_bucket_policy', 'get_bucket_replication', 'get_bucket_request_payment', 'get_bucket_tagging',
                  'get_bucket_versioning', 'get_bucket_website', 'get_object', 'get_object_acl', 'get_object_torrent',
                  'get_paginator', 'get_waiter', 'head_bucket', 'head_object', 'list_buckets', 'list_multipart_uploads',
                  'list_object_versions', 'list_objects', 'list_objects_v2', 'list_parts',
                  'put_bucket_accelerate_configuration', 'put_bucket_acl', 'put_bucket_cors', 'put_bucket_lifecycle',
                  'put_bucket_lifecycle_configuration', 'put_bucket_logging', 'put_bucket_notification',
                  'put_bucket_notification_configuration', 'put_bucket_policy', 'put_bucket_replication',
                  'put_bucket_request_payment', 'put_bucket_tagging', 'put_bucket_versioning', 'put_bucket_website',
                  'put_object', 'put_object_acl', 'restore_object', 'upload_file', 'upload_part', 'upload_part_copy'}
    method_soup_dict = {name: html for name, html in iter_methods(soup.find(id='client'))}
    assert s3_methods == set([str(x) for x in method_soup_dict.keys()])
    abort_multipart_upload_params = [('Bucket', 'string'),
                                     ('Key', 'string'),
                                     ('UploadId', 'string'),
                                     ('RequestPayer', 'string')]
    assert abort_multipart_upload_params == list(
        (name, type) for name, type, desc in iter_params(method_soup_dict['abort_multipart_upload']))
    for method, html in method_soup_dict.iteritems():
        param_dict = {param: type for param, type, description in iter_params(html)}
        # print method, param_dict.keys()

    for line in iter_code_lines(soup):
        print line


def test_generate_code():
    generate_all_services_code(os.path.join(os.path.dirname(__file__), '..', 'pyboto3'))


def test_generate_rds_code():
    generate_service_code('https://boto3.readthedocs.io/en/latest/reference/services/rds.html',
                          os.path.join(os.path.dirname(__file__), '..', 'pyboto3', 'rds.py'))


def test_get_services():
    services = list(iter_all_services())
    print services
    assert ('ACM', 'https://boto3.readthedocs.io/en/latest/reference/services/acm.html') in services
