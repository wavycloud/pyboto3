from pyboto3 import interface_generator
import json


def test_get_services_dir():
    assert interface_generator.get_services_dir()

    service_json_path_dict = dict(interface_generator.iter_services_json_paths())
    for service_name, json_path in service_json_path_dict.iteritems():
        print service_name, json_path

    apigateway_methods = {'can_paginate', 'create_api_key', 'create_authorizer', 'create_base_path_mapping',
                          'create_deployment',
                          'create_domain_name', 'create_model', 'create_resource', 'create_rest_api', 'create_stage',
                          'delete_api_key', 'delete_authorizer', 'delete_base_path_mapping',
                          'delete_client_certificate',
                          'delete_deployment', 'delete_domain_name', 'delete_integration',
                          'delete_integration_response',
                          'delete_method', 'delete_method_response', 'delete_model', 'delete_resource',
                          'delete_rest_api',
                          'delete_stage', 'flush_stage_authorizers_cache', 'flush_stage_cache',
                          'generate_client_certificate',
                          'generate_presigned_url', 'get_account', 'get_api_key', 'get_api_keys', 'get_authorizer',
                          'get_authorizers', 'get_base_path_mapping', 'get_base_path_mappings',
                          'get_client_certificate',
                          'get_client_certificates', 'get_deployment', 'get_deployments', 'get_domain_name',
                          'get_domain_names',
                          'get_export', 'get_integration', 'get_integration_response', 'get_method',
                          'get_method_response',
                          'get_model', 'get_model_template', 'get_models', 'get_paginator', 'get_resource',
                          'get_resources',
                          'get_rest_api', 'get_rest_apis', 'get_sdk', 'get_stage', 'get_stages', 'get_waiter',
                          'import_rest_api',
                          'put_integration', 'put_integration_response', 'put_method', 'put_method_response',
                          'put_rest_api',
                          'test_invoke_authorizer', 'test_invoke_method', 'update_account', 'update_api_key',
                          'update_authorizer',
                          'update_base_path_mapping', 'update_client_certificate', 'update_deployment',
                          'update_domain_name',
                          'update_integration', 'update_integration_response', 'update_method',
                          'update_method_response',
                          'update_model', 'update_resource', 'update_rest_api', 'update_stage'}

    apigateway_dict = json.load(open(service_json_path_dict.get('apigateway')))
    assert set(interface_generator.iter_method_names(apigateway_dict)) == apigateway_methods

    s3_methods = {'abort_multipart_upload', 'can_paginate', 'complete_multipart_upload', 'copy_object',
                  'create_bucket',
                  'create_multipart_upload', 'delete_bucket', 'delete_bucket_cors', 'delete_bucket_lifecycle',
                  'delete_bucket_policy', 'delete_bucket_replication', 'delete_bucket_tagging',
                  'delete_bucket_website',
                  'delete_object', 'delete_objects', 'download_file', 'generate_presigned_post',
                  'generate_presigned_url', 'get_bucket_accelerate_configuration', 'get_bucket_acl',
                  'get_bucket_cors',
                  'get_bucket_lifecycle', 'get_bucket_lifecycle_configuration', 'get_bucket_location',
                  'get_bucket_logging', 'get_bucket_notification', 'get_bucket_notification_configuration',
                  'get_bucket_policy', 'get_bucket_replication', 'get_bucket_request_payment', 'get_bucket_tagging',
                  'get_bucket_versioning', 'get_bucket_website', 'get_object', 'get_object_acl',
                  'get_object_torrent',
                  'get_paginator', 'get_waiter', 'head_bucket', 'head_object', 'list_buckets',
                  'list_multipart_uploads',
                  'list_object_versions', 'list_objects', 'list_objects_v2', 'list_parts',
                  'put_bucket_accelerate_configuration', 'put_bucket_acl', 'put_bucket_cors',
                  'put_bucket_lifecycle',
                  'put_bucket_lifecycle_configuration', 'put_bucket_logging', 'put_bucket_notification',
                  'put_bucket_notification_configuration', 'put_bucket_policy', 'put_bucket_replication',
                  'put_bucket_request_payment', 'put_bucket_tagging', 'put_bucket_versioning', 'put_bucket_website',
                  'put_object', 'put_object_acl', 'restore_object', 'upload_file', 'upload_part',
                  'upload_part_copy'}
    s3_dict = json.load(open(service_json_path_dict.get('s3')))
    assert set(interface_generator.iter_method_names(s3_dict)) == s3_methods
