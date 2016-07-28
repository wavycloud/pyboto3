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

from pyboto3.acm import Acm
from pyboto3.apigateway import Apigateway
from pyboto3.applicationautoscaling import Applicationautoscaling
from pyboto3.autoscaling import Autoscaling
from pyboto3.cloudformation import Cloudformation
from pyboto3.cloudfront import Cloudfront
from pyboto3.cloudhsm import Cloudhsm
from pyboto3.cloudsearch import Cloudsearch
from pyboto3.cloudsearchdomain import Cloudsearchdomain
from pyboto3.cloudtrail import Cloudtrail
from pyboto3.cloudwatch import Cloudwatch
from pyboto3.codecommit import Codecommit
from pyboto3.codedeploy import Codedeploy
from pyboto3.codepipeline import Codepipeline
from pyboto3.cognitoidentity import Cognitoidentity
from pyboto3.cognitoidentityprovider import Cognitoidp
from pyboto3.cognitosync import Cognitosync
from pyboto3.configservice import Config
from pyboto3.datapipeline import Datapipeline
from pyboto3.devicefarm import Devicefarm
from pyboto3.directconnect import Directconnect
from pyboto3.applicationdiscoveryservice import Discovery
from pyboto3.databasemigrationservice import Dms
from pyboto3.directoryservice import Ds
from pyboto3.dynamodb import Dynamodb
from pyboto3.dynamodbstreams import Dynamodbstreams
from pyboto3.ec2 import Ec2
from pyboto3.ecr import Ecr
from pyboto3.ecs import Ecs
from pyboto3.efs import Efs
from pyboto3.elasticache import Elasticache
from pyboto3.elasticbeanstalk import Elasticbeanstalk
from pyboto3.elastictranscoder import Elastictranscoder
from pyboto3.elasticloadbalancing import Elb
from pyboto3.emr import Emr
from pyboto3.elasticsearchservice import Es
from pyboto3.cloudwatchevents import Events
from pyboto3.firehose import Firehose
from pyboto3.gamelift import Gamelift
from pyboto3.glacier import Glacier
from pyboto3.iam import Iam
from pyboto3.importexport import Importexport
from pyboto3.inspector import Inspector
from pyboto3.iot import Iot
from pyboto3.iotdataplane import Iotdata
from pyboto3.kinesis import Kinesis
from pyboto3.kms import Kms
from pyboto3.lambda_ import Lambda
from pyboto3.cloudwatchlogs import Logs
from pyboto3.machinelearning import Machinelearning
from pyboto3.marketplacecommerceanalytics import Marketplacecommerceanalytics
from pyboto3.marketplacemetering import Meteringmarketplace
from pyboto3.opsworks import Opsworks
from pyboto3.rds import Rds
from pyboto3.redshift import Redshift
from pyboto3.route53 import Route53
from pyboto3.route53domains import Route53domains
from pyboto3.s3 import S3
from pyboto3.simpledb import Sdb
from pyboto3.servicecatalog import Servicecatalog
from pyboto3.ses import Ses
from pyboto3.sns import Sns
from pyboto3.sqs import Sqs
from pyboto3.ssm import Ssm
from pyboto3.storagegateway import Storagegateway
from pyboto3.sts import Sts
from pyboto3.support import Support
from pyboto3.swf import Swf
from pyboto3.waf import Waf
from pyboto3.workspaces import Workspaces
